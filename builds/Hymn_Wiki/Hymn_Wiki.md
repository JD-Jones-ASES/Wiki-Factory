# Hymn_Wiki.md --- A Comprehensive Guide to Christian Hymns
## Stories, History, and Scripture Behind the Songs of Faith
### Version 2.0.0

| Field | Value |
|-------|-------|
| **Domain** | Christian Hymnody |
| **Scope** | Hymns, hymn writers, composers, theological themes, and musical traditions from early Christianity through the early 20th century |
| **Audience** | General reader; a mother who loves Christian hymns. Warm, accessible, modern English. |
| **Source count** | 9 (7 hymn history/reference books + 1 hymnal + KJV Bible) |
| **Scale** | Large (1,616 pages) |
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

**Ingest pattern:** Sources 1-4 were ingested in v1.0.0 (initial build). Sources 5-9 were ingested in v2.0.0 via wave-based parallel agents with JSON intermediary files for cross-source enrichment.

---

## Current Stats (v2.0.0)

| Type | Count | Status |
|------|-------|--------|
| Hymns | 1,324 | 500 draft, 824 stub |
| Entities | 227 | Mostly draft; 22 with Wikimedia portraits |
| Concepts | 39 | Draft |
| Sources | 9 | Draft/Complete |
| Synthesis | 5 | Draft |
| Timelines | 1 | Draft |
| Navigation pages | ~12 | Overview hubs, indexes |
| **Total** | **~1,616** | |

---

## Page Types & Schema

- **Hymns** (custom type) --- 1,324 pages, one per Campbell hymn number. Extra fields: `hymn_number`, `first_line`, `meter`, `topic`, `author`, `composer`, `tune_name`, `scripture_refs`, `stanza_count`, `era`. Schema: `factory/schemas/hymn.yaml`.
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
- **Build time:** ~50 seconds for 1,616 pages
- **Config files:** `quartz.config.ts` and `quartz.layout.ts` at wiki build root (overlaid onto fresh Quartz clone during CI)
- **Key Quartz settings:** `enableSPA: false`, no `RemoveDrafts` filter, Explorer `filterFn` excludes individual hymn pages from sidebar, Graph depth-1 for local view
- **Landing page:** Auto-generated by `factory/scripts/build-landing.sh` from wiki metadata

---

## Conventions

- **Hymn titles:** `Hymn_NNNN_First_Line_Words.md` (zero-padded to 4 digits)
- **Entity names:** Full anglicized names
- **Dates:** CE format (1674-1748)
- **Tone:** Warm, accessible, modern English. This is a gift, not a dissertation.
- **Scope:** Western Christian hymns through ~1930. Contemporary worship music is out of scope.
- **Tags:** Always quoted in YAML: `tags: ["#tag-name"]`. Only taxonomy tags.
- **Lyrics:** NEVER reproduced by LLM. All hymn text via Python scripts from source files.
- **External links (YouTube, images):** Use `<a target="_blank">` for new-window behavior in Quartz.

---

## Self-Improvement Log

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
