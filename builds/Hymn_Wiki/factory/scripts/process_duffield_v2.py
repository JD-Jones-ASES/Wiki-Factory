#!/usr/bin/env python3
"""
process_duffield_v2.py  -- Improved extraction from Duffield (1886)
Produces _duffield_hymn_data.json with rich per-hymn objects.
"""

import re, json, sys
from pathlib import Path

INPUT  = Path(r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Duffield.txt")
OUTPUT = Path(r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_duffield_hymn_data.json")

# ──────────────────────────────────────────────────────────────────────────────
#  Text cleaning
# ──────────────────────────────────────────────────────────────────────────────

PAGE_HDR = re.compile(
    r'^(?:ENGLISH\s+HYMNS?\.?\s*\d*|\d+\s+ENGLISH\s+HYMNS?\.?)$', re.I)

def clean(line: str) -> str | None:
    """Strip OCR noise; return None for lines to discard."""
    s = line.strip()
    if not s:
        return None
    if PAGE_HDR.match(s):
        return None
    if re.match(r'^\d+$', s):        # standalone page numbers
        return None
    return re.sub(r'  +', ' ', s)   # collapse double-spaces


# ──────────────────────────────────────────────────────────────────────────────
#  Entry-header detection
# ──────────────────────────────────────────────────────────────────────────────

# Split on an em-dash (—), en-dash (–), or a hyphen surrounded by spaces.
# We also handle the OCR artifact ".-" (period then hyphen, no space).
DASH_SPLIT = re.compile(r'\s*[—–]\s*|\s+-\s+')

# Known false-positive first-line fragments (body-text phrases that slip through)
PROSE_FRAGMENTS = {
    'his education', 'her education', 'cennick\'s history',
    'berridge, early', 'caleb evans', 'dr. beman',
    'dr. hatfield', 'dr. thomas gibbons', 'fifty-second regiment',
    'gospel hymns —', 'his son. christian', 'hitchcock, eddy',
    'it is entitled', 'may 28th', 'middlesex. her',
    'the baptistery', 'this is ps.', 'two scriptures',
    'v. i', 'when i shall meet thee again —', 'wolcott manorial',
    'oliver holden —', 'bernard barton —', 'a braver becket',
    'after his education', 'and cennick', 'anglican church',
    'april, 1797', 'cennick, 1745',
    'safety in christ alone — john',   # subtitle mis-parsed
    'holy, holy, holy lord— god',       # absorbed into previous entry
    'holy, holy, holy lord — god',
}

# Prose-indicator words that appear in the middle of author fields
PROSE_CONNECTIVES = {'a','an','the','and','or','but','in','of','to','is',
                     'was','with','as','at','by','for','from','who','which',
                     'that','his','her','their','he','she','it','this',
                     'have','had','been','not','are','were'}

def is_header(line: str) -> tuple[bool, str, str]:
    """
    Return (True, first_line, author) if this looks like a Duffield entry header.
    A header: starts uppercase, has a dash-attribution, attribution is name-like.
    """
    if not line or len(line) > 160:
        return False, '', ''

    # Must start with an uppercase letter
    if not re.match(r'^[A-Z]', line):
        return False, '', ''

    # Split on em/en dash or spaced hyphen
    parts = DASH_SPLIT.split(line, maxsplit=1)
    if len(parts) < 2:
        return False, '', ''

    first, attr = parts[0].strip(' .,;:'), parts[1].strip(' .,;:')

    # first part: 3-10 words, 8-100 chars
    if len(first) < 8 or len(first) > 105:
        return False, '', ''
    fw = first.split()
    if len(fw) < 3 or len(fw) > 14:
        return False, '', ''

    # attribution: 1-7 words, 2-55 chars, starts uppercase
    if len(attr) < 2 or len(attr) > 60:
        return False, '', ''
    aw = attr.split()
    if len(aw) > 7:
        return False, '', ''
    if not re.match(r'^[A-Z]', attr):
        return False, '', ''

    # Reject if attribution looks like prose (>2 connective words in middle)
    mid_prose = sum(1 for w in aw[1:-1] if w.lower().rstrip('.,;:') in PROSE_CONNECTIVES)
    if mid_prose > 1:
        return False, '', ''

    # Reject known false-positive fragments
    fl_lower = first.lower()
    for frag in PROSE_FRAGMENTS:
        if frag in fl_lower:
            return False, '', ''

    # Reject if author field looks like a scripture ref (John 6 : 68)
    if re.match(r'^[A-Z][a-z]+\s+\d+\s*[:\-]\s*\d+', attr):
        return False, '', ''

    return True, first, attr


# ──────────────────────────────────────────────────────────────────────────────
#  First-line normalisation
# ──────────────────────────────────────────────────────────────────────────────

# Known OCR-garbled first lines (raw -> corrected)
FIRSTLINE_FIXES = {
    "A I'Kw more ycixrs shall roll": "A few more years shall roll",
    "A I Kw more ycixrs shall roll": "A few more years shall roll",
}

def normalise_first_line(raw: str) -> str:
    """Convert OCR-spaced ALL-CAPS first line to Title Case."""
    raw = raw.strip(' .,;:!')

    # Apply known OCR corrections before anything else
    for bad, good in FIRSTLINE_FIXES.items():
        if raw == bad:
            return good

    words = raw.split()
    result = []
    for w in words:
        # Preserve single-letter words (A, I, O)
        if len(w) == 1 and w.isupper():
            result.append(w)
            continue
        # If fully uppercase (excluding punctuation), title-case it
        alpha = re.sub(r'[^A-Za-z]', '', w)
        if alpha and alpha.isupper():
            result.append(w[0].upper() + w[1:].lower())
        else:
            result.append(w)
    return ' '.join(result)


# ──────────────────────────────────────────────────────────────────────────────
#  Author normalisation
# ──────────────────────────────────────────────────────────────────────────────

# Author abbreviation expansions
AUTHOR_FIXES = {
    'Boxar':  'Bonar',
    'Bottar': 'Bonar',
    'HK.ncK': 'Hedge',
    'Hkdgk': 'Hedge',
    'Hcdgc': 'Hedge',
    'Newtox': 'Newton',
    'Moxtgomkry': 'Montgomery',
    'Wkslky': 'Wesley',
    'Chaulks': 'Charles Wesley',
    'Watts.': 'Watts',
    'Cowpkr': 'Cowper',
    'Monlgomery': 'Montgomery',
    'Doddridgk': 'Doddridge',
    'Bcnar': 'Bonar',
    'Bonab': 'Bonar',
}

def normalise_author(raw: str) -> str:
    raw = raw.strip(' .,;:')

    # Fix OCR-garbled translation marker: "/r", "//-", "//'" → "tr."
    # Pattern: author name, comma, then /r or //* variants
    raw = re.sub(r',?\s*/[r/\'\-]+$', ', tr.', raw)
    raw = re.sub(r',?\s*//\s*$', ', tr.', raw)

    # Remove trailing translation markers (clean form)
    raw = re.sub(r',?\s*(?:tr\.|trans\.|from\s+the\s+\w+)\s*$', '', raw, flags=re.I)
    raw = re.sub(r',?\s+tr\.$', '', raw, flags=re.I)
    raw = raw.strip(' .,;:')

    # Apply known OCR fixes
    for bad, good in AUTHOR_FIXES.items():
        if raw == bad:
            raw = good
            break
        # Also check word-boundary match
        raw = re.sub(r'\b' + re.escape(bad) + r'\b', good, raw)

    return raw



# ──────────────────────────────────────────────────────────────────────────────
#  Field extractors
# ──────────────────────────────────────────────────────────────────────────────

SCRIPTURE_RE = re.compile(
    r'\b(?:Gen(?:esis)?|Ex(?:odus)?|Lev(?:iticus)?|Num(?:bers)?|Deut(?:eronomy)?|'
    r'Josh(?:ua)?|Judg(?:es)?|[12]\s*Sam(?:uel)?|[12]\s*Kings?|[12]\s*Chr(?:on)?|'
    r'Ezra|Neh(?:emiah)?|Esth(?:er)?|Job|Ps(?:alms?|\.\s*\d)?|Prov(?:erbs)?|'
    r'Eccl(?:es)?|Isa(?:iah)?|Jer(?:emiah)?|Lam(?:entations)?|Ezek(?:iel)?|'
    r'Dan(?:iel)?|Hos(?:ea)?|Joel|Amos|Mic(?:ah)?|Nah(?:um)?|Hab|Zeph|Hag|'
    r'Zech(?:ariah)?|Mal(?:achi)?|Matt(?:hew)?|Mark|Luke|John|Acts|Rom(?:ans)?|'
    r'[12]\s*Cor(?:inthians)?|Gal(?:atians)?|Eph(?:esians)?|Phil(?:ippians)?|'
    r'Col(?:ossians)?|[12]\s*Thess?|[12]\s*Tim(?:othy)?|Tit(?:us)?|Heb(?:rews)?|'
    r'Jas(?:ames)?|[12]\s*Pet(?:er)?|[123]\s*John|Jude|Rev(?:elation)?)'
    r'\s+\d+\s*[:\-]\s*\d+',
    re.I
)

def extract_scripture(text: str) -> str:
    refs = list(dict.fromkeys(SCRIPTURE_RE.findall(text)))  # dedupe preserving order
    return '; '.join(refs[:5])  # cap at 5


TUNE_CONTEXT = re.compile(
    r'(?:tune[sd]?|sung\s+to|set\s+to|air|melody|music)\s+(?:of\s+|called\s+|named\s+|'
    r'entitled\s+|known\s+as\s+)?["\'""\u2018\u2019]([^"\'""]+)["\'""\u2019]',
    re.I
)
TUNE_QUOTED = re.compile(r'["\'""\u2018\u2019]([A-Z][A-Za-z\s\.]{2,30})["\'""\u2019]')

def extract_tune(text: str) -> str:
    tunes = []
    for m in TUNE_CONTEXT.finditer(text):
        t = m.group(1).strip()
        if t and len(t) < 50:
            tunes.append(t)
    if not tunes:
        # Fallback: look for short capitalized quoted strings near tune words
        for m in TUNE_QUOTED.finditer(text):
            ctx = text[max(0, m.start()-60):m.start()]
            if any(w in ctx.lower() for w in ['tune', 'air', 'melody', 'sung', 'set']):
                tunes.append(m.group(1).strip())
    # Also look for bare tune names like 'tune "HANOVER"'
    bare = re.findall(r'tune\s+"([A-Z][A-Z\s\.]{2,20})"', text)
    tunes.extend(bare)
    seen = []
    for t in tunes:
        if t not in seen:
            seen.append(t)
    return '; '.join(seen[:3])


def extract_year(text: str) -> str:
    """Return the earliest plausible composition year (1300-1890)."""
    years = [int(y) for y in re.findall(r'\b(1[3-8]\d\d)\b', text)
             if 1300 <= int(y) <= 1890]
    return str(min(years)) if years else ''


def extract_publication(text: str) -> str:
    """Extract the most likely first-publication details."""
    patterns = [
        # "From Hymns of Faith and Hope, 1857"
        r'[Ff]rom\s+([A-Z][^,\.;\n]{5,60}?),?\s+(\d{4})',
        # "first published in Olney Hymns, 1779"
        r'(?:first\s+published|published|appeared)\s+in\s+([^,\.\n]{5,60}?),?\s+(\d{4})',
        # "it is No. 188 of Charles Wesley's Short Scripture Hymns, 1762"
        r'No\.\s*\d+\s+of\s+([^,\.\n]{5,60}?),?\s+(\d{4})',
        # "in his Spiritual Songs, 1831-33"
        r'in\s+(?:his|her|the)\s+([A-Z][^,\.\n]{5,55}?),?\s+(\d{4})',
        # "the collection published in 1827"
        r'(?:collection|volume|book)\s+published\s+in\s+(\d{4})',
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            if len(m.groups()) >= 2:
                title = m.group(1).strip(' .,;:')
                year  = m.group(2)
                if 5 < len(title) < 80:
                    return f"{title}, {year}"
            else:
                return m.group(1)
    return ''


def extract_textual_notes(text: str) -> str:
    """Collect notes about alterations, stanzas, attribution disputes."""
    patterns = [
        r'(origin(?:al(?:ly)?)\s+(?:possessed|has|had|contains?)\s+[^.]{10,120}\.)',
        r'((?:eight|six|four|five|seven|nine|ten|\d+)\s+stanzas?[^.]{0,60}\.)',
        r'((?:altered|omit|attributed?|disputed?|ascribed?)[^.]{10,150}\.)',
        r'((?:first|second|third)\s+stanza[^.]{10,80}\.)',
    ]
    notes = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            note = m.group(1).strip()
            if note not in notes and len(note) < 250:
                notes.append(note)
            if len(notes) >= 2:
                break
    return ' | '.join(notes[:2])


COMPOSITION_KW = [
    'composed', 'written', 'wrote', 'pen', 'origin',
    'occasion', 'circumstance', 'he composed', 'she composed',
    'while he', 'while she', 'one evening', 'one night',
    'one morning', 'the author', 'came to him', 'came to her',
    'inspiration', 'dictated', 'manuscript', 'wrote this',
]

def extract_story(text: str, n: int = 3) -> str:
    """Return a 1-3 sentence composition story summary."""
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z\"])', text)
    scored = []
    for s in sents:
        if len(s) < 25:
            continue
        sc = sum(1 for kw in COMPOSITION_KW if kw.lower() in s.lower())
        scored.append((sc, s))
    scored.sort(key=lambda x: -x[0])
    top = [s for sc, s in scored[:n]]
    if not top:
        top = [s for _, s in scored[:n]] if scored else sents[:n]
    result = ' '.join(top[:n])
    return result[:600] if len(result) > 600 else result


ANECDOTE_KW = [
    'incident', 'story', 'anecdote', 'once', 'reported',
    'conversion', 'dying', 'deathbed', 'battle', 'soldier',
    'revival', 'tears', 'effect', 'moved', 'sung at', 'sung by',
    'used at', 'famous', 'remarkable', 'noted',
]

def extract_anecdotes(text: str, n: int = 2) -> str:
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z\"])', text)
    scored = []
    for s in sents:
        if len(s) < 25:
            continue
        sc = sum(1 for kw in ANECDOTE_KW if kw.lower() in s.lower())
        if sc > 0:
            scored.append((sc, s))
    scored.sort(key=lambda x: -x[0])
    top = [s for _, s in scored[:n]]
    result = ' '.join(top[:n])
    return result[:500] if len(result) > 500 else result


# ──────────────────────────────────────────────────────────────────────────────
#  Main parser
# ──────────────────────────────────────────────────────────────────────────────

def parse(path: Path) -> list[dict]:
    with open(path, encoding='utf-8', errors='replace') as f:
        raw_lines = f.readlines()

    print(f"Read {len(raw_lines)} lines")

    BODY_START = 236   # First entry starts here
    BODY_END   = 31510 # End of main body

    entries: list[dict] = []
    cur_first = cur_author = None
    cur_body: list[str] = []

    def flush():
        if cur_first is None:
            return
        body = ' '.join(cur_body).strip()
        e = {
            'first_line':       normalise_first_line(cur_first),
            'author':           normalise_author(cur_author),
            'composition_date': '',
            'composition_story':'',
            'first_published':  '',
            'textual_notes':    '',
            'anecdotes':        '',
            'tune_info':        '',
            'scripture_basis':  '',
            '_raw_body':        body,
        }
        entries.append(e)

    for i, raw in enumerate(raw_lines[BODY_START:BODY_END], start=BODY_START):
        line = clean(raw)
        if line is None:
            continue

        ok, fl, auth = is_header(line)
        if ok:
            flush()
            cur_first, cur_author, cur_body = fl, auth, []
        else:
            if cur_first is not None:
                cur_body.append(line)

    flush()  # last entry

    print(f"Parsed {len(entries)} raw entries")
    return entries


def enrich(entries: list[dict]) -> list[dict]:
    out = []
    for e in entries:
        body = e.pop('_raw_body', '')
        e['scripture_basis']   = extract_scripture(body)
        e['tune_info']         = extract_tune(body)
        e['composition_story'] = extract_story(body)
        e['anecdotes']         = extract_anecdotes(body)
        e['first_published']   = extract_publication(body)
        e['composition_date']  = extract_year(body)
        e['textual_notes']     = extract_textual_notes(body)
        out.append(e)
    return out


def main():
    print("=== Duffield extractor v2 ===")
    entries = parse(INPUT)
    print("Enriching…")
    entries = enrich(entries)
    entries.sort(key=lambda x: x['first_line'].lower())

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    # Stats
    print(f"\nDONE: {len(entries)} entries -> {OUTPUT}")
    stats = {
        'with_author':      sum(1 for e in entries if e['author']),
        'with_scripture':   sum(1 for e in entries if e['scripture_basis']),
        'with_tune':        sum(1 for e in entries if e['tune_info']),
        'with_story':       sum(1 for e in entries if e['composition_story']),
        'with_publication': sum(1 for e in entries if e['first_published']),
        'with_anecdote':    sum(1 for e in entries if e['anecdotes']),
        'with_date':        sum(1 for e in entries if e['composition_date']),
    }
    for k, v in stats.items():
        print(f"  {k:25s}: {v}")

    print("\nSample (first 15):")
    for e in entries[:15]:
        print(f"  [{e['first_line'][:55]:<55}] {e['author'][:30]}")


if __name__ == '__main__':
    main()
