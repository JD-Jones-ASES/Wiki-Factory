// Math Wiki ProblemVaultWidget --- client-side behavior.
//
// Runs on every page via Quartz's afterDOMLoaded hook. Early-returns if the
// current page does not contain a `.problem-vault-widget[data-topic-slug]`
// mount point. On a topic page, fetches the small problem_types_index and
// renders control rows. On first "Add to Vault" click for a given topic,
// lazily fetches the per-topic shard `_data/problems/{topic_slug}.json`,
// picks random problems, and writes their FULL content to localStorage so
// the VaultViewer does not need to refetch anything.

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

type IndexGeneratorEntry = {
  generator_id: string
  display_name: string
  supports_word_problems: boolean
  counts: Partial<Record<Difficulty, number>>
}

type ProblemTypesIndex = {
  version: string
  by_topic: Record<string, IndexGeneratorEntry[]>
}

type TopicShard = {
  version: string
  topic_slug: string
  generators: Record<
    string,
    {
      topic_slug: string
      display_name: string
      difficulties: Record<string, ProblemRecord[]>
    }
  >
}

// Vault entries in the new format are full problem records plus metadata.
type VaultEntry = ProblemRecord & { added_at: number }

const VAULT_KEY = "math-wiki-vault"
const INDEX_CACHE_KEY = "__mathWikiIndex"
const SHARD_CACHE_KEY = "__mathWikiShards"

// --- URL helpers ------------------------------------------------------------

function getMathWikiRoot(): string {
  const match = location.pathname.match(/^(.*?\/Math_Wiki\/)/)
  return match ? match[1] : "/"
}

async function fetchIndex(): Promise<ProblemTypesIndex> {
  const w = window as any
  if (w[INDEX_CACHE_KEY]) return w[INDEX_CACHE_KEY]
  const url = getMathWikiRoot() + "_data/problem_types_index.json"
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Index fetch failed: ${res.status}`)
  w[INDEX_CACHE_KEY] = await res.json()
  return w[INDEX_CACHE_KEY]
}

async function fetchTopicShard(topicSlug: string): Promise<TopicShard> {
  const w = window as any
  if (!w[SHARD_CACHE_KEY]) w[SHARD_CACHE_KEY] = {}
  if (w[SHARD_CACHE_KEY][topicSlug]) return w[SHARD_CACHE_KEY][topicSlug]
  const url = getMathWikiRoot() + `_data/problems/${topicSlug}.json`
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Shard fetch failed for ${topicSlug}: ${res.status}`)
  const shard = (await res.json()) as TopicShard
  w[SHARD_CACHE_KEY][topicSlug] = shard
  return shard
}

// --- Vault state ------------------------------------------------------------

function vaultGet(): VaultEntry[] {
  try {
    const raw = localStorage.getItem(VAULT_KEY)
    if (!raw) return []
    const parsed = JSON.parse(raw)
    if (!Array.isArray(parsed)) return []
    // Filter out any legacy Phase-1 entries that only have {generator_id, problem_id}.
    return parsed.filter(
      (e) => typeof e === "object" && e !== null && "statement_latex" in e,
    ) as VaultEntry[]
  } catch {
    return []
  }
}

function vaultAdd(newEntries: VaultEntry[]) {
  const current = vaultGet()
  localStorage.setItem(VAULT_KEY, JSON.stringify([...current, ...newEntries]))
  document.dispatchEvent(new CustomEvent("math-wiki-vault-change"))
}

// --- KaTeX runtime loading (singleton across all components) ---------------

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

function renderKatexWithRetry(el: HTMLElement) {
  ensureKatex()
    .then(() => renderKatexIn(el))
    .catch((err) => console.warn("[problem-vault-widget] KaTeX unavailable:", err))
}

// --- Toast ------------------------------------------------------------------

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

function renderWidget(
  mount: HTMLElement,
  topicSlug: string,
  generators: IndexGeneratorEntry[],
) {
  if (generators.length === 0) {
    mount.innerHTML =
      `<div class="mwv-empty">No problem types are registered for topic ` +
      `<code>${topicSlug}</code> yet.</div>`
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

  for (const gen of generators) {
    const row = document.createElement("div")
    row.className = "mwv-row"

    const diffs = (Object.keys(gen.counts) as Difficulty[]).filter(
      (d) => (gen.counts[d] ?? 0) > 0,
    )
    const defaultDiff = diffs.includes("medium") ? "medium" : diffs[0] ?? "easy"

    const label = document.createElement("div")
    label.className = "mwv-row-label"
    label.textContent = gen.display_name

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

    button.addEventListener("click", async () => {
      const diff = diffSelect.value
      const n = Math.max(1, Math.min(20, parseInt(count.value, 10) || 3))
      button.disabled = true
      button.textContent = "…"
      try {
        const shard = await fetchTopicShard(topicSlug)
        const pool =
          shard.generators[gen.generator_id]?.difficulties[diff] ?? []
        if (pool.length === 0) {
          toast("No problems available at that difficulty.")
          return
        }
        const picked = pickRandomSubset(pool, n) as ProblemRecord[]
        const now = Date.now()
        vaultAdd(picked.map((p) => ({ ...p, added_at: now })))
        toast(
          `Added ${picked.length} problem${picked.length !== 1 ? "s" : ""} to your Vault.`,
        )
        vaultCountBold.textContent = String(vaultGet().length)
      } catch (err) {
        console.error(err)
        toast("Could not load problems. Check console.")
      } finally {
        button.disabled = false
        button.textContent = "+ Add to Vault"
      }
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

  fetchIndex()
    .then((index) => {
      mounts.forEach((m) => {
        const topicSlug = m.getAttribute("data-topic-slug") ?? ""
        const generators = index.by_topic[topicSlug] ?? []
        renderWidget(m, topicSlug, generators)
      })
    })
    .catch((err) => {
      console.error("[problem-vault-widget]", err)
      mounts.forEach((m) => {
        m.innerHTML = `<div class="mwv-error">Could not load problem index: ${String(err)}</div>`
      })
    })
}

document.addEventListener("nav", initProblemVaultWidget)
