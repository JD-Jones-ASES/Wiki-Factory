// Math Wiki VaultViewer --- renders the user's localStorage vault on /Vault.
//
// Runs on every page via afterDOMLoaded. Early-returns if #vault-mount is
// absent. On the Vault page: fetches the bank, resolves each saved ID,
// renders problems with collapsible hints/answers, and provides
// shuffle/print/clear controls.

type VaultEntry = { generator_id: string; problem_id: string }

type ProblemRecord = {
  id: string
  generator_id: string
  topic_slug: string
  difficulty: "easy" | "medium" | "hard"
  statement_latex: string
  answer_latex: string
  hints: string[]
  solution_steps_latex: string[]
  tags: string[]
}

type ProblemBank = {
  version: string
  generated_at: string
  problem_types: Record<
    string,
    {
      topic_slug: string
      display_name: string
      problems: Record<string, ProblemRecord[]>
    }
  >
}

const VAULT_KEY = "math-wiki-vault"
let BANK_CACHE: ProblemBank | null = null

// --- URL helpers ------------------------------------------------------------

function getMathWikiRoot(): string {
  const match = location.pathname.match(/^(.*?\/Math_Wiki\/)/)
  return match ? match[1] : "/"
}

async function fetchBank(): Promise<ProblemBank> {
  if (BANK_CACHE) return BANK_CACHE
  const url = getMathWikiRoot() + "_data/problems.json"
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Bank fetch failed: ${res.status} at ${url}`)
  BANK_CACHE = (await res.json()) as ProblemBank
  return BANK_CACHE
}

// --- Vault state ------------------------------------------------------------

function vaultGet(): VaultEntry[] {
  try {
    const raw = localStorage.getItem(VAULT_KEY)
    if (!raw) return []
    const parsed = JSON.parse(raw)
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

function vaultSet(entries: VaultEntry[]) {
  localStorage.setItem(VAULT_KEY, JSON.stringify(entries))
}

// --- Lookup -----------------------------------------------------------------

function findProblem(bank: ProblemBank, entry: VaultEntry): ProblemRecord | null {
  const pt = bank.problem_types[entry.generator_id]
  if (!pt) return null
  for (const diff of Object.keys(pt.problems)) {
    const match = pt.problems[diff].find((p) => p.id === entry.problem_id)
    if (match) return match
  }
  return null
}

// --- KaTeX rendering --------------------------------------------------------

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
    // Split on $$...$$ (display) OR $...$ (inline)
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

function renderKatexWithRetry(el: HTMLElement, attempts = 8) {
  if ((window as any).katex) {
    renderKatexIn(el)
    return
  }
  if (attempts <= 0) return
  setTimeout(() => renderKatexWithRetry(el, attempts - 1), 150)
}

// --- Main rendering ---------------------------------------------------------

function renderVault(mount: HTMLElement, bank: ProblemBank) {
  const vault = vaultGet()
  mount.innerHTML = ""
  mount.classList.add("vv-root")

  if (vault.length === 0) {
    const empty = document.createElement("div")
    empty.className = "vv-empty"
    empty.innerHTML = `
      <p>Your vault is empty.</p>
      <p>Navigate to any topic (for example,
      <a href="${getMathWikiRoot()}topics/geometry/Circles">Circles</a>)
      and use the <strong>Add to Vault</strong> button to start building a
      practice set.</p>
    `
    mount.appendChild(empty)
    return
  }

  // Resolve problems; skip any entries that can't be found (stale IDs)
  const problems: Array<{ entry: VaultEntry; problem: ProblemRecord }> = []
  for (const entry of vault) {
    const problem = findProblem(bank, entry)
    if (problem) problems.push({ entry, problem })
  }

  if (problems.length === 0) {
    const empty = document.createElement("div")
    empty.className = "vv-empty"
    empty.innerHTML = `
      <p>None of your saved problems were found in the current bank.</p>
      <p>The bank may have been regenerated since you added them.
      <button type="button" class="vv-btn vv-clear-stale">Clear Stale Vault</button></p>
    `
    mount.appendChild(empty)
    empty.querySelector(".vv-clear-stale")?.addEventListener("click", () => {
      vaultSet([])
      renderVault(mount, bank)
    })
    return
  }

  // --- Header with counts and actions ---
  const header = document.createElement("div")
  header.className = "vv-header"

  const countDiv = document.createElement("div")
  countDiv.className = "vv-count"
  const countBold = document.createElement("strong")
  countBold.textContent = String(problems.length)
  countDiv.appendChild(countBold)
  countDiv.appendChild(
    document.createTextNode(
      ` problem${problems.length !== 1 ? "s" : ""} in your vault`,
    ),
  )

  const actions = document.createElement("div")
  actions.className = "vv-actions vv-no-print"

  const shuffleBtn = document.createElement("button")
  shuffleBtn.type = "button"
  shuffleBtn.className = "vv-btn vv-shuffle"
  shuffleBtn.textContent = "Shuffle"

  const printBtn = document.createElement("button")
  printBtn.type = "button"
  printBtn.className = "vv-btn vv-print"
  printBtn.textContent = "Print Worksheet"

  const clearBtn = document.createElement("button")
  clearBtn.type = "button"
  clearBtn.className = "vv-btn vv-clear"
  clearBtn.textContent = "Clear Vault"

  actions.appendChild(shuffleBtn)
  actions.appendChild(printBtn)
  actions.appendChild(clearBtn)

  header.appendChild(countDiv)
  header.appendChild(actions)
  mount.appendChild(header)

  // --- Problems list ---
  const list = document.createElement("ol")
  list.className = "vv-problems"

  problems.forEach(({ entry, problem }) => {
    const li = document.createElement("li")
    li.className = "vv-problem"

    const statement = document.createElement("div")
    statement.className = "vv-statement"
    statement.textContent = problem.statement_latex
    li.appendChild(statement)

    // Workspace area (blank lines for student work; shown in print)
    const workspace = document.createElement("div")
    workspace.className = "vv-workspace"
    li.appendChild(workspace)

    // Interactive controls (hidden in print)
    const controls = document.createElement("div")
    controls.className = "vv-controls vv-no-print"

    if (problem.hints.length > 0) {
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

    if (problem.solution_steps_latex.length > 0) {
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
      const filtered = current.filter(
        (e) =>
          !(e.generator_id === entry.generator_id && e.problem_id === entry.problem_id),
      )
      vaultSet(filtered)
      renderVault(mount, bank)
    })
    controls.appendChild(removeBtn)

    li.appendChild(controls)
    list.appendChild(li)
  })

  mount.appendChild(list)

  // --- Answer key (opens automatically on print) ---
  const answerKey = document.createElement("details")
  answerKey.className = "vv-answer-key"
  const aks = document.createElement("summary")
  aks.textContent = "Answer Key"
  answerKey.appendChild(aks)
  const akList = document.createElement("ol")
  akList.className = "vv-answer-key-list"
  problems.forEach(({ problem }) => {
    const akli = document.createElement("li")
    akli.textContent = problem.answer_latex
    akList.appendChild(akli)
  })
  answerKey.appendChild(akList)
  mount.appendChild(answerKey)

  // --- Wire up actions ---
  shuffleBtn.addEventListener("click", () => {
    const shuffled = vaultGet().slice()
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    vaultSet(shuffled)
    renderVault(mount, bank)
  })

  printBtn.addEventListener("click", () => {
    // Open answer key so it prints
    answerKey.open = true
    window.print()
  })

  clearBtn.addEventListener("click", () => {
    if (!confirm("Clear all problems from your vault?")) return
    vaultSet([])
    renderVault(mount, bank)
  })

  renderKatexWithRetry(mount)
}

// --- Entry point ------------------------------------------------------------

function initVaultViewer() {
  const mount = document.getElementById("vault-mount")
  if (!mount) return

  fetchBank()
    .then((bank) => renderVault(mount, bank))
    .catch((err) => {
      console.error("[vault-viewer]", err)
      mount.innerHTML = `<div class="vv-error">Could not load the problem bank: ${String(err)}</div>`
    })
}

document.addEventListener("nav", initVaultViewer)

// Re-render when the ProblemVaultWidget (or another tab) adds to the vault
document.addEventListener("math-wiki-vault-change", () => {
  const mount = document.getElementById("vault-mount")
  if (!mount || !BANK_CACHE) return
  renderVault(mount, BANK_CACHE)
})
