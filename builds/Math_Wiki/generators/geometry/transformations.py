"""Transformation generators (Cluster 10).

Two topic slugs covered in one module:

- ``rigid_transformations``
- ``dilations_and_similarity``

Six generators total.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_point


# ---------------------------------------------------------------------------

@register
class TranslatePoint(Generator):
    """Apply a translation $(x, y) \\to (x + a, y + b)$."""
    generator_id = "translate_point"
    topic_slug = "rigid_transformations"
    display_name = "Translate a point by a vector"

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        x = rng.randint(lo, hi)
        y = rng.randint(lo, hi)
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        while a == 0 and b == 0:
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
        x_img = x + a
        y_img = y + b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Apply the translation $(x, y) \\to (x {'+' if a >= 0 else '-'} {abs(a)}, "
                f"y {'+' if b >= 0 else '-'} {abs(b)})$ to the point ${format_point(x, y)}$. "
                f"Give the image."
            ),
            answer_latex=f"${format_point(x_img, y_img)}$",
            hints=[
                "A translation slides every point the same amount in the $x$- and $y$-directions.",
                f"Add ${a}$ to the $x$-coordinate.",
                f"Add ${b}$ to the $y$-coordinate.",
            ],
            solution_steps_latex=[
                f"Start with $(x, y) = {format_point(x, y)}$.",
                f"Add the translation vector: $({x} {'+' if a >= 0 else '-'} {abs(a)}, {y} {'+' if b >= 0 else '-'} {abs(b)})$.",
                f"Simplify: ${format_point(x_img, y_img)}$.",
            ],
            tags=["#branch-geometry", "#topic-transformations", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class ReflectPointOverAxis(Generator):
    """Reflect a point over the x-axis, y-axis, or line y = x."""
    generator_id = "reflect_point_over_axis"
    topic_slug = "rigid_transformations"
    display_name = "Reflect a point over an axis"
    bank_count_per_difficulty = 30

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _LINES = ("x-axis", "y-axis", "y=x")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        x = rng.randint(lo, hi)
        y = rng.randint(lo, hi)
        line = rng.choice(self._LINES)
        if line == "x-axis":
            x_img, y_img = x, -y
            rule = r"(x, y) \to (x, -y)"
        elif line == "y-axis":
            x_img, y_img = -x, y
            rule = r"(x, y) \to (-x, y)"
        else:  # y = x
            x_img, y_img = y, x
            rule = r"(x, y) \to (y, x)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y, line)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Reflect the point ${format_point(x, y)}$ over the ${line}$. "
                f"Give the image."
            ),
            answer_latex=f"${format_point(x_img, y_img)}$",
            hints=[
                r"Reflection over the $x$-axis: negate $y$.",
                r"Reflection over the $y$-axis: negate $x$.",
                r"Reflection over $y = x$: swap $x$ and $y$.",
            ],
            solution_steps_latex=[
                f"Use the reflection rule for the ${line}$: ${rule}$.",
                f"Apply to ${format_point(x, y)}$.",
                f"Image: ${format_point(x_img, y_img)}$.",
            ],
            tags=["#branch-geometry", "#topic-transformations", "#skill-visualization"],
        )


# ---------------------------------------------------------------------------

@register
class RotatePoint90180270(Generator):
    """Rotate a point about the origin by 90°, 180°, or 270° CCW."""
    generator_id = "rotate_point_90_180_270"
    topic_slug = "rigid_transformations"
    display_name = "Rotate a point about the origin"
    bank_count_per_difficulty = 30

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _ANGLES = (90, 180, 270)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        x = rng.randint(lo, hi)
        y = rng.randint(lo, hi)
        while x == 0 and y == 0:
            x = rng.randint(lo, hi)
            y = rng.randint(lo, hi)
        angle = rng.choice(self._ANGLES)
        if angle == 90:
            x_img, y_img = -y, x
            rule = r"(x, y) \to (-y, x)"
        elif angle == 180:
            x_img, y_img = -x, -y
            rule = r"(x, y) \to (-x, -y)"
        else:  # 270
            x_img, y_img = y, -x
            rule = r"(x, y) \to (y, -x)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y, angle)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Rotate the point ${format_point(x, y)}$ by ${angle}^\\circ$ counterclockwise "
                f"about the origin. Give the image."
            ),
            answer_latex=f"${format_point(x_img, y_img)}$",
            hints=[
                r"Rotation rules about the origin (counterclockwise):",
                r"$90^\circ$: $(x, y) \to (-y, x)$. $180^\circ$: $(x, y) \to (-x, -y)$. $270^\circ$: $(x, y) \to (y, -x)$.",
                f"Use the rule for ${angle}^\\circ$: ${rule}$.",
            ],
            solution_steps_latex=[
                f"Apply the ${angle}^\\circ$ counterclockwise rotation rule: ${rule}$.",
                f"Substitute $(x, y) = {format_point(x, y)}$.",
                f"Image: ${format_point(x_img, y_img)}$.",
            ],
            tags=["#branch-geometry", "#topic-transformations", "#skill-visualization"],
        )


# ---------------------------------------------------------------------------

@register
class IdentifyRigidTransformation(Generator):
    """Given preimage and image, identify which rigid transformation maps one to the other."""
    generator_id = "identify_rigid_transformation"
    topic_slug = "rigid_transformations"
    display_name = "Identify the rigid transformation"
    bank_count_per_difficulty = 30

    _RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _TYPES = ("translation", "reflection_x", "reflection_y", "rotation_90", "rotation_180", "rotation_270")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        t = rng.choice(self._TYPES)
        x = rng.randint(lo, hi)
        y = rng.randint(lo, hi)
        while x == 0 and y == 0:
            x = rng.randint(lo, hi)
            y = rng.randint(lo, hi)

        if t == "translation":
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
            while a == 0 and b == 0:
                a = rng.randint(lo, hi)
                b = rng.randint(lo, hi)
            x_img, y_img = x + a, y + b
            sign_a = "+" if a >= 0 else "-"
            sign_b = "+" if b >= 0 else "-"
            description = (
                f"translation by the vector $\\langle {a}, {b} \\rangle$ "
                f"(rule: $(x, y) \\to (x {sign_a} {abs(a)}, y {sign_b} {abs(b)})$)"
            )
        elif t == "reflection_x":
            x_img, y_img = x, -y
            description = r"reflection over the $x$-axis (rule: $(x, y) \to (x, -y)$)"
        elif t == "reflection_y":
            x_img, y_img = -x, y
            description = r"reflection over the $y$-axis (rule: $(x, y) \to (-x, y)$)"
        elif t == "rotation_90":
            x_img, y_img = -y, x
            description = r"$90^\circ$ counterclockwise rotation about the origin"
        elif t == "rotation_180":
            x_img, y_img = -x, -y
            description = r"$180^\circ$ rotation about the origin"
        else:  # rotation_270
            x_img, y_img = y, -x
            description = r"$270^\circ$ counterclockwise rotation about the origin"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (t, x, y)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A rigid transformation maps the point ${format_point(x, y)}$ to "
                f"${format_point(x_img, y_img)}$. Identify the transformation."
            ),
            answer_latex=f"{description}",
            hints=[
                "Compare the preimage and image coordinates.",
                "If only signs changed: it is a reflection or rotation.",
                "If both coordinates changed by the same constant amount: it is a translation.",
            ],
            solution_steps_latex=[
                f"Preimage $= {format_point(x, y)}$, image $= {format_point(x_img, y_img)}$.",
                f"Check: did both coordinates negate? Did they swap? Did they shift by a constant vector?",
                f"The mapping fits: {description}.",
            ],
            tags=["#branch-geometry", "#topic-transformations", "#skill-visualization"],
        )


# ---------------------------------------------------------------------------

@register
class DilatePointFromOrigin(Generator):
    """Apply a dilation $(x, y) \\to (kx, ky)$ from the origin."""
    generator_id = "dilate_point_from_origin"
    topic_slug = "dilations_and_similarity"
    display_name = "Dilate a point from the origin"

    _RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_CHOICES = {"easy": (2, 3), "medium": (2, 3, 4, 5), "hard": (2, 3, 4, 5, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        x = rng.randint(lo, hi)
        y = rng.randint(lo, hi)
        while x == 0 and y == 0:
            x = rng.randint(lo, hi)
            y = rng.randint(lo, hi)
        k = rng.choice(self._K_CHOICES[difficulty])
        x_img = k * x
        y_img = k * y

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Apply a dilation centered at the origin with scale factor $k = {k}$ "
                f"to the point ${format_point(x, y)}$. Give the image."
            ),
            answer_latex=f"${format_point(x_img, y_img)}$",
            hints=[
                r"A dilation from the origin multiplies each coordinate by the scale factor: $(x, y) \to (kx, ky)$.",
                f"Multiply the $x$-coordinate by $k = {k}$.",
                f"Multiply the $y$-coordinate by $k = {k}$.",
            ],
            solution_steps_latex=[
                f"Dilation rule: $(x, y) \\to ({k}x, {k}y)$.",
                f"Substitute: $({k} \\cdot {x}, {k} \\cdot {y})$.",
                f"Image: ${format_point(x_img, y_img)}$.",
            ],
            tags=["#branch-geometry", "#topic-transformations", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class SimilarityRatioAreaVolume(Generator):
    """Given length ratio k, compute area ratio k^2 or volume ratio k^3."""
    generator_id = "similarity_ratio_area_volume"
    topic_slug = "dilations_and_similarity"
    display_name = "Scale length ratio to area or volume ratio"
    bank_count_per_difficulty = 20

    _K_CHOICES = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9, 10),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k = rng.choice(self._K_CHOICES[difficulty])
        dim = rng.choice(["area", "volume"])
        if dim == "area":
            ratio = k * k
            power = 2
        else:
            ratio = k ** 3
            power = 3

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, dim)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two similar figures have a length ratio of ${k} : 1$. "
                f"Determine the ratio of their {dim}s."
            ),
            answer_latex=f"${ratio} : 1$",
            hints=[
                r"If the length scale factor is $k$, then the area ratio is $k^2$.",
                r"And the volume ratio is $k^3$.",
                f"Here $k = {k}$, so the {dim} ratio is $k^{power} = {ratio}$.",
            ],
            solution_steps_latex=[
                r"For similar figures, if lengths scale by $k$, then areas scale by $k^2$ and volumes scale by $k^3$.",
                f"Given $k = {k}$ and we want the {dim} ratio.",
                f"Compute $k^{power} = {k}^{power} = {ratio}$.",
                f"The {dim} ratio is ${ratio} : 1$.",
            ],
            tags=["#branch-geometry", "#topic-similarity-and-congruence", "#skill-formula-substitution"],
        )
