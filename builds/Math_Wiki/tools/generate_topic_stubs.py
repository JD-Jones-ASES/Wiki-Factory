#!/usr/bin/env python3
"""Generate topic stub pages from the consolidated catalog.

Reads ``raw/catalog/topics_{branch}.json`` and emits
``wiki/topics/{branch_dir}/{Slug}.md`` for each topic. Stub pages contain:

- YAML frontmatter (type=topic, branch, tags, status=stub)
- Breadcrumb
- Summary line
- "In the Source Books" section listing every book/chapter/section that
  covers this topic
- Top definitions and properties extracted from the catalog (previews only;
  full body_latex lives in raw/extractions/)
- Widget mount div keyed to the topic slug
- See Also section

Run from ``builds/Math_Wiki/``:

    py -3 tools/generate_topic_stubs.py --all
    py -3 tools/generate_topic_stubs.py --branch algebra-1
    py -3 tools/generate_topic_stubs.py --topic Linear_Equations
    py -3 tools/generate_topic_stubs.py --all --force    # overwrite
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "raw" / "catalog"
TOPICS_DIR = ROOT / "wiki" / "topics"


# Branch → filesystem subfolder under wiki/topics/
BRANCH_DIR = {
    "pre-algebra": "pre_algebra",
    "algebra-1": "algebra",
    "algebra-2": "algebra",
    "pre-calculus": "precalculus",
}

BRANCH_HUB_WIKILINK = {
    "pre-algebra": "[[Algebra_Overview|Algebra]]",  # pre-algebra shares the Algebra hub
    "algebra-1": "[[Algebra_Overview|Algebra]]",
    "algebra-2": "[[Algebra_Overview|Algebra]]",
    "pre-calculus": "[[Precalculus_Overview|Pre-Calculus]]",
}

BRANCH_TAG = {
    "pre-algebra": "#branch-pre-algebra",
    "algebra-1": "#branch-algebra-1",
    "algebra-2": "#branch-algebra-2",
    "pre-calculus": "#branch-pre-calculus",
}


# ---------------------------------------------------------------------------
# YAML-safe string escaping

def yaml_escape(s: str) -> str:
    """Escape a string for use inside YAML double quotes."""
    if s is None:
        return ""
    return s.replace("\\", "\\\\").replace('"', "'").replace("\n", " ").strip()


def clean_preview(preview: str) -> str:
    """Tidy up a preview line for inclusion in markdown bullets."""
    if not preview:
        return ""
    # Strip leading/trailing ellipsis, collapse whitespace
    p = preview.replace("…", "...").strip()
    p = re.sub(r"\s+", " ", p)
    # Truncate very long previews
    if len(p) > 240:
        p = p[:237] + "..."
    return p


# ---------------------------------------------------------------------------
# Stub rendering

def render_stub(topic: dict) -> str:
    slug = topic["slug"]
    title = topic["canonical_title"]
    branch = topic["branch"]
    sources = topic.get("sources", [])
    aliases = topic.get("aliases", [])

    today = date.today().isoformat()
    hub_wikilink = BRANCH_HUB_WIKILINK.get(branch, "[[Topics_Overview|Topics]]")
    branch_tag = BRANCH_TAG.get(branch, f"#branch-{branch}")

    summary = (
        f"{len(sources)} source section(s) across the ingested textbooks."
        f" Auto-generated stub; prose and worked examples come in a future wave."
    )

    lines: list[str] = []

    # --- Frontmatter ---------------------------------------------------------
    lines.append("---")
    lines.append(f'title: "{yaml_escape(title)}"')
    lines.append("type: topic")
    if aliases:
        alias_json = json.dumps([yaml_escape(a) for a in aliases])
        lines.append(f"aliases: {alias_json}")
    else:
        lines.append("aliases: []")
    lines.append(f'tags: ["{branch_tag}", "#topic-auto-generated"]')
    lines.append(f"created: {today}")
    lines.append(f"updated: {today}")
    lines.append("source_refs: []")
    lines.append("related: []")
    lines.append("status: stub")
    lines.append("confidence: medium")
    lines.append(f"branch: {branch}")
    lines.append("prerequisites: []")
    lines.append("problem_type_ids: []")
    lines.append("figures: []")
    lines.append(f'summary: "{yaml_escape(summary)}"')
    lines.append("---")
    lines.append("")

    # --- Breadcrumb ----------------------------------------------------------
    lines.append(f"> [[_overview|Home]] > {hub_wikilink} > {title}")
    lines.append("")

    # --- Heading + summary ---------------------------------------------------
    lines.append(f"# {title}")
    lines.append("")
    lines.append(
        "> _This is an auto-generated stub. Lesson prose, worked examples, and practice problem generators will be added in subsequent waves. The source material below is drawn from the ingested textbook catalog._"
    )
    lines.append("")

    # --- Source references ---------------------------------------------------
    if sources:
        lines.append("## In the Source Books")
        lines.append("")
        seen_sources = set()
        for src in sources:
            key = (src["book_slug"], src["chapter_number"], src["section_number"])
            if key in seen_sources:
                continue
            seen_sources.add(key)
            book_title = src.get("book_title", src["book_slug"])
            ch_num = src["chapter_number"]
            ch_title = src.get("chapter_title", "")
            sec_num = src["section_number"]
            sec_title = src.get("section_title", "")
            lines.append(
                f"- **{book_title}** --- Chapter {ch_num} "
                f"({ch_title}), Section {sec_num}: {sec_title}"
            )
        lines.append("")

    # --- Definitions ---------------------------------------------------------
    definitions = topic.get("definitions", [])
    if definitions:
        lines.append("## Definitions")
        lines.append("")
        for d in definitions[:5]:
            title_text = d.get("title") or "(untitled)"
            preview = clean_preview(d.get("preview", ""))
            if preview:
                lines.append(f"- **{title_text}** --- {preview}")
            else:
                lines.append(f"- **{title_text}**")
        lines.append("")

    # --- Properties and theorems --------------------------------------------
    props_and_thms: list[dict] = list(topic.get("properties", [])) + list(
        topic.get("theorems", [])
    )
    if props_and_thms:
        lines.append("## Key Properties")
        lines.append("")
        for p in props_and_thms[:5]:
            title_text = p.get("title") or "(untitled)"
            preview = clean_preview(p.get("preview", ""))
            if preview:
                lines.append(f"- **{title_text}** --- {preview}")
            else:
                lines.append(f"- **{title_text}**")
        lines.append("")

    # --- Example previews ----------------------------------------------------
    examples = topic.get("examples", [])
    if examples:
        lines.append("## Example Walkthroughs Available")
        lines.append("")
        lines.append(
            f"The source books contain **{len(examples)} worked example(s)** for this topic. "
            "Selected examples will be adapted into this page in a future wave."
        )
        lines.append("")
        for e in examples[:3]:
            title_text = e.get("title") or "(untitled example)"
            book = e.get("book", "")
            lines.append(f"- _{title_text}_ (from {book})")
        if len(examples) > 3:
            lines.append(f"- ... and {len(examples) - 3} more.")
        lines.append("")

    # --- Problems widget mount ----------------------------------------------
    lines.append("## Problems Involving This Topic")
    lines.append("")
    lines.append(
        '<div class="problem-vault-widget" data-topic-slug="'
        + slug.lower()
        + '"></div>'
    )
    lines.append("")

    # --- See Also ------------------------------------------------------------
    lines.append("## See Also")
    lines.append("")
    lines.append(f"- {hub_wikilink}")
    lines.append("- [[Topics_Overview]]")
    lines.append("- [[_overview|Home]]")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File writing with "anywhere in wiki/topics/ exists" check

def existing_slug_paths(topics_root: Path) -> set[str]:
    """Return the set of slugs (stems) that already exist anywhere under wiki/topics/."""
    slugs = set()
    if not topics_root.exists():
        return slugs
    for md in topics_root.rglob("*.md"):
        slugs.add(md.stem)
    return slugs


def write_stub(topic: dict, out_dir: Path, force: bool, already_exist: set[str]) -> str:
    """Write a stub to disk. Returns status string: 'written', 'skipped_exists', 'skipped_elsewhere'."""
    slug = topic["slug"]
    out_file = out_dir / f"{slug}.md"

    if out_file.exists() and not force:
        return "skipped_exists"
    if slug in already_exist and not out_file.exists() and not force:
        # A file with this slug lives somewhere else in wiki/topics/ (e.g., Circles already lives
        # in geometry/). Don't overwrite the existing content.
        return "skipped_elsewhere"

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file.write_text(render_stub(topic), encoding="utf-8")
    return "written"


# ---------------------------------------------------------------------------
# Entry point

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--branch",
        choices=list(BRANCH_DIR.keys()) + ["all"],
        default="all",
        help="restrict to a specific branch",
    )
    parser.add_argument("--topic", help="restrict to a single topic slug")
    parser.add_argument(
        "--force", action="store_true", help="overwrite existing stubs"
    )
    args = parser.parse_args()

    if not CATALOG_DIR.exists():
        print("catalog not found; run consolidate_extractions.py first", file=sys.stderr)
        sys.exit(1)

    already_exist = existing_slug_paths(TOPICS_DIR)

    counts: dict[str, int] = {"written": 0, "skipped_exists": 0, "skipped_elsewhere": 0}
    total_topics_seen = 0

    for branch_slug in BRANCH_DIR.keys():
        if args.branch != "all" and args.branch != branch_slug:
            continue
        cat_file = CATALOG_DIR / f"topics_{branch_slug.replace('-', '_')}.json"
        if not cat_file.exists():
            print(f"  {branch_slug}: no catalog file found, skipping")
            continue
        topics = json.loads(cat_file.read_text(encoding="utf-8"))
        branch_dir = TOPICS_DIR / BRANCH_DIR[branch_slug]

        print(f"  {branch_slug}: processing {len(topics)} topics -> {branch_dir.relative_to(ROOT)}")
        for topic in topics:
            total_topics_seen += 1
            if args.topic and topic["slug"] != args.topic:
                continue
            status = write_stub(topic, branch_dir, args.force, already_exist)
            counts[status] += 1
            if status == "written":
                already_exist.add(topic["slug"])

    print()
    print("=== Summary ===")
    print(f"  topics seen:        {total_topics_seen}")
    print(f"  stubs written:      {counts['written']}")
    print(f"  skipped (exists):   {counts['skipped_exists']}")
    print(f"  skipped (elsewhere):{counts['skipped_elsewhere']}")


if __name__ == "__main__":
    main()
