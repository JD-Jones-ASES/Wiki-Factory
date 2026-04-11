#!/usr/bin/env python3
"""Propagate standardized test tags to topic frontmatter.

Reads tools/test_prep_mapping.yaml and walks wiki/topics/**/*.md. For each
file whose lowercase stem is a key in the mapping, ensures every listed test
tag is present (with the leading `#`) in the YAML `tags:` array. Idempotent:
running twice makes no changes on the second run.

Surgical editing: rewrites ONLY the `tags:` line(s), preserving the rest of
the frontmatter byte-for-byte. This minimizes diff noise.

Usage (from builds/Math_Wiki/):
    py -3 tools/apply_test_tags.py               # apply changes
    py -3 tools/apply_test_tags.py --dry-run     # preview without writing
    py -3 tools/apply_test_tags.py --check       # exit 1 if any file would change

Follows factory/scripts/lint_wiki.py patterns for frontmatter parsing.
After applying, the caller should run:
    py -3 ../../factory/scripts/validate_yaml.py wiki/
    py -3 ../../factory/scripts/lint_wiki.py wiki/
as safety checks.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
MAPPING_FILE = ROOT / "tools" / "test_prep_mapping.yaml"

VALID_TEST_TAGS = {"test-sat", "test-psat", "test-act", "test-clt"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Match a `tags:` entry that either lives on one line (flow-style list)
# or spans multiple lines (block-style list). For the single-line flow
# form we can do a clean surgical replacement; the block-style form is
# rare in this project but we handle it by normalizing to a flow list.
TAGS_SINGLE_LINE_RE = re.compile(r"^(tags:\s*)(\[.*?\])\s*$", re.MULTILINE)


def load_mapping() -> dict[str, list[str]]:
    """Parse test_prep_mapping.yaml into {slug: ['#test-sat', ...]}."""
    raw = yaml.safe_load(MAPPING_FILE.read_text(encoding="utf-8"))
    mappings = raw.get("mappings", {}) or {}
    out: dict[str, list[str]] = {}
    for slug, tests in mappings.items():
        if tests is None:
            continue
        clean = [f"#{t}" for t in tests if t in VALID_TEST_TAGS]
        bad = [t for t in tests if t not in VALID_TEST_TAGS]
        if bad:
            print(f"WARN: mapping entry {slug} has invalid tag(s): {bad}")
        if clean:
            out[slug.lower()] = clean
    return out


def parse_tags_from_frontmatter(fm_yaml: str) -> list[str] | None:
    """Return the current tags list (with '#') from a parsed frontmatter YAML
    string, or None if there is no tags field or it cannot be parsed."""
    try:
        fm = yaml.safe_load(fm_yaml) or {}
    except yaml.YAMLError:
        return None
    tags = fm.get("tags")
    if tags is None:
        return []
    if not isinstance(tags, list):
        return None
    return [str(t) for t in tags]


def render_flow_tags(tags: list[str]) -> str:
    """Render a tag list as a YAML flow-style array matching the project convention:
        tags: ["#branch-algebra-1", "#topic-linear", "#test-sat"]
    """
    inner = ", ".join(f'"{t}"' for t in tags)
    return f"tags: [{inner}]"


def update_file(
    md_path: Path,
    desired_tags: list[str],
    dry_run: bool,
) -> tuple[bool, str]:
    """Returns (changed, message)."""
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return False, f"[skip] no frontmatter: {md_path.name}"

    fm_yaml = m.group(1)
    current = parse_tags_from_frontmatter(fm_yaml)
    if current is None:
        return False, f"[skip] could not parse tags: {md_path.name}"

    missing = [t for t in desired_tags if t not in current]
    if not missing:
        return False, ""

    new_tags = current + missing

    # Surgical single-line replacement. Works for the project's flow-style
    # convention (the overwhelming majority of files).
    tags_match = TAGS_SINGLE_LINE_RE.search(fm_yaml)
    if tags_match:
        new_tags_line = render_flow_tags(new_tags)
        new_fm = (
            fm_yaml[: tags_match.start()]
            + new_tags_line
            + fm_yaml[tags_match.end():]
        )
        new_text = f"---\n{new_fm}\n---\n" + text[m.end():]
    else:
        # Fallback: rebuild the frontmatter via yaml.safe_dump. This reformats
        # the whole frontmatter block, so the diff will be larger. We only hit
        # this for files that use block-style tag lists.
        try:
            fm_obj = yaml.safe_load(fm_yaml) or {}
        except yaml.YAMLError as exc:
            return False, f"[skip] yaml reparse failed ({exc}): {md_path.name}"
        fm_obj["tags"] = new_tags
        new_fm = yaml.safe_dump(
            fm_obj,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=200,
        ).rstrip("\n")
        new_text = f"---\n{new_fm}\n---\n" + text[m.end():]

    rel = md_path.relative_to(ROOT)
    verb = "[would-edit]" if dry_run else "[ok]"
    msg = f"{verb} {rel}  +{len(missing)}: {missing}"

    if not dry_run:
        md_path.write_text(new_text, encoding="utf-8")

    return True, msg


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="preview without writing files")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any file would change (implies --dry-run)")
    ap.add_argument("--verbose", action="store_true",
                    help="also log skipped files")
    args = ap.parse_args()

    dry = args.dry_run or args.check

    if not MAPPING_FILE.exists():
        print(f"error: mapping file not found: {MAPPING_FILE}", file=sys.stderr)
        return 2

    mapping = load_mapping()
    print(f"Loaded mapping: {len(mapping)} topic(s)")

    changed_count = 0
    seen_slugs: set[str] = set()
    for md in sorted(TOPICS_DIR.rglob("*.md")):
        slug = md.stem.lower()
        if slug not in mapping:
            continue
        seen_slugs.add(slug)
        did_change, msg = update_file(md, mapping[slug], dry_run=dry)
        if did_change:
            changed_count += 1
            print(msg)
        elif args.verbose and msg:
            print(msg)

    unmapped_to_file = sorted(set(mapping.keys()) - seen_slugs)
    if unmapped_to_file:
        print(f"\nWARN: {len(unmapped_to_file)} mapping entr(ies) did not match "
              f"any topic file (likely typos or Wave D topics not yet created):")
        for slug in unmapped_to_file[:20]:
            print(f"  {slug}")
        if len(unmapped_to_file) > 20:
            print(f"  ... and {len(unmapped_to_file) - 20} more")

    verb = "would be updated" if dry else "updated"
    print(f"\n{changed_count} topic file(s) {verb}")

    if args.check and changed_count:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
