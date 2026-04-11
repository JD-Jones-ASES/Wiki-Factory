"""Cross-section generators for the ``cross_sections_of_solids`` topic.

Three generators:

- ``cube_hex_cross_section_side``: numeric — the regular hexagonal cross
  section of a cube has side length ``s * sqrt(2) / 2`` where ``s`` is the
  cube's edge length. Backward construction picks ``k`` first, then sets
  ``s = 2k`` so the answer is the clean surd ``k * sqrt(2)``.
- ``classify_cube_cross_section``: qualitative — given a described slice of
  a cube, identify the shape (square / rectangle / triangle / hexagon /
  pentagon). Five orientation scenarios, each paired with a randomly chosen
  cube edge length so the parameter space supports ``>=10`` unique problems.
- ``classify_cone_cross_section``: qualitative — given a described slice of
  a cone, identify the resulting conic section (circle / ellipse / parabola
  / hyperbola / triangle). Five scenarios, varied cone radius + height.

All generators use a fixed scenario lookup with deterministic indexing so
the answer is always verifiable and the problem is always well-formed.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "cross_sections_of_solids"


# ---------------------------------------------------------------------------

@register
class CubeHexCrossSectionSide(Generator):
    """Cube edge ``s`` -> regular hexagonal cross section side ``s*sqrt(2)/2``.

    Backward construction: pick ``k`` (desired coefficient of ``sqrt(2)``),
    then ``s = 2*k``. Answer is always a clean ``k*sqrt(2)`` with no fraction.
    """
    generator_id = "cube_hex_cross_section_side"
    topic_slug = TOPIC_SLUG
    display_name = "Find the hexagonal cross-section side of a cube"

    _K_RANGES = {
        "easy": (1, 12),   # k in 1..12 -> s in 2..24 (12 unique, >= 10 floor)
        "medium": (3, 20),  # k in 3..20 -> s in 6..40 (18 unique)
        "hard": (8, 35),  # k in 8..35 -> s in 16..70 (28 unique)
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        s = 2 * k

        if k == 1:
            answer = r"$\sqrt{2}$"
        else:
            answer = f"${k}\\sqrt{{2}}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A cube has edge length ${s}$. A slicing plane passes through "
                f"the midpoints of six of its edges in a symmetric pattern, "
                f"producing a regular hexagonal cross section. Determine the "
                f"side length of the hexagon, giving an exact answer."
            ),
            answer_latex=answer,
            hints=[
                (
                    r"For a cube with edge length $s$, the regular hexagonal "
                    r"cross section through six edge midpoints has side "
                    r"$\dfrac{s\sqrt{2}}{2}$."
                ),
                f"Substitute $s = {s}$ to get $\\dfrac{{{s}\\sqrt{{2}}}}{{2}}$.",
                f"Simplify to {answer}.",
            ],
            solution_steps_latex=[
                (
                    r"Use the formula for the side of a cube's regular "
                    r"hexagonal cross section: $\dfrac{s\sqrt{2}}{2}$."
                ),
                f"Substitute $s = {s}$: $\\dfrac{{{s}\\sqrt{{2}}}}{{2}}$.",
                f"Cancel: {answer}.",
            ],
            tags=[
                "#branch-geometry",
                "#topic-solid-geometry",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

# (description template, answer shape word)
_CUBE_SCENARIOS: list[tuple[str, str]] = [
    (
        "A cube has edge length ${s}$. A slicing plane is parallel to one of "
        "its faces. Classify the shape of the resulting cross section.",
        "square",
    ),
    (
        "A cube has edge length ${s}$. A slicing plane is vertical and passes "
        "through two opposite edges of the cube (tilted relative to the "
        "faces). Classify the shape of the resulting cross section.",
        "rectangle",
    ),
    (
        "A cube has edge length ${s}$. A slicing plane is symmetric and passes "
        "through three faces meeting at a single vertex, slicing off that "
        "corner. Classify the shape of the resulting cross section.",
        "triangle",
    ),
    (
        "A cube has edge length ${s}$. A slicing plane passes through the "
        "midpoints of six edges in a symmetric pattern. Classify the shape "
        "of the resulting cross section.",
        "hexagon",
    ),
    (
        "A cube has edge length ${s}$. A slicing plane enters and exits "
        "through five of the cube's faces without any special symmetry. "
        "Classify the shape of the resulting cross section.",
        "pentagon",
    ),
]


@register
class ClassifyCubeCrossSection(Generator):
    """Classification problem: pick the shape of a described cube slice."""
    generator_id = "classify_cube_cross_section"
    topic_slug = TOPIC_SLUG
    display_name = "Classify a cube's cross-section shape"

    _S_RANGES = {"easy": (2, 10), "medium": (4, 20), "hard": (6, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        s_lo, s_hi = self._S_RANGES[difficulty]
        s = rng.randint(s_lo, s_hi)
        scenario_idx = rng.randint(0, len(_CUBE_SCENARIOS) - 1)
        template, shape = _CUBE_SCENARIOS[scenario_idx]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (scenario_idx, s)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=template.format(s=s),
            answer_latex=f"${shape}$",
            hints=[
                (
                    r"Cube cross sections depend entirely on how the slicing "
                    r"plane is oriented relative to the cube's faces and edges."
                ),
                (
                    r"A plane parallel to a face gives a square; a tilted "
                    r"plane through two opposite edges gives a rectangle; a "
                    r"symmetric corner cut gives a triangle."
                ),
                (
                    r"A symmetric midpoint cut through six edges gives a "
                    r"regular hexagon, and a less symmetric tilt through "
                    r"five faces gives a pentagon."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Identify the orientation of the slicing plane relative "
                    r"to the cube's faces and edges."
                ),
                (
                    r"Match the orientation to the corresponding cross-section "
                    r"shape from the standard cube cross-section list."
                ),
                f"Conclude: the cross section is a {shape}.",
            ],
            tags=[
                "#branch-geometry",
                "#topic-solid-geometry",
                "#skill-visualization",
            ],
        )


# ---------------------------------------------------------------------------

# (description template, answer shape word)
_CONE_SCENARIOS: list[tuple[str, str]] = [
    (
        "A right circular cone has radius ${r}$ and height ${h}$. A slicing "
        "plane passes through the cone perpendicular to its axis. Classify "
        "the cross section.",
        "circle",
    ),
    (
        "A right circular cone has radius ${r}$ and height ${h}$. A slicing "
        "plane is slightly tilted from horizontal but still cuts all the way "
        "through both sides of the cone's lateral surface without touching "
        "the base. Classify the cross section.",
        "ellipse",
    ),
    (
        "A right circular cone has radius ${r}$ and height ${h}$. A slicing "
        "plane is parallel to one of the slanted side lines (generator lines) "
        "of the cone. Classify the cross section.",
        "parabola",
    ),
    (
        "A right circular cone has radius ${r}$ and height ${h}$. A slicing "
        "plane is tilted steeply enough to cut through both halves of the "
        "double cone (the cone plus its mirror image reflected through the "
        "apex). Classify the cross section.",
        "hyperbola",
    ),
    (
        "A right circular cone has radius ${r}$ and height ${h}$. A slicing "
        "plane passes through the apex and is perpendicular to the base. "
        "Classify the cross section.",
        "triangle",
    ),
]


@register
class ClassifyConeCrossSection(Generator):
    """Classification problem: pick the conic type for a described cone slice."""
    generator_id = "classify_cone_cross_section"
    topic_slug = TOPIC_SLUG
    display_name = "Classify a cone's cross-section shape"

    _R_RANGES = {"easy": (2, 7), "medium": (3, 12), "hard": (5, 20)}
    _H_RANGES = {"easy": (3, 10), "medium": (5, 15), "hard": (8, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r_lo, r_hi = self._R_RANGES[difficulty]
        h_lo, h_hi = self._H_RANGES[difficulty]
        r = rng.randint(r_lo, r_hi)
        h = rng.randint(h_lo, h_hi)
        scenario_idx = rng.randint(0, len(_CONE_SCENARIOS) - 1)
        template, shape = _CONE_SCENARIOS[scenario_idx]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (scenario_idx, r, h)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=template.format(r=r, h=h),
            answer_latex=f"${shape}$",
            hints=[
                (
                    r"The four conic sections — circle, ellipse, parabola, "
                    r"and hyperbola — all come from slicing a cone at "
                    r"different angles."
                ),
                (
                    r"A perpendicular slice gives a circle; a slight tilt "
                    r"gives an ellipse; a plane parallel to a generator "
                    r"line gives a parabola; a steeper tilt through a "
                    r"double cone gives a hyperbola."
                ),
                (
                    r"A plane through the apex of a single cone is a "
                    r"degenerate case producing an isosceles triangle."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Identify the orientation of the slicing plane relative "
                    r"to the cone's axis and its slanted generator lines."
                ),
                (
                    r"Match that orientation to the standard conic-sections "
                    r"classification rule."
                ),
                f"Conclude: the cross section is a {shape}.",
            ],
            tags=[
                "#branch-geometry",
                "#topic-solid-geometry",
                "#skill-visualization",
            ],
        )
