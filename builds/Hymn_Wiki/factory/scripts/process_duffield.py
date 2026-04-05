#!/usr/bin/env python3
"""
process_duffield.py
Processes Duffield's "English Hymns: Their Authors and History" (1886)
and extracts structured hymn data into a JSON file.

Usage: py -3 process_duffield.py
"""

import re
import json
import sys
from pathlib import Path

# Paths
INPUT_FILE = Path(r"C:\Wiki_Factory\builds\Hymn_Wiki\raw\Duffield.txt")
OUTPUT_FILE = Path(r"C:\Wiki_Factory\builds\Hymn_Wiki\wiki\_duffield_hymn_data.json")

# ─── Regex patterns ───────────────────────────────────────────────────────────

# Entry header: caps-heavy first line followed by "— Author" or "—Author"
# Examples:
#   "A BROKEN heart, my God, my King. — Watts."
#   "ABIDE with me ; fast falls the eventide. — Lyte."
#   "A MIGHTY fortress is our God. — Hedge, tr."
HEADER_RE = re.compile(
    r'^([A-Z][A-Z\s,\'\-;:!]+(?:[a-z]+[A-Z\s,\'\-;:!]*)*[.!?;,]*)\s*[—\-–]{1,3}\s*(.+?)\s*$'
)

# Simpler pattern that catches the ALL-CAPS-leading entries more reliably
# The first line of each entry is CAPS-dominant with an em-dash attribution
ENTRY_START_RE = re.compile(
    r'^([A-Z][A-Z][A-Z\s,\'\-\(\);:\.!?]+(?:\s+[a-z]{1,4}\s+[A-Z\s,\'\-;:\.!?]+)*)\s*[\.!;,]?\s*[—\-–]+\s*(.+?)[.\s]*$'
)

# Alternative: lines that are majority uppercase (>50% uppercase letters in words)
# and contain an em-dash

# Page header noise pattern: "ENGLISH HYMNS. 42" or "42 ENGLISH HYMNS."
PAGE_HEADER_RE = re.compile(
    r'^(?:ENGLISH\s+HYMNS\.?\s*\d*|\d+\s+ENGLISH\s+HYMNS\.?)$',
    re.IGNORECASE
)

# Scripture reference patterns
SCRIPTURE_RE = re.compile(
    r'\b(?:Gen(?:esis)?|Ex(?:odus)?|Lev(?:iticus)?|Num(?:bers)?|Deut(?:eronomy)?|'
    r'Josh(?:ua)?|Judg(?:es)?|Ruth|[12]\s*Sam(?:uel)?|[12]\s*Kings?|[12]\s*Chr(?:on(?:icles)?)?|'
    r'Ezra|Neh(?:emiah)?|Esth(?:er)?|Job|Ps(?:alms?)?|Prov(?:erbs)?|Eccl(?:es(?:iastes)?)?|'
    r'Song(?:\s+of\s+Sol(?:omon)?)?|Isa(?:iah)?|Jer(?:emiah)?|Lam(?:entations)?|'
    r'Ezek(?:iel)?|Dan(?:iel)?|Hos(?:ea)?|Joel|Amos|Obad(?:iah)?|Jon(?:ah)?|Mic(?:ah)?|'
    r'Nah(?:um)?|Hab(?:akkuk)?|Zeph(?:aniah)?|Hag(?:gai)?|Zech(?:ariah)?|Mal(?:achi)?|'
    r'Matt(?:hew)?|Mark|Luke|John|Acts|Rom(?:ans)?|[12]\s*Cor(?:inthians)?|'
    r'Gal(?:atians)?|Eph(?:esians)?|Phil(?:ippians)?|Col(?:ossians)?|'
    r'[12]\s*Thess(?:alonians)?|[12]\s*Tim(?:othy)?|Tit(?:us)?|Phlm|Philemon|'
    r'Heb(?:rews)?|Jas(?:ames)?|[12]\s*Pet(?:er)?|[123]\s*John|Jude|'
    r'Rev(?:elation)?)\s*\d+\s*:\s*\d+',
    re.IGNORECASE
)

# Tune name patterns
TUNE_RE = re.compile(
    r'(?:tune[sd]?(?:\s+(?:called|named|known\s+as|entitled))?|set\s+to|'
    r'sung\s+to(?:\s+the)?(?:\s+tune(?:\s+of)?)?|air|melody)\s+'
    r'["\'""]([^"\'""]+)["\'""]',
    re.IGNORECASE
)

# Year patterns for dates
YEAR_RE = re.compile(r'\b(1[456789]\d\d|18\d\d)\b')

# Publication patterns
PUB_RE = re.compile(
    r'(?:first\s+(?:published|appeared|printed|issued)|'
    r'published\s+(?:in|as|at)|'
    r'appeared\s+in|'
    r'in\s+(?:his|her|the))\s+([^,\.]+(?:,\s*\d{4})?)',
    re.IGNORECASE
)

# ─── Helper functions ──────────────────────────────────────────────────────────

def clean_line(line):
    """Remove OCR artifacts and normalize whitespace."""
    # Remove page header noise
    if PAGE_HEADER_RE.match(line.strip()):
        return None

    # Fix common OCR issues
    line = line.strip()

    # Normalize multiple spaces
    line = re.sub(r'  +', ' ', line)

    # Fix fi/fl ligature OCR artifacts (ffi -> ffi, fi -> fi, fl -> fl etc.)
    # These sometimes appear as individual characters

    # Remove standalone page number lines
    if re.match(r'^\d+$', line):
        return None

    return line if line else None


def clean_first_line(raw):
    """Clean up the first line extracted from the header."""
    # Normalize spaces
    raw = re.sub(r'\s+', ' ', raw).strip()

    # Fix OCR spacing in words (e.g., "BROK EN" -> "BROKEN")
    # But be careful not to merge real separate words

    # Convert ALL-CAPS to title case for readability
    # Keep as-is for now; we'll clean during extraction
    words = raw.split()
    result = []
    for word in words:
        # Skip if it's punctuation-only
        if re.match(r'^[,;:\.\!\?]+$', word):
            result.append(word)
        else:
            # Title-case the word
            result.append(word.capitalize() if word.isupper() else word)

    return ' '.join(result).strip(' .,;:')


def clean_author(raw):
    """Clean the author attribution."""
    raw = raw.strip(' .,;:')
    # Remove translation markers
    raw = re.sub(r',?\s*tr\..*$', '', raw, flags=re.IGNORECASE)
    raw = re.sub(r',?\s*trans\..*$', '', raw, flags=re.IGNORECASE)
    # Remove "Jr.", "Sr.", etc. trailing artifacts
    return raw.strip()


def extract_scripture_refs(text):
    """Extract scripture references from text."""
    refs = list(set(SCRIPTURE_RE.findall(text)))
    return refs if refs else []


def extract_tune_info(text):
    """Extract tune/music information from text."""
    tunes = []

    # Look for quoted tune names after tune-related words
    tune_matches = TUNE_RE.findall(text)
    tunes.extend(tune_matches)

    # Look for named tunes in quotes generally
    # e.g. 'the tune "HANOVER"' or '"St. Anne"'
    quoted = re.findall(r'["\'""]([A-Z][A-Za-z\s\.]+)["\'""]', text)
    for q in quoted:
        q = q.strip()
        if len(q) < 50 and re.match(r'^[A-Z]', q):
            # Likely a tune name if it's short and capitalized
            if any(word in text[max(0, text.find(q)-50):text.find(q)].lower()
                   for word in ['tune', 'air', 'melody', 'music', 'sung', 'set']):
                if q not in tunes:
                    tunes.append(q)

    return '; '.join(tunes) if tunes else ''


def extract_years(text):
    """Extract the earliest plausible composition year from text."""
    years = YEAR_RE.findall(text)
    if not years:
        return ''
    # Filter to plausible hymn composition years (1400-1900)
    years = [int(y) for y in years if 1400 <= int(y) <= 1900]
    if not years:
        return ''
    return str(min(years))


def summarize_story(text, max_sentences=3):
    """Extract key composition story sentences."""
    if not text:
        return ''

    # Split on sentence boundaries (roughly)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Prioritize sentences about composition/writing
    composition_keywords = [
        'composed', 'written', 'wrote', 'writing', 'pen', 'composed',
        'origin', 'occasion', 'circumstance', 'wrote this', 'wrote the',
        'while he', 'while she', 'one evening', 'one night', 'one morning',
        'at the', 'in the year', 'the author', 'he composed', 'she composed',
        'it was written', 'came to him', 'came to her', 'inspiration'
    ]

    scored = []
    for s in sentences:
        score = sum(1 for kw in composition_keywords if kw.lower() in s.lower())
        if len(s) > 30:  # Skip very short fragments
            scored.append((score, s))

    # Sort by relevance, take top sentences
    scored.sort(key=lambda x: -x[0])
    top = [s for _, s in scored[:max_sentences]]

    if not top and sentences:
        top = sentences[:max_sentences]

    result = ' '.join(top[:max_sentences])
    # Truncate if too long
    if len(result) > 500:
        result = result[:497] + '...'

    return result.strip()


def summarize_anecdotes(text, max_sentences=2):
    """Extract notable anecdote sentences."""
    if not text:
        return ''

    sentences = re.split(r'(?<=[.!?])\s+', text)

    anecdote_keywords = [
        'incident', 'story', 'anecdote', 'occasion', 'when', 'once',
        'reported', 'conversion', 'dying', 'deathbed', 'battle',
        'soldier', 'revival', 'awakening', 'tears', 'effect', 'moved',
        'sung at', 'sung by', 'used at', 'famous'
    ]

    scored = []
    for s in sentences:
        score = sum(1 for kw in anecdote_keywords if kw.lower() in s.lower())
        if len(s) > 30:
            scored.append((score, s))

    scored.sort(key=lambda x: -x[0])
    top = [s for score, s in scored[:max_sentences] if score > 0]

    result = ' '.join(top[:max_sentences])
    if len(result) > 400:
        result = result[:397] + '...'

    return result.strip()


def extract_publication_info(text):
    """Extract first publication information."""
    # Look for collection names and years
    pub_patterns = [
        r'(?:first\s+(?:published|appeared|printed)|published)\s+in\s+([^,\.]+(?:,?\s*\d{4})?)',
        r'(?:it\s+is|this\s+is|this\s+hymn\s+is)\s+(?:from|in)\s+([^,\.]+(?:,?\s*\d{4})?)',
        r'(?:in|from)\s+(?:his|her|the)\s+([A-Z][^,\.]+(?:,?\s*\d{4})?)',
        r'(?:No\.\s*\d+\s+of|number\s+\d+\s+in)\s+([^,\.]+)',
        r'([A-Z][^,\.]+),\s*(\d{4})',
    ]

    for pattern in pub_patterns:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            result = m.group(1).strip()
            if 10 < len(result) < 100:
                return result

    # Look for standalone year near collection names
    # Pattern: "Collection Name (1760)" or "Collection Name, 1760"
    coll_m = re.search(
        r'([A-Z][A-Za-z\s&\',]+)\s*[\(,]\s*(\d{4})\s*[\)]?',
        text
    )
    if coll_m:
        return f"{coll_m.group(1).strip()}, {coll_m.group(2)}"

    return ''


# ─── Main parser ──────────────────────────────────────────────────────────────

def is_entry_header(line):
    """
    Detect if a line is an entry header.
    Entry headers look like:
      "A BROKEN heart, my God, my King. — Watts."
      "Abide with me ; fast falls the eventide. — Lyte."
      "A MIGHTY fortress is our God. — Hedge, tr."

    Key characteristics:
    1. Starts with an uppercase letter
    2. Contains an em-dash or double-hyphen followed by an author name
    3. Is relatively short (< 120 chars)
    4. The part before the dash is the hymn first line
    """
    line = line.strip()
    if not line:
        return False
    if len(line) > 150:
        return False

    # Must contain em-dash or similar
    if not re.search(r'[—\-–]{1,2}', line):
        return False

    # Must start with uppercase letter
    if not re.match(r'^[A-Z]', line):
        return False

    # Split on em-dash
    parts = re.split(r'\s*[—–]\s*', line, maxsplit=1)
    if len(parts) < 2:
        # Try double-hyphen
        parts = re.split(r'\s*--\s*', line, maxsplit=1)

    if len(parts) < 2:
        return False

    first_part, attribution = parts[0].strip(), parts[1].strip()

    # First part should be a plausible hymn line (5-100 chars)
    if len(first_part) < 5 or len(first_part) > 100:
        return False

    # Attribution should be a plausible author name (2-50 chars)
    if len(attribution) < 2 or len(attribution) > 60:
        return False

    # Attribution shouldn't look like a sentence (no long prose)
    if len(attribution.split()) > 8:
        return False

    # First part should have some uppercase (hymn title characteristic)
    upper_count = sum(1 for c in first_part if c.isupper())
    if upper_count < 2:
        return False

    # Exclude page headers
    if PAGE_HEADER_RE.match(line):
        return False

    return True


def parse_duffield(filepath):
    """Parse the Duffield text file and return a list of entry dicts."""

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from {filepath}")

    # Find the start of the main body (line ~236)
    # and end (line ~31500)
    BODY_START = 236
    BODY_END = 31500

    entries = []
    current_entry = None
    current_lines = []

    for i, raw_line in enumerate(lines[BODY_START:BODY_END], start=BODY_START):
        line = raw_line.rstrip('\n\r')
        clean = clean_line(line)

        if clean is None:
            # Page header noise — skip but continue accumulating
            continue

        if is_entry_header(clean):
            # Save previous entry
            if current_entry is not None and current_lines:
                current_entry['_body'] = ' '.join(current_lines)
                entries.append(current_entry)

            # Parse new entry header
            parts = re.split(r'\s*[—–]\s*', clean, maxsplit=1)
            if len(parts) < 2:
                parts = re.split(r'\s*--\s*', clean, maxsplit=1)

            if len(parts) >= 2:
                raw_first_line = parts[0].strip(' .,;:')
                raw_author = parts[1].strip(' .,;:')

                current_entry = {
                    'first_line': clean_first_line(raw_first_line),
                    'author': clean_author(raw_author),
                    'composition_date': '',
                    'composition_story': '',
                    'first_published': '',
                    'textual_notes': '',
                    'anecdotes': '',
                    'tune_info': '',
                    'scripture_basis': '',
                    '_body': '',
                    '_line_num': i + 1
                }
                current_lines = []
        else:
            # Accumulate body text
            if current_entry is not None and clean:
                current_lines.append(clean)

    # Don't forget the last entry
    if current_entry is not None and current_lines:
        current_entry['_body'] = ' '.join(current_lines)
        entries.append(current_entry)

    print(f"Found {len(entries)} raw entries")
    return entries


def enrich_entries(entries):
    """Post-process entries to extract structured fields from body text."""
    enriched = []

    for entry in entries:
        body = entry.get('_body', '')

        if not body:
            continue

        # Extract fields
        entry['scripture_basis'] = '; '.join(extract_scripture_refs(body))
        entry['tune_info'] = extract_tune_info(body)
        entry['composition_story'] = summarize_story(body)
        entry['anecdotes'] = summarize_anecdotes(body)
        entry['first_published'] = extract_publication_info(body)

        # Extract composition date from body
        year = extract_years(body)
        entry['composition_date'] = year

        # Extract textual notes
        textual_patterns = [
            r'(original(?:ly)?\s+[^.]+(?:stanzas?|verses?|form)[^.]*\.)',
            r'(altered[^.]+\.)',
            r'(omit[^.]+\.)',
            r'(the\s+(?:present|current)\s+(?:form|version|text)[^.]+\.)',
            r'(ascribed[^.]+\.)',
            r'(attributed[^.]+\.)',
            r'(disputed[^.]+\.)',
        ]
        textual_notes = []
        for pat in textual_patterns:
            m = re.search(pat, body, re.IGNORECASE)
            if m:
                note = m.group(1).strip()
                if note not in textual_notes and len(note) < 200:
                    textual_notes.append(note)
        entry['textual_notes'] = ' '.join(textual_notes[:2])

        # Remove internal working field
        del entry['_body']
        del entry['_line_num']

        enriched.append(entry)

    return enriched


def main():
    print("Processing Duffield's English Hymns...")

    # Parse entries
    entries = parse_duffield(INPUT_FILE)

    # Enrich with structured data
    print("Enriching entries...")
    enriched = enrich_entries(entries)

    # Sort by first line alphabetically
    enriched.sort(key=lambda x: x['first_line'].lower())

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)

    print(f"\nDONE: Written {len(enriched)} entries to {OUTPUT_FILE}")

    # Print statistics
    with_author = sum(1 for e in enriched if e['author'])
    with_scripture = sum(1 for e in enriched if e['scripture_basis'])
    with_tune = sum(1 for e in enriched if e['tune_info'])
    with_story = sum(1 for e in enriched if e['composition_story'])
    with_pub = sum(1 for e in enriched if e['first_published'])

    print(f"\nStatistics:")
    print(f"  Total entries: {len(enriched)}")
    print(f"  With author: {with_author}")
    print(f"  With scripture reference: {with_scripture}")
    print(f"  With tune info: {with_tune}")
    print(f"  With composition story: {with_story}")
    print(f"  With publication info: {with_pub}")

    # Show first 10 entries
    print(f"\nFirst 10 entries:")
    for e in enriched[:10]:
        print(f"  [{e['first_line'][:50]}] — {e['author']}")

    return enriched


if __name__ == '__main__':
    main()
