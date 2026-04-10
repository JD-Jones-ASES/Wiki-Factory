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
// Navigation happens via overview hubs, search, and wikilinks.
//
// The Explorer sidebar aims to be a short, scannable list of navigation targets.
// It currently shows: branch hubs (Algebra, Geometry, Trigonometry, Precalculus),
// the landing page, Vault, Topic_Status, the category overviews (Formulas,
// Techniques, Sources, Synthesis, Entities, Problem_Types), and small folders
// (formulas/, techniques/, sources/, synthesis/). Large collections (topics/,
// problem_types/, entities/) are hidden — students reach them via branch hubs,
// search, and wikilinks.
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

// Friendlier sidebar labels. Folder-level mappings use an emoji + word.
// File-level mappings pick out the few high-traffic root files (Vault,
// Topic_Status) so they stand out from the branch-overview list. The rest of
// the files in the sidebar render with their frontmatter title as usual.
const mathExplorerMap = (node: FileTrieNode) => {
  const friendlyFolderNames: Record<string, string> = {
    "formulas": "🧮 Formulas",
    "techniques": "🛠️ Techniques",
    "sources": "📚 Sources",
    "synthesis": "📖 Comparisons",
  }
  const friendlyFileNames: Record<string, string> = {
    "Vault": "🎒 Your Vault",
    "Topic_Status": "📊 Progress Dashboard",
    "_overview": "🏠 Home",
    "Algebra_Overview": "📘 Algebra",
    "Geometry_Overview": "📐 Geometry",
    "Trigonometry_Overview": "📏 Trigonometry",
    "Precalculus_Overview": "🧮 Pre-Calculus",
    "Topics_Overview": "📖 All Topics",
    "Problem_Types_Overview": "🎯 Problem Types",
    "Formulas_Overview": "🧮 All Formulas",
    "Techniques_Overview": "🛠️ All Techniques",
    "Sources_Overview": "📚 All Sources",
    "Synthesis_Overview": "📖 All Comparisons",
    "Entities_Overview": "👩‍🏫 Mathematicians",
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
