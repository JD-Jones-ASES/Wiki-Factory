# Hymn_Wiki.md --- A Comprehensive Guide to Christian Hymns
## Stories, History, and Scripture Behind the Songs of Faith
### Version 1.0.0

| Field | Value |
|-------|-------|
| **Domain** | Christian Hymnody |
| **Scope** | Hymns, hymn writers, composers, theological themes, and musical traditions from early Christianity through the early 20th century |
| **Audience** | General reader; a mother who loves Christian hymns. Warm, accessible, modern English. |
| **Source count** | 4 (3 hymn history books + KJV Bible) |
| **Expected scale** | Large (1,500+ pages) |

---

## Domain Analysis

Christian hymnody spans 2,000 years of worship through song. The domain naturally organizes around:

- **Hymns** --- the central artifacts. Each has text, a writer, often a composer, a historical context, and theological themes.
- **People** --- hymn writers, composers, translators, and related historical figures.
- **Themes** --- theological and devotional categories (praise, suffering, trust, missions, etc.).
- **Traditions** --- denominational and national streams (Lutheran, Methodist, Anglican, American, German, Scandinavian, etc.).
- **Eras** --- historical periods that shaped hymnody (Reformation, Pietism, Great Awakening, Revival, etc.).
- **Musical forms** --- meters (Common, Long, Short), tune names, and compositional traditions.
- **Scripture** --- Bible passages that inspired or are referenced by hymns.

Key relationships: chronological (who influenced whom), thematic (hymns sharing theological concerns), scriptural (hymns based on the same passages), and musical (shared tunes or meters).

---

## Source Inventory

| # | Title | Author/Compiler | Type | Year | Lines | Priority |
|---|-------|----------------|------|------|-------|----------|
| 1 | The Christian Hymn Book | Alexander Campbell et al. | Hymnal (1,324 hymns) | 1870 | 39,567 | Highest --- provides all hymn texts |
| 2 | The Story of Our Hymns | Ernest Edwin Ryden | History/biography | 1930 | 16,023 | High --- chronological backbone |
| 3 | The Story of the Hymns and Tunes | Theron Brown & Hezekiah Butterworth | History/narrative | 1906 | 18,946 | High --- musical/thematic depth |
| 4 | King James Version of the Bible | N/A | Scripture | 1611 | 99,971 | Reference --- verse integration |

**Campbell** is the structural backbone: 1,324 numbered hymns with meter markings, topic headings, and first-line index. Provides all hymn text (critical for avoiding API content errors).

**Ryden** is the biographical backbone: chronological coverage of 150-200 hymn writers from early Christianity through 1930, organized by national tradition (German, Scandinavian, English, American). Deepest biographical content.

**Butterworth-Brown** supplements with musical history (tune provenance, composition stories) and thematic organization (14 chapters by hymn category). More anecdotal and narrative.

**KJV** provides scripture references quoted inline on hymn pages and in a master scripture index.

---

## Page Types

- [x] **Hymns** (custom type) --- 1,324 pages, one per Campbell hymn number
- [x] **Entities** --- hymn writers, composers, translators, historical figures (~200+)
- [x] **Concepts** --- theological themes, musical forms, historical movements (~50+)
- [x] **Sources** --- 4 source summary pages
- [x] **Synthesis** --- cross-cutting analyses (era overviews, comparisons, thematic surveys)
- [x] **Timelines** --- chronological narratives by era

### Hymn Page Schema

Extends base frontmatter with:

```yaml
extra_fields:
  - name: hymn_number
    type: integer
    applies_to: [hymn]
    description: Campbell numbering (1-1324)
  - name: first_line
    type: string
    applies_to: [hymn]
    description: First line of the hymn text
  - name: meter
    type: string
    applies_to: [hymn]
    description: "Meter marking (L.M., C.M., S.M., C.M.D., P.M., 7s, etc.)"
  - name: topic
    type: string
    applies_to: [hymn]
    description: Campbell's subject heading
  - name: author
    type: string
    applies_to: [hymn]
    description: Hymn writer name
  - name: composer
    type: string
    applies_to: [hymn]
    description: Tune composer (when known)
  - name: tune_name
    type: string
    applies_to: [hymn]
    description: Named tune (when known)
  - name: scripture_refs
    type: list
    applies_to: [hymn]
    description: Bible verse references
  - name: stanza_count
    type: integer
    applies_to: [hymn]
    description: Number of stanzas
  - name: era
    type: string
    values: [early-church, medieval, reformation, post-reformation, 18th-century, 19th-century, 20th-century]
    applies_to: [hymn, entity, concept]
```

---

## Tag Taxonomy Bootstrap

See `wiki/_tag_taxonomy.md` for the full controlled vocabulary. Initial categories:

- **Eras:** `#era-early-church` through `#era-20th-century`
- **Traditions:** `#tradition-lutheran`, `#tradition-methodist`, `#tradition-anglican`, etc.
- **Themes:** `#theme-praise`, `#theme-devotion`, `#theme-trust`, `#theme-suffering`, etc.
- **Musical:** `#meter-common`, `#meter-long`, `#meter-short`, `#meter-peculiar`
- **Geographic:** `#origin-german`, `#origin-english`, `#origin-american`, etc.
- **Meta:** `#needs-review`, `#needs-expansion`, `#contradicted`, `#key-hymn`

---

## Ingest Workflow

### Phase A: Scripted Extraction (no LLM)

1. `parse_campbell.py` extracts all 1,324 hymns into JSON
2. `parse_kjv.py` extracts Bible into verse-level JSON
3. `generate_hymn_pages.py` creates 1,324 hymn stub pages
4. `bible_linker.py` injects scripture references

### Phase B: LLM-Driven Narrative Ingest

**Ingest order:** Ryden (chronological backbone) -> Butterworth-Brown (musical/thematic supplements) -> Campbell source page -> KJV source page.

**Granularity:** Process each Part/Chapter as a unit. Ryden has 5 parts (~40 chapters). Butterworth-Brown has 14 chapters.

**Entity extraction:** Anyone who wrote, composed, translated, or significantly promoted hymns. Also major historical figures who shaped hymnody (monarchs, church leaders, etc.).

**Concept extraction:** Theological themes, musical forms/meters, denominational traditions, historical movements (Reformation, Pietism, Great Awakening, Oxford Movement, etc.).

**Contradiction handling:** When Ryden and Butterworth-Brown disagree on dates, attributions, or facts, note both accounts with source attribution. Tag with `#contradicted`.

**Citation style:** Inline source attribution: "According to Ryden, ..." or "(Butterworth-Brown, Ch. 3)". Wikilink to source page: `[[The_Story_of_Our_Hymns]]`.

---

## Output Formats

- [x] **Marp slide decks** --- "Highlights of Christian Hymnody" overview deck
- [x] **Scripture index** --- `_scripture_index.md` mapping Bible verses to hymns
- [ ] **Charts/figures** --- possible timeline visualization
- [ ] **Reading lists** --- possible curated recommendations

---

## Conventions

- **Hymn page titles:** `Hymn_NNN_First_Line_Words.md` (e.g., `Hymn_001_The_Heavens_Declare_Thy_Glory.md`)
- **Entity names:** Full anglicized names (e.g., "Isaac Watts" not "Dr. Watts")
- **Dates:** CE format (e.g., 1674-1748). No BCE dates expected in this domain.
- **Terminology:** "hymn writer" (not "hymnist" or "hymnodist" unless quoting). "Tune" for melody. "Meter" for rhythmic pattern.
- **Scope boundaries:** Focus on Christian hymns in the Western tradition as covered by the four sources. Contemporary worship music (post-1930) is out of scope. Eastern Orthodox hymnody is lightly covered (Ryden's early chapters only).
- **Tone:** Warm, accessible, modern English. This is a gift, not a dissertation. Write as if explaining to someone who loves these hymns and wants to know their stories.

---

## Self-Improvement Log

### Version 1.0.0 --- Build Complete (2026-04-04)

**Final stats:** 1,530+ pages. 1,324 hymns, 160 entities, 23 concepts, 5 synthesis, 1 timeline, 4 sources, plus navigation and index pages. HTML site generated via Quartz.

**What worked:**
- **Script-first extraction pipeline.** Parsing Campbell and KJV into JSON before generating pages was essential at this scale. The scripts (`parse_campbell.py`, `parse_kjv.py`, `generate_hymn_pages.py`, `bible_linker.py`) handled 1,324 pages in seconds. LLM-driven page generation for 1,324 hymns would have been impossibly slow and error-prone.
- **Parallel sub-agents for narrative ingest.** Processing Ryden's 5 parts and Butterworth-Brown's 14 chapters via parallel Sonnet agents cut ingest time dramatically. Each agent independently read its section and created pages without conflicts.
- **Warm, modern English tone.** The instruction "this is a gift, not a dissertation" produced consistently accessible writing across all agents.
- **Breadcrumb navigation on every page.** The `add_navigation.py` script injected `> [[_overview|Home]] > Section` into all 1,500+ pages in one pass. Essential for non-Obsidian users and for the HTML export.
- **Type-overview pages.** Creating `Hymns_Overview.md`, `People_Overview.md`, `Concepts_Overview.md`, and `Synthesis_Overview.md` as navigation hubs made "Browse by Type" on the home page functional and intuitive.

**What failed and how it was fixed:**
- **Content API blocks hymn lyrics.** Sub-agents attempting to quote hymn stanzas in entity/concept pages hit content filter errors. Fix: explicit instruction "NEVER quote hymn lyrics" in every agent prompt. All hymn text handled exclusively by Python scripts copying from the source file.
- **YAML `#` tags parsed as comments.** Sub-agents wrote tags like `[#era-reformation, #origin-german]` without quotes. YAML interprets `#` as inline comments. Fix: batch script to quote all tag values. Prevention: future agent prompts must specify `tags: ["#tag-name"]` with quotes.
- **Empty root-level files from Obsidian.** When agents created wikilinks to non-existent pages, Obsidian sometimes created empty stub files at the wiki root (e.g., `wiki/Charles Wesley.md`), conflicting with the real `wiki/entities/Charles_Wesley.md`. Fix: delete root stubs. Prevention: always use underscored filenames in wikilinks.
- **Quartz SPA mode incompatible with simple servers.** SPA routing requires server-side fallback. Python's `http.server` returns 404 for extensionless URLs. Fix: disabled SPA mode and wrote a `_serve.py` with clean-URL handling.
- **Campbell parser edge cases.** Hymn 47 had a "PART FIRST" subheading that broke the parser (no text captured). Hymn 203 captured stanza 2 as the first line. Hymn 403 (Amazing Grace) had duplicate stanza numbering from the Gutenberg source. Fix: manual corrections. Prevention: parser validation should check for empty `text` fields and flag them.

**What the next version should address:**
- Enriching the 1,324 hymn stub pages with historical context (most still say "will be enriched during narrative ingest")
- Linking entity pages directly to the hymn pages of hymns they discuss
- Populating the empty `era` and `composer` frontmatter fields on hymn pages
- Adding `related` links to hymn pages (currently empty on all)
- Resolving the ~30 dead author wikilinks on hymn pages (minor figures without entity pages)
