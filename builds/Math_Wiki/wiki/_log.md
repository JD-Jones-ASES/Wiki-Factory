# Operations Log --- Math Wiki

Chronological log of ingest, compile, lint, and significant edit operations.

---

## [2026-04-11] Post-v2.3.0 stub cleanup

Deleted 9 thin auto-stubs whose content was fully covered by existing live topics. Merge rules added to `tools/aliases.yaml` to prevent regeneration on the next `generate_topic_stubs.py` run. Two inbound wikilinks rewritten to canonical live targets: `Circles.md` updated its Prerequisites link from the deleted `Coordinate_Plane` stub to the live `The_Coordinate_Plane` (algebra, 1423 words), and `Simplifying_Radical_Expressions.md` dropped a redundant See Also entry since peer links already cover the content. Also fixed 4 references in `Sinusoid.md` pointing to the deleted `Transformations` stub (2 frontmatter paths + 2 body wikilinks) to the canonical live `Transformations_I_Shifts_And_Reflections`.

Deleted stubs (all auto-generated, 0 generators, ≤245 words, no unique prose):
- `algebra/Absolute_Value_Equations_And_Inequalities` → covered by live `Absolute_Value_Equations` + `Absolute_Value_Inequalities`
- `algebra/Slopes_Of_Lines` → duplicate of live `Slope`
- `algebra/The_Real_Numbers` → covered by live `Irrational_Numbers_And_Real_Numbers`
- `algebra/Powers_And_Roots` → covered by live `Properties_Of_Exponents` + `Square_Roots_And_Cube_Roots` + `Operations_With_Radicals`
- `algebra/Operations_With_Rational_Expressions` → covered by live `Multiplying_And_Dividing_Rational_Expressions` + `Adding_And_Subtracting_Rational_Expressions`
- `algebra/Applications_Of_Systems` → 19-word near-empty stub; applications are part of live `Systems_Of_Linear_Equations`
- `geometry/Coordinate_Plane` → duplicate of live algebra `The_Coordinate_Plane` (1423 words) and pre-algebra `Plotting_Points_And_The_Coordinate_Plane`
- `pre_algebra/Powers_And_Exponent_Notation` → duplicate of live `Exponents_And_Powers`
- `precalculus/Transformations` → covered by live split `Transformations_I_Shifts_And_Reflections` + `Transformations_Ii_Stretches_Compressions_And_Combined`

Post-cleanup metrics: **259 → 250 topics, 208 draft, 51 → 42 stubs, avg score 71.6 → 73.8**. Per-branch bumps: algebra 74.4 → 78.5, geometry 82.7 → 89.3, pre_algebra 61.1 → 61.6, precalculus 82.1 → 83.4. No generator orphaning (all 9 deleted stubs had 0 generators). Regenerated `_index.md`, `Topic_Status.md`, `_data/prereq_graph.json`, and all 5 course hub `AUTO:TOPICS` blocks.

**Not in scope:** The other 3 survey-flagged merge candidates (`Applications_Of_Quadratics`, `Percent_Applications`, `Ratios_And_Proportions`) have 2-3 generators attached each and require generator `topic_slug` reassignment to a canonical live topic before deletion. Deferred to a future session.

---

## [2026-04-11] Test-Prep Phase (v2.3.0)

Massive expansion and refinement phase focused on standardized test coverage and filling stub backlogs.

**Deliverable 1 --- Precalculus nav bugfix (commit 3aa7986).** Removed `"Precalculus"` from `wiki/Precalculus.md` aliases. The self-alias was producing an `AliasRedirects` HTML that clobbered the canonical hub, serving blank. Same bug class as the Vault.md fix. Gotcha #4 in Math_Wiki.md generalized.

**Deliverable 2 --- Standardized test tagging (commit c8e855e).**
- Added Section 7 to `wiki/_tag_taxonomy.md` defining `#test-sat`, `#test-psat`, `#test-act`, `#test-clt`.
- New `tools/test_prep_mapping.yaml` --- hand-curated slug-to-tests map (150 -> 209 entries by phase end, grown wave by wave).
- New `tools/apply_test_tags.py` --- idempotent surgical frontmatter editor with --dry-run / --check modes. No lint_wiki.py changes needed; the linter reads the taxonomy dynamically.
- Applied to 150 live topics: every test-relevant wiki topic now carries the appropriate combination of test tags.
- Coverage: test-act 150+, test-sat 110+, test-psat 94+, test-clt 51+. Approximately 49 topics quad-tagged (all 4 tests).
- Quartz auto-generates `/tags/test-sat`, `/tags/test-psat`, `/tags/test-act`, `/tags/test-clt` as de-facto "everything on exam X" indexes --- zero custom hub authoring.

**Deliverable 3 --- Stub activation waves A/B/C.**

- **Wave A (commit 1933ef0, pre-algebra) --- 22 stubs, +48 generators, +3 figures.** 6 prose-only enrichments (topics already had 3+ generators) plus 16 full-content activations. 4 content + 2 generator + 1 figure sub-agents in parallel. pre_algebra avg score 45.4 -> 61.1.
- **Wave B (commit 6e0994a, algebra) --- 25 stubs, +52 generators, +4 figures.** 7 prose-only + 2 partial-gen extension (systems) + 16 full-content. 4 content + 2 generator + 1 figure sub-agents. algebra avg score 58.1 -> 73.7.
- **Wave C (commit 1d8dd3d, precalculus) --- 16 stubs, +48 generators, +4 figures.** All full-content (0 prose-only available in precalc). 3 content + 2 generator + 1 figure sub-agents. 4 stubs intentionally skipped as redundant/niche (`Conic_Sections_In_Polar_Coordinates`, `Inequalities`, `Parfrac`, `Transformations`). precalculus avg score 54.4 -> 82.1 (the biggest per-branch jump in the phase).

Each wave: content agents prose-enrich stubs, generator agents ship 3+ Python classes per topic, figure agent renders SVGs. Post-wave pipeline: pytest, validate_yaml, lint_wiki, copyright shingle test, build_problem_bank, topic_status, update_course_hubs, build_prereq_graph, apply_test_tags.

**Deliverable 4 --- Wave D (commit b891393, new gap topics) --- 10 new topics, +30 generators, +6 figures.**
- Algebra 2 (5): `Piecewise_Functions`, `Conditional_Probability`, `Margin_Of_Error_And_Confidence_Intervals`, `Sampling_Methods_And_Bias`, `Correlation_And_Residuals`.
- Algebra 1 (1): `Histograms_And_Box_Plots` (quad-tagged: all 4 tests).
- Pre-Calculus (4): `Permutations_And_Combinations`, `Normal_Distribution`, `Expected_Value`, `Binomial_Probability`.
- These filled the identified gaps where tests commonly ask but no stub existed. 3 content + 2 generator + 1 figure sub-agents.

**Rework during waves.** Copyright 15-word shingle test caught ~10 textbook-adjacent phrasings across pre-algebra + algebra content (and zero in Wave C and Wave D --- the forbidden-idiom list in prompts had fully internalized). All resolved via 1-line in-place rewrites. Three generator bank_count_per_difficulty floor adjustments for tight parameter spaces (rearrange_simple_two_step_literal, factor_difference_of_squares_solve, circle_meets_line_substitution, nPr_direct_compute, nCr_direct_compute, combine_rational_and_sign_to_narrow_search). One infinite-loop rewrite: `ratios_and_proportions_algebra.SolveProportionWithVariable` was retrying until a divisibility condition held --- rewrote as pure backward construction picking the cross-product first. Three ad-hoc content tags (`#skill-equation-solving`) replaced with taxonomy tags. Ten dead wikilinks in Wave C3 content (`Scatter_Plots`, `Functions_And_Relations`, `Substitution_Method`, `Quadratic_Equations`, `Conic_Sections`, `Correlation` --- all invented, not live) fixed by pointing to actual live slugs with pipe aliases.

**Final phase stats.**

| Metric | Before | After | Delta |
|---|---:|---:|---:|
| Live topics (3+ gens, 300+ words) | 144 | **210** | +66 |
| Active generators | 460 | **638** | +178 |
| Verified problems | 36,010 | **49,443** | +13,433 |
| Figures | 45 | **62** | +17 |
| Stubs on disk | 112 | **51** | -61 |
| Avg score (pre_algebra) | 45.4 | **61.1** | +15.7 |
| Avg score (algebra) | 58.1 | **74.4** | +16.3 |
| Avg score (precalculus) | 54.4 | **82.1** | +27.7 |
| Avg score (geometry) | 82.7 | 82.7 | -- |
| **Overall avg** | **53.9** | **71.6** | +17.7 |
| Topics with any test tag | 0 | **200+** | +200 |

Four commits shipped in sequence; CI green on every push.

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
- `tools/rewrite_breadcrumbs.py` rewrote every topic-page breadcrumb `> _overview|Home > {OldBranchHub}|Label > Title` and every See Also wikilink pointing at the old branch hubs to point at the new course hub (`Middle_School_Math`, `Algebra_1`, `Algebra_2`, `Precalculus`, `Geometry`) based on each topic's `branch:` field. Ran across 239 topic files.
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

## [2026-04-11] Cluster 10 | HS Geometry expansion

**Scope:** 16 new or enriched topic pages, 50 new SymPy-verified generators in 10 modules, 14 new matplotlib SVG figures.

**New geometry topic pages (10 files, `branch: geometry`):**
- Triangle_Congruence_Criteria (SSS, SAS, ASA, AAS, HL; why AAA and SSA fail)
- Special_Right_Triangles (30-60-90 and 45-45-90 side ratios, derivations)
- Polygon_Angle_Sums (interior sum, exterior sum, regular polygon angles)
- Inscribed_Angles_And_Arcs (central vs inscribed, semicircle case, arc length)
- Chords_Secants_And_Tangents (chord-chord power, tangent perpendicular to radius)
- Equations_Of_Circles (standard to general form and back via completing the square)
- Rigid_Transformations (translations, rotations, reflections, coordinate rules)
- Dilations_And_Similarity (scale factor, area ratio k^2, volume ratio k^3)
- Coordinate_Geometry_Proofs (using slope/distance/midpoint to prove figure types)
- Cross_Sections_Of_Solids (cube, cone, cylinder sections; conic preview)

**Enriched pre-algebra stubs (6 files, kept `branch: pre-algebra`, appear in both Middle School Math and Geometry hubs):**
- Classifying_Triangles_And_Quadrilaterals (triangle classification + quadrilateral hierarchy)
- Points_Lines_Angles_And_Angle_Relationships (basic terms + parallel lines & transversals)
- Volume_Of_Prisms_And_Cylinders (V = Bh, backward construction)
- Volume_Of_Pyramids_And_Cones (V = (1/3)Bh, one-third factor intuition)
- Surface_Area_Of_Prisms_And_Cylinders (net approach, cylinder wraparound)
- Surface_Area_And_Volume_Of_Spheres (4*pi*r^2 and (4/3)*pi*r^3)

**New generator modules (10, 50 total generators):**
- `generators/geometry/parallel_lines.py` (5): alt-interior, corresponding, co-interior, solve-for-x, complementary/supplementary
- `generators/geometry/triangle_congruence.py` (5): identify criterion, find missing side, find missing angle, not-congruent ambiguity, proof-step selection
- `generators/geometry/special_right_triangles.py` (5): 45-45-90 from leg or hypotenuse, 30-60-90 from short/long leg or hypotenuse
- `generators/geometry/polygon_angles.py` (4): interior sum, regular interior, regular exterior, n from interior angle
- `generators/geometry/quadrilaterals.py` (4): parallelogram angle, rectangle diagonal, rhombus side, trapezoid area
- `generators/geometry/circle_theorems.py` (6): inscribed angle from arc, inscribed in semicircle, chord-chord power, tangent-perpendicular-radius, standard to general form, general to standard form
- `generators/geometry/transformations.py` (6): translate, reflect, rotate by 90/180/270, identify rigid transformation, dilate from origin, area/volume ratio from length ratio
- `generators/geometry/volume.py` (6): rectangular prism, cylinder from r+h, cylinder find h, rectangular pyramid, cone, cone find r
- `generators/geometry/surface_area.py` (5): rectangular prism, cube, cylinder, sphere SA, sphere V
- `generators/geometry/coord_geometry.py` (4): parallelogram from slopes, rectangle from perpendicular, rhombus from distances, midpoint drill

**New figures (14, under `wiki/assets/figures/geometry/`):**
parallel_lines_transversal.svg, triangle_congruence_criteria.svg, special_right_triangles.svg, regular_polygon_interior_angle.svg, inscribed_angle_theorem.svg, chord_secant_tangent.svg, quadrilateral_hierarchy.svg, prism_cylinder_labeled.svg, pyramid_cone_labeled.svg, sphere_labeled.svg, rigid_transformations.svg, dilation.svg, coord_proof_parallelogram.svg, cube_cross_sections.svg

**Execution:** 4 parallel sub-agents (Content Batch A: 8 topics, Content Batch B: 8 topics, Generators: 10 modules, Figures: 14 SVGs). Each agent received: gold-standard files to imitate, forbidden-idiom list, structural template, hard constraints, and the current live-topics list for cross-referencing.

**Validation after Cluster 10:**
- `pytest generators/tests/ -q`: **29/29 passing** (parametrized all-generators suite now exercises all 460 generators across all difficulties).
- `validate_yaml.py wiki/`: **263 files clean**.
- `lint_wiki.py wiki/`: **0 errors, 0 warnings, 1 info** (115 stubs, expected).
- `build_problem_bank.py`: **151 topics, 460 generators, 36,010 problems**. Total bank size 29.9 MB. Largest new shard: triangle_congruence_criteria at 306 KB (under the 320 KB limit).
- `topic_status.py`: average score **53.8** (was 50.1 pre-Cluster-10). Geometry branch score jumped from **47.5 to 82.7**. Pre-algebra branch from 39.4 to 45.2.
- `test_copyright_safety.py`: clean first pass. The 4 agents followed the forbidden-idiom list proactively.

**Counts after Cluster 10:**
- Topics: 239 → **249** (+10 new geometry files)
- Live topics: 136 → **151** (+15: 10 new + 5 enriched pre-algebra stubs that stayed pre-algebra but became draft)
- Generators: 410 → **460**
- Problems: 32,698 → **36,010**
- Figures: 31 → **45**

**What worked:**
- Parallelism scaled cleanly at 4 agents. No file collisions, no cross-talk.
- Enriching existing pre-algebra stubs AS WELL AS creating new geometry files gave Cluster 10 reach into two course hubs for the price of one.
- The forbidden-idiom list and fresh-scenario guidance (drones, skate parks, 3D prints) produced zero copyright hits on first pass.
- `GEOMETRY_ADJACENT_ALLOWLIST` in `update_course_hubs.py` automatically surfaced the enriched pre-algebra topics in the Geometry hub without manual cross-listing.

**Cluster 10 complete.** Next: Phase 3 polish (4 outlier topics + figure wave) then Phase 4 (prereq graph widget).

## [2026-04-11] Phase 3 polish + Phase 4 PrereqWidget + Phase 5a Vault export/import

**Phase 3 polish (minimal after Cluster 10's cross-link density):**
- Added `geometry/circle_parts.svg` embed to `Circumference_And_Area_Of_Circles` frontmatter + body.
- Added `pre_algebra/place_value_chart.svg` embed to `Place_Value_Rounding_And_Estimation` frontmatter + body.
- Filled 3 prerequisites on `Place_Value_Rounding_And_Estimation` (previously `[]`).
- The three topics originally flagged at score 70 (Completing_The_Square, Parallel_And_Perpendicular_Lines, Scatter_Plots_And_Trend_Lines) all reached 95 automatically from Cluster 10's new inbound wikilinks -- no hand edits needed.

**Phase 4 prereq graph widget:**
- `tools/build_prereq_graph.py`: walks `wiki/topics/**/*.md`, reads YAML `prerequisites:` lists, normalizes paths to stems, looks up display titles, and writes `wiki/_data/prereq_graph.json`. Graph stats: 92 KB, 249 topics, 137 with prereqs, 400 directed edges. Also emits reverse `used_by` edges for future "next steps" widget.
- `quartz_components/PrereqWidget.tsx`: thin component, server-side empty, registers the inline script + stylesheet.
- `quartz_components/prereqWidget.inline.ts`: fetches graph once per session, extracts current page stem from `location.pathname`, looks up the topic in the graph, injects a "Review these first" card into the right sidebar. Early-returns on non-topic pages. Graceful fallback through sidebar selectors (`.sidebar.right`, `[data-layout="sidebar-right"]`, `.backlinks` parent, `article`).
- `quartz_components/prereqWidget.scss`: compact card styling using existing Quartz theme variables.
- `quartz.layout.ts`: imports `PrereqWidget` and adds it to `sharedPageComponents.afterBody` alongside ProblemVaultWidget and VaultViewer.
- CI: no deploy.yml changes. The existing overlay step already copies the full `quartz_components/` directory into `quartz/components/` before the Quartz build.

**Phase 5a Vault export/import:**
- `quartz_components/vaultViewer.inline.ts` gains two new buttons: **Export JSON** downloads the current vault as `math-wiki-vault-YYYY-MM-DD.json` via a Blob + object URL. **Import JSON** reads a previously-exported file via a hidden file input, validates each entry has `id` and `statement_latex` fields, and offers the student a merge-or-replace confirmation. Merge adds new problems while skipping duplicates by id. Replace wipes the existing vault entirely with the imported set. Malformed files are caught and surfaced via alert() with the error message.
- Accepts two import shapes: a bare array of problems, or the wrapped `{version, exported_at, problem_count, problems}` envelope that Export emits.
- `wiki/Vault.md`: rewritten "How the Vault Works" section to document shuffle, print, export, import, and clear. Status flipped from `stub` → `complete`. Removed the legacy "Phase 1 VaultViewer ships later" placeholder.

**Validation:**
- `pytest generators/tests/ -q`: 29/29 passing.
- `validate_yaml.py wiki/`: 263 files clean.
- `lint_wiki.py wiki/`: 0 errors, 0 warnings, 1 info (114 stubs, down from 115 as Vault.md flipped to complete).

**Deferred Phase 5 items:**
- Custom worksheet builder (dedicated page where the student picks N topics × difficulty × count → mixed set). Requires a new page + new Quartz component. Left for a later session.
- jsPDF polished PDF export (replace `@media print` with a rendered-KaTeX→PDF pipeline). The `window.print()` path works well today and the browser dialog produces a clean worksheet; jsPDF is a nice-to-have, not a blocker.
- Input-and-check answer grader. Stretch goal from the original plan.

**State at end of this session:**
- Topics: 249 (136 live at session start → 151 live now)
- Generators: 460 (was 410; +50)
- Problems: 36,010 (was 32,698; +3,312)
- Figures: 45 (was 31; +14)
- Sidebar: 10 student-first entries (was 14)
- Course hubs: 5 (Middle School Math, Algebra 1, Geometry, Algebra 2, Pre-Calculus & Trig)
- Student-facing wiki: **standalone** (no source-book references anywhere in content)
- New student features: **prereq-graph widget** + **vault export/import**

**Phases 1-4 + 5a complete.** Math Wiki is now navigable from middle school through advanced high school, with the biggest content gap (HS Geometry) filled, a prereq-graph helper in the sidebar, and import/export to move practice sets across devices.
