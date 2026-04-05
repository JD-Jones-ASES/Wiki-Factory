#!/usr/bin/env python3
"""
parse_longfellow_johnson.py
Parse 'A Book of Hymns for Public and Private Devotion' (Longfellow & Johnson, 1848)
into structured JSON for wiki integration.

Usage: py -3 factory/scripts/parse_longfellow_johnson.py
Output: builds/Hymn_Wiki/raw/extracted/longfellow_johnson_hymns.json
"""

import json
import os
import re

SOURCE_FILE = os.path.join("builds", "Hymn_Wiki", "raw", "Longfellow_Johnson.txt")
OUTPUT_FILE = os.path.join("builds", "Hymn_Wiki", "raw", "extracted", "longfellow_johnson_hymns.json")

# Section headers as they appear in the body text (centered, with Roman numerals)
# Matched by stripping and checking against these patterns
SECTION_PATTERNS = [
    (r"I\.\s*PUBLIC WORSHIP", "Public Worship"),
    (r"II\.\s*GOD", "God"),
    (r"III\.\s*JESUS CHRIST", "Jesus Christ"),
    (r"IV\.\s*REMEMBRANCE OF CHRIST", "Remembrance of Christ"),
    (r"V\.\s*CHRISTIANITY AND THE KINGDOM OF HEAVEN", "Christianity and the Kingdom of Heaven"),
    (r"VI\.\s*THE CHRISTIAN CHARACTER", "The Christian Character"),
    (r"VII\.\s*THE CHRISTIAN LIFE", "The Christian Life"),
    (r"VIII\.\s*VARIOUS OCCASIONS", "Various Occasions"),
    (r"IX\.\s*MISCELLANEOUS", "Miscellaneous"),
    (r"SUPPLEMENT\.", "Supplement"),
]


def parse_hymnal(filepath):
    """Parse the Longfellow-Johnson hymnal text file."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Find where actual hymns begin (after "HYMNS." header)
    hymn_start = text.find("I. PUBLIC WORSHIP")
    if hymn_start == -1:
        hymn_start = text.find("1.                ")
    content = text[hymn_start:]

    # Split into hymn blocks using the number pattern
    # Pattern: number followed by period, spaces, meter, optional spaces, optional author
    hymn_pattern = re.compile(
        r'^(\d+)\.\s+'           # hymn number
        r'(\S+(?:\s*(?:&|,)\s*\S+)*(?:\s+M\.?)?)' # meter (like "S. M." or "8 & 7s. M." or "P. M.")
        r'\s*'
        r'(.*?)$',               # author (rest of line, may be empty)
        re.MULTILINE
    )

    # More robust: find all hymn header lines
    lines = content.split('\n')
    hymns = []
    current_section = "Public Worship"
    current_hymn = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check for section headers (centered lines with Roman numerals)
        for pattern, section_name in SECTION_PATTERNS:
            if re.match(pattern + r'\.?$', stripped):
                current_section = section_name
                break

        # Check for hymn header line: starts with number + period
        m = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if m:
            hymn_num = int(m.group(1))
            rest = m.group(2).strip()

            # Parse meter and author from rest
            # Meter patterns: S. M., C. M., L. M., P. M., 7s. M., 8 & 7s. M.,
            # 11 & 10s. M., 8, 7 & 4s. M., etc.
            meter_match = re.match(
                r'((?:\d+(?:\s*[,&]\s*\d+)*s?\.\s*M\.?)|'  # numeric meters like "8 & 7s. M."
                r'(?:[SCLP]\.\s*M\.?)|'                      # standard S.M., C.M., L.M., P.M.
                r'(?:\d+s\.\s*M\.?))'                        # like "7s. M."
                r'\s*(.*)',
                rest
            )

            if meter_match:
                meter = meter_match.group(1).strip().rstrip('.')
                if not meter.endswith('M'):
                    meter = meter  # keep as-is
                author = meter_match.group(2).strip().rstrip('.')
            else:
                meter = rest
                author = ""

            # Clean author - remove leading asterisk (indicates modification)
            modified = False
            if author.startswith('*'):
                modified = True
                author = author[1:].strip()

            # Save previous hymn if exists
            if current_hymn:
                finalize_hymn(current_hymn)
                hymns.append(current_hymn)

            current_hymn = {
                "hymn_number": hymn_num,
                "meter": meter,
                "author": author,
                "modified": modified,
                "title": "",
                "text": "",
                "stanza_count": 0,
                "section": current_section,
                "first_line": "",
                "_text_lines": [],
            }

            # Next non-empty line(s) should be the title
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines):
                title_line = lines[j].strip()
                # Title lines are centered, not stanza numbers
                if not re.match(r'^\d+\s', title_line):
                    current_hymn["title"] = title_line
                    i = j
            i += 1
            continue

        # Accumulate text for current hymn
        if current_hymn is not None and stripped:
            # Check if this is a stanza line (starts with number or is indented text)
            if re.match(r'^\d+\s', stripped) or (line.startswith('  ') and stripped):
                current_hymn["_text_lines"].append(line.rstrip())

        i += 1

    # Save last hymn
    if current_hymn:
        finalize_hymn(current_hymn)
        hymns.append(current_hymn)

    return hymns


def finalize_hymn(hymn):
    """Finalize hymn text, extract first line and stanza count."""
    text_lines = hymn.pop("_text_lines", [])
    full_text = "\n".join(text_lines).strip()
    hymn["text"] = full_text

    # Extract first line (first non-empty line after any stanza number)
    for line in text_lines:
        stripped = line.strip()
        # Remove leading stanza number
        clean = re.sub(r'^\d+\s+', '', stripped).strip()
        if clean:
            hymn["first_line"] = clean
            break

    # Count stanzas (lines starting with a digit at the beginning)
    stanza_nums = set()
    for line in text_lines:
        m = re.match(r'^\s*(\d+)\s', line)
        if m:
            stanza_nums.add(int(m.group(1)))
    hymn["stanza_count"] = len(stanza_nums) if stanza_nums else 1


def main():
    hymns = parse_hymnal(SOURCE_FILE)

    print(f"Parsed {len(hymns)} hymns")

    # Stats
    with_author = sum(1 for h in hymns if h["author"])
    without_author = sum(1 for h in hymns if not h["author"])
    modified = sum(1 for h in hymns if h["modified"])
    sections = set(h["section"] for h in hymns)

    print(f"  With author: {with_author}")
    print(f"  Without author (anonymous): {without_author}")
    print(f"  Modified by compilers (*): {modified}")
    print(f"  Sections: {sorted(sections)}")

    # Show first 5 for verification
    print("\nFirst 5 hymns:")
    for h in hymns[:5]:
        print(f"  #{h['hymn_number']}: {h['first_line'][:50]}... [{h['meter']}] by {h['author'] or 'Anonymous'} ({h['section']})")

    # Show last 5
    print("\nLast 5 hymns:")
    for h in hymns[-5:]:
        print(f"  #{h['hymn_number']}: {h['first_line'][:50]}... [{h['meter']}] by {h['author'] or 'Anonymous'} ({h['section']})")

    # Save JSON
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(hymns, f, indent=2, ensure_ascii=False)

    print(f"\nSaved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
