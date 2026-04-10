"""Lines and linear equation generators (Phase 2c Wave 4).

Five topic slugs covered:

- writing_linear_equations (Writing_Linear_Equations.md)
- parallel_and_perpendicular_lines (Parallel_And_Perpendicular_Lines.md)
- linear_functions (Linear_Functions.md)
- modeling_with_linear_functions (Modeling_With_Linear_Functions.md)
- graphing_linear_equations_from_tables (Graphing_Linear_Equations_From_Tables.md)

Each topic has three generators for a total of 15. All generators use
backward construction: parameters are picked so the answer comes out clean,
then the statement is rendered.
"""
from __future__ import annotations

import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_fraction, format_point


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _render_linear(m: int, b: int, y: str = "y") -> str:
    """Render y = mx + b in LaTeX with clean signs and 1/-1 coefficient handling."""
    if m == 0:
        return f"{y} = {b}"
    if m == 1:
        mx = "x"
    elif m == -1:
        mx = "-x"
    else:
        mx = f"{m}x"
    if b == 0:
        return f"{y} = {mx}"
    sign = "+" if b > 0 else "-"
    return f"{y} = {mx} {sign} {abs(b)}"


def _render_function(m: int, b: int) -> str:
    """Render f(x) = mx + b in LaTeX with clean signs."""
    return _render_linear(m, b, y="f(x)")


def _render_linear_frac(m: Fraction, b: Fraction) -> str:
    """Render y = mx + b where m and b may be fractions."""
    # m term
    if m == 0:
        mx = ""
    elif m == 1:
        mx = "x"
    elif m == -1:
        mx = "-x"
    elif m.denominator == 1:
        mx = f"{m.numerator}x"
    else:
        mx = rf"\frac{{{m.numerator}}}{{{m.denominator}}}x"
    # b term
    if b == 0:
        b_str = ""
    elif b.denominator == 1:
        b_str = f"{b.numerator}"
    else:
        b_str = rf"\frac{{{b.numerator}}}{{{b.denominator}}}"

    if mx == "" and b_str == "":
        return "y = 0"
    if mx == "":
        return f"y = {b_str}"
    if b_str == "":
        return f"y = {mx}"
    sign = "+" if b > 0 else "-"
    # For negative fractions, strip the leading minus on b_str before the sign.
    if b < 0:
        if b.denominator == 1:
            b_str = f"{-b.numerator}"
        else:
            b_str = rf"\frac{{{-b.numerator}}}{{{b.denominator}}}"
    return f"y = {mx} {sign} {b_str}"


# ===========================================================================
# Topic 1: writing_linear_equations
# ===========================================================================

@register
class WriteLineSlopeYIntercept(Generator):
    """Given slope m and y-intercept b, write y = mx + b. Trivial substitution."""
    generator_id = "write_line_slope_y_intercept"
    topic_slug = "writing_linear_equations"
    display_name = "Write y = mx + b given slope and y-intercept"

    _RANGES = {"easy": (-9, 9), "medium": (-18, 18), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        m = rng.randint(lo, hi)
        while m == 0:
            m = rng.randint(lo, hi)
        b = rng.randint(lo, hi)

        answer = _render_linear(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the line with slope $m = {m}$ and "
                f"$y$-intercept $b = {b}$. Give your answer in slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Slope-intercept form is $y = mx + b$.",
                f"Substitute $m = {m}$ and $b = {b}$ directly into the template.",
            ],
            solution_steps_latex=[
                r"Start with the template $y = mx + b$.",
                f"Substitute $m = {m}$ and $b = {b}$.",
                f"The equation is ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-formula-substitution"],
        )


@register
class WriteLineSlopeAndPoint(Generator):
    """Given slope m and point (x0, y0), write y = mx + b."""
    generator_id = "write_line_slope_and_point"
    topic_slug = "writing_linear_equations"
    display_name = "Write y = mx + b given slope and a point"

    _M_RANGES = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-20, 20)}
    _BX_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._BX_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        x0 = rng.randint(b_lo, b_hi)
        y0 = m * x0 + b  # backward: derive matching y

        answer = _render_linear(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, x0, y0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the line with slope $m = {m}$ that passes "
                f"through the point ${format_point(x0, y0)}$. Give your answer "
                "in slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Start from point-slope form: $y - y_0 = m(x - x_0)$.",
                f"Substitute $m = {m}$, $x_0 = {x0}$, $y_0 = {y0}$.",
                f"Solve for $b$: $b = y_0 - m x_0 = {y0} - ({m})({x0}) = {b}$.",
            ],
            solution_steps_latex=[
                f"Use the template $y = mx + b$ with $m = {m}$.",
                f"Substitute the point $({x0}, {y0})$: ${y0} = ({m})({x0}) + b$.",
                f"Simplify: ${y0} = {m * x0} + b$, so $b = {y0} - {m * x0} = {b}$.",
                f"The equation is ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class WriteLineFromTwoPoints(Generator):
    """Given two points, derive slope and intercept, write y = mx + b."""
    generator_id = "write_line_from_two_points"
    topic_slug = "writing_linear_equations"
    display_name = "Write y = mx + b given two points"

    _M_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _BX_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._BX_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        x1 = rng.randint(b_lo, b_hi)
        x2 = rng.randint(b_lo, b_hi)
        while x2 == x1:
            x2 = rng.randint(b_lo, b_hi)
        y1 = m * x1 + b
        y2 = m * x2 + b

        answer = _render_linear(m, b)
        dy = y2 - y1
        dx = x2 - x1

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the line passing through "
                f"${format_point(x1, y1)}$ and ${format_point(x2, y2)}$. "
                "Give your answer in slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"First compute the slope $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.",
                r"Then use $b = y_1 - m x_1$ to find the $y$-intercept.",
                f"Finally write $y = mx + b$.",
            ],
            solution_steps_latex=[
                f"Slope: $m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\dfrac{{{dy}}}{{{dx}}} = {m}$.",
                f"Intercept: $b = {y1} - ({m})({x1}) = {b}$.",
                f"Equation: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


# ===========================================================================
# Topic 2: parallel_and_perpendicular_lines
# ===========================================================================

@register
class ParallelLineThroughPoint(Generator):
    """Given y = mx + b0 and a point (x0, y0), write the parallel line through that point."""
    generator_id = "parallel_line_through_point"
    topic_slug = "parallel_and_perpendicular_lines"
    display_name = "Write the parallel line through a given point"

    _M_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _B_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        # Pick two different intercepts so the parallel line is NOT the original.
        b0 = rng.randint(b_lo, b_hi)
        b_new = rng.randint(b_lo, b_hi)
        while b_new == b0:
            b_new = rng.randint(b_lo, b_hi)
        # Derive a point on the new line
        x0 = rng.randint(b_lo, b_hi)
        y0 = m * x0 + b_new

        original = _render_linear(m, b0)
        answer = _render_linear(m, b_new)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b0, x0, y0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the line parallel to ${original}$ that "
                f"passes through the point ${format_point(x0, y0)}$. Give your "
                "answer in slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                "Parallel lines have the **same** slope.",
                f"So the new line has slope $m = {m}$.",
                f"Substitute the point to find $b$: $b = {y0} - ({m})({x0}) = {b_new}$.",
            ],
            solution_steps_latex=[
                f"Read the slope of the given line: $m = {m}$.",
                f"The parallel line has the same slope, so use $y = {m}x + b$.",
                f"Substitute $({x0}, {y0})$: ${y0} = ({m})({x0}) + b$, so $b = {b_new}$.",
                f"Equation: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class PerpendicularLineThroughPoint(Generator):
    """Given y = mx + b0 and a point, write the perpendicular line (slope -1/m) through it."""
    generator_id = "perpendicular_line_through_point"
    topic_slug = "parallel_and_perpendicular_lines"
    display_name = "Write the perpendicular line through a given point"

    # m is the original slope. perp slope is -1/m, which stays as a clean
    # fraction when m is a nonzero integer.
    _M_RANGES = {"easy": (2, 7), "medium": (2, 11), "hard": (2, 15)}
    _B_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        m_abs = rng.randint(m_lo, m_hi)
        sign = rng.choice([-1, 1])
        m = sign * m_abs  # nonzero integer
        b0 = rng.randint(b_lo, b_hi)

        # Perpendicular slope: -1/m (Fraction)
        m_perp = -Fraction(1, m)

        # Pick the point as a multiple of m so b comes out as a clean integer.
        # y0 = m_perp * x0 + b_new. Choose x0 divisible by m.
        k = rng.randint(-8, 8)
        x0 = k * m  # divisible by m (may be 0)
        # Pick integer b_new
        b_new = rng.randint(b_lo, b_hi)
        # Compute y0 from (m_perp, b_new, x0)
        y0_frac = m_perp * x0 + b_new  # Fraction
        # Because x0 is a multiple of m, m_perp * x0 = -x0/m is an integer.
        assert y0_frac.denominator == 1
        y0 = int(y0_frac)

        original = _render_linear(m, b0)
        m_perp_latex = format_fraction(m_perp.numerator, m_perp.denominator)
        answer = _render_linear_frac(m_perp, Fraction(b_new, 1))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b0, x0, y0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the line perpendicular to ${original}$ that "
                f"passes through ${format_point(x0, y0)}$. Give your answer in "
                "slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                "Perpendicular lines have slopes that are negative reciprocals of each other.",
                rf"If the original slope is $m = {m}$, the perpendicular slope is $-\dfrac{{1}}{{{m}}} = {m_perp_latex}$.",
                f"Substitute the point $({x0}, {y0})$ to solve for $b$.",
            ],
            solution_steps_latex=[
                f"Read the slope of the given line: $m = {m}$.",
                rf"Take the negative reciprocal: $m_\perp = -\dfrac{{1}}{{{m}}} = {m_perp_latex}$.",
                f"Substitute the point $({x0}, {y0})$ into $y = {m_perp_latex}x + b$: "
                f"${y0} = ({m_perp_latex})({x0}) + b$.",
                f"Solve for $b$: $b = {b_new}$.",
                f"Equation: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class ClassifyParallelPerpendicularOrNeither(Generator):
    """Given two linear equations in slope-intercept form, classify the relationship."""
    generator_id = "classify_parallel_perpendicular_or_neither"
    topic_slug = "parallel_and_perpendicular_lines"
    display_name = "Classify two lines: parallel, perpendicular, or neither"

    _RANGES = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick category uniformly for variety
        category = rng.choice(["parallel", "perpendicular", "neither"])

        # Pick a nonzero integer slope m1 for both parallel and perpendicular
        # (so the perpendicular slope -1/m1 stays as a clean fraction).
        m1 = rng.randint(lo, hi)
        while m1 == 0:
            m1 = rng.randint(lo, hi)
        b1 = rng.randint(lo, hi)

        if category == "parallel":
            # Same slope, different intercept so they're distinct lines
            m2 = m1
            b2 = rng.randint(lo, hi)
            while b2 == b1:
                b2 = rng.randint(lo, hi)
            # Use integer m2 so rendering is clean
            m2_render = _render_linear(m2, b2)
        elif category == "perpendicular":
            # slope2 = -1/m1 (Fraction). Render as fraction.
            m2_frac = -Fraction(1, m1)
            b2 = rng.randint(lo, hi)
            m2_render = _render_linear_frac(m2_frac, Fraction(b2, 1))
        else:  # neither
            # Pick m2 != m1 and m2 * m1 != -1
            while True:
                m2 = rng.randint(lo, hi)
                if m2 == m1:
                    continue
                if m1 * m2 == -1:
                    continue
                if m2 == 0:
                    continue
                break
            b2 = rng.randint(lo, hi)
            m2_render = _render_linear(m2, b2)

        eq1 = _render_linear(m1, b1)

        answer_label = {
            "parallel": "parallel",
            "perpendicular": "perpendicular",
            "neither": "neither",
        }[category]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (category, m1, b1, b2, eq1, m2_render)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Classify the two lines ${eq1}$ and ${m2_render}$ as parallel, "
                "perpendicular, or neither."
            ),
            answer_latex=answer_label,
            hints=[
                "Two lines are parallel if they have the **same** slope.",
                r"Two lines are perpendicular if the product of their slopes is $-1$ (they are negative reciprocals).",
                "Otherwise, they are neither.",
            ],
            solution_steps_latex=[
                f"Read the slopes from slope-intercept form. The first line has slope $m_1 = {m1}$.",
                f"Read the slope of the second line.",
                f"Compare the slopes: the relationship is **{answer_label}**.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-visualization"],
        )


# ===========================================================================
# Topic 3: linear_functions
# ===========================================================================

@register
class EvaluateLinearFunction(Generator):
    """Given f(x) = mx + b and an input x0, compute f(x0)."""
    generator_id = "evaluate_linear_function"
    topic_slug = "linear_functions"
    display_name = "Evaluate f(x) = mx + b at a given input"

    _RANGES = {"easy": (-9, 9), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        m = rng.randint(lo, hi)
        while m == 0:
            m = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        x0 = rng.randint(lo, hi)
        result = m * x0 + b

        fn = _render_function(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b, x0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Given ${fn}$, find $f({x0})$.",
            answer_latex=f"$f({x0}) = {result}$",
            hints=[
                f"Substitute $x = {x0}$ into the function.",
                f"Evaluate $({m})({x0}) + ({b})$.",
            ],
            solution_steps_latex=[
                f"Start with ${fn}$.",
                f"Substitute $x = {x0}$: $f({x0}) = ({m})({x0}) + ({b})$.",
                f"Simplify: $f({x0}) = {m * x0} + ({b}) = {result}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-formula-substitution"],
        )


@register
class LinearFunctionFromSlopeAndPoint(Generator):
    """Given slope and a point, write f(x) = mx + b."""
    generator_id = "linear_function_from_slope_and_point"
    topic_slug = "linear_functions"
    display_name = "Write f(x) = mx + b given slope and a point"

    _M_RANGES = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-20, 20)}
    _BX_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._BX_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        x0 = rng.randint(b_lo, b_hi)
        y0 = m * x0 + b

        answer = _render_function(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, x0, y0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A linear function has slope $m = {m}$ and passes through "
                f"the point ${format_point(x0, y0)}$. Write the function in "
                "the form $f(x) = mx + b$."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Use the template $f(x) = mx + b$.",
                f"Substitute the point $(x_0, y_0) = ({x0}, {y0})$ to solve for $b$.",
                f"$b = y_0 - m x_0 = {y0} - ({m})({x0}) = {b}$.",
            ],
            solution_steps_latex=[
                f"Start with $f(x) = mx + b$ and $m = {m}$.",
                f"Substitute $({x0}, {y0})$: ${y0} = ({m})({x0}) + b$.",
                f"Simplify: ${y0} = {m * x0} + b$, so $b = {b}$.",
                f"The function is ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class LinearFunctionFindZero(Generator):
    """Given f(x) = mx + b, find the x-value where f(x) = 0 (solve mx + b = 0)."""
    generator_id = "linear_function_find_zero"
    topic_slug = "linear_functions"
    display_name = "Find the zero of f(x) = mx + b"

    _RANGES = {"easy": (-9, 9), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        m = rng.randint(lo, hi)
        while m == 0:
            m = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        while b == 0:
            b = rng.randint(lo, hi)

        # Zero: x = -b / m (as a Fraction)
        zero = Fraction(-b, m)
        zero_latex = format_fraction(zero.numerator, zero.denominator)

        fn = _render_function(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find the zero of ${fn}$. That is, find the value of $x$ where $f(x) = 0$.",
            answer_latex=f"$x = {zero_latex}$",
            hints=[
                r"Set $f(x) = 0$ and solve for $x$.",
                f"This gives ${m}x + ({b}) = 0$.",
                f"Subtract ${b}$ from both sides, then divide by ${m}$.",
            ],
            solution_steps_latex=[
                f"Set $f(x) = 0$: ${m}x + ({b}) = 0$.",
                f"Subtract ${b}$: ${m}x = {-b}$.",
                f"Divide by ${m}$: $x = \\dfrac{{{-b}}}{{{m}}} = {zero_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 4: modeling_with_linear_functions
# ===========================================================================

# Generic, non-copyrighted scenario templates: (place, fee_label, unit)
_SCENARIOS = [
    ("gym", "membership", "month"),
    ("pool", "entry", "visit"),
    ("tutor", "session", "hour"),
    ("taxi", "ride", "mile"),
    ("rental", "booking", "day"),
    ("printer", "print job", "page"),
    ("shipping", "order", "pound"),
    ("cafe", "drink", "refill"),
]


@register
class LinearModelCostProblem(Generator):
    """A flat fee F plus rate R per unit. Write C(x) = Rx + F."""
    generator_id = "linear_model_cost_problem"
    topic_slug = "modeling_with_linear_functions"
    display_name = "Write a linear cost model C(x) = Rx + F"
    supports_word_problems = True

    _F_RANGES = {"easy": (5, 40), "medium": (10, 80), "hard": (20, 150)}
    _R_RANGES = {"easy": (2, 12), "medium": (3, 25), "hard": (5, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        f_lo, f_hi = self._F_RANGES[difficulty]
        r_lo, r_hi = self._R_RANGES[difficulty]
        F = rng.randint(f_lo, f_hi)
        R = rng.randint(r_lo, r_hi)
        place, fee_label, unit = rng.choice(_SCENARIOS)

        answer = f"C(x) = {R}x + {F}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (F, R, place, unit)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {place} charges a flat {fee_label} fee of $\\${F}$ plus "
                f"$\\${R}$ per {unit}. Write a linear function $C(x)$ that "
                f"gives the total cost for $x$ {unit}s."
            ),
            answer_latex=f"${answer}$",
            hints=[
                "A linear cost model has the form $C(x) = (\\text{rate}) \\cdot x + (\\text{flat fee})$.",
                f"The rate is $\\${R}$ per {unit} and the flat fee is $\\${F}$.",
            ],
            solution_steps_latex=[
                "Identify the per-unit rate and the flat fee.",
                f"Per-unit rate: $\\${R}$ per {unit}. Flat fee: $\\${F}$.",
                f"Assemble: $C(x) = {R}x + {F}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-modeling"],
        )


@register
class LinearModelPredictValue(Generator):
    """Given initial value y0 and rate m per x-unit, find Y when X = x_target."""
    generator_id = "linear_model_predict_value"
    topic_slug = "modeling_with_linear_functions"
    display_name = "Use a linear model to predict Y at a given X"
    supports_word_problems = True

    _M_RANGES = {"easy": (2, 10), "medium": (3, 18), "hard": (4, 30)}
    _Y0_RANGES = {"easy": (5, 40), "medium": (10, 80), "hard": (20, 150)}
    _X_RANGES = {"easy": (1, 10), "medium": (2, 15), "hard": (3, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        y0_lo, y0_hi = self._Y0_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        y0 = rng.randint(y0_lo, y0_hi)
        x_target = rng.randint(x_lo, x_hi)
        place, fee_label, unit = rng.choice(_SCENARIOS)
        # sign: half the time decreasing
        if rng.random() < 0.5:
            m = -m

        y_target = m * x_target + y0  # backward guarantee integer

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, y0, x_target, place, unit)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A quantity $y$ starts at $y_0 = {y0}$ and changes by ${m}$ "
                f"for each additional unit of $x$ (here, per {unit}). "
                f"Using the linear model $y = {m}x + {y0}$, find $y$ when $x = {x_target}$."
            ),
            answer_latex=f"$y = {y_target}$",
            hints=[
                r"Substitute $x = x_0$ into the linear model $y = mx + y_0$.",
                f"Here $m = {m}$, $y_0 = {y0}$, and $x = {x_target}$.",
            ],
            solution_steps_latex=[
                f"Start with the model $y = {m}x + {y0}$.",
                f"Substitute $x = {x_target}$: $y = ({m})({x_target}) + {y0}$.",
                f"Simplify: $y = {m * x_target} + {y0} = {y_target}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-modeling"],
        )


@register
class LinearModelFindInputForOutput(Generator):
    """Given y = mx + b, find x when y = y_target. Clean-integer x."""
    generator_id = "linear_model_find_input_for_output"
    topic_slug = "modeling_with_linear_functions"
    display_name = "Use a linear model to find X for a target Y"
    supports_word_problems = True

    _M_RANGES = {"easy": (2, 9), "medium": (2, 15), "hard": (3, 25)}
    _B_RANGES = {"easy": (5, 40), "medium": (10, 80), "hard": (20, 150)}
    _X_RANGES = {"easy": (1, 10), "medium": (2, 18), "hard": (3, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        x_ans = rng.randint(x_lo, x_hi)
        # sign: half the time the rate is negative
        if rng.random() < 0.5:
            m = -m
        y_target = m * x_ans + b  # backward: clean integer x_ans

        place, fee_label, unit = rng.choice(_SCENARIOS)
        model_latex = _render_linear(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b, y_target, place, unit)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A linear model is given by ${model_latex}$. Find the value "
                f"of $x$ that makes $y = {y_target}$."
            ),
            answer_latex=f"$x = {x_ans}$",
            hints=[
                f"Substitute $y = {y_target}$ into the model and solve for $x$.",
                f"You get ${m}x + ({b}) = {y_target}$.",
                f"Isolate $x$: subtract ${b}$, then divide by ${m}$.",
            ],
            solution_steps_latex=[
                f"Set $y = {y_target}$: ${m}x + ({b}) = {y_target}$.",
                f"Subtract ${b}$: ${m}x = {y_target - b}$.",
                f"Divide by ${m}$: $x = \\dfrac{{{y_target - b}}}{{{m}}} = {x_ans}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-modeling"],
        )


# ===========================================================================
# Topic 5: graphing_linear_equations_from_tables
# ===========================================================================

@register
class TableEvaluateLinear(Generator):
    """Given y = mx + b, compute y-values for a list of x-values. Output as a table."""
    generator_id = "table_evaluate_linear"
    topic_slug = "graphing_linear_equations_from_tables"
    display_name = "Fill in a table of (x, y) values from y = mx + b"

    _M_RANGES = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-20, 20)}
    _B_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}
    _X_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        # Pick 4 distinct x values
        xs: list[int] = []
        attempts = 0
        while len(xs) < 4 and attempts < 50:
            candidate = rng.randint(x_lo, x_hi)
            if candidate not in xs:
                xs.append(candidate)
            attempts += 1
        xs.sort()
        ys = [m * x + b for x in xs]

        eq_latex = _render_linear(m, b)
        # Build a LaTeX array / matrix table for the statement:
        x_row = " & ".join(str(x) for x in xs)
        y_row = " & ".join("?" for _ in xs)
        col_spec = "|c|" + "c|" * len(xs)
        table_statement = (
            r"\begin{array}{" + col_spec + "}\\hline "
            rf"x & {x_row} \\\hline "
            rf"y & {y_row} \\\hline "
            r"\end{array}"
        )

        # Build the answer list
        pair_strs = ", ".join(f"({x},\\;{y})" for x, y in zip(xs, ys))
        answer = f"({pair_strs})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b, tuple(xs))),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the equation ${eq_latex}$, fill in the missing $y$ "
                f"values in the table: $${table_statement}$$"
            ),
            answer_latex=f"${answer}$",
            hints=[
                f"Substitute each $x$-value into ${eq_latex}$ and simplify.",
                "Line up the output $y$ with the matching $x$ in the table.",
            ],
            solution_steps_latex=[
                f"Substitute each $x$ into ${eq_latex}$.",
                " ".join(
                    f"$x = {x}$: $y = ({m})({x}) + ({b}) = {y}$."
                    for x, y in zip(xs, ys)
                ),
                f"Table of $(x, y)$ pairs: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-formula-substitution"],
        )


@register
class TableIsLinearCheck(Generator):
    """Given a table of (x, y) pairs with equally-spaced x-values, determine whether linear."""
    generator_id = "table_is_linear_check"
    topic_slug = "graphing_linear_equations_from_tables"
    display_name = "Check whether a table of (x, y) values is linear"
    bank_count_per_difficulty = 40  # two categories, keep parameter space modest

    _M_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _B_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}
    _X_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]

        category = rng.choice(["linear", "not_linear"])
        # Build 4 x-values with constant step
        step = rng.choice([1, 2, 3])
        start = rng.randint(x_lo, x_hi - 3 * step)
        xs = [start + i * step for i in range(4)]

        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        ys = [m * x + b for x in xs]

        if category == "not_linear":
            # Perturb one y (not the first) by a nonzero delta to break linearity.
            idx = rng.choice([1, 2, 3])
            delta = rng.choice([-3, -2, -1, 1, 2, 3])
            ys[idx] += delta

        x_row = " & ".join(str(x) for x in xs)
        y_row = " & ".join(str(y) for y in ys)
        col_spec = "|c|" + "c|" * len(xs)
        table_latex = (
            r"\begin{array}{" + col_spec + "}\\hline "
            rf"x & {x_row} \\\hline "
            rf"y & {y_row} \\\hline "
            r"\end{array}"
        )

        if category == "linear":
            answer_label = f"Linear. The slope is $m = {m}$."
        else:
            answer_label = "Not linear."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (category, m, b, tuple(xs), tuple(ys))),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Determine whether the following table of values is linear. "
                "If it is, state the slope. $$" + table_latex + "$$"
            ),
            answer_latex=answer_label,
            hints=[
                "A table represents a linear relationship when the first differences "
                "($\\Delta y$ for equal $\\Delta x$) are constant.",
                r"Compute $\Delta y$ between consecutive rows and check that all values match.",
                "If they match, the constant first difference divided by the step in $x$ equals the slope.",
            ],
            solution_steps_latex=[
                f"Check that $x$-values increase by a constant step (here, $\\Delta x = {step}$).",
                "Compute consecutive differences in $y$: "
                + ", ".join(f"${ys[i + 1] - ys[i]}$" for i in range(len(ys) - 1))
                + ".",
                "If these are all equal, the data is linear; otherwise it is not.",
                f"Conclusion: {answer_label}",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-visualization"],
        )


@register
class TableFindEquationFromTable(Generator):
    """Given a linear table, derive y = mx + b from the first two rows."""
    generator_id = "table_find_equation_from_table"
    topic_slug = "graphing_linear_equations_from_tables"
    display_name = "Find y = mx + b from a table of (x, y) values"

    _M_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _B_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}
    _X_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        # 4 distinct x-values, sorted
        xs: list[int] = []
        attempts = 0
        while len(xs) < 4 and attempts < 50:
            candidate = rng.randint(x_lo, x_hi)
            if candidate not in xs:
                xs.append(candidate)
            attempts += 1
        xs.sort()
        ys = [m * x + b for x in xs]

        x_row = " & ".join(str(x) for x in xs)
        y_row = " & ".join(str(y) for y in ys)
        col_spec = "|c|" + "c|" * len(xs)
        table_latex = (
            r"\begin{array}{" + col_spec + "}\\hline "
            rf"x & {x_row} \\\hline "
            rf"y & {y_row} \\\hline "
            r"\end{array}"
        )

        answer = _render_linear(m, b)
        dy = ys[1] - ys[0]
        dx = xs[1] - xs[0]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b, tuple(xs))),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "The values in the table below lie on a line. Write the equation "
                "in slope-intercept form. $$" + table_latex + "$$"
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Use the first two rows to find the slope $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.",
                f"Then substitute one row into $y = mx + b$ to solve for $b$.",
            ],
            solution_steps_latex=[
                f"Slope from first two rows: $m = \\dfrac{{{ys[1]} - ({ys[0]})}}{{{xs[1]} - ({xs[0]})}} "
                f"= \\dfrac{{{dy}}}{{{dx}}} = {m}$.",
                f"Substitute $({xs[0]}, {ys[0]})$: ${ys[0]} = ({m})({xs[0]}) + b$, so $b = {b}$.",
                f"Equation: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )
