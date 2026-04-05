#!/usr/bin/env python3
"""
integrate_longfellow_johnson.py
Cross-reference Longfellow-Johnson hymns with Campbell hymns.
For overlaps: enrich existing Campbell pages with LJ source reference.
For unique LJ hymns: generate new wiki pages.

Usage: py -3 factory/scripts/integrate_longfellow_johnson.py [--dry-run]
"""

import json
import os
import re
import glob
import sys
from difflib import SequenceMatcher

WIKI_DIR = os.path.join("builds", "Hymn_Wiki", "wiki")
HYMNS_DIR = os.path.join(WIKI_DIR, "hymns")
LJ_JSON = os.path.join("builds", "Hymn_Wiki", "raw", "extracted", "longfellow_johnson_hymns.json")
CAMPBELL_JSON = os.path.join("builds", "Hymn_Wiki", "raw", "extracted", "campbell_hymns.json")

SOURCE_WIKILINK = "[[Book_of_Hymns_for_Public_and_Private_Devotion]]"
SOURCE_SHORT = "[[Book_of_Hymns_for_Public_and_Private_Devotion|A Book of Hymns]]"

SIMILARITY_THRESHOLD = 0.75


def normalize_first_line(s):
    """Normalize a first line for fuzzy matching."""
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def find_campbell_match(lj_first_line, campbell_index):
    """Find best matching Campbell hymn by first line."""
    norm_lj = normalize_first_line(lj_first_line)
    best_match = None
    best_score = 0

    for norm_campbell, campbell_data in campbell_index.items():
        score = similarity(norm_lj, norm_campbell)
        if score > best_score:
            best_score = score
            best_match = campbell_data

    if best_score >= SIMILARITY_THRESHOLD:
        return best_match, best_score
    return None, 0


def find_hymn_file(hymn_number):
    """Find the actual Campbell hymn file by number prefix."""
    pattern = os.path.join(HYMNS_DIR, f"Hymn_{hymn_number:04d}_*.md")
    matches = glob.glob(pattern)
    return matches[0] if matches else None


def enrich_campbell_hymn(filepath, lj_hymn, dry_run=False):
    """Add LJ cross-reference to an existing Campbell hymn page."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already cross-referenced
    if "Book_of_Hymns_for_Public_and_Private_Devotion" in content:
        return False

    # Add to source_refs in frontmatter
    old_refs = re.search(r'^source_refs:\s*\[(.+?)\]', content, re.MULTILINE)
    if old_refs:
        existing = old_refs.group(1)
        new_refs = f'source_refs: [{existing}, "{SOURCE_WIKILINK}"]'
        content = content.replace(old_refs.group(0), new_refs, 1)

    # Add cross-reference note in Historical Context section
    lj_note = (
        f"\n### Also in A Book of Hymns (1848)\n\n"
        f"This hymn also appears as Hymn {lj_hymn['hymn_number']} in "
        f"{SOURCE_SHORT} (1848), compiled by [[Samuel_Longfellow]] and "
        f"[[Samuel_Johnson_Hymn_Compiler|Samuel Johnson]]"
    )
    if lj_hymn["author"]:
        lj_note += f", attributed to {lj_hymn['author']}"
    if lj_hymn["modified"]:
        lj_note += " (modified by compilers)"
    lj_note += f'. Section: "{lj_hymn["section"]}".\n'

    # Insert before last section or at end of Historical Context
    hist_match = re.search(r'## Historical Context\n', content)
    if hist_match:
        # Find next ## or end
        next_section = re.search(r'\n## (?!Historical)', content[hist_match.end():])
        if next_section:
            insert_pos = hist_match.end() + next_section.start()
        else:
            insert_pos = len(content)
        content = content[:insert_pos].rstrip() + "\n" + lj_note + "\n" + content[insert_pos:]
    else:
        content = content.rstrip() + "\n\n## Historical Context\n" + lj_note

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return True


def sanitize_filename(s):
    """Create a safe filename from a string."""
    s = re.sub(r'[^\w\s]', '', s)
    words = s.split()[:6]
    return "_".join(w.capitalize() for w in words)


def generate_lj_hymn_page(lj_hymn, dry_run=False):
    """Generate a new wiki page for a unique LJ hymn."""
    num = lj_hymn["hymn_number"]
    first_line = lj_hymn["first_line"]
    title_part = sanitize_filename(first_line)
    filename = f"Hymn_LJ_{num:04d}_{title_part}.md"
    filepath = os.path.join(HYMNS_DIR, filename)

    if os.path.exists(filepath):
        return filename, False

    author = lj_hymn["author"] or "Anonymous"
    # Map meter abbreviations
    meter = lj_hymn["meter"]

    # Determine meter tag
    meter_tag = "#meter-peculiar"
    meter_lower = meter.lower().replace(" ", "")
    if "c.m" in meter_lower or "c.m" in meter_lower.replace(" ", ""):
        meter_tag = "#meter-common"
    elif "l.m" in meter_lower:
        meter_tag = "#meter-long"
    elif "s.m" in meter_lower:
        meter_tag = "#meter-short"
    elif "p.m" in meter_lower:
        meter_tag = "#meter-peculiar"
    elif "7s" in meter_lower:
        meter_tag = "#meter-sevens"
    elif "8s" in meter_lower or ("8" in meter_lower and "&" not in meter_lower):
        meter_tag = "#meter-eights"

    # Map section to theme tag
    section_theme_map = {
        "Public Worship": "#theme-worship",
        "God": "#theme-praise",
        "Jesus Christ": "#theme-devotion",
        "Remembrance of Christ": "#theme-communion",
        "Christianity and the Kingdom of Heaven": "#theme-missionary",
        "The Christian Character": "#theme-devotion",
        "The Christian Life": "#theme-pilgrimage",
        "Various Occasions": "#theme-worship",
        "Miscellaneous": "#theme-devotion",
        "Supplement": "#theme-worship",
    }
    theme_tag = section_theme_map.get(lj_hymn["section"], "#theme-devotion")

    content = f'''---
title: "LJ Hymn {num}: {first_line[:60]}"
type: hymn
aliases: ["{first_line}"]
tags: ["{meter_tag}", "{theme_tag}"]
created: 2026-04-05
updated: 2026-04-05
source_refs: ["{SOURCE_WIKILINK}"]
related: []
status: stub
confidence: high
hymn_number: {num}
first_line: "{first_line.replace('"', '\\"')}"
meter: "{meter}"
topic: "{lj_hymn['title']}"
author: "{author}"
composer: ""
tune_name: ""
scripture_refs: []
stanza_count: {lj_hymn['stanza_count']}
era: ""
collection: "Longfellow-Johnson"
---


> [[_overview|Home]] > [[Hymns_Overview|Hymns]]

# LJ Hymn {num}: {first_line}

| Field | Value |
|-------|-------|
| **Author** | {author} |
| **Meter** | {meter} |
| **Topic** | {lj_hymn['title']} |
| **Section** | {lj_hymn['section']} |
| **Stanzas** | {lj_hymn['stanza_count']} |
| **Collection** | {SOURCE_SHORT} (1848) |

## Text

> *From {SOURCE_SHORT} (1848), Hymn {num}*

```
{lj_hymn['text']}
```

## Scripture References

*No scripture reference in source.*

## Historical Context

*No individual historical commentary found in available sources. See author and concept pages for broader context.*
'''

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return filename, True


def main():
    dry_run = "--dry-run" in sys.argv

    # Load data
    with open(LJ_JSON, "r", encoding="utf-8") as f:
        lj_hymns = json.load(f)
    with open(CAMPBELL_JSON, "r", encoding="utf-8") as f:
        campbell_hymns = json.load(f)

    print(f"Loaded {len(lj_hymns)} LJ hymns, {len(campbell_hymns)} Campbell hymns")

    # Build Campbell index by normalized first line
    campbell_index = {}
    for ch in campbell_hymns:
        norm = normalize_first_line(ch["first_line"])
        campbell_index[norm] = ch

    # Process each LJ hymn
    overlaps = 0
    unique = 0
    enriched = 0
    new_pages = []

    for lj in lj_hymns:
        match, score = find_campbell_match(lj["first_line"], campbell_index)

        if match:
            overlaps += 1
            # Find the Campbell hymn file
            hymn_file = find_hymn_file(match["hymn_number"])
            if hymn_file:
                if enrich_campbell_hymn(hymn_file, lj, dry_run):
                    enriched += 1
                    if not dry_run:
                        print(f"  Enriched Campbell #{match['hymn_number']} (LJ #{lj['hymn_number']}): {lj['first_line'][:40]}... (score={score:.2f})")
        else:
            unique += 1
            filename, created = generate_lj_hymn_page(lj, dry_run)
            if created:
                new_pages.append(filename)
                if not dry_run and len(new_pages) <= 10:
                    print(f"  Created {filename}")

    print(f"\nResults:")
    print(f"  Overlapping hymns: {overlaps} (enriched {enriched} Campbell pages)")
    print(f"  Unique LJ hymns: {unique} (created {len(new_pages)} new pages)")
    print(f"  Total: {overlaps + unique}")

    if dry_run:
        print("\n[DRY RUN - no files modified]")


if __name__ == "__main__":
    main()
