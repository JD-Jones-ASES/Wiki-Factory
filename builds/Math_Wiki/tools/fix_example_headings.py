#!/usr/bin/env python3
"""One-shot migration: rewrite **Example N.** bold-inline example markers
to ### Example N H3 headings so topic_status.py's EXAMPLE_HEADING_RE regex
picks them up.

Context:
  37 live topics scored 75 on the dashboard because they used the pattern

      ## Worked examples

      **Example 1.** <body paragraph>

      **Example 2.** <body paragraph>

  while topic_status.py only counts headings that match
  ``^##+\s+(?:worked\s+)?example(?:\s+\d+|\s*:|\s*$)``. The **Example 1.**
  bold markers are not headings, so the scorer reports zero examples on
  files that actually have three.

  The fix: rewrite each ``**Example N[.][ (descriptor)].**`` line to an
  ``### Example N`` (or ``### Example N: descriptor``) H3 sub-heading
  followed by a blank line and the original body text. H3 keeps the
  example inside the parent ``## Worked examples`` section (does not
  promote it to a top-level page section) and matches the scorer regex
  (``##+`` means 2+ hashes, so ### qualifies).

  Run once; then this script can be deleted or kept as a reference.

Usage:
    py -3 tools/fix_example_headings.py --dry-run   # report, no writes
    py -3 tools/fix_example_headings.py             # apply in place
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATUS_FILE = ROOT / "wiki" / "_data" / "topic_status.json"

# Three observed variants across the sub-75 corpus:
#   **Example 1.**                         -> num=1, no descriptor
#   **Example 2 (linear).**                -> num=2, paren descriptor="linear"
#   **Example 3. Restaurant bill.**        -> num=3, dot descriptor="Restaurant bill"
#
# Alternation order matters: paren and dot-descriptor variants must be tried
# BEFORE the bare ".**" variant or the bare form greedy-matches everything.
EXAMPLE_LINE_RE = re.compile(
    r"^\*\*Example\s+(\d+)"
    r"(?:"
    r"\s*\(([^)]*)\)\s*\.\*\*"  # variant 2: (descriptor).**
    r"|"
    r"\.\s+([^*]+?)\.\*\*"  # variant 3: . Descriptor.**
    r"|"
    r"\s*\.\*\*"  # variant 1: .**
    r")"
    r"\s*(.*)$",
    re.MULTILINE,
)


def rewrite(text: str) -> tuple[str, int]:
    """Return (new_text, count_of_rewrites) for one file body."""

    def _replacer(m: re.Match) -> str:
        num = m.group(1)
        # Variant 2 -> group(2); variant 3 -> group(3); variant 1 -> neither
        descriptor = (m.group(2) or m.group(3) or "").strip()
        body = m.group(4)
        heading = f"### Example {num}" + (f": {descriptor}" if descriptor else "")
        return f"{heading}\n\n{body}"

    new_text, count = EXAMPLE_LINE_RE.subn(_replacer, text)
    return new_text, count


def main(dry_run: bool) -> int:
    data = json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    targets = [
        t
        for t in data["topics"]
        if t["status"] != "stub" and t["score"] == 75
    ]
    print(f"Targeting {len(targets)} live topic files with score == 75")
    print()

    changed = 0
    zero_match = []
    for t in targets:
        path = ROOT / t["relpath"]
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"  MISSING: {t['relpath']}")
            continue

        new_text, count = rewrite(text)
        if count == 0:
            zero_match.append(t["slug"])
            print(f"  no matches: {t['slug']}")
            continue

        print(f"  {t['slug']}: {count} example(s) rewritten")
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        changed += 1

    print()
    print(f"Rewrote {changed}/{len(targets)} files")
    if zero_match:
        print(f"Needs manual review ({len(zero_match)}):")
        for s in zero_match:
            print(f"  {s}")

    if dry_run:
        print()
        print("DRY RUN - no files were modified. Re-run without --dry-run to apply.")
    return 0 if not zero_match else 1


if __name__ == "__main__":
    sys.exit(main(dry_run="--dry-run" in sys.argv))
