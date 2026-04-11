"""Midpoint formula generators.

Canonical topic slug ``the_midpoint_formula`` at
wiki/topics/pre_algebra/The_Midpoint_Formula.md.

- midpoint_from_two_points: compute the midpoint of a segment in the plane
- endpoint_from_midpoint_and_other_endpoint: find the missing endpoint
- midpoint_on_number_line_1d: midpoint of two integers on the number line

All 2D generators use backward construction so the midpoint has clean
integer coordinates. The 1D generator picks two integers of the same
parity so the midpoint is also an integer.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_point


# ---------------------------------------------------------------------------

@register
class MidpointFromTwoPoints(Generator):
    """Given two points, compute the midpoint of the segment between them."""
    generator_id = "midpoint_from_two_points"
    topic_slug = "the_midpoint_formula"
    display_name = "Midpoint of two points"

    # (coord_range, offset_range) per difficulty. Offsets are added to and
    # subtracted from the midpoint, so endpoints stay symmetric about it.
    _PARAMS = {
        "easy":   {"mid_range": (-10, 10), "offset_range": (1, 5)},
        "medium": {"mid_range": (-20, 20), "offset_range": (1, 10)},
        "hard":   {"mid_range": (-50, 50), "offset_range": (2, 18)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        lo, hi = params["mid_range"]
        dlo, dhi = params["offset_range"]

        mx = rng.randint(lo, hi)
        my = rng.randint(lo, hi)
        dx = rng.randint(dlo, dhi)
        dy = rng.randint(dlo, dhi)

        x1 = mx - dx
        y1 = my - dy
        x2 = mx + dx
        y2 = my + dy

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the midpoint of the segment from ${format_point(x1, y1)}$ "
                f"to ${format_point(x2, y2)}$."
            ),
            answer_latex=f"${format_point(mx, my)}$",
            hints=[
                r"The midpoint formula averages the coordinates: $M = \left(\dfrac{x_1+x_2}{2},\ \dfrac{y_1+y_2}{2}\right)$.",
                rf"Average the $x$-coordinates: $\dfrac{{{x1}+{x2}}}{{2}} = \dfrac{{{x1 + x2}}}{{2}} = {mx}$.",
                rf"Average the $y$-coordinates: $\dfrac{{{y1}+{y2}}}{{2}} = \dfrac{{{y1 + y2}}}{{2}} = {my}$.",
            ],
            solution_steps_latex=[
                rf"Label the endpoints $(x_1, y_1) = {format_point(x1, y1)}$ and $(x_2, y_2) = {format_point(x2, y2)}$.",
                rf"Apply the midpoint formula: $M = \left(\dfrac{{{x1}+{x2}}}{{2}},\ \dfrac{{{y1}+{y2}}}{{2}}\right)$.",
                f"Simplify: $M = {format_point(mx, my)}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class EndpointFromMidpointAndOtherEndpoint(Generator):
    """Given a midpoint $M$ and one endpoint $A$, find the other endpoint $B$.

    Uses the relation $M = \\dfrac{A + B}{2}$, so $B = 2M - A$.
    """
    generator_id = "endpoint_from_midpoint_and_other_endpoint"
    topic_slug = "the_midpoint_formula"
    display_name = "Find the missing endpoint"

    _PARAMS = {
        "easy":   {"mid_range": (-8, 8),   "offset_range": (1, 6)},
        "medium": {"mid_range": (-20, 20), "offset_range": (2, 12)},
        "hard":   {"mid_range": (-50, 50), "offset_range": (3, 20)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        lo, hi = params["mid_range"]
        dlo, dhi = params["offset_range"]

        mx = rng.randint(lo, hi)
        my = rng.randint(lo, hi)
        dx = rng.randint(dlo, dhi)
        dy = rng.randint(dlo, dhi)
        # Randomly pick which side of the midpoint A sits on.
        side_x = rng.choice([-1, 1])
        side_y = rng.choice([-1, 1])

        ax = mx + side_x * dx
        ay = my + side_y * dy
        bx = 2 * mx - ax
        by = 2 * my - ay

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (ax, ay, mx, my)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"The midpoint of segment $AB$ is $M = {format_point(mx, my)}$. "
                f"One endpoint is $A = {format_point(ax, ay)}$. "
                f"Determine the coordinates of the other endpoint $B$."
            ),
            answer_latex=f"$B = {format_point(bx, by)}$",
            hints=[
                r"Since the midpoint averages the endpoints, $M = \dfrac{A + B}{2}$, so $B = 2M - A$.",
                rf"$B_x = 2 \cdot {mx} - {ax} = {bx}$.",
                rf"$B_y = 2 \cdot {my} - {ay} = {by}$.",
            ],
            solution_steps_latex=[
                rf"Set up the midpoint equation: $M = \dfrac{{A + B}}{{2}}$, so $B = 2M - A$.",
                rf"Compute the $x$-coordinate of $B$: $2({mx}) - ({ax}) = {bx}$.",
                rf"Compute the $y$-coordinate of $B$: $2({my}) - ({ay}) = {by}$.",
                f"So $B = {format_point(bx, by)}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-analytic-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class MidpointOnNumberLine1d(Generator):
    """Midpoint of two integers $a$ and $b$ on the number line.

    Uses backward construction: pick the midpoint and a positive offset,
    so $a = m - d$ and $b = m + d$ always share parity and the midpoint
    stays an integer.
    """
    generator_id = "midpoint_on_number_line_1d"
    topic_slug = "the_midpoint_formula"
    display_name = "Midpoint on the number line"

    _PARAMS = {
        "easy":   {"mid_range": (-15, 15),  "offset_range": (1, 8)},
        "medium": {"mid_range": (-40, 40),  "offset_range": (2, 18)},
        "hard":   {"mid_range": (-150, 150),"offset_range": (5, 40)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        mlo, mhi = params["mid_range"]
        dlo, dhi = params["offset_range"]
        midpoint = rng.randint(mlo, mhi)
        d = rng.randint(dlo, dhi)
        # Randomize which side is `a` vs `b` for variety.
        if rng.random() < 0.5:
            a = midpoint - d
            b = midpoint + d
        else:
            a = midpoint + d
            b = midpoint - d

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find the midpoint between ${a}$ and ${b}$ on the number line.",
            answer_latex=f"${midpoint}$",
            hints=[
                r"On a number line, the midpoint of $a$ and $b$ is their average: $\dfrac{a+b}{2}$.",
                rf"Add the two numbers: ${a} + {b} = {a + b}$.",
                rf"Divide by $2$: $\dfrac{{{a + b}}}{{2}} = {midpoint}$.",
            ],
            solution_steps_latex=[
                rf"The midpoint of ${a}$ and ${b}$ on a number line is $\dfrac{{{a} + {b}}}{{2}}$.",
                rf"Compute the sum: ${a} + {b} = {a + b}$.",
                rf"Divide by $2$: $\dfrac{{{a + b}}}{{2}} = {midpoint}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )
