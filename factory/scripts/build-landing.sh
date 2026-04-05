#!/bin/bash
# build-landing.sh — Generate the Wiki Factory landing page HTML
# Scans builds/ for wiki directories (skips _* prefixed), extracts metadata,
# and emits a responsive HTML page with a card per wiki.
#
# Usage: bash factory/scripts/build-landing.sh > _site/index.html

BUILDS_DIR="builds"

# Count pages in a wiki directory
count_pages() {
    find "$1" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' '
}

# Extract title from _overview.md frontmatter
get_title() {
    local overview="$1/wiki/_overview.md"
    if [ -f "$overview" ]; then
        grep '^title:' "$overview" | head -1 | sed 's/^title:\s*"*//;s/"*\s*$//'
    else
        basename "$1" | tr '_' ' '
    fi
}

# Extract description from project spec
get_description() {
    local spec="$1/$(basename "$1").md"
    if [ -f "$spec" ]; then
        # Match table row: | **Scope** | description |
        grep '\*\*Scope\*\*' "$spec" | head -1 | sed 's/.*\*\*Scope\*\* *| *//;s/ *|.*$//'
    else
        echo "A comprehensive wiki"
    fi
}

# Collect wiki data
wikis=()
while IFS= read -r -d '' dir; do
    name=$(basename "$dir")
    # Skip _prefixed directories
    [[ "$name" == _* ]] && continue
    # Must have a wiki/ subdirectory
    [ -d "$dir/wiki" ] || continue
    wikis+=("$dir")
done < <(find "$BUILDS_DIR" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

# Emit HTML
cat << 'HEADER'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wiki Factory</title>
    <style>
        :root {
            --bg: #faf8f8;
            --card-bg: #ffffff;
            --text: #2b2b2b;
            --text-muted: #6b6b6b;
            --accent: #284b63;
            --accent-light: #84a59d;
            --border: #e5e5e5;
            --shadow: rgba(0, 0, 0, 0.06);
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --bg: #161618;
                --card-bg: #1e1e20;
                --text: #ebebec;
                --text-muted: #a0a0a0;
                --accent: #7b97aa;
                --accent-light: #84a59d;
                --border: #393639;
                --shadow: rgba(0, 0, 0, 0.2);
            }
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        header {
            text-align: center;
            padding: 3rem 1.5rem 1.5rem;
            max-width: 640px;
        }
        header h1 {
            font-family: 'Schibsted Grotesk', sans-serif;
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--accent);
            margin-bottom: 0.5rem;
        }
        header p {
            font-size: 1.1rem;
            color: var(--text-muted);
            line-height: 1.5;
        }
        .wikis {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            padding: 1.5rem;
            max-width: 900px;
            width: 100%;
        }
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.8rem;
            text-decoration: none;
            color: inherit;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
            box-shadow: 0 2px 8px var(--shadow);
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px var(--shadow);
        }
        .card h2 {
            font-family: 'Schibsted Grotesk', sans-serif;
            font-size: 1.4rem;
            color: var(--accent);
            margin-bottom: 0.5rem;
        }
        .card .description {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 1rem;
        }
        .card .stats {
            font-size: 0.85rem;
            color: var(--accent-light);
            font-weight: 600;
        }
        footer {
            margin-top: auto;
            padding: 2rem 1.5rem;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
        }
        footer a { color: var(--accent-light); text-decoration: none; }
        footer a:hover { text-decoration: underline; }
        @media (max-width: 480px) {
            header h1 { font-size: 1.8rem; }
            .wikis { padding: 1rem; gap: 1rem; }
            .card { padding: 1.3rem; }
        }
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;700&family=Source+Sans+Pro:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <h1>Wiki Factory</h1>
        <p>Encyclopedic wikis built from primary sources. Browse, search, and explore.</p>
    </header>
    <div class="wikis">
HEADER

# Emit a card for each wiki
for dir in "${wikis[@]}"; do
    name=$(basename "$dir")
    title=$(get_title "$dir")
    desc=$(get_description "$dir")
    pages=$(count_pages "$dir/wiki")

    cat << CARD
        <a class="card" href="./${name}/" target="_blank" rel="noopener">
            <h2>${title}</h2>
            <div class="description">${desc}</div>
            <div class="stats">${pages} pages</div>
        </a>
CARD
done

cat << 'FOOTER'
    </div>
    <footer>
        Built with <a href="https://github.com/JD-Jones-ASES/Wiki-Factory">Wiki Factory</a> &middot;
        Content licensed <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>
    </footer>
</body>
</html>
FOOTER
