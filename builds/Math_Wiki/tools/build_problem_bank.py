#!/usr/bin/env python3
"""Build the problem bank JSON shards from the generator registry.

Writes TWO kinds of files under ``wiki/_data/``:

    problem_types_index.json             --- small lookup table, one entry per
                                             generator. Fetched by the widget on
                                             every topic page.

    problems/{topic_slug}.json           --- one file per topic. Contains every
                                             generator's batch for that topic,
                                             structured as
                                             {generator_id: {difficulty: [...]}}
                                             Fetched lazily on first click.

Size budget: each per-topic shard should stay under ~500 KB. Achieved by
defaulting generators to 30 problems per difficulty and letting each
generator override via its ``bank_count_per_difficulty`` class attribute.

Run from ``builds/Math_Wiki/``:

    py -3 tools/build_problem_bank.py
    py -3 tools/build_problem_bank.py --count 50  # override default
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from generators import all_generators  # noqa: E402


DEFAULT_COUNT_PER_DIFFICULTY = 30
DEFAULT_SEED = 42

# Fallback cascade for generators whose parameter space cannot produce the
# requested batch size.
FALLBACK_COUNTS = (25, 20, 15, 10, 8)


def effective_count(gen, requested: int) -> int:
    """Per-generator override respected via bank_count_per_difficulty attribute."""
    override = getattr(gen, "bank_count_per_difficulty", None)
    if override is None:
        return requested
    return min(requested, int(override))


def try_generate(gen, difficulty: str, requested: int, seed: int) -> list | None:
    """Try the requested count, then smaller counts on failure. Returns None if all fail."""
    attempts = [requested, *FALLBACK_COUNTS]
    last_error: Exception | None = None
    seen = set()
    uniq_attempts = [c for c in attempts if c not in seen and not seen.add(c)]
    for count in uniq_attempts:
        if count > requested:
            continue
        try:
            return gen.generate_batch(difficulty, count=count, seed=seed)
        except RuntimeError as e:
            last_error = e
    if last_error:
        print(f"    last error: {last_error}", file=sys.stderr)
    return None


def build_topic_shards(count_per_difficulty: int, seed: int) -> tuple[dict, dict]:
    """Generate problems for every registered generator and group by topic.

    Returns (topic_shards, index) where:
      topic_shards: {topic_slug: {"generators": {generator_id: {difficulty: [...]}}}}
      index:        compact metadata for the widget (no problem content)
    """
    gens = all_generators()
    if not gens:
        raise RuntimeError(
            "No generators are registered. Ensure generators/__init__.py imports all submodules."
        )

    topic_shards: dict[str, dict] = defaultdict(lambda: {"generators": {}})
    index_generators: list[dict] = []

    for gen in gens:
        gen_id = gen.generator_id
        topic = gen.topic_slug
        requested = effective_count(gen, count_per_difficulty)

        gen_entry: dict = {
            "topic_slug": topic,
            "display_name": gen.display_name,
            "supports_word_problems": gen.supports_word_problems,
            "difficulties": {},
        }

        difficulty_counts: dict[str, int] = {}

        for difficulty in gen.supports_difficulties:
            batch = try_generate(gen, difficulty, requested, seed)
            if batch is None:
                print(
                    f"  SKIP  {gen_id}/{difficulty}: parameter space too small",
                    file=sys.stderr,
                )
                continue
            gen_entry["difficulties"][difficulty] = [p.to_dict() for p in batch]
            difficulty_counts[difficulty] = len(batch)
            print(f"  OK    {gen_id}/{difficulty}: {len(batch)} problems")

        topic_shards[topic]["generators"][gen_id] = gen_entry
        index_generators.append(
            {
                "generator_id": gen_id,
                "topic_slug": topic,
                "display_name": gen.display_name,
                "supports_word_problems": gen.supports_word_problems,
                "counts": difficulty_counts,
                "shard_file": f"problems/{topic}.json",
            }
        )

    # Build final index: topic -> list of generator entries
    index = {
        "version": "2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "seed_base": seed,
        "default_count_per_difficulty": count_per_difficulty,
        "generator_count": len(gens),
        "by_topic": defaultdict(list),
        "by_generator": {},
    }
    for entry in index_generators:
        index["by_topic"][entry["topic_slug"]].append(
            {
                "generator_id": entry["generator_id"],
                "display_name": entry["display_name"],
                "supports_word_problems": entry["supports_word_problems"],
                "counts": entry["counts"],
            }
        )
        index["by_generator"][entry["generator_id"]] = {
            "topic_slug": entry["topic_slug"],
            "display_name": entry["display_name"],
            "counts": entry["counts"],
            "shard_file": entry["shard_file"],
        }
    # defaultdict -> plain dict for JSON
    index["by_topic"] = dict(index["by_topic"])

    return dict(topic_shards), index


def write_outputs(topic_shards: dict, index: dict, out_dir: Path) -> tuple[int, int]:
    """Write per-topic shards and the index file. Returns (total_problems, total_bytes)."""
    # Clean any old single-file bank (Phase 1 artifact)
    legacy_bank = out_dir / "problems.json"
    if legacy_bank.exists():
        legacy_bank.unlink()
        print(f"  removed legacy {legacy_bank.name}")

    problems_dir = out_dir / "problems"
    problems_dir.mkdir(parents=True, exist_ok=True)

    # Remove any stale topic shards so stale files don't linger
    for old in problems_dir.glob("*.json"):
        old.unlink()

    total_problems = 0
    total_bytes = 0

    for topic_slug, shard in topic_shards.items():
        out_file = problems_dir / f"{topic_slug}.json"
        # Compact JSON: no indent => significantly smaller files.
        # Preserve Unicode characters for LaTeX readability.
        payload = {
            "version": "2.0",
            "topic_slug": topic_slug,
            "generated_at": index["generated_at"],
            "generators": shard["generators"],
        }
        out_file.write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
        size_kb = out_file.stat().st_size / 1024
        total_bytes += out_file.stat().st_size
        topic_problem_count = sum(
            len(d) for gen in shard["generators"].values() for d in gen["difficulties"].values()
        )
        total_problems += topic_problem_count
        if size_kb > 500:
            print(
                f"  WARN  {out_file.name}: {size_kb:.1f} KB exceeds 500 KB budget",
                file=sys.stderr,
            )
        print(f"  wrote problems/{topic_slug}.json ({size_kb:.1f} KB, {topic_problem_count} problems)")

    # Index file (pretty-printed for human debugging; it is tiny)
    index_file = out_dir / "problem_types_index.json"
    index_file.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    index_kb = index_file.stat().st_size / 1024
    print(f"  wrote {index_file.name} ({index_kb:.1f} KB)")

    return total_problems, total_bytes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--count", type=int, default=DEFAULT_COUNT_PER_DIFFICULTY,
        help=f"problems per difficulty (default {DEFAULT_COUNT_PER_DIFFICULTY})",
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="base seed")
    parser.add_argument(
        "--out-dir", type=Path, default=ROOT / "wiki" / "_data",
        help="output directory",
    )
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Building sharded problem bank (count={args.count}, seed={args.seed})")

    topic_shards, index = build_topic_shards(args.count, args.seed)
    total_problems, total_bytes = write_outputs(topic_shards, index, args.out_dir)

    print()
    print(f"Total topics: {len(topic_shards)}")
    print(f"Total generators: {index['generator_count']}")
    print(f"Total problems: {total_problems}")
    print(f"Total bank size: {total_bytes / 1024:.1f} KB")


if __name__ == "__main__":
    main()
