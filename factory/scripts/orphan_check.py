"""Orphan Check - Find wiki pages with no inbound wikilinks."""

import sys
import re
from pathlib import Path

SYSTEM_FILES = {"_index.md", "_log.md", "_overview.md", "_tag_taxonomy.md"}


def find_orphans(wiki_dir):
    """Find pages with no inbound wikilinks from other pages."""
    wiki_path = Path(wiki_dir)
    if not wiki_path.exists():
        print(f"ERROR: Wiki directory not found: {wiki_dir}")
        return 1

    # Collect all page stems
    all_pages = {}
    for md_file in wiki_path.rglob("*.md"):
        if md_file.name not in SYSTEM_FILES:
            all_pages[md_file.stem] = md_file.relative_to(wiki_path)

    # Collect all wikilink targets (from ALL files including system files)
    linked_targets = set()
    for md_file in wiki_path.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)
        for link in links:
            linked_targets.add(link)
            linked_targets.add(link.replace(" ", "_"))
            linked_targets.add(link.replace("_", " "))

    # Find orphans
    orphans = []
    for stem, rel_path in sorted(all_pages.items()):
        if stem not in linked_targets and stem.replace("_", " ") not in linked_targets:
            orphans.append((stem, str(rel_path)))

    print(f"\nOrphan Check: {wiki_dir}")
    print(f"Total pages: {len(all_pages)}")
    print(f"Orphan pages: {len(orphans)}")

    if orphans:
        print()
        for stem, path in orphans:
            print(f"  - {path}")

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py -3 orphan_check.py <wiki_directory>")
        sys.exit(1)
    find_orphans(sys.argv[1])
