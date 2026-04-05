# CLAUDE.md --- Wiki Factory Operating Instructions
## Version 1.2.0

---

## What This Is

This file governs the Wiki Factory --- a system that transforms raw inputs (documents, books, articles, websites) into structured, interlinked Markdown wikis. Claude Code operates as the **CTO and Chief Engineer**, with authority to hire sub-agents, select tools, and make architectural decisions autonomously.

Each build is a self-contained Obsidian vault in `builds/[Wiki_Name]/`, zippable and deliverable.

| Field | Value |
|-------|-------|
| **Root** | `C:\Wiki_Factory` |
| **Platform** | Windows 11, `py -3` for Python |
| **Repository** | Git-tracked, deployed via GitHub Pages |
| **License** | CC BY-SA 4.0 (wiki content), MIT (tooling) |

---

## Architecture: Three Layers

```
[RAW SOURCES]  ──→  [THE WIKI]  ──→  [OUTPUTS]
  Immutable           LLM-owned        Derived
  User-curated        Markdown          Slides, HTML, charts
```

**Raw sources** (`raw/`) --- immutable input documents. The LLM reads but never modifies these.

**The wiki** (`wiki/`) --- LLM-generated and LLM-maintained Markdown. Summaries, entity pages, concept pages, syntheses, an index, a log. The LLM owns this layer entirely. The user reads it; the LLM writes it.

**Outputs** (`outputs/`) --- consumer products derived from the wiki. Marp slide decks, charts, future HTML sites. Generated on demand.

---

## Layered Inheritance

```
CLAUDE.md (this file)
    │  Global conventions, operations, quality gates
    ▼
Template.md
    │  Meta-instructions for generating project specs
    ▼
builds/[Wiki_Name]/[Wiki_Name].md
    │  Project-specific spec (inherits + overrides)
    ▼
The wiki pages themselves
```

- **CLAUDE.md** defines how the factory works. Read this every session.
- **Template.md** defines how to generate a project spec from raw input. Read this when starting a new build.
- **[Wiki_Name].md** defines project-specific conventions. This file self-improves during the build. Read this when resuming a build.

A project spec can override any Template.md default. Template.md can reference but never override CLAUDE.md.

---

## The Factory Pipeline

```
[RAW INPUT]
    │
    ▼
┌─────────────────────────────────┐
│  INGEST                         │
│  Read source → extract info     │
│  Write source summary page      │
│  Update entity/concept pages    │
│  Update index + log             │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  COMPILE                        │
│  Cross-reference pages          │
│  Resolve contradictions         │
│  Build synthesis pages          │
│  Strengthen wikilinks           │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  LINT                           │
│  Health-check the wiki          │
│  Find orphans, stubs, gaps      │
│  Verify tag taxonomy            │
│  Check frontmatter consistency  │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  OUTPUT                         │
│  Generate slides (Marp)         │
│  Generate charts (matplotlib)   │
│  File useful Q&A back to wiki   │
└─────────────────────────────────┘
```

---

## Operations

### Ingest

Process a new source into the wiki. A single source may touch 10-15 wiki pages.

1. Validate the source exists and is readable
2. Read the source completely
3. Create a source summary page in `wiki/sources/` with full frontmatter
4. For each entity mentioned: create or update its page in `wiki/entities/`
5. For each concept discussed: create or update its page in `wiki/concepts/`
6. Add wikilinks (`[[Page Name]]`) in every page that references another
7. Update `wiki/_index.md` with new entries
8. Append to `wiki/_log.md`: `## [YYYY-MM-DD] ingest | Source Title`

**Critical:** After ingest, check existing pages for information the new source contradicts or supplements. Update those pages, noting the contradiction with source attribution.

### Query

Answer questions against the wiki.

1. Read `wiki/_index.md` to find relevant pages
2. Read those pages
3. Synthesize an answer with `[[wikilink]]` citations
4. If the answer is substantive and reusable, file it as a new wiki page (synthesis or concept)

**Important:** Good answers compound. A comparison, an analysis, a connection --- these should be filed back into the wiki so future queries benefit from past work.

### Lint

Health-check the wiki. Run periodically or when the user requests it.

- **Orphan pages:** pages with no inbound wikilinks
- **Dead links:** wikilinks pointing to non-existent pages
- **Stale pages:** pages not updated despite newer contradicting sources
- **Stub pages:** status: stub that should be expanded
- **Tag violations:** tags not in `_tag_taxonomy.md`
- **Missing frontmatter:** pages lacking required YAML fields
- **Index drift:** pages that exist but aren't listed in `_index.md`

Use `py -3 factory/scripts/lint_wiki.py builds/[Wiki_Name]/wiki/` for automated checks. Manual review for semantic issues (contradictions, staleness).

### Build (Outputs)

Generate consumer products from wiki content.

- **Marp slides:** `npx marp [input.md] -o [output.html]`
- **Charts:** `py -3` with matplotlib
- **Quartz HTML site (local):** Clone Quartz into `outputs/quartz/`, copy wiki into `content/`, run `npx quartz build`. Key config: `enableSPA: false`, no `RemoveDrafts` filter, copy `_overview.md` as `content/index.md`.
- **GitHub Pages (production):** Store `quartz.config.ts` and `quartz.layout.ts` at wiki build root. CI workflow (`.github/workflows/deploy.yml`) clones Quartz fresh, overlays config, copies wiki to content, builds, deploys. Landing page auto-generated from `builds/*/` metadata. Push to `main` triggers build + deploy (~50 seconds).

**Quartz UX for large wikis:**
- Explorer sidebar: use `filterFn` to exclude large item collections (e.g., 1,324 hymn files) from sidebar navigation. Users navigate via search, overview pages, or direct links.
- Graph view: set `localGraph.depth: 1` to show only direct connections, preventing visual overwhelm.
- External links (YouTube, etc.): use `<a target="_blank">` since standard markdown links open in the same tab.
- Quartz strips `<script>` tags from markdown. Features needing client-side JS require Quartz custom components (TypeScript in `quartz/components/`) or must be static alternatives.

---

## Page Types and Frontmatter

Every wiki page has YAML frontmatter. Required fields:

```yaml
---
title: "Page Title"
type: entity | concept | source | synthesis | timeline | overview | [custom]
aliases: []
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_refs: []
related: []
status: stub | draft | complete
confidence: high | medium | low
---
```

See `factory/schemas/` for full schema definitions per page type.

### Page Type Guidelines

| Type | Directory | Purpose | Example |
|------|-----------|---------|---------|
| **entity** | `entities/` | People, places, organizations, works | `Aristotle.md` |
| **concept** | `concepts/` | Ideas, themes, theories, methods | `Virtue_Ethics.md` |
| **source** | `sources/` | One per ingested source document | `Nicomachean_Ethics.md` |
| **synthesis** | `synthesis/` | Cross-cutting analysis, comparisons | `Greek_vs_Roman_Ethics.md` |
| **timeline** | `timelines/` | Chronological narratives | `Ancient_Philosophy_Timeline.md` |
| **overview** | root wiki/ | Landing page, executive summary | `_overview.md` |
| **[custom]** | `[custom]/` | Domain-specific type (define schema in `factory/schemas/`) | `hymn` type in Hymn Wiki |

Projects may define custom page types. Add the schema YAML to `factory/schemas/` and the type name to `lint_wiki.py`'s `VALID_TYPES`.

---

## Scaling Strategy

### Small wiki (<100 pages)
- `_index.md` maintained manually by the LLM
- Tags browsed via Obsidian tag pane
- Wikilinks + backlinks sufficient for navigation

### Medium wiki (100-500 pages)
- `_index.md` organized hierarchically by type and subcategory
- `_tag_taxonomy.md` enforced --- no ad-hoc tags
- `py -3 factory/scripts/build_index.py` to regenerate index from frontmatter
- Dataview queries for dynamic views

### Large wiki (500+ pages)
- Scripted index regeneration mandatory (manual index maintenance breaks down)
- Consider subdirectories within type folders (e.g., `entities/people/`, `entities/places/`)
- Consider search tooling (qmd or custom)
- Periodic lint runs to catch drift
- **Wave-based parallel ingest** for adding multiple sources: process in waves of 2-3 books, each wave handling sources with minimal entity overlap. Use JSON intermediary files for structured extraction, then a Python script to fuzzy-match and inject into existing pages at scale.
- **Explorer sidebar filtering** in Quartz: use `filterFn` to hide large item collections (1,000+ items) from the sidebar. Users navigate via search and overview pages instead.

---

## Build Directory Structure

Every project in `builds/` follows this layout:

```
builds/[Wiki_Name]/
├── [Wiki_Name].md             ← Project spec (self-improving)
├── quartz.config.ts           ← Quartz site config (overlaid during CI build)
├── quartz.layout.ts           ← Quartz layout config (overlaid during CI build)
├── .obsidian/                 ← Vault config (from factory/templates/obsidian/)
├── raw/                       ← Immutable source documents (gitignored)
│   ├── assets/                ← Downloaded images from sources
│   └── [source files]
├── wiki/                      ← LLM-generated markdown
│   ├── _index.md              ← Content catalog
│   ├── _log.md                ← Chronological operations log
│   ├── _overview.md           ← Landing page (UPDATE AFTER EVERY INGEST WAVE)
│   ├── _tag_taxonomy.md       ← Controlled tag vocabulary
│   ├── [Type]_Overview.md     ← One navigation hub per page type
│   ├── entities/
│   ├── concepts/
│   ├── sources/
│   ├── synthesis/
│   ├── timelines/
│   └── assets/                ← Wiki-generated images
└── outputs/                   ← Derived artifacts (gitignored)
    ├── slides/                ← Marp slide decks
    ├── charts/                ← Generated visuals
    ├── site/                  ← Quartz HTML site (local browsing)
    └── quartz/                ← Quartz build directory (local dev only)
```

---

## Naming Conventions

- **Page files:** `Title_With_Underscores.md` (no spaces, capitalize significant words)
- **Wikilinks:** `[[Title With Spaces]]` or `[[Title_With_Underscores]]` (Obsidian resolves both)
- **Tags:** `#lowercase-kebab-case` from the controlled taxonomy
- **Source files:** keep original filenames in `raw/`, reference by title in source summary pages
- **Directories:** lowercase with underscores where needed

---

## Self-Improvement Protocol

### During Iteration (per-project)

While building a wiki, the project spec `[Wiki_Name].md` self-improves:
- Discovered pitfalls get integrated (not appended --- woven into relevant sections)
- Unnecessary instructions get removed
- Patterns that worked get reinforced with concrete examples
- The spec gets shorter and more precise, not longer

### After Completion (factory-wide)

When a wiki build is approved:
1. The Chief Engineer reviews what `[Wiki_Name].md` learned
2. Generalizable lessons are integrated into `Template.md`
3. Redundant or superseded instructions in `Template.md` are removed
4. `Template.md` version is incremented

**The measure of improvement is compression, not accumulation.**

---

## Tool Manifest

| Tool | Purpose | Cost |
|------|---------|------|
| **Python 3** | Scripting, charts, wiki tooling | Free |
| **Marp CLI** | Markdown → slides (HTML/PDF/PPTX) | Free |
| **Obsidian** | IDE for browsing/editing the wiki | Free |
| **Git / GitHub** | Version control + deployment | Free |
| **GitHub Pages** | Static site hosting via Actions CI/CD | Free |
| **GitHub CLI (`gh`)** | Repo management, Actions monitoring | Free |
| **Claude Code** | Chief Engineer | API budget |
| **Matplotlib** | Chart/figure generation | Free |
| **Quartz v4** | Obsidian vault → static HTML site | Free |
| **Wikimedia Commons** | Public domain images (portraits, scenes) | Free |
| **Web Search** | Research to enrich stubs beyond book sources | Free |

### Liberal Tool Autonomy

The Chief Engineer is explicitly authorized to:
- Install Python packages as needed (`pip install`)
- Install npm packages as needed
- Use web search to research best practices
- Choose libraries and approaches based on engineering judgment
- Add new tools to this manifest when justified
- Run background processes for long operations
- Launch parallel agents for independent tasks

---

## Quality Gates

```
RAW SOURCE ──[exists, readable]──→ INGEST
WIKI PAGES ──[frontmatter valid, links resolve]──→ COMPILE
COMPILED WIKI ──[index current, no orphans]──→ LINT
LINT PASS ──[no critical issues]──→ OUTPUT
```

No output moves forward without validation.

---

## Standing Orders

- **Always add frontmatter** to every wiki page. No exceptions.
- **Always update `_index.md`** after creating or deleting a page.
- **Always append to `_log.md`** after every ingest, lint, or significant edit.
- **Always update `_overview.md`** after every ingest wave. It drifts fast (source counts, page counts, navigation sections). This is the user's front door.
- **Always use wikilinks** `[[Page Name]]` for cross-references, never raw markdown links between wiki pages.
- **Always check for contradictions** when ingesting a new source --- update existing pages that the new information affects.
- **Always use the tag taxonomy** --- no ad-hoc tags. Propose new tags to the taxonomy first. When prompting sub-agents, include the actual taxonomy content, not just a reference to the file.
- **Never modify raw sources** --- `raw/` is immutable.
- **Always add navigation breadcrumbs** to every wiki page: `> [[_overview|Home]] > [[Section_Overview|Section]]`. Use `py -3 factory/scripts/add_navigation.py` for bulk injection.
- **Always create type-overview pages** for every page type used (Hymns_Overview, People_Overview, Concepts_Overview, Sources_Overview, Synthesis_Overview, etc.). Missing overview pages = broken breadcrumbs.
- **Always quote tag values in YAML** --- write `tags: ["#tag-name"]` not `tags: [#tag-name]`. Unquoted `#` is a YAML comment.
- **Never reproduce copyrighted or sensitive content via LLM** --- song lyrics, poems, etc. must come from source files via scripts.
- **Never add instructions that duplicate existing ones** --- integrate or replace.
- **Research before implementing** --- web search for best practices, not guesswork.
- **External links open in new windows** --- use `<a target="_blank" rel="noopener">` for YouTube, Wikimedia, and other external links in wiki pages destined for Quartz rendering.
