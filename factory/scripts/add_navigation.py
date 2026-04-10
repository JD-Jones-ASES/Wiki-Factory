"""
Add navigation breadcrumbs to all wiki pages.

Adds a breadcrumb line after the frontmatter closing '---' on every page:
  > [[_overview|Home]] > [[Section_Overview|Section]] > Page Title

Skips pages that already have a navigation breadcrumb.
Skips _overview.md itself (it IS home).

Usage: py -3 factory/scripts/add_navigation.py <wiki_directory>
"""
import sys
import re
import os
import yaml


# Map each wiki subdirectory to an ordered list of (label, hub_stem)
# candidates. At runtime the first candidate whose ``{wiki_dir}/{stem}.md``
# file exists wins. This lets multiple wikis share the same subdir name
# (e.g., both Hymn Wiki and Math Wiki have ``entities/``) but render the
# breadcrumb with the wiki-appropriate label and target.
SECTION_MAP = {
    'hymns': [('Hymns', 'Hymns_Overview')],
    'entities': [
        ('People', 'People_Overview'),                # Hymn Wiki
        ('Mathematicians', 'Entities_Overview'),      # Math Wiki
    ],
    'concepts': [('Ideas', 'Concepts_Overview')],
    'synthesis': [('Stories', 'Synthesis_Overview')],
    'timelines': [('Stories', 'Synthesis_Overview')],
    'sources': [('Sources', 'Sources_Overview')],
    # Math Wiki sections
    'topics':        [('Topics',        'Topics_Overview')],
    'problem_types': [('Problem Types', 'Problem_Types_Overview')],
    'techniques':    [('Techniques',    'Techniques_Overview')],
    'formulas':      [('Formulas',      'Formulas_Overview')],
}


def resolve_section_hub(candidates, wiki_dir):
    """Return a wikilink string for the first candidate hub that exists.

    If none of the candidate hub files exist yet, emit the first candidate
    as a link anyway so the breadcrumb starts resolving the moment the hub
    is created.
    """
    for label, stem in candidates:
        if os.path.exists(os.path.join(wiki_dir, stem + '.md')):
            return f'[[{stem}|{label}]]'
    if candidates:
        label, stem = candidates[0]
        return f'[[{stem}|{label}]]'
    return ''


def get_section(filepath, wiki_dir):
    """Determine which section a file belongs to based on its directory."""
    rel = os.path.relpath(filepath, wiki_dir)
    parts = rel.replace('\\', '/').split('/')

    if len(parts) > 1:
        subdir = parts[0]
        if subdir in SECTION_MAP:
            candidates = SECTION_MAP[subdir]
            return (resolve_section_hub(candidates, wiki_dir), subdir)

    return None


def add_nav_to_file(filepath, wiki_dir):
    """Add navigation breadcrumb to a single file."""
    filename = os.path.basename(filepath)

    # Skip system/overview files that don't need breadcrumbs
    skip_files = {'_overview.md', '_index.md', '_log.md', '_tag_taxonomy.md'}
    if filename in skip_files:
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has navigation
    if '[[_overview|Home]]' in content:
        return False

    # Find the end of frontmatter
    fm_match = re.match(r'^(---\s*\n.*?\n---\s*\n)', content, re.DOTALL)
    if not fm_match:
        return False

    fm_end = fm_match.end()
    rest = content[fm_end:]

    # Determine section
    section_info = get_section(filepath, wiki_dir)

    if section_info:
        section_link, section_name = section_info
        nav_line = f"\n> [[_overview|Home]] > {section_link}\n\n"
    else:
        # Root-level wiki files (overview pages, etc.)
        nav_line = f"\n> [[_overview|Home]]\n\n"

    # Remove any existing leading blank lines from rest
    rest = rest.lstrip('\n')

    new_content = content[:fm_end] + nav_line + rest

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: py -3 add_navigation.py <wiki_directory>", file=sys.stderr)
        sys.exit(1)

    wiki_dir = sys.argv[1]

    if not os.path.isdir(wiki_dir):
        print(f"ERROR: Not a directory: {wiki_dir}", file=sys.stderr)
        sys.exit(1)

    updated = 0
    skipped = 0

    for root, dirs, files in os.walk(wiki_dir):
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            if add_nav_to_file(filepath, wiki_dir):
                updated += 1
            else:
                skipped += 1

    print(f"Updated {updated} files with navigation breadcrumbs", file=sys.stderr)
    print(f"Skipped {skipped} files (already had nav or are system files)", file=sys.stderr)


if __name__ == '__main__':
    main()
