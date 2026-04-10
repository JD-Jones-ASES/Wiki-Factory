#!/usr/bin/env python3
"""Build the problem bank JSON from the generator registry.

Run from builds/Math_Wiki/ :

    py -3 tools/build_problem_bank.py

Produces two files under wiki/_data/ :

    problems.json                # full verified bank
    problem_types_index.json     # fast topic -> generator lookup

Both are committed to git. The deployed site fetches problems.json at
runtime when the ProblemVaultWidget loads.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Make the builds/Math_Wiki root importable so `from generators import ...` works
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from generators import all_generators  # noqa: E402


DEFAULT_COUNT_PER_DIFFICULTY = 100
DEFAULT_SEED = 42

# Fallback cascade: if a generator's parameter space cannot support
# `count_per_difficulty` unique problems, try progressively smaller batches.
FALLBACK_COUNTS = (75, 50, 30, 20, 15, 10)


def build_bank(count_per_difficulty: int, seed: int) -> dict:
    """Iterate every registered generator and produce a verified problem bank.

    Each generator is asked for `count_per_difficulty` problems at each
    difficulty it supports. If the parameter space cannot produce that many
    unique problems, the loop retries with progressively smaller counts
    until it finds one that works (down to FALLBACK_COUNTS[-1]).
    """
    gens = all_generators()
    if not gens:
        raise RuntimeError(
            "No generators are registered. Did `generators/__init__.py` import the submodules?"
        )

    bank: dict = {
        "version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "seed_base": seed,
        "requested_count_per_difficulty": count_per_difficulty,
        "generator_count": len(gens),
        "total_problems": 0,
        "problem_types": {},
    }

    total = 0
    for gen in gens:
        entry: dict = {
            "topic_slug": gen.topic_slug,
            "generator_id": gen.generator_id,
            "display_name": gen.display_name,
            "supports_word_problems": gen.supports_word_problems,
            "problems": {},
        }

        for difficulty in gen.supports_difficulties:
            batch = _try_generate(gen, difficulty, count_per_difficulty, seed)
            if batch is None:
                print(
                    f"  SKIP  {gen.generator_id}/{difficulty}: "
                    f"parameter space too small for any tested batch size",
                    file=sys.stderr,
                )
                continue
            entry["problems"][difficulty] = [p.to_dict() for p in batch]
            total += len(batch)
            print(f"  OK    {gen.generator_id}/{difficulty}: {len(batch)} problems")

        bank["problem_types"][gen.generator_id] = entry

    bank["total_problems"] = total
    return bank


def _try_generate(gen, difficulty, requested, seed):
    """Try the requested count, then progressively smaller counts on failure."""
    attempts = [requested, *FALLBACK_COUNTS]
    last_error: Exception | None = None
    for count in attempts:
        if count > requested:
            continue
        try:
            return gen.generate_batch(difficulty, count=count, seed=seed)
        except RuntimeError as e:
            last_error = e
            continue
    if last_error:
        print(f"    last error: {last_error}", file=sys.stderr)
    return None


def build_index(bank: dict) -> dict:
    """Build a small lookup table the widget uses to pick generators by topic."""
    index: dict = {
        "version": "1.0",
        "generated_at": bank["generated_at"],
        "by_topic": {},
        "by_generator": {},
    }
    for gen_id, entry in bank["problem_types"].items():
        topic = entry["topic_slug"]
        index["by_topic"].setdefault(topic, []).append(
            {
                "generator_id": gen_id,
                "display_name": entry["display_name"],
                "supports_difficulties": list(entry["problems"].keys()),
                "counts": {d: len(probs) for d, probs in entry["problems"].items()},
                "supports_word_problems": entry["supports_word_problems"],
            }
        )
        index["by_generator"][gen_id] = {
            "topic_slug": topic,
            "display_name": entry["display_name"],
        }
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--count",
        type=int,
        default=DEFAULT_COUNT_PER_DIFFICULTY,
        help=f"problems per difficulty per generator (default: {DEFAULT_COUNT_PER_DIFFICULTY})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"base seed for reproducibility (default: {DEFAULT_SEED})",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "wiki" / "_data",
        help="output directory for bank JSON files",
    )
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Building problem bank (count={args.count}, seed={args.seed})")
    bank = build_bank(args.count, args.seed)
    index = build_index(bank)

    bank_path = args.out_dir / "problems.json"
    index_path = args.out_dir / "problem_types_index.json"

    bank_path.write_text(json.dumps(bank, indent=2), encoding="utf-8")
    index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")

    bank_kb = bank_path.stat().st_size / 1024
    index_kb = index_path.stat().st_size / 1024
    print()
    print(f"Wrote {bank_path.relative_to(ROOT)} ({bank_kb:.1f} KB)")
    print(f"Wrote {index_path.relative_to(ROOT)} ({index_kb:.1f} KB)")
    print(f"Total problems: {bank['total_problems']}")
    print(f"Generator count: {bank['generator_count']}")


if __name__ == "__main__":
    main()
