"""Catalog snapshot + alias-application tests for consolidate_extractions.

Runs ``consolidate()`` against a tiny pinned extraction fixture and verifies
the output matches a golden slug set. Also verifies that ``apply_aliases()``
correctly handles rename, merge, and split operations.

Catches regressions where ingest or normalization logic changes would
silently reshape the canonical topic graph.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


HERE = Path(__file__).resolve().parent
FIXTURE_EXTRACTIONS = HERE / "fixtures" / "mini_extractions"


# Add tools/ to sys.path so we can import the consolidate module directly.
TOOLS = HERE.parent.parent / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))


@pytest.fixture(scope="module")
def mini_topics():
    """Consolidate the fixture and return the raw topics dict (pre-alias)."""
    import consolidate_extractions as ce
    topics = ce.consolidate(extractions_dir=FIXTURE_EXTRACTIONS)
    return topics


def test_mini_fixture_produces_expected_slugs(mini_topics):
    """The fixture has 2 sections -> 2 canonical topics."""
    assert set(mini_topics.keys()) == {"Variables_And_Expressions", "Order_Of_Operations"}


def test_mini_fixture_topic_has_expected_structure(mini_topics):
    topic = mini_topics["Variables_And_Expressions"]
    assert topic["branch"] == "pre-algebra"
    assert topic["canonical_title"] == "Variables and Expressions"
    assert len(topic["sources"]) == 1
    assert topic["sources"][0]["book_slug"] == "book_mini"
    assert len(topic["definitions"]) == 1
    assert len(topic["examples"]) == 1
    assert topic["definitions"][0]["title"] == "Variable"


def test_consolidate_is_deterministic(mini_topics):
    """Running consolidate twice on the same fixture gives identical output."""
    import consolidate_extractions as ce
    second = ce.consolidate(extractions_dir=FIXTURE_EXTRACTIONS)
    assert sorted(mini_topics.keys()) == sorted(second.keys())
    for slug in mini_topics:
        assert mini_topics[slug]["sources"] == second[slug]["sources"]
        assert mini_topics[slug]["definitions"] == second[slug]["definitions"]


def test_empty_aliases_is_noop(tmp_path, mini_topics):
    """An aliases.yaml with only `version: 1` changes nothing."""
    import consolidate_extractions as ce
    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text("version: 1\n", encoding="utf-8")
    before = {k: dict(v) for k, v in mini_topics.items()}
    ce.apply_aliases(before, aliases_file=aliases_file)
    assert set(before.keys()) == set(mini_topics.keys())


def test_rename_updates_slug_and_title(tmp_path, mini_topics):
    """A rename rule changes slug + canonical_title, nothing else."""
    import consolidate_extractions as ce
    topics = {k: dict(v) for k, v in mini_topics.items()}
    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text(
        "version: 1\n"
        "renames:\n"
        "  - from: \"Order_Of_Operations\"\n"
        "    to: \"Order_Of_Ops\"\n"
        "    canonical_title: \"Order of Ops\"\n"
        "    rationale: \"test rename\"\n",
        encoding="utf-8",
    )
    ce.apply_aliases(topics, aliases_file=aliases_file)
    assert "Order_Of_Operations" not in topics
    assert "Order_Of_Ops" in topics
    assert topics["Order_Of_Ops"]["canonical_title"] == "Order of Ops"
    assert topics["Order_Of_Ops"]["slug"] == "Order_Of_Ops"


def test_merge_collapses_slugs_and_preserves_blocks(tmp_path, mini_topics):
    """Merging two slugs keeps every source+definition+example."""
    import consolidate_extractions as ce
    topics = {k: dict(v) for k, v in mini_topics.items()}
    # Deep-copy inner lists so we don't mutate the fixture
    for slug, topic in topics.items():
        for key in ("sources", "definitions", "properties", "examples", "theorems",
                    "figures", "checkpoints", "notes", "concepts", "aliases"):
            topic[key] = list(topic.get(key, []))

    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text(
        "version: 1\n"
        "merges:\n"
        "  - from: [\"Variables_And_Expressions\", \"Order_Of_Operations\"]\n"
        "    into: \"Foundations\"\n"
        "    canonical_title: \"Foundations\"\n"
        "    rationale: \"test merge\"\n",
        encoding="utf-8",
    )
    ce.apply_aliases(topics, aliases_file=aliases_file)
    assert "Variables_And_Expressions" not in topics
    assert "Order_Of_Operations" not in topics
    assert "Foundations" in topics
    merged = topics["Foundations"]
    # Both source blocks should survive
    assert len(merged["sources"]) == 2
    assert len(merged["definitions"]) == 1
    assert len(merged["examples"]) == 1
    assert len(merged["properties"]) == 1
    # Old titles preserved as aliases
    assert "Variables and Expressions" in merged["aliases"]
    assert "Order of Operations" in merged["aliases"]


def test_merge_into_existing_slug_keeps_target(tmp_path, mini_topics):
    """When 'into' is one of the 'from' slugs, the target topic is reused."""
    import consolidate_extractions as ce
    topics = {k: dict(v) for k, v in mini_topics.items()}
    for slug, topic in topics.items():
        for key in ("sources", "definitions", "properties", "examples", "theorems",
                    "figures", "checkpoints", "notes", "concepts", "aliases"):
            topic[key] = list(topic.get(key, []))

    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text(
        "version: 1\n"
        "merges:\n"
        "  - from: [\"Variables_And_Expressions\", \"Order_Of_Operations\"]\n"
        "    into: \"Variables_And_Expressions\"\n"
        "    rationale: \"target is one of the sources\"\n",
        encoding="utf-8",
    )
    ce.apply_aliases(topics, aliases_file=aliases_file)
    assert "Order_Of_Operations" not in topics
    assert "Variables_And_Expressions" in topics
    assert len(topics["Variables_And_Expressions"]["sources"]) == 2


def test_split_partitions_by_source(tmp_path, mini_topics):
    """A split rule routes sources/blocks to children by book_slug + section."""
    import consolidate_extractions as ce
    # Seed a single 'Combined' topic containing both sections.
    topics = {k: dict(v) for k, v in mini_topics.items()}
    combined = ce.new_topic("Combined", "pre-algebra", "Combined")
    for k in ("sources", "definitions", "properties", "examples"):
        combined[k] = (
            list(topics["Variables_And_Expressions"].get(k, []))
            + list(topics["Order_Of_Operations"].get(k, []))
        )
    # Remove the originals so only Combined exists
    del topics["Variables_And_Expressions"]
    del topics["Order_Of_Operations"]
    topics["Combined"] = combined

    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text(
        "version: 1\n"
        "splits:\n"
        "  - from: \"Combined\"\n"
        "    into:\n"
        "      - slug: \"Vars\"\n"
        "        canonical_title: \"Vars\"\n"
        "        keep_sources_matching:\n"
        "          - section_prefix: \"1.1\"\n"
        "      - slug: \"Ord\"\n"
        "        canonical_title: \"Ord\"\n"
        "        keep_sources_matching:\n"
        "          - section_prefix: \"1.2\"\n"
        "    rationale: \"test split\"\n",
        encoding="utf-8",
    )
    ce.apply_aliases(topics, aliases_file=aliases_file)
    assert "Combined" not in topics
    assert "Vars" in topics
    assert "Ord" in topics
    assert len(topics["Vars"]["definitions"]) == 1
    assert len(topics["Ord"]["properties"]) == 1
    assert len(topics["Vars"]["examples"]) == 1
    assert len(topics["Ord"]["examples"]) == 0


def test_rule_conflict_raises(tmp_path, mini_topics):
    """A slug touched by multiple destination rules should error."""
    import consolidate_extractions as ce
    topics = {k: dict(v) for k, v in mini_topics.items()}
    aliases_file = tmp_path / "aliases.yaml"
    aliases_file.write_text(
        "version: 1\n"
        "renames:\n"
        "  - from: \"Order_Of_Operations\"\n"
        "    to: \"Target\"\n"
        "    rationale: \"first claim\"\n"
        "merges:\n"
        "  - from: [\"Variables_And_Expressions\"]\n"
        "    into: \"Target\"\n"
        "    rationale: \"second claim\"\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="multiple rules"):
        ce.apply_aliases(topics, aliases_file=aliases_file)


def test_golden_branch_distribution():
    """The LIVE catalog (raw/catalog/) must have the expected branch counts.

    This is a snapshot test on the real Math_Wiki catalog: if anyone tweaks
    ingest or normalization and the branch counts drift without an aliases.yaml
    rule to explain it, this test fails.
    """
    repo_root = HERE.parent.parent
    index_file = repo_root / "raw" / "catalog" / "index.json"
    if not index_file.exists():
        pytest.skip("live catalog not built yet")

    index = json.loads(index_file.read_text(encoding="utf-8"))
    by_branch = index["by_branch"]
    # Known good values as of the plan's starting state (Phase 2c Wave 3).
    # If aliases.yaml rules change these numbers, update this assertion
    # together with the aliases.yaml change and commit them in the same PR.
    expected_ranges = {
        # Allow ±3 per branch to accommodate minor fixture or alias edits.
        "pre-algebra": (85, 95),
        "algebra-1": (40, 55),
        "algebra-2": (40, 55),
        "pre-calculus": (35, 60),
    }
    for branch, (lo, hi) in expected_ranges.items():
        assert branch in by_branch, f"branch {branch} missing from catalog index"
        count = by_branch[branch]["topic_count"]
        assert lo <= count <= hi, (
            f"branch {branch} has {count} topics, expected {lo}-{hi}. "
            f"If this change is intentional, update the range in "
            f"test_consolidate_snapshot.py and document in aliases.yaml."
        )
