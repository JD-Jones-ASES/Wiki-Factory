"""Perimeter and area generators for basic polygons.

Three generators for the ``perimeter_and_area_of_polygons`` topic:

- ``area_of_triangle``: A = (1/2) * b * h, with backward construction
  forcing either b or h to be even so A is always an integer.
- ``area_of_trapezoid``: A = (1/2) * (b1 + b2) * h, with backward
  construction forcing ``b1 + b2`` to be even so A is always an integer.
- ``perimeter_of_regular_polygon``: P = n * s for a regular n-gon of
  side length s. Purely integer arithmetic.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "perimeter_and_area_of_polygons"


# ---------------------------------------------------------------------------

@register
class AreaOfTriangle(Generator):
    """Triangle: ``A = (1/2) * b * h`` with integer answer.

    Backward construction: pick ``b`` and ``h`` such that at least one
    is even, guaranteeing ``b*h`` is even and ``A`` is a whole number.
    """
    generator_id = "area_of_triangle"
    topic_slug = TOPIC_SLUG
    display_name = "Find the area of a triangle"

    _RANGES = {"easy": (2, 12), "medium": (4, 20), "hard": (6, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Decide which dimension will be even, then pick the other freely.
        # This guarantees b*h is even without a retry loop.
        even_side = rng.choice(("base", "height"))
        # Even values in [lo, hi]
        even_lo = lo if lo % 2 == 0 else lo + 1
        even_hi = hi if hi % 2 == 0 else hi - 1
        even_val = rng.randrange(even_lo, even_hi + 1, 2)
        other_val = rng.randint(lo, hi)

        if even_side == "base":
            b, h = even_val, other_val
        else:
            b, h = other_val, even_val

        area = (b * h) // 2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A triangle has a base of length ${b}$ and a height of "
                f"${h}$. Determine its area."
            ),
            answer_latex=f"${area}$",
            hints=[
                (
                    r"The area of a triangle is $A = \dfrac{1}{2} \cdot "
                    r"\text{base} \cdot \text{height}$."
                ),
                (
                    f"Substitute the base $= {b}$ and height $= {h}$."
                ),
                (
                    f"Multiply the base and height first: "
                    f"${b} \\cdot {h} = {b * h}$."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Use the triangle area formula "
                    r"$A = \dfrac{1}{2} b h$."
                ),
                (
                    f"Substitute: $A = \\dfrac{{1}}{{2}} \\cdot {b} \\cdot "
                    f"{h}$."
                ),
                (
                    f"Compute the product: ${b} \\cdot {h} = {b * h}$."
                ),
                (
                    f"Take half: $A = \\dfrac{{{b * h}}}{{2}} = {area}$."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

@register
class AreaOfTrapezoid(Generator):
    """Trapezoid: ``A = (1/2) * (b1 + b2) * h`` with integer answer.

    Backward construction: pick ``b1`` and ``b2`` such that their sum
    is even, then pick any ``h``. Ensures ``(b1 + b2) * h`` is even and
    the area is an integer.
    """
    generator_id = "area_of_trapezoid"
    topic_slug = TOPIC_SLUG
    display_name = "Find the area of a trapezoid"

    _BASE_RANGES = {"easy": (2, 12), "medium": (3, 18), "hard": (4, 28)}
    _HEIGHT_RANGES = {"easy": (2, 10), "medium": (3, 15), "hard": (4, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        b_lo, b_hi = self._BASE_RANGES[difficulty]
        h_lo, h_hi = self._HEIGHT_RANGES[difficulty]

        # Force b1 + b2 even by picking both with the same parity.
        parity = rng.choice((0, 1))
        b1 = rng.randrange(
            b_lo if b_lo % 2 == parity else b_lo + 1,
            b_hi + 1,
            2,
        )
        b2 = rng.randrange(
            b_lo if b_lo % 2 == parity else b_lo + 1,
            b_hi + 1,
            2,
        )
        # Make sure b1 != b2 so the shape is a genuine trapezoid.
        if b1 == b2:
            # Shift b2 by 2 within the range (or down 2 if at the top).
            if b2 + 2 <= b_hi:
                b2 += 2
            else:
                b2 -= 2
        h = rng.randint(h_lo, h_hi)

        sum_bases = b1 + b2
        area = (sum_bases * h) // 2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b1, b2, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A trapezoid has parallel sides of length ${b1}$ and "
                f"${b2}$, and a height of ${h}$. Determine its area."
            ),
            answer_latex=f"${area}$",
            hints=[
                (
                    r"The area of a trapezoid is "
                    r"$A = \dfrac{1}{2}(b_1 + b_2) h$."
                ),
                (
                    f"Add the parallel sides first: "
                    f"${b1} + {b2} = {sum_bases}$."
                ),
                (
                    f"Multiply by the height $h = {h}$, then halve."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Use the trapezoid area formula "
                    r"$A = \dfrac{1}{2}(b_1 + b_2) h$."
                ),
                (
                    f"Substitute: $A = \\dfrac{{1}}{{2}}({b1} + {b2}) \\cdot "
                    f"{h}$."
                ),
                (
                    f"Compute the sum of the bases: ${b1} + {b2} = "
                    f"{sum_bases}$."
                ),
                (
                    f"Multiply by the height: ${sum_bases} \\cdot {h} = "
                    f"{sum_bases * h}$."
                ),
                (
                    f"Halve the result: $A = \\dfrac{{{sum_bases * h}}}{{2}} "
                    f"= {area}$."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

_POLYGON_NAMES: dict[int, str] = {
    3: "equilateral triangle",
    4: "square",
    5: "regular pentagon",
    6: "regular hexagon",
    8: "regular octagon",
}


@register
class PerimeterOfRegularPolygon(Generator):
    """Regular polygon: ``P = n * s`` where ``n`` is the number of sides.

    Choose ``n`` from ``{3, 4, 5, 6, 8}`` and ``s`` from the difficulty
    range. Purely integer arithmetic.
    """
    generator_id = "perimeter_of_regular_polygon"
    topic_slug = TOPIC_SLUG
    display_name = "Find the perimeter of a regular polygon"

    _SIDES = (3, 4, 5, 6, 8)
    _SIDE_LEN_RANGES = {"easy": (2, 15), "medium": (4, 25), "hard": (6, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n = rng.choice(self._SIDES)
        lo, hi = self._SIDE_LEN_RANGES[difficulty]
        s = rng.randint(lo, hi)
        perimeter = n * s
        name = _POLYGON_NAMES[n]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, s)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {name} has a side length of ${s}$. Determine its "
                f"perimeter."
            ),
            answer_latex=f"${perimeter}$",
            hints=[
                (
                    r"A regular polygon has all sides equal in length. "
                    r"Its perimeter is the number of sides times the "
                    r"side length: $P = n \cdot s$."
                ),
                (
                    f"A {name} has $n = {n}$ sides."
                ),
                (
                    f"Multiply $n$ and $s$: ${n} \\cdot {s}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the number of sides: a {name} has $n = {n}$ "
                    f"sides."
                ),
                (
                    r"Use the regular-polygon perimeter formula "
                    r"$P = n \cdot s$."
                ),
                (
                    f"Substitute: $P = {n} \\cdot {s} = {perimeter}$."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#skill-formula-substitution",
            ],
        )
