#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, hymns 201 through 748.
Version 4: Hardcoded OCR corrections for specific known errors.

Key OCR correction rules identified from sequence analysis:
- "303" at line 16577 → 203
- "230" at line 17664 → 220 (between 218 and 221)
- "347" at line 19330 → 247
- "350","351","352" at lines 19468,19559,19626 → 250,251,252
- "360","363" at lines 20206,20408 → 260,263 (but need to verify 261,262)
- "369" at line 20903 → 269
- "371" at line 21098 → 271
- "312" at line 28864 → 372 (between 371 and 373)
- "332" at line 40672 → 532
- "330","351" at lines 41885,41929 → 550,551
- "355" at line 42243 → 555
"""

import re
import json

SOURCE_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt"
OUTPUT_FILE = r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part2.json"

START_LINE = 16443
END_LINE = 55660

# Explicit OCR corrections: file_line_number → corrected_hymn_number
# When the detected OCR number is wrong, we specify the correct hymn number.
EXPLICIT_CORRECTIONS = {
    16577: 203,   # "303" → 203 (leading 3 vs 2)
    17664: 220,   # "230" → 220 (between 218 and 221)
    19330: 247,   # "347" → 247
    19468: 250,   # "350" → 250
    19559: 251,   # "351" → 251
    19626: 252,   # "352" → 252
    20206: 260,   # "360" → 260
    20408: 263,   # "363" → 263
    20465: 264,   # "364" → 264
    20500: 265,   # "365" → 265
    20674: 267,   # "367" → 267
    20903: 269,   # "369" → 269
    21098: 271,   # "371" → 271
    27502: 352,   # "358" → 352 (between 351 and 353)
    28864: 372,   # "312" → 372 (between 371 and 373)
    32346: 422,   # "433" → 422 (before 426, "Work for the night is coming")
    40672: 532,   # "332" → 532
    41885: 550,   # "330" → 550
    41929: 551,   # "351" → 551
    42243: 555,   # "355" → 555
}

# Lines where OCR damage is too severe for normal detection,
# or where the "meter" field is a Latin title (for chants).
# Format: file_line_number → (hymn_number, meter_or_title_string)
FORCED_ENTRIES = {
    18201: (228, "C. M."),           # "22S  C, IL" → 228, C.M.
    18738: (238, "9s, 8s."),         # "238  98\ufffd  8s-" → 238 (meter garbled)
    # Chants and Occasional Pieces (Latin titles instead of meters)
    54380: (728, "Venite, Exultemus Domino"),   # "7S8  VenitCf..." → 728
    54439: (729, "Te Deum Laudamus"),            # "739  Deum Laudamus*" → 729
    54590: (730, "Jubilate Deo"),                # "730  Jubilate Deo."
    54631: (731, "Magnificat"),                  # "731  Magnificat."
    54751: (733, "Nunc Dimittis"),               # "733  Nunc Dimittis."
    54782: (734, "Invocation Sentence"),         # "734  Invocation Sentence*"
    54979: (737, "Gloria Patri"),                # "737  Gloria Patria."
    54993: (738, "The Ten Commandments"),        # "738  The Ten Commandments."
    55087: (739, "Offertory Sentence"),          # "739  Offertory Sentence." (second 739)
    55129: (742, "Gloria in Excelsis"),          # "742  Gloria in Exceltis."
    55251: (744, "Crossing the Bar"),            # "744  Grossing the Bar*"
    55620: (748, "Benediction"),                 # "748  Benediction*"
}

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

def ocr_correct_prefix(s):
    """Apply basic OCR character corrections to a number string."""
    table = str.maketrans('aoilSOB', '2011508')
    return s.translate(table)

def detect_hymn_header(line_text):
    """
    Detect hymn header lines.
    Returns (ocr_corrected_num, meter_str) or (None, None).
    """
    stripped = line_text.strip()
    m = re.match(r'^([A-Za-z0-9]{2,3})\s{1,6}(.{3,45})$', stripped)
    if not m:
        return None, None

    prefix = m.group(1)
    rest = m.group(2).strip()

    meter_patterns = [
        r'^[CcLlSsMmPp]\.?\s*[Mm]\.?',   # C.M., L.M., S.M., P.M.
        r'^[CcLlSsMmPp]-\s*[Mm]\.?',      # L- M. (OCR dash)
        r'^[CcLlSsMmPp]\.\s+[Dd]\.?',     # S. D. (S.M.D.)
        r'^[Ss]s',                          # Ss, (Short stanzas)
        r'^[0-9]+\s*s',                    # 7s, 8s, 10s
        r'^[0-9]+\s*[,\.]\s*[0-9]',       # 8, 7, 8, 7
        r'^P\.\s*M\.',                      # P.M.
        r'^[0-9]{2}\s+[0-9]',             # 11 10
        r'^lis\.?',                         # lis. (11s)
        r'^-[0-9]',                         # -78, (OCR artifact meter)
        r'^[0-9]+\.',                       # 108. or 78. (short meters)
        r'^9[0-9]\s*[,\s]',               # 98, 8s (D.S.M.)
        r'^[0-9]+\s*\*',                   # 8* (starred meter)
    ]
    if not any(re.match(pat, rest) for pat in meter_patterns):
        return None, None

    corrected = ocr_correct_prefix(prefix)
    try:
        num = int(corrected)
        if 150 <= num <= 800:
            return num, rest
    except ValueError:
        pass

    return None, None

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
    Build hymn blocks.
    Applies explicit corrections for known OCR errors.
    """
    current_section = "Hymns on the Holy Scriptures"
    headers = []  # (file_line_num, hymn_num, meter, section)

    for file_line_num, line_text in lines:
        if is_page_header(line_text):
            continue
        sec = is_section_header(line_text)
        if sec:
            current_section = sec
            continue

        # Check for forced entries (OCR too damaged to auto-detect)
        if file_line_num in FORCED_ENTRIES:
            forced_num, forced_meter = FORCED_ENTRIES[file_line_num]
            headers.append((file_line_num, forced_num, forced_meter, current_section))
            continue

        ocr_num, meter = detect_hymn_header(line_text)
        if ocr_num is None:
            continue

        # Apply explicit OCR correction
        corrected_num = ocr_num
        if file_line_num in EXPLICIT_CORRECTIONS:
            corrected_num = EXPLICIT_CORRECTIONS[file_line_num]

        if 200 <= corrected_num <= 750:
            headers.append((file_line_num, corrected_num, meter, current_section))

    print(f"  Detected {len(headers)} hymn headers")

    # Build line-indexed dict for fast block boundary lookup
    # We need to associate each header with its content block
    # Content: from line AFTER header to line BEFORE next header

    # Build a sorted list of (file_line_num, hymn_num, meter, section)
    headers.sort(key=lambda x: x[0])

    # Build line number → index mapping
    lines_dict = {ln: text for ln, text in lines}

    blocks = []
    for i, (fln, hymn_num, meter, section) in enumerate(headers):
        # Find next header line
        next_fln = headers[i+1][0] if i+1 < len(headers) else END_LINE + 1

        # Collect content lines
        block_lines = []
        for ln in range(fln + 1, next_fln):
            if ln in lines_dict:
                ltext = lines_dict[ln]
                if not is_page_header(ltext) and not is_section_header(ltext):
                    block_lines.append(ltext)

        blocks.append({
            'hymn_number': hymn_num,
            'meter': meter,
            'section': section,
            'start_line': fln,
            'raw_text': '\n'.join(block_lines),
        })

    # Deduplicate: for each hymn number, keep the entry with more content
    by_num = {}
    for block in blocks:
        n = block['hymn_number']
        if n not in by_num:
            by_num[n] = block
        else:
            # Keep the one with longer annotation (more content = better)
            if len(block['raw_text']) > len(by_num[n]['raw_text']):
                by_num[n] = block

    deduped = sorted(by_num.values(), key=lambda x: x['hymn_number'])
    print(f"  After dedup: {len(deduped)} unique hymns")
    return deduped

def find_author_line(lines_list):
    """Find author attribution and return (author, annot_start_idx)."""
    author_pats = [
        # "Firstname Lastname." with optional middle, titles
        r'^((?:Tr\.\s+(?:from\s+\w+\s+)?by\s+)?[A-Z][a-zA-Z\-]+\.?\s+[A-Z][a-zA-Z\.\-]+\.?\s*(?:[A-Z]\.?\s+[a-zA-Z\.]+\.?)?\s*(?:,?\s*(?:[A-Z]\.){1,3})?\s*[.,f]?\s*)$',
        r'^(Author\s+Unknown\.?|Unknown\.?|Anonymous\.?)$',
        r'^([A-Z][a-z]{3,15}\.)\s*$',  # Single last name like "Watts."
        r'^([A-Z][a-zA-Z\.\s]+and\s+[A-Z][a-zA-Z\.\s]+[.,]?)\s*$',  # Two authors
        r'^([A-Z][a-zA-Z\-]+\s+[A-Z][a-zA-Z\.\s\-]+,\s*(?:D\.D\.|LL\.D\.|Jr\.|Rev\.))\s*$',
    ]
    for i, line in enumerate(lines_list):
        if i < 2 or i > 50:
            continue
        stripped = line.strip()
        if not stripped:
            continue
        for pat in author_pats:
            m = re.match(pat, stripped)
            if m:
                author = m.group(1).strip().rstrip('.,f')
                words = author.split()
                if 1 <= len(words) <= 7:
                    return author, i + 1
    return "", 0

def extract_first_line(stanza_lines):
    for line in stanza_lines[:20]:
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r'^\d{1,3}$', stripped):
            continue
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
    raw = block['raw_text']
    lines = raw.split('\n')

    author, annot_start = find_author_line(lines)

    if annot_start > 0:
        stanza_lines = lines[:annot_start - 1]
        annotation_lines = lines[annot_start:]
    else:
        # Find prose start by looking for long lowercase-heavy lines
        split_at = 10
        for i, line in enumerate(lines):
            stripped = line.strip()
            lc = sum(1 for c in stripped if c.islower())
            if len(stripped) > 60 and lc > 20:
                split_at = i
                break
        stanza_lines = lines[:split_at]
        annotation_lines = lines[split_at:]

    first_line = extract_first_line(stanza_lines)
    annotation_clean = clean_text('\n'.join(annotation_lines))

    # Composition date
    composition_date = ""
    years = re.findall(r'\b(1[4-9]\d\d)\b', annotation_clean)
    if years:
        composition_date = years[0]

    # First published
    first_published = ""
    pub_pats = [
        r'[Ff]irst\s+(?:published|appeared?|printed)\s+in\s+([^.;]{5,100})',
        r'[Pp]ublished\s+in\s+([^.;]{5,100})',
        r'[Ff]rom\s+((?:the\s+)?[A-Z][a-zA-Z]+(?:\s+(?:of|the|and|[A-Za-z]+)){1,8}(?:,\s*\d{4})?)',
        r'[Aa]ppeared?\s+in\s+([^.;]{5,80})',
        r'[Ii]n\s+((?:[A-Z][a-zA-Z]+(?:\s+[A-Za-z]+){1,5}),?\s*\d{4})',
    ]
    for pat in pub_pats:
        m = re.search(pat, annotation_clean)
        if m:
            pub = clean_text(m.group(1).rstrip('.;,'))
            if 5 < len(pub) < 120:
                first_published = pub
                break

    # Scripture basis
    scripture_basis = ""
    scr_pats = [
        r'[Bb]ased\s+(?:on|upon)\s+((?:[Pp]salm|[A-Z][a-z]+\.?)\s*\w+[\s.:\d,-]{0,30})',
        r'[Ff]ounded\s+(?:on|upon)\s+((?:[A-Z][a-z]+\.?)\s*\w+[\s.:\d,-]{0,30})',
        r'\(([A-Z][a-z]{2,}\.?\s*[xivlXIVL\d]+[\s.:\d,-]{0,20})\)',
    ]
    for pat in scr_pats:
        m = re.search(pat, annotation_clean)
        if m:
            scripture_basis = clean_text(m.group(1))[:100]
            break

    # Original stanza count
    original_stanzas = None
    num_words = {
        'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
        'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
        'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
        'twenty':20,'twenty-four':24,'twenty-eight':28,'twenty-five':25,
        'twenty-six':26,'twenty-seven':27,'thirty':30,'thirty-two':32
    }
    stanza_pats = [
        r'original\s+(?:has|contains?|consisted?\s+of|is\s+(?:made\s+up\s+of|composed\s+of))\s+(\w+(?:-\w+)?)\s+stanzas?',
        r'(\w+(?:-\w+)?)\s+stanzas?\s+in\s+the\s+original',
        r'consists?\s+of\s+(\w+(?:-\w+)?)\s+stanzas?',
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

    # Composition story
    composition_story = ""
    if annotation_clean:
        sents = re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(])', annotation_clean)
        parts = []
        char_ct = 0
        for s in sents:
            s = clean_text(s)
            if len(s) < 15 or re.match(r'^\d+\s+[A-Z]', s):
                continue
            parts.append(s)
            char_ct += len(s)
            if len(parts) >= 3 or char_ct >= 500:
                break
        composition_story = ' '.join(parts)[:800]

    # Textual notes
    textual_notes = ""
    txt_pats = [
        r'((?:[Tt]wo|[Tt]hree|[Oo]ne|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|\d+)\s+stanzas?\s+(?:are|have\s+been|were|is)\s+omitted[^.]{0,200}\.)',
        r'([Tt]he\s+original\s+has\s+\w+\s+stanzas?[^.]{0,200}\.)',
        r'([Cc]hanges?\s+have\s+been\s+made[^.]{0,200}\.)',
        r'([Tt]hese\s+are\s+verses?[^.]{0,200}\.)',
    ]
    for pat in txt_pats:
        m = re.search(pat, annotation_clean)
        if m:
            textual_notes = clean_text(m.group(1))[:400]
            break

    # Anecdotes
    anecdotes = ""
    anec_pats = [
        r'([Oo]n\s+one\s+occasion[^.]{20,300}\.)',
        r'([Ii]t\s+is\s+(?:said|reported|told)\s+that[^.]{20,300}\.)',
        r'([Ww]hile\s+(?:lying|kneeling|dying|sitting|standing|traveling)[^.]{20,250}\.)',
        r'([Aa]t\s+(?:the\s+)?(?:time\s+of|deathbed|funeral|close)[^.]{20,250}\.)',
    ]
    for pat in anec_pats:
        m = re.search(pat, annotation_clean)
        if m:
            anecdotes = clean_text(m.group(1))[:400]
            break

    # Tune name
    tune_name = ""
    tune_m = re.search(r'(?:[Tt]une\s+(?:named?|called?|titled?\s+)?|[Ss]et\s+to\s+music\s+by\s+|[Mm]usic\s+(?:by|composed\s+by)\s+)([A-Z][^.;,\n]{2,60})', annotation_clean)
    if tune_m:
        tune_name = clean_text(tune_m.group(1))[:80]

    # Critical assessment
    critical_assessment = ""
    crit_pats = [
        r'([Oo]ne\s+of\s+the\s+(?:finest|greatest|best|noblest|most\s+\w+)[^.]{0,300}\.)',
        r'([Rr]anks?\s+(?:with|among)\s+the\s+(?:first|best|greatest)[^.]{0,300}\.)',
        r'([Uu]niversally\s+(?:sung|loved|known|used)[^.]{0,200}\.)',
        r'([Jj]ulian\s+(?:says?|remarks?|writes?)[^.]{0,300}\.)',
        r'("(?:[Ii]t\s+ranks?|[Ii]t\s+is\s+one\s+of)[^"]{0,200}")',
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
        "tune_composer": "",
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

    if hymn_data:
        nums = sorted(h['nutter_hymn_number'] for h in hymn_data)
        print(f"\nHymn range: {nums[0]} to {nums[-1]}")

        expected = set(range(201, 749))
        found = set(nums)
        missing = sorted(expected - found)

        if missing:
            groups = []
            start = end = missing[0]
            for mv in missing[1:]:
                if mv == end + 1:
                    end = mv
                else:
                    groups.append(f"{start}" if start==end else f"{start}-{end}")
                    start = end = mv
            groups.append(f"{start}" if start==end else f"{start}-{end}")
            print(f"Missing {len(missing)} hymns from 201-748: {', '.join(groups[:40])}")

        print(f"\nSample entries:")
        for target in [201, 207, 210, 247, 260, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 718, 730, 748]:
            h = next((x for x in hymn_data if x['nutter_hymn_number'] == target), None)
            if h:
                print(f"  #{h['nutter_hymn_number']:3d}: '{h['first_line'][:45]}' | by '{h['author'][:25]}' | {h['topic_section'][:30]}")

    print(f"\nWriting to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(hymn_data, f, indent=2, ensure_ascii=False)

    print(f"Done! {len(hymn_data)} hymns written.")

if __name__ == '__main__':
    main()
