#!/usr/bin/env python3
"""Strip source-book references from topic stub pages.

The wiki presents itself as a standalone resource. Auto-generated stub topic
pages still contain leftover boilerplate from the ingestion pipeline:

    * a "> _This is an auto-generated stub..." blockquote callout,
    * a ``## In the Source Books`` section listing book/chapter references,
    * a ``## Example Walkthroughs Available`` section whose bullets carry
      ``(from algebra_1)`` attributions,
    * a frontmatter ``summary:`` line that mentions "source section(s) across
      the ingested textbooks".

This tool walks ``wiki/topics/**/*.md``, removes all four, and leaves any
useful content (Definitions, Key Properties, the widget mount, See Also)
intact. Live enriched topic pages are untouched unless they happen to
contain the exact stub patterns.

YAML frontmatter ``source_refs:`` remains in place as internal metadata --
the rendered page never displays it, and downstream tooling still reads it.

Usage:
    py -3 tools/purge_source_mentions.py --dry-run   # preview diffs
    py -3 tools/purge_source_mentions.py             # write changes
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOPICS_DIR = ROOT / "wiki" / "topics"


# The one-line blockquote callout on every auto-stub.
AUTO_STUB_BLOCKQUOTE = re.compile(
    r"^> _This is an auto-generated stub\..*?$\n?",
    re.MULTILINE,
)

# "## In the Source Books" up to the next top-level section or horizontal rule.
IN_SOURCE_BOOKS_SECTION = re.compile(
    r"^## In the Source Books[^\n]*\n.*?(?=^## |^---\n|\Z)",
    re.MULTILINE | re.DOTALL,
)

# "## Example Walkthroughs Available" up to the next top-level section.
EXAMPLES_AVAILABLE_SECTION = re.compile(
    r"^## Example Walkthroughs Available[^\n]*\n.*?(?=^## |^---\n|\Z)",
    re.MULTILINE | re.DOTALL,
)

# Frontmatter summary replacement.
SUMMARY_WITH_SOURCE_LANG = re.compile(
    r'^summary:\s*"(?:\d+\s*source section\(s\)[^"]*|\d+\s*source[^"]*ingested[^"]*)"',
    re.MULTILINE,
)

# A catch-all pattern for any remaining "ingested textbook" phrase in body text.
INGESTED_TEXTBOOK = re.compile(r"ingested textbook[^\n.]*\.?", re.IGNORECASE)

# Collapse runs of 3+ blank lines down to 2.
EXCESS_BLANK_LINES = re.compile(r"\n{3,}")


def purge_file(path: Path) -> tuple[str, str] | None:
    """Return (original, purged) if changes were made, else None."""
    original = path.read_text(encoding="utf-8")
    text = original

    # 1. Frontmatter summary rewrite (only if the old one mentions sources).
    text = SUMMARY_WITH_SOURCE_LANG.sub(
        'summary: "Topic scaffolding. Lesson content coming in a future update."',
        text,
    )

    # 2. Auto-stub blockquote callout.
    text = AUTO_STUB_BLOCKQUOTE.sub("", text)

    # 3. "## In the Source Books" section.
    text = IN_SOURCE_BOOKS_SECTION.sub("", text)

    # 4. "## Example Walkthroughs Available" section.
    text = EXAMPLES_AVAILABLE_SECTION.sub("", text)

    # 5. Any leftover "ingested textbook..." phrases in prose.
    text = INGESTED_TEXTBOOK.sub("", text)

    # 6. Normalize blank-line runs.
    text = EXCESS_BLANK_LINES.sub("\n\n", text)

    if text == original:
        return None
    return original, text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="preview only")
    parser.add_argument("--verbose", action="store_true", help="list every file")
    args = parser.parse_args()

    if not TOPICS_DIR.exists():
        print(f"topics directory not found: {TOPICS_DIR}", file=sys.stderr)
        sys.exit(1)

    files = sorted(TOPICS_DIR.rglob("*.md"))
    changed = 0
    for path in files:
        result = purge_file(path)
        if result is None:
            continue
        original, new = result
        rel = path.relative_to(ROOT)
        if args.dry_run:
            print(f"would edit {rel}")
            if args.verbose:
                _print_diff_preview(original, new)
        else:
            path.write_text(new, encoding="utf-8")
            print(f"edited {rel}")
        changed += 1

    if args.dry_run:
        print(f"\n{changed} file(s) would be modified (dry run)")
    else:
        print(f"\n{changed} file(s) modified")


def _print_diff_preview(original: str, new: str) -> None:
    """Print a tiny diff preview (first 6 removed/changed lines)."""
    original_lines = original.splitlines()
    new_set = set(new.splitlines())
    removed = [line for line in original_lines if line not in new_set][:6]
    for line in removed:
        print(f"    -{line[:100]}")


if __name__ == "__main__":
    main()
