#!/usr/bin/env python3
"""
clean_placeholders.py
Replaces misleading enrichment placeholder text in hymn pages.

The placeholder "This section will be enriched during narrative ingest from
[[The_Story_of_Our_Hymns]] and [[The_Story_of_the_Hymns_and_Tunes]]."
is replaced with a clean note that no individual historical commentary
was found in available sources.
"""

import os
import glob
import sys

HYMNS_DIR = os.path.join("builds", "Hymn_Wiki", "wiki", "hymns")

OLD_PLACEHOLDER = "*This section will be enriched during narrative ingest from [[The_Story_of_Our_Hymns]] and [[The_Story_of_the_Hymns_and_Tunes]].*"

NEW_TEXT = "*No individual historical commentary found in available sources. See author and concept pages for broader context.*"


def main():
    dry_run = "--dry-run" in sys.argv

    hymn_files = glob.glob(os.path.join(HYMNS_DIR, "Hymn_*.md"))
    updated = 0

    for filepath in sorted(hymn_files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if OLD_PLACEHOLDER in content:
            if dry_run:
                updated += 1
                continue

            new_content = content.replace(OLD_PLACEHOLDER, NEW_TEXT)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated += 1

    action = "Would update" if dry_run else "Updated"
    print(f"{action} {updated} hymn files (replaced placeholder text)")


if __name__ == "__main__":
    main()
