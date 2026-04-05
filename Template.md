# Template.md --- Meta-Instructions for Generating Wiki Specs
## Version 1.2.0

This document tells the Chief Engineer how to generate a project-specific `[Wiki_Name].md` from any raw input. It is not a template to fill in --- it is a set of meta-instructions that produce a build specification.

**Origin:** Adapted from the Curriculum Factory's Template.md (42 completed textbook projects). Rules here exist because their absence caused real failures across 1 completed wiki build (Hymn Wiki, 1,616 pages, 9 sources).

---

## The Workflow

```
RAW INPUT (documents, books, articles, websites)
    │
    ├── Chief Engineer analyzes the domain and sources
    │
    ▼
Template.md (this file) + domain analysis
    │
    ▼
[Wiki_Name].md (project-specific build spec)
    │
    ▼
Wiki scaffolding + ingest cycles + output generation
    │
    ▼
builds/[Wiki_Name]/ (self-contained Obsidian vault, deployable via Quartz)
```

---

## Required Sections in Every [Wiki_Name].md

### 1. Header

```markdown
# [Wiki_Name].md --- [Full Title]
## [Subtitle: scope and domain]
### Version 1.0.0
```

Key-value table:

| Field | Value |
|-------|-------|
| **Domain** | e.g., Ancient Greek Philosophy |
| **Scope** | What's included and excluded |
| **Audience** | Who will read this wiki |
| **Source count** | Initial number of sources |
| **Expected scale** | Small / Medium / Large |

### 2. Domain Analysis

Describe the knowledge domain:
- What kind of information? (historical, scientific, literary, technical)
- What are the natural categories? (people, events, theories, experiments)
- What relationships matter most? (chronological, causal, thematic, hierarchical)
- Are there established taxonomies to adopt? (scientific classification, historical periods)

### 3. Source Inventory

List all initial sources with metadata:

| # | Title | Type | Size | Priority | Role |
|---|-------|------|------|----------|------|
| 1 | [Title] | book/article/website | pages/words | high/medium/low | What unique info does it provide? |

Note overlaps, biases, and limitations. When adding sources later (Phase C ingest), update this table and increment the spec version.

### 4. Page Type Selection

Not all wikis need every type. Select what applies:

- [ ] **Entities** --- always needed (people, places, organizations, works)
- [ ] **Concepts** --- almost always needed (ideas, themes, theories)
- [ ] **Sources** --- always needed (one per ingested source)
- [ ] **Synthesis** --- needed for comparative/analytical wikis
- [ ] **Timelines** --- needed for chronological domains
- [ ] **Custom type:** [describe if the domain needs something unique]

### 5. Tag Taxonomy Bootstrap

Define the initial controlled vocabulary. This taxonomy will grow during the build, but all new tags must be added to `_tag_taxonomy.md` before use. Include the taxonomy file's content in all sub-agent prompts to prevent tag drift.

### 6. Ingest Workflow

Specify how sources should be processed:

- **Ingest order:** By priority/dependency (backbone sources first, supplements second)
- **Granularity:** One source summary per book? Per chapter? Per article?
- **Entity/concept extraction criteria:** What qualifies in this domain?
- **Contradiction handling:** How should conflicting claims be presented?
- **Citation style:** Inline source attribution pattern

### 7. Output Formats

- [ ] **Quartz HTML site** --- recommended for all wikis intended for non-Obsidian readers
- [ ] **Marp slide decks** --- presentation summaries
- [ ] **Charts/figures** --- data visualizations
- [ ] **Custom:** [describe]

### 8. Conventions

Domain-specific rules for naming, dates, terminology, scope boundaries, and tone.

---

## Scaffolding Checklist

When generating a new build:

1. [ ] Create `builds/[Wiki_Name]/` directory structure (see CLAUDE.md)
2. [ ] Copy `.obsidian/` config from `factory/templates/obsidian/`
3. [ ] Write `[Wiki_Name].md` project spec
4. [ ] Create `wiki/_overview.md` (landing page)
5. [ ] Create `wiki/_index.md` with empty category structure
6. [ ] Create `wiki/_log.md` with header
7. [ ] Create `wiki/_tag_taxonomy.md` with bootstrapped taxonomy
8. [ ] **Create type-overview pages for ALL page types used** (Hymns_Overview, People_Overview, Concepts_Overview, Sources_Overview, Synthesis_Overview, etc.)
9. [ ] Place raw sources in `raw/`
10. [ ] If deploying via Quartz: create `quartz.config.ts` and `quartz.layout.ts` at build root
11. [ ] Begin ingest cycle

---

## Quality Expectations

### Source Summaries
- Capture key claims, evidence, and methodology
- Note perspective, biases, and limitations
- Link every entity and concept mentioned: `[[Entity Name]]`

### Entity Pages
- Brief identification, dates, significance within domain
- Key claims across all sources, with attribution
- Contradictions noted explicitly with `#contradicted` tag
- Related entities and concepts linked

### Concept Pages
- Clear definition, historical development
- Key proponents linked as `[[Entity]]`
- Open questions or debates

### Synthesis Pages
- Clear thesis, evidence from multiple sources with attribution
- Counterarguments noted, conclusions stated with confidence level

---

## Lessons from Completed Builds

### Build 1: Hymn Wiki (v1.0.0 → v2.0.0, 2026-04-04 to 2026-04-05)

**Scale pattern for large source-driven wikis (1,000+ pages):**

When a source contains many structured items (hymns, recipes, case studies, statutes), use a **script-first pipeline**: parse into JSON, generate stub pages programmatically. Reserve LLM effort for narrative content requiring understanding.

**Wave-based parallel ingest for adding sources to an existing wiki:**

Process multiple new sources in waves of 2-3, parallelized by source. Each wave contains sources with minimal entity overlap. Each agent receives the current entity inventory to prevent duplicate creation. Agents output both (a) wiki pages directly and (b) JSON data files for structured extraction. A Python script then fuzzy-matches JSON data into existing pages at scale (e.g., SequenceMatcher at 0.75 threshold matched 419/1,081 Duffield hymn entries to Campbell hymns). This is far more reliable than having agents directly edit hundreds of files.

**Content filter constraints:**

The API blocks reproduction of copyrighted or sensitive text. All such text must be extracted by scripts from source files. Every agent prompt must include explicit "NEVER quote [content type]" instructions.

**Sub-agent YAML and tag hygiene:**

Agents writing YAML frontmatter frequently produce unquoted `#` tags and invent tags. Every agent prompt must: (1) specify `tags: ["#tag-name"]` with quotes, (2) include the actual `_tag_taxonomy.md` content (not just a reference). Run a taxonomy reconciliation after each ingest wave --- expand the taxonomy for legitimate new tags, fix the rest.

**Navigation architecture:**

Every page needs a breadcrumb (`> [[_overview|Home]] > [[Section_Overview|Section]]`). Every page type needs an overview page as a navigation hub. The `_overview.md` landing page must be updated after every ingest wave --- it drifts fast. Create a `Sources_Overview.md` alongside the other overview pages; the original build missed this.

**Quartz deployment:**

- Store `quartz.config.ts` and `quartz.layout.ts` at the wiki build root (not inside outputs/quartz/)
- CI clones Quartz fresh, overlays config, copies `wiki/` to `content/`, builds
- `enableSPA: false` for compatibility with simple servers
- Explorer `filterFn` to exclude large item collections from sidebar (e.g., 1,324 hymn files)
- Graph with `depth: 1` for local view to prevent visual overwhelm
- No `RemoveDrafts` filter (wiki pages use status: draft legitimately)

**GitHub Pages + GitHub Actions:**

Single workflow file. Build + deploy in ~50 seconds for 1,616 pages. Landing page auto-generated from `builds/*/wiki/_overview.md` metadata. Adding a new wiki requires zero landing page edits --- just push a new `builds/[name]/` directory.

**Media enrichment:**

Wikimedia Commons images via thumbnail URLs work in both Obsidian and Quartz with no local downloads. YouTube links should use `<a target="_blank">` for new-window behavior. Quartz strips `<script>` tags from markdown content --- features needing client-side JS must use Quartz custom components or be static.

**Web research fills gaps that book sources miss:**

Primary sources from the 19th-20th century lack modern cultural context. Web search adds the "rest of the story" that enriches stubs beyond what any single book can provide. Prioritize famous items first for maximum reader impact.
