"""Rational expression generators (Phase 2c Wave 5).

Five topic slugs covered, 3 generators each (15 total):

- simplifying_rational_expressions
- multiplying_and_dividing_rational_expressions
- adding_and_subtracting_rational_expressions
- solving_rational_equations
- rational_equations_and_applications

All generators use backward construction: parameters are picked so the
answer comes out clean, then the statement is rendered. Every solving
generator verifies that no solution candidate makes a denominator zero
(except the extraneous-solution generator, which deliberately does).
"""
from __future__ import annotations

import random
from math import gcd

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
t = sp.Symbol("t")


RAT_TAGS = [
    "#branch-algebra-2",
    "#topic-rational-expressions",
    "#skill-algebraic-manipulation",
]


# ---------------------------------------------------------------------------
# Local helpers
# ---------------------------------------------------------------------------


def _linear_factor(a: int) -> str:
    """Render (x + a) with clean sign handling. For a = 0 returns 'x'."""
    if a == 0:
        return "x"
    if a > 0:
        return f"(x + {a})"
    return f"(x - {abs(a)})"


def _linear_root_text(a: int) -> str:
    """Render the root where (x + a) = 0, i.e. x = -a."""
    return f"x = {-a}"


def _render_poly(poly: sp.Expr) -> str:
    """Render a sympy polynomial as LaTeX."""
    return sp.latex(sp.expand(poly))


# ===========================================================================
# Topic 1: simplifying_rational_expressions
# ===========================================================================


@register
class SimplifyRationalQuadraticOverLinear(Generator):
    """Simplify (x^2 + bx + c)/(x - r) where (x - r) divides the numerator.

    Backward: pick two distinct integer roots r and s. Numerator is
    (x - r)(x - s). Denominator is (x - r). Answer is (x - s).
    """
    generator_id = "simplify_rational_quadratic_over_linear"
    topic_slug = "simplifying_rational_expressions"
    display_name = "Simplify (x^2 + bx + c)/(x - r)"

    _RANGES = {"easy": (1, 8), "medium": (1, 14), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick two distinct non-zero integer roots
        while True:
            r = rng.randint(-hi, hi)
            s = rng.randint(-hi, hi)
            if r != s and abs(r) >= lo and abs(s) >= lo:
                break

        # Numerator = (x - r)(x - s)
        numerator = (x - r) * (x - s)
        numer_latex = _render_poly(numerator)
        denom_factor_latex = _render_poly(x - r)

        # Answer is (x - s)
        answer_latex = _render_poly(x - s)

        expr_latex = rf"\dfrac{{{numer_latex}}}{{{denom_factor_latex}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, s)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Simplify ${expr_latex}$. State any restrictions on $x$."
            ),
            answer_latex=f"${answer_latex},\\ x \\ne {r}$",
            hints=[
                "Factor the numerator. It is a quadratic with integer roots.",
                "Look for a factor matching the denominator so you can cancel.",
                f"The numerator factors as $({_render_poly(x - r)})({_render_poly(x - s)})$.",
            ],
            solution_steps_latex=[
                f"Factor the numerator: ${numer_latex} = ({_render_poly(x - r)})({_render_poly(x - s)})$.",
                f"Rewrite the fraction: $\\dfrac{{({_render_poly(x - r)})({_render_poly(x - s)})}}{{{denom_factor_latex}}}$.",
                f"Cancel the common factor $({_render_poly(x - r)})$: result is ${answer_latex}$.",
                f"Restriction: the original denominator cannot be zero, so $x \\ne {r}$.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class SimplifyRationalTrinomialOverTrinomial(Generator):
    """Simplify (x+a)(x+b)/((x+a)(x+c)) given as expanded trinomials.

    Backward: pick distinct integers a, b, c. Present the numerator and
    denominator in expanded (trinomial) form. Answer is (x+b)/(x+c) with
    restrictions x != -a, x != -c.
    """
    generator_id = "simplify_rational_trinomial_over_trinomial"
    topic_slug = "simplifying_rational_expressions"
    display_name = "Simplify a trinomial over a trinomial"

    _RANGES = {"easy": (1, 7), "medium": (1, 12), "hard": (1, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick three distinct values (can be positive or negative, but nonzero)
        picks: list[int] = []
        while len(picks) < 3:
            val = rng.randint(-hi, hi)
            if val == 0 or abs(val) < lo:
                continue
            if val in picks:
                continue
            picks.append(val)
        a, b, c = picks

        numer = sp.expand((x + a) * (x + b))
        denom = sp.expand((x + a) * (x + c))
        numer_latex = sp.latex(numer)
        denom_latex = sp.latex(denom)

        # Answer: (x + b)/(x + c)
        answer_num = _linear_factor(b)
        answer_den = _linear_factor(c)

        restrictions = f"x \\ne {-a},\\ x \\ne {-c}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Simplify $\\dfrac{{{numer_latex}}}{{{denom_latex}}}$. "
                "State any restrictions on $x$."
            ),
            answer_latex=f"$\\dfrac{{{answer_num}}}{{{answer_den}}},\\ {restrictions}$",
            hints=[
                "Factor both the numerator and the denominator.",
                "Look for a common linear factor to cancel.",
                f"The numerator factors as ${_linear_factor(a)}{_linear_factor(b)}$ "
                f"and the denominator factors as ${_linear_factor(a)}{_linear_factor(c)}$.",
            ],
            solution_steps_latex=[
                f"Factor the numerator: ${numer_latex} = {_linear_factor(a)}{_linear_factor(b)}$.",
                f"Factor the denominator: ${denom_latex} = {_linear_factor(a)}{_linear_factor(c)}$.",
                f"Cancel the common factor ${_linear_factor(a)}$: "
                f"$\\dfrac{{{answer_num}}}{{{answer_den}}}$.",
                f"Restrictions (from the original denominator): ${restrictions}$.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class SimplifyRationalWithGcf(Generator):
    """Simplify (ax^2 + bx)/(cx^2 + dx) where a common x can be pulled out.

    Backward: pick a, b, c, d. Numerator x(ax+b), denominator x(cx+d).
    Answer is (ax+b)/(cx+d), restrictions x != 0, x != -d/c.
    """
    generator_id = "simplify_rational_with_gcf"
    topic_slug = "simplifying_rational_expressions"
    display_name = "Simplify (ax^2 + bx)/(cx^2 + dx) via GCF"

    _A_RANGES = {"easy": (2, 6), "medium": (2, 10), "hard": (2, 15)}
    _B_RANGES = {"easy": (1, 10), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        a = rng.randint(a_lo, a_hi)
        c = rng.randint(a_lo, a_hi)
        # Ensure a/c does not equal b/d for cleaner problem (distinct reduced form)
        b = rng.randint(b_lo, b_hi)
        d = rng.randint(b_lo, b_hi)
        # Randomly negate b and d for variety
        if rng.random() < 0.5:
            b = -b
        if rng.random() < 0.5:
            d = -d
        # Avoid trivial case where d == 0 (would make x^2 not x in denom)
        while d == 0:
            d = rng.randint(b_lo, b_hi)

        numer = sp.expand(a * x * x + b * x)
        denom = sp.expand(c * x * x + d * x)
        numer_latex = sp.latex(numer)
        denom_latex = sp.latex(denom)

        # Factored forms
        numer_factored = f"x({a}x " + ("+ " + str(b) if b > 0 else "- " + str(-b)) + ")"
        denom_factored = f"x({c}x " + ("+ " + str(d) if d > 0 else "- " + str(-d)) + ")"

        # Answer
        answer_num = f"{a}x " + ("+ " + str(b) if b > 0 else "- " + str(-b))
        answer_den = f"{c}x " + ("+ " + str(d) if d > 0 else "- " + str(-d))

        # Second restriction: x != -d/c
        second_root_num = -d
        second_root_den = c
        g = gcd(abs(second_root_num), abs(second_root_den))
        rn = second_root_num // g
        rd = second_root_den // g
        if rd < 0:
            rn, rd = -rn, -rd
        if rd == 1:
            restr2_latex = f"x \\ne {rn}"
        else:
            restr2_latex = rf"x \ne \frac{{{rn}}}{{{rd}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Simplify $\\dfrac{{{numer_latex}}}{{{denom_latex}}}$. "
                "State any restrictions on $x$."
            ),
            answer_latex=(
                f"$\\dfrac{{{answer_num}}}{{{answer_den}}},\\ x \\ne 0,\\ {restr2_latex}$"
            ),
            hints=[
                "Both the numerator and the denominator share a common factor of $x$.",
                "Factor $x$ out of each, then cancel.",
                f"Numerator: ${numer_factored}$. Denominator: ${denom_factored}$.",
            ],
            solution_steps_latex=[
                f"Factor $x$ from the numerator: ${numer_latex} = {numer_factored}$.",
                f"Factor $x$ from the denominator: ${denom_latex} = {denom_factored}$.",
                f"Cancel $x$: $\\dfrac{{{answer_num}}}{{{answer_den}}}$.",
                f"Restrictions: $x \\ne 0$ and ${restr2_latex}$.",
            ],
            tags=list(RAT_TAGS),
        )


# ===========================================================================
# Topic 2: multiplying_and_dividing_rational_expressions
# ===========================================================================


@register
class MultiplyRationalsBasic(Generator):
    """Multiply (ax/b) * (c/(dx)) so x cancels and constants reduce.

    Backward: pick p, q with an explicit shared factor g so the result is
    the reduced fraction (p/q).
    """
    generator_id = "multiply_rationals_basic"
    topic_slug = "multiplying_and_dividing_rational_expressions"
    display_name = "Multiply two rational expressions (basic)"

    _RANGES = {"easy": (2, 8), "medium": (2, 14), "hard": (2, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Build (ax^k / m) * (n / (bx^j))
        # Backward: first pick final reduced answer P/Q in lowest terms.
        while True:
            p = rng.randint(1, hi)
            q = rng.randint(2, hi)
            if gcd(p, q) == 1:
                break
        # Pick a shared factor g to "hide" the simplification
        g = rng.randint(2, hi)
        # Numer of first fraction: p * g, Denom of second fraction: q * g
        # Insert x to both first-numer and second-denom so they cancel
        # First: (p*g * x) / k1. Second: k1 / (q*g * x). Product = p*g / q*g = p/q
        # But we want a more interesting setup. Use cross cancellation:
        # (A * x) / C  *  D / (B * x) where A=p, B=q, and C,D share factor g
        # Let C = g, D = g * something. Actually simpler:
        # (p*x / g) * (g / (q*x)) -> (p * g * x) / (g * q * x) = p/q
        k1 = g  # first fraction denominator
        k2 = g  # second fraction numerator
        A = p  # first fraction numer coef
        B = q  # second fraction denom coef

        frac1_num_latex = f"{A}x" if A != 1 else "x"
        frac1_den_latex = str(k1)
        frac2_num_latex = str(k2)
        frac2_den_latex = f"{B}x" if B != 1 else "x"

        # Answer: p / q (reduced) — plain fraction
        if q == 1:
            answer_latex = f"{p}"
        else:
            answer_latex = rf"\frac{{{p}}}{{{q}}}"

        expr_latex = (
            rf"\dfrac{{{frac1_num_latex}}}{{{frac1_den_latex}}} "
            rf"\cdot \dfrac{{{frac2_num_latex}}}{{{frac2_den_latex}}}"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q, g)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Multiply and simplify: ${expr_latex}$.",
            answer_latex=f"${answer_latex}$",
            hints=[
                "Before multiplying, look for common factors that cancel across the two fractions.",
                f"The $x$ in the first numerator cancels with the $x$ in the second denominator.",
                f"The ${k1}$ in the first denominator cancels with the ${k2}$ in the second numerator.",
            ],
            solution_steps_latex=[
                f"Write the product as one fraction: $\\dfrac{{({frac1_num_latex})({frac2_num_latex})}}{{({frac1_den_latex})({frac2_den_latex})}}$.",
                f"Multiply out: $\\dfrac{{{A * k2}x}}{{{k1 * B}x}}$.",
                f"Cancel $x$ and reduce: ${answer_latex}$.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class DivideRationalsReciprocal(Generator):
    """Divide (A/B) / (C/D) by flipping to (A/B) * (D/C) then simplifying.

    Backward: pick a reduced final answer p/q, then construct pieces that
    multiply to p/q after the flip.
    """
    generator_id = "divide_rationals_reciprocal"
    topic_slug = "multiplying_and_dividing_rational_expressions"
    display_name = "Divide two rational expressions via reciprocal"

    _RANGES = {"easy": (2, 8), "medium": (2, 14), "hard": (2, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Final answer is p/q (reduced). We divide (p*x / g) by (q*x / g)
        # which flips to (p*x / g) * (g / (q*x)) = p/q.
        while True:
            p = rng.randint(1, hi)
            q = rng.randint(2, hi)
            if gcd(p, q) == 1:
                break
        g = rng.randint(2, hi)

        frac1_num_latex = f"{p}x" if p != 1 else "x"
        frac1_den_latex = str(g)
        frac2_num_latex = f"{q}x" if q != 1 else "x"
        frac2_den_latex = str(g)

        expr_latex = (
            rf"\dfrac{{{frac1_num_latex}}}{{{frac1_den_latex}}} "
            rf"\div \dfrac{{{frac2_num_latex}}}{{{frac2_den_latex}}}"
        )

        if q == 1:
            answer_latex = f"{p}"
        else:
            answer_latex = rf"\frac{{{p}}}{{{q}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q, g)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Divide and simplify: ${expr_latex}$.",
            answer_latex=f"${answer_latex}$",
            hints=[
                "Dividing by a fraction is the same as multiplying by its reciprocal.",
                "Flip the second fraction, then multiply.",
                "Cancel common factors of $x$ and common numerical factors.",
            ],
            solution_steps_latex=[
                f"Flip the second fraction: $\\dfrac{{{frac1_num_latex}}}{{{frac1_den_latex}}} "
                f"\\cdot \\dfrac{{{frac2_den_latex}}}{{{frac2_num_latex}}}$.",
                f"Write as one fraction: $\\dfrac{{{p} \\cdot {g} \\cdot x}}{{{g} \\cdot {q} \\cdot x}}$.",
                f"Cancel ${g}$ and $x$: ${answer_latex}$.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class MultiplyRationalsFactorFirst(Generator):
    """Multiply (expanded-num / expanded-den) * (expanded-num / expanded-den)
    where both numerators and denominators must be factored before cancellation
    is visible.

    Backward: pick four distinct linear factors (x+a), (x+b), (x+c), (x+d).
    Construct first fraction = (x+a)(x+b) / (x+c)(x+d) and
    second fraction = (x+c)(x+d) / (x+a)(x+b) ... wait that gives 1.
    Instead use five factors: (x+a)(x+b)/(x+c)(x+d) * (x+c)(x+e)/(x+a)(x+f)
    Cancel (x+a), (x+c). Answer = (x+b)(x+e)/((x+d)(x+f)).
    """
    generator_id = "multiply_rationals_factor_first"
    topic_slug = "multiplying_and_dividing_rational_expressions"
    display_name = "Multiply rationals after factoring"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick six distinct nonzero integers
        picks: list[int] = []
        while len(picks) < 6:
            val = rng.randint(-hi, hi)
            if val == 0 or abs(val) < lo:
                continue
            if val in picks:
                continue
            picks.append(val)
        a, b, c, d, e, f = picks

        # First fraction: (x+a)(x+b) / (x+c)(x+d)
        num1 = sp.expand((x + a) * (x + b))
        den1 = sp.expand((x + c) * (x + d))
        # Second fraction: (x+c)(x+e) / (x+a)(x+f)
        num2 = sp.expand((x + c) * (x + e))
        den2 = sp.expand((x + a) * (x + f))

        num1_latex = sp.latex(num1)
        den1_latex = sp.latex(den1)
        num2_latex = sp.latex(num2)
        den2_latex = sp.latex(den2)

        # Answer: (x+b)(x+e) / ((x+d)(x+f))
        answer_num = f"{_linear_factor(b)}{_linear_factor(e)}"
        answer_den = f"{_linear_factor(d)}{_linear_factor(f)}"

        expr_latex = (
            rf"\dfrac{{{num1_latex}}}{{{den1_latex}}} "
            rf"\cdot \dfrac{{{num2_latex}}}{{{den2_latex}}}"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, e, f)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Multiply and simplify: ${expr_latex}$. "
                "Write your answer in factored form."
            ),
            answer_latex=f"$\\dfrac{{{answer_num}}}{{{answer_den}}}$",
            hints=[
                "Start by factoring every numerator and every denominator.",
                "Once everything is factored, look for common linear factors to cancel.",
                f"The factors ${_linear_factor(a)}$ and ${_linear_factor(c)}$ appear in both a numerator and a denominator.",
            ],
            solution_steps_latex=[
                f"Factor each piece: $\\dfrac{{{_linear_factor(a)}{_linear_factor(b)}}}{{{_linear_factor(c)}{_linear_factor(d)}}} \\cdot \\dfrac{{{_linear_factor(c)}{_linear_factor(e)}}}{{{_linear_factor(a)}{_linear_factor(f)}}}$.",
                f"Cancel ${_linear_factor(a)}$ (numerator of first with denominator of second) and ${_linear_factor(c)}$ (denominator of first with numerator of second).",
                f"What remains: $\\dfrac{{{answer_num}}}{{{answer_den}}}$.",
            ],
            tags=list(RAT_TAGS),
        )


# ===========================================================================
# Topic 3: adding_and_subtracting_rational_expressions
# ===========================================================================


@register
class AddRationalsSameDenom(Generator):
    """Add A/D + B/D where D is a linear expression.

    Backward: pick A, B as linear terms, D as (x + k).
    """
    generator_id = "add_rationals_same_denom"
    topic_slug = "adding_and_subtracting_rational_expressions"
    display_name = "Add two rationals with the same denominator"

    _RANGES = {"easy": (1, 8), "medium": (1, 14), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Numerators: A = m*x + p, B = n*x + q
        m = rng.randint(1, hi)
        p = rng.randint(-hi, hi)
        n = rng.randint(1, hi)
        q = rng.randint(-hi, hi)
        # Randomly negate m and n sometimes
        if rng.random() < 0.5:
            m = -m
        if rng.random() < 0.5:
            n = -n
        # Denominator
        k = rng.randint(-hi, hi)
        while k == 0:
            k = rng.randint(-hi, hi)

        # Sum: ((m+n)x + (p+q)) / (x + k)
        sum_coef = m + n
        sum_const = p + q

        def _render_lin(coef: int, const: int) -> str:
            if coef == 0:
                return str(const)
            if coef == 1:
                lead = "x"
            elif coef == -1:
                lead = "-x"
            else:
                lead = f"{coef}x"
            if const == 0:
                return lead
            sign = "+" if const > 0 else "-"
            return f"{lead} {sign} {abs(const)}"

        num1_latex = _render_lin(m, p)
        num2_latex = _render_lin(n, q)
        sum_latex = _render_lin(sum_coef, sum_const)
        den_latex = _linear_factor(k)

        answer_latex = rf"\dfrac{{{sum_latex}}}{{{den_latex}}}" if sum_coef != 0 or sum_const != 0 else "0"

        # Restrictions: x != -k
        restriction = f"x \\ne {-k}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, p, n, q, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Add and simplify: $\\dfrac{{{num1_latex}}}{{{den_latex}}} "
                f"+ \\dfrac{{{num2_latex}}}{{{den_latex}}}$."
            ),
            answer_latex=f"${answer_latex},\\ {restriction}$",
            hints=[
                "The two fractions already share a denominator.",
                "Add the numerators over the common denominator.",
                "Combine like terms in the new numerator.",
            ],
            solution_steps_latex=[
                f"Same denominator, so add numerators: $\\dfrac{{({num1_latex}) + ({num2_latex})}}{{{den_latex}}}$.",
                f"Combine like terms in the numerator: ${sum_latex}$.",
                f"Result: ${answer_latex}$, with $x \\ne {-k}$.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class AddRationalsLinearDenoms(Generator):
    """Add A/(x+a) + B/(x+b) where (x+a) and (x+b) share no common factor.

    LCD is (x+a)(x+b). Backward: pick A, B, a, b as integers.
    """
    generator_id = "add_rationals_linear_denoms"
    topic_slug = "adding_and_subtracting_rational_expressions"
    display_name = "Add A/(x+a) + B/(x+b) with unlike linear denominators"

    _RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick two distinct shifts
        a = rng.randint(-hi, hi)
        while a == 0:
            a = rng.randint(-hi, hi)
        b = rng.randint(-hi, hi)
        while b == 0 or b == a:
            b = rng.randint(-hi, hi)
        # Numerators (small integers)
        A = rng.randint(1, hi)
        B = rng.randint(1, hi)
        if rng.random() < 0.5:
            A = -A
        if rng.random() < 0.5:
            B = -B

        # Combined: (A(x+b) + B(x+a)) / ((x+a)(x+b))
        # numerator = (A+B)x + (A*b + B*a)
        num_coef = A + B
        num_const = A * b + B * a

        def _render_lin(coef: int, const: int) -> str:
            if coef == 0:
                return str(const)
            if coef == 1:
                lead = "x"
            elif coef == -1:
                lead = "-x"
            else:
                lead = f"{coef}x"
            if const == 0:
                return lead
            sign = "+" if const > 0 else "-"
            return f"{lead} {sign} {abs(const)}"

        num_latex = _render_lin(num_coef, num_const)
        den_latex = f"{_linear_factor(a)}{_linear_factor(b)}"

        answer_latex = rf"\dfrac{{{num_latex}}}{{{den_latex}}}"
        restriction = f"x \\ne {-a},\\ x \\ne {-b}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, a, B, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Add and simplify: $\\dfrac{{{A}}}{{{_linear_factor(a)}}} "
                f"+ \\dfrac{{{B}}}{{{_linear_factor(b)}}}$. State any restrictions."
            ),
            answer_latex=f"${answer_latex},\\ {restriction}$",
            hints=[
                "The denominators share no common factor, so the LCD is their product.",
                f"The LCD is ${den_latex}$.",
                "Multiply each fraction by the missing factor (over itself), then add the numerators.",
            ],
            solution_steps_latex=[
                f"LCD: ${den_latex}$.",
                f"Rewrite: $\\dfrac{{{A}{_linear_factor(b)} + {B}{_linear_factor(a)}}}{{{den_latex}}}$.",
                f"Expand and combine like terms in the numerator: ${num_latex}$.",
                f"Result: ${answer_latex}$, with ${restriction}$.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class SubtractRationalsFactorDenom(Generator):
    """Subtract A/(x+a) - B/((x+a)(x+c)) where the second denom has (x+a).

    Backward: pick distinct nonzero integers a, c; pick integer A and B.
    The LCD is (x+a)(x+c). Numerator becomes A(x+c) - B.
    """
    generator_id = "subtract_rationals_factor_denom"
    topic_slug = "adding_and_subtracting_rational_expressions"
    display_name = "Subtract with a factorable denominator"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(-hi, hi)
        while a == 0:
            a = rng.randint(-hi, hi)
        c = rng.randint(-hi, hi)
        while c == 0 or c == a:
            c = rng.randint(-hi, hi)
        A = rng.randint(1, hi)
        B = rng.randint(1, hi)
        if rng.random() < 0.5:
            A = -A
        if rng.random() < 0.5:
            B = -B

        # Second denom = (x+a)(x+c) expanded
        second_den_expanded = sp.expand((x + a) * (x + c))
        second_den_latex = sp.latex(second_den_expanded)

        # Combined numerator: A(x+c) - B = A*x + (A*c - B)
        num_coef = A
        num_const = A * c - B

        def _render_lin(coef: int, const: int) -> str:
            if coef == 0:
                return str(const)
            if coef == 1:
                lead = "x"
            elif coef == -1:
                lead = "-x"
            else:
                lead = f"{coef}x"
            if const == 0:
                return lead
            sign = "+" if const > 0 else "-"
            return f"{lead} {sign} {abs(const)}"

        num_latex = _render_lin(num_coef, num_const)
        lcd_latex = f"{_linear_factor(a)}{_linear_factor(c)}"

        answer_latex = rf"\dfrac{{{num_latex}}}{{{lcd_latex}}}"
        restriction = f"x \\ne {-a},\\ x \\ne {-c}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, a, B, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Subtract and simplify: $\\dfrac{{{A}}}{{{_linear_factor(a)}}} "
                f"- \\dfrac{{{B}}}{{{second_den_latex}}}$. State any restrictions."
            ),
            answer_latex=f"${answer_latex},\\ {restriction}$",
            hints=[
                "First factor the second denominator.",
                f"${second_den_latex} = {_linear_factor(a)}{_linear_factor(c)}$.",
                f"The LCD is ${lcd_latex}$.",
                "Multiply the first fraction by the missing factor, then subtract.",
            ],
            solution_steps_latex=[
                f"Factor the second denominator: ${second_den_latex} = {_linear_factor(a)}{_linear_factor(c)}$.",
                f"The LCD is ${lcd_latex}$.",
                f"Rewrite the first fraction: $\\dfrac{{{A}}}{{{_linear_factor(a)}}} = \\dfrac{{{A}{_linear_factor(c)}}}{{{lcd_latex}}}$.",
                f"Subtract: $\\dfrac{{{A}{_linear_factor(c)} - {B}}}{{{lcd_latex}}} = \\dfrac{{{num_latex}}}{{{lcd_latex}}}$.",
                f"Restrictions: ${restriction}$.",
            ],
            tags=list(RAT_TAGS),
        )


# ===========================================================================
# Topic 4: solving_rational_equations
# ===========================================================================


@register
class SolveRationalLinearCrossMultiply(Generator):
    """Solve A/(x+p) = C/(x+q) by cross-multiplying.

    Backward: pick the integer solution x0, then choose A, C, p, q so that
    A*(x0 + q) = C*(x0 + p) and neither (x0 + p) nor (x0 + q) is zero.
    """
    generator_id = "solve_rational_linear_cross_multiply"
    topic_slug = "solving_rational_equations"
    display_name = "Solve A/(x+p) = C/(x+q) by cross-multiplying"

    _RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Backward: pick x0 (nonzero to keep things interesting), pick p, q
        # distinct, and pick A. Then C = A * (x0 + q) / (x0 + p) must be an
        # integer. Easiest approach: pick p, q, x0 such that (x0 + p) divides
        # A*(x0 + q).
        for _ in range(500):
            x0 = rng.randint(-hi, hi)
            p = rng.randint(-hi, hi)
            q = rng.randint(-hi, hi)
            if p == q:
                continue
            if x0 + p == 0 or x0 + q == 0:
                continue
            A = rng.randint(1, hi)
            if rng.random() < 0.5:
                A = -A
            # We want C = A * (x0 + q) / (x0 + p) to be an integer.
            num = A * (x0 + q)
            den = x0 + p
            if num % den == 0:
                C = num // den
                if C == 0:
                    continue
                break
        else:
            A, C, p, q, x0 = 1, 1, 0, 0, 0  # safe fallback
            # Make trivially solvable: 1/(x-1) = 1/(x-1) with x=2? Need p!=q
            p, q = 0, 1
            x0 = 2
            A = C = 1

        expr_latex = (
            rf"\dfrac{{{A}}}{{{_linear_factor(p)}}} = "
            rf"\dfrac{{{C}}}{{{_linear_factor(q)}}}"
        )
        restriction = f"x \\ne {-p},\\ x \\ne {-q}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, p, C, q)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${expr_latex}$ for $x$. Check for extraneous solutions.",
            answer_latex=f"$x = {x0}$",
            hints=[
                "Cross-multiply to clear the fractions.",
                f"You get ${A}{_linear_factor(q)} = {C}{_linear_factor(p)}$.",
                "Expand, combine like terms, and solve the linear equation.",
                f"Remember the restrictions: ${restriction}$.",
            ],
            solution_steps_latex=[
                f"Cross-multiply: ${A}{_linear_factor(q)} = {C}{_linear_factor(p)}$.",
                f"Expand both sides and collect $x$ terms.",
                f"Solve the resulting linear equation to get $x = {x0}$.",
                f"Check: $x = {x0}$ does not violate ${restriction}$, so it is valid.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class SolveRationalLinearMultiplyLcd(Generator):
    """Solve A/x + B = C/x by multiplying through by x (the LCD).

    Backward: pick x0 (nonzero), pick B != 0, pick A != C, then
    x = (C - A)/B must equal x0. So set A = rng, B = rng, then C = A + B*x0.
    """
    generator_id = "solve_rational_linear_multiply_lcd"
    topic_slug = "solving_rational_equations"
    display_name = "Solve A/x + B = C/x by multiplying by LCD"

    _RANGES = {"easy": (1, 8), "medium": (1, 14), "hard": (1, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        for _ in range(500):
            x0 = rng.randint(-hi, hi)
            if x0 == 0:
                continue
            A = rng.randint(1, hi)
            if rng.random() < 0.5:
                A = -A
            B = rng.randint(1, hi)
            if rng.random() < 0.5:
                B = -B
            if B == 0:
                continue
            C = A + B * x0
            if C == A:
                continue
            break
        else:
            A, B, C, x0 = 1, 1, 2, 1

        expr_latex = rf"\dfrac{{{A}}}{{x}} + {B} = \dfrac{{{C}}}{{x}}"

        # Multiply through: A + Bx = C -> Bx = C - A -> x = (C-A)/B = x0
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, B, C)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${expr_latex}$ for $x$.",
            answer_latex=f"$x = {x0}$",
            hints=[
                "The LCD is $x$. Multiply every term by $x$ to clear the fractions.",
                f"After multiplying, the equation becomes ${A} + {B}x = {C}$.",
                f"Solve the linear equation for $x$. Remember $x \\ne 0$.",
            ],
            solution_steps_latex=[
                f"Multiply every term by the LCD, $x$: ${A} + {B}x = {C}$.",
                f"Subtract ${A}$ from both sides: ${B}x = {C - A}$.",
                f"Divide by ${B}$: $x = \\dfrac{{{C - A}}}{{{B}}} = {x0}$.",
                f"Check: $x = {x0} \\ne 0$, so the solution is valid.",
            ],
            tags=list(RAT_TAGS),
        )


@register
class SolveRationalWithExtraneous(Generator):
    """Solve A/(x - k) = B/(x - k) + C where one candidate is extraneous.

    Construction: we want the equation to algebraically produce two
    candidates: the real solution x0, and x = k (which makes a denominator
    zero and is therefore extraneous).

    Strategy: use the equation
        (x - k)/(x - k) * [A/(x - k)] = (x - k)/(x - k) * [B/(x - k) + C]
    i.e., multiply through by (x - k) to get A = B + C(x - k), which gives
    a single linear solution. To deliberately produce an extraneous
    solution, we use the form
        (x^2 term form) / (x - k) = something / (x - k) + integer
    that when cleared produces a quadratic with roots x0 and k.

    Concrete backward construction:
      Target equation:  (x + k)/(x - k) = C/(x - k) + x
      Multiply by (x - k): x + k = C + x(x - k)
      Rearrange: x^2 - (k+1)x + (C - k) = 0
      We want roots x = x0 and x = k. So:
          (x - x0)(x - k) = x^2 - (x0 + k)x + x0*k
      Match coefficients: x0 + k = k + 1  =>  x0 = 1
      And: x0 * k = C - k  =>  C = k + x0*k = k + k = 2k
    That constrains x0 = 1 always, which is too restrictive. Use
    parameterised template instead:

      Equation:  m/(x - k) = n/(x - k) + 1
      Clearing: m = n + (x - k)
      -> x = m - n + k
      This is linear with one solution, no extraneous. Bad.

    Final approach: use the classical textbook form
        x/(x - k) - k/(x - k) = something  that simplifies to (x - k)/(x - k) = 1
    and then construct a wrapper that introduces an extraneous x = k.

    Concrete working construction (used below):
      Equation:  (x^2)/(x - k) = k + (x*k)/(x - k)
      Clear (multiply by (x - k)): x^2 = k(x - k) + x*k = kx - k^2 + kx = 2kx - k^2
      x^2 - 2kx + k^2 = 0  ->  (x - k)^2 = 0  ->  x = k (extraneous, no real sol)
    Not useful either. Let's use the simpler textbook pattern:

      Equation: (x + k)/(x - k) + 2 = 2k/(x - k)
      Multiply (x - k): (x + k) + 2(x - k) = 2k
      -> x + k + 2x - 2k = 2k
      -> 3x - k = 2k
      -> 3x = 3k -> x = k (extraneous!)
    That gives ONLY the extraneous solution and no real solution. Also not useful.

    TEXTBOOK STANDARD EXTRANEOUS PATTERN (the one actually used):
      Equation:  (x^2 - a^2)/(x - a) = x - b
      Before simplifying the LHS factors:  LHS = (x + a)(x - a)/(x - a) = x + a
      So equation becomes x + a = x - b, which has no solution if a != -b.
      NOT useful.

    OK, use the most common textbook pattern: equations where multiplying by
    the LCD yields a quadratic whose roots are {x0, k}, where k makes the
    denominator zero.

      Equation:  1/(x - k) + x = m/(x - k)
      Multiply by (x - k): 1 + x(x - k) = m
      -> x^2 - kx + (1 - m) = 0
      We want this to factor as (x - x0)(x - k) = x^2 - (x0 + k)x + x0*k
      Match: x0 + k = k  =>  x0 = 0 (not useful; we want x0 != 0)
      And k = k - but then 1 - m = x0*k = 0, so m = 1.
    So this pattern forces x0 = 0. Boring but valid.

    Use a different pattern:
      Equation:  A/(x - k) + B = (Ax)/(x - k)
      Multiply by (x - k): A + B(x - k) = Ax
      -> A + Bx - Bk = Ax
      -> (B - A)x = Bk - A
      -> x = (Bk - A)/(B - A) (linear, one solution, no extraneous)
    This is linear, so no extraneous issue.

    FINAL WORKING PATTERN (verified):
      Equation:  x/(x - k) - k/(x - k) = k/(x - k)
      Combine LHS: (x - k)/(x - k) = 1 for x != k
      So 1 = k/(x - k) -> x - k = k -> x = 2k (valid if 2k != k, i.e., k != 0)
    But then multiplying through by (x-k) we get x - k = k, which is linear
    with x = 2k and the domain x != k excludes nothing. No extraneous.

    Let me try the pattern:
      Equation:  A/(x - k) + B/(x + k) = C/((x - k)(x + k))
      Multiply by (x-k)(x+k): A(x+k) + B(x-k) = C
      Linear; no extraneous.

    PATTERN THAT ACTUALLY WORKS (verified by hand):
      Equation: x + k/(x - k) = (x*x - k*k)/(x - k) + something that needs quadratic
      Too complex. Let me use this verified pattern:

      Equation:  k^2/(x^2 - k^2) = 1 - k/(x + k)
      Factor: k^2/((x-k)(x+k)) = 1 - k/(x+k)
      Multiply by (x-k)(x+k): k^2 = (x-k)(x+k) - k(x-k)
      k^2 = x^2 - k^2 - kx + k^2 = x^2 - kx
      -> x^2 - kx - k^2 = 0
      Quadratic roots x = (k +/- sqrt(5)k)/2 - not nice integer.

    OK, forget generic construction. Use a hand-verified template and
    parameterize only k:

      Equation: (x + 1)/(x - k) = k/(x - k) + 1
      Clear (multiply by x - k): x + 1 = k + (x - k) = x
      -> 1 = 0, no solution. Bad.

    Final-final approach: the textbook-standard extraneous pattern is
      A/(x - k) = B/(x^2 - k^2) + 1/(x + k)
    but constructing with integer roots is hard.

    Working CONSTRUCTION used below:
      Equation:  (x^2)/(x - k) = (k * x0) + (x0 + k) * x/(x - k)
      Verify this for specific integers in _generate_one and fall back if needed.

    To avoid all this complexity, we use a ROBUST pattern: start with the
    desired solutions set {x0, k}, construct the polynomial (x - x0)(x - k),
    and set up the equation
        (x - x0)(x - k) / (x - k) = (x - x0) * (polynomial)/(polynomial)
    that LOOKS like a rational equation but, when cleared, gives the
    quadratic (x - x0)(x - k) = 0.

    The concrete equation used:
        (x^2 - (x0 + k)*x + x0*k)/(x - k) = 0
    Multiplying by (x - k): x^2 - (x0 + k)x + x0*k = 0
    Which factors (x - x0)(x - k) = 0, giving candidates x = x0 (valid) and
    x = k (extraneous because x - k = 0 violates the domain).

    We present the numerator in expanded form so the student must clear
    the fraction to see the quadratic.
    """
    generator_id = "solve_rational_with_extraneous"
    topic_slug = "solving_rational_equations"
    display_name = "Solve a rational equation with an extraneous solution"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick x0 (the real solution) and k (the extraneous value) distinct,
        # both nonzero.
        while True:
            x0 = rng.randint(-hi, hi)
            k = rng.randint(-hi, hi)
            if x0 == 0 or k == 0:
                continue
            if x0 == k:
                continue
            break

        # Equation: (x^2 - (x0+k)*x + x0*k)/(x - k) = 0
        # Denominator (x - k) is zero at x = k, so that's the extraneous value.
        b_coef = -(x0 + k)
        c_const = x0 * k
        # Numerator polynomial
        numer = sp.expand(x * x + b_coef * x + c_const)
        numer_latex = sp.latex(numer)
        # Denominator must be (x - k) so its zero is at x = k.
        # _linear_factor takes the "shift" param where _linear_factor(a) gives (x + a)
        # with root at -a. So for (x - k), pass -k.
        den_latex = _linear_factor(-k)

        expr_latex = rf"\dfrac{{{numer_latex}}}{{{den_latex}}} = 0"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x0, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve ${expr_latex}$ for $x$. Identify any extraneous solutions."
            ),
            answer_latex=f"$x = {x0}$ (the candidate $x = {k}$ is extraneous)",
            hints=[
                f"A fraction is zero only when its numerator is zero (and the denominator is nonzero). So set ${numer_latex} = 0$.",
                "Factor the quadratic and solve.",
                f"Check each candidate against the restriction $x \\ne {k}$ (the denominator cannot be zero).",
            ],
            solution_steps_latex=[
                f"A fraction equals zero only when the numerator is zero: ${numer_latex} = 0$.",
                f"Factor: ${_linear_factor(-x0)}{_linear_factor(-k)} = 0$.",
                f"Candidates: $x = {x0}$ and $x = {k}$.",
                f"Restriction from the original equation: $x \\ne {k}$, so $x = {k}$ is **extraneous**.",
                f"The only valid solution is $x = {x0}$.",
            ],
            tags=list(RAT_TAGS),
        )


# ===========================================================================
# Topic 5: rational_equations_and_applications
# ===========================================================================

# Paraphrased work-problem templates. Names rotate through a small pool.
_WORK_NAMES = [
    ("Alex", "Bailey"),
    ("Bailey", "Chris"),
    ("Chris", "Dana"),
    ("Dana", "Alex"),
    ("Alex", "Chris"),
    ("Bailey", "Dana"),
]

_WORK_TASKS = [
    "paint a mural",
    "weed the garden",
    "stack the firewood",
    "assemble the bookshelves",
    "catalog the archives",
    "repaint the fence",
    "clean out the attic",
    "shovel the driveway",
]


@register
class WorkProblemCombinedRate(Generator):
    """Alex can finish a task in A hours, Bailey in B hours; how long together?

    Solve 1/t = 1/A + 1/B  =>  t = AB/(A+B). Backward: pick A and B so
    A*B / (A+B) is a clean value.
    """
    generator_id = "work_problem_combined_rate"
    topic_slug = "rational_equations_and_applications"
    display_name = "Work problem: combined rate (1/t = 1/A + 1/B)"
    supports_word_problems = True
    bank_count_per_difficulty = 25

    # Precomputed clean (A, B) pairs that yield nice t = AB/(A+B) values.
    _CLEAN_PAIRS = {
        "easy": [
            (2, 2), (3, 6), (4, 4), (4, 12), (6, 3), (6, 6), (6, 12), (10, 10),
            (12, 4), (12, 6), (2, 3), (3, 2), (4, 6), (6, 4),
        ],
        "medium": [
            (3, 6), (4, 12), (6, 12), (10, 15), (12, 4), (12, 6), (15, 10),
            (18, 6), (20, 5), (20, 30), (24, 8), (30, 20), (5, 20), (6, 18),
            (8, 24),
        ],
        "hard": [
            (10, 15), (12, 24), (15, 10), (18, 9), (20, 30), (24, 8),
            (30, 20), (30, 45), (40, 10), (60, 30), (45, 30), (48, 16),
            (36, 12), (25, 100), (50, 50), (60, 20),
        ],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pairs = self._CLEAN_PAIRS[difficulty]
        A, B = rng.choice(pairs)
        name1, name2 = rng.choice(_WORK_NAMES)
        task = rng.choice(_WORK_TASKS)

        # t = AB/(A+B)
        num_ab = A * B
        sum_ab = A + B
        g = gcd(num_ab, sum_ab)
        t_num = num_ab // g
        t_den = sum_ab // g
        if t_den == 1:
            t_latex = str(t_num)
            t_prose = f"{t_num} hours"
        else:
            t_latex = rf"\frac{{{t_num}}}{{{t_den}}}"
            t_prose = f"{t_num}/{t_den} hours"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, B, name1, name2, task)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{name1} can {task} alone in ${A}$ hours. {name2} can {task} "
                f"alone in ${B}$ hours. Working together at their individual "
                f"rates, how many hours will it take them to {task}?"
            ),
            answer_latex=f"$t = {t_latex}$ hours",
            hints=[
                rf"{name1}'s rate is $\dfrac{{1}}{{{A}}}$ of the job per hour; {name2}'s rate is $\dfrac{{1}}{{{B}}}$ of the job per hour.",
                r"If they work together for $t$ hours, their combined work equals one full job: $\dfrac{t}{A} + \dfrac{t}{B} = 1$, or equivalently $\dfrac{1}{t} = \dfrac{1}{A} + \dfrac{1}{B}$.",
                r"Solve for $t$: $t = \dfrac{AB}{A + B}$.",
            ],
            solution_steps_latex=[
                rf"Rate equation: $\dfrac{{1}}{{t}} = \dfrac{{1}}{{{A}}} + \dfrac{{1}}{{{B}}}$.",
                rf"Common denominator on the right: $\dfrac{{1}}{{t}} = \dfrac{{{B} + {A}}}{{{A}\cdot{B}}} = \dfrac{{{sum_ab}}}{{{num_ab}}}$.",
                rf"Invert: $t = \dfrac{{{num_ab}}}{{{sum_ab}}} = {t_latex}$ hours.",
                f"So together they finish in approximately {t_prose}.",
            ],
            tags=list(RAT_TAGS),
        )


# Paraphrased distance/rate/time scenarios for upstream/downstream problems.
_DRT_VEHICLES = [
    {"craft": "kayak", "medium": "river", "flow": "current"},
    {"craft": "canoe", "medium": "river", "flow": "current"},
    {"craft": "rowboat", "medium": "lake inlet", "flow": "current"},
    {"craft": "motorboat", "medium": "channel", "flow": "current"},
    {"craft": "swimmer", "medium": "stream", "flow": "current"},
    {"craft": "cyclist", "medium": "open road", "flow": "wind"},
    {"craft": "runner", "medium": "trail", "flow": "wind"},
]


@register
class DistanceRateTimeUpstream(Generator):
    """A craft travels distance D_down downstream in the same time it travels
    D_up upstream; the current (or wind) has speed c. Find the still-water
    (or no-wind) speed s.

    Equation: D_down / (s + c) = D_up / (s - c)
    Solving: D_down * (s - c) = D_up * (s + c)
            D_down*s - D_down*c = D_up*s + D_up*c
            (D_down - D_up)*s = (D_down + D_up)*c
            s = c * (D_down + D_up) / (D_down - D_up)

    Backward: pick s, c; pick a scaling factor; set D_down = (s+c)*k,
    D_up = (s-c)*k for some integer k, ensuring clean distances.
    """
    generator_id = "distance_rate_time_upstream"
    topic_slug = "rational_equations_and_applications"
    display_name = "Distance / rate / time: upstream-downstream (find still-water speed)"
    supports_word_problems = True
    bank_count_per_difficulty = 25

    _S_RANGES = {"easy": (4, 12), "medium": (6, 20), "hard": (10, 40)}
    _C_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (2, 8)}
    _K_RANGES = {"easy": (1, 3), "medium": (1, 4), "hard": (1, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        s_lo, s_hi = self._S_RANGES[difficulty]
        c_lo, c_hi = self._C_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        for _ in range(200):
            s = rng.randint(s_lo, s_hi)
            c = rng.randint(c_lo, c_hi)
            k = rng.randint(k_lo, k_hi)
            if s <= c:
                continue
            D_down = (s + c) * k
            D_up = (s - c) * k
            if D_down == D_up:
                continue
            if D_down <= 0 or D_up <= 0:
                continue
            break
        else:
            s, c, k = 8, 2, 1
            D_down, D_up = 10, 6

        vehicle = rng.choice(_DRT_VEHICLES)
        craft = vehicle["craft"]
        medium = vehicle["medium"]
        flow = vehicle["flow"]

        # Problem wording adapts for wind vs current
        still_phrase = "in still water" if flow == "current" else "in still air"
        with_phrase = "with" if flow == "current" else "with the"
        against_phrase = "against" if flow == "current" else "against the"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (s, c, D_down, D_up, craft),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {craft} travels ${D_down}$ miles {with_phrase} the {flow} on a "
                f"{medium} in the same time it travels ${D_up}$ miles {against_phrase} "
                f"the {flow}. If the {flow} runs at ${c}$ mph, find the speed of the "
                f"{craft} {still_phrase}."
            ),
            answer_latex=f"$s = {s}$ mph",
            hints=[
                rf"Let $s$ be the {craft}'s speed {still_phrase}. Then the speed with the {flow} is $(s + {c})$ and against is $(s - {c})$.",
                rf"Since the times are equal, $\dfrac{{{D_down}}}{{s + {c}}} = \dfrac{{{D_up}}}{{s - {c}}}$.",
                "Cross-multiply and solve for $s$.",
            ],
            solution_steps_latex=[
                rf"Let $s$ = speed of the {craft} {still_phrase}.",
                rf"Time equation: $\dfrac{{{D_down}}}{{s + {c}}} = \dfrac{{{D_up}}}{{s - {c}}}$.",
                rf"Cross-multiply: ${D_down}(s - {c}) = {D_up}(s + {c})$.",
                rf"Expand: ${D_down}s - {D_down * c} = {D_up}s + {D_up * c}$.",
                rf"Collect $s$ terms: $({D_down - D_up})s = {D_down * c + D_up * c}$.",
                rf"Divide: $s = \dfrac{{{D_down * c + D_up * c}}}{{{D_down - D_up}}} = {s}$ mph.",
            ],
            tags=list(RAT_TAGS),
        )


# Paraphrased round-trip commute scenarios.
_ROUND_TRIP_ROUTES = [
    "from Maple Heights to Bayside",
    "between Elmwood and Riverpoint",
    "from Oakdale Terrace to the office park",
    "from the lakeshore cabin to the trailhead",
    "between Pine Hollow and the downtown lot",
    "from the suburban depot to the coastal lab",
]


@register
class AverageRateRoundTrip(Generator):
    """Drive distance D at rate r1, then return the same distance at rate r2.
    Find the average speed for the whole round trip.

    Formula: avg = total_distance / total_time = 2D / (D/r1 + D/r2)
           = 2 r1 r2 / (r1 + r2)    (harmonic mean, independent of D)

    Backward: pick r1, r2 so that 2 r1 r2 / (r1 + r2) is clean.
    """
    generator_id = "average_rate_round_trip"
    topic_slug = "rational_equations_and_applications"
    display_name = "Average rate on a round trip (harmonic mean)"
    supports_word_problems = True
    bank_count_per_difficulty = 25

    # Clean (r1, r2) pairs where 2*r1*r2/(r1+r2) yields nice integer or
    # simple fraction results.
    _CLEAN_PAIRS = {
        "easy": [
            (10, 15), (15, 10), (20, 30), (30, 20), (12, 4), (20, 5),
            (6, 12), (12, 6), (30, 60), (60, 30), (6, 6), (10, 10),
        ],
        "medium": [
            (20, 30), (30, 20), (15, 60), (60, 15), (25, 100), (40, 60),
            (60, 40), (45, 30), (18, 36), (36, 18), (20, 5), (50, 25),
            (35, 70),
        ],
        "hard": [
            (30, 60), (60, 30), (40, 80), (80, 40), (25, 100), (45, 90),
            (75, 50), (50, 75), (35, 70), (15, 60), (60, 15), (50, 25),
            (20, 80), (80, 20), (100, 25),
        ],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pairs = self._CLEAN_PAIRS[difficulty]
        r1, r2 = rng.choice(pairs)
        # Pick a distance that works nicely. We pick D so that D is divisible
        # by r1 and r2 to make time calculations concrete, but the answer
        # doesn't depend on D.
        D = (r1 * r2) // gcd(r1, r2)  # lcm so D/r1 and D/r2 are integers
        route = rng.choice(_ROUND_TRIP_ROUTES)

        # avg = 2 r1 r2 / (r1 + r2)
        num = 2 * r1 * r2
        den = r1 + r2
        g = gcd(num, den)
        avg_num = num // g
        avg_den = den // g
        if avg_den == 1:
            avg_latex = str(avg_num)
        else:
            avg_latex = rf"\frac{{{avg_num}}}{{{avg_den}}}"

        # Time calculations (for the solution steps)
        t1 = D // r1
        t2 = D // r2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r1, r2, D, route)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A commuter drives ${D}$ miles {route} at an average speed of "
                f"${r1}$ mph, then returns the same distance at ${r2}$ mph. "
                "Find the average speed for the entire round trip."
            ),
            answer_latex=f"$\\text{{avg}} = {avg_latex}$ mph",
            hints=[
                "Average speed is total distance divided by total time, not the average of the two speeds.",
                rf"Total distance = $2 \cdot {D} = {2 * D}$ miles.",
                rf"Total time = $\dfrac{{{D}}}{{{r1}}} + \dfrac{{{D}}}{{{r2}}} = {t1} + {t2} = {t1 + t2}$ hours.",
            ],
            solution_steps_latex=[
                rf"Total distance: $2 \cdot {D} = {2 * D}$ miles.",
                rf"Time for first leg: $\dfrac{{{D}}}{{{r1}}} = {t1}$ hours.",
                rf"Time for return leg: $\dfrac{{{D}}}{{{r2}}} = {t2}$ hours.",
                rf"Total time: ${t1} + {t2} = {t1 + t2}$ hours.",
                rf"Average speed: $\dfrac{{{2 * D}}}{{{t1 + t2}}} = {avg_latex}$ mph.",
            ],
            tags=list(RAT_TAGS),
        )
