"""Scale-drawing and map generators.

Three generators for the ``scale_drawings_and_maps`` topic:

- ``scale_distance_forward``: given a ``1 unit = k units`` scale and a
  drawing distance ``d``, compute the real-world distance ``d * k``.
- ``scale_distance_reverse``: given a ``1 : k`` scale and a real
  dimension ``R``, compute the model/drawing dimension ``R / k``.
  Backward construction picks the model dimension first so the answer
  is always a clean integer or half-integer number.
- ``scale_factor_from_pair``: given a drawing dimension and the
  corresponding real dimension, compute the scale ratio in the form
  ``1 unit_a = k unit_b``.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "scale_drawings_and_maps"


# ---------------------------------------------------------------------------

# (scale_unit_singular, real_unit, map_context_phrase)
# Each entry describes a scale relation of the form "1 {scale_unit} = k {real_unit}"
_FORWARD_CONTEXTS: tuple[tuple[str, str, str], ...] = (
    ("inch", "miles", "map"),
    ("inch", "feet", "floor plan"),
    ("centimeter", "meters", "scale drawing"),
    ("centimeter", "kilometers", "trail map"),
    ("inch", "yards", "garden plan"),
)


@register
class ScaleDistanceForward(Generator):
    """Given scale ``1 scale_unit = k real_unit`` and drawing distance ``d``,
    compute the real-world distance ``d * k``.
    """
    generator_id = "scale_distance_forward"
    topic_slug = TOPIC_SLUG
    display_name = "Find real distance from a map scale"

    _K_RANGES = {"easy": (5, 25), "medium": (10, 60), "hard": (20, 120)}
    _D_RANGES = {"easy": (2, 10), "medium": (3, 18), "hard": (4, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scale_unit, real_unit, context = rng.choice(_FORWARD_CONTEXTS)
        k_lo, k_hi = self._K_RANGES[difficulty]
        d_lo, d_hi = self._D_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        d = rng.randint(d_lo, d_hi)
        real = d * k

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (scale_unit, real_unit, k, d)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {context} uses a scale of $1\\text{{ {scale_unit}}} = "
                f"{k}\\text{{ {real_unit}}}$. Two landmarks are ${d}$ "
                f"{scale_unit}s apart on the {context}. Determine the "
                f"real-world distance between them."
            ),
            answer_latex=f"${real}$ {real_unit}",
            hints=[
                (
                    f"Each ${scale_unit}$ on the {context} stands for "
                    f"${k}$ {real_unit} in the real world."
                ),
                (
                    r"Multiply the drawing distance by the scale factor: "
                    r"$\text{real} = \text{drawing} \cdot k$."
                ),
                (
                    f"Compute: ${d} \\cdot {k}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Set up a proportion using the scale "
                    f"$\\dfrac{{1\\text{{ {scale_unit}}}}}{{{k}\\text{{ "
                    f"{real_unit}}}}} = \\dfrac{{{d}\\text{{ {scale_unit}}}}}"
                    f"{{x\\text{{ {real_unit}}}}}$."
                ),
                (
                    f"Cross multiply: $1 \\cdot x = {k} \\cdot {d}$."
                ),
                (
                    f"Simplify: $x = {real}$ {real_unit}."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

# Reverse direction: given a real dimension, find the model dimension.
# (context, scale_unit, kind) entries; the scale is 1 : ratio meaning the
# model is 1/ratio times the real object.
_REVERSE_CONTEXTS: tuple[tuple[str, str], ...] = (
    ("model train", "inches"),
    ("dollhouse", "inches"),
    ("architectural model", "centimeters"),
    ("model airplane", "centimeters"),
    ("toy car", "inches"),
)

_REVERSE_RATIOS: dict[str, tuple[int, ...]] = {
    "easy": (10, 12, 20, 24, 25),
    "medium": (12, 20, 24, 25, 48, 50, 60, 72, 87, 100),
    "hard": (24, 48, 50, 60, 72, 87, 100, 120, 144, 160, 200),
}


@register
class ScaleDistanceReverse(Generator):
    """Given a ``1 : ratio`` scale and a real dimension, compute the model
    dimension. Backward construction: pick the model dimension first as a
    small integer, then set the real dimension to ``model * ratio``.
    """
    generator_id = "scale_distance_reverse"
    topic_slug = TOPIC_SLUG
    display_name = "Find a model's dimension from real measurements"

    _MODEL_RANGES = {"easy": (2, 10), "medium": (3, 18), "hard": (4, 28)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        context, unit = rng.choice(_REVERSE_CONTEXTS)
        ratio = rng.choice(_REVERSE_RATIOS[difficulty])
        lo, hi = self._MODEL_RANGES[difficulty]
        model = rng.randint(lo, hi)
        real = model * ratio

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (context, unit, ratio, model)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {context} is built to a scale of $1:{ratio}$. The real "
                f"object it represents is ${real}$ {unit} long. Determine "
                f"the length of the {context} in {unit}."
            ),
            answer_latex=f"${model}$ {unit}",
            hints=[
                (
                    f"A scale of $1:{ratio}$ means every ${1}$ {unit} on "
                    f"the {context} corresponds to ${ratio}$ {unit} on the "
                    f"real object."
                ),
                (
                    r"Divide the real dimension by the scale ratio to get "
                    r"the model dimension: "
                    r"$\text{model} = \dfrac{\text{real}}{\text{ratio}}$."
                ),
                (
                    f"Compute: $\\dfrac{{{real}}}{{{ratio}}}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Set up a proportion using the scale: "
                    f"$\\dfrac{{1}}{{{ratio}}} = \\dfrac{{x}}{{{real}}}$."
                ),
                (
                    f"Cross multiply: ${ratio} \\cdot x = 1 \\cdot {real} = "
                    f"{real}$."
                ),
                (
                    f"Divide both sides by ${ratio}$: "
                    f"$x = \\dfrac{{{real}}}{{{ratio}}} = {model}$ {unit}."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

# (drawing_unit, real_unit, context_phrase)
_PAIR_CONTEXTS: tuple[tuple[str, str, str], ...] = (
    ("inch", "feet", "architectural blueprint"),
    ("inch", "miles", "road map"),
    ("centimeter", "meters", "site plan"),
    ("centimeter", "kilometers", "regional map"),
    ("inch", "yards", "park layout"),
)


@register
class ScaleFactorFromPair(Generator):
    """Given a drawing distance and the matching real distance, compute the
    scale in the form ``1 drawing_unit = k real_unit``. Backward
    construction: pick ``k`` and the drawing distance first, then set the
    real distance to ``drawing * k``.
    """
    generator_id = "scale_factor_from_pair"
    topic_slug = TOPIC_SLUG
    display_name = "Find the scale from a drawing-real pair"

    _K_RANGES = {"easy": (4, 20), "medium": (6, 40), "hard": (10, 80)}
    _DRAWING_RANGES = {"easy": (2, 10), "medium": (3, 15), "hard": (4, 24)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        drawing_unit, real_unit, context = rng.choice(_PAIR_CONTEXTS)
        k_lo, k_hi = self._K_RANGES[difficulty]
        d_lo, d_hi = self._DRAWING_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        drawing = rng.randint(d_lo, d_hi)
        real = drawing * k

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (drawing_unit, real_unit, k, drawing),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"On an {context}, a feature that is ${real}$ {real_unit} "
                f"in the real world is drawn as ${drawing}$ {drawing_unit}s "
                f"on the page. Determine the scale of the drawing in the "
                f"form $1\\text{{ {drawing_unit}}} = k\\text{{ {real_unit}}}$."
            ),
            answer_latex=(
                f"$1\\text{{ {drawing_unit}}} = {k}\\text{{ {real_unit}}}$"
            ),
            hints=[
                (
                    r"A scale tells you how many real units correspond to "
                    r"one drawing unit."
                ),
                (
                    r"Form the ratio $\dfrac{\text{real}}{\text{drawing}}$ "
                    r"to find how many real units match one drawing unit."
                ),
                (
                    f"Compute $\\dfrac{{{real}}}{{{drawing}}}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Divide the real length by the drawing length: "
                    f"$\\dfrac{{{real}\\text{{ {real_unit}}}}}"
                    f"{{{drawing}\\text{{ {drawing_unit}}}}}$."
                ),
                (
                    f"Simplify: $\\dfrac{{{real}}}{{{drawing}}} = {k}$ "
                    f"{real_unit} per {drawing_unit}."
                ),
                (
                    f"So the scale is $1\\text{{ {drawing_unit}}} = "
                    f"{k}\\text{{ {real_unit}}}$."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-translation",
            ],
        )
