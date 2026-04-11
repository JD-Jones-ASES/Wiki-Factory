"""Absolute value and opposites generators.

Canonical topic slug ``absolute_value_and_opposites`` at
wiki/topics/pre_algebra/Absolute_Value_And_Opposites.md (Math I).

- abs_value_evaluate: compute |n| for signed integers
- opposite_of_integer: find the additive inverse -n
- abs_value_equation_solve: solve |x| = k (two solutions: +/- k)

All three target the distance-from-zero interpretation of absolute value
and the mirror-image-across-zero interpretation of opposites. The
parameter space on ``abs_value_equation_solve`` at easy difficulty only
has 20 distinct values, so ``bank_count_per_difficulty`` is lowered.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


_TAGS_PROCEDURAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_ALGEBRA = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-algebraic-manipulation",
]


def _fmt_integer(n: int) -> str:
    """Wrap negatives in parentheses for readability inside LaTeX."""
    return f"({n})" if n < 0 else f"{n}"


# ---------------------------------------------------------------------------

@register
class AbsValueEvaluate(Generator):
    """Evaluate $|n|$ for a signed integer $n$.

    Distinct from the ``absolute_value`` generator in ``integers_ext.py``:
    that one lives under ``integers_and_the_number_line``; this one targets
    the dedicated ``absolute_value_and_opposites`` topic with different
    ranges and wording.
    """
    generator_id = "abs_value_evaluate"
    topic_slug = "absolute_value_and_opposites"
    display_name = "Evaluate an absolute value expression"

    # Maximum absolute value per difficulty (n is assembled as sign*magnitude).
    _MAX = {"easy": 20, "medium": 100, "hard": 500}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        max_abs = self._MAX[difficulty]
        magnitude = rng.randint(1, max_abs)
        sign = rng.choice([-1, 1])
        n = sign * magnitude
        result = magnitude

        if n > 0:
            direction = "right"
            distance_note = f"${n}$ is already ${n}$ units to the right of zero."
        else:
            direction = "left"
            distance_note = (
                f"${_fmt_integer(n)}$ is ${result}$ units to the left of zero, "
                f"so its distance from zero is ${result}$."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute $|{_fmt_integer(n)}|$.",
            answer_latex=f"${result}$",
            hints=[
                "Absolute value strips any negative sign --- you are measuring how far from zero the number sits.",
                f"${_fmt_integer(n)}$ lies ${result}$ units to the {direction} of $0$ on the number line.",
                f"Since $|{_fmt_integer(n)}| = {result}$, the answer is $\\boxed{{{result}}}$.",
            ],
            solution_steps_latex=[
                f"Identify the value inside the bars: ${_fmt_integer(n)}$.",
                distance_note,
                f"Therefore $|{_fmt_integer(n)}| = {result}$.",
            ],
            tags=_TAGS_PROCEDURAL,
        )


# ---------------------------------------------------------------------------

@register
class OppositeOfInteger(Generator):
    """Give the opposite (additive inverse) of a signed integer.

    Output format is a plain signed integer. For $n = -5$ the answer is
    $5$; for $n = 7$ the answer is $-7$.
    """
    generator_id = "opposite_of_integer"
    topic_slug = "absolute_value_and_opposites"
    display_name = "Find the opposite of an integer"

    _MAX = {"easy": 50, "medium": 200, "hard": 999}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        max_abs = self._MAX[difficulty]
        magnitude = rng.randint(1, max_abs)
        sign = rng.choice([-1, 1])
        n = sign * magnitude
        opposite = -n

        if n > 0:
            mirror_line = (
                f"On the number line, ${n}$ sits ${n}$ units to the right of $0$, "
                f"so its mirror image is ${abs(opposite)}$ units to the left: "
                f"${opposite}$."
            )
        else:
            mirror_line = (
                f"On the number line, ${_fmt_integer(n)}$ sits ${abs(n)}$ units to the left of $0$, "
                f"so its mirror image is ${opposite}$ units to the right: "
                f"${opposite}$."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Give the opposite of ${_fmt_integer(n)}$.",
            answer_latex=f"${opposite}$",
            hints=[
                "The opposite of a number is its mirror image across zero --- same distance, other side.",
                "Flip the sign: change positive to negative or negative to positive.",
                f"The opposite of ${_fmt_integer(n)}$ is ${opposite}$.",
            ],
            solution_steps_latex=[
                f"Start with ${_fmt_integer(n)}$.",
                mirror_line,
                f"Therefore the opposite is ${opposite}$.",
            ],
            tags=_TAGS_ALGEBRA,
        )


# ---------------------------------------------------------------------------

@register
class AbsValueEquationSolve(Generator):
    """Solve $|x| = k$ for $k > 0$ (two real solutions)."""
    generator_id = "abs_value_equation_solve"
    topic_slug = "absolute_value_and_opposites"
    display_name = "Solve |x| = k"

    _RANGES = {"easy": (1, 40), "medium": (41, 200), "hard": (201, 800)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        k = rng.randint(lo, hi)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find all real $x$ for which $|x| = {k}$.",
            answer_latex=f"$x = \\pm {k}$",
            hints=[
                f"$|x| = {k}$ has two solutions: one positive and one negative, both at distance ${k}$ from $0$.",
                f"Write both solutions: $x = {k}$ or $x = -{k}$.",
                "Any value whose distance from zero is the given number works --- do not forget the negative.",
            ],
            solution_steps_latex=[
                f"The equation $|x| = {k}$ asks for every number whose distance from $0$ is ${k}$.",
                f"Two numbers have that distance: ${k}$ and $-{k}$.",
                f"Therefore $x = {k}$ or $x = -{k}$, written compactly as $x = \\pm {k}$.",
            ],
            tags=_TAGS_ALGEBRA,
        )
