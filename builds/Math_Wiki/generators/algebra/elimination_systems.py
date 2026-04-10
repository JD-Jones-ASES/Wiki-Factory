"""Systems by elimination generators (Phase 2c Wave 3).

Canonical topic slug ``solving_systems_by_elimination`` at
wiki/topics/algebra/Solving_Systems_By_Elimination.md (Algebra I Ch 5.3).

- elimination_direct: coefficients are already set up to eliminate on add/subtract
- elimination_with_multiplication: must multiply one equation first
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


# ---------------------------------------------------------------------------

@register
class EliminationDirect(Generator):
    """Both equations have matching or opposite y-coefficients (no multiplication needed)."""
    generator_id = "systems_elimination_direct"
    topic_slug = "solving_systems_by_elimination"
    display_name = "Solve by elimination (no scaling needed)"

    _COEF_RANGE = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        # Pick solution first
        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # y-coefficients: equal and opposite so adding eliminates y
        b = rng.randint(coef_lo, coef_hi)

        # Distinct x-coefficients so we actually have a unique solution
        a1 = rng.randint(coef_lo, coef_hi)
        a2 = rng.randint(coef_lo, coef_hi)
        while a2 == a1:
            a2 = rng.randint(coef_lo, coef_hi)

        c1 = a1 * x_val + b * y_val
        c2 = a2 * x_val - b * y_val

        eq1_latex = sp.latex(sp.Eq(a1 * x + b * y, c1))
        eq2_latex = sp.latex(sp.Eq(a2 * x - b * y, c2))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, b, c1, a2, c2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by elimination:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                "The $y$-coefficients are opposites. Add the two equations to eliminate $y$.",
                f"Adding gives $({a1 + a2})x = {c1 + c2}$, so $x = {x_val}$.",
                "Substitute $x$ back into either equation to find $y$.",
            ],
            solution_steps_latex=[
                r"Add the two equations to eliminate $y$:",
                f"$({a1})x + ({b})y + ({a2})x - ({b})y = {c1} + {c2}$",
                f"$({a1 + a2})x = {c1 + c2}$",
                f"$x = {x_val}$.",
                f"Substitute $x = {x_val}$ into the first equation: $({a1})({x_val}) + ({b})y = {c1}$, so $y = {y_val}$.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )


@register
class EliminationWithMultiplication(Generator):
    """One equation must be scaled before adding to eliminate a variable."""
    generator_id = "systems_elimination_with_multiplication"
    topic_slug = "solving_systems_by_elimination"
    display_name = "Solve by elimination (multiply one equation first)"

    _COEF_RANGE = {"easy": (2, 6), "medium": (2, 8), "hard": (2, 12)}
    _VAR_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # First equation: random coefficients.
        a1 = rng.randint(coef_lo, coef_hi)
        b1 = rng.randint(coef_lo, coef_hi)
        c1 = a1 * x_val + b1 * y_val

        # Second equation's y-coefficient must be a small multiple of b1 so scaling works.
        scale = rng.choice([2, 3])
        b2_mag = b1 * scale
        # Make it opposite sign of b1 so scaling + adding eliminates y.
        b2 = -b2_mag
        # Choose a2 independently so the system is not degenerate.
        a2 = rng.randint(coef_lo, coef_hi)
        while a2 * (-b2) == a1 * b1 * -1:  # avoid dependent
            a2 = rng.randint(coef_lo, coef_hi)
        c2 = a2 * x_val + b2 * y_val

        eq1_latex = sp.latex(sp.Eq(a1 * x + b1 * y, c1))
        eq2_latex = sp.latex(sp.Eq(a2 * x + b2 * y, c2))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, b1, c1, a2, b2, c2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by elimination:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                f"To eliminate $y$, multiply the first equation by ${scale}$.",
                f"The new first equation has $y$-coefficient ${b1 * scale}$, which cancels with ${b2}$ in the second.",
                f"Add the scaled first equation to the second, solve for $x$, then find $y$.",
            ],
            solution_steps_latex=[
                f"Multiply the first equation by ${scale}$: ${a1 * scale}x + {b1 * scale}y = {c1 * scale}$.",
                f"Add the new first equation and the original second: $({a1 * scale + a2})x = {c1 * scale + c2}$.",
                f"Solve: $x = {x_val}$.",
                f"Substitute $x = {x_val}$ into the original first equation: $y = {y_val}$.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )
