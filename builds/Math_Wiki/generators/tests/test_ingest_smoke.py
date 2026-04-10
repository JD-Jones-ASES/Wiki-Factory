"""End-to-end ingest smoke test.

Exercises the full ingest -> consolidate -> stub-generation pipeline against
a self-contained synthetic test book at
``generators/tests/fixtures/book_test/``. Verifies the pipeline survives
changes to any component without requiring the real 62 MB of raw textbook
source.

This is the "future ingest preserved" guarantee from the Math_Wiki buildout
plan: any refactor that breaks ingestion of a new book will fail this test.

The test:
  1. Parses the synthetic book via ``parse_chapter_layout_book()``
  2. Writes the per-chapter extraction JSON to a tmp path
  3. Runs ``consolidate()`` against that tmp extractions tree
  4. Applies an empty ``aliases.yaml`` (verifies it's a no-op on fresh data)
  5. Verifies the expected topic slug + block counts + branch assignment
  6. Generates a stub via ``render_stub()`` and validates its YAML frontmatter

The synthetic book has exactly ONE chapter, ONE section, FIVE blocks:
  - 1 definition (counting-number)
  - 1 property (successor)
  - 1 example (listing successors)
  - 1 checkpoint (try counting)
  - 1 note (historical)
These counts are asserted in the test body.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml


HERE = Path(__file__).resolve().parent
FIXTURE_BOOK = HERE / "fixtures" / "book_test"
ROOT = HERE.parent.parent
TOOLS = ROOT / "tools"

# Make ingest and consolidate importable as modules.
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))


@pytest.fixture(scope="module")
def synthetic_book_spec():
    """Build a BookSpec pointing at the fixture. Uses CURRICULUM_ENVS."""
    import ingest_math_book as ing
    return ing.BookSpec(
        slug="book_test",
        title="Synthetic Test Book",
        branch_hint="pre-algebra",
        root_dir=FIXTURE_BOOK,
        layout="chapters",
        env_map=ing.CURRICULUM_ENVS,
    )


@pytest.fixture(scope="module")
def extracted_shards(synthetic_book_spec):
    """Run ingest on the synthetic book without writing anywhere."""
    import ingest_math_book as ing
    return ing.parse_chapter_layout_book(synthetic_book_spec)


def test_ingest_produces_one_chapter(extracted_shards):
    assert len(extracted_shards) == 1
    ch = extracted_shards[0]
    assert ch["book_slug"] == "book_test"
    assert ch["branch_hint"] == "pre-algebra"
    assert ch["chapter_number"] == "1"
    assert "Foundations" in ch["chapter_title"] or "Synthetic" in ch["chapter_title"]


def test_ingest_produces_one_section(extracted_shards):
    sections = extracted_shards[0]["sections"]
    assert len(sections) == 1
    sec = sections[0]
    assert sec["number"] == "1.1"
    assert sec["title_plain"] == "Synthetic Counting"


def test_ingest_extracts_all_five_blocks(extracted_shards):
    blocks = extracted_shards[0]["sections"][0]["blocks"]
    assert len(blocks) == 5
    kinds = sorted(b["kind"] for b in blocks)
    assert kinds == ["checkpoint", "definition", "example", "note", "property"]


def test_ingest_extracts_block_titles(extracted_shards):
    blocks = extracted_shards[0]["sections"][0]["blocks"]
    by_kind = {b["kind"]: b for b in blocks}
    assert by_kind["definition"]["title"] == "Counting Number"
    assert by_kind["property"]["title"] == "Successor Rule"
    assert "Listing" in by_kind["example"]["title"]


def test_consolidate_produces_one_canonical_topic(tmp_path, extracted_shards):
    """Write the shards to a tmp extractions tree, then consolidate."""
    import consolidate_extractions as ce

    # Mirror the expected layout: tmp_path/book_test/chapter_01.json
    book_out = tmp_path / "book_test"
    book_out.mkdir(parents=True, exist_ok=True)
    for shard in extracted_shards:
        ch_num = int(shard["chapter_number"])
        out_file = book_out / f"chapter_{ch_num:02d}.json"
        out_file.write_text(
            json.dumps(shard, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    topics = ce.consolidate(extractions_dir=tmp_path)

    assert len(topics) == 1, f"expected 1 topic, got {list(topics.keys())}"
    slug, topic = next(iter(topics.items()))
    assert slug == "Synthetic_Counting"
    assert topic["branch"] == "pre-algebra"
    assert topic["canonical_title"] == "Synthetic Counting"
    assert len(topic["definitions"]) == 1
    assert len(topic["properties"]) == 1
    assert len(topic["examples"]) == 1
    assert len(topic["checkpoints"]) == 1
    assert len(topic["notes"]) == 1
    assert len(topic["sources"]) == 1
    assert topic["sources"][0]["book_slug"] == "book_test"


def test_empty_aliases_yaml_is_a_noop(tmp_path, extracted_shards):
    """A freshly-written aliases.yaml with only `version: 1` must not change anything."""
    import consolidate_extractions as ce

    book_out = tmp_path / "book_test"
    book_out.mkdir(parents=True, exist_ok=True)
    for shard in extracted_shards:
        ch_num = int(shard["chapter_number"])
        (book_out / f"chapter_{ch_num:02d}.json").write_text(
            json.dumps(shard, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text("version: 1\n", encoding="utf-8")

    topics = ce.consolidate(extractions_dir=tmp_path)
    before = set(topics.keys())
    ce.apply_aliases(topics, aliases_file=aliases_file)
    after = set(topics.keys())
    assert before == after


def test_stub_generation_emits_valid_yaml_frontmatter(tmp_path, extracted_shards):
    """Generate a stub for the synthetic topic and parse its frontmatter back."""
    import consolidate_extractions as ce
    import generate_topic_stubs as gts

    book_out = tmp_path / "book_test"
    book_out.mkdir(parents=True, exist_ok=True)
    for shard in extracted_shards:
        ch_num = int(shard["chapter_number"])
        (book_out / f"chapter_{ch_num:02d}.json").write_text(
            json.dumps(shard, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    topics = ce.consolidate(extractions_dir=tmp_path)
    _, topic = next(iter(topics.items()))
    rendered = gts.render_stub(topic)

    # Frontmatter round-trips through yaml.safe_load without error
    assert rendered.startswith("---\n")
    fm_end = rendered.find("\n---\n", 4)
    assert fm_end > 0
    fm_text = rendered[4:fm_end]
    fm = yaml.safe_load(fm_text)

    assert fm is not None
    assert fm["type"] == "topic"
    assert fm["branch"] == "pre-algebra"
    assert fm["status"] == "stub"
    # Body contains the widget mount div with the correct slug
    assert 'data-topic-slug="synthetic_counting"' in rendered
    # Body references the source book
    assert "book_test" in rendered or "Synthetic Test Book" in rendered


def test_merge_rule_survives_on_synthetic_book(tmp_path, extracted_shards):
    """A merge rule naming the synthetic topic collapses correctly even with one source."""
    import consolidate_extractions as ce

    book_out = tmp_path / "book_test"
    book_out.mkdir(parents=True, exist_ok=True)
    for shard in extracted_shards:
        ch_num = int(shard["chapter_number"])
        (book_out / f"chapter_{ch_num:02d}.json").write_text(
            json.dumps(shard, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    topics = ce.consolidate(extractions_dir=tmp_path)

    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text(
        "version: 1\n"
        "renames:\n"
        "  - from: \"Synthetic_Counting\"\n"
        "    to: \"Counting_Numbers\"\n"
        "    canonical_title: \"Counting Numbers\"\n"
        "    rationale: \"test rename via smoke test\"\n",
        encoding="utf-8",
    )
    ce.apply_aliases(topics, aliases_file=aliases_file)
    assert "Synthetic_Counting" not in topics
    assert "Counting_Numbers" in topics
    assert topics["Counting_Numbers"]["canonical_title"] == "Counting Numbers"
