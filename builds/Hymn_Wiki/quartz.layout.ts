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
      filterFn: (node: FileTrieNode) => {
        const name = node.slugSegment
        if (!name) return true
        // Hide individual hymn pages (1,740 items — navigate via Hymns_Overview or search)
        if (name.startsWith("Hymn_")) return false
        // Hide entities folder (284 items — navigate via People_Overview)
        if (name === "entities") return false
        // Hide concepts folder (46 items — navigate via Concepts_Overview)
        if (name === "concepts") return false
        // Hide internal/maintenance files
        if (name.startsWith("_") && name !== "_overview" && name !== "_scripture_index" && name !== "_index") return false
        // Hide JSON data files
        if (name.endsWith("_data") || name.endsWith("_data_part1") || name.endsWith("_data_part2")) return false
        return true
      },
      mapFn: (node: FileTrieNode) => {
        const friendlyNames: Record<string, string> = {
          "sources": "📚 Sources",
          "synthesis": "📖 Stories & Analysis",
          "timelines": "📅 Timelines",
        }
        if (node.isFolder && node.slugSegment && friendlyNames[node.slugSegment]) {
          node.displayName = friendlyNames[node.slugSegment]
        }
      },
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        depth: 1,        // Show only direct connections
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
      filterFn: (node: FileTrieNode) => {
        const name = node.slugSegment
        if (!name) return true
        if (name.startsWith("Hymn_")) return false
        if (name === "entities") return false
        if (name === "concepts") return false
        if (name.startsWith("_") && name !== "_overview" && name !== "_scripture_index" && name !== "_index") return false
        if (name.endsWith("_data") || name.endsWith("_data_part1") || name.endsWith("_data_part2")) return false
        return true
      },
      mapFn: (node: FileTrieNode) => {
        const friendlyNames: Record<string, string> = {
          "sources": "📚 Sources",
          "synthesis": "📖 Stories & Analysis",
          "timelines": "📅 Timelines",
        }
        if (node.isFolder && node.slugSegment && friendlyNames[node.slugSegment]) {
          node.displayName = friendlyNames[node.slugSegment]
        }
      },
    }),
  ],
  right: [],
}
