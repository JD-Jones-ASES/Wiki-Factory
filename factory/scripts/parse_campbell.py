"""
Parse campbell.txt into structured JSON.

Extracts all 1,324 hymns with:
  - hymn_number, meter, topic, scripture_ref, first_line, stanzas, stanza_count

Also parses the first-line index to extract author attributions.

Usage: py -3 factory/scripts/parse_campbell.py <campbell.txt> <output.json>
"""
import sys
import re
import json


def parse_first_line_index(lines, start_idx):
    """Parse the first-line index at the end of the file to get author attributions.

    Format: '  first line text,                  _Author Name._ 123'
    Returns dict mapping hymn_number (int) -> author (str)
    """
    authors = {}
    # Pattern: first line text, possibly with commas, then _Author._ number
    # The author is between underscores: _Author Name._
    pat = re.compile(r'_([^_]+)\._\s+(\d+)\s*$')

    for i in range(start_idx, len(lines)):
        line = lines[i]
        m = pat.search(line)
        if m:
            author = m.group(1).strip()
            num = int(m.group(2))
            authors[num] = author

    return authors


def find_first_line_index_start(lines):
    """Find where the alphabetical first-line index begins."""
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == 'INDEX OF FIRST LINES.' or stripped == 'ALPHABETICAL INDEX.' or stripped == 'INDEX.':
            return i
    # Fallback: look for the pattern after CONTENTS and INDEX OF SUBJECTS
    # The first-line index typically starts with single letters as headers (A, B, C...)
    # and lines matching the author pattern
    in_contents = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if 'INDEX OF SUBJECTS' in stripped:
            in_contents = True
        if in_contents and re.match(r'^\s+[A-Z]\s*$', line):
            # Check if next non-blank lines look like index entries
            for j in range(i+1, min(i+10, len(lines))):
                if re.search(r'_[^_]+\._\s+\d+', lines[j]):
                    return i
    return None


def parse_hymns(text):
    """Parse the hymn body (before the CONTENTS section)."""
    lines = text.split('\n')

    # Find where hymns end (CONTENTS section)
    contents_line = None
    for i, line in enumerate(lines):
        if line.strip() == 'CONTENTS.':
            contents_line = i
            break

    if contents_line is None:
        print("WARNING: Could not find CONTENTS section, parsing all lines", file=sys.stderr)
        hymn_lines = lines
        index_lines = []
    else:
        hymn_lines = lines[:contents_line]
        index_lines = lines[contents_line:]

    # Parse author attributions from the first-line index
    # The index is in the latter part of the file
    idx_start = find_first_line_index_start(lines)
    if idx_start:
        authors = parse_first_line_index(lines, idx_start)
        print(f"Parsed {len(authors)} author attributions from index", file=sys.stderr)
    else:
        authors = {}
        print("WARNING: Could not find first-line index", file=sys.stderr)

    # Pattern for hymn start: number at left margin, meter at right
    # Examples:
    #   "1                                                                L. M."
    #   "10                                                               C. M."
    #   "326                                                           L. P. M."
    #   "614                                                                 7s."
    hymn_start_pat = re.compile(
        r'^(\d+)\s{5,}(.+?)\s*$'
    )

    # Section header pattern (ALL CAPS centered text)
    section_header_pat = re.compile(r'^\s{10,}[A-Z][A-Z\s,;:\-—\.\'&]+\.\s*$')

    hymns = []
    current_section = ""
    i = 0

    # Skip to the first hymn
    while i < len(hymn_lines):
        m = hymn_start_pat.match(hymn_lines[i])
        if m and m.group(1) == '1':
            break
        # Check for section headers before first hymn
        if section_header_pat.match(hymn_lines[i]):
            current_section = hymn_lines[i].strip().rstrip('.')
        i += 1

    while i < len(hymn_lines):
        line = hymn_lines[i]

        # Check for section header
        if section_header_pat.match(line):
            candidate = line.strip().rstrip('.')
            # Don't treat short lines or stanza lines as sections
            if len(candidate) > 3 and not candidate.isdigit():
                current_section = candidate
            i += 1
            continue

        # Check for hymn start
        m = hymn_start_pat.match(line)
        if m:
            hymn_num = int(m.group(1))
            meter = m.group(2).strip().rstrip('.')

            i += 1

            # Read topic line(s)
            topic_lines = []
            scripture_ref = ""

            while i < len(hymn_lines) and hymn_lines[i].strip() == '':
                i += 1

            # Topic is indented text before the hymn body
            while i < len(hymn_lines):
                stripped = hymn_lines[i].strip()
                if stripped == '':
                    break
                # Check if this looks like a scripture reference
                if re.match(r'^(Psalm|Gen\.|Ex\.|Lev\.|Num\.|Deut\.|Josh\.|Judg\.|Ruth|1 Sam\.|2 Sam\.|1 Kings|2 Kings|1 Chron\.|2 Chron\.|Ezra|Neh\.|Esth\.|Job|Prov\.|Eccl\.|Song|Isa\.|Jer\.|Lam\.|Ezek\.|Dan\.|Hos\.|Joel|Amos|Obad\.|Jonah|Mic\.|Nah\.|Hab\.|Zeph\.|Hag\.|Zech\.|Mal\.|Matt\.|Mark|Luke|John|Acts|Rom\.|1 Cor\.|2 Cor\.|Gal\.|Eph\.|Phil\.|Col\.|1 Thes\.|2 Thes\.|1 Tim\.|2 Tim\.|Tit\.|Philem\.|Heb\.|Jas\.|1 Pet\.|2 Pet\.|1 John|2 John|3 John|Jude|Rev\.)', stripped):
                    scripture_ref = stripped
                elif re.match(r'^\d+\s+(Tim|Cor|Sam|Kings|Chron|Thes|Pet|John)', stripped):
                    scripture_ref = stripped
                else:
                    topic_lines.append(stripped)
                i += 1

            topic = ' '.join(topic_lines).strip()

            # Skip blank lines before stanzas
            while i < len(hymn_lines) and hymn_lines[i].strip() == '':
                i += 1

            # Read stanzas until next hymn number or section header or EOF
            stanza_lines = []
            while i < len(hymn_lines):
                # Check if this is the start of the next hymn
                next_m = hymn_start_pat.match(hymn_lines[i])
                if next_m:
                    next_num = int(next_m.group(1))
                    # Verify it's a reasonable next hymn number
                    if next_num > hymn_num and next_num <= hymn_num + 5:
                        break
                    # Could be a large jump for a new section
                    if next_num > hymn_num:
                        break

                # Check for section header
                if section_header_pat.match(hymn_lines[i]):
                    candidate = hymn_lines[i].strip().rstrip('.')
                    if len(candidate) > 3 and not candidate.isdigit():
                        break

                stanza_lines.append(hymn_lines[i])
                i += 1

            # Parse stanzas
            stanza_text = '\n'.join(stanza_lines).strip()

            # Count stanzas: look for stanza numbers at left margin
            # First stanza has no number, subsequent have "  2 ...", "  3 ..." etc.
            stanza_nums = re.findall(r'^\s{0,2}(\d+)\s+\S', stanza_text, re.MULTILINE)
            if stanza_nums:
                stanza_count = max(int(n) for n in stanza_nums)
            else:
                stanza_count = 1

            # Extract first line
            first_line = ""
            for sl in stanza_text.split('\n'):
                sl_stripped = sl.strip()
                if sl_stripped and not sl_stripped.isdigit():
                    first_line = sl_stripped
                    break

            # Clean up first line (remove trailing punctuation for matching)
            first_line_clean = first_line.rstrip(',;:!.')

            # Get author from index
            author = authors.get(hymn_num, "")

            hymn = {
                "hymn_number": hymn_num,
                "meter": meter,
                "topic": topic,
                "scripture_ref": scripture_ref,
                "first_line": first_line,
                "author": author,
                "stanza_count": stanza_count,
                "section": current_section,
                "text": stanza_text
            }

            hymns.append(hymn)
        else:
            i += 1

    return hymns


def main():
    if len(sys.argv) != 3:
        print("Usage: py -3 parse_campbell.py <campbell.txt> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    hymns = parse_hymns(text)

    print(f"Extracted {len(hymns)} hymns", file=sys.stderr)

    # Validate
    expected = 1324
    if len(hymns) != expected:
        print(f"WARNING: Expected {expected} hymns but got {len(hymns)}", file=sys.stderr)
        # Show which numbers are missing
        found_nums = {h['hymn_number'] for h in hymns}
        missing = [n for n in range(1, expected + 1) if n not in found_nums]
        if missing:
            print(f"Missing hymn numbers: {missing[:20]}{'...' if len(missing) > 20 else ''}", file=sys.stderr)
        # Show any duplicates
        from collections import Counter
        num_counts = Counter(h['hymn_number'] for h in hymns)
        dupes = {n: c for n, c in num_counts.items() if c > 1}
        if dupes:
            print(f"Duplicate hymn numbers: {dupes}", file=sys.stderr)

    # Stats
    with_author = sum(1 for h in hymns if h['author'])
    with_scripture = sum(1 for h in hymns if h['scripture_ref'])
    print(f"  With author attribution: {with_author}", file=sys.stderr)
    print(f"  With scripture reference: {with_scripture}", file=sys.stderr)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(hymns, f, indent=2, ensure_ascii=False)

    print(f"Output written to {output_path}", file=sys.stderr)


if __name__ == '__main__':
    main()
