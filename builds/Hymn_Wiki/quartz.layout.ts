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
        // Hide individual hymn pages from the explorer sidebar
        // (there are 1,324 of them — users navigate via search or Hymns_Overview)
        const name = node.slugSegment
        if (name && name.startsWith("Hymn_")) return false
        return true
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
        if (name && name.startsWith("Hymn_")) return false
        return true
      },
    }),
  ],
  right: [],
}
