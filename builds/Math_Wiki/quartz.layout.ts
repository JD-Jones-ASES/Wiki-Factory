import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import { FileTrieNode } from "./quartz/util/fileTrie"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      "All Wikis": "https://JD-Jones-ASES.github.io/Wiki-Factory/",
      "Source": "https://github.com/JD-Jones-ASES/Wiki-Factory",
    },
  }),
}

// Shared filter: hide large collections and internal files from the Explorer sidebar.
// Navigation happens via overview hubs, search, and wikilinks.
const mathExplorerFilter = (node: FileTrieNode) => {
  const name = node.slugSegment
  if (!name) return true
  // Hide topic folders (navigate via branch overview pages like Algebra_Overview)
  if (name === "topics") return false
  // Hide problem_type folders (navigate via topic pages' Problems Involving widget)
  if (name === "problem_types") return false
  // Hide entities folder (sparingly populated; navigate via Entities_Overview)
  if (name === "entities") return false
  // Hide internal/maintenance files and JSON data shards
  if (name.startsWith("_") && !["_overview", "_index"].includes(name)) return false
  if (name === "problems" || name.startsWith("problems_")) return false
  return true
}

const mathExplorerMap = (node: FileTrieNode) => {
  const friendlyNames: Record<string, string> = {
    "formulas": "🧮 Formulas",
    "techniques": "🛠️ Techniques",
    "sources": "📚 Sources",
    "synthesis": "📖 Comparisons",
  }
  if (node.isFolder && node.slugSegment && friendlyNames[node.slugSegment]) {
    node.displayName = friendlyNames[node.slugSegment]
  }
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      filterFn: mathExplorerFilter,
      mapFn: mathExplorerMap,
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        depth: 1,        // Show only direct connections (prevents visual overwhelm)
        repelForce: 0.5,
        linkDistance: 30,
      },
      globalGraph: {
        depth: -1,
        repelForce: 0.1,
        linkDistance: 30,
      },
    }),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      filterFn: mathExplorerFilter,
      mapFn: mathExplorerMap,
    }),
  ],
  right: [],
}
