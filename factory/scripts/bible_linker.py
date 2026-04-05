"""
Bible Linker: Inject KJV verse text into hymn pages and build scripture index.

1. Scans hymn pages for scripture_refs in frontmatter
2. Resolves references to KJV verse text
3. Injects quoted verse text into the Scripture References section
4. Builds _scripture_index.md mapping Bible passages to hymns

Usage: py -3 factory/scripts/bible_linker.py <kjv_verses.json> <wiki_hymns_dir> <wiki_dir>
"""
import sys
import re
import json
import os
import yaml


def parse_scripture_ref(ref, abbreviations):
    """Parse a scripture reference string into (book, chapter, verse_start, verse_end).

    Examples:
      'Psalm 19.' -> ('Psalms', '19', None, None)
      'Psalm 19:1' -> ('Psalms', '19', '1', '1')
      'Psalm 119:105' -> ('Psalms', '119', '105', '105')
      'Gen. 22:14' -> ('Genesis', '22', '14', '14')
      '2 Tim. 1:13' -> ('2 Timothy', '1', '13', '13')
      'Psalm 119:9' -> ('Psalms', '119', '9', '9')
      'Gen. 20:19-22' -> ('Genesis', '20', '19', '22')
    """
    ref = ref.strip().rstrip('.')

    # Try to match "Book chapter:verse-verse" or "Book chapter:verse" or "Book chapter"
    # Handle numbered books: "1 Tim.", "2 Cor.", etc.

    # Pattern for references with chapter:verse
    m = re.match(r'^(\d?\s*\w[\w\s.]*?)\s+(\d+):(\d+)(?:-(\d+))?$', ref)
    if m:
        book_abbr = m.group(1).strip()
        chapter = m.group(2)
        verse_start = m.group(3)
        verse_end = m.group(4) or verse_start

        book = resolve_book(book_abbr, abbreviations)
        if book:
            return (book, chapter, verse_start, verse_end)

    # Pattern for references with just chapter (e.g., "Psalm 19")
    m = re.match(r'^(\d?\s*\w[\w\s.]*?)\s+(\d+)$', ref)
    if m:
        book_abbr = m.group(1).strip()
        chapter = m.group(2)

        book = resolve_book(book_abbr, abbreviations)
        if book:
            return (book, chapter, None, None)

    return None


def resolve_book(abbr, abbreviations):
    """Resolve a book abbreviation to full canonical name."""
    # Direct lookup
    if abbr in abbreviations:
        return abbreviations[abbr]

    # Try with period
    if not abbr.endswith('.') and (abbr + '.') in abbreviations:
        return abbreviations[abbr + '.']

    # Try without period
    if abbr.endswith('.') and abbr[:-1] in abbreviations:
        return abbreviations[abbr[:-1]]

    # Handle "Psalm" -> "Psalms"
    if abbr.lower().startswith('psalm'):
        return 'Psalms'

    # Try case-insensitive match
    abbr_lower = abbr.lower().rstrip('.')
    for key, val in abbreviations.items():
        if key.lower().rstrip('.') == abbr_lower:
            return val

    # Direct book name match
    if abbr in abbreviations.values():
        return abbr

    return None


def get_verses(bible, book, chapter, verse_start, verse_end):
    """Retrieve verse text from the parsed Bible."""
    if book not in bible:
        return None

    if chapter not in bible[book]:
        return None

    if verse_start is None:
        # Return first few verses of the chapter as a sample
        verses = bible[book][chapter]
        result = []
        for v_num in sorted(verses.keys(), key=int)[:3]:
            result.append(f"**{book} {chapter}:{v_num}** --- {verses[v_num]}")
        if len(verses) > 3:
            result.append(f"*...and {len(verses) - 3} more verses*")
        return '\n\n'.join(result)

    verses = bible[book][chapter]
    result = []
    for v in range(int(verse_start), int(verse_end) + 1):
        v_str = str(v)
        if v_str in verses:
            result.append(f"**{book} {chapter}:{v_str}** --- {verses[v_str]}")

    return '\n\n'.join(result) if result else None


def process_hymn_page(filepath, bible, abbreviations):
    """Process a single hymn page: extract refs, inject verse text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract scripture_refs from frontmatter
    # Simple approach: find the YAML block and parse scripture_refs
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None

    fm_text = fm_match.group(1)

    # Extract scripture_refs list
    refs_match = re.search(r'scripture_refs:\s*\[(.*?)\]', fm_text)
    if not refs_match:
        return None

    refs_raw = refs_match.group(1).strip()
    if not refs_raw:
        return None

    # Parse the refs (they're JSON-formatted strings)
    refs = []
    for r in re.findall(r'"([^"]+)"', refs_raw):
        refs.append(r)

    if not refs:
        return None

    # Resolve each reference
    verse_sections = []
    resolved_refs = []
    for ref in refs:
        parsed = parse_scripture_ref(ref, abbreviations)
        if parsed:
            book, chapter, vs, ve = parsed
            verse_text = get_verses(bible['books'], book, chapter, vs, ve)
            if verse_text:
                verse_sections.append(verse_text)
                ref_key = f"{book} {chapter}"
                if vs:
                    ref_key += f":{vs}"
                    if ve and ve != vs:
                        ref_key += f"-{ve}"
                resolved_refs.append(ref_key)

    if not verse_sections:
        return None

    # Replace the Scripture References section
    new_section = "## Scripture References\n\n"
    for ref, verses in zip(refs, verse_sections):
        new_section += f"### {ref}\n\n{verses}\n\n"

    # Find and replace the scripture section in the content
    pattern = r'## Scripture References\n\n(?:.*?)(?=\n## |\Z)'
    replacement = new_section.rstrip() + '\n\n'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return resolved_refs


def build_scripture_index(index_data, output_path):
    """Build _scripture_index.md mapping Bible passages to hymns."""
    # Group by book
    by_book = {}
    for ref, hymn_info in sorted(index_data):
        book = ref.split(' ')[0]
        # Handle numbered books
        if ref[0].isdigit():
            book = ' '.join(ref.split(' ')[:2])

        if book not in by_book:
            by_book[book] = []
        by_book[book].append((ref, hymn_info))

    page = """---
title: "Scripture Index"
type: overview
aliases: ["Bible Index", "Verse Index"]
tags: ["#theme-scripture"]
created: 2026-04-04
updated: 2026-04-04
source_refs: ["[[King_James_Bible]]", "[[The_Christian_Hymn_Book]]"]
related: []
status: draft
confidence: high
---

# Scripture Index

Bible passages referenced by hymns in this wiki. Verses are from the King James Version.

"""

    # Sort books in Bible order
    bible_order = [
        'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
        'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel',
        '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles',
        'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs',
        'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah',
        'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos',
        'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah',
        'Haggai', 'Zechariah', 'Malachi',
        'Matthew', 'Mark', 'Luke', 'John', 'Acts',
        'Romans', '1 Corinthians', '2 Corinthians', 'Galatians',
        'Ephesians', 'Philippians', 'Colossians',
        '1 Thessalonians', '2 Thessalonians',
        '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews',
        'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John',
        'Jude', 'Revelation'
    ]

    sorted_books = sorted(by_book.keys(),
                          key=lambda b: bible_order.index(b) if b in bible_order else 999)

    for book in sorted_books:
        entries = by_book[book]
        page += f"## {book}\n\n"
        for ref, hymn_info in entries:
            page += f"- **{ref}** --- {hymn_info}\n"
        page += "\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(page)


def main():
    if len(sys.argv) != 4:
        print("Usage: py -3 bible_linker.py <kjv_verses.json> <wiki_hymns_dir> <wiki_dir>",
              file=sys.stderr)
        sys.exit(1)

    kjv_path = sys.argv[1]
    hymns_dir = sys.argv[2]
    wiki_dir = sys.argv[3]

    with open(kjv_path, 'r', encoding='utf-8') as f:
        bible = json.load(f)

    abbreviations = bible['abbreviations']

    # Process all hymn pages
    hymn_files = sorted(f for f in os.listdir(hymns_dir) if f.endswith('.md'))
    print(f"Processing {len(hymn_files)} hymn pages...", file=sys.stderr)

    index_data = []
    linked_count = 0

    for filename in hymn_files:
        filepath = os.path.join(hymns_dir, filename)
        resolved = process_hymn_page(filepath, bible, abbreviations)
        if resolved:
            linked_count += 1
            # Extract hymn number and first line for the index
            hymn_num_match = re.match(r'Hymn_(\d+)_(.+)\.md', filename)
            if hymn_num_match:
                num = int(hymn_num_match.group(1))
                name_part = hymn_num_match.group(2).replace('_', ' ')
                hymn_link = f"[[{filename[:-3]}|Hymn {num}: {name_part}]]"
                for ref in resolved:
                    index_data.append((ref, hymn_link))

    print(f"Linked {linked_count} hymns to scripture", file=sys.stderr)
    print(f"Total scripture references in index: {len(index_data)}", file=sys.stderr)

    # Build scripture index
    index_path = os.path.join(wiki_dir, '_scripture_index.md')
    build_scripture_index(index_data, index_path)
    print(f"Scripture index written to {index_path}", file=sys.stderr)


if __name__ == '__main__':
    main()
