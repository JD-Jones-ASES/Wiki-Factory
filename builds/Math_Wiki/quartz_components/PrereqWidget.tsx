import { QuartzComponent, QuartzComponentConstructor } from "./types"
// @ts-ignore
import script from "./prereqWidget.inline"
import style from "./prereqWidget.scss"

/**
 * PrereqWidget --- Math Wiki custom component.
 *
 * Renders a "Review these first" card on topic pages. The card lists each
 * topic's immediate prerequisites (from YAML frontmatter) as clickable
 * links, giving a struggling student an obvious next-step backward.
 *
 * Server-side output is empty. The inline script fetches the prereq graph
 * on first topic-page load and injects the card next to the backlinks /
 * graph view in the right sidebar. Mount point lookup is slug-driven so
 * the widget only renders on pages that actually have an entry.
 */
const PrereqWidget: QuartzComponent = () => <></>

PrereqWidget.css = style
PrereqWidget.afterDOMLoaded = script

export default (() => PrereqWidget) satisfies QuartzComponentConstructor
