# Wiki Factory

A system that transforms raw sources (books, articles, documents) into structured, interlinked Markdown wikis. Each build is a self-contained Obsidian vault, deployable as a static HTML site via Quartz and GitHub Pages.

Part of the **Curricula By Design** AI-assisted Educational Publishing system.

## What It Does

Given a collection of source documents, the factory produces a complete interlinked wiki containing:

- **Source summaries** --- structured analysis of each input document
- **Entity pages** --- people, places, organizations, works, with cross-source synthesis
- **Concept pages** --- ideas, themes, theories, movements, with historical development
- **Synthesis pages** --- cross-cutting analyses connecting entities, concepts, and sources
- **Timelines** --- chronological narratives across the domain
- **Custom page types** --- domain-specific structures (e.g., hymn pages with meter, scripture refs)
- **Navigation hubs** --- overview pages, indexes, tag taxonomy, scripture index
- **Static HTML site** --- deployed via Quartz v4 on GitHub Pages

## Design Philosophy

- **Three-layer architecture** --- immutable raw sources, LLM-owned wiki layer, derived outputs
- **Layered inheritance** --- CLAUDE.md (factory) > Template.md (meta-instructions) > [Wiki_Name].md (project spec) > wiki pages
- **Self-improving specs** --- project specs evolve during the build; generalizable lessons flow back to Template.md
- **Script-first at scale** --- structured data is parsed by Python scripts, not LLM; LLM effort reserved for narrative content
- **Wave-based parallel ingest** --- multiple sources processed concurrently with JSON intermediary files for cross-source enrichment

## Project Structure

```
Wiki_Factory/
  CLAUDE.md            # Factory operating instructions (read every session)
  Template.md          # Meta-instructions for generating project specs
  factory/
    scripts/           # Python tooling (parsers, enrichment, linting, indexing)
    schemas/           # YAML page type schemas
    templates/         # Obsidian vault config templates
  builds/
    [Wiki_Name]/
      [Wiki_Name].md   # Project spec (self-improving)
      quartz.config.ts # Quartz site config (overlaid during CI)
      quartz.layout.ts # Quartz layout config
      raw/             # Immutable source documents (gitignored)
      wiki/            # LLM-generated Markdown (the wiki itself)
      outputs/         # Derived artifacts (gitignored)
  .github/
    workflows/         # CI/CD for GitHub Pages deployment
```

## Current Builds

### Hymn Wiki

A comprehensive guide to Christian hymns --- their stories, their writers, and the Scripture that inspired them.

- **1,740 hymns** from two historic hymnals (Campbell 1870, Longfellow-Johnson 1848)
- **284 hymn writers**, composers, and translators
- **45+ concept pages** on theological themes, musical traditions, and historical movements
- **11 primary sources** spanning three centuries of hymnological scholarship
- **Live site:** [jd-jones-ases.github.io/Wiki-Factory/Hymn_Wiki](https://jd-jones-ases.github.io/Wiki-Factory/Hymn_Wiki/)

## Usage

1. Place source documents in `builds/[Wiki_Name]/raw/`
2. Generate a project spec: read Template.md, analyze sources, write `[Wiki_Name].md`
3. Scaffold the wiki structure (see CLAUDE.md scaffolding checklist)
4. Run the factory pipeline: INGEST > COMPILE > LINT > OUTPUT
5. Deploy via `git push` (GitHub Actions builds and deploys automatically)

## Designers

- **JD Jones** --- [Curricula By Design](https://www.curriculabydesign.com/)
- **Claude Code** by Anthropic

## License

- **Wiki content** (everything in `builds/*/wiki/`): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Tooling** (scripts, schemas, templates, CI workflows): [MIT License](https://opensource.org/licenses/MIT)

Copyright 2026 JD Jones, Curricula By Design
