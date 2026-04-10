"""Slope-intercept form generators (Phase 2c Wave 2).

Canonical topic slug ``slope_intercept_form`` at
wiki/topics/pre_algebra/Slope_Intercept_Form.md (Math II Ch 8.6).

- slope_intercept_from_slope_and_point: given m and (x, y), write y = mx + b
- slope_intercept_from_two_points: given two points, write y = mx + b
- slope_intercept_identify_from_equation: given y = mx + b, state slope and y-intercept
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_fraction, format_point


def _render_linear(m: int, b: int) -> str:
    """Render y = mx + b in LaTeX with clean signs and 1/-1 coefficient handling."""
    if m == 0:
        return f"y = {b}"
    if m == 1:
        mx = "x"
    elif m == -1:
        mx = "-x"
    else:
        mx = f"{m}x"
    if b == 0:
        return f"y = {mx}"
    sign = "+" if b > 0 else "-"
    return f"y = {mx} {sign} {abs(b)}"


# ---------------------------------------------------------------------------

@register
class SlopeInterceptFromSlopeAndPoint(Generator):
    """Given slope m and a point (x1, y1), write the line in slope-intercept form."""
    generator_id = "slope_intercept_from_slope_and_point"
    topic_slug = "slope_intercept_form"
    display_name = "Write y = mx + b given slope and a point"

    _RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        m = rng.randint(lo, hi)
        while m == 0:
            m = rng.randint(lo, hi)
        x1 = rng.randint(lo, hi)
        y1 = rng.randint(lo, hi)
        # b = y1 - m * x1
        b = y1 - m * x1

        answer = _render_linear(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, x1, y1)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the line with slope $m = {m}$ that passes "
                f"through the point ${format_point(x1, y1)}$. Give your answer "
                "in slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Slope-intercept form is $y = mx + b$. You already know $m$ --- you need to find $b$.",
                rf"Substitute the known point $({x1}, {y1})$ into $y = mx + b$: ${y1} = ({m})({x1}) + b$.",
                f"Solve for $b$: $b = {y1} - ({m})({x1}) = {b}$.",
            ],
            solution_steps_latex=[
                f"Start with the slope-intercept template $y = mx + b$, using $m = {m}$.",
                f"Substitute the point $({x1}, {y1})$: ${y1} = ({m})({x1}) + b$.",
                f"Simplify: ${y1} = {m * x1} + b$, so $b = {y1} - {m * x1} = {b}$.",
                f"Write the equation: ${answer}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-linear", "#skill-multi-step"],
        )


@register
class SlopeInterceptFromTwoPoints(Generator):
    """Given two points, write the line in slope-intercept form (integer slope only)."""
    generator_id = "slope_intercept_from_two_points"
    topic_slug = "slope_intercept_form"
    display_name = "Write y = mx + b given two points"

    _M_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _X_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Construct forward: pick m (integer), pick b, pick two distinct x's, derive y's
        m_lo, m_hi = self._M_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        while m == 0:
            m = rng.randint(m_lo, m_hi)
        b = rng.randint(x_lo, x_hi)
        x1 = rng.randint(x_lo, x_hi)
        x2 = rng.randint(x_lo, x_hi)
        while x2 == x1:
            x2 = rng.randint(x_lo, x_hi)
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
                f"Write the equation of the line passing through the points "
                f"${format_point(x1, y1)}$ and ${format_point(x2, y2)}$. "
                "Give your answer in slope-intercept form."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Step 1: compute the slope $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.",
                f"Step 2: use $b = y_1 - m x_1$ to find the $y$-intercept.",
                f"Slope: $m = \\dfrac{{{dy}}}{{{dx}}} = {m}$. Intercept: $b = {y1} - ({m})({x1}) = {b}$.",
            ],
            solution_steps_latex=[
                f"Compute the slope: $m = \\dfrac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\dfrac{{{dy}}}{{{dx}}} = {m}$.",
                f"Find $b$ by substituting $({x1}, {y1})$: ${y1} = ({m})({x1}) + b$, so $b = {b}$.",
                f"Write the equation: ${answer}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-linear", "#skill-multi-step"],
        )


@register
class SlopeInterceptIdentify(Generator):
    """Given y = mx + b, state the slope and y-intercept."""
    generator_id = "slope_intercept_identify_from_equation"
    topic_slug = "slope_intercept_form"
    display_name = "Identify slope and y-intercept from y = mx + b"

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-30, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        m = rng.randint(lo, hi)
        while m == 0:
            m = rng.randint(lo, hi)
        b = rng.randint(lo, hi)

        equation = _render_linear(m, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Identify the slope and $y$-intercept of ${equation}$.",
            answer_latex=f"Slope $m = {m}$, $y$-intercept $= {b}$",
            hints=[
                r"Slope-intercept form is $y = mx + b$ where $m$ is the slope and $b$ is the $y$-intercept.",
                r"Match the coefficient of $x$ with $m$, and the constant term with $b$.",
            ],
            solution_steps_latex=[
                r"Compare ${y = mx + b}$ with the given equation.",
                f"The coefficient of $x$ is ${m}$, so $m = {m}$.",
                f"The constant term is ${b}$, so $b = {b}$.",
                f"Slope: ${m}$. $y$-intercept: ${b}$ (point $(0, {b})$).",
            ],
            tags=["#branch-pre-algebra", "#topic-linear", "#skill-visualization"],
        )
