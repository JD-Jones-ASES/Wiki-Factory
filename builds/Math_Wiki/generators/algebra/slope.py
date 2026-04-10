"""Slope generators (Phase 2c Wave 1).

Covers the canonical topic slug ``slope`` at wiki/topics/algebra/Slope.md:

- slope_from_two_points: given two points, compute the slope m = (y2-y1)/(x2-x1)
- slope_from_slope_intercept: given y = mx + b, read off the slope
- slope_classify_from_points: classify as positive/negative/zero/undefined
- slope_parallel_perpendicular: given a slope, find parallel and perpendicular slopes
"""
from __future__ import annotations

import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_fraction, format_point


# ---------------------------------------------------------------------------

@register
class SlopeFromTwoPoints(Generator):
    """Given two points (x1,y1), (x2,y2), compute the slope."""
    generator_id = "slope_from_two_points"
    topic_slug = "slope"
    display_name = "Find slope from two points"

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Keep x1 != x2 so slope is defined.
        while True:
            x1 = rng.randint(lo, hi)
            x2 = rng.randint(lo, hi)
            if x2 != x1:
                break
        y1 = rng.randint(lo, hi)
        y2 = rng.randint(lo, hi)
        dx = x2 - x1
        dy = y2 - y1
        slope = Fraction(dy, dx)
        slope_latex = format_fraction(slope.numerator, slope.denominator)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the slope of the line passing through the points "
                f"${format_point(x1, y1)}$ and ${format_point(x2, y2)}$."
            ),
            answer_latex=f"$m = {slope_latex}$",
            hints=[
                r"The slope formula is $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.",
                f"Here $(x_1, y_1) = {format_point(x1, y1)}$ and $(x_2, y_2) = {format_point(x2, y2)}$.",
                f"Compute the rise: ${y2} - ({y1}) = {dy}$.",
                f"Compute the run: ${x2} - ({x1}) = {dx}$.",
            ],
            solution_steps_latex=[
                r"Use the slope formula $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.",
                f"Substitute: $m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\dfrac{{{dy}}}{{{dx}}}$.",
                f"Simplify: $m = {slope_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-formula-substitution"],
        )


@register
class SlopeFromSlopeInterceptForm(Generator):
    """Given y = mx + b in slope-intercept form, read off the slope."""
    generator_id = "slope_from_slope_intercept_form"
    topic_slug = "slope"
    display_name = "Find slope from y = mx + b"

    _RANGES = {"easy": (-9, 9), "medium": (-20, 20), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        m = rng.randint(lo, hi)
        while m == 0:
            m = rng.randint(lo, hi)
        b = rng.randint(lo, hi)

        xs = sp.Symbol("x")
        eq_latex = sp.latex(sp.Eq(sp.Symbol("y"), m * xs + b))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find the slope of the line ${eq_latex}$.",
            answer_latex=f"$m = {m}$",
            hints=[
                r"Slope-intercept form is $y = mx + b$, where $m$ is the slope.",
                r"Match the coefficient of $x$ with $m$.",
                f"The coefficient of $x$ is ${m}$.",
            ],
            solution_steps_latex=[
                r"Compare ${y = mx + b}$ with the given equation.",
                f"The coefficient of $x$ is ${m}$, so the slope is $m = {m}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-visualization"],
        )


@register
class ClassifySlopeFromPoints(Generator):
    """Given two points, classify the slope of the line through them."""
    generator_id = "slope_classify_from_points"
    topic_slug = "slope"
    display_name = "Classify slope as positive, negative, zero, or undefined"
    bank_count_per_difficulty = 40  # small parameter space, but 4 categories

    _RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick category uniformly to guarantee variety.
        category = rng.choice(["positive", "negative", "zero", "undefined"])
        while True:
            x1 = rng.randint(lo, hi)
            x2 = rng.randint(lo, hi)
            y1 = rng.randint(lo, hi)
            y2 = rng.randint(lo, hi)
            if category == "zero":
                y2 = y1
                if x1 == x2:
                    continue
                break
            if category == "undefined":
                x2 = x1
                if y1 == y2:
                    continue
                break
            if x1 == x2:
                continue
            if category == "positive" and (y2 - y1) * (x2 - x1) > 0:
                break
            if category == "negative" and (y2 - y1) * (x2 - x1) < 0:
                break

        answer_label = {
            "positive": "positive",
            "negative": "negative",
            "zero": "zero (horizontal line)",
            "undefined": "undefined (vertical line)",
        }[category]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Classify the slope of the line through "
                f"${format_point(x1, y1)}$ and ${format_point(x2, y2)}$ as "
                "positive, negative, zero, or undefined."
            ),
            answer_latex=answer_label,
            hints=[
                r"Slope is $m = \dfrac{\text{rise}}{\text{run}}$. If the run is $0$, the slope is undefined (vertical line). If the rise is $0$, the slope is $0$ (horizontal line).",
                f"Rise: ${y2} - ({y1}) = {y2 - y1}$.",
                f"Run: ${x2} - ({x1}) = {x2 - x1}$.",
            ],
            solution_steps_latex=[
                f"Compute rise $= {y2} - ({y1}) = {y2 - y1}$ and run $= {x2} - ({x1}) = {x2 - x1}$.",
                "If run is $0$: vertical line, undefined slope. "
                "If rise is $0$: horizontal line, zero slope. "
                "Otherwise, check the sign of rise/run.",
                f"Here the slope is {answer_label}.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-visualization"],
        )


@register
class ParallelPerpendicularSlope(Generator):
    """Given a line's slope m, state the slope of a parallel and perpendicular line."""
    generator_id = "slope_parallel_perpendicular"
    topic_slug = "slope"
    display_name = "Find slopes of parallel and perpendicular lines"

    _RANGES = {"easy": (1, 8), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        numer = rng.randint(lo, hi)
        denom = rng.randint(lo, hi)
        # 50/50 sign
        if rng.random() < 0.5:
            numer = -numer
        m = Fraction(numer, denom)
        parallel = m
        perpendicular = -Fraction(m.denominator, m.numerator)

        m_latex = format_fraction(m.numerator, m.denominator)
        par_latex = format_fraction(parallel.numerator, parallel.denominator)
        perp_latex = format_fraction(perpendicular.numerator, perpendicular.denominator)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (numer, denom)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A line has slope $m = {m_latex}$. "
                "Find the slope of any line parallel to it, and the slope of any line perpendicular to it."
            ),
            answer_latex=f"Parallel: ${par_latex}$. Perpendicular: ${perp_latex}$.",
            hints=[
                "Parallel lines have the **same** slope.",
                r"Perpendicular lines have slopes that are **negative reciprocals**: if $m$ is the slope of one line, the other is $-\dfrac{1}{m}$.",
                f"The negative reciprocal of ${m_latex}$ is ${perp_latex}$.",
            ],
            solution_steps_latex=[
                f"Parallel: the parallel line shares the same slope, so its slope is ${par_latex}$.",
                f"Perpendicular: the perpendicular line's slope is the negative reciprocal of ${m_latex}$.",
                f"Compute the reciprocal: $\\dfrac{{1}}{{{m_latex}}} = {format_fraction(m.denominator, m.numerator)}$.",
                f"Negate it: ${perp_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation"],
        )
