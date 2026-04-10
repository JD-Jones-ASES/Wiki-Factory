#!/usr/bin/env python3
"""Regenerate branch overview hub pages with topic lists from the catalog.

Overwrites the Start/Explore sections of each *_Overview.md hub page with
an auto-generated topic listing. Manual sections above and below the markers
are preserved.

Markers (HTML comments) delimit the auto-generated block:

    <!-- AUTO:TOPICS:BEGIN -->
    ... auto-generated topic list ...
    <!-- AUTO:TOPICS:END -->

If markers are missing on a page, the block is inserted before the "See Also"
section.

Run from ``builds/Math_Wiki/``:

    py -3 tools/update_branch_hubs.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "raw" / "catalog"
WIKI_DIR = ROOT / "wiki"
PROBLEM_TYPES_INDEX = WIKI_DIR / "_data" / "problem_types_index.json"


# Map branches (as they appear in the catalog) to hub file and grouping title.
BRANCH_TO_HUB: dict[str, dict] = {
    "pre-algebra": {
        "hub_file": "Algebra_Overview.md",      # pre-algebra shares the Algebra hub
        "group_label": "Pre-Algebra topics (middle-school foundations)",
    },
    "algebra-1": {
        "hub_file": "Algebra_Overview.md",
        "group_label": "Algebra 1 topics",
    },
    "algebra-2": {
        "hub_file": "Algebra_Overview.md",
        "group_label": "Algebra 2 topics",
    },
    "pre-calculus": {
        "hub_file": "Precalculus_Overview.md",
        "group_label": "Pre-Calculus topics (Stitz-Zeager AlgTrig)",
    },
}


BEGIN_MARKER = "<!-- AUTO:TOPICS:BEGIN -->"
END_MARKER = "<!-- AUTO:TOPICS:END -->"


def load_catalog() -> dict[str, list]:
    """Return a map of branch -> list of topic dicts."""
    data: dict[str, list] = {}
    for branch_slug in BRANCH_TO_HUB.keys():
        branch_file = CATALOG_DIR / f"topics_{branch_slug.replace('-', '_')}.json"
        if branch_file.exists():
            data[branch_slug] = json.loads(branch_file.read_text(encoding="utf-8"))
        else:
            data[branch_slug] = []
    return data


def load_live_slugs() -> set[str]:
    """Return the set of lowercase topic slugs that have registered generators.

    A "live" topic is one that appears in ``wiki/_data/problem_types_index.json``
    under ``by_topic``. These topics have at least one problem generator and
    therefore show a populated practice widget on their page.
    """
    if not PROBLEM_TYPES_INDEX.exists():
        return set()
    idx = json.loads(PROBLEM_TYPES_INDEX.read_text(encoding="utf-8"))
    return set(idx.get("by_topic", {}).keys())


def render_block_for_hub(hub_file: str, catalog: dict[str, list], live_slugs: set[str]) -> str:
    """Render the auto-generated topic block for a given hub file.

    Emits two subsections per branch group:
      1. "Live topics" --- those with a registered generator (🟢)
      2. "Stub topics" --- everything else (⚪)

    Each line carries a generator-count badge for live topics and a worked-
    example count for stubs so students can see which source material is
    richest.
    """
    lines: list[str] = [BEGIN_MARKER, ""]
    for branch_slug, info in BRANCH_TO_HUB.items():
        if info["hub_file"] != hub_file:
            continue
        topics = sorted(catalog.get(branch_slug, []), key=lambda t: t["canonical_title"])
        if not topics:
            continue

        live = [t for t in topics if t["slug"].lower() in live_slugs]
        stubs = [t for t in topics if t["slug"].lower() not in live_slugs]

        group_label = info["group_label"]
        lines.append(
            f"### {group_label} --- "
            f"{len(live)} live / {len(topics)} total"
        )
        lines.append("")

        if live:
            lines.append(f"**🟢 Live topics with practice widgets ({len(live)})**")
            lines.append("")
            for t in live:
                wikilink = f"[[{t['slug']}|{t['canonical_title']}]]"
                lines.append(f"- 🟢 {wikilink}")
            lines.append("")

        if stubs:
            lines.append(f"<details>")
            lines.append(
                f"<summary>⚪ {len(stubs)} stub topic(s) "
                f"(click to expand)</summary>"
            )
            lines.append("")
            for t in stubs:
                wikilink = f"[[{t['slug']}|{t['canonical_title']}]]"
                source_count = len(t.get("sources", []))
                example_count = len(t.get("examples", []))
                annotation = []
                if source_count > 1:
                    annotation.append(f"covered by {source_count} books")
                if example_count > 0:
                    annotation.append(f"{example_count} worked example(s)")
                suffix = f" --- _{', '.join(annotation)}_" if annotation else ""
                lines.append(f"- ⚪ {wikilink}{suffix}")
            lines.append("")
            lines.append("</details>")
            lines.append("")

    lines.append(END_MARKER)
    return "\n".join(lines)


def inject_block(page_text: str, block: str) -> str:
    """Replace the block between BEGIN_MARKER and END_MARKER, or insert before See Also."""
    if BEGIN_MARKER in page_text and END_MARKER in page_text:
        pattern = re.compile(
            re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER),
            re.DOTALL,
        )
        return pattern.sub(block, page_text)

    # Not present --- insert before the "## See Also" heading if any
    see_also = re.search(r"^## See Also", page_text, re.MULTILINE)
    if see_also:
        insert_at = see_also.start()
        return page_text[:insert_at] + block + "\n\n" + page_text[insert_at:]

    # Otherwise append
    return page_text.rstrip() + "\n\n" + block + "\n"


def main():
    if not CATALOG_DIR.exists():
        print("catalog not found; run consolidate_extractions.py first", file=sys.stderr)
        sys.exit(1)

    catalog = load_catalog()
    live_slugs = load_live_slugs()
    print(f"  {len(live_slugs)} live topic slug(s) from problem_types_index.json")

    # Deduplicate hub files (multiple branches may point at the same hub)
    hub_files = sorted({info["hub_file"] for info in BRANCH_TO_HUB.values()})

    for hub_filename in hub_files:
        hub_path = WIKI_DIR / hub_filename
        if not hub_path.exists():
            print(f"  hub not found: {hub_filename} (skipping)")
            continue

        page_text = hub_path.read_text(encoding="utf-8")
        block = render_block_for_hub(hub_filename, catalog, live_slugs)
        new_text = inject_block(page_text, block)
        if new_text == page_text:
            print(f"  {hub_filename}: unchanged")
            continue
        hub_path.write_text(new_text, encoding="utf-8")
        topic_count = sum(
            len(catalog.get(branch_slug, []))
            for branch_slug, info in BRANCH_TO_HUB.items()
            if info["hub_file"] == hub_filename
        )
        print(f"  {hub_filename}: updated ({topic_count} topics listed)")


if __name__ == "__main__":
    main()
