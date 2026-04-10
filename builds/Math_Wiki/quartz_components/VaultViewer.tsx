import { QuartzComponent, QuartzComponentConstructor } from "./types"
// @ts-ignore
import script from "./vaultViewer.inline"
import style from "./vaultViewer.scss"

/**
 * VaultViewer --- renders the contents of `math-wiki-vault` localStorage
 * inside any `#vault-mount` div on the page. Only the Vault.md page has
 * such a div; all other pages early-return.
 */
const VaultViewer: QuartzComponent = () => <></>

VaultViewer.css = style
VaultViewer.afterDOMLoaded = script

export default (() => VaultViewer) satisfies QuartzComponentConstructor
