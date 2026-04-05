#!/usr/bin/env python3
"""
Extract hymn annotation data from Nutter.txt, lines 622-30000.
Version 3: Handles extensive OCR artifacts.
Produces: builds/Hymn_Wiki/wiki/_nutter_hymn_data_part1.json
"""

import re
import json
import sys

INPUT_FILE = r'C:\Wiki_Factory\builds\Hymn_Wiki\raw\Nutter.txt'
OUTPUT_FILE = r'C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_nutter_hymn_data_part1.json'

START_LINE = 621   # 0-indexed
END_LINE   = 30001

with open(INPUT_FILE, 'r', encoding='utf-8', errors='replace') as f:
    raw = f.readlines()
lines = [l.rstrip('\n') for l in raw]
total_lines = len(lines)
print(f"Loaded {total_lines} lines", file=sys.stderr)

# =========================================================================
# OCR normalization
# =========================================================================
def clean_ws(s):
    return re.sub(r'\s+', ' ', s).strip()

def is_page_header(s):
    s = s.strip()
    patterns = [
        r'^ANNOTATED\s+HYMNAL',
        r'^HYMNS\s+(OF|TO|ON|OP|FOR)',
        r'^THE\s+METHODIST',
        r'^WORSHIP\.?\s*$',
        r'^THE\s+CHRISTIAN\s+LIFE\.?\s*$',
        r'^THE\s+LORD\s+JESUS',
        r'^THE\s+SON\.?\s*\d*\s*$',
        r'^THE\s+GOSPEL',
        r'^THE\s+CHURCH',
        r'^THE\s+HOLY\s+SPIRIT',
        r'^THE\s+HOLY\s+SCRIPTURES',
        r'^TIMES\s+AND\s+SEASONS',
        r'^THE\s+FUTURE\s+LIFE',
        r'^FATHER\.?\s*\d*\s*$',
    ]
    for p in patterns:
        if re.match(p, s, re.I):
            return True
    return False

def is_page_number_line(line_idx):
    """True if standalone number at line_idx is a book page number."""
    s = lines[line_idx].strip()
    if not re.match(r'^\d{1,3}$', s):
        return False
    for j in range(line_idx+1, min(line_idx+5, total_lines)):
        ahead = lines[j].strip()
        if not ahead:
            continue
        if re.match(r'^ANNOTATED\s+HYMNAL', ahead, re.I):
            return True
        break
    return False

# =========================================================================
# Pre-normalize lines for number detection
# OCR artifacts in hymn numbers:
#   "Ill" = "111", "^2" = "72", "l" = "1", "I" = "1" at line start
# =========================================================================

def normalize_line_for_hymn_detection(s):
    """Try to normalize OCR artifacts in potential hymn header lines."""
    s_stripped = s.strip()

    # "Ill  7s. D." -> "111  7s. D."
    s_stripped = re.sub(r'^Ill\b', '111', s_stripped)

    # "^2  meter" -> "72  meter"
    s_stripped = re.sub(r'^\^(\d)', r'7\1', s_stripped)

    # "l9  meter" -> "19  meter" (lowercase l before digit)
    s_stripped = re.sub(r'^l(\d)', r'1\1', s_stripped)

    return s_stripped

# =========================================================================
# Meter normalization
# =========================================================================
def normalize_meter(s):
    s = clean_ws(s)
    # OCR artifacts in meters
    s = re.sub(r'\bL-\s*M\b', 'L. M.', s)   # 'L- M.' -> 'L. M.'
    s = re.sub(r'\bI-\s*M\b', 'L. M.', s)   # 'I- M.' -> 'L. M.'
    s = re.sub(r'\bu\s+M\b', 'L. M.', s)    # 'u M.' -> 'L. M.'
    s = re.sub(r'\bl\s*M\b', 'L. M.', s)    # 'l M.' -> 'L. M.'
    s = re.sub(r'\bL\s+M\b', 'L. M.', s)
    s = re.sub(r'\bC\s+M\b', 'C. M.', s)
    s = re.sub(r'\bS\s+M\b', 'S. M.', s)
    # "lis" = "11s", "lOs" = "10s"
    s = re.sub(r'\blis\b', '11s', s)
    s = re.sub(r'\blOs\b', '10s', s)
    s = re.sub(r'\bSs\b', '8s', s)
    s = re.sub(r'\b6L\b', '6D', s)   # "6L" likely "6D"
    s = re.sub(r'\b61\b', '6s', s)   # "61" could be "6s"
    return s.rstrip('.,')

# =========================================================================
# Detect hymn header lines
# =========================================================================

# Full meter pattern (lenient to catch variants)
def looks_like_meter(s):
    """Return True if s appears to be a hymn meter specification."""
    s = s.strip()
    if len(s) < 2 or len(s) > 50:
        return False

    # Normalize OCR artifacts before checking
    sn = s
    sn = re.sub(r'\blis\b', '11s', sn, flags=re.I)
    sn = re.sub(r'\blOs\b', '10s', sn, flags=re.I)
    sn = re.sub(r'\bSs\b', '8s', sn, flags=re.I)
    # '88' in meter context usually means '8s' or '8,8'
    sn = re.sub(r'\b88\b(?!,)', '8s', sn)
    # 'G' in digit list -> '6'
    sn = re.sub(r'\bG\b', '6', sn)
    # 's. M,' at START -> 'S. M.' (OCR dropped capital S, comma for period)
    if re.match(r'^s\s*\.\s*[Mm]', sn):
        sn = sn[0].upper() + sn[1:]  # capitalize first char only
    # Replace commas with periods in meter strings (OCR artifact)
    sn = re.sub(r',\s*$', '.', sn)  # trailing comma -> period
    # 'I-  M.' -> 'L. M.'  (I- is OCR for L.)
    sn = re.sub(r'^I-\s*', 'L. ', sn)
    # Remove non-ASCII OCR artifacts before pattern matching
    sn = re.sub(r'[^\x00-\x7F]', '', sn)
    # Garbled meters like 'ii  ii  11. 5.' - contain non-digit non-letter garbage
    # If string has lots of non-alphanumeric chars, skip
    non_alph = len(re.findall(r'[^0-9A-Za-z\s\.,]', sn))
    if non_alph >= 2:
        return False
    # If string contains letter sequences that aren't meter abbrevs, skip
    # e.g. 'ii ii 11. 5.' has 'ii' which is garbled
    # But we keep 's', 'D', 'M', 'C', 'L', 'S', 'P', 'H', 'Irregular' as valid
    if re.search(r'Irregular', sn, re.I):
        pass  # 'Irregular' is a valid meter qualifier, don't check further
    else:
        letter_only = re.sub(r'[0-9\s\.,]', '', sn)
        if re.search(r'[a-z]{2,}', letter_only, re.I):
            # Contains letter runs - check if they're all valid abbrevs
            suspicious = re.sub(r'[sDMLCPH]', '', letter_only, flags=re.I)
            if re.search(r'[a-zA-Z]{2,}', suspicious):
                return False

    patterns = [
        r'^[CLSPHclsp]\s*[\.\s-]\s*[Mm]\s*\.?\s*[Dd]?\.?\s*\d*\.?$',  # C.M., L.M., L.M.61., S.M.D.
        r'^[CLSPHuIl]\s*[Mm]\.?\s*\d*\.?$',                             # LM. uM.
        r'^[1-9][0-9]?s[\.,]?\s*[1-9]?[0-9]?s?[\.,]?\s*[Dd]?\.?$',    # 7s., 11s., 10s., etc.
        r'^[1-9][0-9]?s[\.,]?\s*[1-9][0-9]?s[\.,]?\s*[Dd]?\.?$',       # 8s,7s.
        r'^[\d,\s\.]{4,}(?:[Dd]\.?)?$',                                  # 6,6,8,4. D.
        r'^10,10,11,11',
        r'^\d{1,2}[\.,]\s*\d{1,2}[\.,]',                                 # digit,digit patterns
        r'^[78][.,]?[78][.,]?$',                                          # 78., 7.8.
        r'^\d{1,2}s[\.,]?\s*\d{1,2}s[\.,]',                              # 8s,7s,
        r'Irregular',
        r'^[1-9][0-9]?\s*s\s*[\.,]',                                      # "5s." "9s." "7s,"
        r'^\d{2,3}\s*[\.,]',                                              # "88," "88."
    ]
    for p in patterns:
        if re.match(p, sn, re.I):
            return True
    return False

HYMN_HEADER_RE = re.compile(
    r'^(\d{1,3})\s*:?\s+'
    r'(.+)$'
)

hymn_map = {}   # hymn_num -> line_idx
meter_map = {}  # hymn_num -> meter string

# Manual overrides for hymns with completely garbled OCR headers
# Format: (0-indexed line number, hymn_number, meter_string)
MANUAL_HYMN_OVERRIDES = [
    (5585, 58, '11. 11. 11. 5.'),   # '58  ii  ii  11.  5.' - "NOW GOD be with us"
]

i = START_LINE
while i < END_LINE and i < total_lines:
    original = lines[i]
    stripped = original.strip()
    normalized = normalize_line_for_hymn_detection(stripped)

    # Try: normalized line starts with number, rest looks like meter
    m = HYMN_HEADER_RE.match(normalized)
    if m:
        num = int(m.group(1))
        rest = m.group(2).strip()
        if 1 <= num <= 400 and looks_like_meter(rest):
            if num not in hymn_map:
                hymn_map[num] = i
                meter_map[num] = normalize_meter(rest)
            i += 1
            continue

    # Standalone number line
    m2 = re.match(r'^(\d{1,3})\s*$', normalized)
    if m2:
        num = int(m2.group(1))
        if 1 <= num <= 400 and not is_page_number_line(i):
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
                meter_map[num] = normalize_meter(meter) if meter else ''
        i += 1
        continue

    i += 1

# Apply manual overrides
for line_idx, num, meter in MANUAL_HYMN_OVERRIDES:
    if num not in hymn_map:
        hymn_map[num] = line_idx
        meter_map[num] = meter

hymn_locs = sorted(hymn_map.items(), key=lambda x: x[1])
nums_found = [n for n,_ in hymn_locs]
print(f"Detected {len(hymn_locs)} hymns", file=sys.stderr)
print(f"Range: {min(nums_found)} to {max(nums_found)}", file=sys.stderr)
missing_1_200 = [n for n in range(1, 201) if n not in hymn_map]
if missing_1_200:
    print(f"Missing 1-200: {missing_1_200}", file=sys.stderr)

# =========================================================================
# Section tracking
# =========================================================================
SECTION_MAP = {
    r'HYMNS\s+OF\s+WORSHIP': 'Worship',
    r'WORSHIP\.?\s*$': 'Worship',
    r'HYMNS\s+TO\s+THE\s+FATHER': 'Hymns to the Father',
    r'FATHER\s+\d': 'Hymns to the Father',
    r'HYMNS\s+TO\s+THE\s+SON|LORD\s+JESUS|THE\s+SON\.': 'The Lord Jesus Christ',
    r'HYMNS\s+TO\s+THE\s+HOLY\s+SPIRIT|THE\s+HOLY\s+SPIRIT': 'The Holy Spirit',
    r'HYMNS\s+ON\s+THE\s+HOLY\s+SCRIPTURES|THE\s+HOLY\s+SCRIPTURES': 'The Holy Scriptures',
    r'HYMNS\s+ON\s+THE\s+CHRISTIAN\s+LIFE|THE\s+CHRISTIAN\s+LIFE': 'The Christian Life',
    r'THE\s+CHURCH': 'The Church',
    r'THE\s+GOSPEL': 'The Gospel',
    r'TIMES\s+AND\s+SEASONS': 'Times and Seasons',
    r'THE\s+FUTURE\s+LIFE': 'The Future Life',
}

# Build section lookup
section_changes = []  # (line_idx, section_name)
for i in range(START_LINE, min(END_LINE, total_lines)):
    s = lines[i].strip()
    for pat, name in SECTION_MAP.items():
        if re.search(pat, s, re.I) and len(s) < 60:
            section_changes.append((i, name))
            break

section_changes.sort()

def get_section(line_idx):
    section = 'Worship'
    for idx, name in section_changes:
        if idx <= line_idx:
            section = name
        else:
            break
    return section

# =========================================================================
# Build hymn ranges
# =========================================================================
hymn_ranges = []
for idx, (hymn_num, start_line) in enumerate(hymn_locs):
    if idx + 1 < len(hymn_locs):
        end_line = hymn_locs[idx+1][1]
    else:
        end_line = min(start_line + 400, END_LINE, total_lines)
    hymn_ranges.append((hymn_num, start_line, end_line))

# =========================================================================
# Extract fields from a hymn block
# =========================================================================

def extract_first_line(block):
    for j in range(1, min(25, len(block))):
        s = block[j].strip()
        if not s:
            continue
        if is_page_header(s):
            continue
        if looks_like_meter(s):
            continue
        # Skip stanza numbers >= 2
        m = re.match(r'^(\d+)\s+[A-Z]', s)
        if m and int(m.group(1)) >= 2:
            continue
        # Skip single/few char OCR dropped capitals
        if len(s) <= 4 and re.match(r'^[A-Z"\'\^!]+$', s):
            continue
        result = clean_ws(s)
        return result
    return ''

def find_author(block):
    """Find author attribution line in hymn block.

    Strategy: scan for a short line (< 80 chars) that:
    1. Starts with a capital letter
    2. Looks like one or more proper names (optionally with Alt./Tr. by)
    3. Is followed within 3 lines by annotation prose OR is the last
       short line before longer prose
    """
    # Primary author pattern (strict)
    author_re = re.compile(
        r'^([A-Z][a-z]+(?:\s+[A-Z]\.?)?\s+[A-Z][a-zA-Z\-\']+(?:,?\s*(?:Jr\.|D\.D\.|LL\.D\.|M\.D\.))?)'
        r'(?:\s*\(.*?\))?'
        r'(?:\s*[,.]?\s*(?:Alt(?:ered)?\.?\s*(?:by\s+.{0,50})?|Tr\.?\s*(?:by\s+.{0,50})?|Trans\.?\s*(?:by\s+.{0,50})?))?'
        r'\s*[.,]?\s*$'
    )
    # Secondary: looser match for OCR-garbled names
    # Must be short, start with capital, end with comma/period, and
    # be followed by annotation prose
    PROSE_STARTERS = re.compile(
        r'^(This\s|The\s|From\s|It\s+is|He\s+was|He\s+had|Author|Based|Written|Title|'
        r'Published|In\s+\d|These|A\s+(?:hymn|poem|beautiful|grand|great)|'
        r'Among|One\s+of|Perhaps)',
        re.I
    )

    for j in range(4, min(150, len(block))):
        s = block[j].strip()
        if not s or is_page_header(s):
            continue

        # Primary match
        m = author_re.match(s)
        if m and 4 <= len(s) <= 80:
            return j, clean_ws(re.sub(r'[,.]$', '', s))

        # Secondary: short line ending in period/comma, followed by prose
        # Must look like a proper name (capitalized words, no common hymn words)
        if (4 <= len(s) <= 80 and
                re.match(r'^[A-Z]', s) and
                re.search(r'[.,]\s*$', s)):
            # Check it looks like a name (not a hymn line or prose)
            words = s.rstrip('.,').split()
            if len(words) <= 6:
                cap_words = sum(1 for w in words if re.match(r'^[A-Z]', w))
                common_words = {'all', 'the', 'of', 'thy', 'his', 'her', 'our', 'your',
                                'their', 'my', 'by', 'in', 'to', 'for', 'and', 'but',
                                'or', 'not', 'with', 'from', 'that', 'this', 'which',
                                'are', 'were', 'was', 'let', 'him', 'them', 'us', 'ye',
                                'he', 'she', 'it', 'we', 'on', 'at', 'as', 'so', 'up'}
                has_common = any(w.lower().rstrip('.,') in common_words for w in words)
                if cap_words >= 2 and not has_common:
                    # Check next non-empty line is annotation prose
                    for k in range(j+1, min(j+4, len(block))):
                        nxt = block[k].strip()
                        if not nxt:
                            continue
                        if PROSE_STARTERS.match(nxt) or is_page_header(nxt):
                            return j, clean_ws(re.sub(r'[,.]$', '', s))
                        break

    return None, ''

def get_annotation(block, author_idx):
    start = author_idx + 1 if author_idx is not None else 20
    pieces = []
    for j in range(start, len(block)):
        s = block[j].strip()
        if s and not is_page_header(s):
            pieces.append(s)
    return clean_ws(' '.join(pieces))

def parse_fields(ann):
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

    # Scripture
    for pat in [
        r'based\s+on\s+([A-Za-z][a-z]+\s+[\w\.\s:,]+?)(?:\.|;|$)',
        r'(?:paraphrase|version)\s+of\s+([A-Za-z][a-z]+\s+[\w\.\s:,]+?)(?:\.|;|$)',
        r'scripture\s+basis\s+is\s+([^.]{5,60})',
    ]:
        m = re.search(pat, ann, re.I)
        if m:
            f['scripture_basis'] = clean_ws(m.group(1))
            break

    # First published
    for pat in [
        r'(?:first\s+appeared|published)\s+in\s+(?:the\s+)?(?:author.s\s+)?([^,\.]{8,70},?\s*\d{4})',
        r'[Ff]rom\s+(?:the\s+)?(?:author.s\s+)?([A-Z][^,\.]{5,60}(?:,\s*|\s)\d{4})',
        r'[Ii]n\s+((?:[A-Z][a-z]+\s+){1,4}(?:Hymns?|Poems?|Book|Collection|Psalms?)[^,\.]{0,30},?\s*\d{4})',
    ]:
        m = re.search(pat, ann)
        if m:
            f['first_published'] = clean_ws(m.group(0))
            break

    # Original stanza count
    for pat in [
        r'(?:eighteen|seventeen|sixteen|fifteen|fourteen|thirteen|twelve|eleven|ten|nine|eight|seven|six|five)\s+stanzas?',
        r'(\d+)\s+stanzas?\s+(?:in\s+all|originally|altogether)',
        r'originally\s+(?:contained|comprised|had)\s+(\w+|\d+)\s+stanzas?',
        r'poem\s+(?:of|containing|with)\s+(\d+|\w+)\s+stanzas?',
    ]:
        m = re.search(pat, ann, re.I)
        if m:
            f['original_stanzas'] = clean_ws(m.group(0))
            break

    # Composition date
    for pat in [
        r'written\s+(?:in\s+|on\s+)?([A-Z][a-z]+\s+\d+,?\s*\d{4})',
        r'written\s+in\s+(\d{4})',
        r'composed\s+(?:in\s+)?(\d{4})',
        r'(?:written|composed)\s+(?:about|circa|c\.)\s*(\d{4})',
    ]:
        m = re.search(pat, ann, re.I)
        if m:
            f['composition_date'] = clean_ws(m.group(1))
            break

    # Tune name
    for pat in [
        r'tune\s+(?:known\s+as\s+|called\s+)?["\u201c\*]([A-Za-z][A-Za-z\s\-]{2,30})["\u201d\*]',
        r'named\s+["\u201c]([A-Za-z\s\-]+)["\u201d]',
        r'sung\s+to\s+(?:the\s+tune\s+(?:of\s+)?)?["\u201c]([A-Za-z\s\-]+)["\u201d]',
        r'appropriately\s+named\s+["\u201c\*]?([A-Za-z\s\-]+)["\u201d\*]?',
    ]:
        m = re.search(pat, ann, re.I)
        if m:
            f['tune_name'] = clean_ws(m.group(1))
            break

    # Critical assessment (substantial quoted evaluation)
    crit_found = []
    for m in re.finditer(r'["\u201c]([A-Z][^"]{20,250})["\u201d]', ann):
        text = m.group(1)
        if re.search(r'\bhymn\b|\bpoem\b|\bverse\b|\bsong\b|\blanguage\b|\bauthor\b', text, re.I):
            crit_found.append(clean_ws(text))
    if crit_found:
        f['critical_assessment'] = crit_found[0]

    # Composition story
    for pat in [
        r'(?:written\s+while|composed\s+while|written\s+at\s+the|inspired\s+by|on\s+the\s+occasion)[^.]{10,250}\.',
        r'(?:anniversary|first\s+anniversary)[^.]{10,150}\.',
    ]:
        m = re.search(pat, ann, re.I)
        if m:
            f['composition_story'] = clean_ws(m.group(0))
            break

    # Textual notes
    for pat in [
        r'(?:unaltered(?:\s+except)?|unaltered,?\s+from)[^.]{0,150}\.',
        r'(?:author\s+wrote|originally\s+read|changed\s+(?:by|from)|altered\s+(?:by|from))[^.]{10,200}\.',
    ]:
        m = re.search(pat, ann, re.I)
        if m:
            f['textual_notes'] = clean_ws(m.group(0))
            break

    return f

# =========================================================================
# Main extraction
# =========================================================================
hymns_output = []

for hymn_num, start_line, end_line in hymn_ranges:
    block = lines[start_line:end_line]
    first_line = extract_first_line(block)
    author_idx, author_name = find_author(block)
    ann_text = get_annotation(block, author_idx)
    fields = parse_fields(ann_text)
    section = get_section(start_line)
    meter = meter_map.get(hymn_num, '')

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
print("\nSample records:", file=sys.stderr)
for h in hymns_output[:12]:
    print(f"  #{h['nutter_hymn_number']:3d}: '{h['first_line'][:50]:<50}' | {h['author'][:30]}", file=sys.stderr)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(hymns_output, f, indent=2, ensure_ascii=False)

print(f"\nWritten to {OUTPUT_FILE}", file=sys.stderr)
