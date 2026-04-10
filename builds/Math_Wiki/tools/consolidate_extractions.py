#!/usr/bin/env python3
"""Merge per-book chapter extractions into a canonical topic catalog.

Strategy: each section in each book becomes a candidate topic. Sections with
the same normalized title merge into one canonical topic; others create new
entries. No fuzzy matching (to avoid false merges) --- the first pass keeps
high precision and some duplicates are expected and can be merged later by
hand or by a second-pass review.

Output: per-branch topic catalog shards in ``raw/catalog/topics_{branch}.json``,
plus a summary ``raw/catalog/index.json``. Each per-branch file stays under
~300 KB.

Run from ``builds/Math_Wiki/``:

    py -3 tools/consolidate_extractions.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXTRACTIONS = ROOT / "raw" / "extractions"
CATALOG = ROOT / "raw" / "catalog"


# ---------------------------------------------------------------------------
# Title normalization

_STOPWORD_PREFIXES = ("the ", "a ", "an ")

_SYNONYM_REPLACEMENTS = [
    (r"\bequations in one variable\b", "equations"),
    (r"\bequations in two variables\b", "linear equations"),
    (r"\bintroduction to\b", ""),
    (r"\ba review of\b", ""),
    (r"\bbasics?\b", ""),
    (r"\bfundamentals?\b", ""),
    (r"\bpart\s+\d+\b", ""),       # "Graphing Rational Functions: Part 1" → "graphing rational functions"
    (r":\s*part\s+(i{1,3}|\d+)$", ""),
    (r"\s*\(review\)\s*$", ""),
    (r"[\-_]+", " "),              # hyphens/underscores → spaces
]


def normalize_title(title: str) -> str:
    """Normalize a section title for comparison.

    Lowercases, strips leading articles, applies synonym replacements,
    splits CamelCase (for Stitz-Zeager file names), collapses whitespace,
    drops punctuation.
    """
    t = (title or "").strip()
    # Split CamelCase: "AbsoluteValueFunctions" -> "Absolute Value Functions"
    t = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", t)
    t = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", t)
    t = t.lower()
    for prefix in _STOPWORD_PREFIXES:
        if t.startswith(prefix):
            t = t[len(prefix):]
    for pattern, replacement in _SYNONYM_REPLACEMENTS:
        t = re.sub(pattern, replacement, t)
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def title_case_slug(title: str) -> str:
    """Convert a plain title to a Title_Case slug safe for filenames."""
    plain = re.sub(r"[^A-Za-z0-9\s]", " ", title or "")
    words = plain.split()
    if not words:
        return "Untitled"
    return "_".join(w.capitalize() for w in words)


# ---------------------------------------------------------------------------
# Consolidation

def new_topic(canonical_title: str, branch: str, slug: str) -> dict:
    return {
        "slug": slug,
        "canonical_title": canonical_title,
        "aliases": [],
        "branch": branch,
        "sources": [],
        "definitions": [],
        "properties": [],
        "theorems": [],
        "examples": [],
        "figures": [],
        "checkpoints": [],
        "notes": [],
        "concepts": [],
    }


def block_record(block: dict, book_slug: str, chapter_number: str, section_number: str) -> dict:
    """Compact record for a single block.

    Keeps a preview plus metadata. Full body_latex lives in the per-chapter
    extraction shards (raw/extractions/{book_slug}/chapter_NN.json) and can
    be fetched from there on demand. Omitting it here keeps every per-branch
    catalog shard under ~400 KB.
    """
    return {
        "book": book_slug,
        "chapter": chapter_number,
        "section": section_number,
        "title": block.get("title_plain") or block.get("title"),
        "preview": block["body_preview"],
        "label": block["label"],
        "body_length": len(block.get("body_latex", "")),
    }


def consolidate() -> dict[str, dict]:
    topics: dict[str, dict] = {}
    # Reverse lookup: normalized_title → slug (so we find an existing topic by title)
    norm_to_slug: dict[str, str] = {}

    book_dirs = sorted([d for d in EXTRACTIONS.iterdir() if d.is_dir()])
    if not book_dirs:
        print("  No extractions found. Run ingest_math_book.py first.", file=sys.stderr)
        return topics

    for book_dir in book_dirs:
        book_slug = book_dir.name
        for chapter_file in sorted(book_dir.glob("chapter_*.json")):
            chapter = json.loads(chapter_file.read_text(encoding="utf-8"))
            branch = chapter.get("branch_hint", "unknown")

            for section in chapter["sections"]:
                section_title = section["title_plain"] or f"Section {section['number']}"
                normalized = normalize_title(section_title)

                # Find or create a canonical topic
                if normalized in norm_to_slug:
                    slug = norm_to_slug[normalized]
                    topic = topics[slug]
                    if section_title not in topic["aliases"] and section_title != topic["canonical_title"]:
                        topic["aliases"].append(section_title)
                else:
                    base_slug = title_case_slug(section_title)
                    slug = base_slug
                    suffix = 1
                    while slug in topics:
                        slug = f"{base_slug}_{suffix}"
                        suffix += 1
                    topic = new_topic(section_title, branch, slug)
                    topics[slug] = topic
                    norm_to_slug[normalized] = slug

                # Add source reference
                topic["sources"].append(
                    {
                        "book_slug": book_slug,
                        "book_title": chapter["book_title"],
                        "chapter_number": chapter["chapter_number"],
                        "chapter_title": chapter["chapter_title"],
                        "section_number": section["number"],
                        "section_title": section_title,
                        "block_counts": section["block_counts"],
                        "source_file": section["source_file"],
                    }
                )

                # Append blocks by kind
                for block in section["blocks"]:
                    kind = block["kind"]
                    record = block_record(
                        block, book_slug, chapter["chapter_number"], section["number"]
                    )
                    if kind == "definition":
                        topic["definitions"].append(record)
                    elif kind == "property":
                        topic["properties"].append(record)
                    elif kind == "theorem":
                        topic["theorems"].append(record)
                    elif kind == "example":
                        topic["examples"].append(record)
                    elif kind == "figure":
                        topic["figures"].append(record)
                    elif kind == "checkpoint":
                        topic["checkpoints"].append(record)
                    elif kind == "note":
                        topic["notes"].append(record)
                    elif kind == "concept":
                        topic["concepts"].append(record)

    return topics


def shard_by_branch(topics: dict) -> dict[str, list[dict]]:
    shards: dict[str, list[dict]] = defaultdict(list)
    for slug, topic in topics.items():
        shards[topic["branch"]].append(topic)
    return shards


def write_shards(shards: dict) -> dict:
    CATALOG.mkdir(parents=True, exist_ok=True)
    summary = {}
    for branch, topic_list in shards.items():
        branch_slug = branch.replace("-", "_")
        out_file = CATALOG / f"topics_{branch_slug}.json"
        out_file.write_text(
            json.dumps(topic_list, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        size_kb = out_file.stat().st_size / 1024
        summary[branch] = {"topic_count": len(topic_list), "file": out_file.name, "size_kb": size_kb}
    return summary


def write_index(topics: dict, summary: dict) -> Path:
    index = {
        "total_topics": len(topics),
        "by_branch": summary,
        "topics": [
            {
                "slug": slug,
                "title": t["canonical_title"],
                "branch": t["branch"],
                "alias_count": len(t["aliases"]),
                "source_count": len(t["sources"]),
                "definition_count": len(t["definitions"]),
                "example_count": len(t["examples"]),
                "property_count": len(t["properties"]),
                "theorem_count": len(t["theorems"]),
            }
            for slug, t in sorted(topics.items())
        ],
    }
    out_file = CATALOG / "index.json"
    out_file.write_text(json.dumps(index, indent=2), encoding="utf-8")
    return out_file


def main():
    print("Consolidating extractions...")
    topics = consolidate()
    print(f"  {len(topics)} canonical topic candidates from all books")

    shards = shard_by_branch(topics)
    summary = write_shards(shards)

    for branch, info in sorted(summary.items()):
        print(f"  {branch:<15} {info['topic_count']:>3} topics -> {info['file']} ({info['size_kb']:>6.1f} KB)")

    index_file = write_index(topics, summary)
    print(f"  index -> {index_file.name} ({index_file.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
