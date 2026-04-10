"""Multi-step equation generators (Phase 2c Wave 2).

Canonical topic slug ``multi_step_equations`` at
wiki/topics/algebra/Multi_Step_Equations.md (Algebra I Ch 2.2).

- multi_step_eq_two_step: solve ax + b = c
- multi_step_eq_distribution: solve a(x + b) = c
- multi_step_eq_variables_both_sides: solve ax + b = cx + d
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


# ---------------------------------------------------------------------------

@register
class MultiStepTwoStep(Generator):
    """Solve ax + b = c for clean integer x."""
    generator_id = "multi_step_eq_two_step"
    topic_slug = "multi_step_equations"
    display_name = "Solve ax + b = c"

    _RANGES = {"easy": (2, 10), "medium": (2, 20), "hard": (2, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        x_val = rng.randint(-hi, hi)
        b = rng.randint(-hi, hi)
        c = a * x_val + b  # guarantees clean integer x

        eq_latex = sp.latex(sp.Eq(a * x + b, c))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"First, isolate the $x$ term by moving the constant to the other side.",
                f"Subtract ${b}$ from both sides: ${a}x = {c - b}$.",
                f"Then divide both sides by ${a}$: $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Subtract ${b}$ from both sides: ${a}x = {c} - ({b}) = {c - b}$.",
                f"Divide both sides by ${a}$: $x = \\dfrac{{{c - b}}}{{{a}}} = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class MultiStepDistribution(Generator):
    """Solve a(x + b) = c by distributing then solving."""
    generator_id = "multi_step_eq_distribution"
    topic_slug = "multi_step_equations"
    display_name = "Solve a(x + b) = c"

    _A_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 20)}
    _X_RANGE = {"easy": (-10, 10), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        x_val = rng.randint(x_lo, x_hi)
        b = rng.randint(x_lo, x_hi)
        # a(x + b) = a*x_val + a*b = c when x = x_val
        c = a * (x_val + b)

        eq_latex = sp.latex(sp.Eq(a * (x + b), c))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"First, distribute the ${a}$ across the parentheses.",
                f"You get ${a}x + {a * b} = {c}$.",
                f"Now solve as a two-step equation: $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Distribute: ${a}x + ({a})({b}) = {c}$, which gives ${a}x + {a * b} = {c}$.",
                f"Subtract ${a * b}$ from both sides: ${a}x = {c - a * b}$.",
                f"Divide by ${a}$: $x = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class MultiStepVariablesBothSides(Generator):
    """Solve ax + b = cx + d (variables on both sides)."""
    generator_id = "multi_step_eq_variables_both_sides"
    topic_slug = "multi_step_equations"
    display_name = "Solve ax + b = cx + d"

    _COEF_RANGE = {"easy": (2, 9), "medium": (2, 15), "hard": (2, 25)}
    _CONST_RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        const_lo, const_hi = self._CONST_RANGE[difficulty]
        # Pick a, c different so (a - c) != 0
        while True:
            a = rng.randint(coef_lo, coef_hi)
            c = rng.randint(coef_lo, coef_hi)
            if a != c:
                break
        x_val = rng.randint(const_lo, const_hi)
        b = rng.randint(const_lo, const_hi)
        # d = a*x_val + b - c*x_val
        d = a * x_val + b - c * x_val

        eq_latex = sp.latex(sp.Eq(a * x + b, c * x + d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                r"When $x$ appears on both sides, get all $x$ terms to one side.",
                f"Subtract ${c}x$ from both sides to clear the right side: $({a - c})x + {b} = {d}$.",
                f"Then subtract ${b}$: $({a - c})x = {d - b}$. Divide by $({a - c})$: $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Subtract ${c}x$ from both sides: $({a - c})x + {b} = {d}$.",
                f"Subtract ${b}$ from both sides: $({a - c})x = {d - b}$.",
                f"Divide by $({a - c})$: $x = \\dfrac{{{d - b}}}{{{a - c}}} = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )
