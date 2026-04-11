"""Irrational numbers and real numbers generators.

Canonical topic slug ``irrational_numbers_and_real_numbers`` at
wiki/topics/pre_algebra/Irrational_Numbers_And_Real_Numbers.md (Math I).

- classify_number_rational_irrational: classify a given number
- locate_irrational_between_integers: find the two integers bracketing $\\sqrt{n}$
- approximate_pi_computation: express a circumference in terms of $\\pi$

The classification generator has a small hand-curated parameter space, so
its ``bank_count_per_difficulty`` is capped at $12$.
"""
from __future__ import annotations

import math as _math
import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

# Hand-curated numbers. Each tuple is (latex, category, description).
# `latex` is raw LaTeX (no surrounding $...$).
_CLASSIFY_NUMBERS: tuple[tuple[str, str, str], ...] = (
    (r"\tfrac{3}{4}", "rational", "a ratio of two integers"),
    (r"\tfrac{7}{2}", "rational", "a ratio of two integers"),
    ("-8", "rational", "an integer (every integer is rational)"),
    ("0", "rational", "zero, which is an integer and so rational"),
    ("0.25", "rational", "a terminating decimal"),
    ("-2.6", "rational", "a terminating decimal"),
    (r"0.\overline{3}", "rational", "a repeating decimal"),
    (r"0.\overline{27}", "rational", "a repeating decimal"),
    (r"\tfrac{22}{7}", "rational", "a ratio of two integers (a common approximation of pi, but itself rational)"),
    (r"\sqrt{9}", "rational", "equals 3, which is rational"),
    (r"\sqrt{16}", "rational", "equals 4, which is rational"),
    (r"\sqrt{0.25}", "rational", "equals 0.5, which is rational"),
    (r"\sqrt{2}", "irrational", "the square root of a non-perfect-square integer"),
    (r"\sqrt{3}", "irrational", "the square root of a non-perfect-square integer"),
    (r"\sqrt{5}", "irrational", "the square root of a non-perfect-square integer"),
    (r"\sqrt{7}", "irrational", "the square root of a non-perfect-square integer"),
    (r"\sqrt{10}", "irrational", "the square root of a non-perfect-square integer"),
    (r"\pi", "irrational", "pi, a famous irrational constant"),
    (r"2\pi", "irrational", "a nonzero rational multiple of an irrational is irrational"),
    (r"\pi + 1", "irrational", "adding a rational to an irrational yields an irrational"),
    (r"\sqrt{2} + 3", "irrational", "adding a rational to an irrational yields an irrational"),
    (r"-\sqrt{11}", "irrational", "the negative of an irrational is irrational"),
)


@register
class ClassifyNumberRationalIrrational(Generator):
    """Classify a given number as rational or irrational.

    The parameter space is the fixed ``_CLASSIFY_NUMBERS`` table, so the
    bank cap is set to a value smaller than the table length.
    """
    generator_id = "classify_number_rational_irrational"
    topic_slug = "irrational_numbers_and_real_numbers"
    display_name = "Classify as rational or irrational"

    bank_count_per_difficulty = 12

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(_CLASSIFY_NUMBERS))
        n_latex, category, description = _CLASSIFY_NUMBERS[idx]

        answer = rf"$\text{{{category}}}$"

        if category == "rational":
            rule_hint = (
                r"A number is rational if it can be written as a ratio of two integers --- that includes every integer, "
                r"every terminating decimal, and every repeating decimal."
            )
        else:
            rule_hint = (
                r"A number is irrational if it cannot be written as a ratio of two integers. Common examples are "
                r"$\pi$ and square roots of non-perfect-square integers."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Classify the number ${n_latex}$ as rational or irrational.",
            answer_latex=answer,
            hints=[
                rule_hint,
                f"Think about what ${n_latex}$ is: {description}.",
                f"Therefore ${n_latex}$ is {category}.",
            ],
            solution_steps_latex=[
                f"Look at the number ${n_latex}$.",
                f"It is {description}.",
                f"So ${n_latex}$ is {category}.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

# Non-square integers in [2, N]. Computed once per difficulty at class load.
def _non_squares(lo: int, hi: int) -> list[int]:
    out = []
    for n in range(lo, hi + 1):
        root = _math.isqrt(n)
        if root * root != n:
            out.append(n)
    return out


@register
class LocateIrrationalBetweenIntegers(Generator):
    """Determine the two consecutive integers between which $\\sqrt{n}$ lies."""
    generator_id = "locate_irrational_between_integers"
    topic_slug = "irrational_numbers_and_real_numbers"
    display_name = "Bracket a square root by consecutive integers"

    _RANGES = {"easy": (2, 50), "medium": (2, 120), "hard": (50, 400)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        candidates = _non_squares(lo, hi)
        n = candidates[rng.randrange(len(candidates))]
        floor = _math.isqrt(n)
        ceil = floor + 1
        floor_sq = floor * floor
        ceil_sq = ceil * ceil

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"$\\sqrt{{{n}}}$ lies between which two consecutive integers?",
            answer_latex=f"${floor}$ and ${ceil}$",
            hints=[
                r"Find the two closest perfect squares on either side of the radicand.",
                f"${floor_sq} < {n} < {ceil_sq}$, so $\\sqrt{{{floor_sq}}} < \\sqrt{{{n}}} < \\sqrt{{{ceil_sq}}}$.",
                f"That is, ${floor} < \\sqrt{{{n}}} < {ceil}$.",
            ],
            solution_steps_latex=[
                f"Look for perfect squares near ${n}$.",
                f"${floor}^2 = {floor_sq}$ and ${ceil}^2 = {ceil_sq}$, so ${floor_sq} < {n} < {ceil_sq}$.",
                f"Taking the square root preserves the inequalities: ${floor} < \\sqrt{{{n}}} < {ceil}$.",
                f"So $\\sqrt{{{n}}}$ lies between ${floor}$ and ${ceil}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class ApproximatePiComputation(Generator):
    """Express the circumference of a circle (given its diameter) in terms of $\\pi$.

    The answer is left in exact form ``{d}\\pi`` units so the student sees
    that $\\pi$ is an irrational constant that stays in the answer.
    """
    generator_id = "approximate_pi_computation"
    topic_slug = "irrational_numbers_and_real_numbers"
    display_name = "Circumference in terms of pi"

    _RANGES = {"easy": (1, 30), "medium": (2, 80), "hard": (5, 200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        d = rng.randint(lo, hi)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (d,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A circle has diameter ${d}$ units. "
                r"Express the circumference in terms of $\pi$."
            ),
            answer_latex=f"${d}\\pi$ units",
            hints=[
                r"The circumference of a circle equals $\pi$ times its diameter: $C = \pi d$.",
                f"Substitute $d = {d}$.",
                r"Since $\pi$ is irrational, leave the answer in the form (number)$\pi$.",
            ],
            solution_steps_latex=[
                r"Write the circumference formula: $C = \pi d$.",
                f"Substitute $d = {d}$: $C = {d}\\pi$.",
                f"The circumference is ${d}\\pi$ units.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-formula-substitution"],
        )
