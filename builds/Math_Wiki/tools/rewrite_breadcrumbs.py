#!/usr/bin/env python3
"""Rewrite breadcrumbs and See Also wikilinks from old branch hubs to new course hubs.

Walks ``wiki/topics/**/*.md``. For each topic file:

  * Reads the ``branch:`` field from YAML frontmatter.
  * Maps the branch to its new course hub file.
  * Rewrites the breadcrumb line ``> [[_overview|Home]] > [[OldHub|Label]] > Title``
    to point at the new course hub.
  * Rewrites any See Also wikilinks like ``[[Algebra_Overview|Algebra]]`` to the
    matching course hub.

The mapping mirrors ``tools/update_course_hubs.py``:

    pre-algebra   -> Middle_School_Math   (label "Middle School Math")
    algebra-1     -> Algebra_1            (label "Algebra 1")
    algebra-2     -> Algebra_2            (label "Algebra 2")
    pre-calculus  -> Precalculus          (label "Pre-Calculus & Trig")
    geometry      -> Geometry             (label "Geometry")

Run from ``builds/Math_Wiki/``:

    py -3 tools/rewrite_breadcrumbs.py --dry-run   # preview
    py -3 tools/rewrite_breadcrumbs.py             # write
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"


# Branch (YAML value) -> (course hub file stem, display label for breadcrumbs).
BRANCH_TO_COURSE: dict[str, tuple[str, str]] = {
    "pre-algebra":  ("Middle_School_Math", "Middle School Math"),
    "algebra-1":    ("Algebra_1",          "Algebra 1"),
    "algebra-2":    ("Algebra_2",          "Algebra 2"),
    "pre-calculus": ("Precalculus",        "Pre-Calculus & Trig"),
    "geometry":     ("Geometry",           "Geometry"),
}

# Old hub names that may appear in breadcrumb or See Also wikilinks.
OLD_HUB_ALIASES = {
    "Algebra_Overview",
    "Precalculus_Overview",
    "Geometry_Overview",
    "Trigonometry_Overview",
}


FRONTMATTER_BRANCH = re.compile(r"^branch:\s*(\S+)", re.MULTILINE)
# Breadcrumb pattern: `> [[_overview|Home]] > [[<oldhub>|<label>]] > <rest>`
BREADCRUMB = re.compile(
    r"^(>\s*\[\[_overview\|Home\]\]\s*>\s*)\[\[(?P<oldhub>\w+_Overview)\|[^\]]+\]\](\s*>\s*.*)$",
    re.MULTILINE,
)


def resolve_branch_from_path(path: Path) -> str | None:
    """Infer branch from the topic file's parent directory name."""
    parent = path.parent.name
    return {
        "pre_algebra": "pre-algebra",
        "algebra":     None,  # ambiguous: could be algebra-1 or algebra-2
        "precalculus": "pre-calculus",
        "geometry":    "geometry",
        "trigonometry": "pre-calculus",
    }.get(parent)


def extract_branch(text: str, path: Path) -> str | None:
    """Read ``branch:`` from frontmatter, falling back to parent directory."""
    m = FRONTMATTER_BRANCH.search(text)
    if m:
        return m.group(1).strip('"').strip("'")
    return resolve_branch_from_path(path)


def rewrite_text(text: str, course_stem: str, course_label: str) -> str:
    """Rewrite breadcrumb and See Also wikilinks in a single topic page."""
    # 1. Breadcrumb line rewrite.
    def _fix_crumb(m: re.Match) -> str:
        head = m.group(1)
        tail = m.group(3)
        return f"{head}[[{course_stem}|{course_label}]]{tail}"

    text = BREADCRUMB.sub(_fix_crumb, text)

    # 2. Generic wikilink rewrite for See Also + inline refs to old hubs.
    #    Replace every [[OldHub|label]] and [[OldHub]] with the course hub link.
    for old in OLD_HUB_ALIASES:
        # labeled form: [[OldHub|Anything]]
        text = re.sub(
            r"\[\[" + re.escape(old) + r"\|[^\]]*\]\]",
            f"[[{course_stem}|{course_label}]]",
            text,
        )
        # bare form: [[OldHub]]
        text = re.sub(
            r"\[\[" + re.escape(old) + r"\]\]",
            f"[[{course_stem}|{course_label}]]",
            text,
        )

    return text


def process_file(path: Path, dry_run: bool) -> bool:
    """Rewrite one topic file. Return True if changes would be made."""
    original = path.read_text(encoding="utf-8")
    branch = extract_branch(original, path)
    if branch is None:
        return False

    course = BRANCH_TO_COURSE.get(branch)
    if course is None:
        return False

    course_stem, course_label = course
    new_text = rewrite_text(original, course_stem, course_label)
    if new_text == original:
        return False

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="preview only")
    args = parser.parse_args()

    if not TOPICS_DIR.exists():
        print(f"topics directory not found: {TOPICS_DIR}", file=sys.stderr)
        sys.exit(1)

    files = sorted(TOPICS_DIR.rglob("*.md"))
    changed = 0
    for path in files:
        if process_file(path, args.dry_run):
            rel = path.relative_to(ROOT)
            verb = "would edit" if args.dry_run else "edited"
            print(f"{verb} {rel}")
            changed += 1

    suffix = " (dry run)" if args.dry_run else ""
    print(f"\n{changed} file(s){' would be' if args.dry_run else ''} modified{suffix}")


if __name__ == "__main__":
    main()
