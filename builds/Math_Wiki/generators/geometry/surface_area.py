"""Surface-area generators (Cluster 10).

Two topic slugs covered in one module:

- ``surface_area_of_prisms_and_cylinders``
- ``surface_area_and_volume_of_spheres``

Five generators. Answers with pi are integer multiples of pi.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

@register
class SurfaceAreaRectangularPrism(Generator):
    """Rectangular prism: SA = 2(lw + lh + wh)."""
    generator_id = "surface_area_rectangular_prism"
    topic_slug = "surface_area_of_prisms_and_cylinders"
    display_name = "Find the surface area of a rectangular prism"

    _RANGES = {"easy": (1, 10), "medium": (2, 20), "hard": (3, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        l = rng.randint(lo, hi)
        w = rng.randint(lo, hi)
        h = rng.randint(lo, hi)
        sa = 2 * (l * w + l * h + w * h)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (l, w, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A rectangular prism has length ${l}$, width ${w}$, and height ${h}$. "
                f"Determine its surface area."
            ),
            answer_latex=f"${sa}$",
            hints=[
                r"Surface area of a rectangular prism: $SA = 2(\ell w + \ell h + w h)$.",
                f"Compute each product: $\\ell w = {l * w}$, $\\ell h = {l * h}$, $w h = {w * h}$.",
                f"Sum: ${l * w} + {l * h} + {w * h} = {l * w + l * h + w * h}$, then double.",
            ],
            solution_steps_latex=[
                r"Use $SA = 2(\ell w + \ell h + w h)$.",
                f"Substitute: $SA = 2({l} \\cdot {w} + {l} \\cdot {h} + {w} \\cdot {h})$.",
                f"Simplify inside: $SA = 2({l * w} + {l * h} + {w * h}) = 2 \\cdot {l * w + l * h + w * h}$.",
                f"Final: $SA = {sa}$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class SurfaceAreaCube(Generator):
    """Cube: SA = 6 s^2."""
    generator_id = "surface_area_cube"
    topic_slug = "surface_area_of_prisms_and_cylinders"
    display_name = "Find the surface area of a cube"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 20), "medium": (2, 35), "hard": (3, 55)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        s = rng.randint(lo, hi)
        sa = 6 * s * s

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (s,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cube has edge length ${s}$. Determine its surface area."
            ),
            answer_latex=f"${sa}$",
            hints=[
                r"A cube has six congruent square faces.",
                r"Surface area of a cube: $SA = 6 s^2$.",
                f"Compute $s^2 = {s * s}$, then multiply by $6$.",
            ],
            solution_steps_latex=[
                r"Use $SA = 6 s^2$.",
                f"Substitute $s = {s}$: $SA = 6 \\cdot {s}^2 = 6 \\cdot {s * s}$.",
                f"Simplify: $SA = {sa}$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class SurfaceAreaCylinder(Generator):
    """Cylinder: SA = 2 pi r^2 + 2 pi r h = 2 pi r (r + h). Answer: integer * pi."""
    generator_id = "surface_area_cylinder"
    topic_slug = "surface_area_of_prisms_and_cylinders"
    display_name = "Find the surface area of a cylinder"

    _RANGES = {"easy": (1, 10), "medium": (2, 18), "hard": (3, 28)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        r = rng.randint(lo, hi)
        h = rng.randint(lo, hi)
        coef = 2 * r * (r + h)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cylinder has radius ${r}$ and height ${h}$. "
                r"Determine its surface area. Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${coef}\\pi$",
            hints=[
                r"Surface area of a cylinder: $SA = 2\pi r^2 + 2\pi r h$, which factors as $SA = 2\pi r (r + h)$.",
                f"Compute $r + h = {r} + {h} = {r + h}$.",
                f"Then $2 r (r + h) = 2 \\cdot {r} \\cdot {r + h} = {coef}$.",
            ],
            solution_steps_latex=[
                r"Use $SA = 2\pi r^2 + 2\pi r h = 2\pi r (r + h)$.",
                f"Substitute: $SA = 2\\pi \\cdot {r} \\cdot ({r} + {h}) = 2\\pi \\cdot {r} \\cdot {r + h}$.",
                f"Simplify the numerical factor: $2 \\cdot {r} \\cdot {r + h} = {coef}$.",
                f"Final: $SA = {coef}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-multi-step"],
        )


# ---------------------------------------------------------------------------

@register
class SurfaceAreaSphere(Generator):
    """Sphere: SA = 4 pi r^2. Answer: integer * pi."""
    generator_id = "surface_area_sphere"
    topic_slug = "surface_area_and_volume_of_spheres"
    display_name = "Find the surface area of a sphere"
    bank_count_per_difficulty = 20

    _RANGES = {"easy": (1, 15), "medium": (2, 25), "hard": (3, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        r = rng.randint(lo, hi)
        coef = 4 * r * r

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A sphere has radius ${r}$. "
                r"Determine its surface area. Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${coef}\\pi$",
            hints=[
                r"Surface area of a sphere: $SA = 4\pi r^2$.",
                f"Compute $r^2 = {r}^2 = {r * r}$.",
                f"Multiply by $4$: $4 \\cdot {r * r} = {coef}$.",
            ],
            solution_steps_latex=[
                r"Use $SA = 4\pi r^2$.",
                f"Substitute $r = {r}$: $SA = 4\\pi \\cdot {r}^2 = 4\\pi \\cdot {r * r}$.",
                f"Simplify: $SA = {coef}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class VolumeSphere(Generator):
    """Sphere: V = (4/3) pi r^3. Backward-construct for clean coefficient."""
    generator_id = "volume_sphere"
    topic_slug = "surface_area_and_volume_of_spheres"
    display_name = "Find the volume of a sphere"
    bank_count_per_difficulty = 16

    # Use multiples of 3 for r so r^3 * 4 / 3 is integer
    _R_CHOICES = {
        "easy": [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],
        "medium": [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],
        "hard": [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.choice(self._R_CHOICES[difficulty])
        coef = 4 * (r ** 3) // 3

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A sphere has radius ${r}$. "
                r"Determine its volume. Leave your answer in terms of $\pi$."
            ),
            answer_latex=f"${coef}\\pi$",
            hints=[
                r"Volume of a sphere: $V = \dfrac{4}{3} \pi r^3$.",
                f"Compute $r^3 = {r}^3 = {r ** 3}$.",
                f"Then $\\dfrac{{4}}{{3}} \\cdot {r ** 3} = {coef}$.",
            ],
            solution_steps_latex=[
                r"Use $V = \dfrac{4}{3} \pi r^3$.",
                f"Substitute $r = {r}$: $V = \\dfrac{{4}}{{3}} \\pi \\cdot {r ** 3}$.",
                f"Simplify: $V = \\dfrac{{4 \\cdot {r ** 3}}}{{3}} \\pi = {coef}\\pi$.",
            ],
            tags=["#branch-geometry", "#topic-solid-geometry", "#skill-formula-substitution"],
        )
