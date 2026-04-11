# Math_Wiki.md --- A Practice-First Math Wiki & Tutor
## Student-facing, course-based navigation from middle school through pre-calculus
### Version 2.1.0 --- Standalone conversion + 5 course hubs. (2026-04-11)

| Field | Value |
|-------|-------|
| **Domain** | Middle and High School Mathematics |
| **Scope** | Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus (through conics, matrices, complex numbers). Calculus + advanced statistics deferred. |
| **Audience** | Students grades 6-12. Warm, tutor-adjacent tone. Intuition first, formalism second. |
| **Presentation** | **Standalone wiki.** No "paraphrased from textbooks" language in student-facing content. Internal `raw/books/` and `raw/extractions/` remain as build inputs but never surface in wiki output. |
| **Scale** | **136 live topics / 410 generators / 32,698 verified problems / 31 figures** |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD, ~90s build time |
| **URL** | https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/ |
| **Status** | 9-cluster content buildout **COMPLETE**. Phase 1 (standalone + course-hub nav redesign) shipped. Cluster 10 (Geometry expansion) is the next major content phase. |

---

## Orientation for a New Session

**Read this file top to bottom before touching anything.** The history of how we got here has been compressed; what remains is the state you need to keep building safely.

### First commands in a fresh session

```bash
cd /c/Wiki_Factory/builds/Math_Wiki

# Sanity check: all four should be green
py -3 -m pytest generators/tests/ -q                # 29/29 passing
py -3 ../../factory/scripts/validate_yaml.py wiki/  # 257/257 clean
py -3 ../../factory/scripts/lint_wiki.py wiki/      # 0 errors, 0 warnings
py -3 tools/topic_status.py                         # avg ~53, 136 topics at 3+ gens
```

If any of those fail, something has regressed — fix that before doing anything else.

### 30-second mental model

Math_Wiki is a **standalone, practice-first wiki**. Every live topic page has (a) clear original prose with worked examples and (b) an interactive problem-vault widget fed by SymPy-verified Python generators. Students read → add problems to a browser-local Vault → download worksheets. The site deploys to GitHub Pages via Quartz v4 on every push to main.

Navigation is **course-first**. Five course hubs (Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus & Trig) are the student's primary entry points. A 7th grader opens Middle School Math; a sophomore opens Algebra 2. Branch-level organization still exists in the underlying data model but is hidden from the student-facing sidebar.

The content buildout shipped in **9 clusters** (pre-algebra foundations → linear → quadratics → rationals → functions → exp/log → trig → sequences/probability → conics). Each cluster delivered 10-15 topics fully finished (prose + generators + figures + cross-links). All 9 content clusters are shipped. Phase 1 (standalone conversion + course hub redesign) is shipped. **Cluster 10 (Geometry expansion)** is the next major phase.

### Where things live

| Path | What |
|---|---|
| `raw/books/` | Original LaTeX source material used during initial ingestion (gitignored, ~62 MB). Build inputs only; never surface in the wiki. |
| `raw/extractions/{book_slug}/chapter_NN.json` | Per-chapter parsed blocks from initial ingestion (gitignored). Internal build artifact. |
| `raw/catalog/topics_{branch}.json` | Per-branch canonical topic catalog (post-alias-merge). Internal build artifact. |
| `tools/aliases.yaml` | Manual merge/rename/split rules for `consolidate_extractions.py` |
| `wiki/_overview.md` | Landing page (hero + 5 course hub cards + learning paths) |
| `wiki/{Middle_School_Math,Algebra_1,Geometry,Algebra_2,Precalculus}.md` | Five student-facing course hubs (hand intro + learning path + AUTO:TOPICS block) |
| `wiki/Topics_Overview.md` | Alphabetical index grouped by course |
| `wiki/Topic_Status.md` | Auto-generated progress dashboard (regen with `topic_status.py`) |
| `wiki/Vault.md` | Interactive vault page (mounts VaultViewer) |
| `wiki/Formulas_Overview.md` | Named formulas and theorems index |
| `wiki/topics/{pre_algebra,algebra,precalculus,geometry}/*.md` | Topic pages (enriched or auto-stub). Grouped on disk by branch, surfaced by course hub. |
| `wiki/_data/problem_types_index.json` | Widget lookup: topic_slug → generators. Drives live/stub classification. |
| `wiki/_data/problems/{topic_slug}.json` | Per-topic problem shards (committed, <320 KB each) |
| `wiki/assets/figures/{branch}/*.svg` | 31+ matplotlib SVG figures across branches |
| `generators/{algebra,pre_algebra,precalculus,geometry}/*.py` | 410 generators across 4 branch packages |
| `generators/base.py` | `Problem` dataclass, `Generator` ABC, `@register`, `all_generators()` |
| `generators/tests/` | Pytest: parametrized suite (circles), copyright shingle check, consolidate snapshot, ingest smoke |
| `generators/latex_helpers.py` | `format_fraction`, `format_point`, `shift_expr`, `signed_int` |
| `quartz.config.ts` / `quartz.layout.ts` | Quartz v4 config + layout. Sidebar shows 10 entries: 🏠 Home, 5 course hubs, 📖 All Topics, 🎒 Vault, 📊 Progress, 🧮 Formulas. |
| `quartz_components/*.tsx, *.inline.ts` | `ProblemVaultWidget`, `VaultViewer` — overlaid onto Quartz at CI time |
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

**Raw** (`raw/books/`, `raw/extractions/`, `raw/catalog/`) — immutable source plus LLM-generated but never-student-facing intermediaries. All gitignored except `raw/catalog/`, which IS committed.

**Wiki** (`wiki/`) — LLM-owned markdown. 136 enriched topic pages + ~103 auto-stubs still on disk + overview/hub pages + problem bank shards.

**Outputs** — derived artifacts at build time (Quartz HTML). Not committed.

### Sharded problem bank

- `wiki/_data/problem_types_index.json` — small lookup (~250 KB). Fetched by the widget on every topic-page load. Maps `topic_slug` → list of `{generator_id, display_name, counts, supports_word_problems}`. Also contains `by_generator` and `by_topic` keys the CLI tools read from.
- `wiki/_data/problems/{topic_slug}.json` — per-topic shard, lazy-fetched on first "Add to Vault" click.
- Every shard stays under **320 KB** by default (30 problems per difficulty per generator). Override with `bank_count_per_difficulty = N` class attr when parameter space is smaller.
- Compact JSON output (no indent, `ensure_ascii=False`).

### LocalStorage-first vault

- On "Add to Vault", `problemVaultWidget.inline.ts` fetches the topic shard, picks random problems, and writes **full problem objects** (statement, answer, hints, solution steps) into `localStorage["math-wiki-vault"]`.
- The `/Vault` page reads entries directly from localStorage. **It never fetches the bank.** Instant load, zero external fetches.

### Widget architecture

- Each live topic page has `<div class="problem-vault-widget" data-topic-slug="{slug_lower}"></div>` in its markdown body.
- `ProblemVaultWidget.tsx` and `VaultViewer.tsx` are custom Quartz components imported by `quartz.layout.ts` via explicit relative paths (`./quartz/components/...`). The CI overlay copies `quartz_components/*` into `quartz/components/` before `npx quartz build`.
- Both register `.css` and `.afterDOMLoaded` entries; the components emit nothing server-side and mount on the client only when their hook div is present.

### Runtime KaTeX loader

Quartz's `Plugin.Latex({ renderEngine: "katex" })` ships **only** `katex.min.css` plus the `copy-tex` contrib JS. It does **NOT** ship `katex.min.js` (Quartz renders math server-side at build time). For dynamic widget content:

- `ensureKatex()` is a singleton in both `.inline.ts` files. Uses `window.__mathWikiKatexLoad` to share the loading promise across components.
- Injects `<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" data-math-wiki-katex="1">` once on demand.
- `renderKatexIn(element)` walks text nodes and converts `$...$` and `$$...$$` into rendered spans/divs.

### Base URL awareness

Widgets fetch data using `getMathWikiRoot()`, which parses `location.pathname` to find the `/Math_Wiki/` segment. Handles both local dev (`/Math_Wiki/...`) and production (`/Wiki-Factory/Math_Wiki/...`) without hardcoding.

---

## Source Inventory

5 books, all in `builds/Math_Wiki/raw/books/` (gitignored).

| # | Slug | Book | Layout | Chapters | Blocks | Role |
|---|---|---|---|---:|---:|---|
| 1 | `math_1` | Math I | curriculum-factory | 9 | 642 | Middle school: whole numbers, integers, fractions, decimals, ratios, percents, intro algebra, basic geo/data |
| 2 | `math_2` | Math II | curriculum-factory | 9 | 527 | Middle school: exponents, rationals, proportions, expressions, inequalities, Pythagoras, coordinate plane, stats |
| 3 | `algebra_1` | Algebra — The First Year | curriculum-factory | 9 | 431 | Foundations, equations, inequalities, linear functions, systems, exponents/polynomials, factoring, quadratics, rationals/radicals |
| 4 | `algebra_2` | Algebra — The Second Year | curriculum-factory | 9 | 638 | Sets/numbers, linear, quadratics, functions, polynomials, rationals, exp/log, transformations, conic sections |
| 5 | `algtrig` | Stitz-Zeager College Algebra & Trig (3rd ed) | topic-folder | 11 | 498 | Pre-calc with trig: relations/functions, quadratics, polynomials, rationals, exp/log, trig, sequences, conics, matrices |

**Total: 47 chapters, 2,736 extracted blocks, ~3.4 MB of JSON extractions.**

### Environment conventions

- Books 1-4 share **Curriculum Factory**: `keyterm`, `property`, `example`, `checkpoint`, `note`, `caution`, `keyconcept`, `figure`.
- Book 5 uses **AMS-theorem**: `defn`, `thm`, `cor`, `ex`, `eqn`.
- Both handled by `tools/ingest_math_book.py` via per-book `env_map` attributes.

### Copyright rule (non-negotiable)

**NEVER reproduce problem text, worked examples, or extended prose verbatim from any source book.** All practice problems come from SymPy-verified Python generators producing fresh problems. Definitions and pedagogy are always paraphrased. Enforced by `generators/tests/test_copyright_safety.py` (15-word shingle match against `raw/extractions/**/*.json`).

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
│   ├── linear_equations.py slope.py multi_step_equations.py systems.py elimination_systems.py
│   ├── absolute_value.py quadratic_formula.py factoring.py exponent_rules.py
│   ├── inequalities.py lines.py coord_scatter.py                    # Cluster 2
│   ├── polynomials.py quadratics_methods.py quadratic_functions.py  # Cluster 3
│   ├── rationals.py radicals.py radical_functions.py                # Cluster 4
│   ├── function_fundamentals.py function_families.py advanced_functions.py  # Cluster 5
│   ├── exponentials.py logarithms.py                                # Cluster 6
├── pre_algebra/               # 16 modules, ~50 generators
│   ├── integers.py integers_ext.py order_of_operations.py foundations.py
│   ├── fractions_basics.py fractions_addsub.py fractions_muldiv.py
│   ├── decimals_arith.py decimals_divplace.py
│   ├── percents.py percent_change.py eval_and_ratios.py rates_and_proportions.py
│   ├── slope_intercept.py algebra_intro.py inequalities_intro.py    # Cluster 2
├── precalculus/               # 5 modules, ~90 generators  (created in Cluster 7)
│   ├── trig_core.py trig_advanced.py                                # Cluster 7
│   ├── sequences_and_stats.py                                       # Cluster 8
│   ├── conics_and_complex.py matrices.py                            # Cluster 9
├── geometry/                  # 2 modules
│   ├── circles.py pythagoras.py
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
4. **Vault.md cannot have `"Vault"` in its `aliases:` list.** Alias=filename creates an alias-redirect HTML that overwrites the canonical page. (Phase 1 bugfix.)
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

**Do NOT include "Practice generators for this topic are coming in a future wave" lines** — the 9-cluster plan is complete. Every live topic has live generators.

### Course hub structure

Hand-written intro paragraph + suggested learning path + `<!-- AUTO:TOPICS:BEGIN/END -->` block regenerated by `tools/update_course_hubs.py`. The auto block walks `wiki/topics/**/*.md`, reads each file's `branch:` frontmatter, groups by the five course hubs, and uses `wiki/_data/problem_types_index.json` to split each course's topic list into a flat "🟢 Live topics" section and a collapsed `<details>` "⚪ Stub topic(s)" section. The Geometry hub additionally pulls in an explicit allowlist of geometry-adjacent pre-algebra slugs (`GEOMETRY_ADJACENT_ALLOWLIST` in the script).

### Landing page (`wiki/_overview.md`) structure

```
# Math Wiki
<tagline + stats row: 136 topics · 410 generators · 32,698 problems>
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

## The Completed 9-Cluster Buildout Plan

All shipped. This table is the final state of the plan.

| Cluster | Name | Topics | Gens | Problems | Commit |
|:---:|---|---:|---:|---:|---|
| **0** | Infrastructure hardening + alias merge | 0 | 0 | 0 | `8c1b4ac` |
| **1** | Pre-algebra foundations | 20 | 60 | 5,286 | `f27052f` |
| — | Navigation UI redesign | 0 | 0 | 0 | `a0f4c4f` |
| **2** | Linear world completion | 14 | 42 | 3,714 | `49dfa00` |
| **3** | Polynomials + Quadratics deep | 14 | 42 | 3,590 | `bb768cc` |
| **4** | Rationals & Radicals | 12 | 36 | 3,052 | `a3db819` |
| **5** | Functions & Transformations | 14 | 42 | 3,353 | `bedee97` |
| **6** | Exponentials & Logarithms | 10 | 30 | 2,084 | `db5421c` |
| **7** | Trigonometry | 15 | 45 | 2,594 | `c78a1f1` |
| **8** | Sequences, probability, statistics | 9 | 27 | 2,015 | `710120f` |
| **9** | Conics, matrices, complex numbers | 12 | 36 | 2,675 | `50904eb` |
| **Totals** | | **120** | **360** | **28,363** | |

*(Cluster 1's 5,286 includes initial generator waves on top of the baseline. The totals above + the ~16 topics, 50 gens, 4,335 problems that existed at Cluster 0 start = current state of 136 / 410 / 32,698.)*

**Per-cluster verification** (from `tools/topic_status.py`): prose body 300+ words, 2+ worked examples, 3+ generators, 3+ prerequisite links, 3+ see-also links, figure where visually useful, `status: draft|complete`.

---

## Post-Plan Follow-Up Work

The 9 content clusters are done. Remaining work is polish, new-book ingests, and optional features.

### Cluster L (lint / polish / closeout)

- Final read-through of all 136 live topics. Look for typos, awkward phrasings, thin examples.
- Strengthen cross-links where the graph is thin. Currently 134 topics have 3+ generators; bumping the 2 outliers up.
- Figures: roughly half of live topics still lack a figure. Target the ones where a figure would unlock the explanation (transformations, trig identities, conics).

### Prereq-graph widget

- Every live topic has a `prerequisites: [...]` YAML field. That's a directed graph in waiting.
- Build a new Quartz component (`PrereqWidget.tsx`) that reads `wiki/_data/prereq_graph.json` (to be generated from frontmatter) and renders a "struggling? review X first" widget in the right sidebar.
- Candidate algorithm: topological distance from the current topic over the prereq edges.

### Vault polish

From the Site Expansion Proposal section (now pruned but these are the top candidates):

1. **Custom worksheet builder** — a dedicated page where the student picks N topics × difficulty × count → mixed worksheet. Builds on Vault infrastructure.
2. **jsPDF polished download** — replace `@media print` with a rendered-KaTeX→PDF pipeline for consistent cross-browser output.
3. **Input-and-check answers** — string matching on normalized LaTeX handles 80% of cases; Pyodide SymPy handles the rest if we want to pay the 5 MB cost.
4. **Vault export/import** — JSON dump/upload, so students can move practice sets across devices or share with a teacher.
5. **Difficulty auto-tune** — track correct/incorrect per generator in localStorage, suggest next difficulty.

### Future ingests

~103 stubs remain in the catalog after the 9-cluster plan — secondary entries that weren't in the core curriculum scope. Activating one is straightforward:

1. `tools/generate_topic_stubs.py --branch all --force` ensures the stub exists.
2. Write the content following the topic skeleton above.
3. Add generators under the appropriate branch package.
4. `build_problem_bank.py` → `topic_status.py` → `update_course_hubs.py` → commit.

Adding a whole new source book is supported end-to-end:

1. Drop the book's LaTeX tree under `raw/books/new_book/`.
2. Write an `env_map` in `tools/ingest_math_book.py` (see the env_map Author's Guide section).
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

These are patterns the 8-cluster session (2-9) proved effective. Future sessions should default to these unless something better shows up.

### Parallel sub-agent dispatch

- **Content wave:** 3-4 sub-agents in parallel, each owning 2-4 topics. They edit different files, so there are no collisions.
- **Generator wave:** 2-3 sub-agents, each owning a generator module (one file). The `__init__.py` import lines are distinct, so parallel edits land cleanly.
- **Figures agent:** 1 sub-agent extends `tools/generate_figures.py` in parallel with content batch 2.
- **Sequencing matters within a cluster:** batch 1 content before batch 2 content so batch 2 can wikilink to just-shipped pages. Generators run after content so generators can read the prose.
- **Sub-agent daily usage limit:** If it hits mid-cluster, pivot to direct writing by the main session (Cluster 5 validated this fallback with no quality loss).

### Sub-agent prompt template (what works)

Every sub-agent prompt must include:

1. The exact topic file paths and catalog entries to read.
2. The source extraction JSON paths for each topic (usually 1-2 per topic).
3. 2-3 gold-standard files to imitate for structure (`Circles.md`, `The_Distributive_Property.md`, and one from a recent cluster).
4. The structural template verbatim (frontmatter + sections + widget div).
5. The forbidden-idiom list (see Gotchas section above — the full list keeps growing).
6. Hard constraints: word count floors, YAML rules, LaTeX rules, widget slug rule.
7. Explicit "Do NOT include 'Practice generators are coming in Cluster X'" — the 9-cluster plan is complete.
8. A short process list ending in a brief return summary.

### Validation cadence after a batch

```bash
py -3 -m pytest generators/tests/test_copyright_safety.py -q
py -3 ../../factory/scripts/validate_yaml.py wiki/
py -3 ../../factory/scripts/lint_wiki.py wiki/
```

Expected: 3 pytest passes, 257/257 YAML, 0 lint errors. If you get copyright hits, grep for the flagged phrase across `wiki/topics/` to find them all, then do 1-line rewrites.

### What NOT to do

- **Don't** skip the gold-standard read in content prompts. Sub-agents trained to "match The_Distributive_Property.md" produce consistently better prose than ones given the template from scratch.
- **Don't** trust a single copyright pass. Run the shingle test, fix, run again — sometimes rewriting one idiom surfaces a previously-masked neighbor.
- **Don't** commit a cluster with dead wikilinks. Lint catches them but only after Quartz gets them wrong in production.
- **Don't** invent new tags. Every new tag needs to be added to `_tag_taxonomy.md` first.
- **Don't** forget `py -3 tools/update_course_hubs.py` after adding live topics. The course hub "AUTO:TOPICS" block is stale otherwise.
- **Don't** ship a cluster without updating `_overview.md`'s Learning Paths and `Topics_Overview.md`'s Live Topics sections. These are student-facing front doors.

---

## Deployment

- **Repo:** `JD-Jones-ASES/Wiki-Factory`
- **URL:** https://JD-Jones-ASES.github.io/Wiki-Factory/Math_Wiki/
- **Build time:** ~90 seconds for ~270 pages including overlay + Quartz build
- **CI workflow:** `.github/workflows/deploy.yml` (shared with Hymn Wiki). Runs pytest + validate_yaml + build_index, then clones Quartz v4 fresh, overlays `quartz.config.ts` / `quartz.layout.ts` / `quartz_components/` / `static/` from the build root, copies `wiki/*` into `content/`, runs `npx quartz build`, deploys. Overlays are directory-existence-guarded so Hymn Wiki's build is unaffected.
- **Per-build Quartz settings:** `enableSPA: false`, `Plugin.Latex({ renderEngine: "katex" })`, Explorer `filterFn` hides `topics/` + `problem_types/` + `entities/` folders, `localGraph.depth: 1`.

### Custom components loaded in layout

```typescript
// quartz.layout.ts (abbreviated)
import ProblemVaultWidget from "./quartz/components/ProblemVaultWidget"
import VaultViewer from "./quartz/components/VaultViewer"

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [ProblemVaultWidget(), VaultViewer()],  // early-return if mount absent
  footer: Component.Footer({ ... }),
}
```

---

## Recent Session History (Compressed)

The full cluster-by-cluster log is in git history (see the commit table above). This section keeps the most recent session-level lessons in a form future sessions can skim quickly.

### Version 2.0.0 — 9-cluster plan complete. Post-plan state. (2026-04-11)

**Session shipped Clusters 2 through 9 in one sitting** (88 hours of agent time over one day), plus Cluster 0 and 1 earlier. All 9 clusters shipped and deployed. CI green across all pushes. The wiki grew from 36 live topics / 9,621 problems / 22.2 status to **136 / 32,698 / 53.4**.

**What worked at session scale:**

- **Cluster 0 upfront infrastructure investment** paid off over every subsequent cluster: copyright pytest, YAML validator, topic status dashboard, alias merge pipeline, and the ingest smoke test meant every cluster could ship green on the first validation pass after small idiom fixes.
- **Parallel sub-agent dispatch** (3-4 content + 2-3 generators + 1 figures per cluster) sustained ~15 topics/cluster pace without review-burden collapse.
- **Backward construction for all generators** eliminated the guess-and-check infinite-loop class of bugs entirely after Cluster 2's one quadratic incident.
- **Forbidden-idiom discipline grew** with every cluster. By Cluster 7+, first-pass copyright hits dropped to zero or one per cluster.
- **Pre-calc branch created as a first-class package** (`generators/precalculus/`) starting in Cluster 7 — set the precedent for Cluster 8 and 9's organizational moves.
- **Hybrid execution pivot** in Cluster 5: when sub-agent daily limits hit mid-cluster, the main session wrote 6 pages directly with no quality loss. This fallback is viable and worth keeping in reserve.

**What needs to keep being watched:**

- **Dead wikilink drift:** when an agent invents a topic name that doesn't exist (`[[Rational_Roots_Theorem]]`, `[[Pre_Algebra_Overview]]`), lint catches it, but we want to prevent them at generation time. Consider pre-seeding every agent prompt with the current live-topics list.
- **Tag taxonomy drift:** same problem with tags. Occasionally an agent invents `#topic-trigonometry` or `#topic-equations-and-inequalities` that isn't in the taxonomy. Lint catches it; prompts need explicit "all tags from `_tag_taxonomy.md`" reminders.
- **Shard size budget:** every shard stays under 320 KB today, but the larger-parameter-space generators are inching up. If a generator goes over budget, prefer a `bank_count_per_difficulty` reduction over raising the cap.

**What to do first in a next session:**

1. Run the four sanity-check commands at the top of this file. Confirm all green.
2. Check `gh run list --limit 3` — the last 3 CI runs should all be green.
3. Read `wiki/Topic_Status.md` to see the current per-topic score distribution. If any topic scores below 60, it probably needs a figure, more examples, or a generator count bump.
4. Decide whether you're doing polish (Cluster L), a new-book ingest, a Vault feature, or something else. Pick one and start; all four are described above in the "Post-Plan Follow-Up Work" section.

---

## Self-Improvement Protocol

This file self-improves with each session:

- **During iteration:** pitfalls get woven into relevant sections (not appended). Patterns that worked get reinforced with concrete examples. The spec gets shorter and more precise, not longer.
- **After a session:** roll up detailed cluster logs into the "Recent Session History" compression. Keep only the forward-looking lessons.
- **Measure improvement in compression, not accumulation.** This file was 1769 lines before the v2.0.0 refactor. It should stay under 1000 going forward unless there's a genuinely new architectural layer to document.

Future contributors: if you find yourself adding a section that doesn't answer a question a new-session you would ask, delete it or fold it into an existing section. This file is a context-boot for Claude, not a changelog.
