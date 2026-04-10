// Math Wiki ProblemVaultWidget --- client-side behavior.
//
// Runs on every page via Quartz's afterDOMLoaded hook. Early-returns if the
// current page does not contain a `.problem-vault-widget[data-topic-slug]`
// mount point. On a topic page, fetches the problem bank JSON, filters by
// topic_slug, and renders an interactive control strip with Add-to-Vault
// buttons that write to localStorage.

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

type ProblemTypeEntry = {
  topic_slug: string
  generator_id: string
  display_name: string
  supports_word_problems: boolean
  problems: Record<string, ProblemRecord[]>
}

type ProblemBank = {
  version: string
  generated_at: string
  total_problems: number
  problem_types: Record<string, ProblemTypeEntry>
}

type VaultEntry = { generator_id: string; problem_id: string }

const VAULT_KEY = "math-wiki-vault"
let BANK_CACHE: ProblemBank | null = null

// --- URL helpers ------------------------------------------------------------

function getMathWikiRoot(): string {
  // Works for both local dev (/Math_Wiki/...) and prod (/Wiki-Factory/Math_Wiki/...).
  const match = location.pathname.match(/^(.*?\/Math_Wiki\/)/)
  return match ? match[1] : "/"
}

async function fetchBank(): Promise<ProblemBank> {
  if (BANK_CACHE) return BANK_CACHE
  const url = getMathWikiRoot() + "_data/problems.json"
  const res = await fetch(url)
  if (!res.ok) {
    throw new Error(`Problem bank fetch failed: ${res.status} at ${url}`)
  }
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

function vaultAdd(entries: VaultEntry[]) {
  const current = vaultGet()
  localStorage.setItem(VAULT_KEY, JSON.stringify([...current, ...entries]))
  document.dispatchEvent(new CustomEvent("math-wiki-vault-change"))
}

// --- Toast notifications ----------------------------------------------------

function toast(message: string) {
  const el = document.createElement("div")
  el.className = "mwv-toast"
  el.textContent = message
  document.body.appendChild(el)
  requestAnimationFrame(() => el.classList.add("mwv-toast-show"))
  setTimeout(() => {
    el.classList.remove("mwv-toast-show")
    setTimeout(() => el.remove(), 300)
  }, 2400)
}

// --- KaTeX dynamic rendering ------------------------------------------------

function renderKatexIn(root: HTMLElement) {
  const katex = (window as any).katex
  if (!katex || typeof katex.render !== "function") return

  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT)
  const texts: Text[] = []
  let current: Node | null
  while ((current = walker.nextNode())) texts.push(current as Text)

  for (const text of texts) {
    const content = text.textContent ?? ""
    if (!content.includes("$")) continue
    const parts = content.split(/(\$[^$\n]+\$)/g)
    if (parts.length <= 1) continue
    const frag = document.createDocumentFragment()
    for (const part of parts) {
      if (part.startsWith("$") && part.endsWith("$") && part.length > 2) {
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
  const katex = (window as any).katex
  if (katex) {
    renderKatexIn(el)
    return
  }
  if (attempts <= 0) return
  setTimeout(() => renderKatexWithRetry(el, attempts - 1), 150)
}

// --- Random selection -------------------------------------------------------

function pickRandomSubset<T>(arr: T[], n: number): T[] {
  const copy = arr.slice()
  const result: T[] = []
  const limit = Math.min(n, copy.length)
  for (let i = 0; i < limit; i++) {
    const j = Math.floor(Math.random() * copy.length)
    result.push(copy.splice(j, 1)[0])
  }
  return result
}

// --- Widget rendering -------------------------------------------------------

function renderWidget(mount: HTMLElement, bank: ProblemBank) {
  const topicSlug = mount.getAttribute("data-topic-slug")
  if (!topicSlug) {
    mount.textContent = "(problem-vault-widget is missing data-topic-slug)"
    return
  }

  const matching: ProblemTypeEntry[] = Object.values(bank.problem_types).filter(
    (pt) => pt.topic_slug === topicSlug,
  )

  if (matching.length === 0) {
    mount.innerHTML =
      `<div class="mwv-empty">No problem types are registered for topic ` +
      `<code>${topicSlug}</code> yet. Check back after Phase 2 ingest.</div>`
    return
  }

  mount.innerHTML = ""
  mount.classList.add("mwv-widget")

  const header = document.createElement("div")
  header.className = "mwv-header"
  const titleStrong = document.createElement("strong")
  titleStrong.textContent = "Build your practice set"
  const vaultCount = document.createElement("span")
  vaultCount.className = "mwv-vault-count"
  const vaultCountBold = document.createElement("b")
  vaultCountBold.textContent = String(vaultGet().length)
  vaultCount.appendChild(document.createTextNode("Vault: "))
  vaultCount.appendChild(vaultCountBold)
  header.appendChild(titleStrong)
  header.appendChild(vaultCount)
  mount.appendChild(header)

  for (const pt of matching) {
    const row = document.createElement("div")
    row.className = "mwv-row"

    const diffs = Object.keys(pt.problems).filter((d) => pt.problems[d].length > 0)
    const defaultDiff = diffs.includes("medium") ? "medium" : diffs[0] ?? "easy"

    const label = document.createElement("div")
    label.className = "mwv-row-label"
    label.textContent = pt.display_name

    const controls = document.createElement("div")
    controls.className = "mwv-row-controls"

    const diffSelect = document.createElement("select")
    diffSelect.className = "mwv-difficulty"
    diffSelect.setAttribute("aria-label", "Difficulty")
    for (const d of diffs) {
      const opt = document.createElement("option")
      opt.value = d
      opt.textContent = d
      if (d === defaultDiff) opt.selected = true
      diffSelect.appendChild(opt)
    }

    const count = document.createElement("input")
    count.type = "number"
    count.min = "1"
    count.max = "20"
    count.value = "3"
    count.className = "mwv-count"
    count.setAttribute("aria-label", "Number of problems")

    const button = document.createElement("button")
    button.type = "button"
    button.className = "mwv-add"
    button.textContent = "+ Add to Vault"

    button.addEventListener("click", () => {
      const diff = diffSelect.value
      const n = Math.max(1, Math.min(20, parseInt(count.value, 10) || 3))
      const pool = pt.problems[diff] ?? []
      if (pool.length === 0) {
        toast("No problems available at that difficulty.")
        return
      }
      const picked = pickRandomSubset(pool, n)
      vaultAdd(
        picked.map((p) => ({ generator_id: pt.generator_id, problem_id: p.id })),
      )
      toast(`Added ${picked.length} problem${picked.length !== 1 ? "s" : ""} to your Vault.`)
      vaultCountBold.textContent = String(vaultGet().length)
    })

    controls.appendChild(diffSelect)
    controls.appendChild(count)
    controls.appendChild(button)
    row.appendChild(label)
    row.appendChild(controls)
    mount.appendChild(row)
  }

  const footer = document.createElement("div")
  footer.className = "mwv-footer"
  const link = document.createElement("a")
  link.href = getMathWikiRoot() + "Vault"
  link.textContent = "View your Vault →"
  link.className = "mwv-vault-link"
  footer.appendChild(link)
  mount.appendChild(footer)

  renderKatexWithRetry(mount)
}

// --- Entry point ------------------------------------------------------------

function initProblemVaultWidget() {
  const mounts = document.querySelectorAll<HTMLElement>(
    ".problem-vault-widget[data-topic-slug]",
  )
  if (mounts.length === 0) return

  fetchBank()
    .then((bank) => {
      mounts.forEach((m) => renderWidget(m, bank))
    })
    .catch((err) => {
      console.error("[problem-vault-widget]", err)
      mounts.forEach((m) => {
        m.innerHTML = `<div class="mwv-error">Could not load problem bank: ${String(err)}</div>`
      })
    })
}

// Run on Quartz SPA navigation and initial load
document.addEventListener("nav", initProblemVaultWidget)
