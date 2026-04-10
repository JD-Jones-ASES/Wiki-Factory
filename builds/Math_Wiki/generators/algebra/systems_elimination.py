"""Systems-by-elimination generators (Phase 2c Wave 3).

Canonical topic slug ``solving_systems_by_elimination`` at
wiki/topics/algebra/Solving_Systems_By_Elimination.md (Algebra I Ch 5.3).
Pairs with the substitution generators from Wave 2.

- elimination_direct: coefficients already match; add or subtract to eliminate
- elimination_multiply_one: multiply one equation first
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


def _fmt_eq(a: int, b: int, c: int) -> str:
    """Format ax + by = c with nice signs and 1/-1 handling."""
    return sp.latex(sp.Eq(a * x + b * y, c))


# ---------------------------------------------------------------------------

@register
class EliminationDirect(Generator):
    """Coefficient of one variable matches (possibly with opposite sign) so adding/subtracting eliminates it."""
    generator_id = "elimination_direct"
    topic_slug = "solving_systems_by_elimination"
    display_name = "Solve a system by direct elimination"

    _COEF_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # Choose which variable to eliminate (x or y) and whether by adding or subtracting
        eliminate = rng.choice(["x", "y"])
        same_sign = rng.choice([True, False])  # add if opposite sign, subtract if same

        if eliminate == "x":
            a = rng.randint(1, coef_hi)
            if not same_sign:
                # Second equation uses -a so adding eliminates x
                a1, a2 = a, -a
                operation = "add"
            else:
                a1, a2 = a, a
                operation = "subtract"
            b1 = rng.randint(1, coef_hi)
            while b1 == 0:
                b1 = rng.randint(1, coef_hi)
            if rng.random() < 0.5:
                b1 = -b1
            b2 = rng.randint(1, coef_hi)
            while b2 == 0 or b2 == b1:
                b2 = rng.randint(1, coef_hi)
            if rng.random() < 0.5:
                b2 = -b2
        else:
            b = rng.randint(1, coef_hi)
            if not same_sign:
                b1, b2 = b, -b
                operation = "add"
            else:
                b1, b2 = b, b
                operation = "subtract"
            a1 = rng.randint(1, coef_hi)
            while a1 == 0:
                a1 = rng.randint(1, coef_hi)
            if rng.random() < 0.5:
                a1 = -a1
            a2 = rng.randint(1, coef_hi)
            while a2 == 0 or a2 == a1:
                a2 = rng.randint(1, coef_hi)
            if rng.random() < 0.5:
                a2 = -a2

        c1 = a1 * x_val + b1 * y_val
        c2 = a2 * x_val + b2 * y_val

        eq1 = _fmt_eq(a1, b1, c1)
        eq2 = _fmt_eq(a2, b2, c2)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, b1, c1, a2, b2, c2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by elimination:\n\n"
                f"$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                f"Look at the coefficients of ${eliminate}$ in both equations. They match (possibly with opposite sign), so you can eliminate ${eliminate}$ by {'adding' if operation == 'add' else 'subtracting'} the equations.",
                f"After eliminating ${eliminate}$, you'll have a one-variable equation. Solve it, then substitute back.",
            ],
            solution_steps_latex=[
                f"Equation 1: ${eq1}$.",
                f"Equation 2: ${eq2}$.",
                f"The coefficients of ${eliminate}$ match (possibly up to a sign), so {operation} the equations to eliminate ${eliminate}$.",
                f"Solving the resulting one-variable equation gives the remaining variable, then substitute back.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )


@register
class EliminationMultiplyOne(Generator):
    """Need to multiply one equation by an integer so coefficients match."""
    generator_id = "elimination_multiply_one"
    topic_slug = "solving_systems_by_elimination"
    display_name = "Solve a system by elimination (multiply one equation)"

    _COEF_RANGE = {"easy": (2, 6), "medium": (2, 10), "hard": (2, 14)}
    _VAR_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # Pick small coefficients for equation 1, then make equation 2 a non-multiple
        a1 = rng.randint(2, coef_hi)
        b1 = rng.randint(1, coef_hi)
        if rng.random() < 0.5:
            b1 = -b1
        # Eq 2: multiply eq1's x coefficient by k to give a matching target
        k = rng.randint(2, 4)
        a2 = a1 * k
        # Give eq2 a different y coefficient so it's not a scalar multiple of eq1
        while True:
            b2 = rng.randint(1, coef_hi)
            if rng.random() < 0.5:
                b2 = -b2
            if b2 != b1 * k:
                break

        c1 = a1 * x_val + b1 * y_val
        c2 = a2 * x_val + b2 * y_val

        eq1 = _fmt_eq(a1, b1, c1)
        eq2 = _fmt_eq(a2, b2, c2)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, b1, c1, a2, b2, c2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by elimination. You will need to multiply one of the equations first:\n\n"
                f"$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                f"Multiply the first equation by ${k}$ so that the coefficient of $x$ matches ${a2}$.",
                f"Then subtract the two equations to eliminate $x$, leaving a single-variable equation in $y$.",
                f"Solve for $y$, then substitute back to find $x$.",
            ],
            solution_steps_latex=[
                f"Equation 1: ${eq1}$.",
                f"Equation 2: ${eq2}$.",
                f"Multiply Equation 1 by ${k}$ so that the coefficients of $x$ become equal: ${k} \\cdot ({eq1})$.",
                f"Subtract the modified Equation 1 from Equation 2 to eliminate $x$.",
                f"Solve the resulting one-variable equation, then substitute back.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )
