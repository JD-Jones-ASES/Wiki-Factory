"""Wiki Linter - Health check a wiki directory for common issues."""

import sys
import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

REQUIRED_FIELDS = ["title", "type", "tags", "created", "updated", "status"]
VALID_TYPES = {"entity", "concept", "source", "synthesis", "timeline", "overview", "hymn"}
VALID_STATUSES = {"stub", "draft", "complete"}
VALID_CONFIDENCES = {"high", "medium", "low"}
SYSTEM_FILES = {"_index.md", "_log.md", "_overview.md", "_tag_taxonomy.md"}


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, text
    try:
        fm = yaml.safe_load(match.group(1))
        return fm, text
    except yaml.YAMLError:
        return None, text


def extract_wikilinks(text):
    """Extract all [[wikilinks]] from text."""
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)


def lint_wiki(wiki_dir):
    """Run all lint checks on a wiki directory."""
    wiki_path = Path(wiki_dir)
    if not wiki_path.exists():
        print(f"ERROR: Wiki directory not found: {wiki_dir}")
        return 1

    issues = []
    pages = {}  # filename_stem -> frontmatter
    all_wikilinks = defaultdict(list)  # target -> [source pages]
    all_tags = set()
    tag_taxonomy = set()

    # Load tag taxonomy if it exists
    taxonomy_file = wiki_path / "_tag_taxonomy.md"
    if taxonomy_file.exists():
        tax_text = taxonomy_file.read_text(encoding="utf-8")
        tag_taxonomy = set(re.findall(r"#([\w-]+)", tax_text))

    # Scan all markdown files
    md_files = list(wiki_path.rglob("*.md"))
    for md_file in md_files:
        rel_path = md_file.relative_to(wiki_path)
        name = md_file.name

        # Skip system files for frontmatter checks
        if name in SYSTEM_FILES:
            continue

        fm, text = extract_frontmatter(md_file)

        # Check frontmatter exists
        if fm is None:
            issues.append(("ERROR", str(rel_path), "Missing or invalid YAML frontmatter"))
            continue

        pages[md_file.stem] = fm

        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in fm:
                issues.append(("WARN", str(rel_path), f"Missing required field: {field}"))

        # Validate type
        if "type" in fm and fm["type"] not in VALID_TYPES:
            issues.append(("ERROR", str(rel_path), f"Invalid type: {fm['type']}"))

        # Validate status
        if "status" in fm and fm["status"] not in VALID_STATUSES:
            issues.append(("WARN", str(rel_path), f"Invalid status: {fm['status']}"))

        # Validate confidence
        if "confidence" in fm and fm["confidence"] not in VALID_CONFIDENCES:
            issues.append(("WARN", str(rel_path), f"Invalid confidence: {fm['confidence']}"))

        # Collect tags
        if "tags" in fm and isinstance(fm["tags"], list):
            for tag in fm["tags"]:
                all_tags.add(tag)
                # Normalize: strip leading # for comparison
                tag_bare = tag.lstrip("#") if isinstance(tag, str) else str(tag)
                if tag_taxonomy and tag_bare not in tag_taxonomy:
                    issues.append(("WARN", str(rel_path), f"Tag not in taxonomy: {tag}"))

        # Collect wikilinks
        links = extract_wikilinks(text)
        for link in links:
            all_wikilinks[link].append(str(rel_path))

    # Build resolvable names lookup: maps any resolvable name → page stem
    resolvable = {}  # normalized name → stem
    for stem, fm in pages.items():
        resolvable[stem.lower()] = stem
        resolvable[stem.replace("_", " ").lower()] = stem
        if "title" in fm and fm["title"]:
            resolvable[fm["title"].lower()] = stem
        if "aliases" in fm and isinstance(fm["aliases"], list):
            for alias in fm["aliases"]:
                resolvable[alias.lower()] = stem

    # Check for orphan pages (no inbound wikilinks)
    all_page_stems = {p.stem for p in md_files if p.name not in SYSTEM_FILES}
    linked_stems = set()
    for target in all_wikilinks:
        resolved = resolvable.get(target.lower())
        if resolved:
            linked_stems.add(resolved)

    for stem in all_page_stems:
        if stem not in linked_stems:
            issues.append(("INFO", f"{stem}.md", "Orphan page (no inbound wikilinks)"))

    # Check for dead wikilinks
    for target, sources in all_wikilinks.items():
        if target.lower() not in resolvable:
            for src in sources:
                issues.append(("WARN", src, f"Dead wikilink: [[{target}]]"))

    # Check index drift
    index_file = wiki_path / "_index.md"
    if index_file.exists():
        index_text = index_file.read_text(encoding="utf-8")
        indexed_links = set(extract_wikilinks(index_text))
        indexed_normalized = {l.replace(" ", "_") for l in indexed_links}
        indexed_normalized.update(indexed_links)

        for stem in all_page_stems:
            if stem not in indexed_normalized and stem.replace("_", " ") not in indexed_normalized:
                issues.append(("WARN", f"{stem}.md", "Not listed in _index.md"))

    # Count stubs
    stub_count = sum(1 for fm in pages.values() if fm.get("status") == "stub")
    if stub_count > 0:
        issues.append(("INFO", "wiki", f"{stub_count} stub page(s) needing expansion"))

    # Report
    print(f"\n{'='*60}")
    print(f"Wiki Lint Report: {wiki_dir}")
    print(f"{'='*60}")
    print(f"Pages scanned: {len(pages)}")
    print(f"Unique tags: {len(all_tags)}")
    print(f"Wikilink targets: {len(all_wikilinks)}")
    print()

    if not issues:
        print("No issues found.")
        return 0

    # Sort by severity
    severity_order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    issues.sort(key=lambda x: severity_order.get(x[0], 3))

    errors = sum(1 for i in issues if i[0] == "ERROR")
    warnings = sum(1 for i in issues if i[0] == "WARN")
    infos = sum(1 for i in issues if i[0] == "INFO")

    for severity, location, message in issues:
        print(f"[{severity}] {location}: {message}")

    print(f"\nSummary: {errors} error(s), {warnings} warning(s), {infos} info(s)")
    return 1 if errors > 0 else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py -3 lint_wiki.py <wiki_directory>")
        print("Example: py -3 lint_wiki.py builds/My_Wiki/wiki/")
        sys.exit(1)
    sys.exit(lint_wiki(sys.argv[1]))
