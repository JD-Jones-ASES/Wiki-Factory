"""Coordinate plane introductory generators (Phase 2c Wave B).

Canonical topic slug ``the_coordinate_plane`` at
wiki/topics/algebra/The_Coordinate_Plane.md.

These are *introductory* coordinate-plane exercises, preceding the full
distance formula in ``plotting_points_and_the_coordinate_plane``.

- identify_quadrant_of_point: given (x, y), name the quadrant or axis.
- plot_point_from_description: translate a word description (e.g. "3 units
  right and 4 units down from the origin") into an ordered pair.
- distance_or_direction_between_points: two points that share a row or
  column; compute the unsigned horizontal or vertical distance.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_point


@register
class IdentifyQuadrantOfPoint(Generator):
    """Given a point $(x, y)$, identify its quadrant (or axis/origin).

    Backward construction: pick the target category first, then sample
    coordinates consistent with that category.
    """
    generator_id = "identify_quadrant_of_point"
    topic_slug = "the_coordinate_plane"
    display_name = "Identify the quadrant of a point"
    bank_count_per_difficulty = 20

    _RANGE = {"easy": (1, 9), "medium": (1, 18), "hard": (1, 32)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        category = rng.choices(
            population=[
                "Quadrant I",
                "Quadrant II",
                "Quadrant III",
                "Quadrant IV",
                "x-axis",
                "y-axis",
            ],
            weights=[4, 4, 4, 4, 2, 2],
            k=1,
        )[0]

        if category == "Quadrant I":
            x, y = rng.randint(lo, hi), rng.randint(lo, hi)
        elif category == "Quadrant II":
            x, y = -rng.randint(lo, hi), rng.randint(lo, hi)
        elif category == "Quadrant III":
            x, y = -rng.randint(lo, hi), -rng.randint(lo, hi)
        elif category == "Quadrant IV":
            x, y = rng.randint(lo, hi), -rng.randint(lo, hi)
        elif category == "x-axis":
            sign = rng.choice([-1, 1])
            x = sign * rng.randint(lo, hi)
            y = 0
        else:  # y-axis
            sign = rng.choice([-1, 1])
            y = sign * rng.randint(lo, hi)
            x = 0

        point_latex = format_point(x, y)

        if category.startswith("Quadrant"):
            sign_x = "positive" if x > 0 else "negative"
            sign_y = "positive" if y > 0 else "negative"
            rule = (
                "Quadrant I: both positive. Quadrant II: $x$ negative, $y$ positive. "
                "Quadrant III: both negative. Quadrant IV: $x$ positive, $y$ negative."
            )
            reason = (
                f"The $x$-coordinate is {sign_x} and the $y$-coordinate is {sign_y}."
            )
        elif category == "x-axis":
            rule = "Any point with $y = 0$ lies on the $x$-axis."
            reason = f"The $y$-coordinate is $0$, so the point sits on the $x$-axis."
        else:
            rule = "Any point with $x = 0$ lies on the $y$-axis."
            reason = f"The $x$-coordinate is $0$, so the point sits on the $y$-axis."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Give the quadrant (or axis) that contains the point "
                f"${point_latex}$."
            ),
            answer_latex=category,
            hints=[
                "Check the signs of the two coordinates. A zero coordinate means the point sits on an axis instead of inside a quadrant.",
                rule,
                reason,
            ],
            solution_steps_latex=[
                f"The point is ${point_latex}$.",
                reason,
                f"So the point lies in {category}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-analytic-geometry",
                "#skill-visualization",
            ],
        )


@register
class PlotPointFromDescription(Generator):
    """Turn a verbal movement description into an ordered pair.

    Backward construction: pick the target point $(x, y)$ directly, then
    generate a corresponding "$n$ units right/left and $m$ units up/down from
    the origin" description.
    """
    generator_id = "plot_point_from_description"
    topic_slug = "the_coordinate_plane"
    display_name = "Ordered pair from a movement description"

    _RANGE = {"easy": (1, 9), "medium": (1, 16), "hard": (1, 28)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        dx = rng.randint(lo, hi)
        dy = rng.randint(lo, hi)
        horizontal = rng.choice(["right", "left"])
        vertical = rng.choice(["up", "down"])

        x = dx if horizontal == "right" else -dx
        y = dy if vertical == "up" else -dy

        u_h = "unit" if dx == 1 else "units"
        u_v = "unit" if dy == 1 else "units"

        names = ["Maya", "Kai", "Priya", "Rohan", "Zoe", "Emilia", "Mateo", "Leilani"]
        name = rng.choice(names)
        contexts = [
            "laying out a school mural grid",
            "mapping a community garden plot",
            "programming a robot in maker space",
            "positioning beads on a graph paper design",
            "sketching a blueprint for a pop-up book",
        ]
        context = rng.choice(contexts)

        description = (
            f"While {context}, {name} starts at the origin and moves "
            f"${dx}$ {u_h} {horizontal} and then ${dy}$ {u_v} {vertical}."
        )

        point_latex = format_point(x, y)

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (dx, dy, horizontal, vertical),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"{description} Give the ordered pair {name} lands on.",
            answer_latex=f"${point_latex}$",
            hints=[
                "Right and up are positive; left and down are negative.",
                "Track the horizontal and vertical moves separately. Horizontal goes to $x$; vertical goes to $y$.",
                f"Moving ${dx}$ {u_h} {horizontal} gives $x = {x}$, and moving ${dy}$ {u_v} {vertical} gives $y = {y}$.",
            ],
            solution_steps_latex=[
                "Start at the origin $(0, 0)$.",
                f"Horizontal step: ${dx}$ {u_h} {horizontal}, so $x = {x}$.",
                f"Vertical step: ${dy}$ {u_v} {vertical}, so $y = {y}$.",
                f"The ordered pair is ${point_latex}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-analytic-geometry",
                "#skill-visualization",
            ],
        )


@register
class DistanceOrDirectionBetweenPoints(Generator):
    """Distance between two points sharing a row or a column.

    This is the 1D precursor to the distance formula: when two points share
    one coordinate, the distance is the absolute difference of the other.
    Backward: pick orientation (horizontal/vertical), the shared coordinate,
    and two distinct values for the varying coordinate.
    """
    generator_id = "distance_or_direction_between_points"
    topic_slug = "the_coordinate_plane"
    display_name = "Distance between two points on a common axis line"

    _RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        orientation = rng.choice(["horizontal", "vertical"])
        shared = rng.randint(lo, hi)
        v1 = rng.randint(lo, hi)
        v2 = rng.randint(lo, hi)
        while v2 == v1:
            v2 = rng.randint(lo, hi)

        if orientation == "horizontal":
            # Same y-coordinate.
            p1 = (v1, shared)
            p2 = (v2, shared)
            distance = abs(v2 - v1)
            direction = "horizontal"
            same_label = "$y$"
            diff_label = "$x$"
        else:
            # Same x-coordinate.
            p1 = (shared, v1)
            p2 = (shared, v2)
            distance = abs(v2 - v1)
            direction = "vertical"
            same_label = "$x$"
            diff_label = "$y$"

        p1_latex = format_point(*p1)
        p2_latex = format_point(*p2)

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (orientation, shared, v1, v2),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the distance between ${p1_latex}$ and ${p2_latex}$."
            ),
            answer_latex=f"${distance}$ units",
            hints=[
                f"The two points share the same {same_label}-coordinate, so the segment connecting them is {direction}.",
                f"When one coordinate matches, the distance is just the absolute difference of the other coordinate.",
                f"Compute $|{v2} - {v1}| = {distance}$.",
            ],
            solution_steps_latex=[
                f"Compare ${p1_latex}$ and ${p2_latex}$: the {same_label}-coordinates match.",
                f"The segment is {direction}, so the distance is the absolute difference of the {diff_label}-coordinates.",
                f"$|{v2} - {v1}| = {distance}$.",
                f"The distance is ${distance}$ units.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-analytic-geometry",
                "#skill-visualization",
            ],
        )
