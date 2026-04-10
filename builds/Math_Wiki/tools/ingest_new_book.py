#!/usr/bin/env python3
"""Guided pipeline to ingest a new textbook into Math_Wiki.

This script is the canonical entry point for adding a SIXTH (or seventh,
...) textbook to Math_Wiki. It doubles as executable documentation of the
ingest workflow: each step prints what it's about to do, runs it, and
prints what changed. Any step can be run in isolation via flags.

The pipeline:

  1. Verify the book source directory exists under ``raw/books/<slug>/``
  2. Verify the book is registered in ``tools/ingest_math_book.py`` (BOOKS dict)
  3. Run ``ingest_math_book.py --book <slug>`` to extract per-chapter JSON
  4. Run ``consolidate_extractions.py`` to rebuild the catalog
     (this re-runs on ALL books, not just the new one, so merges and renames
     in aliases.yaml stay in force)
  5. Diff the new catalog against the old to show what's added/changed
  6. Run ``generate_topic_stubs.py --branch all`` to emit new stub pages
     (existing pages, including hand-written ones, are left alone)
  7. Run ``update_branch_hubs.py`` to refresh auto-populated topic lists
  8. Run ``build_index.py`` to refresh the wiki index
  9. Run ``lint_wiki.py`` for a sanity check
 10. Remind you to propose alias merges in ``tools/aliases.yaml`` for any
     duplicates the conservative consolidator didn't catch.

Usage:

    py -3 tools/ingest_new_book.py --slug my_new_book
    py -3 tools/ingest_new_book.py --slug my_new_book --dry-run
    py -3 tools/ingest_new_book.py --slug my_new_book --skip-steps 7,9

Prerequisites before running this script:

  1. Copy the book's LaTeX source into ``raw/books/<slug>/``
     (gitignored; safe to put large files there).
  2. Add an entry to the ``BOOKS`` dict in ``tools/ingest_math_book.py``
     with the slug, title, branch_hint, root_dir, layout, and env_map.
     If the book uses a new LaTeX convention, extend ``CURRICULUM_ENVS``
     or ``STITZ_ENVS`` or add a new env_map.
  3. Skim a few .tex files in the new book to verify the regex-based
     block extractor will find ``\\begin{env}[title]...\\end{env}`` blocks.
     If the book uses a very different structure, you may need to add
     a new layout type to ingest_math_book.py.

See the "env_map Author's Guide" section of Math_Wiki.md for how to
write an env_map for a new LaTeX convention.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT / "raw" / "books"
CATALOG_DIR = ROOT / "raw" / "catalog"
WIKI_DIR = ROOT / "wiki"
FACTORY = ROOT.parent.parent / "factory" / "scripts"


# ---------------------------------------------------------------------------
# Step runners

def banner(title: str) -> None:
    bar = "=" * 70
    print(f"\n{bar}\n  {title}\n{bar}")


def run(cmd: list[str], *, dry_run: bool = False, cwd: Path | None = None) -> int:
    print("  $ " + " ".join(str(c) for c in cmd))
    if dry_run:
        print("    (dry-run; skipped)")
        return 0
    result = subprocess.run(cmd, cwd=cwd or ROOT, check=False)
    return result.returncode


# ---------------------------------------------------------------------------
# Pre-flight checks

def verify_book_source(slug: str) -> bool:
    path = BOOKS_DIR / slug
    if not path.exists():
        print(f"  FAIL: no book source directory at {path}")
        print("  -> copy the book's LaTeX source into that directory first")
        return False
    print(f"  OK  : book source found at {path}")
    return True


def verify_book_registered(slug: str) -> bool:
    """Confirm the slug is in ingest_math_book.py's BOOKS dict."""
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        import ingest_math_book as ing
    finally:
        sys.path.pop(0)
    if slug not in ing.BOOKS:
        print(f"  FAIL: slug {slug!r} not in tools/ingest_math_book.py BOOKS dict")
        print("  -> add a BookSpec entry with layout + env_map")
        print(f"  known slugs: {sorted(ing.BOOKS.keys())}")
        return False
    spec = ing.BOOKS[slug]
    print(f"  OK  : registered as {spec.slug} ({spec.title}, layout={spec.layout})")
    print(f"        branch hint: {spec.branch_hint}")
    print(f"        env_map:     {spec.env_map}")
    return True


# ---------------------------------------------------------------------------
# Main steps

def snapshot_catalog() -> dict:
    """Capture a small snapshot of the current catalog for before/after diff."""
    index_file = CATALOG_DIR / "index.json"
    if not index_file.exists():
        return {"total_topics": 0, "slugs": set()}
    idx = json.loads(index_file.read_text(encoding="utf-8"))
    return {
        "total_topics": idx.get("total_topics", 0),
        "slugs": {t["slug"] for t in idx.get("topics", [])},
        "by_branch": {
            branch: info["topic_count"]
            for branch, info in idx.get("by_branch", {}).items()
        },
    }


def diff_catalog_snapshots(before: dict, after: dict) -> None:
    added = sorted(after["slugs"] - before["slugs"])
    removed = sorted(before["slugs"] - after["slugs"])
    print(f"  topics before: {before['total_topics']}")
    print(f"  topics after:  {after['total_topics']}")
    print(f"  added: {len(added)}")
    print(f"  removed: {len(removed)}")
    if added:
        preview = added[:15]
        print(f"  new topic slugs (first 15): {preview}")
        if len(added) > 15:
            print(f"    ... and {len(added) - 15} more")
    if removed:
        print(f"  REMOVED topic slugs: {removed}")
        print("  WARN: a consolidation run removed topics. Usually this means")
        print("         an aliases.yaml merge rule took effect. Verify it was intended.")
    branches_before = before.get("by_branch", {})
    branches_after = after.get("by_branch", {})
    for branch in sorted(set(branches_before) | set(branches_after)):
        b = branches_before.get(branch, 0)
        a = branches_after.get(branch, 0)
        if a != b:
            delta = a - b
            sign = "+" if delta >= 0 else ""
            print(f"  {branch}: {b} -> {a} ({sign}{delta})")


# ---------------------------------------------------------------------------
# Entry point

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="book slug registered in ingest_math_book.py")
    parser.add_argument("--dry-run", action="store_true", help="print commands without running")
    parser.add_argument("--skip-steps", default="", help="comma-separated step numbers to skip")
    args = parser.parse_args()

    skip = {int(s) for s in args.skip_steps.split(",") if s.strip().isdigit()}

    banner(f"Ingesting new book: {args.slug}")

    # Pre-flight
    if not verify_book_source(args.slug):
        return 1
    if not verify_book_registered(args.slug):
        return 1

    # Step 1: ingest -> per-chapter extractions
    if 1 not in skip:
        banner("Step 1/9: Parse LaTeX -> per-chapter JSON")
        if run(["py", "-3", str(ROOT / "tools" / "ingest_math_book.py"), "--book", args.slug],
               dry_run=args.dry_run) != 0:
            return 1

    # Step 2: snapshot pre-consolidation catalog
    before = snapshot_catalog() if not args.dry_run else {"total_topics": 0, "slugs": set()}

    # Step 3: consolidate extractions -> catalog
    if 2 not in skip:
        banner("Step 2/9: Consolidate -> canonical topic catalog")
        if run(["py", "-3", str(ROOT / "tools" / "consolidate_extractions.py")],
               dry_run=args.dry_run) != 0:
            return 1

    # Step 4: diff
    if 3 not in skip and not args.dry_run:
        banner("Step 3/9: Catalog diff")
        after = snapshot_catalog()
        diff_catalog_snapshots(before, after)

    # Step 5: generate stub pages
    if 4 not in skip:
        banner("Step 4/9: Generate stub pages for new topics")
        if run(["py", "-3", str(ROOT / "tools" / "generate_topic_stubs.py"), "--branch", "all"],
               dry_run=args.dry_run) != 0:
            return 1

    # Step 6: update branch hubs
    if 5 not in skip:
        banner("Step 5/9: Update branch hub topic listings")
        if run(["py", "-3", str(ROOT / "tools" / "update_branch_hubs.py")],
               dry_run=args.dry_run) != 0:
            return 1

    # Step 7: regenerate wiki index
    if 6 not in skip:
        banner("Step 6/9: Rebuild _index.md")
        if run(["py", "-3", str(FACTORY / "build_index.py"), str(WIKI_DIR)],
               dry_run=args.dry_run) != 0:
            return 1

    # Step 8: lint
    if 7 not in skip:
        banner("Step 7/9: Lint wiki")
        if run(["py", "-3", str(FACTORY / "lint_wiki.py"), str(WIKI_DIR)],
               dry_run=args.dry_run) != 0:
            print("  (lint reported issues; review above)")

    # Step 9: pytest
    if 8 not in skip:
        banner("Step 8/9: Run pytest (generators + copyright + snapshot + smoke)")
        if run(["py", "-3", "-m", "pytest", "generators/tests/", "-q"],
               dry_run=args.dry_run, cwd=ROOT) != 0:
            print("  (pytest failures; review above)")

    # Step 10: reminder about alias review
    if 9 not in skip:
        banner("Step 9/9: Next steps")
        print("  - Review the catalog for duplicates with existing topics.")
        print("    Open tools/aliases.yaml and add merge/rename rules if needed.")
        print("  - Re-run `py -3 tools/consolidate_extractions.py` after editing aliases.")
        print("  - Re-run `py -3 tools/generate_topic_stubs.py --branch all --force`")
        print("    ONLY for slugs affected by your aliases.yaml changes.")
        print("  - Commit the new:")
        print("    * tools/ingest_math_book.py (if you added a BOOKS entry)")
        print("    * tools/aliases.yaml  (if you added merges)")
        print("    * wiki/topics/**  (new stubs)")
        print("    * wiki/_index.md, wiki/{Branch}_Overview.md  (regenerated)")
        print("  - DO NOT commit:")
        print("    * raw/books/  (gitignored)")
        print("    * raw/extractions/  (gitignored)")
        print("    * raw/catalog/  (gitignored)")
        print()
        print("Done. Welcome to the wiki.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
