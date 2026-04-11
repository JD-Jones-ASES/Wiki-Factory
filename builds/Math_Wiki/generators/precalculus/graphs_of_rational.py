"""Graphs of rational functions (pre-calculus Wave C).

Three generators covering the ``graphs_of_rational_functions`` topic slug:

- FindVerticalAsymptotesRational: locate zeros of the denominator that are
  not canceled by a matching numerator factor.
- FindHorizontalAsymptoteRational: classify the horizontal asymptote by
  comparing the degrees of numerator and denominator.
- IdentifyHoleFromFactors: recognise a removable discontinuity when a
  common factor in numerator and denominator cancels.

Backward construction throughout: pick the asymptote locations (or
degrees, or hole location) first, then assemble the rational expression
so the answer is a small integer or short list. SymPy verifies every
answer via ``sp.together`` factorisation and ``sp.limit``.
"""
from __future__ import annotations

import random
from typing import Literal

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared constants and helpers
# ---------------------------------------------------------------------------


RATIONAL_TAGS = [
    "#branch-pre-calculus",
    "#topic-rational-expressions",
    "#skill-procedural-calculation",
]


def _linear_factor(root: int) -> str:
    """Render $(x - root)$ with a clean sign.

    >>> _linear_factor(3)
    '(x - 3)'
    >>> _linear_factor(-2)
    '(x + 2)'
    >>> _linear_factor(0)
    'x'
    """
    if root == 0:
        return "x"
    sign = "-" if root > 0 else "+"
    return f"(x {sign} {abs(root)})"


def _expand_factor_product(roots: list[int]) -> sp.Expr:
    """Return the SymPy expansion of $\\prod (x - r_i)$ for listed roots."""
    x = sp.symbols("x")
    expr = sp.Integer(1)
    for r in roots:
        expr *= (x - r)
    return sp.expand(expr)


def _polynomial_to_latex(roots: list[int], var: str = "x") -> str:
    """Render an expanded polynomial built from linear factors as LaTeX.

    Uses SymPy's ``latex`` output but prefers factored form when two or
    more factors are present (more readable for the student).
    """
    if not roots:
        return "1"
    pieces = [_linear_factor(r) for r in roots]
    return "".join(pieces)


# ===========================================================================
# Generator 1: find_vertical_asymptotes_rational
# ===========================================================================


@register
class FindVerticalAsymptotesRational(Generator):
    """Given a rational function in factored form, find the vertical asymptotes.

    Backward: pick distinct integer roots for the denominator (these are
    the asymptote candidates) and distinct integer roots for the numerator
    (these are the zeros). No factors are shared, so every denominator
    root is a true vertical asymptote.
    """

    generator_id = "find_vertical_asymptotes_rational"
    topic_slug = "graphs_of_rational_functions"
    display_name = "Locate the vertical asymptotes of a factored rational function"

    _NUM_ROOT_COUNTS = {"easy": 1, "medium": 2, "hard": 2}
    _DEN_ROOT_COUNTS = {"easy": 1, "medium": 2, "hard": 3}
    _POOLS = {
        "easy": (-5, -4, -3, -2, -1, 1, 2, 3, 4, 5),
        "medium": (-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6),
        "hard": (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pool = list(self._POOLS[difficulty])
        rng.shuffle(pool)
        num_count = self._NUM_ROOT_COUNTS[difficulty]
        den_count = self._DEN_ROOT_COUNTS[difficulty]

        num_roots = sorted(pool[:num_count])
        den_roots = sorted(pool[num_count:num_count + den_count])

        num_latex = _polynomial_to_latex(num_roots)
        den_latex = _polynomial_to_latex(den_roots)
        statement_latex = (
            f"For the rational function "
            f"$f(x) = \\dfrac{{{num_latex}}}{{{den_latex}}}$, find every "
            "vertical asymptote."
        )

        # Verify with SymPy by computing the limit from each side of each root.
        x = sp.symbols("x")
        num_expr = sp.prod([x - r for r in num_roots])
        den_expr = sp.prod([x - r for r in den_roots])
        asymptotes = []
        for r in den_roots:
            lim_right = sp.limit(num_expr / den_expr, x, r, "+")
            if lim_right.is_infinite:
                asymptotes.append(r)
        asymptotes.sort()

        equation_parts = [f"x = {r}" for r in asymptotes]
        answer_latex = "$" + ",\\ ".join(equation_parts) + "$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (tuple(num_roots), tuple(den_roots))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=answer_latex,
            hints=[
                (
                    "Vertical asymptotes occur at zeros of the denominator that "
                    "are NOT also zeros of the numerator."
                ),
                (
                    "Set each factor of the denominator equal to zero and solve. "
                    "If the same factor appears in the numerator, it cancels and "
                    "produces a hole instead of an asymptote."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Set each denominator factor equal to zero: "
                    + ", ".join(f"${_linear_factor(r)} = 0$" for r in den_roots)
                    + "."
                ),
                (
                    "Solve each equation: "
                    + ", ".join(f"$x = {r}$" for r in den_roots)
                    + "."
                ),
                (
                    "Check that none of these values also zero the numerator "
                    f"(which has zeros at $"
                    + ",\\ ".join(f"x = {r}" for r in num_roots)
                    + "$). None cancel, so every denominator zero is a true "
                    "vertical asymptote."
                ),
                (
                    "Vertical asymptotes: " + answer_latex + "."
                ),
            ],
            tags=RATIONAL_TAGS,
        )


# ===========================================================================
# Generator 2: find_horizontal_asymptote_rational
# ===========================================================================


@register
class FindHorizontalAsymptoteRational(Generator):
    """Classify the horizontal asymptote of a rational function by degree.

    Backward: pick degrees for the numerator and denominator first, then
    random leading coefficients and a handful of extra terms. Three cases:

    - deg(num) < deg(den)  ==>  $y = 0$
    - deg(num) = deg(den)  ==>  $y = a_{\\text{num}} / a_{\\text{den}}$
    - deg(num) > deg(den)  ==>  no horizontal asymptote
    """

    generator_id = "find_horizontal_asymptote_rational"
    topic_slug = "graphs_of_rational_functions"
    display_name = "Find the horizontal asymptote of a rational function via degree comparison"

    _CASES = ("less", "equal", "greater")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(self._CASES)

        # Difficulty controls the overall magnitude and number of non-leading
        # terms shown in the expressions.
        coeff_cap = {"easy": 5, "medium": 8, "hard": 12}[difficulty]
        base_deg = {"easy": 2, "medium": 3, "hard": 4}[difficulty]

        if case == "less":
            den_deg = base_deg
            num_deg = rng.randint(0, den_deg - 1)
        elif case == "equal":
            num_deg = base_deg
            den_deg = base_deg
        else:  # greater
            num_deg = base_deg + 1
            den_deg = rng.randint(1, base_deg)

        def random_poly(deg: int) -> tuple[sp.Expr, int]:
            """Build a polynomial of the given degree with nonzero leading coeff."""
            leading = rng.choice(
                [c for c in range(-coeff_cap, coeff_cap + 1) if c != 0]
            )
            lower = [
                rng.randint(-coeff_cap, coeff_cap) for _ in range(deg)
            ]
            x = sp.symbols("x")
            expr = leading * x ** deg
            for k, c in enumerate(lower):
                if c != 0:
                    expr += c * x ** k
            return sp.expand(expr), leading

        num_expr, num_leading = random_poly(num_deg)
        den_expr, den_leading = random_poly(den_deg)

        num_latex = sp.latex(num_expr)
        den_latex = sp.latex(den_expr)

        if case == "less":
            answer_latex = "$y = 0$"
            rule_explanation = (
                f"Since $\\deg(\\text{{numerator}}) = {num_deg} < {den_deg} = "
                "\\deg(\\text{denominator})$, the horizontal asymptote is "
                "$y = 0$."
            )
        elif case == "equal":
            ratio = sp.Rational(num_leading, den_leading)
            if ratio.q == 1:
                ratio_latex = f"{ratio.p}"
            else:
                sign = "-" if ratio.p < 0 else ""
                ratio_latex = (
                    f"{sign}\\dfrac{{{abs(ratio.p)}}}{{{ratio.q}}}"
                )
            answer_latex = f"$y = {ratio_latex}$"
            rule_explanation = (
                f"Since the degrees are equal (${num_deg} = {den_deg}$), the "
                f"horizontal asymptote is the ratio of the leading coefficients: "
                f"$y = \\dfrac{{{num_leading}}}{{{den_leading}}} = {ratio_latex}$."
            )
        else:
            answer_latex = "No horizontal asymptote"
            rule_explanation = (
                f"Since $\\deg(\\text{{numerator}}) = {num_deg} > {den_deg} = "
                "\\deg(\\text{denominator})$, there is no horizontal asymptote. "
                "(The function has an oblique or curved end behaviour instead.)"
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (case, num_deg, den_deg, num_leading, den_leading)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the horizontal asymptote of "
                f"$f(x) = \\dfrac{{{num_latex}}}{{{den_latex}}}$, or state that "
                "none exists."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Compare the degree of the numerator $n$ to the degree of the "
                    "denominator $m$: three cases give three answers."
                ),
                (
                    "If $n < m$, the horizontal asymptote is $y = 0$. If $n = m$, "
                    "it is the ratio of leading coefficients. If $n > m$, there "
                    "is no horizontal asymptote."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read the degrees: $\\deg(\\text{{num}}) = {num_deg}$ and "
                    f"$\\deg(\\text{{den}}) = {den_deg}$."
                ),
                rule_explanation,
                f"Conclusion: {answer_latex}.",
            ],
            tags=RATIONAL_TAGS,
        )


# ===========================================================================
# Generator 3: identify_hole_from_factors
# ===========================================================================


@register
class IdentifyHoleFromFactors(Generator):
    """Identify the removable hole and the remaining vertical asymptote.

    Backward: pick three distinct integers $a, b, c$. Build
    $f(x) = \\dfrac{(x - a)(x - b)}{(x - a)(x - c)}$. The factor $(x - a)$
    cancels, leaving a hole at $x = a$ and a vertical asymptote at $x = c$.
    The $y$-coordinate of the hole is $(a - b)/(a - c)$, chosen to be a
    clean rational.
    """

    generator_id = "identify_hole_from_factors"
    topic_slug = "graphs_of_rational_functions"
    display_name = "Identify the hole and asymptote of a rational function with a common factor"

    _A_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}
    _B_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}
    _C_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        while True:
            a = rng.randint(*self._A_RANGES[difficulty])
            b = rng.randint(*self._B_RANGES[difficulty])
            c = rng.randint(*self._C_RANGES[difficulty])
            if a != b and a != c and b != c:
                break

        # y-value of the hole is obtained from the reduced function.
        x = sp.symbols("x")
        reduced = (x - b) / (x - c)
        y_at_hole = sp.simplify(reduced.subs(x, a))
        num = int((a - b))
        den = int((a - c))
        y_latex = sp.latex(y_at_hole)

        numerator_latex = f"{_linear_factor(a)}{_linear_factor(b)}"
        denominator_latex = f"{_linear_factor(a)}{_linear_factor(c)}"

        hole_point_latex = f"\\left({a},\\ {y_latex}\\right)"
        asymptote_latex = f"x = {c}"
        answer_latex = (
            f"Hole: ${hole_point_latex}$; vertical asymptote: ${asymptote_latex}$"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"The rational function "
                f"$f(x) = \\dfrac{{{numerator_latex}}}{{{denominator_latex}}}$ "
                "has one removable discontinuity (a hole) and one vertical "
                "asymptote. Identify both."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "A factor shared by numerator and denominator cancels and "
                    "produces a hole, not an asymptote. The remaining zero of the "
                    "denominator is the true vertical asymptote."
                ),
                (
                    "After cancelling the shared factor, substitute the hole's "
                    "$x$-value into the reduced expression to find its "
                    "$y$-coordinate."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the shared factor $(x - {a})$ in both numerator "
                    "and denominator."
                ),
                (
                    "Cancel it: $f(x) = "
                    f"\\dfrac{{x - {b} \\text{{ if we cancel}}}}{{x - {c}}}$, "
                    f"or more cleanly $f(x) = \\dfrac{{{_linear_factor(b)}}}{{{_linear_factor(c)}}}$ "
                    f"when $x \\ne {a}$."
                ),
                (
                    f"The cancelled factor gives a hole at $x = {a}$. "
                    f"Substitute into the reduced form: "
                    f"$y = \\dfrac{{{a} - {b}}}{{{a} - {c}}} = \\dfrac{{{num}}}{{{den}}} = {y_latex}$."
                ),
                (
                    f"The remaining denominator factor gives the vertical "
                    f"asymptote ${asymptote_latex}$."
                ),
                f"Final answer: {answer_latex}.",
            ],
            tags=RATIONAL_TAGS,
        )
