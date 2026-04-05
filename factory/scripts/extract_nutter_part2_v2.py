#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, hymns 201 through 748.
Lines approximately 16443 to 55660 in the raw file.
Output: builds/Hymn_Wiki/wiki/_nutter_hymn_data_part2.json

Version 2: Improved section tracking and annotation extraction.
"""

import re
import json

SOURCE_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt"
OUTPUT_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part2.json"

# Line range for part 2 (hymns 201 onwards)
START_LINE = 16443   # hymn 201 entry
END_LINE = 55660     # after hymn 748 (last benediction)

# Known section header patterns → normalized names
SECTION_MAP = [
    (r'HYMNS\s+ON\s+THE\s+HOLY\s+SCRIPTURES?', "Hymns on the Holy Scriptures"),
    (r'INSTITUTIONS\s+O[FP]\s+CHRISTIANITY', "Institutions of Christianity"),
    (r'HYMNS\s+O[NX]+\s+THE\s+GOSPEL\s+CALL', "Hymns on the Gospel Call"),
    (r'HYMNS\s+O[NX]+\s+THE\s+CHRISTIAN\s+LIFE', "Hymns on the Christian Life"),
    (r'HYMNS\s+ON\s+TL?IME\s+AND\s+ETERNITY', "Hymns on Time and Eternity"),
    (r'HYMNS\s+ON\s+TIME', "Hymns on Time and Eternity"),
    (r'AND\s+ETERNITY$', "Hymns on Time and Eternity"),
    (r'SPECIAL\s+SUBJECTS\s+AND\s+OCCASIONS?', "Special Subjects and Occasions"),
    (r'^DOXOLOGIES?$', "Doxologies"),
    (r'CHANTS\s+AND\s+OCCASIONAL\s+PIECES', "Chants and Occasional Pieces"),
]

def clean_text(text):
    """Clean up OCR artifacts and extra whitespace."""
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_section(raw):
    """Normalize a section header string."""
    raw = re.sub(r'\s+', ' ', raw.strip().rstrip('.'))
    for pattern, name in SECTION_MAP:
        if re.search(pattern, raw, re.IGNORECASE):
            return name
    return None

def is_page_header(line_text):
    """Detect OCR page headers to ignore."""
    stripped = line_text.strip()
    if re.match(r'^\d{1,3}$', stripped):
        return True
    if re.search(r'ANNOTATED\s+HYMNAL', stripped):
        return True
    return False

def is_section_header(line_text):
    """Returns normalized section name if line is a section header, else None."""
    stripped = line_text.strip()
    # Must be mostly caps, multi-word
    if not stripped or not re.match(r'^[A-Z]', stripped):
        return None
    if len(stripped) < 8:
        return None
    # Check if it looks like a header (mostly uppercase)
    upper_count = sum(1 for c in stripped if c.isupper())
    total_alpha = sum(1 for c in stripped if c.isalpha())
    if total_alpha > 0 and upper_count / total_alpha < 0.7:
        return None
    return normalize_section(stripped)

def detect_hymn_number(line_text):
    """
    Detect lines that start a new hymn entry.
    Returns (hymn_num, meter) or (None, None).
    Handles OCR variants like "aoi" for "201".
    """
    stripped = line_text.strip()

    # Standard pattern: 2-3 digit number, whitespace, meter info
    # Meter can be: L. M., C. M., S. M., 7s, 8s, P.M., etc.
    m = re.match(r'^(\d{2,3})\s{1,6}(.{3,40})$', stripped)
    if m:
        try:
            num = int(m.group(1))
            if 200 <= num <= 748:
                return num, m.group(2).strip()
        except ValueError:
            pass

    # Some OCR-mangled patterns for specific numbers
    # e.g. "aoi c. M." = "201 c. M."
    ocr_fixes = [
        (r'^aoi\s+(.+)$', 201),
        (r'^sol\s+(.+)$', 201),
        (r'^20i\s+(.+)$', 201),
        (r'^aoa\s+(.+)$', 203),
        (r'^a05\s+(.+)$', 205),
        (r'^aig\s+(.+)$', 219),
        (r'^aao\s+(.+)$', 220),
        (r'^aai\s+(.+)$', 221),
        (r'^aaa\s+(.+)$', 222),
        (r'^aas\s+(.+)$', 223),
        (r'^ao4\s+(.+)$', 204),
        (r'^ao6\s+(.+)$', 206),
        (r'^4a3\s+(.+)$', 423),
        (r'^433\s+(.+)$', 433),
    ]
    for pattern, num in ocr_fixes:
        m = re.match(pattern, stripped, re.IGNORECASE)
        if m:
            return num, m.group(1).strip()

    return None, None

def read_file_range(filepath, start_line, end_line):
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

def split_into_hymn_blocks(lines):
    """
    Split file lines into hymn blocks.
    Returns list of dicts: {hymn_number, meter, section, start_line, raw_text}
    """
    blocks = []
    current_num = None
    current_meter = ""
    current_section = "Hymns on the Holy Scriptures"  # default at start of our range
    current_lines = []
    current_start = None

    for line_num, line_text in lines:
        # Skip running page headers
        if is_page_header(line_text):
            continue

        # Check for section header
        sec = is_section_header(line_text)
        if sec:
            current_section = sec
            continue

        # Check for hymn number line
        hymn_num, meter = detect_hymn_number(line_text)
        if hymn_num:
            # Save previous block
            if current_num is not None:
                blocks.append({
                    'hymn_number': current_num,
                    'meter': current_meter,
                    'section': current_section,
                    'start_line': current_start,
                    'raw_text': '\n'.join(current_lines),
                })
            current_num = hymn_num
            current_meter = meter
            current_start = line_num
            current_lines = []
        elif current_num is not None:
            current_lines.append(line_text)

    # Save last block
    if current_num is not None:
        blocks.append({
            'hymn_number': current_num,
            'meter': current_meter,
            'section': current_section,
            'start_line': current_start,
            'raw_text': '\n'.join(current_lines),
        })

    return blocks

def find_annotation_start(lines_list):
    """
    Find the line index where the annotation (prose) begins.
    Before that: hymn stanzas. After: prose annotation.
    The author name line typically marks the transition.
    """
    # Author name patterns
    author_patterns = [
        # "John Newton." or "Charles Wesley," etc.
        r'^((?:Tr\.\s+(?:from\s+\w+\s+)?by\s+)?[A-Z][a-zA-Z\-]+\.?\s+[A-Z][a-zA-Z\-]+\.?\s*(?:[A-Z][a-zA-Z\-]+\.?)?\s*(?:,?\s*(?:D\.D\.|LL\.D\.|Jr\.|Rev\.))?\s*[.,]?\s*)$',
        # "Author Unknown." or "Unknown."
        r'^(Author\s+Unknown\.?|Unknown\.?)$',
        # "Tr. from German by ..."
        r'^(Tr\.\s+from\s+\w+\s+by\s+[A-Z][a-zA-Z\s\.]+)$',
    ]

    for i, line in enumerate(lines_list):
        stripped = line.strip()
        if not stripped:
            continue
        for pat in author_patterns:
            if re.match(pat, stripped):
                return stripped.rstrip('.,'), i + 1

    return "", 0

def extract_hymn_data(block):
    """Extract structured annotation data from a hymn block."""
    raw = block['raw_text']
    lines = raw.split('\n')

    # Find first line of hymn text (skip leading blank lines)
    first_line = ""
    hymn_text_lines = []
    annotation_lines = []

    # Find author line (marks end of hymn stanzas)
    author, annot_start_idx = find_annotation_start(lines)

    if annot_start_idx > 0:
        hymn_text_lines = lines[:annot_start_idx - 1]
        annotation_lines = lines[annot_start_idx:]
    else:
        # Try to find annotation by looking for prose paragraph pattern
        # Prose starts with a capital letter followed by lowercase (not a stanza)
        in_stanza = True
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped:
                continue
            # A prose line: long, mixed case, doesn't start like a stanza number
            if in_stanza and len(stripped) > 60 and not re.match(r'^\d\s+[A-Z]', stripped):
                if sum(1 for c in stripped if c.islower()) > len(stripped) * 0.3:
                    annot_start_idx = i
                    in_stanza = False
                    break
        hymn_text_lines = lines[:annot_start_idx] if annot_start_idx > 0 else lines[:10]
        annotation_lines = lines[annot_start_idx:] if annot_start_idx > 0 else []

    # Extract first line of hymn
    for line in hymn_text_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r'^\d+\s+[A-Z]', stripped):
            # It's a stanza number + text
            stripped = re.sub(r'^\d+\s+', '', stripped)
        if len(stripped) > 5 and not re.match(r'^[0-9]+$', stripped):
            first_line = re.sub(r'\s{2,}', ' ', stripped).strip()
            break

    annotation_text = '\n'.join(annotation_lines)
    annotation_clean = re.sub(r'\s+', ' ', annotation_text).strip()

    # --- Extract fields from annotation ---

    # Composition date (look for 4-digit years)
    composition_date = ""
    year_matches = re.findall(r'\b(1[4-9]\d\d)\b', annotation_clean)
    if year_matches:
        composition_date = year_matches[0]

    # First published
    first_published = ""
    pub_patterns = [
        r'[Ff]irst\s+(?:published|appeared|printed)\s+in\s+([^.;]{5,80})',
        r'[Pp]ublished\s+in\s+([^.;]{5,80})',
        r'[Ff]rom\s+((?:the\s+)?[A-Z][^.;]{5,80})',
        r'[Aa]ppeared\s+in\s+([^.;]{5,80})',
        r'[Pp]rinted\s+in\s+([^.;]{5,80})',
    ]
    for pat in pub_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            pub = clean_text(m.group(1).rstrip('.;,'))
            if len(pub) < 120:
                first_published = pub
                break

    # Scripture basis
    scripture_basis = ""
    # Look for explicit scripture references
    scripture_patterns = [
        r'[Bb]ased\s+(?:on|upon)\s+([A-Z][a-z]+\.?\s*(?:i{1,3}|iv|v{1,3}|vi{1,3}|ix|x{1,4}|xi{1,3}|xiv|xv{1,3}|xix|xx{1,3})?\s*\d+[\s.:\d,-]+)',
        r'\(([A-Z][a-z]+\.?\s*(?:i{1,3}|iv|v{1,3}|vi{1,3}|ix|x{1,4}|xi{1,3}|xiv|xv{1,3}|xix|xx{1,3})?\s*\d+[\s.:\d,-]+)\)',
        r'(?:founded\s+upon|from)\s+([A-Z][a-z]+\.?\s*\w+\.?\s*\d+)',
    ]
    for pat in scripture_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            scripture_basis = clean_text(m.group(1))
            break

    # Original stanza count
    original_stanzas = None
    stanza_match = re.search(r'original\s+(?:has|contains?|contained?|consisted?\s+of)\s+(\w+)\s+stanzas?', annotation_clean, re.IGNORECASE)
    if not stanza_match:
        stanza_match = re.search(r'(\w+)\s+stanzas?\s+in\s+the\s+original', annotation_clean, re.IGNORECASE)
    if stanza_match:
        word = stanza_match.group(1).lower()
        num_words = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
                    'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
                    'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
                    'twenty':20,'twenty-four':24,'twenty-eight':28,'twenty-five':25,'thirty':30}
        if word.isdigit():
            original_stanzas = int(word)
        elif word in num_words:
            original_stanzas = num_words[word]

    # Stanzas in hymnal (omitted stanzas give us clues)
    stanzas_in_hymnal = None

    # Composition story - first 3 sentences of annotation
    composition_story = ""
    if annotation_clean:
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', annotation_clean)
        story_parts = []
        char_count = 0
        for sent in sentences:
            sent = clean_text(sent)
            if len(sent) < 15:
                continue
            # Skip if it starts with a stanza number
            if re.match(r'^\d+\s+[A-Z]', sent):
                continue
            # Skip quoted stanza lines
            if re.match(r'^[A-Z][a-zA-Z,\s]+!?\s*$', sent) and len(sent) < 50:
                continue
            story_parts.append(sent)
            char_count += len(sent)
            if len(story_parts) >= 3 or char_count >= 500:
                break
        composition_story = ' '.join(story_parts)
        if len(composition_story) > 800:
            composition_story = composition_story[:800]

    # Textual notes (alterations, omissions)
    textual_notes = ""
    textual_patterns = [
        r'([Tt]wo stanzas? (?:are|have been) omitted[^.]{0,200}\.)',
        r'([Oo]ne stanza (?:is|has been) omitted[^.]{0,200}\.)',
        r'([Tt]hree stanzas? (?:are|have been) omitted[^.]{0,200}\.)',
        r'([Ss]tanzas? (?:\w+(?:,\s*\w+)*)\s+(?:are|were|have been) omitted[^.]{0,200}\.)',
        r'([Tt]he (?:last|first|following) stanza[^.]{0,200}(?:omitted|altered|changed)[^.]{0,100}\.)',
        r'([Cc]hanges?\s+have\s+been\s+made[^.]{0,200}\.)',
        r'([Aa]ltered?\s+(?:from|by)[^.]{0,200}\.)',
        r'([Vv]erse[s]?\s+\w+\s+(?:and|are|were|have)[^.]{0,150}\.)',
    ]
    for pat in textual_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            textual_notes = clean_text(m.group(1))
            break

    # Anecdotes (stories about the hymn)
    anecdotes = ""
    anec_patterns = [
        r'([Aa]t\s+(?:the|a|his|her)\s+\w+[^.]{20,350}\.)',
        r'([Ww]hen\s+(?:the|a|he|she|this)[^.]{20,350}\.)',
        r'([Tt]he\s+story\s+(?:is|goes|of)[^.]{20,350}\.)',
        r'([Ii]t\s+is\s+(?:said|reported|stated|told)[^.]{20,300}\.)',
        r'([Oo]n\s+one\s+occasion[^.]{20,300}\.)',
        r'([Aa]\s+(?:remarkable|notable|famous|touching)\s+incident[^.]{20,300}\.)',
        r'([Oo]n\s+the\s+occasion[^.]{20,300}\.)',
    ]
    for pat in anec_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            anec = clean_text(m.group(1))
            if len(anec) > 20:
                anecdotes = anec[:400]
                break

    # Tune info
    tune_name = ""
    tune_composer = ""
    tune_match = re.search(r'(?:tune|set\s+to\s+(?:music\s+)?(?:by|of)|music\s+(?:by|composed\s+by))\s+([A-Z][^.;]{3,60})', annotation_clean, re.IGNORECASE)
    if tune_match:
        tune_name = clean_text(tune_match.group(1))[:80]

    # Critical assessment
    critical_assessment = ""
    crit_patterns = [
        r'((?:[Oo]ne\s+of\s+the\s+(?:finest|greatest|best|noblest|most\s+\w+)|ranks\s+(?:with|among)|universally\s+(?:sung|loved|known)|great\s+hymn|magnificent)[^.]{0,300}\.)',
        r'((?:[Jj]ulian|[Jj]ulian\s+remarks?|[Ii]t\s+(?:is|has\s+been)\s+(?:said|praised))[^.]{0,300}\.)',
    ]
    for pat in crit_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            critical_assessment = clean_text(m.group(1))[:400]
            break

    return {
        "nutter_hymn_number": block['hymn_number'],
        "first_line": first_line,
        "author": clean_text(author),
        "meter": clean_text(block['meter']),
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
        "topic_section": block['section'],
    }

def main():
    print(f"Reading {SOURCE_FILE}...")
    print(f"Processing lines {START_LINE} to {END_LINE}...")

    lines = read_file_range(SOURCE_FILE, START_LINE, END_LINE)
    print(f"Read {len(lines)} lines.")

    print("Splitting into hymn blocks...")
    blocks = split_into_hymn_blocks(lines)
    print(f"Found {len(blocks)} hymn blocks.")

    print("Extracting annotation data...")
    hymn_data = []
    for block in blocks:
        data = extract_hymn_data(block)
        hymn_data.append(data)

    # Sort by hymn number
    hymn_data.sort(key=lambda x: x['nutter_hymn_number'])

    # Report section distribution
    sections = {}
    for h in hymn_data:
        s = h['topic_section']
        sections[s] = sections.get(s, 0) + 1

    print(f"\nExtracted {len(hymn_data)} hymns")
    print("\nSection distribution:")
    for s, count in sorted(sections.items()):
        print(f"  {s}: {count}")

    # Report hymn number range
    if hymn_data:
        nums = sorted(h['nutter_hymn_number'] for h in hymn_data)
        print(f"\nHymn numbers: {nums[0]} to {nums[-1]}")

        # Find gaps
        expected = set(range(nums[0], nums[-1]+1))
        found = set(nums)
        missing = sorted(expected - found)
        if missing:
            print(f"Missing hymn numbers: {missing[:30]}{'...' if len(missing) > 30 else ''}")
        print(f"Total hymns: {len(nums)}, unique numbers: {len(found)}")

        # Sample
        print(f"\nFirst: #{hymn_data[0]['nutter_hymn_number']} - {hymn_data[0]['first_line'][:50]}")
        print(f"Last:  #{hymn_data[-1]['nutter_hymn_number']} - {hymn_data[-1]['first_line'][:50]}")

    print(f"\nWriting to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(hymn_data, f, indent=2, ensure_ascii=False)

    print(f"Done! {len(hymn_data)} hymns written.")
    return hymn_data

if __name__ == '__main__':
    main()
