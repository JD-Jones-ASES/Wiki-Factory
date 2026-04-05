# Template.md --- Meta-Instructions for Generating Wiki Specs
## Version 1.1.0

This document tells the Chief Engineer how to generate a project-specific `[Wiki_Name].md` from any raw input. It is not a template to fill in --- it is a set of meta-instructions that produce a build specification.

**Origin:** Adapted from the Curriculum Factory's Template.md pattern (42 completed textbook projects). Every rule here exists because its absence caused a real failure or because the Karpathy LLM Wiki pattern requires it.

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
Wiki scaffolding (directories, _index.md, _log.md, _tag_taxonomy.md, _overview.md)
    │
    ├── 1. Create directory structure
    ├── 2. Bootstrap tag taxonomy for this domain
    ├── 3. Write _overview.md (initial landing page)
    ├── 4. Ingest sources one at a time (or batched)
    ├── 5. Compile cross-references
    ├── 6. Lint and iterate
    │
    ▼
builds/[Wiki_Name]/ (self-contained Obsidian vault)
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

```markdown
| # | Title | Type | Size | Priority |
|---|-------|------|------|----------|
| 1 | [Title] | book/article/website | pages/words | high/medium/low |
```

For each source, note: what unique information does it contribute? Does it overlap with other sources? Any known biases or limitations?

### 4. Page Type Selection

Not all wikis need every page type. Select which apply:

- [ ] **Entities** --- always needed (people, places, organizations, works)
- [ ] **Concepts** --- almost always needed (ideas, themes, theories)
- [ ] **Sources** --- always needed (one per ingested source)
- [ ] **Synthesis** --- needed for comparative/analytical wikis
- [ ] **Timelines** --- needed for chronological domains
- [ ] **Custom type:** [describe if the domain needs something unique]

### 5. Tag Taxonomy Bootstrap

Define the initial controlled vocabulary for tags. Organize hierarchically:

```markdown
## Tag Taxonomy

### Domain
- #[broad-category]
  - #[subcategory]
  - #[subcategory]

### Status/Meta
- #needs-review
- #needs-expansion
- #contradicted
- #key-finding
```

This taxonomy will grow during the build. New tags must be added to `_tag_taxonomy.md` before use.

### 6. Ingest Workflow

Specify how sources should be processed for this domain:

- **Ingest order:** Chronological? By importance? By topic?
- **Granularity:** One source summary per book? Per chapter? Per article?
- **Entity extraction:** What counts as an entity in this domain?
- **Concept extraction:** What counts as a concept?
- **Contradiction handling:** How should conflicting claims be presented?
- **Citation style:** How should sources be attributed in wiki pages?

### 7. Output Formats

Specify what consumer products should be generated:

- [ ] **Marp slide decks** --- presentation summaries of key topics
- [ ] **Charts/figures** --- data visualizations, timelines, relationship maps
- [ ] **Comparison tables** --- side-by-side analyses
- [ ] **Reading lists** --- curated source recommendations
- [ ] **Custom:** [describe]

### 8. Conventions

Domain-specific rules:

- **Naming:** How should page titles be formed? (full names vs. short names, translated vs. original)
- **Dates:** What calendar/format? (BCE/CE, specific era conventions)
- **Terminology:** Any standardized terms to prefer? (e.g., "polis" not "city-state")
- **Transliteration:** For non-Latin scripts, what convention? (Pinyin, Romaji, etc.)
- **Scope boundaries:** What is explicitly out of scope?

---

## Frontmatter Schemas

All schemas are defined in `factory/schemas/`. The project spec can extend these with domain-specific fields by adding to the `extra_fields` section.

### Adding Domain-Specific Frontmatter

If the domain requires fields not in the base schema, define them:

```yaml
# In [Wiki_Name].md
extra_fields:
  - name: era
    type: string
    values: [archaic, classical, hellenistic, roman]
    applies_to: [entity, concept]
  - name: school
    type: string
    values: [platonic, aristotelian, stoic, epicurean, skeptic]
    applies_to: [entity, concept]
```

These fields are added to the base schema for this project only.

---

## Scaffolding Checklist

When generating a new build from this template:

1. [ ] Create `builds/[Wiki_Name]/` directory structure (see CLAUDE.md)
2. [ ] Copy `.obsidian/` config from `factory/templates/obsidian/`
3. [ ] Write `[Wiki_Name].md` project spec (this template's output)
4. [ ] Create `wiki/_overview.md` with initial landing page
5. [ ] Create `wiki/_index.md` with empty category structure
6. [ ] Create `wiki/_log.md` with header
7. [ ] Create `wiki/_tag_taxonomy.md` with bootstrapped taxonomy
8. [ ] Place raw sources in `raw/`
9. [ ] Begin ingest cycle

---

## Quality Expectations

### Source Summaries
- Capture key claims, arguments, evidence, and conclusions
- Note the source's perspective, biases, and limitations
- Link to every entity and concept mentioned: `[[Entity Name]]`
- Include page/section references for important claims

### Entity Pages
- Brief identification (who/what/where, dates if applicable)
- Significance within the wiki's domain
- Key claims about this entity across all sources, with attribution
- Contradictions between sources noted explicitly
- Related entities and concepts linked

### Concept Pages
- Clear definition
- Historical development (if relevant)
- Key thinkers/proponents linked as `[[Entity]]`
- Relationship to other concepts
- Open questions or debates

### Synthesis Pages
- Clear thesis or analytical question
- Evidence drawn from multiple sources with attribution
- Counterarguments or alternative interpretations noted
- Conclusions stated with confidence level

---

## Self-Improvement During Build

As the wiki grows, the project spec `[Wiki_Name].md` should be updated:

- **What worked:** Reinforce with concrete examples
- **What failed:** Integrate the fix into the relevant section
- **What's unnecessary:** Remove
- **What's missing:** Add

The spec should get shorter and more precise with each iteration. After the build is approved, generalizable lessons return to this Template.md.

---

## Lessons from Completed Builds

### Build 1: Hymn Wiki (2026-04-04)

**Scale pattern for large source-driven wikis (1,000+ pages):**

When a source contains a large number of structured items (hymns, recipes, case studies, statutes), use a **script-first pipeline**: parse the source into JSON, then generate stub pages programmatically. Reserve LLM effort for narrative content (biographies, analysis, synthesis) that requires understanding and summarization.

**Content filter constraints:**

The content API will block reproduction of copyrighted or sensitive text (song lyrics, certain religious texts, etc.). All such text must be extracted by Python scripts directly from source files --- never generated by the LLM. Agent prompts for narrative ingest must include explicit "NEVER quote [content type]" instructions.

**Sub-agent YAML hygiene:**

Sub-agents writing YAML frontmatter frequently produce unquoted `#` tags (interpreted as YAML comments) and invent tags not in the taxonomy. Every sub-agent prompt must specify: (1) tags must be quoted (`["#tag-name"]`), and (2) only tags from `_tag_taxonomy.md` may be used. Run a batch YAML fix script after each ingest wave.

**Navigation for non-Obsidian delivery:**

Add a breadcrumb navigation line (`> [[_overview|Home]] > Section`) to every wiki page via script. Create type-overview pages (one per page type) as navigation hubs. This serves both Obsidian users and HTML export. The `add_navigation.py` script handles this.

**HTML export via Quartz:**

Quartz v4 is the recommended static site generator for Obsidian vaults. Key settings: `enableSPA: false` (required for simple local servers), remove `RemoveDrafts` filter (wiki pages use status: draft). Include a `_serve.py` (clean-URL Python server) and `Start_Wiki.bat` launcher in the HTML output for local browsing. The Quartz `content/` directory receives a copy of the wiki, and `index.md` is a copy of `_overview.md`.

**Custom page types:**

The base schemas (entity, concept, source, synthesis, timeline) are extensible. The Hymn Wiki added a `hymn` type with domain-specific fields (meter, first_line, hymn_number, scripture_refs). Add the custom type to `lint_wiki.py`'s `VALID_TYPES` set. Add the schema YAML to `factory/schemas/`.

**Scaffolding checklist update:**

Add to the scaffolding checklist:
- [ ] Create type-overview pages (one per page type used)
- [ ] Add navigation breadcrumbs to all pages via `add_navigation.py`
- [ ] If HTML export planned: configure Quartz and include launcher scripts
