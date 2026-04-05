#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, lines 622-30000.
Handles OCR artifacts extensively.
Produces: builds/Hymn_Wiki/wiki/_nutter_hymn_data_part1.json
"""

import re
import json
import sys

INPUT_FILE = r'C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt'
OUTPUT_FILE = r'C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part1.json'

START_LINE = 621   # 0-indexed (file line 622)
END_LINE   = 30001 # exclusive

# =========================================================================
# Load file
# =========================================================================
with open(INPUT_FILE, 'r', encoding='utf-8', errors='replace') as f:
    raw = f.readlines()
lines = [l.rstrip('\n') for l in raw]
total_lines = len(lines)
print(f"Loaded {total_lines} lines", file=sys.stderr)

# =========================================================================
# OCR cleanup helpers
# =========================================================================
def clean_ws(s):
    return re.sub(r'\s+', ' ', s).strip()

def clean_text(s):
    """Basic OCR cleanup for prose text."""
    s = re.sub(r'\s+', ' ', s).strip()
    # Common OCR word fixes
    replacements = [
        (r'\bgrrace\b', 'grace'), (r'\bgrracious\b', 'gracious'),
        (r'\btlie\b', 'the'), (r'\btho\b', 'the'),
        (r'\biiim\b', 'him'), (r'\bliis\b', 'his'),
        (r'\bIlls\b', 'His'), (r'\btha\b', 'the'),
        (r'\bln\b', 'in'), (r'\bIs\b', 'Is'),
    ]
    for pat, repl in replacements:
        s = re.sub(pat, repl, s)
    return s

def is_page_header(s):
    """True if line is a running page header (to be ignored in content)."""
    s = s.strip()
    patterns = [
        r'^ANNOTATED\s+HYMNAL',
        r'^HYMNS\s+(OF|TO|ON|OP|FOR)',
        r'^THE\s+METHODIST',
        r'^WORSHIP\.?\s*$',
        r'^THE\s+CHRISTIAN\s+LIFE\.?\s*$',
        r'^THE\s+LORD\s+JESUS',
        r'^THE\s+GOSPEL',
        r'^THE\s+CHURCH',
        r'^THE\s+HOLY\s+SPIRIT',
        r'^THE\s+HOLY\s+SCRIPTURES',
        r'^TIMES\s+AND\s+SEASONS',
        r'^THE\s+FUTURE\s+LIFE',
    ]
    for p in patterns:
        if re.match(p, s, re.I):
            return True
    return False

def is_page_number(s, line_idx):
    """True if s is a standalone page number (not a hymn header number)."""
    s = s.strip()
    if not re.match(r'^\d{1,3}$', s):
        return False
    num = int(s)
    # Check if ANNOTATED HYMNAL follows within next 3 non-empty lines
    count = 0
    for j in range(line_idx+1, min(line_idx+6, total_lines)):
        ahead = lines[j].strip()
        if not ahead:
            continue
        count += 1
        if re.match(r'^ANNOTATED\s+HYMNAL', ahead, re.I):
            return True
        if count >= 3:
            break
    return False

# =========================================================================
# Detect hymn header lines
# Formats:
#   (A) "N  C. M." / "N  L. M." etc. (number + meter on one line)
#   (B) "N:  6, 6, 8, 4. D." (colon separator)
#   (C) "N  L M." / "N  u M." / "N  6, 6, 8, 4" (various OCR mangling)
#   (D) standalone "N" followed by meter line within a few lines,
#       not followed by ANNOTATED HYMNAL (which marks page numbers)
# =========================================================================

# Meter patterns (lenient to catch OCR variants)
METER_PATTERNS = [
    # Standard abbreviated meters
    r'[CcLlSsPpHh]\s*[\.\s]\s*[Mm]\s*\.?',  # C.M. L.M. etc
    r'[CcLlSsPpHh]\s*\.?\s*[Mm]\s*\.?\s*D\.?',  # C.M.D.
    r'[LlUu]\s*[Mm]\s*\.?\s*\d+',  # L.M.61 etc
    # Digit-based meters
    r'\d[\d,\s\.]+[Dd]\.?',  # 6,6,8,4. D.
    r'\d[\d,\s\.]{3,}',      # 8. 8. 6.
    # Named shortened meters
    r'[678]\s*s\.?',          # 7s. 8s.
    r'10,10,11,11',
    r'8s,7s',
]
METER_RE = re.compile('(?:' + '|'.join(METER_PATTERNS) + ')', re.I)

def looks_like_meter(s):
    """Return True if s appears to be a meter string."""
    s = s.strip()
    if len(s) < 3 or len(s) > 30:
        return False
    return bool(METER_RE.match(s))

# Strict pattern for full hymn header on one line
HEADER_STRICT = re.compile(
    r'^(\d{1,3})\s*:?\s+'
    r'([CcLlSsPpHh]\s*[\.\s]\s*[Mm]\s*\.?'    # C.M., L.M., u M., etc.
    r'|[CcLlSsPpHh]\s*[\.\s]\s*[Mm]\s*\.?\s*[Dd]\.?'
    r'|[LlUu]\s*[Mm]\s*\.?\s*\d*'             # L M. 61
    r'|[\d,\s\.]{3,}[Dd]\.?'                  # 6, 6, 8, 4. D.
    r'|[678]\s*s\.?'                           # 7s.
    r'|10,10,11,11'
    r')\s*$',
    re.IGNORECASE
)

hymn_map = {}  # hymn_number -> line_idx (0-indexed)
meter_map = {} # hymn_number -> meter string

i = START_LINE
while i < END_LINE and i < total_lines:
    stripped = lines[i].strip()

    # Pattern A/B/C: number + meter on same line
    m = HEADER_STRICT.match(stripped)
    if m:
        num = int(m.group(1))
        if 1 <= num <= 400:
            meter = clean_ws(m.group(2))
            if num not in hymn_map:
                hymn_map[num] = i
                meter_map[num] = meter
        i += 1
        continue

    # Pattern D: standalone number
    m2 = re.match(r'^(\d{1,3})\s*$', stripped)
    if m2:
        num = int(m2.group(1))
        if 1 <= num <= 400 and not is_page_number(stripped, i):
            # Look ahead for meter
            meter = ''
            non_empty = 0
            for j in range(i+1, min(i+8, total_lines)):
                ahead = lines[j].strip()
                if not ahead:
                    continue
                non_empty += 1
                if looks_like_meter(ahead):
                    meter = ahead
                    break
                if is_page_header(ahead):
                    break
                if non_empty >= 4:
                    break
            if num not in hymn_map:
                hymn_map[num] = i
                meter_map[num] = meter
        i += 1
        continue

    i += 1

# Sort by line number
hymn_locs = sorted(hymn_map.items(), key=lambda x: x[1])
print(f"Detected hymn headers for {len(hymn_locs)} hymns", file=sys.stderr)
nums = [n for n,_ in hymn_locs]
print(f"Range: hymn {min(nums)} to hymn {max(nums)}", file=sys.stderr)
missing = [n for n in range(1, min(max(nums)+1, 201)) if n not in hymn_map]
if missing:
    print(f"Missing 1-200: {missing}", file=sys.stderr)

# =========================================================================
# Section tracking
# Sections appear as running headers split across pages.
# We track them by scanning the text for section-name strings.
# =========================================================================

section_boundaries = []
# Pre-scan for section changes
SECTION_NAMES = {
    'WORSHIP': 'Worship',
    'THE LORD JESUS CHRIST': 'The Lord Jesus Christ',
    'THE HOLY SPIRIT': 'The Holy Spirit',
    'THE HOLY SCRIPTURES': 'The Holy Scriptures',
    'THE CHRISTIAN LIFE': 'The Christian Life',
    'THE CHURCH': 'The Church',
    'THE GOSPEL': 'The Gospel',
    'HYMNS TO THE FATHER': 'Hymns to the Father',
    'TIMES AND SEASONS': 'Times and Seasons',
    'THE FUTURE LIFE': 'The Future Life',
}

current_section = 'Worship'
section_at_line = {}
for i in range(START_LINE, min(END_LINE, total_lines)):
    s = lines[i].strip().upper()
    for key, val in SECTION_NAMES.items():
        if key in s and len(s) < len(key) + 15:
            current_section = val
            break
    section_at_line[i] = current_section

def get_section(line_idx):
    return section_at_line.get(line_idx, 'Worship')

# =========================================================================
# For each hymn, extract content
# =========================================================================

# Build list of (hymn_num, start_line, end_line)
hymn_ranges = []
for idx, (hymn_num, start_line) in enumerate(hymn_locs):
    if idx + 1 < len(hymn_locs):
        end_line = hymn_locs[idx+1][1]
    else:
        end_line = min(start_line + 400, END_LINE, total_lines)
    hymn_ranges.append((hymn_num, start_line, end_line))

def extract_first_line(block):
    """Get the first line of the hymn text."""
    for j in range(1, min(25, len(block))):
        s = block[j].strip()
        if not s:
            continue
        if is_page_header(s):
            continue
        if looks_like_meter(s):
            continue
        # Skip obvious stanza markers (stanza 2+)
        m = re.match(r'^(\d+)\s+([A-Z])', s)
        if m and int(m.group(1)) >= 2:
            continue
        # Skip single-letter OCR artifacts (dropped capitals)
        if len(s) <= 3 and re.match(r'^[A-Z"\']+$', s):
            continue
        # This is our first line
        result = clean_ws(s)
        # Fix "COME" -> "C OME" style OCR - actually reverse: the OCR sometimes
        # renders "COME" as "C" on one line and "OME" on next
        # More common: "OW great" = "HOW great" (dropped first letter)
        return result
    return ''

def find_author_in_block(block):
    """Find author attribution line and its index in block."""
    # Author line: a proper name, 2-4 words, relatively short
    # Appears after the hymn stanzas, before annotation prose
    author_re = re.compile(
        r'^([A-Z][a-z]+(?:\s+[A-Z]\.?)?\s+[A-Z][a-zA-Z\-\']+(?:,?\s*(?:Jr\.|D\.D\.|LL\.D\.))?)'
        r'(?:\s*\(.*?\))?'
        r'(?:\s*\.?\s*Alt(?:ered)?\.?\s*(?:by\s+.+)?)?'
        r'\s*\.?\s*$'
    )
    # Also match: "Tr. by Name Name" or "Trans. Name Name"
    trans_re = re.compile(r'^(?:Tr\.|Trans\.?|Translated\s+by)\s+(.+)$', re.I)
    # Attributed form: "Author's Name. Alt. by Other Name."

    for j in range(4, min(120, len(block))):
        s = block[j].strip()
        if not s or is_page_header(s):
            continue

        # Trans. by Name
        mt = trans_re.match(s)
        if mt and len(s) < 80:
            if j >= 4:
                return j, clean_ws(s.rstrip('.'))

        # Standard author name
        m = author_re.match(s)
        if m and len(s) < 80:
            if j >= 4:
                return j, clean_ws(s.rstrip('.'))

    return None, ''

def extract_annotation_text(block, author_idx):
    """Extract the annotation prose text."""
    if author_idx is not None:
        start = author_idx + 1
    else:
        # Find start of annotation prose
        start = None
        for j in range(5, min(80, len(block))):
            s = block[j].strip()
            if not s or is_page_header(s):
                continue
            # Annotation starts with certain words
            if re.match(r'^(This\s|The\s|From\s|Author|It\s+is|He\s+was|She\s|Based|Written|Published|These\s)', s, re.I):
                if j >= 6:
                    start = j
                    break
        if start is None:
            start = min(25, len(block))

    pieces = []
    for j in range(start, len(block)):
        s = block[j].strip()
        if s and not is_page_header(s):
            pieces.append(s)

    return clean_ws(' '.join(pieces))

# =========================================================================
# Parse annotation text for specific fields
# =========================================================================

def parse_annotation(ann_text):
    """Extract structured fields from annotation prose."""
    f = {
        'composition_date': '',
        'first_published': '',
        'original_stanzas': '',
        'stanzas_in_hymnal': '',
        'scripture_basis': '',
        'composition_story': '',
        'textual_notes': '',
        'anecdotes': '',
        'tune_name': '',
        'tune_composer': '',
        'critical_assessment': '',
    }

    # Scripture basis
    patterns_scripture = [
        re.compile(r'based\s+on\s+([A-Za-z\s]+\s+\w+\s*[\.\d:]+[^\.]{0,30})', re.I),
        re.compile(r'(?:paraphrase\s+of|metrical\s+version\s+of|founded\s+on)\s+([A-Za-z\s\d:]+(?:Psalm|verse)?[^\.]{0,40})', re.I),
        re.compile(r'scripture\s+basis\s+is\s+([^\.]{5,60})', re.I),
        re.compile(r'(?:Psalm|Psalms|Isaiah|Matthew|John|Luke|Romans|Hebrews|Acts|Genesis|Exodus|Numbers|Deuteronomy|Joshua|Proverbs|Ecclesiastes|Song\s+of|Revelation|Philippians|Colossians|Ephesians|Galatians|Thessalonians|Timothy|Titus|Corinthians|Peter)\s+[\w\.:\-]+', re.I),
    ]
    for pat in patterns_scripture:
        m = pat.search(ann_text)
        if m:
            f['scripture_basis'] = clean_ws(m.group(0))
            break

    # First published
    pub_patterns = [
        re.compile(r'(?:first\s+appeared\s+in|first\s+published\s+in|published\s+in|appeared\s+in|printed\s+in)\s+(?:the\s+)?(?:author.s\s+)?([^,\.]{8,70}(?:,\s*\d{4}|\d{4}))', re.I),
        re.compile(r'[Ff]rom\s+(?:the\s+)?(?:author.s\s+)?([A-Z][^,\.]{5,60}(?:,\s*|\s+)\d{4})', re.I),
        re.compile(r'(?:In|from)\s+((?:[A-Z][a-z]+\s+){1,5}(?:Hymns?|Psalms?|Poems?|Songs?|Book|Collection)[^,\.]{0,30},?\s*\d{4})', re.I),
    ]
    for pat in pub_patterns:
        m = pat.search(ann_text)
        if m:
            f['first_published'] = clean_ws(m.group(0))
            break

    # Original stanza count
    stanza_patterns = [
        re.compile(r'(?:original(?:ly)?\s+)?(?:contained|comprises?|consisted\s+of|had)\s+(\w+(?:-\w+)?|\d+)\s+stanzas?', re.I),
        re.compile(r'(?:eighteen|seventeen|sixteen|fifteen|fourteen|thirteen|twelve|eleven|ten|nine|eight|seven|six|five|four|three)\s+stanzas?', re.I),
        re.compile(r'(\d+)\s+stanza\s+poem', re.I),
        re.compile(r'poem\s+(?:of|containing)\s+(\d+|\w+)\s+stanzas?', re.I),
    ]
    for pat in stanza_patterns:
        m = pat.search(ann_text)
        if m:
            f['original_stanzas'] = clean_ws(m.group(0))
            break

    # Stanzas in hymnal
    hymnal_stanza_patterns = [
        re.compile(r'(?:stanzas?|verses?)\s+(\d+)\s+to\s+(\d+)', re.I),
        re.compile(r'composed\s+of\s+(?:stanzas?|verses?)\s+(\d+)\s+to\s+(\d+)', re.I),
        re.compile(r'(?:the\s+)?hymn\s+is\s+(?:stanzas?|verses?)\s+(\d+)\s+(?:to|through|-)\s+(\d+)', re.I),
    ]
    for pat in hymnal_stanza_patterns:
        m = pat.search(ann_text)
        if m:
            f['stanzas_in_hymnal'] = clean_ws(m.group(0))
            break

    # Composition date
    date_patterns = [
        re.compile(r'written\s+(?:in\s+|on\s+)?([A-Z][a-z]+\s+\d+,?\s*\d{4})', re.I),
        re.compile(r'written\s+in\s+(\d{4})', re.I),
        re.compile(r'composed\s+(?:in\s+)?(\d{4})', re.I),
        re.compile(r'written\s+(?:about|circa|c\.)\s+(\d{4})', re.I),
    ]
    for pat in date_patterns:
        m = pat.search(ann_text)
        if m:
            f['composition_date'] = clean_ws(m.group(1))
            break

    # Tune name
    tune_patterns = [
        re.compile(r'tune\s+(?:known\s+as\s+|called\s+)?["\u201c]([A-Za-z\s\-]+)["\u201d]', re.I),
        re.compile(r'sung\s+to\s+(?:the\s+tune\s+(?:of\s+)?)?["\u201c]([A-Za-z\s\-]+)["\u201d]', re.I),
        re.compile(r'named\s+["\u201c]([A-Za-z\s]+)["\u201d]', re.I),
    ]
    for pat in tune_patterns:
        m = pat.search(ann_text)
        if m:
            f['tune_name'] = clean_ws(m.group(1))
            break

    # Critical assessment (first substantial quoted evaluation)
    # Look for quotes like: "This is..." or "There is not in our language..." etc.
    crit_pattern = re.compile(r'["\u201c]([A-Z][^"]{20,200})["\u201d]')
    for m in crit_pattern.finditer(ann_text):
        text = m.group(1)
        # Skip if it's clearly a Bible verse or hymn text
        if not re.search(r'\bhymn\b|\bpoet\b|\bverse\b|\bling\w*\b|\bauthor\b|\blanguage\b', text, re.I):
            continue
        f['critical_assessment'] = clean_ws(text)
        break

    # Composition story (narrative about when/how it was written)
    story_patterns = [
        re.compile(r'(?:hymn\s+was\s+written|written\s+while|composed\s+while|written\s+at\s+the|inspired\s+by)[^.]{10,200}\.', re.I),
        re.compile(r'(?:anniversary|occasion|circumstance|story\s+of)[^.]{10,200}\.', re.I),
    ]
    for pat in story_patterns:
        m = pat.search(ann_text)
        if m:
            f['composition_story'] = clean_ws(m.group(0))
            break

    # Textual notes (changes from original)
    textual_patterns = [
        re.compile(r'(?:author\s+wrote|originally\s+read|original(?:ly)?\s+(?:ran|was)|changed\s+(?:by|from)|altered\s+(?:by|from))[^.]{10,200}\.', re.I),
        re.compile(r'(?:unaltered|unchanged|without\s+alteration)[^.]{0,100}\.', re.I),
    ]
    for pat in textual_patterns:
        m = pat.search(ann_text)
        if m:
            f['textual_notes'] = clean_ws(m.group(0))
            break

    return f

# =========================================================================
# Main extraction loop
# =========================================================================
hymns_output = []

for hymn_num, start_line, end_line in hymn_ranges:
    block = lines[start_line:end_line]

    # First line of hymn
    first_line = extract_first_line(block)

    # Author
    author_idx, author_name = find_author_in_block(block)

    # Annotation text
    ann_text = extract_annotation_text(block, author_idx)

    # Parse fields from annotation
    fields = parse_annotation(ann_text)

    # Section
    section = get_section(start_line)

    # Meter (clean up)
    meter = clean_ws(meter_map.get(hymn_num, ''))
    # Normalize common OCR meter artifacts
    meter = re.sub(r'\bu\s*M\b', 'L. M.', meter)  # 'u M.' -> 'L. M.'
    meter = re.sub(r'\bL\s+M\b', 'L. M.', meter)
    meter = re.sub(r'\bC\s+M\b', 'C. M.', meter)
    meter = re.sub(r'\bS\s+M\b', 'S. M.', meter)

    hymn_obj = {
        'nutter_hymn_number': hymn_num,
        'first_line': first_line,
        'author': author_name,
        'meter': meter,
        'composition_date': fields['composition_date'],
        'first_published': fields['first_published'],
        'original_stanzas': fields['original_stanzas'],
        'stanzas_in_hymnal': fields['stanzas_in_hymnal'],
        'scripture_basis': fields['scripture_basis'],
        'composition_story': fields['composition_story'],
        'textual_notes': fields['textual_notes'],
        'anecdotes': fields['anecdotes'],
        'tune_name': fields['tune_name'],
        'tune_composer': fields['tune_composer'],
        'critical_assessment': fields['critical_assessment'],
        'topic_section': section,
        '_annotation_sample': ann_text[:500],
    }

    hymns_output.append(hymn_obj)

print(f"\nExtracted {len(hymns_output)} hymn records", file=sys.stderr)

# Show sample
for h in hymns_output[:8]:
    print(f"  #{h['nutter_hymn_number']:3d}: {h['first_line'][:55]:<55} | {h['author'][:30]}", file=sys.stderr)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(hymns_output, f, indent=2, ensure_ascii=False)

print(f"\nOutput written to {OUTPUT_FILE}", file=sys.stderr)
