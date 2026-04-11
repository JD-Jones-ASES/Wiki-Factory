"""Coordinate-geometry-proof generators (Cluster 10).

Topic slug: ``coordinate_geometry_proofs``.

Four generators:

- coord_prove_parallelogram_slope: check opposite sides have equal slopes
- coord_prove_rectangle_perpendicular: check adjacent sides are perpendicular (slopes multiply to -1)
- coord_prove_rhombus_distances: check all four sides have equal length (distance formula)
- coord_midpoint_of_segment: basic drill, midpoint formula
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_fraction, format_point


TOPIC_SLUG = "coordinate_geometry_proofs"


def _slope_latex(x1, y1, x2, y2) -> str:
    """Return the slope from (x1,y1) to (x2,y2) as a LaTeX fraction or integer."""
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        return r"\text{undefined}"
    f = Fraction(dy, dx)
    return format_fraction(f.numerator, f.denominator)


# ---------------------------------------------------------------------------

@register
class CoordProveParallelogramSlope(Generator):
    """Given four vertices of a parallelogram, verify opposite sides have equal slopes."""
    generator_id = "coord_prove_parallelogram_slope"
    topic_slug = TOPIC_SLUG
    display_name = "Prove parallelogram via slope of opposite sides"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Backward-construct a parallelogram: choose A, vector u = B-A, vector v = D-A
        # Then C = A + u + v.
        ax = rng.randint(lo, hi)
        ay = rng.randint(lo, hi)
        ux = rng.randint(1, hi - lo)
        uy = rng.randint(lo, hi)
        vx = rng.randint(lo, hi)
        vy = rng.randint(1, hi - lo)
        # Keep u and v non-parallel
        if ux * vy - uy * vx == 0:
            vx = vx + 1

        bx, by = ax + ux, ay + uy
        dx, dy = ax + vx, ay + vy
        cx, cy = ax + ux + vx, ay + uy + vy
        slope_ab = _slope_latex(ax, ay, bx, by)
        slope_dc = _slope_latex(dx, dy, cx, cy)
        slope_ad = _slope_latex(ax, ay, dx, dy)
        slope_bc = _slope_latex(bx, by, cx, cy)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (ax, ay, ux, uy, vx, vy)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Four points $A = {format_point(ax, ay)}$, $B = {format_point(bx, by)}$, "
                f"$C = {format_point(cx, cy)}$, $D = {format_point(dx, dy)}$ are the vertices "
                f"of a quadrilateral (in order). Compute the slopes of sides $AB$ and $DC$ "
                f"to show that $ABCD$ is a parallelogram."
            ),
            answer_latex=(
                f"Slope $AB = {slope_ab}$, slope $DC = {slope_dc}$. Equal, so $AB \\parallel DC$. "
                f"Slope $AD = {slope_ad}$, slope $BC = {slope_bc}$, so $AD \\parallel BC$."
            ),
            hints=[
                r"A parallelogram has two pairs of parallel sides.",
                r"Use the slope formula $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ on each side.",
                r"If opposite sides have equal slopes, they are parallel.",
            ],
            solution_steps_latex=[
                f"Slope of $AB$: $\\dfrac{{{by} - ({ay})}}{{{bx} - ({ax})}} = {slope_ab}$.",
                f"Slope of $DC$: $\\dfrac{{{cy} - ({dy})}}{{{cx} - ({dx})}} = {slope_dc}$.",
                f"Since slope $AB =$ slope $DC$, sides $AB$ and $DC$ are parallel.",
                f"Similarly, slope of $AD$: ${slope_ad}$ and slope of $BC$: ${slope_bc}$, so $AD \\parallel BC$.",
                f"Both pairs of opposite sides are parallel, so $ABCD$ is a parallelogram.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class CoordProveRectanglePerpendicular(Generator):
    """Check adjacent sides of a rectangle are perpendicular (slopes multiply to -1)."""
    generator_id = "coord_prove_rectangle_perpendicular"
    topic_slug = TOPIC_SLUG
    display_name = "Prove rectangle via perpendicular adjacent sides"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-14, 14)}
    _BASE_DELTAS = [(1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                    (1, 1), (2, 2), (3, 3), (1, -1), (2, -2), (3, -3), (2, 1), (1, 2)]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        ax = rng.randint(lo, hi)
        ay = rng.randint(lo, hi)
        # Choose a direction vector u = (p, q) for side AB, and perpendicular v = (-q, p) for side AD
        p, q = rng.choice(self._BASE_DELTAS)
        # Scale by a positive integer to vary size
        scale_u = rng.randint(1, 3)
        scale_v = rng.randint(1, 3)
        ux, uy = scale_u * p, scale_u * q
        vx, vy = scale_v * (-q), scale_v * p

        bx, by = ax + ux, ay + uy
        dx, dy = ax + vx, ay + vy
        cx, cy = ax + ux + vx, ay + uy + vy

        slope_ab = _slope_latex(ax, ay, bx, by)
        slope_ad = _slope_latex(ax, ay, dx, dy)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (ax, ay, ux, uy, vx, vy)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A quadrilateral $ABCD$ has vertices $A = {format_point(ax, ay)}$, "
                f"$B = {format_point(bx, by)}$, $C = {format_point(cx, cy)}$, "
                f"$D = {format_point(dx, dy)}$. The figure is already a parallelogram. "
                f"Compute the slopes of adjacent sides $AB$ and $AD$ and show their product "
                f"equals $-1$, proving $ABCD$ is a rectangle."
            ),
            answer_latex=(
                f"Slope $AB = {slope_ab}$, slope $AD = {slope_ad}$. "
                f"Product $= -1$, so $AB \\perp AD$ and $ABCD$ is a rectangle."
            ),
            hints=[
                r"Two lines are perpendicular when the product of their slopes is $-1$.",
                r"Compute slope $AB = \dfrac{y_B - y_A}{x_B - x_A}$ and slope $AD$ similarly.",
                "Multiply the two slopes; if the result is $-1$, the sides are perpendicular.",
            ],
            solution_steps_latex=[
                f"Slope of $AB$: $\\dfrac{{{by} - ({ay})}}{{{bx} - ({ax})}} = {slope_ab}$.",
                f"Slope of $AD$: $\\dfrac{{{dy} - ({ay})}}{{{dx} - ({ax})}} = {slope_ad}$.",
                f"Multiply: $({slope_ab}) \\cdot ({slope_ad}) = -1$.",
                f"Since the product of slopes is $-1$, $AB \\perp AD$. A parallelogram with a right angle is a rectangle.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class CoordProveRhombusDistances(Generator):
    """Check all four sides of a rhombus are congruent via distance formula."""
    generator_id = "coord_prove_rhombus_distances"
    topic_slug = TOPIC_SLUG
    display_name = "Prove rhombus via equal side lengths (distance formula)"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (-20, 20), "medium": (-30, 30), "hard": (-40, 40)}
    # Pythagorean triples (a, b, c): a, b are the half-diagonal legs, c is the side
    _TRIPLES_BY_DIFF = {
        "easy": [(3, 4, 5), (6, 8, 10)],
        "medium": [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)],
        "hard": [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (9, 12, 15),
                 (7, 24, 25), (12, 16, 20), (20, 21, 29)],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a, b, c = rng.choice(self._TRIPLES_BY_DIFF[difficulty])
        m = max(a, b)
        # Ensure there's room for the rhombus vertices inside [lo, hi]
        cx_lo = lo + m
        cx_hi = hi - m
        if cx_hi < cx_lo:
            cx_lo, cx_hi = -m, m
        cx = rng.randint(cx_lo, cx_hi)
        cy = rng.randint(cx_lo, cx_hi)
        # Vertices along perpendicular diagonals: (cx ± a, cy) and (cx, cy ± b)
        v1 = (cx - a, cy)
        v2 = (cx, cy - b)
        v3 = (cx + a, cy)
        v4 = (cx, cy + b)

        ax, ay = v1
        bx, by = v2
        cxv, cyv = v3
        dx, dy = v4
        side_len_sq = a * a + b * b
        side_len = c

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (cx, cy, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A quadrilateral has vertices $A = {format_point(ax, ay)}$, "
                f"$B = {format_point(bx, by)}$, $C = {format_point(cxv, cyv)}$, "
                f"$D = {format_point(dx, dy)}$. Use the distance formula to show that all four "
                f"sides have the same length, proving the quadrilateral is a rhombus."
            ),
            answer_latex=f"All four side lengths equal ${side_len}$, so $ABCD$ is a rhombus.",
            hints=[
                r"Distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
                "Compute each side length: $AB$, $BC$, $CD$, $DA$.",
                "If all four lengths are equal, the quadrilateral is a rhombus.",
            ],
            solution_steps_latex=[
                f"Length of $AB$: $\\sqrt{{({bx} - ({ax}))^2 + ({by} - ({ay}))^2}} = \\sqrt{{{(bx - ax) ** 2} + {(by - ay) ** 2}}} = \\sqrt{{{side_len_sq}}} = {side_len}$.",
                f"Length of $BC$: by the same method, $= {side_len}$.",
                f"Length of $CD$: $= {side_len}$.",
                f"Length of $DA$: $= {side_len}$.",
                f"All four sides have length ${side_len}$, so $ABCD$ is a rhombus.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class CoordMidpointOfSegment(Generator):
    """Basic drill: find the midpoint of a segment given two endpoints."""
    generator_id = "coord_midpoint_of_segment"
    topic_slug = TOPIC_SLUG
    display_name = "Find the midpoint of a segment"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (-12, 12), "medium": (-20, 20), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Choose endpoints whose sum is even so the midpoint is an integer pair
        while True:
            x1 = rng.randint(lo, hi)
            x2 = rng.randint(lo, hi)
            if (x1 + x2) % 2 == 0 and x1 != x2:
                break
        while True:
            y1 = rng.randint(lo, hi)
            y2 = rng.randint(lo, hi)
            if (y1 + y2) % 2 == 0 and y1 != y2:
                break
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the midpoint of the segment joining "
                f"${format_point(x1, y1)}$ and ${format_point(x2, y2)}$."
            ),
            answer_latex=f"${format_point(mx, my)}$",
            hints=[
                r"The midpoint formula: $M = \left( \dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2} \right)$.",
                f"Sum of $x$-coordinates: ${x1} + {x2} = {x1 + x2}$.",
                f"Sum of $y$-coordinates: ${y1} + {y2} = {y1 + y2}$.",
            ],
            solution_steps_latex=[
                r"Use the midpoint formula: $M = \left( \dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2} \right)$.",
                f"Substitute: $M = \\left( \\dfrac{{{x1} + {x2}}}{{2}}, \\dfrac{{{y1} + {y2}}}{{2}} \\right)$.",
                f"Simplify: $M = \\left( \\dfrac{{{x1 + x2}}}{{2}}, \\dfrac{{{y1 + y2}}}{{2}} \\right) = {format_point(mx, my)}$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )
