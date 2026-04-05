#!/usr/bin/env python3
"""
add_related_links.py — Populate the `related` field in hymn page frontmatter.

Usage:
    py -3 factory/scripts/add_related_links.py C:/Wiki_Factory/builds/Hymn_Wiki

What it does:
1. Reads all hymn pages and extracts frontmatter (author, era, tags, hymn_number, topic).
2. Groups hymns by author — each hymn gets links to 2-3 sibling hymns (same author, ≥3 hymns).
3. Maps author short names → entity page filenames, adds entity link if the file exists.
4. Maps era values → concept page filenames, adds concept link if the file exists.
5. Maps specific tags → concept page filenames, adds concept link if the file exists.
6. Limits related list to 5-8 items; skips hymns that already have non-empty related.
7. Writes the updated frontmatter back to each file.
"""

import os
import re
import sys
import random
from collections import defaultdict


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Hard-coded author short-name → entity page stem (without .md)
AUTHOR_TO_ENTITY = {
    "Watts": "Isaac_Watts",
    "C. Wesley": "Charles_Wesley",
    "J. Wesley": "Charles_Wesley",   # fallback — no John Wesley entity
    "Newton": "John_Newton",
    "Cowper": "William_Cowper",
    "Doddridge": "Philip_Doddridge",
    "Montgomery": "James_Montgomery",
    "Toplady": "Augustus_Toplady",
    "Mrs. Steele": "Anna_Steele",
    "Steele": "Anna_Steele",
    "Addison": "Joseph_Addison",
    "Heber": "Reginald_Heber",
    "F. Lyte": "Henry_Francis_Lyte",
    "Charlotte Elliott": "Charlotte_Elliott",
    "Bonar": "Horatius_Bonar",
    "Robinson": "Robert_Robinson",
    "Medley": "Samuel_Medley",
    "Fawcett": "John_Fawcett",
    "Stennett": "Samuel_Stennett",
    "Hart": "Joseph_Hart",
    "Kenn": "Thomas_Ken",
    "Kelly": "Thomas_Kelly",
    "Kelley": "Thomas_Kelly",
    "Ray Palmer": "Ray_Palmer",
    "Palmer": "Ray_Palmer",
    "Beddome": "Benjamin_Beddome",
    "Whittier": "John_Greenleaf_Whittier",
    "Bowring": "Sir_John_Bowring",
    "S. F. Smith": "Samuel_Francis_Smith",
    "Toplady": "Augustus_Toplady",
    "Keble": "John_Keble",
    "Olivers": "Thomas_Olivers",
    "Perronet": "Edward_Perronet",
    "Pierpont": "John_Pierpont",
    "Grant": "Robert_Grant",
    "Sir Robt. Grant": "Robert_Grant",
    "Newman": "John_Henry_Newman",
    "T. Hastings": "Thomas_Hastings",
    "Hastings": "Thomas_Hastings",
    "Dwight": "Timothy_Dwight",
    "Gerhardt": "Paul_Gerhardt",
    "Joachim Neander": "Joachim_Neander",
    "Count Zinzendorf": "Count_Nikolaus_von_Zinzendorf",
    "Madame Guyon": "Madame_Guyon",
    "F. S. Key": "Francis_Scott_Key",
    "O. W. Holmes": "Oliver_Wendell_Holmes",
    "H. K. White": "Henry_Kirke_White",
    "Cennick": "John_Cennick",
    "Rippon's Coll": None,  # collection, not a person
    "Tate & Brady": None,
    "Breviary": None,
    "Ancient Hymns": None,
    "Miss A. A. Procter": "Adelaide_Anne_Procter",
    "Faber": "Frederick_William_Faber",
    "Doane": "William_H_Doane",
    "Miss H. M. Williams": "Helen_Maria_Williams",
    "S. Longfellow": "Samuel_Longfellow",
    "Bernard": "Bernard_of_Clairvaux",
    "Wordsworth": "Christopher_Wordsworth",
    "Hammond": "William_Hammond",
    "Toplady": "Augustus_Toplady",
}

# era value → concept page stem
ERA_TO_CONCEPT = {
    "18th-century": "18th_Century_Hymnody",
    "19th-century": "19th_Century_Hymnody",
    "post-reformation": "Post-Reformation_Hymnody",
    "reformation": "Reformation_Hymnody",
    "medieval": "Medieval_Hymnody",
    "early-christian": "Early_Christian_Hymnody",
    "latin": "Latin_Hymnody",
    "20th-century": "20th_Century_Hymnody",
}

# tag value → concept page stem (only theme/tradition tags, not meter)
TAG_TO_CONCEPT = {
    "#tradition-lutheran": "Lutheran_Hymnody",
    "#tradition-methodist": "Methodist_Hymnody",
    "#tradition-baptist": "Baptist_Hymnody",
    "#tradition-anglican": "Anglican_Hymnody",
    "#tradition-moravian": "Moravian_Hymnody",
    "#tradition-presbyterian": "Presbyterian_Hymnody",
    "#tradition-welsh": "Welsh_Hymnody",
    "#tradition-german": "German_Baptist_Hymnody",
    "#theme-missionary": "Missionary_Hymns",
    "#theme-revival": "Revival_Hymns",
    "#theme-consolation": "Hymns_of_Consolation",
    "#theme-funeral": "Hymns_of_Consolation",
    "#theme-patriotic": "Patriotic_Hymns",
    "#theme-children": "Sunday_School_Hymns",
    "#theme-suffering": "Hymns_of_Consolation",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Return (frontmatter_str, body_str) split at the YAML fences.
    Returns (None, text) if no frontmatter found."""
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', text, re.DOTALL)
    if m:
        return m.group(1), m.group(2)
    return None, text


def get_field(fm_str, key):
    """Extract a scalar YAML field value (string) from frontmatter text."""
    pattern = rf'^{re.escape(key)}:\s*"([^"]*)"'
    m = re.search(pattern, fm_str, re.MULTILINE)
    if m:
        return m.group(1)
    # Try unquoted
    pattern2 = rf'^{re.escape(key)}:\s*([^\[\n][^\n]*)'
    m2 = re.search(pattern2, fm_str, re.MULTILINE)
    if m2:
        return m2.group(1).strip().strip('"')
    return ""


def get_list_field(fm_str, key):
    """Extract a YAML list field as a Python list of strings.
    Handles values containing [[wikilinks]] which have nested brackets."""
    # Match key: followed by everything up to end of line (the whole list is one line)
    pattern = rf'^{re.escape(key)}:\s*(.+)$'
    m = re.search(pattern, fm_str, re.MULTILINE)
    if not m:
        return []
    line_val = m.group(1).strip()
    # Must start with [ ... ]
    if not (line_val.startswith('[') and line_val.endswith(']')):
        return []
    inner = line_val[1:-1].strip()
    if not inner:
        return []
    # Extract all double-quoted strings
    items = re.findall(r'"([^"]*)"', inner)
    return items


def set_related_field(fm_str, related_list):
    """Replace the related: [...] line in frontmatter with the new list."""
    # Format list as ["[[A]]", "[[B]]", ...]
    if related_list:
        items_str = ", ".join(f'"{item}"' for item in related_list)
        new_line = f'related: [{items_str}]'
    else:
        new_line = 'related: []'

    # Replace existing related line (handles both empty and populated)
    new_fm = re.sub(r'^related:.*$', new_line, fm_str, flags=re.MULTILINE)
    return new_fm


def file_exists_in_dir(directory, stem):
    """Check whether stem.md exists in directory (case-insensitive on Windows)."""
    path = os.path.join(directory, stem + ".md")
    return os.path.isfile(path)


def build_last_name_index(entities_dir):
    """Build a dict mapping lowercase last name → entity stem, from the entities dir."""
    index = {}
    if not os.path.isdir(entities_dir):
        return index
    for fname in os.listdir(entities_dir):
        if not fname.endswith(".md"):
            continue
        stem = fname[:-3]  # strip .md
        parts = stem.split("_")
        if parts:
            last = parts[-1].lower()
            # Only map if not already mapped (first occurrence wins)
            if last not in index:
                index[last] = stem
    return index


def resolve_entity(author, entities_dir, last_name_index):
    """Try to find an entity page for the given author string.
    Returns the wikilink stem (without .md) or None."""
    if not author:
        return None

    # 1. Hard-coded mapping
    mapped = AUTHOR_TO_ENTITY.get(author)
    if mapped is None and author in AUTHOR_TO_ENTITY:
        # Explicit None → skip
        return None
    if mapped:
        if file_exists_in_dir(entities_dir, mapped):
            return mapped
        # Try anyway — might exist under a slightly different name
        return None

    # 2. Try converting author string directly to underscore stem
    # e.g. "Charlotte Elliott" → "Charlotte_Elliott"
    direct_stem = "_".join(w for w in author.split())
    if file_exists_in_dir(entities_dir, direct_stem):
        return direct_stem

    # 3. Try last-name lookup from index
    # Take the last word of the author string as last name
    last_word = author.split()[-1].lower().rstrip(".,;")
    candidate = last_name_index.get(last_word)
    if candidate and file_exists_in_dir(entities_dir, candidate):
        return candidate

    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: py -3 add_related_links.py <build_root>")
        sys.exit(1)

    build_root = sys.argv[1]
    hymns_dir = os.path.join(build_root, "wiki", "hymns")
    entities_dir = os.path.join(build_root, "wiki", "entities")
    concepts_dir = os.path.join(build_root, "wiki", "concepts")

    if not os.path.isdir(hymns_dir):
        print(f"ERROR: hymns directory not found: {hymns_dir}")
        sys.exit(1)

    # Build last-name → entity stem index from entities dir
    last_name_index = build_last_name_index(entities_dir)

    # -----------------------------------------------------------------------
    # Pass 1: Read all hymn frontmatter into memory
    # -----------------------------------------------------------------------
    hymn_files = sorted(
        f for f in os.listdir(hymns_dir) if f.endswith(".md")
    )

    hymns = []  # list of dicts
    for fname in hymn_files:
        fpath = os.path.join(hymns_dir, fname)
        with open(fpath, encoding="utf-8") as fh:
            text = fh.read()
        fm_str, body = parse_frontmatter(text)
        if fm_str is None:
            continue

        hymn = {
            "fname": fname,
            "fpath": fpath,
            "stem": fname[:-3],      # filename without .md
            "fm_str": fm_str,
            "body": body,
            "full_text": text,
            "author": get_field(fm_str, "author"),
            "era": get_field(fm_str, "era"),
            "tags": get_list_field(fm_str, "tags"),
            "related_existing": get_list_field(fm_str, "related"),
            "topic": get_field(fm_str, "topic"),
            "hymn_number": get_field(fm_str, "hymn_number"),
        }
        hymns.append(hymn)

    print(f"Read {len(hymns)} hymn pages.")

    # -----------------------------------------------------------------------
    # Pass 2: Group hymns by author
    # -----------------------------------------------------------------------
    author_groups = defaultdict(list)
    for h in hymns:
        if h["author"]:
            author_groups[h["author"]].append(h)

    # Only keep authors with ≥3 hymns for sibling links
    prolific_authors = {
        author: group
        for author, group in author_groups.items()
        if len(group) >= 3
    }

    print(f"Authors with 3+ hymns: {len(prolific_authors)}")

    # For variety, pre-sort each group by hymn_number so we can sample
    # hymns that are "far apart" (different topics / parts of the book)
    def get_number(h):
        try:
            return int(h["hymn_number"])
        except (ValueError, TypeError):
            return 9999

    for author in prolific_authors:
        prolific_authors[author].sort(key=get_number)

    # -----------------------------------------------------------------------
    # Pass 3: Build related links for each hymn
    # -----------------------------------------------------------------------
    MAX_RELATED = 7
    MIN_RELATED = 2

    updated_count = 0
    total_links = 0

    for h in hymns:
        # Skip if already populated
        if h["related_existing"]:
            continue

        related = []

        # --- A. Author entity link ---
        entity_stem = resolve_entity(h["author"], entities_dir, last_name_index)
        if entity_stem:
            related.append(f"[[{entity_stem}]]")

        # --- B. Era concept link ---
        era = h["era"].strip().lower()
        era_concept = ERA_TO_CONCEPT.get(era)
        if era_concept and file_exists_in_dir(concepts_dir, era_concept):
            related.append(f"[[{era_concept}]]")

        # --- C. Tag concept links ---
        tags_added = set()
        for tag in h["tags"]:
            concept_stem = TAG_TO_CONCEPT.get(tag)
            if concept_stem and concept_stem not in tags_added:
                if file_exists_in_dir(concepts_dir, concept_stem):
                    related.append(f"[[{concept_stem}]]")
                    tags_added.add(concept_stem)

        # --- D. Sibling hymns by same author ---
        siblings_needed = max(0, MIN_RELATED - len(related))
        max_siblings = max(0, MAX_RELATED - len(related))
        # Aim for 2-3 siblings, but respect the cap
        target_siblings = min(3, max_siblings)

        if h["author"] in prolific_authors and target_siblings > 0:
            group = prolific_authors[h["author"]]
            # Exclude self
            candidates = [x for x in group if x["stem"] != h["stem"]]

            if candidates:
                # Pick siblings spread across the book for topic variety.
                # Use deterministic spacing: divide the list into target_siblings
                # buckets and pick the middle element of each.
                n = len(candidates)
                if n <= target_siblings:
                    chosen = candidates
                else:
                    # Evenly spaced sample
                    indices = [
                        int((i + 0.5) * n / target_siblings)
                        for i in range(target_siblings)
                    ]
                    chosen = [candidates[i] for i in indices]

                for sib in chosen:
                    link = f"[[{sib['stem']}]]"
                    if link not in related:
                        related.append(link)

        # Trim to MAX_RELATED
        related = related[:MAX_RELATED]

        if not related:
            continue

        # -----------------------------------------------------------------------
        # Pass 4: Write back to file
        # -----------------------------------------------------------------------
        new_fm = set_related_field(h["fm_str"], related)
        new_text = f"---\n{new_fm}\n---\n{h['body']}"

        with open(h["fpath"], "w", encoding="utf-8") as fh:
            fh.write(new_text)

        updated_count += 1
        total_links += len(related)

    print(f"\n--- Results ---")
    print(f"Hymn pages updated:        {updated_count}")
    print(f"Total related links added: {total_links}")
    if updated_count:
        avg = total_links / updated_count
        print(f"Average links per page:    {avg:.2f}")
    print(f"Hymns already had related: {sum(1 for h in hymns if h['related_existing'])}")
    print(f"Hymns skipped (no links):  {len(hymns) - updated_count - sum(1 for h in hymns if h['related_existing'])}")


if __name__ == "__main__":
    main()
