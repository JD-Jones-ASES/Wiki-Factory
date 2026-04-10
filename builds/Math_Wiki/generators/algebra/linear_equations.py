"""Linear equation generators (Phase 2c Wave 1).

One-step equations of four flavors: addition, subtraction, multiplication,
division. The canonical topic slug ``one_step_equations`` matches the
auto-generated stub at wiki/topics/algebra/One_Step_Equations.md.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


# ---------------------------------------------------------------------------

@register
class SolveOneStepAddition(Generator):
    """Solve x + a = b. Answer: x = b - a."""
    generator_id = "one_step_eq_add"
    topic_slug = "one_step_equations"
    display_name = "Solve x + a = b"

    _RANGES = {"easy": (1, 15), "medium": (1, 40), "hard": (1, 100)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        x_val = rng.randint(-hi, hi)
        b = x_val + a

        equation_latex = sp.latex(sp.Eq(x + a, b))
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${equation_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"To get $x$ alone, undo the $+ {a}$.",
                f"Subtract ${a}$ from both sides.",
                f"$x = {b} - {a} = {x_val}$",
            ],
            solution_steps_latex=[
                f"Start with ${equation_latex}$.",
                f"Subtract ${a}$ from both sides: $x = {b} - {a}$.",
                f"Simplify: $x = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation"],
        )


@register
class SolveOneStepSubtraction(Generator):
    """Solve x - a = b. Answer: x = b + a."""
    generator_id = "one_step_eq_sub"
    topic_slug = "one_step_equations"
    display_name = "Solve x - a = b"

    _RANGES = {"easy": (1, 15), "medium": (1, 40), "hard": (1, 100)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        x_val = rng.randint(-hi, hi)
        b = x_val - a

        equation_latex = sp.latex(sp.Eq(x - a, b))
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${equation_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"To get $x$ alone, undo the $- {a}$.",
                f"Add ${a}$ to both sides.",
                f"$x = {b} + {a} = {x_val}$",
            ],
            solution_steps_latex=[
                f"Start with ${equation_latex}$.",
                f"Add ${a}$ to both sides: $x = {b} + {a}$.",
                f"Simplify: $x = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation"],
        )


@register
class SolveOneStepMultiplication(Generator):
    """Solve ax = b. Answer: x = b/a (kept as clean integer)."""
    generator_id = "one_step_eq_mul"
    topic_slug = "one_step_equations"
    display_name = "Solve a·x = b"

    _RANGES = {"easy": (2, 12), "medium": (2, 25), "hard": (2, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        x_val = rng.randint(-hi, hi)
        b = a * x_val  # ensures x comes out clean

        equation_latex = sp.latex(sp.Eq(a * x, b))
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${equation_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"To get $x$ alone, undo the multiplication by ${a}$.",
                f"Divide both sides by ${a}$.",
                f"$x = \\dfrac{{{b}}}{{{a}}} = {x_val}$",
            ],
            solution_steps_latex=[
                f"Start with ${equation_latex}$.",
                f"Divide both sides by ${a}$: $x = \\dfrac{{{b}}}{{{a}}}$.",
                f"Simplify: $x = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation"],
        )


@register
class SolveOneStepDivision(Generator):
    """Solve x/a = b. Answer: x = a*b."""
    generator_id = "one_step_eq_div"
    topic_slug = "one_step_equations"
    display_name = "Solve x/a = b"

    _RANGES = {"easy": (2, 12), "medium": (2, 20), "hard": (2, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(-hi, hi)
        x_val = a * b

        equation_latex = f"\\dfrac{{x}}{{{a}}} = {b}"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${equation_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"To get $x$ alone, undo the division by ${a}$.",
                f"Multiply both sides by ${a}$.",
                f"$x = {a} \\cdot {b} = {x_val}$",
            ],
            solution_steps_latex=[
                f"Start with ${equation_latex}$.",
                f"Multiply both sides by ${a}$: $x = {a} \\cdot {b}$.",
                f"Simplify: $x = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation"],
        )
