"""Tag Report - Analyze tag usage across wiki pages."""

import sys
import re
import yaml
from pathlib import Path
from collections import Counter

SYSTEM_FILES = {"_index.md", "_log.md", "_overview.md", "_tag_taxonomy.md"}


def tag_report(wiki_dir):
    """Generate a tag frequency and taxonomy compliance report."""
    wiki_path = Path(wiki_dir)
    if not wiki_path.exists():
        print(f"ERROR: Wiki directory not found: {wiki_dir}")
        return 1

    # Load taxonomy
    taxonomy_tags = set()
    taxonomy_file = wiki_path / "_tag_taxonomy.md"
    if taxonomy_file.exists():
        tax_text = taxonomy_file.read_text(encoding="utf-8")
        taxonomy_tags = set(re.findall(r"#([\w-]+)", tax_text))

    # Count tags across all pages
    tag_counts = Counter()
    pages_without_tags = []

    for md_file in wiki_path.rglob("*.md"):
        if md_file.name in SYSTEM_FILES:
            continue

        text = md_file.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            continue

        try:
            fm = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            continue

        tags = fm.get("tags", [])
        if not tags:
            pages_without_tags.append(str(md_file.relative_to(wiki_path)))
        elif isinstance(tags, list):
            for tag in tags:
                tag_counts[tag] += 1

    # Report
    print(f"\nTag Report: {wiki_dir}")
    print(f"{'='*50}")
    print(f"Unique tags: {len(tag_counts)}")
    print(f"Taxonomy tags: {len(taxonomy_tags)}")
    print()

    if tag_counts:
        print("Tag frequency (descending):")
        for tag, count in tag_counts.most_common():
            in_taxonomy = " " if (not taxonomy_tags or tag in taxonomy_tags) else " [NOT IN TAXONOMY]"
            print(f"  #{tag}: {count}{in_taxonomy}")

    if taxonomy_tags:
        unused = taxonomy_tags - set(tag_counts.keys())
        if unused:
            print(f"\nUnused taxonomy tags ({len(unused)}):")
            for tag in sorted(unused):
                print(f"  #{tag}")

    rogue = set(tag_counts.keys()) - taxonomy_tags if taxonomy_tags else set()
    if rogue:
        print(f"\nTags not in taxonomy ({len(rogue)}):")
        for tag in sorted(rogue):
            print(f"  #{tag} (used {tag_counts[tag]}x)")

    if pages_without_tags:
        print(f"\nPages without tags ({len(pages_without_tags)}):")
        for p in pages_without_tags:
            print(f"  - {p}")

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py -3 tag_report.py <wiki_directory>")
        sys.exit(1)
    tag_report(sys.argv[1])
