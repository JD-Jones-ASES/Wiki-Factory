"""Build Index - Regenerate _index.md from wiki page frontmatter."""

import sys
import re
import yaml
from pathlib import Path
from collections import defaultdict


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def first_sentence(filepath):
    """Extract first non-frontmatter, non-heading sentence."""
    text = filepath.read_text(encoding="utf-8")
    # Strip frontmatter
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    # Find first non-empty, non-heading line
    for line in text.split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            # Truncate to ~80 chars
            if len(line) > 80:
                return line[:77] + "..."
            return line
    return ""


def build_index(wiki_dir):
    """Regenerate _index.md from frontmatter."""
    wiki_path = Path(wiki_dir)
    if not wiki_path.exists():
        print(f"ERROR: Wiki directory not found: {wiki_dir}")
        return 1

    system_files = {"_index.md", "_log.md", "_overview.md", "_tag_taxonomy.md"}
    pages_by_type = defaultdict(list)

    # Scan all markdown files
    for md_file in wiki_path.rglob("*.md"):
        if md_file.name in system_files:
            continue

        fm = extract_frontmatter(md_file)
        if fm is None:
            continue

        page_type = fm.get("type", "uncategorized")
        title = fm.get("title", md_file.stem.replace("_", " "))
        status = fm.get("status", "unknown")
        source_count = len(fm.get("source_refs", []))
        summary = first_sentence(md_file)

        pages_by_type[page_type].append({
            "title": title,
            "stem": md_file.stem,
            "status": status,
            "source_count": source_count,
            "summary": summary,
        })

    # Sort pages within each type
    for page_type in pages_by_type:
        pages_by_type[page_type].sort(key=lambda p: p["title"])

    # Generate index
    type_order = ["entity", "concept", "source", "synthesis", "timeline"]
    lines = [
        "---",
        "title: \"Wiki Index\"",
        "type: overview",
        f"updated: {__import__('datetime').date.today().isoformat()}",
        "---",
        "",
        "# Wiki Index",
        "",
        f"Total pages: {sum(len(v) for v in pages_by_type.values())}",
        "",
    ]

    for page_type in type_order:
        if page_type not in pages_by_type:
            continue
        pages = pages_by_type[page_type]
        type_labels = {
            "entity": "Entities", "concept": "Concepts", "source": "Sources",
            "synthesis": "Synthesis", "timeline": "Timelines",
        }
        type_label = type_labels.get(page_type, page_type.capitalize() + "s")
        lines.append(f"## {type_label}")
        lines.append("")
        for p in pages:
            status_marker = "" if p["status"] == "complete" else f" [{p['status']}]"
            src_note = f" ({p['source_count']} sources)" if p["source_count"] > 0 else ""
            summary_note = f" --- {p['summary']}" if p["summary"] else ""
            lines.append(f"- [[{p['title']}]]{status_marker}{src_note}{summary_note}")
        lines.append("")

    # Handle uncategorized
    if "uncategorized" in pages_by_type:
        lines.append("## Uncategorized")
        lines.append("")
        for p in pages_by_type["uncategorized"]:
            lines.append(f"- [[{p['title']}]] [uncategorized]")
        lines.append("")

    # Write index
    index_path = wiki_path / "_index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for v in pages_by_type.values())
    print(f"Index rebuilt: {total} pages across {len(pages_by_type)} types")
    print(f"Written to: {index_path}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py -3 build_index.py <wiki_directory>")
        print("Example: py -3 build_index.py builds/My_Wiki/wiki/")
        sys.exit(1)
    sys.exit(build_index(sys.argv[1]))
