#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, hymns 201 through end (748).
Lines approximately 16443 to 55660 in the raw file.
Output: builds/Hymn_Wiki/wiki/_nutter_hymn_data_part2.json
"""

import re
import json
import sys

SOURCE_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt"
OUTPUT_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part2.json"

# Line range for part 2 (hymns 201 onwards)
START_LINE = 16443   # hymn 201 entry
END_LINE = 55660     # after hymn 748 (last benediction)

# Section headings - we'll track them as we parse
SECTION_HEADINGS = {
    16169: "Hymns on the Holy Scriptures",
    # Additional sections will be tracked dynamically
}

def clean_text(text):
    """Clean up OCR artifacts and extra whitespace."""
    if not text:
        return ""
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Fix common OCR errors in names
    text = text.replace('  ', ' ')
    return text

def read_file_section(filepath, start_line, end_line):
    """Read specific line range from file (1-indexed)."""
    lines = []
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for i, line in enumerate(f, 1):
            if i < start_line:
                continue
            if i > end_line:
                break
            lines.append((i, line.rstrip('\n')))
    return lines

def is_page_header(line_text):
    """Detect OCR page headers to ignore."""
    stripped = line_text.strip()
    # Page numbers (just digits)
    if re.match(r'^\d{1,3}$', stripped):
        return True
    # "ANNOTATED HYMNAL." headers
    if 'ANNOTATED  HYMNAL' in stripped or 'ANNOTATED HYMNAL' in stripped:
        return True
    return False

def is_hymn_number_line(line_text):
    """
    Detect lines that start a new hymn entry.
    Format: "NNN  METER" where NNN is 3-digit number and METER is like "L. M.", "C. M.", "7s", etc.
    OCR sometimes garbles the number (e.g., "aoi" for 201).
    """
    stripped = line_text.strip()
    # Standard pattern: digits followed by meter
    m = re.match(r'^(\d{2,3})\s{1,4}([0-9A-Za-z.,\s]+M\.?|P\.\s*M\.?|[0-9,\s]+[sS][\s,]|[0-9,\s]+\.?\s*[0-9,\s]+\.?)', stripped)
    if m:
        num = int(m.group(1))
        if 201 <= num <= 748:
            return num, m.group(0)
    # Some entries have OCR mangled numbers but recognizable meter
    # Check for "aoi", "sol", etc followed by meter - skip these as too error-prone
    return None, None

def looks_like_section_header(line_text):
    """Detect section header lines."""
    stripped = line_text.strip()
    section_patterns = [
        r'^HYMNS\s+ON\s+THE\s+',
        r'^HYMNS\s+ON\s+TL?IME',
        r'^SPECIAL\s+SUBJECTS',
        r'^DOXOLOGIES$',
        r'^CHANTS\s+AND',
    ]
    for pat in section_patterns:
        if re.match(pat, stripped, re.IGNORECASE):
            return True
    return False

def extract_author_from_block(text_block):
    """Extract author name from annotation block."""
    # Author lines typically appear right after the hymn stanzas
    # They look like "First Last." or "First Last, D.D." or "Tr. by First Last."
    lines = text_block.split('\n')
    for i, line in enumerate(lines[:8]):  # Check first 8 lines
        stripped = line.strip()
        if not stripped:
            continue
        # Author line patterns
        if re.match(r'^(Tr\.\s+)?[A-Z][a-z]+\s+[A-Z]\.?\s+[A-Z][a-zA-Z]+\.?\s*$', stripped):
            return stripped
        if re.match(r'^[A-Z][a-z]+\s+[A-Z][a-zA-Z]+,?\s*(D\.|LL\.|Jr\.|Rev\.)?.*$', stripped):
            # Check it's not a sentence (too long or has lowercase at start)
            words = stripped.split()
            if len(words) <= 6 and not stripped[0].islower():
                return stripped
    return ""

def parse_hymn_entries(lines):
    """
    Parse lines into hymn entries.
    Returns list of (hymn_number, start_line_idx, lines_list) tuples.
    """
    entries = []
    current_hymn = None
    current_start = None
    current_lines = []
    current_section = "Hymns on the Holy Scriptures"

    i = 0
    while i < len(lines):
        line_num, line_text = lines[i]

        # Skip page headers
        if is_page_header(line_text):
            i += 1
            continue

        # Check for section headers
        if looks_like_section_header(line_text):
            current_section = line_text.strip()
            # Try to get next line for continuation
            if i + 1 < len(lines) and lines[i+1][1].strip() and not is_page_header(lines[i+1][1]):
                next_line = lines[i+1][1].strip()
                if next_line and not re.match(r'^\d', next_line):
                    current_section = current_section + ' ' + next_line
            i += 1
            continue

        # Check for hymn number line
        hymn_num, _ = is_hymn_number_line(line_text)
        if hymn_num:
            # Save previous hymn
            if current_hymn is not None:
                entries.append({
                    'hymn_number': current_hymn,
                    'start_line': current_start,
                    'section': current_section,
                    'raw_lines': current_lines[:]
                })
            current_hymn = hymn_num
            current_start = line_num
            current_lines = [(line_num, line_text)]
        elif current_hymn is not None:
            current_lines.append((line_num, line_text))

        i += 1

    # Save last hymn
    if current_hymn is not None:
        entries.append({
            'hymn_number': current_hymn,
            'start_line': current_start,
            'section': current_section,
            'raw_lines': current_lines[:]
        })

    return entries

def extract_annotation_data(entry):
    """
    Extract structured data from a hymn entry's raw lines.
    """
    lines = [text for _, text in entry['raw_lines']]
    full_text = '\n'.join(lines)

    hymn_num = entry['hymn_number']

    # --- First line of hymn (first substantial line after the number+meter line) ---
    first_line = ""
    meter = ""

    # Parse the header line
    header = lines[0].strip()
    meter_match = re.match(r'^(\d{2,3})\s+(.*)', header)
    if meter_match:
        meter = meter_match.group(2).strip()

    # Find the first actual hymn text line
    # Hymn text lines: capitalized, not OCR headers, not annotation
    for i in range(1, min(10, len(lines))):
        line = lines[i].strip()
        if not line:
            continue
        if is_page_header(lines[i]):
            continue
        # First hymn stanza line is often all caps for first word
        if line and (line[0].isupper() or line[0] == 'O' or line[0] == '"'):
            # Check it's not an author line (too short or all caps)
            if len(line) > 5 and not re.match(r'^[A-Z\s\.]+$', line):
                first_line = line
                # Clean up OCR spacing
                first_line = re.sub(r'\s{2,}', ' ', first_line).strip()
                break

    # --- Author ---
    author = ""
    # Author typically appears after the last stanza and before annotation text
    # Look for lines that match author pattern
    annotation_start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Author line pattern: "Firstname Lastname." or "Tr. from X by Y."
        if re.match(r'^(Tr\.\s+(from\s+\w+\s+)?by\s+)?[A-Z][a-zA-Z\.\-]+\s+[A-Z][a-zA-Z\.\-]+[\.,]?\s*(D\.\s*D\.|LL\.\s*D\.|Jr\.?)?\s*$', stripped):
            if i > 2:  # Not the very first lines
                author = stripped.rstrip('.')
                annotation_start = i + 1
                break
        # Multiple names: "Firstname Lastname and Firstname Lastname"
        if re.match(r'^[A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+\s+and\s+[A-Z][a-zA-Z]+\.\s*$', stripped):
            if i > 2:
                author = stripped.rstrip('.')
                annotation_start = i + 1
                break

    # Get annotation text (everything after author line)
    annotation_lines = lines[annotation_start:] if annotation_start > 0 else []
    annotation_text = '\n'.join(annotation_lines)

    # --- Composition date ---
    composition_date = ""
    date_match = re.search(r'\b(1[4-9]\d\d|20[01]\d)\b', annotation_text)
    if date_match:
        composition_date = date_match.group(1)

    # --- First published ---
    first_published = ""
    pub_match = re.search(r'(?:published\s+in|appeared\s+in|From|first\s+appeared\s+in|printed\s+in)\s+([^.;]{5,80}[.;])', annotation_text, re.IGNORECASE)
    if pub_match:
        first_published = clean_text(pub_match.group(1).rstrip('.;'))

    # --- Scripture basis ---
    scripture_basis = ""
    scripture_match = re.search(r'(?:based\s+(?:on|upon)|from)\s+([A-Z][a-z]+\.?\s+[xivXIV\d]+[.:\s\d-]+)', annotation_text, re.IGNORECASE)
    if scripture_match:
        scripture_basis = clean_text(scripture_match.group(1))
    # Also look for parenthetical Bible refs
    scripture_match2 = re.search(r'\(([A-Z][a-z]+\.?\s+[xivXIV\d]+[\d.,:\s-]*)\)', annotation_text)
    if scripture_match2 and not scripture_basis:
        scripture_basis = clean_text(scripture_match2.group(1))

    # --- Stanza counts ---
    original_stanzas = None
    stanzas_in_hymnal = None
    stanza_match = re.search(r'original\s+(?:has|contained?)\s+(\w+)\s+stanzas?', annotation_text, re.IGNORECASE)
    if stanza_match:
        word = stanza_match.group(1)
        num_words = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
                    'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
                    'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
        if word.isdigit():
            original_stanzas = int(word)
        elif word.lower() in num_words:
            original_stanzas = num_words[word.lower()]

    # --- Composition story (summarize annotation) ---
    composition_story = ""
    if annotation_text:
        # Take first 2-3 sentences of annotation
        sentences = re.split(r'(?<=[.!?])\s+', annotation_text.strip())
        story_sentences = []
        char_count = 0
        for s in sentences:
            s = clean_text(s)
            if not s or len(s) < 10:
                continue
            # Skip lines that are just quoted stanzas (start with number + stanza)
            if re.match(r'^\d+\s+[A-Z]', s):
                continue
            story_sentences.append(s)
            char_count += len(s)
            if len(story_sentences) >= 3 or char_count > 400:
                break
        composition_story = ' '.join(story_sentences)
        composition_story = composition_story[:600]  # Limit length

    # --- Textual notes ---
    textual_notes = ""
    textual_match = re.search(r'((?:omitted?|altered?|changed?|stanzas?\s+(?:are|were|have\s+been)|two\s+stanzas?|one\s+stanza|verses?\s+\w+\s+(?:and|are|were))[^.]{0,200}\.)', annotation_text, re.IGNORECASE)
    if textual_match:
        textual_notes = clean_text(textual_match.group(1))

    # --- Anecdotes ---
    anecdotes = ""
    # Look for story-telling phrases
    anec_match = re.search(r'((?:story|told|said|reported|occasion|when|once|incident|remarkable|famous)[^.]{20,300}\.)', annotation_text, re.IGNORECASE)
    if anec_match:
        anecdotes = clean_text(anec_match.group(1))

    # --- Tune info ---
    tune_name = ""
    tune_composer = ""
    tune_match = re.search(r'(?:tune|set to\s+(?:music\s+)?(?:by|of)|composed\s+by)\s+([A-Z][^.;]{3,50})', annotation_text, re.IGNORECASE)
    if tune_match:
        tune_name = clean_text(tune_match.group(1))

    # --- Critical assessment ---
    critical_assessment = ""
    crit_match = re.search(r'(?:one\s+of\s+the\s+(?:finest|greatest|best|most\s+\w+)|ranks\s+among|universally\s+(?:sung|loved|known)|great\s+(?:hymn|song))[^.]{0,300}\.', annotation_text, re.IGNORECASE)
    if crit_match:
        critical_assessment = clean_text(crit_match.group(0))

    # Clean up section name
    section = clean_text(entry['section'])
    # Normalize section names
    if 'HOLY SCRIPTURES' in section.upper() or 'SCRIPTURE' in section.upper():
        section = "Hymns on the Holy Scriptures"
    elif 'CHRISTIAN LIFE' in section.upper():
        section = "Hymns on the Christian Life"
    elif 'TIME AND ETERNITY' in section.upper() or 'TLME' in section.upper():
        section = "Hymns on Time and Eternity"
    elif 'SPECIAL SUBJECTS' in section.upper():
        section = "Special Subjects and Occasions"
    elif 'DOXOLOG' in section.upper():
        section = "Doxologies"
    elif 'CHANTS' in section.upper():
        section = "Chants and Occasional Pieces"

    return {
        "nutter_hymn_number": hymn_num,
        "first_line": first_line,
        "author": clean_text(author),
        "meter": clean_text(meter),
        "composition_date": composition_date,
        "first_published": first_published,
        "original_stanzas": original_stanzas,
        "stanzas_in_hymnal": stanzas_in_hymnal,
        "scripture_basis": scripture_basis,
        "composition_story": composition_story,
        "textual_notes": textual_notes,
        "anecdotes": anecdotes,
        "tune_name": tune_name,
        "tune_composer": tune_composer,
        "critical_assessment": critical_assessment,
        "topic_section": section,
    }

def main():
    print(f"Reading {SOURCE_FILE}...")
    print(f"Processing lines {START_LINE} to {END_LINE}...")

    lines = read_file_section(SOURCE_FILE, START_LINE, END_LINE)
    print(f"Read {len(lines)} lines.")

    print("Parsing hymn entries...")
    entries = parse_hymn_entries(lines)
    print(f"Found {len(entries)} hymn entries.")

    print("Extracting annotation data...")
    hymn_data = []
    for entry in entries:
        data = extract_annotation_data(entry)
        hymn_data.append(data)

    # Sort by hymn number
    hymn_data.sort(key=lambda x: x['nutter_hymn_number'])

    # Report
    print(f"\nExtracted {len(hymn_data)} hymns")

    # Check section distribution
    sections = {}
    for h in hymn_data:
        s = h['topic_section']
        sections[s] = sections.get(s, 0) + 1
    print("\nSection distribution:")
    for s, count in sorted(sections.items()):
        print(f"  {s}: {count}")

    # Sample output
    if hymn_data:
        print(f"\nFirst hymn: #{hymn_data[0]['nutter_hymn_number']} - {hymn_data[0]['first_line'][:50]}")
        print(f"Last hymn: #{hymn_data[-1]['nutter_hymn_number']} - {hymn_data[-1]['first_line'][:50]}")

    print(f"\nWriting to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(hymn_data, f, indent=2, ensure_ascii=False)

    print(f"Done! {len(hymn_data)} hymns written.")
    return hymn_data

if __name__ == '__main__':
    main()
