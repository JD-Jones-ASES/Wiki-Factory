#!/usr/bin/env python3
"""Validate YAML frontmatter of every markdown file in a wiki directory.

Prevents the "quoted hash tag" and "cascading backslash" class of YAML
errors caught in Hymn Wiki v3 by running ``yaml.safe_load()`` on every
frontmatter block and reporting any that fail to parse.

Also validates:

- Frontmatter opens with ``---`` and closes with ``---``
- Loaded YAML is a mapping (dict), not a list or scalar
- ``type`` is one of the known page types
- ``status`` is one of stub/draft/complete
- ``tags`` is a list of strings starting with ``#``

Exits 0 on success, 1 on any failure. Paths are reported as error lines so
editors/CI can surface them.

Usage:
    py -3 factory/scripts/validate_yaml.py <wiki_dir>        # check a wiki
    py -3 factory/scripts/validate_yaml.py file1.md file2.md # check files

    # As a pre-commit hook (add to .git/hooks/pre-commit):
    #   py -3 factory/scripts/validate_yaml.py $(git diff --cached --name-only --diff-filter=ACM | grep .md)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

VALID_TYPES = {
    "entity", "concept", "source", "synthesis", "timeline", "overview",
    "hymn", "topic", "problem_type", "technique", "formula",
}
VALID_STATUSES = {"stub", "draft", "complete"}


def validate_file(path: Path) -> list[str]:
    """Return a list of error messages; empty means clean."""
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return [f"{path}: could not read: {e}"]

    if not text.strip():
        return []  # empty file is not a frontmatter issue

    m = FRONTMATTER_RE.match(text)
    if not m:
        # Files without frontmatter are allowed (system files, etc.) — skip
        # validation but note they exist. The linter has its own rules.
        return []

    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid YAML frontmatter: {e}")
        return errors

    if fm is None:
        errors.append(f"{path}: frontmatter is empty")
        return errors
    if not isinstance(fm, dict):
        errors.append(f"{path}: frontmatter is not a mapping (got {type(fm).__name__})")
        return errors

    page_type = fm.get("type")
    if page_type is not None and page_type not in VALID_TYPES:
        errors.append(f"{path}: unknown type {page_type!r} (valid: {sorted(VALID_TYPES)})")

    status = fm.get("status")
    if status is not None and status not in VALID_STATUSES:
        errors.append(f"{path}: unknown status {status!r} (valid: {sorted(VALID_STATUSES)})")

    tags = fm.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append(f"{path}: tags is not a list (got {type(tags).__name__})")
        else:
            for t in tags:
                if not isinstance(t, str):
                    errors.append(f"{path}: tag {t!r} is not a string (YAML `#tag` without quotes becomes null)")
                elif not t.startswith("#"):
                    errors.append(f"{path}: tag {t!r} must start with `#`")

    aliases = fm.get("aliases")
    if aliases is not None and not isinstance(aliases, list):
        errors.append(f"{path}: aliases must be a list, got {type(aliases).__name__}")

    return errors


def gather_files(args: list[str]) -> list[Path]:
    """Expand arguments into a list of .md files to check."""
    files: list[Path] = []
    for arg in args:
        p = Path(arg)
        if not p.exists():
            print(f"skip: not found: {arg}", file=sys.stderr)
            continue
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.suffix == ".md":
            files.append(p)
    return files


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: py -3 validate_yaml.py <wiki_dir|file.md> [...]", file=sys.stderr)
        return 2

    files = gather_files(argv)
    if not files:
        print("No .md files to validate.", file=sys.stderr)
        return 0

    all_errors: list[str] = []
    for f in files:
        all_errors.extend(validate_file(f))

    if all_errors:
        for line in all_errors:
            print(line, file=sys.stderr)
        print(
            f"\nYAML frontmatter validation FAILED: "
            f"{len(all_errors)} issue(s) in {len(files)} file(s)",
            file=sys.stderr,
        )
        return 1

    print(f"YAML frontmatter validation OK: {len(files)} file(s) clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
