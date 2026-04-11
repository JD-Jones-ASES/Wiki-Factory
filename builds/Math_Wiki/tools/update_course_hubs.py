#!/usr/bin/env python3
"""Regenerate course-level hub pages with topic lists grouped by course.

Walks ``wiki/topics/**/*.md``, reads each topic's YAML frontmatter, groups
topics by their ``branch:`` field (and optional ``courses:`` list), then
rewrites the ``<!-- AUTO:TOPICS:BEGIN -->`` / ``<!-- AUTO:TOPICS:END -->``
block of each course hub page.

The five course hubs (replacing the legacy four branch hubs):

    pre-algebra   -> Middle_School_Math.md
    algebra-1     -> Algebra_1.md
    algebra-2     -> Algebra_2.md
    pre-calculus  -> Precalculus.md
    geometry      -> Geometry.md  (plus a curated allowlist of geometry-
                                   adjacent pre-algebra topics)

A topic is "live" if its lowercase slug appears in
``wiki/_data/problem_types_index.json`` under ``by_topic``. Live topics get
a 🟢 marker; stubs get a ⚪ marker and are collapsed inside a ``<details>``
block.

Run from ``builds/Math_Wiki/``:

    py -3 tools/update_course_hubs.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
PROBLEM_TYPES_INDEX = WIKI_DIR / "_data" / "problem_types_index.json"


# Course hub mapping: branch value in frontmatter -> (hub filename, display label)
BRANCH_TO_HUB: dict[str, tuple[str, str]] = {
    "pre-algebra":  ("Middle_School_Math.md", "Middle School Math topics"),
    "algebra-1":    ("Algebra_1.md",          "Algebra 1 topics"),
    "algebra-2":    ("Algebra_2.md",          "Algebra 2 topics"),
    "pre-calculus": ("Precalculus.md",        "Pre-Calculus & Trigonometry topics"),
    "geometry":     ("Geometry.md",           "Core Geometry topics"),
}


# Pre-algebra topics that belong in the Geometry course hub as well.
# These are geometry-adjacent slugs that a HS Geometry student expects to find.
# Each entry is the bare filename stem (no .md).
GEOMETRY_ADJACENT_ALLOWLIST: list[str] = [
    "Applications_Of_The_Pythagorean_Theorem",
    "Circumference_And_Area_Of_Circles",
    "Classifying_Triangles_And_Quadrilaterals",
    "Composite_Figures",
    "Perimeter_And_Area_Of_Polygons",
    "Plotting_Points_And_The_Coordinate_Plane",
    "Points_Lines_Angles_And_Angle_Relationships",
    "Proportions_In_Similar_Figures",
    "Review_Of_Perimeter_And_Area",
    "Scale_Drawings_And_Maps",
    "Similar_Triangles",
    "Surface_Area_And_Volume_Of_Spheres",
    "Surface_Area_Of_Prisms_And_Cylinders",
    "The_Distance_Formula",
    "The_Midpoint_Formula",
    "The_Pythagorean_Theorem",
    "Triangle_Angle_Sum_And_Exterior_Angles",
    "Volume_Of_Prisms_And_Cylinders",
    "Volume_Of_Pyramids_And_Cones",
]


BEGIN_MARKER = "<!-- AUTO:TOPICS:BEGIN -->"
END_MARKER = "<!-- AUTO:TOPICS:END -->"


def parse_frontmatter(text: str) -> dict:
    """Return a minimal dict from YAML frontmatter. Only extracts fields we need.

    This is intentionally lightweight (no pyyaml dependency) because we only
    read a handful of scalar fields and one optional list.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    body = text[3:end]
    result: dict = {}
    current_key = None
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        # List continuation under the last key
        if line.startswith(" ") or line.startswith("\t"):
            if current_key and stripped.startswith("- "):
                result.setdefault(current_key, []).append(stripped[2:].strip(' "\''))
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", stripped)
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        current_key = key
        if value == "" or value.startswith("#"):
            continue
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if inner:
                items = [p.strip().strip('"').strip("'") for p in inner.split(",")]
                result[key] = [i for i in items if i]
            else:
                result[key] = []
        else:
            result[key] = value.strip('"').strip("'")
    return result


def load_topics() -> list[dict]:
    """Walk wiki/topics/ and return a list of topic metadata dicts."""
    topics: list[dict] = []
    for md_file in sorted(TOPICS_DIR.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        slug = md_file.stem
        topics.append({
            "slug": slug,
            "title": fm.get("title", slug.replace("_", " ")),
            "branch": fm.get("branch", ""),
            "courses": fm.get("courses", []) if isinstance(fm.get("courses"), list) else [],
            "path": md_file,
        })
    return topics


def load_live_slugs() -> set[str]:
    """Return the set of lowercase topic slugs that have registered generators."""
    if not PROBLEM_TYPES_INDEX.exists():
        return set()
    idx = json.loads(PROBLEM_TYPES_INDEX.read_text(encoding="utf-8"))
    return set(idx.get("by_topic", {}).keys())


def topics_for_hub(hub_branch: str, all_topics: list[dict]) -> list[dict]:
    """Return the topic list that should appear under a given course hub."""
    matched = []
    seen_slugs: set[str] = set()

    for t in all_topics:
        if t["slug"] in seen_slugs:
            continue
        primary = t["branch"] == hub_branch
        multi = hub_branch in t["courses"]
        if primary or multi:
            matched.append(t)
            seen_slugs.add(t["slug"])

    # Second pass: the Geometry hub also picks up allowlisted pre-algebra topics.
    if hub_branch == "geometry":
        for t in all_topics:
            if t["slug"] in seen_slugs:
                continue
            if t["slug"] in GEOMETRY_ADJACENT_ALLOWLIST:
                matched.append(t)
                seen_slugs.add(t["slug"])

    matched.sort(key=lambda t: t["title"])
    return matched


def render_block(hub_branch: str, topics: list[dict], live_slugs: set[str], label: str) -> str:
    """Build the auto-generated markdown block for a course hub."""
    lines = [BEGIN_MARKER, ""]
    live = [t for t in topics if t["slug"].lower() in live_slugs]
    stubs = [t for t in topics if t["slug"].lower() not in live_slugs]

    lines.append(f"### {label} --- {len(live)} live / {len(topics)} total")
    lines.append("")

    if live:
        lines.append(f"**🟢 Live topics with practice widgets ({len(live)})**")
        lines.append("")
        for t in live:
            lines.append(f"- 🟢 [[{t['slug']}|{t['title']}]]")
        lines.append("")
    else:
        lines.append("_No live topics yet. All entries below are scaffolded stubs._")
        lines.append("")

    if stubs:
        lines.append("<details>")
        lines.append(f"<summary>⚪ {len(stubs)} stub topic(s) (click to expand)</summary>")
        lines.append("")
        for t in stubs:
            lines.append(f"- ⚪ [[{t['slug']}|{t['title']}]]")
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
        return pattern.sub(lambda _m: block, page_text)

    see_also = re.search(r"^## See Also", page_text, re.MULTILINE)
    if see_also:
        insert_at = see_also.start()
        return page_text[:insert_at] + block + "\n\n" + page_text[insert_at:]

    return page_text.rstrip() + "\n\n" + block + "\n"


def main() -> None:
    if not TOPICS_DIR.exists():
        print(f"topics directory not found: {TOPICS_DIR}", file=sys.stderr)
        sys.exit(1)

    all_topics = load_topics()
    live_slugs = load_live_slugs()
    print(f"  {len(all_topics)} topic files scanned, {len(live_slugs)} live slug(s)")

    for branch_slug, (hub_file, label) in BRANCH_TO_HUB.items():
        hub_path = WIKI_DIR / hub_file
        if not hub_path.exists():
            print(f"  {hub_file}: missing (create the hub page first, skipping)")
            continue

        topics = topics_for_hub(branch_slug, all_topics)
        block = render_block(branch_slug, topics, live_slugs, label)

        page_text = hub_path.read_text(encoding="utf-8")
        new_text = inject_block(page_text, block)
        if new_text == page_text:
            print(f"  {hub_file}: unchanged ({len(topics)} topics)")
            continue
        hub_path.write_text(new_text, encoding="utf-8")
        live_count = sum(1 for t in topics if t["slug"].lower() in live_slugs)
        print(f"  {hub_file}: updated ({live_count} live / {len(topics)} total)")


if __name__ == "__main__":
    main()
