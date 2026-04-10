"""Smoke tests for Phase 1 circle generators.

Each test runs against every registered generator and every supported
difficulty. A broken generator fails the build.
"""
from __future__ import annotations

import pytest

# Importing generators registers every @register-decorated class.
import generators  # noqa: F401
from generators.base import all_generators, DIFFICULTIES, Problem


# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def registered():
    return all_generators()


@pytest.fixture(scope="session")
def circle_generators(registered):
    return [g for g in registered if g.topic_slug == "circles"]


# ---------------------------------------------------------------------------

def test_phase1_ships_at_least_five_circle_generators(circle_generators):
    assert len(circle_generators) >= 5, (
        f"Phase 1 expects >=5 circle generators, found {len(circle_generators)}"
    )


def test_generator_ids_are_unique(registered):
    ids = [g.generator_id for g in registered]
    assert len(set(ids)) == len(ids), f"Duplicate generator_ids: {ids}"


def test_generator_topic_slugs_set(registered):
    for g in registered:
        assert g.topic_slug, f"{g.generator_id} missing topic_slug"
        assert g.display_name, f"{g.generator_id} missing display_name"


# ---------------------------------------------------------------------------

@pytest.mark.parametrize("difficulty", DIFFICULTIES)
def test_each_generator_produces_batch(registered, difficulty):
    """Every generator produces a small verified batch at every difficulty.

    Respects each generator's ``bank_count_per_difficulty`` override so
    small-parameter-space generators (e.g., Pythagorean triples) aren't
    asked for more problems than they can produce. Caps at 10 problems
    to keep the test fast.
    """
    TEST_FLOOR = 5  # must produce at least this many per difficulty
    TEST_CEIL = 10  # but no more than this (keeps tests fast)
    for gen in registered:
        if difficulty not in gen.supports_difficulties:
            continue
        generator_cap = getattr(gen, "bank_count_per_difficulty", None) or TEST_CEIL
        count = max(TEST_FLOOR, min(TEST_CEIL, generator_cap))
        batch = gen.generate_batch(difficulty, count=count, seed=42)
        assert len(batch) == count, f"{gen.generator_id}/{difficulty}: wrong count"
        ids = {p.id for p in batch}
        assert len(ids) == count, f"{gen.generator_id}/{difficulty}: duplicate IDs"
        for p in batch:
            _assert_problem_well_formed(p, gen.generator_id, difficulty)


def _assert_problem_well_formed(p: Problem, gen_id: str, difficulty: str) -> None:
    assert isinstance(p, Problem)
    assert p.generator_id == gen_id
    assert p.difficulty == difficulty
    assert p.statement_latex.strip(), f"{p.id}: empty statement"
    assert p.answer_latex.strip(), f"{p.id}: empty answer"
    assert len(p.hints) >= 2, f"{p.id}: expected >=2 hints"
    assert len(p.solution_steps_latex) >= 2, f"{p.id}: expected >=2 solution steps"
    # Every hint and step should be non-empty.
    for i, h in enumerate(p.hints):
        assert h.strip(), f"{p.id}: hint {i} is empty"
    for i, s in enumerate(p.solution_steps_latex):
        assert s.strip(), f"{p.id}: solution step {i} is empty"
    # Tags should be taxonomy-style (quoted hash tags).
    for t in p.tags:
        assert isinstance(t, str)
        assert t.startswith("#"), f"{p.id}: tag {t!r} missing leading '#'"


# ---------------------------------------------------------------------------

def test_batches_are_reproducible(circle_generators):
    """Identical (difficulty, seed) yields identical problem IDs in identical order."""
    for gen in circle_generators:
        batch_a = gen.generate_batch("medium", count=10, seed=123)
        batch_b = gen.generate_batch("medium", count=10, seed=123)
        assert [p.id for p in batch_a] == [p.id for p in batch_b], (
            f"{gen.generator_id} is not reproducible"
        )


def test_different_seeds_produce_different_ordering(circle_generators):
    """Different seeds should produce different problem sequences.

    (Ordered comparison rather than set equality, since for small-parameter
    generators two seeds may draw the same SET of problems but in different
    order — that still counts as distinct batches for a student.)
    """
    for gen in circle_generators:
        batch_a = gen.generate_batch("medium", count=10, seed=100)
        batch_b = gen.generate_batch("medium", count=10, seed=200)
        ids_a = [p.id for p in batch_a]
        ids_b = [p.id for p in batch_b]
        assert ids_a != ids_b, (
            f"{gen.generator_id}: seeds 100 and 200 produced the same ordered batch"
        )
