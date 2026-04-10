"""Quadratics methods generators (Phase 2c Wave 4).

Five related topics covered in one module:

- factoring_special_forms
    - factor_difference_of_squares_general: a^2 x^2 - b^2 -> (ax+b)(ax-b)
    - factor_perfect_square_trinomial_sum:  a^2 x^2 + 2abx + b^2 -> (ax+b)^2
    - factor_perfect_square_trinomial_diff: a^2 x^2 - 2abx + b^2 -> (ax-b)^2

- factoring_completely
    - factor_completely_gcf_then_dos:       k*x*(x^2 - m^2) style
    - factor_completely_gcf_then_trinomial: k*(x-p)*(x-q) style
    - factor_by_grouping_4_terms:           (Ax+B)(x^2+D) style

- solving_quadratics_by_factoring
    - solve_quadratic_by_factoring_simple:     x^2 + bx + c = 0, integer roots
    - solve_quadratic_by_factoring_rearranged: x^2 + bx = c, rearrange first
    - solve_quadratic_by_factoring_gcf:        ax^2 + bx = 0, factor out x

- solving_quadratics_by_square_roots
    - solve_x_squared_equals_k:        x^2 = k (k a perfect square)
    - solve_binomial_squared_equals_k: (x - h)^2 = k
    - solve_quadratic_to_square_form:  ax^2 - c = 0 -> x^2 = c/a

- completing_the_square
    - complete_square_leading_one:  x^2 + bx + c = 0, leading coefficient 1
    - complete_square_integer_k:    same, but answers come out as clean integers
    - complete_square_with_a:       ax^2 + bx + c = 0, a in {2, 3}
"""
from __future__ import annotations

import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


# ---------------------------------------------------------------------------
# Local formatting helpers
# ---------------------------------------------------------------------------

def _sign_term(coef: int, var: str = "x") -> str:
    """Format a signed polynomial term like '- 3x' or '+ 12'. Never includes sign at start."""
    if coef >= 0:
        return f"+ {coef}{var}" if var else f"+ {coef}"
    return f"- {abs(coef)}{var}" if var else f"- {abs(coef)}"


def _format_factored_linear(a: int, k: int) -> str:
    """Return LaTeX for (ax +/- k) with correct signs, using 1 implicit coefficient."""
    coef = "" if a == 1 else str(a)
    if k >= 0:
        return f"({coef}x + {k})"
    return f"({coef}x - {abs(k)})"


def _format_pm_int(base: int, radicand: int) -> str:
    """Render 'base ± sqrt(radicand)' as LaTeX. If radicand is a perfect square,
    simplify."""
    r = sp.sqrt(radicand)
    return f"{base} \\pm {sp.latex(r)}"


# ===========================================================================
# Topic 1: factoring_special_forms
# ===========================================================================

@register
class FactorDifferenceOfSquaresGeneral(Generator):
    """Factor a^2 x^2 - b^2 as (ax + b)(ax - b).

    Backward construction: pick a, b, then the quadratic is a^2 x^2 - b^2.
    """
    generator_id = "factor_difference_of_squares_general"
    topic_slug = "factoring_special_forms"
    display_name = "Factor a difference of squares (general form)"

    _A_RANGE = {"easy": (1, 4), "medium": (1, 7), "hard": (1, 12)}
    _B_RANGE = {"easy": (2, 10), "medium": (2, 15), "hard": (2, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)
        # Quadratic: (ax)^2 - b^2
        expr = (a * x) ** 2 - b * b
        expr_latex = sp.latex(sp.expand(expr))
        answer = f"({a}x + {b})({a}x - {b})" if a != 1 else f"(x + {b})(x - {b})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"This is a **difference of squares**: $A^2 - B^2 = (A + B)(A - B)$.",
                f"Identify $A^2 = {a * a}x^2$, so $A = {a}x$. And $B^2 = {b * b}$, so $B = {b}$.",
                f"Substitute into the pattern: $(A + B)(A - B) = ({a}x + {b})({a}x - {b})$.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $A^2 - B^2 = (A + B)(A - B)$.",
                f"Identify $A$: $A^2 = {a * a}x^2$, so $A = {a}x$.",
                f"Identify $B$: $B^2 = {b * b}$, so $B = {b}$.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class FactorPerfectSquareTrinomialSum(Generator):
    """Factor a^2 x^2 + 2abx + b^2 as (ax + b)^2.

    Backward construction: pick a, b, compute the trinomial.
    """
    generator_id = "factor_perfect_square_trinomial_sum"
    topic_slug = "factoring_special_forms"
    display_name = "Factor a perfect square trinomial (sum form)"

    _A_RANGE = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 8)}
    _B_RANGE = {"easy": (1, 9), "medium": (1, 14), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)
        # (ax + b)^2 = a^2 x^2 + 2abx + b^2
        poly = (a * x + b) ** 2
        expanded = sp.expand(poly)
        expr_latex = sp.latex(expanded)
        if a == 1:
            answer = f"(x + {b})^2"
        else:
            answer = f"({a}x + {b})^2"
        middle = 2 * a * b
        leading = a * a
        last = b * b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the perfect square trinomial ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"A **perfect square trinomial** has the form $A^2 + 2AB + B^2 = (A + B)^2$.",
                f"Check the first term: ${leading}x^2 = ({a}x)^2$, so $A = {a}x$.",
                f"Check the last term: ${last} = ({b})^2$, so $B = {b}$. Then verify the middle term is $2AB = 2({a}x)({b}) = {middle}x$.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $A^2 + 2AB + B^2 = (A + B)^2$.",
                f"Identify $A$: $A^2 = {leading}x^2$, so $A = {a}x$.",
                f"Identify $B$: $B^2 = {last}$, so $B = {b}$.",
                f"Verify the middle term: $2AB = 2({a}x)({b}) = {middle}x$. It matches.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class FactorPerfectSquareTrinomialDiff(Generator):
    """Factor a^2 x^2 - 2abx + b^2 as (ax - b)^2.

    Backward construction: pick a, b, compute the trinomial.
    """
    generator_id = "factor_perfect_square_trinomial_diff"
    topic_slug = "factoring_special_forms"
    display_name = "Factor a perfect square trinomial (difference form)"

    _A_RANGE = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 8)}
    _B_RANGE = {"easy": (1, 9), "medium": (1, 14), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)
        # (ax - b)^2 = a^2 x^2 - 2abx + b^2
        poly = (a * x - b) ** 2
        expanded = sp.expand(poly)
        expr_latex = sp.latex(expanded)
        if a == 1:
            answer = f"(x - {b})^2"
        else:
            answer = f"({a}x - {b})^2"
        middle = 2 * a * b
        leading = a * a
        last = b * b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor the perfect square trinomial ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"A **perfect square trinomial** has the form $A^2 - 2AB + B^2 = (A - B)^2$.",
                f"Check the first term: ${leading}x^2 = ({a}x)^2$, so $A = {a}x$.",
                f"Check the last term: ${last} = ({b})^2$, so $B = {b}$. Verify the middle term is $-2AB = -2({a}x)({b}) = -{middle}x$.",
            ],
            solution_steps_latex=[
                r"Recognize the pattern $A^2 - 2AB + B^2 = (A - B)^2$.",
                f"Identify $A$: $A^2 = {leading}x^2$, so $A = {a}x$.",
                f"Identify $B$: $B^2 = {last}$, so $B = {b}$.",
                f"Verify the middle term: $-2AB = -2({a}x)({b}) = -{middle}x$. It matches.",
                f"Write the factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 2: factoring_completely
# ===========================================================================

@register
class FactorCompletelyGCFThenDOS(Generator):
    """Factor completely: pull GCF, then difference of squares.

    Like 8x^3 - 32x = 8x(x^2 - 4) = 8x(x + 2)(x - 2).

    Backward: pick GCF g*x, pick difference (x^2 - k^2), multiply out.
    """
    generator_id = "factor_completely_gcf_then_dos"
    topic_slug = "factoring_completely"
    display_name = "Factor completely: GCF, then difference of squares"
    bank_count_per_difficulty = 25

    _G_RANGE = {"easy": (2, 6), "medium": (2, 9), "hard": (2, 14)}
    _K_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        g_lo, g_hi = self._G_RANGE[difficulty]
        k_lo, k_hi = self._K_RANGE[difficulty]
        g = rng.randint(g_lo, g_hi)
        k = rng.randint(k_lo, k_hi)
        # Expression: g*x * (x^2 - k^2) = g*x^3 - g*k^2*x
        expr = g * x * (x * x - k * k)
        expanded = sp.expand(expr)
        expr_latex = sp.latex(expanded)
        answer = f"{g}x(x + {k})(x - {k})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (g, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor completely: ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Always look for a **greatest common factor (GCF)** first.",
                f"The GCF of ${g}x^3$ and ${g * k * k}x$ is ${g}x$. Factor it out: ${g}x(x^2 - {k * k})$.",
                f"The expression in parentheses is a difference of squares: $x^2 - {k * k} = (x + {k})(x - {k})$.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                f"Factor out the GCF ${g}x$: ${g}x(x^2 - {k * k})$.",
                f"Recognize $x^2 - {k * k}$ as a difference of squares: $(x + {k})(x - {k})$.",
                f"Write the fully factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class FactorCompletelyGCFThenTrinomial(Generator):
    """Factor completely: pull GCF, then a simple trinomial.

    Like 3x^2 - 21x + 30 = 3(x - 5)(x - 2).
    """
    generator_id = "factor_completely_gcf_then_trinomial"
    topic_slug = "factoring_completely"
    display_name = "Factor completely: GCF, then trinomial"

    _G_RANGE = {"easy": (2, 5), "medium": (2, 7), "hard": (2, 10)}
    _ROOT_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        g_lo, g_hi = self._G_RANGE[difficulty]
        r_lo, r_hi = self._ROOT_RANGE[difficulty]
        g = rng.randint(g_lo, g_hi)
        # Pick two non-zero, distinct integer roots
        while True:
            p = rng.randint(r_lo, r_hi)
            q = rng.randint(r_lo, r_hi)
            if p != 0 and q != 0 and p != q:
                break
        # g * (x - p) * (x - q) => g*x^2 - g*(p+q)*x + g*p*q
        expr = g * (x - p) * (x - q)
        expanded = sp.expand(expr)
        expr_latex = sp.latex(expanded)

        def _lin(root):
            if root >= 0:
                return f"(x - {root})"
            return f"(x + {abs(root)})"

        answer = f"{g}{_lin(p)}{_lin(q)}"
        inside_b = -(p + q)
        inside_c = p * q
        inside_poly = x * x + inside_b * x + inside_c
        inside_latex = sp.latex(inside_poly)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (g, p, q)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor completely: ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Look for a **greatest common factor (GCF)** first.",
                f"Every term is divisible by ${g}$. Factor it out: ${g}({inside_latex})$.",
                f"Factor the trinomial inside: find two numbers whose product is ${inside_c}$ and whose sum is ${inside_b}$.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                f"Factor out the GCF ${g}$: ${g}({inside_latex})$.",
                f"Factor the trinomial $x^2 + ({inside_b})x + ({inside_c})$ into ${_lin(p)}{_lin(q)}$.",
                f"Write the fully factored form: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class FactorByGrouping4Terms(Generator):
    """Factor a 4-term polynomial by grouping.

    Backward construction: pick factored form (x + m)(A x^2 + B), expand
    to 4 terms, and the student groups back.
    Example:  (x + 2)(x^2 - 3) = x^3 - 3x + 2x^2 - 6 = x^3 + 2x^2 - 3x - 6.
    """
    generator_id = "factor_by_grouping_4_terms"
    topic_slug = "factoring_completely"
    display_name = "Factor by grouping (4 terms)"
    bank_count_per_difficulty = 25

    _M_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _B_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-22, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        # (x + m)(x^2 + B)
        while True:
            m = rng.randint(m_lo, m_hi)
            b = rng.randint(b_lo, b_hi)
            if m != 0 and b != 0:
                break
        factored_expr = (x + m) * (x * x + b)
        expanded = sp.expand(factored_expr)
        expr_latex = sp.latex(expanded)

        def _lin(val, var):
            if val >= 0:
                return f"({var} + {val})"
            return f"({var} - {abs(val)})"

        # The grouping the student does:
        # x^3 + m x^2 + b x + m b
        #   = x^2 (x + m) + b (x + m)
        #   = (x + m)(x^2 + b)
        left_factor = _lin(m, "x")
        right_factor = _lin(b, "x^2")
        answer = f"{left_factor}{right_factor}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Factor by grouping: ${expr_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"**Grouping** works when a 4-term polynomial can be split into two pairs sharing a common binomial factor.",
                r"Group the first two terms and the last two terms: $(x^3 + mx^2) + (bx + mb)$.",
                f"Factor $x^2$ from the first group and ${b}$ from the second group. The remaining $(x + {m})$ should match.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                r"Group in pairs: $(x^3 + " + f"{m}" + r" x^2) + (" + f"{b}" + r" x + " + f"{m * b}" + r")$.",
                f"Factor $x^2$ from the first pair and ${b}$ from the second pair: $x^2{left_factor} + {b}{left_factor}$.",
                f"Factor out the common binomial ${left_factor}$: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 3: solving_quadratics_by_factoring
# ===========================================================================

@register
class SolveQuadraticByFactoringSimple(Generator):
    """Solve x^2 + bx + c = 0 with leading coefficient 1 and integer roots.

    Backward: pick roots p, q; equation is (x - p)(x - q) = 0.
    """
    generator_id = "solve_quadratic_by_factoring_simple"
    topic_slug = "solving_quadratics_by_factoring"
    display_name = "Solve a quadratic by factoring (leading coefficient 1)"

    _RANGES = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        while True:
            p = rng.randint(lo, hi)
            q = rng.randint(lo, hi)
            if p != q:
                break
        # (x - p)(x - q) = x^2 - (p+q)x + pq
        b = -(p + q)
        c = p * q
        poly = x * x + b * x + c
        eq_latex = sp.latex(sp.Eq(poly, 0))

        def _lin(root):
            if root >= 0:
                return f"(x - {root})"
            return f"(x + {abs(root)})"

        factored = f"{_lin(p)}{_lin(q)}"
        roots = sorted([p, q])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ by factoring.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                f"Find two numbers whose product is ${c}$ and whose sum is ${b}$.",
                f"Those two numbers are ${p}$ and ${q}$. Factor as ${factored} = 0$.",
                r"Apply the **Zero Product Property**: if $AB = 0$, then $A = 0$ or $B = 0$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Find two numbers whose product is ${c}$ and whose sum is ${b}$: they are ${p}$ and ${q}$.",
                f"Factor: ${factored} = 0$.",
                f"Apply the Zero Product Property: $x - ({p}) = 0$ or $x - ({q}) = 0$.",
                f"Solve each: $x = {p}$ or $x = {q}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class SolveQuadraticByFactoringRearranged(Generator):
    """Solve a quadratic like x^2 + bx = k that requires rearranging first.

    Backward: pick roots p, q; write x^2 + bx + c = 0 then move c to RHS
    (so the student sees x^2 + bx = -c).
    """
    generator_id = "solve_quadratic_by_factoring_rearranged"
    topic_slug = "solving_quadratics_by_factoring"
    display_name = "Solve a quadratic by factoring (rearrange first)"

    _RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        while True:
            p = rng.randint(lo, hi)
            q = rng.randint(lo, hi)
            # Need c = p*q != 0 so the rearrangement is non-trivial.
            if p != q and p * q != 0:
                break
        b = -(p + q)
        c = p * q
        rhs = -c  # Move c to the other side: x^2 + bx = -c
        lhs_poly = x * x + b * x
        lhs_latex = sp.latex(lhs_poly)
        # LHS might still include "0" for b == 0; skip that edge case
        if b == 0:
            lhs_latex = "x^{2}"
        # Standard-form display
        std_poly = x * x + b * x + c
        std_eq_latex = sp.latex(sp.Eq(std_poly, 0))

        def _lin(root):
            if root >= 0:
                return f"(x - {root})"
            return f"(x + {abs(root)})"

        factored = f"{_lin(p)}{_lin(q)}"
        roots = sorted([p, q])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c, rhs)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${lhs_latex} = {rhs}$ by factoring.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"To factor, first rewrite the equation in **standard form** $ax^2 + bx + c = 0$.",
                f"Subtract ${rhs}$ from both sides to get ${std_eq_latex}$.",
                f"Now factor: find two numbers whose product is ${c}$ and whose sum is ${b}$.",
            ],
            solution_steps_latex=[
                f"Start with ${lhs_latex} = {rhs}$.",
                f"Rewrite in standard form by moving ${rhs}$ to the left: ${std_eq_latex}$.",
                f"Find two numbers with product ${c}$ and sum ${b}$: ${p}$ and ${q}$.",
                f"Factor: ${factored} = 0$.",
                f"Apply the Zero Product Property: $x = {p}$ or $x = {q}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class SolveQuadraticByFactoringGCF(Generator):
    """Solve ax^2 + bx = 0 by factoring out x.

    Always two roots: x = 0 and x = -b/a. Backward construction picks a, b
    with b divisible by a (or a = 1).
    """
    generator_id = "solve_quadratic_by_factoring_gcf"
    topic_slug = "solving_quadratics_by_factoring"
    display_name = "Solve ax^2 + bx = 0 (factor out the GCF)"

    _A_RANGE = {"easy": (1, 4), "medium": (1, 7), "hard": (1, 11)}
    _ROOT_RANGE = {"easy": (-9, 9), "medium": (-15, 15), "hard": (-22, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        r_lo, r_hi = self._ROOT_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        # Pick non-zero integer second root, then b = -a*second_root
        while True:
            second_root = rng.randint(r_lo, r_hi)
            if second_root != 0:
                break
        b = -a * second_root
        poly = a * x * x + b * x
        eq_latex = sp.latex(sp.Eq(poly, 0))
        # Factored form: x * (ax + b) = 0
        if a == 1:
            inside = f"(x{_sign_term(b, '')})"
        else:
            inside = f"({a}x{_sign_term(b, '')})"
        factored = f"x{inside}"
        roots = sorted([0, second_root])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ by factoring.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"Notice the equation has no constant term --- every term contains $x$.",
                f"Factor out the GCF, which is $x$: ${factored} = 0$.",
                r"Apply the **Zero Product Property**: $x = 0$ or the other factor is $0$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Factor out $x$ (the greatest common factor): ${factored} = 0$.",
                f"Set each factor equal to zero: $x = 0$ or ${inside.strip('()')} = 0$.",
                f"Solve the second equation: ${a if a != 1 else ''}x = {-b}$, so $x = {second_root}$.",
                f"The two solutions are $x = {roots[0]}$ and $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 4: solving_quadratics_by_square_roots
# ===========================================================================

@register
class SolveXSquaredEqualsK(Generator):
    """Solve x^2 = k where k is a positive perfect square.

    Answer: x = +/- sqrt(k).
    """
    generator_id = "solve_x_squared_equals_k"
    topic_slug = "solving_quadratics_by_square_roots"
    display_name = "Solve x^2 = k (k a perfect square)"
    bank_count_per_difficulty = 20

    _K_RANGE = {"easy": (2, 12), "medium": (2, 20), "hard": (2, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGE[difficulty]
        root = rng.randint(k_lo, k_hi)
        k = root * root
        eq_latex = f"x^{{2}} = {k}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$.",
            answer_latex=f"$x = {root}$ or $x = -{root}$",
            hints=[
                r"Take the square root of both sides --- remember to include **both** the positive and negative roots.",
                f"$x = \\pm \\sqrt{{{k}}}$, and $\\sqrt{{{k}}} = {root}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Take the square root of both sides: $x = \\pm\\sqrt{{{k}}}$.",
                f"Simplify: $\\sqrt{{{k}}} = {root}$, so $x = \\pm {root}$.",
                f"The two solutions are $x = {root}$ and $x = -{root}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class SolveBinomialSquaredEqualsK(Generator):
    """Solve (x - h)^2 = k where k is a positive perfect square.

    Answer: x = h +/- sqrt(k).
    """
    generator_id = "solve_binomial_squared_equals_k"
    topic_slug = "solving_quadratics_by_square_roots"
    display_name = "Solve (x - h)^2 = k"

    _H_RANGE = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-18, 18)}
    _K_RANGE = {"easy": (2, 10), "medium": (2, 15), "hard": (2, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGE[difficulty]
        k_lo, k_hi = self._K_RANGE[difficulty]
        h = rng.randint(h_lo, h_hi)
        root = rng.randint(k_lo, k_hi)
        k = root * root
        if h >= 0:
            lhs = f"(x - {h})^{{2}}"
        else:
            lhs = f"(x + {abs(h)})^{{2}}"
        eq_latex = f"{lhs} = {k}"
        x1 = h + root
        x2 = h - root
        roots = sorted([x1, x2])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"Take the square root of both sides. Keep the $\pm$ so you capture both branches.",
                f"$x - ({h}) = \\pm\\sqrt{{{k}}} = \\pm {root}$.",
                f"Add ${h}$ to both sides: $x = {h} \\pm {root}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Take the square root of both sides: $x - ({h}) = \\pm\\sqrt{{{k}}}$.",
                f"Simplify: $x - ({h}) = \\pm {root}$.",
                f"Add ${h}$ to both sides: $x = {h} \\pm {root}$.",
                f"The two solutions are $x = {roots[0]}$ and $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class SolveQuadraticToSquareForm(Generator):
    """Solve ax^2 - c = 0 by rearranging to x^2 = c/a then square-rooting.

    Backward: pick small a in {1, 2, 3, 4} and integer root r, then
    c = a * r^2. Guarantees x = +/- r comes out clean.
    """
    generator_id = "solve_quadratic_to_square_form"
    topic_slug = "solving_quadratics_by_square_roots"
    display_name = "Solve ax^2 - c = 0 (rearrange then square root)"

    _A_CHOICES = [1, 2, 3, 4, 5]
    _R_RANGE = {"easy": (2, 8), "medium": (2, 13), "hard": (2, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r_lo, r_hi = self._R_RANGE[difficulty]
        a = rng.choice(self._A_CHOICES)
        r = rng.randint(r_lo, r_hi)
        c = a * r * r  # So ax^2 = c becomes x^2 = r^2
        # Display as ax^2 - c = 0
        poly = a * x * x - c
        eq_latex = sp.latex(sp.Eq(poly, 0))
        # After rearranging
        rhs_after = c
        squared_val = r * r  # x^2 = r^2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$.",
            answer_latex=f"$x = {r}$ or $x = -{r}$",
            hints=[
                r"First isolate $x^2$: move the constant to the other side, then divide by the coefficient of $x^2$.",
                f"Add ${c}$ to both sides: ${a}x^2 = {rhs_after}$.",
                f"Divide both sides by ${a}$: $x^2 = {squared_val}$. Then take square roots.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Add ${c}$ to both sides: ${a}x^2 = {rhs_after}$.",
                f"Divide both sides by ${a}$: $x^2 = {squared_val}$.",
                f"Take the square root of both sides: $x = \\pm\\sqrt{{{squared_val}}} = \\pm {r}$.",
                f"The two solutions are $x = {r}$ and $x = -{r}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 5: completing_the_square
# ===========================================================================

@register
class CompleteSquareLeadingOne(Generator):
    """Solve x^2 + bx + c = 0 by completing the square (leading coefficient 1).

    Backward: pick center h (integer) and square-root value s (small positive
    integer so k = s^2 is a clean perfect square). Answer: x = h +/- s.
    Equation (x - h)^2 = s^2 expands to x^2 - 2hx + (h^2 - s^2) = 0, so
    b = -2h and c = h^2 - s^2.
    """
    generator_id = "complete_square_leading_one"
    topic_slug = "completing_the_square"
    display_name = "Complete the square (leading coefficient 1)"

    _H_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _S_RANGE = {"easy": (2, 6), "medium": (2, 9), "hard": (2, 13)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGE[difficulty]
        s_lo, s_hi = self._S_RANGE[difficulty]
        h = rng.randint(h_lo, h_hi)
        s = rng.randint(s_lo, s_hi)
        # b = -2h, c = h^2 - s^2
        b = -2 * h
        c = h * h - s * s
        poly = x * x + b * x + c
        eq_latex = sp.latex(sp.Eq(poly, 0))
        half_b = b // 2  # integer because b = -2h
        half_b_sq = half_b * half_b
        # After moving c: x^2 + bx = -c
        rhs1 = -c
        # After adding half_b_sq: x^2 + bx + half_b_sq = rhs1 + half_b_sq = s^2
        k = s * s
        # (x + half_b)^2 = k  -->  x = -half_b +/- s = h +/- s
        root_plus = h + s
        root_minus = h - s
        roots = sorted([root_plus, root_minus])
        binom_sign = "+" if half_b >= 0 else "-"
        binom_val = abs(half_b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ by completing the square.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                f"Move the constant to the other side: $x^2 + ({b})x = {rhs1}$.",
                r"Take half of the coefficient of $x$ and square it: $\left(\dfrac{b}{2}\right)^2$.",
                f"Here $\\left(\\dfrac{{{b}}}{{2}}\\right)^2 = ({half_b})^2 = {half_b_sq}$. Add this to both sides.",
                f"The left side is now a perfect square: $(x {binom_sign} {binom_val})^2 = {k}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Move the constant to the right: $x^2 + ({b})x = {rhs1}$.",
                f"Compute $\\left(\\dfrac{{b}}{{2}}\\right)^2 = \\left(\\dfrac{{{b}}}{{2}}\\right)^2 = {half_b_sq}$.",
                f"Add ${half_b_sq}$ to both sides: $x^2 + ({b})x + {half_b_sq} = {rhs1 + half_b_sq}$.",
                f"Factor the left side: $(x {binom_sign} {binom_val})^2 = {k}$.",
                f"Take square roots: $x {binom_sign} {binom_val} = \\pm {s}$.",
                f"Solve: $x = {roots[0]}$ or $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class CompleteSquareIntegerK(Generator):
    """Complete the square with a guaranteed-integer answer.

    Backward construction picks h and even s so the roots are integers, and
    requires b to be a clean even number by construction (b = -2h is always
    even). We simply vary h and s to keep parameter space distinct from
    CompleteSquareLeadingOne by using slightly different ranges.
    """
    generator_id = "complete_square_integer_k"
    topic_slug = "completing_the_square"
    display_name = "Complete the square (integer answers)"
    bank_count_per_difficulty = 25

    _H_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _S_RANGE = {"easy": (1, 5), "medium": (2, 8), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGE[difficulty]
        s_lo, s_hi = self._S_RANGE[difficulty]
        h = rng.randint(h_lo, h_hi)
        s = rng.randint(s_lo, s_hi)
        b = -2 * h
        c = h * h - s * s
        poly = x * x + b * x + c
        eq_latex = sp.latex(sp.Eq(poly, 0))
        half_b = b // 2
        half_b_sq = half_b * half_b
        k = s * s
        rhs1 = -c
        root_plus = h + s
        root_minus = h - s
        roots = sorted([root_plus, root_minus])
        binom_sign = "+" if half_b >= 0 else "-"
        binom_val = abs(half_b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ by completing the square.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"Complete the square: move the constant, then add $\left(\dfrac{b}{2}\right)^2$ to both sides.",
                f"$\\left(\\dfrac{{{b}}}{{2}}\\right)^2 = ({half_b})^2 = {half_b_sq}$.",
                f"After completing the square the equation becomes $(x {binom_sign} {binom_val})^2 = {k}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Move the constant: $x^2 + ({b})x = {rhs1}$.",
                f"Add $\\left(\\dfrac{{b}}{{2}}\\right)^2 = {half_b_sq}$ to both sides: $x^2 + ({b})x + {half_b_sq} = {rhs1 + half_b_sq}$.",
                f"Factor: $(x {binom_sign} {binom_val})^2 = {k}$.",
                f"Take square roots: $x {binom_sign} {binom_val} = \\pm {s}$, so $x = {roots[0]}$ or $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


@register
class CompleteSquareWithA(Generator):
    """Complete the square with leading coefficient a in {2, 3}.

    Divide by a first so the equation becomes x^2 + (b/a)x + (c/a) = 0, then
    complete the square. Backward construction ensures b/a is an even integer
    and the final answer is clean.

    Parameter choice: pick a in {2, 3}, integer h, integer s, then set
        b = -2*a*h        (so b/a = -2h is an even integer)
        c = a*(h^2 - s^2)  (so c/a = h^2 - s^2)
    The resulting equation ax^2 + bx + c = 0 has roots x = h +/- s.
    """
    generator_id = "complete_square_with_a"
    topic_slug = "completing_the_square"
    display_name = "Complete the square (leading coefficient != 1)"
    bank_count_per_difficulty = 20

    _A_CHOICES = [2, 3]
    _H_RANGE = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-11, 11)}
    _S_RANGE = {"easy": (1, 4), "medium": (1, 6), "hard": (2, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGE[difficulty]
        s_lo, s_hi = self._S_RANGE[difficulty]
        a = rng.choice(self._A_CHOICES)
        h = rng.randint(h_lo, h_hi)
        s = rng.randint(s_lo, s_hi)
        b = -2 * a * h
        c = a * (h * h - s * s)
        poly = a * x * x + b * x + c
        eq_latex = sp.latex(sp.Eq(poly, 0))

        # After dividing by a:
        b_over_a = b // a  # = -2h, an integer
        c_over_a = c // a  # = h^2 - s^2
        divided_poly = x * x + b_over_a * x + c_over_a
        divided_eq_latex = sp.latex(sp.Eq(divided_poly, 0))

        # Completing the square with leading coefficient 1:
        half_b = b_over_a // 2  # = -h
        half_b_sq = half_b * half_b  # = h^2
        k = s * s
        rhs1 = -c_over_a  # = s^2 - h^2
        # After adding half_b_sq: x^2 + (b/a)x + h^2 = s^2 - h^2 + h^2 = s^2
        roots = sorted([h + s, h - s])
        binom_sign = "+" if half_b >= 0 else "-"
        binom_val = abs(half_b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ by completing the square.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                f"The leading coefficient is ${a}$, not $1$. Divide every term by ${a}$ first.",
                f"You get ${divided_eq_latex}$, which now has a leading coefficient of $1$.",
                f"Complete the square on this: add $\\left(\\dfrac{{{b_over_a}}}{{2}}\\right)^2 = {half_b_sq}$ to both sides.",
                f"The result is $(x {binom_sign} {binom_val})^2 = {k}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Divide both sides by ${a}$: ${divided_eq_latex}$.",
                f"Move the constant: $x^2 + ({b_over_a})x = {rhs1}$.",
                f"Add $\\left(\\dfrac{{{b_over_a}}}{{2}}\\right)^2 = {half_b_sq}$ to both sides: $x^2 + ({b_over_a})x + {half_b_sq} = {rhs1 + half_b_sq}$.",
                f"Factor the left side: $(x {binom_sign} {binom_val})^2 = {k}$.",
                f"Take square roots: $x {binom_sign} {binom_val} = \\pm {s}$, so $x = {roots[0]}$ or $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )
