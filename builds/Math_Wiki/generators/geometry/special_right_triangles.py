"""Special right triangles generators (Cluster 10).

Topic slug: ``special_right_triangles``.

Ratios:
  45-45-90:  legs are $s$, hypotenuse is $s\\sqrt{2}$.
  30-60-90:  short leg $s$, long leg $s\\sqrt{3}$, hypotenuse $2s$.

Five generators:

- special_45_45_90_from_leg
- special_45_45_90_from_hypotenuse
- special_30_60_90_from_short_leg
- special_30_60_90_from_hypotenuse
- special_30_60_90_from_long_leg
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "special_right_triangles"


# ---------------------------------------------------------------------------

@register
class Special454590FromLeg(Generator):
    """45-45-90 triangle: given the leg, find the hypotenuse."""
    generator_id = "special_45_45_90_from_leg"
    topic_slug = TOPIC_SLUG
    display_name = "Find hypotenuse of a 45-45-90 from leg"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 12), "medium": (2, 25), "hard": (3, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        leg = rng.randint(lo, hi)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (leg,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In a 45-45-90 right triangle, each leg has length ${leg}$. "
                f"Determine the exact length of the hypotenuse."
            ),
            answer_latex=f"${leg}\\sqrt{{2}}$",
            hints=[
                r"In a 45-45-90 triangle, the two legs are congruent and the hypotenuse is $\sqrt{2}$ times a leg.",
                r"Use the ratio $\text{leg} : \text{leg} : \text{hypotenuse} = 1 : 1 : \sqrt{2}$.",
                f"Multiply the leg by $\\sqrt{{2}}$: ${leg} \\cdot \\sqrt{{2}} = {leg}\\sqrt{{2}}$.",
            ],
            solution_steps_latex=[
                r"Recall the 45-45-90 ratio: $1 : 1 : \sqrt{2}$ (leg : leg : hypotenuse).",
                f"Given leg $= {leg}$, scale the ratio by ${leg}$.",
                f"Hypotenuse $= {leg} \\cdot \\sqrt{{2}} = {leg}\\sqrt{{2}}$.",
            ],
            tags=["#branch-geometry", "#topic-right-triangles", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class Special454590FromHypotenuse(Generator):
    """45-45-90 triangle: given the hypotenuse (as $s\\sqrt{2}$), find the leg."""
    generator_id = "special_45_45_90_from_hypotenuse"
    topic_slug = TOPIC_SLUG
    display_name = "Find leg of a 45-45-90 from hypotenuse"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 10), "medium": (2, 20), "hard": (3, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        leg = rng.randint(lo, hi)
        # hypotenuse is leg * sqrt(2) -- present as "leg * sqrt(2)" so the answer is clean leg
        hyp_str = f"{leg}\\sqrt{{2}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (leg,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In a 45-45-90 right triangle, the hypotenuse has length ${hyp_str}$. "
                f"Determine the exact length of each leg."
            ),
            answer_latex=f"${leg}$",
            hints=[
                r"In a 45-45-90 triangle the ratio is $\text{leg} : \text{leg} : \text{hypotenuse} = 1 : 1 : \sqrt{2}$.",
                r"Divide the hypotenuse by $\sqrt{2}$ to find a leg.",
                f"${hyp_str} \\div \\sqrt{{2}} = {leg}$.",
            ],
            solution_steps_latex=[
                r"The 45-45-90 ratio is $1 : 1 : \sqrt{2}$.",
                f"Given hypotenuse $= {hyp_str}$, divide by $\\sqrt{{2}}$ to get the leg.",
                f"Leg $= \\dfrac{{{hyp_str}}}{{\\sqrt{{2}}}} = {leg}$.",
            ],
            tags=["#branch-geometry", "#topic-right-triangles", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class Special306090FromShortLeg(Generator):
    """30-60-90 triangle: given the short leg, find the long leg and hypotenuse."""
    generator_id = "special_30_60_90_from_short_leg"
    topic_slug = TOPIC_SLUG
    display_name = "Find long leg and hypotenuse of a 30-60-90 from short leg"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 12), "medium": (2, 25), "hard": (3, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        short = rng.randint(lo, hi)
        long_leg = f"{short}\\sqrt{{3}}"
        hyp = 2 * short

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (short,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In a 30-60-90 right triangle, the short leg (opposite the $30^\\circ$ angle) "
                f"has length ${short}$. Determine the exact lengths of the long leg and the hypotenuse."
            ),
            answer_latex=f"Long leg $= {long_leg}$, hypotenuse $= {hyp}$",
            hints=[
                r"The 30-60-90 ratio is $\text{short} : \text{long} : \text{hypotenuse} = 1 : \sqrt{3} : 2$.",
                r"Multiply the short leg by $\sqrt{3}$ for the long leg.",
                "Multiply the short leg by $2$ for the hypotenuse.",
            ],
            solution_steps_latex=[
                r"Recall the 30-60-90 ratio: $1 : \sqrt{3} : 2$.",
                f"Short leg $= {short}$, so scale the ratio by ${short}$.",
                f"Long leg $= {short} \\cdot \\sqrt{{3}} = {long_leg}$.",
                f"Hypotenuse $= {short} \\cdot 2 = {hyp}$.",
            ],
            tags=["#branch-geometry", "#topic-right-triangles", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class Special306090FromHypotenuse(Generator):
    """30-60-90 triangle: given the hypotenuse, find both legs."""
    generator_id = "special_30_60_90_from_hypotenuse"
    topic_slug = TOPIC_SLUG
    display_name = "Find legs of a 30-60-90 from hypotenuse"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (2, 24), "medium": (4, 50), "hard": (6, 80)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Use even hypotenuse so short = hyp/2 is a clean integer
        hyp = 2 * rng.randint(lo // 2, max(hi // 2, lo // 2 + 1))
        short = hyp // 2
        long_leg = f"{short}\\sqrt{{3}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (hyp,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In a 30-60-90 right triangle, the hypotenuse has length ${hyp}$. "
                f"Determine the exact lengths of the short leg and the long leg."
            ),
            answer_latex=f"Short leg $= {short}$, long leg $= {long_leg}$",
            hints=[
                r"The 30-60-90 ratio is $\text{short} : \text{long} : \text{hypotenuse} = 1 : \sqrt{3} : 2$.",
                "The short leg is half the hypotenuse.",
                r"The long leg is the short leg times $\sqrt{3}$.",
            ],
            solution_steps_latex=[
                r"Recall the 30-60-90 ratio: $1 : \sqrt{3} : 2$.",
                f"Short leg $= \\dfrac{{\\text{{hypotenuse}}}}{{2}} = \\dfrac{{{hyp}}}{{2}} = {short}$.",
                f"Long leg $= {short} \\cdot \\sqrt{{3}} = {long_leg}$.",
            ],
            tags=["#branch-geometry", "#topic-right-triangles", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class Special306090FromLongLeg(Generator):
    """30-60-90 triangle: given the long leg (as $s\\sqrt{3}$), find short leg and hypotenuse."""
    generator_id = "special_30_60_90_from_long_leg"
    topic_slug = TOPIC_SLUG
    display_name = "Find other sides of a 30-60-90 from long leg"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 12), "medium": (2, 25), "hard": (3, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        short = rng.randint(lo, hi)
        long_leg_str = f"{short}\\sqrt{{3}}"
        hyp = 2 * short

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (short,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In a 30-60-90 right triangle, the long leg (opposite the $60^\\circ$ angle) "
                f"has length ${long_leg_str}$. Determine the exact lengths of the short leg and the hypotenuse."
            ),
            answer_latex=f"Short leg $= {short}$, hypotenuse $= {hyp}$",
            hints=[
                r"The 30-60-90 ratio is $\text{short} : \text{long} : \text{hypotenuse} = 1 : \sqrt{3} : 2$.",
                r"Divide the long leg by $\sqrt{3}$ to get the short leg.",
                "Double the short leg to get the hypotenuse.",
            ],
            solution_steps_latex=[
                r"Recall the 30-60-90 ratio: $1 : \sqrt{3} : 2$.",
                f"Short leg $= \\dfrac{{{long_leg_str}}}{{\\sqrt{{3}}}} = {short}$.",
                f"Hypotenuse $= 2 \\cdot {short} = {hyp}$.",
            ],
            tags=["#branch-geometry", "#topic-right-triangles", "#skill-algebraic-manipulation"],
        )
