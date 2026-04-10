"""Quadratic formula generators (Phase 2c Wave 1).

Canonical topic slug ``the_quadratic_formula`` at
wiki/topics/algebra/The_Quadratic_Formula.md.

- quadratic_formula_integer_roots: integer a, b, c designed so the two roots
  are integers. Student practices the mechanical application.
- quadratic_formula_real_roots: a, b, c produce real irrational roots. Answer
  is left in simplified radical form.
- quadratic_discriminant: compute b^2 - 4ac and classify the roots as
  "two real", "one real (double)", or "no real (complex)".
"""
from __future__ import annotations

import math
import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


def _format_quadratic(a: int, b: int, c: int) -> str:
    """Return LaTeX for ax^2 + bx + c = 0 with nice signs."""
    poly = a * x**2 + b * x + c
    return sp.latex(sp.Eq(poly, 0))


# ---------------------------------------------------------------------------

@register
class QuadraticFormulaIntegerRoots(Generator):
    """Solve ax^2 + bx + c = 0 where both roots are integers."""
    generator_id = "quadratic_formula_integer_roots"
    topic_slug = "the_quadratic_formula"
    display_name = "Solve ax^2 + bx + c = 0 (integer roots)"

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _A_VALUES = {"easy": (1, 1), "medium": (1, 3), "hard": (1, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a_lo, a_hi = self._A_VALUES[difficulty]
        a = rng.randint(a_lo, a_hi)
        # Pick two integer roots
        r1 = rng.randint(lo, hi)
        r2 = rng.randint(lo, hi)
        while r2 == r1:
            r2 = rng.randint(lo, hi)
        # Expand a(x - r1)(x - r2) = a*x^2 - a*(r1+r2)*x + a*r1*r2
        b = -a * (r1 + r2)
        c = a * r1 * r2

        eq_latex = _format_quadratic(a, b, c)
        # Present the roots in order
        roots = sorted([r1, r2])
        discriminant = b * b - 4 * a * c
        sqrt_disc = int(round(math.sqrt(discriminant)))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ using the quadratic formula.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"The quadratic formula is $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.",
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Compute the discriminant: $b^2 - 4ac = ({b})^2 - 4({a})({c}) = {discriminant}$.",
                f"$\\sqrt{{{discriminant}}} = {sqrt_disc}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$, so $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Discriminant: $b^2 - 4ac = ({b})^2 - 4({a})({c}) = {b * b} - {4 * a * c} = {discriminant}$.",
                f"Apply the formula: $x = \\dfrac{{-({b}) \\pm \\sqrt{{{discriminant}}}}}{{2({a})}} = \\dfrac{{{-b} \\pm {sqrt_disc}}}{{{2 * a}}}$.",
                f"The two solutions are $x = {roots[0]}$ and $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-formula-substitution"],
        )


@register
class QuadraticDiscriminant(Generator):
    """Compute b^2 - 4ac and classify the roots."""
    generator_id = "quadratic_discriminant"
    topic_slug = "the_quadratic_formula"
    display_name = "Compute the discriminant and classify roots"

    _RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _A_VALUES = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a_lo, a_hi = self._A_VALUES[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        discriminant = b * b - 4 * a * c
        if discriminant > 0:
            classification = "two real solutions (the parabola crosses the x-axis twice)"
        elif discriminant == 0:
            classification = "one real solution (the parabola touches the x-axis once)"
        else:
            classification = "no real solutions (the parabola does not touch the x-axis)"

        eq_latex = _format_quadratic(a, b, c)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Compute the discriminant of ${eq_latex}$ and state how many "
                "real solutions the equation has."
            ),
            answer_latex=f"Discriminant $= {discriminant}$. {classification}.",
            hints=[
                r"The discriminant is $\Delta = b^2 - 4ac$.",
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                "If $\\Delta > 0$: two real roots. If $\\Delta = 0$: one real (double) root. If $\\Delta < 0$: no real roots.",
            ],
            solution_steps_latex=[
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Compute $\\Delta = b^2 - 4ac = ({b})^2 - 4({a})({c}) = {b * b} - {4 * a * c} = {discriminant}$.",
                f"Because $\\Delta = {discriminant}$, the equation has {classification}.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-procedural-calculation"],
        )


@register
class QuadraticFormulaReducedRadical(Generator):
    """Solve ax^2 + bx + c = 0 where the discriminant is a positive non-square."""
    generator_id = "quadratic_formula_radical_roots"
    topic_slug = "the_quadratic_formula"
    display_name = "Solve using the quadratic formula (radical answers)"
    bank_count_per_difficulty = 25  # modest count keeps generation fast

    # Allowed non-square positive discriminants we're willing to ship as answers.
    _ALLOWED_DISCS = {
        "easy": {5, 8, 12, 13, 17, 20, 21, 24},
        "medium": {5, 8, 12, 13, 17, 20, 21, 24, 28, 29, 32, 33, 37, 40, 41, 44, 45, 48, 52, 53},
        "hard": {
            8, 12, 13, 17, 20, 24, 28, 29, 32, 40, 44, 48, 52, 53, 56, 60, 61,
            65, 68, 72, 76, 80, 84, 88, 92, 96, 97,
        },
    }

    _A_CHOICES = [1, 1, 1, 2]  # bias toward a=1 for readability
    _B_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-14, 14)}
    _C_RANGE = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        allowed = self._ALLOWED_DISCS[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]

        a = b = c = disc = None
        # Forward construction: pick a, b, c, compute disc, accept if in allowed set.
        for _ in range(500):
            a_try = rng.choice(self._A_CHOICES)
            b_try = rng.randint(b_lo, b_hi)
            c_try = rng.randint(c_lo, c_hi)
            if c_try == 0:
                continue
            disc_try = b_try * b_try - 4 * a_try * c_try
            if disc_try in allowed:
                a, b, c, disc = a_try, b_try, c_try, disc_try
                break
        if a is None:
            # Bounded fallback: known-good problem
            a, b, c = 1, 3, 1
            disc = b * b - 4 * a * c

        eq_latex = _format_quadratic(a, b, c)
        # Sympy gives us the exact roots
        poly = a * x * x + b * x + c
        roots_expr = sp.solve(sp.Eq(poly, 0), x)
        roots_latex = ",\\ ".join(f"x = {sp.latex(r)}" for r in roots_expr)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve ${eq_latex}$ using the quadratic formula. "
                "Leave your answer in exact radical form."
            ),
            answer_latex=f"${roots_latex}$",
            hints=[
                r"Use $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.",
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Discriminant: $b^2 - 4ac = {disc}$, which is not a perfect square --- the answer will contain $\\sqrt{{{disc}}}$.",
            ],
            solution_steps_latex=[
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Compute the discriminant: $b^2 - 4ac = ({b})^2 - 4({a})({c}) = {disc}$.",
                f"Apply the formula: $x = \\dfrac{{-({b}) \\pm \\sqrt{{{disc}}}}}{{2({a})}}$.",
                f"Simplify: ${roots_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-formula-substitution"],
        )
