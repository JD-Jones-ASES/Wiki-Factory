"""
Parse KJV.txt into verse-level JSON for scripture lookups.

Output structure:
{
  "Genesis": {
    "1": {
      "1": "In the beginning God created the heaven and the earth.",
      "2": "And the earth was without form..."
    }
  }
}

Also generates a book-name alias map for resolving abbreviations used in Campbell.

Usage: py -3 factory/scripts/parse_kjv.py <KJV.txt> <output.json>
"""
import sys
import re
import json


# Map of full book titles in KJV.txt to canonical short names
BOOK_TITLE_MAP = {
    "The First Book of Moses: Called Genesis": "Genesis",
    "The Second Book of Moses: Called Exodus": "Exodus",
    "The Third Book of Moses: Called Leviticus": "Leviticus",
    "The Fourth Book of Moses: Called Numbers": "Numbers",
    "The Fifth Book of Moses: Called Deuteronomy": "Deuteronomy",
    "The Book of Joshua": "Joshua",
    "The Book of Judges": "Judges",
    "The Book of Ruth": "Ruth",
    "The First Book of Samuel": "1 Samuel",
    "The Second Book of Samuel": "2 Samuel",
    "The First Book of the Kings": "1 Kings",
    "The Second Book of the Kings": "2 Kings",
    "The First Book of the Chronicles": "1 Chronicles",
    "The Second Book of the Chronicles": "2 Chronicles",
    "Ezra": "Ezra",
    "The Book of Nehemiah": "Nehemiah",
    "The Book of Esther": "Esther",
    "The Book of Job": "Job",
    "The Book of Psalms": "Psalms",
    "The Proverbs": "Proverbs",
    "Ecclesiastes": "Ecclesiastes",
    "The Song of Solomon": "Song of Solomon",
    "The Book of the Prophet Isaiah": "Isaiah",
    "The Book of the Prophet Jeremiah": "Jeremiah",
    "The Lamentations of Jeremiah": "Lamentations",
    "The Book of the Prophet Ezekiel": "Ezekiel",
    "The Book of Daniel": "Daniel",
    "Hosea": "Hosea",
    "Joel": "Joel",
    "Amos": "Amos",
    "Obadiah": "Obadiah",
    "Jonah": "Jonah",
    "Micah": "Micah",
    "Nahum": "Nahum",
    "Habakkuk": "Habakkuk",
    "Zephaniah": "Zephaniah",
    "Haggai": "Haggai",
    "Zechariah": "Zechariah",
    "Malachi": "Malachi",
    "The Gospel According to Saint Matthew": "Matthew",
    "The Gospel According to Saint Mark": "Mark",
    "The Gospel According to Saint Luke": "Luke",
    "The Gospel According to Saint John": "John",
    "The Acts of the Apostles": "Acts",
    "The Epistle of Paul the Apostle to the Romans": "Romans",
    "The First Epistle of Paul the Apostle to the Corinthians": "1 Corinthians",
    "The Second Epistle of Paul the Apostle to the Corinthians": "2 Corinthians",
    "The Epistle of Paul the Apostle to the Galatians": "Galatians",
    "The Epistle of Paul the Apostle to the Ephesians": "Ephesians",
    "The Epistle of Paul the Apostle to the Philippians": "Philippians",
    "The Epistle of Paul the Apostle to the Colossians": "Colossians",
    "The First Epistle of Paul the Apostle to the Thessalonians": "1 Thessalonians",
    "The Second Epistle of Paul the Apostle to the Thessalonians": "2 Thessalonians",
    "The First Epistle of Paul the Apostle to Timothy": "1 Timothy",
    "The Second Epistle of Paul the Apostle to Timothy": "2 Timothy",
    "The Epistle of Paul the Apostle to Titus": "Titus",
    "The Epistle of Paul the Apostle to Philemon": "Philemon",
    "The Epistle of Paul the Apostle to the Hebrews": "Hebrews",
    "The General Epistle of James": "James",
    "The First Epistle General of Peter": "1 Peter",
    "The Second General Epistle of Peter": "2 Peter",
    "The First Epistle General of John": "1 John",
    "The Second Epistle General of John": "2 John",
    "The Third Epistle General of John": "3 John",
    "The General Epistle of Jude": "Jude",
    "The Revelation of Saint John the Divine": "Revelation",
}

# Abbreviation map for resolving Campbell references
ABBREVIATION_MAP = {
    "Gen.": "Genesis", "Ex.": "Exodus", "Lev.": "Leviticus",
    "Num.": "Numbers", "Deut.": "Deuteronomy", "Josh.": "Joshua",
    "Judg.": "Judges", "1 Sam.": "1 Samuel", "2 Sam.": "2 Samuel",
    "1 Kings": "1 Kings", "2 Kings": "2 Kings",
    "1 Chron.": "1 Chronicles", "2 Chron.": "2 Chronicles",
    "Neh.": "Nehemiah", "Esth.": "Esther",
    "Prov.": "Proverbs", "Eccl.": "Ecclesiastes",
    "Song": "Song of Solomon", "Isa.": "Isaiah", "Jer.": "Jeremiah",
    "Lam.": "Lamentations", "Ezek.": "Ezekiel", "Dan.": "Daniel",
    "Hos.": "Hosea", "Obad.": "Obadiah", "Mic.": "Micah",
    "Nah.": "Nahum", "Hab.": "Habakkuk", "Zeph.": "Zephaniah",
    "Hag.": "Haggai", "Zech.": "Zechariah", "Mal.": "Malachi",
    "Matt.": "Matthew", "Rom.": "Romans",
    "1 Cor.": "1 Corinthians", "2 Cor.": "2 Corinthians",
    "Gal.": "Galatians", "Eph.": "Ephesians", "Phil.": "Philippians",
    "Col.": "Colossians", "1 Thes.": "1 Thessalonians",
    "2 Thes.": "2 Thessalonians", "1 Tim.": "1 Timothy",
    "2 Tim.": "2 Timothy", "Tit.": "Titus", "Philem.": "Philemon",
    "Heb.": "Hebrews", "Jas.": "James",
    "1 Pet.": "1 Peter", "2 Pet.": "2 Peter",
    "Rev.": "Revelation",
    "Psalm": "Psalms", "Psalms": "Psalms",
}


def parse_kjv(text):
    """Parse KJV text into nested dict: book -> chapter -> verse -> text."""
    lines = text.split('\n')
    bible = {}
    current_book = None

    # Skip the table of contents (before the actual text starts)
    # The actual text starts after "The Old Testament of the King James Version of the Bible"
    started = False

    verse_pat = re.compile(r'^(\d+):(\d+)\s+(.*)')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not started:
            if line == "The Old Testament of the King James Version of the Bible":
                started = True
            i += 1
            continue

        # Check for book title
        if line in BOOK_TITLE_MAP:
            current_book = BOOK_TITLE_MAP[line]
            if current_book not in bible:
                bible[current_book] = {}
            i += 1
            continue

        # Also check for NT header
        if line == "The New Testament of the King James Bible":
            i += 1
            continue

        # Check for verse
        m = verse_pat.match(line)
        if m and current_book:
            chapter = m.group(1)
            verse = m.group(2)
            verse_text = m.group(3)

            # Verses can span multiple lines - collect continuation lines
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                # Stop if: empty line, new verse, new book title, or Gutenberg footer
                if not next_line:
                    break
                if verse_pat.match(next_line):
                    break
                if next_line in BOOK_TITLE_MAP:
                    break
                if next_line.startswith('*** END OF'):
                    break
                verse_text += ' ' + next_line
                i += 1

            if chapter not in bible[current_book]:
                bible[current_book][chapter] = {}
            bible[current_book][chapter][verse] = verse_text.strip()
        else:
            i += 1

    return bible


def main():
    if len(sys.argv) != 3:
        print("Usage: py -3 parse_kjv.py <KJV.txt> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    bible = parse_kjv(text)

    # Stats
    total_books = len(bible)
    total_verses = sum(
        len(verses)
        for chapters in bible.values()
        for verses in chapters.values()
    )
    print(f"Parsed {total_books} books, {total_verses} verses", file=sys.stderr)

    # Verify key books exist
    for book in ['Genesis', 'Psalms', 'Isaiah', 'Matthew', 'John', 'Revelation']:
        if book in bible:
            chapters = len(bible[book])
            print(f"  {book}: {chapters} chapters", file=sys.stderr)
        else:
            print(f"  WARNING: {book} not found!", file=sys.stderr)

    # Save with abbreviation map included
    output = {
        "books": bible,
        "abbreviations": ABBREVIATION_MAP,
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Output written to {output_path}", file=sys.stderr)


if __name__ == '__main__':
    main()
