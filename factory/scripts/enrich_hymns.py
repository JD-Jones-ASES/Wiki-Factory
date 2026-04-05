#!/usr/bin/env python3
"""
enrich_hymns.py - Enrich hymn stub pages with data from Duffield, Metcalf, and Nutter.

Matches extracted JSON data to existing hymn pages by first-line fuzzy matching,
then injects historical context, composer/tune info, era assignments, and related links.

Usage: py -3 factory/scripts/enrich_hymns.py builds/Hymn_Wiki/
"""

import json
import os
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher


def normalize_first_line(s):
    """Normalize a first line for fuzzy matching."""
    s = s.lower().strip()
    # Remove punctuation except apostrophes
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def similarity(a, b):
    """Return similarity ratio between two normalized strings."""
    return SequenceMatcher(None, a, b).ratio()


def load_json(path):
    """Load a JSON file with utf-8 encoding."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"  WARNING: Could not load {path}: {e}")
        return None


def parse_hymn_frontmatter(content):
    """Extract frontmatter fields from a hymn page."""
    fm = {}
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).split("\n"):
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            # Remove quotes
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fm[key] = val
    return fm


def update_frontmatter_field(content, field, new_value):
    """Update a single frontmatter field in the content string."""
    # Match the field line in frontmatter
    pattern = rf'^({field}:\s*)(.*)$'
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        old_line = match.group(0)
        new_line = f'{field}: {new_value}'
        content = content.replace(old_line, new_line, 1)
    return content


def build_historical_context(duffield_entry, nutter_entries):
    """Build a Historical Context section from available data."""
    sections = []

    if duffield_entry:
        parts = []
        story = duffield_entry.get("composition_story", "").strip()
        if story and len(story) > 20:
            # Clean OCR artifacts
            story = re.sub(r"\s+", " ", story).strip()
            parts.append(story)

        textual = duffield_entry.get("textual_notes", "").strip()
        if textual and len(textual) > 20:
            textual = re.sub(r"\s+", " ", textual).strip()
            parts.append(textual)

        anecdotes = duffield_entry.get("anecdotes", "").strip()
        if anecdotes and len(anecdotes) > 20:
            anecdotes = re.sub(r"\s+", " ", anecdotes).strip()
            parts.append(anecdotes)

        if parts:
            sections.append("### From Duffield (1886)\n\n" + "\n\n".join(parts))

    for nutter in nutter_entries:
        parts = []
        story = nutter.get("composition_story", "").strip()
        if story and len(story) > 20:
            story = re.sub(r"\s+", " ", story).strip()
            parts.append(story)

        textual = nutter.get("textual_notes", "").strip()
        if textual and len(textual) > 20:
            textual = re.sub(r"\s+", " ", textual).strip()
            parts.append(textual)

        anecdotes = nutter.get("anecdotes", "").strip()
        if anecdotes and len(anecdotes) > 20:
            anecdotes = re.sub(r"\s+", " ", anecdotes).strip()
            parts.append(anecdotes)

        assessment = nutter.get("critical_assessment", "").strip()
        if assessment and len(assessment) > 20:
            assessment = re.sub(r"\s+", " ", assessment).strip()
            parts.append(assessment)

        if parts:
            sections.append("### From Nutter & Tillett (1911)\n\n" + "\n\n".join(parts))

    if sections:
        return "## Historical Context\n\n" + "\n\n".join(sections)
    return ""


def determine_era(author_name, dates_hint=""):
    """Guess era from known author dates. Returns era string or empty."""
    # Known major authors and their eras
    era_map = {
        "watts": "18th-century",
        "wesley": "18th-century",
        "newton": "18th-century",
        "cowper": "18th-century",
        "doddridge": "18th-century",
        "toplady": "18th-century",
        "steele": "18th-century",
        "perronet": "18th-century",
        "hart": "18th-century",
        "robinson": "18th-century",
        "medley": "18th-century",
        "fawcett": "18th-century",
        "stennett": "18th-century",
        "addison": "18th-century",
        "ken": "18th-century",
        "gerhardt": "post-reformation",
        "luther": "reformation",
        "heermann": "post-reformation",
        "nicolai": "post-reformation",
        "rinkart": "post-reformation",
        "neander": "post-reformation",
        "tersteegen": "18th-century",
        "zinzendorf": "18th-century",
        "heber": "19th-century",
        "lyte": "19th-century",
        "elliott": "19th-century",
        "newman": "19th-century",
        "keble": "19th-century",
        "bonar": "19th-century",
        "crosby": "19th-century",
        "faber": "19th-century",
        "havergal": "19th-century",
        "brooks": "19th-century",
        "whittier": "19th-century",
        "montgomery": "19th-century",
        "palmer": "19th-century",
        "smith": "19th-century",
        "baring-gould": "19th-century",
        "matheson": "19th-century",
        "spafford": "19th-century",
        "bliss": "19th-century",
        "lowry": "19th-century",
        "doane": "19th-century",
        "alexander": "19th-century",
        "ambrose": "early-church",
        "bernard": "medieval",
        "aquinas": "medieval",
        "fortunatus": "early-church",
        "prudentius": "early-church",
        "john of damascus": "early-church",
        "ephrem": "early-church",
        "clement": "early-church",
        "gregory": "early-church",
    }
    if author_name:
        name_lower = author_name.lower().strip()
        for key, era in era_map.items():
            if key in name_lower:
                return era
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: py -3 factory/scripts/enrich_hymns.py builds/Hymn_Wiki/")
        sys.exit(1)

    wiki_root = Path(sys.argv[1])
    hymns_dir = wiki_root / "wiki" / "hymns"
    data_dir = wiki_root / "wiki"

    if not hymns_dir.exists():
        print(f"ERROR: {hymns_dir} not found")
        sys.exit(1)

    # Load all data sources
    print("Loading data sources...")
    duffield_data = load_json(data_dir / "_duffield_hymn_data.json") or []
    print(f"  Duffield: {len(duffield_data)} entries")

    metcalf_raw = load_json(data_dir / "_metcalf_tune_data.json")
    metcalf_tunes = metcalf_raw.get("tunes", []) if isinstance(metcalf_raw, dict) else metcalf_raw or []
    print(f"  Metcalf: {len(metcalf_tunes)} tune entries")

    nutter_p1 = load_json(data_dir / "_nutter_hymn_data_part1.json") or []
    nutter_p2 = load_json(data_dir / "_nutter_hymn_data_part2.json") or []
    nutter_hymns = nutter_p1 + nutter_p2
    print(f"  Nutter: {len(nutter_hymns)} hymn entries")

    nutter_comp_raw = load_json(data_dir / "_nutter_composer_data.json")
    nutter_composers = nutter_comp_raw.get("composers", []) if isinstance(nutter_comp_raw, dict) else []
    print(f"  Nutter composers: {len(nutter_composers)} entries")

    # Build lookup indexes
    print("\nBuilding lookup indexes...")

    # Duffield: index by normalized first line
    duffield_index = {}
    for entry in duffield_data:
        fl = normalize_first_line(entry.get("first_line", ""))
        if fl:
            duffield_index[fl] = entry

    # Metcalf: index by normalized hymn first line
    metcalf_index = {}
    for entry in metcalf_tunes:
        fl = normalize_first_line(entry.get("hymn_first_line", ""))
        if fl:
            metcalf_index[fl] = entry

    # Nutter: index by normalized first line
    nutter_index = {}
    for entry in nutter_hymns:
        fl = normalize_first_line(entry.get("first_line", ""))
        if fl:
            if fl not in nutter_index:
                nutter_index[fl] = []
            nutter_index[fl].append(entry)

    # Nutter composers: build tune-to-composer map
    tune_composer_map = {}
    for comp in nutter_composers:
        name = comp.get("name", "")
        dates = comp.get("dates", "")
        for tune in comp.get("tunes", []):
            tune_lower = tune.lower().strip()
            tune_composer_map[tune_lower] = {"name": name, "dates": dates}

    # Also add Metcalf tune-to-composer mappings
    for entry in metcalf_tunes:
        tune = entry.get("tune_name", "").lower().strip()
        if tune:
            tune_composer_map[tune] = {"name": entry.get("composer", ""), "dates": ""}

    print(f"  Duffield index: {len(duffield_index)} entries")
    print(f"  Metcalf index: {len(metcalf_index)} entries")
    print(f"  Nutter index: {len(nutter_index)} entries")
    print(f"  Tune-composer map: {len(tune_composer_map)} entries")

    # Process hymn pages
    print("\nProcessing hymn pages...")
    hymn_files = sorted(hymns_dir.glob("Hymn_*.md"))
    print(f"  Found {len(hymn_files)} hymn files")

    stats = {
        "total": len(hymn_files),
        "duffield_matched": 0,
        "metcalf_matched": 0,
        "nutter_matched": 0,
        "context_added": 0,
        "composer_filled": 0,
        "tune_filled": 0,
        "era_filled": 0,
        "status_upgraded": 0,
        "source_refs_added": 0,
        "skipped_not_stub": 0,
    }

    for hymn_file in hymn_files:
        content = hymn_file.read_text(encoding="utf-8")
        fm = parse_hymn_frontmatter(content)
        first_line = fm.get("first_line", "")
        author = fm.get("author", "")
        norm_fl = normalize_first_line(first_line)

        if not norm_fl:
            continue

        # Match against each data source (fuzzy matching)
        duffield_match = None
        best_sim = 0
        for dfl, entry in duffield_index.items():
            sim = similarity(norm_fl, dfl)
            if sim > best_sim and sim > 0.75:
                best_sim = sim
                duffield_match = entry
        if duffield_match:
            stats["duffield_matched"] += 1

        metcalf_match = None
        best_sim = 0
        for mfl, entry in metcalf_index.items():
            sim = similarity(norm_fl, mfl)
            if sim > best_sim and sim > 0.75:
                best_sim = sim
                metcalf_match = entry
        if metcalf_match:
            stats["metcalf_matched"] += 1

        nutter_matches = []
        best_sim = 0
        best_key = None
        for nfl in nutter_index:
            sim = similarity(norm_fl, nfl)
            if sim > best_sim and sim > 0.75:
                best_sim = sim
                best_key = nfl
        if best_key:
            nutter_matches = nutter_index[best_key]
            stats["nutter_matched"] += 1

        # Determine what to update
        modified = False
        new_source_refs = []

        # 1. Fill composer field if empty
        current_composer = fm.get("composer", "").strip().strip('"')
        if not current_composer:
            composer_name = ""
            if metcalf_match:
                composer_name = metcalf_match.get("composer", "")
            if not composer_name and nutter_matches:
                for nm in nutter_matches:
                    c = nm.get("tune_composer", "")
                    if c:
                        composer_name = c
                        break
            if not composer_name and duffield_match:
                ti = duffield_match.get("tune_info", "")
                if ti:
                    composer_name = ti.split(",")[0].strip() if "," in ti else ti.strip()

            if composer_name and len(composer_name) > 2:
                content = update_frontmatter_field(content, "composer", f'"{composer_name}"')
                stats["composer_filled"] += 1
                modified = True

        # 2. Fill tune_name if empty
        current_tune = fm.get("tune_name", "").strip().strip('"')
        if not current_tune:
            tune_name = ""
            if metcalf_match:
                tune_name = metcalf_match.get("tune_name", "")
            if not tune_name and nutter_matches:
                for nm in nutter_matches:
                    t = nm.get("tune_name", "")
                    if t:
                        tune_name = t
                        break

            if tune_name and len(tune_name) > 1:
                content = update_frontmatter_field(content, "tune_name", f'"{tune_name}"')
                stats["tune_filled"] += 1
                modified = True

        # 3. Fill era if empty
        current_era = fm.get("era", "").strip().strip('"')
        if not current_era:
            era = determine_era(author)
            if era:
                content = update_frontmatter_field(content, "era", f'"{era}"')
                stats["era_filled"] += 1
                modified = True

        # 4. Add or replace Historical Context section
        context = build_historical_context(duffield_match, nutter_matches)
        if context:
            # Check if there's a placeholder to replace
            placeholder_pattern = r"## Historical Context\s*\n\s*\*This section will be enriched.*?\*\s*"
            if re.search(placeholder_pattern, content):
                content = re.sub(placeholder_pattern, lambda m: context + "\n", content)
                stats["context_added"] += 1
                modified = True
            elif "## Historical Context" not in content:
                # No context section at all — append
                content = content.rstrip() + "\n\n" + context + "\n"
                stats["context_added"] += 1
                modified = True

        # 5. Update source_refs
        current_refs = fm.get("source_refs", "")
        refs_to_add = []
        if duffield_match and "English_Hymns_Their_Authors_and_History" not in current_refs:
            refs_to_add.append("[[English_Hymns_Their_Authors_and_History]]")
        if nutter_matches and "The_Hymns_and_Hymn_Writers_of_the_Church" not in current_refs:
            refs_to_add.append("[[The_Hymns_and_Hymn_Writers_of_the_Church]]")
        if metcalf_match and "American_Writers_and_Compilers_of_Sacred_Music" not in current_refs:
            refs_to_add.append("[[American_Writers_and_Compilers_of_Sacred_Music]]")

        if refs_to_add:
            # Parse existing source_refs
            existing = re.findall(r'\[\[([^\]]+)\]\]', current_refs)
            all_refs = existing + [r.strip("[]") for r in refs_to_add]
            new_refs_str = "[" + ", ".join(f'"[[{r}]]"' for r in all_refs) + "]"
            content = update_frontmatter_field(content, "source_refs", new_refs_str)
            stats["source_refs_added"] += 1
            modified = True

        # 6. Upgrade status from stub to draft if we added meaningful content
        current_status = fm.get("status", "").strip().strip('"')
        if current_status == "stub" and (duffield_match or nutter_matches or metcalf_match):
            content = update_frontmatter_field(content, "status", "draft")
            content = update_frontmatter_field(content, "updated", "2026-04-05")
            stats["status_upgraded"] += 1
            modified = True

        # Write back if modified
        if modified:
            hymn_file.write_text(content, encoding="utf-8")

    # Report
    print("\n" + "=" * 60)
    print("ENRICHMENT COMPLETE")
    print("=" * 60)
    print(f"Total hymn pages processed: {stats['total']}")
    print(f"Duffield matches: {stats['duffield_matched']}")
    print(f"Metcalf matches: {stats['metcalf_matched']}")
    print(f"Nutter matches: {stats['nutter_matched']}")
    print(f"Historical context added: {stats['context_added']}")
    print(f"Composer fields filled: {stats['composer_filled']}")
    print(f"Tune name fields filled: {stats['tune_filled']}")
    print(f"Era fields filled: {stats['era_filled']}")
    print(f"Status upgraded (stub -> draft): {stats['status_upgraded']}")
    print(f"Source refs added: {stats['source_refs_added']}")


if __name__ == "__main__":
    main()
