#!/usr/bin/env python3
"""
add_hymns_by_author.py
Builds reverse mapping from Campbell author abbreviations to entity pages,
then injects a '## Hymns in The Christian Hymn Book' section into each
author page listing all their hymns with wikilinks.
"""

import json
import os
import re
import glob
import sys

WIKI_DIR = os.path.join("builds", "Hymn_Wiki", "wiki")
HYMNS_DIR = os.path.join(WIKI_DIR, "hymns")
ENTITIES_DIR = os.path.join(WIKI_DIR, "entities")
CAMPBELL_JSON = os.path.join("builds", "Hymn_Wiki", "raw", "extracted", "campbell_hymns.json")

# Manual mapping: Campbell author abbreviation -> entity page filename (without .md)
# Only maps to entity pages that actually exist
AUTHOR_MAP = {
    "Watts": "Isaac_Watts",
    "C. Wesley": "Charles_Wesley",
    "Montgomery": "James_Montgomery",
    "Mrs. Steele": "Anna_Steele",
    "Doddridge": "Philip_Doddridge",
    "Newton": "John_Newton",
    "Bonar": "Horatius_Bonar",
    "Kelly": "Thomas_Kelly",
    "Beddome": "Benjamin_Beddome",
    "Cowper": "William_Cowper",
    "W. T. Moore": "W_T_Moore",
    "F. Lyte": "Henry_Francis_Lyte",
    "Heber": "Reginald_Heber",
    "S. F. Smith": "Samuel_Francis_Smith",
    "Ray Palmer": "Ray_Palmer",
    "Conder": "Josiah_Conder",
    "Stennett": "Samuel_Stennett",
    "Bowring": "Sir_John_Bowring",
    "T. Hastings": "Thomas_Hastings",
    "Moore": "Thomas_Moore",
    "Fawcett": "John_Fawcett",
    "Collyer": "William_Bengo_Collyer",
    "Charlotte Elliott": "Charlotte_Elliott",
    "Medley": "Samuel_Medley",
    "Mrs. Hemans": "Felicia_Hemans",
    "Palmer": "Ray_Palmer",  # ambiguous but Ray Palmer is the hymn writer
    "Mrs. Barbauld": "Anna_Laetitia_Barbauld",
    "Gibbons": "Thomas_Gibbons",
    "Toplady": "Augustus_Toplady",
    "Edmeston": "James_Edmeston",
    "Grant": "Robert_Grant",
    "Addison": "Joseph_Addison",
    "Raffles": None,  # Thomas Raffles - no entity page
    "Doane": "William_H_Doane",
    "Mrs. Sigourney": "Lydia_Sigourney",
    "Barton": "Bernard_Barton",
    "Muhlenberg": "William_Augustus_Muhlenberg",
    "A. C. Coxe": "Arthur_Cleveland_Coxe",
    "A. S. Hayden": "A_S_Hayden",
    "Keble": "John_Keble",
    "Whittier": "John_Greenleaf_Whittier",
    "W. C. Bryant": "William_Cullen_Bryant",
    "Hart": "Joseph_Hart",
    "Hastings": "Thomas_Hastings",
    "H. K. White": "Henry_Kirke_White",
    "Dwight": "Timothy_Dwight",
    "Reed": None,  # no clear match
    "Francis": "Benjamin_Francis",
    "Cennick": "John_Cennick",
    "B. Barton": "Bernard_Barton",
    "W. B. Tappan": None,  # no entity page
    "Gerhardt": "Paul_Gerhardt",
    "Logan": "John_Logan",
    "Needham": "John_Needham",
    "B. Skene": None,  # no entity page
    "Bulfinch": None,  # no entity page
    "Pierpont": "John_Pierpont",
    "W. Baxter": None,  # not Richard_Baxter
    "W. Hunter": None,  # no entity page
    "Milton": "John_Milton",
    "Longfellow": "Samuel_Longfellow",
    "S. Longfellow": "Samuel_Longfellow",
    "Nelson": "David_Nelson",
    "Kirkham": None,  # no entity page
    "E. Scott": None,  # no entity page
    "Kenn": "Thomas_Ken",
    "Ryland": None,  # no entity page
    "O. W. Holmes": "Oliver_Wendell_Holmes",
    "G. B. Ide": None,  # no entity page
    "Hammond": "William_Hammond",
    "T. Scott": None,  # no entity page
    "J. Taylor": None,  # no entity page
    "I. Williams": None,  # no entity page
    "S. Johnson": None,  # no entity page
    "Dale": None,
    "Berridge": None,
    "Enfield": None,
    "Shrubsole": "William_Shrubsole",
    "G. Burgess": None,
    "G. Terstergan": "Gerhard_Tersteegen",
    "Gaskell": None,
    "Sir Robt. Grant": "Robert_Grant",
    "Sir W. Scott": "Sir_Walter_Scott",
    "Sarah F. Adams": "Sarah_Flower_Adams",
    "Mrs. S. F. Adams": "Sarah_Flower_Adams",
    "Miss A. A. Procter": "Adelaide_Anne_Procter",
    "Burder": None,
    "J. F. Clarke": None,
    "A. Broaddus": "Andrew_Broaddus",
    "Bernard": "Bernard_of_Clairvaux",
    "Rippon\u2019s Coll": None,  # collection, not a person
    # "Tate & Brady" handled in DUAL_AUTHORS below
    "Altered by Toplady": "Augustus_Toplady",
    "Alice Carey": "Alice_Cary",
    "A. D. Fillmore": "Augustus_Dillard_Fillmore",
    "A. L. Waring": "Anna_Letitia_Waring",
    "Anna L. Waring": "Anna_Letitia_Waring",
    "Anna W. Hall": "Anna_W_Hall",
    "Count Zinzendorf": "Count_Nikolaus_von_Zinzendorf",
    "De Fleury": "Maria_De_Fleury",
    "Maria De Fleury": "Maria_De_Fleury",
    "Robinson": "Robert_Robinson",
    "Perronet": "Edward_Perronet",
    "Olivers": "Thomas_Olivers",
    "Oliver": "Thomas_Olivers",
    "Swain": "Joseph_Swain",
    "Gambold": "John_Gambold",
    "Langford": "John_Langford",
    "Patrick": "John_Patrick",
    "Baldwin": "Thomas_Baldwin",
    "Grinfield": "Thomas_Grinfield",
    "Stowell": "Hugh_Stowell",
    "Newman": "John_Henry_Newman",
    "Faber": "Frederick_William_Faber",
    "F. S. Key": "Francis_Scott_Key",
    "F. T. Palgrave": "Francis_Turner_Palgrave",
    "F. Whitfield": "Frederick_Whitfield",
    "J. Wesley": "John_Wesley",
    "John Austin": "John_Austin",
    "John Bowdler": "John_Bowdler",
    "John Byrom": "John_Byrom",
    "Joachim Neander": "Joachim_Neander",
    "J. S. B. Monsell": "John_Samuel_Bewley_Monsell",
    "J. H. Gurney": "John_Hampden_Gurney",
    "J. F. Oberlin": "John_Frederick_Oberlin",
    "B. Schmolk": "Benjamin_Schmolck",
    "May L. Duncan": "May_L_Duncan",
    "Eliza Scudder": "Eliza_Scudder",
    "Madame Guyon": "Madame_Guyon",
    "Henry Alford": "Henry_Alford",
    "Henry Downton": "Henry_Downton",
    "Hugh White": "Hugh_White",
    "H. Moore": "Henry_Moore",
    "N. P. Willis": "Nathaniel_Parker_Willis",
    "Wordsworth": "Christopher_Wordsworth",
    "R. Baxter": "Richard_Baxter",
    "Pearce": "Samuel_Pearce",
    "Ryle": "John_Charles_Ryle",
    "W. H. Burleigh": "William_Henry_Burleigh",
    "S. Wesley, sen": "Samuel_Wesley_Sr",
    "Denham": "David_Denham",
    "Dobell": "John_Dobell",
    "Dobel": "John_Dobell",
    "J. Roberts": "John_Roberts",
    "G. N. Allen": "George_Nelson_Allen",
    "Barry Cornwall": None,  # pen name of Bryan Procter, no entity page
    "Bakewell": None,
    "Kelley": "Thomas_Kelly",  # variant spelling
    "E. A. Scott": None,
    "Mason": "Lowell_Mason",
    "Allen": "George_Nelson_Allen",
    "Bacon": None,
    "L. Bacon": None,
    "Sears": None,  # Edmund Hamilton Sears - no entity page
    "E. H. Sears": None,
    "T. Moore": "Thomas_Moore",
    "Williams": "William_Williams_of_Pantycelyn",
    "Kent": None,
    "Martineau\u2019s Coll": None,
    "Hill": "Rowland_Hill",
    "T. Campbell": None,  # Thomas Campbell (poet), not Alexander
    "Wm. Wilson": None,
    "Pratt\u2019s Coll": None,
    "E. Robinson": None,
    "Wardlaw": None,
    "Wardlaw\u2019s Coll": None,
    "Miss H. M. Williams": "Helen_Maria_Williams",
    "Bourne\u2019s Coll": None,
    "Noel\u2019s Coll": None,
    "R. W. Noel": None,
    "B. W. Noel": None,
    "Hill\u2019s Coll": None,
    "Winchell\u2019s Sel": None,
    "Breviary": None,
    "Ancient Hymns": None,
    "Select Hymns": None,
    "Sac. Songs": None,
    "Christian Register": None,
    "Lyra Cath": None,
    "Hymns from Land of Luther": None,
    "Hymns, anc. & mod": None,
    "Con. Ev. Mag": None,
    "Spirit of the Psalms": None,
    "From the German": None,
    "From the German, by Whittier": "John_Greenleaf_Whittier",
    "Dub. Coll": None,
    "Dub. Uni. Mag": None,
    "Epis. Coll": None,
    "Exeter Coll": None,
    "Bath Coll": None,
    "Psalmist": None,
    "Pres\u2019t Davis": None,
    "A. R. W": None,
    "from the German of Hiller": None,
}

# Tate & Brady special handling - maps to both Nahum_Tate and Nicholas_Brady
DUAL_AUTHORS = {
    "Tate & Brady": ["Nahum_Tate", "Nicholas_Brady"],
}


def get_hymn_filename(hymn_number, first_line):
    """Construct the expected hymn filename from number and first line."""
    # Clean the first line for filename
    clean = first_line.strip().rstrip("!.,;:?")
    clean = re.sub(r'[^\w\s]', '', clean)
    words = clean.split()[:6]  # first 6 words
    title_part = "_".join(w.capitalize() for w in words)
    return f"Hymn_{hymn_number:04d}_{title_part}"


def find_hymn_file(hymn_number):
    """Find the actual hymn file by number prefix."""
    pattern = os.path.join(HYMNS_DIR, f"Hymn_{hymn_number:04d}_*.md")
    matches = glob.glob(pattern)
    if matches:
        return os.path.basename(matches[0]).replace(".md", "")
    return None


def build_author_hymn_map(hymns):
    """Build mapping: entity_page_name -> list of (hymn_number, first_line, hymn_filename)."""
    author_hymns = {}

    for h in hymns:
        author = h["author"]
        if not author:
            continue

        # Check dual-author mapping first, then direct mapping
        entities = []
        if author in DUAL_AUTHORS:
            entities.extend(DUAL_AUTHORS[author])
        elif author in AUTHOR_MAP:
            if AUTHOR_MAP[author]:
                entities.append(AUTHOR_MAP[author])
        else:
            # Unmapped author - skip
            pass

        hymn_file = find_hymn_file(h["hymn_number"])
        if not hymn_file:
            continue

        for entity in entities:
            if entity not in author_hymns:
                author_hymns[entity] = []
            author_hymns[entity].append({
                "number": h["hymn_number"],
                "first_line": h["first_line"],
                "filename": hymn_file,
                "section": h.get("section", ""),
            })

    # Sort each author's hymns by number
    for entity in author_hymns:
        author_hymns[entity].sort(key=lambda x: x["number"])

    return author_hymns


def build_hymns_section(hymn_list, entity_name):
    """Build the markdown section listing hymns by this author."""
    lines = []
    lines.append("## Hymns in The Christian Hymn Book")
    lines.append("")
    lines.append(f"*{len(hymn_list)} hymn(s) attributed to this author in [[The_Christian_Hymn_Book|The Christian Hymn Book]] (1870):*")
    lines.append("")

    # Group by section
    current_section = None
    for h in hymn_list:
        lines.append(f"- **{h['number']}.** [[{h['filename']}|{h['first_line']}]]")

    lines.append("")
    return "\n".join(lines)


def has_hymns_section(content):
    """Check if the page already has a hymns section."""
    return bool(re.search(r'^## Hymns in The Christian Hymn Book', content, re.MULTILINE))


def inject_hymns_section(filepath, section_text):
    """Inject the hymns section into an entity page.

    Places it before the last major section (usually ## Related Pages or similar),
    or at the end of the file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_hymns_section(content):
        # Replace existing section
        # Find from "## Hymns in The Christian Hymn Book" to the next ## or end
        pattern = r'## Hymns in The Christian Hymn Book\n.*?(?=\n## |\Z)'
        content = re.sub(pattern, section_text.rstrip(), content, flags=re.DOTALL)
    else:
        # Find a good insertion point - before ## Related Pages, ## See Also, or at end
        # Try to insert before the last ## section that looks like navigation
        insert_patterns = [
            r'\n## Related Pages',
            r'\n## See Also',
            r'\n## Related',
            r'\n## External Links',
        ]

        inserted = False
        for pat in insert_patterns:
            match = re.search(pat, content)
            if match:
                insert_pos = match.start()
                content = content[:insert_pos] + "\n\n" + section_text + content[insert_pos:]
                inserted = True
                break

        if not inserted:
            # Append at end
            content = content.rstrip() + "\n\n" + section_text + "\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    dry_run = "--dry-run" in sys.argv

    # Load Campbell hymns
    with open(CAMPBELL_JSON, "r", encoding="utf-8") as f:
        hymns = json.load(f)

    print(f"Loaded {len(hymns)} hymns from Campbell JSON")

    # Build author-hymn mapping
    author_hymns = build_author_hymn_map(hymns)
    print(f"Mapped {sum(len(v) for v in author_hymns.values())} hymns to {len(author_hymns)} entity pages")

    # Check which entities exist
    updated = 0
    skipped = 0
    missing_entities = []

    # Also track unmapped authors
    mapped_authors = set(AUTHOR_MAP.keys()) | set(DUAL_AUTHORS.keys())
    unmapped = set()
    for h in hymns:
        if h["author"] and h["author"] not in mapped_authors:
            unmapped.add(h["author"])

    if unmapped:
        print(f"\nWARNING: {len(unmapped)} unmapped author values:")
        for a in sorted(unmapped):
            count = sum(1 for h in hymns if h["author"] == a)
            print(f"  {count:3d}  {a}")

    print()

    for entity_name, hymn_list in sorted(author_hymns.items()):
        entity_path = os.path.join(ENTITIES_DIR, entity_name + ".md")
        if not os.path.exists(entity_path):
            missing_entities.append(entity_name)
            continue

        section_text = build_hymns_section(hymn_list, entity_name)

        if dry_run:
            print(f"[DRY RUN] Would update {entity_name}.md with {len(hymn_list)} hymns")
        else:
            inject_hymns_section(entity_path, section_text)
            print(f"Updated {entity_name}.md with {len(hymn_list)} hymn(s)")
            updated += 1

    if missing_entities:
        print(f"\nMissing entity pages ({len(missing_entities)}):")
        for e in missing_entities:
            print(f"  {e}")

    print(f"\nDone. Updated {updated} entity pages, skipped {skipped}, {len(missing_entities)} missing.")


if __name__ == "__main__":
    main()
