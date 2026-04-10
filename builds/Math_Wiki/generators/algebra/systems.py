"""Systems-of-equations generators (Phase 2c Wave 2).

Canonical topic slug ``solving_systems_by_substitution`` at
wiki/topics/algebra/Solving_Systems_By_Substitution.md (Algebra I Ch 5.2).

- systems_substitution_isolated_y: one equation is already y = ...; substitute into the other
- systems_substitution_any: both equations in general form; isolate one variable and substitute
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


# ---------------------------------------------------------------------------

@register
class SystemsSubstitutionIsolatedY(Generator):
    """Solve a system where one equation is already y = mx + b."""
    generator_id = "systems_substitution_isolated_y"
    topic_slug = "solving_systems_by_substitution"
    display_name = "Solve a system by substitution (y isolated)"

    _COEF_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        # Pick the solution first
        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # First equation: y = m*x + b
        m = rng.randint(-coef_hi, coef_hi)
        while m == 0:
            m = rng.randint(-coef_hi, coef_hi)
        b1 = y_val - m * x_val

        # Second equation: a*x + c*y = d with integer coefficients
        a = rng.randint(1, coef_hi)
        c = rng.randint(1, coef_hi)
        if rng.random() < 0.5:
            c = -c
        d = a * x_val + c * y_val

        eq1_latex = sp.latex(sp.Eq(y, m * x + b1))
        eq2_latex = sp.latex(sp.Eq(a * x + c * y, d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b1, a, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by substitution:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                r"The first equation gives $y$ directly. Substitute that expression for $y$ into the second equation.",
                f"Replace $y$ with ${sp.latex(m * x + b1)}$ in the second equation.",
                f"Solve the resulting one-variable equation for $x$, then use $x = {x_val}$ to find $y$.",
            ],
            solution_steps_latex=[
                f"First equation: $y = {sp.latex(m * x + b1)}$.",
                f"Substitute into the second equation: ${a}x + ({c})({sp.latex(m * x + b1)}) = {d}$.",
                f"Simplify and solve: $x = {x_val}$.",
                f"Substitute back: $y = ({m})({x_val}) + ({b1}) = {y_val}$.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )


@register
class SystemsSubstitutionIsolatedX(Generator):
    """Solve a system where one equation is already x = ...; substitute into the other."""
    generator_id = "systems_substitution_isolated_x"
    topic_slug = "solving_systems_by_substitution"
    display_name = "Solve a system by substitution (x isolated)"

    _COEF_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # First equation: x = m*y + b
        m = rng.randint(-coef_hi, coef_hi)
        while m == 0:
            m = rng.randint(-coef_hi, coef_hi)
        b1 = x_val - m * y_val

        a = rng.randint(1, coef_hi)
        c = rng.randint(1, coef_hi)
        if rng.random() < 0.5:
            c = -c
        d = a * x_val + c * y_val

        eq1_latex = sp.latex(sp.Eq(x, m * y + b1))
        eq2_latex = sp.latex(sp.Eq(a * x + c * y, d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b1, a, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by substitution:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                r"The first equation gives $x$ directly. Substitute that expression for $x$ into the second equation.",
                f"Replace $x$ with ${sp.latex(m * y + b1)}$ in the second equation.",
                f"Solve the resulting one-variable equation for $y$, then compute $x$.",
            ],
            solution_steps_latex=[
                f"First equation: $x = {sp.latex(m * y + b1)}$.",
                f"Substitute into the second: $({a})({sp.latex(m * y + b1)}) + ({c})y = {d}$.",
                f"Simplify and solve: $y = {y_val}$.",
                f"Substitute back: $x = ({m})({y_val}) + ({b1}) = {x_val}$.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )
