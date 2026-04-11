"""Trigonometric inequalities (pre-calculus Wave C).

Three generators for the ``trigonometric_inequalities`` topic slug:

- SolveSinGreaterThanHalf: solve $\\sin x > k$ (or $\\geq$, $<$, $\\leq$)
  on $[0, 2\\pi)$ where $k$ is a clean unit-circle value.
- SolveCosComparison: analogous for cosine.
- SolveTanComparison: tangent on a restricted interval (one period).

Backward construction: pick the defining reference angles $a$ and $b$
first, then read off the comparison value and render the statement.
"""
from __future__ import annotations

import math
import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TRIG_INEQ_TAGS = [
    "#branch-pre-calculus",
    "#topic-trig-equations",
    "#skill-multi-step",
]


def _format_pi_fraction(num: int, den: int) -> str:
    """Render (num*pi)/den as LaTeX."""
    if num == 0:
        return "0"
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    sign = "-" if num < 0 else ""
    a = abs(num)
    if den == 1:
        if a == 1:
            return f"{sign}\\pi"
        return rf"{sign}{a}\pi"
    if a == 1:
        return rf"{sign}\dfrac{{\pi}}{{{den}}}"
    return rf"{sign}\dfrac{{{a}\pi}}{{{den}}}"


def _render_interval_open_or_closed(
    lo_pair: tuple[int, int],
    hi_pair: tuple[int, int],
    left_closed: bool,
    right_closed: bool,
) -> str:
    lo_latex = _format_pi_fraction(*lo_pair)
    hi_latex = _format_pi_fraction(*hi_pair)
    lb = "[" if left_closed else "("
    rb = "]" if right_closed else ")"
    return f"{lb}{lo_latex},\\ {hi_latex}{rb}"


# ===========================================================================
# Generator 1: solve_sin_greater_than_half
# ===========================================================================


# Clean unit-circle sine values with the two angles in [0, 2*pi) where
# sin theta = value. All values are in (-1, 1) so the solutions are
# proper open intervals.
# Each entry: (value_sym, value_latex, x1_num, x1_den, x2_num, x2_den)
# where x1 < x2 and sin x1 = sin x2 = value.
_SIN_TABLE: tuple[tuple[sp.Expr, str, int, int, int, int], ...] = (
    # value 1/2 -> pi/6 and 5*pi/6
    (sp.Rational(1, 2), r"\dfrac{1}{2}", 1, 6, 5, 6),
    # value sqrt(2)/2 -> pi/4 and 3*pi/4
    (sp.sqrt(2) / 2, r"\dfrac{\sqrt{2}}{2}", 1, 4, 3, 4),
    # value sqrt(3)/2 -> pi/3 and 2*pi/3
    (sp.sqrt(3) / 2, r"\dfrac{\sqrt{3}}{2}", 1, 3, 2, 3),
    # value -1/2 -> 7*pi/6 and 11*pi/6
    (sp.Rational(-1, 2), r"-\dfrac{1}{2}", 7, 6, 11, 6),
    # value -sqrt(2)/2 -> 5*pi/4 and 7*pi/4
    (-sp.sqrt(2) / 2, r"-\dfrac{\sqrt{2}}{2}", 5, 4, 7, 4),
    # value -sqrt(3)/2 -> 4*pi/3 and 5*pi/3
    (-sp.sqrt(3) / 2, r"-\dfrac{\sqrt{3}}{2}", 4, 3, 5, 3),
)


@register
class SolveSinGreaterThanHalf(Generator):
    """Solve $\\sin x \\,\\square\\, k$ on $[0, 2\\pi)$ with clean $k$.

    Backward: pick the clean value $k$ (one of the six in ``_SIN_TABLE``),
    decide the direction of the inequality (> or >=, < or <=), and emit
    the solution as a union (or single interval) of intervals with
    exact unit-circle endpoints.
    """
    generator_id = "solve_sin_greater_than_half"
    topic_slug = "trigonometric_inequalities"
    display_name = "Solve a sine inequality on [0, 2pi)"

    _SIGNS = (">", ">=", "<", "<=")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        value_sym, value_latex, x1_n, x1_d, x2_n, x2_d = rng.choice(_SIN_TABLE)
        sign = rng.choice(self._SIGNS)

        # Boundary inclusion depends on strict vs non-strict.
        closed = sign in ("<=", ">=")

        # Build solution interval(s).
        # If sin x > k on [0, 2*pi): solution is (x1, x2) (an open arc above the chord).
        # If sin x < k: solution is [0, x1) ∪ (x2, 2*pi), but we use closed intervals
        #              at 0 and 2*pi depending on whether those endpoints satisfy
        #              the inequality. sin(0) = 0, sin(2pi - epsilon) = 0 limit.
        x1_latex = _format_pi_fraction(x1_n, x1_d)
        x2_latex = _format_pi_fraction(x2_n, x2_d)

        if sign in (">", ">="):
            # Solution is the arc between x1 and x2 where sin > value.
            lb = "[" if closed else "("
            rb = "]" if closed else ")"
            answer_latex = f"${lb}{x1_latex},\\ {x2_latex}{rb}$"
            solve_explanation = (
                f"The sine curve is above $y = {value_latex}$ on the open arc "
                f"from $x = {x1_latex}$ to $x = {x2_latex}$ within $[0,\\ 2\\pi)$. "
                + ("The boundary values are " + ("included" if closed else "excluded")
                   + f" since the inequality is {'non-strict' if closed else 'strict'}.")
            )
        else:
            # sin x <= value (or < value)
            lb = "[" if closed else "("
            rb = "]" if closed else ")"
            # Two intervals: [0, x1] (closed) union [x2, 2 pi). Actually, the
            # left of x1 we must start from 0 which is always included (closed),
            # and the right interval ends at 2 pi (never included because the
            # domain is [0, 2 pi)).
            answer_latex = (
                f"$[0,\\ {x1_latex}{rb} \\cup {lb}{x2_latex},\\ 2\\pi)$"
            )
            solve_explanation = (
                f"The sine curve is below $y = {value_latex}$ on two pieces of "
                f"$[0,\\ 2\\pi)$: the arc near $0$ (up to $x = {x1_latex}$) and "
                f"the arc starting at $x = {x2_latex}$ and running back toward "
                f"$2\\pi$. Combine them as a union."
            )

        sign_latex = {">": ">", ">=": r"\geq", "<": "<", "<=": r"\leq"}[sign]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (value_latex, sign, x1_n, x1_d)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve $\\sin x {sign_latex} {value_latex}$ on the interval "
                f"$[0,\\ 2\\pi)$. Give your answer as an interval or union of "
                "intervals."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    f"Start by finding every $x$ in $[0,\\ 2\\pi)$ where "
                    f"$\\sin x = {value_latex}$. These are the boundary values."
                ),
                (
                    "Test a point in each resulting interval to decide whether "
                    "the inequality is satisfied there, then assemble the "
                    "solution set."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Solve the boundary equation $\\sin x = {value_latex}$: "
                    f"$x = {x1_latex}$ or $x = {x2_latex}$."
                ),
                solve_explanation,
                f"Solution set: {answer_latex}.",
            ],
            tags=TRIG_INEQ_TAGS,
        )


# ===========================================================================
# Generator 2: solve_cos_comparison
# ===========================================================================


# Each entry: (value_sym, value_latex, x1_num, x1_den, x2_num, x2_den)
# where 0 <= x1 < x2 < 2*pi and cos x1 = cos x2 = value.
_COS_TABLE: tuple[tuple[sp.Expr, str, int, int, int, int], ...] = (
    # cos = 1/2 -> pi/3 and 5*pi/3
    (sp.Rational(1, 2), r"\dfrac{1}{2}", 1, 3, 5, 3),
    # cos = sqrt(2)/2 -> pi/4 and 7*pi/4
    (sp.sqrt(2) / 2, r"\dfrac{\sqrt{2}}{2}", 1, 4, 7, 4),
    # cos = sqrt(3)/2 -> pi/6 and 11*pi/6
    (sp.sqrt(3) / 2, r"\dfrac{\sqrt{3}}{2}", 1, 6, 11, 6),
    # cos = -1/2 -> 2*pi/3 and 4*pi/3
    (sp.Rational(-1, 2), r"-\dfrac{1}{2}", 2, 3, 4, 3),
    # cos = -sqrt(2)/2 -> 3*pi/4 and 5*pi/4
    (-sp.sqrt(2) / 2, r"-\dfrac{\sqrt{2}}{2}", 3, 4, 5, 4),
    # cos = -sqrt(3)/2 -> 5*pi/6 and 7*pi/6
    (-sp.sqrt(3) / 2, r"-\dfrac{\sqrt{3}}{2}", 5, 6, 7, 6),
)


@register
class SolveCosComparison(Generator):
    """Solve $\\cos x \\,\\square\\, k$ on $[0, 2\\pi)$ with clean $k$.

    Because cosine is $1$ at $0$ (the left endpoint of $[0, 2\\pi)$),
    the "greater than" cases have solution $[0, x_1) \\cup (x_2, 2\\pi)$,
    while "less than" cases have a single interval $(x_1, x_2)$.
    """
    generator_id = "solve_cos_comparison"
    topic_slug = "trigonometric_inequalities"
    display_name = "Solve a cosine inequality on [0, 2pi)"

    _SIGNS = (">", ">=", "<", "<=")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        value_sym, value_latex, x1_n, x1_d, x2_n, x2_d = rng.choice(_COS_TABLE)
        sign = rng.choice(self._SIGNS)
        closed = sign in ("<=", ">=")

        x1_latex = _format_pi_fraction(x1_n, x1_d)
        x2_latex = _format_pi_fraction(x2_n, x2_d)

        if sign in ("<", "<="):
            lb = "[" if closed else "("
            rb = "]" if closed else ")"
            answer_latex = f"${lb}{x1_latex},\\ {x2_latex}{rb}$"
            solve_explanation = (
                f"Cosine dips below $y = {value_latex}$ between the two "
                f"boundary angles $x = {x1_latex}$ and $x = {x2_latex}$, so the "
                "solution is a single interval."
            )
        else:  # > or >=
            lb = "[" if closed else "("
            rb = "]" if closed else ")"
            answer_latex = (
                f"$[0,\\ {x1_latex}{rb} \\cup {lb}{x2_latex},\\ 2\\pi)$"
            )
            solve_explanation = (
                f"Cosine is above $y = {value_latex}$ on two arcs: from $0$ up "
                f"to $x = {x1_latex}$ and from $x = {x2_latex}$ back toward "
                f"$2\\pi$. The solution is the union of these arcs."
            )

        sign_latex = {">": ">", ">=": r"\geq", "<": "<", "<=": r"\leq"}[sign]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (value_latex, sign, x1_n, x1_d)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve $\\cos x {sign_latex} {value_latex}$ on $[0,\\ 2\\pi)$. "
                "Write your answer as an interval or union of intervals."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    f"Find every $x$ in $[0,\\ 2\\pi)$ where $\\cos x = "
                    f"{value_latex}$."
                ),
                (
                    "Cosine is symmetric about $x = \\pi$, so the two boundary "
                    "angles are reflections across that line."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Solve $\\cos x = {value_latex}$ in $[0,\\ 2\\pi)$: "
                    f"$x = {x1_latex}$ or $x = {x2_latex}$."
                ),
                solve_explanation,
                f"Solution set: {answer_latex}.",
            ],
            tags=TRIG_INEQ_TAGS,
        )


# ===========================================================================
# Generator 3: solve_tan_comparison
# ===========================================================================


# Tan entries with x in (-pi/2, pi/2) (the principal period).
# Each entry: (value_sym, value_latex, x_num, x_den) with tan(x) = value.
_TAN_TABLE: tuple[tuple[sp.Expr, str, int, int], ...] = (
    # tan = 1 at pi/4
    (sp.Integer(1), r"1", 1, 4),
    # tan = -1 at -pi/4
    (sp.Integer(-1), r"-1", -1, 4),
    # tan = sqrt(3) at pi/3
    (sp.sqrt(3), r"\sqrt{3}", 1, 3),
    # tan = -sqrt(3) at -pi/3
    (-sp.sqrt(3), r"-\sqrt{3}", -1, 3),
    # tan = sqrt(3)/3 at pi/6
    (sp.sqrt(3) / 3, r"\dfrac{\sqrt{3}}{3}", 1, 6),
    # tan = -sqrt(3)/3 at -pi/6
    (-sp.sqrt(3) / 3, r"-\dfrac{\sqrt{3}}{3}", -1, 6),
    # tan = 0 at 0 (edge case)
    (sp.Integer(0), r"0", 0, 1),
)


@register
class SolveTanComparison(Generator):
    """Solve $\\tan x \\,\\square\\, k$ on the principal period $(-\\pi/2, \\pi/2)$.

    Because tangent is strictly increasing on $(-\\pi/2, \\pi/2)$, each
    inequality has a single interval solution whose boundary is the
    unique $x_0$ with $\\tan x_0 = k$.
    """
    generator_id = "solve_tan_comparison"
    topic_slug = "trigonometric_inequalities"
    display_name = "Solve a tangent inequality on a one-period interval"

    _SIGNS = (">", ">=", "<", "<=")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        value_sym, value_latex, x_n, x_d = rng.choice(_TAN_TABLE)
        sign = rng.choice(self._SIGNS)
        closed = sign in ("<=", ">=")

        x0_latex = _format_pi_fraction(x_n, x_d)

        # Domain endpoints are ALWAYS open (tan is undefined there).
        neg_half = r"-\dfrac{\pi}{2}"
        pos_half = r"\dfrac{\pi}{2}"

        if sign in (">", ">="):
            rb = "]" if closed else ")"
            lb = "[" if closed else "("
            answer_latex = f"${lb}{x0_latex},\\ {pos_half})$"
            solve_explanation = (
                f"Tangent is strictly increasing on the principal period, so "
                f"$\\tan x > {value_latex}$ exactly when $x > {x0_latex}$ "
                "(within the period's right half)."
            )
        else:
            rb = "]" if closed else ")"
            lb = "[" if closed else "("
            answer_latex = f"$({neg_half},\\ {x0_latex}{rb}$"
            solve_explanation = (
                f"Tangent is strictly increasing on the principal period, so "
                f"$\\tan x < {value_latex}$ exactly when $x < {x0_latex}$ "
                "(within the period's left half)."
            )

        sign_latex = {">": ">", ">=": r"\geq", "<": "<", "<=": r"\leq"}[sign]
        domain_latex = rf"\left(-\dfrac{{\pi}}{{2}},\ \dfrac{{\pi}}{{2}}\right)"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (value_latex, sign, x_n, x_d)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve $\\tan x {sign_latex} {value_latex}$ on the interval "
                f"${domain_latex}$ (one period of tangent)."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    f"Find the unique $x_0$ in ${domain_latex}$ with "
                    f"$\\tan x_0 = {value_latex}$."
                ),
                (
                    "Because tangent is strictly increasing on its principal "
                    "period, the inequality translates directly into an "
                    "inequality on $x$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Solve the boundary equation $\\tan x = {value_latex}$ in "
                    f"${domain_latex}$: $x = {x0_latex}$."
                ),
                solve_explanation,
                f"Solution set: {answer_latex}.",
            ],
            tags=TRIG_INEQ_TAGS,
        )
