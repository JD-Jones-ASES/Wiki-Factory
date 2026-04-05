#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, hymns 201 through 748.
Final version: Corrects OCR number errors using sequence analysis.

The dominant OCR error pattern is a leading "3" being inserted where
the first digit should be "2" (and sometimes the reverse), causing
numbers like 203→303, 247→347, 250→350, 260→360, etc.

Strategy: Collect all header lines in file order. For each ±100 or ±200
jump followed by a jump back, correct the anomalous numbers.
"""

import re
import json

SOURCE_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt"
OUTPUT_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part2.json"

START_LINE = 16443
END_LINE = 55660

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

def ocr_correct(s):
    """Apply basic OCR character corrections."""
    table = str.maketrans('aoilSOB', '2011508')
    return s.translate(table)

def detect_hymn_header(line_text):
    """
    Detect hymn header lines.
    Returns (ocr_corrected_num, raw_prefix, meter_str) or (None, None, None).
    """
    stripped = line_text.strip()
    m = re.match(r'^([A-Za-z0-9]{2,3})\s{1,6}(.{3,45})$', stripped)
    if not m:
        return None, None, None

    prefix = m.group(1)
    rest = m.group(2).strip()

    # Meter patterns
    meter_patterns = [
        r'^[CcLlSsMmPp]\.?\s*[Mm]\.?',  # C.M., L.M., S.M., P.M.
        r'^[0-9]+\s*s',                   # 7s, 8s, 10s
        r'^[0-9]+\s*[,\.]\s*[0-9]',      # 8, 7, 8, 7
        r'^P\.\s*M\.',                     # P.M.
        r'^[0-9]{2}\s+[0-9]',            # 11 10
        r'^lis\.?',                        # lis. (11s)
    ]
    if not any(re.match(pat, rest) for pat in meter_patterns):
        return None, None, None

    # Try to parse prefix as integer (with OCR correction)
    corrected = ocr_correct(prefix)
    try:
        num = int(corrected)
        if 150 <= num <= 800:
            return num, prefix, rest
    except ValueError:
        pass

    return None, None, None

def correct_sequence(raw_nums):
    """
    Given a list of (line_idx, ocr_num, ...) tuples in file order,
    correct OCR errors in hymn numbers.

    Key observation: when a number jumps by exactly +100 and later jumps
    back by -100, the intervening numbers have a leading 3 instead of 2
    (or leading 4 instead of 3, etc.)

    Returns list of corrected numbers.
    """
    if not raw_nums:
        return []

    n = len(raw_nums)
    corrected = [x[2] for x in raw_nums]  # Start with ocr numbers (index 2 = ocr_num)

    # Sliding window correction: look for ±100 anomalies
    for i in range(1, n - 1):
        prev = corrected[i-1]
        curr = corrected[i]
        next_val = corrected[i+1] if i+1 < n else None

        # Check for +100 jump (curr is 100 more than expected)
        if curr - prev >= 90 and curr - prev <= 115:
            # This is suspicious. Check if next value goes back down.
            if next_val and next_val < curr:
                # Likely OCR error: leading digit shifted
                candidate = curr - 100
                if candidate > 0 and abs(candidate - prev) <= 15:
                    corrected[i] = candidate

        # Check for -100 jump after a previous +100 correction
        elif curr < prev - 80 and curr > prev - 115:
            candidate = curr + 100
            if abs(candidate - prev) <= 15:
                corrected[i] = candidate

        # Check for ±200 anomaly
        elif abs(curr - prev) >= 190 and abs(curr - prev) <= 215:
            if next_val:
                # Try -200 correction
                candidate = curr - 200 if curr - prev > 0 else curr + 200
                if abs(candidate - prev) <= 15:
                    corrected[i] = candidate

    # Second pass: handle remaining anomalies
    for i in range(1, n):
        prev = corrected[i-1]
        curr = corrected[i]
        # If current is way off from previous sequence (more than 60 away)
        # AND the raw number with a leading digit swap corrects it:
        if abs(curr - prev) > 20 and abs(curr - prev) not in range(90, 115):
            # Try -60, +60 (for 371→312 type errors)
            for adj in [-60, 60, -20, 20]:
                candidate = curr + adj
                if abs(candidate - prev) <= 10 and candidate > 0:
                    corrected[i] = candidate
                    break

    return corrected

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

def build_hymn_blocks(lines):
    """
    Build hymn blocks with OCR-corrected numbers.
    Returns list of block dicts.
    """
    current_section = "Hymns on the Holy Scriptures"

    # First pass: collect all hymn header candidates
    raw_headers = []  # (idx_in_lines, file_line_num, ocr_num, raw_prefix, meter, section)
    section_at = {}   # idx -> section name

    for idx, (file_line_num, line_text) in enumerate(lines):
        if is_page_header(line_text):
            continue
        sec = is_section_header(line_text)
        if sec:
            current_section = sec
            section_at[idx] = sec
            continue
        ocr_num, raw_prefix, meter = detect_hymn_header(line_text)
        if ocr_num is not None:
            raw_headers.append((idx, file_line_num, ocr_num, raw_prefix, meter, current_section))

    print(f"  Raw headers detected: {len(raw_headers)}")

    # Second pass: correct sequence
    corrected_nums = correct_sequence(raw_headers)

    # Build corrected header list
    corrected_headers = []
    for i, (idx, file_line_num, ocr_num, raw_prefix, meter, section) in enumerate(raw_headers):
        corrected = corrected_nums[i]
        if corrected < 200 or corrected > 750:
            continue  # Skip out-of-range
        corrected_headers.append((idx, file_line_num, corrected, meter, section))

    print(f"  After correction: {len(corrected_headers)} headers in range 200-750")

    # Third pass: deduplicate (keep first occurrence of each number)
    seen_nums = set()
    dedup_headers = []
    for header in corrected_headers:
        num = header[2]
        if num not in seen_nums:
            seen_nums.add(num)
            dedup_headers.append(header)
    corrected_headers = dedup_headers

    print(f"  After dedup: {len(corrected_headers)} unique headers")

    # Build blocks
    blocks = []
    for i, (idx, file_line_num, hymn_num, meter, section) in enumerate(corrected_headers):
        # Lines for this block: from after header to start of next header
        if i + 1 < len(corrected_headers):
            next_idx = corrected_headers[i+1][0]
        else:
            next_idx = len(lines)

        block_lines = []
        for j in range(idx + 1, next_idx):
            if j < len(lines):
                lnum, ltext = lines[j]
                if not is_page_header(ltext):
                    sec = is_section_header(ltext)
                    if not sec:
                        block_lines.append(ltext)

        blocks.append({
            'hymn_number': hymn_num,
            'meter': meter,
            'section': section,
            'start_line': file_line_num,
            'raw_text': '\n'.join(block_lines),
        })

    return blocks

def find_author_line(lines_list):
    """
    Find the author attribution line and return (author, idx_after_author).
    """
    # Author name pattern: typically on a line by itself, like "John Newton."
    # After stanza text but before annotation prose
    author_pats = [
        # Standard name: "Firstname Lastname." possibly with middle initial or Jr./D.D.
        r'^((?:Tr\.\s+(?:from\s+\w+\s+)?by\s+)?[A-Z][a-zA-Z\-]+\.?\s+[A-Z][a-zA-Z\.\-]+\.?\s*(?:[A-Z]\.?\s+[a-zA-Z\.]+\.?)?\s*(?:,?\s*(?:[A-Z]\.){1,3})?\s*[.,f]?\s*)$',
        # Author Unknown
        r'^(Author\s+Unknown\.?|Unknown\.?|Anonymous\.?)$',
        # Simple last name with period: "Watts." - rare but occurs
        r'^([A-Z][a-z]{3,15}\.)\s*$',
        # Two authors: "A. B. and C. D."
        r'^([A-Z][a-zA-Z\.\s]+and\s+[A-Z][a-zA-Z\.\s]+[.,]?)\s*$',
    ]

    for i, line in enumerate(lines_list):
        stripped = line.strip()
        if not stripped:
            continue
        if i < 2:  # Skip first 2 lines (header content)
            continue
        if i > 50:  # Don't look too deep
            break
        for pat in author_pats:
            m = re.match(pat, stripped)
            if m:
                author = m.group(1).strip().rstrip('.,f')
                # Verify this looks like a name (not a sentence)
                words = author.split()
                # Max 6 words for an author name
                if 1 <= len(words) <= 6:
                    return author, i + 1
    return "", 0

def extract_first_line(stanza_lines):
    """Extract the first line of hymn text from stanza lines."""
    for line in stanza_lines[:20]:
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r'^\d{1,3}$', stripped):  # Page numbers
            continue
        # Strip stanza number prefix
        stripped = re.sub(r'^\d+\s+', '', stripped)
        stripped = re.sub(r'\s{2,}', ' ', stripped).strip()
        if len(stripped) > 5 and not re.match(r'^[0-9\s]+$', stripped):
            return stripped
    return ""

def clean_text(text):
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def extract_annotation(block):
    """Extract structured annotation data from a block."""
    raw = block['raw_text']
    lines = raw.split('\n')

    author, annot_start = find_author_line(lines)

    if annot_start > 0:
        stanza_lines = lines[:annot_start - 1]
        annotation_lines = lines[annot_start:]
    else:
        # Fallback: look for first long lowercase-heavy line
        stanza_lines = []
        annotation_lines = []
        threshold = len(lines)
        for i, line in enumerate(lines):
            stripped = line.strip()
            lc = sum(1 for c in stripped if c.islower())
            if len(stripped) > 60 and lc > 20:
                threshold = i
                break
        stanza_lines = lines[:threshold]
        annotation_lines = lines[threshold:]

    first_line = extract_first_line(stanza_lines)
    annotation_clean = clean_text('\n'.join(annotation_lines))

    # --- Composition date ---
    composition_date = ""
    year_m = re.findall(r'\b(1[4-9]\d\d)\b', annotation_clean)
    if year_m:
        composition_date = year_m[0]

    # --- First published ---
    first_published = ""
    pub_pats = [
        r'[Ff]irst\s+(?:published|appeared?|printed)\s+in\s+([^.;]{5,100})',
        r'[Pp]ublished\s+in\s+([^.;]{5,100})',
        r'[Ff]rom\s+((?:the\s+)?[A-Z][a-zA-Z]+(?:\s+(?:of|the|and|[A-Za-z]+)){1,8}(?:,\s*\d{4})?)',
        r'[Aa]ppeared?\s+in\s+([^.;]{5,80})',
        r'[Ii]ncluded\s+in\s+([^.;]{5,80})',
    ]
    for pat in pub_pats:
        m = re.search(pat, annotation_clean)
        if m:
            pub = clean_text(m.group(1).rstrip('.;,'))
            if 5 < len(pub) < 120:
                first_published = pub
                break

    # --- Scripture basis ---
    scripture_basis = ""
    scr_pats = [
        r'[Bb]ased\s+(?:on|upon)\s+((?:[Pp]salm|[A-Z][a-z]+\.?)\s*\w+[\s.:\d,-]{0,30})',
        r'[Ff]ounded\s+(?:on|upon)\s+((?:[A-Z][a-z]+\.?)\s*\w+[\s.:\d,-]{0,30})',
        r'\(([A-Z][a-z]{2,}\.?\s*[xivlXIVL\d]+[\s.:\d,-]{0,20})\)',
        r'(?:Ps\.|Psalm)\s*([cxvi\d]+\.?\s*[\d\s,\-:]{0,20})',
    ]
    for pat in scr_pats:
        m = re.search(pat, annotation_clean)
        if m:
            scripture_basis = clean_text(m.group(1))[:100]
            break

    # --- Original stanza count ---
    original_stanzas = None
    num_words = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
                'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
                'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
                'twenty':20,'twenty-four':24,'twenty-eight':28,'twenty-five':25,
                'twenty-six':26,'twenty-seven':27,'thirty':30,'thirty-two':32}
    stanza_pats = [
        r'original\s+(?:has|contains?|consisted?\s+of|is\s+(?:made\s+up\s+of|composed\s+of))\s+(\w+)\s+stanzas?',
        r'(\w+)\s+stanzas?\s+in\s+the\s+original',
        r'contains?\s+(\w+)\s+stanzas?',
        r'(?:consists?|composed)\s+of\s+(\w+)\s+stanzas?',
    ]
    for pat in stanza_pats:
        m = re.search(pat, annotation_clean, re.IGNORECASE)
        if m:
            word = m.group(1).lower()
            if word.isdigit():
                original_stanzas = int(word)
            elif word in num_words:
                original_stanzas = num_words[word]
            break

    # --- Composition story ---
    composition_story = ""
    if annotation_clean:
        sents = re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(])', annotation_clean)
        parts = []
        char_ct = 0
        for s in sents:
            s = clean_text(s)
            if len(s) < 15:
                continue
            if re.match(r'^\d+\s+[A-Z]', s):  # Stanza
                continue
            parts.append(s)
            char_ct += len(s)
            if len(parts) >= 3 or char_ct >= 500:
                break
        composition_story = ' '.join(parts)[:800]

    # --- Textual notes ---
    textual_notes = ""
    txt_pats = [
        r'((?:[Tt]wo|[Tt]hree|[Oo]ne|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|\d+)\s+stanzas?\s+(?:are|have\s+been|were|is)\s+omitted[^.]{0,200}\.)',
        r'([Tt]he\s+original\s+has\s+\w+\s+stanzas?[^.]{0,200}\.)',
        r'([Cc]hanges?\s+have\s+been\s+made[^.]{0,200}\.)',
        r'([Aa]ltered?\s+(?:from|by)[^.]{0,200}\.)',
        r'([Tt]hese\s+are\s+verses?[^.]{0,200}\.)',
        r'([Vv]erses?\s+(?:one|two|three|four|\d+)[^.]{0,200}omitted[^.]{0,100}\.)',
    ]
    for pat in txt_pats:
        m = re.search(pat, annotation_clean)
        if m:
            textual_notes = clean_text(m.group(1))[:400]
            break

    # --- Anecdotes ---
    anecdotes = ""
    anec_pats = [
        r'([Oo]n\s+one\s+occasion[^.]{20,300}\.)',
        r'([Ii]t\s+is\s+(?:said|reported|told)\s+that[^.]{20,300}\.)',
        r'([Aa]\s+(?:remarkable|notable|touching|famous)\s+(?:story|incident|account|anecdote)[^.]{20,300}\.)',
        r'([Ww]hile\s+(?:lying|kneeling|dying|sitting|standing|traveling)[^.]{20,250}\.)',
        r'([Aa]t\s+(?:the\s+)?(?:time\s+of|deathbed|funeral|close\s+of)[^.]{20,250}\.)',
        r'([Ww]hen\s+(?:dying|this\s+hymn|the\s+author|first\s+published)[^.]{20,250}\.)',
    ]
    for pat in anec_pats:
        m = re.search(pat, annotation_clean)
        if m:
            anecdotes = clean_text(m.group(1))[:400]
            break

    # --- Tune name/composer ---
    tune_name = ""
    tune_composer = ""
    tune_m = re.search(r'(?:[Tt]une\s*(?:named?|called?|titled?)?\s+|[Ss]et\s+to\s+music\s+(?:by\s+)?|[Mm]usic\s+(?:by|composed\s+by)\s+)([A-Z][^.;,\n]{2,60})', annotation_clean)
    if tune_m:
        tune_name = clean_text(tune_m.group(1))[:80]

    # --- Critical assessment ---
    critical_assessment = ""
    crit_pats = [
        r'([Oo]ne\s+of\s+the\s+(?:finest|greatest|best|noblest|most\s+\w+)[^.]{0,300}\.)',
        r'([Rr]anks?\s+(?:with|among)\s+the\s+(?:first|best|greatest)[^.]{0,300}\.)',
        r'([Uu]niversally\s+(?:sung|loved|known|used)[^.]{0,200}\.)',
        r'("(?:[Ii]t\s+ranks?|[Ii]t\s+is\s+one\s+of)[^"]{0,200}")',
        r'([Jj]ulian\s+(?:says?|remarks?|writes?)[^.]{0,300}\.)',
    ]
    for pat in crit_pats:
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

    print("Building hymn blocks...")
    blocks = build_hymn_blocks(lines)
    print(f"Built {len(blocks)} blocks.")

    print("Extracting annotation data...")
    hymn_data = []
    for block in blocks:
        data = extract_annotation(block)
        hymn_data.append(data)

    hymn_data.sort(key=lambda x: x['nutter_hymn_number'])

    # Section distribution
    sections = {}
    for h in hymn_data:
        s = h['topic_section']
        sections[s] = sections.get(s, 0) + 1

    print(f"\nExtracted {len(hymn_data)} hymns")
    print("\nSection distribution:")
    for s, count in sorted(sections.items()):
        print(f"  {s}: {count}")

    nums = sorted(h['nutter_hymn_number'] for h in hymn_data)
    print(f"\nHymn range: {nums[0]} to {nums[-1]}")

    # Show what's missing from 201-748 range
    expected = set(range(201, 749))
    found = set(nums)
    missing = sorted(expected - found)
    if missing:
        # Group consecutive missing numbers
        groups = []
        start = missing[0]
        end = missing[0]
        for m in missing[1:]:
            if m == end + 1:
                end = m
            else:
                groups.append(f"{start}" if start == end else f"{start}-{end}")
                start = end = m
        groups.append(f"{start}" if start == end else f"{start}-{end}")
        print(f"Missing {len(missing)} hymns: {', '.join(groups[:30])}")

    # Quality check: show some entries
    print(f"\nSample entries:")
    samples = [h for h in hymn_data if h['nutter_hymn_number'] in [201, 207, 250, 300, 400, 500, 600, 718, 748]]
    for h in samples:
        print(f"  #{h['nutter_hymn_number']:3d}: '{h['first_line'][:45]}' | '{h['author'][:25]}' | {h['topic_section'][:30]}")

    print(f"\nWriting to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(hymn_data, f, indent=2, ensure_ascii=False)

    print(f"Done! {len(hymn_data)} hymns written.")

if __name__ == '__main__':
    main()
