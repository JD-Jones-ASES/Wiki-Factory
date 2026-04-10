"""Base classes and registry for math problem generators.

Every generator subclasses `Generator` and self-registers via `@register`.
Generators produce `Problem` instances with deterministic, seed-driven content
so the build pipeline can reproduce identical banks on identical inputs.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from hashlib import md5
from typing import Literal
import random


Difficulty = Literal["easy", "medium", "hard"]
DIFFICULTIES: tuple[Difficulty, ...] = ("easy", "medium", "hard")


@dataclass
class Problem:
    """A single verified practice problem.

    All text fields may contain LaTeX wrapped in `$...$` (inline) or
    `$$...$$` (display). The frontend uses KaTeX to render them at runtime.
    """
    id: str
    generator_id: str
    topic_slug: str
    difficulty: Difficulty
    statement_latex: str            # Student-facing problem
    answer_latex: str               # Correct answer
    hints: list[str]                # Progressive hints
    solution_steps_latex: list[str] # Step-by-step worked solution
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Return a JSON-serialisable dict form."""
        return asdict(self)


def make_problem_id(generator_id: str, difficulty: Difficulty, params: tuple) -> str:
    """Deterministic problem ID from generator + difficulty + parameter tuple.

    Identical parameters yield identical IDs, so the duplicate check in
    `Generator.generate_batch` works correctly even across different seeds.
    """
    payload = f"{generator_id}|{difficulty}|{params}".encode("utf-8")
    return f"{generator_id}_{difficulty[0]}_{md5(payload).hexdigest()[:10]}"


class Generator(ABC):
    """Abstract base for a problem generator.

    Subclasses must set the class-level metadata and implement `_generate_one`.
    Decorate with `@register` so the build pipeline picks them up.
    """
    generator_id: str = ""
    topic_slug: str = ""
    display_name: str = ""
    supports_difficulties: tuple[Difficulty, ...] = DIFFICULTIES
    supports_word_problems: bool = False

    @abstractmethod
    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        """Produce a single problem using the provided RNG for determinism."""
        ...

    def generate_batch(
        self,
        difficulty: Difficulty,
        count: int,
        seed: int,
    ) -> list[Problem]:
        """Generate `count` unique problems deterministically from `seed`.

        Uses a fresh `random.Random` per attempt so each problem is
        independent but the overall batch is reproducible. Raises if we
        cannot produce enough unique problems within the attempt budget.
        """
        if difficulty not in self.supports_difficulties:
            raise ValueError(
                f"{self.generator_id} does not support difficulty {difficulty!r}"
            )
        problems: list[Problem] = []
        seen_ids: set[str] = set()
        # Prime-multiplier helps spread seeds across the parameter space.
        for i in range(count * 5):
            rng = random.Random(seed * 1_000_003 + i * 9791)
            problem = self._generate_one(difficulty, rng)
            if problem.id in seen_ids:
                continue
            self._verify(problem)
            problems.append(problem)
            seen_ids.add(problem.id)
            if len(problems) == count:
                break
        if len(problems) < count:
            raise RuntimeError(
                f"{self.generator_id}: only produced {len(problems)}/{count} "
                f"unique problems at difficulty {difficulty} in the attempt budget"
            )
        return problems

    def _verify(self, problem: Problem) -> None:
        """Structural sanity-check. Subclasses may override for deeper checks.

        The default asserts required fields are non-empty. Phase 1 relies on
        careful generator authoring; Phase 3 adds SymPy round-trip verification.
        """
        if not problem.statement_latex.strip():
            raise ValueError(f"{problem.id}: empty statement")
        if not problem.answer_latex.strip():
            raise ValueError(f"{problem.id}: empty answer")
        if not problem.hints:
            raise ValueError(f"{problem.id}: no hints provided")
        if not problem.solution_steps_latex:
            raise ValueError(f"{problem.id}: no solution steps provided")


# Module-level registry, populated by @register at import time.
_REGISTRY: dict[str, Generator] = {}


def register(cls: type[Generator]) -> type[Generator]:
    """Decorator: instantiate and register a generator class (idempotent)."""
    instance = cls()
    if not instance.generator_id:
        raise ValueError(f"{cls.__name__} must set a non-empty generator_id")
    if not instance.topic_slug:
        raise ValueError(f"{cls.__name__} must set a non-empty topic_slug")
    if instance.generator_id in _REGISTRY:
        # Idempotent: re-importing a module does not re-register.
        return cls
    _REGISTRY[instance.generator_id] = instance
    return cls


def all_generators() -> list[Generator]:
    """Return every registered generator in insertion order."""
    return list(_REGISTRY.values())


def get_generator(generator_id: str) -> Generator | None:
    """Look up a generator by ID, or None if not registered."""
    return _REGISTRY.get(generator_id)


def _clear_registry_for_tests() -> None:
    """Test hook: empty the registry. NOT for production use."""
    _REGISTRY.clear()
