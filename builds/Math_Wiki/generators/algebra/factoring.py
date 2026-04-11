"""Factoring generators (Phase 2c Wave 2 + Wave B).

Canonical topic slug ``factoring_trinomials_leading_coefficient_1`` at
wiki/topics/algebra/Factoring_Trinomials_Leading_Coefficient_1.md.

- factor_trinomial_leading_1: factor x^2 + bx + c into (x + p)(x + q)
- factor_difference_of_squares: factor x^2 - k^2 into (x - k)(x + k)
- factor_perfect_square_trinomial: factor x^2 + 2kx + k^2 into (x + k)^2

Wave B additions (topic slug ``factoring_expressions``):

- factor_gcf_binomial_or_trinomial: factor the GCF out of 2- or 3-term
  expressions that are *not* factorable trinomials.
- recognize_and_factor: multi-strategy recognizer (GCF, difference of
  squares, perfect-square trinomial, grouping).
- factor_difference_of_squares_simple: a^2 - b^2 with a and b as small ints.
"""
from __future__ import annotations

import math
import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


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


# ---------------------------------------------------------------------------
# Topic: factoring_expressions (Wave B)
# ---------------------------------------------------------------------------


@register
class FactorGCFBinomialOrTrinomial(Generator):
    """Factor the GCF out of a 2- or 3-term expression (not a trinomial pattern).

    Backward construction: pick the GCF (coefficient + x-power) and a
    "leftover" polynomial with 2 or 3 terms whose coefficients are pairwise
    coprime. Multiply to present the expression.
    """
    generator_id = "factor_gcf_binomial_or_trinomial"
    topic_slug = "factoring_expressions"
    display_name = "Factor out the GCF from 2 or 3 terms"

    _GCF_COEF = {"easy": (2, 5), "medium": (2, 8), "hard": (3, 12)}
    _INNER = {"easy": (1, 7), "medium": (1, 11), "hard": (1, 15)}
    _GCF_XEXP = {"easy": (0, 1), "medium": (1, 2), "hard": (1, 2)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        g_lo, g_hi = self._GCF_COEF[difficulty]
        i_lo, i_hi = self._INNER[difficulty]
        xe_lo, xe_hi = self._GCF_XEXP[difficulty]
        gcf_c = rng.randint(g_lo, g_hi)
        gcf_x_exp = rng.randint(xe_lo, xe_hi)
        n_terms = rng.choice([2, 3])

        # Inner coefficients, pairwise coprime so the GCF we picked is exactly
        # the full GCF (nothing extra slips in).
        while True:
            coefs: list[int] = [
                rng.randint(i_lo, i_hi) * rng.choice([-1, 1])
                for _ in range(n_terms)
            ]
            if all(c != 0 for c in coefs):
                g = abs(coefs[0])
                for c in coefs[1:]:
                    g = math.gcd(g, abs(c))
                if g == 1:
                    break

        # Inner x-exponents: at least one must be 0 so the GCF doesn't pick
        # up extra x powers; pick inner exponents in [0, 2].
        inner_exps: list[int] = []
        zero_assigned = False
        for i in range(n_terms):
            exp = rng.randint(0, 2)
            if i == n_terms - 1 and not zero_assigned:
                exp = 0
            if exp == 0:
                zero_assigned = True
            inner_exps.append(exp)

        # Build the inner polynomial (in x).
        inner_poly = sum(coefs[i] * x ** inner_exps[i] for i in range(n_terms))
        gcf_expr = gcf_c * x ** gcf_x_exp
        expression = sp.expand(gcf_expr * inner_poly)

        gcf_latex = sp.latex(gcf_expr)
        inner_latex = sp.latex(sp.expand(inner_poly))
        expr_latex = sp.latex(expression)
        answer = f"{gcf_latex}\\left({inner_latex}\\right)"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (gcf_c, gcf_x_exp, tuple(coefs), tuple(inner_exps)),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the GCF out of ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                "Start by finding the greatest common factor of all the coefficients.",
                "Then take the lowest power of $x$ that appears in every term.",
                f"The GCF is ${gcf_latex}$. Divide each term by it to find what goes inside the parentheses.",
            ],
            solution_steps_latex=[
                f"Identify the GCF of every term: ${gcf_latex}$.",
                f"Divide each term of ${expr_latex}$ by ${gcf_latex}$, obtaining ${inner_latex}$.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-polynomials",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class RecognizeAndFactor(Generator):
    """Multi-type recognizer: GCF, difference of squares, perfect-square
    trinomial, or grouping. The student must name the technique and apply it.

    A tight finite parameter space, so the bank count is modest.
    """
    generator_id = "recognize_and_factor"
    topic_slug = "factoring_expressions"
    display_name = "Recognize the correct factoring strategy and apply it"
    bank_count_per_difficulty = 25

    _K = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K[difficulty]
        strategy = rng.choice(["gcf", "dos", "pst", "grouping"])

        if strategy == "gcf":
            g = rng.randint(2, k_hi)
            a = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
            b = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
            while math.gcd(abs(a), abs(b)) != 1 or a == 0 or b == 0:
                a = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
                b = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
            expr = sp.expand(g * (a * x + b))
            expr_latex = sp.latex(expr)
            answer = f"{g}({sp.latex(a * x + b)})"
            name = "GCF factoring"
            hints = [
                "Every coefficient shares a factor. Pull out the greatest common factor first.",
                f"The numeric GCF is ${g}$.",
                f"Divide both terms by ${g}$ to get ${sp.latex(a * x + b)}$ inside the parentheses.",
            ]
            steps = [
                f"Look at ${expr_latex}$. Both terms share the factor ${g}$.",
                f"Factor it out: ${answer}$.",
            ]
        elif strategy == "dos":
            k = rng.randint(k_lo, k_hi)
            expr = x * x - k * k
            expr_latex = sp.latex(expr)
            answer = f"(x + {k})(x - {k})"
            name = "difference of squares"
            hints = [
                r"Recognize the shape $A^2 - B^2$: two squares with a minus sign between them.",
                f"Here $A = x$ and $B = {k}$ since $B^2 = {k * k}$.",
                r"Apply $A^2 - B^2 = (A + B)(A - B)$.",
            ]
            steps = [
                f"${expr_latex}$ has the form $A^2 - B^2$ with $A = x$, $B = {k}$.",
                r"$A^2 - B^2 = (A + B)(A - B)$, so the factored form is $(x + "
                f"{k})(x - {k})$.",
            ]
        elif strategy == "pst":
            k = rng.randint(k_lo, k_hi)
            sign = rng.choice([1, -1])
            expr = x * x + sign * 2 * k * x + k * k
            expr_latex = sp.latex(expr)
            if sign > 0:
                answer = f"(x + {k})^2"
                sign_word = "+"
            else:
                answer = f"(x - {k})^2"
                sign_word = "-"
            name = "perfect-square trinomial"
            hints = [
                r"Recognize $A^2 \pm 2AB + B^2 = (A \pm B)^2$.",
                f"Here $A = x$ and $B = {k}$ (since the last term is ${k * k} = {k}^2$).",
                f"Check the middle term: $2({k}) = {2 * k}$, which matches the absolute value of the middle coefficient.",
            ]
            steps = [
                f"${expr_latex}$ is a perfect-square trinomial.",
                f"The square root of the first term is $x$, of the last term is ${k}$; the middle sign is '{sign_word}'.",
                f"Factored form: ${answer}$.",
            ]
        else:  # grouping
            m = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
            b = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
            while m == 0 or b == 0:
                m = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
                b = rng.randint(k_lo, k_hi) * rng.choice([-1, 1])
            expr = sp.expand((x + m) * (x * x + b))
            expr_latex = sp.latex(expr)

            def _lin(val, var):
                if val >= 0:
                    return f"({var} + {val})"
                return f"({var} - {abs(val)})"

            answer = f"{_lin(m, 'x')}{_lin(b, 'x^2')}"
            name = "factoring by grouping"
            hints = [
                "Four terms and no obvious common factor? Try factoring by grouping.",
                "Group the first two and the last two terms and look for a shared binomial.",
                f"You should see $(x + {m})$ appear in both groups.",
            ]
            steps = [
                f"${expr_latex}$ has four terms. Try grouping.",
                f"Group pairs: $(x^3 + {m}x^2) + ({b}x + {m * b})$.",
                f"Factor each pair: $x^2(x + {m}) + {b}(x + {m})$.",
                f"Pull out the common $(x + {m})$: ${answer}$.",
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (strategy, expr_latex),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Factor completely: ${expr_latex}$. "
                f"Name the technique you used."
            ),
            answer_latex=f"${answer}$ (via {name})",
            hints=hints,
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-polynomials",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class FactorDifferenceOfSquaresSimple(Generator):
    """Factor a^2 - b^2 where a and b are small integers (variables).

    Presented as ``A^2 - B^2`` with A = a*x and B = b (so the student works
    with a classic $x^2 - k$ form).  Backward construction keeps everything
    clean.
    """
    generator_id = "factor_difference_of_squares_simple"
    topic_slug = "factoring_expressions"
    display_name = "Factor a^2 - b^2"
    bank_count_per_difficulty = 20

    _A = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _B = {"easy": (2, 10), "medium": (2, 15), "hard": (2, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        b_lo, b_hi = self._B[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        expr = (a * x) ** 2 - b * b
        expr_latex = sp.latex(sp.expand(expr))
        if a == 1:
            answer = f"(x + {b})(x - {b})"
        else:
            answer = f"({a}x + {b})({a}x - {b})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Both terms are perfect squares with a minus sign between them, so this is a difference of squares.",
                r"Pattern: $A^2 - B^2 = (A + B)(A - B)$.",
                f"Here $A = {sp.latex(a * x)}$ and $B = {b}$.",
            ],
            solution_steps_latex=[
                r"Recognize $A^2 - B^2 = (A + B)(A - B)$.",
                f"Identify $A^2 = {sp.latex((a * x) ** 2)}$, so $A = {sp.latex(a * x)}$.",
                f"Identify $B^2 = {b * b}$, so $B = {b}$.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-polynomials",
                "#skill-algebraic-manipulation",
            ],
        )
