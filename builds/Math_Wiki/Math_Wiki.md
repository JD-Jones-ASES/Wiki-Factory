# Math_Wiki.md --- A Practice-First Math Wiki & Tutor
## From Pre-Algebra through Pre-Calculus, with procedurally generated practice
### Version 1.0.0

| Field | Value |
|-------|-------|
| **Domain** | Middle and High School Mathematics |
| **Scope** | Pre-Algebra, Algebra 1, Geometry, Algebra 2, Trigonometry, Pre-Calculus. Calculus/Statistics deferred to a future ingest wave. |
| **Audience** | Students grades 6-12. Warm, encouraging, clear. Tutor-adjacent, not textbook-formal. |
| **Source count** | 5 (to be provided by user and placed in `raw/books/`) |
| **Scale** | Large (target: ~200 topic pages, ~100 generators, ~20,000+ verified problems) |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD |
| **URL** | `https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/` |

---

## Domain Analysis

Mathematics is a **procedural, hierarchical, and heavily cross-linked** domain. Unlike the Hymn Wiki's historical/biographical knowledge (where books cover different centuries and composers), math books cover the **same concepts** with different emphasis and pedagogy. This shapes every design choice:

- **Procedural:** Math is learned by doing, not reading. The core artifact of this wiki is **practice problems**, procedurally generated and verified, not prose summaries.
- **Hierarchical:** Concepts build on prerequisites (you cannot solve a quadratic until you understand a linear equation). Every topic page declares its prerequisites and related concepts.
- **Cross-linked:** A single technique (e.g., Completing the Square) appears in multiple topics (quadratics, conic sections, integration). A single formula (e.g., Pythagorean Theorem) underlies many topic areas. The wiki must link densely.
- **Overlapping sources:** All 5 books will cover linear equations, factoring, triangles, etc. The ingest pipeline must **merge** rather than **partition** — each topic page aggregates what every book teaches.

### Natural categories

- **Branches:** Pre-Algebra, Algebra 1, Geometry, Algebra 2, Trigonometry, Pre-Calculus.
- **Topics** (nouns): Linear Equations, Quadratic Functions, Circles, Right Triangles, Logarithms, ...
- **Problem Types** (verbs): Solve for x, Graph a line, Find area, Simplify expression, ...
- **Techniques** (methods): Factoring, Substitution, Completing the Square, Law of Sines, ...
- **Formulas** (named artifacts): Quadratic Formula, Pythagorean Theorem, Distance Formula, ...

### Key relationships

- `Topic → prerequisites → Topic` (directed, cycles forbidden)
- `Topic → uses → Formula`
- `Topic → uses → Technique`
- `Topic → exposes → Problem Type`
- `Problem Type → generates → many Problems` (via Python generator)
- `Problem Type → applies → Technique(s)`

These relationships drive both the wikilink structure and the widget's ability to surface "Problems involving [This]" on any topic page.

---

## Source Inventory

| # | Title | Author | Type | Pages | Priority | Role |
|---|-------|--------|------|-------|----------|------|
| 1 | _TBD_ | _TBD_ | textbook | _TBD_ | high | _Waiting for user to provide_ |
| 2 | _TBD_ | _TBD_ | textbook | _TBD_ | high | _Waiting for user to provide_ |
| 3 | _TBD_ | _TBD_ | textbook | _TBD_ | high | _Waiting for user to provide_ |
| 4 | _TBD_ | _TBD_ | textbook | _TBD_ | high | _Waiting for user to provide_ |
| 5 | _TBD_ | _TBD_ | textbook | _TBD_ | high | _Waiting for user to provide_ |

**Ingest strategy:** Because math books overlap heavily, this wiki uses a **merge-focused** ingest pipeline (different from the Hymn Wiki's partition-focused wave strategy):

1. Extract each book into a per-book JSON catalog (topics touched, problem types seen, formulas named, techniques discussed).
2. Consolidate all catalogs into canonical topic/formula/technique/problem_type pages.
3. Deduplicate problem-type names via fuzzy matching (SequenceMatcher, 0.80 threshold — per Hymn Wiki v2 precedent).
4. Write topic pages with contributions from multiple books clearly attributed (e.g., "From Book A: ..."; "From Book B adds: ...").
5. Run `yaml.safe_load()` on every modified file (Hymn Wiki v3 lesson).

**Copyright constraint:** Books are read for **structure and pedagogy**, not for copying. The same rule that governed Hymn Wiki lyrics ("NEVER reproduced by LLM; all text via Python scripts from source files") applies here:

> **NEVER reproduce problem text verbatim from any source book. Extract problem PATTERNS only (what's given, what's asked). Generate fresh problems via SymPy-verified Python generators. Copying is a hard failure and a legal risk.**

---

## Page Types & Schema

This wiki adds **four new custom page types** to the factory:

- **topic** (custom) — A math subject. Primary noun. Lesson prose, prerequisites, linked formulas, linked techniques, problem-type listings, figures. Schema: `factory/schemas/topic.yaml`.
- **problem_type** (custom) — A parametrized problem category tied to a Python generator. One page per canonical problem type. Schema: `factory/schemas/problem_type.yaml`.
- **technique** (custom) — A problem-solving method (e.g., Completing the Square). Schema: `factory/schemas/technique.yaml`.
- **formula** (custom) — A named formula (e.g., Quadratic Formula). Schema: `factory/schemas/formula.yaml`.

And reuses these standard factory types:

- **source** — One per ingested book.
- **synthesis** — Cross-topic analyses and comparisons.
- **entity** — Mathematicians (sparingly populated; historical color only).
- **overview** — Navigation hubs (landing page, branch hubs, type hubs).

### Directory layout under `wiki/`

```
wiki/
├── _overview.md                  ← Landing page (update after every ingest wave)
├── _index.md                     ← Content catalog (regenerated by build_index.py)
├── _log.md                       ← Chronological operations log
├── _tag_taxonomy.md              ← Controlled tag vocabulary
├── _data/                        ← Generated problem bank JSON (gitignored until stable)
├── Vault.md                      ← Interactive vault page (mounts VaultViewer component)
├── {Algebra,Geometry,Trigonometry,Precalculus}_Overview.md  ← Branch hubs
├── {Topics,Formulas,Problem_Types,Techniques,Sources,Synthesis,Entities}_Overview.md  ← Type hubs
├── topics/{algebra,geometry,trigonometry,precalculus}/
├── problem_types/{algebra,geometry,trigonometry,precalculus}/
├── techniques/
├── formulas/
├── entities/
├── sources/
├── synthesis/
└── assets/{figures,animations}/
```

---

## Ingest Workflow

### Phase A: Scripted extraction (per book, parallelizable)

`tools/ingest_math_book.py` parses each PDF via `pdfplumber` (with `pytesseract` OCR fallback for scanned pages), identifies chapter boundaries from the table of contents, and emits `raw/extractions/{book_slug}.json`. No LLM involved.

### Phase B: LLM narrative ingest (one agent per book, in parallel)

One Sonnet sub-agent per book. Each agent:
1. Receives: book extraction JSON + current state of `wiki/topics/` + full `_tag_taxonomy.md` content (not a reference — Hymn Wiki v2 lesson).
2. For each chapter, identifies topic(s) taught, drafts stubs or adds `From {Book Title}` subsections to existing topic pages, paraphrasing all definitions.
3. Records problem-type names seen (strings like "solve linear equation for x", not the problems themselves).
4. Outputs `raw/extractions/{book_slug}_llm.json` summarizing what it touched.

**Every agent prompt includes the copyright rule above, verbatim.**

### Phase C: Consolidation (single run, no agents)

`tools/consolidate_extractions.py`:
1. Merges all per-book extraction JSONs.
2. Deduplicates problem-type names via `difflib.SequenceMatcher` at 0.80 threshold.
3. Creates `wiki/problem_types/{branch}/{Name}.md` with placeholder `generator_id` for each canonical type.
4. Creates `wiki/formulas/{Name}.md` and `wiki/techniques/{Name}.md` stubs.
5. Runs `tools/sanitize_frontmatter.py` and `yaml.safe_load()` on everything it wrote.
6. Logs the catalog to `wiki/_log.md`.

### Phase D: Generator development

With the canonical problem-type catalog, write Python generators for each one. Order of priority: linear equations → quadratics → basic geometry → trig → pre-calc. Every generator lands with pytest coverage and SymPy verification. `tools/build_problem_bank.py` regenerates `wiki/_data/problems.json` after each batch.

### Phase E: Figures, linking, overviews

`tools/generate_figures.py` produces matplotlib SVGs referenced by topic frontmatter. `py -3 factory/scripts/add_navigation.py` injects breadcrumbs. `py -3 factory/scripts/build_index.py` rebuilds `_index.md`. Overview hubs populate with topic tables.

### Phase F: Deploy

Commit and push. GitHub Actions overlays `quartz.config.ts`, `quartz.layout.ts`, and the new `quartz_components/` and `static/` directories onto a fresh Quartz clone, then deploys to Pages.

---

## Interactive Features (beyond the factory default)

This is the first factory build with **client-side interactivity**. The implementation uses Quartz custom components overlaid into the cloned Quartz via CI, with all problem content pre-generated and shipped as a static JSON bank.

- **ProblemVaultWidget** on every topic page — lists problem types from the bank matching the current topic, lets the student add N problems at chosen difficulty to a localStorage vault.
- **VaultViewer** on `Vault.md` — renders vault contents with Show Hint / Show Answer / Remove controls, plus Print Worksheet and Download PDF.
- **Runtime KaTeX rendering** — widgets call `katex.render()` on dynamically injected math spans. KaTeX is loaded via CDN `afterDOMReady` by Quartz's `Plugin.Latex` emitter, so `window.katex` is available in widget code.
- **Problem bank** — `wiki/_data/problems.json` (committed) generated by `tools/build_problem_bank.py`. Sharded by branch if size exceeds ~2 MB.

See the full architecture in the approved plan at `C:\Users\jdj32\.claude\plans\serene-whistling-starfish.md`.

---

## Deployment

**GitHub Pages** via Quartz v4 static site generator with GitHub Actions CI/CD.

- **Repo:** `JD-Jones-ASES/Wiki-Factory`
- **URL:** `https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/`
- **Config files:** `quartz.config.ts` and `quartz.layout.ts` at this build root (overlaid onto fresh Quartz clone during CI)
- **Additional overlay:** `quartz_components/` (custom widgets) and `static/` (extra static assets), both guarded by directory existence checks in `.github/workflows/deploy.yml`. Hymn Wiki's build is unaffected.
- **Key Quartz settings:** `enableSPA: false`, `Plugin.Latex({ renderEngine: "katex" })`, Explorer `filterFn` hides `topics/`, `problem_types/`, `entities/` folders (navigated via overview hubs and search), Graph depth-1 local view.

---

## Conventions

- **Topic titles:** Title Case with underscores in filenames (`Linear_Equations.md`), spaces in `title:` frontmatter and wikilinks.
- **Problem type titles:** Descriptive verb phrase (`Find_Circle_Equation_From_Center_And_Radius.md`).
- **Formula titles:** Named formula (`Quadratic_Formula.md`, `Pythagorean_Theorem.md`).
- **Technique titles:** Gerund or noun phrase (`Completing_The_Square.md`, `Substitution_Method.md`).
- **LaTeX:** Use `$...$` for inline math, `$$...$$` for display math. KaTeX-compatible only.
- **Tags:** Always quoted in YAML (`tags: ["#tag-name"]`). Only tags from `_tag_taxonomy.md`.
- **Tone:** Warm, encouraging, clear. Explain the intuition first, then the formal statement. Avoid condescension. Assume the student is smart but learning. Every topic page ends with "You've got this" in spirit, not literally.
- **Copyright:** NEVER reproduce problems verbatim from any source. Extract patterns only. All problems come from `generators/` and are SymPy-verified.
- **Frontmatter hygiene:** After any scripted batch write, run `yaml.safe_load()` on every modified file. Sanitize quotes, backslashes, and unclosed brackets before writing. Hymn Wiki v3 lesson — do not repeat their three YAML failure modes.
- **External links:** Use `<a target="_blank" rel="noopener">` for YouTube, Desmos, external math tools.

---

## Self-Improvement Log

### Version 1.0.0 --- Phase 0 Scaffold (2026-04-10)

**What:** Factory schemas extended with `topic`, `problem_type`, `technique`, `formula`. Lint and navigation scripts updated. Math_Wiki build directory scaffolded with Obsidian config, Quartz config/layout, empty wiki subdirectories, and overview hub stubs.

**What worked:**
- Reusing Hymn Wiki's `quartz.config.ts` and `quartz.layout.ts` verbatim with only three changes (`pageTitle`, `pageTitleSuffix`, `baseUrl`) and a math-specific `filterFn`. `Plugin.Latex({ renderEngine: "katex" })` was already in the factory template.
- Adding new types to `lint_wiki.py` `VALID_TYPES` was a one-line change. Adding new sections to `add_navigation.py` `SECTION_MAP` was a four-line addition. Both non-breaking for Hymn Wiki.

**Open items carried forward:**
- The existing `SECTION_MAP['entities']` routes to `People_Overview`, which is Hymn Wiki-specific. Math Wiki's entities folder is not populated in Phase 0; if/when it is, the conflict will need a resolution (either a per-wiki override mechanism in `add_navigation.py`, or rename Math Wiki's hub to `People_Overview.md`, or relocate mathematicians to `wiki/people/`). Decision deferred to the phase where Math Wiki actually needs mathematician pages.
- `deploy.yml` overlay for `quartz_components/` and `static/` directories is applied in Phase 0 but is a no-op until Phase 1 writes the first components.

---
