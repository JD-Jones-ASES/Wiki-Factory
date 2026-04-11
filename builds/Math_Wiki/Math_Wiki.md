# Math_Wiki.md --- A Practice-First Math Wiki & Tutor
## Student-facing, course-based navigation from middle school through pre-calculus
### Version 2.4.0 --- Zero-Stub Phase: big merge cleanup + 12-topic activation + Vault PDF export + example-heading fix. (2026-04-11)

| Field | Value |
|-------|-------|
| **Domain** | Middle and High School Mathematics |
| **Scope** | Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus (through conics, matrices, complex numbers). Calculus + advanced statistics deferred. |
| **Audience** | Students grades 6-12. Warm, tutor-adjacent tone. Intuition first, formalism second. Now also: SAT / PSAT / ACT / CLT test-takers. |
| **Presentation** | **Standalone wiki.** No "paraphrased from textbooks" language in student-facing content. Internal `raw/books/` and `raw/extractions/` remain as build inputs but never surface in wiki output. |
| **Scale** | **220 live topics / 677 generators / 52,763 verified problems / 66 figures / 0 stubs** |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD, ~2 min build time |
| **URL** | https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/ |
| **Status** | v2.4.0 **zero-stub phase shipped.** First time in the build that every topic on disk is live (220/220). Overall average score **71.6 → 90.1**; every branch ≥ 89. 219/220 topics carry at least one test tag (`Induction` is intentionally unmapped). Vault now has **Save as PDF** via a lazy jsPDF + html2canvas pipeline with KaTeX-aware rendering. Remaining: 3 deferred Vault polish items (worksheet builder, input-and-check grader, difficulty auto-tune) and optional new-book ingests. |

---

## Orientation for a New Session

**Read this file top to bottom before touching anything.** The history of how we got here has been compressed; what remains is the state you need to keep building safely.

### First commands in a fresh session

```bash
cd /c/Wiki_Factory/builds/Math_Wiki

# Sanity check: all four should be green
py -3 -m pytest generators/tests/ -q                # 29/29 passing
py -3 ../../factory/scripts/validate_yaml.py wiki/  # 234/234 clean
py -3 ../../factory/scripts/lint_wiki.py wiki/      # 0 errors, 0 warnings
py -3 tools/topic_status.py                         # avg ~90.1, 220 live topics, 0 stubs
```

If any of those fail, something has regressed — fix that before doing anything else.

### 30-second mental model

Math_Wiki is a **standalone, practice-first wiki**. Every live topic page has (a) clear original prose with worked examples and (b) an interactive problem-vault widget fed by SymPy-verified Python generators. Students read → add problems to a browser-local Vault → download worksheets. The site deploys to GitHub Pages via Quartz v4 on every push to main.

Navigation is **course-first**. Five course hubs (Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus & Trig) are the student's primary entry points. A 7th grader opens Middle School Math; a sophomore opens Algebra 2. Branch-level organization still exists in the underlying data model but is hidden from the student-facing sidebar.

Ten content clusters shipped the initial buildout; v2.2-v2.4 finished the long tail via stub activation waves, merge cleanup, and one multi-topic quality bump. The wiki runs a **PrereqWidget** ("Review these first" card) in the right sidebar on every topic page, powered by YAML `prerequisites:` frontmatter. The Vault supports JSON export/import and **Save as PDF** — a lazy jsPDF + html2canvas pipeline that renders KaTeX off-screen, snapshots to canvas, and slices into US-Letter pages with the answer key on its own page.

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
| `wiki/assets/figures/{branch}/*.svg` | 62 matplotlib SVG figures across branches |
| `generators/{algebra,pre_algebra,precalculus,geometry}/*.py` | 638 generators across 4 branch packages (82 modules total) |
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

**Wiki** (`wiki/`) — LLM-owned markdown. 210 live topic pages + 51 leftover stubs + 5 course hubs + problem bank shards + prereq graph + standardized-test tag overlay (~200 topics carry `#test-{sat,psat,act,clt}`).

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
- **VaultViewer** mounts on `/Vault` (element id `vault-mount`). Renders the current localStorage vault with hints, answers, solution steps, and the action row. The **Save as PDF** button uses two more lazy CDN singletons — `ensureJsPdf()` (jspdf@2.5.1 UMD) and `ensureHtml2Canvas()` (html2canvas@1.4.1), both mirroring the `ensureKatex()` pattern exactly. On click: build an off-screen `.vv-pdf-offscreen` DOM, run `renderKatexIn()`, await `document.fonts.ready` + one `requestAnimationFrame`, snapshot via `html2canvas(scale: 2, useCORS: true)`, slice the tall canvas into US-Letter page-height strips, and emit `math-wiki-worksheet-YYYY-MM-DD.pdf`. A `doc.addPage()` between problems and answer key forces the key onto a fresh page. On CDN failure the catch-path falls back to `window.print()` against the preserved `@media print` stylesheet (Ctrl+P still works too).
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
├── algebra/                   # 35 modules, ~270 generators
│   (linear equations, slopes, systems, absolute value, quadratic methods,
│    polynomials, factoring, rationals, radicals, functions & families,
│    transformations, exponentials, logarithms, piecewise, probability,
│    stats inference, stats displays, ratios_and_proportions_algebra,
│    variables_and_expressions, scientific_notation, coordinate_plane_intro)
├── pre_algebra/               # 22 modules, ~190 generators
│   (integers, fractions, decimals, percents, ratios, order of operations,
│    algebra intro, inequalities intro, slope intercept, absolute value ops,
│    exponents intro, real numbers, midpoint, word translation, number theory)
├── precalculus/               # 13 modules, ~140 generators
│   (trig core + advanced, sequences & stats, conics & complex, matrices,
│    function foundations, polynomial foundations, graphs_of_rational,
│    polar_parametric, trig_inequalities, relations, nonlinear_systems)
├── geometry/                  # 12 modules, ~60 generators
│   (circles, pythagoras, parallel_lines, triangle_congruence,
│    special_right_triangles, polygon_angles, quadrilaterals, circle_theorems,
│    transformations, volume, surface_area, coord_geometry)
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

8. **Parameter space needs ≥30 unique problems per difficulty** or set `bank_count_per_difficulty = N`. Pytest's floor is **5 unique problems per difficulty** — `bank_count_per_difficulty` must be ≥ 5, and the *actual* number of unique outputs at each difficulty must be ≥ `min(10, bank_count_per_difficulty)`. Count your real parameter-space cardinality before shipping. v2.3.0 shipped 6 generators that declared `bank_count = 20` but only produced 6-9 unique outputs at easy difficulty — each needed a post-hoc floor reduction. Agent prompts should explicitly ask: "if your parameter space is < 10, set `bank_count_per_difficulty = actual_count`."
9. **Backward construction beats forward.** Pick the answer first (integer roots, Pythagorean triples, clean unit-circle values), derive the parameters. Forward construction with retries can infinite-loop on edge cases. Concrete anti-pattern that shipped in v2.3.0 and hung pytest for 60s: `while True: a = rng.randint(...); if numerator % a == 0: break`. Rewrite rule: if you find yourself writing a `while True` that retries until a cleanliness/divisibility condition holds, that's a red flag. Pick the clean output first, derive the parameters.
10. **Use `sp.latex(sp.Eq(...))` for signed equations** — handles negative coefficients correctly where string formatting does not.
11. **Named tags, not freehand.** Use `#skill-algebraic-manipulation`, `#skill-visualization`, `#word-problem-support` etc. from the taxonomy. Inline the FULL taxonomy (all 7 sections as of v2.3.0) in every agent prompt — don't just reference the file. v2.3.0 had 3 ad-hoc tags (`#skill-equation-solving`, `#skill-modeling`, `#skill-proportional-reasoning`) slip past because the prompts listed only the most common skill tags. Copy the taxonomy wholesale.

### Process rules

12. **Don't trust write retries.** If a file write fails and you retry with a different name, **check for dead siblings** afterward. Lost an hour in Cluster 2 to two orphaned generator files sitting next to the real ones.
13. **`py -3` on Windows.** Not `python`, not `python3`.
14. **`builds/*/raw/` is gitignored.** The 62 MB of textbook source stays local by design. Don't try to `git rm` it.
15. **CI runs pytest + validate_yaml + build_index before Quartz.** A broken test fails the deploy. Fix local before pushing.
16. **Rewrite the hub script before deleting old hubs.** Cluster 10 planning caught this: `update_course_hubs.py` must exist and point at the new hub filenames before you delete `Algebra_Overview.md` etc. Otherwise the old script errors or silently no-ops.
17. **Breadcrumb sweeps touch every topic file.** A breadcrumb rewrite script needs `--dry-run` mode and a unified-diff preview before execution. One bad regex and every topic's navigation breaks. Phase 1's `rewrite_breadcrumbs.py` is the template.
18. **Cross-branch wikilinks must use the canonical live-topic slug + pipe display.** Wave C3 shipped 10 dead wikilinks to invented names (`[[Scatter_Plots]]` → should be `[[Scatter_Plots_And_Trend_Lines|Scatter Plots and Trend Lines]]`, `[[Correlation]]` → doesn't exist, `[[Functions_And_Relations]]` → should be `[[Relations_And_Functions|...]]`, `[[Substitution_Method]]` → should be `[[Solving_Systems_By_Substitution|...]]`, `[[Quadratic_Equations]]` → should be `[[The_Quadratic_Formula|...]]`, `[[Conic_Sections]]` → should be `[[Introduction_To_Conics]]`). Prevention: inline the live-topics list in every agent prompt **organized by branch**, and state explicitly: "cross-branch links use pipe form `[[Target|Display]]`; never invent a target name."
19. **Frontmatter `related:` and `prerequisites:` paths use `topics/{branch}/Name` form** — not `topics/{branch_underscored_hyphenated}/Name`. Wave C3 had several `topics/algebra_1/Slope` entries (wrong) instead of `topics/algebra/Slope`. These are informational in the graph (don't break lint) but break the prereq widget. Use the ACTUAL directory name.
20. **`### Example N` H3 headings, never `**Example 1.**` bold-inline** *(content)*. `topic_status.py`'s example counter matches `^##+\s+(?:worked\s+)?example(?:\s+\d+|\s*:|\s*$)` — bold-inline markers silently score zero. v2.4 found 37 topics stuck at 75 because they used `**Example 1.**` bodies; the one-shot `tools/fix_example_headings.py` rewrote all three observed variants (bare `.**`, paren-descriptor `(X).**`, dot-descriptor `. X.**`) to `### Example N[: descriptor]`.
21. **Duplicate `generator_id` silently shadows** *(generator)*. If two `@register` classes share an id, import order decides the winner — the loser is dead code never in the registry. v2.4 found a duplicate `projectile_max_height` in `applications_of_quadratics.py` shadowed by the canonical one in `quadratic_functions.py`; the stub looked like it had 3 gens when it had 2. Verify with `py -3 -c "from generators.base import all_generators; print([g for g in all_generators() if g.generator_id == 'X'])"`. Corollary: "this stub has generators so we can't delete it" claims may be lying — check first.
22. **Generator retargeting for stub-merges with attached generators** *(process)*. When a merge-candidate stub has live generators: (1) find and delete shadowed duplicates, (2) rewrite `topic_slug` on survivors to the canonical live target, (3) pytest, (4) rebuild the bank, (5) git rm the stub + add the `aliases.yaml` rule, (6) regenerate course hubs + prereq graph + topic status + index. Doing 5-6 before 1-4 leaves an orphan bank shard.

### Copyright discipline (accumulated across 10 clusters + v2.3.0 test-prep phase)

The copyright pytest caught many near-misses. These are the **textbook phrasings that reliably collide with 15-word shingles** in the source corpus — avoid them in future content. Every content sub-agent prompt MUST inline this list.

**Problem statement openers to avoid** (use "Give...", "Determine...", "What is...", "Compute...", "Find all real solutions to...", "Express...", "Classify...", "Identify..." instead):
- "Find the equation of the line..."
- "Write the equation of the line with slope..."
- "Solve the equation..."
- "Evaluate..." as a bare opener
- "Find the value of x..."

**Banned definitional phrasings** (paraphrase each one freshly):
- *Core algebra/arithmetic:* "the absolute value of a number is its distance from zero", "a rational number is any number that can be written as a fraction", "an algebraic expression is any combination of variables constants and operations", "a polynomial is an expression with one or more terms", "like terms are terms with the same variable and exponent", "the degree of a polynomial is the highest power of the variable", "a literal equation is an equation with more than one variable", "a number is in scientific notation when it is written as", "isolate the variable", "do the same thing to both sides", "the coordinate plane is a two-dimensional surface with two perpendicular number lines", "a ratio is a comparison of two quantities", "a proportion is an equation stating that two ratios are equal", "a prime is a whole number greater than 1 whose only factors are 1 and itself", "every point on the number line corresponds to exactly one real number", "every natural number is an integer every integer is rational"
- *Number theory / factoring:* "every whole number greater than 1 can be written as a product of primes in exactly one way", "the greatest common factor of two or more whole numbers is the", "the least common multiple of two or more whole numbers is the", "two numbers whose product is and whose sum is"
- *Trig / functions:* "an identity is an equation that is true for every angle", "a rational function is a quotient of polynomials", "a sequence is an ordered list of numbers", "a complex number is a number of the form a + bi where a and b are real", "a matrix is a rectangular array of numbers", "the hypotenuse is always opposite the right angle", "in an arithmetic sequence, each term is obtained by adding a constant", "multiply every term on both sides by the LCD", "a function is a relation that assigns exactly one output to each input", "a relation is a set of ordered pairs", "the domain of a function is the set of all possible input values", "the range of a function is the set of all possible output values", "the vertical line test states that a graph represents a function if and only if no vertical line crosses it more than once", "a polynomial function is of the form", "vertical asymptotes occur where the denominator is zero"
- *Stats / probability:* "a piecewise function is defined by different formulas on different intervals", "conditional probability is the probability of an event given that another event has occurred", "the margin of error tells you how far the true population value is likely to be from the sample estimate", "a confidence interval is a range of values likely to contain the true parameter", "a sample is a subset of a population", "bias in sampling occurs when a sample is not representative of the population", "a histogram is a bar graph of frequencies", "a box plot displays the five-number summary", "correlation measures the strength and direction of a linear relationship", "a residual is the difference between the observed value and the predicted value", "a permutation is an arrangement of objects in a specific order", "a combination is a selection of objects without regard to order", "the empirical rule states that approximately 68, 95, and 99.7 percent of data lies within 1, 2, and 3 standard deviations", "a z-score measures how many standard deviations a value is from the mean", "expected value is the long-run average of a random variable", "a binomial distribution describes the number of successes in n independent trials with probability p"

**Theorem openers to paraphrase** — never "The X theorem states that..." or "The Rule of Y states..." verbatim. Examples: Law of Sines, Pythagorean theorem, De Moivre's theorem, Zero Product Property, Rational Root Theorem, Descartes's Rule of Signs, Fundamental Theorem of Arithmetic.

**Banned step phrases:** "take the log of both sides", "take the root first and then raise to the power", "check for extraneous solutions", "equals the sum of the two remote interior angles", "group the first two terms and the last two terms", "collect the terms on the left and the constants on the right", "the parabola opens to the right because p > 0", "every positive number has two square roots", "the midpoint of the segment joining the foci", "follow the order of operations", "add the same quantity to both sides", "multiply both sides by 2", "when you multiply or divide both sides of an inequality by a negative, flip the inequality".

**Banned parenthetical:** "(also called ...)" for synonyms — use an em-dash aside instead: "— sometimes called a —".

**Banned hedges / filler:** "it is important to note that", "as you can see", "in other words", "another way to say this is", "clearly", "it can be shown that".

**Word-problem scenarios:** don't reuse textbook scenarios verbatim (Alice/Bob working together, a ball thrown upward, a taxi fare, a PortaBoy). Invent fresh names and contexts. The approved name pool: Maya, Kai, Priya, Rohan, Zoe, Emilia, Mateo, Leilani. Approved context pool: community garden, school newspaper, coffee shop, tutoring center, science fair, local band, food pantry, maker space, hiking club, jewelry maker, photography class, farmer's market, pop-up book, school pep rally.

**Workflow:** run the shingle test after every wave, not just at the end. If a hit fires, grep for the flagged phrase across `wiki/topics/`, do 1-line rewrites, re-run. Expect **rework rings** — the `hits[:3]` truncation in the test masks subsequent hits, so fixing the first three often surfaces three more. Budget ~2 rework passes per pre-algebra/algebra wave, 0 per precalc wave.

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

The wiki is at zero stubs as of v2.4. The roadmap is now short.

### Deferred Vault polish

These ride on existing Vault infrastructure so they do not need new data pipelines.

1. **Custom worksheet builder** — dedicated page where the student picks N topics × difficulty × count → mixed worksheet. New Quartz component, new `wiki/Worksheet_Builder.md` page. Can reuse `ProblemVaultWidget`'s shard-fetch logic.
2. **Input-and-check answer grader** — string matching on normalized LaTeX handles ~80% of cases; Pyodide SymPy handles the rest if the 5 MB load cost is acceptable. Extends `VaultEntry` with `user_answer`, `marked_correct`, `timestamp`.
3. **Difficulty auto-tune** — track per-generator correct/incorrect in localStorage, suggest the next difficulty. Depends on the grader above.

**Shipped in v2.4:** jsPDF polished PDF export (see Widget architecture above — lazy `ensureJsPdf()` + `ensureHtml2Canvas()` singletons mirroring the `ensureKatex()` pattern, off-screen KaTeX → html2canvas → jsPDF slice-and-addImage pipeline, `@media print` fallback preserved).

### Future content expansion

No stub backlog. Growth vectors are **new-book ingest** (see env_map Author's Guide below), **new gap topics** (domains the wiki doesn't yet cover — e.g., calculus, advanced statistics, linear algebra — all explicitly out of scope for v2.x), or **enrichment passes** on existing topics (add a second figure, add worked example #4, deepen the prose). Enrichment passes get diminishing returns above avg score 90.

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

Expected: all tests green, 273/273 YAML clean, 0 lint errors. If you get copyright hits, grep for the flagged phrase across `wiki/topics/` to find all occurrences, then do 1-line rewrites. Expect 2-3 rework rings on pre-algebra/algebra waves — the `hits[:3]` test truncation masks subsequent offenders.

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
- **Build time:** ~2 minutes for ~269 pages including overlay + Quartz build
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

### Versions 2.0 → 2.4 — from content buildout to zero-stub

**v2.0-v2.2 (content buildout + nav redesign + PrereqWidget).** Ten clusters shipped 36 → 146 live topics + infrastructure (copyright pytest, YAML validator, topic status dashboard, alias merge pipeline, ingest smoke test). Replaced 4 branch hubs with 5 course hubs + rewrote breadcrumbs across 239 files in one sweep. Cluster 10 added 10 HS Geometry topics + 50 new generators + 14 figures. PrereqWidget ("Review these first" sidebar card) shipped via `tools/build_prereq_graph.py` + `quartz_components/PrereqWidget.tsx`. Vault gained JSON export/import.

**v2.3 (test-prep phase).** Precalculus nav bugfix (alias-redirect collision, same bug class as Vault.md — Gotcha #4 generalized). Standardized-test tagging infrastructure: `tools/test_prep_mapping.yaml` + idempotent `tools/apply_test_tags.py` + tag taxonomy Section 7 + auto `/tags/test-*` index pages. Four activation waves (pre-algebra, algebra, precalc, Wave D gap topics): 144 → 210 live, 460 → 638 generators, 45 → 62 figures, 112 → 51 stubs, avg 53.9 → 71.6. Cross-wave wikilink drift surfaced as Gotcha #18.

**v2.4 (zero-stub phase).** Three work threads in one session. **(1) Vault Save-as-PDF** (5 commits): replaced `window.print()` with a jsPDF + html2canvas pipeline in 3 risk-split commits (singletons → pipeline + SCSS → button rewire). Post-ship color regression fixed with `!important` overrides on `color`/`fill`/`stroke` inside `.vv-pdf-offscreen *`. **(2) Quality bump** (2 commits): 37 topics stuck at score 75 all had the same deficit — fully-written examples marked `**Example N.**` bold-inline instead of `### Example N` H3 (which the scorer regex doesn't count). `tools/fix_example_headings.py` rewrote all 37 from 75 → 90 without changing any prose. `Cross_Sections_Of_Solids` got 3 new generators so nothing scored below 80. Surfaced Gotchas #20 (heading regex) and #21 (dead class shadowing). **(3) Zero-stub push** (3 commits): triaged the remaining 42 stubs into 30 merge-deletes (30 `aliases.yaml` rules, 8 `topic_slug` retargets, 1 shadowed duplicate removed, 16 inbound wikilinks rewritten) and 12 activation targets (3 content + 3 generator + 1 figure parallel agents → ~16,900 words + 36 generators + 4 figures). One copyright rework on `Set_Notation_And_The_Real_Numbers.md` (added 2 phrasings to the banned list). Test-prep tagging pass: +13 new mappings, -3 stale ones. **Net v2.4 delta:** 210 → **220 live topics**, 638 → **677 generators**, 51 → **0 stubs**, avg 71.6 → **90.1**. Pre-algebra was the biggest mover: 61.1 → 89.2. Every branch now ≥ 89.

### What works at session scale (proven across 5 versions)

- **Parallel sub-agent dispatch** (3 content + 3 generators + 1 figures per wave) sustains 12-25 topic activations per wave without review-burden collapse. v2.3 ran four waves × 6-7 parallel agents; v2.4 ran one wave × 7 with clean file-partitioning.
- **Plan-then-execute with a Plan agent.** Use for phases with 20+ topic activations or non-trivial feature ships (the v2.4 Vault PDF export used a Plan agent to design the jsPDF pipeline before any implementation). Plan agent reads the dashboard + the project spec + the critical files and returns a file manifest or implementation sketch. Cheap insurance.
- **Count parameter-space cardinality from the index, not guessing.** Before dispatching a wave, run a one-liner over `wiki/_data/topic_status.json` to pin exact counts per branch/status/deficit. v2.3's "15 prose-only per branch" guess was off by 2×; v2.4's dashboard-driven triage was exact.
- **Backward construction everywhere in generators** (Gotcha #9). Pick the answer, derive the parameters. `while True` retry loops are an infinite-loop smell.
- **Forbidden-idiom list + FULL taxonomy + live-topic slug list inlined in every content prompt.** By Wave D the first-pass copyright hit rate was near zero. v2.4 had one rework ring on `Set_Notation_And_The_Real_Numbers.md` (added 2 phrasings to the banned list).
- **Gold-standard read first.** Every content prompt starts with "read these 3 files and match their tone." Pick golds that score ≥90 on `topic_status.py`.
- **Three-commit split for risky features.** v2.4 shipped jsPDF in 3 commits — (1) CDN singletons only, (2) pipeline functions + SCSS, (3) button rewire. Each independently testable, each revertable without losing the others. Worth the overhead for anything that touches runtime behavior.
- **Convention-drift diagnosis before content work.** When many topics fail the same way, check whether the scorer/validator is reading the convention they actually use. v2.4's heading-regex fix moved 37 topics 75 → 90 with zero prose changes — the "quality bump" was a regex bug.

### What to watch

- **Dead wikilink drift** (Gotcha #18). Lint catches it, but pre-seeding the live-topics list *organized by branch* in every agent prompt prevents it.
- **Tag taxonomy drift.** Copy ALL 7 sections of `_tag_taxonomy.md` into agent prompts, not just a reference. Partial lists let close-sounding tags slip in.
- **Parameter-space underestimate.** Agents set `bank_count_per_difficulty = 20` when reality is < 10. Prompt generator agents to compute cardinality before declaring the bank count.
- **Shard size budget 320 KB.** Prefer reducing `bank_count_per_difficulty` over raising the cap.
- **Copyright shingle ring-effect.** `hits[:3]` truncation masks later hits. Budget 1-2 rework rings per algebra/pre-algebra wave.
- **Hub script rewrite order.** Rewrite `update_course_hubs.py` BEFORE deleting any old hub files it references.
- **`@register` shadowing** (Gotcha #21). Duplicate `generator_id`s silently lose to import order. Verify with the one-liner in Gotcha #21 before trusting a class is live.

### What to do first in a next session

1. Run the four sanity-check commands at the top of this file. Expected: pytest 29/29, validate_yaml 234/234, lint 0/0, topic_status avg ~90.1, 220 live topics, 0 stubs.
2. `gh run list --limit 3` — confirm the last CI runs are all green.
3. Read `wiki/Topic_Status.md` for the current distribution. Every live topic should score ≥ 85 and most score 90+. An outlier probably needs a figure, an example, or a cross-link bump.
4. Pick one from **Remaining Work**: custom worksheet builder, input-and-check grader (+ difficulty auto-tune as a follow-on), or a new-textbook ingest. Follow the Session Patterns section — parallel sub-agents for anything that splits across files; three-commit split for feature work that touches runtime behavior.

---

## Self-Improvement Protocol

This file self-improves with each session:

- **During iteration:** pitfalls get woven into relevant sections (not appended). Patterns that worked get reinforced with concrete examples. The spec gets shorter and more precise, not longer.
- **After a session:** roll up detailed cluster logs into the "Recent Session History" compression. Keep only the forward-looking lessons.
- **Measure improvement in compression, not accumulation.** This file was 1769 lines before the v2.0.0 refactor. It should stay under 1000 going forward unless there's a genuinely new architectural layer to document.

Future contributors: if you find yourself adding a section that doesn't answer a question a new-session you would ask, delete it or fold it into an existing section. This file is a context-boot for Claude, not a changelog.
