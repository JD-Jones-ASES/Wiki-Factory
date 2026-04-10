import { QuartzComponent, QuartzComponentConstructor } from "./types"
// @ts-ignore
import script from "./problemVaultWidget.inline"
import style from "./problemVaultWidget.scss"

/**
 * ProblemVaultWidget --- Math Wiki custom component.
 *
 * Renders nothing server-side. Its job is to register the inline client
 * script and stylesheet with Quartz's resource pipeline so they ship on
 * every page. The actual widget UI is injected at runtime into any
 *   <div class="problem-vault-widget" data-topic-slug="..."></div>
 * mount point found on the current page.
 */
const ProblemVaultWidget: QuartzComponent = () => <></>

ProblemVaultWidget.css = style
ProblemVaultWidget.afterDOMLoaded = script

export default (() => ProblemVaultWidget) satisfies QuartzComponentConstructor
