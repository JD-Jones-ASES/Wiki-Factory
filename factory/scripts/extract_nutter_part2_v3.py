#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, hymns 201 through 748.
Version 3: Sequence-based OCR correction for hymn numbers.

Key insight: Hymn numbers in the file are mostly sequential. When a number
appears out of sequence, it's likely an OCR error. We correct using context.
"""

import re
import json

SOURCE_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt"
OUTPUT_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part2.json"

START_LINE = 16443
END_LINE = 55660

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

def normalize_section(raw):
    raw = re.sub(r'\s+', ' ', raw.strip().rstrip('.'))
    for pattern, name in SECTION_MAP:
        if re.search(pattern, raw, re.IGNORECASE):
            return name
    return None

def is_page_header(line_text):
    stripped = line_text.strip()
    if re.match(r'^\d{1,3}$', stripped):
        return True
    if re.search(r'ANNOTATED\s+HYMNAL', stripped):
        return True
    return False

def is_section_header(line_text):
    stripped = line_text.strip()
    if not stripped or not re.match(r'^[A-Z]', stripped):
        return None
    if len(stripped) < 8:
        return None
    upper_count = sum(1 for c in stripped if c.isupper())
    total_alpha = sum(1 for c in stripped if c.isalpha())
    if total_alpha > 0 and upper_count / total_alpha < 0.7:
        return None
    return normalize_section(stripped)

def detect_hymn_header(line_text):
    """
    Detect a hymn header line (number + meter).
    Returns (raw_number_str, meter_str) or (None, None).
    Raw number string is what appeared in the file (may be OCR'd).
    """
    stripped = line_text.strip()

    # Pattern: 2-3 alphanumeric chars + whitespace + meter-like content
    m = re.match(r'^([A-Za-z0-9]{2,3})\s{1,6}(.{3,45})$', stripped)
    if not m:
        return None, None

    prefix = m.group(1)
    rest = m.group(2).strip()

    # Rest must look like a meter specification
    # L. M., C. M., S. M., P. M., 7s, 8s, 8, 7, 8, 7, etc.
    meter_indicators = [
        r'^[CcLlSsMmPp]\.?\s*[Mm]\.?',  # C.M., L.M., S.M., P.M.
        r'^[0-9]+s',                       # 7s, 8s, 10s
        r'^[0-9]+\s*[,\.]\s*[0-9]',       # 8, 7, 8, 7 or 8.7
        r'^[CcLlSs]\.\s*[Mm]\.\s*D\.',    # C.M.D., L.M.D.
        r'^P\.\s*M\.',                      # P.M.
        r'^[0-9]+\s+[0-9]',               # 11 10
        r'^lis\.',                          # lis. (11s)
    ]
    if not any(re.match(pat, rest) for pat in meter_indicators):
        return None, None

    # Prefix must be plausibly a hymn number
    # Convert common OCR substitutions
    ocr_map = {'a': '2', 'o': '0', 'i': '1', 'l': '1', 'I': '1', 'S': '5', 'O': '0'}

    # Try to parse prefix as integer
    try:
        num = int(prefix)
        # Plausible range
        if 150 <= num <= 800:
            return prefix, rest
        return None, None
    except ValueError:
        pass

    # Try OCR correction
    corrected = ''
    for c in prefix:
        corrected += ocr_map.get(c, c)

    try:
        num = int(corrected)
        if 150 <= num <= 800:
            return prefix, rest  # Return original prefix, caller handles correction
    except ValueError:
        pass

    return None, None

def ocr_to_num(prefix):
    """Convert OCR-corrupted prefix to integer."""
    ocr_map = {'a': '2', 'o': '0', 'i': '1', 'l': '1', 'I': '1', 'S': '5', 'O': '0'}
    corrected = ''
    for c in prefix:
        corrected += ocr_map.get(c, c)
    try:
        return int(corrected)
    except ValueError:
        return None

def correct_hymn_number(raw_prefix, ocr_num, prev_num, next_nums_preview=None):
    """
    Given an OCR'd hymn number and its context, return the corrected number.
    Strategy: The number should be prev_num + 1 (mostly sequential).
    If the OCR'd number is within reasonable range of expected, use it.
    Otherwise try to correct it.
    """
    if ocr_num is None:
        return prev_num + 1 if prev_num else None

    expected = prev_num + 1 if prev_num else None

    if expected and abs(ocr_num - expected) <= 3:
        # Close enough, trust OCR
        return ocr_num

    if expected and ocr_num != expected:
        # OCR error - try to see if the number could be corrected
        # Common OCR errors: 2→a, 2→3, 0→O, 1→i
        # If expected is in range [prev+1, prev+5], use expected
        if expected and ocr_num == expected + 100:
            # "30X" for "20X" - leading 3 instead of 2
            corrected_str = str(expected)
            try:
                return int(corrected_str)
            except:
                pass

        # If clearly sequential, return expected
        if expected:
            return expected

    return ocr_num

def read_file_range(filepath, start_line, end_line):
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
    Split file lines into hymn blocks with OCR-corrected numbers.
    """
    # First pass: collect all hymn header positions with raw numbers
    raw_headers = []  # (line_idx, raw_prefix, ocr_num, meter, section_at_time)
    current_section = "Hymns on the Holy Scriptures"

    for idx, (line_num, line_text) in enumerate(lines):
        if is_page_header(line_text):
            continue
        sec = is_section_header(line_text)
        if sec:
            current_section = sec
            continue
        raw_prefix, meter = detect_hymn_header(line_text)
        if raw_prefix:
            ocr_num = ocr_to_num(raw_prefix)
            raw_headers.append((idx, line_num, raw_prefix, ocr_num, meter, current_section))

    # Second pass: correct hymn numbers using sequence
    corrected_headers = []
    prev_corrected = 200  # We start just before 201

    for i, (idx, line_num, raw_prefix, ocr_num, meter, section) in enumerate(raw_headers):
        if ocr_num is None:
            corrected_num = prev_corrected + 1
        elif ocr_num <= 150:
            # Too small, likely a page number or other artifact
            continue
        elif ocr_num > 800:
            # Too large
            continue
        else:
            # Apply sequence correction
            # Expected should be around prev_corrected + 1 (allow gaps of up to 15 for missing hymns)
            expected = prev_corrected + 1

            if abs(ocr_num - expected) <= 15:
                # Within tolerance, trust OCR
                corrected_num = ocr_num
            elif ocr_num > expected + 15 and ocr_num < expected + 120:
                # Probably an OCR error adding 100 to the number
                # e.g., "330" for "230", "347" for "247"
                candidate = ocr_num - 100
                if abs(candidate - expected) <= 15:
                    corrected_num = candidate
                else:
                    # Try other corrections
                    corrected_num = ocr_num  # Accept as-is, might be a real gap
            elif ocr_num < expected - 15:
                # Going backwards - OCR error
                # e.g., file has 421 then shows "033" - skip or use expected
                if ocr_num < 200:
                    continue  # Skip - not a hymn number
                corrected_num = ocr_num  # Could be a legitimate lower number
            else:
                corrected_num = ocr_num

        prev_corrected = corrected_num
        corrected_headers.append((idx, line_num, corrected_num, meter, section))

    # Third pass: build blocks
    blocks = []
    for i, (idx, line_num, hymn_num, meter, section) in enumerate(corrected_headers):
        # Find end of this block (start of next block)
        if i + 1 < len(corrected_headers):
            next_idx = corrected_headers[i+1][0]
        else:
            next_idx = len(lines)

        # Collect lines for this block (excluding the header line itself)
        block_lines = []
        for j in range(idx + 1, next_idx):
            if j < len(lines):
                lnum, ltext = lines[j]
                if not is_page_header(ltext) and not is_section_header(ltext):
                    block_lines.append(ltext)

        blocks.append({
            'hymn_number': hymn_num,
            'meter': meter,
            'section': section,
            'start_line': line_num,
            'raw_text': '\n'.join(block_lines),
        })

    return blocks

def find_author_and_annotation(lines_list):
    """
    Find author name and start of annotation text.
    Returns (author_str, annotation_start_idx).
    """
    author_patterns = [
        # Standard: "John Newton." or "Charles Wesley,"
        r'^((?:Tr\.\s+(?:from\s+\w+\s+)?by\s+)?[A-Z][a-zA-Z\-]+\.?\s+[A-Z][a-zA-Z\-]+\.?\s*(?:[A-Z][a-zA-Z\-]+\.?)?\s*(?:,?\s*(?:[A-Z]\.)+)?\s*[.,]?\s*)$',
        # "Author Unknown."
        r'^(Author\s+Unknown\.?|Unknown\.?|Anonymous\.?)$',
        # "Tr. from German by William Williams."
        r'^(Tr\.\s+from\s+\w+\s+by\s+[A-Z][a-zA-Z\s\.]+[.,]?)$',
        # Name with comma suffix: "John Newton, D.D."
        r'^([A-Z][a-zA-Z\-]+\s+[A-Z][a-zA-Z\.\s\-]+,\s*(?:D\.D\.|LL\.D\.|Jr\.|Rev\.)\s*)$',
        # Just a last name with title: "Watts."
        r'^([A-Z][a-z]{3,15}\.)\s*$',
        # Name with "f," OCR artifact: "Charles Wesleyf,"
        r'^([A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+[,f]+\s*)$',
    ]

    for i, line in enumerate(lines_list):
        stripped = line.strip()
        if not stripped or len(stripped) < 4:
            continue
        # Don't look in first 2 lines (those are hymn stanza text)
        if i < 2:
            continue
        # Don't look past line 40 (too deep into annotation)
        if i > 40:
            break
        for pat in author_patterns:
            m = re.match(pat, stripped)
            if m:
                author = m.group(1).strip().rstrip('.,f')
                return author, i + 1

    return "", 0

def extract_first_hymn_line(lines_list):
    """Extract the first line of hymn text."""
    for line in lines_list[:15]:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip OCR artifacts that are page numbers
        if re.match(r'^\d{1,3}$', stripped):
            continue
        # Skip stanza numbers (just a number)
        if re.match(r'^\d+$', stripped):
            continue
        # Remove stanza number prefix "2 " "3 "
        stripped = re.sub(r'^\d+\s+', '', stripped)
        # Clean up OCR spacing
        stripped = re.sub(r'\s{2,}', ' ', stripped)
        if len(stripped) > 5 and not re.match(r'^[0-9\s]+$', stripped):
            return stripped
    return ""

def clean_text(text):
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def extract_hymn_data(block):
    raw = block['raw_text']
    lines = raw.split('\n')

    # Find author line and annotation start
    author, annot_start = find_author_and_annotation(lines)

    if annot_start > 0:
        stanza_lines = lines[:annot_start - 1]
        annotation_lines = lines[annot_start:]
    else:
        # Fallback: look for prose transition
        stanza_lines = lines[:10]
        annotation_lines = lines[10:]
        # Better fallback: find first long mixed-case line
        for i, line in enumerate(lines):
            stripped = line.strip()
            if len(stripped) > 80 and sum(1 for c in stripped if c.islower()) > 20:
                stanza_lines = lines[:i]
                annotation_lines = lines[i:]
                break

    first_line = extract_first_hymn_line(stanza_lines)
    annotation_text = '\n'.join(annotation_lines)
    annotation_clean = re.sub(r'\s+', ' ', annotation_text).strip()

    # Composition date
    composition_date = ""
    year_matches = re.findall(r'\b(1[4-9]\d\d)\b', annotation_clean)
    if year_matches:
        composition_date = year_matches[0]

    # First published
    first_published = ""
    pub_patterns = [
        r'[Ff]irst\s+(?:published|appeared?|printed)\s+in\s+([^.;]{5,100})',
        r'[Pp]ublished\s+in\s+([^.;]{5,100})',
        r'[Ff]rom\s+((?:the\s+)?(?:[A-Z][a-zA-Z]+(?:\s+[A-Za-z]+){1,8})(?:,\s*\d{4})?)',
        r'[Aa]ppeared?\s+in\s+([^.;]{5,80})',
        r'[Ii]n\s+((?:[A-Z][a-zA-Z]+(?:\s+[A-Za-z]+){1,6}),?\s*\d{4})',
    ]
    for pat in pub_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            pub = clean_text(m.group(1).rstrip('.;,'))
            if 5 < len(pub) < 120:
                first_published = pub
                break

    # Scripture basis
    scripture_basis = ""
    scripture_patterns = [
        r'[Bb]ased\s+(?:on|upon)\s+(?:[Pp]salm\s+\w+[\w\s.:\-,]+|[A-Z][a-z]+\.?\s*[xivXIV\d]+[\s.:\d,-]*)',
        r'[Ff]ounded\s+(?:on|upon)\s+([A-Z][a-z]+\.?\s*[xivXIV\d]+[\s.:\d,-]*)',
    ]
    for pat in scripture_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            scripture_basis = clean_text(m.group(0))[:100]
            break
    if not scripture_basis:
        # Parenthetical scripture reference
        m = re.search(r'\(([A-Z][a-z]+\.?\s*[xivXIV\d]+[\s.:\d,-]+)\)', annotation_clean)
        if m:
            scripture_basis = clean_text(m.group(1))

    # Original stanza count
    original_stanzas = None
    stanza_patterns = [
        r'original\s+(?:has|contains?|consisted?\s+of|is\s+(?:made\s+up\s+of|composed\s+of))\s+(\w+)\s+stanzas?',
        r'(\w+)\s+stanzas?\s+in\s+the\s+original',
        r'contains?\s+(\w+)\s+stanzas?\s+(?:and|in)',
    ]
    num_words = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
                'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
                'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
                'twenty':20,'twenty-four':24,'twenty-eight':28,'twenty-five':25,
                'twenty-six':26,'twenty-seven':27,'thirty':30,'thirty-two':32}

    for pat in stanza_patterns:
        m = re.search(pat, annotation_clean, re.IGNORECASE)
        if m:
            word = m.group(1).lower()
            if word.isdigit():
                original_stanzas = int(word)
            elif word in num_words:
                original_stanzas = num_words[word]
            break

    # Composition story
    composition_story = ""
    if annotation_clean:
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(])', annotation_clean)
        story_parts = []
        char_count = 0
        for sent in sentences:
            sent_clean = clean_text(sent)
            if len(sent_clean) < 15:
                continue
            if re.match(r'^\d+\s+[A-Z]', sent_clean):
                continue
            story_parts.append(sent_clean)
            char_count += len(sent_clean)
            if len(story_parts) >= 3 or char_count >= 500:
                break
        composition_story = ' '.join(story_parts)
        if len(composition_story) > 800:
            composition_story = composition_story[:800]

    # Textual notes
    textual_notes = ""
    textual_patterns = [
        r'((?:[Tt]wo|[Tt]hree|[Oo]ne|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Tt]en|\d+)\s+stanzas?\s+(?:are|have\s+been|were|is)\s+omitted[^.]{0,200}\.)',
        r'([Tt]he\s+original\s+has\s+\w+\s+stanzas?[^.]{0,200}\.)',
        r'([Cc]hanges?\s+have\s+been\s+made[^.]{0,200}\.)',
        r'([Aa]ltered?\s+by[^.]{0,200}\.)',
        r'([Vv]erses?\s+\w[\w,\s]+(?:are\s+given|used|omitted)[^.]{0,150}\.)',
    ]
    for pat in textual_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            textual_notes = clean_text(m.group(1))[:400]
            break

    # Anecdotes
    anecdotes = ""
    anec_patterns = [
        r'([Aa]t\s+(?:the|a|his|her)\s+(?:time|death|funeral|service|meeting|close)[^.]{20,350}\.)',
        r'([Oo]n\s+one\s+occasion[^.]{20,300}\.)',
        r'([Ii]t\s+is\s+(?:said|reported|told)\s+that[^.]{20,300}\.)',
        r'([Aa]\s+(?:remarkable|notable|touching)\s+(?:story|incident|account)[^.]{20,300}\.)',
        r'([Ww]hile\s+(?:lying|kneeling|dying|sitting|standing)[^.]{20,250}\.)',
    ]
    for pat in anec_patterns:
        m = re.search(pat, annotation_clean)
        if m:
            anecdotes = clean_text(m.group(1))[:400]
            break

    # Tune name/composer
    tune_name = ""
    tune_composer = ""
    tune_match = re.search(r'(?:[Tt]une|[Ss]et\s+to\s+music\s+by|[Mm]usic\s+(?:by|composed\s+by))\s+([A-Z][^.;,]{2,60})', annotation_clean)
    if tune_match:
        tune_name = clean_text(tune_match.group(1))[:80]

    # Critical assessment
    critical_assessment = ""
    crit_patterns = [
        r'((?:[Oo]ne\s+of\s+the\s+(?:finest|greatest|best|noblest)|[Rr]anks?\s+(?:with|among)\s+the\s+(?:first|best|greatest)|[Uu]niversally\s+(?:sung|loved|known)|[Jj]ulian\s+(?:says?|remarks?))[^.]{0,300}\.)',
        r'("(?:[Ii]t\s+ranks?|[Ii]t\s+is\s+one\s+of)[^"]{0,200}")',
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
        "stanzas_in_hymnal": None,
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

    # Sort by hymn number, deduplicate by taking first occurrence
    hymn_data.sort(key=lambda x: x['nutter_hymn_number'])
    seen = set()
    deduped = []
    for h in hymn_data:
        n = h['nutter_hymn_number']
        if n not in seen:
            seen.add(n)
            deduped.append(h)

    hymn_data = deduped

    # Section distribution
    sections = {}
    for h in hymn_data:
        s = h['topic_section']
        sections[s] = sections.get(s, 0) + 1

    print(f"\nExtracted {len(hymn_data)} unique hymns")
    print("\nSection distribution:")
    for s, count in sorted(sections.items()):
        print(f"  {s}: {count}")

    if hymn_data:
        nums = sorted(h['nutter_hymn_number'] for h in hymn_data)
        print(f"\nHymn numbers: {nums[0]} to {nums[-1]}")
        expected_set = set(range(201, 749))
        found_set = set(nums) - {200}
        missing = sorted(expected_set - found_set)
        if missing:
            print(f"Potentially missing: {missing[:50]}")

        print(f"\nSample entries:")
        for h in hymn_data[:3]:
            print(f"  #{h['nutter_hymn_number']}: '{h['first_line'][:50]}' by {h['author']}")
        print(f"  ...")
        for h in hymn_data[-3:]:
            print(f"  #{h['nutter_hymn_number']}: '{h['first_line'][:50]}' by {h['author']}")

    print(f"\nWriting to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(hymn_data, f, indent=2, ensure_ascii=False)

    print(f"Done! {len(hymn_data)} hymns written.")

if __name__ == '__main__':
    main()
