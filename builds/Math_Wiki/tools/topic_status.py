#!/usr/bin/env python3
"""Topic progress dashboard for Math_Wiki.

Scans every topic page under ``wiki/topics/`` and reports, for each topic:

- ``status`` from frontmatter (stub / draft / complete)
- body word count (excluding frontmatter, widget divs, HTML, code blocks)
- number of worked examples (Heading ``## Example`` or ``### Example``)
- number of figures (``![[...svg]]`` embeds and ``figures:`` frontmatter list)
- number of outbound wikilinks (excluding asset embeds)
- number of registered generators (from ``wiki/_data/problem_types_index.json``)
- a completion score (0-100) that rolls the above into a single number

Produces two outputs under ``wiki/_data/``:

1. ``topic_status.json`` --- machine-readable JSON report
2. ``Topic_Status.md`` --- human-readable table, grouped by branch, living in
   the wiki so it deploys to the site

Run from ``builds/Math_Wiki/``:

    py -3 tools/topic_status.py                   # print summary + write files
    py -3 tools/topic_status.py --json            # JSON only to stdout
    py -3 tools/topic_status.py --branch algebra  # filter one branch
    py -3 tools/topic_status.py --verbose         # per-topic table on stdout

The completion score thresholds are calibrated against the plan's cluster
verification rules (>=300 body words, >=2 examples, >=3 generators, >=3
prerequisite links, >=3 see-also links).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
DATA_DIR = WIKI_DIR / "_data"
INDEX_FILE = DATA_DIR / "problem_types_index.json"


# Regex helpers -------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
ASSET_EXT_RE = re.compile(r"\.(svg|png|jpe?g|gif|webp|mp4|webm|mp3|wav|pdf)$", re.IGNORECASE)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"\$[^$\n]+\$")
EXAMPLE_HEADING_RE = re.compile(
    # Matches "## Example 1", "## Example:", "## Worked Example", "### Example 2", etc.
    # Intentionally does NOT match "## Example Walkthroughs Available" (the auto-stub
    # placeholder) or bare "## Examples" without a number/colon, because neither
    # indicates a real worked example is present.
    r"^##+\s+(?:worked\s+)?example(?:\s+\d+|\s*:|\s*$)",
    re.IGNORECASE | re.MULTILINE,
)
FIGURE_EMBED_RE = re.compile(r"!\[\[[^\]]+\.(svg|png|jpe?g|gif|webp)[^\]]*\]\]", re.IGNORECASE)


# ---------------------------------------------------------------------------

def _strip_frontmatter(text: str) -> tuple[dict | None, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, text[m.end():]
    return fm, text[m.end():]


def _strip_for_word_count(body: str) -> str:
    """Remove code, HTML, math, wikilinks so only actual prose counts."""
    b = CODE_FENCE_RE.sub(" ", body)
    b = MATH_BLOCK_RE.sub(" ", b)
    b = INLINE_MATH_RE.sub(" ", b)
    b = HTML_TAG_RE.sub(" ", b)
    # Remove wikilinks (keep the pipe-rendered label if present)
    b = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", b)
    b = re.sub(r"\[\[([^\]]+)\]\]", r"\1", b)
    # Remove markdown image embeds and Obsidian embeds
    b = re.sub(r"!\[\[[^\]]+\]\]", " ", b)
    b = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", b)
    # Collapse whitespace
    b = re.sub(r"\s+", " ", b).strip()
    return b


def _word_count(prose: str) -> int:
    return len(re.findall(r"\b\w+\b", prose))


def _count_examples(body: str) -> int:
    return len(EXAMPLE_HEADING_RE.findall(body))


def _count_figures(body: str, fm: dict) -> int:
    embeds = len(FIGURE_EMBED_RE.findall(body))
    fm_figs = len(fm.get("figures", []) or []) if fm else 0
    return max(embeds, fm_figs)


def _count_outbound_wikilinks(body: str) -> int:
    targets = WIKILINK_RE.findall(body)
    return sum(1 for t in targets if not ASSET_EXT_RE.search(t))


def _count_prereq_links(fm: dict | None) -> int:
    if not fm:
        return 0
    return len(fm.get("prerequisites", []) or [])


def _count_related_links(fm: dict | None) -> int:
    if not fm:
        return 0
    return len(fm.get("related", []) or [])


def load_generators_by_topic() -> dict[str, list[str]]:
    """Return {topic_slug_lower: [generator_id, ...]} from problem_types_index.json."""
    if not INDEX_FILE.exists():
        return {}
    index = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    by_topic = index.get("by_topic", {})
    return {
        topic_slug.lower(): [g["generator_id"] for g in gens]
        for topic_slug, gens in by_topic.items()
    }


def scan_topic(md_path: Path, generators_by_topic: dict[str, list[str]]) -> dict:
    """Collect all metrics for one topic page."""
    text = md_path.read_text(encoding="utf-8")
    fm, body = _strip_frontmatter(text)
    slug_key = md_path.stem.lower()

    prose = _strip_for_word_count(body)
    word_count = _word_count(prose)
    example_count = _count_examples(body)
    figure_count = _count_figures(body, fm or {})
    wikilinks = _count_outbound_wikilinks(body)
    generators = generators_by_topic.get(slug_key, [])
    generator_count = len(generators)

    fm_status = (fm or {}).get("status", "unknown")
    fm_confidence = (fm or {}).get("confidence", "unknown")
    prereq_count = _count_prereq_links(fm)
    related_count = _count_related_links(fm)

    score = _completion_score(
        status=fm_status,
        word_count=word_count,
        example_count=example_count,
        figure_count=figure_count,
        generator_count=generator_count,
        prereq_count=prereq_count,
        related_count=related_count,
    )

    branch = md_path.parent.name
    return {
        "slug": md_path.stem,
        "branch": branch,
        "relpath": str(md_path.relative_to(ROOT)).replace("\\", "/"),
        "status": fm_status,
        "confidence": fm_confidence,
        "word_count": word_count,
        "example_count": example_count,
        "figure_count": figure_count,
        "wikilink_count": wikilinks,
        "generator_count": generator_count,
        "generators": generators,
        "prerequisite_count": prereq_count,
        "related_count": related_count,
        "score": score,
    }


def _completion_score(*, status: str, word_count: int, example_count: int,
                      figure_count: int, generator_count: int,
                      prereq_count: int, related_count: int) -> int:
    """Roll the topic's metrics into a 0-100 score.

    The weights match the plan's per-cluster verification rules:
      - prose body 300+ words:  25 points
      - 2+ worked examples:     15 points
      - 3+ generators:          25 points (ramp: 0/1/2/3 = 0/10/18/25)
      - 3+ prereq links:        10 points
      - 3+ related links:       10 points
      - 1+ figure:               5 points
      - status field:           10 points (stub=0, draft=5, complete=10)
    """
    pts = 0
    if word_count >= 300:
        pts += 25
    elif word_count >= 150:
        pts += 15
    elif word_count >= 50:
        pts += 5

    if example_count >= 2:
        pts += 15
    elif example_count >= 1:
        pts += 8

    gen_ladder = {0: 0, 1: 10, 2: 18}
    pts += gen_ladder.get(generator_count, 25 if generator_count >= 3 else 0)

    if prereq_count >= 3:
        pts += 10
    elif prereq_count >= 1:
        pts += 5

    if related_count >= 3:
        pts += 10
    elif related_count >= 1:
        pts += 5

    if figure_count >= 1:
        pts += 5

    if status == "complete":
        pts += 10
    elif status == "draft":
        pts += 5
    # stub = 0

    return min(pts, 100)


def scan_all(branches: list[str] | None = None) -> list[dict]:
    gbt = load_generators_by_topic()
    results: list[dict] = []
    if not TOPICS_DIR.exists():
        return results
    for md in sorted(TOPICS_DIR.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        if branches and md.parent.name not in branches:
            continue
        results.append(scan_topic(md, gbt))
    return results


def summarize(results: list[dict]) -> dict:
    """Collapse per-topic rows into branch + overall summaries."""
    by_branch: dict[str, dict] = {}
    for r in results:
        b = r["branch"]
        bucket = by_branch.setdefault(b, {
            "branch": b,
            "topic_count": 0,
            "with_generators": 0,
            "with_prose_300": 0,
            "with_examples_2": 0,
            "with_figure": 0,
            "avg_score": 0.0,
            "status_counts": {"stub": 0, "draft": 0, "complete": 0, "unknown": 0},
        })
        bucket["topic_count"] += 1
        if r["generator_count"] >= 3:
            bucket["with_generators"] += 1
        if r["word_count"] >= 300:
            bucket["with_prose_300"] += 1
        if r["example_count"] >= 2:
            bucket["with_examples_2"] += 1
        if r["figure_count"] >= 1:
            bucket["with_figure"] += 1
        bucket["avg_score"] += r["score"]
        status = r["status"] if r["status"] in bucket["status_counts"] else "unknown"
        bucket["status_counts"][status] += 1

    for b in by_branch.values():
        if b["topic_count"]:
            b["avg_score"] = round(b["avg_score"] / b["topic_count"], 1)

    total = len(results)
    overall = {
        "total_topics": total,
        "complete": sum(1 for r in results if r["status"] == "complete"),
        "draft": sum(1 for r in results if r["status"] == "draft"),
        "stub": sum(1 for r in results if r["status"] == "stub"),
        "with_3plus_generators": sum(1 for r in results if r["generator_count"] >= 3),
        "with_300plus_words": sum(1 for r in results if r["word_count"] >= 300),
        "avg_score": round(sum(r["score"] for r in results) / total, 1) if total else 0.0,
    }
    return {"overall": overall, "by_branch": by_branch}


# ---------------------------------------------------------------------------
# Markdown rendering

def render_markdown(results: list[dict], summary: dict) -> str:
    lines: list[str] = []
    today = date.today().isoformat()
    lines.append("---")
    lines.append('title: "Topic Status Dashboard"')
    lines.append("type: overview")
    lines.append("aliases: []")
    lines.append('tags: ["#meta-dashboard"]')
    lines.append(f"created: {today}")
    lines.append(f"updated: {today}")
    lines.append("source_refs: []")
    lines.append("related: []")
    lines.append("status: complete")
    lines.append("confidence: high")
    lines.append(
        'summary: "Auto-generated progress dashboard. Regenerate with tools/topic_status.py."'
    )
    lines.append("---")
    lines.append("")
    lines.append("> [[_overview|Home]] > Topic Status")
    lines.append("")
    lines.append("# Topic Status Dashboard")
    lines.append("")
    lines.append("_This page is generated by `tools/topic_status.py`. Do not hand-edit._")
    lines.append("")

    overall = summary["overall"]
    lines.append("## Overall")
    lines.append("")
    lines.append(f"- **Total topics:** {overall['total_topics']}")
    lines.append(f"- **Complete (status):** {overall['complete']}")
    lines.append(f"- **Draft (status):** {overall['draft']}")
    lines.append(f"- **Stub (status):** {overall['stub']}")
    lines.append(f"- **With 3+ generators:** {overall['with_3plus_generators']}")
    lines.append(f"- **With 300+ body words:** {overall['with_300plus_words']}")
    lines.append(f"- **Average completion score:** {overall['avg_score']} / 100")
    lines.append("")

    lines.append("## By branch")
    lines.append("")
    lines.append("| Branch | Topics | 3+ gens | 300+ words | 2+ examples | Has figure | Stubs | Avg score |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for b in sorted(summary["by_branch"].values(), key=lambda x: x["branch"]):
        lines.append(
            f"| {b['branch']} | {b['topic_count']} | {b['with_generators']} | "
            f"{b['with_prose_300']} | {b['with_examples_2']} | {b['with_figure']} | "
            f"{b['status_counts']['stub']} | {b['avg_score']} |"
        )
    lines.append("")

    # Per-branch topic tables, top-scored first
    by_branch_rows: dict[str, list[dict]] = {}
    for r in results:
        by_branch_rows.setdefault(r["branch"], []).append(r)

    for branch in sorted(by_branch_rows):
        rows = sorted(by_branch_rows[branch], key=lambda r: (-r["score"], r["slug"]))
        lines.append(f"## {branch} ({len(rows)} topics)")
        lines.append("")
        lines.append("| Topic | Status | Words | Exs | Figs | Links | Gens | Score |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for r in rows:
            link = f"[[{r['slug']}]]"
            lines.append(
                f"| {link} | {r['status']} | {r['word_count']} | {r['example_count']} | "
                f"{r['figure_count']} | {r['wikilink_count']} | {r['generator_count']} | "
                f"{r['score']} |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("### Completion score rubric")
    lines.append("")
    lines.append("- **Prose 300+ words:** 25 pts (150+ = 15, 50+ = 5)")
    lines.append("- **2+ worked examples:** 15 pts (1 = 8)")
    lines.append("- **3+ generators:** 25 pts (2 = 18, 1 = 10)")
    lines.append("- **3+ prerequisite links:** 10 pts (1+ = 5)")
    lines.append("- **3+ see-also links:** 10 pts (1+ = 5)")
    lines.append("- **Figure present:** 5 pts")
    lines.append("- **Status field:** complete = 10, draft = 5, stub = 0")
    lines.append("")
    lines.append("A topic at 90+ satisfies the plan's cluster verification rules.")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", help="filter to a single branch (e.g., algebra)")
    parser.add_argument("--json", action="store_true", help="print JSON report to stdout")
    parser.add_argument("--verbose", action="store_true", help="print per-topic table")
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="skip writing the dashboard files (useful for dry runs / CI gates)",
    )
    args = parser.parse_args()

    branches = [args.branch] if args.branch else None
    results = scan_all(branches)
    summary = summarize(results)

    if args.json:
        print(json.dumps({"summary": summary, "topics": results}, indent=2))
        return

    overall = summary["overall"]
    print(f"Topic Status: {overall['total_topics']} topics across "
          f"{len(summary['by_branch'])} branches")
    print(f"  complete: {overall['complete']}  draft: {overall['draft']}  "
          f"stub: {overall['stub']}")
    print(f"  3+ generators: {overall['with_3plus_generators']}  "
          f"300+ words: {overall['with_300plus_words']}")
    print(f"  avg score: {overall['avg_score']} / 100")
    print()
    for b in sorted(summary["by_branch"].values(), key=lambda x: x["branch"]):
        print(
            f"  {b['branch']:<15} {b['topic_count']:>3} topics, "
            f"{b['with_generators']:>3} with 3+ gens, avg {b['avg_score']:>5.1f}"
        )

    if args.verbose:
        print()
        print("Per-topic:")
        for r in sorted(results, key=lambda r: (-r["score"], r["slug"])):
            print(
                f"  [{r['score']:>3}]  {r['branch']:<12} {r['slug']:<45} "
                f"status={r['status']:<8} words={r['word_count']:>4} "
                f"exs={r['example_count']} gens={r['generator_count']}"
            )

    if args.no_write:
        return

    # Write JSON + markdown dashboards to wiki/_data/ and wiki/
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    json_out = DATA_DIR / "topic_status.json"
    json_out.write_text(
        json.dumps({"summary": summary, "topics": results}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n  JSON  -> {json_out.relative_to(ROOT)} ({json_out.stat().st_size / 1024:.1f} KB)")

    md_out = WIKI_DIR / "Topic_Status.md"
    md_out.write_text(render_markdown(results, summary), encoding="utf-8")
    print(f"  MD    -> {md_out.relative_to(ROOT)} ({md_out.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
