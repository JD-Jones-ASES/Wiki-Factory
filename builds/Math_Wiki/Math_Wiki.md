# Math_Wiki.md --- A Practice-First Math Wiki & Tutor
## From Pre-Algebra through Pre-Calculus, with procedurally generated practice
### Version 1.5.0 --- Cluster 0 infrastructure shipped (2026-04-10)

| Field | Value |
|-------|-------|
| **Domain** | Middle and High School Mathematics |
| **Scope** | Pre-Algebra, Algebra 1, Geometry, Algebra 2, Trigonometry, Pre-Calculus. Calculus & Statistics deferred (books don't cover them). |
| **Audience** | Students grades 6--12. Warm, encouraging, clear. Tutor-adjacent, not textbook-formal. |
| **Source count** | 5 textbooks (see Source Inventory below) |
| **Scale** | Live: 16 topics with working widgets, 50 generators, 4,335 verified problems. Catalog: 246 canonical topics (~230 still need generators). |
| **Comprehensive buildout plan** | 9-cluster schedule; see "Buildout Plan" section below. |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD |
| **URL** | https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/ |

---

## Orientation for a New Session

**Read this file top to bottom before doing anything else.** It is the single source of truth for what exists, what works, and what's next.

### Quick start commands

All commands run from `builds/Math_Wiki/`:

```bash
cd builds/Math_Wiki

# Sanity checks (do these first)
py -3 -m pytest generators/tests/                # generators + copyright + snapshot + smoke (29/29)
py -3 tools/build_problem_bank.py                # should succeed, ~16 shards
py -3 tools/topic_status.py                      # progress dashboard (writes wiki/Topic_Status.md)
py -3 ../../factory/scripts/validate_yaml.py wiki/  # YAML frontmatter sanity
py -3 ../../factory/scripts/build_index.py wiki/    # regenerate wiki/_index.md
py -3 ../../factory/scripts/lint_wiki.py wiki/      # 0 errors expected

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

# Regenerate branch hub pages' auto-generated topic lists
py -3 tools/update_branch_hubs.py

# Regenerate matplotlib figures
py -3 tools/generate_figures.py
```

### Where things live

| Path | What |
|---|---|
| `raw/books/{math_1,math_2,algebra_1,algebra_2,algtrig}/` | Original LaTeX source (gitignored, ~62 MB) |
| `raw/extractions/{book_slug}/chapter_NN.json` | Per-chapter parsed blocks (gitignored, ~3.4 MB) |
| `raw/catalog/topics_{branch}.json` | Per-branch canonical topic catalog |
| `raw/catalog/index.json` | Catalog summary with counts by branch |
| `wiki/topics/{pre_algebra,algebra,precalculus,geometry}/` | Topic pages (auto-stubs + hand-written) |
| `wiki/formulas/` | Formula pages (currently just Pythagorean_Theorem stub) |
| `wiki/_data/problem_types_index.json` | Widget lookup: topic_slug → [generators] |
| `wiki/_data/problems/{topic_slug}.json` | Per-topic problem shards (committed) |
| `wiki/assets/figures/{branch}/` | Matplotlib SVGs |
| `wiki/Vault.md` | Interactive vault page (mounts VaultViewer) |
| `wiki/{Algebra,Precalculus,Geometry,Trigonometry}_Overview.md` | Branch hubs (auto-populated blocks) |
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
| **0** | Infrastructure hardening + global alias merge | 0 | **shipping in this session** |
| **1** | Pre-algebra foundations | ~18 | pending |
| **2** | Linear world completion | ~14 | pending |
| **3** | Polynomials + Quadratics deep | ~14 | pending |
| **4** | Rationals & Radicals | ~12 | pending |
| **5** | Functions & Transformations | ~14 | pending |
| **6** | Exponentials & Logarithms | ~10 | pending |
| **7** | Trigonometry | ~15 | pending |
| **8** | Sequences, probability, statistics | ~10 | pending |
| **9** | Conics, matrices, complex numbers, vectors | ~12 | pending |
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
