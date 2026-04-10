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


# Map page type/directory to breadcrumb section
SECTION_MAP = {
    'hymns': ('[[Hymns_Overview|Hymns]]', 'hymns'),
    'entities': ('[[People_Overview|People]]', 'entities'),
    'concepts': ('[[Concepts_Overview|Ideas]]', 'concepts'),
    'synthesis': ('[[Synthesis_Overview|Stories]]', 'synthesis'),
    'timelines': ('[[Synthesis_Overview|Stories]]', 'timelines'),
    'sources': ('Sources', 'sources'),
    # Math Wiki sections
    'topics': ('[[Topics_Overview|Topics]]', 'topics'),
    'problem_types': ('[[Problem_Types_Overview|Problem Types]]', 'problem_types'),
    'techniques': ('[[Techniques_Overview|Techniques]]', 'techniques'),
    'formulas': ('[[Formulas_Overview|Formulas]]', 'formulas'),
}


def get_section(filepath, wiki_dir):
    """Determine which section a file belongs to based on its directory."""
    rel = os.path.relpath(filepath, wiki_dir)
    parts = rel.replace('\\', '/').split('/')

    if len(parts) > 1:
        subdir = parts[0]
        if subdir in SECTION_MAP:
            return SECTION_MAP[subdir]

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
