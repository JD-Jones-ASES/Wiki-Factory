"""Conic sections, complex numbers, and polar coordinate generators.

Eight topic slugs covered across algebra-2, pre-algebra, and pre-calculus:

Algebra-2 / pre-calculus:
- parabolas                            (Parabolas.md)
- ellipses                             (Ellipses.md)
- hyperbolas                           (Hyperbolas.md)
- the_complex_number_system            (The_Complex_Number_System.md)
- complex_zeros                        (Complex_Zeros.md)
- polar_form_of_complex_numbers        (Polar_Form_Of_Complex_Numbers.md)
- introduction_to_polar_coordinates    (Introduction_To_Polar_Coordinates.md)

Pre-algebra:
- circumference_and_area_of_circles    (Circumference_And_Area_Of_Circles.md)

Each topic has three generators for a total of 24. Backward construction is
used throughout: parameters are chosen so answers come out clean (integer
foci, Pythagorean-triple moduli, exact-value polar arguments), then the
statement is rendered. SymPy handles all exact arithmetic for conics,
complex numbers, and polar conversions; LaTeX is rendered with ``\\dfrac``,
``\\sqrt``, ``\\cos``, ``\\sin``.
"""
from __future__ import annotations

import math
import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _signed_paren(n: int) -> str:
    """Wrap a negative integer in parentheses so it reads well after an op."""
    return f"({n})" if n < 0 else str(n)


def _shift_expr(var: str, shift: int) -> str:
    """Format `(var - shift)` with correct sign handling.

    >>> _shift_expr('x', 3)
    '(x - 3)'
    >>> _shift_expr('y', -2)
    '(y + 2)'
    >>> _shift_expr('x', 0)
    'x'
    """
    if shift == 0:
        return var
    op = "-" if shift > 0 else "+"
    return f"({var} {op} {abs(shift)})"


def _format_point(x, y) -> str:
    """Format a 2D point as `(x, y)` — accepts any stringifiable coordinates."""
    return f"({x},\\ {y})"


def _format_pi_fraction(num: int, den: int) -> str:
    """Render (num * pi) / den as a clean LaTeX expression."""
    if num == 0:
        return "0"
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    sign = "-" if num < 0 else ""
    a = abs(num)
    if den == 1:
        if a == 1:
            return f"{sign}\\pi"
        return rf"{sign}{a}\pi"
    if a == 1:
        return rf"{sign}\dfrac{{\pi}}{{{den}}}"
    return rf"{sign}\dfrac{{{a}\pi}}{{{den}}}"


def _pi_angle(num: int, den: int) -> sp.Expr:
    """Return sympy angle (num * pi) / den."""
    return sp.Rational(num, den) * sp.pi


# Tag branches ---------------------------------------------------------------

CONIC_TAGS = ["#branch-algebra-2", "#topic-conic-sections"]
CIRCLE_GEO_TAGS = ["#branch-pre-algebra", "#topic-euclidean-geometry"]
COMPLEX_TAGS_ALG2 = ["#branch-algebra-2", "#topic-complex-numbers"]
COMPLEX_TAGS_PRECALC = ["#branch-pre-calculus", "#topic-complex-numbers"]
POLAR_TAGS = ["#branch-pre-calculus", "#topic-unit-circle"]


# ===========================================================================
# Topic 1: parabolas
# ===========================================================================


@register
class ParabolaIdentifyVertexFocusDirectrix(Generator):
    """Given $(x-h)^2 = 4p(y-k)$, identify the vertex, focus, and directrix.

    Backward construction: pick integer $h$, $k$, and a small signed $p$
    (positive or negative). Since the parabola opens vertically, the focus
    is at $(h,\\ k + p)$ and the directrix is $y = k - p$.
    """

    generator_id = "parabola_identify_vertex_focus_directrix"
    topic_slug = "parabolas"
    display_name = "Identify vertex, focus, and directrix of a parabola in standard form"

    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _P_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        p_lo, p_hi = self._P_RANGES[difficulty]

        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        p_mag = rng.randint(p_lo, p_hi)
        p = rng.choice([-1, 1]) * p_mag

        four_p = 4 * p
        lhs = f"{_shift_expr('x', h)}^2"
        if four_p < 0:
            rhs = f"-{abs(four_p)}{_shift_expr('y', k)}"
        else:
            rhs = f"{four_p}{_shift_expr('y', k)}"

        equation_latex = f"{lhs} = {rhs}"

        vertex_latex = _format_point(h, k)
        focus_latex = _format_point(h, k + p)
        directrix_latex = f"y = {k - p}"

        answer_latex = (
            f"Vertex: ${vertex_latex}$; "
            f"focus: ${focus_latex}$; "
            f"directrix: ${directrix_latex}$"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, p)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the parabola ${equation_latex}$, identify the vertex, "
                "focus, and directrix."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"A parabola $(x - h)^2 = 4p(y - k)$ has vertex $(h,\ k)$, "
                    r"focus $(h,\ k + p)$, and directrix $y = k - p$."
                ),
                (
                    f"Match coefficients: $h = {h}$, $k = {k}$, and "
                    f"$4p = {four_p}$ so $p = {p}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compare ${equation_latex}$ to the standard form "
                    r"$(x - h)^2 = 4p(y - k)$."
                ),
                (
                    f"Read off $h = {h}$, $k = {k}$, and $4p = {four_p}$, "
                    f"giving $p = {p}$."
                ),
                (
                    f"Vertex $(h,\\ k) = {vertex_latex}$; "
                    f"focus $(h,\\ k + p) = {focus_latex}$; "
                    f"directrix $y = k - p$, i.e. ${directrix_latex}$."
                ),
            ],
            tags=CONIC_TAGS,
        )


@register
class ParabolaWriteEquationFromFeatures(Generator):
    """Given vertex and focus, write the standard form equation of the parabola.

    Backward: pick vertex $(h, k)$ and integer $p \\ne 0$; set focus at
    $(h, k + p)$. Ask the student to recover $(x - h)^2 = 4p(y - k)$.
    """

    generator_id = "parabola_write_equation_from_features"
    topic_slug = "parabolas"
    display_name = "Write a parabola's equation from vertex and focus"

    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _P_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        p_lo, p_hi = self._P_RANGES[difficulty]

        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        p = rng.choice([-1, 1]) * rng.randint(p_lo, p_hi)

        vertex_latex = _format_point(h, k)
        focus_latex = _format_point(h, k + p)

        four_p = 4 * p
        lhs = f"{_shift_expr('x', h)}^2"
        if four_p < 0:
            rhs = f"-{abs(four_p)}{_shift_expr('y', k)}"
        else:
            rhs = f"{four_p}{_shift_expr('y', k)}"
        equation_latex = f"{lhs} = {rhs}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, p)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the standard-form equation of the parabola with vertex "
                f"${vertex_latex}$ and focus ${focus_latex}$."
            ),
            answer_latex=f"${equation_latex}$",
            hints=[
                (
                    r"A vertical-axis parabola with vertex $(h,\ k)$ and focus "
                    r"$(h,\ k + p)$ has the form $(x - h)^2 = 4p(y - k)$."
                ),
                (
                    f"Find $p$ as the signed distance from the vertex to the "
                    f"focus along the $y$-axis: $p = {p}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Vertex is $(h,\\ k) = {vertex_latex}$, so $h = {h}$ and "
                    f"$k = {k}$."
                ),
                (
                    f"Focus $(h,\\ k + p) = {focus_latex}$ gives "
                    f"$p = {k + p} - {k} = {p}$."
                ),
                (
                    f"Substitute into $(x - h)^2 = 4p(y - k)$: "
                    f"${equation_latex}$."
                ),
            ],
            tags=CONIC_TAGS,
        )


@register
class ParabolaHorizontalVsVertical(Generator):
    """Classify whether a parabola opens up, down, left, or right.

    Backward: randomly pick orientation and sign of $p$, generate the
    equation, ask for direction.
    """

    generator_id = "parabola_horizontal_vs_vertical"
    topic_slug = "parabolas"
    display_name = "Classify parabola direction (up, down, left, or right)"

    bank_count_per_difficulty = 20

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        orientation = rng.choice(["vertical", "horizontal"])
        p_mag = rng.randint(1, 6)
        p_sign = rng.choice([-1, 1])
        p = p_sign * p_mag
        h = rng.randint(-5, 5)
        k = rng.randint(-5, 5)

        four_p = 4 * p

        if orientation == "vertical":
            lhs = f"{_shift_expr('x', h)}^2"
            if four_p < 0:
                rhs = f"-{abs(four_p)}{_shift_expr('y', k)}"
            else:
                rhs = f"{four_p}{_shift_expr('y', k)}"
            direction = "up" if p > 0 else "down"
            reason = (
                r"The squared term is $(x - h)^2$, so the axis of symmetry is "
                r"vertical. Since $p > 0$ it opens up; $p < 0$ opens down."
            )
        else:
            lhs = f"{_shift_expr('y', k)}^2"
            if four_p < 0:
                rhs = f"-{abs(four_p)}{_shift_expr('x', h)}"
            else:
                rhs = f"{four_p}{_shift_expr('x', h)}"
            direction = "right" if p > 0 else "left"
            reason = (
                r"The squared term is $(y - k)^2$, so the axis of symmetry is "
                r"horizontal. Since $p > 0$ it opens right; $p < 0$ opens left."
            )

        equation_latex = f"{lhs} = {rhs}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (orientation, h, k, p)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In which direction does the parabola ${equation_latex}$ "
                "open? (up, down, left, or right)"
            ),
            answer_latex=f"The parabola opens **{direction}**.",
            hints=[
                (
                    r"If $x$ is squared, the parabola opens up or down. If $y$ "
                    r"is squared, it opens left or right."
                ),
                (
                    r"The sign of the coefficient $4p$ determines the specific "
                    r"direction."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Examine ${equation_latex}$: identify which variable is "
                    "squared."
                ),
                reason,
                f"Therefore the parabola opens **{direction}**.",
            ],
            tags=CONIC_TAGS,
        )


# ===========================================================================
# Topic 2: ellipses
# ===========================================================================


@register
class EllipseIdentifyCenterAxes(Generator):
    """Given standard-form ellipse, identify center, major-axis length,
    minor-axis length.

    Backward: pick center $(h, k)$ and two distinct positive $a, b$. Always
    render with $a > b$ or with the longer axis on whichever is larger.
    """

    generator_id = "ellipse_identify_center_axes"
    topic_slug = "ellipses"
    display_name = "Identify center, major axis, and minor axis of an ellipse"

    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _AB_CHOICES = {
        "easy": ((2, 3), (3, 4), (4, 5), (3, 5), (2, 5)),
        "medium": ((2, 3), (3, 4), (4, 5), (2, 5), (3, 5), (4, 6), (5, 6)),
        "hard": ((2, 3), (3, 4), (4, 5), (5, 6), (2, 7), (3, 7), (4, 7), (6, 7)),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])

        pair = rng.choice(self._AB_CHOICES[difficulty])
        a, b = max(pair), min(pair)  # a is the larger semi-axis
        # Randomly put the larger axis on x or y.
        horizontal = rng.choice([True, False])
        if horizontal:
            denom_x, denom_y = a * a, b * b
        else:
            denom_x, denom_y = b * b, a * a

        x_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{denom_x}}}"
        y_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{denom_y}}}"
        equation_latex = f"{x_term} + {y_term} = 1"

        center_latex = _format_point(h, k)
        major_len = 2 * a
        minor_len = 2 * b
        axis_word = "horizontal" if horizontal else "vertical"

        answer_latex = (
            f"Center: ${center_latex}$; major axis (${axis_word}$) length "
            f"$= {major_len}$; minor axis length $= {minor_len}$"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (h, k, a, b, horizontal)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the ellipse ${equation_latex}$, identify the center, "
                "the length of the major axis, and the length of the minor "
                "axis."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"An ellipse $\dfrac{(x - h)^2}{a^2} + \dfrac{(y - k)^2}{b^2} "
                    r"= 1$ has center $(h,\ k)$. The larger denominator belongs "
                    r"to the major-axis variable."
                ),
                (
                    f"Here the larger denominator is ${a * a}$, giving "
                    f"$a = {a}$, and the smaller is ${b * b}$, giving $b = {b}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compare ${equation_latex}$ to the standard form. The "
                    f"center is $(h,\\ k) = {center_latex}$."
                ),
                (
                    f"The larger denominator ${a * a}$ sits under the "
                    f"${'x' if horizontal else 'y'}$-term, so $a = {a}$ and "
                    f"the major axis is {axis_word} with length $2a = {major_len}$."
                ),
                (
                    f"The smaller denominator ${b * b}$ gives $b = {b}$, so "
                    f"the minor axis has length $2b = {minor_len}$."
                ),
            ],
            tags=CONIC_TAGS,
        )


@register
class EllipseFindFoci(Generator):
    """Given standard-form ellipse, compute $c = \\sqrt{a^2 - b^2}$ and state foci.

    Backward: pick integer $a, b$ with $a > b$ such that $a^2 - b^2$ is a
    perfect square.
    """

    generator_id = "ellipse_find_foci"
    topic_slug = "ellipses"
    display_name = "Find the foci of an ellipse with a clean a^2 - b^2"

    # Pythagorean-style (a, b, c) with c = sqrt(a^2 - b^2) an integer.
    _TRIPLES = (
        (5, 3, 4),
        (5, 4, 3),
        (10, 6, 8),
        (10, 8, 6),
        (13, 5, 12),
        (13, 12, 5),
        (17, 8, 15),
        (17, 15, 8),
        (25, 7, 24),
        (25, 24, 7),
        (15, 9, 12),
        (15, 12, 9),
    )

    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c = rng.choice(self._TRIPLES)
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])
        horizontal = rng.choice([True, False])

        if horizontal:
            denom_x, denom_y = a * a, b * b
            focus1 = (h - c, k)
            focus2 = (h + c, k)
            axis_word = "horizontal"
        else:
            denom_x, denom_y = b * b, a * a
            focus1 = (h, k - c)
            focus2 = (h, k + c)
            axis_word = "vertical"

        x_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{denom_x}}}"
        y_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{denom_y}}}"
        equation_latex = f"{x_term} + {y_term} = 1"

        focus1_latex = _format_point(*focus1)
        focus2_latex = _format_point(*focus2)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (h, k, a, b, c, horizontal)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the foci of the ellipse ${equation_latex}$."
            ),
            answer_latex=f"Foci: ${focus1_latex}$ and ${focus2_latex}$",
            hints=[
                (
                    r"For an ellipse with $a > b$, the focal distance is "
                    r"$c = \sqrt{a^2 - b^2}$. The foci lie on the major axis, "
                    r"$c$ units on either side of the center."
                ),
                (
                    f"Compute $c = \\sqrt{{{a * a} - {b * b}}} = \\sqrt{{{a * a - b * b}}} = {c}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify $a^2 = {a * a}$, $b^2 = {b * b}$, so "
                    f"$c^2 = a^2 - b^2 = {a * a - b * b}$ and $c = {c}$."
                ),
                (
                    f"The major axis is {axis_word}, so the foci are offset "
                    f"by $c = {c}$ from the center in the "
                    f"{'x' if horizontal else 'y'}-direction."
                ),
                (
                    f"Foci: ${focus1_latex}$ and ${focus2_latex}$."
                ),
            ],
            tags=CONIC_TAGS,
        )


@register
class EllipseWriteFromCenterAndAxes(Generator):
    """Given center, $a$, and $b$, write the standard-form ellipse equation.

    Backward: pick center $(h, k)$, $a, b$, and orientation; output the
    equation.
    """

    generator_id = "ellipse_write_from_center_and_axes"
    topic_slug = "ellipses"
    display_name = "Write an ellipse equation from center and axis lengths"

    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _AB_CHOICES = {
        "easy": ((2, 3), (3, 4), (4, 5), (3, 5)),
        "medium": ((2, 3), (3, 4), (4, 5), (3, 5), (4, 6), (5, 6)),
        "hard": ((3, 5), (4, 6), (5, 7), (4, 8), (6, 8), (5, 9)),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])
        pair = rng.choice(self._AB_CHOICES[difficulty])
        a, b = max(pair), min(pair)  # a is the larger semi-axis
        horizontal = rng.choice([True, False])

        if horizontal:
            denom_x, denom_y = a * a, b * b
            axis_word = "horizontal"
        else:
            denom_x, denom_y = b * b, a * a
            axis_word = "vertical"

        x_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{denom_x}}}"
        y_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{denom_y}}}"
        equation_latex = f"{x_term} + {y_term} = 1"

        center_latex = _format_point(h, k)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (h, k, a, b, horizontal)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the standard-form equation of an ellipse with center "
                f"${center_latex}$, semi-major axis $a = {a}$, and semi-minor "
                f"axis $b = {b}$, where the major axis is {axis_word}."
            ),
            answer_latex=f"${equation_latex}$",
            hints=[
                (
                    r"Use the standard form $\dfrac{(x - h)^2}{a^2} + "
                    r"\dfrac{(y - k)^2}{b^2} = 1$. If the major axis is "
                    r"horizontal, $a^2$ sits under the $x$-term; otherwise "
                    r"under the $y$-term."
                ),
                (
                    f"Square the semi-axes: $a^2 = {a * a}$ and $b^2 = {b * b}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Center $(h,\\ k) = {center_latex}$, so "
                    f"$h = {h}$ and $k = {k}$."
                ),
                (
                    f"With a {axis_word} major axis, the larger square ${a * a}$ "
                    f"goes under the $\\mathit{{{'x' if horizontal else 'y'}}}$-term, "
                    f"and ${b * b}$ under the other."
                ),
                f"Substitute to obtain ${equation_latex}$.",
            ],
            tags=CONIC_TAGS,
        )


# ===========================================================================
# Topic 3: hyperbolas
# ===========================================================================


@register
class HyperbolaIdentifyFeatures(Generator):
    """Given standard-form hyperbola, identify center, vertices, and foci.

    Backward: pick integer $a, b$ so $c = \\sqrt{a^2 + b^2}$ is also an
    integer (Pythagorean triples).
    """

    generator_id = "hyperbola_identify_features"
    topic_slug = "hyperbolas"
    display_name = "Identify center, vertices, and foci of a hyperbola"

    _TRIPLES = (
        (3, 4, 5),
        (4, 3, 5),
        (5, 12, 13),
        (12, 5, 13),
        (8, 15, 17),
        (15, 8, 17),
        (7, 24, 25),
        (24, 7, 25),
        (6, 8, 10),
        (8, 6, 10),
        (9, 12, 15),
        (12, 9, 15),
    )

    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c = rng.choice(self._TRIPLES)
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])
        horizontal = rng.choice([True, False])

        if horizontal:
            # (x-h)^2/a^2 - (y-k)^2/b^2 = 1
            positive_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{a * a}}}"
            negative_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{b * b}}}"
            vertex1 = (h - a, k)
            vertex2 = (h + a, k)
            focus1 = (h - c, k)
            focus2 = (h + c, k)
            axis_word = "horizontal (the x-axis of the hyperbola)"
        else:
            positive_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{a * a}}}"
            negative_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{b * b}}}"
            vertex1 = (h, k - a)
            vertex2 = (h, k + a)
            focus1 = (h, k - c)
            focus2 = (h, k + c)
            axis_word = "vertical (the y-axis of the hyperbola)"

        equation_latex = f"{positive_term} - {negative_term} = 1"
        center_latex = _format_point(h, k)
        v1_latex = _format_point(*vertex1)
        v2_latex = _format_point(*vertex2)
        f1_latex = _format_point(*focus1)
        f2_latex = _format_point(*focus2)

        answer_latex = (
            f"Center: ${center_latex}$; "
            f"vertices: ${v1_latex}$, ${v2_latex}$; "
            f"foci: ${f1_latex}$, ${f2_latex}$"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (h, k, a, b, c, horizontal)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Identify the center, vertices, and foci of the hyperbola "
                f"${equation_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"For a hyperbola, the transverse axis passes through the "
                    r"vertex of the positive term. Vertices sit $a$ units from "
                    r"the center along that axis."
                ),
                (
                    r"Use $c^2 = a^2 + b^2$ (plus, not minus) to locate the foci. "
                    f"Here $c = \\sqrt{{{a * a} + {b * b}}} = \\sqrt{{{a * a + b * b}}} = {c}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read $a^2 = {a * a}$ (so $a = {a}$) and "
                    f"$b^2 = {b * b}$ (so $b = {b}$). Compute "
                    f"$c = \\sqrt{{a^2 + b^2}} = \\sqrt{{{a * a + b * b}}} = {c}$."
                ),
                (
                    f"The transverse axis is {axis_word}."
                ),
                (
                    f"Center ${center_latex}$; "
                    f"vertices ${v1_latex}$ and ${v2_latex}$; "
                    f"foci ${f1_latex}$ and ${f2_latex}$."
                ),
            ],
            tags=CONIC_TAGS,
        )


@register
class HyperbolaWriteAsymptoteEquations(Generator):
    """Given standard-form hyperbola, write the asymptote equations.

    For horizontal-axis hyperbolas the asymptotes are
    $y - k = \\pm (b/a)(x - h)$; for vertical, $y - k = \\pm (a/b)(x - h)$.
    """

    generator_id = "hyperbola_write_asymptote_equations"
    topic_slug = "hyperbolas"
    display_name = "Write the asymptote equations of a hyperbola"

    _A_CHOICES = {"easy": (2, 3, 4), "medium": (2, 3, 4, 5, 6), "hard": (2, 3, 4, 5, 6, 7, 8)}
    _B_CHOICES = {"easy": (1, 2, 3), "medium": (1, 2, 3, 4, 5), "hard": (1, 2, 3, 4, 5, 6, 7)}
    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-10, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        b = rng.choice(self._B_CHOICES[difficulty])
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])
        horizontal = rng.choice([True, False])

        if horizontal:
            positive_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{a * a}}}"
            negative_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{b * b}}}"
            # slopes +/- b/a
            slope = sp.Rational(b, a)
        else:
            positive_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{a * a}}}"
            negative_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{b * b}}}"
            # slopes +/- a/b
            slope = sp.Rational(a, b)

        equation_latex = f"{positive_term} - {negative_term} = 1"
        slope_latex = sp.latex(slope)

        lhs = _shift_expr("y", -k)  # (y + k) if k negative etc -- but we want y - k
        # The helper uses (var op n) style with "y - k"; using _shift_expr('y', k)
        # returns "(y - k)" for k > 0 and "(y + |k|)" for k < 0. For asymptote
        # form we want "y - k" without outer parens, so recompute.
        if k == 0:
            y_side = "y"
        elif k > 0:
            y_side = f"y - {k}"
        else:
            y_side = f"y + {abs(k)}"
        if h == 0:
            x_side = "x"
        elif h > 0:
            x_side = f"(x - {h})"
        else:
            x_side = f"(x + {abs(h)})"

        asymptote_latex = rf"{y_side} = \pm {slope_latex}{x_side}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (h, k, a, b, horizontal)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the equations of the asymptotes of the hyperbola "
                f"${equation_latex}$."
            ),
            answer_latex=f"${asymptote_latex}$",
            hints=[
                (
                    r"For $\dfrac{(x - h)^2}{a^2} - \dfrac{(y - k)^2}{b^2} = 1$ "
                    r"the asymptotes are $y - k = \pm \dfrac{b}{a}(x - h)$."
                ),
                (
                    r"For the vertical-transverse variant $\dfrac{(y - k)^2}{a^2} - "
                    r"\dfrac{(x - h)^2}{b^2} = 1$, use slopes $\pm \dfrac{a}{b}$ instead."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read $a = {a}$, $b = {b}$, center $(h,\\ k) = "
                    f"{_format_point(h, k)}$."
                ),
                (
                    f"The transverse axis is "
                    f"{'horizontal' if horizontal else 'vertical'}, so the "
                    f"asymptote slopes are "
                    f"$\\pm {slope_latex}$."
                ),
                (
                    f"Write the asymptote equations: ${asymptote_latex}$."
                ),
            ],
            tags=CONIC_TAGS,
        )


@register
class HyperbolaHorizontalVsVerticalAxis(Generator):
    """Classify whether a hyperbola has horizontal or vertical transverse axis.

    Based on which variable sits in the positive term.
    """

    generator_id = "hyperbola_horizontal_vs_vertical_axis"
    topic_slug = "hyperbolas"
    display_name = "Classify hyperbola transverse axis (horizontal or vertical)"

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice([2, 3, 4, 5, 6])
        b = rng.choice([2, 3, 4, 5, 6])
        h = rng.randint(-5, 5)
        k = rng.randint(-5, 5)
        horizontal = rng.choice([True, False])

        if horizontal:
            positive_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{a * a}}}"
            negative_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{b * b}}}"
            answer_word = "horizontal"
            reason = (
                r"The positive term contains $(x - h)^2$, so the transverse "
                r"axis is horizontal (parallel to the $x$-axis)."
            )
        else:
            positive_term = rf"\dfrac{{{_shift_expr('y', k)}^2}}{{{a * a}}}"
            negative_term = rf"\dfrac{{{_shift_expr('x', h)}^2}}{{{b * b}}}"
            answer_word = "vertical"
            reason = (
                r"The positive term contains $(y - k)^2$, so the transverse "
                r"axis is vertical (parallel to the $y$-axis)."
            )

        equation_latex = f"{positive_term} - {negative_term} = 1"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (h, k, a, b, horizontal)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Does the hyperbola ${equation_latex}$ have a horizontal "
                "or vertical transverse axis?"
            ),
            answer_latex=f"The transverse axis is **{answer_word}**.",
            hints=[
                (
                    r"In the standard form of a hyperbola, one term is positive "
                    r"and the other negative. The positive term tells you which "
                    r"variable 'opens'."
                ),
                (
                    r"If $(x - h)^2$ is positive, the axis is horizontal. If "
                    r"$(y - k)^2$ is positive, the axis is vertical."
                ),
            ],
            solution_steps_latex=[
                f"Look at the standard form ${equation_latex}$.",
                reason,
                f"Therefore the transverse axis is **{answer_word}**.",
            ],
            tags=CONIC_TAGS,
        )


# ===========================================================================
# Topic 4: circumference_and_area_of_circles
# ===========================================================================


def _format_pi_coef(coef) -> str:
    """Render a coefficient times pi, omitting 1 and handling 0."""
    if coef == 0:
        return "0"
    if coef == 1:
        return r"\pi"
    if coef == -1:
        return r"-\pi"
    return rf"{coef}\pi"


@register
class CircleCircumferenceFromRadius(Generator):
    """Given integer radius, compute circumference $C = 2\\pi r$.

    Provides both exact (in terms of pi) and decimal (pi ~ 3.14) answers.
    """

    generator_id = "circle_circumference_from_radius"
    topic_slug = "circumference_and_area_of_circles"
    display_name = "Compute the circumference of a circle from its radius"

    _R_RANGES = {"easy": (1, 10), "medium": (1, 20), "hard": (1, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.randint(*self._R_RANGES[difficulty])

        exact_latex = _format_pi_coef(2 * r)
        decimal_value = 2 * r * 3.14
        decimal_latex = f"{decimal_value:.2f}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A circle has radius $r = {r}$ units. Find its circumference "
                f"exactly (in terms of $\\pi$) and approximately "
                r"(using $\pi \approx 3.14$, rounded to 2 decimal places)."
            ),
            answer_latex=(
                f"Exact: $C = {exact_latex}$ units; approx: $C \\approx {decimal_latex}$ units"
            ),
            hints=[
                r"The circumference of a circle is $C = 2\pi r$.",
                (
                    r"For the exact answer, leave $\pi$ as a symbol. For the "
                    r"decimal answer, multiply your exact coefficient by $3.14$."
                ),
            ],
            solution_steps_latex=[
                f"Substitute $r = {r}$ into $C = 2\\pi r$: $C = 2\\pi({r})$.",
                f"Simplify: $C = {exact_latex}$ units (exact).",
                (
                    f"Approximate with $\\pi \\approx 3.14$: "
                    f"$C \\approx {2 * r} \\times 3.14 = {decimal_latex}$ units."
                ),
            ],
            tags=CIRCLE_GEO_TAGS,
        )


@register
class CircleAreaFromRadius(Generator):
    """Given integer radius, compute area $A = \\pi r^2$."""

    generator_id = "circle_area_from_radius"
    topic_slug = "circumference_and_area_of_circles"
    display_name = "Compute the area of a circle from its radius"

    _R_RANGES = {"easy": (1, 10), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.randint(*self._R_RANGES[difficulty])

        exact_latex = _format_pi_coef(r * r)
        decimal_value = r * r * 3.14
        decimal_latex = f"{decimal_value:.2f}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A circle has radius $r = {r}$ units. Find its area exactly "
                f"(in terms of $\\pi$) and approximately "
                r"(using $\pi \approx 3.14$, rounded to 2 decimal places)."
            ),
            answer_latex=(
                f"Exact: $A = {exact_latex}$ square units; "
                f"approx: $A \\approx {decimal_latex}$ square units"
            ),
            hints=[
                r"The area of a circle is $A = \pi r^2$.",
                (
                    r"Square $r$ first, then multiply by $\pi$ for the exact "
                    r"answer (or by $3.14$ for the decimal approximation)."
                ),
            ],
            solution_steps_latex=[
                f"Substitute $r = {r}$ into $A = \\pi r^2$: $A = \\pi({r})^2$.",
                f"Square the radius: ${r}^2 = {r * r}$.",
                f"Multiply by $\\pi$: $A = {exact_latex}$ square units (exact).",
                (
                    f"Approximate with $\\pi \\approx 3.14$: "
                    f"$A \\approx {r * r} \\times 3.14 = {decimal_latex}$ square units."
                ),
            ],
            tags=CIRCLE_GEO_TAGS,
        )


@register
class CircleRadiusFromCircumferenceOrArea(Generator):
    """Given $C$ or $A$ in terms of $\\pi$, find the radius.

    Backward: pick integer $r$, then present either $C = 2\\pi r$ or
    $A = \\pi r^2$, and ask for $r$.
    """

    generator_id = "circle_radius_from_circumference_or_area"
    topic_slug = "circumference_and_area_of_circles"
    display_name = "Find the radius of a circle from its circumference or area"

    _R_RANGES = {"easy": (2, 10), "medium": (2, 15), "hard": (2, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.randint(*self._R_RANGES[difficulty])
        use_area = rng.choice([True, False])

        if use_area:
            measure_coef = r * r
            measure_latex = _format_pi_coef(measure_coef)
            statement = (
                f"A circle has area $A = {measure_latex}$ square units. Find "
                "its radius."
            )
            hint_1 = r"Start with $A = \pi r^2$, divide both sides by $\pi$, and take the square root."
            hint_2 = f"Here $\\pi r^2 = {measure_latex}$, so $r^2 = {measure_coef}$."
            step_1 = f"From $A = \\pi r^2 = {measure_latex}$ divide by $\\pi$: $r^2 = {measure_coef}$."
            step_2 = f"Take the positive square root: $r = \\sqrt{{{measure_coef}}} = {r}$ units."
        else:
            measure_coef = 2 * r
            measure_latex = _format_pi_coef(measure_coef)
            statement = (
                f"A circle has circumference $C = {measure_latex}$ units. "
                "Find its radius."
            )
            hint_1 = r"Start with $C = 2\pi r$ and solve for $r$ by dividing both sides by $2\pi$."
            hint_2 = f"Here $2\\pi r = {measure_latex}$, so $r = \\dfrac{{{measure_coef}}}{{2}} = {r}$."
            step_1 = f"From $C = 2\\pi r = {measure_latex}$ divide by $\\pi$: $2r = {measure_coef}$."
            step_2 = f"Divide by 2: $r = {r}$ units."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, use_area)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$r = {r}$ units",
            hints=[hint_1, hint_2],
            solution_steps_latex=[step_1, step_2],
            tags=CIRCLE_GEO_TAGS,
        )


# ===========================================================================
# Topic 5: the_complex_number_system
# ===========================================================================


def _format_complex(a: int, b: int) -> str:
    """Render a + bi with clean signs and omitting 0 parts.

    >>> _format_complex(3, 4)
    '3 + 4i'
    >>> _format_complex(0, 4)
    '4i'
    >>> _format_complex(3, 0)
    '3'
    >>> _format_complex(3, -1)
    '3 - i'
    >>> _format_complex(-2, 1)
    '-2 + i'
    >>> _format_complex(0, -1)
    '-i'
    """
    if a == 0 and b == 0:
        return "0"
    if a == 0:
        if b == 1:
            return "i"
        if b == -1:
            return "-i"
        return f"{b}i"
    if b == 0:
        return str(a)
    # Both nonzero
    if b > 0:
        if b == 1:
            return f"{a} + i"
        return f"{a} + {b}i"
    else:
        if b == -1:
            return f"{a} - i"
        return f"{a} - {abs(b)}i"


def _format_complex_parens(a: int, b: int) -> str:
    """Same as _format_complex but wraps in parens for display after 'x'."""
    return f"({_format_complex(a, b)})"


@register
class ComplexArithmeticBasic(Generator):
    """Compute a sum or product of two complex numbers with integer parts."""

    generator_id = "complex_arithmetic_basic"
    topic_slug = "the_complex_number_system"
    display_name = "Add or multiply complex numbers (a + bi operations)"

    _RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        d = rng.randint(lo, hi)
        while a == 0 and b == 0:
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
        while c == 0 and d == 0:
            c = rng.randint(lo, hi)
            d = rng.randint(lo, hi)

        op = rng.choice(["+", "*"])

        z1_latex = _format_complex(a, b)
        z2_latex = _format_complex(c, d)

        if op == "+":
            real = a + c
            imag = b + d
            statement = f"Compute $({z1_latex}) + ({z2_latex})$."
            expansion_step = (
                f"Combine real and imaginary parts separately: "
                f"$({a} + {c}) + ({b} + {d})i$."
            )
        else:
            # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
            real = a * c - b * d
            imag = a * d + b * c
            statement = f"Compute $({z1_latex})({z2_latex})$."
            expansion_step = (
                f"Expand using FOIL and $i^2 = -1$: "
                f"$({a})({c}) + ({a})({d})i + ({b})({c})i + ({b})({d})i^2$."
            )

        answer_latex = _format_complex(real, imag)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, op)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"For addition, add real parts and imaginary parts separately. "
                    r"For multiplication, FOIL and use $i^2 = -1$."
                ),
                (
                    r"Keep track of which terms are 'real' (no $i$) and which "
                    r"are 'imaginary' (one factor of $i$)."
                ),
            ],
            solution_steps_latex=[
                f"Start with $({z1_latex}) {op if op == '+' else '\\cdot'} ({z2_latex})$.",
                expansion_step,
                (
                    f"Combine real parts: ${real}$. Combine imaginary parts: "
                    f"${imag}i$."
                ),
                f"Final answer: ${answer_latex}$.",
            ],
            tags=COMPLEX_TAGS_ALG2,
        )


@register
class ComplexConjugateAndModulus(Generator):
    """Given $a + bi$ with $(a, b)$ from a Pythagorean triple, give its
    conjugate and integer modulus."""

    generator_id = "complex_conjugate_and_modulus"
    topic_slug = "the_complex_number_system"
    display_name = "Compute the conjugate and modulus of a complex number"

    # (a, b, |z|) Pythagorean triples and axis cases.
    _TRIPLES = (
        (3, 4, 5),
        (4, 3, 5),
        (5, 12, 13),
        (12, 5, 13),
        (8, 15, 17),
        (15, 8, 17),
        (7, 24, 25),
        (24, 7, 25),
        (6, 8, 10),
        (8, 6, 10),
        (9, 12, 15),
        (12, 9, 15),
        (0, 5, 5),
        (5, 0, 5),
        (0, 12, 12),
        (12, 0, 12),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a0, b0, r = rng.choice(self._TRIPLES)
        sign_a = rng.choice([-1, 1]) if a0 != 0 else 1
        sign_b = rng.choice([-1, 1]) if b0 != 0 else 1
        a = sign_a * a0
        b = sign_b * b0

        z_latex = _format_complex(a, b)
        conj_latex = _format_complex(a, -b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the complex number $z = {z_latex}$, find its conjugate "
                r"$\bar z$ and its modulus $|z|$."
            ),
            answer_latex=(
                rf"$\bar z = {conj_latex}$; $|z| = {r}$"
            ),
            hints=[
                (
                    r"The conjugate of $a + bi$ is $a - bi$ — flip the sign of "
                    r"the imaginary part only."
                ),
                (
                    r"The modulus is $|a + bi| = \sqrt{a^2 + b^2}$, the "
                    r"distance from the origin to the point $(a,\ b)$ in the "
                    r"complex plane."
                ),
            ],
            solution_steps_latex=[
                f"Starting with $z = {z_latex}$, flip the sign of the imaginary part to find the conjugate: $\\bar z = {conj_latex}$.",
                (
                    f"Apply $|z| = \\sqrt{{a^2 + b^2}}$: "
                    f"$|z| = \\sqrt{{{a * a} + {b * b}}} = \\sqrt{{{a * a + b * b}}} = {r}$."
                ),
            ],
            tags=COMPLEX_TAGS_ALG2,
        )


@register
class ComplexDivisionByConjugate(Generator):
    """Compute $(a + bi)/(c + di)$ by multiplying top and bottom by the
    conjugate of the denominator.

    Backward: pick integers $(c, d)$ so $c^2 + d^2$ is small, and integers
    $(p, q)$ for the quotient; then build the numerator as
    $(p + qi)(c + di)$.
    """

    generator_id = "complex_division_by_conjugate"
    topic_slug = "the_complex_number_system"
    display_name = "Divide complex numbers using the conjugate of the denominator"

    _DENOM_CHOICES = (
        (1, 1), (1, -1), (2, 1), (2, -1), (1, 2), (1, -2),
        (3, 1), (3, -1), (1, 3), (1, -3), (2, 3), (2, -3), (3, 2), (3, -2),
    )
    _QUOT_RANGES = {"easy": (-3, 3), "medium": (-5, 5), "hard": (-7, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c, d = rng.choice(self._DENOM_CHOICES)
        lo, hi = self._QUOT_RANGES[difficulty]
        p = rng.randint(lo, hi)
        q = rng.randint(lo, hi)
        while p == 0 and q == 0:
            p = rng.randint(lo, hi)
            q = rng.randint(lo, hi)

        # numerator = (p + qi)(c + di)
        a = p * c - q * d
        b = p * d + q * c

        num_latex = _format_complex(a, b)
        den_latex = _format_complex(c, d)
        conj_latex = _format_complex(c, -d)
        quotient_latex = _format_complex(p, q)
        modsq = c * c + d * d

        statement = (
            f"Compute $\\dfrac{{{num_latex}}}{{{den_latex}}}$. "
            "Give your answer in $a + bi$ form."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, d, p, q)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${quotient_latex}$",
            hints=[
                (
                    r"Multiply numerator and denominator by the conjugate of "
                    r"the denominator. The new denominator is "
                    r"$c^2 + d^2$ (a real number)."
                ),
                (
                    r"After multiplying, expand using FOIL and $i^2 = -1$, "
                    r"then separate real and imaginary parts and divide each "
                    r"by the new denominator."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Multiply top and bottom by the conjugate of the "
                    f"denominator, ${conj_latex}$: "
                    f"$\\dfrac{{({num_latex})({conj_latex})}}{{({den_latex})({conj_latex})}}$."
                ),
                (
                    f"The denominator becomes "
                    f"$({c})^2 + ({d})^2 = {modsq}$."
                ),
                (
                    f"Expand the numerator and divide by ${modsq}$ to obtain "
                    f"${quotient_latex}$."
                ),
            ],
            tags=COMPLEX_TAGS_ALG2,
        )


# ===========================================================================
# Topic 6: complex_zeros
# ===========================================================================


@register
class ComplexRootsFromQuadratic(Generator):
    """Given a real-coefficient quadratic with negative discriminant, find
    the complex roots via the quadratic formula.

    Backward: pick integer real part $p$ and positive imaginary part $q$.
    The roots are $p \\pm qi$, with $a = 1$, $b = -2p$, $c = p^2 + q^2$.
    """

    generator_id = "complex_roots_from_quadratic"
    topic_slug = "complex_zeros"
    display_name = "Find complex roots of a quadratic via the quadratic formula"

    _P_RANGES = {"easy": (-3, 3), "medium": (-5, 5), "hard": (-8, 8)}
    _Q_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        p = rng.randint(*self._P_RANGES[difficulty])
        q = rng.randint(*self._Q_RANGES[difficulty])

        a = 1
        b = -2 * p
        c = p * p + q * q

        # Render quadratic
        def _q_term(coeff: int, var: str) -> str:
            if coeff == 0:
                return ""
            sign = " + " if coeff > 0 else " - "
            mag = abs(coeff)
            mag_s = "" if mag == 1 else str(mag)
            return f"{sign}{mag_s}{var}"

        poly_latex = f"x^2{_q_term(b, 'x')}{_q_term(c, '')}"
        poly_latex = poly_latex.replace(" + ", " + ", 1) if poly_latex.startswith("x^2 + ") else poly_latex
        # Clean leading ' + ': impossible since starts with 'x^2'
        root1_latex = _format_complex(p, q)
        root2_latex = _format_complex(p, -q)
        disc = b * b - 4 * a * c  # = -4q^2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the complex roots of the equation ${poly_latex} = 0$. "
                "Give your answer in $a + bi$ form."
            ),
            answer_latex=f"$x = {root1_latex}$ and $x = {root2_latex}$",
            hints=[
                (
                    r"Apply the quadratic formula "
                    r"$x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. The "
                    r"discriminant is negative, so use "
                    r"$\sqrt{-k} = i\sqrt{k}$."
                ),
                (
                    f"Here $a = 1$, $b = {b}$, $c = {c}$, so "
                    f"$b^2 - 4ac = {disc}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify $a = 1$, $b = {b}$, $c = {c}$, and compute "
                    f"the discriminant $b^2 - 4ac = {disc}$."
                ),
                (
                    f"Since the discriminant is negative, factor out $-1$: "
                    f"$\\sqrt{{{disc}}} = {2 * q}i$."
                ),
                (
                    f"Plug into the quadratic formula: "
                    f"$x = \\dfrac{{{-b} \\pm {2 * q}i}}{{2}}$."
                ),
                (
                    f"Simplify: $x = {root1_latex}$ and $x = {root2_latex}$."
                ),
            ],
            tags=COMPLEX_TAGS_ALG2,
        )


@register
class ComplexConjugatePairsApply(Generator):
    """Given one complex root of a real-coefficient polynomial, state the
    other root (its conjugate)."""

    generator_id = "complex_conjugate_pairs_apply"
    topic_slug = "complex_zeros"
    display_name = "Apply the conjugate root theorem"

    _RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(1, hi)  # positive imaginary part so the statement is distinctive
        sign_b = rng.choice([-1, 1])
        b *= sign_b

        z_latex = _format_complex(a, b)
        conj_latex = _format_complex(a, -b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A polynomial with real coefficients has ${z_latex}$ as a "
                "root. State another root that must also appear."
            ),
            answer_latex=f"${conj_latex}$",
            hints=[
                (
                    r"The Conjugate Root Theorem says that for a polynomial "
                    r"with real coefficients, complex roots come in conjugate "
                    r"pairs."
                ),
                (
                    r"To find the conjugate, flip the sign of the imaginary "
                    r"part: $a + bi \to a - bi$."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Since the polynomial has real coefficients and "
                    f"${z_latex}$ is a root, the complex conjugate must also "
                    r"be a root."
                ),
                f"Flip the sign of the imaginary part: ${z_latex} \\to {conj_latex}$.",
                f"Therefore, ${conj_latex}$ is also a root.",
            ],
            tags=COMPLEX_TAGS_ALG2,
        )


@register
class PolynomialFromGivenZeros(Generator):
    """Given one real zero and a conjugate pair, multiply them out to a
    cubic with real integer coefficients.

    Backward: pick integer real root $r$, and a conjugate pair $p \\pm qi$;
    multiply out $(x - r)(x - (p + qi))(x - (p - qi))
    = (x - r)(x^2 - 2px + (p^2 + q^2))$.
    """

    generator_id = "polynomial_from_given_zeros"
    topic_slug = "complex_zeros"
    display_name = "Build a cubic polynomial from one real and a conjugate pair of zeros"

    bank_count_per_difficulty = 18

    _R_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}
    _P_RANGES = {"easy": (-3, 3), "medium": (-5, 5), "hard": (-6, 6)}
    _Q_RANGES = {"easy": (1, 3), "medium": (1, 4), "hard": (1, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.randint(*self._R_RANGES[difficulty])
        while r == 0:
            r = rng.randint(*self._R_RANGES[difficulty])
        p = rng.randint(*self._P_RANGES[difficulty])
        q = rng.randint(*self._Q_RANGES[difficulty])

        # Quadratic factor from the conjugate pair: x^2 - 2px + (p^2 + q^2)
        b_q = -2 * p
        c_q = p * p + q * q

        # Cubic: (x - r)(x^2 + b_q*x + c_q)
        x = sp.Symbol("x")
        poly = sp.expand((x - r) * (x * x + b_q * x + c_q))
        coeffs = sp.Poly(poly, x).all_coeffs()  # highest degree first
        while len(coeffs) < 4:
            coeffs.insert(0, 0)
        a3, a2, a1, a0 = coeffs

        def _render_term(coef: int, power: int) -> str:
            if coef == 0:
                return ""
            if power == 0:
                body = str(abs(coef))
            elif power == 1:
                body = f"{abs(coef)}x" if abs(coef) != 1 else "x"
            else:
                body = f"{abs(coef)}x^{power}" if abs(coef) != 1 else f"x^{power}"
            sign = " + " if coef > 0 else " - "
            return sign + body

        poly_str = ""
        # a3 is 1, always
        poly_str += "x^3" if a3 == 1 else f"{a3}x^3"
        poly_str += _render_term(int(a2), 2)
        poly_str += _render_term(int(a1), 1)
        poly_str += _render_term(int(a0), 0)

        conj_pair_latex = f"{_format_complex(p, q)},\\ {_format_complex(p, -q)}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, p, q)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find a monic polynomial with real integer coefficients of "
                f"degree 3 whose zeros are $x = {r}$, $x = {_format_complex(p, q)}$, "
                f"and $x = {_format_complex(p, -q)}$."
            ),
            answer_latex=f"$P(x) = {poly_str}$",
            hints=[
                (
                    r"A polynomial with a complex root $p + qi$ and real "
                    r"coefficients must also have $p - qi$ as a root. Their "
                    r"joint factor is the quadratic $x^2 - 2px + (p^2 + q^2)$."
                ),
                (
                    f"Multiply $(x - {r})$ by the quadratic factor and expand "
                    r"to get a real-coefficient cubic."
                ),
            ],
            solution_steps_latex=[
                (
                    f"From the conjugate pair ${conj_pair_latex}$, form the "
                    f"quadratic factor $x^2 - 2({p})x + ({p}^2 + {q}^2) = "
                    f"x^2{' + ' if b_q >= 0 else ' - '}{abs(b_q)}x + {c_q}$."
                ),
                (
                    f"Multiply by the linear factor $(x - {r})$: "
                    f"$(x - {r})(x^2{' + ' if b_q >= 0 else ' - '}{abs(b_q)}x + {c_q})$."
                ),
                f"Expand to obtain ${poly_str}$.",
            ],
            tags=COMPLEX_TAGS_ALG2,
        )


# ===========================================================================
# Topic 7: polar_form_of_complex_numbers
# ===========================================================================


# Standard angles: (num, den) giving num*pi/den in [0, 2pi). Twelve entries.
_POLAR_ANGLES = (
    (0, 1),
    (1, 6),
    (1, 4),
    (1, 3),
    (1, 2),
    (2, 3),
    (3, 4),
    (5, 6),
    (1, 1),
    (7, 6),
    (5, 4),
    (4, 3),
    (3, 2),
    (5, 3),
    (7, 4),
    (11, 6),
)


def _format_polar(r_sym: sp.Expr, angle_latex: str) -> str:
    """Render $r(\\cos\\theta + i\\sin\\theta)$."""
    r_latex = sp.latex(r_sym)
    if r_latex == "1":
        head = ""
    else:
        head = r_latex
    return rf"{head}\left(\cos {angle_latex} + i\sin {angle_latex}\right)"


@register
class RectToPolarComplex(Generator):
    """Given $a + bi$ (with $a, b$ chosen from unit-circle-compatible values),
    convert to $r(\\cos\\theta + i\\sin\\theta)$.

    Backward: pick $r$ and standard $\\theta$, compute $a = r\\cos\\theta$,
    $b = r\\sin\\theta$, but restricted to combinations where $(a, b)$ is
    an integer or simple surd pair.
    """

    generator_id = "rect_to_polar_complex"
    topic_slug = "polar_form_of_complex_numbers"
    display_name = "Convert a complex number from rectangular to polar form"

    # Entries: (a, b, r_sym_str, (num, den) for angle)
    # Using only cases where a and b are integers -> purely axial angles.
    _CASES = (
        # r = 1
        (1, 0, 1, (0, 1)),
        (0, 1, 1, (1, 2)),
        (-1, 0, 1, (1, 1)),
        (0, -1, 1, (3, 2)),
        # r = 2
        (2, 0, 2, (0, 1)),
        (0, 2, 2, (1, 2)),
        (-2, 0, 2, (1, 1)),
        (0, -2, 2, (3, 2)),
        # r = 3
        (3, 0, 3, (0, 1)),
        (0, 3, 3, (1, 2)),
        (-3, 0, 3, (1, 1)),
        (0, -3, 3, (3, 2)),
        # r = 4
        (4, 0, 4, (0, 1)),
        (0, 4, 4, (1, 2)),
        (-4, 0, 4, (1, 1)),
        (0, -4, 4, (3, 2)),
        # Diagonal: r*sqrt(2)/2 style gives 45-degree cases — we provide
        # ones with integer a & b for simplicity. r = sqrt(2): (1, 1).
        # Keeping it simple: axial cases only so a, b are integers.
    )

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, r_val, (num, den) = rng.choice(self._CASES)
        z_latex = _format_complex(a, b)
        angle_latex = _format_pi_fraction(num, den)
        polar_latex = _format_polar(sp.Integer(r_val), angle_latex)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, num, den)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the complex number $z = {z_latex}$ in polar form "
                r"$r(\cos\theta + i\sin\theta)$."
            ),
            answer_latex=f"$z = {polar_latex}$",
            hints=[
                (
                    r"Compute the modulus $r = \sqrt{a^2 + b^2}$ and the "
                    r"argument $\theta$ with $\tan\theta = b/a$ (paying "
                    r"attention to the quadrant)."
                ),
                (
                    r"For numbers on the axes the argument is one of "
                    r"$0,\ \pi/2,\ \pi,\ 3\pi/2$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute $r = \\sqrt{{({a})^2 + ({b})^2}} = "
                    f"\\sqrt{{{a * a + b * b}}} = {r_val}$."
                ),
                (
                    f"The point $({a},\\ {b})$ in the complex plane gives "
                    f"argument $\\theta = {angle_latex}$."
                ),
                f"Write in polar form: $z = {polar_latex}$.",
            ],
            tags=COMPLEX_TAGS_PRECALC,
        )


@register
class PolarMultiplication(Generator):
    """Multiply two complex numbers in polar form: multiply moduli, add
    arguments.

    Backward: pick $r_1, r_2$ and two standard angles so the result stays
    within $[0, 2\\pi)$ after reduction.
    """

    generator_id = "polar_multiplication"
    topic_slug = "polar_form_of_complex_numbers"
    display_name = "Multiply two complex numbers in polar form"

    _R_CHOICES = {"easy": (1, 2, 3), "medium": (1, 2, 3, 4, 5), "hard": (1, 2, 3, 4, 5, 6, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r1 = rng.choice(self._R_CHOICES[difficulty])
        r2 = rng.choice(self._R_CHOICES[difficulty])
        num1, den1 = rng.choice(_POLAR_ANGLES)
        num2, den2 = rng.choice(_POLAR_ANGLES)

        # Add angles: (num1/den1 + num2/den2) * pi
        common = den1 * den2 // math.gcd(den1, den2)
        sum_num = num1 * (common // den1) + num2 * (common // den2)
        sum_den = common
        # Reduce into [0, 2*sum_den), equivalent to subtracting 2k from
        # sum_num / sum_den until in [0, 2).
        # angle = sum_num/sum_den * pi, we want representative in [0, 2*pi)
        # i.e. sum_num/sum_den in [0, 2) -> 0 <= sum_num < 2*sum_den
        while sum_num >= 2 * sum_den:
            sum_num -= 2 * sum_den
        while sum_num < 0:
            sum_num += 2 * sum_den

        ang1_latex = _format_pi_fraction(num1, den1)
        ang2_latex = _format_pi_fraction(num2, den2)
        sum_latex = _format_pi_fraction(sum_num, sum_den)

        z1_latex = _format_polar(sp.Integer(r1), ang1_latex)
        z2_latex = _format_polar(sp.Integer(r2), ang2_latex)
        product_latex = _format_polar(sp.Integer(r1 * r2), sum_latex)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (r1, r2, num1, den1, num2, den2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $z_1 = {z1_latex}$ and $z_2 = {z2_latex}$. Compute "
                "$z_1 z_2$ in polar form, with the argument in $[0,\\ 2\\pi)$."
            ),
            answer_latex=f"$z_1 z_2 = {product_latex}$",
            hints=[
                (
                    r"When multiplying complex numbers in polar form, multiply "
                    r"their moduli and add their arguments: "
                    r"$r_1 r_2(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2))$."
                ),
                (
                    r"After adding the angles, reduce into $[0,\ 2\pi)$ by "
                    r"subtracting $2\pi$ if necessary."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Multiply the moduli: $r_1 r_2 = {r1} \\cdot {r2} = {r1 * r2}$."
                ),
                (
                    f"Add the arguments: $\\theta_1 + \\theta_2 = "
                    f"{ang1_latex} + {ang2_latex}$, reduced to "
                    f"${sum_latex}$."
                ),
                f"Combine: $z_1 z_2 = {product_latex}$.",
            ],
            tags=COMPLEX_TAGS_PRECALC,
        )


@register
class DeMoivrePower(Generator):
    """Apply De Moivre's theorem: $[r(\\cos\\theta + i\\sin\\theta)]^n =
    r^n(\\cos(n\\theta) + i\\sin(n\\theta))$.

    Backward: pick small $n$ and a standard $\\theta$; reduce $n\\theta$ to
    $[0, 2\\pi)$.
    """

    generator_id = "de_moivre_power"
    topic_slug = "polar_form_of_complex_numbers"
    display_name = "Compute a power of a complex number via De Moivre's theorem"

    bank_count_per_difficulty = 18

    _R_CHOICES = {"easy": (1, 2), "medium": (1, 2, 3), "hard": (1, 2, 3, 4)}
    _N_CHOICES = {"easy": (2, 3, 4), "medium": (2, 3, 4, 5), "hard": (2, 3, 4, 5, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.choice(self._R_CHOICES[difficulty])
        n = rng.choice(self._N_CHOICES[difficulty])
        num, den = rng.choice(_POLAR_ANGLES)

        # n*theta = n*num*pi/den; reduce to [0, 2*pi)
        new_num = n * num
        new_den = den
        while new_num >= 2 * new_den:
            new_num -= 2 * new_den
        while new_num < 0:
            new_num += 2 * new_den

        base_angle_latex = _format_pi_fraction(num, den)
        result_angle_latex = _format_pi_fraction(new_num, new_den)

        z_latex = _format_polar(sp.Integer(r), base_angle_latex)
        r_n = r ** n
        result_latex = _format_polar(sp.Integer(r_n), result_angle_latex)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (r, n, num, den)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use De Moivre's theorem to compute $z^{{{n}}}$ where "
                f"$z = {z_latex}$. Give your answer in polar form with the "
                r"argument in $[0,\ 2\pi)$."
            ),
            answer_latex=f"$z^{{{n}}} = {result_latex}$",
            hints=[
                (
                    r"De Moivre's theorem: "
                    r"$[r(\cos\theta + i\sin\theta)]^n = "
                    r"r^n(\cos(n\theta) + i\sin(n\theta))$."
                ),
                (
                    r"Raise the modulus to the $n$-th power and multiply the "
                    r"argument by $n$, then reduce into $[0,\ 2\pi)$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Apply De Moivre: $z^{{{n}}} = {r}^{{{n}}}"
                    f"(\\cos({n} \\cdot {base_angle_latex}) + "
                    f"i\\sin({n} \\cdot {base_angle_latex}))$."
                ),
                (
                    f"Compute the new modulus: ${r}^{{{n}}} = {r_n}$, and the "
                    f"new argument, ${n} \\cdot {base_angle_latex}$, reduced "
                    f"to ${result_angle_latex}$."
                ),
                f"Therefore $z^{{{n}}} = {result_latex}$.",
            ],
            tags=COMPLEX_TAGS_PRECALC,
        )


# ===========================================================================
# Topic 8: introduction_to_polar_coordinates
# ===========================================================================


def _exact_trig_pair(num: int, den: int) -> tuple[sp.Expr, sp.Expr]:
    """Return exact sympy (cos theta, sin theta) for theta = num*pi/den."""
    theta = _pi_angle(num, den)
    return sp.cos(theta), sp.sin(theta)


@register
class PolarToRectConversion(Generator):
    """Given $(r, \\theta)$ with $\\theta$ an exact-value angle, compute
    $(x, y) = (r\\cos\\theta, r\\sin\\theta)$.
    """

    generator_id = "polar_to_rect_conversion"
    topic_slug = "introduction_to_polar_coordinates"
    display_name = "Convert a polar point (r, theta) to rectangular (x, y)"

    _R_CHOICES = {"easy": (1, 2, 3, 4), "medium": (1, 2, 3, 4, 5, 6), "hard": (1, 2, 3, 4, 5, 6, 7, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.choice(self._R_CHOICES[difficulty])
        num, den = rng.choice(_POLAR_ANGLES)

        cos_sym, sin_sym = _exact_trig_pair(num, den)
        x_sym = sp.nsimplify(r * cos_sym, rational=False)
        y_sym = sp.nsimplify(r * sin_sym, rational=False)

        x_latex = sp.latex(sp.simplify(x_sym))
        y_latex = sp.latex(sp.simplify(y_sym))

        theta_latex = _format_pi_fraction(num, den)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (r, num, den)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Convert the polar point $(r,\\ \\theta) = ({r},\\ "
                f"{theta_latex})$ to rectangular coordinates $(x,\\ y)$. "
                "Leave your answer in exact form."
            ),
            answer_latex=f"$(x,\\ y) = \\left({x_latex},\\ {y_latex}\\right)$",
            hints=[
                (
                    r"Use the conversion formulas $x = r\cos\theta$ and "
                    r"$y = r\sin\theta$."
                ),
                (
                    r"Look up $\cos\theta$ and $\sin\theta$ on the unit "
                    r"circle, then multiply each by $r$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Look up $\\cos({theta_latex}) = {sp.latex(cos_sym)}$ and "
                    f"$\\sin({theta_latex}) = {sp.latex(sin_sym)}$."
                ),
                (
                    f"Multiply by $r = {r}$: $x = {r} \\cdot {sp.latex(cos_sym)} "
                    f"= {x_latex}$ and $y = {r} \\cdot {sp.latex(sin_sym)} = "
                    f"{y_latex}$."
                ),
                f"Therefore $(x,\\ y) = \\left({x_latex},\\ {y_latex}\\right)$.",
            ],
            tags=POLAR_TAGS,
        )


@register
class RectToPolarConversion(Generator):
    """Given an integer point $(x, y)$ on a unit-circle-compatible ray,
    compute $(r, \\theta)$ with $\\theta$ an exact-value angle.

    Backward: pick $r$ and a standard angle; require the resulting $(x, y)$
    to be a pair of integers.
    """

    generator_id = "rect_to_polar_conversion"
    topic_slug = "introduction_to_polar_coordinates"
    display_name = "Convert a rectangular point (x, y) to polar (r, theta)"

    # Each entry: (x, y, r, (num, den))
    _CASES = (
        # Axes, r = 1, 2, 3, 4
        (1, 0, 1, (0, 1)),
        (0, 1, 1, (1, 2)),
        (-1, 0, 1, (1, 1)),
        (0, -1, 1, (3, 2)),
        (2, 0, 2, (0, 1)),
        (0, 2, 2, (1, 2)),
        (-2, 0, 2, (1, 1)),
        (0, -2, 2, (3, 2)),
        (3, 0, 3, (0, 1)),
        (0, 3, 3, (1, 2)),
        (-3, 0, 3, (1, 1)),
        (0, -3, 3, (3, 2)),
        (4, 0, 4, (0, 1)),
        (0, 4, 4, (1, 2)),
        (-4, 0, 4, (1, 1)),
        (0, -4, 4, (3, 2)),
        (5, 0, 5, (0, 1)),
        (0, 5, 5, (1, 2)),
        (-5, 0, 5, (1, 1)),
        (0, -5, 5, (3, 2)),
    )

    bank_count_per_difficulty = 20

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x, y, r, (num, den) = rng.choice(self._CASES)
        theta_latex = _format_pi_fraction(num, den)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, y)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Convert the rectangular point $(x,\\ y) = ({x},\\ {y})$ "
                "to polar coordinates $(r,\\ \\theta)$ with $r \\ge 0$ and "
                r"$\theta \in [0,\ 2\pi)$."
            ),
            answer_latex=(
                f"$(r,\\ \\theta) = ({r},\\ {theta_latex})$"
            ),
            hints=[
                (
                    r"Compute $r = \sqrt{x^2 + y^2}$, and find $\theta$ from "
                    r"the point's quadrant (or axis)."
                ),
                (
                    r"For points on the axes, $\theta$ is $0,\ \pi/2,\ \pi,"
                    r"\ 3\pi/2$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute $r = \\sqrt{{({x})^2 + ({y})^2}} = "
                    f"\\sqrt{{{x * x + y * y}}} = {r}$."
                ),
                (
                    f"Identify the angle from the location of $({x},\\ {y})$: "
                    f"$\\theta = {theta_latex}$."
                ),
                (
                    f"Therefore $(r,\\ \\theta) = ({r},\\ {theta_latex})$."
                ),
            ],
            tags=POLAR_TAGS,
        )


@register
class PolarIdentifyQuadrant(Generator):
    """Given a polar point with $r > 0$ and standard $\\theta$, state
    which quadrant (or axis) it sits in.
    """

    generator_id = "polar_identify_quadrant"
    topic_slug = "introduction_to_polar_coordinates"
    display_name = "Identify the quadrant of a polar point"

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.choice([1, 2, 3, 4, 5])
        num, den = rng.choice(_POLAR_ANGLES)

        # Reduce num/den into [0, 2), then decide location.
        n = num
        d = den
        # fraction of 2*pi: value = n/d (in units of pi)
        # quadrant I:  (0,     pi/2)  -> n/d in (0,    0.5)
        # quadrant II: (pi/2,  pi)    -> n/d in (0.5,  1)
        # quadrant III:(pi,    3pi/2) -> n/d in (1,    1.5)
        # quadrant IV: (3pi/2, 2pi)   -> n/d in (1.5,  2)
        # Axes: 0, pi/2, pi, 3pi/2
        ratio = sp.Rational(n, d)
        if ratio == 0:
            location = "on the positive x-axis"
        elif ratio == sp.Rational(1, 2):
            location = "on the positive y-axis"
        elif ratio == sp.Rational(1, 1):
            location = "on the negative x-axis"
        elif ratio == sp.Rational(3, 2):
            location = "on the negative y-axis"
        elif 0 < ratio < sp.Rational(1, 2):
            location = "in quadrant I"
        elif sp.Rational(1, 2) < ratio < sp.Rational(1, 1):
            location = "in quadrant II"
        elif sp.Rational(1, 1) < ratio < sp.Rational(3, 2):
            location = "in quadrant III"
        else:
            location = "in quadrant IV"

        theta_latex = _format_pi_fraction(n, d)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r, n, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"The polar point $(r,\\ \\theta) = ({r},\\ {theta_latex})$ "
                r"is located in which quadrant (or on which axis)?"
            ),
            answer_latex=f"The point lies **{location}**.",
            hints=[
                (
                    r"Since $r > 0$, the quadrant is determined entirely by "
                    r"$\theta$. Angles in $(0,\ \pi/2)$ are Q1, $(\pi/2,\ \pi)$ "
                    r"are Q2, $(\pi,\ 3\pi/2)$ are Q3, and $(3\pi/2,\ 2\pi)$ "
                    r"are Q4."
                ),
                (
                    r"Angles of exactly $0,\ \pi/2,\ \pi,\ 3\pi/2$ land on the "
                    r"axes, not in a quadrant."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compare $\\theta = {theta_latex}$ to the quadrant "
                    r"boundaries $0,\ \pi/2,\ \pi,\ 3\pi/2,\ 2\pi$."
                ),
                f"The point lies **{location}**.",
            ],
            tags=POLAR_TAGS,
        )
