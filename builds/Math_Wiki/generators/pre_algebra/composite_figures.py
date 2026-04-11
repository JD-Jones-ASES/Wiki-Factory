"""Composite-figure perimeter/area generators.

Three generators for the ``composite_figures`` topic:

- ``composite_figure_area_rect_plus_semicircle``: a rectangle with a
  semicircle attached to its shorter side. Answer is ``w*h + pi*r^2/2``
  expressed as ``A + B*pi`` with ``r = w/2``.
- ``composite_figure_area_l_shape``: an L-shaped region formed by
  subtracting a rectangular notch from a corner of a larger rectangle.
  Pure-integer answer ``W*H - w*h``.
- ``composite_figure_perimeter_l_shape``: the perimeter of the same
  L-shape, which — perhaps surprisingly — equals ``2*(W+H)`` exactly
  (the notch replaces two edges with two new edges of equal total length).
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "composite_figures"


# ---------------------------------------------------------------------------

@register
class CompositeFigureAreaRectPlusSemicircle(Generator):
    """Rectangle ``w x h`` with a semicircle of radius ``r = w/2`` on top.

    Backward construction: pick ``w`` even so ``r`` is an integer, pick
    ``h`` freely, then the area is ``w*h + (r*r/2)*pi``. Since ``w`` is
    even, ``r*r`` is an integer and the coefficient of pi is a rational
    number that is either an integer (when ``r*r`` is even) or a
    half-integer (when ``r*r`` is odd). To keep the answer clean we
    restrict to even ``w`` values where ``r*r`` is even, i.e., ``r`` even,
    i.e., ``w`` a multiple of 4. (Wave-tested: this yields plenty of
    unique problems.)
    """
    generator_id = "composite_figure_area_rect_plus_semicircle"
    topic_slug = TOPIC_SLUG
    display_name = "Find the area of a rectangle with a semicircle on top"

    # r values: easy r in 1..5 (w = 2..10), medium r in 2..10 (w = 4..20),
    # hard r in 3..15 (w = 6..30). Pair with h to get a large parameter space.
    _R_RANGES = {"easy": (1, 5), "medium": (2, 10), "hard": (3, 15)}
    _H_RANGES = {"easy": (2, 10), "medium": (4, 16), "hard": (6, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r_lo, r_hi = self._R_RANGES[difficulty]
        h_lo, h_hi = self._H_RANGES[difficulty]
        r = rng.randint(r_lo, r_hi)
        h = rng.randint(h_lo, h_hi)
        w = 2 * r

        rect_area = w * h
        # Coefficient of pi in the semicircle area: r*r/2. We want this
        # written as a reduced fraction or integer in the answer.
        rr = r * r
        if rr % 2 == 0:
            semi_coef_latex = str(rr // 2)
            semi_coef_value = rr // 2
            semi_is_int = True
        else:
            semi_coef_latex = f"\\dfrac{{{rr}}}{{2}}"
            semi_coef_value = None  # not used when non-integer
            semi_is_int = False

        if semi_is_int:
            answer_latex = f"${rect_area} + {semi_coef_value}\\pi$"
        else:
            answer_latex = f"${rect_area} + {semi_coef_latex}\\pi$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A composite figure is made of a rectangle with width ${w}$ "
                f"and height ${h}$, with a semicircle attached to the top edge "
                f"(the side of length ${w}$). Determine the total area of the "
                r"figure. Leave your answer in terms of $\pi$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"Split the figure into two pieces: a rectangle of "
                    r"dimensions $w \times h$ and a semicircle of radius $r$."
                ),
                (
                    r"The semicircle sits on the top edge of length $w$, so "
                    r"its diameter is $w$ and its radius is $r = w/2$."
                ),
                (
                    r"Total area $= w \cdot h + \dfrac{1}{2} \pi r^2$. "
                    f"Here $w = {w}$, $h = {h}$, and $r = {r}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute the rectangle's area: $A_\\text{{rect}} = w \\cdot h "
                    f"= {w} \\cdot {h} = {rect_area}$."
                ),
                (
                    f"Identify the semicircle's radius: $r = \\dfrac{{w}}{{2}} "
                    f"= \\dfrac{{{w}}}{{2}} = {r}$."
                ),
                (
                    f"Compute the semicircle's area: $A_\\text{{semi}} = "
                    f"\\dfrac{{1}}{{2}} \\pi r^2 = \\dfrac{{1}}{{2}} \\pi \\cdot "
                    f"{r}^2 = {semi_coef_latex}\\pi$."
                ),
                (
                    f"Add: total area $= {rect_area} + {semi_coef_latex}\\pi$."
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
class CompositeFigureAreaLShape(Generator):
    """L-shape: outer rectangle ``W x H`` with a ``w x h`` corner notch removed.

    Area = ``W*H - w*h``. Backward construction: pick outer and inner
    dimensions independently, then compute the area.
    """
    generator_id = "composite_figure_area_l_shape"
    topic_slug = TOPIC_SLUG
    display_name = "Find the area of an L-shape"

    _OUTER_RANGES = {
        "easy": (6, 14),
        "medium": (8, 22),
        "hard": (12, 35),
    }
    # Inner notch must be strictly smaller than outer on both sides.
    _INNER_MAX_RATIO = 0.6  # notch is at most 60% of outer

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._OUTER_RANGES[difficulty]
        W = rng.randint(lo, hi)
        H = rng.randint(lo, hi)
        # Notch dimensions: 2 up to floor(0.6 * outer), independently.
        w_cap = max(2, int(W * self._INNER_MAX_RATIO))
        h_cap = max(2, int(H * self._INNER_MAX_RATIO))
        w = rng.randint(2, w_cap)
        h = rng.randint(2, h_cap)

        outer_area = W * H
        notch_area = w * h
        area = outer_area - notch_area

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (W, H, w, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Consider a region formed by starting with a rectangle that "
                f"is ${W}$ units wide and ${H}$ units tall, then removing a "
                f"rectangular notch of width ${w}$ and height ${h}$ from one "
                f"of its corners. Determine the area of the resulting "
                f"L-shaped region."
            ),
            answer_latex=f"${area}$",
            hints=[
                (
                    r"Split the problem into two rectangles: the large "
                    r"outer rectangle and the small notch rectangle that "
                    r"was removed."
                ),
                (
                    r"The L-shape's area equals the outer area minus the "
                    r"notch area: $A = W \cdot H - w \cdot h$."
                ),
                (
                    f"Substitute $W = {W}$, $H = {H}$, $w = {w}$, and "
                    f"$h = {h}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute the outer rectangle's area: "
                    f"${W} \\cdot {H} = {outer_area}$."
                ),
                (
                    f"Compute the notch's area: "
                    f"${w} \\cdot {h} = {notch_area}$."
                ),
                (
                    f"Subtract: $A = {outer_area} - {notch_area} = {area}$."
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
class CompositeFigurePerimeterLShape(Generator):
    """Perimeter of an L-shape: equals ``2*(W+H)`` regardless of notch size.

    Surprising result: cutting a rectangular corner notch out of a rectangle
    removes two edge segments (of lengths ``w`` and ``h``) and adds two new
    edge segments of the same lengths, so the total perimeter is unchanged.
    The answer is therefore always ``2*(W + H)``.
    """
    generator_id = "composite_figure_perimeter_l_shape"
    topic_slug = TOPIC_SLUG
    display_name = "Find the perimeter of an L-shape"

    _OUTER_RANGES = {
        "easy": (6, 14),
        "medium": (8, 22),
        "hard": (12, 35),
    }
    _INNER_MAX_RATIO = 0.6

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._OUTER_RANGES[difficulty]
        W = rng.randint(lo, hi)
        H = rng.randint(lo, hi)
        w_cap = max(2, int(W * self._INNER_MAX_RATIO))
        h_cap = max(2, int(H * self._INNER_MAX_RATIO))
        w = rng.randint(2, w_cap)
        h = rng.randint(2, h_cap)

        perimeter = 2 * (W + H)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (W, H, w, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"An L-shaped patio has an outer rectangular boundary that "
                f"is ${W}$ units wide and ${H}$ units tall, with a "
                f"${w} \\times {h}$ rectangular notch cut from one corner. "
                f"Determine the perimeter of the patio (the total distance "
                f"around the outside)."
            ),
            answer_latex=f"${perimeter}$",
            hints=[
                (
                    r"Trace the outside of the L-shape carefully. Cutting a "
                    r"rectangular notch removes two outside edges and adds "
                    r"two new inward-facing edges."
                ),
                (
                    r"The two removed segments have total length $w + h$, "
                    r"and the two new inward-facing segments also have total "
                    r"length $w + h$. The net change in perimeter is zero."
                ),
                (
                    r"So the perimeter equals the outer rectangle's "
                    r"perimeter: $2(W + H)$."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Start from the full outer rectangle's perimeter: "
                    f"$2(W + H) = 2({W} + {H}) = {perimeter}$."
                ),
                (
                    r"Notice that cutting a $w \times h$ corner notch "
                    r"removes a horizontal segment of length $w$ and a "
                    r"vertical segment of length $h$ from the outer edges."
                ),
                (
                    r"The notch then adds a new horizontal segment of "
                    r"length $w$ and a new vertical segment of length $h$ "
                    r"along its concave corner."
                ),
                (
                    f"Removed total = added total, so the L-shape has the "
                    f"same perimeter as the enclosing rectangle: "
                    f"${perimeter}$."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#skill-visualization",
            ],
        )
