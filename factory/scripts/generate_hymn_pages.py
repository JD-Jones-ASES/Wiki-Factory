"""
Generate 1,324 hymn markdown pages from campbell_hymns.json.

Each page includes:
- Full YAML frontmatter with hymn-specific fields
- Hymn text copied verbatim from source
- Wikilinks to author entity pages
- Placeholder for scripture references (bible_linker.py fills these)

Usage: py -3 factory/scripts/generate_hymn_pages.py <campbell_hymns.json> <wiki_hymns_dir>
"""
import sys
import re
import json
import os


def sanitize_filename(text, max_words=6):
    """Create a filesystem-safe filename from text."""
    # Remove punctuation except apostrophes
    text = re.sub(r"[^\w\s']", '', text)
    # Split into words, take first N
    words = text.split()[:max_words]
    # Join with underscores, capitalize
    name = '_'.join(w.capitalize() for w in words)
    # Remove any remaining unsafe chars
    name = re.sub(r"[^\w]", '', name)
    return name


def format_author_wikilink(author):
    """Format author name as a wikilink to their entity page."""
    if not author:
        return "Unknown"

    # Clean up common abbreviations
    author = author.strip()

    # Map known abbreviated names to full names
    author_map = {
        "Watts": "Isaac Watts",
        "C. Wesley": "Charles Wesley",
        "J. Wesley": "John Wesley",
        "Newton": "John Newton",
        "Cowper": "William Cowper",
        "Doddridge": "Philip Doddridge",
        "Montgomery": "James Montgomery",
        "Heber": "Reginald Heber",
        "Bonar": "Horatius Bonar",
        "F. Lyte": "Henry Francis Lyte",
        "Toplady": "Augustus Toplady",
        "Gerhardt": "Paul Gerhardt",
        "Addison": "Joseph Addison",
        "Medley": "Samuel Medley",
        "Steele": "Anne Steele",
        "Mrs. Steele": "Anne Steele",
        "Beddome": "Benjamin Beddome",
        "Kelly": "Thomas Kelly",
        "Faber": "Frederick William Faber",
        "Keble": "John Keble",
        "Whittier": "John Greenleaf Whittier",
        "Ray Palmer": "Ray Palmer",
        "S. F. Smith": "Samuel Francis Smith",
        "T. Hastings": "Thomas Hastings",
        "Charlotte Elliott": "Charlotte Elliott",
        "Mrs. Barbauld": "Anna Laetitia Barbauld",
        "Mrs. Hemans": "Felicia Hemans",
        "Mrs. Sigourney": "Lydia Sigourney",
        "Tate & Brady": "Tate and Brady",
        "Patrick": "John Patrick",
        "Gibbons": "Thomas Gibbons",
        "Stennett": "Samuel Stennett",
        "Collyer": "William Bengo Collyer",
        "H. K. White": "Henry Kirke White",
        "Wordsworth": "Christopher Wordsworth",
        "Breviary": "Breviary",
        "Hart": "Joseph Hart",
        "Cennick": "John Cennick",
        "Swain": "Joseph Swain",
        "Rippon": "John Rippon",
        "Logan": "John Logan",
        "Leland": "John Leland",
        "Croly": "George Croly",
        "Bowring": "John Bowring",
        "Pierpont": "John Pierpont",
        "Bath Coll.": "Bath Collection",
        "French": "Unknown (French)",
        "Lamar": "Unknown (Lamar)",
        "B. Schmolk": "Benjamin Schmolck",
        "Madame Guyon": "Madame Guyon",
        "J. Roberts": "John Roberts",
        "John Byrom": "John Byrom",
        "H. Moore": "Henry Moore",
        "Francis": "Benjamin Francis",
        "Grinfield": "Thomas Grinfield",
        "B. Barton": "Bernard Barton",
        "Needham": "John Needham",
        "Dobel": "John Dobell",
        "G. Gaskell": "George Gaskell",
        "J. F. Oberlin": "John Frederick Oberlin",
        "Langford": "John Langford",
        "G. N. Allen": "George Nelson Allen",
        "Nelson": "David Nelson",
        "Neal": "Unknown (Neal)",
        "Malon": "Unknown (Malon)",
        "Denham": "David Denham",
        "Ryle": "John Charles Ryle",
        "Baldwin": "Thomas Baldwin",
        "L. H. Jameson": "Unknown (L. H. Jameson)",
    }

    full_name = author_map.get(author, author)
    return f"[[{full_name}]]"


def meter_tag(meter):
    """Map meter abbreviation to a tag."""
    meter_upper = meter.upper().replace('.', '').replace(' ', '')
    if 'CM' in meter_upper and 'D' in meter_upper:
        return "#meter-common-double"
    if 'CM' in meter_upper:
        return "#meter-common"
    if 'LM' in meter_upper:
        return "#meter-long"
    if 'SM' in meter_upper:
        return "#meter-short"
    if 'LPM' in meter_upper:
        return "#meter-long-particular"
    if 'SPM' in meter_upper:
        return "#meter-short-particular"
    if 'HM' in meter_upper:
        return "#meter-peculiar"
    if 'PM' in meter_upper:
        return "#meter-peculiar"
    return "#meter-peculiar"


def section_to_tags(section):
    """Map Campbell section headings to theme tags."""
    section_lower = section.lower()
    tags = []

    mapping = {
        "holy scriptures": "#theme-scripture",
        "god": "#theme-praise",
        "creation": "#theme-nature",
        "providence": "#theme-trust",
        "redemption": "#theme-grace",
        "christ": "#theme-praise",
        "nativity": "#theme-christmas",
        "suffering": "#theme-suffering",
        "crucifixion": "#theme-easter",
        "resurrection": "#theme-easter",
        "ascension": "#theme-praise",
        "gospel": "#theme-grace",
        "baptism": "#theme-baptism",
        "church": "#theme-devotion",
        "lord's supper": "#theme-communion",
        "worship": "#theme-praise",
        "new life": "#theme-devotion",
        "trust": "#theme-trust",
        "affliction": "#theme-suffering",
        "death": "#theme-funeral",
        "heaven": "#theme-funeral",
        "judgment": "#theme-pilgrimage",
        "home": "#theme-devotion",
        "morning": "#theme-devotion",
        "evening": "#theme-devotion",
        "missionary": "#theme-missionary",
        "sea": "#theme-sailors",
        "thanksgiving": "#theme-praise",
        "marriage": "#theme-devotion",
        "youth": "#theme-children",
        "miscellaneous": "",
    }

    for key, tag in mapping.items():
        if key in section_lower and tag:
            tags.append(tag)

    return tags if tags else ["#theme-devotion"]


def generate_page(hymn, output_dir):
    """Generate a single hymn markdown page."""
    num = hymn['hymn_number']
    first_line = hymn['first_line']
    meter = hymn['meter']
    topic = hymn['topic']
    author = hymn['author']
    scripture_ref = hymn['scripture_ref']
    stanza_count = hymn['stanza_count']
    section = hymn['section']
    text = hymn['text']

    # Build filename
    first_words = sanitize_filename(first_line, max_words=5)
    filename = f"Hymn_{num:04d}_{first_words}.md"

    # Build tags
    tags = [meter_tag(meter)] + section_to_tags(section)
    tags = list(dict.fromkeys(tags))  # deduplicate preserving order

    # Build aliases
    aliases = [first_line]
    if topic and topic != first_line:
        aliases.append(topic)

    # Format scripture refs
    scripture_list = []
    if scripture_ref:
        scripture_list.append(scripture_ref)

    # Author wikilink
    author_link = format_author_wikilink(author)

    # Title
    title = f"Hymn {num}: {first_line}"
    if len(title) > 100:
        title = f"Hymn {num}: {first_line[:80]}..."

    # Build the page
    page = f"""---
title: "{title.replace('"', "'")}"
type: hymn
aliases: {json.dumps(aliases, ensure_ascii=False)}
tags: {json.dumps(tags)}
created: 2026-04-04
updated: 2026-04-04
source_refs: ["[[The_Christian_Hymn_Book]]"]
related: []
status: stub
confidence: high
hymn_number: {num}
first_line: "{first_line.replace('"', "'")}"
meter: "{meter}"
topic: "{topic.replace('"', "'")}"
author: "{author.replace('"', "'")}"
composer: ""
tune_name: ""
scripture_refs: {json.dumps(scripture_list)}
stanza_count: {stanza_count}
era: ""
---

# Hymn {num}: {first_line}

| Field | Value |
|-------|-------|
| **Author** | {author_link} |
| **Meter** | {meter} |
| **Topic** | {topic} |
| **Section** | {section.title()} |
| **Stanzas** | {stanza_count} |

## Text

> *From [[The_Christian_Hymn_Book|The Christian Hymn Book]] (1870), Hymn {num}*

```
{text}
```

## Scripture References

"""

    if scripture_ref:
        page += f"- {scripture_ref}\n\n"
    else:
        page += "*No scripture reference in source.*\n\n"

    page += """## Historical Context

*This section will be enriched during narrative ingest from [[The_Story_of_Our_Hymns]] and [[The_Story_of_the_Hymns_and_Tunes]].*
"""

    # Write file
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page)

    return filename


def main():
    if len(sys.argv) != 3:
        print("Usage: py -3 generate_hymn_pages.py <campbell_hymns.json> <wiki_hymns_dir>",
              file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]

    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f:
        hymns = json.load(f)

    print(f"Generating {len(hymns)} hymn pages...", file=sys.stderr)

    filenames = []
    for hymn in hymns:
        fn = generate_page(hymn, output_dir)
        filenames.append(fn)

    print(f"Generated {len(filenames)} pages in {output_dir}", file=sys.stderr)

    # Verify file count
    actual_files = [f for f in os.listdir(output_dir) if f.endswith('.md')]
    print(f"Files on disk: {len(actual_files)}", file=sys.stderr)


if __name__ == '__main__':
    main()
