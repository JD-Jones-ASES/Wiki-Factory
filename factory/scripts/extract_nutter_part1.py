#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, lines 622-30000.
Produces: builds/Hymn_Wiki/wiki/_nutter_hymn_data_part1.json
"""

import re
import json
import sys

INPUT_FILE = r'C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt'
OUTPUT_FILE = r'C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part1.json'

START_LINE = 621   # 0-indexed
END_LINE   = 30000 # exclusive, 0-indexed

# -------------------------------------------------------------------------
# Load file
# -------------------------------------------------------------------------
with open(INPUT_FILE, 'r', encoding='utf-8', errors='replace') as f:
    raw = f.readlines()

lines = [l.rstrip('\n') for l in raw]
print(f"Loaded {len(lines)} lines", file=sys.stderr)

# -------------------------------------------------------------------------
# Utility
# -------------------------------------------------------------------------
def clean(s):
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def is_page_header(s):
    s = s.strip()
    if re.match(r'^(HYMNS\s+(OF|TO|ON|OP|FOR)|ANNOTATED\s+HYMNAL|THE\s+METHODIST)', s, re.I):
        return True
    if re.match(r'^(WORSHIP|CHRISTIAN\s+LIFE|THE\s+GOSPEL|THE\s+CHURCH|THE\s+LORD\s+JESUS)\.?\s*$', s, re.I):
        return True
    if re.match(r'^\d{1,3}\s*$', s):
        return True
    return False

# -------------------------------------------------------------------------
# Section tracking
# -------------------------------------------------------------------------
SECTION_MARKERS = [
    (629, 'Worship'),
    (6960, 'Hymns to the Father'),
    (9386, 'The Lord Jesus Christ'),
    (14953, 'The Holy Spirit'),
    (16169, 'The Holy Scriptures'),
]

def get_section_at(line_idx):
    section = 'Worship'
    for marker_line, marker_section in SECTION_MARKERS:
        if line_idx >= marker_line:
            section = marker_section
    return section

# -------------------------------------------------------------------------
# Identify all hymn boundaries
# -------------------------------------------------------------------------
METER_FULL_RE = re.compile(
    r'^(\d{1,3})\s+'
    r'((?:C|L|S|P|H)\s*\.\s*M\s*\.'
    r'|(?:\d[\d,\s\.]+)+\s*[Dd]\.?'
    r'|[678]s\s*\.?'
    r'|L\s*M\s*\.\s*\d+'
    r'|10,10,11,11\.?'
    r'|8s,7s\.?'
    r')\s*$',
    re.IGNORECASE
)

HYMN_NUM_ALONE_RE = re.compile(r'^\s*(\d{1,3})\s*$')

hymn_starts = []

i = START_LINE
while i < END_LINE and i < len(lines):
    stripped = lines[i].strip()

    # Full hymn header on one line
    m = METER_FULL_RE.match(stripped)
    if m:
        num = int(m.group(1))
        if 1 <= num <= 400:
            meter = re.sub(r'\s+', ' ', m.group(2)).strip()
            hymn_starts.append((i, num, meter))
            i += 1
            continue

    # Standalone number, meter on nearby line
    m2 = HYMN_NUM_ALONE_RE.match(stripped)
    if m2:
        num = int(m2.group(1))
        if 1 <= num <= 400:
            meter = ''
            for j in range(i+1, min(i+8, len(lines))):
                ahead = lines[j].strip()
                if not ahead:
                    continue
                if re.match(r'^((?:C|L|S|P|H)\s*\.\s*M\s*\.'
                            r'|[678]s\s*\.?'
                            r'|[\d,\s\.]{3,}[Dd]?\.?'
                            r')\s*$', ahead, re.I):
                    meter = re.sub(r'\s+', ' ', ahead).strip()
                    break
                if len(ahead) > 40:
                    break
                if is_page_header(ahead):
                    continue
            hymn_starts.append((i, num, meter))
            i += 1
            continue

    i += 1

print(f"Found {len(hymn_starts)} hymn start markers", file=sys.stderr)

# Deduplicate and sort
seen_lines = set()
unique_starts = []
for item in hymn_starts:
    if item[0] not in seen_lines:
        seen_lines.add(item[0])
        unique_starts.append(item)

unique_starts.sort(key=lambda x: x[0])
print(f"After dedup: {len(unique_starts)} hymn starts", file=sys.stderr)

# -------------------------------------------------------------------------
# Process each hymn
# -------------------------------------------------------------------------

def extract_first_line(block, start_offset=1):
    for j in range(start_offset, min(20, len(block))):
        s = block[j].strip()
        if not s:
            continue
        if is_page_header(s):
            continue
        if re.match(r'^(C\.|L\.|S\.|P\.|H\.|[678]s|[\d,\.\s]{2,})\s*$', s, re.I):
            continue
        # Skip stanza numbers > 1
        m_stanza = re.match(r'^(\d+)\s+[A-Z]', s)
        if m_stanza and int(m_stanza.group(1)) > 1:
            continue
        result = clean(s)
        # Fix OCR double-capital at start like "OFOR" -> "O FOR"
        result = re.sub(r'^([A-Z]{2,})', lambda mm: mm.group(0)[0] + ' ' + mm.group(0)[1:], result)
        return result
    return ''

def find_author_line(block):
    author_re = re.compile(
        r'^([A-Z][a-z]+(?:\s+[A-Z]\.?)?\s+[A-Z][a-zA-Z\-\']+(?:,?\s*Jr\.?|,?\s*D\.?D\.?)?)'
        r'(?:\s*\(.*?\))?'
        r'(?:\s*\.?\s*(?:Alt(?:ered)?\.?\s+by\s+[A-Z][a-z]+\s+[A-Z][a-zA-Z]+))?'
        r'\s*\.?\s*$'
    )
    # Also handle "Isaac Watts. Alt. by John Wesley." format
    author_with_alt_re = re.compile(
        r'^([A-Z][a-z]+\s+[A-Z][a-zA-Z]+)(?:\s*\(.*?\))?\s*\.\s*Alt(?:ered)?\.?\s*by\s+(.+)\.\s*$'
    )

    for j in range(5, min(100, len(block))):
        s = block[j].strip()
        if not s or is_page_header(s):
            continue

        m = author_with_alt_re.match(s)
        if m and len(s) < 80:
            if j >= 5:
                return j, clean(s.rstrip('.'))

        m = author_re.match(s)
        if m and len(s) < 70:
            if j >= 5:
                return j, clean(s.rstrip('.'))

    return None, ''

def extract_annotation(block, author_idx):
    if author_idx is not None:
        ann_lines = block[author_idx+1:]
    else:
        # Find start of prose
        for j in range(5, min(60, len(block))):
            s = block[j].strip()
            if not s:
                continue
            if re.match(r'^(This|The|From|Author|It\s|He\s|She\s|These|A\s|An\s)', s):
                if j >= 8:
                    ann_lines = block[j:]
                    break
        else:
            ann_lines = block[20:]

    return clean(' '.join(l.strip() for l in ann_lines if not is_page_header(l.strip())))

def parse_fields(ann_text, author_name):
    fields = {
        'author': author_name,
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
    scripture_re = re.compile(
        r'(?:based\s+on|basis\s+is|paraphrase\s+of)\s+([^.]{5,60})',
        re.I
    )
    m = scripture_re.search(ann_text)
    if m:
        fields['scripture_basis'] = clean(m.group(0))

    # First published - look for "first appeared in X, YYYY" or "From X, YYYY"
    pub_patterns = [
        re.compile(r'(?:first\s+appeared\s+in|published\s+in|appeared\s+in|from)\s+(?:the\s+)?(?:author.s\s+)?([^,\.]{5,60},?\s*\d{4})', re.I),
        re.compile(r'(?:From|In)\s+([A-Z][^,\.]{5,60}(?:,|\.)\s*\d{4})', re.I),
    ]
    for pat in pub_patterns:
        m = pat.search(ann_text)
        if m:
            fields['first_published'] = clean(m.group(0))
            break

    # Original stanza count
    stanza_count_re = re.compile(
        r'(?:original(?:ly)?\s+(?:contained|comprised|had)|contained|comprises?)\s+'
        r'(\w+(?:-\w+)?)\s+stanza',
        re.I
    )
    m = stanza_count_re.search(ann_text)
    if m:
        fields['original_stanzas'] = clean(m.group(0))

    # Composition date
    date_patterns = [
        re.compile(r'written\s+(?:in|on)?\s*([A-Z][a-z]+\s+\d+,?\s*\d{4})', re.I),
        re.compile(r'written\s+in\s+(\d{4})', re.I),
        re.compile(r'composed\s+in\s+(\d{4})', re.I),
    ]
    for pat in date_patterns:
        m = pat.search(ann_text)
        if m:
            fields['composition_date'] = clean(m.group(1))
            break

    # Tune name
    tune_re = re.compile(r'tune\s+(?:known\s+as\s+)?["\"]([A-Za-z\s]+)["\"]', re.I)
    m = tune_re.search(ann_text)
    if m:
        fields['tune_name'] = clean(m.group(1))

    # Critical assessment (look for quoted praise/criticism)
    crit_re = re.compile(r'"([^"]{20,150})"', re.I)
    m = crit_re.search(ann_text)
    if m:
        fields['critical_assessment'] = clean(m.group(1))

    return fields

hymns = []

for idx, (start_line, hymn_num, meter_raw) in enumerate(unique_starts):
    if idx + 1 < len(unique_starts):
        end_line = unique_starts[idx + 1][0]
    else:
        end_line = min(start_line + 300, END_LINE, len(lines))

    block = lines[start_line:end_line]

    # Extract first line
    first_line = extract_first_line(block)

    # Find author
    author_idx, author_name = find_author_line(block)

    # Extract annotation
    ann_text = extract_annotation(block, author_idx)

    # Parse fields
    fields = parse_fields(ann_text, author_name)

    # Section
    section = get_section_at(start_line)

    # Clean meter
    meter = re.sub(r'\s+', ' ', meter_raw).strip().rstrip('.')

    hymn_obj = {
        'nutter_hymn_number': hymn_num,
        'first_line': first_line,
        'author': fields['author'],
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
        '_raw_annotation_sample': ann_text[:600],
    }

    hymns.append(hymn_obj)

print(f"Extracted {len(hymns)} hymns", file=sys.stderr)
for h in hymns[:5]:
    print(f"  #{h['nutter_hymn_number']}: '{h['first_line'][:50]}' / author={h['author']}", file=sys.stderr)

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(hymns, f, indent=2, ensure_ascii=False)

print(f"Written to {OUTPUT_FILE}", file=sys.stderr)
