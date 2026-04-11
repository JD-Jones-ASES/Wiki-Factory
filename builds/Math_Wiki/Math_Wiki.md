# Math_Wiki.md --- A Practice-First Math Wiki & Tutor
## Student-facing, course-based navigation from middle school through pre-calculus
### Version 2.3.0 --- Test-Prep Phase: 4 waves, Precalc nav fix, standardized test tagging. (2026-04-11)

| Field | Value |
|-------|-------|
| **Domain** | Middle and High School Mathematics |
| **Scope** | Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus (through conics, matrices, complex numbers). Calculus + advanced statistics deferred. |
| **Audience** | Students grades 6-12. Warm, tutor-adjacent tone. Intuition first, formalism second. Now also: SAT / PSAT / ACT / CLT test-takers. |
| **Presentation** | **Standalone wiki.** No "paraphrased from textbooks" language in student-facing content. Internal `raw/books/` and `raw/extractions/` remain as build inputs but never surface in wiki output. |
| **Scale** | **210 live topics / 638 generators / 49,443 verified problems / 62 figures** |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD, ~2 min build time |
| **URL** | https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/ |
| **Status** | v2.3.0 **test-prep phase shipped** (nav fix + 4 waves + test tagging). Overall average score 53.9 -> 71.6. ~200 topics now carry at least one test tag. Auto-generated `/tags/test-{sat,psat,act,clt}` index pages serve as per-exam hubs. Remaining: 51 leftover stubs (mostly redundant/low-value), deferred Vault polish (worksheet builder, jsPDF, input-and-check answers), and optional new-book ingests. |

---

## Orientation for a New Session

**Read this file top to bottom before touching anything.** The history of how we got here has been compressed; what remains is the state you need to keep building safely.

### First commands in a fresh session

```bash
cd /c/Wiki_Factory/builds/Math_Wiki

# Sanity check: all four should be green
py -3 -m pytest generators/tests/ -q                # 29/29 passing
py -3 ../../factory/scripts/validate_yaml.py wiki/  # 273/273 clean
py -3 ../../factory/scripts/lint_wiki.py wiki/      # 0 errors, 0 warnings
py -3 tools/topic_status.py                         # avg ~71.6, 210 live topics at 3+ gens
```

If any of those fail, something has regressed — fix that before doing anything else.

### 30-second mental model

Math_Wiki is a **standalone, practice-first wiki**. Every live topic page has (a) clear original prose with worked examples and (b) an interactive problem-vault widget fed by SymPy-verified Python generators. Students read → add problems to a browser-local Vault → download worksheets. The site deploys to GitHub Pages via Quartz v4 on every push to main.

Navigation is **course-first**. Five course hubs (Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus & Trig) are the student's primary entry points. A 7th grader opens Middle School Math; a sophomore opens Algebra 2. Branch-level organization still exists in the underlying data model but is hidden from the student-facing sidebar.

Ten content clusters shipped (9 original + Cluster 10 HS Geometry). Each cluster delivered ~12-18 topics fully finished (prose + generators + figures + cross-links). The wiki also runs a **PrereqWidget** ("Review these first" card) in the right sidebar on every topic page, powered by YAML `prerequisites:` frontmatter, and the Vault supports JSON export/import so students can move practice sets across devices.

### Where things live

| Path | What |
|---|---|
| `raw/books/`, `raw/extractions/`, `raw/catalog/` | Internal build inputs and artifacts from the initial ingestion. Gitignored (except `raw/catalog/`). Never surface in the wiki. |
| `tools/aliases.yaml` | Manual merge/rename/split rules for `consolidate_extractions.py` |
| `wiki/_overview.md` | Landing page (hero + 5 course hub cards + learning paths) |
| `wiki/{Middle_School_Math,Algebra_1,Geometry,Algebra_2,Precalculus}.md` | Five student-facing course hubs (hand intro + learning path + AUTO:TOPICS block) |
| `wiki/Topics_Overview.md` | Alphabetical index grouped by course |
| `wiki/Topic_Status.md` | Auto-generated progress dashboard (regen with `topic_status.py`) |
| `wiki/Vault.md` | Interactive vault page (mounts VaultViewer with shuffle / print / export / import / clear) |
| `wiki/Formulas_Overview.md` | Named formulas and theorems index |
| `wiki/topics/{pre_algebra,algebra,precalculus,geometry}/*.md` | Topic pages. Grouped on disk by branch, surfaced by course hub via `branch:` frontmatter. |
| `wiki/_data/problem_types_index.json` | Widget lookup: topic_slug → generators. Drives live/stub classification. |
| `wiki/_data/problems/{topic_slug}.json` | Per-topic problem shards (committed, <320 KB each) |
| `wiki/_data/prereq_graph.json` | Directed prereq graph generated from YAML frontmatter. Fetched once per session by `PrereqWidget`. |
| `wiki/assets/figures/{branch}/*.svg` | 45 matplotlib SVG figures across branches |
| `generators/{algebra,pre_algebra,precalculus,geometry}/*.py` | 460 generators across 4 branch packages |
| `generators/base.py` | `Problem` dataclass, `Generator` ABC, `@register`, `all_generators()` |
| `generators/tests/` | Pytest: parametrized all-generators suite, copyright shingle check, consolidate snapshot, ingest smoke |
| `generators/latex_helpers.py` | `format_fraction`, `format_point`, `shift_expr`, `signed_int` |
| `quartz.config.ts` / `quartz.layout.ts` | Quartz v4 config + layout. Sidebar shows 10 entries: 🏠 Home, 5 course hubs, 📖 All Topics, 🎒 Vault, 📊 Progress, 🧮 Formulas. |
| `quartz_components/*.tsx, *.inline.ts` | `ProblemVaultWidget`, `VaultViewer`, `PrereqWidget` — overlaid onto Quartz at CI time |
| `tools/` | Build scripts (see Toolchain table below) |
| `.github/workflows/deploy.yml` | CI: pytest → validate_yaml → build_index → clone Quartz → overlay → build → deploy |

### All the useful commands

```bash
cd /c/Wiki_Factory/builds/Math_Wiki

# Validation (run these after any content or generator changes)
py -3 -m pytest generators/tests/ -q
py -3 ../../factory/scripts/validate_yaml.py wiki/
py -3 ../../factory/scripts/lint_wiki.py wiki/
py -3 -m pytest generators/tests/test_copyright_safety.py -q

# Bank and dashboard
py -3 tools/build_problem_bank.py                  # rebuild bank from generators (idempotent)
py -3 tools/topic_status.py                        # regenerate Topic_Status.md dashboard
py -3 tools/update_course_hubs.py                  # regenerate course hub AUTO:TOPICS blocks
py -3 tools/build_prereq_graph.py                  # regenerate wiki/_data/prereq_graph.json
py -3 tools/generate_figures.py                    # regenerate all matplotlib SVGs (deterministic)

# Ingest pipeline (rarely needed — only when adding a book or catalog tweak)
py -3 tools/ingest_math_book.py --all              # re-parse LaTeX → raw/extractions/
py -3 tools/consolidate_extractions.py             # raw/extractions/ + aliases.yaml → raw/catalog/
py -3 tools/generate_topic_stubs.py --branch all   # catalog → wiki/topics/ auto-stubs (skips existing)

# Add a NEW textbook end-to-end (guided, dry-run first)
py -3 tools/ingest_new_book.py --slug new_book --dry-run
py -3 tools/ingest_new_book.py --slug new_book
```

---

## Architecture

### The layers

```
[RAW BOOKS] → [PARSED EXTRACTIONS] → [CATALOG] → [WIKI PAGES]
   LaTeX         per-chapter JSON      per-branch    markdown
                                                         │
                                                         ▼
                                                  [PROBLEM BANK]
                                                  sharded JSON
                                                         │
                                                         ▼
                                                 [DEPLOYED SITE]
                                                 Quartz + custom TSX
                                                         │
                                                         ▼
                                                    [BROWSER]
                                              widget + localStorage vault
```

**Raw** (`raw/books/`, `raw/extractions/`, `raw/catalog/`) — build inputs and intermediaries from initial ingestion. All gitignored except `raw/catalog/`. Never surface in the wiki.

**Wiki** (`wiki/`) — LLM-owned markdown. 151 live topic pages + ~98 auto-stubs still on disk + 5 course hubs + problem bank shards + prereq graph.

**Outputs** — derived artifacts at build time (Quartz HTML). Not committed.

### Sharded problem bank

- `wiki/_data/problem_types_index.json` — small lookup (~250 KB). Fetched by the widget on every topic-page load. Maps `topic_slug` → list of `{generator_id, display_name, counts, supports_word_problems}`. Also contains `by_generator` and `by_topic` keys the CLI tools read from.
- `wiki/_data/problems/{topic_slug}.json` — per-topic shard, lazy-fetched on first "Add to Vault" click.
- Every shard stays under **320 KB** by default (30 problems per difficulty per generator). Override with `bank_count_per_difficulty = N` class attr when parameter space is smaller.
- Compact JSON output (no indent, `ensure_ascii=False`).

### LocalStorage-first vault

- On "Add to Vault", `problemVaultWidget.inline.ts` fetches the topic shard, picks random problems, and writes **full problem objects** (statement, answer, hints, solution steps) into `localStorage["math-wiki-vault"]`.
- The `/Vault` page reads entries directly from localStorage. **It never fetches the bank.** Instant load, zero external fetches.
- VaultViewer exposes five actions: Shuffle, Print Worksheet, Export JSON, Import JSON, Clear Vault. Export dumps a timestamped `math-wiki-vault-YYYY-MM-DD.json` via Blob + object URL. Import reads a file, validates minimum schema (`id`, `statement_latex`), and offers merge-or-replace.

### Widget architecture

- **ProblemVaultWidget** mounts on any page with `<div class="problem-vault-widget" data-topic-slug="{slug_lower}"></div>`. Renders the practice rows with difficulty + count + Add-to-Vault buttons.
- **VaultViewer** mounts on `/Vault` (element id `vault-mount`). Renders the current localStorage vault with hints, answers, solution steps, and the action row.
- **PrereqWidget** mounts on every topic page via URL-based lookup against `wiki/_data/prereq_graph.json`. Injects a "Review these first" card into the right sidebar with up to 6 clickable prerequisite links. Silent early-return on non-topic pages or pages missing from the graph.
- All three are custom Quartz components imported by `quartz.layout.ts` via explicit relative paths (`./quartz/components/...`). The CI overlay copies `quartz_components/*` into `quartz/components/` before `npx quartz build`. Each registers `.css` and `.afterDOMLoaded` entries; server-side output is empty.

### Runtime KaTeX loader

Quartz's `Plugin.Latex({ renderEngine: "katex" })` ships **only** `katex.min.css` plus the `copy-tex` contrib JS. It does **NOT** ship `katex.min.js` (Quartz renders math server-side at build time). For dynamic widget content:

- `ensureKatex()` is a singleton in both `.inline.ts` files. Uses `window.__mathWikiKatexLoad` to share the loading promise across components.
- Injects `<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" data-math-wiki-katex="1">` once on demand.
- `renderKatexIn(element)` walks text nodes and converts `$...$` and `$$...$$` into rendered spans/divs.

### Base URL awareness

Widgets fetch data using `getMathWikiRoot()`, which parses `location.pathname` to find the `/Math_Wiki/` segment. Handles both local dev (`/Math_Wiki/...`) and production (`/Wiki-Factory/Math_Wiki/...`) without hardcoding.

---

## Internal Build Inputs

The initial ingestion pulled from 5 textbooks in `raw/books/` (gitignored): `math_1` and `math_2` (middle school curriculum-factory layout), `algebra_1` and `algebra_2` (high school curriculum-factory), and `algtrig` (Stitz-Zeager topic-folder layout, pre-calc with trig). Totals: 47 chapters, 2,736 extracted blocks, ~3.4 MB of JSON extractions. Both LaTeX conventions are handled by `tools/ingest_math_book.py` via per-book `env_map` attributes — see the env_map Author's Guide section for adding a new book.

### Copyright rule (non-negotiable)

**NEVER reproduce problem text, worked examples, or extended prose verbatim from any source book.** All practice problems come from SymPy-verified Python generators producing fresh problems. Definitions and pedagogy are always paraphrased. Enforced by `generators/tests/test_copyright_safety.py` (15-word shingle match against `raw/extractions/**/*.json`). The wiki presents as standalone; source references are an internal build-tooling concept only.

---

## The Toolchain

All `tools/*.py` scripts are idempotent unless noted. Run from `builds/Math_Wiki/` with `py -3` (Windows).

| Tool | Purpose |
|---|---|
| `tools/ingest_math_book.py` | Parse LaTeX source → per-chapter JSON shards in `raw/extractions/`. Destructive. |
| `tools/consolidate_extractions.py` | Merge extractions → per-branch catalog shards in `raw/catalog/`. Applies `aliases.yaml` rules. Destructive. |
| `tools/ingest_new_book.py` | 9-step guided pipeline for adding a new textbook. Dry-run supported. Doubles as docs. |
| `tools/generate_topic_stubs.py` | Catalog → `wiki/topics/{branch}/*.md` stubs. Skips existing slugs; `--force` to overwrite. |
| `tools/update_course_hubs.py` | Regenerate `<!-- AUTO:TOPICS:BEGIN/END -->` blocks in the five course hubs. Walks topic frontmatter to group by course; reads `problem_types_index.json` to mark live vs stub. Also handles the Geometry allowlist second pass. |
| `tools/build_problem_bank.py` | Walk generator registry → per-topic shards + index. Cleans stale shards. |
| `tools/topic_status.py` | Score every topic 0-100 (prose/examples/generators/prereqs/see-also/figures/status). Writes `wiki/Topic_Status.md` + `wiki/_data/topic_status.json`. |
| `tools/build_prereq_graph.py` | Walk topic frontmatter → `wiki/_data/prereq_graph.json`. Emits forward (`prerequisites`) and reverse (`used_by`) edges. Feeds the PrereqWidget right-sidebar card. |
| `tools/generate_figures.py` | Matplotlib → deterministic SVGs in `wiki/assets/figures/`. Uses `svg.hashsalt` + `metadata={"Date": None}` for byte-identical output. |

Factory-level (run from repo root `/c/Wiki_Factory/`):

| Tool | Purpose |
|---|---|
| `factory/scripts/lint_wiki.py` | Validate frontmatter, check wikilinks, find orphans, verify tags. |
| `factory/scripts/validate_yaml.py` | `yaml.safe_load()` every `.md` frontmatter + type/status/tags validation. |
| `factory/scripts/build_index.py` | Regenerate `wiki/_index.md` from page frontmatter. |
| `factory/scripts/add_navigation.py` | Inject breadcrumbs on every page (multi-wiki-aware). |

---

## Generator Architecture

### Conventions

- **File:** `generators/{branch}/{topic_family}.py`
- **Class:** `@register`-decorated subclass of `Generator` from `generators.base`
- **Required attrs:** `generator_id` (snake_case unique), `topic_slug` (lowercase matching wiki page filename stem), `display_name`
- **Method:** `_generate_one(difficulty, rng) -> Problem`
- **`Problem` fields (all non-empty):** `id`, `generator_id`, `topic_slug`, `difficulty`, `statement_latex`, `answer_latex`, `hints` (≥2), `solution_steps_latex` (≥2), `tags` (quoted, from `_tag_taxonomy.md`)
- **Registration side effect:** importing the file via `generators/{branch}/__init__.py` adds the class to `generators.base.REGISTRY`. No manual registry list.

### Parameter-space discipline

- **Default:** 30 unique problems per difficulty (easy/medium/hard).
- **Override:** set `bank_count_per_difficulty = N` as a class attr when the parameter space is smaller (unit circle exact values, n-choose-k for small n, etc.). Pytest clamps test counts to `[5, min(10, bank_count_per_difficulty)]`.
- **Backward construction** is the rule, not the exception: pick the answer first, derive the parameters. This eliminates guess-and-check loops and guarantees clean integer or simple-fraction answers.

### Branch packages and what they contain

```
generators/
├── algebra/                   # 23 modules, ~200 generators
│   (linear equations, slopes, systems, absolute value, quadratic methods,
│    polynomials, factoring, rationals, radicals, functions & families,
│    transformations, exponentials, logarithms)
├── pre_algebra/               # 16 modules, ~50 generators
│   (integers, fractions, decimals, percents, ratios, order of operations,
│    algebra intro, inequalities intro, slope intercept)
├── precalculus/               # 5 modules, ~90 generators
│   (trig core + advanced, sequences & stats, conics & complex, matrices)
├── geometry/                  # 12 modules, ~60 generators  (expanded in Cluster 10)
│   ├── circles.py pythagoras.py                                    # pre-Cluster-10
│   ├── parallel_lines.py triangle_congruence.py                    # Cluster 10
│   ├── special_right_triangles.py polygon_angles.py quadrilaterals.py
│   ├── circle_theorems.py transformations.py
│   ├── volume.py surface_area.py coord_geometry.py
├── base.py                    # Generator, Problem, @register, make_problem_id, all_generators
├── latex_helpers.py           # format_fraction, format_point, shift_expr, signed_int
└── tests/
    ├── test_circles.py                 # parametrized all-generators smoke test
    ├── test_copyright_safety.py        # 15-word shingle scan
    ├── test_consolidate_snapshot.py    # catalog snapshot + alias ops
    └── test_ingest_smoke.py            # synthetic book fixture through full pipeline
```

### Testing flow after adding a generator

```bash
py -3 -m pytest generators/tests/ -q          # all 29 tests green
py -3 tools/build_problem_bank.py             # bank shard created/updated, <320 KB
py -3 tools/topic_status.py                   # topic's score bumps
```

---

## Gotchas That Bit Us (Internalize These)

These are the mechanical rules the build system enforces. Violating them breaks something downstream.

### Content authoring rules

1. **LaTeX display math needs multi-line `$$`.** Single-line `$$expr$$` renders as **inline** KaTeX. Always:
   ```markdown
   $$
   (x - h)^2 + (y - k)^2 = r^2
   $$
   ```
2. **Figures use Obsidian embed syntax, not markdown.** Quartz's link rewriter adds an extra `..` to `![alt](../../path)` and breaks paths. Use `![[figure.svg|caption]]`; Obsidian resolves by walking the vault.
3. **Widget slug is the lowercase filename stem.** For `Slope_Intercept_Form.md` the widget is `<div class="problem-vault-widget" data-topic-slug="slope_intercept_form">` and the generator uses `topic_slug = "slope_intercept_form"`.
4. **A page's `aliases:` list must never contain its own filename stem.** Alias=filename creates an alias-redirect HTML that overwrites the canonical page with a blank redirect stub — the page turns into a blank white page in production. Hit twice so far: Vault.md (Phase 1) and Precalculus.md (Phase 2). Every time you touch a hub file's frontmatter, double-check the aliases line.
5. **Quote all hash tags in YAML:** `tags: ["#branch-algebra-1"]`. Unquoted `#` starts a comment.
6. **All tags must exist in `wiki/_tag_taxonomy.md`.** Lint catches ad-hoc tags. No inventing new tags without editing the taxonomy first.
7. **Run `yaml.safe_load()` after every batch write.** `factory/scripts/validate_yaml.py` catches unescaped quotes, backslash artifacts, and regex-breakage. CI runs it on every push.

### Generator authoring rules

8. **Parameter space needs ≥30 unique problems per difficulty** or set `bank_count_per_difficulty = N`.
9. **Backward construction beats forward.** Pick the answer first (integer roots, Pythagorean triples, clean unit-circle values), derive the parameters. Forward construction with retries can infinite-loop on edge cases.
10. **Use `sp.latex(sp.Eq(...))` for signed equations** — handles negative coefficients correctly where string formatting does not.
11. **Named tags, not freehand.** Use `#skill-algebraic-manipulation`, `#skill-visualization`, `#word-problem-support` etc. from the taxonomy.

### Process rules

12. **Don't trust write retries.** If a file write fails and you retry with a different name, **check for dead siblings** afterward. Lost an hour in Cluster 2 to two orphaned generator files sitting next to the real ones.
13. **`py -3` on Windows.** Not `python`, not `python3`.
14. **`builds/*/raw/` is gitignored.** The 62 MB of textbook source stays local by design. Don't try to `git rm` it.
15. **CI runs pytest + validate_yaml + build_index before Quartz.** A broken test fails the deploy. Fix local before pushing.
16. **Rewrite the hub script before deleting old hubs.** Cluster 10 planning caught this: `update_course_hubs.py` must exist and point at the new hub filenames before you delete `Algebra_Overview.md` etc. Otherwise the old script errors or silently no-ops.
17. **Breadcrumb sweeps touch every topic file.** A breadcrumb rewrite script needs `--dry-run` mode and a unified-diff preview before execution. One bad regex and every topic's navigation breaks. Phase 1's `rewrite_breadcrumbs.py` is the template.

### Copyright discipline (8 clusters' worth of forbidden idioms)

The copyright pytest caught many near-misses across clusters. These are the **textbook phrasings that reliably collide with 15-word shingles** in the source corpus — avoid them in future content:

- Problem statement starters: don't use "Find the equation of the line...", "Write the equation of the line with slope...", "Solve the equation...", "Evaluate..." as bare openers. Use "Give...", "Determine...", "What is...", "Compute...", "Find all real solutions to...", "Express...".
- Definitional phrasings: "an identity is an equation that is true for every angle", "a rational function is a quotient of polynomials", "a sequence is an ordered list of numbers", "a complex number is a number of the form a + bi where a and b are real", "a matrix is a rectangular array of numbers", "the hypotenuse is always opposite the right angle", "in an arithmetic sequence, each term is obtained by adding a constant", "multiply every term on both sides by the LCD" — all rephrase.
- Theorem openers: "The Law of Sines states that...", "The Pythagorean theorem states that...", "De Moivre's theorem states that..." — paraphrase the content.
- "(also called ...)" parenthetical for synonyms — use an em-dash aside instead: "— sometimes called a —".
- Idiomatic step phrases: "take the log of both sides", "take the root first and then raise to the power", "check for extraneous solutions", "equals the sum of the two remote interior angles", "group the first two terms and the last two terms", "collect the terms on the left and the constants on the right", "the parabola opens to the right because p > 0", "every positive number has two square roots", "the midpoint of the segment joining the foci".
- Word-problem scenarios: don't reuse textbook scenarios verbatim (Alice/Bob working together, a ball thrown upward, a taxi fare, a PortaBoy). Invent fresh names and contexts.

When a new content agent is dispatched, include this list in its prompt so it avoids the traps proactively.

---

## Navigation Design

Math_Wiki uses Quartz v4's three-pane layout with wiki-specific overrides.

### Layout zones

```
┌──────────────────────────────────────────────────────┐
│ header (empty)                                       │
├──────────┬──────────────────────────┬────────────────┤
│ LEFT     │ MAIN (article body)      │ RIGHT          │
│ Explorer │                          │ Graph, TOC,    │
│ sidebar  │                          │ Backlinks      │
├──────────┴──────────────────────────┴────────────────┤
│ afterBody: ProblemVaultWidget + VaultViewer          │
│            (mount only if hook div present)          │
│ footer: "All Wikis" + "Source" links                 │
└──────────────────────────────────────────────────────┘
```

### Left sidebar Explorer

`mathExplorerFilter` HIDES large collections (`topics/` ≈239 pages, `problem_types/`) and empty-shell folders (`entities/`, `synthesis/`, `techniques/`, `sources/`) plus underscore-prefixed internal files except `_overview`. `mathExplorerMap` rewrites remaining entries to emoji-prefixed friendly labels:

| Label | Target |
|---|---|
| 🏠 Home | `_overview.md` |
| 🔢 Middle School Math | `Middle_School_Math.md` |
| 📗 Algebra 1 | `Algebra_1.md` |
| 📕 Geometry | `Geometry.md` |
| 📙 Algebra 2 | `Algebra_2.md` |
| 📓 Pre-Calculus & Trig | `Precalculus.md` |
| 📖 All Topics | `Topics_Overview.md` |
| 🎒 Your Vault | `Vault.md` |
| 📊 Progress | `Topic_Status.md` |
| 🧮 Formulas | `Formulas_Overview.md` |

**Ten sidebar entries, course-first.** A middle schooler clicks 🔢 Middle School Math. A sophomore clicks 📕 Geometry or 📙 Algebra 2. A pre-calc student clicks 📓 Pre-Calculus & Trig. Everything under `topics/` is reachable via course hubs, search, and wikilinks only. The old branch hubs (`Algebra_Overview`, `Geometry_Overview`, `Trigonometry_Overview`, `Precalculus_Overview`) and empty-shell overviews (`Sources_Overview`, `Entities_Overview`, `Synthesis_Overview`, `Techniques_Overview`, `Problem_Types_Overview`) were deleted during the Phase 1 standalone conversion.

### Right sidebar (content pages)

1. **Graph view** — `localGraph.depth=1` (avoids visual overload on heavily-linked topics)
2. **TableOfContents** (desktop only)
3. **Backlinks**

### Topic page skeleton

```markdown
---
title: "{Title}"
type: topic
aliases: []
tags: ["#branch-{name}", "#topic-{area}", ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_refs: [{book: "...", chapter: "...", section: "..."}, ...]
related: [...]
status: draft | complete
confidence: high | medium | low
branch: pre-algebra | algebra-1 | algebra-2 | pre-calculus | geometry
prerequisites: [...]
problem_type_ids: []
figures: []    # or ["branch/figure.svg"]
summary: "one-sentence hook"
---

> [[_overview|Home]] > [[{Course_Hub}|{Course Label}]] > {Title}

# {Title}

{Intuition paragraph — 2-4 sentences, plain language}

{Optional: ![[figure.svg|caption]]}

---

## {Key ideas / Why it works / Key form in display math}

---

## Example 1 / 2 / 3 (three required, YOUR numbers, YOUR scenarios)

---

## Common pitfalls

- 3-4 bullets

---

## Prerequisites

- [[Slug]] — reason

---

## Problems Involving {Topic}

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="{lowercase_slug}"></div>

---

## See Also

- [[Peer_Topic_1]]
- [[Peer_Topic_2]]
- [[Algebra_1|Algebra 1]]   # or whichever course this topic belongs to
- [[Topics_Overview]]
- [[_overview|Home]]
```

**Do NOT include "Practice generators for this topic are coming in a future wave" lines.** Every live topic has live generators, and every stub is a scaffold to enrich later, not a waiting room for a future cluster wave.

### Course hub structure

Hand-written intro paragraph + suggested learning path + `<!-- AUTO:TOPICS:BEGIN/END -->` block regenerated by `tools/update_course_hubs.py`. The auto block walks `wiki/topics/**/*.md`, reads each file's `branch:` frontmatter, groups by the five course hubs, and uses `wiki/_data/problem_types_index.json` to split each course's topic list into a flat "🟢 Live topics" section and a collapsed `<details>` "⚪ Stub topic(s)" section. The Geometry hub additionally pulls in an explicit allowlist of geometry-adjacent pre-algebra slugs (`GEOMETRY_ADJACENT_ALLOWLIST` in the script).

### Landing page (`wiki/_overview.md`) structure

```
# Math Wiki
<tagline + stats row: N live topics · M generators · P verified problems>
<privacy note: vault is browser-local>

## Start Here
- Five course hub cards (Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calc & Trig)
- Topics_Overview link for alphabetical index

## How to Use This Wiki
<5-step guide: pick course, read lesson, add to vault, review, repeat>

## Live Learning Paths
<16 curated topic threads that cross course boundaries>

## Your Tools
- Vault, Topic_Status, Topics_Overview, Formulas_Overview

## About
<audience, render tech, privacy, license, repo>
```

Stats numbers are updated by hand after each content cluster. The tagline + stats row is right below the `# Math Wiki` heading.

---

## Conventions Cheat Sheet

- **Topic filenames:** `Title_With_Underscores.md` (Title Case, underscores). Frontmatter `title:` uses spaces.
- **Widget mount slug:** lowercase of the filename stem. Must match `topic_slug` in the generator.
- **Generator IDs:** `snake_case` descriptive verb phrase (`one_step_eq_add`, `slope_from_two_points`).
- **Formula titles:** Title Case of the named formula (`Quadratic_Formula.md`, `Pythagorean_Theorem.md`).
- **LaTeX:** Inline `$...$`. Display `$$\n...\n$$` on separate lines. KaTeX-compatible only.
- **Tags:** Quoted in YAML (`tags: ["#branch-algebra-1"]`). Must exist in `wiki/_tag_taxonomy.md`.
- **Tone:** Warm, tutor-adjacent, intuition first, formal second. Assume a smart student who's learning.
- **Generator coverage standard:** **Minimum 3 generators per topic.** Generators must span the span of variants (e.g., Slope: from-two-points, from-equation, classify, parallel/perpendicular).
- **Cross-linking:** Every `status: draft|complete` topic has ≥3 `prerequisites` and ≥3 `related`/see-also wikilinks. Scored by `topic_status.py`.
- **Backward construction everywhere** in generators. Pick the answer, derive the parameters.
- **External links:** `<a target="_blank" rel="noopener">` for YouTube, Desmos, etc.

---

## Remaining Work

Most of the roadmap items from earlier versions of this spec are now shipped. What's left:

### Deferred Vault polish

These were in scope for Phase 5 but deferred for a future session. They ride on existing Vault infrastructure so they do not need new data pipelines.

1. **Custom worksheet builder** — dedicated page where the student picks N topics × difficulty × count → mixed worksheet. New Quartz component, new `wiki/Worksheet_Builder.md` page. Can reuse `ProblemVaultWidget`'s shard fetch logic.
2. **jsPDF polished PDF export** — replace `@media print` with a KaTeX-rendered-canvas → PDF pipeline for consistent cross-browser output. Import jsPDF via CDN singleton, mirror `ensureKatex()` pattern.
3. **Input-and-check answer grader** — string matching on normalized LaTeX handles ~80% of cases; Pyodide SymPy handles the rest if the 5 MB load cost is acceptable.
4. **Difficulty auto-tune** — track per-generator correct/incorrect in localStorage, suggest the next difficulty.

### Future content expansion

~98 auto-stubs still live on disk — secondary catalog entries that were not in any cluster's scope. Activating one is the normal loop:

1. Write the content following the topic skeleton below (the existing stub file is fine to overwrite).
2. Add 3+ generators under the appropriate branch package, imported in that package's `__init__.py`.
3. `build_problem_bank.py` → `topic_status.py` → `update_course_hubs.py` → `build_prereq_graph.py` → commit → push.

Cluster 10's pattern (enrich several pre-algebra geometry stubs while creating new HS-branch geometry topics) is a good template for future geometry/measurement work — enriching an existing stub surfaces it in both Middle School Math and Geometry course hubs for the cost of one file.

### Adding a whole new textbook

1. Drop the book's LaTeX tree under `raw/books/new_book/`.
2. Write an `env_map` in `tools/ingest_math_book.py` (see env_map Author's Guide below).
3. `py -3 tools/ingest_new_book.py --slug new_book --dry-run`. Review output.
4. `py -3 tools/ingest_new_book.py --slug new_book`. This runs every pipeline stage and snapshots the catalog before/after.
5. Review `tools/aliases.yaml` for duplicate topics with existing books. Add merge rules where titles are functionally identical but normalization didn't match.
6. `py -3 tools/consolidate_extractions.py` again to apply the merges.

The synthetic `raw/books/book_test/` fixture + `generators/tests/test_ingest_smoke.py` guarantees the pipeline survives code changes — run pytest after any tooling edits.

---

## env_map Author's Guide

To ingest a textbook that doesn't use the Curriculum Factory or Stitz-Zeager conventions, teach `ingest_math_book.py` the new book's blocks.

### Step 1: survey the source

Open a few section `.tex` files from the new book and list every `\begin{env}...\end{env}` you see. Typical environments:

| LaTeX env | Usual meaning | Canonical kind |
|---|---|---|
| `definition` / `defn` / `keyterm` | A defined term | `definition` |
| `theorem` / `thm` | A provable statement | `theorem` |
| `corollary` / `cor` | A direct consequence | `corollary` |
| `property` / `rule` | An identity or manipulation rule | `property` |
| `example` / `ex` / `problem` | A worked example | `example` |
| `exercise` / `checkpoint` / `practice` | Try-it-yourself problems | `checkpoint` |
| `equation` / `eqn` / `display` | Labeled display equation | `equation` |
| `note` / `remark` | Editorial note | `note` |
| `caution` / `warning` | Pitfall callout | `caution` |
| `figure` / `fig` | A figure caption block | `figure` |

### Step 2: write the env_map

```python
# In tools/ingest_math_book.py, next to CURRICULUM_ENVS / STITZ_ENVS:
NEWBOOK_ENVS = {
    "definition": "definition",
    "theorem":    "theorem",
    "example":    "example",
    "remark":     "note",
    "exercise":   "checkpoint",
    "figure":     "figure",
}
```

Unknown environments are silently ignored. Only list what you want extracted.

### Step 3: register the book

```python
BOOKS["new_book"] = BookSpec(
    slug="new_book",
    title="New Textbook Title",
    branch_hint="algebra-1",
    root_dir=BOOKS_DIR / "new_book",
    layout="chapters",    # or "topicfolders" for Stitz-Zeager style
    env_map=NEWBOOK_ENVS,
)
```

### Step 4: verify layout

Two layouts supported:

- **`chapters`** (Curriculum Factory): `chapters/ch01/chapter.tex` + `chapters/ch01/sections/sec01.tex`, ...
- **`topicfolders`** (Stitz-Zeager): topic folders like `LinearQuadratic/` with multiple `.tex` sections. Add a new `BOOK{N}_CHAPTER_FOLDERS` list and a branch in `parse_topicfolder_layout_book`.

### Step 5: guided ingest

```bash
py -3 tools/ingest_new_book.py --slug new_book --dry-run
py -3 tools/ingest_new_book.py --slug new_book
```

### Step 6: propose merges in `tools/aliases.yaml`

```yaml
merges:
  - from: ["New_Book_Slug", "Existing_Slug"]
    into: "Existing_Slug"
    rationale: "Same topic; new book's section title wasn't normalized identically"
```

Then `py -3 tools/consolidate_extractions.py` to apply.

---

## Session Patterns That Worked

Cluster-shipping and feature-shipping patterns that have been validated across 10 clusters, Phase 1 nav redesign, and Phase 4-5 widget work. Session-scale summary lives in the Recent Session History section below; this section is the concrete checklist.

### Sub-agent prompt template

Every content or generator sub-agent prompt must include:

1. The exact file paths to read (for content: existing stub or new path; for generators: new module path).
2. 2-3 gold-standard files to imitate for structure (`Circles.md`, `The_Distributive_Property.md`, and one recent example from the same branch).
3. The structural template verbatim (frontmatter + sections + widget div).
4. The forbidden-idiom list (see Gotchas section above).
5. The current valid-tags list from `_tag_taxonomy.md` (inlined, not referenced — agents do not always fetch files from references).
6. The current live-topics list to cross-reference in `related:` and See Also — prevents dead-wikilink drift.
7. Hard constraints: word count floors, YAML rules, LaTeX rules, widget slug rule.
8. Explicit "Do NOT include 'Practice generators are coming in Cluster X'" — every live topic has live generators now.
9. A short process list ending in a brief return summary.

### Validation cadence after a batch

```bash
py -3 -m pytest generators/tests/test_copyright_safety.py -q
py -3 ../../factory/scripts/validate_yaml.py wiki/
py -3 ../../factory/scripts/lint_wiki.py wiki/
```

Expected: 3 pytest passes, 263/263 YAML clean, 0 lint errors. If you get copyright hits, grep for the flagged phrase across `wiki/topics/` to find all occurrences, then do 1-line rewrites.

### What NOT to do

- **Don't** skip the gold-standard read in content prompts. Agents told to "match The_Distributive_Property.md" produce consistently better prose than agents given a bare template.
- **Don't** trust a single copyright pass. Run the shingle test, fix, run again — rewriting one idiom sometimes surfaces a previously-masked neighbor.
- **Don't** commit a cluster with dead wikilinks. Lint catches them, but only after Quartz has already rendered them wrong in production if you push too fast.
- **Don't** invent new tags. Every new tag needs to be added to `_tag_taxonomy.md` first.
- **Don't** forget `py -3 tools/update_course_hubs.py` after adding live topics. The course hub "AUTO:TOPICS" block is stale otherwise.
- **Don't** forget `py -3 tools/build_prereq_graph.py` after touching `prerequisites:` frontmatter. The PrereqWidget card is stale otherwise.
- **Don't** ship a cluster without updating `_overview.md`'s Learning Paths and `Topics_Overview.md`'s Live Topics sections. These are the student-facing front doors.

---

## Deployment

- **Repo:** `JD-Jones-ASES/Wiki-Factory`
- **URL:** https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/
- **Build time:** ~2 minutes for ~260 pages including overlay + Quartz build
- **CI workflow:** `.github/workflows/deploy.yml` (shared with Hymn Wiki). Runs pytest + validate_yaml + build_index, then clones Quartz v4 fresh, overlays `quartz.config.ts` / `quartz.layout.ts` / `quartz_components/` / `static/` from the build root, copies `wiki/*` into `content/`, runs `npx quartz build`, deploys. Overlays are directory-existence-guarded so Hymn Wiki's build is unaffected.
- **Per-build Quartz settings:** `enableSPA: false`, `Plugin.Latex({ renderEngine: "katex" })`, Explorer `filterFn` hides `topics/` + `problem_types/` + empty-shell folders, `localGraph.depth: 1`.

### Custom components loaded in layout

```typescript
// quartz.layout.ts (abbreviated)
import ProblemVaultWidget from "./quartz/components/ProblemVaultWidget"
import VaultViewer from "./quartz/components/VaultViewer"
import PrereqWidget from "./quartz/components/PrereqWidget"

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [ProblemVaultWidget(), VaultViewer(), PrereqWidget()], // each early-returns if mount absent
  footer: Component.Footer({ ... }),
}
```

---

## Recent Session History (Compressed)

Full cluster-by-cluster detail lives in git history. This section keeps forward-looking lessons future sessions can skim quickly.

### Versions 2.0 → 2.2 — from content buildout to student-first wiki

**v2.0.0 (Clusters 0-9, content buildout).** Nine clusters shipped in a single multi-day session. Wiki grew from 36 live topics to 136, from 9,621 problems to 32,698. Infrastructure (copyright pytest, YAML validator, topic status dashboard, alias merge pipeline, ingest smoke test) was laid down in Cluster 0 and paid off for every subsequent cluster — most shipped green on first validation after small idiom fixes.

**v2.1.0 (Phase 1, standalone + course nav).** Replaced 4 branch hubs with 5 course hubs (Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus & Trig). Purged source-book boilerplate from 133 stub topic files. Rewrote breadcrumbs in 239 topic files in a single sweep. Deleted 9 empty-shell overviews. Trimmed the sidebar from 14 to 10 entries. `tools/update_course_hubs.py` replaces `update_branch_hubs.py`; uses a `GEOMETRY_ADJACENT_ALLOWLIST` second pass so pre-algebra geometry topics surface in both hubs.

**v2.2.0 (Cluster 10 + Phase 4 + Phase 5a, previous session).** Cluster 10 shipped 10 new HS Geometry topic pages + enriched 6 pre-algebra geometry stubs + 50 new generators in 10 modules + 14 new figures. Executed by 4 parallel sub-agents (2 content, 1 generators, 1 figures) with zero first-pass copyright hits. PrereqWidget shipped: `tools/build_prereq_graph.py` writes `wiki/_data/prereq_graph.json` from YAML frontmatter (400 edges across 137 topics); `quartz_components/PrereqWidget.tsx` injects a "Review these first" card into the right sidebar on topic pages. Vault gained JSON export/import buttons via a bump to `vaultViewer.inline.ts`. Geometry branch score jumped from 47.5 to 82.7.

**v2.3.0 (Test-Prep Phase, this session).** Shipped in four commits over one session:
- **Nav fix (commit `3aa7986`):** `wiki/Precalculus.md` had `"Precalculus"` in its `aliases:` list. Quartz's `AliasRedirects` plugin generated a self-redirect HTML that overwrote the canonical hub, serving blank. Same bug class as the Vault.md fix. 1-token deletion; Gotcha #4 generalized to "never put the filename in aliases."
- **Test tagging (commit `c8e855e`):** new `tools/test_prep_mapping.yaml` (150 slugs -> 209 by phase end) + new `tools/apply_test_tags.py` (idempotent, surgical, --dry-run / --check modes). Added Section 7 `#test-sat/#test-psat/#test-act/#test-clt` to `_tag_taxonomy.md`. No lint_wiki.py changes (it reads taxonomy dynamically via regex). Auto-generated Quartz tag index pages `/tags/test-*` become de-facto per-exam hubs with zero custom authoring.
- **Stub activation (commits `1933ef0` Wave A, `6e0994a` Wave B, `1d8dd3d` Wave C):** 63 stubs activated across 3 branches. Wave A (pre-algebra, 22 stubs) pushed branch avg 45.4 -> 61.1. Wave B (algebra, 25 stubs) pushed 58.1 -> 73.7. Wave C (precalc, 16 stubs) pushed 54.4 -> 82.1 (biggest per-branch jump). Each wave = 3-4 content + 2 generator + 1 figure sub-agents in parallel.
- **New gap topics (commit `b891393` Wave D):** 10 brand-new topic pages filling identified test-prep gaps (Piecewise_Functions, Conditional_Probability, Permutations_And_Combinations, Normal_Distribution, Margin_Of_Error, Expected_Value, Binomial_Probability, Sampling_Methods_And_Bias, Histograms_And_Box_Plots, Correlation_And_Residuals). 30 new generators + 6 new figures. Wave D first-pass copyright-clean.
- **Net delta:** 144 -> 210 live topics (+66), 460 -> 638 generators (+178), 36,010 -> 49,443 problems (+13,433), 45 -> 62 figures (+17), 112 -> 51 stubs (-61). Overall avg 53.9 -> 71.6.

### Forbidden-idiom additions shipped this phase

Phase 2-3 content reviews added ~15 more near-verbatim textbook phrasings to the banned list (the `hits[:3]` truncation in the copyright test masks subsequent hits, so each pass typically surfaces a new ring). Key adds:

- **Pre-algebra foundations:** "the absolute value of a number is its distance from zero", "a rational number is any number that can be written as a fraction", "every whole number greater than 1 can be written as a product of primes in exactly one way", "every point on the number line corresponds to exactly one real number", "the greatest common factor of two or more whole numbers is the", "the least common multiple of two or more whole numbers is the", "a prime is a whole number greater than 1 whose only factors are", "the principal (the original amount) is the annual interest rate as a decimal", "the bill comes to ... how much is the tip and what is the total"
- **Algebra 1 / 2:** "a number is in scientific notation when it is written as", "an algebraic expression is any combination of variables constants and operations", "two numbers whose product is and whose sum is", "less than ... greater than ... on the number line is farther to the left", "strict less than strict greater than less than or equal to greater than or equal to", "multiplying or dividing both sides by a negative number reflects every real number", "slope is rise over run, not run over rise", "the part is X, the percent is Y, and the whole is the unknown", "the leading coefficient ... multiply the leading coefficient by the constant. Now find two numbers whose product is ... and whose sum is"
- **Algebra/Precalc (surfaced in Wave C/D subagent guidance):** "a polynomial function is of the form", "a rational function is a quotient of two polynomials", "vertical asymptotes occur where the denominator is zero", "a function is a relation that assigns exactly one output to each input", "a graph of an equation is the set of all points whose coordinates satisfy the equation"

Include these in every future content-agent prompt alongside the original Cluster-0-through-9 forbidden list.

### What works at session scale (proven across 3 versions)

- **Parallel sub-agent dispatch** (3-4 content + 2-3 generators + 1 figures per cluster) sustains ~15 topics per cluster without review-burden collapse. Four agents in one message with no file-overlap works cleanly.
- **Backward construction for all generators** eliminates guess-and-check infinite loops. Pick the answer, derive the parameters.
- **Forbidden-idiom list in every content prompt.** By Cluster 10, first-pass copyright hits dropped to zero. The list keeps growing — see the Gotchas section.
- **Enrich-and-create hybrid** (Cluster 10 pattern): when planning a new cluster, check for existing auto-stubs whose titles match your intended content. Enriching a stub is cheaper than creating a new file, and an enriched pre-algebra stub surfaces in two course hubs (Middle School Math + the relevant HS course) via the allowlist.
- **Single 136-file sweep for nav changes.** Phase 1 proved that breadcrumb rewrites + source purges should be batched into one sweep over topic files, not two.
- **Gold-standard read first.** Every content sub-agent prompt starts with "read these 3 files and match their tone." Agents trained to imitate a specific file produce consistently better prose than agents given a bare template.

### What to watch

- **Dead wikilink drift** when agents invent topic names. Lint catches them, but pre-seeding every agent prompt with the current live-topics list prevents them.
- **Tag taxonomy drift.** Same prevention: include the actual taxonomy contents in agent prompts, not just a reference to the file.
- **Shard size budget.** Every shard stays under 320 KB today. If a generator goes over, prefer reducing `bank_count_per_difficulty` over raising the cap.
- **Hub script rewrite order.** Rewrite `update_course_hubs.py` (or its successor) BEFORE deleting any old hub files it references — or the script will error or silently no-op.

### What to do first in a next session

1. Run the four sanity-check commands at the top of this file. Confirm all green.
2. `gh run list --limit 3` — confirm the last CI runs are all green.
3. Read `wiki/Topic_Status.md` for the current distribution. No live topic should score below 80; any outlier probably needs a figure, an example, or a cross-link bump.
4. Pick one from **Remaining Work** (custom worksheet builder, jsPDF PDF export, input-and-check grader, difficulty auto-tune, new textbook ingest, stub activation wave) and ship it. Follow the Session Patterns section — parallel sub-agents for anything that can be split across files.

---

## Self-Improvement Protocol

This file self-improves with each session:

- **During iteration:** pitfalls get woven into relevant sections (not appended). Patterns that worked get reinforced with concrete examples. The spec gets shorter and more precise, not longer.
- **After a session:** roll up detailed cluster logs into the "Recent Session History" compression. Keep only the forward-looking lessons.
- **Measure improvement in compression, not accumulation.** This file was 1769 lines before the v2.0.0 refactor. It should stay under 1000 going forward unless there's a genuinely new architectural layer to document.

Future contributors: if you find yourself adding a section that doesn't answer a question a new-session you would ask, delete it or fold it into an existing section. This file is a context-boot for Claude, not a changelog.
