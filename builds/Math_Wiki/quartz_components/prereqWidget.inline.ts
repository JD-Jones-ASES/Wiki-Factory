// Math Wiki PrereqWidget --- client-side behavior.
//
// Runs on every page via Quartz's afterDOMLoaded hook. Early-returns if the
// current page is not a topic page (determined by URL slug lookup in the
// fetched prereq graph). On a topic page, fetches the prereq graph once per
// session and injects a "Review these first" card into the right sidebar.

type PrereqEntry = {
  slug: string
  stem: string
  title: string
}

type PrereqTopic = {
  title: string
  slug: string
  branch: string
  prerequisites: PrereqEntry[]
  used_by: string[]
}

type PrereqGraph = {
  version: string
  generated_from: string
  topics: Record<string, PrereqTopic>
}

const GRAPH_CACHE_KEY = "__mathWikiPrereqGraph"

// --- URL helpers ------------------------------------------------------------

function getMathWikiRoot(): string {
  const match = location.pathname.match(/^(.*?\/Math_Wiki\/)/)
  return match ? match[1] : "/"
}

async function fetchGraph(): Promise<PrereqGraph> {
  const w = window as any
  if (w[GRAPH_CACHE_KEY]) return w[GRAPH_CACHE_KEY]
  const url = getMathWikiRoot() + "_data/prereq_graph.json"
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Prereq graph fetch failed: ${res.status}`)
  w[GRAPH_CACHE_KEY] = (await res.json()) as PrereqGraph
  return w[GRAPH_CACHE_KEY]
}

// Extract the stem (e.g., "Triangle_Congruence_Criteria") from the current
// page URL. Topic pages live at /Math_Wiki/topics/<branch>/<stem>/ in
// production and /topics/<branch>/<stem> locally. Everything after the last
// "topics" segment up to the trailing slash is the stem, but we also handle
// a possible trailing segment name that carries the stem.
function currentPageStem(): string | null {
  const path = location.pathname.replace(/\/+$/, "")
  const parts = path.split("/").filter(Boolean)
  const topicsIdx = parts.lastIndexOf("topics")
  if (topicsIdx < 0) return null
  // Expect at least: topics / <branch> / <stem>
  const rest = parts.slice(topicsIdx + 1)
  if (rest.length < 2) return null
  // The stem is the last non-index segment.
  const tail = rest[rest.length - 1]
  if (!tail || tail === "index") return null
  // Quartz emits directory indexes, so the tail might be the stem already.
  // Capitalize / normalize: keep original casing (graph is keyed by stem).
  return tail
}

// The graph keys are stem casing (Underscored_Title_Case). The URL often
// uses lowercase. Try exact first, then case-insensitive lookup.
function lookupStem(graph: PrereqGraph, urlSegment: string): PrereqTopic | null {
  if (graph.topics[urlSegment]) return graph.topics[urlSegment]
  const lower = urlSegment.toLowerCase()
  for (const [stem, topic] of Object.entries(graph.topics)) {
    if (stem.toLowerCase() === lower) return topic
  }
  return null
}

// --- DOM ------------------------------------------------------------------

function buildCard(topic: PrereqTopic): HTMLElement {
  const card = document.createElement("div")
  card.className = "prereq-widget-card"

  const header = document.createElement("div")
  header.className = "prereq-widget-header"
  header.textContent = "Review these first"
  card.appendChild(header)

  if (topic.prerequisites.length === 0) {
    const empty = document.createElement("p")
    empty.className = "prereq-widget-empty"
    empty.textContent = "No prerequisites listed for this topic."
    card.appendChild(empty)
    return card
  }

  const ul = document.createElement("ul")
  ul.className = "prereq-widget-list"
  const limit = Math.min(topic.prerequisites.length, 6)
  for (let i = 0; i < limit; i++) {
    const prereq = topic.prerequisites[i]
    const li = document.createElement("li")
    const a = document.createElement("a")
    a.href = getMathWikiRoot() + prereq.slug
    a.textContent = prereq.title
    li.appendChild(a)
    ul.appendChild(li)
  }
  card.appendChild(ul)

  if (topic.prerequisites.length > limit) {
    const more = document.createElement("p")
    more.className = "prereq-widget-more"
    more.textContent = `and ${topic.prerequisites.length - limit} more`
    card.appendChild(more)
  }

  return card
}

// Insert the card into the right sidebar. Quartz renders the right pane
// with a consistent class name; we pick it up at runtime and append our
// card below the existing sidebar cells.
function insertCard(card: HTMLElement): void {
  // Try the canonical Quartz right sidebar first.
  const sidebar =
    document.querySelector(".sidebar.right") ||
    document.querySelector(".right.sidebar") ||
    document.querySelector('[data-layout="sidebar-right"]')
  if (sidebar) {
    sidebar.appendChild(card)
    return
  }
  // Fallback: append after the Backlinks component if that is on the page.
  const backlinks = document.querySelector(".backlinks")
  if (backlinks && backlinks.parentElement) {
    backlinks.parentElement.appendChild(card)
    return
  }
  // Final fallback: append to the article body just before See Also.
  const article = document.querySelector("article") || document.body
  article.appendChild(card)
}

// --- Boot ------------------------------------------------------------------

async function boot(): Promise<void> {
  const stem = currentPageStem()
  if (!stem) return

  let graph: PrereqGraph
  try {
    graph = await fetchGraph()
  } catch (err) {
    // Silent failure: the widget simply does not render. No console spam.
    return
  }

  const topic = lookupStem(graph, stem)
  if (!topic) return

  // Avoid re-inserting the card on SPA-like navigations. Quartz has
  // enableSPA: false for Math Wiki, so each nav is a full reload, but
  // belt-and-suspenders: look for an existing card before adding one.
  if (document.querySelector(".prereq-widget-card")) return

  const card = buildCard(topic)
  insertCard(card)
}

// Boot on DOM ready. Multiple hook fires on the same page are a no-op
// because of the existing-card check.
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => {
    void boot()
  })
} else {
  void boot()
}
