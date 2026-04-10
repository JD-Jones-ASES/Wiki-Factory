"""Circle problem generators.

Five Phase 1 generators covering the foundational circle problem types:

- circles_equation_from_center_radius    (standard form from center + radius)
- circles_center_radius_from_equation    (reverse: read off center + radius)
- circles_area_from_radius               (area = pi * r^2)
- circles_circumference_from_radius      (C = 2 * pi * r)
- circles_area_from_diameter             (multi-step: r = d/2, then area)

All problems keep answers as exact integers or integer multiples of pi
so that verification and rendering stay simple.
"""
from __future__ import annotations

import random

from ..base import Generator, Problem, Difficulty, make_problem_id, register
from ..latex_helpers import shift_expr, format_point


# ---------------------------------------------------------------------------

@register
class CircleEquationFromCenterRadius(Generator):
    """Build the standard form equation from a center and radius."""
    generator_id = "circles_equation_from_center_radius"
    topic_slug = "circles"
    display_name = "Find circle equation from center and radius"

    _HK_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _R_MAXES = {"easy": 10, "medium": 15, "hard": 20}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._HK_RANGES[difficulty]
        r_max = self._R_MAXES[difficulty]
        h = rng.randint(lo, hi)
        k = rng.randint(lo, hi)
        r = rng.randint(1, r_max)

        eq_lhs = f"{shift_expr('x', h)}^2 + {shift_expr('y', k)}^2"
        eq_rhs = f"{r * r}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, r)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the equation of the circle with center "
                f"${format_point(h, k)}$ and radius ${r}$."
            ),
            answer_latex=f"${eq_lhs} = {eq_rhs}$",
            hints=[
                r"Recall the standard form of a circle: $(x - h)^2 + (y - k)^2 = r^2$.",
                f"Here the center is $(h, k) = {format_point(h, k)}$ and the radius is $r = {r}$.",
                f"Substitute, then square the radius: $r^2 = {r * r}$.",
            ],
            solution_steps_latex=[
                r"Start with the standard form: $(x - h)^2 + (y - k)^2 = r^2$.",
                f"Substitute the center $(h, k) = {format_point(h, k)}$: ${eq_lhs} = r^2$.",
                f"Substitute $r = {r}$ and compute $r^2 = {r * r}$: ${eq_lhs} = {eq_rhs}$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class CircleCenterRadiusFromEquation(Generator):
    """Read off the center and radius from a standard-form equation."""
    generator_id = "circles_center_radius_from_equation"
    topic_slug = "circles"
    display_name = "Find center and radius from circle equation"

    _HK_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _R_MAXES = {"easy": 10, "medium": 15, "hard": 20}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._HK_RANGES[difficulty]
        r_max = self._R_MAXES[difficulty]
        h = rng.randint(lo, hi)
        k = rng.randint(lo, hi)
        r = rng.randint(1, r_max)

        equation = f"{shift_expr('x', h)}^2 + {shift_expr('y', k)}^2 = {r * r}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, r)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the center and radius of the circle with equation ${equation}$."
            ),
            answer_latex=f"Center $= {format_point(h, k)}$, radius $= {r}$",
            hints=[
                r"Compare to the standard form: $(x - h)^2 + (y - k)^2 = r^2$.",
                r"Read $h$ and $k$ directly from the equation. Watch the signs --- "
                r"$(x - h)$ means $h$ is whatever is subtracted.",
                f"The right side equals $r^2$, so take its square root.",
            ],
            solution_steps_latex=[
                r"Compare term by term to $(x - h)^2 + (y - k)^2 = r^2$.",
                f"Match the $x$-term: $h = {h}$. Match the $y$-term: $k = {k}$.",
                f"The right side is $r^2 = {r * r}$, so $r = \\sqrt{{{r * r}}} = {r}$.",
                f"Center: ${format_point(h, k)}$. Radius: ${r}$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class CircleAreaFromRadius(Generator):
    """Compute the area given the radius, answer in terms of pi."""
    generator_id = "circles_area_from_radius"
    topic_slug = "circles"
    display_name = "Find circle area from radius"

    _R_RANGES = {"easy": (1, 30), "medium": (5, 80), "hard": (10, 200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]
        r = rng.randint(lo, hi)
        area_coefficient = r * r

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the area of a circle with radius ${r}$. "
                r"Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${area_coefficient}\\pi$",
            hints=[
                r"Recall the area formula for a circle: $A = \pi r^2$.",
                f"Here $r = {r}$.",
                f"Square the radius: $r^2 = {r * r}$.",
            ],
            solution_steps_latex=[
                r"Use the area formula $A = \pi r^2$.",
                f"Substitute $r = {r}$: $A = \\pi \\cdot {r}^2$.",
                f"Simplify: $A = {area_coefficient}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class CircleCircumferenceFromRadius(Generator):
    """Compute the circumference given the radius, answer in terms of pi."""
    generator_id = "circles_circumference_from_radius"
    topic_slug = "circles"
    display_name = "Find circle circumference from radius"

    _R_RANGES = {"easy": (1, 30), "medium": (5, 80), "hard": (10, 200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]
        r = rng.randint(lo, hi)
        circ_coefficient = 2 * r

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the circumference of a circle with radius ${r}$. "
                r"Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${circ_coefficient}\\pi$",
            hints=[
                r"Recall the circumference formula: $C = 2\pi r$.",
                f"Here $r = {r}$.",
                f"Multiply: $2 \\cdot {r} = {circ_coefficient}$.",
            ],
            solution_steps_latex=[
                r"Use the circumference formula $C = 2\pi r$.",
                f"Substitute $r = {r}$: $C = 2\\pi \\cdot {r}$.",
                f"Simplify: $C = {circ_coefficient}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class CircleAreaFromDiameter(Generator):
    """Multi-step: convert diameter to radius, then compute area."""
    generator_id = "circles_area_from_diameter"
    topic_slug = "circles"
    display_name = "Find circle area from diameter"

    # Only even diameters so r stays a clean integer.
    _D_RANGES = {"easy": (2, 60), "medium": (10, 160), "hard": (20, 400)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._D_RANGES[difficulty]
        d = 2 * rng.randint(lo // 2, hi // 2)
        r = d // 2
        area_coefficient = r * r

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (d,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the area of a circle with diameter ${d}$. "
                r"Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${area_coefficient}\\pi$",
            hints=[
                r"First convert diameter to radius: $r = d / 2$.",
                f"Here $d = {d}$, so $r = {r}$.",
                r"Then use $A = \pi r^2$.",
            ],
            solution_steps_latex=[
                f"Find the radius: $r = d / 2 = {d} / 2 = {r}$.",
                f"Use the area formula $A = \\pi r^2$: $A = \\pi \\cdot {r}^2$.",
                f"Simplify: $A = {area_coefficient}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-multi-step"],
        )
