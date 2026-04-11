"""Volume generators (Cluster 10).

Two topic slugs covered in one module:

- ``volume_of_prisms_and_cylinders``
- ``volume_of_pyramids_and_cones``

Six generators. All answers with pi are integer multiples of pi.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

@register
class VolumeRectangularPrism(Generator):
    """Rectangular prism: V = l * w * h."""
    generator_id = "volume_rectangular_prism"
    topic_slug = "volume_of_prisms_and_cylinders"
    display_name = "Find the volume of a rectangular prism"

    _RANGES = {"easy": (1, 10), "medium": (2, 20), "hard": (3, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        l = rng.randint(lo, hi)
        w = rng.randint(lo, hi)
        h = rng.randint(lo, hi)
        volume = l * w * h

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (l, w, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A rectangular prism has length ${l}$, width ${w}$, and height ${h}$. "
                f"Determine its volume."
            ),
            answer_latex=f"${volume}$",
            hints=[
                r"Volume of a rectangular prism: $V = \ell w h$.",
                f"Multiply: ${l} \\cdot {w} = {l * w}$.",
                f"Then multiply by $h = {h}$: ${l * w} \\cdot {h} = {volume}$.",
            ],
            solution_steps_latex=[
                r"Use the formula $V = \ell w h$.",
                f"Substitute: $V = {l} \\cdot {w} \\cdot {h}$.",
                f"Simplify: $V = {volume}$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class VolumeCylinderFromRadiusHeight(Generator):
    """Cylinder: V = pi r^2 h. Answer as integer times pi."""
    generator_id = "volume_cylinder_from_radius_height"
    topic_slug = "volume_of_prisms_and_cylinders"
    display_name = "Find the volume of a cylinder"

    _RANGES = {"easy": (1, 10), "medium": (2, 18), "hard": (3, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        r = rng.randint(lo, hi)
        h = rng.randint(lo, hi)
        coef = r * r * h

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cylinder has radius ${r}$ and height ${h}$. "
                r"Determine its volume. Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${coef}\\pi$",
            hints=[
                r"Volume of a cylinder: $V = \pi r^2 h$.",
                f"Compute $r^2 = {r}^2 = {r * r}$.",
                f"Multiply by $h = {h}$: ${r * r} \\cdot {h} = {coef}$.",
            ],
            solution_steps_latex=[
                r"Use the formula $V = \pi r^2 h$.",
                f"Substitute: $V = \\pi \\cdot {r}^2 \\cdot {h}$.",
                f"Simplify the numerical factor: ${r * r} \\cdot {h} = {coef}$.",
                f"Final answer: $V = {coef}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class VolumeCylinderFindHeight(Generator):
    """Cylinder: given V (as coefficient of pi) and r, solve for h."""
    generator_id = "volume_cylinder_find_height"
    topic_slug = "volume_of_prisms_and_cylinders"
    display_name = "Find the height of a cylinder from volume and radius"

    _RANGES = {"easy": (1, 8), "medium": (2, 15), "hard": (3, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        r = rng.randint(lo, hi)
        h = rng.randint(lo, hi)
        coef = r * r * h  # V = coef * pi

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cylinder has radius ${r}$ and volume ${coef}\\pi$. "
                f"Determine its height."
            ),
            answer_latex=f"${h}$",
            hints=[
                r"Start with $V = \pi r^2 h$.",
                r"Solve for $h$: $h = \dfrac{V}{\pi r^2}$.",
                f"Compute $r^2 = {r * r}$.",
            ],
            solution_steps_latex=[
                r"Use $V = \pi r^2 h$ and solve for $h$: $h = \dfrac{V}{\pi r^2}$.",
                f"Substitute: $h = \\dfrac{{{coef}\\pi}}{{\\pi \\cdot {r}^2}} = \\dfrac{{{coef}}}{{{r * r}}}$.",
                f"Simplify: $h = {h}$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class VolumePyramidRectangular(Generator):
    """Rectangular pyramid: V = (1/3) l * w * h. Backward-construct for integer V."""
    generator_id = "volume_pyramid_rectangular"
    topic_slug = "volume_of_pyramids_and_cones"
    display_name = "Find the volume of a rectangular pyramid"

    _RANGES = {"easy": (1, 10), "medium": (2, 20), "hard": (3, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Ensure l*w*h is divisible by 3 for clean answer
        while True:
            l = rng.randint(lo, hi)
            w = rng.randint(lo, hi)
            h = rng.randint(lo, hi)
            if (l * w * h) % 3 == 0:
                break
        volume = l * w * h // 3

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (l, w, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A rectangular pyramid has a base of length ${l}$ and width ${w}$, "
                f"and a height of ${h}$. Determine its volume."
            ),
            answer_latex=f"${volume}$",
            hints=[
                r"Volume of a pyramid: $V = \dfrac{1}{3} \cdot (\text{base area}) \cdot h$.",
                f"Base area $= \\ell \\cdot w = {l} \\cdot {w} = {l * w}$.",
                f"Then $V = \\dfrac{{1}}{{3}} \\cdot {l * w} \\cdot {h}$.",
            ],
            solution_steps_latex=[
                r"Use $V = \dfrac{1}{3} \ell w h$ for a rectangular pyramid.",
                f"Substitute: $V = \\dfrac{{1}}{{3}} \\cdot {l} \\cdot {w} \\cdot {h}$.",
                f"Compute the numerator: ${l} \\cdot {w} \\cdot {h} = {l * w * h}$.",
                f"Divide by $3$: $V = \\dfrac{{{l * w * h}}}{{3}} = {volume}$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class VolumeCone(Generator):
    """Cone: V = (1/3) pi r^2 h. Backward-construct for integer coefficient."""
    generator_id = "volume_cone"
    topic_slug = "volume_of_pyramids_and_cones"
    display_name = "Find the volume of a cone"

    _RANGES = {"easy": (1, 9), "medium": (2, 15), "hard": (3, 24)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Ensure r*r*h is divisible by 3 for clean answer
        while True:
            r = rng.randint(lo, hi)
            h = rng.randint(lo, hi)
            if (r * r * h) % 3 == 0:
                break
        coef = r * r * h // 3

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cone has radius ${r}$ and height ${h}$. "
                r"Determine its volume. Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${coef}\\pi$",
            hints=[
                r"Volume of a cone: $V = \dfrac{1}{3} \pi r^2 h$.",
                f"Compute $r^2 = {r * r}$.",
                f"Then $V = \\dfrac{{1}}{{3}} \\pi \\cdot {r * r} \\cdot {h}$.",
            ],
            solution_steps_latex=[
                r"Use $V = \dfrac{1}{3} \pi r^2 h$.",
                f"Substitute: $V = \\dfrac{{1}}{{3}} \\pi \\cdot {r}^2 \\cdot {h}$.",
                f"Simplify: $V = \\dfrac{{{r * r * h}}}{{3}} \\pi = {coef}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class VolumeConeFindRadius(Generator):
    """Cone: given V (= coef * pi) and h, solve for r."""
    generator_id = "volume_cone_find_radius"
    topic_slug = "volume_of_pyramids_and_cones"
    display_name = "Find the radius of a cone from volume and height"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 8), "medium": (2, 12), "hard": (3, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Ensure (r^2 * h) % 3 == 0 for clean integer coefficient
        while True:
            r = rng.randint(lo, hi)
            h = rng.randint(lo, hi)
            if (r * r * h) % 3 == 0:
                break
        coef = r * r * h // 3  # so that V = coef * pi

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cone has height ${h}$ and volume ${coef}\\pi$. "
                f"Determine its radius."
            ),
            answer_latex=f"${r}$",
            hints=[
                r"Start with $V = \dfrac{1}{3} \pi r^2 h$.",
                r"Solve for $r^2$: $r^2 = \dfrac{3V}{\pi h}$.",
                f"Then take the positive square root.",
            ],
            solution_steps_latex=[
                r"Rearrange $V = \dfrac{1}{3} \pi r^2 h$ to isolate $r^2$: $r^2 = \dfrac{3V}{\pi h}$.",
                f"Substitute $V = {coef}\\pi$ and $h = {h}$: $r^2 = \\dfrac{{3 \\cdot {coef}\\pi}}{{\\pi \\cdot {h}}} = \\dfrac{{{3 * coef}}}{{{h}}}$.",
                f"Simplify: $r^2 = {r * r}$.",
                f"Take the positive root: $r = {r}$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-algebraic-manipulation"],
        )
