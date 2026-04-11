// Math Wiki VaultViewer --- renders the user's localStorage vault on /Vault.
//
// Phase 2 redesign: vault entries now store the FULL problem content, not
// just IDs. VaultViewer reads them directly and does not fetch any bank.
// Legacy entries from Phase 1 (which only stored {generator_id, problem_id})
// are detected and the user is prompted to clear stale data.

type Difficulty = "easy" | "medium" | "hard"

type ProblemRecord = {
  id: string
  generator_id: string
  topic_slug: string
  difficulty: Difficulty
  statement_latex: string
  answer_latex: string
  hints: string[]
  solution_steps_latex: string[]
  tags: string[]
}

type VaultEntry = ProblemRecord & { added_at?: number }

const VAULT_KEY = "math-wiki-vault"

// --- URL helpers ------------------------------------------------------------

function getMathWikiRoot(): string {
  const match = location.pathname.match(/^(.*?\/Math_Wiki\/)/)
  return match ? match[1] : "/"
}

// --- Vault state ------------------------------------------------------------

function vaultGetRaw(): any[] {
  try {
    const raw = localStorage.getItem(VAULT_KEY)
    if (!raw) return []
    const parsed = JSON.parse(raw)
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

function vaultGet(): VaultEntry[] {
  return vaultGetRaw().filter(
    (e) => typeof e === "object" && e !== null && "statement_latex" in e,
  ) as VaultEntry[]
}

function vaultSet(entries: VaultEntry[]) {
  localStorage.setItem(VAULT_KEY, JSON.stringify(entries))
}

function hasLegacyEntries(): boolean {
  return vaultGetRaw().some(
    (e) =>
      typeof e === "object" && e !== null &&
      !("statement_latex" in e) &&
      "problem_id" in e,
  )
}

// --- KaTeX runtime loading (singleton) --------------------------------------

function ensureKatex(): Promise<any> {
  const w = window as any
  if (w.katex) return Promise.resolve(w.katex)
  if (w.__mathWikiKatexLoad) return w.__mathWikiKatexLoad

  w.__mathWikiKatexLoad = new Promise((resolve, reject) => {
    const existing = document.querySelector<HTMLScriptElement>(
      'script[data-math-wiki-katex="1"]',
    )
    if (existing) {
      existing.addEventListener("load", () => resolve(w.katex))
      existing.addEventListener("error", () => reject(new Error("katex load failed")))
      return
    }
    const script = document.createElement("script")
    script.src = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"
    script.async = true
    script.dataset.mathWikiKatex = "1"
    script.onload = () => resolve(w.katex)
    script.onerror = () => {
      w.__mathWikiKatexLoad = null
      reject(new Error("katex load failed"))
    }
    document.head.appendChild(script)
  })

  return w.__mathWikiKatexLoad
}

function renderKatexIn(root: HTMLElement) {
  const katex = (window as any).katex
  if (!katex || typeof katex.render !== "function") return

  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT)
  const texts: Text[] = []
  let n: Node | null
  while ((n = walker.nextNode())) texts.push(n as Text)

  for (const text of texts) {
    const content = text.textContent ?? ""
    if (!content.includes("$")) continue
    const parts = content.split(/(\$\$[^$]+\$\$|\$[^$\n]+\$)/g)
    if (parts.length <= 1) continue
    const frag = document.createDocumentFragment()
    for (const part of parts) {
      if (part.startsWith("$$") && part.endsWith("$$") && part.length > 4) {
        const div = document.createElement("div")
        div.className = "vv-display-math"
        try {
          katex.render(part.slice(2, -2), div, {
            throwOnError: false,
            displayMode: true,
          })
        } catch {
          div.textContent = part
        }
        frag.appendChild(div)
      } else if (part.startsWith("$") && part.endsWith("$") && part.length > 2) {
        const span = document.createElement("span")
        try {
          katex.render(part.slice(1, -1), span, { throwOnError: false })
        } catch {
          span.textContent = part
        }
        frag.appendChild(span)
      } else if (part) {
        frag.appendChild(document.createTextNode(part))
      }
    }
    text.parentNode?.replaceChild(frag, text)
  }
}

function renderKatexWithRetry(el: HTMLElement) {
  ensureKatex()
    .then(() => renderKatexIn(el))
    .catch((err) => console.warn("[vault-viewer] KaTeX unavailable:", err))
}

// --- jsPDF + html2canvas runtime loading (singletons) ----------------------
//
// Both follow the same pattern as ensureKatex() above: lazy CDN load on first
// call, shared-load promise on window so concurrent callers reuse the fetch,
// dedupe marker on the script tag so a reload of this inline bundle does not
// re-inject. Null out the shared promise on error so a retry can try again.

function ensureJsPdf(): Promise<any> {
  const w = window as any
  if (w.jspdf) return Promise.resolve(w.jspdf)
  if (w.__mathWikiJsPdfLoad) return w.__mathWikiJsPdfLoad

  w.__mathWikiJsPdfLoad = new Promise((resolve, reject) => {
    const existing = document.querySelector<HTMLScriptElement>(
      'script[data-math-wiki-jspdf="1"]',
    )
    if (existing) {
      existing.addEventListener("load", () => resolve(w.jspdf))
      existing.addEventListener("error", () => reject(new Error("jspdf load failed")))
      return
    }
    const script = document.createElement("script")
    script.src = "https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"
    script.async = true
    script.dataset.mathWikiJspdf = "1"
    script.onload = () => resolve(w.jspdf)
    script.onerror = () => {
      w.__mathWikiJsPdfLoad = null
      reject(new Error("jspdf load failed"))
    }
    document.head.appendChild(script)
  })

  return w.__mathWikiJsPdfLoad
}

function ensureHtml2Canvas(): Promise<any> {
  const w = window as any
  if (w.html2canvas) return Promise.resolve(w.html2canvas)
  if (w.__mathWikiHtml2CanvasLoad) return w.__mathWikiHtml2CanvasLoad

  w.__mathWikiHtml2CanvasLoad = new Promise((resolve, reject) => {
    const existing = document.querySelector<HTMLScriptElement>(
      'script[data-math-wiki-html2canvas="1"]',
    )
    if (existing) {
      existing.addEventListener("load", () => resolve(w.html2canvas))
      existing.addEventListener("error", () => reject(new Error("html2canvas load failed")))
      return
    }
    const script = document.createElement("script")
    script.src = "https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"
    script.async = true
    script.dataset.mathWikiHtml2canvas = "1"
    script.onload = () => resolve(w.html2canvas)
    script.onerror = () => {
      w.__mathWikiHtml2CanvasLoad = null
      reject(new Error("html2canvas load failed"))
    }
    document.head.appendChild(script)
  })

  return w.__mathWikiHtml2CanvasLoad
}

// --- PDF export pipeline ---------------------------------------------------
//
// The export flow:
//   1. Build an off-screen, fixed-width DOM container that lists every vault
//      problem (and, on a second pass, every answer row).
//   2. Render KaTeX into the container so $...$ and $$...$$ become proper
//      math glyphs. Wait for web fonts so html2canvas captures real glyphs
//      instead of fallback system font.
//   3. html2canvas the whole container into one tall canvas.
//   4. Slice that canvas vertically into page-height strips and addImage
//      each strip into jsPDF at the correct page offset.
//   5. doc.addPage() is called before the answer-key pass to force the
//      answer key to start on its own fresh page regardless of how many
//      pages the problems consumed.

function buildOffscreenProblemDom(
  problem: VaultEntry,
  indexOneBased: number,
): HTMLElement {
  const wrap = document.createElement("div")
  wrap.className = "vv-pdf-problem"

  const num = document.createElement("div")
  num.className = "vv-pdf-num"
  num.textContent = `${indexOneBased}.`

  const body = document.createElement("div")
  body.className = "vv-pdf-body"

  const stmt = document.createElement("div")
  stmt.className = "vv-pdf-statement"
  // Text node content: the $...$ walker (renderKatexIn) will replace math.
  stmt.textContent = problem.statement_latex
  body.appendChild(stmt)

  const workspace = document.createElement("div")
  workspace.className = "vv-pdf-workspace"
  body.appendChild(workspace)

  wrap.appendChild(num)
  wrap.appendChild(body)
  return wrap
}

function buildOffscreenAnswerDom(
  problem: VaultEntry,
  indexOneBased: number,
): HTMLElement {
  const row = document.createElement("div")
  row.className = "vv-pdf-answer-row"

  const num = document.createElement("span")
  num.className = "vv-pdf-num-inline"
  num.textContent = `${indexOneBased}. `

  const ans = document.createElement("span")
  ans.className = "vv-pdf-answer-text"
  ans.textContent = problem.answer_latex

  row.appendChild(num)
  row.appendChild(ans)
  return row
}

async function renderBlockToCanvas(
  node: HTMLElement,
  widthPx: number,
): Promise<HTMLCanvasElement> {
  const host = document.createElement("div")
  host.className = "vv-pdf-offscreen"
  host.style.width = `${widthPx}px`
  host.appendChild(node)
  document.body.appendChild(host)

  try {
    await ensureKatex()
    renderKatexIn(host)

    // Wait for KaTeX's web fonts so html2canvas captures real glyphs
    // instead of a fallback system font. FontFaceSet.ready is supported in
    // every evergreen browser; guard defensively just in case.
    const fonts = (document as any).fonts
    if (fonts && fonts.ready) {
      try {
        await fonts.ready
      } catch {}
    }

    // One animation-frame yield so layout settles after renderKatexIn has
    // replaced text nodes with DocumentFragments of rendered KaTeX markup.
    await new Promise<void>((resolve) => requestAnimationFrame(() => resolve()))

    const html2canvas = (window as any).html2canvas
    const canvas: HTMLCanvasElement = await html2canvas(host, {
      scale: 2,
      backgroundColor: "#ffffff",
      useCORS: true,
      logging: false,
      windowWidth: widthPx,
    })
    return canvas
  } finally {
    host.remove()
  }
}

function sliceCanvasToPdfPages(
  doc: any,
  srcCanvas: HTMLCanvasElement,
  contentWmm: number,
  contentHmm: number,
  marginMm: number,
): void {
  // Canvas intrinsic width corresponds to contentWmm in paper units; this
  // gives us a consistent px-per-mm factor for slice-height math.
  const pxPerMm = srcCanvas.width / contentWmm
  const pageHeightPx = Math.floor(contentHmm * pxPerMm)
  if (pageHeightPx <= 0) return

  let yOffset = 0
  let firstSlice = true

  while (yOffset < srcCanvas.height) {
    const sliceHeightPx = Math.min(pageHeightPx, srcCanvas.height - yOffset)
    const sliceCanvas = document.createElement("canvas")
    sliceCanvas.width = srcCanvas.width
    sliceCanvas.height = sliceHeightPx

    const ctx = sliceCanvas.getContext("2d")
    if (!ctx) break
    // Solid white background so transparent source pixels do not become
    // black in the final PNG encoding.
    ctx.fillStyle = "#ffffff"
    ctx.fillRect(0, 0, sliceCanvas.width, sliceCanvas.height)
    ctx.drawImage(
      srcCanvas,
      0,
      yOffset,
      srcCanvas.width,
      sliceHeightPx,
      0,
      0,
      srcCanvas.width,
      sliceHeightPx,
    )

    const dataUrl = sliceCanvas.toDataURL("image/png")
    if (!firstSlice) doc.addPage()
    const sliceHeightMm = sliceHeightPx / pxPerMm
    doc.addImage(
      dataUrl,
      "PNG",
      marginMm,
      marginMm,
      contentWmm,
      sliceHeightMm,
      undefined,
      "FAST",
    )

    yOffset += sliceHeightPx
    firstSlice = false
  }
}

async function exportVaultToPdf(vault: VaultEntry[]): Promise<void> {
  // US Letter, portrait, 1 inch margins.
  const PAGE_W_MM = 215.9 // 8.5 in
  const PAGE_H_MM = 279.4 // 11 in
  const MARGIN_MM = 25.4 // 1 in
  const CONTENT_W_MM = PAGE_W_MM - 2 * MARGIN_MM // 165.1 mm
  const CONTENT_H_MM = PAGE_H_MM - 2 * MARGIN_MM // 228.6 mm
  // Off-screen CSS width chosen at 96 dpi so px ratios match CSS inch units.
  const OFFSCREEN_W_PX = Math.round((CONTENT_W_MM * 96) / 25.4) // ~624 px

  await Promise.all([ensureJsPdf(), ensureHtml2Canvas(), ensureKatex()])
  const { jsPDF } = (window as any).jspdf
  const doc = new jsPDF({
    unit: "mm",
    format: "letter",
    orientation: "portrait",
  })

  // --- Problems page(s) ---
  const problemsContainer = document.createElement("div")
  problemsContainer.className = "vv-pdf-page"

  const heading = document.createElement("div")
  heading.className = "vv-pdf-heading"
  heading.textContent = `Math Wiki Worksheet — ${vault.length} problem${
    vault.length !== 1 ? "s" : ""
  }`
  problemsContainer.appendChild(heading)

  vault.forEach((p, i) =>
    problemsContainer.appendChild(buildOffscreenProblemDom(p, i + 1)),
  )

  const problemsCanvas = await renderBlockToCanvas(
    problemsContainer,
    OFFSCREEN_W_PX,
  )
  sliceCanvasToPdfPages(doc, problemsCanvas, CONTENT_W_MM, CONTENT_H_MM, MARGIN_MM)

  // --- Answer key on its own fresh page ---
  doc.addPage()

  const answerContainer = document.createElement("div")
  answerContainer.className = "vv-pdf-page"

  const akHeading = document.createElement("div")
  akHeading.className = "vv-pdf-heading"
  akHeading.textContent = "Answer Key"
  answerContainer.appendChild(akHeading)

  vault.forEach((p, i) =>
    answerContainer.appendChild(buildOffscreenAnswerDom(p, i + 1)),
  )

  const answerCanvas = await renderBlockToCanvas(answerContainer, OFFSCREEN_W_PX)
  sliceCanvasToPdfPages(doc, answerCanvas, CONTENT_W_MM, CONTENT_H_MM, MARGIN_MM)

  const stamp = new Date().toISOString().slice(0, 10)
  doc.save(`math-wiki-worksheet-${stamp}.pdf`)
}

// --- Main rendering ---------------------------------------------------------

function renderVault(mount: HTMLElement) {
  const vault = vaultGet()
  const legacyExists = hasLegacyEntries()
  mount.innerHTML = ""
  mount.classList.add("vv-root")

  if (vault.length === 0) {
    const empty = document.createElement("div")
    empty.className = "vv-empty"
    if (legacyExists) {
      empty.innerHTML = `
        <p><strong>Your vault has legacy entries from before the Phase 2 refactor.</strong></p>
        <p>The storage format changed so the VaultViewer no longer has to fetch the problem bank every time it loads. Please clear your vault and add fresh problems.</p>
        <p><button type="button" class="vv-btn vv-clear-stale">Clear Legacy Vault</button></p>
      `
    } else {
      empty.innerHTML = `
        <p>Your vault is empty.</p>
        <p>Navigate to any topic (for example,
        <a href="${getMathWikiRoot()}topics/geometry/Circles">Circles</a>)
        and use the <strong>Add to Vault</strong> button to start building a
        practice set.</p>
      `
    }
    mount.appendChild(empty)
    const clearBtn = empty.querySelector(".vv-clear-stale")
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        localStorage.removeItem(VAULT_KEY)
        renderVault(mount)
      })
    }
    return
  }

  // Header with counts and actions
  const header = document.createElement("div")
  header.className = "vv-header"

  const countDiv = document.createElement("div")
  countDiv.className = "vv-count"
  const countBold = document.createElement("strong")
  countBold.textContent = String(vault.length)
  countDiv.appendChild(countBold)
  countDiv.appendChild(
    document.createTextNode(` problem${vault.length !== 1 ? "s" : ""} in your vault`),
  )

  const actions = document.createElement("div")
  actions.className = "vv-actions vv-no-print"

  const shuffleBtn = document.createElement("button")
  shuffleBtn.type = "button"
  shuffleBtn.className = "vv-btn vv-shuffle"
  shuffleBtn.textContent = "Shuffle"

  const pdfBtn = document.createElement("button")
  pdfBtn.type = "button"
  pdfBtn.className = "vv-btn vv-pdf"
  pdfBtn.textContent = "Save as PDF"

  const exportBtn = document.createElement("button")
  exportBtn.type = "button"
  exportBtn.className = "vv-btn vv-export"
  exportBtn.textContent = "Export JSON"

  const importBtn = document.createElement("button")
  importBtn.type = "button"
  importBtn.className = "vv-btn vv-import"
  importBtn.textContent = "Import JSON"

  // Hidden file input that "Import JSON" triggers.
  const importInput = document.createElement("input")
  importInput.type = "file"
  importInput.accept = "application/json,.json"
  importInput.style.display = "none"

  const clearBtn = document.createElement("button")
  clearBtn.type = "button"
  clearBtn.className = "vv-btn vv-clear"
  clearBtn.textContent = "Clear Vault"

  actions.appendChild(shuffleBtn)
  actions.appendChild(pdfBtn)
  actions.appendChild(exportBtn)
  actions.appendChild(importBtn)
  actions.appendChild(importInput)
  actions.appendChild(clearBtn)

  header.appendChild(countDiv)
  header.appendChild(actions)
  mount.appendChild(header)

  // Problems list
  const list = document.createElement("ol")
  list.className = "vv-problems"

  vault.forEach((problem, idx) => {
    const li = document.createElement("li")
    li.className = "vv-problem"

    const statement = document.createElement("div")
    statement.className = "vv-statement"
    statement.textContent = problem.statement_latex
    li.appendChild(statement)

    // Workspace area (print-only)
    const workspace = document.createElement("div")
    workspace.className = "vv-workspace"
    li.appendChild(workspace)

    // Controls (hidden in print)
    const controls = document.createElement("div")
    controls.className = "vv-controls vv-no-print"

    if (problem.hints && problem.hints.length > 0) {
      const hintsDetails = document.createElement("details")
      hintsDetails.className = "vv-hints"
      const hintsSummary = document.createElement("summary")
      hintsSummary.textContent = `Hints (${problem.hints.length})`
      hintsDetails.appendChild(hintsSummary)
      const hintsList = document.createElement("ol")
      hintsList.className = "vv-hints-list"
      problem.hints.forEach((h) => {
        const hli = document.createElement("li")
        hli.textContent = h
        hintsList.appendChild(hli)
      })
      hintsDetails.appendChild(hintsList)
      controls.appendChild(hintsDetails)
    }

    const answerDetails = document.createElement("details")
    answerDetails.className = "vv-answer"
    const answerSummary = document.createElement("summary")
    answerSummary.textContent = "Show answer"
    answerDetails.appendChild(answerSummary)
    const answerContent = document.createElement("div")
    answerContent.className = "vv-answer-content"
    answerContent.textContent = problem.answer_latex
    answerDetails.appendChild(answerContent)
    controls.appendChild(answerDetails)

    if (problem.solution_steps_latex && problem.solution_steps_latex.length > 0) {
      const stepsDetails = document.createElement("details")
      stepsDetails.className = "vv-steps"
      const stepsSummary = document.createElement("summary")
      stepsSummary.textContent = "Show solution steps"
      stepsDetails.appendChild(stepsSummary)
      const stepsList = document.createElement("ol")
      stepsList.className = "vv-steps-list"
      problem.solution_steps_latex.forEach((s) => {
        const sli = document.createElement("li")
        sli.textContent = s
        stepsList.appendChild(sli)
      })
      stepsDetails.appendChild(stepsList)
      controls.appendChild(stepsDetails)
    }

    const removeBtn = document.createElement("button")
    removeBtn.type = "button"
    removeBtn.className = "vv-remove"
    removeBtn.textContent = "× Remove"
    removeBtn.addEventListener("click", () => {
      const current = vaultGet()
      const filtered = current.filter((e) => e.id !== problem.id)
      vaultSet(filtered)
      renderVault(mount)
    })
    controls.appendChild(removeBtn)

    li.appendChild(controls)
    list.appendChild(li)
  })

  mount.appendChild(list)

  // Answer key
  const answerKey = document.createElement("details")
  answerKey.className = "vv-answer-key"
  const aks = document.createElement("summary")
  aks.textContent = "Answer Key"
  answerKey.appendChild(aks)
  const akList = document.createElement("ol")
  akList.className = "vv-answer-key-list"
  vault.forEach((problem) => {
    const akli = document.createElement("li")
    akli.textContent = problem.answer_latex
    akList.appendChild(akli)
  })
  answerKey.appendChild(akList)
  mount.appendChild(answerKey)

  // Wire up actions
  shuffleBtn.addEventListener("click", () => {
    const shuffled = vaultGet().slice()
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    vaultSet(shuffled)
    renderVault(mount)
  })

  pdfBtn.addEventListener("click", async () => {
    const originalLabel = pdfBtn.textContent
    pdfBtn.disabled = true
    pdfBtn.textContent = "Generating PDF..."
    try {
      // Open the on-screen answer key so the window.print() fallback path
      // (triggered in the catch branch below) still includes the answers
      // if jsPDF fails to load.
      answerKey.open = true
      await exportVaultToPdf(vaultGet())
    } catch (err) {
      console.warn("[vault-viewer] PDF export failed, falling back to print:", err)
      alert("PDF export failed — falling back to browser print.")
      try {
        window.print()
      } catch {}
    } finally {
      pdfBtn.disabled = false
      pdfBtn.textContent = originalLabel ?? "Save as PDF"
    }
  })

  exportBtn.addEventListener("click", () => {
    const payload = {
      version: "math-wiki-vault-export/1",
      exported_at: new Date().toISOString(),
      problem_count: vault.length,
      problems: vaultGet(),
    }
    const json = JSON.stringify(payload, null, 2)
    const blob = new Blob([json], { type: "application/json" })
    const url = URL.createObjectURL(blob)
    const a = document.createElement("a")
    const stamp = new Date().toISOString().slice(0, 10)
    a.href = url
    a.download = `math-wiki-vault-${stamp}.json`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    // Revoke on the next tick to give the browser time to trigger the download.
    setTimeout(() => URL.revokeObjectURL(url), 0)
  })

  importBtn.addEventListener("click", () => {
    importInput.click()
  })

  importInput.addEventListener("change", () => {
    const file = importInput.files && importInput.files[0]
    if (!file) return
    const reader = new FileReader()
    reader.onload = () => {
      try {
        const text = String(reader.result || "")
        const parsed = JSON.parse(text)
        // Accept either the wrapped envelope or a bare array of problems.
        let incoming: any[] = []
        if (Array.isArray(parsed)) {
          incoming = parsed
        } else if (parsed && Array.isArray(parsed.problems)) {
          incoming = parsed.problems
        } else {
          throw new Error("expected an array or {problems: []} envelope")
        }
        // Validate each incoming entry has the minimum fields we need.
        const valid = incoming.filter(
          (e: any) =>
            typeof e === "object" &&
            e !== null &&
            typeof e.id === "string" &&
            typeof e.statement_latex === "string",
        ) as VaultEntry[]
        if (valid.length === 0) {
          alert("No valid problems found in that file.")
          return
        }
        const mode = confirm(
          `Import ${valid.length} problem${valid.length !== 1 ? "s" : ""}?\n\n` +
            "OK = add to your current vault (merged, duplicates removed)\n" +
            "Cancel = replace your vault entirely",
        )
        if (mode) {
          // Merge by id.
          const current = vaultGet()
          const seen = new Set(current.map((e) => e.id))
          for (const entry of valid) {
            if (!seen.has(entry.id)) {
              current.push(entry)
              seen.add(entry.id)
            }
          }
          vaultSet(current)
        } else {
          if (!confirm(`Replace your current vault with ${valid.length} imported problem${valid.length !== 1 ? "s" : ""}?`)) {
            return
          }
          vaultSet(valid)
        }
        renderVault(mount)
      } catch (err: any) {
        alert("Import failed: " + (err && err.message ? err.message : err))
      } finally {
        importInput.value = ""
      }
    }
    reader.onerror = () => {
      alert("Could not read that file.")
      importInput.value = ""
    }
    reader.readAsText(file)
  })

  clearBtn.addEventListener("click", () => {
    if (!confirm("Clear all problems from your vault?")) return
    localStorage.removeItem(VAULT_KEY)
    renderVault(mount)
  })

  renderKatexWithRetry(mount)
}

// --- Entry point ------------------------------------------------------------

function initVaultViewer() {
  const mount = document.getElementById("vault-mount")
  if (!mount) return
  renderVault(mount)
}

document.addEventListener("nav", initVaultViewer)

// Re-render on external vault changes (same tab, from ProblemVaultWidget)
document.addEventListener("math-wiki-vault-change", () => {
  const mount = document.getElementById("vault-mount")
  if (mount) renderVault(mount)
})
