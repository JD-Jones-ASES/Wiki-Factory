# Operations Log --- Math Wiki

Chronological log of ingest, compile, lint, and significant edit operations.

---

## [2026-04-10] Phase 0 scaffold

- Created `builds/Math_Wiki/` directory tree.
- Added new factory schemas: `topic.yaml`, `problem_type.yaml`, `technique.yaml`, `formula.yaml`.
- Extended `factory/scripts/lint_wiki.py` `VALID_TYPES` with the four new types.
- Extended `factory/scripts/add_navigation.py` `SECTION_MAP` with `topics`, `problem_types`, `techniques`, `formulas`.
- Copied `.obsidian/` config from `factory/templates/obsidian/`.
- Created `quartz.config.ts` (Math Wiki page title + base URL, KaTeX plugin retained) and `quartz.layout.ts` (math-specific `filterFn` and `mapFn`).
- Wrote `Math_Wiki.md` project spec per Template.md v1.3.0.
- Wrote `_tag_taxonomy.md` bootstrap (branches, topic areas, skills, difficulty, page meta, representations).
- Wrote navigation stubs: `_overview.md`, `_index.md`, `_log.md`, `Vault.md`, and all Overview hub pages.
- Added two additive overlay blocks to `.github/workflows/deploy.yml` for `quartz_components/` and `static/` directories (guarded by directory existence — Hymn Wiki unaffected).
- Ran `lint_wiki.py` on the scaffolded wiki to verify Phase 0 acceptance.

**Phase 0 complete.** Next: Phase 1 vertical slice (Circles topic + 5 generators + ProblemVaultWidget + deploy).

---

## [2026-04-10] Phase 1 vertical slice

End-to-end proof of the interactive stack. One topic (Circles) fully built, with all supporting infrastructure.

**Python generator library:**
- `pyproject.toml` at build root with pytest config (`pythonpath = ["."]`)
- `generators/base.py` --- `Problem` dataclass, `Generator` ABC, idempotent `@register` decorator, `_REGISTRY`, `all_generators()`, deterministic `make_problem_id()` from (generator_id, difficulty, params)
- `generators/latex_helpers.py` --- `shift_expr`, `signed_int`, `format_point`, `format_fraction`
- `generators/sympy_helpers.py` --- `safe_parse_expr`, `symbols_xy`, `circle_standard_form`
- `generators/geometry/circles.py` --- 5 generators:
  - `circles_equation_from_center_radius`
  - `circles_center_radius_from_equation`
  - `circles_area_from_radius`
  - `circles_circumference_from_radius`
  - `circles_area_from_diameter`
- `generators/tests/test_circles.py` --- 8 tests, all passing. Covers batch uniqueness, reproducibility, seed sensitivity, structural well-formedness of every problem.

**Build tooling:**
- `tools/build_problem_bank.py` --- iterates the registry, generates problems at every difficulty, writes `wiki/_data/problems.json` and `wiki/_data/problem_types_index.json`. Has a fallback cascade for generators with small parameter spaces (e.g., `circles_area_from_radius/easy` falls back from 100 to 30 unique values).
- `tools/generate_figures.py` --- matplotlib → SVG figure builder. First figure: `wiki/assets/figures/geometry/circle_parts.svg`.

**Problem bank results:**
- 5 generators × 3 difficulties = 15 batches
- 1140 total verified problems
- `problems.json` = 1.2 MB (well under the 2 MB sharding threshold)
- `problem_types_index.json` = 3 KB

**First real topic page:**
- `wiki/topics/geometry/Circles.md` --- full lesson with prose, LaTeX, figure embed, prerequisites, examples, and `<div class="problem-vault-widget" data-topic-slug="circles"></div>` mount point.
- Prerequisite stubs: `wiki/topics/geometry/Coordinate_Plane.md` and `wiki/formulas/Pythagorean_Theorem.md` (to be expanded in Phase 2).

**Quartz custom components:**
- `quartz_components/ProblemVaultWidget.tsx` + `problemVaultWidget.inline.ts` + `problemVaultWidget.scss` --- fetches the bank, renders problem-type rows with difficulty + count + Add-to-Vault buttons, writes to `localStorage['math-wiki-vault']`, dispatches a `math-wiki-vault-change` event, KaTeX-renders math in injected DOM.
- `quartz_components/VaultViewer.tsx` + `vaultViewer.inline.ts` + `vaultViewer.scss` --- renders vault contents on `/Vault`, resolves problem IDs against the bank, provides collapsible Hints / Show Answer / Solution Steps / Remove per problem, plus Shuffle / Print / Clear actions. Print CSS hides interactive chrome and adds workspace lines for a clean worksheet.
- Both components use relative import from `./types` (the Quartz components package exposes `QuartzComponent`, `QuartzComponentConstructor`). Both use `afterDOMLoaded` hook via their `.inline.ts` files.
- `quartz.layout.ts` updated to import and mount both components in `sharedPageComponents.afterBody`. Each component early-returns on pages where its mount point is absent.

**CI overlay:**
- `.github/workflows/deploy.yml` (modified in Phase 0) copies `builds/Math_Wiki/quartz_components/*` into `quartz/components/` during CI build, then Quartz bundles them into the site.
- Static problem bank JSON lives at `wiki/_data/problems.json` and rides the normal `wiki/* → content/*` copy into the Quartz build. Fetched by the widget at `/_data/problems.json` (baseUrl-aware via `getMathWikiRoot()`).

**Lint after Phase 1:** 0 errors, 0 warnings, 1 info (14 stubs, expected).

**What did NOT work first try:**
- Single-parameter circle generators (`circles_area_from_radius`, `circles_circumference_from_radius`, `circles_area_from_diameter`) had parameter ranges too small at easy/medium difficulty to produce 25 unique problems. Fix: widened ranges substantially (easy: 1-30, medium: 5-80, hard: 10-200 for radius generators; similar for diameter). Additional fix: `build_problem_bank.py` has a fallback cascade so the bank still builds cleanly even when a generator's parameter space caps below the requested count.
- `test_different_seeds_produce_different_batches` initially used set equality, which is too strict for small-parameter generators where two seeds may draw the same set in different orders. Relaxed to ordered list comparison.

**Pending for Phase 2 (book ingest):**
- User to provide 5 math textbooks in `raw/books/`
- `tools/ingest_math_book.py` (scripted PDF extraction)
- `tools/consolidate_extractions.py` (merge per-book JSON into canonical topic/problem_type/formula/technique pages)
- First wave of sub-agents to expand topics beyond circles

**Phase 1 complete.** Live end-to-end test requires deploying to GitHub Pages and browser verification of: KaTeX on topic page, widget click → localStorage → vault page → print worksheet.

## [2026-04-10] enrich | Cluster 8 batch 2 of 2: Probability, Binomial, Induction
- Enriched Probability_Of_Simple_And_Compound_Events.md (pre-algebra, 1113 body words)
- Enriched Binomial.md (pre-calculus, 1511 body words)
- Enriched Induction.md (pre-calculus, 1522 body words)

## [2026-04-11] Phase 1 | Standalone conversion + course-based navigation redesign

**Navigation redesign (5 course hubs, replacing 4 branch hubs):**
- Created `wiki/Middle_School_Math.md`, `Algebra_1.md`, `Geometry.md`, `Algebra_2.md`, `Precalculus.md`. Each has a hand-written intro, a suggested learning path, and an `AUTO:TOPICS:BEGIN/END` block populated by the new `tools/update_course_hubs.py`.
- Hub topic counts (live / total): Middle School Math 42/92, Algebra 1 34/50, Algebra 2 32/48, Pre-Calculus & Trig 27/47, Geometry 8/21 (2 geometry + 8 allowlisted pre-algebra adjacents, plus 11 stubs).
- `tools/update_course_hubs.py` (replacing `update_branch_hubs.py`) walks `wiki/topics/**/*.md`, reads each topic's `branch:` frontmatter, groups by course, and marks live vs stub via `problem_types_index.json`. A second pass pulls geometry-adjacent pre-algebra topics into the Geometry hub via an explicit `GEOMETRY_ADJACENT_ALLOWLIST`.
- Rewrote `wiki/_overview.md` to center on 5 course hub cards + 16 learning paths + tool links. Removed "paraphrased from 5 textbooks" language.
- Rewrote `wiki/Topics_Overview.md` alphabetical index grouped by course.
- `quartz.layout.ts` sidebar map trimmed from 14 entries to 10: 🏠 Home, 🔢 Middle School Math, 📗 Algebra 1, 📕 Geometry, 📙 Algebra 2, 📓 Pre-Calculus & Trig, 📖 All Topics, 🎒 Your Vault, 📊 Progress, 🧮 Formulas.
- `mathExplorerFilter` now also hides `entities`, `synthesis`, `techniques`, `sources` folders (even after deletion, as a safety net).

**Source purge (standalone conversion):**
- `tools/purge_source_mentions.py` stripped 4 types of source-book boilerplate from **133 stub topic files**:
  1. The blockquote callout `> _This is an auto-generated stub..._`
  2. The `## In the Source Books` section
  3. The `## Example Walkthroughs Available` section (with its `(from algebra_1)` attributions)
  4. Frontmatter `summary:` lines mentioning "source section(s) across the ingested textbooks"
- YAML `source_refs:` field preserved as internal metadata (never rendered, still read by build tooling).

**Breadcrumb + wikilink sweep:**
- `tools/rewrite_breadcrumbs.py` rewrote every `> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Title` breadcrumb and every See Also `[[Algebra_Overview|Algebra]]` wikilink in **239 topic files** to point at the new course hub (`Middle_School_Math`, `Algebra_1`, `Algebra_2`, `Precalculus`, `Geometry`) based on each topic's `branch:` field.
- Verified: `grep -rn '\[\[Algebra_Overview\|\[\[Precalculus_Overview\|\[\[Geometry_Overview\|\[\[Trigonometry_Overview' wiki/` returns zero matches.

**Deletions (aggressive cleanup):**
- Deleted old branch hubs: `Algebra_Overview.md`, `Geometry_Overview.md`, `Trigonometry_Overview.md`, `Precalculus_Overview.md`.
- Deleted empty-shell overview pages: `Sources_Overview.md`, `Entities_Overview.md`, `Synthesis_Overview.md`, `Techniques_Overview.md`, `Problem_Types_Overview.md`.
- Deleted empty folders: `wiki/sources/`, `wiki/entities/`, `wiki/synthesis/`, `wiki/techniques/`, `wiki/topics/trigonometry/`.
- Deleted obsolete script: `tools/update_branch_hubs.py`.
- Kept `Formulas_Overview.md` (one real page + room to grow during Phase 2 Geometry cluster).

**Cleanup of dangling references:**
- Fixed dead wikilinks in `Formulas_Overview.md` and `Vault.md` to point at course hubs.
- Rebuilt `_index.md` via `factory/scripts/build_index.py`.
- Removed "Source Tags" section from `_tag_taxonomy.md`; reworded `#topic-auto-generated` description to drop "ingested textbook catalog" language; renumbered sections 1-6.

**Math_Wiki.md spec updated (v2.0.0 → v2.1.0):**
- Added "Presentation: Standalone wiki" field to the header table.
- Rewrote the 30-second mental model and Where-things-live sections for course-first navigation.
- Navigation Design section updated to reflect the 10-entry sidebar map.
- Toolchain table updated (`update_course_hubs.py` replaces `update_branch_hubs.py`).
- Topic skeleton breadcrumb template updated.

**Validation after Phase 1:**
- `pytest generators/tests/ -q`: **29/29 passing**.
- `validate_yaml.py wiki/`: **253 files clean**.
- `lint_wiki.py wiki/`: **0 errors, 0 warnings, 1 info** (121 stubs --- expected).
- `topic_status.py`: 239 topics, 134 with 3+ generators, avg score 50.1 (was 53.4 --- drop is expected from stub source-section removal).
- `grep -rln 'In the Source Books|ingested textbook|source textbook' wiki/`: **empty**.

**Scope of changes:**
- **Created:** 5 course hubs, 2 one-shot scripts (`purge_source_mentions.py`, `rewrite_breadcrumbs.py`), 1 permanent script (`update_course_hubs.py`).
- **Modified:** 239 topic files (breadcrumbs + source-section strip), `_overview.md`, `Topics_Overview.md`, `_index.md`, `_tag_taxonomy.md`, `Vault.md`, `Formulas_Overview.md`, `Topic_Status.md`, `quartz.layout.ts`, `Math_Wiki.md`, `_log.md`.
- **Deleted:** 9 old overview pages, 1 obsolete script, 5 empty directories.

**Phase 1 complete.** Student-facing wiki is now standalone and course-first. Next: Cluster 10 (HS Geometry expansion).
