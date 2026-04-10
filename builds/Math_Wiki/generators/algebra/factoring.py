"""Factoring generators (Phase 2c Wave 2).

Canonical topic slug ``factoring_trinomials_leading_coefficient_1`` at
wiki/topics/algebra/Factoring_Trinomials_Leading_Coefficient_1.md.

- factor_trinomial_leading_1: factor x^2 + bx + c into (x + p)(x + q)
- factor_difference_of_squares: factor x^2 - k^2 into (x - k)(x + k)
- factor_perfect_square_trinomial: factor x^2 + 2kx + k^2 into (x + k)^2
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


# ---------------------------------------------------------------------------

@register
class FactorTrinomialLeading1(Generator):
    """Factor x^2 + bx + c where b, c are chosen so the roots are integers."""
    generator_id = "factor_trinomial_leading_1"
    topic_slug = "factoring_trinomials_leading_coefficient_1"
    display_name = "Factor x^2 + bx + c"

    _RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick two integer roots -p, -q so (x + p)(x + q) = x^2 + (p+q)x + pq
        p = rng.randint(lo, hi)
        q = rng.randint(lo, hi)
        while p == 0 and q == 0:
            p = rng.randint(lo, hi)
            q = rng.randint(lo, hi)
        b = p + q
        c = p * q
        trinomial = x * x + b * x + c
        trin_latex = sp.latex(trinomial)

        # Render the factored form with correct signs
        def factor_term(val):
            if val >= 0:
                return f"(x + {val})"
            return f"(x - {abs(val)})"

        factored = factor_term(p) + factor_term(q)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the trinomial ${trin_latex}$.",
            answer_latex=f"${factored}$",
            hints=[
                r"Look for two numbers $p$ and $q$ such that $p \cdot q = c$ and $p + q = b$.",
                f"Here $b = {b}$ and $c = {c}$, so find two numbers whose product is ${c}$ and whose sum is ${b}$.",
                f"Those two numbers are ${p}$ and ${q}$.",
            ],
            solution_steps_latex=[
                rf"Find two numbers whose product is $c = {c}$ and whose sum is $b = {b}$.",
                f"The two numbers are ${p}$ and ${q}$: $({p}) \\cdot ({q}) = {c}$ and $({p}) + ({q}) = {b}$.",
                f"Write the factored form: ${factored}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class FactorDifferenceOfSquares(Generator):
    """Factor x^2 - k^2 as (x + k)(x - k)."""
    generator_id = "factor_difference_of_squares"
    topic_slug = "factoring_trinomials_leading_coefficient_1"
    display_name = "Factor x^2 - k^2 (difference of squares)"
    bank_count_per_difficulty = 20

    _K_RANGES = {"easy": (2, 12), "medium": (2, 20), "hard": (2, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._K_RANGES[difficulty]
        k = rng.randint(lo, hi)
        expression = x * x - k * k
        expr_latex = sp.latex(expression)
        answer = f"(x + {k})(x - {k})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"This is a **difference of squares**: $a^2 - b^2 = (a + b)(a - b)$.",
                f"Here $a = x$ and $b = {k}$ (because $b^2 = {k * k}$, so $b = {k}$).",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $a^2 - b^2 = (a + b)(a - b)$.",
                f"Identify $a = x$ (since $a^2 = x^2$) and $b = {k}$ (since $b^2 = {k * k}$).",
                f"Write the factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class FactorPerfectSquareTrinomial(Generator):
    """Factor x^2 + 2kx + k^2 as (x + k)^2 (or the - variant)."""
    generator_id = "factor_perfect_square_trinomial"
    topic_slug = "factoring_trinomials_leading_coefficient_1"
    display_name = "Factor a perfect square trinomial"
    bank_count_per_difficulty = 20

    _K_RANGES = {"easy": (1, 10), "medium": (1, 15), "hard": (1, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._K_RANGES[difficulty]
        k = rng.randint(lo, hi)
        # 50/50: (x + k)^2 or (x - k)^2
        if rng.random() < 0.5:
            b = 2 * k
            sign_label = "+"
            answer = f"(x + {k})^2"
        else:
            b = -2 * k
            sign_label = "-"
            answer = f"(x - {k})^2"
        c = k * k
        trinomial = x * x + b * x + c
        trin_latex = sp.latex(trinomial)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the perfect square trinomial ${trin_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"A **perfect square trinomial** has the form $a^2 \pm 2ab + b^2 = (a \pm b)^2$.",
                f"Check that the first term is a perfect square: $x^2$. The last term is ${c}$, and $\\sqrt{{{c}}} = {k}$.",
                f"Check that the middle term equals $2 \\cdot x \\cdot {k} = {2 * k}$ (sign: {sign_label}). It does.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $x^2 \pm 2kx + k^2 = (x \pm k)^2$.",
                f"The last term ${c}$ is a perfect square: $\\sqrt{{{c}}} = {k}$, so $k = {k}$.",
                f"The middle term ${b}x = {sign_label}2({k})x$, which matches the pattern.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )
