#!/usr/bin/env python3
"""Merge per-book chapter extractions into a canonical topic catalog.

Strategy: each section in each book becomes a candidate topic. Sections with
the same normalized title merge into one canonical topic; others create new
entries. After normalized merging, ``raw/catalog/aliases.yaml`` (if present)
applies any manual rename/merge/split decisions.

Output: per-branch topic catalog shards in ``raw/catalog/topics_{branch}.json``,
plus a summary ``raw/catalog/index.json``. Each per-branch file stays under
~500 KB.

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
# aliases.yaml lives in tools/ (version-controlled) because raw/ is gitignored
# on every build. The file is input-configuration, not pipeline output.
ALIASES_FILE = ROOT / "tools" / "aliases.yaml"


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


def consolidate(extractions_dir: Path | None = None) -> dict[str, dict]:
    """Walk per-chapter extractions and build the canonical topic dict.

    ``extractions_dir`` lets tests and downstream tooling point at a fixture
    set instead of the live ``raw/extractions/`` tree.
    """
    if extractions_dir is None:
        extractions_dir = EXTRACTIONS

    topics: dict[str, dict] = {}
    # Reverse lookup: normalized_title → slug (so we find an existing topic by title)
    norm_to_slug: dict[str, str] = {}

    book_dirs = sorted([d for d in extractions_dir.iterdir() if d.is_dir()])
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


def write_shards(shards: dict, catalog_dir: Path | None = None) -> dict:
    if catalog_dir is None:
        catalog_dir = CATALOG
    catalog_dir.mkdir(parents=True, exist_ok=True)
    summary = {}
    for branch, topic_list in shards.items():
        branch_slug = branch.replace("-", "_")
        out_file = catalog_dir / f"topics_{branch_slug}.json"
        out_file.write_text(
            json.dumps(topic_list, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        size_kb = out_file.stat().st_size / 1024
        summary[branch] = {"topic_count": len(topic_list), "file": out_file.name, "size_kb": size_kb}
    return summary


def write_index(topics: dict, summary: dict, catalog_dir: Path | None = None) -> Path:
    if catalog_dir is None:
        catalog_dir = CATALOG
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
    out_file = catalog_dir / "index.json"
    out_file.write_text(json.dumps(index, indent=2), encoding="utf-8")
    return out_file


# ---------------------------------------------------------------------------
# Alias application (renames, merges, splits)

def _load_aliases(aliases_file: Path) -> dict:
    """Load aliases.yaml if present, return a dict with empty defaults otherwise."""
    empty = {"version": 1, "renames": [], "merges": [], "splits": []}
    if not aliases_file.exists():
        return empty
    try:
        import yaml
    except ImportError:
        print(
            "  WARN: PyYAML not installed; aliases.yaml ignored. "
            "Install with `py -3 -m pip install pyyaml`.",
            file=sys.stderr,
        )
        return empty
    with aliases_file.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("renames", [])
    data.setdefault("merges", [])
    data.setdefault("splits", [])
    return data


def _humanize_slug(slug: str) -> str:
    """Default canonical-title from a slug when no explicit title is supplied."""
    return slug.replace("_", " ")


def _apply_renames(topics: dict[str, dict], rules: list[dict]) -> None:
    """Rename a topic slug in-place. The topic dict stays the same object."""
    for rule in rules:
        old = rule["from"]
        new = rule["to"]
        if old not in topics:
            print(f"  WARN: rename skipped, source slug not found: {old}", file=sys.stderr)
            continue
        if new in topics and new != old:
            raise ValueError(
                f"Cannot rename {old!r} → {new!r}: destination slug already exists. "
                f"Use a merge rule instead."
            )
        topic = topics.pop(old)
        topic["slug"] = new
        if "canonical_title" in rule:
            topic["canonical_title"] = rule["canonical_title"]
        else:
            topic["canonical_title"] = _humanize_slug(new)
        topics[new] = topic


def _apply_merges(topics: dict[str, dict], rules: list[dict]) -> None:
    """Collapse multiple topic slugs into one. The 'into' slug becomes canonical."""
    for rule in rules:
        sources = list(rule["from"])
        target = rule["into"]
        if target not in sources:
            # allow merges where 'into' is a fresh slug or an existing one not in 'from'
            if target not in topics and target in sources:
                raise ValueError(f"merge target {target!r} listed in both 'from' and missing")
        present = [s for s in sources if s in topics]
        if not present:
            print(
                f"  WARN: merge skipped, no source slugs found in catalog: {sources}",
                file=sys.stderr,
            )
            continue

        # Pick (or create) the target topic. Branch assignment rules:
        #   1. If the rule specifies `branch:`, use that.
        #   2. Else if the target slug exists, keep its branch.
        #   3. Else pick the branch that appears earliest in a priority
        #      order (pre-algebra > algebra-1 > algebra-2 > pre-calculus).
        #      This keeps merged topics in the most-introductory branch
        #      they appear in, which is usually what students expect.
        _BRANCH_PRIORITY = [
            "pre-algebra", "algebra-1", "geometry",
            "algebra-2", "trigonometry", "pre-calculus",
        ]
        if target in topics:
            merged = topics[target]
            if "branch" in rule:
                merged["branch"] = rule["branch"]
        else:
            # target isn't in catalog yet, pick a branch
            source_branches = [topics[s]["branch"] for s in present]
            if "branch" in rule:
                branch_choice = rule["branch"]
            else:
                # Pick the most-introductory branch among the sources.
                branch_choice = min(
                    source_branches,
                    key=lambda b: _BRANCH_PRIORITY.index(b)
                    if b in _BRANCH_PRIORITY
                    else len(_BRANCH_PRIORITY),
                )
            merged = new_topic(
                canonical_title=rule.get("canonical_title") or _humanize_slug(target),
                branch=branch_choice,
                slug=target,
            )
            topics[target] = merged

        if "canonical_title" in rule:
            merged["canonical_title"] = rule["canonical_title"]

        # Absorb each source into merged (skip target itself).
        for slug in present:
            if slug == target:
                continue
            src = topics.pop(slug)
            # Keep the old canonical_title as an alias.
            if src.get("canonical_title") and src["canonical_title"] not in merged["aliases"]:
                merged["aliases"].append(src["canonical_title"])
            for alias in src.get("aliases", []):
                if alias not in merged["aliases"]:
                    merged["aliases"].append(alias)
            for key in ("sources", "definitions", "properties", "theorems",
                        "examples", "figures", "checkpoints", "notes", "concepts"):
                merged.setdefault(key, []).extend(src.get(key, []))


def _source_matches(source: dict, criteria: list[dict]) -> bool:
    """A split-rule matcher: the source must match ANY criterion."""
    if not criteria:
        return False
    for c in criteria:
        book_ok = "book_slug" not in c or source.get("book_slug") == c["book_slug"]
        section_ok = "section_prefix" not in c or str(source.get("section_number", "")).startswith(c["section_prefix"])
        chapter_ok = "chapter_number" not in c or str(source.get("chapter_number", "")) == str(c["chapter_number"])
        if book_ok and section_ok and chapter_ok:
            return True
    return False


def _partition_by_source(topic: dict, children_specs: list[dict]) -> dict[str, dict]:
    """Distribute a topic's sources + blocks into children based on match rules.

    Each block's (book, chapter, section) tuple is matched against each child's
    keep_sources_matching criteria; the first matching child wins. Blocks that
    match no child are dropped with a warning (they'd otherwise orphan).
    """
    children: dict[str, dict] = {}
    for spec in children_specs:
        slug = spec["slug"]
        child = new_topic(
            canonical_title=spec.get("canonical_title") or _humanize_slug(slug),
            branch=topic["branch"],
            slug=slug,
        )
        children[slug] = child

    def match_child(book_slug: str, chapter: str, section: str) -> str | None:
        for spec in children_specs:
            criteria = spec.get("keep_sources_matching", [])
            fake_source = {
                "book_slug": book_slug,
                "chapter_number": chapter,
                "section_number": section,
            }
            if _source_matches(fake_source, criteria):
                return spec["slug"]
        return None

    # Distribute sources (the source header rows)
    for source in topic.get("sources", []):
        child_slug = match_child(
            source.get("book_slug", ""),
            source.get("chapter_number", ""),
            source.get("section_number", ""),
        )
        if child_slug is None:
            print(
                f"  WARN: split {topic['slug']}: source "
                f"{source.get('book_slug')}/{source.get('chapter_number')}.{source.get('section_number')} "
                f"matched no child, dropped",
                file=sys.stderr,
            )
            continue
        children[child_slug]["sources"].append(source)

    # Distribute block records (definitions, examples, etc.)
    for key in ("definitions", "properties", "theorems", "examples",
                "figures", "checkpoints", "notes", "concepts"):
        for block in topic.get(key, []):
            child_slug = match_child(
                block.get("book", ""),
                block.get("chapter", ""),
                block.get("section", ""),
            )
            if child_slug is None:
                continue
            children[child_slug][key].append(block)

    return children


def _apply_splits(topics: dict[str, dict], rules: list[dict]) -> None:
    """Carve one topic into multiple child topics by source-matching rules."""
    for rule in rules:
        src_slug = rule["from"]
        if src_slug not in topics:
            print(f"  WARN: split skipped, source slug not found: {src_slug}", file=sys.stderr)
            continue
        original = topics.pop(src_slug)
        children = _partition_by_source(original, rule["into"])
        for slug, child in children.items():
            if slug in topics:
                raise ValueError(
                    f"split produced slug {slug!r}, which already exists. "
                    f"Pick a different child slug or merge afterward."
                )
            topics[slug] = child


def _check_rule_conflicts(aliases: dict) -> None:
    """Fail fast if a slug is touched by more than one rule."""
    touched: dict[str, list[str]] = defaultdict(list)
    for rule in aliases.get("renames", []):
        touched[rule["from"]].append("rename")
        touched[rule["to"]].append("rename-dest")
    for rule in aliases.get("merges", []):
        for s in rule.get("from", []):
            touched[s].append("merge-src")
        touched[rule["into"]].append("merge-dest")
    for rule in aliases.get("splits", []):
        touched[rule["from"]].append("split-src")
        for spec in rule.get("into", []):
            touched[spec["slug"]].append("split-dest")

    conflicts = {slug: roles for slug, roles in touched.items() if len(roles) > 1 and len(set(roles)) > 1}
    # Allow a slug to appear as dest once and src once (e.g., renamed then merged into),
    # but not if it's multiply assigned as a destination or source.
    real_conflicts = {}
    for slug, roles in touched.items():
        dests = sum(1 for r in roles if r.endswith("-dest") or r == "rename")
        if dests > 1:
            real_conflicts[slug] = roles
    if real_conflicts:
        raise ValueError(f"aliases.yaml: slugs assigned by multiple rules: {real_conflicts}")


def apply_aliases(topics: dict[str, dict], aliases_file: Path | None = None) -> dict[str, dict]:
    """Apply renames, merges, and splits from aliases.yaml (in that order).

    Returns the same dict (mutated) for convenience.
    """
    if aliases_file is None:
        aliases_file = ALIASES_FILE
    aliases = _load_aliases(aliases_file)
    _check_rule_conflicts(aliases)
    _apply_renames(topics, aliases.get("renames", []))
    _apply_merges(topics, aliases.get("merges", []))
    _apply_splits(topics, aliases.get("splits", []))
    return topics


def main():
    print("Consolidating extractions...")
    topics = consolidate()
    print(f"  {len(topics)} canonical topic candidates from all books (pre-alias)")

    before_count = len(topics)
    apply_aliases(topics)
    after_count = len(topics)
    if before_count != after_count:
        delta = after_count - before_count
        sign = "+" if delta >= 0 else ""
        print(f"  aliases.yaml applied: {after_count} topics ({sign}{delta} from rules)")
    else:
        print(f"  aliases.yaml applied: no net change")

    shards = shard_by_branch(topics)
    summary = write_shards(shards)

    for branch, info in sorted(summary.items()):
        print(f"  {branch:<15} {info['topic_count']:>3} topics -> {info['file']} ({info['size_kb']:>6.1f} KB)")

    index_file = write_index(topics, summary)
    print(f"  index -> {index_file.name} ({index_file.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
