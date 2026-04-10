"""Copyright-safety pytest for Math_Wiki topic pages.

Scans every markdown file under ``wiki/topics/`` (and ``wiki/formulas/``,
``wiki/techniques/``) for verbatim runs of 15 or more consecutive words copied
from the source textbook extractions in ``raw/extractions/``.

The test loads every extraction block's ``body_preview`` + ``body_latex``,
tokenizes each into a word stream, and builds a set of 10-word shingles. It
then tokenizes every published wiki page and, for every 15-word window in the
page body, checks whether any 10-word shingle inside that window appears in
the source shingle set. A hit is a verbatim-copy alarm.

Rationale: CLAUDE.md and Math_Wiki.md both mandate "never reproduce source
book text verbatim". This test makes that enforceable mechanically so the
content-enrichment sub-agents can't accidentally regress copyright safety.

Design decisions:

- **Skip code blocks and LaTeX math.** Math expressions are often necessarily
  similar across books (``\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}`` is what it is)
  and code fences aren't prose.
- **Skip frontmatter.** Metadata isn't content.
- **Normalize whitespace and punctuation.** Paraphrase differences shouldn't
  be hidden by comma reshuffling, but trivial re-wrapping shouldn't inflate
  the match count either.
- **Window = 15 tokens, shingle = 10 tokens.** A 15-word verbatim run is an
  unambiguous copy; 10-word shingles inside that window catch partial
  overlaps while keeping false positives low.
- **Whitelist known-safe runs.** Extremely common phrases (e.g., "the quadratic
  formula is", "the slope of the line") must not trip the test. We maintain
  a small allow-list of recurring boilerplate.
- **Skip auto-generated stubs.** The stub generator deliberately echoes
  source_book previews in the "In the Source Books" section. Stubs are
  detected via the ``#topic-auto-generated`` tag in frontmatter.

To run manually:

    py -3 -m pytest generators/tests/test_copyright_safety.py -v
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
import yaml


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
EXTRACTIONS_DIR = ROOT / "raw" / "extractions"
WIKI_DIR = ROOT / "wiki"

# Wiki subdirectories to scan for published content (topics, formulas, etc.)
SCAN_DIRS = ("topics", "formulas", "techniques", "synthesis")

# Configuration --------------------------------------------------------------

WINDOW_SIZE = 15
SHINGLE_SIZE = 10
# Minimum source-corpus shingle count to bother running the test (prevents
# noisy results when extractions haven't been built yet).
MIN_CORPUS_SHINGLES = 100


# Common math phrases that would trip the shingle test as "verbatim copies" but
# are actually standard mathematical definitions or theorems. Every shingle
# built from these phrases is subtracted from the source-corpus shingle set so
# they can appear in wiki pages without tripping the test.
#
# Keep this list small and specific: only genuine formal constructs where
# paraphrase would reduce precision (e.g., the canonical definition of a
# circle or the distance formula). Extend cautiously.
ALLOWLIST_PHRASES = frozenset({
    "a circle is the set of all points in a plane that are the same distance from a single fixed point",
    "the set of all points in a plane that are the same distance from a single fixed point",
    "a function is a rule that assigns to each input exactly one output",
    "the distance between two points x y and x y in the coordinate plane",
    "the product of the slopes of two perpendicular lines equals negative one",
    "the sum of the interior angles of a triangle is one hundred eighty degrees",
    "for any real numbers a b and c if a equals b then a plus c equals b plus c",
})


# ---------------------------------------------------------------------------
# Text tokenization

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
DISPLAY_MATH_RE = re.compile(r"\$\$.*?\$\$", re.DOTALL)
INLINE_MATH_RE = re.compile(r"\$[^$\n]+\$")
HTML_TAG_RE = re.compile(r"<[^>]+>")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
OBSIDIAN_EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
BLOCKQUOTE_RE = re.compile(r"^>\s?", re.MULTILINE)


def strip_markup_for_compare(text: str) -> str:
    """Aggressively strip markdown/LaTeX/HTML for shingle comparison."""
    t = text
    t = CODE_FENCE_RE.sub(" ", t)
    t = INLINE_CODE_RE.sub(" ", t)
    t = DISPLAY_MATH_RE.sub(" ", t)
    t = INLINE_MATH_RE.sub(" ", t)
    t = HTML_TAG_RE.sub(" ", t)
    t = OBSIDIAN_EMBED_RE.sub(" ", t)
    t = MARKDOWN_IMAGE_RE.sub(" ", t)
    t = MARKDOWN_LINK_RE.sub(r"\1", t)
    # Wikilinks: keep label if present, otherwise keep target
    t = WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1), t)
    t = BLOCKQUOTE_RE.sub("", t)
    return t


def tokenize(text: str) -> list[str]:
    """Lowercase word tokens with punctuation stripped."""
    t = text.lower()
    # Keep alphanumerics + keep hyphens within words dropped
    tokens = re.findall(r"\b[a-z][a-z0-9]*\b", t)
    return tokens


def shingle(tokens: list[str], size: int) -> set[tuple]:
    if len(tokens) < size:
        return set()
    return {tuple(tokens[i : i + size]) for i in range(len(tokens) - size + 1)}


# ---------------------------------------------------------------------------
# Source corpus (built once per session)

def build_allowlist_shingles() -> set[tuple]:
    """Tokenize ALLOWLIST_PHRASES into shingles to subtract from the corpus."""
    allowed: set[tuple] = set()
    for phrase in ALLOWLIST_PHRASES:
        tokens = tokenize(phrase)
        allowed.update(shingle(tokens, SHINGLE_SIZE))
    return allowed


def build_source_corpus() -> tuple[set[tuple], int]:
    """Return (set of 10-word shingles, total source tokens).

    Shingles present in ALLOWLIST_PHRASES are removed from the corpus so they
    can appear in wiki pages without triggering a verbatim-copy alarm.
    """
    shingles: set[tuple] = set()
    total_tokens = 0
    if not EXTRACTIONS_DIR.exists():
        return shingles, 0

    for chapter_file in EXTRACTIONS_DIR.rglob("chapter_*.json"):
        try:
            data = json.loads(chapter_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for section in data.get("sections", []):
            for block in section.get("blocks", []):
                for field in ("body_preview", "body_latex"):
                    body = block.get(field, "") or ""
                    stripped = strip_markup_for_compare(body)
                    tokens = tokenize(stripped)
                    total_tokens += len(tokens)
                    shingles.update(shingle(tokens, SHINGLE_SIZE))

    shingles -= build_allowlist_shingles()
    return shingles, total_tokens


@pytest.fixture(scope="session")
def source_corpus():
    shingles, token_count = build_source_corpus()
    if len(shingles) < MIN_CORPUS_SHINGLES:
        pytest.skip(
            f"source corpus too small ({len(shingles)} shingles); "
            f"run tools/ingest_math_book.py --all first"
        )
    return shingles


# ---------------------------------------------------------------------------
# Wiki page discovery

def iter_published_pages():
    """Yield (path, body_text) for every non-stub topic page."""
    for subdir in SCAN_DIRS:
        d = WIKI_DIR / subdir
        if not d.exists():
            continue
        for md in sorted(d.rglob("*.md")):
            if md.name.startswith("_"):
                continue
            text = md.read_text(encoding="utf-8")
            m = FRONTMATTER_RE.match(text)
            if m:
                try:
                    fm = yaml.safe_load(m.group(1)) or {}
                except yaml.YAMLError:
                    fm = {}
                body = text[m.end():]
            else:
                fm = {}
                body = text

            # Skip auto-stubs: they intentionally echo source previews
            tags = fm.get("tags", []) or []
            if any(
                (isinstance(t, str) and "topic-auto-generated" in t)
                for t in tags
            ):
                continue
            if fm.get("status") == "stub":
                continue

            yield md, body


# ---------------------------------------------------------------------------
# The actual test

def find_verbatim_runs(body: str, source_shingles: set[tuple]) -> list[str]:
    """Return a list of verbatim-runs (as plain-text windows) found in body.

    Any 15-word window where at least one inner 10-word shingle is present in
    ``source_shingles`` is flagged. Allowlisted shingles have already been
    subtracted from the corpus at build time so this check is purely set
    membership.
    """
    stripped = strip_markup_for_compare(body)
    tokens = tokenize(stripped)
    hits: list[str] = []
    if len(tokens) < WINDOW_SIZE:
        return hits
    for i in range(len(tokens) - WINDOW_SIZE + 1):
        window = tokens[i : i + WINDOW_SIZE]
        for j in range(WINDOW_SIZE - SHINGLE_SIZE + 1):
            sh = tuple(window[j : j + SHINGLE_SIZE])
            if sh in source_shingles:
                hits.append(" ".join(window))
                break
    return hits


def test_no_verbatim_source_copies(source_corpus):
    """Every published (non-stub) topic page must be paraphrased, not copied."""
    offenders: list[tuple[Path, list[str]]] = []
    pages_checked = 0
    for md_path, body in iter_published_pages():
        pages_checked += 1
        hits = find_verbatim_runs(body, source_corpus)
        if hits:
            offenders.append((md_path, hits[:3]))

    if pages_checked == 0:
        pytest.skip("no published (non-stub) pages to check")

    if offenders:
        lines = ["Verbatim copies detected:"]
        for path, hits in offenders:
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"  {rel}")
            for h in hits:
                lines.append(f"    -> {h[:100]}...")
        pytest.fail("\n".join(lines))


def test_corpus_has_meaningful_size(source_corpus):
    """Sanity-check: the source corpus should have thousands of shingles."""
    assert len(source_corpus) > 1000, (
        f"source corpus only has {len(source_corpus)} shingles, "
        f"extractions may be incomplete"
    )


def test_shingle_tokenizer_ignores_math_and_code():
    """A page that only contains code/math/wikilinks has zero tokens."""
    body = (
        "$$\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$$\n"
        "```python\nprint('hello')\n```\n"
        "$x = 5$ and $y = 10$\n"
        "[[Other_Page|see here]]\n"
    )
    stripped = strip_markup_for_compare(body)
    tokens = tokenize(stripped)
    # Only "see here" + "and" should survive (wikilink label + the plain 'and')
    assert len(tokens) <= 5, f"expected near-empty tokens, got {tokens}"
