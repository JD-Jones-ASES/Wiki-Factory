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
