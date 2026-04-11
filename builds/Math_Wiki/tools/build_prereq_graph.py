#!/usr/bin/env python3
"""Build ``wiki/_data/prereq_graph.json`` from topic frontmatter.

Walks ``wiki/topics/**/*.md`` and, for each topic, reads the ``prerequisites:``
YAML list. Each entry points at another topic by relative path (e.g.
``topics/pre_algebra/Similar_Triangles``). The builder:

  * Normalizes each prerequisite path to the target topic's lowercase slug
    (matching the convention used by ``problem_vault_widget``).
  * Records per-topic immediate prerequisites as a list of
    ``{slug, title, href}`` dicts the widget can render directly.
  * Records a reverse edge list (``used_by``) so a topic sees which later
    topics depend on it (useful for a future "next steps" widget).
  * Looks up each target's display title from its frontmatter.
  * Writes the resulting JSON to ``wiki/_data/prereq_graph.json``.

Idempotent. Run from ``builds/Math_Wiki/``:

    py -3 tools/build_prereq_graph.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
OUTPUT = WIKI_DIR / "_data" / "prereq_graph.json"


def extract_frontmatter(text: str) -> dict:
    """Parse the YAML frontmatter block into a minimal dict.

    No pyyaml dependency: we only need a few scalar fields and one list.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    body = text[3:end]
    result: dict = {}
    current_key = None
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            if current_key and stripped.startswith("- "):
                result.setdefault(current_key, []).append(stripped[2:].strip(" \"'"))
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", stripped)
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        current_key = key
        if value == "" or value.startswith("#"):
            continue
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if inner:
                items = [p.strip().strip(" \"'") for p in inner.split(",")]
                result[key] = [i for i in items if i]
            else:
                result[key] = []
        else:
            result[key] = value.strip(" \"'")
    return result


def normalize_target(target: str) -> str:
    """Pull the bare filename stem from a prerequisite path.

    Handles all the shapes the frontmatter uses in practice:
      ``topics/pre_algebra/Similar_Triangles``  -> ``Similar_Triangles``
      ``topics/algebra/The_Quadratic_Formula``  -> ``The_Quadratic_Formula``
      ``Similar_Triangles``                    -> ``Similar_Triangles``
      ``Similar_Triangles.md``                 -> ``Similar_Triangles``
    """
    target = target.strip()
    if target.endswith(".md"):
        target = target[:-3]
    # Drop any leading slashes / directories.
    if "/" in target:
        target = target.rsplit("/", 1)[-1]
    return target


def main() -> None:
    if not TOPICS_DIR.exists():
        print(f"topics directory not found: {TOPICS_DIR}", file=sys.stderr)
        sys.exit(1)

    # First pass: build a stem -> (title, slug, branch) map for every topic file.
    stem_info: dict[str, dict] = {}
    for md in TOPICS_DIR.rglob("*.md"):
        stem = md.stem
        text = md.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        stem_info[stem] = {
            "slug": stem.lower(),
            "title": fm.get("title", stem.replace("_", " ")),
            "stem": stem,
            "branch": fm.get("branch", ""),
        }

    # Second pass: build the immediate prerequisite list for every topic.
    immediate: dict[str, list[dict]] = {}
    used_by: dict[str, list[str]] = {}

    for md in sorted(TOPICS_DIR.rglob("*.md")):
        stem = md.stem
        text = md.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        prereqs = fm.get("prerequisites", []) or []
        if not isinstance(prereqs, list):
            continue

        resolved: list[dict] = []
        seen: set[str] = set()
        for p in prereqs:
            target_stem = normalize_target(p)
            if not target_stem or target_stem in seen:
                continue
            seen.add(target_stem)
            if target_stem not in stem_info:
                # Dangling prerequisite: skip silently. The lint should catch
                # this separately; we do not emit broken entries.
                continue
            info = stem_info[target_stem]
            resolved.append({
                "slug": info["slug"],
                "stem": info["stem"],
                "title": info["title"],
            })
            used_by.setdefault(info["stem"], []).append(stem)

        if resolved:
            immediate[stem] = resolved

    # Write the graph.
    graph = {
        "version": "1",
        "generated_from": "topic frontmatter prerequisites field",
        "topics": {
            stem: {
                "title": info["title"],
                "slug": info["slug"],
                "branch": info["branch"],
                "prerequisites": immediate.get(stem, []),
                "used_by": sorted(set(used_by.get(stem, []))),
            }
            for stem, info in stem_info.items()
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(graph, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    topics_with_prereqs = sum(1 for t in graph["topics"].values() if t["prerequisites"])
    total_edges = sum(len(t["prerequisites"]) for t in graph["topics"].values())
    size_kb = OUTPUT.stat().st_size / 1024
    print(
        f"  wrote {OUTPUT.relative_to(ROOT)} "
        f"({size_kb:.1f} KB, {len(graph['topics'])} topics, "
        f"{topics_with_prereqs} with prereqs, {total_edges} edges)"
    )


if __name__ == "__main__":
    main()
