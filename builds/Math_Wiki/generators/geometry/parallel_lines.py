"""Parallel-lines and angle-relationship generators (Cluster 10).

Topic slug: ``points_lines_angles_and_angle_relationships``.

Five generators covering the foundational angle relationships:

- parallel_lines_find_alternate_interior: given one angle, find its alt interior partner
- parallel_lines_find_corresponding: given one angle, find its corresponding partner
- parallel_lines_find_cointerior: given one angle, find the co-interior (supplementary)
- parallel_lines_solve_for_x: algebraic expressions for two angles, solve for x
- complementary_supplementary_find: given one angle, find its complement or supplement

Backward construction: pick the target angle first, then set up the scenario.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "points_lines_angles_and_angle_relationships"


# ---------------------------------------------------------------------------

@register
class ParallelLinesAlternateInterior(Generator):
    """Two parallel lines cut by a transversal: find the alternate interior angle."""
    generator_id = "parallel_lines_find_alternate_interior"
    topic_slug = TOPIC_SLUG
    display_name = "Find alternate interior angle for parallel lines"
    bank_count_per_difficulty = 18

    _RANGES = {"easy": (30, 75), "medium": (20, 160), "hard": (10, 170)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        angle = rng.randint(lo, hi)
        # Alternate interior angles are congruent when lines are parallel
        partner = angle

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (angle,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two parallel lines are cut by a transversal. One of the interior angles on "
                f"one side of the transversal measures ${angle}^\\circ$. "
                f"Determine the measure of its alternate interior angle (the interior angle "
                f"on the opposite side of the transversal)."
            ),
            answer_latex=f"${partner}^\\circ$",
            hints=[
                r"Alternate interior angles are the pair of interior angles that lie on opposite sides of the transversal.",
                r"When two lines are parallel, alternate interior angles are congruent (equal in measure).",
                f"So the unknown angle equals the given angle: ${angle}^\\circ$.",
            ],
            solution_steps_latex=[
                r"Recognize the configuration: parallel lines cut by a transversal form alternate interior angle pairs.",
                r"Apply the Alternate Interior Angles Theorem: if two parallel lines are cut by a transversal, then alternate interior angles are congruent.",
                f"Therefore the alternate interior angle also measures ${angle}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

@register
class ParallelLinesCorresponding(Generator):
    """Two parallel lines cut by a transversal: find the corresponding angle."""
    generator_id = "parallel_lines_find_corresponding"
    topic_slug = TOPIC_SLUG
    display_name = "Find corresponding angle for parallel lines"
    bank_count_per_difficulty = 18

    _RANGES = {"easy": (30, 75), "medium": (20, 160), "hard": (10, 170)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        angle = rng.randint(lo, hi)
        partner = angle  # corresponding angles are congruent

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (angle,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two parallel lines are cut by a transversal. One angle at the upper intersection "
                f"measures ${angle}^\\circ$. Determine the measure of the corresponding angle at the "
                f"lower intersection (the angle in the same relative position)."
            ),
            answer_latex=f"${partner}^\\circ$",
            hints=[
                r"Corresponding angles lie in the same position at each intersection (e.g., both upper-right).",
                r"When two lines are parallel, corresponding angles are congruent.",
                f"So the corresponding angle also measures ${angle}^\\circ$.",
            ],
            solution_steps_latex=[
                r"Identify the corresponding angle: it is in the same relative position at the other intersection.",
                r"Apply the Corresponding Angles Postulate: if two parallel lines are cut by a transversal, corresponding angles are congruent.",
                f"Conclude: the corresponding angle measures ${angle}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

@register
class ParallelLinesCoInterior(Generator):
    """Two parallel lines cut by a transversal: find the co-interior (supplementary) angle."""
    generator_id = "parallel_lines_find_cointerior"
    topic_slug = TOPIC_SLUG
    display_name = "Find co-interior angle for parallel lines"
    bank_count_per_difficulty = 18

    _RANGES = {"easy": (30, 80), "medium": (20, 160), "hard": (10, 170)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        angle = rng.randint(lo, hi)
        partner = 180 - angle

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (angle,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two parallel lines are cut by a transversal. One interior angle on one side of "
                f"the transversal measures ${angle}^\\circ$. Determine the measure of the "
                f"co-interior angle (same-side interior angle) at the other intersection."
            ),
            answer_latex=f"${partner}^\\circ$",
            hints=[
                r"Co-interior (same-side interior) angles are the pair of interior angles on the **same** side of the transversal.",
                r"When two lines are parallel, co-interior angles are supplementary: they sum to $180^\circ$.",
                f"So the unknown angle is $180^\\circ - {angle}^\\circ = {partner}^\\circ$.",
            ],
            solution_steps_latex=[
                r"Recognize that co-interior angles lie on the same side of the transversal between the two parallel lines.",
                r"Apply the Same-Side Interior Angles Theorem: co-interior angles are supplementary, so their measures sum to $180^\circ$.",
                f"Set up the equation: ${angle} + x = 180$.",
                f"Solve: $x = 180 - {angle} = {partner}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class ParallelLinesSolveForX(Generator):
    """Two angle expressions equal (corresponding/alternate), solve for x."""
    generator_id = "parallel_lines_solve_for_x"
    topic_slug = TOPIC_SLUG
    display_name = "Solve for x using parallel line angle relationships"
    bank_count_per_difficulty = 18

    _RANGES = {"easy": (2, 12), "medium": (2, 20), "hard": (3, 30)}
    _COEF = {"easy": (2, 6), "medium": (2, 9), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._RANGES[difficulty]
        c_lo, c_hi = self._COEF[difficulty]
        # Backward: pick x first, then build expressions ax+b and cx+d congruent
        x_val = rng.randint(x_lo, x_hi)
        a = rng.randint(c_lo, c_hi)
        c = rng.randint(c_lo, c_hi)
        while c == a:
            c = rng.randint(c_lo, c_hi)
        # value of the angle
        angle_value = rng.randint(30, 90)
        b = angle_value - a * x_val
        d = angle_value - c * x_val
        # Keep constants reasonable
        if abs(b) > 60 or abs(d) > 60:
            # fall back to small offsets
            b = rng.randint(-10, 10)
            d = (a - c) * x_val + b

        def fmt(coef, const, var="x"):
            if const == 0:
                return f"{coef}{var}"
            sign = "+" if const > 0 else "-"
            return f"{coef}{var} {sign} {abs(const)}"

        expr1 = fmt(a, b)
        expr2 = fmt(c, d)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, x_val)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two parallel lines are cut by a transversal. A pair of congruent angles "
                f"(alternate interior angles) have measures $({expr1})^\\circ$ and "
                f"$({expr2})^\\circ$. Determine the value of $x$."
            ),
            answer_latex=f"$x = {x_val}$",
            hints=[
                r"Alternate interior angles formed by parallel lines and a transversal are congruent.",
                "Set the two expressions equal to each other.",
                "Collect like terms and solve for $x$.",
            ],
            solution_steps_latex=[
                "Since the angles are congruent (alternate interior), set the expressions equal: "
                f"${expr1} = {expr2}$.",
                f"Subtract ${c}x$ from both sides: ${a - c}x {('+' if b >= 0 else '-')} {abs(b)} = {d}$.",
                f"Isolate the $x$ term: ${a - c}x = {d - b}$.",
                f"Divide both sides by ${a - c}$: $x = {x_val}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class ComplementarySupplementaryFind(Generator):
    """Given one angle, find its complement or supplement."""
    generator_id = "complementary_supplementary_find"
    topic_slug = TOPIC_SLUG
    display_name = "Find complementary or supplementary angle"
    bank_count_per_difficulty = 18

    _COMP_RANGES = {"easy": (10, 80), "medium": (5, 85), "hard": (1, 89)}
    _SUPP_RANGES = {"easy": (30, 150), "medium": (15, 165), "hard": (5, 175)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        is_complement = rng.random() < 0.5
        if is_complement:
            lo, hi = self._COMP_RANGES[difficulty]
            angle = rng.randint(lo, hi)
            partner = 90 - angle
            kind = "complementary"
            total = 90
        else:
            lo, hi = self._SUPP_RANGES[difficulty]
            angle = rng.randint(lo, hi)
            partner = 180 - angle
            kind = "supplementary"
            total = 180

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (angle, kind)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two angles are {kind}. One of them measures ${angle}^\\circ$. "
                f"Determine the measure of the other angle."
            ),
            answer_latex=f"${partner}^\\circ$",
            hints=[
                (
                    r"Complementary angles sum to $90^\circ$." if is_complement
                    else r"Supplementary angles sum to $180^\circ$."
                ),
                f"Set up the equation: ${angle} + x = {total}$.",
                f"Solve for $x$: $x = {total} - {angle} = {partner}$.",
            ],
            solution_steps_latex=[
                (
                    r"Recall: two angles are complementary when their measures sum to $90^\circ$."
                    if is_complement
                    else r"Recall: two angles are supplementary when their measures sum to $180^\circ$."
                ),
                f"Let $x$ be the unknown angle. Write: ${angle} + x = {total}$.",
                f"Subtract ${angle}$ from both sides: $x = {total - angle}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-formula-substitution"],
        )
