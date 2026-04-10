"""Polynomial arithmetic and factoring generators (Phase 2c Wave 4).

Covers five canonical topic slugs under the algebra branch:

- ``adding_and_subtracting_polynomials``
    - poly_add_like_terms
    - poly_subtract
    - poly_combine_mixed
- ``multiplying_polynomials``
    - poly_monomial_times_polynomial
    - poly_binomial_times_binomial_foil
    - poly_binomial_times_trinomial
- ``special_products``
    - special_product_difference_of_squares
    - special_product_perfect_square_sum
    - special_product_perfect_square_diff
- ``greatest_common_factor``
    - gcf_of_monomials
    - gcf_factor_polynomial
    - gcf_factor_binomial_common
- ``factoring_trinomials_general``
    - factor_general_trinomial_positive_leading
    - factor_general_trinomial_mixed_signs
    - factor_trinomial_with_gcf_first

Every generator uses backward construction: pick the clean answer first, then
assemble the inputs around it. All polynomial arithmetic is delegated to
sympy so multi-term formatting (signs, exponents, ordering) is consistent.
"""
from __future__ import annotations

import math
import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


def _paren_poly(poly_expr) -> str:
    """LaTeX a polynomial wrapped in parentheses."""
    return f"\\left({sp.latex(sp.expand(poly_expr))}\\right)"


def _split_coef(value: int, rng: random.Random, lo: int = -9, hi: int = 9) -> tuple[int, int]:
    """Split ``value`` into two integer summands a + b == value inside [lo, hi]."""
    # Pick a first, then derive b. Clamp so b stays in range too.
    a_lo = max(lo, value - hi)
    a_hi = min(hi, value - lo)
    if a_lo > a_hi:
        # Fallback: just go half/half
        a = value // 2
        return a, value - a
    a = rng.randint(a_lo, a_hi)
    return a, value - a


# ---------------------------------------------------------------------------
# Topic 1: Adding and subtracting polynomials
# ---------------------------------------------------------------------------


@register
class PolyAddLikeTerms(Generator):
    """Add two quadratic polynomials. Backward: pick the sum, split each coefficient."""
    generator_id = "poly_add_like_terms"
    topic_slug = "adding_and_subtracting_polynomials"
    display_name = "Add polynomials (combine like terms)"

    _RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}
    _SPLIT = {"easy": 7, "medium": 12, "hard": 18}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        s = self._SPLIT[difficulty]
        # Backward: pick the answer sum coefficients (a2, a1, a0) in [lo, hi]
        while True:
            a2 = rng.randint(lo, hi)
            a1 = rng.randint(lo, hi)
            a0 = rng.randint(lo, hi)
            if a2 != 0:
                break

        # Split each coefficient into two summands
        p2, q2 = _split_coef(a2, rng, -s, s)
        p1, q1 = _split_coef(a1, rng, -s, s)
        p0, q0 = _split_coef(a0, rng, -s, s)

        poly_p = p2 * x * x + p1 * x + p0
        poly_q = q2 * x * x + q1 * x + q0
        answer = sp.expand(poly_p + poly_q)

        statement = f"{_paren_poly(poly_p)} + {_paren_poly(poly_q)}"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p2, p1, p0, q2, q1, q0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement}$.",
            answer_latex=f"${sp.latex(answer)}$",
            hints=[
                "Drop the parentheses (addition doesn't change any signs) and group like terms.",
                f"The $x^2$ terms: ${p2}x^2 + ({q2})x^2 = {a2}x^2$.",
                f"The $x$ terms: ${p1}x + ({q1})x = {a1}x$. The constants: ${p0} + ({q0}) = {a0}$.",
            ],
            solution_steps_latex=[
                f"Drop the parentheses: ${p2}x^2 + {p1}x + {p0} + {q2}x^2 + {q1}x + {q0}$.",
                "Group like terms: "
                f"$({p2} + {q2})x^2 + ({p1} + {q1})x + ({p0} + {q0})$.",
                f"Simplify each group: ${sp.latex(answer)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class PolySubtract(Generator):
    """Subtract two polynomials, distributing the minus sign. Backward construction."""
    generator_id = "poly_subtract"
    topic_slug = "adding_and_subtracting_polynomials"
    display_name = "Subtract polynomials"

    _RANGES = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-20, 20)}
    _SPLIT = {"easy": 6, "medium": 11, "hard": 16}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        s = self._SPLIT[difficulty]
        # Answer coefficients
        while True:
            d2 = rng.randint(lo, hi)
            d1 = rng.randint(lo, hi)
            d0 = rng.randint(lo, hi)
            if d2 != 0:
                break
        # poly_a - poly_b = answer
        # Choose poly_b freely, then poly_a = poly_b + answer.
        b2 = rng.randint(-s, s)
        b1 = rng.randint(-s, s)
        b0 = rng.randint(-s, s)
        a2 = d2 + b2
        a1 = d1 + b1
        a0 = d0 + b0

        poly_a = a2 * x * x + a1 * x + a0
        poly_b = b2 * x * x + b1 * x + b0
        answer = sp.expand(poly_a - poly_b)

        statement = f"{_paren_poly(poly_a)} - {_paren_poly(poly_b)}"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a2, a1, a0, b2, b1, b0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement}$.",
            answer_latex=f"${sp.latex(answer)}$",
            hints=[
                "Distribute the minus sign to **every** term of the second polynomial. The sign of each term flips.",
                f"After distributing: ${a2}x^2 + {a1}x + {a0} - {b2}x^2 - ({b1})x - ({b0})$.",
                "Then group and combine like terms.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                f"Distribute $-1$ across the second polynomial: "
                f"${a2}x^2 + {a1}x + {a0} + ({-b2})x^2 + ({-b1})x + ({-b0})$.",
                "Combine like terms: "
                f"$({a2} + ({-b2}))x^2 + ({a1} + ({-b1}))x + ({a0} + ({-b0}))$.",
                f"Simplify: ${sp.latex(answer)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class PolyCombineMixed(Generator):
    """Three polynomials with mixed + and - between them."""
    generator_id = "poly_combine_mixed"
    topic_slug = "adding_and_subtracting_polynomials"
    display_name = "Combine polynomials with mixed signs"

    _RANGE = {"easy": 6, "medium": 10, "hard": 15}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGE[difficulty]
        # Three polynomials, each quadratic or linear
        def rand_poly():
            return (rng.randint(-r, r), rng.randint(-r, r), rng.randint(-r, r))

        coefs_a = rand_poly()
        coefs_b = rand_poly()
        coefs_c = rand_poly()
        # Ensure at least one x^2 term so the result is non-trivial
        if coefs_a[0] == 0 and coefs_b[0] == 0 and coefs_c[0] == 0:
            coefs_a = (rng.choice([-3, -2, -1, 1, 2, 3]), coefs_a[1], coefs_a[2])

        poly_a = coefs_a[0] * x * x + coefs_a[1] * x + coefs_a[2]
        poly_b = coefs_b[0] * x * x + coefs_b[1] * x + coefs_b[2]
        poly_c = coefs_c[0] * x * x + coefs_c[1] * x + coefs_c[2]
        answer = sp.expand(poly_a - poly_b + poly_c)

        statement = f"{_paren_poly(poly_a)} - {_paren_poly(poly_b)} + {_paren_poly(poly_c)}"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (*coefs_a, *coefs_b, *coefs_c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement}$.",
            answer_latex=f"${sp.latex(answer)}$",
            hints=[
                "Keep the leading sign of each group: ${+}$, ${-}$, ${+}$. Distribute the middle minus sign to every term inside its parentheses.",
                "Then group by degree and add coefficients.",
                f"The $x^2$ coefficient becomes $({coefs_a[0]}) - ({coefs_b[0]}) + ({coefs_c[0]})$.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                "Distribute the signs in front of each parenthesis (the middle one flips every term):",
                f"${sp.latex(sp.expand(poly_a))} + {sp.latex(-sp.expand(poly_b))} + {sp.latex(sp.expand(poly_c))}$.",
                "Group like terms and combine: "
                f"${sp.latex(answer)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------
# Topic 2: Multiplying polynomials
# ---------------------------------------------------------------------------


@register
class PolyMonomialTimesPolynomial(Generator):
    """Distribute a monomial across a polynomial: k*x^n * (polynomial)."""
    generator_id = "poly_monomial_times_polynomial"
    topic_slug = "multiplying_polynomials"
    display_name = "Distribute a monomial over a polynomial"

    _RANGE = {"easy": (2, 6), "medium": (2, 9), "hard": (2, 12)}
    _INNER = {"easy": 6, "medium": 10, "hard": 15}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._RANGE[difficulty]
        inner = self._INNER[difficulty]
        k = rng.choice([-1, 1]) * rng.randint(k_lo, k_hi)
        n = rng.randint(1, 3)  # monomial degree
        # Inner polynomial: 2 or 3 non-zero terms
        inner_deg = rng.choice([2, 3])
        coefs: list[int] = []
        for _ in range(inner_deg + 1):
            c = rng.randint(-inner, inner)
            coefs.append(c)
        # Ensure the leading inner coefficient is non-zero
        if coefs[0] == 0:
            coefs[0] = rng.choice([-3, -2, 2, 3])

        inner_poly = sum(c * x ** (inner_deg - i) for i, c in enumerate(coefs))
        monomial = k * x ** n
        product = sp.expand(monomial * inner_poly)

        mono_latex = sp.latex(monomial)
        statement = f"{mono_latex} \\cdot \\left({sp.latex(sp.expand(inner_poly))}\\right)"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, n, tuple(coefs))),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Expand ${statement}$.",
            answer_latex=f"${sp.latex(product)}$",
            hints=[
                "Use the **distributive property**: multiply the monomial by every term inside the parentheses.",
                "When multiplying powers of $x$, add the exponents: $x^a \\cdot x^b = x^{a+b}$.",
                f"Multiply ${mono_latex}$ into each term separately, then collect the results.",
            ],
            solution_steps_latex=[
                f"Distribute ${mono_latex}$ across each term:",
                " + ".join(
                    f"\\left({mono_latex}\\right)\\left({sp.latex(c * x ** (inner_deg - i))}\\right)"
                    for i, c in enumerate(coefs)
                    if c != 0
                ) + ".",
                f"Simplify each product and combine: ${sp.latex(product)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class PolyBinomialTimesBinomialFOIL(Generator):
    """FOIL: (ax + b)(cx + d). Backward: pick (a, b, c, d), multiply out."""
    generator_id = "poly_binomial_times_binomial_foil"
    topic_slug = "multiplying_polynomials"
    display_name = "Multiply (ax + b)(cx + d) using FOIL"

    _COEF = {"easy": (1, 6), "medium": (1, 9), "hard": (1, 12)}
    _CONST = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEF[difficulty]
        k_lo, k_hi = self._CONST[difficulty]
        a = rng.randint(c_lo, c_hi) * rng.choice([-1, 1])
        c = rng.randint(c_lo, c_hi) * rng.choice([-1, 1])
        b = rng.randint(k_lo, k_hi)
        d = rng.randint(k_lo, k_hi)
        while b == 0 and d == 0:
            b = rng.randint(k_lo, k_hi)

        f1 = a * x + b
        f2 = c * x + d
        product = sp.expand(f1 * f2)

        first = a * c
        outer = a * d
        inner = b * c
        last = b * d
        middle = outer + inner

        statement = f"{_paren_poly(f1)}{_paren_poly(f2)}"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Expand ${statement}$.",
            answer_latex=f"${sp.latex(product)}$",
            hints=[
                r"Use **FOIL**: **F**irst, **O**uter, **I**nner, **L**ast.",
                f"First: $({a}x)({c}x) = {first}x^2$. Outer: $({a}x)({d}) = {outer}x$. "
                f"Inner: $({b})({c}x) = {inner}x$. Last: $({b})({d}) = {last}$.",
                f"Combine the two middle $x$ terms: ${outer}x + {inner}x = {middle}x$.",
            ],
            solution_steps_latex=[
                f"Apply FOIL to ${statement}$.",
                f"First: $({a}x)({c}x) = {first}x^2$.",
                f"Outer: $({a}x)({d}) = {outer}x$.",
                f"Inner: $({b})({c}x) = {inner}x$.",
                f"Last: $({b})({d}) = {last}$.",
                f"Combine the middle terms and simplify: ${sp.latex(product)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class PolyBinomialTimesTrinomial(Generator):
    """(x + a)(x^2 + bx + c) — distribute across all 6 pairs."""
    generator_id = "poly_binomial_times_trinomial"
    topic_slug = "multiplying_polynomials"
    display_name = "Multiply (x + a)(x^2 + bx + c)"

    _RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        a = rng.randint(lo, hi)
        while a == 0:
            a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        while c == 0 and b == 0:
            c = rng.randint(lo, hi)

        binom = x + a
        trinom = x ** 2 + b * x + c
        product = sp.expand(binom * trinom)

        statement = f"{_paren_poly(binom)}{_paren_poly(trinom)}"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Expand ${statement}$.",
            answer_latex=f"${sp.latex(product)}$",
            hints=[
                "Distribute every term of the binomial across every term of the trinomial. That gives $2 \\cdot 3 = 6$ products.",
                f"From the $x$ part: $x \\cdot (x^2 + {b}x + {c}) = x^3 + {b}x^2 + {c}x$.",
                f"From the $({a})$ part: ${a}(x^2 + {b}x + {c}) = {a}x^2 + {a * b}x + {a * c}$.",
            ],
            solution_steps_latex=[
                f"Multiply each term of $(x + {a})$ by each term of $(x^2 + {b}x + {c})$.",
                f"$x \\cdot x^2 = x^3$, $\\;x \\cdot {b}x = {b}x^2$, $\\;x \\cdot {c} = {c}x$.",
                f"$({a}) \\cdot x^2 = {a}x^2$, $\\;({a}) \\cdot {b}x = {a * b}x$, $\\;({a}) \\cdot {c} = {a * c}$.",
                "Add all six results and combine like terms: "
                f"${sp.latex(product)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------
# Topic 3: Special products
# ---------------------------------------------------------------------------


@register
class SpecialProductDifferenceOfSquares(Generator):
    """Expand (ax + b)(ax - b) = a^2 x^2 - b^2. Backward construction."""
    generator_id = "special_product_difference_of_squares"
    topic_slug = "special_products"
    display_name = "Expand (ax + b)(ax - b)"

    _A = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _B = {"easy": (1, 9), "medium": (1, 14), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        b_lo, b_hi = self._B[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        lhs = (a * x + b) * (a * x - b)
        product = sp.expand(lhs)

        statement = f"\\left({a}x + {b}\\right)\\left({a}x - {b}\\right)"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Expand ${statement}$.",
            answer_latex=f"${sp.latex(product)}$",
            hints=[
                r"Use the **difference of squares** pattern: $(p + q)(p - q) = p^2 - q^2$.",
                f"Here $p = {a}x$ and $q = {b}$.",
                f"So $p^2 = {a * a}x^2$ and $q^2 = {b * b}$.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $(p + q)(p - q) = p^2 - q^2$.",
                f"Identify $p = {a}x$ and $q = {b}$.",
                f"Compute $p^2 = ({a}x)^2 = {a * a}x^2$ and $q^2 = {b}^2 = {b * b}$.",
                f"Write the difference: ${sp.latex(product)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class SpecialProductPerfectSquareSum(Generator):
    """Expand (ax + b)^2 = a^2 x^2 + 2ab x + b^2."""
    generator_id = "special_product_perfect_square_sum"
    topic_slug = "special_products"
    display_name = "Expand (ax + b)^2"

    _A = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _B = {"easy": (1, 9), "medium": (1, 13), "hard": (1, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        b_lo, b_hi = self._B[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        lhs = (a * x + b) ** 2
        product = sp.expand(lhs)

        statement = f"\\left({a}x + {b}\\right)^2"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Expand ${statement}$.",
            answer_latex=f"${sp.latex(product)}$",
            hints=[
                r"Use the **perfect square** pattern: $(p + q)^2 = p^2 + 2pq + q^2$.",
                f"Here $p = {a}x$ and $q = {b}$.",
                f"The middle term is $2pq = 2 \\cdot {a}x \\cdot {b} = {2 * a * b}x$.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $(p + q)^2 = p^2 + 2pq + q^2$.",
                f"Identify $p = {a}x$ and $q = {b}$.",
                f"Compute $p^2 = {a * a}x^2$, $\\; 2pq = {2 * a * b}x$, $\\; q^2 = {b * b}$.",
                f"Write the expansion: ${sp.latex(product)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class SpecialProductPerfectSquareDiff(Generator):
    """Expand (ax - b)^2 = a^2 x^2 - 2ab x + b^2."""
    generator_id = "special_product_perfect_square_diff"
    topic_slug = "special_products"
    display_name = "Expand (ax - b)^2"

    _A = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _B = {"easy": (1, 9), "medium": (1, 13), "hard": (1, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        b_lo, b_hi = self._B[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        lhs = (a * x - b) ** 2
        product = sp.expand(lhs)

        statement = f"\\left({a}x - {b}\\right)^2"
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Expand ${statement}$.",
            answer_latex=f"${sp.latex(product)}$",
            hints=[
                r"Use the **perfect square difference** pattern: $(p - q)^2 = p^2 - 2pq + q^2$.",
                f"Here $p = {a}x$ and $q = {b}$. Notice the middle term is **negative**.",
                f"The middle term is $-2pq = -2 \\cdot {a}x \\cdot {b} = {-2 * a * b}x$.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $(p - q)^2 = p^2 - 2pq + q^2$.",
                f"Identify $p = {a}x$ and $q = {b}$.",
                f"Compute $p^2 = {a * a}x^2$, $\\; -2pq = {-2 * a * b}x$, $\\; q^2 = {b * b}$.",
                f"Write the expansion: ${sp.latex(product)}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------
# Topic 4: Greatest common factor
# ---------------------------------------------------------------------------


def _fmt_monomial(coef: int, xexp: int, yexp: int) -> str:
    """Format a monomial like 12 x^3 y^2 in LaTeX."""
    parts: list[str] = []
    if coef == 1 and (xexp > 0 or yexp > 0):
        pass
    elif coef == -1 and (xexp > 0 or yexp > 0):
        parts.append("-")
    else:
        parts.append(str(coef))
    if xexp > 0:
        parts.append("x" if xexp == 1 else f"x^{{{xexp}}}")
    if yexp > 0:
        parts.append("y" if yexp == 1 else f"y^{{{yexp}}}")
    if not parts:
        return "1"
    return "".join(parts)


@register
class GCFOfMonomials(Generator):
    """Find the GCF of 2 or 3 monomials. Backward: pick GCF, multiply by extras."""
    generator_id = "gcf_of_monomials"
    topic_slug = "greatest_common_factor"
    display_name = "Find the GCF of monomials"

    _COEF = {"easy": (1, 7), "medium": (1, 11), "hard": (2, 14)}
    _EXTRA = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEF[difficulty]
        e_lo, e_hi = self._EXTRA[difficulty]
        # Pick GCF coefficient + exponents
        gcf_c = rng.randint(c_lo, c_hi)
        gcf_x = rng.randint(1, 3)
        gcf_y = rng.randint(0, 2)

        # Two or three monomials, each = gcf * extra, where extras are coprime pairwise
        n_monos = rng.choice([2, 3])
        monos = []
        extras: list[tuple[int, int, int]] = []
        for i in range(n_monos):
            while True:
                ec = rng.randint(e_lo, e_hi)
                ex = rng.randint(0, 2)
                ey = rng.randint(0, 1)
                # Avoid accidentally sharing a factor across all extras.
                extras.append((ec, ex, ey))
                # Check the pairwise gcds across extras so the overall GCF stays as chosen.
                coef_gcd = 0
                for (c, _, _) in extras:
                    coef_gcd = math.gcd(coef_gcd, c)
                if coef_gcd == 1 or len(extras) < 2:
                    # For the first mono we can't yet enforce the pairwise property;
                    # allow it and rely on later monomials to knock it down.
                    break
                extras.pop()  # try again
            ec, ex, ey = extras[-1]
            mc = gcf_c * ec
            mx = gcf_x + ex
            my = gcf_y + ey
            monos.append((mc, mx, my))

        # If the first mono's extra didn't get paired with a knock-down later,
        # force the last extra coefficient to be coprime with the first.
        while True:
            g = 0
            for (c, _, _) in extras:
                g = math.gcd(g, c)
            if g == 1:
                break
            # Bump the last extra coef by +1 until gcd becomes 1
            c, ex, ey = extras[-1]
            extras[-1] = (c + 1, ex, ey)
            monos[-1] = (gcf_c * (c + 1), gcf_x + ex, gcf_y + ey)

        gcf_latex = _fmt_monomial(gcf_c, gcf_x, gcf_y)
        mono_latex = [_fmt_monomial(*m) for m in monos]

        param_tuple = (gcf_c, gcf_x, gcf_y, tuple(monos))
        return Problem(
            id=make_problem_id(self.generator_id, difficulty, param_tuple),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find the greatest common factor of ${', \\; '.join(mono_latex)}$.",
            answer_latex=f"${gcf_latex}$",
            hints=[
                "The GCF of monomials is the largest monomial that divides each one. Find it piece by piece: the numeric GCF of the coefficients, then the lowest power of each variable that appears in every term.",
                f"Coefficients: find $\\gcd$ of ${', '.join(str(m[0]) for m in monos)}$.",
                f"Variables: take the lowest power of $x$ across all terms, then the lowest power of $y$.",
            ],
            solution_steps_latex=[
                f"Numeric GCF of ${', '.join(str(m[0]) for m in monos)}$ is ${gcf_c}$.",
                f"Lowest power of $x$ across the terms: $x^{{{gcf_x}}}$.",
                f"Lowest power of $y$ across the terms: "
                + (f"$y^{{{gcf_y}}}$." if gcf_y > 0 else "$y^0 = 1$ (no $y$ in the GCF)."),
                f"Combine: ${gcf_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class GCFFactorPolynomial(Generator):
    """Factor the GCF out of a polynomial. Backward: pick GCF and remainder, multiply."""
    generator_id = "gcf_factor_polynomial"
    topic_slug = "greatest_common_factor"
    display_name = "Factor the GCF from a polynomial"

    _GCF_COEF = {"easy": (2, 6), "medium": (2, 9), "hard": (2, 12)}
    _INNER = {"easy": (1, 7), "medium": (1, 11), "hard": (1, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        g_lo, g_hi = self._GCF_COEF[difficulty]
        i_lo, i_hi = self._INNER[difficulty]
        gcf_c = rng.randint(g_lo, g_hi)
        gcf_x = rng.randint(1, 2)
        # Inner polynomial coefficients, pairwise coprime with each other
        while True:
            a = rng.randint(i_lo, i_hi) * rng.choice([-1, 1])
            b = rng.randint(i_lo, i_hi) * rng.choice([-1, 1])
            c = rng.randint(i_lo, i_hi) * rng.choice([-1, 1])
            if a != 0 and math.gcd(math.gcd(abs(a), abs(b)), abs(c)) == 1:
                break

        gcf = gcf_c * x ** gcf_x
        inner = a * x ** 2 + b * x + c
        poly = sp.expand(gcf * inner)

        gcf_latex = sp.latex(gcf)
        inner_latex = sp.latex(inner)
        poly_latex = sp.latex(poly)
        answer = f"{gcf_latex}\\left({inner_latex}\\right)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (gcf_c, gcf_x, a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the GCF out of ${poly_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                "First find the GCF of the coefficients, then take the lowest power of $x$ that appears in every term.",
                f"The numeric GCF of the coefficients is ${gcf_c}$; the lowest power of $x$ is $x^{{{gcf_x}}}$.",
                f"Divide every term by ${gcf_latex}$ to get the polynomial that goes inside the parentheses.",
            ],
            solution_steps_latex=[
                f"Identify the GCF: ${gcf_latex}$.",
                f"Divide each term of ${poly_latex}$ by ${gcf_latex}$: "
                f"${sp.latex(sp.expand(poly / gcf))}$.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class GCFFactorBinomialCommon(Generator):
    """Factor out a common binomial factor. e.g., 3(x-5) + 2x(x-5) = (x-5)(3 + 2x)."""
    generator_id = "gcf_factor_binomial_common"
    topic_slug = "greatest_common_factor"
    display_name = "Factor out a common binomial"

    _RANGE = {"easy": (1, 7), "medium": (1, 10), "hard": (1, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        # The shared binomial (x - k) or (x + k)
        k = rng.randint(lo, hi) * rng.choice([-1, 1])
        # First coefficient (constant) and second coefficient (linear ax)
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi) * rng.choice([-1, 1])
        while b == 0:
            b = rng.randint(lo, hi) * rng.choice([-1, 1])

        binom = x + k  # sympy will render with the right sign
        # Expression: a * binom + b*x * binom  =>  (binom)(a + b*x)
        term_a_latex = f"{a}{_paren_poly(binom)}"
        term_b_expr = b * x
        term_b_latex = f"{sp.latex(term_b_expr)}{_paren_poly(binom)}"

        expr_latex = f"{term_a_latex} + {term_b_latex}"
        factored_inner = sp.expand(a + b * x)
        answer = f"{_paren_poly(binom)}\\left({sp.latex(factored_inner)}\\right)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor ${expr_latex}$ by pulling out the common binomial.",
            answer_latex=f"${answer}$",
            hints=[
                f"Both terms share the binomial factor ${_paren_poly(binom)}$. Treat the binomial as a single unit and factor it out.",
                f"After removing ${_paren_poly(binom)}$, the first term leaves behind ${a}$ and the second leaves behind ${sp.latex(term_b_expr)}$.",
                f"Combine the leftover pieces inside new parentheses.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                f"Notice that ${_paren_poly(binom)}$ is a common factor in both terms.",
                f"Factor it out: ${_paren_poly(binom)}\\left({a} + {sp.latex(term_b_expr)}\\right)$.",
                f"Simplify the second factor: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------
# Topic 5: Factoring general trinomials (leading coefficient > 1)
# ---------------------------------------------------------------------------


@register
class FactorGeneralTrinomialPositiveLeading(Generator):
    """Factor ax^2 + bx + c, a > 1, integer factorization. Backward from (px+q)(rx+s)."""
    generator_id = "factor_general_trinomial_positive_leading"
    topic_slug = "factoring_trinomials_general"
    display_name = "Factor ax^2 + bx + c (a > 1)"

    _A = {"easy": (2, 3), "medium": (2, 4), "hard": (2, 5)}
    _CONST = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        k_lo, k_hi = self._CONST[difficulty]
        # Pick (px + q)(rx + s) with p*r = a (a ≤ 5), q, s both positive (so b, c positive)
        while True:
            p = rng.randint(1, a_hi)
            r = rng.randint(1, a_hi)
            a_val = p * r
            if a_lo <= a_val <= a_hi:
                break
        q = rng.randint(k_lo, k_hi)
        s = rng.randint(k_lo, k_hi)

        f1 = p * x + q
        f2 = r * x + s
        trinomial = sp.expand(f1 * f2)
        a = p * r
        b = p * s + q * r
        c = q * s

        trin_latex = sp.latex(trinomial)
        answer = f"{_paren_poly(f1)}{_paren_poly(f2)}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q, r, s)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the trinomial ${trin_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Use the **AC method**. Multiply $a$ and $c$, then find two numbers whose product is $ac$ and whose sum is $b$.",
                f"Here $a = {a}$, $b = {b}$, $c = {c}$, so $ac = {a * c}$. Find two numbers with product ${a * c}$ and sum ${b}$.",
                f"Those numbers are ${p * s}$ and ${q * r}$. Rewrite $b x$ using them, then factor by grouping.",
            ],
            solution_steps_latex=[
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Compute $ac = {a * c}$. Two numbers with product ${a * c}$ and sum ${b}$: ${p * s}$ and ${q * r}$.",
                f"Rewrite the middle term: ${a}x^2 + {p * s}x + {q * r}x + {c}$.",
                f"Group and factor: ${p}x({r}x + {s}) + {q}({r}x + {s}) = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class FactorGeneralTrinomialMixedSigns(Generator):
    """Factor ax^2 + bx + c with c < 0 (mixed signs inside factors)."""
    generator_id = "factor_general_trinomial_mixed_signs"
    topic_slug = "factoring_trinomials_general"
    display_name = "Factor ax^2 + bx + c with c negative"

    _A = {"easy": (2, 3), "medium": (2, 4), "hard": (2, 5)}
    _CONST = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 11)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        k_lo, k_hi = self._CONST[difficulty]
        while True:
            p = rng.randint(1, a_hi)
            r = rng.randint(1, a_hi)
            if a_lo <= p * r <= a_hi:
                break
        q = rng.randint(k_lo, k_hi)
        s = rng.randint(k_lo, k_hi)
        # Force mixed signs so c = q * s is negative
        if rng.random() < 0.5:
            q = -q
        else:
            s = -s

        f1 = p * x + q
        f2 = r * x + s
        trinomial = sp.expand(f1 * f2)
        a = p * r
        b = p * s + q * r
        c = q * s
        # Guard: avoid degenerate b == 0 (would look like difference of squares)
        if b == 0:
            # Nudge q by 1 to break symmetry
            q = q + 1 if q >= 0 else q - 1
            f1 = p * x + q
            trinomial = sp.expand(f1 * f2)
            a = p * r
            b = p * s + q * r
            c = q * s

        trin_latex = sp.latex(trinomial)
        answer = f"{_paren_poly(f1)}{_paren_poly(f2)}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q, r, s)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the trinomial ${trin_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Use the **AC method**. Because $c$ is negative, the two factors will have **opposite signs**.",
                f"Here $a = {a}$, $b = {b}$, $c = {c}$. Compute $ac = {a * c}$.",
                f"Find two numbers whose product is ${a * c}$ and whose sum is ${b}$: ${p * s}$ and ${q * r}$.",
            ],
            solution_steps_latex=[
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$. Since $c < 0$, the factors will have opposite signs.",
                f"Compute $ac = {a * c}$. Two numbers with product ${a * c}$ and sum ${b}$: ${p * s}$ and ${q * r}$.",
                f"Rewrite the middle term and factor by grouping to get ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )


@register
class FactorTrinomialWithGCFFirst(Generator):
    """Factor ax^2 + bx + c where an integer GCF can be pulled first."""
    generator_id = "factor_trinomial_with_gcf_first"
    topic_slug = "factoring_trinomials_general"
    display_name = "Factor out a GCF, then a trinomial"

    _G = {"easy": (2, 4), "medium": (2, 6), "hard": (2, 8)}
    _INNER_A = {"easy": (2, 3), "medium": (2, 4), "hard": (2, 5)}
    _CONST = {"easy": (1, 5), "medium": (1, 7), "hard": (1, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        g_lo, g_hi = self._G[difficulty]
        a_lo, a_hi = self._INNER_A[difficulty]
        k_lo, k_hi = self._CONST[difficulty]
        # Pick inner factors (px + q)(rx + s) with coprime outer coefficients
        while True:
            p = rng.randint(1, a_hi)
            r = rng.randint(1, a_hi)
            if a_lo <= p * r <= a_hi:
                break
        q = rng.randint(k_lo, k_hi)
        s = rng.randint(k_lo, k_hi)
        g = rng.randint(g_lo, g_hi)

        f1 = p * x + q
        f2 = r * x + s
        inner_trinomial = sp.expand(f1 * f2)
        trinomial = sp.expand(g * inner_trinomial)

        a = g * p * r
        b = g * (p * s + q * r)
        c = g * q * s

        trin_latex = sp.latex(trinomial)
        inner_latex = sp.latex(inner_trinomial)
        answer = f"{g}{_paren_poly(f1)}{_paren_poly(f2)}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (g, p, q, r, s)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor completely: ${trin_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                "Always look for a GCF first. Check whether an integer divides every coefficient.",
                f"Here all three coefficients (${a}, {b}, {c}$) share the factor ${g}$. Pull it out.",
                f"That leaves ${g}\\left({inner_latex}\\right)$. Now factor the trinomial inside.",
            ],
            solution_steps_latex=[
                f"Check for a GCF among ${a}$, ${b}$, and ${c}$. The GCF is ${g}$.",
                f"Factor it out: ${g}\\left({inner_latex}\\right)$.",
                f"Factor the inner trinomial using the AC method: $\\left({inner_latex}\\right) = {_paren_poly(f1)}{_paren_poly(f2)}$.",
                f"Write the fully factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-polynomials", "#skill-algebraic-manipulation"],
        )
