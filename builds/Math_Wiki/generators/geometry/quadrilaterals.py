"""Quadrilateral generators (Cluster 10).

Topic slug: ``classifying_triangles_and_quadrilaterals``.

Four generators:

- quad_parallelogram_solve_angle: opposite angles equal, consecutive supplementary
- quad_rectangle_solve_diagonal: Pythagorean diagonal from sides
- quad_rhombus_solve_side: diagonals perpendicular bisectors, find side length
- quad_trapezoid_area: A = 1/2 * (b1 + b2) * h, backward construction
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "classifying_triangles_and_quadrilaterals"


# ---------------------------------------------------------------------------

@register
class QuadParallelogramSolveAngle(Generator):
    """Parallelogram: consecutive angles supplementary, solve for x."""
    generator_id = "quad_parallelogram_solve_angle"
    topic_slug = TOPIC_SLUG
    display_name = "Solve for x in a parallelogram angle"

    _RANGES = {"easy": (2, 15), "medium": (3, 25), "hard": (4, 35)}
    _COEFS = {"easy": (2, 6), "medium": (2, 9), "hard": (3, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._RANGES[difficulty]
        c_lo, c_hi = self._COEFS[difficulty]
        x = rng.randint(x_lo, x_hi)
        a = rng.randint(c_lo, c_hi)
        # Target: one angle = a*x + b, its supplement has measure (180 - (a*x + b))
        # Describe only the first angle and say consecutive angles are supplementary
        angle1 = a * x
        b = rng.randint(10, 90 - min(angle1, 80))
        angle1_val = a * x + b
        # Need angle1_val < 180 for the problem to make sense
        if angle1_val >= 175:
            b = 175 - a * x
            angle1_val = a * x + b
        angle2_val = 180 - angle1_val

        expr1 = f"({a}x + {b})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, x)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In parallelogram $ABCD$, $\\angle A = {expr1}^\\circ$ and "
                f"$\\angle B = {angle2_val}^\\circ$. The angles $A$ and $B$ are consecutive, "
                f"so they are supplementary. Determine the value of $x$."
            ),
            answer_latex=f"$x = {x}$",
            hints=[
                r"In a parallelogram, consecutive angles are supplementary: they sum to $180^\circ$.",
                f"Set up the equation: $({expr1}) + {angle2_val} = 180$.",
                f"Solve: $({a}x + {b}) = {180 - angle2_val}$, so ${a}x = {180 - angle2_val - b}$.",
            ],
            solution_steps_latex=[
                r"Property of parallelograms: consecutive angles are supplementary.",
                f"Write: ${expr1} + {angle2_val} = 180$.",
                f"Subtract ${angle2_val}$: ${expr1} = {180 - angle2_val}$.",
                f"Subtract ${b}$: ${a}x = {180 - angle2_val - b}$.",
                f"Divide by ${a}$: $x = {x}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class QuadRectangleSolveDiagonal(Generator):
    """Rectangle: use Pythagoras to find diagonal from sides."""
    generator_id = "quad_rectangle_solve_diagonal"
    topic_slug = TOPIC_SLUG
    display_name = "Find the diagonal of a rectangle"
    bank_count_per_difficulty = 20

    # Pythagorean triples for clean answers. Both (a, b) and (b, a) are included
    # explicitly so the parameter space doesn't depend on a 50/50 swap.
    _TRIPLES = [
        (3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13),
        (8, 15, 17), (15, 8, 17), (7, 24, 25), (24, 7, 25),
        (9, 12, 15), (12, 9, 15), (10, 24, 26), (24, 10, 26),
        (12, 16, 20), (16, 12, 20), (20, 21, 29), (21, 20, 29), (9, 40, 41),
        (15, 20, 25), (20, 15, 25), (12, 35, 37), (16, 30, 34), (30, 16, 34),
        (24, 32, 40), (32, 24, 40), (18, 24, 30), (24, 18, 30),
    ]

    _DIFFS = {
        "easy": [t for t in _TRIPLES if t[2] <= 17],
        "medium": [t for t in _TRIPLES if 10 <= t[2] <= 30],
        "hard": [t for t in _TRIPLES if t[2] >= 20],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c = rng.choice(self._DIFFS[difficulty])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A rectangle has length ${a}$ and width ${b}$. "
                f"Determine the exact length of its diagonal."
            ),
            answer_latex=f"${c}$",
            hints=[
                r"The diagonal of a rectangle, together with its length and width, forms a right triangle.",
                r"Apply the Pythagorean theorem: $d^2 = \ell^2 + w^2$.",
                f"Compute: ${a}^2 + {b}^2 = {a * a} + {b * b} = {a * a + b * b}$.",
            ],
            solution_steps_latex=[
                r"The diagonal of a rectangle forms a right triangle with the length and width.",
                f"Apply Pythagoras: $d^2 = {a}^2 + {b}^2 = {a * a + b * b}$.",
                f"Take the positive square root: $d = \\sqrt{{{a * a + b * b}}} = {c}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-multi-step"],
        )


# ---------------------------------------------------------------------------

@register
class QuadRhombusSolveSide(Generator):
    """Rhombus: diagonals are perpendicular bisectors. Find side length."""
    generator_id = "quad_rhombus_solve_side"
    topic_slug = TOPIC_SLUG
    display_name = "Find the side of a rhombus from its diagonals"
    bank_count_per_difficulty = 20

    # Double Pythagorean triples so the half-diagonals form a clean triple.
    # Both (a, b) and (b, a) are listed so the parameter space is large enough.
    _TRIPLES = [
        (3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13),
        (8, 15, 17), (15, 8, 17), (7, 24, 25), (24, 7, 25),
        (9, 12, 15), (12, 9, 15), (12, 16, 20), (16, 12, 20),
        (20, 21, 29), (21, 20, 29), (9, 40, 41), (15, 20, 25), (20, 15, 25),
        (12, 35, 37), (16, 30, 34), (30, 16, 34),
    ]

    _DIFFS = {
        "easy": [t for t in _TRIPLES if t[2] <= 17],
        "medium": [t for t in _TRIPLES if 10 <= t[2] <= 25],
        "hard": [t for t in _TRIPLES if t[2] >= 17],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        half_a, half_b, side = rng.choice(self._DIFFS[difficulty])
        d1 = 2 * half_a
        d2 = 2 * half_b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (d1, d2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A rhombus has diagonals of length ${d1}$ and ${d2}$. "
                f"Determine the length of each side of the rhombus."
            ),
            answer_latex=f"${side}$",
            hints=[
                r"The diagonals of a rhombus are perpendicular bisectors of each other.",
                r"They split the rhombus into four congruent right triangles whose legs are the half-diagonals.",
                f"So each side is the hypotenuse of a right triangle with legs $\\dfrac{{{d1}}}{{2}}$ and $\\dfrac{{{d2}}}{{2}}$.",
            ],
            solution_steps_latex=[
                "The diagonals bisect each other at right angles.",
                f"Half of the diagonals: $\\dfrac{{{d1}}}{{2}} = {d1 // 2}$ and $\\dfrac{{{d2}}}{{2}} = {d2 // 2}$.",
                f"Apply Pythagoras to the right triangle formed: $s^2 = {d1 // 2}^2 + {d2 // 2}^2 = {(d1 // 2) ** 2} + {(d2 // 2) ** 2} = {(d1 // 2) ** 2 + (d2 // 2) ** 2}$.",
                f"Take the positive root: $s = {side}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-multi-step"],
        )


# ---------------------------------------------------------------------------

@register
class QuadTrapezoidArea(Generator):
    """Trapezoid area: A = (b1 + b2) * h / 2. Backward-construct for integer A."""
    generator_id = "quad_trapezoid_area"
    topic_slug = TOPIC_SLUG
    display_name = "Find the area of a trapezoid"

    _RANGES = {"easy": (2, 12), "medium": (4, 25), "hard": (6, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Choose b1, b2, h so that (b1 + b2) is even (ensures integer A)
        while True:
            b1 = rng.randint(lo, hi)
            b2 = rng.randint(lo, hi)
            if b1 == b2:
                continue
            if (b1 + b2) % 2 == 0:
                break
        h = rng.randint(lo, hi)
        area = (b1 + b2) * h // 2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b1, b2, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A trapezoid has parallel bases of length ${b1}$ and ${b2}$ and a height of ${h}$. "
                f"Determine its area."
            ),
            answer_latex=f"${area}$",
            hints=[
                r"The area of a trapezoid is $A = \dfrac{1}{2}(b_1 + b_2) h$, where $b_1$ and $b_2$ are the parallel bases and $h$ is the perpendicular height.",
                f"Compute the sum of the bases: ${b1} + {b2} = {b1 + b2}$.",
                f"Multiply by the height and halve: $\\dfrac{{1}}{{2}} \\cdot {b1 + b2} \\cdot {h} = {area}$.",
            ],
            solution_steps_latex=[
                r"Use the formula $A = \dfrac{1}{2}(b_1 + b_2) h$.",
                f"Substitute: $A = \\dfrac{{1}}{{2}}({b1} + {b2}) \\cdot {h}$.",
                f"Simplify: $A = \\dfrac{{1}}{{2}} \\cdot {b1 + b2} \\cdot {h} = {area}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-formula-substitution"],
        )
