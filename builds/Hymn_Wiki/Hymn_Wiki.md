# Hymn_Wiki.md --- A Comprehensive Guide to Christian Hymns
## Stories, History, and Scripture Behind the Songs of Faith
### Version 3.0.0

| Field | Value |
|-------|-------|
| **Domain** | Christian Hymnody |
| **Scope** | Hymns, hymn writers, composers, theological themes, and musical traditions from early Christianity through the early 20th century |
| **Audience** | General reader; a mother who loves Christian hymns. Warm, accessible, modern English. |
| **Source count** | 11 (8 hymn history/reference books + 2 hymnals + KJV Bible) |
| **Scale** | Large (~1,890 pages) |
| **Deployment** | GitHub Pages via Quartz v4 + GitHub Actions CI/CD |

---

## Source Inventory

| # | Title | Author/Compiler | Type | Year | Lines | Role |
|---|-------|----------------|------|------|-------|------|
| 1 | The Christian Hymn Book | Alexander Campbell | Hymnal (1,324 hymns) | 1870 | 39,567 | **Structural backbone** --- all hymn texts |
| 2 | The Story of Our Hymns | Ernest Edwin Ryden | History/biography | 1930 | 16,023 | **Biographical backbone** --- chronological, by tradition |
| 3 | The Story of the Hymns and Tunes | Brown & Butterworth | History/narrative | 1906 | 18,946 | Musical/thematic depth, tune stories |
| 4 | King James Bible | --- | Scripture | 1611 | 99,971 | Verse integration (458 hymn linkages) |
| 5 | The English Hymn | Louis F. Benson | Institutional history | 1915 | 34,910 | Denominational adoption patterns |
| 6 | English Hymns: Authors & History | S.W. Duffield | Hymn encyclopedia | 1886 | 38,337 | Hymn-by-hymn entries (1,081 extracted) |
| 7 | Baptist Hymn Writers | Henry S. Burrage | Biographical dictionary | 1888 | 36,616 | 200+ Baptist writers globally |
| 8 | Hymns & Hymn Writers of the Church | Nutter & Tillett | Annotated hymnal | 1911 | 90,912 | 383 hymns annotated, 306 author profiles |
| 9 | American Sacred Music Writers | Frank J. Metcalf | Composer dictionary | 1925 | 15,981 | 70+ tune composers, tune-to-hymn pairings |
| 10 | A Book of Hymns for Public and Private Devotion | Longfellow & Johnson | Hymnal (600 hymns) | 1848 | 19,000 | Second hymnal; 416 unique + 184 overlap with Campbell |
| 11 | The Singing Church | Edmund S. Lorenz | Pastoral hymnology | 1938 | 11,474 | Theory, history, and practical use of hymns |

**Ingest pattern:** Sources 1-4 ingested in v1.0.0. Sources 5-9 ingested in v2.0.0 via wave-based parallel agents. Sources 10-11 ingested in v3.0.0: hymnal parsed via scripted extraction with cross-reference matching; pastoral book via 3-wave LLM narrative ingest.

---

## Current Stats (v3.0.0)

| Type | Count | Status |
|------|-------|--------|
| Hymns | 1,740 | 1,324 Campbell + 416 Longfellow-Johnson (184 cross-referenced) |
| Entities | 284 | Mostly draft; 33 enriched with Lorenz; 22 with Wikimedia portraits |
| Concepts | 46 | Draft; 7 new from Lorenz (hymnology theory + practice) |
| Sources | 11 | Draft/Complete |
| Synthesis | 5 | Draft |
| Timelines | 1 | Draft |
| Navigation pages | ~12 | Overview hubs, indexes, scripture index |
| **Total** | **~1,890** | |

---

## Page Types & Schema

- **Hymns** (custom type) --- 1,740 pages from two collections. Campbell: `Hymn_NNNN_...`, Longfellow-Johnson: `Hymn_LJ_NNNN_...`. Extra fields: `hymn_number`, `first_line`, `meter`, `topic`, `author`, `composer`, `tune_name`, `scripture_refs`, `stanza_count`, `era`, `collection`. Schema: `factory/schemas/hymn.yaml`.
- **Entities** --- hymn writers, composers, translators, historical figures
- **Concepts** --- theological themes, musical forms, historical movements, denominational traditions
- **Sources** --- one per ingested source document
- **Synthesis** --- cross-cutting analyses
- **Timelines** --- chronological narratives

---

## Ingest Workflow

### Phase A: Scripted Extraction (no LLM)

For sources with structured data (hymnals, Bibles): parse into JSON, generate stub pages programmatically. Scripts: `parse_campbell.py`, `parse_kjv.py`, `generate_hymn_pages.py`, `bible_linker.py`.

### Phase B: LLM Narrative Ingest (initial sources)

Process each Part/Chapter as a unit via parallel Sonnet agents. Each agent gets a source section, the existing entity list, and clear create/update instructions.

### Phase C: Wave-Based Batch Ingest (additional sources)

For ingesting multiple new sources into an existing wiki:

1. **Copy sources to `raw/`**, create source pages in `wiki/sources/`
2. **Generate current entity/concept inventory** for agent reference (prevents duplicates)
3. **Process in waves** of 2-3 books per wave, parallelized by source:
   - Wave 1: Sources with least entity overlap (new composers, new traditions)
   - Wave 2: Sources with moderate overlap (update existing + create new)
   - Wave 3: Largest source, split across multiple agents by section
4. **Each agent outputs two things:** (a) wiki pages created/updated directly, (b) JSON data files for structured extraction
5. **Run enrichment script** to fuzzy-match JSON data into existing pages (e.g., `enrich_hymns.py` matched 419 Duffield entries to Campbell hymns using SequenceMatcher at 0.75 threshold)
6. **Post-wave:** rebuild index, update taxonomy, lint, update overview pages

### Phase D: Web Research Enrichment

For famous items where book sources are thin, web search fills gaps. Focus on stories, cultural impact, and facts that primary sources miss (e.g., Amazing Grace's African-American final stanza, Joy to the World's misidentification as a Christmas carol).

### Phase E: Media Enrichment

- **Wikimedia Commons:** Portraits and historical scene images via thumbnail URLs (`/thumb/.../250px-filename`). Works in both Obsidian and Quartz without downloading files.
- **YouTube:** Performance links on hymn pages. Convert to `<a target="_blank">` for new-window behavior in Quartz.

---

## Deployment

**GitHub Pages** via Quartz v4 static site generator with GitHub Actions CI/CD.

- **Repo:** `JD-Jones-ASES/Wiki-Factory` (public)
- **URL:** `https://JD-Jones-ASES.github.io/Wiki-Factory/Hymn_Wiki/`
- **Build time:** ~60 seconds for ~1,890 pages
- **Config files:** `quartz.config.ts` and `quartz.layout.ts` at wiki build root (overlaid onto fresh Quartz clone during CI)
- **Key Quartz settings:** `enableSPA: false`, no `RemoveDrafts` filter, Explorer `filterFn` excludes hymns/entities/concepts folders from sidebar, `mapFn` for friendly folder names, Graph depth-1 for local view
- **Landing page:** Auto-generated by `factory/scripts/build-landing.sh` from wiki metadata

---

## Conventions

- **Hymn titles:** Campbell: `Hymn_NNNN_First_Line_Words.md`. Longfellow-Johnson: `Hymn_LJ_NNNN_First_Line_Words.md`.
- **Entity names:** Full anglicized names
- **Dates:** CE format (1674-1748)
- **Tone:** Warm, accessible, modern English. This is a gift, not a dissertation.
- **Scope:** Western Christian hymns through ~1930. Contemporary worship music is out of scope.
- **Tags:** Always quoted in YAML: `tags: ["#tag-name"]`. Only taxonomy tags.
- **Lyrics:** NEVER reproduced by LLM. All hymn text via Python scripts from source files.
- **External links (YouTube, images):** Use `<a target="_blank">` for new-window behavior in Quartz.

---

## Self-Improvement Log

### Version 3.0.0 --- Two-Source Ingest + Navigation Redesign (2026-04-05)

**Stats:** ~1,890 pages. 1,740 hymns (+416 LJ), 284 entities (+2 new, 33 Lorenz-enriched, 116 with hymn listings), 46 concepts (+7), 11 sources (+2). Navigation redesigned.

**What worked:**
- **Multi-hymnal integration via scripted cross-reference.** Parsed a second 600-hymn collection into JSON, fuzzy-matched first lines against existing hymns (184 overlaps at 0.75 threshold), auto-generated 416 new pages and enriched 181 existing pages. The `Hymn_LJ_` prefix cleanly separates the two collections while sharing the same wiki infrastructure.
- **Pastoral/expository source via 3-wave LLM narrative ingest.** The Lorenz book (theory, history, practical) split naturally into 3 parallel agents. Each wave targeted different page types (concepts vs. entity enrichment vs. practical concepts). 33 entity pages enriched with "From Lorenz (1938)" subsections; 7 new concept pages created.
- **Author-hymn reverse mapping.** Script-built "Hymns in The Christian Hymn Book" sections for 116 author pages (748 hymns linked). Campbell's abbreviated author names (e.g., "Mrs. Steele" → Anna_Steele) required a manual mapping dictionary.
- **Navigation redesign.** Tiered landing page (Start Here > Explore > More). Explorer sidebar filtered to ~15 items (hid entities/ and concepts/ folders). Hub cross-linking via "See Also" sections. Prolific-authors table on People_Overview.

**What failed and how it was fixed:**
- **YAML corruption from regex in cross-reference script.** The `integrate_longfellow_johnson.py` script used a non-greedy regex `(.+?)` to match `source_refs` arrays, which broke on wikilinks containing `]]`. This produced malformed YAML that failed the Quartz build. Fix: rebuilt all 181 affected source_refs from scratch. Prevention: use greedy match or extract wikilinks by pattern, never by simple bracket matching.
- **Unescaped quotes in generated frontmatter.** Hymn titles containing quotation marks (e.g., `"It is Good to be Here."`) produced invalid YAML when inserted into `topic:` and `title:` fields. Fix: replaced internal double quotes with single quotes in 416 files. Prevention: the page-generation script must sanitize all string values before writing frontmatter.
- **Stray backslashes from cascading fixes.** The first quote-fix pass replaced `"` with `'` but left `\'` artifacts in 11 files. Fix: second pass removed all backslashes from frontmatter. Prevention: validate YAML with `yaml.safe_load()` after every batch modification.
- **Two failed GitHub Pages builds.** Caused by the YAML issues above. Prevention: add YAML validation as a pre-commit check or CI gate.

**What v2.0.0 flagged and v3.0.0 addressed:**
- ✅ Resolved dead author wikilinks (282 entities now, all linked)
- ✅ Added author → hymn reverse navigation (116 entity pages with hymn listings)
- ⬜ Adding `related` links to hymn pages (still mostly empty on non-enriched pages)

### Version 2.0.0 --- Five-Source Ingest + GitHub Pages (2026-04-05)

**Stats:** 1,616 pages. 227 entities (+67), 39 concepts (+9), 9 sources (+5). 500 hymns upgraded stub→draft. 486 hymns received historical context. 22 pages with Wikimedia portraits. 12 hymns with YouTube links. Site live on GitHub Pages.

**What worked:**
- **Wave-based parallel ingest.** 217K lines across 5 books processed via 8+ Sonnet agents in 3 waves (~2 hours wall time). Each wave contained sources with minimal entity overlap. Zero merge conflicts.
- **JSON intermediary pattern.** Agents extracted structured data (tune mappings, hymn annotations, composer data) into JSON files. A Python script then fuzzy-matched and injected into 1,324 hymn pages. Far more reliable than having agents directly edit hundreds of files.
- **GitHub Actions CI/CD.** Single workflow file deploys in ~50 seconds. Quartz cloned fresh each build (no node_modules in repo). Landing page auto-discovers wikis from `builds/*/`.
- **Wikimedia Commons via URL.** Thumbnail pattern (`/thumb/.../250px-filename`) works in Obsidian and Quartz with no local downloads.
- **Web search fills gaps books miss.** Cultural context, modern scholarship, and "rest of the story" details that 19th/early 20th century sources couldn't cover.

**What failed and how it was fixed:**
- **Quartz strips `<script>` from markdown.** Random Hymn page with client-side JS redirect didn't work. Fix: replaced with static discovery page. Lesson: features needing JS require Quartz custom components (TypeScript in `quartz/components/`) or must be static.
- **Explorer sidebar overwhelm.** 1,324 hymn files expanded in sidebar was unusable. Fix: `filterFn` in layout to exclude `Hymn_*` slugs. Users navigate via search, overview pages, or direct links.
- **Tag drift across many agents.** Despite instructions, agents created ~60 non-taxonomy tags. Fix: expanded taxonomy post-ingest. Prevention: include the actual taxonomy file content in agent prompts, not just a reference to it.
- **Overview page drift.** The `_overview.md` showed "four sources" long after 9 existed, and had duplicate navigation sections. Fix: manual update. Prevention: add "update overview page" as an explicit step in every ingest wave checklist.
- **Missing Sources_Overview.md.** New source pages used breadcrumbs pointing to a page that didn't exist. Fix: created it. Prevention: scaffolding checklist must include ALL type-overview pages, not just the ones that seem obvious at build time.

**What v1.0.0 flagged and v2.0.0 addressed:**
- ✅ Enriching hymn stubs with historical context (486 pages)
- ✅ Populating empty `era` and `composer` fields (505 era, 29 composer)
- ⬜ Adding `related` links to hymn pages (still mostly empty)
- ⬜ Resolving ~30 dead author wikilinks (partially addressed via new entities)

### Version 1.0.0 --- Initial Build (2026-04-04)

**Stats:** 1,530 pages. 1,324 hymns, 160 entities, 23 concepts, 5 synthesis, 1 timeline, 4 sources.

**Key lessons (still valid):**
- Script-first extraction for structured data at scale
- Parallel sub-agents for narrative ingest
- "NEVER quote hymn lyrics" in every agent prompt
- YAML `#` tags must be quoted
- Breadcrumb navigation on every page via script
- Type-overview pages as navigation hubs
