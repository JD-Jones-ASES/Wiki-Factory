"""Circle theorem generators (Cluster 10).

Three topic slugs covered in one module:

- ``inscribed_angles_and_arcs``
- ``chords_secants_and_tangents``
- ``equations_of_circles``

Six generators total.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import shift_expr, format_point


# ---------------------------------------------------------------------------

@register
class InscribedAngleFromArc(Generator):
    """Given an intercepted arc, find the inscribed angle (half of arc)."""
    generator_id = "inscribed_angle_from_arc"
    topic_slug = "inscribed_angles_and_arcs"
    display_name = "Find inscribed angle from intercepted arc"
    bank_count_per_difficulty = 30

    _RANGES = {"easy": (20, 160), "medium": (10, 180), "hard": (10, 220)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Even arc so the inscribed angle is an integer
        arc = 2 * rng.randint(lo // 2, hi // 2)
        inscribed = arc // 2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (arc,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"An inscribed angle in a circle intercepts an arc of measure ${arc}^\\circ$. "
                f"Determine the measure of the inscribed angle."
            ),
            answer_latex=f"${inscribed}^\\circ$",
            hints=[
                r"The **Inscribed Angle Theorem**: an inscribed angle is half the measure of its intercepted arc.",
                r"Use the formula $\theta = \dfrac{1}{2} \cdot (\text{arc})$.",
                f"Compute: $\\dfrac{{{arc}}}{{2}} = {inscribed}^\\circ$.",
            ],
            solution_steps_latex=[
                r"Apply the Inscribed Angle Theorem: inscribed angle $= \dfrac{1}{2} \cdot$ intercepted arc.",
                f"Substitute: $\\theta = \\dfrac{{{arc}}}{{2}}$.",
                f"Simplify: $\\theta = {inscribed}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-formula-substitution"],
        )


# ---------------------------------------------------------------------------

@register
class InscribedAngleSemicircle(Generator):
    """Triangle inscribed in a semicircle: the angle at the circumference is 90°; find the missing acute angle."""
    generator_id = "inscribed_angle_semicircle"
    topic_slug = "inscribed_angles_and_arcs"
    display_name = "Find missing angle in a semicircle triangle"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (20, 70), "medium": (10, 80), "hard": (5, 85)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        given_angle = rng.randint(lo, hi)
        missing = 90 - given_angle

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (given_angle,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A triangle is inscribed in a circle so that one side is a diameter. "
                f"One of the acute angles of the triangle measures ${given_angle}^\\circ$. "
                f"Determine the measure of the other acute angle."
            ),
            answer_latex=f"${missing}^\\circ$",
            hints=[
                r"**Thales' theorem**: a triangle inscribed in a semicircle (with the diameter as a side) has a right angle opposite the diameter.",
                r"The three angles of a triangle sum to $180^\circ$. One of them is $90^\circ$.",
                f"So the other two acute angles sum to $90^\\circ$: ${given_angle} + x = 90$.",
            ],
            solution_steps_latex=[
                r"Thales' theorem: the angle opposite the diameter is a right angle ($90^\circ$).",
                f"The three angles of the triangle sum to $180^\\circ$: $90 + {given_angle} + x = 180$.",
                f"Solve: $x = 180 - 90 - {given_angle} = {missing}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-multi-step"],
        )


# ---------------------------------------------------------------------------

@register
class ChordChordPower(Generator):
    """Two chords intersect inside a circle: $a \\cdot b = c \\cdot d$."""
    generator_id = "chord_chord_power"
    topic_slug = "chords_secants_and_tangents"
    display_name = "Chord-chord power of a point"

    _RANGES = {"easy": (2, 12), "medium": (3, 20), "hard": (4, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Backward: pick a, b, c and compute d so that a*b = c*d
        while True:
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
            c = rng.randint(lo, hi)
            if c == 0:
                continue
            product = a * b
            if product % c == 0:
                d = product // c
                if lo <= d <= hi * 3:
                    break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Two chords of a circle intersect inside the circle at point $P$. "
                f"One chord is divided by $P$ into segments of length ${a}$ and ${b}$. "
                f"The other chord is divided by $P$ into segments of length ${c}$ and $x$. "
                f"Determine the value of $x$."
            ),
            answer_latex=f"$x = {d}$",
            hints=[
                r"The **Chord-Chord Power Theorem**: when two chords intersect inside a circle, the product of the segments of one chord equals the product of the segments of the other.",
                f"Set up: ${a} \\cdot {b} = {c} \\cdot x$.",
                f"Compute: ${a * b} = {c} \\cdot x$.",
            ],
            solution_steps_latex=[
                r"Apply the Chord-Chord Power Theorem: $a \cdot b = c \cdot d$.",
                f"Substitute known lengths: ${a} \\cdot {b} = {c} \\cdot x$.",
                f"Simplify the left side: ${a * b} = {c} x$.",
                f"Solve: $x = \\dfrac{{{a * b}}}{{{c}}} = {d}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class TangentPerpendicularRadius(Generator):
    """Tangent meets a radius at 90°. Given tangent length and radius, find distance from external point to center."""
    generator_id = "tangent_perpendicular_radius"
    topic_slug = "chords_secants_and_tangents"
    display_name = "Distance from external point to center using tangent-radius right angle"
    bank_count_per_difficulty = 20

    # Both (radius, tangent) and (tangent, radius) listed explicitly so the
    # parameter space is deterministic without a random swap.
    _TRIPLES = [
        (3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13),
        (6, 8, 10), (8, 6, 10), (8, 15, 17), (15, 8, 17),
        (7, 24, 25), (24, 7, 25), (9, 12, 15), (12, 9, 15),
        (9, 40, 41), (10, 24, 26), (24, 10, 26),
        (12, 35, 37), (20, 21, 29), (21, 20, 29),
        (15, 20, 25), (20, 15, 25), (12, 16, 20), (16, 12, 20),
        (16, 30, 34), (30, 16, 34), (18, 24, 30), (24, 18, 30),
    ]
    _DIFFS = {
        "easy": [t for t in _TRIPLES if t[2] <= 17],
        "medium": [t for t in _TRIPLES if 10 <= t[2] <= 30],
        "hard": [t for t in _TRIPLES if t[2] >= 20],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        radius, tangent, distance = rng.choice(self._DIFFS[difficulty])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (radius, tangent)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"From an external point $P$, a tangent line touches a circle at point $T$. "
                f"The length $PT$ equals ${tangent}$ and the circle has radius ${radius}$. "
                f"Determine the distance from $P$ to the center of the circle."
            ),
            answer_latex=f"${distance}$",
            hints=[
                r"A tangent line is perpendicular to the radius drawn to the point of tangency.",
                r"So triangle $OPT$ is a right triangle with legs $OT = r$ and $PT$, and hypotenuse $OP$.",
                f"Apply Pythagoras: $OP^2 = {radius}^2 + {tangent}^2 = {radius ** 2 + tangent ** 2}$.",
            ],
            solution_steps_latex=[
                r"Key fact: a tangent is perpendicular to the radius at the point of tangency.",
                f"Triangle $OPT$ has legs $OT = {radius}$ (radius) and $PT = {tangent}$ (tangent).",
                f"Hypotenuse $OP^2 = {radius}^2 + {tangent}^2 = {radius * radius} + {tangent * tangent} = {radius * radius + tangent * tangent}$.",
                f"So $OP = \\sqrt{{{radius ** 2 + tangent ** 2}}} = {distance}$.",
            ],
            tags=["#branch-geometry", "#topic-euclidean-geometry", "#skill-multi-step"],
        )


# ---------------------------------------------------------------------------

@register
class CircleEquationStandardToGeneral(Generator):
    """Expand the standard form of a circle to general form."""
    generator_id = "equation_of_circle_from_center_radius_general_form"
    topic_slug = "equations_of_circles"
    display_name = "Convert standard-form circle to general form"

    _HK_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _R_MAXES = {"easy": 8, "medium": 12, "hard": 18}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._HK_RANGES[difficulty]
        r_max = self._R_MAXES[difficulty]
        h = rng.randint(lo, hi)
        k = rng.randint(lo, hi)
        r = rng.randint(1, r_max)
        # General form: x^2 + y^2 + Dx + Ey + F = 0
        # Expand (x - h)^2 + (y - k)^2 - r^2 = 0
        D = -2 * h
        E = -2 * k
        F = h * h + k * k - r * r

        def sign_term(coef: int, var: str) -> str:
            if coef == 0:
                return ""
            s = "+" if coef > 0 else "-"
            if abs(coef) == 1:
                return f" {s} {var}"
            return f" {s} {abs(coef)}{var}"

        def sign_const(c: int) -> str:
            if c == 0:
                return ""
            s = "+" if c > 0 else "-"
            return f" {s} {abs(c)}"

        general = f"x^2 + y^2{sign_term(D, 'x')}{sign_term(E, 'y')}{sign_const(F)} = 0"
        standard = f"{shift_expr('x', h)}^2 + {shift_expr('y', k)}^2 = {r * r}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, r)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A circle has center ${format_point(h, k)}$ and radius ${r}$. "
                f"Give the equation of the circle in general form "
                f"$x^2 + y^2 + Dx + Ey + F = 0$."
            ),
            answer_latex=f"${general}$",
            hints=[
                r"Start with the standard form: $(x - h)^2 + (y - k)^2 = r^2$.",
                r"Expand each squared binomial: $(x - h)^2 = x^2 - 2hx + h^2$ and similarly for $y$.",
                "Collect the $x^2 + y^2$ terms on the left and move the constant to the left as well.",
            ],
            solution_steps_latex=[
                f"Start: ${standard}$.",
                f"Expand the binomials: $x^2 - {2 * h if h != 0 else 0}x + {h * h} + y^2 - {2 * k if k != 0 else 0}y + {k * k} = {r * r}$.",
                f"Move ${r * r}$ to the left side and combine constants: the constant term becomes ${F}$.",
                f"General form: ${general}$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-algebraic-manipulation"],
        )


# ---------------------------------------------------------------------------

@register
class CircleEquationGeneralToStandard(Generator):
    """Complete the square: general form to standard form; read off center and radius."""
    generator_id = "equation_of_circle_general_to_standard"
    topic_slug = "equations_of_circles"
    display_name = "Convert general-form circle to standard; find center and radius"

    _HK_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _R_MAXES = {"easy": 8, "medium": 12, "hard": 18}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._HK_RANGES[difficulty]
        r_max = self._R_MAXES[difficulty]
        h = rng.randint(lo, hi)
        k = rng.randint(lo, hi)
        r = rng.randint(1, r_max)
        D = -2 * h
        E = -2 * k
        F = h * h + k * k - r * r

        def sign_term(coef: int, var: str) -> str:
            if coef == 0:
                return ""
            s = "+" if coef > 0 else "-"
            if abs(coef) == 1:
                return f" {s} {var}"
            return f" {s} {abs(coef)}{var}"

        def sign_const(c: int) -> str:
            if c == 0:
                return ""
            s = "+" if c > 0 else "-"
            return f" {s} {abs(c)}"

        general = f"x^2 + y^2{sign_term(D, 'x')}{sign_term(E, 'y')}{sign_const(F)} = 0"
        standard = f"{shift_expr('x', h)}^2 + {shift_expr('y', k)}^2 = {r * r}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, r)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A circle has general-form equation ${general}$. "
                f"Complete the square to rewrite it in standard form, and give the center and radius."
            ),
            answer_latex=f"Center $= {format_point(h, k)}$, radius $= {r}$",
            hints=[
                r"Group the $x$ terms and the $y$ terms, then complete the square for each.",
                r"For $x^2 + Dx$, add $(D/2)^2$ to complete the square. Do the same for $y^2 + Ey$.",
                "Remember to balance both sides when you add these completing-the-square constants.",
            ],
            solution_steps_latex=[
                f"Start: ${general}$.",
                f"Group: $(x^2{sign_term(D, 'x')}) + (y^2{sign_term(E, 'y')}) = {-F}$.",
                f"Complete the square: add $({D // 2})^2 = {(D // 2) ** 2}$ and $({E // 2})^2 = {(E // 2) ** 2}$ to both sides.",
                f"Rewrite: ${standard}$.",
                f"Read off the center $(h, k) = {format_point(h, k)}$ and radius $r = {r}$.",
            ],
            tags=["#branch-geometry", "#topic-analytic-geometry", "#skill-multi-step"],
        )
