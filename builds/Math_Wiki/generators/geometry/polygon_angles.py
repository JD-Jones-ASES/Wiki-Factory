"""Polygon angle-sum generators (Cluster 10).

Topic slug: ``polygon_angle_sums``.

Four generators:

- polygon_interior_sum: given n, compute (n-2) * 180
- polygon_regular_interior_angle: given n, each interior angle of a regular polygon
- polygon_regular_exterior_angle: given n, each exterior angle (= 360/n)
- polygon_find_n_from_interior_angle: given an interior angle, solve for n
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_fraction


TOPIC_SLUG = "polygon_angle_sums"


# ---------------------------------------------------------------------------

@register
class PolygonInteriorSum(Generator):
    """Given n, compute the sum of interior angles = (n - 2) * 180."""
    generator_id = "polygon_interior_sum"
    topic_slug = TOPIC_SLUG
    display_name = "Find the interior angle sum of an n-gon"
    bank_count_per_difficulty = 25

    _N_RANGES = {"easy": (3, 15), "medium": (5, 30), "hard": (8, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._N_RANGES[difficulty]
        n = rng.randint(lo, hi)
        total = (n - 2) * 180

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the sum of the interior angles of a convex polygon with ${n}$ sides."
            ),
            answer_latex=f"${total}^\\circ$",
            hints=[
                r"The sum of interior angles of an $n$-gon is $(n - 2) \cdot 180^\circ$.",
                f"Substitute $n = {n}$: $(n - 2) = {n - 2}$.",
                f"Multiply: ${n - 2} \\cdot 180 = {total}$.",
            ],
            solution_steps_latex=[
                r"Use the interior angle sum formula: $S = (n - 2) \cdot 180^\circ$.",
                f"Substitute $n = {n}$: $S = ({n} - 2) \\cdot 180^\\circ$.",
                f"Simplify: $S = {n - 2} \\cdot 180^\\circ = {total}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class PolygonRegularInteriorAngle(Generator):
    """Given n, compute each interior angle of a regular n-gon = (n-2)*180/n."""
    generator_id = "polygon_regular_interior_angle"
    topic_slug = TOPIC_SLUG
    display_name = "Find each interior angle of a regular n-gon"
    bank_count_per_difficulty = 25

    _N_CHOICES = {
        "easy": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        "medium": [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 25, 30],
        "hard": [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n = rng.choice(self._N_CHOICES[difficulty])
        total = (n - 2) * 180
        # Use a Fraction so the display is exact
        each = Fraction(total, n)
        each_latex = format_fraction(each.numerator, each.denominator)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the measure of each interior angle of a regular polygon with ${n}$ sides."
            ),
            answer_latex=f"${each_latex}^\\circ$",
            hints=[
                r"In a regular polygon, every interior angle has the same measure.",
                r"Use the formula: each interior angle $= \dfrac{(n - 2) \cdot 180^\circ}{n}$.",
                f"Substitute $n = {n}$: numerator $= {n - 2} \\cdot 180 = {total}$.",
            ],
            solution_steps_latex=[
                r"Each interior angle of a regular $n$-gon is $\dfrac{(n - 2) \cdot 180^\circ}{n}$.",
                f"Substitute $n = {n}$: $\\dfrac{{({n} - 2) \\cdot 180}}{{{n}}} = \\dfrac{{{total}}}{{{n}}}$.",
                f"Simplify: ${each_latex}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class PolygonRegularExteriorAngle(Generator):
    """Given n, compute each exterior angle of a regular n-gon = 360/n."""
    generator_id = "polygon_regular_exterior_angle"
    topic_slug = TOPIC_SLUG
    display_name = "Find each exterior angle of a regular n-gon"
    bank_count_per_difficulty = 25

    _N_CHOICES = {
        "easy": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        "medium": [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 25, 30],
        "hard": [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n = rng.choice(self._N_CHOICES[difficulty])
        each = Fraction(360, n)
        each_latex = format_fraction(each.numerator, each.denominator)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the measure of each exterior angle of a regular polygon with ${n}$ sides."
            ),
            answer_latex=f"${each_latex}^\\circ$",
            hints=[
                r"The sum of the exterior angles of any convex polygon is $360^\circ$.",
                r"For a regular polygon, divide that sum evenly: each exterior angle $= \dfrac{360^\circ}{n}$.",
                f"Substitute $n = {n}$: $\\dfrac{{360}}{{{n}}} = {each_latex}^\\circ$.",
            ],
            solution_steps_latex=[
                r"Each exterior angle of a regular $n$-gon is $\dfrac{360^\circ}{n}$.",
                f"Substitute $n = {n}$: $\\dfrac{{360}}{{{n}}} = {each_latex}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class PolygonFindNFromInteriorAngle(Generator):
    """Given each interior angle of a regular polygon, solve for n."""
    generator_id = "polygon_find_n_from_interior_angle"
    topic_slug = TOPIC_SLUG
    display_name = "Find n given interior angle of a regular polygon"
    bank_count_per_difficulty = 15

    # n values that give integer interior angles (must have 360 % (180 - interior) == 0)
    _N_CHOICES = {
        "easy": [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120],
        "medium": [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120],
        "hard": [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Select only n values where the interior angle is integer
        choices = [n for n in self._N_CHOICES[difficulty] if ((n - 2) * 180) % n == 0]
        n = rng.choice(choices)
        interior = ((n - 2) * 180) // n

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Each interior angle of a regular polygon measures ${interior}^\\circ$. "
                f"Determine the number of sides of the polygon."
            ),
            answer_latex=f"$n = {n}$",
            hints=[
                r"For a regular $n$-gon, each interior angle is $\dfrac{(n - 2) \cdot 180}{n}$.",
                f"Set up the equation: $\\dfrac{{(n - 2) \\cdot 180}}{{n}} = {interior}$.",
                r"Alternatively, use the exterior angle: each exterior angle is $180 - (\text{interior})$ and equals $\dfrac{360}{n}$.",
            ],
            solution_steps_latex=[
                f"Each exterior angle is $180^\\circ - {interior}^\\circ = {180 - interior}^\\circ$.",
                r"The exterior angles of a regular $n$-gon satisfy $\dfrac{360}{n} = \text{(each exterior angle)}$.",
                f"Solve: $n = \\dfrac{{360}}{{{180 - interior}}} = {n}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-algebraic-manipulation"],
        )
