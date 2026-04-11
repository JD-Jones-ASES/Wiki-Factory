import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import { FileTrieNode } from "./quartz/util/fileTrie"
// Math Wiki custom components (overlaid into quartz/components/ during CI build)
import ProblemVaultWidget from "./quartz/components/ProblemVaultWidget"
import VaultViewer from "./quartz/components/VaultViewer"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [ProblemVaultWidget(), VaultViewer()],
  footer: Component.Footer({
    links: {
      "All Wikis": "https://JD-Jones-ASES.github.io/Wiki-Factory/",
      "Source": "https://github.com/JD-Jones-ASES/Wiki-Factory",
    },
  }),
}

// Shared filter: hide large collections and internal files from the Explorer sidebar.
// Navigation happens via the five course hubs, search, and wikilinks.
//
// The Explorer sidebar is a short, scannable list of navigation targets:
// the landing page, the five course hubs (Middle School Math, Algebra 1,
// Geometry, Algebra 2, Pre-Calculus), the Vault and Progress dashboard,
// the Formulas index, and the All Topics index. Large collections
// (topics/, problem_types/, entities/, synthesis/, techniques/, sources/)
// are hidden -- students reach them via course hubs, search, and wikilinks.
const mathExplorerFilter = (node: FileTrieNode) => {
  const name = node.slugSegment
  if (!name) return true
  // Hide topic folders (navigate via course hubs like Algebra_1)
  if (name === "topics") return false
  // Hide problem_type folders (navigate via topic pages' Problems Involving widget)
  if (name === "problem_types") return false
  // Hide empty-shell folders that may still exist on disk
  if (name === "entities") return false
  if (name === "synthesis") return false
  if (name === "techniques") return false
  if (name === "sources") return false
  // Hide internal/maintenance files and JSON data shards
  if (name.startsWith("_") && !["_overview", "_index"].includes(name)) return false
  if (name === "problems" || name.startsWith("problems_")) return false
  return true
}

// Friendlier sidebar labels. Folder-level mappings use an emoji + word.
// File-level mappings pick out the root files that should stand out as
// navigation targets (the five course hubs, Vault, Progress, All Topics).
// Every other file renders with its frontmatter title as usual.
const mathExplorerMap = (node: FileTrieNode) => {
  const friendlyFolderNames: Record<string, string> = {
    "formulas": "🧮 Formulas",
  }
  const friendlyFileNames: Record<string, string> = {
    "_overview":          "🏠 Home",
    "Middle_School_Math": "🔢 Middle School Math",
    "Algebra_1":          "📗 Algebra 1",
    "Geometry":           "📕 Geometry",
    "Algebra_2":          "📙 Algebra 2",
    "Precalculus":        "📓 Pre-Calculus & Trig",
    "Topics_Overview":    "📖 All Topics",
    "Vault":              "🎒 Your Vault",
    "Topic_Status":       "📊 Progress",
    "Formulas_Overview":  "🧮 Formulas",
  }
  if (node.isFolder && node.slugSegment && friendlyFolderNames[node.slugSegment]) {
    node.displayName = friendlyFolderNames[node.slugSegment]
  }
  if (!node.isFolder && node.slugSegment && friendlyFileNames[node.slugSegment]) {
    node.displayName = friendlyFileNames[node.slugSegment]
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
