# Math_Wiki.md --- A Practice-First Math Wiki & Tutor
## From Pre-Algebra through Pre-Calculus, with procedurally generated practice
### Version 1.15.0 --- 9-CLUSTER PLAN COMPLETE. 136 live topics. 32,698 problems. (2026-04-11)

| Field | Value |
|-------|-------|
| **Domain** | Middle and High School Mathematics |
| **Scope** | Pre-Algebra, Algebra 1, Geometry, Algebra 2, Trigonometry, Pre-Calculus. Calculus & Statistics deferred (books don't cover them). |
| **Audience** | Students grades 6--12. Warm, encouraging, clear. Tutor-adjacent, not textbook-formal. |
| **Source count** | 5 textbooks (see Source Inventory below) |
| **Scale** | Live: 136 topics with working widgets, 410 generators, 32,698 verified problems. Catalog: 238 canonical topics (post-alias-merge). **9-cluster buildout plan complete.** |
| **Comprehensive buildout plan** | 9-cluster schedule; see "Buildout Plan" section below. |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD |
| **URL** | https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/ |

---

## Orientation for a New Session

**Read this file top to bottom before doing anything else.** It is the single source of truth for what exists, what works, and what's next.

### Where the session is right now

- **Cluster 0** (infrastructure + alias merge) — **shipped** commit `8c1b4ac`
- **Cluster 1** (pre-algebra foundations, 20 topics) — **shipped** commit `f27052f`
- **Navigation UI redesign** — shipped commit `a0f4c4f`
- **Cluster 2** (linear world completion, 14 topics) — **shipped** commit `49dfa00`
- **Cluster 3** (polynomials + quadratics deep, 14 topics) — **shipped** commit `bb768cc`
- **Cluster 4** (rationals & radicals, 12 topics) — **shipped** commit `a3db819`
- **Cluster 5** (functions & transformations, 14 topics) — **shipped** commit `bedee97`
- **Cluster 6** (exponentials & logarithms, 10 topics) — **shipped** commit `db5421c`
- **Cluster 7** (trigonometry, 15 topics) — **shipped** commit `c78a1f1`
- **Cluster 8** (sequences, probability, statistics, 9 topics) — **shipped** commit `710120f`
- **Cluster 9** (conics, matrices, complex numbers, 12 topics) — **shipped** (this version, **136 live topics, 32,698 problems**)
- **9-cluster plan complete.** Future work: L (lint/polish pass), more figures for existing pages, prereq-graph widget.

### 30-second mental model

Math_Wiki is a **practice-first wiki**. Every live topic page has (a) rich prose paraphrased from 5 source textbooks and (b) an interactive problem-vault widget fed by SymPy-verified Python generators. Students read, add problems to a browser-local Vault, and download worksheets. The site deploys to GitHub Pages via Quartz v4 on every push to main.

The 9-cluster buildout plan ships one topic cluster at a time (foundations → linear → quadratics → rationals → functions → exp/log → trig → seq/stats → conics). Each cluster delivers ~15 topics fully finished (content + generators + figures + cross-links).

### First things to run in a fresh session

```bash
cd builds/Math_Wiki

# 1. Sanity-check the project state (should all be green/clean)
py -3 -m pytest generators/tests/                   # 29/29 passing
py -3 tools/topic_status.py                         # see where we stand (baseline avg ~22/100)
py -3 ../../factory/scripts/validate_yaml.py wiki/  # 257/257 clean
py -3 ../../factory/scripts/lint_wiki.py wiki/      # 0 errors

# 2. Skim this file, especially:
#    - "Current Status" table (what's live now)
#    - "Buildout Plan" table (what cluster is next)
#    - "Navigation Design" section (how the UI serves students)
#    - "Self-Improvement Log" top entry (most recent session's lessons)
```

### All the other useful commands

All commands run from `builds/Math_Wiki/`:

```bash
cd builds/Math_Wiki

# Rebuild the problem bank from generators (idempotent)
py -3 tools/build_problem_bank.py

# Regenerate branch hub live/stub topic lists (reads problem_types_index.json)
py -3 tools/update_branch_hubs.py

# Regenerate matplotlib figures
py -3 tools/generate_figures.py

# Re-parse books from LaTeX source (destructive: overwrites raw/extractions/)
py -3 tools/ingest_math_book.py --all

# Re-build catalog from extractions + apply tools/aliases.yaml
# (destructive: overwrites raw/catalog/)
py -3 tools/consolidate_extractions.py

# Ingest a NEW textbook end-to-end (dry-run first)
py -3 tools/ingest_new_book.py --slug <new_book_slug> --dry-run
py -3 tools/ingest_new_book.py --slug <new_book_slug>

# Generate new stub pages for any catalog topics that don't already have one
py -3 tools/generate_topic_stubs.py --branch all
py -3 tools/generate_topic_stubs.py --branch all --force   # overwrite existing stubs
```

### Where things live

| Path | What |
|---|---|
| `raw/books/{math_1,math_2,algebra_1,algebra_2,algtrig}/` | Original LaTeX source (gitignored, ~62 MB) |
| `raw/extractions/{book_slug}/chapter_NN.json` | Per-chapter parsed blocks (gitignored, ~3.4 MB) |
| `raw/catalog/topics_{branch}.json` | Per-branch canonical topic catalog |
| `raw/catalog/index.json` | Catalog summary with counts by branch |
| `wiki/_overview.md` | Landing page (hero + learning paths + cluster status) |
| `wiki/Topics_Overview.md` | All live topics grouped by branch + sub-category |
| `wiki/Topic_Status.md` | Auto-generated progress dashboard (regen with `topic_status.py`) |
| `wiki/Vault.md` | Interactive vault page (mounts VaultViewer) |
| `wiki/{Algebra,Precalculus,Geometry,Trigonometry}_Overview.md` | Branch hubs (hand intro + AUTO:TOPICS live/stub block) |
| `wiki/topics/{pre_algebra,algebra,precalculus,geometry}/` | Topic pages (auto-stubs + enriched lesson pages) |
| `wiki/formulas/` | Formula pages (currently just Pythagorean_Theorem stub) |
| `wiki/_data/problem_types_index.json` | Widget lookup: topic_slug → [generators] (drives live/stub classification) |
| `wiki/_data/problems/{topic_slug}.json` | Per-topic problem shards (committed) |
| `wiki/_data/topic_status.json` | Per-topic metrics from `topic_status.py` (CI artifact) |
| `wiki/assets/figures/{branch}/` | Matplotlib SVGs |
| `quartz.config.ts` | Quartz v4 site config (pageTitle, baseUrl, plugins) |
| `quartz.layout.ts` | Layout component ordering, Explorer filter/map, widget mounts |
| `generators/{pre_algebra,algebra,geometry}/*.py` | Python generator modules |
| `generators/base.py` | Problem dataclass, Generator ABC, `@register`, `all_generators()` |
| `generators/tests/test_circles.py` | Parametrized test suite (tests every registered generator) |
| `quartz_components/*.tsx, *.inline.ts, *.scss` | Custom widgets overlaid into Quartz during CI |
| `tools/` | Build scripts (ingest, consolidate, stub gen, bank build, figures, hub update) |
| `pyproject.toml` | pytest config (pythonpath=["."]) |

---

## Current Status (2026-04-10, end of Cluster 0)

**Cluster 0 ships the infrastructure that every cluster 1-9 depends on.**
No new topics or generators — this is the hardening pass.

### Cluster 0 deliverables (new in this session)

- **`tools/aliases.yaml`** — version-controlled alias merge rules applied by
  `consolidate_extractions.py`. Starts empty; populated in the X pass.
- **`tools/consolidate_extractions.py`** — now accepts `extractions_dir` kwarg
  and applies `apply_aliases()` (renames/merges/splits) before sharding.
- **`tools/topic_status.py`** — progress dashboard. Writes
  `wiki/_data/topic_status.json` + `wiki/Topic_Status.md`. Scores every
  topic 0-100 against the plan's per-cluster verification rules.
- **`tools/ingest_new_book.py`** — end-to-end guided pipeline for adding
  a new textbook. Dry-run supported. Replaces ad-hoc ingest documentation.
- **`generators/tests/test_consolidate_snapshot.py`** — catalog snapshot
  test (fixture under `generators/tests/fixtures/mini_extractions/`) plus
  tests for every alias operation (rename, merge, split, conflict).
- **`generators/tests/test_copyright_safety.py`** — shingle-based verbatim
  detection. Builds 10-word shingles from every extraction block and
  scans published topic pages for 15-word runs. Auto-stubs are skipped
  (they echo source previews by design). An allowlist subtracts known
  definitional phrases from the corpus.
- **`generators/tests/test_ingest_smoke.py`** — synthetic book fixture
  under `generators/tests/fixtures/book_test/` runs through the full
  ingest -> consolidate -> stub pipeline end-to-end in pytest. This is
  the "future ingest preserved" guarantee.
- **`factory/scripts/build_index.py`** — extended with math page types
  (topic, formula, technique, problem_type) and grouped-by-letter output
  for large collections. Replaces 245 cosmetic "not in _index.md" warnings.
- **`factory/scripts/validate_yaml.py`** — new. YAML frontmatter sanity
  checker: type/status/tags validation + `yaml.safe_load()` on every
  modified page. Runnable as a pre-commit hook OR in CI.
- **`factory/scripts/add_navigation.py`** — multi-wiki hub resolution.
  Candidate hub stems per subdir; first existing file wins. Fixes the
  Hymn Wiki / Math Wiki entities/People hub collision.
- **`.github/workflows/deploy.yml`** — now runs `pytest`, `validate_yaml`,
  and `build_index` on every push before Quartz build.

### Gate checks after Cluster 0

- **Pytest:** 29 passing (8 generators + 10 consolidate-snapshot + 3 copyright + 8 smoke)
- **Lint:** 0 errors, 0 warnings, 1 info (stub count)
- **Topic status:** 247 topics, avg score 16.2 / 100 (baseline; Cluster 1 bumps it)
- **Catalog:** 246 topics (unchanged; alias merge pass pending in X)
- **CI:** green on every commit

### What's live on GitHub Pages

**16 topics with working interactive widgets:**

| Branch | Topic | Generators |
|---|---|---|
| Geometry | Circles | 5 |
| Algebra 1 | One-Step Equations | 4 |
| Algebra 1 | Multi-Step Equations | 3 |
| Algebra 1 | Slope | 4 |
| Algebra 1 | The Quadratic Formula | 3 |
| Algebra 1 | Factoring Trinomials (Leading Coefficient 1) | 3 |
| Algebra 1 | Solving Systems by Substitution | 2 |
| Algebra 1 | Solving Systems by Elimination | 2 |
| Algebra 1 | Absolute Value Equations | 3 |
| Algebra 1 | Properties of Exponents | 3 |
| Pre-Algebra | Order of Operations | 3 |
| Pre-Algebra | Adding and Subtracting Integers | 3 |
| Pre-Algebra | Finding a Percent of a Number | 3 |
| Pre-Algebra | Percent Increase and Decrease | 3 |
| Pre-Algebra | Slope-Intercept Form | 3 |
| Pre-Algebra | The Pythagorean Theorem | 3 |
| **Total** | **16 topics** | **50 generators** |

**Auto-generated stub pages (browseable, but widgets show "no problem types yet"):**
- 92 pages in `wiki/topics/pre_algebra/`
- 98 pages in `wiki/topics/algebra/` (combines algebra-1 + algebra-2)
- 55 pages in `wiki/topics/precalculus/`
- 2 pages in `wiki/topics/geometry/` (Circles + Coordinate_Plane)
- **247 topic pages total**; 16 have generators, **231 do not**

### Bank size health

| File | Size | Budget (500 KB) |
|---|---|---|
| Largest shard (`circles.json`) | 313 KB | ✅ |
| All other shards | 153-283 KB | ✅ |
| `problem_types_index.json` | 29 KB | tiny |
| **Total bank** | 3.1 MB across 16 shards | |

### Git state

- Phase 2c Wave 3 (`2935342`, `8f54c32`, `5bfcd60`) committed and pushed.
- Cluster 0 infrastructure pending commit at end of this session.

### Commit history (through Phase 2c Wave 3)

| Commit | Phase | What |
|---|---|---|
| `888e610` | Phase 0 | Scaffold: factory schemas, build dir, Quartz config, overview stubs |
| `baa6c66` | Phase 1 | Circles vertical slice: 5 generators, widgets, first deploy |
| `215c644` | Fix | Display math single-line `$$` → multi-line |
| `70bad13` | Fix | Vault page 404 (alias-vs-filename collision) |
| `ea19019` | Fix | Figure embed via Obsidian `![[]]` syntax + runtime KaTeX loader |
| `9e57332` | Phase 2a | LaTeX parser, catalog, sharded bank, full-problem localStorage vault |
| `473d35b` | Phase 2b | 245 auto-generated topic stubs + branch hub listings |
| `7e142e8` | Phase 2c Wave 1 | +17 generators across 5 topics (+1455 problems) |
| `690f0d8` | Phase 2c Wave 2 | +14 generators across 5 topics (+1185 problems) |
| `2935342` | Phase 2c Wave 3 | +15 generators across 5 topics (+1245 problems) |
| `8f54c32` | Cleanup | Remove dead generator files from Wave 3 write-retry |
| `5bfcd60` | Doc | Update Math_Wiki.md end-of-session state |

---

## Architecture: What You Need to Know

### The four layers

```
[RAW BOOKS] ──→ [PARSED EXTRACTIONS] ──→ [CONSOLIDATED CATALOG] ──→ [WIKI PAGES]
   LaTeX           per-chapter JSON           per-branch JSON            markdown stubs
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

### Sharded problem bank

- `wiki/_data/problem_types_index.json` — small lookup (29 KB). Fetched by the widget on every topic page load. Maps `topic_slug` → list of `{generator_id, display_name, counts, supports_word_problems}`.
- `wiki/_data/problems/{topic_slug}.json` — per-topic shard, one file per topic. Fetched lazily on first "Add to Vault" click.
- Every shard stays under ~320 KB by default (30 problems per difficulty per generator, overridable via `bank_count_per_difficulty` class attribute).
- Compact JSON output (no indent, `ensure_ascii=False`) to minimize file size.

### LocalStorage-first vault

- When the student clicks "Add to Vault", `problemVaultWidget.inline.ts` fetches the topic shard, picks random problems, and writes **full problem objects** (including `statement_latex`, `answer_latex`, `hints`, `solution_steps_latex`) into `localStorage["math-wiki-vault"]`.
- The VaultViewer component on `/Vault` reads entries directly from localStorage. **It never fetches the bank.** The Vault page loads instantly with zero external fetches.
- Phase 1 stored only `{generator_id, problem_id}` references. Phase 2a refactored to store full problem objects. Legacy vault entries are detected and the user is prompted to clear them.

### Widget architecture

- Each topic page's markdown contains `<div class="problem-vault-widget" data-topic-slug="{slug_lower}"></div>`. The widget mount div is part of the page content.
- `ProblemVaultWidget.tsx` is a thin Quartz component that emits nothing server-side but registers:
  - `ProblemVaultWidget.css = style` — SCSS from `problemVaultWidget.scss`
  - `ProblemVaultWidget.afterDOMLoaded = script` — client JS from `problemVaultWidget.inline.ts`
- `quartz.layout.ts` imports both `ProblemVaultWidget` and `VaultViewer` via explicit relative paths (`./quartz/components/...`) so they work without editing Quartz's `components/index.ts`.
- The Quartz CI overlay in `.github/workflows/deploy.yml` copies `quartz_components/*` into `quartz/components/` before `npx quartz build`.

### Runtime KaTeX loader

Quartz's `Plugin.Latex({ renderEngine: "katex" })` ships **only** `katex.min.css` plus the `copy-tex` contrib JS. It does **NOT** ship `katex.min.js` (Quartz renders math server-side at build time). For dynamic widget content, we inject the KaTeX JS CDN on demand:

- `ensureKatex()` is a singleton in both `problemVaultWidget.inline.ts` and `vaultViewer.inline.ts`
- Uses `window.__mathWikiKatexLoad` to share the loading promise across components
- Injects `<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" data-math-wiki-katex="1">` once
- After KaTeX loads, `renderKatexIn(element)` walks text nodes and converts `$...$` and `$$...$$` into rendered spans/divs

### Base URL awareness

Widgets fetch data using `getMathWikiRoot()`, which parses `location.pathname` to find the `/Math_Wiki/` segment. This handles both local dev (`/Math_Wiki/...`) and production (`/Wiki-Factory/Math_Wiki/...`) without hardcoding.

---

## Source Inventory (as ingested)

All 5 books live under `builds/Math_Wiki/raw/books/` (gitignored). The originals are at `C:/Project_Launchpad/private/textbooks/` and `C:/Users/jdj32/Downloads/`; this build treats its own `raw/books/` copies as read-only.

| # | Slug | Book Title | Layout | Chapters | Blocks | Role |
|---|---|---|---|---|---|---|
| 1 | `math_1` | Math I | 9-chapter curriculum-factory layout | 9 | 642 | Middle school: whole numbers, integers, fractions, decimals, ratios, percents, intro algebra, basic geo/data |
| 2 | `math_2` | Math II | 9-chapter curriculum-factory layout | 9 | 527 | Middle school continuation: exponents, rationals, proportions, expressions, inequalities, measurement, Pythagoras, coordinate plane, functions/prob/stats |
| 3 | `algebra_1` | Algebra - The First Year (Student) | 9-chapter curriculum-factory layout | 9 | 431 | Foundations, equations, inequalities, linear functions, systems, exponents/polynomials, factoring, quadratics, rationals/radicals |
| 4 | `algebra_2` | Algebra - The Second Year (Student) | 9-chapter curriculum-factory layout | 9 | 638 | Sets/numbers, linear, quadratics, functions, polynomials, rationals, exp/log, transformations, conic sections |
| 5 | `algtrig` | Stitz-Zeager College Algebra & Trigonometry (Corrected 3rd Edition) | topic-folder layout | 11 | 498 | Pre-calc with trig: relations/functions, linear/quadratic, polynomials, rationals, further, exp/log, trig foundations, trig applications, sequences, conics, matrices |

**Total: 47 chapters, 2736 extracted blocks, ~3.4 MB of JSON extractions.**

### Environment conventions discovered

Books 1-4 share the "Curriculum Factory" convention:
- `keyterm` → definition
- `property` → property (rules/theorems)
- `example` → example
- `checkpoint` → practice checkpoint
- `note`, `caution`, `keyconcept`, `figure`

Book 5 uses AMS-theorem conventions:
- `defn` → definition
- `thm` → theorem
- `cor` → corollary
- `ex` → example
- `eqn` → equation

Both are handled by `tools/ingest_math_book.py` via per-book `env_map` attributes.

**Copyright constraint (mandatory for every ingest/generator author):**

> **NEVER reproduce problem text, worked examples, or extended prose verbatim from any source book.** Use source material as reference for *what* to teach. All practice problems come from SymPy-verified Python generators producing fresh problems. Copying is a hard failure and a legal risk.

---

## Canonical Catalog (raw/catalog/)

`tools/consolidate_extractions.py` merges per-book extractions by normalized section title into canonical topics. Current state:

| Branch | Topics | Catalog file | Size |
|---|---|---|---|
| pre-algebra | 92 | `topics_pre_algebra.json` | 468 KB |
| algebra-1 | 50 | `topics_algebra_1.json` | 232 KB |
| algebra-2 | 49 | `topics_algebra_2.json` | 297 KB |
| pre-calculus | 55 | `topics_pre_calculus.json` | 209 KB |
| **Total** | **246** | | |

The consolidation pass is intentionally conservative (exact normalized-title match only, no fuzzy merging) to avoid false positives. Each catalog entry contains:

```json
{
  "slug": "The_Quadratic_Formula",
  "canonical_title": "The Quadratic Formula",
  "aliases": [],
  "branch": "algebra-1",
  "sources": [{"book_slug": "...", "chapter_number": "...", "section_number": "...", "block_counts": {...}}],
  "definitions": [{"book": "...", "chapter": "...", "section": "...", "title": "...", "preview": "...", "body_length": ...}],
  "properties": [...],
  "theorems": [...],
  "examples": [...],
  "figures": [...],
  "checkpoints": [...],
  "notes": [...],
  "concepts": [...]
}
```

Full `body_latex` is **not** stored in the catalog (would blow past the 500 KB per-file budget). If a stub generator needs the full text of a block, it should fetch it from `raw/extractions/{book_slug}/chapter_NN.json` via the `book`/`chapter`/`section` fields.

---

## The Toolchain

| Tool | Purpose | Idempotent? |
|---|---|---|
| `tools/ingest_math_book.py` | Parse LaTeX source → per-chapter JSON shards | Yes (overwrites) |
| `tools/consolidate_extractions.py` | Merge extractions → per-branch catalog shards | Yes (overwrites) |
| `tools/generate_topic_stubs.py` | Catalog → wiki/topics/{branch}/*.md stubs | Yes; `--force` to overwrite |
| `tools/update_branch_hubs.py` | Regenerate `<!-- AUTO:TOPICS:BEGIN/END -->` blocks in hub pages | Yes |
| `tools/build_problem_bank.py` | Iterate generator registry → per-topic shards + index | Yes (cleans stale shards) |
| `tools/generate_figures.py` | Matplotlib → SVG figures in `wiki/assets/figures/` | Yes (overwrites) |

Factory-level tools (run from repo root):

| Tool | Purpose |
|---|---|
| `factory/scripts/lint_wiki.py` | Validate frontmatter, check wikilinks, find orphans, verify tags |
| `factory/scripts/build_index.py` | Regenerate `wiki/_index.md` from page frontmatter |
| `factory/scripts/add_navigation.py` | Inject breadcrumbs on every page |

Extended in Phase 2 to handle math types:
- `lint_wiki.py` `VALID_TYPES` now includes `topic`, `problem_type`, `technique`, `formula`
- `add_navigation.py` `SECTION_MAP` has entries for `topics`, `problem_types`, `techniques`, `formulas`
- `lint_wiki.py` `extract_wikilinks()` now filters asset embeds (`![[file.svg]]`) by extension
- `lint_wiki.py` now extracts wikilinks from system files so breadcrumb backlinks count

---

## Ingest Pipeline (as executed)

### Phase A: Scripted extraction

`tools/ingest_math_book.py --all` walks each book's `chapters/` (or topic-folder) tree, extracts every `\begin{env}[title]...\end{env}` block for each book's env map, and writes `raw/extractions/{book_slug}/chapter_NN.json`. No LLM involved. **Ran once; reruns are cheap (~1 second per book).**

### Phase B: Consolidation

`tools/consolidate_extractions.py` walks all extractions and merges sections by normalized title into per-branch catalog shards. **Ran once; reruns should stay deterministic.**

### Phase C: Stub generation

`tools/generate_topic_stubs.py --branch all` reads each branch's catalog and writes one `*.md` stub per topic under `wiki/topics/{branch_dir}/`. Skips any topic whose slug already exists anywhere under `wiki/topics/` (so Circles.md in geometry/ is left alone). **Ran once; rerun only when catalog changes.**

### Phase D: Generator development (ongoing)

For each target topic, write a Python module in `generators/{branch}/{topic_family}.py` containing one or more `@register`-decorated subclasses of `Generator`. Each generator must:

1. Set `generator_id`, `topic_slug` (matching the lowercase of the wiki page slug), `display_name`.
2. Implement `_generate_one(difficulty, rng) -> Problem` using deterministic construction (usually backward from a chosen answer).
3. Return a `Problem` with non-empty `statement_latex`, `answer_latex`, `hints` (≥ 2), and `solution_steps_latex` (≥ 2).
4. Optionally set `bank_count_per_difficulty` class attribute if the parameter space is small.
5. Be imported from the appropriate `__init__.py` so it reaches the central registry.

Then run `py -3 -m pytest generators/tests/` — the parametrized test suite will exercise the new generator automatically at easy/medium/hard and verify batch uniqueness, reproducibility, and structural well-formedness.

Finally run `py -3 tools/build_problem_bank.py` to regenerate the bank shards.

### Phase E: Commit and deploy

Commit the new generator files, updated `__init__.py`, updated `wiki/_data/problem_types_index.json`, and new `wiki/_data/problems/{slug}.json` files together. Push → GitHub Actions rebuilds the site in ~70 seconds → changes are live.

---

## Topics with Generators (Phase 2c Waves 1-3 detail)

### Wave 1 (commit `7e142e8`, +17 generators)
- `one_step_equations`: `one_step_eq_add`, `one_step_eq_sub`, `one_step_eq_mul`, `one_step_eq_div`
- `slope`: `slope_from_two_points`, `slope_from_slope_intercept_form`, `slope_classify_from_points`, `slope_parallel_perpendicular`
- `the_quadratic_formula`: `quadratic_formula_integer_roots`, `quadratic_discriminant`, `quadratic_formula_radical_roots`
- `the_pythagorean_theorem`: `pythagoras_find_hypotenuse`, `pythagoras_find_leg`, `pythagoras_check_right_triangle`
- `finding_a_percent_of_a_number`: `percent_of_number`, `percent_one_is_of_other`, `percent_find_whole`

### Wave 2 (commit `690f0d8`, +14 generators)
- `slope_intercept_form`: `slope_intercept_from_slope_and_point`, `slope_intercept_from_two_points`, `slope_intercept_identify_from_equation`
- `multi_step_equations`: `multi_step_eq_two_step`, `multi_step_eq_distribution`, `multi_step_eq_variables_both_sides`
- `factoring_trinomials_leading_coefficient_1`: `factor_trinomial_leading_1`, `factor_difference_of_squares`, `factor_perfect_square_trinomial`
- `solving_systems_by_substitution`: `systems_substitution_isolated_y`, `systems_substitution_isolated_x`
- `percent_increase_and_decrease`: `percent_change_find_percent`, `percent_change_find_new_value`, `percent_change_find_original`

### Wave 3 (commit `2935342`, +15 generators)
- `order_of_operations`: `order_of_ops_basic`, `order_of_ops_with_exponents`, `order_of_ops_nested_parens`
- `adding_and_subtracting_integers`: `add_two_integers`, `subtract_two_integers`, `integer_sum_chain`
- `solving_systems_by_elimination`: `systems_elimination_direct`, `systems_elimination_with_multiplication`
- `absolute_value_equations`: `abs_val_eq_simple`, `abs_val_eq_linear`, `abs_val_eq_no_solution`
- `properties_of_exponents`: `exponent_product_rule`, `exponent_quotient_rule`, `exponent_power_rule`

Plus Phase 1's `circles` topic (5 generators: equation from center+radius, center+radius from equation, area from radius, circumference from radius, area from diameter).

---

## Wave Plan for Continuation (Wave 4 onward)

The catalog has ~230 topics that still need generators. Realistic pace is ~5 topics × ~3 generators per wave. Proposed milestones:

### Milestone 2: Intermediate algebra (Waves 4-7)

Target topics (all have auto-stubs in `wiki/topics/algebra/`):

- **Wave 4:** Polynomial fundamentals
  - `polynomial_basics` (Adding and Subtracting Polynomials)
  - `multiplying_polynomials` (FOIL + distribution)
  - `special_products` (difference of squares, perfect squares — different from Wave 2's factoring)
  - `factoring_trinomials_general` (ax² + bx + c)
  - `factoring_completely` (combined GCF + pattern + trinomial)

- **Wave 5:** Rational expressions
  - `simplifying_rational_expressions`
  - `adding_and_subtracting_rational_expressions`
  - `multiplying_and_dividing_rational_expressions`
  - `solving_rational_equations`
  - `rational_equations_and_applications`

- **Wave 6:** Radicals and roots
  - `simplifying_radical_expressions`
  - `operations_with_radicals`
  - `rational_exponents`
  - `square_roots_and_cube_roots` (pre-algebra)
  - `the_distance_formula`

- **Wave 7:** Inequalities
  - `inequalities_and_their_graphs`
  - `solving_multi_step_inequalities`
  - `compound_inequalities`
  - `absolute_value_inequalities`
  - `systems_of_linear_inequalities`

### Milestone 3: Geometry breadth (Waves 8-10)

- **Wave 8:** Triangles
  - `triangle_angle_sum_and_exterior_angles`
  - `similar_triangles`
  - `proportions_in_similar_figures`
  - `applications_of_the_pythagorean_theorem`
  - `classifying_triangles_and_quadrilaterals`

- **Wave 9:** Area, perimeter, volume
  - `perimeter_and_area_of_polygons`
  - `circumference_and_area_of_circles`
  - `surface_area_of_prisms_and_cylinders`
  - `volume_of_prisms_and_cylinders`
  - `volume_of_pyramids_and_cones`

- **Wave 10:** Coordinate geometry
  - `plotting_points_and_the_coordinate_plane`
  - `the_midpoint_formula`
  - `points_lines_angles_and_angle_relationships`
  - `scale_drawings_and_maps`
  - `composite_figures`

### Milestone 4: Functions and graphs (Waves 11-13)

- Function notation, domain/range, composition, inverse
- Linear function writing, standard form, point-slope form
- Quadratic graphing (vertex form, direction, range)
- Power functions, absolute value functions, square root functions
- Function arithmetic and composition
- Transformations (shifts, reflections, stretches)
- Piecewise functions

### Milestone 5: Exponentials and logarithms (Waves 14-15)

- Exponential functions
- The natural base e
- Logarithm properties
- Solving exponential equations
- Solving logarithmic equations
- Growth, decay, applications
- Change of base

### Milestone 6: Trigonometry (Waves 16-19)

- Right triangle trig (SOH CAH TOA)
- Angles and radian measure
- Unit circle and circular function definitions
- Graphs of sine, cosine, tangent
- Pythagorean and sum/difference identities
- Trigonometric equations
- Law of Sines and Law of Cosines
- Polar coordinates (if scoping in)
- Vectors (if scoping in)

### Milestone 7: Sequences, series, probability, statistics (Waves 20-22)

- Arithmetic sequences and series
- Geometric sequences and series
- Induction (light)
- Permutations and combinations
- Probability of simple and compound events
- Data displays and measures of spread
- Histograms and box plots

### Milestone 8: Conics, matrices, complex numbers (Waves 23-26)

- Parabolas, ellipses, hyperbolas (generators complementing Phase 1's Circles)
- Matrix arithmetic
- Determinants
- Solving systems with matrices
- Complex number arithmetic
- Polar form of complex numbers
- De Moivre's theorem

### Milestone 9: Pre-algebra middle-school depth (Waves 27-30)

- Fractions (adding, subtracting, multiplying, dividing, mixed numbers)
- Decimal operations
- Order of operations with fractions/integers
- Ratios and unit rates
- Proportions and cross multiplication
- Percent applications (tax, tip, discount, simple interest)
- Divisibility, factors, prime factorization
- Distributive property with variables

**Rough scale estimate:** ~230 topics, ~3 generators each → ~700 total new generators. At current pace (~15 generators per wave), that's ~47 waves. Realistic reduction: not every topic will get full generator coverage on first pass — some one-off topics can stay as stubs pointing at source book sections.

**Priority heuristic for Wave N:**
1. Topics that unlock prerequisites for the next wave's topics
2. Topics covered by 2+ books in the catalog (high confidence, high reach)
3. Topics with lots of auto-stub "source book" references (rich material)
4. Topics that complete a visible learning path (student-visible win)

---

## Site Expansion Proposal (beyond content waves)

These are polish/feature ideas, prioritized by student impact. Each is a small standalone project.

### High impact, low effort

1. **More matplotlib figures** — Phase 1 shipped only `circle_parts.svg`. Every topic page could benefit from 1-2 diagrams. Candidates: slope types, coordinate plane, function transformations, unit circle, right triangles with labels, factoring grids.

2. **Better cross-linking** — Every topic's "See Also" section could include 3-5 related topic wikilinks. Automate by walking the catalog and building a prerequisite graph. Topics sharing a keyword or containing each other's name link automatically.

3. **Progress counter on the VaultBadge** — Small header component showing `Vault: N` on every page. Currently only the widget header shows it.

4. **Print worksheet polish** — The current `@media print` CSS works but is rough. Add:
   - Cover page with topic list and difficulty summary
   - Page breaks between problems
   - Answer key on a separate page
   - Configurable header (date, student name)

### Medium impact

5. **Input-and-check answers** — Student types their answer, widget verifies. Two options:
   - Client-side SymPy via Pyodide (~5 MB download, all offline)
   - Symbolic string matching (exact match on normalized LaTeX)
   
   Pyodide is correct but heavy. String matching handles 80% of cases and is free.

6. **Difficulty auto-tune** — Track correct/incorrect per generator in localStorage. Suggest next difficulty based on success rate.

7. **Custom worksheet builder** — A dedicated page where the student picks N topics, each with a difficulty and count, and builds a mixed worksheet. Builds on the Vault infrastructure.

8. **jsPDF polished download** — Phase 1 plan included this. Current implementation uses browser print. A dedicated "Download PDF" button that renders KaTeX into canvas and writes a PDF directly gives consistent output across browsers.

### Lower priority but cool

9. **Manim hero animations** — 10-20 curated visualizations for high-impact topics:
    - Slope as rate of change (line rotating around a point)
    - Unit circle generating sine/cosine
    - Completing the square (square literally being completed)
    - Limit (epsilon-delta)
    - Derivative as slope of secant → tangent
    - Quadratic vertex shifting
    
    Expensive (Manim + FFmpeg) but visually striking.

10. **Prerequisite graph visualization** — Use the `prerequisites` field in topic frontmatter to build a directed graph. Render as Graphviz SVG and drop onto the Topics_Overview page.

11. **Per-topic example walkthrough cards** — The catalog has ~1200 worked examples from source books. Instead of reproducing them (copyright!), use them as templates: extract the problem pattern, generate a fresh version with different numbers, show the full solution. Each topic page gets 2-3 hand-authored worked examples that way.

12. **Student vault export/import** — JSON dump / upload. Lets students save a vault across devices or share with a teacher.

13. **Search-within-problems** — Tag problems with skill/concept tags (many already exist). Let the student filter: "Show me all problems involving the distributive property."

### Infrastructure / maintenance

14. **Auto `_index.md` regeneration in CI** — Currently a stale index causes 245 cosmetic lint warnings. Have `build_index.py` run as part of CI (or commit hook) so it stays current.

15. **Nightly cron: rebuild bank from generators** — So the committed bank is always in sync with generator code. Could be a GitHub Actions scheduled workflow.

16. **Pre-commit hook: YAML validation** — Hymn Wiki v3 lesson that never got applied here. Run `yaml.safe_load()` on every modified `.md` before allowing the commit.

17. **Per-generator coverage dashboard** — Which topics have generators, which don't. Auto-regenerate into the Problem_Types_Overview page.

---

## Gotchas and Lessons Learned

**Critical rules caught via bugs this session. Any future contributor must internalize these.**

### Quartz / widget rules

1. **Display math requires multi-line `$$` syntax.** Single-line `$$(x-h)^2 + (y-k)^2 = r^2$$` is rendered as **inline** KaTeX. Use:
   ```markdown
   $$
   (x - h)^2 + (y - k)^2 = r^2
   $$
   ```
   (Phase 1 bugfix commit `215c644`.)

2. **Image embeds must use Obsidian syntax, not markdown image syntax.** Quartz's link rewriter transforms `![alt](../../assets/...)` by adding an extra `..`, breaking the path. Use:
   ```markdown
   ![[circle_parts.svg|Parts of a circle]]
   ```
   The ObsidianFlavoredMarkdown plugin resolves by filename walking the vault. (Phase 1 bugfix commit `ea19019`.)

3. **Vault.md alias must not match its filename.** An alias in `aliases: [...]` that matches the filename stem creates an alias-redirect HTML file that overwrites the canonical page. Phase 1 bug: `Vault.md` with `aliases: ["Vault", "Practice"]` → `/Vault` only served a meta refresh. Fix: removed `"Vault"` from the alias list. (Phase 1 bugfix commit `70bad13`.)

4. **Runtime KaTeX is not available by default.** Quartz's `Plugin.Latex` loads only `katex.min.css`. For dynamic LaTeX in widget content you must inject the KaTeX JS CDN yourself via `ensureKatex()`. See the singleton loader at the top of both `.inline.ts` files.

5. **`data-topic-slug` attribute is lowercased.** The stub generator writes `<div class="problem-vault-widget" data-topic-slug="{slug.lower()}">`. Your generator's `topic_slug` attribute **must** match that lowercase form. If `One_Step_Equations.md` is the page, the generator uses `topic_slug = "one_step_equations"`.

### Generator rules

6. **Parameter space must support at least 30 unique problems per difficulty** (or set `bank_count_per_difficulty` lower). The Pythagorean theorem easy variant only has 6 triples × 2 orderings = 12 possibilities, so it has `bank_count_per_difficulty = 25` as a cap.

7. **Forward construction avoids infinite loops.** Don't pick a target answer and brute-force for valid parameters — pick parameters and accept whichever answer they produce, with a bounded retry for special constraints. Phase 2c Wave 1 had an infinite loop bug in `quadratic_formula_radical_roots` that was fixed by flipping construction direction.

8. **Backward construction ensures clean answers.** For `one_step_eq_mul`, pick `a` and `x_val`, then compute `b = a * x_val` — this guarantees an integer solution. Same technique for percent generators (pick `p` and `whole` divisible by `100/gcd(p,100)`).

9. **SymPy's `sp.latex()` handles signed equations correctly.** Use `sp.latex(sp.Eq(a*x + b, c))` instead of manual string formatting when `b` could be negative.

10. **The test suite respects `bank_count_per_difficulty`.** Tests clamp count to `[5, min(10, bank_count_per_difficulty)]`. Fine-tune the attribute rather than rewriting tests.

### YAML and parsing rules

11. **Always quote hash tags in YAML frontmatter**: `tags: ["#topic-auto-generated"]` not `tags: [#topic-auto-generated]`. Unquoted `#` starts a comment in YAML. (Hymn Wiki v3 lesson.)

12. **Run `yaml.safe_load()` on every modified file after batch writes.** Three cascading failure modes in Hymn Wiki v3: non-greedy regex breaking on wikilinks, unescaped quotes, cascading backslash artifacts. Validate post-write to catch all of them.

13. **CamelCase file names need splitting during normalization.** Stitz-Zeager files like `AbsoluteValueFunctions.tex` should normalize to "absolute value functions" to merge with `Absolute Value Functions` from other books. The `consolidate_extractions.py` regex handles this but is conservative; manual slug cleanup may be needed for edge cases.

### Process rules

14. **Don't trust write retries to replace a file** — check for dead siblings. Phase 2c Wave 3 left two dead files (`absolute_value_equations.py`, `systems_elimination.py`) because a failed first Write created a new file, and a retry with a different name created a second file. Both existed but only one was imported. Cleanup commit `8f54c32` removed them. Always diff the expected file list against what's on disk after a batch write.

15. **Python 3 on Windows is `py -3`, not `python`.** Shell CWD persists between Bash calls but must be explicitly set each session; use `cd /c/Wiki_Factory/builds/Math_Wiki` as a first step.

16. **The `builds/*/raw/` path is gitignored by the root `.gitignore`.** The 62 MB of textbook source and 3.4 MB of extractions stay local. No need to `git rm` them.

---

## Deployment

**GitHub Pages** via Quartz v4 + GitHub Actions CI/CD.

- **Repo:** `JD-Jones-ASES/Wiki-Factory`
- **URL:** https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/
- **Build time:** ~60-70 seconds for ~270 pages
- **CI workflow:** `.github/workflows/deploy.yml` (shared with Hymn Wiki). Clones Quartz v4 fresh, overlays `quartz.config.ts`/`quartz.layout.ts`/`quartz_components/`/`static/` from the build root, copies `wiki/*` into `content/`, runs `npx quartz build`.
- **Overlay blocks** for `quartz_components/` and `static/` are guarded by directory-existence checks so Hymn Wiki's build is unaffected.
- **Per-build Quartz settings:** `enableSPA: false`, `Plugin.Latex({ renderEngine: "katex" })`, Explorer `filterFn` hides `topics/`, `problem_types/`, `entities/` folders (students navigate via overview hubs and search), Graph depth-1 for local view.

### Custom components loaded in layout

```typescript
// quartz.layout.ts (abbreviated)
import ProblemVaultWidget from "./quartz/components/ProblemVaultWidget"
import VaultViewer from "./quartz/components/VaultViewer"

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [ProblemVaultWidget(), VaultViewer()],  // on every page; early-return if mount absent
  footer: Component.Footer({ ... }),
}
```

---

## Navigation Design (what students see)

Math_Wiki uses Quartz v4's three-pane layout with wiki-specific overrides. This section documents the current information architecture so future sessions extend it consistently.

### Layout zones

```
┌─────────────────────────────────────────────────────────────┐
│  header (empty)                                             │
├────────────┬──────────────────────────────────┬────────────┤
│            │                                  │            │
│ LEFT       │  MAIN CONTENT                    │ RIGHT      │
│ (Explorer  │  (article body)                  │ (graph,    │
│  sidebar)  │                                  │  TOC,      │
│            │                                  │  backlinks)│
│            │                                  │            │
├────────────┴──────────────────────────────────┴────────────┤
│  afterBody: ProblemVaultWidget + VaultViewer (both mount   │
│              only on pages with the right hook div)        │
│  footer: "All Wikis", "Source" links                        │
└─────────────────────────────────────────────────────────────┘
```

### Left sidebar (every page)

Components in order, defined in `quartz.layout.ts`:

1. **Page title** — "Math Wiki" (links to home)
2. **Flex row** — Search (grows) + Darkmode toggle + Reader mode toggle
3. **Explorer** — file tree, filtered + relabeled

The Explorer is deliberately short and scannable. `mathExplorerFilter` HIDES the three large collections (`topics/` with ~239 pages, `problem_types/`, `entities/`) plus all underscore-prefixed internal files except `_overview`. `mathExplorerMap` REWRITES sidebar labels to emoji-prefixed friendly names:

| Sidebar label | Points at |
|---|---|
| 🏠 Home | `_overview.md` |
| 📘 Algebra | `Algebra_Overview.md` |
| 📐 Geometry | `Geometry_Overview.md` |
| 📏 Trigonometry | `Trigonometry_Overview.md` |
| 🧮 Pre-Calculus | `Precalculus_Overview.md` |
| 📖 All Topics | `Topics_Overview.md` |
| 🎒 Your Vault | `Vault.md` |
| 📊 Progress Dashboard | `Topic_Status.md` |
| 🎯 Problem Types | `Problem_Types_Overview.md` |
| 🧮 All Formulas | `Formulas_Overview.md` |
| 🛠️ All Techniques | `Techniques_Overview.md` |
| 📚 All Sources | `Sources_Overview.md` |
| 📖 All Comparisons | `Synthesis_Overview.md` |
| 👩‍🏫 Mathematicians | `Entities_Overview.md` |
| 🧮 Formulas (folder) | `formulas/` |
| 🛠️ Techniques (folder) | `techniques/` |
| 📚 Sources (folder) | `sources/` |
| 📖 Comparisons (folder) | `synthesis/` |

Everything else (individual topic pages under `topics/`) is reachable through branch hubs, search, and wikilinks — not the sidebar.

### Right sidebar (content pages only)

Components in order:

1. **Graph view** — `localGraph.depth=1` shows only direct connections (prevents visual overload on heavily-linked topics); global graph is also exposed but depth-unlimited
2. **TableOfContents** (desktop only) — auto-generated from H2/H3 headings
3. **Backlinks** — who links to this page

Topic pages with many prerequisite/related wikilinks produce meaningful local graphs. The home page and hubs have thinner graphs but still render the graph widget.

### Main content (every page)

Before body (in order):
1. **Breadcrumbs** (skipped on the home page via ConditionalRender)
2. **Article title**
3. **Content meta** (date, tags)
4. **Tag list**

After body (injected when the mount hook is present):
1. **ProblemVaultWidget** — renders only when `<div class="problem-vault-widget" data-topic-slug="...">` exists in the page body. Every live topic page has this div.
2. **VaultViewer** — renders only on `Vault.md` via the VaultViewer mount div. Reads problems from localStorage.

### Landing page (`wiki/_overview.md`)

The home page is structured as a student-first hero:

```
# Math Wiki
<tagline + stats row: 36 topics · 110 generators · 9,621 problems>
<copyright/privacy note>

## Start Here
- Browse live topics → Topics_Overview
- Your Practice Vault → Vault
- Progress Dashboard → Topic_Status

## Live Learning Paths
<7 curated topic sequences: Foundations, Proportional Reasoning, Expressions
 and Variables, Linear Equations, Lines and Slopes, Quadratics/Exponents,
 Geometry Cornerstones>

## Explore by Branch
<4 branch hub links with live/total counts>

## Other Reference Pages
<Formulas, Techniques, Problem Types, Sources, Comparisons, Mathematicians>

## How to Use This Wiki
<5-step workflow: pick → read → add → open vault → download>

## Current Status
<Cluster 0-L progress table>

## About
<source attribution, privacy, license, repo link>
```

Key design principle: the learning paths are the PRIMARY entry point for students who don't know where to start. They're hand-curated sequences of live topics, not exhaustive lists. As more clusters ship, new learning paths are added here.

### Branch hub pages (`*_Overview.md`)

Structure (hand-written intro + auto-generated topic block):

```
# {Branch} Overview

{Hand-written intro paragraph: what is this branch about, warmly written}

## What You'll Learn
{Hand-written bullet list of sub-areas}

## Topics
{Hand-written note: N live, M stubs, link to comprehensive plan}

## Key Formulas
{Pointer to Formulas_Overview}

## Common Techniques
{Pointer to Techniques_Overview}

<!-- AUTO:TOPICS:BEGIN -->
### {Group label} --- N live / M total

**🟢 Live topics with practice widgets (N)**
- 🟢 [[Slug|Title]]
- ...

<details>
<summary>⚪ M stub topic(s) (click to expand)</summary>
- ⚪ [[Slug|Title]] --- _annotation_
- ...
</details>
<!-- AUTO:TOPICS:END -->

## See Also
```

The auto-generated block is regenerated by `tools/update_branch_hubs.py`, which reads the catalog AND `wiki/_data/problem_types_index.json` to distinguish live (has ≥1 generator) from stub topics. Live topics render as a flat bulleted list with 🟢 markers. Stub topics are wrapped in a collapsed `<details>` element so the page stays scannable even when a branch has hundreds of stubs.

### Topic page layout

Every live topic follows the same structure (established by `Circles.md`):

```markdown
---
<frontmatter: title, type, tags, source_refs, related, prerequisites,
 status, confidence, figures, problem_type_ids, summary>
---

> [[_overview|Home]] > [[{Branch}_Overview|{Branch}]] > {Title}

# {Title}

{Intuition paragraph}

![[optional/figure.svg|caption]]

## What it means
## The rule ($$ display math $$)
## Why it works
## Worked examples (2-3 with step-by-step solutions)
## Common mistakes
## Prerequisites  (wikilinks to 2-4 prereq topics)
## Problems Involving This Topic
<div class="problem-vault-widget" data-topic-slug="{lowercase_slug}"></div>
## See also  (wikilinks to 3-5 related topics)
## Sources in the ingested textbooks
```

The `<div class="problem-vault-widget">` is the mount hook the Quartz custom component scans for.

### Expandability (adding more pages to navigation)

When Cluster N ships:

1. **New topic pages** get the topic-page layout above. They automatically show in branch hubs (rerun `update_branch_hubs.py`) and in `Topics_Overview.md` (requires a hand edit to add them to the "Live Topics" section).
2. **New learning paths** on the landing page: edit the "Live Learning Paths" section in `wiki/_overview.md` to add a new H3 and a sequence of wikilinks.
3. **New category pages** (if a cluster needs one, e.g., "Trigonometry Cornerstones"): add an entry to `mathExplorerMap.friendlyFileNames` in `quartz.layout.ts` so the sidebar gets an emoji label.
4. **New synthesis / comparison pages**: drop them in `wiki/synthesis/`; they auto-appear in the Explorer sidebar under "📖 Comparisons".

### What the navigation deliberately does NOT do

- **No "recently updated" feed.** Quartz has ContentIndex, but a feed needs curation to be useful. Defer until we have >100 live topics.
- **No student progress tracking server-side.** Vault is localStorage-only by design.
- **No sidebar enumeration of 239 topic pages.** The Explorer would become unnavigable. Students drill via hubs, search, and wikilinks instead.
- **No custom landing-page components (hero CSS, animated counters, etc.).** Quartz strips `<script>` tags from markdown; any rich home page would need a new custom Quartz component. The current markdown-based home page is intentionally simple.

---

## Conventions

- **Topic titles:** Title Case with underscores in filenames (`Linear_Equations.md`). Frontmatter `title:` uses spaces ("Linear Equations").
- **Widget mount slug:** Always the lowercase form of the file stem (`linear_equations`). Match in generator `topic_slug`.
- **Problem-type IDs:** `snake_case` descriptive verb phrase (`one_step_eq_add`, `slope_from_two_points`).
- **Formula titles:** Title Case of the named formula (`Quadratic_Formula.md`, `Pythagorean_Theorem.md`).
- **Technique titles:** Gerund or noun phrase (`Completing_The_Square.md`, `Substitution_Method.md`).
- **LaTeX:** Inline `$...$`, display `$$\n...\n$$` (multi-line!). KaTeX-compatible only.
- **Tags:** Quoted in YAML (`tags: ["#tag-name"]`). Must appear in `_tag_taxonomy.md`.
- **Tone:** Warm, encouraging, clear. Explain intuition first, then formal. Assume the student is smart but learning.
- **Copyright:** Never reproduce source-book problems or prose verbatim. All practice problems come from `generators/`. Enforced by `generators/tests/test_copyright_safety.py`.
- **Frontmatter hygiene:** Post-write YAML validation on batch operations. CI runs `factory/scripts/validate_yaml.py` on every push.
- **External links:** `<a target="_blank" rel="noopener">` for YouTube, Desmos, external tools.
- **Generator coverage standard:** **Minimum 3 generators per topic, target 4.** Generators must span the span of problem variants (e.g., for Slope: from-two-points, from-equation, classify, parallel/perpendicular). Topics with fewer than 3 generators don't count toward cluster-verification completeness.
- **Cross-linking targets:** Every topic page at `status: draft` or `complete` should have at least 3 `prerequisites` links and at least 3 `related` / see-also links. Enforced by the `tools/topic_status.py` scoring rubric.

---

## Buildout Plan (9 clusters + closeout)

The comprehensive buildout from the current state to complete integration of the 5 textbooks is structured as 9 topic clusters plus a closing polish pass. Each cluster finishes a coherent learning path (content + generators + figures + cross-links) so the site stays usable as it grows. The full plan is at `C:\Users\jdj32\.claude\plans\sorted-skipping-pudding.md`.

| Cluster | Name | Topics | Status |
|---|---|---:|---|
| **0** | Infrastructure hardening + global alias merge | 0 | **shipped** |
| **1** | Pre-algebra foundations | 20 | **shipped** |
| **2** | Linear world completion | 14 | **shipped** |
| **3** | Polynomials + Quadratics deep | 14 | **shipped** |
| **4** | Rationals & Radicals | 12 | **shipped** |
| **5** | Functions & Transformations | 14 | **shipped** |
| **6** | Exponentials & Logarithms | 10 | **shipped** |
| **7** | Trigonometry | 15 | **shipped** |
| **8** | Sequences, probability, statistics | 9 | **shipped** |
| **9** | Conics, matrices, complex numbers | 12 | **shipped in this session — 9-cluster plan COMPLETE** |
| **L** | Lint/polish + prereq-graph widget + ingest smoke test | 0 | pending |

**Four workstreams run concurrently within each cluster:**

- **I** --- Infrastructure (Cluster 0 only; one-time hardening)
- **X** --- Alias merge pass (Cluster 0 only; edits `tools/aliases.yaml`)
- **C** --- Content enrichment (per-cluster; auto-stub -> rich lesson page)
- **G** --- Generator waves (per-cluster; existing Waves 4-30 plan reorganized)

**Parallelization:** 6-8 content agents + 2-3 generator agents per cluster wave, never on the same topic simultaneously. Expected throughput: ~12-16 topics enriched per cluster week.

**Per-cluster verification** (from `tools/topic_status.py` rubric):
- Prose body 300+ words
- 2+ worked examples
- 3+ generators
- 3+ prerequisite links
- 3+ see-also links
- At least one figure where visually useful
- `status: draft` or `complete` in frontmatter

A topic at score 90+ meets the plan's per-cluster verification rules.

---

## env_map Author's Guide (adding a new book's LaTeX convention)

To ingest a new textbook that doesn't use the Curriculum Factory or Stitz-Zeager conventions, you need to teach `ingest_math_book.py` how to recognize its blocks.

### Step 1: survey the source

Open a few section `.tex` files from the new book and list every `\begin{env}...\end{env}` block you see. Typical environments in math textbooks:

| LaTeX env | Usual meaning | Canonical kind |
|---|---|---|
| `definition` / `defn` / `keyterm` | A defined term | `definition` |
| `theorem` / `thm` | A provable statement | `theorem` |
| `corollary` / `cor` | A direct consequence | `corollary` |
| `property` / `rule` | An algebraic identity or manipulation rule | `property` |
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

Only list environments the ingest should extract. Unknown environments are silently ignored.

### Step 3: register the book

```python
BOOKS["new_book"] = BookSpec(
    slug="new_book",
    title="New Textbook Title",
    branch_hint="algebra-1",
    root_dir=BOOKS_DIR / "new_book",
    layout="chapters",    # or "topicfolders" for a Stitz-Zeager-style layout
    env_map=NEWBOOK_ENVS,
)
```

### Step 4: verify layout

Two layouts are supported out of the box:

- **`chapters`** (Curriculum Factory style): `chapters/ch01/chapter.tex` + `chapters/ch01/sections/sec01.tex`, `sec02.tex`, ... per chapter. Chapter title comes from `\chapter{...}`, section title from `\section{...}`.
- **`topicfolders`** (Stitz-Zeager style): topic folders like `LinearQuadratic/` containing multiple `.tex` section files. Chapter order and titles come from the `BOOK5_CHAPTER_FOLDERS` list in `ingest_math_book.py`; for a new book you'd add a new list and a matching branch in `parse_topicfolder_layout_book`.

If neither layout fits, add a new one. Keep the two existing ones untouched.

### Step 5: run the guided ingest

```bash
py -3 tools/ingest_new_book.py --slug new_book --dry-run
py -3 tools/ingest_new_book.py --slug new_book
```

The script walks every pipeline stage, snapshots the catalog before/after, and reminds you to review `tools/aliases.yaml` for duplicate topics with existing books.

### Step 6: propose merges

After ingesting, open `raw/catalog/index.json` and look for your new slugs. Any topic whose canonical form obviously matches an existing topic should be merged via `tools/aliases.yaml`:

```yaml
merges:
  - from: ["New_Book_Slug", "Existing_Slug"]
    into: "Existing_Slug"
    rationale: "Same topic; new book's section title wasn't normalized identically"
```

Then rerun `consolidate_extractions.py` to apply the merges.

---

## Self-Improvement Log

### Version 1.15.0 --- Cluster 9 Conics, Complex Numbers, and Matrices — 9-CLUSTER PLAN COMPLETE (2026-04-11)

**Stats:** 12 topics enriched (+12 live, now **136 total**), 36 new generators (+36, now 410 total), 2,675 new verified problems (+2,675, now **32,698 total**), 3 new matplotlib figures (conic sections gallery, complex plane, polar coordinate grid). **The 9-cluster buildout plan is complete.**

**Topics shipped in the final cluster:**

- **Conic sections (4):** Circumference_And_Area_Of_Circles (pre-algebra), Parabolas (conic view, algebra-2), Ellipses (algebra-2, 2 sources), Hyperbolas (algebra-2, 2 sources — richest)
- **Complex numbers (3):** The_Complex_Number_System (algebra-2), Complex_Zeros (pre-calc), Polar_Form_Of_Complex_Numbers (pre-calc)
- **Polar coordinates (1):** Introduction_To_Polar_Coordinates (pre-calc)
- **Matrices (4):** Matrix_Arithmetic (pre-calc), Augmented_Matrices (pre-calc), Determinants (pre-calc), Matrix_Methods (pre-calc)

Seven of the twelve topics are pre-calculus, bringing the pre-calc branch from 20/47 → **27/47** live. The pre-calc branch now covers trigonometry, exp/log, sequences/binomial/induction, conics, complex numbers, polar coordinates, and matrices — essentially the full pre-calc curriculum.

**Generator modules added (2):**

- `generators/precalculus/conics_and_complex.py` — 24 generators covering 8 topics (parabolas × 3, ellipses × 3, hyperbolas × 3, circumference_and_area × 3, complex system × 3, complex zeros × 3, polar form × 3, polar coords × 3)
- `generators/precalculus/matrices.py` — 12 generators covering 4 topics (matrix arithmetic × 3, augmented × 3, determinants × 3, matrix methods × 3)

**Figures added:**

- `wiki/assets/figures/algebra/conic_sections_gallery.svg` — 2×2 grid of circle, ellipse, parabola, hyperbola — the one figure that gives students a visual vocabulary for the entire conic family
- `wiki/assets/figures/precalculus/complex_plane.svg` — complex plane with four points plotted and labeled, making the "pair of real numbers" interpretation of complex numbers concrete
- `wiki/assets/figures/precalculus/polar_coordinates.svg` — full polar grid with concentric circles and radial lines, three labeled points showing the $(r, \theta)$ representation

**Execution model:**

3 parallel content sub-agents (4+4+4 topics) + 2 parallel generator sub-agents (24 + 12) + 1 figures sub-agent. All 6 sub-agents dispatched together and returned clean results. The 24-generator `conics_and_complex.py` module is the second-largest single generator batch this session after Cluster 7's `trig_advanced.py` (30 generators).

**What worked:**

- **Backward construction for conics.** Every conic generator picks the geometric features first (vertex, center, $a$, $b$, $c$) and derives the equation, so the "write the equation from features" direction is the same code path as the "read features off the equation" direction. Pythagorean triples ($3\text{-}4\text{-}5$, $5\text{-}12\text{-}13$, $8\text{-}15\text{-}17$) appear all over Ellipses and Hyperbolas to keep $c$ integer.
- **Complex numbers treated as "pairs of reals that multiply in a funny way"** rather than "mysterious $i$ things". The complex plane figure anchors this visually. Addition is componentwise just like vectors; multiplication is the part that's new.
- **De Moivre's theorem as "the whole point" of polar form.** Teaching polar form without De Moivre is teaching a notation without a payoff. The generator for `de_moivre_power` gives students immediate experience with why polar form makes $(1+i)^{10}$ computable in one step instead of ten.
- **Unimodular matrix construction** in the `matrices.py` module. The `_draw_unimodular()` helper builds 2×2 matrices with determinant $\pm 1$ by starting from six base matrices and applying elementary row replacements, guaranteeing integer inverses. This is the trick that keeps the `matrix_inverse_2x2` and `solve_system_via_inverse` generators producing clean student-friendly answers instead of ugly fractions.
- **Complete backward construction for hyperbolas.** The $c^2 = a^2 + b^2$ sign difference from ellipse is exactly the Pythagorean theorem, so using Pythagorean triples backwards gives integer foci. Example: pick $a = 4$, $b = 3$ → $c = 5$; pick $a = 12$, $b = 5$ → $c = 13$.

**What failed and how it was fixed:**

- **2 copyright near-misses** in the conics batch: "the parabola opens to the right because $p > 0$" matched source language, and "midpoint of the segment joining the foci is the center" matched an ellipse definition. Both rewrote in one line each.
- **3 dead wikilinks** from the sub-agents inventing targets: `[[Rational_Roots_Theorem]]`, `[[Polynomial_Long_Division]]`, and `[[Pre_Algebra_Overview]]` on Complex_Zeros / Circumference_And_Area_Of_Circles. Fixed: removed the rational-roots link (it was inline), rewired the long-division link to `[[Factoring_Completely]]`, and changed the breadcrumb/see-also to `[[Algebra_Overview]]`.
- **1 tag-taxonomy violation** (`#topic-trigonometry`, which is not in the taxonomy) on `Introduction_To_Polar_Coordinates.md`. Rewrote to `#topic-unit-circle`.
- **Zero parameter-space-too-small failures** this cluster. The backward-construction discipline built up over 8 clusters pays off here: every generator's easy pool is large enough on first try.

**Final gate checks after Cluster 9:**

- **Pytest:** 29/29 green (8 circles-parametrized across 410 generators + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (130 stub pages — down from 142).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score **53.4** / 100 (was 49.9). 134 topics with 3+ generators (was 122). Pre-calculus avg jumped from 46.9 → **57.0** as the 7 new pre-calc topics all landed with full generator coverage.
- **Bank size:** 27.1 MB across 136 shards, all under 320 KB each.
- **Branch hubs:** Algebra_Overview (109 live) and Precalculus_Overview (27 live) both regenerated.

## End of the 9-cluster buildout plan

The plan set out in Cluster 0 (`C:\Users\jdj32\.claude\plans\sorted-skipping-pudding.md`) called for nine topic clusters covering the full algebra and pre-calculus curriculum. Six months of session-planning in one afternoon, and the final state is:

| Metric | Plan start | Plan end |
|---|---:|---:|
| Live topics | 16 | **136** |
| Generators | 50 | **410** |
| Verified problems | 4,335 | **32,698** |
| Figures | 1 | **31** |
| Bank size | 3.1 MB | 27.1 MB |
| Topic status avg | 16.2 / 100 | 53.4 / 100 |
| Algebra branch avg | ~18 | 60.7 |
| Pre-calculus branch live | 0 | 27 / 47 |

**What the wiki now covers end-to-end:** Every page from pre-algebra foundations (integers, fractions, decimals, ratios) through Algebra 1 (linear equations, quadratics, factoring), through Algebra 2 (exponentials, logarithms, rationals, functions, transformations, conics, complex numbers, matrices), through Pre-Calculus (trigonometry with unit circle and identities, sequences and series, polar coordinates, matrices). All 136 topics have full prose lessons with 300+ word bodies, worked examples with step-by-step solutions, 3+ problem generators each, wikilinked cross-references, and SymPy-verified practice problems.

**What's out of scope but remains as stubs (~103 topics):** Secondary catalog entries that didn't make the 9-cluster priority list — mostly algebra-1 alternative treatments (Variables_And_Expressions, Scientific_Notation), pre-algebra sub-topics (Place_Value detail pages, additional geometry angle types), and the remaining Stitz-Zeager pre-calc chapters (Parametric, Polar Graphs, Nonlinear Systems, Partial Fractions, Induction detail). These stubs have auto-generated frontmatter and source references so they can be activated in a future follow-up session, but they aren't part of the original 9-cluster scope.

**Future work (post-plan):**

- **Cluster L** (lint/polish): a final pass through all 136 live topics with a senior reviewer, checking for consistency, flagging any remaining typos, and strengthening cross-links where the graph is thin.
- **Prereq-graph widget**: a client-side visualization of the topic dependency graph, built from the `prerequisites:` YAML fields already populated on every page.
- **Additional figures**: roughly 50% of live topics have at least one figure; the other half could benefit from one.
- **Follow-up ingest**: bringing more source books into the catalog is fully supported by the `tools/ingest_new_book.py` pipeline from Cluster 0. Each new book will enrich existing topics with more examples and may unlock a handful of new topics.
- **Vault feature polish**: the Vault is working but could use export/import, custom worksheet builder, and jsPDF download (all listed in the Site Expansion Proposal section above).

### Version 1.14.0 --- Cluster 8 Sequences, Probability, and Statistics (2026-04-11)

**Stats:** 9 topics enriched (+9 live, now **124 total**), 27 new generators (+27, now 374 total), 2,015 new verified problems (+2,015, now **30,023 total — crossed 30k**), 3 new matplotlib figures (Pascal's triangle, box plot, histogram). First cluster with a dedicated pre-calc stats/sequences generator module, and the first cluster to exceed 30,000 verified practice problems in the bank.

**Topics shipped (all at draft status):**

- **Sequences and series (4):**
  - Arithmetic_Sequences_And_Linear_Patterns (pre-algebra)
  - Sequences (algebra-2, 2 sources — richest)
  - Summation (pre-calculus)
  - Induction (pre-calculus)
- **Probability and counting (2):**
  - Probability_Of_Simple_And_Compound_Events (pre-algebra)
  - Binomial (pre-calculus — binomial theorem)
- **Statistics (3):**
  - Mean_Median_Mode_And_Range (pre-algebra)
  - Data_Displays (pre-algebra)
  - Data_Displays_And_Measures_Of_Spread (pre-algebra)

Three of the nine topics are pre-calculus, bringing the pre-calc branch from 17/47 → 20/47 live. The last remaining pre-calc gaps are the Conics/Matrices/Complex-Numbers cluster (Cluster 9).

**Generator module added (1):**

- `generators/precalculus/sequences_and_stats.py` — 27 generators covering all 9 topics (3 each). Added to `generators/precalculus/__init__.py` alongside `trig_core` and `trig_advanced`.

**Figures added:**

- `wiki/assets/figures/precalculus/pascals_triangle.svg` — Pascal's triangle rows 0-6 with parent-sum lines connecting each entry to the two above it
- `wiki/assets/figures/pre_algebra/box_plot.svg` — horizontal box plot with five-number-summary annotation on the 11-value data set $\{12, 18, 22, 25, 28, 30, 33, 38, 42, 48, 55\}$
- `wiki/assets/figures/pre_algebra/histogram_example.svg` — 5-bin histogram of test-score frequencies, showing the touching-bars characteristic that distinguishes histograms from bar graphs

**Execution model:**

3 parallel content sub-agents (3+3+3 topics) + 1 generator sub-agent (27 generators in one module) + 1 figures sub-agent (3 figures). All 5 sub-agents dispatched together; the generator agent handled 27 generators in a single module cleanly.

**What worked:**

- **Topic-family module consolidation.** The sequences_and_stats.py module bundles 27 generators across 9 topics into one file — the tightest generator packing so far, because the 9 topics are small and share a lot of utility code (sympy for fractions, pattern-building for sum formulas, template lists for probability scenarios).
- **Arithmetic sequence ↔ linear function bridge.** Teaching arithmetic sequences as "linear functions with integer domains" rather than a separate formula-to-memorize is the pedagogical move here. Students who know the [[Linear_Functions]] page don't have to start from scratch.
- **Geometric sequence ↔ exponential function bridge.** Same move, different family. Geometric sequences ARE exponential functions evaluated at integers.
- **Induction base case plus inductive step walked through end-to-end** in Example 1 on the Induction page. The domino analogy grounds the technique before the symbol pushing starts.
- **Box plot figure with labeled five-number summary** is the single most valuable figure in the cluster — students can read the box plot as a visual reference and the figure's explicit labels teach the terminology without repeating the page content.
- **Probability AND/OR distinction** is the core pedagogical move for the probability page. Independent events → multiply; mutually exclusive events → add. Covering both in separate examples with concrete numbers locks in the rule.

**What failed and how it was fixed:**

- **2 copyright near-misses on definitional phrases**: "in which every term after the first is obtained by multiplying the previous term" on Sequences and "a data set can have no mode, one mode, or several modes" on Mean_Median_Mode_And_Range. Both rewrote in one line each.
- **Parameter-space-too-small on 3 generators**: `prob_and_independent` (16), `prob_or_mutually_exclusive` (16), `induction_inductive_step_setup` (10). Fixed by widening pools and adding `bank_count_per_difficulty` overrides during first pytest iteration.
- **No dead wikilinks this cluster** — the idiom discipline has become tight enough that both content and reference integrity pass lint on first attempt when sub-agents follow the template.

**Gate checks after Cluster 8:**

- **Pytest:** 29/29 green (8 circles-parametrized across 374 generators + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (142 stub pages — down from 151).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score **49.9** / 100 (was 47.2). 122 topics with 3+ generators (was 113). Pre-calculus avg 42.1 → 46.9; pre-algebra avg 39.2 → 43.1 (both new topics on each branch moved the needle).
- **Bank size:** 24.8 MB across 124 shards, all under 320 KB each.
- **Branch hubs:** Algebra_Overview (104 live) and Precalculus_Overview (20 live) both regenerated.

**Milestone: 30,000 verified problems.** The Math_Wiki bank now holds more than 30,000 individually SymPy-verified practice problems — three times the problem count at session start (9,621). Every problem is generated by a registered Python class, every problem has a statement, answer, hints, and step-by-step solution, and every generator is covered by the parametrized smoke test.

**What's next (Cluster 9 — the final cluster):** Conics, matrices, complex numbers. ~12 topics covering parabolas (revisited as conic sections), circles (revisited), ellipses, hyperbolas, matrix arithmetic, matrix inverses and determinants, systems via matrices, complex number arithmetic, complex numbers in polar form, De Moivre's theorem. This is the last cluster in the 9-cluster plan. After this, the Math_Wiki will cover essentially all of the 238-topic catalog that has meaningful student-facing content — an end-to-end algebra/pre-calc reference with complete interactive practice.

### Version 1.13.0 --- Cluster 7 Trigonometry (2026-04-10)

**Stats:** 15 topics enriched (+15 live, now **115 total**), 45 new generators (+45, now 347 total), 2,594 new verified problems (+2,594, now 28,008 total), 4 new matplotlib figures (unit circle with 16 special angles, sine/cosine graphs, SOH-CAH-TOA 3-4-5 triangle, vector addition head-to-tail). First cluster to populate the `#branch-pre-calculus` trigonometry pages AND the `#topic-trig-*` tag family.

**Topics shipped (all at draft status):**

- **Pre-algebra geometry foundations (3):** Similar_Triangles, Triangle_Angle_Sum_And_Exterior_Angles, Applications_Of_The_Pythagorean_Theorem
- **Angles and definitions (1):** Angles (pre-calculus)
- **Unit circle and circular functions (3):** Circular_Functions, The_Unit_Circle, Inverse_Trigonometric_Functions (pre-calculus)
- **Identities, equations, graphs, sinusoids (4):** Identities, Trigonometric_Equations, Graphs_Of_Trigonometric_Functions, Sinusoid (pre-calculus)
- **Laws and vectors (4):** Law_Of_Sines, Law_Of_Cosines, Vectors, Dot_Product (pre-calculus)

**12 new pre-calc topics** shipped in this cluster, bringing the pre-calculus branch from 5/47 → 17/47 live. The precalculus hub now shows a genuine body of content (angles, unit circle, identities, equations, laws, vectors) rather than scattered orphans.

**Generator modules added (2, in a new subdirectory):**

- **Created `generators/precalculus/` directory** — new package for pre-calc-specific generators, with its own `__init__.py`. Top-level `generators/__init__.py` now imports it.
- `generators/precalculus/trig_core.py` — 15 generators covering 5 core topics (angles × 3, circular_functions × 3, the_unit_circle × 3, inverse_trigonometric_functions × 3, graphs_of_trigonometric_functions × 3)
- `generators/precalculus/trig_advanced.py` — 30 generators covering 10 topics (similar_triangles × 3, triangle_angle_sum × 3, applications_of_pythagorean × 3, identities × 3, trigonometric_equations × 3, sinusoid × 3, law_of_sines × 3, law_of_cosines × 3, vectors × 3, dot_product × 3)

**Figures added** (all in NEW `wiki/assets/figures/precalculus/` subdirectory):

- `unit_circle.svg` — 8×8 square unit circle with all 16 special angles plotted, radius lines drawn, and $(x, y)$ coordinates labeled in exact form (fractions of $\sqrt{2}/2, \sqrt{3}/2, 1/2$, etc.)
- `sine_cosine_graphs.svg` — stacked subplots of $y = \sin x$ and $y = \cos x$ over $[-2\pi, 2\pi]$, x-axis labeled in π units, reference lines at ±1 and 0
- `right_triangle_soh_cah_toa.svg` — 3-4-5 right triangle with labeled sides (opposite, adjacent, hypotenuse), angle θ marked with an arc, and the three trig ratio equations displayed underneath
- `vector_addition.svg` — $\vec{u} = \langle 5, 1 \rangle$ and $\vec{v} = \langle 2, 4 \rangle$ added head-to-tail to produce $\vec{u} + \vec{v} = \langle 7, 5 \rangle$, with all three vectors drawn as arrows

**Execution model:**

4 parallel content sub-agents (4+4+4+3 topics) + 2 parallel generator sub-agents (15+30 generators) + 1 figures sub-agent. All 7 sub-agents succeeded on the first dispatch. The trig_advanced agent authored 30 generators in a single module — the largest single-agent generator batch this session, and it handled it cleanly.

**What worked:**

- **Trig pedagogy anchored on the unit circle.** Rather than treating SOH-CAH-TOA as the starting point (which limits you to 0-90° angles), the cluster uses the unit-circle definition as the foundation and presents right-triangle trig as a special case of it. That unified view pays off immediately when trig functions need to accept angles beyond 90°.
- **Pre-calc directory organization.** Moving pre-calc generators to their own `generators/precalculus/` subdirectory (instead of lumping them under `generators/algebra/`) is cleaner and makes the import graph match the content graph. This is a good precedent for Cluster 9 (where conics, matrices, and complex numbers will also get their own home).
- **Identity derivations.** The Identities page derives $\sin^2\theta + \cos^2\theta = 1$ from the unit-circle equation $x^2 + y^2 = 1$, then builds the derived identities from that single fact. Students don't have to memorize a pile of disconnected rules; they can regenerate the whole family from one anchor.
- **SSA ambiguous case for Law of Sines.** Including an explicit zero/one/two-triangle classification in both the content and the generator is the right pedagogical move — this is the single most confusing case in oblique-triangle solving, and every student should see it.
- **Backward construction for trig generators.** All 45 generators pick clean answer values (unit-circle exact values, Pythagorean-triple triangle sides, integer angles) and derive the problem parameters. No guess-and-check, no parameter-space-too-small failures after first iteration.
- **Figures with exact values on the unit circle.** The unit circle figure shows all 16 special angles with their exact $(x, y)$ coordinates labeled. This turns the figure into a genuine reference students can come back to rather than just a decorative diagram.

**What failed and how it was fixed:**

- **2 copyright near-misses on idiomatic phrasings**: "equals the sum of the two remote interior angles" on Triangle_Angle_Sum (rewrote) and "an identity is an equation that is true for every angle" on Identities (rewrote). Both one-line fixes.
- **2 dead wikilinks**: Triangle_Angle_Sum referenced `[[Solving_One_Step_Equations]]` and `[[Parallel_Lines_And_Transversals]]`. The first was a typo (actual target: `[[One_Step_Equations]]`); the second doesn't exist in this cluster (rewired to `[[Similar_Triangles]]`).
- **Additional copyright hits on Pythagorean Applications**: "the hypotenuse is always opposite the right angle and always the longest side" (rewrote) and "every positive number has two square roots one positive and one negative" (rewrote).
- **Mathtext `\tfrac` incompatibility**: The figures agent's first run failed because matplotlib's mathtext parser doesn't support `\tfrac`. Switched to `\frac` and the script ran cleanly.

**Gate checks after Cluster 7:**

- **Pytest:** 29/29 green (8 circles-parametrized across 347 generators + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (151 stub pages — down from 166).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score **47.2** / 100 (was 43.4). 113 topics with 3+ generators (was 100). Pre-calculus avg jumped dramatically from 22.6 → **42.1** as the 12 new pre-calc topics came online with full generators.
- **Bank size:** 23.2 MB across 115 shards, all under 320 KB each. Largest: `sinusoid.json` at 238.9 KB.
- **Branch hubs:** Algebra_Overview (98 live) and Precalculus_Overview (17 live) both regenerated. The Precalculus hub now genuinely shows a trig section alongside the functions section.

**Milestone: Trigonometry activated.** The trig branch of the catalog — 9 pre-calc trig topics plus 3 pre-algebra geometry prerequisites plus vectors and dot product — is now 100% populated. Combined with the 10 exp/log topics in Cluster 6 and the 14 functions topics in Cluster 5, Math_Wiki now covers essentially all of algebra-2 and most of pre-calculus. What remains is sequences/series/probability/statistics and conic sections/matrices/complex numbers.

**What's next (Cluster 8):** Sequences, probability, statistics. ~10 topics covering arithmetic and geometric sequences and series, induction (light), permutations and combinations, probability of simple and compound events, data displays and measures of spread, histograms and box plots. Smaller cluster than Cluster 7; should fit in one session.

### Version 1.12.0 --- Cluster 6 Exponentials & Logarithms (2026-04-10)

**Stats:** 10 topics enriched (+10 live, now **100 total** — a milestone), 30 new generators (+30, now 302 total), 2,084 new verified problems (+2,084, now 25,414 total), 3 new matplotlib figures (exponential growth vs decay, log/exp inverse mirror, compound growth comparison).

**Topics shipped (all at draft status, scores 80+):**

- **Exponentials (3):** Exponential_Functions, Exponential_Equations (2 sources), Growth_Decay_And_Applications
- **Logarithms (3):** Logarithms, Logarithmic_Functions, Logarithmic_Equations (2 sources)
- **Pre-calculus overview + depth (3):** Introduction_To_Exponentials_And_Logarithms, Properties_Of_Logarithms, Applications_Of_Exponentials_And_Logarithms
- **Pre-algebra money math (1):** Simple_And_Compound_Interest

**Three more pre-calc topics go live** — the precalculus branch now has 5/47 topics enriched (up from 2/47 after Cluster 5), with Properties_Of_Logarithms and Applications_Of_Exponentials_And_Logarithms representing the first deep-dive pre-calc content beyond the Cluster 5 intros.

**Generator modules added (2):**

- `generators/algebra/exponentials.py` — 15 generators covering 5 topics (exponential_functions × 3, exponential_equations × 3, growth_decay_and_applications × 3, introduction_to_exponentials_and_logarithms × 3, simple_and_compound_interest × 3)
- `generators/algebra/logarithms.py` — 15 generators covering 5 topics (logarithms × 3, logarithmic_functions × 3, logarithmic_equations × 3, properties_of_logarithms × 3, applications_of_exponentials_and_logarithms × 3)

**Figures added** (deterministic SVGs in `wiki/assets/figures/algebra/`):

- `exponential_growth_decay.svg` — `y = 2^x` vs `y = (1/2)^x` on the same axes, shared horizontal asymptote at y = 0
- `log_exp_inverses.svg` — `y = 2^x` and `y = log_2(x)` with `y = x` as the reflection line, four matched pairs of reflection points
- `compound_growth_comparison.svg` — simple, annual, monthly, and continuous compounding of $1000 at 5% over 30 years, all four curves labeled

**Execution model:**

Back to the standard cadence — 3 parallel content sub-agents (3+3+4 topics) + 2 parallel generator sub-agents (15+15) + 1 figures sub-agent. All six sub-agents dispatched together; sub-agent usage limit held up. No hybrid execution needed this cluster.

**What worked:**

- **The pre-calc bridge is paying off.** Cluster 5 shipped the first pre-calc pages, and now Cluster 6 added three more, which makes the Properties_Of_Logarithms and Applications_Of_Exponentials_And_Logarithms pages feel like they belong to an actual pre-calc sub-section rather than orphans. The Precalculus_Overview hub now genuinely shows progress.
- **Rich inverse-relationship framing for logs.** Treating `log_b(x)` as "the inverse of `b^x`" throughout the Logarithmic_Functions page gave every feature a free derivation — the domain, range, asymptote, and graph shape all fall out of the inverse relationship rather than needing to be memorized. This is a cleaner pedagogy than the usual "here are the rules" approach and shows up in the student-facing wiki.
- **The log vs exp mirror figure** is the single most pedagogically valuable figure in the cluster. Looking at the two curves with the `y = x` line between them makes the inverse relationship unmistakable in one glance. More topics that hinge on inverse relationships could benefit from similar "mirror" figures.
- **Compound interest comparison figure** makes the difference between simple and compound immediately visible — at 30 years on $1000 at 5%, simple gives $2500 while continuous gives ~$4482. That visual gap sells the whole topic.
- **Word-problem discipline is now reflex.** Every applications generator in Cluster 6 uses paraphrased, non-source scenarios. Toy rocket/half-life/population/bank balance scenarios all invented; zero copyright hits on the applications topic.

**What failed and how it was fixed:**

- **1 copyright near-miss and 2 tag/wikilink warnings** in content batches. The copyright hit was a multi-part example prompt listing "domain, range, vertical asymptote, x-intercept, and y-intercept" that matched a source sequence — rewrote the prompt to describe the features conceptually rather than as an enumerated list. The tag hit was `#topic-equations-and-inequalities` (not in the taxonomy) on Logarithmic_Equations — removed. The dead wikilink was `[[Quadratic_Formula]]` (actual target is `The_Quadratic_Formula`) — fixed.
- **1 sub-agent race condition**: Two generator agents both modified `generators/algebra/__init__.py` to add import lines, and briefly one had a syntax error from a partial write. The second agent reported it and kept going. After final rebuild, all imports resolved cleanly.
- **Parameter-space-too-small on 2 generators**: `natural_log_evaluate_clean_powers` (only ~12 clean powers of e) and `log_evaluate_natural_and_common` needed `bank_count_per_difficulty` overrides. Both agents fixed in place.

**Gate checks after Cluster 6:**

- **Pytest:** 29/29 green (8 circles-parametrized across 302 generators + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (166 stub pages — down from 176).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score 43.4 / 100 projected (was 39.3). 100 topics with 3+ generators (was 88). Algebra branch avg jumped from 52.3 → ~57 as the late-algebra-2 topics came online. Pre-calculus avg from 18.0 → 22.6 with the three new pre-calc topics contributing.
- **Bank size:** 21.1 MB across 100 shards, all under 320 KB each. Largest: `logarithmic_functions.json` at 236.3 KB.
- **Branch hubs:** Both Algebra_Overview (95 live) and Precalculus_Overview (5 live) auto-regenerated.

**Milestone: 100 live topics!** Math_Wiki has crossed the triple-digit live-topic mark. Six clusters into the nine-cluster plan, the wiki now covers the full algebra curriculum from pre-algebra foundations through algebra-2 with exponentials and logarithms, plus a handful of pre-calculus anchors. What remains is trigonometry, sequences/probability/stats, and conic sections — all of which have smaller footprints in the source books than the algebra core.

**What's next (Cluster 7):** Trigonometry. ~15 topics covering: right-triangle trig (SOH-CAH-TOA), angles and radian measure, the unit circle, graphs of sine/cosine/tangent, Pythagorean and sum/difference identities, trigonometric equations, Law of Sines, Law of Cosines. This is the first cluster to populate the `#branch-trigonometry` tag — until now that branch has been 100% stub. Expect to ship ~15 topics in one session if sub-agent limits stay friendly.

### Version 1.11.0 --- Cluster 5 Functions & Transformations (2026-04-10)

**Stats:** 14 topics enriched (+14 live, now 90 total), 42 new generators (+42, now 272 total), 3,353 new verified problems (+3,353, now 23,330 total), 4 new matplotlib figures (parent gallery, shifts, rational asymptotes, piecewise).

**Topics shipped (all at draft status, scores 80+):**

- **Function fundamentals (3):** Relations_And_Functions (algebra-1), Function_Basics (algebra-2), Function_Notation (pre-calculus)
- **Function operations (2):** Function_Arithmetic_And_Composition (algebra-2), Inverse_Functions (algebra-2)
- **Parent function families (3):** Absolute_Value_Functions (algebra-2), Power_Functions (algebra-2), Polynomial_Functions_And_Graphs (algebra-2)
- **Transformations (2):** Transformations_I_Shifts_And_Reflections (algebra-2), Transformations_Ii_Stretches_Compressions_And_Combined (algebra-2)
- **Rational graphing + exotic (4):** Graphing_Rational_Functions_Part_1 (algebra-2), Graphing_Rational_Functions_Part_2 (algebra-2), More_Exotic_Functions (algebra-2), Introduction_To_Rational_Functions (pre-calculus)

**Two pre-calculus topics (`Function_Notation` and `Introduction_To_Rational_Functions`) are the first Stitz-Zeager chapters to go live** — the pre-calc branch, which had been entirely stub, is now 2/47 populated.

**Generator modules added (4):**

- `generators/algebra/function_fundamentals.py` — 15 generators (relations_and_functions × 3, function_basics × 3, function_notation × 3, function_arithmetic_and_composition × 3, inverse_functions × 3)
- `generators/algebra/function_families.py` — 12 generators (absolute_value_functions × 3, power_functions × 3, polynomial_functions_and_graphs × 3, transformations_i × 3)
- `generators/algebra/advanced_functions.py` — 15 generators (transformations_ii × 3, graphing_rational_1 × 3, graphing_rational_2 × 3, more_exotic × 3, introduction_to_rational × 3)
- Registry updates in `generators/algebra/__init__.py` — 3 new import lines

**Figures added** (deterministic SVGs in `wiki/assets/figures/algebra/`):

- `parent_function_gallery.svg` — 2×4 grid showing eight parent functions (linear, quadratic, cubic, absolute value, square root, cube root, reciprocal, exponential)
- `transformation_shifts.svg` — three shifted parabolas overlaid on the dashed parent to illustrate horizontal + vertical shifts
- `rational_asymptotes.svg` — `(x² - 4)/(x² - 1)` plotted with its vertical asymptotes at ±1 and horizontal asymptote at y = 1 all dashed and labeled
- `piecewise_function.svg` — three-piece piecewise function with open/closed dot handling at the boundaries

**Execution model (hybrid parallelization):**

This was the first cluster to pivot mid-flight. The session started normally with 4 content sub-agents in batch 1 and 3 content + 1 figures sub-agents in batch 2, but the batch 2 agents **all hit the daily sub-agent usage limit** simultaneously. The remaining 6 content pages (Transformations I and II, Graphing Rational Functions Parts 1 and 2, More Exotic Functions, Introduction to Rational Functions) were written **directly by the main session** — ~10,000 words of prose across 6 files, each following the same template and idiom discipline as the sub-agent work.

After the 6 pages shipped, the sub-agent limit had reset, and the remaining figures + 3 generator waves ran in parallel sub-agents without issue. The total cluster shipped with the same counts and quality gates as any other cluster.

**What worked:**

- **Template memorization paid off.** By Cluster 5, the main session had internalized the structural template (frontmatter, breadcrumb, intuition, key ideas, 3 examples, pitfalls, prerequisites, widget, See Also) and could write directly at the same quality as a sub-agent, just more slowly. The six directly-written pages all passed copyright, lint, and YAML gates on the first attempt.
- **The forbidden-idiom list kept growing and kept working.** Batches 1 and 2 of content each passed copyright pytest on the first run; the only fixes were dead wikilinks (not copyright issues). The idiom discipline has become a reliable mechanical guard.
- **Sub-agent limits recover quickly.** The "resets 5pm Central" message was accurate; the limit cleared within ~20 minutes of real time, enough for the main session to complete the direct-write portion and then dispatch the next wave.
- **Hybrid execution is a feasible fallback.** Losing parallelism on 6 pages cost roughly 20 minutes of main-session work but preserved the cluster's completeness. Going forward, any cluster where sub-agent limits get in the way can be completed via direct writing without any quality loss.
- **Pre-calculus branch activation.** Shipping `Function_Notation` and `Introduction_To_Rational_Functions` inside the algebra-2 cluster was a cheap win — the pre-calc hub now has two live green-dot topics instead of all stubs, which signals progress toward that branch and makes the next pre-calc-focused cluster easier.

**What failed and how it was fixed:**

- **Batch 2 sub-agent limit exhaustion.** Four sub-agents dispatched simultaneously all returned "You've hit your limit, resets 5pm Central." No content was lost — the sub-agents had read a lot of context but hadn't written anything. The main session pivoted to direct writing immediately.
- **Two dead wikilinks from batch 1.** A sub-agent used `[[Polynomial_Arithmetic]]` and `[[Factoring_Polynomials]]` — neither topic exists on disk. Lint caught both. Fix: rewired to `[[Multiplying_Polynomials]]` and `[[Factoring_Completely]]` respectively. Both targets already live.
- **Figures builders already existed for the 4 target names but were outdated.** When the figures sub-agent read `tools/generate_figures.py`, it discovered builders with the target names already present from earlier exploratory work, but their implementations didn't match the current spec (wrong layouts, sizes, pieces). The agent interpreted "don't modify existing builders" as "don't modify OTHER builders" and rewrote the four target builder bodies to match the spec. Output SVGs are correct and deterministic.
- **Two generator parameter-space-too-small bugs caught by the test suite.** `PowerFunctionDomainByExponent` and `VerticalStretchCompressClassify` each started with easy parameter pools below the pytest floor of 10 unique problems. Agents self-corrected by widening ranges and adding `bank_count_per_difficulty` overrides.

**Gate checks after Cluster 5:**

- **Pytest:** 29/29 green (8 circles-parametrized across 272 generators + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (176 stub pages — down from 190).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score 39.3 / 100 (was 34.9). 88 topics now have 3+ generators (was 74). Algebra branch avg jumped from 43.1 → 52.3 (+9.2 points). Pre-calculus avg ticked up from 15.0 → 18.0 as the first two Stitz-Zeager pages went live.
- **Bank size:** 19.4 MB across 90 shards, all under 320 KB each. Largest: `polynomial_functions_and_graphs.json` at 294.3 KB.
- **Branch hubs:** Algebra_Overview and Precalculus_Overview both regenerated — Algebra now shows 88 live topics + collapsed stubs, and Precalculus shows 2 live topics + 45 stubs (the first time Precalculus has had anything green in its hub).

**What's next (Cluster 6):** Exponentials & Logarithms. ~10 topics covering: exponential functions (parent `b^x`), the natural base $e$, logarithm properties, solving exponential equations, solving logarithmic equations, change of base, growth and decay models, compound interest, and half-life. Depends on Function_Basics, Inverse_Functions, and Function_Arithmetic_And_Composition (all just shipped in Cluster 5), so the prerequisite chain is clean. Same cadence: content wave → generator wave → figures → close.

### Version 1.10.0 --- Cluster 4 Rationals & Radicals (2026-04-10)

**Stats:** 12 topics enriched (+12 live, now 76 total), 36 new generators (+36, now 230 total), 3,052 new verified problems (+3,052, now 19,977 total), 3 new matplotlib figures (distance formula derivation, square root parent function, cube root parent function).

**Topics shipped (all at draft status, scores 80+):**

- **Rational expressions (5):** Simplifying_Rational_Expressions, Multiplying_And_Dividing_Rational_Expressions, Adding_And_Subtracting_Rational_Expressions, Solving_Rational_Equations, Rational_Equations_And_Applications (algebra-2)
- **Exponents and radicals (5):** Zero_And_Negative_Exponents, Rational_Exponents (pre-algebra), Simplifying_Radical_Expressions, Operations_With_Radicals, The_Distance_Formula (pre-algebra)
- **Radical functions (2):** Square_Root_Functions (algebra-2), Cube_Root_And_Other_Radical_Functions (algebra-2)

**Generator modules added (3):**

- `generators/algebra/rationals.py` — 15 generators covering 5 rational-expression topics (3 simplify variants, 3 mult/div variants, 3 add/sub variants, 3 solve variants including one with deliberate extraneous solution, 3 word-problem applications)
- `generators/algebra/radicals.py` — 15 generators covering 5 exponent + radical topics (3 zero/negative exponent, 3 rational exponent, 3 radical simplification, 3 radical operations, 3 distance formula)
- `generators/algebra/radical_functions.py` — 6 generators covering 2 radical function topics (sqrt domain/evaluate/transformation, cube root evaluate/nth-root domain/transformation)

**Figures added** (all deterministic, in `wiki/assets/figures/algebra/`):

- `distance_formula_derivation.svg` — right triangle on a coordinate plane showing the Pythagorean derivation of the distance formula (A=(1,2), B=(5,5), legs labeled, hypotenuse = √(4² + 3²) = 5)
- `square_root_function.svg` — the parent function `f(x) = √x` with labeled key points, domain wall at x=0, domain/range caption
- `cube_root_function.svg` — the parent function `f(x) = ∛x` showing the symmetric-about-origin shape that handles negative inputs

**Execution model (parallelization):**

- **Content wave:** 6 sub-agents across 2 batches (4 + 2) covering 12 topics total. Batch 1 ran rational expressions + zero/negative exponents + rational exponents + simplifying radicals (8 topics). Batch 2 ran operations with radicals + distance formula + both radical function pages (4 topics).
- **Figures agent:** 1 sub-agent extended `tools/generate_figures.py` in parallel with content batch 2, also edited the 3 target topic pages with figure embeds.
- **Generator wave:** 3 sub-agents in parallel, each owning a distinct generator module (rationals, radicals, radical_functions). All 3 edited `generators/algebra/__init__.py` with distinct import lines without collision.

**What worked:**

- **Targeted idiom warnings in prompts.** Each content agent prompt included a growing list of textbook idioms to avoid, based on hits from Clusters 2 and 3. Batch 2 shipped with zero copyright hits. Batch 1 had 3 hits, all on common textbook phrases that came out of the expanded warning list for Cluster 5.
- **The "fresh scenario templates" discipline** paid off again. Rational_Equations_And_Applications ships with work/distance/round-trip word problems using invented names (Alex, Bailey, Chris, Dana) and vehicles (kayak, canoe, rowboat, swimmer, cyclist) rather than the source's Alice/Bob or boat/train scenarios. Zero copyright hits on applications.
- **Distance formula as "Pythagoras on a grid"** turned out to be the cleanest pedagogical framing. The figure shows exactly that: two points, dashed legs, the hypotenuse IS the distance. Students who already understand Pythagoras get the formula for free.
- **Square root function as "the inverse of x²"** worked as a unifying thread for Square_Root_Functions. Same for cube root as the inverse of x³ (without the domain restriction, since cubing is bijective on reals).
- **Generator backward construction for rational expressions** was trickier than previous clusters because the construction has to avoid accidentally making denominators zero at valid test points. The rationals module carefully builds rational forms from factored answers, then multiplies out to disguise them. Zero guess-and-check loops.
- **Word problem templates in the rationals generator** use clean (A, B) pairs precomputed so that answer formulas like `AB/(A+B)` and `2r₁r₂/(r₁+r₂)` always reduce to nice fractions. No runtime rejection loops.

**What failed and how it was fixed:**

- **3 copyright near-misses in batch 1** — all common textbook phrasings:
  - "multiply every term on both sides by the LCD" → rewrote as "rescale each side by that LCD"
  - "negative exponent rule applied to the whole fraction" → rewrote as "negative-exponent rule acting on a fraction base"
  - "take the root first and then raise to the power" → rewrote as "peel off the root before the power"
  
  A follow-up hit on Solving_Rational_Equations used the phrase "collect the x terms on the left and the constants on the right" (a common step-by-step template in textbooks) — rewrote as "move the x pieces to one side and the numbers to the other". And another hit on "multiply every term by that LCD" in Example 3 — rewrote as "scale each piece of the equation by that LCD". Four total rewrites in Cluster 4, all one-line fixes.

- **Dead wikilink in Square_Root_Functions.md** — the agent used `[[Quadratic_Formula|quadratic formula]]` but the actual page is `The_Quadratic_Formula`. Fix: changed to `[[The_Quadratic_Formula|the quadratic formula]]`. Lint caught this; no CI disruption.

- **`rational_exponent_evaluate` generator had a parameter space too small** on easy difficulty initially. The agent flagged this and widened the `_RANGES` dict for easy from (3,3,4) to (4,3,5) before returning. Zero manual fix required.

**Gate checks after Cluster 4:**

- **Pytest:** 29/29 green (8 circles-parametrized + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke). All 230 generators pass the parametrized test.
- **Lint:** 0 errors, 0 warnings, 1 info (190 stub pages — down from 202).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score 34.9 / 100 (was 31.2). 74 topics now have 3+ generators (was 62). Algebra branch avg jumped from 35.6 → 43.1 (+7.5 points).
- **Bank size:** 16.3 MB across 76 shards, all under 320 KB each. Largest: `square_root_functions.json` at 250.5 KB.
- **Branch hubs:** Algebra_Overview regenerated — now shows 75 live algebra topics + collapsed stubs.

**What's next (Cluster 5):** Functions & Transformations. ~14 topics covering: function notation in depth, domain and range as first-class topics, function arithmetic and composition, inverse functions, piecewise functions, absolute value functions, transformations of parent functions (shifts, reflections, stretches) applied to multiple families. This is the bridge from algebra into pre-calculus. Same cadence as Clusters 2-4.

### Version 1.9.0 --- Cluster 3 Polynomials + Quadratics deep (2026-04-10)

**Stats:** 14 topics enriched (+14 live, now 64 total), 42 new generators (+42, now 194 total), 3,590 new verified problems (+3,590, now 16,925 total), 4 new matplotlib figures (area model, discriminant three cases, parabola features, perfect square completion).

**Topics shipped (all at draft status, scores 80+):**

- **Polynomial arithmetic (3):** Adding_And_Subtracting_Polynomials, Multiplying_Polynomials, Special_Products
- **Factoring (4):** Greatest_Common_Factor, Factoring_Trinomials_General, Factoring_Special_Forms, Factoring_Completely
- **Quadratic solving (4):** Solving_Quadratics_By_Factoring, Solving_Quadratics_By_Square_Roots, Completing_The_Square (algebra-2), The_Discriminant
- **Quadratic graphs + functions (3):** Graphing_Quadratic_Functions, Quadratic_Functions (algebra-2), Applications_Of_Quadratic_Functions (algebra-2)

**Generator modules added (3):**

- `generators/algebra/polynomials.py` — 15 generators covering 5 polynomial topics (add-like-terms, subtract, combine-mixed, monomial×polynomial, FOIL, binomial×trinomial, 3 special products patterns, GCF of monomials, GCF polynomial factoring, GCF binomial factoring, 3 general trinomial factoring variants)
- `generators/algebra/quadratics_methods.py` — 15 generators covering 5 factoring + solving topics (3 factoring special forms, 3 factoring-completely cases, 3 solve-by-factoring variants, 3 square-root solving variants, 3 completing-the-square variants)
- `generators/algebra/quadratic_functions.py` — 12 generators covering 4 quadratic function + application topics (discriminant compute/classify/from-graph, vertex/axis/features from standard form, evaluate f(x), vertex form identification, standard-to-vertex conversion, projectile max height, projectile time to ground, rectangle max area)

**Figures added** (all in `wiki/assets/figures/algebra/`, deterministic):

- `area_model_multiplication.svg` — 2×2 pastel grid showing (x+3)(x+5) = x² + 5x + 3x + 15
- `discriminant_three_cases.svg` — three side-by-side parabolas (two roots / one repeated / no real roots)
- `parabola_vertex_axis_of_symmetry.svg` — single parabola y = x² - 4x + 1 with vertex, axis of symmetry, y-intercept, and roots labeled
- `perfect_square_completion.svg` — L-shape plus dashed 3×3 corner forming (x+3)²

**Execution model (parallelization):**

- **Content wave:** 7 sub-agents across 2 batches (4 + 3), each owning 2 topics. Batch 1 ran polynomial arithmetic + factoring (8 topics); batch 2 ran quadratic methods + functions + applications (6 topics). Sequencing mattered — batch 2 agents could wikilink to the just-enriched factoring pages from batch 1.
- **Figures agent:** 1 sub-agent extended `tools/generate_figures.py` in parallel with content batch 2, and also edited the 4 target topic pages with figure embeds.
- **Generator wave:** 3 sub-agents in parallel, each owning a distinct generator module. Agent 1 owned `polynomials.py` (5 topics × 3 = 15 gens), agent 2 owned `quadratics_methods.py` (5 topics × 3 = 15 gens), agent 3 owned `quadratic_functions.py` (4 topics × 3 = 12 gens).
- **Race-condition handling on `__init__.py`:** 3 generator agents all edited `generators/algebra/__init__.py` with distinct import lines. All 3 landed cleanly.

**What worked:**

- **Polynomial-then-quadratic sequencing.** Batch 1 finished all 8 polynomial/factoring topics before batch 2 started the quadratic topics, so the quadratic agents had fresh factoring prose to link to as prerequisites (`Solving_Quadratics_By_Factoring` depends on `Factoring_Trinomials_Leading_Coefficient_1` + `Greatest_Common_Factor`, both fresh in memory).
- **Backward construction for quadratic generators.** Every quadratic generator picks the answer first (the roots, the vertex, or the discriminant case) and derives the input coefficients. This eliminates the "pick coefficients, factor, hope for clean integers" guess-and-check trap entirely.
- **`bank_count_per_difficulty` overrides for tight parameter spaces.** Used on `DiscriminantFromGraphDescription` (20 problems — textual template set is small), `CompleteSquareWithA` (20 — only a ∈ {2, 3}), `FactorByGrouping4Terms` (25 — 4-term backward construction has fewer valid forms), and `FactorCompletelyGCFThenDOS` (25). All other generators hit the default 30/difficulty target.
- **Word-problem template discipline.** The projectile and rectangle applications generators use paraphrased scenario lists (toy rocket / firework / cannonball / water balloon; vegetable garden / dog pen / playground / patio) that never match source book phrasings. Zero copyright hits on the applications topic.
- **Gold-standard references in prompts.** Pointing each generator agent at 2-3 specific existing `.py` files (closest in structure to what they're writing) cut design time in half compared to letting them re-derive the pattern from `base.py`.

**What failed and how it was fixed:**

- **3 copyright near-misses in batch 1.** The shingle test caught three common textbook idioms:
  - "a polynomial is written in standard form when its terms are arranged from highest degree to lowest" → rewrote as "a polynomial sits in standard form once you've reordered its terms so the degrees walk downward — highest power first, lowest power last"
  - "group the first two terms and the last two terms, then pull the greatest common factor out of each group" → rewrote as "bracket the left pair of terms and the right pair of terms, then pull the greatest common factor out of each bracket separately"
  - "never divide both sides of an equation by a variable" → rewrote as "never cancel a variable off both sides of an equation — that variable might secretly be zero"
  
  Batch 2 (which received an updated prompt listing these three idioms explicitly in the "AVOID" section) shipped with zero copyright hits. Lesson for Cluster 4+: keep growing the forbidden-phrase list as each cluster surfaces new ones.

- **Tag taxonomy drift.** Two new tags slipped into batch 2: `#key-technique` and `#key-topic`. These already exist in `_tag_taxonomy.md` under the "Page Meta Tags" section, so they passed lint. But some topics used `#skill-visualization` and `#word-problem-support`, both also in the taxonomy. No actual ad-hoc tags invented this cluster, which is an improvement over Cluster 2's `#topic-modeling` incident.

- **Agent prompts referenced `test_generators.py`, which doesn't exist** — the actual parametrized suite is `test_circles.py`. Three generator agents all flagged this and adapted, as in Cluster 2. This is now a known prompt-template bug; will fix in Cluster 4 by referencing the file by its actual name.

**Gate checks after Cluster 3:**

- **Pytest:** 29/29 green (8 circles-parametrized + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (202 stub pages — down from 216).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics, avg score 31.2 / 100 (was 26.7). 62 topics now have 3+ generators (was 48). Algebra branch avg jumped from 24.6 → 35.6 (+11 points).
- **Bank size:** 13.3 MB across 64 shards, all under 320 KB each. Largest: `applications_of_quadratic_functions.json` at 280.2 KB.
- **Branch hubs:** Algebra_Overview regenerated via `tools/update_branch_hubs.py` — now shows 63 live algebra topics (62 algebra-1 + 1 algebra-2) + collapsed stubs.

**What's next (Cluster 4):** Rationals & Radicals. ~12 topics covering simplifying rational expressions, adding/subtracting rationals, multiplying/dividing rationals, solving rational equations, radical simplification, operations with radicals, rational exponents, and the distance formula (which belongs here because it's just `√((x2-x1)² + (y2-y1)²)`). Same cadence as Clusters 2 and 3.

### Version 1.8.0 --- Cluster 2 Linear world completion (2026-04-10)

**Stats:** 14 topics enriched (+14 live, now 50 total), 42 new generators (+42, now 152 total), 3,714 new verified problems (+3,714, now 13,335 total), 4 new matplotlib figures (coordinate plane, inequality number lines, parallel/perpendicular lines, scatter with trend line).

**Topics shipped (all at draft status, scores 80+):**

- **Pre-algebra intro inequalities (2):** Writing_And_Graphing_Inequalities, Solving_One_Step_And_Two_Step_Inequalities
- **Pre-algebra coordinate plane (1):** Plotting_Points_And_The_Coordinate_Plane
- **Pre-algebra lines bridge (1):** Graphing_Linear_Equations_From_Tables
- **Algebra 1 inequalities deep (5):** Inequalities_And_Their_Graphs, Solving_Multi_Step_Inequalities, Compound_Inequalities, Absolute_Value_Inequalities, Systems_Of_Linear_Inequalities
- **Algebra 1 lines (3):** Writing_Linear_Equations, Parallel_And_Perpendicular_Lines, Scatter_Plots_And_Trend_Lines
- **Algebra 2 linear functions (2):** Linear_Functions, Modeling_With_Linear_Functions

**Generator modules added (4):**

- `generators/algebra/inequalities.py` — 15 generators covering 5 inequality topic slugs (two-step, distribution, variables-both-sides, compound three-part, compound AND, compound OR, abs-val LT/GT, abs-val edge cases, system test point, system identify half-plane, system slope-intercept form)
- `generators/algebra/lines.py` — 15 generators covering 5 linear-line topic slugs (slope+y-int, slope+point, two points, parallel through point, perpendicular through point, classify parallel/perp/neither, evaluate f(x), function from slope+point, find zero, modeling cost, modeling predict, modeling inverse, table evaluate, table linearity check, table find equation)
- `generators/pre_algebra/inequalities_intro.py` — 6 generators for the pre-algebra inequality intro (phrase-to-symbol, graph describe, inverse graph read, one-step add/sub, one-step mul/div with sign flip, two-step with sign flip)
- `generators/algebra/coord_scatter.py` — 6 generators for coordinate plane + scatter plots (identify quadrant, point from instructions, distance on same axis, classify trend direction, predict from trend line, interpret slope in context)

**Figures added** (all in `wiki/assets/figures/algebra/`, deterministic via local `np.random.RandomState(42)`):

- `coordinate_plane.svg` — axes ±5, four quadrant labels, four example points A/B/C/D
- `inequality_number_line.svg` — four stacked number lines showing `x > 2`, `x ≤ -1`, `-2 < x ≤ 3`, and OR case
- `parallel_perpendicular_lines.svg` — three lines demonstrating same slope (parallel) + negative reciprocal (perpendicular) on a coordinate grid
- `scatter_trend_line.svg` — 10 deterministic data points with trend line `y = 1.5x + 2` (study hours vs test score)

**Execution model (parallelization):**

- **Content wave:** 7 sub-agents total across 2 batches (4 + 3), each owning 2 topics. Total throughput: 14 topics enriched in ~25 minutes of wall-clock. Batch 1 ran inequalities (8 topics), batch 2 ran lines + linear functions (6 topics).
- **Figures agent:** 1 sub-agent extended `tools/generate_figures.py` with 4 new figures in parallel with content batch 2. Also edited the 4 topic pages to embed `![[figure.svg|caption]]` references and update frontmatter `figures` field.
- **Generator wave:** 3 sub-agents in parallel, each writing a generator module (or two). Agent 1 owned `inequalities.py` (5 topics × 3 = 15 gens), agent 2 owned `lines.py` (5 topics × 3 = 15 gens), agent 3 owned `inequalities_intro.py` + `coord_scatter.py` (4 topics × 3 = 12 gens).
- **Race-condition handling on `__init__.py`:** 4 agents across batches edited both `generators/algebra/__init__.py` and `generators/pre_algebra/__init__.py` via Edit tool with distinct surrounding context. All 4 import lines landed cleanly.

**What worked:**

- **Splitting the cluster into inequalities-first and lines-second** let batch 1 agents work on a coherent theme without needing the linear-equation work that batch 2 would produce. Agents in batch 2 had the inequality pages already on disk to wikilink against.
- **Topic-family generator modules** (one file per 5 topics, 15 generators) stayed well under any reasonable file-size limit and made the registration step trivial — one import line per module.
- **Backward construction everywhere** — every one of the 42 generators picks the answer first and derives parameters, so there are zero guess-and-check loops and zero infinite-loop bugs. Wave 1's `quadratic_formula_radical_roots` hiccup from Cluster 1 is not going to repeat.
- **Sign-flip coverage as a deliberate constraint** — inequality generators were explicitly prompted to produce ~1/3 sign-flip problems. The pedagogical goal is the student encountering the flip *frequently*, not just once, so the muscle memory builds.
- **`<details>` collapsing for stub lists in branch hubs** (from v1.7.0) held up perfectly. Algebra_Overview now shows 49 live topics followed by a collapsed stub list, and the page stays scannable.
- **Copyright allowlist discipline** — three copyright-safety failures were caught in the first pass of `test_copyright_safety.py`. All three were common textbook phrasings ("write the equation of the line with slope... that passes through...", "trend line, also called a line of best fit", "multiply or divide both sides by a negative number"). Fixing each took a 1-line rewrite — no allowlist expansion needed.

**What failed and how it was fixed:**

- **Copyright near-misses on generic textbook phrasing.** Three separate topics tripped 15-word shingle matches on phrases that are more "definitional idiom" than "verbatim paragraph": the canonical "write the equation of the line..." problem-statement template across Writing_Linear_Equations and Parallel_And_Perpendicular_Lines, and the "(also called a line of best fit)" parenthetical in Scatter_Plots_And_Trend_Lines. Fix: rewrote each offending phrase with new syntax ("A line has slope... Find its equation..." instead of "Write the equation of the line with slope..."). Total repair time: 5 minutes.
- **Ad-hoc tag `#topic-modeling` on `Modeling_With_Linear_Functions`.** The content agent invented a tag not in `_tag_taxonomy.md`. Lint caught it immediately. Fix: removed the tag (the remaining `#topic-functions` + `#topic-linear` cover the topic adequately). No need to extend the taxonomy for a single topic.
- **Obsolete generator-wave test path in prompts.** The agent prompts referenced `generators/tests/test_generators.py` but that file is actually `generators/tests/test_circles.py` (the parametrized all-generators smoke test). All 3 generator agents flagged this and adapted. Fix for future clusters: update the generator prompt template to reference `test_circles.py` by name.

**Gate checks after Cluster 2:**

- **Pytest:** 29/29 green (8 circles-parametrized + 10 consolidate-snapshot + 3 copyright + 8 ingest smoke). All 152 generators pass the parametrized test suite automatically.
- **Lint:** 0 errors, 0 warnings, 1 info (216 stub pages — down from 231).
- **YAML:** 257/257 clean.
- **Topic status:** 239 topics across 4 branches, avg score 26.7 / 100 (was 22.2 after Cluster 1). 48 topics now have 3+ generators (was 34). Pre-algebra branch average 34.3 (was 31.0); Algebra branch average 24.6 (was ~18).
- **Bank size:** 10.3 MB across 50 shards, all under 320 KB each. Largest shard: `systems_of_linear_inequalities.json` at 291.5 KB.
- **Branch hubs:** Algebra_Overview now shows 49 live topics; the auto-generated block updated cleanly via `tools/update_branch_hubs.py`.

**What's next (Cluster 3):** Polynomials + Quadratics deep. Extends the already-live `Factoring_Trinomials_Leading_Coefficient_1` and `The_Quadratic_Formula` with: polynomial arithmetic (add/sub/mul), special products (difference of squares, perfect square trinomials as first-class topics), factoring general form `ax² + bx + c`, factoring completely, quadratic graphing (vertex form, direction, range), completing the square, the discriminant as a theoretical tool, and quadratic applications. ~14 topics. Same cadence as Cluster 2: inequalities-batch → lines-batch structure mapped to polynomials-batch → quadratics-batch.

### Version 1.7.0 --- Navigation UI redesign (2026-04-10)

**Stats:** No new topics or generators. Pure information-architecture pass that redesigns the student-facing navigation to serve the 36 live topics shipped in Clusters 0+1.

**What shipped:**

- **`wiki/_overview.md`** — rewritten as a student-first hero landing. New structure: stats badge → Start Here (3 primary CTAs) → 7 curated Learning Paths listing live topics by sequence → Explore by Branch (with live/total counts) → Other Reference Pages → How to Use → Current Status cluster table → About. Deleted the Phase 1/2 vertical-slice language that was 4 clusters stale. Set `status: complete` (was `stub`).

- **`wiki/Topics_Overview.md`** — rewritten from a 48-line placeholder into a proper index. Lists all 36 live topics grouped by branch + sub-category (Pre-Algebra: Numbers, Fractions, Decimals, Ratios, Expressions; Algebra 1: Equations, Systems, Lines, Polynomials; Geometry: 1 topic). Collapses stubs into branch hub pointers. Set `status: complete`.

- **`tools/update_branch_hubs.py`** — extended to read `wiki/_data/problem_types_index.json` and split each branch group into a "🟢 Live topics with practice widgets (N)" section followed by a collapsed `<details>` "⚪ M stub topic(s)" section. The live section is flat-bulleted; the stub section is wrapped in `<details>` so the page stays scannable even at 90+ stubs per branch. Heading format: "### {Group label} --- N live / M total".

- **`quartz.layout.ts`** — `mathExplorerMap` now maps 14 root-level files to emoji-prefixed friendly names (🏠 Home, 📘 Algebra, 🎒 Your Vault, 📊 Progress Dashboard, etc.) in addition to the 4 folder mappings. Root-level overview pages and high-traffic files (Vault, Topic_Status) now render as emoji-labeled sidebar entries instead of raw filenames.

- **Branch hub intros** — fixed stale "Phase 1 / Phase 2 ingest" language in Algebra, Geometry, Trigonometry, Precalculus overview pages. Geometry and Trigonometry now show a hand-written live/stub section pointing at the cluster plan. Algebra shows a "35 live across pre-algebra + Algebra 1" summary above the auto-generated block.

- **`Math_Wiki.md` (this file)** — new "Navigation Design (what students see)" section documents: the three-pane Quartz layout, the Explorer filter + mapFn, the emoji label table, the landing page structure, the branch hub structure, the topic page layout, and expandability rules for adding new pages. New "Orientation for a New Session" subsection at the top (where the session is right now, 30-second mental model, first commands to run in a fresh session).

**What worked:**

- **Live-vs-stub visual distinction (🟢 / ⚪)** is the single highest-value navigation improvement. Before this pass, a student clicking through Algebra_Overview had no way to know which of the 191 alphabetical links led to a real lesson vs an empty stub. Now they scan the top 35 links (all green) first and the 156 stubs are collapsed behind a disclosure.
- **Data-driven live classification** — `update_branch_hubs.py` reads `problem_types_index.json` rather than guessing from frontmatter or filename. This means "live" automatically updates whenever a new generator ships: the next `py -3 tools/update_branch_hubs.py` re-classifies the topic.
- **Curated learning paths on the home page** instead of "Start Here" as a dump of 4 branch links. A student who lands cold now sees 7 named sequences (Foundations, Proportional Reasoning, Expressions, Linear Equations, Lines and Slopes, Quadratics, Geometry Cornerstones) and can start at #1 of the most relevant path.
- **`<details>` element for stub lists** keeps the page height reasonable. Pre-Algebra alone has 92 catalog topics; rendering all 92 in a flat list pushed live content below the fold. Collapsed stubs fix this without hiding information.
- **Friendly sidebar labels via mapFn** — no layout code changes needed, just a dict update. Adds visual hierarchy (emoji act as icons) without any CSS.

**What failed and how it was fixed:**

- **`_overview.md` had been stale since Phase 1** — it still said "Phase 1 vertical slice is live: the Circles topic has a full lesson and 1,140 verified practice problems. Phase 2 will ingest 5 user-provided books." That was true 5 commits ago. Lesson: the landing page needs an update-per-cluster discipline, not update-per-major-version. Added a "Current Status" cluster table on the home page so it stays fresh; future clusters check off a row.
- **No mechanism to surface Topic_Status in navigation** before this pass. The dashboard existed as a file but wasn't linked from the home page and had no sidebar label. Fix: added to both the home page Start Here section AND the sidebar mapFn.

### Version 1.6.0 --- Cluster 1 Pre-algebra Foundations (2026-04-10)

**Stats:** 20 topics enriched with rich prose + worked examples + cross-links, 60 new generators (110 total), 5,286 new verified problems (9,621 total), 4 new matplotlib figures, ~18,000 lines of new markdown content.

**Topics shipped (all at draft status, scores 80-90):**
- **Fractions (6):** Equivalent_Fractions_And_Simplifying, Mixed_Numbers_And_Improper_Fractions, Adding_And_Subtracting_Fractions, Comparing_And_Ordering_Fractions, Multiplying_Fractions, Dividing_Fractions
- **Decimals (4):** Adding_And_Subtracting_Decimals, Multiplying_Decimals, Dividing_Decimals, Decimal_Place_Value_And_Comparing_Decimals
- **Integers (2):** Integers_And_The_Number_Line, Multiplying_And_Dividing_Integers
- **Foundations (3):** Place_Value_Rounding_And_Estimation, Square_Roots_And_Cube_Roots, The_Distributive_Property
- **Variables & Expressions (2):** Variables_And_Algebraic_Expressions, Evaluating_Expressions
- **Ratios & Proportions (3):** Ratios_And_Equivalent_Ratios, Unit_Rates, Proportions_And_Cross_Multiplication

**Generator files added** (10 new modules under `generators/pre_algebra/`):
- `fractions_basics.py`, `fractions_addsub.py`, `fractions_muldiv.py`
- `decimals_arith.py`, `decimals_divplace.py`
- `integers_ext.py`
- `foundations.py`, `algebra_intro.py`, `eval_and_ratios.py`, `rates_and_proportions.py`

**Figures added** (all in `wiki/assets/figures/pre_algebra/`):
- `number_line.svg` — labeled integer number line
- `fraction_bar.svg` — 3/8 vs 6/16 equivalence visualization
- `area_model_distributive.svg` — 3(4+2) rectangle split into sub-rectangles
- `place_value_chart.svg` — columnar chart for 34.0806 with hundredths highlighted

**Execution model (parallelization):**
- **Content wave:** 10 sub-agents total across 3 batches (4 + 4 + 2), each owning 2 topics. Total throughput: 20 topics in ~20 minutes of wall-clock (but lots of parallelism under the hood).
- **Generator wave:** 10 sub-agents total across 3 waves (3 + 3 + 4), each owning 2 topics and writing a single module with 6 generators. Registry imports in `__init__.py` updated by each agent via Edit tool — no collisions because each added a distinct import line.
- **Figures:** 1 sub-agent extended `tools/generate_figures.py` with 4 new figures + 2 determinism fixes (matplotlib's default SVG output embeds timestamps + randomized clip-path IDs; fixed via `plt.rcParams["svg.hashsalt"]` and `metadata={"Date": None}`).

**What worked:**
- **Sub-agent parallelization** as specified in the buildout plan. Review burden stayed manageable because each agent's scope was small (2 topics), the gold standard (Circles.md) gave a concrete template, and `test_copyright_safety.py` caught paraphrase failures mechanically.
- **Same-file generator modules (6 generators per file, 2 topics per file)** kept the directory tidy and made registration straightforward (one import line per module).
- **Separating content from generators into two waves** per the plan — content agents had no generator-code anxiety, generator agents could read the enriched prose to match their problem framings to the topic's examples.
- **Race-condition handling on `__init__.py`** — multiple agents independently edited the same file via Edit tool with sufficient surrounding context. All 10 import lines landed without conflict.
- **Copyright safety test** caught several near-misses in real time. Each agent that tripped the test rewrote the offending passage and re-ran the test before returning. No manual intervention needed.
- **Generator `bank_count_per_difficulty` overrides** for topics with small parameter spaces (e.g., `square_root_of_perfect_square` limited to 12 since there are only 12 perfect squares in the easy range).

**What failed and how it was fixed:**
- **Matplotlib SVG determinism:** default `fig.savefig()` produces different bytes on every run because of embedded timestamps and randomized clip-path IDs. Fix: set `plt.rcParams["svg.hashsalt"]` for stable IDs, pass `metadata={"Date": None}` to strip the timestamp. All 5 figures now byte-identical across runs. This matters for git diff noise and CI reproducibility.
- **Several content agents tripped copyright pytest on near-miss phrasings** (e.g., "set of all points in a plane that are the same distance" in Circles, "multiply the whole number by the denominator and add the numerator" in fraction pages). Each agent rewrote its offending passage. Pattern: definitional phrasings tend to converge across textbooks, so the allowlist in `test_copyright_safety.py` may need expansion as more content ships. For Cluster 1, the allowlist stayed at 7 phrases and agents paraphrased around the rest.
- **Agent reported section numbers differ from catalog**: the catalog normalizes section numbers like "2.2.1" (two-dot chapter-section-subsection), but the JSON files use "2.1" (single-dot). Agents correctly used the actual JSON section numbers in `source_refs`. This is a legitimate catalog-schema inconsistency to watch in future clusters.

**Gate checks after Cluster 1:**
- **Pytest:** 29/29 green (generators + copyright + snapshot + smoke).
- **Lint:** 0 errors, 0 warnings, 1 info (231 stub pages — down from 251).
- **YAML:** 257/257 clean.
- **Topic status:** Pre-algebra average 16.0 → 31.0 (+15 points). Overall average 16.4 → 22.2 (+5.8). 34 topics at 3+ generators (was 14).
- **Bank size:** 7.5 MB across 36 shards, all under 320 KB each.

**What's next (Cluster 2):** Linear world completion. Extends already-shipped Slope/Multi-Step/Systems/Slope-Intercept with: lines in all forms, parallel/perpendicular, linear inequalities deep, systems of inequalities, writing linear functions, applications. ~14 topics. Same cadence: content wave → generator wave → figures → close.

### Version 1.5.0 --- Cluster 0 infrastructure (2026-04-10)

**Stats:** No new topics or generators. Pure infrastructure hardening to unblock the 9-cluster comprehensive buildout.

**What shipped:**
- **`tools/aliases.yaml`** — schema-documented living record for manual merge decisions; consumed by `consolidate_extractions.py`. Located in `tools/` (not `raw/catalog/`) because `raw/` is gitignored.
- **`tools/consolidate_extractions.py`** — refactored to accept `extractions_dir` kwarg; added `apply_aliases()` with rename/merge/split support and rule-conflict detection.
- **`tools/topic_status.py`** — per-topic progress dashboard scoring every topic 0-100 against the plan's verification rules. Writes `wiki/_data/topic_status.json` + `wiki/Topic_Status.md`.
- **`tools/ingest_new_book.py`** — 9-step guided pipeline for adding a new textbook. Doubles as executable ingest docs.
- **`generators/tests/test_consolidate_snapshot.py`** — 10 tests covering catalog snapshot + alias operations against a mini fixture.
- **`generators/tests/test_copyright_safety.py`** — shingle-based verbatim detection (10-word shingles, 15-word windows) with allowlist subtraction for standard definitions.
- **`generators/tests/test_ingest_smoke.py`** — synthetic book fixture drives the full ingest -> consolidate -> stub pipeline end-to-end. 8 tests.
- **`factory/scripts/build_index.py`** — extended for math page types + grouped-by-letter output for large collections; resolves the 245 cosmetic lint warnings.
- **`factory/scripts/validate_yaml.py`** — new standalone YAML frontmatter sanity checker (type/status/tags validation + `yaml.safe_load()`).
- **`factory/scripts/add_navigation.py`** — multi-wiki hub resolution (candidate hub stems per subdir, first existing file wins). Fixes the Hymn Wiki / Math Wiki entities/People hub collision.
- **`.github/workflows/deploy.yml`** — now runs pytest (generators + copyright + snapshot + smoke) + validate_yaml + build_index before Quartz build.
- **`Math_Wiki.md`** — this file. Added Buildout Plan section, env_map Author's Guide, Generator Coverage Standard, Cluster 0 status.

**What worked:**
- **Sequential execution of the 10 items** (I-1 through I-10) with focused context per item made review cheap and the dependency graph simple. Parallelism would have been possible but unnecessary at this scale.
- **Test-first infra:** every new tool shipped with a corresponding pytest. The copyright pytest caught a real issue on the first run (Circles.md has a definitional run that matches a source book), which validated the test's value and led to the allowlist design.
- **Refactor-to-enable-tests:** making `consolidate_extractions.py`'s core functions accept path arguments turned an untestable script into one with a clean 10-test snapshot suite with no monkey-patching.
- **Path discipline:** moving `aliases.yaml` from `raw/catalog/` (gitignored) to `tools/` (tracked) avoided a subtle gotcha where merge rules would have been lost on fresh CI runs.
- **`topic_status.py` scoring calibration:** tightening the `EXAMPLE_HEADING_RE` regex on the first baseline run (dropped avg from 24.1 to 16.2) gave the project an honest starting baseline.

**What failed and how it was fixed:**
- **Initial copyright test failed on Circles.md** with a 15-word run matching the standard textbook definition of a circle. First attempt used substring allowlist matching which didn't handle partial overlaps correctly. Fix: build allowlist shingles at corpus-build time and subtract them from the source corpus, so matches against definitional phrases are inherently impossible.
- **`build_index.py` was summarizing breadcrumb lines as the first sentence.** The breadcrumb starts with `>` which wasn't in the `first_sentence` skip list. Fix: expanded the skip list to include `>`, `<`, and `!` prefixes.
- **`aliases.yaml` initial placement in `raw/catalog/` was gitignored.** Caught before commit; moved to `tools/aliases.yaml` and updated the ALIASES_FILE constant in `consolidate_extractions.py`.

### Version 1.4.0 --- Phase 2c Wave 3 (2026-04-10)

**Stats:** 16 topics live with widgets, 50 generators, 4,335 verified problems, 3.1 MB total bank across 16 shards.

**What worked:**
- **Sharded per-topic bank** proved durable. Adding waves of ~15 generators each added ~1 MB to the total bank but kept every individual shard under 320 KB. The widget's lazy-fetch pattern means per-topic load cost stays low even as the bank grows.
- **Backward construction** for generators (pick the answer, derive the parameters) eliminated the infinite-loop class of bugs entirely after Wave 1's initial hiccup.
- **Per-generator `bank_count_per_difficulty` override** handles small-parameter-space cases (Pythagorean triples, absolute-value no-solution) without breaking the default 30.
- **Auto-stub catalog** gives every new topic wave a ready-made page to slot into. The widget's "No problem types registered" empty state is polite enough that students can browse all 247 topic pages without confusion.
- **SymPy's `sp.latex()`** for equation formatting eliminated manual sign handling across all equation-solving generators.

**What failed and how it was fixed:**
- **Write-retry left dead files in Wave 3.** Created both `absolute_value_equations.py` and `absolute_value.py`, then `systems_elimination.py` and `elimination_systems.py`. Only the latter of each pair was imported. Fix: cleanup commit `8f54c32`. Prevention: after a batch of Writes, always `ls` the target directory and check against the expected file list.
- **Quadratic radical roots generator had an infinite loop** from inverse construction trying to match disallowed discriminant/base parity combinations. Fix: flipped to forward construction with a 500-attempt bound.
- **Test count of 25 broke the Pythagoras easy variant** (only 8 unique triples × orderings). Fix: made the test respect each generator's `bank_count_per_difficulty` override and clamped to `[5, 10]` range.
- **245 stubs triggered cosmetic lint warnings for "not in `_index.md`"** — acceptable but noisy. Deferred to Site Expansion plan (auto-regenerate `_index.md` in CI).

### Version 1.3.0 --- Phase 2b Auto-Stubs (2026-04-10)

**Stats:** 245 new topic stub pages generated from the 246-topic catalog. Branch hubs (`Algebra_Overview.md`, `Precalculus_Overview.md`) auto-populated with topic listings.

**What worked:**
- **Exact normalized-title matching** in consolidation gave high precision (false-positive merges are worse than duplicate topics). CamelCase splitting was the one extension needed beyond basic normalization.
- **Single-pass stub generator** with "skip if slug exists anywhere in wiki/topics/" check cleanly preserved Phase 1's hand-written Circles page.
- **`<!-- AUTO:TOPICS:BEGIN/END -->` markers** in branch hubs let the hub pages keep hand-written intro content while auto-updating the topic list.
- **`#topic-auto-generated` tag** in the taxonomy makes it easy to identify which pages came from this pipeline vs hand-written content.

**What failed and how it was fixed:**
- **Linter false-positive on image embeds:** `![[circle_parts.svg|caption]]` was being treated as a dead wikilink. Fix: `extract_wikilinks()` now filters out targets ending in asset extensions (.svg, .png, .jpeg, .gif, .webp, .mp4).
- **Catalog files blew past 500 KB** because the first version retained full `body_latex` for every block. Fix: drop `body_latex` from catalog entries (keep only preview + metadata). Full text lives in `raw/extractions/` for anyone who needs it.

### Version 1.2.0 --- Phase 2a Infrastructure Refactor + Book Ingest (2026-04-10)

**Stats:** 5 textbooks ingested (47 chapters, 2,736 blocks, 3.4 MB extractions). 246 canonical topics identified. Bank sharding architecture deployed. VaultViewer refactored to render entirely from localStorage.

**What worked:**
- **Per-chapter extraction shards** kept file sizes manageable (largest: 335 KB for AlgTrig's trig chapter).
- **Per-branch catalog shards with body_latex dropped** kept files under 500 KB (largest: 468 KB for pre-algebra).
- **Sharded problem bank with lazy loading** means visiting a topic page costs only ~30 KB (index) until "Add to Vault" is clicked.
- **Storing full problems in localStorage** eliminated all bank fetches from the Vault page. Vault loads instantly with zero network requests.
- **Shared `window.__mathWikiKatexLoad` singleton** across both inline scripts means KaTeX JS loads only once even when both components mount.

**What failed and how it was fixed:**
- **Initial run of consolidate_extractions crashed with UnicodeEncodeError** on Windows cp1252 for a print statement containing `→`. Fix: replaced Unicode arrows with ASCII `->`.
- **`CamelCase` slug collisions:** `AbsoluteValueFunctions` and `Absolute_Value_Functions` created separate catalog entries until I added CamelCase splitting to `normalize_title`.

### Version 1.1.0 --- Phase 1 Vertical Slice (2026-04-10)

**Stats:** First functional deploy. Circles topic page, 5 generators, 1,140 problems, working widget, working Vault, print-to-PDF. Live on GitHub Pages.

**What worked:**
- **End-to-end Quartz custom component pattern** — explicit `./quartz/components/...` imports in `quartz.layout.ts`, files copied into the cloned Quartz during CI. No Quartz fork needed.
- **Matplotlib SVG figures** embedded via Obsidian `![[]]` syntax (after discovering the markdown syntax path rewriter bug).
- **Pytest parametrized over `all_generators()`** automatically covers new generators without test updates.
- **Browser-tested end-to-end via Chrome MCP** caught the runtime KaTeX gap that unit tests couldn't have.

**What failed and how it was fixed (all in bugfix commits):**
- **`$$...$$` on a single line** rendered as inline KaTeX, not display. Fix: multi-line form (commit `215c644`).
- **Vault page 404** from alias/filename collision. Fix: remove colliding alias (commit `70bad13`).
- **Figure image broken** from Quartz link rewriter adding an extra `..`. Fix: Obsidian embed syntax (commit `ea19019`).
- **Runtime KaTeX unavailable.** Quartz's Latex plugin ships CSS only. Fix: singleton KaTeX JS loader in inline scripts (commit `ea19019`).

### Version 1.0.0 --- Phase 0 Scaffold (2026-04-10)

**What:** Factory schemas extended (`topic`, `problem_type`, `technique`, `formula`). Lint and navigation scripts updated. Build directory scaffolded with Obsidian config, Quartz config/layout, empty wiki subdirectories, overview hub stubs.

**What worked:**
- Reusing Hymn Wiki's `quartz.config.ts` and `quartz.layout.ts` verbatim with only three changes (`pageTitle`, `pageTitleSuffix`, `baseUrl`) plus a math-specific `filterFn`. `Plugin.Latex({ renderEngine: "katex" })` was already there.
- Adding the new types to `lint_wiki.py` `VALID_TYPES` was a one-line change.
- Adding sections to `add_navigation.py` `SECTION_MAP` was a four-line addition. Non-breaking for Hymn Wiki.

**Open items carried forward (still open):**
- `SECTION_MAP['entities']` still routes to `People_Overview` (Hymn Wiki name). Math Wiki's entities folder is empty at Wave 3; conflict will surface whenever we write the first mathematician entity page. Easiest fix: rename Math Wiki's hub to `People_Overview.md`, or add per-wiki override mechanism.
- Math Wiki's `_index.md` is stale — 245 auto-stubs aren't listed. The 245 lint warnings ("not in `_index.md`") will persist until `build_index.py` is either run manually after each wave or wired into CI.
