#!/usr/bin/env python3
"""Parse a math textbook's LaTeX source into per-chapter JSON shards.

Handles two LaTeX conventions discovered in the source books:

  * Books 1-4 (Curriculum Factory convention):
      keyterm, property, example, checkpoint, note, caution, keyconcept, figure
  * Book 5 (Stitz-Zeager AlgTrig):
      defn, thm, cor, ex, eqn, fig

Output lands in ``raw/extractions/{book_slug}/chapter_NN.json`` --- one file per
chapter so no single JSON balloons.  Each chapter file contains the section
hierarchy plus every extracted block (definitions, theorems, examples, ...).

Run from ``builds/Math_Wiki/``:

    py -3 tools/ingest_math_book.py --book algebra_1
    py -3 tools/ingest_math_book.py --all
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BOOKS_DIR = ROOT / "raw" / "books"
EXTRACTIONS_DIR = ROOT / "raw" / "extractions"


# ---------------------------------------------------------------------------
# Book registry

@dataclass
class BookSpec:
    slug: str
    title: str
    branch_hint: str        # suggested math branch for topics from this book
    root_dir: Path          # where the book source lives
    layout: str             # "chapters" for books 1-4, "topicfolders" for book 5
    env_map: dict           # env_name → canonical_kind


# Books 1-4 share the Curriculum Factory env convention
CURRICULUM_ENVS = {
    "keyterm": "definition",
    "property": "property",
    "example": "example",
    "checkpoint": "checkpoint",
    "note": "note",
    "caution": "caution",
    "keyconcept": "concept",
    "figure": "figure",
}

# Book 5 (Stitz-Zeager) uses amsthm-style environments
STITZ_ENVS = {
    "defn": "definition",
    "thm": "theorem",
    "cor": "corollary",
    "ex": "example",
    "eqn": "equation",
    "fig": "figure",
}


BOOKS = {
    "math_1": BookSpec(
        slug="math_1",
        title="Math I",
        branch_hint="pre-algebra",
        root_dir=BOOKS_DIR / "math_1",
        layout="chapters",
        env_map=CURRICULUM_ENVS,
    ),
    "math_2": BookSpec(
        slug="math_2",
        title="Math II",
        branch_hint="pre-algebra",
        root_dir=BOOKS_DIR / "math_2",
        layout="chapters",
        env_map=CURRICULUM_ENVS,
    ),
    "algebra_1": BookSpec(
        slug="algebra_1",
        title="Algebra I",
        branch_hint="algebra-1",
        root_dir=BOOKS_DIR / "algebra_1",
        layout="chapters",
        env_map=CURRICULUM_ENVS,
    ),
    "algebra_2": BookSpec(
        slug="algebra_2",
        title="Algebra II",
        branch_hint="algebra-2",
        root_dir=BOOKS_DIR / "algebra_2",
        layout="chapters",
        env_map=CURRICULUM_ENVS,
    ),
    "algtrig": BookSpec(
        slug="algtrig",
        title="Algebra & Trigonometry (Stitz-Zeager, Corrected 3rd)",
        branch_hint="pre-calculus",
        root_dir=BOOKS_DIR / "algtrig",
        layout="topicfolders",
        env_map=STITZ_ENVS,
    ),
}


# ---------------------------------------------------------------------------
# Light LaTeX stripping (for plain-text titles and summaries)

def strip_latex(text: str) -> str:
    """Convert LaTeX markup to approximate plain text.

    Preserves inline math content (drops the ``$`` delimiters). Drops
    `\\label`, `\\index`, and `\\textbf`/`\\emph`-style wrappers.
    """
    t = text
    # Strip \label{...} and \index{...} entirely
    t = re.sub(r"\\(?:label|index)\{[^}]*\}", "", t)
    # Unwrap \textbf{X}, \textit{X}, \emph{X}, \text{X}, \mathbf{X}, \mathrm{X}
    wrappers = ("textbf", "textit", "emph", "text", "mathbf", "mathrm", "mathit")
    for w in wrappers:
        t = re.sub(r"\\" + w + r"\{([^{}]*)\}", r"\1", t)
    # Strip \frac{a}{b} → a/b, not perfect but readable
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    # Drop remaining backslashed commands with braced arguments (one-level)
    t = re.sub(r"\\[a-zA-Z]+\*?\{([^{}]*)\}", r"\1", t)
    # Drop remaining backslashed commands without arguments
    t = re.sub(r"\\[a-zA-Z]+\*?", "", t)
    # Drop $ delimiters, keep content
    t = re.sub(r"\$([^$]*)\$", r"\1", t)
    # Collapse whitespace
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def slugify(text: str) -> str:
    """Title-case slug (underscores) suitable for wiki filenames."""
    # Strip LaTeX first
    plain = strip_latex(text)
    # Title-case each word, strip non-alphanumerics
    words = re.findall(r"[A-Za-z0-9]+", plain)
    if not words:
        return "untitled"
    return "_".join(w.capitalize() for w in words)


# ---------------------------------------------------------------------------
# Block extraction

@dataclass
class Block:
    env: str                # raw env name (e.g. "keyterm")
    kind: str               # canonical kind (e.g. "definition")
    title: str | None       # optional [title] argument
    title_plain: str | None
    label: str | None       # inner \label{...} if present
    body_latex: str
    body_preview: str       # first ~200 chars of stripped body


@dataclass
class Section:
    number: str
    title: str
    title_plain: str
    label: str | None
    source_file: str
    blocks: list[Block] = field(default_factory=list)


def extract_blocks(text: str, env_map: dict) -> list[Block]:
    """Extract all matching \\begin{env}[title]...\\end{env} blocks.

    Does not handle nested same-env blocks (rare in these textbooks).
    """
    results: list[Block] = []
    for env, kind in env_map.items():
        pattern = re.compile(
            r"\\begin\{" + re.escape(env) + r"\}"
            r"(?:\[([^\]]*)\])?"
            r"(.*?)"
            r"\\end\{" + re.escape(env) + r"\}",
            re.DOTALL,
        )
        for m in pattern.finditer(text):
            title = m.group(1)
            body = m.group(2).strip()
            label_m = re.search(r"\\label\{([^}]+)\}", body)
            body_plain = strip_latex(body)
            results.append(
                Block(
                    env=env,
                    kind=kind,
                    title=title,
                    title_plain=strip_latex(title) if title else None,
                    label=label_m.group(1) if label_m else None,
                    body_latex=body,
                    body_preview=body_plain[:200] + ("…" if len(body_plain) > 200 else ""),
                )
            )
    return results


# ---------------------------------------------------------------------------
# Books 1-4: chapters/chNN/sections/secMM.tex layout

CHAPTER_DIR_RE = re.compile(r"^ch(\d+)$")
SECTION_FILE_RE = re.compile(r"^sec(\d+)\.tex$")
CHAPTER_TITLE_RE = re.compile(r"\\chapter\*?\{([^}]+)\}")
SECTION_TITLE_RE = re.compile(r"\\section\*?\{([^}]+)\}")


def parse_chapter_layout_book(book: BookSpec) -> list[dict]:
    """Parse a book with chapters/chNN/sections/secMM.tex layout."""
    chapters_dir = book.root_dir / "chapters"
    if not chapters_dir.exists():
        print(f"  ERROR: no chapters/ directory under {book.root_dir}", file=sys.stderr)
        return []

    chapter_dirs = sorted(
        [d for d in chapters_dir.iterdir() if d.is_dir() and CHAPTER_DIR_RE.match(d.name)],
        key=lambda d: int(CHAPTER_DIR_RE.match(d.name).group(1)),
    )

    chapter_shards: list[dict] = []

    for ch_dir in chapter_dirs:
        ch_num_int = int(CHAPTER_DIR_RE.match(ch_dir.name).group(1))
        ch_num = str(ch_num_int)

        chapter_file = ch_dir / "chapter.tex"
        if not chapter_file.exists():
            continue
        ch_text = chapter_file.read_text(encoding="utf-8", errors="ignore")
        ch_title_m = CHAPTER_TITLE_RE.search(ch_text)
        ch_title = strip_latex(ch_title_m.group(1)) if ch_title_m else f"Chapter {ch_num}"

        # Section files
        sections_dir = ch_dir / "sections"
        if not sections_dir.exists():
            print(f"  skip {book.slug} ch{ch_num}: no sections/ dir")
            continue
        section_files = sorted(
            [f for f in sections_dir.iterdir() if SECTION_FILE_RE.match(f.name)],
            key=lambda f: int(SECTION_FILE_RE.match(f.name).group(1)),
        )

        sections: list[Section] = []
        for idx, sf in enumerate(section_files, start=1):
            sec_text = sf.read_text(encoding="utf-8", errors="ignore")
            title_m = SECTION_TITLE_RE.search(sec_text)
            sec_title_raw = title_m.group(1) if title_m else f"Section {ch_num}.{idx}"
            sec_title_plain = strip_latex(sec_title_raw)

            label_m = re.search(r"\\label\{([^}]+)\}", sec_text)
            rel_path = str(sf.relative_to(book.root_dir)).replace("\\", "/")

            blocks = extract_blocks(sec_text, book.env_map)

            sections.append(
                Section(
                    number=f"{ch_num}.{idx}",
                    title=sec_title_raw,
                    title_plain=sec_title_plain,
                    label=label_m.group(1) if label_m else None,
                    source_file=rel_path,
                    blocks=blocks,
                )
            )

        chapter_shards.append(
            {
                "book_slug": book.slug,
                "book_title": book.title,
                "branch_hint": book.branch_hint,
                "chapter_number": ch_num,
                "chapter_title": ch_title,
                "sections": [_section_to_dict(s) for s in sections],
            }
        )

    return chapter_shards


# ---------------------------------------------------------------------------
# Book 5: topic-folder layout

# Book 5 has topic folders like LinearQuadratic/, each containing section .tex files.
# Use folder order from the SectionGuide.tex if available, otherwise alpha.
BOOK5_CHAPTER_FOLDERS = [
    ("RelationsandFunctions", "1", "Relations and Functions"),
    ("LinearQuadratic", "2", "Linear and Quadratic Functions"),
    ("Polynomials", "3", "Polynomial Functions"),
    ("Rationals", "4", "Rational Functions"),
    ("Further", "5", "Further Topics in Functions"),
    ("ExpLogs", "6", "Exponential and Logarithmic Functions"),
    ("IntroTrig", "7", "Foundations of Trigonometry"),
    ("AppExt", "8", "Applications of Trigonometry"),
    ("SequencesandSeries", "9", "Sequences and the Binomial Theorem"),
    ("Conics", "10", "Conic Sections"),
    ("Matrices", "11", "Systems of Equations and Matrices"),
]


def parse_topicfolder_layout_book(book: BookSpec) -> list[dict]:
    chapter_shards: list[dict] = []

    for folder_name, ch_num, ch_title_default in BOOK5_CHAPTER_FOLDERS:
        folder = book.root_dir / folder_name
        if not folder.exists():
            continue

        # Section files: every .tex in the folder, sorted alphabetically by name,
        # excluding the chapter compiler/glue files.
        all_tex = sorted(folder.glob("*.tex"))
        section_files = [
            f for f in all_tex
            if not f.name.startswith("Compiler")
            and not f.name.startswith("Chapter")
            and f.name != folder_name + ".tex"  # exclude the chapter glue file
        ]

        sections: list[Section] = []
        for idx, sf in enumerate(section_files, start=1):
            sec_text = sf.read_text(encoding="utf-8", errors="ignore")
            title_m = SECTION_TITLE_RE.search(sec_text)
            sec_title_raw = title_m.group(1) if title_m else sf.stem
            sec_title_plain = strip_latex(sec_title_raw)
            label_m = re.search(r"\\label\{([^}]+)\}", sec_text)
            rel_path = str(sf.relative_to(book.root_dir)).replace("\\", "/")

            blocks = extract_blocks(sec_text, book.env_map)

            sections.append(
                Section(
                    number=f"{ch_num}.{idx}",
                    title=sec_title_raw,
                    title_plain=sec_title_plain,
                    label=label_m.group(1) if label_m else None,
                    source_file=rel_path,
                    blocks=blocks,
                )
            )

        if not sections:
            continue

        chapter_shards.append(
            {
                "book_slug": book.slug,
                "book_title": book.title,
                "branch_hint": book.branch_hint,
                "chapter_number": ch_num,
                "chapter_title": ch_title_default,
                "sections": [_section_to_dict(s) for s in sections],
            }
        )

    return chapter_shards


def _section_to_dict(s: Section) -> dict:
    block_dicts = [asdict(b) for b in s.blocks]
    block_counts: dict[str, int] = {}
    for b in s.blocks:
        block_counts[b.kind] = block_counts.get(b.kind, 0) + 1
    return {
        "number": s.number,
        "title_latex": s.title,
        "title_plain": s.title_plain,
        "label": s.label,
        "source_file": s.source_file,
        "block_counts": block_counts,
        "blocks": block_dicts,
    }


# ---------------------------------------------------------------------------
# Entry points

def ingest_book(book: BookSpec) -> dict:
    """Parse a book and write per-chapter JSON shards. Return summary."""
    print(f"Ingesting {book.slug} ({book.title}) --- layout={book.layout}")
    out_dir = EXTRACTIONS_DIR / book.slug
    out_dir.mkdir(parents=True, exist_ok=True)

    if book.layout == "chapters":
        shards = parse_chapter_layout_book(book)
    elif book.layout == "topicfolders":
        shards = parse_topicfolder_layout_book(book)
    else:
        raise ValueError(f"unknown layout: {book.layout}")

    total_blocks = 0
    total_bytes = 0
    for shard in shards:
        ch_num = shard["chapter_number"]
        out_file = out_dir / f"chapter_{int(ch_num):02d}.json"
        out_file.write_text(
            json.dumps(shard, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        section_count = len(shard["sections"])
        block_count = sum(len(s["blocks"]) for s in shard["sections"])
        size_kb = out_file.stat().st_size / 1024
        total_blocks += block_count
        total_bytes += out_file.stat().st_size
        print(f"  ch{ch_num:>2} {shard['chapter_title']:<45} "
              f"{section_count:>2} sections, {block_count:>3} blocks, {size_kb:>6.1f} KB")

    print(f"  {book.slug}: {len(shards)} chapters, "
          f"{total_blocks} blocks, {total_bytes / 1024:.1f} KB total")
    return {
        "book_slug": book.slug,
        "chapter_count": len(shards),
        "total_blocks": total_blocks,
        "total_bytes": total_bytes,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", help="ingest one book by slug", choices=list(BOOKS.keys()))
    parser.add_argument("--all", action="store_true", help="ingest all books")
    args = parser.parse_args()

    if not args.book and not args.all:
        parser.error("specify --book <slug> or --all")

    EXTRACTIONS_DIR.mkdir(parents=True, exist_ok=True)

    summaries: list[dict] = []
    if args.all:
        for slug, book in BOOKS.items():
            summaries.append(ingest_book(book))
    else:
        summaries.append(ingest_book(BOOKS[args.book]))

    print()
    print("=== Summary ===")
    for s in summaries:
        print(f"  {s['book_slug']}: {s['chapter_count']} chapters, "
              f"{s['total_blocks']} blocks, {s['total_bytes'] / 1024:.1f} KB")


if __name__ == "__main__":
    main()
