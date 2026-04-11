"""Advanced trigonometry, geometry, and vector generators.

Ten topic slugs covered across pre-algebra and pre-calculus:

Pre-algebra:
- similar_triangles
- triangle_angle_sum_and_exterior_angles
- applications_of_the_pythagorean_theorem

Pre-calculus:
- identities
- trigonometric_equations
- sinusoid
- law_of_sines
- law_of_cosines
- vectors
- dot_product

Each topic has three generators for a total of 30. Backward construction is
used throughout: parameters are chosen so the answer comes out clean
(integer sides, clean angle values, exact trig values), then the statement
is rendered. SymPy is used for exact trig value lookups.
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


# Pythagorean triples for ladder/diagonal/distance problems.
_PRIMITIVE_TRIPLES: list[tuple[int, int, int]] = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
    (9, 40, 41),
]


def _scaled_triple(rng: random.Random, max_hyp: int = 50) -> tuple[int, int, int]:
    """Pick a primitive triple and scale it by a small integer."""
    a, b, c = rng.choice(_PRIMITIVE_TRIPLES)
    max_k = max(1, max_hyp // c)
    k = rng.randint(1, max(1, max_k))
    return (a * k, b * k, c * k)


def _fmt_pi_fraction(num: int, den: int) -> str:
    """Render num*pi/den as a clean LaTeX string, reducing and handling edge cases."""
    if num == 0:
        return "0"
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den == 1:
        if num == 1:
            return r"\pi"
        if num == -1:
            return r"-\pi"
        return rf"{num}\pi"
    # numerator may be 1 or other
    if num == 1:
        return rf"\dfrac{{\pi}}{{{den}}}"
    if num == -1:
        return rf"-\dfrac{{\pi}}{{{den}}}"
    return rf"\dfrac{{{num}\pi}}{{{den}}}"


def _fmt_sqrt_over(num: int | str, den: int) -> str:
    """Render num/den where num may be 'sqrt(k)' style already (string passthrough)."""
    if den == 1:
        return str(num)
    return rf"\dfrac{{{num}}}{{{den}}}"


def _sympy_to_latex(expr) -> str:
    """Render a sympy expression to LaTeX without surrounding $."""
    return sp.latex(sp.nsimplify(expr, rational=True))


# Map a rational sine/cosine exact-value to an angle in [0, 2*pi).
# Used for trigonometric_equations and identity problems.
# Entries: (sympy_expr_value, list_of_angles_as_pi_fractions)
def _angles_for_sin(value) -> list[tuple[int, int]]:
    """Return list of (num, den) such that sin(num*pi/den) == value, in [0, 2pi)."""
    v = sp.nsimplify(value, rational=False)
    hits: list[tuple[int, int]] = []
    # Sweep candidate angles over a fine grid of pi-fractions.
    candidates = [
        (0, 1), (1, 6), (1, 4), (1, 3), (1, 2),
        (2, 3), (3, 4), (5, 6), (1, 1),
        (7, 6), (5, 4), (4, 3), (3, 2),
        (5, 3), (7, 4), (11, 6),
    ]
    for num, den in candidates:
        theta = sp.Rational(num, den) * sp.pi
        if sp.simplify(sp.sin(theta) - v) == 0:
            hits.append((num, den))
    return hits


def _angles_for_cos(value) -> list[tuple[int, int]]:
    """Return list of (num, den) such that cos(num*pi/den) == value, in [0, 2pi)."""
    v = sp.nsimplify(value, rational=False)
    hits: list[tuple[int, int]] = []
    candidates = [
        (0, 1), (1, 6), (1, 4), (1, 3), (1, 2),
        (2, 3), (3, 4), (5, 6), (1, 1),
        (7, 6), (5, 4), (4, 3), (3, 2),
        (5, 3), (7, 4), (11, 6),
    ]
    for num, den in candidates:
        theta = sp.Rational(num, den) * sp.pi
        if sp.simplify(sp.cos(theta) - v) == 0:
            hits.append((num, den))
    return hits


# ===========================================================================
# Topic 1: similar_triangles  (pre-algebra)
# ===========================================================================


@register
class SimilarTrianglesFindMissingSide(Generator):
    """Given two similar triangles with some sides labeled, find the missing side.

    Backward: pick a scale factor k (simple ratio) and three small integer
    sides for the first triangle; the second triangle's sides are k times
    the first. One side is hidden and the student solves a proportion.
    """
    generator_id = "similar_triangles_find_missing_side"
    topic_slug = "similar_triangles"
    display_name = "Find a missing side using similar triangles"

    _K_CHOICES = {
        "easy": [(2, 1), (3, 1), (1, 2)],
        "medium": [(2, 1), (3, 1), (4, 1), (1, 2), (3, 2), (2, 3)],
        "hard": [(3, 2), (5, 2), (4, 3), (5, 3), (2, 3), (3, 4)],
    }
    _BASE_SIDE_RANGES = {"easy": (2, 8), "medium": (3, 12), "hard": (4, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        kn, kd = rng.choice(self._K_CHOICES[difficulty])
        lo, hi = self._BASE_SIDE_RANGES[difficulty]
        # Choose small triangle side a; we need ka/kd to be integer.
        # Pick a as a multiple of kd.
        a = rng.randint(lo, hi) * kd
        if a > 3 * hi * kd:
            a = kd
        # Corresponding side in second triangle
        a_prime = a * kn // kd
        # A third side so we present a meaningful proportion.
        b = rng.randint(lo, hi) * kd
        if b == a:
            b += kd
        b_prime = b * kn // kd

        # Student sees: a, b, a', and finds b'.
        # Proportion: a / a' = b / b', so b' = b * a' / a.
        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (kn, kd, a, b, a_prime)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Triangles $ABC$ and $DEF$ are similar. Corresponding sides "
                rf"$AB$ and $DE$ have lengths ${a}$ and ${a_prime}$. "
                rf"If side $BC$ has length ${b}$, find the length of the "
                rf"corresponding side $EF$."
            ),
            answer_latex=rf"$EF = {b_prime}$",
            hints=[
                (
                    "In similar triangles, corresponding sides are in the same "
                    "ratio. Set up a proportion."
                ),
                rf"Write: $\dfrac{{AB}}{{DE}} = \dfrac{{BC}}{{EF}}$.",
                rf"Substitute the known values and solve for $EF$.",
            ],
            solution_steps_latex=[
                rf"Set up a proportion from corresponding sides: "
                rf"$\dfrac{{{a}}}{{{a_prime}}} = \dfrac{{{b}}}{{EF}}$.",
                rf"Cross-multiply: ${a} \cdot EF = {a_prime} \cdot {b}$.",
                rf"Divide: $EF = \dfrac{{{a_prime} \cdot {b}}}{{{a}}} = {b_prime}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#topic-similarity-and-congruence",
            ],
        )


@register
class SimilarTrianglesCheckAA(Generator):
    """Given two triangles with angle information, decide if they are similar by AA.

    Mixes cases where two angles match (similar) with cases where only one
    angle matches (not enough info) or where angles do not match at all.
    """
    generator_id = "similar_triangles_check_aa"
    topic_slug = "similar_triangles"
    display_name = "Decide if two triangles are similar (AA criterion)"
    bank_count_per_difficulty = 30

    _ANGLE_POOL = (30, 40, 45, 50, 55, 60, 65, 70, 80, 85, 90, 100)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(["yes", "yes", "not_enough", "no"])
        # Build triangle 1
        while True:
            a1 = rng.choice(self._ANGLE_POOL)
            b1 = rng.choice(self._ANGLE_POOL)
            if a1 + b1 < 180 and a1 != b1:
                break
        c1 = 180 - a1 - b1

        if case == "yes":
            # Two angles of triangle 2 match two angles of triangle 1.
            a2 = a1
            b2 = b1
            c2 = 180 - a2 - b2
            statement_angles_2 = (a2, b2)
            answer = "Yes, the triangles are similar by AA."
            reason = (
                f"Two angles of the second triangle (${a2}^\\circ$ and "
                f"${b2}^\\circ$) match two angles of the first. "
                "By the AA (Angle-Angle) criterion, the triangles are similar."
            )
        elif case == "not_enough":
            # Only one shared angle
            a2 = a1
            while True:
                b2 = rng.choice(self._ANGLE_POOL)
                if b2 != b1 and b2 != c1 and a2 + b2 < 180:
                    break
            statement_angles_2 = (a2, b2)
            answer = "Not enough information to conclude similarity."
            reason = (
                f"Only one angle of the second triangle matches the first "
                f"(${a2}^\\circ$). A single shared angle is not enough --- "
                "AA requires two pairs of equal angles."
            )
        else:  # no
            while True:
                a2 = rng.choice(self._ANGLE_POOL)
                b2 = rng.choice(self._ANGLE_POOL)
                if (
                    a2 + b2 < 180
                    and a2 not in (a1, b1, c1)
                    and b2 not in (a1, b1, c1)
                    and a2 != b2
                ):
                    break
            statement_angles_2 = (a2, b2)
            answer = "No, the triangles are not similar (angles do not match)."
            reason = (
                f"Neither ${a2}^\\circ$ nor ${b2}^\\circ$ matches any angle of "
                "the first triangle, so the triangles cannot be similar by AA."
            )

        a2_s, b2_s = statement_angles_2

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a1, b1, a2_s, b2_s, case),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Triangle $P$ has angles of ${a1}^\circ$ and ${b1}^\circ$. "
                rf"Triangle $Q$ has angles of ${a2_s}^\circ$ and ${b2_s}^\circ$. "
                rf"Are the two triangles similar by the AA criterion?"
            ),
            answer_latex=answer,
            hints=[
                (
                    "The AA (Angle-Angle) criterion: if two angles of one "
                    "triangle equal two angles of another, the triangles are similar."
                ),
                (
                    "Compare the given angles pair by pair. Count the matches."
                ),
            ],
            solution_steps_latex=[
                rf"Triangle $P$ has angles ${a1}^\circ$, ${b1}^\circ$, and "
                rf"${c1}^\circ$ (since angles sum to $180^\circ$).",
                rf"Triangle $Q$ has angles ${a2_s}^\circ$, ${b2_s}^\circ$, and "
                rf"${180 - a2_s - b2_s}^\circ$.",
                reason,
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#topic-similarity-and-congruence",
            ],
        )


@register
class SimilarTrianglesScaleFactor(Generator):
    """Given corresponding sides of two similar triangles, find the scale factor.

    Backward: pick a scale factor (as a rational), choose integer sides
    for the smaller triangle, derive the larger triangle, ask for the ratio.
    """
    generator_id = "similar_triangles_scale_factor"
    topic_slug = "similar_triangles"
    display_name = "Find the scale factor between two similar triangles"

    _K_CHOICES = {
        "easy": [(2, 1), (3, 1), (4, 1), (5, 1)],
        "medium": [(2, 1), (3, 1), (5, 2), (3, 2), (4, 3)],
        "hard": [(5, 2), (7, 2), (3, 2), (4, 3), (5, 3), (7, 4)],
    }
    _BASE_RANGES = {"easy": (2, 9), "medium": (3, 12), "hard": (4, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        kn, kd = rng.choice(self._K_CHOICES[difficulty])
        lo, hi = self._BASE_RANGES[difficulty]
        # Ensure a * kn / kd is integer
        a_small = rng.randint(lo, hi) * kd
        a_large = a_small * kn // kd

        if kd == 1:
            k_latex = f"{kn}"
        else:
            k_latex = rf"\dfrac{{{kn}}}{{{kd}}}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (kn, kd, a_small)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Two similar triangles have corresponding sides of lengths "
                rf"${a_small}$ and ${a_large}$. Find the scale factor "
                rf"from the smaller triangle to the larger triangle."
            ),
            answer_latex=rf"${k_latex}$",
            hints=[
                (
                    "The scale factor is the ratio of a pair of corresponding "
                    "sides (larger side over smaller side)."
                ),
                rf"Simplify $\dfrac{{{a_large}}}{{{a_small}}}$ to lowest terms.",
            ],
            solution_steps_latex=[
                rf"The scale factor is "
                rf"$k = \dfrac{{\text{{larger side}}}}{{\text{{smaller side}}}}"
                rf" = \dfrac{{{a_large}}}{{{a_small}}}$.",
                rf"Simplify: $k = {k_latex}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
                "#topic-similarity-and-congruence",
            ],
        )


# ===========================================================================
# Topic 2: triangle_angle_sum_and_exterior_angles  (pre-algebra)
# ===========================================================================


@register
class TriangleFindMissingAngle(Generator):
    """Given two angles of a triangle, find the third (180 - a - b)."""
    generator_id = "triangle_find_missing_angle"
    topic_slug = "triangle_angle_sum_and_exterior_angles"
    display_name = "Find the missing angle of a triangle"

    _RANGES = {
        "easy": (20, 80),
        "medium": (15, 110),
        "hard": (10, 130),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        while True:
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
            if a + b < 175 and a + b > 15 and a != b:
                break
        c = 180 - a - b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Two angles of a triangle measure ${a}^\circ$ and ${b}^\circ$. "
                rf"Find the measure of the third angle."
            ),
            answer_latex=rf"${c}^\circ$",
            hints=[
                r"The three angles of any triangle sum to $180^\circ$.",
                rf"Set up: $a + b + c = 180$ and solve for $c$.",
            ],
            solution_steps_latex=[
                r"Use the Triangle Angle Sum Theorem: $a + b + c = 180^\circ$.",
                rf"Substitute: ${a} + {b} + c = 180$.",
                rf"Simplify: ${a + b} + c = 180$.",
                rf"Solve: $c = 180 - {a + b} = {c}^\circ$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
            ],
        )


@register
class ExteriorAngleTheorem(Generator):
    """Given two interior angles, find the exterior angle at the third vertex.

    Exterior Angle Theorem: the exterior angle equals the sum of the two
    non-adjacent interior angles.
    """
    generator_id = "exterior_angle_theorem"
    topic_slug = "triangle_angle_sum_and_exterior_angles"
    display_name = "Apply the Exterior Angle Theorem"

    _RANGES = {
        "easy": (20, 70),
        "medium": (15, 90),
        "hard": (10, 120),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        while True:
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
            if a + b < 170 and a + b > 20:
                break
        exterior = a + b
        third_interior = 180 - a - b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"In triangle $ABC$, the interior angles at vertices $A$ and $B$ "
                rf"measure ${a}^\circ$ and ${b}^\circ$. Find the exterior angle at "
                rf"vertex $C$."
            ),
            answer_latex=rf"${exterior}^\circ$",
            hints=[
                (
                    "The Exterior Angle Theorem: an exterior angle of a triangle "
                    "equals the sum of the two non-adjacent interior angles."
                ),
                rf"The two non-adjacent angles are ${a}^\circ$ and ${b}^\circ$.",
            ],
            solution_steps_latex=[
                (
                    "By the Exterior Angle Theorem, the exterior angle at $C$ "
                    "equals the sum of the two non-adjacent interior angles."
                ),
                rf"The non-adjacent angles are $A = {a}^\circ$ and $B = {b}^\circ$.",
                rf"Exterior angle at $C = {a} + {b} = {exterior}^\circ$.",
                (
                    rf"Check: interior angle at $C$ is $180 - {a} - {b} = "
                    rf"{third_interior}^\circ$; exterior + interior $= "
                    rf"{exterior} + {third_interior} = 180^\circ$. Consistent."
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
            ],
        )


@register
class TriangleAngleFromEquation(Generator):
    """Given an expression for a triangle's angles, solve for x.

    Example: "Angles are x, 2x, and 3x" => x = 30.
    """
    generator_id = "triangle_angle_from_equation"
    topic_slug = "triangle_angle_sum_and_exterior_angles"
    display_name = "Solve for $x$ given algebraic angle expressions"
    bank_count_per_difficulty = 10

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Pick template: coefficients (c1, c2, c3) with constants (k1, k2, k3).
        # Sum: (c1+c2+c3)*x + (k1+k2+k3) = 180, so x = (180 - ksum)/csum.
        if difficulty == "easy":
            templates = [
                ((1, 2, 3), (0, 0, 0)),      # x + 2x + 3x = 180, x=30
                ((1, 1, 2), (0, 0, 0)),      # x + x + 2x = 180, x=45
                ((1, 2, 6), (0, 0, 0)),      # x + 2x + 6x = 180, x=20
                ((2, 3, 4), (0, 0, 0)),      # 2x+3x+4x=180, x=20
                ((1, 3, 5), (0, 0, 0)),      # 9x=180, x=20
                ((1, 4, 5), (0, 0, 0)),      # 10x=180, x=18
                ((1, 2, 9), (0, 0, 0)),      # 12x=180, x=15
                ((2, 3, 7), (0, 0, 0)),      # 12x=180, x=15
                ((1, 5, 6), (0, 0, 0)),      # 12x=180, x=15
                ((1, 2, 3), (30, 0, 0)),     # 6x+30=180, x=25
                ((1, 1, 1), (30, 60, 0)),    # 3x+90=180, x=30
                ((1, 2, 1), (20, 0, 40)),    # 4x+60=180, x=30
            ]
        elif difficulty == "medium":
            templates = [
                ((1, 1, 1), (20, 30, 10)),
                ((1, 2, 3), (10, 10, 10)),
                ((2, 3, 1), (20, 10, 30)),
                ((1, 2, 2), (10, 20, 30)),
                ((3, 4, 5), (0, 0, 0)),
                ((1, 2, 3), (5, 10, 15)),
                ((1, 1, 4), (15, 45, 0)),
                ((1, 2, 3), (25, 30, 5)),
                ((2, 2, 5), (10, 20, 15)),
                ((1, 1, 1), (10, 20, 30)),
                ((1, 1, 2), (0, 30, 30)),
                ((1, 1, 2), (10, 20, 30)),
                ((1, 3, 2), (10, 20, 30)),
                ((2, 3, 1), (0, 0, 0)),
                ((1, 2, 3), (0, 0, 60)),
                ((1, 2, 3), (60, 0, 0)),
                ((1, 3, 2), (5, 10, 45)),
                ((1, 1, 2), (30, 30, 0)),
                ((2, 2, 2), (10, 20, 30)),
                ((1, 1, 1), (30, 30, 30)),
                ((1, 1, 1), (15, 45, 30)),
                ((1, 3, 1), (0, 0, 0)),
                ((1, 2, 1), (0, 0, 0)),
            ]
        else:  # hard
            templates = [
                ((2, 3, 5), (10, 20, 30)),   # 10x+60=180, x=12
                ((2, 2, 2), (15, 20, 25)),   # 6x+60=180, x=20
                ((3, 5, 7), (0, 0, 0)),      # 15x=180, x=12
                ((1, 4, 7), (0, 0, 0)),      # 12x=180, x=15
                ((2, 4, 6), (12, 8, 4)),     # 12x+24=180, x=13
                ((3, 4, 5), (5, 10, 15)),    # 12x+30=180, x=12.5 skip if not integer
                ((2, 3, 7), (10, 10, 40)),   # 12x+60=180, x=10
                ((3, 5, 4), (5, 10, 15)),    # 12x+30=180
                ((1, 5, 6), (10, 20, 30)),   # 12x+60=180, x=10
                ((2, 7, 3), (0, 0, 0)),      # 12x=180, x=15
                ((1, 3, 8), (0, 0, 0)),      # 12x=180, x=15
                ((3, 6, 9), (0, 0, 0)),      # 18x=180, x=10
                ((1, 2, 7), (0, 0, 0)),      # 10x=180, x=18
                ((1, 4, 5), (5, 10, 15)),    # 10x+30=180, x=15
                ((2, 3, 5), (5, 10, 15)),    # 10x+30=180, x=15
                ((1, 1, 2), (10, 20, 30)),   # 4x+60=180, x=30
                ((2, 4, 6), (5, 10, 15)),    # 12x+30=180, x=12.5 skip
                ((3, 5, 7), (5, 10, 15)),    # 15x+30=180, x=10
            ]

        # Filter only templates that yield integer x.
        valid = []
        for (c1, c2, c3), (k1, k2, k3) in templates:
            csum = c1 + c2 + c3
            ksum = k1 + k2 + k3
            rhs = 180 - ksum
            if csum > 0 and rhs > 0 and rhs % csum == 0 and rhs // csum > 0:
                x_val = rhs // csum
                a1 = c1 * x_val + k1
                a2 = c2 * x_val + k2
                a3 = c3 * x_val + k3
                if min(a1, a2, a3) > 0 and max(a1, a2, a3) < 180:
                    valid.append(((c1, c2, c3), (k1, k2, k3), x_val))

        if not valid:
            # Fallback: safe template
            c1, c2, c3, k1, k2, k3, x_val = 1, 2, 3, 0, 0, 0, 30
        else:
            (c1, c2, c3), (k1, k2, k3), x_val = rng.choice(valid)

        def fmt_term(c: int, k: int) -> str:
            if c == 0:
                return str(k)
            if c == 1:
                body = "x"
            else:
                body = f"{c}x"
            if k == 0:
                return body
            if k > 0:
                return f"{body} + {k}"
            return f"{body} - {-k}"

        csum = c1 + c2 + c3
        ksum = k1 + k2 + k3
        rhs = 180 - ksum

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (c1, c2, c3, k1, k2, k3),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"The three interior angles of a triangle measure "
                rf"${fmt_term(c1, k1)}^\circ$, ${fmt_term(c2, k2)}^\circ$, and "
                rf"${fmt_term(c3, k3)}^\circ$. Find $x$."
            ),
            answer_latex=rf"$x = {x_val}$",
            hints=[
                r"The angles of a triangle sum to $180^\circ$.",
                (
                    "Add the three expressions, set the sum equal to 180, and "
                    "solve for $x$."
                ),
            ],
            solution_steps_latex=[
                rf"Set the sum of the angle measures equal to $180^\circ$: "
                rf"$({fmt_term(c1, k1)}) + ({fmt_term(c2, k2)}) + "
                rf"({fmt_term(c3, k3)}) = 180$.",
                rf"Combine like terms: ${csum}x + {ksum} = 180$."
                if ksum != 0 else rf"Combine like terms: ${csum}x = 180$.",
                rf"Solve: $x = \dfrac{{{rhs}}}{{{csum}}} = {x_val}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-euclidean-geometry",
            ],
        )


# ===========================================================================
# Topic 3: applications_of_the_pythagorean_theorem  (pre-algebra)
# ===========================================================================


@register
class LadderProblem(Generator):
    """Ladder leaning against a wall word problem using Pythagorean triples."""
    generator_id = "ladder_problem"
    topic_slug = "applications_of_the_pythagorean_theorem"
    display_name = "Ladder against a wall (Pythagorean triple)"
    supports_word_problems = True
    bank_count_per_difficulty = 24

    # For each triple (a,b,c), both legs can play the "base" role with the other as "height",
    # so there are effectively 2*len(triples) configurations.
    _TRIPLES_EASY = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]
    _TRIPLES_MEDIUM = [
        (5, 12, 13), (8, 15, 17), (9, 12, 15), (10, 24, 26),
        (12, 16, 20), (7, 24, 25), (6, 8, 10), (15, 20, 25),
    ]
    _TRIPLES_HARD = [
        (7, 24, 25), (8, 15, 17), (9, 40, 41), (20, 21, 29),
        (12, 35, 37), (11, 60, 61), (13, 84, 85), (10, 24, 26),
        (16, 30, 34), (18, 24, 30),
    ]

    _TEMPLATES = [
        (
            "A {L}-foot ladder leans against a vertical wall with the base of "
            "the ladder {b} feet away from the wall. How far up the wall does "
            "the ladder reach?"
        ),
        (
            "A painter's {L}-foot ladder is placed against a wall so that its "
            "foot is {b} feet from the base of the wall. Find the height at "
            "which the top of the ladder meets the wall."
        ),
        (
            "A ladder of length {L} feet rests on level ground and leans "
            "against a wall. If the distance from the wall to the ladder's "
            "base is {b} feet, how high up the wall does the top reach?"
        ),
        (
            "A firefighter props a {L}-foot ladder against a building. The "
            "bottom of the ladder is {b} feet from the base of the building. "
            "How high on the building does the top of the ladder touch?"
        ),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = {
            "easy": self._TRIPLES_EASY,
            "medium": self._TRIPLES_MEDIUM,
            "hard": self._TRIPLES_HARD,
        }[difficulty]
        a, b, c = rng.choice(triples)
        # Randomly swap which leg plays the base role to double the variety.
        if rng.random() < 0.5:
            a, b = b, a
        # In the problem: ladder = hypotenuse = L, base distance = b (first leg),
        # height reached = a (the other leg).
        L = c
        base = b
        height = a

        template_idx = rng.randrange(len(self._TEMPLATES))
        template = self._TEMPLATES[template_idx]
        statement = template.format(L=L, b=base)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (L, base, height, template_idx)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=rf"${height}$ feet",
            hints=[
                (
                    "The ladder, the wall, and the ground form a right triangle. "
                    "The ladder is the hypotenuse."
                ),
                rf"Apply the Pythagorean theorem: $a^2 + b^2 = c^2$ where "
                rf"$c$ is the ladder length.",
                rf"Solve for the missing leg: $a^2 = {L}^2 - {base}^2$.",
            ],
            solution_steps_latex=[
                rf"Model the situation as a right triangle with hypotenuse "
                rf"$c = {L}$ (the ladder), one leg $b = {base}$ (distance from "
                rf"wall), and unknown leg $a$ (height on wall).",
                rf"Pythagorean theorem: $a^2 + {base}^2 = {L}^2$.",
                rf"Compute: $a^2 = {L * L} - {base * base} = {L * L - base * base}$.",
                rf"Take the positive square root: $a = "
                rf"\sqrt{{{L * L - base * base}}} = {height}$ feet.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-right-triangles",
                "#representation-verbal",
            ],
        )


@register
class DiagonalOfRectangle(Generator):
    """Find the diagonal of a rectangle given length and width (Pythagorean triple)."""
    generator_id = "diagonal_of_rectangle"
    topic_slug = "applications_of_the_pythagorean_theorem"
    display_name = "Find the diagonal of a rectangle"
    supports_word_problems = True
    bank_count_per_difficulty = 24

    _TRIPLES_EASY = [
        (3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17),
    ]
    _TRIPLES_MEDIUM = [
        (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20),
        (7, 24, 25), (10, 24, 26), (15, 20, 25), (6, 8, 10),
    ]
    _TRIPLES_HARD = [
        (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37),
        (11, 60, 61), (13, 84, 85), (8, 15, 17), (16, 30, 34),
        (18, 24, 30), (27, 36, 45),
    ]

    _TEMPLATES = [
        (
            "A rectangular garden measures {a} meters by {b} meters. Find the "
            "length of its diagonal."
        ),
        (
            "A rectangular courtyard is {a} feet wide and {b} feet long. "
            "How long is the diagonal that runs from one corner to the "
            "opposite corner?"
        ),
        (
            "A rectangle has a length of {b} units and a width of {a} units. "
            "Determine the length of its diagonal."
        ),
        (
            "A soccer field is a rectangle ${a}$ meters wide and ${b}$ meters "
            "long. How far is it in a straight line from one corner to the "
            "opposite corner?"
        ),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = {
            "easy": self._TRIPLES_EASY,
            "medium": self._TRIPLES_MEDIUM,
            "hard": self._TRIPLES_HARD,
        }[difficulty]
        a, b, c = rng.choice(triples)
        template_idx = rng.randrange(len(self._TEMPLATES))
        template = self._TEMPLATES[template_idx]
        statement = template.format(a=a, b=b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, template_idx)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=rf"${c}$ units",
            hints=[
                (
                    "A rectangle's diagonal splits it into two right triangles "
                    "whose legs are the length and the width."
                ),
                rf"Apply the Pythagorean theorem with legs ${a}$ and ${b}$.",
            ],
            solution_steps_latex=[
                rf"The diagonal $d$ is the hypotenuse of a right triangle with "
                rf"legs ${a}$ and ${b}$.",
                rf"$d^2 = {a}^2 + {b}^2 = {a * a} + {b * b} = {a * a + b * b}$.",
                rf"$d = \sqrt{{{a * a + b * b}}} = {c}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-right-triangles",
                "#topic-analytic-geometry",
            ],
        )


@register
class DistanceBetweenPoints2D(Generator):
    """Distance between two points on a grid using a Pythagorean triple."""
    generator_id = "distance_between_points_2d"
    topic_slug = "applications_of_the_pythagorean_theorem"
    display_name = "Distance between two points on a grid"
    bank_count_per_difficulty = 30

    _TRIPLES_EASY = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    _TRIPLES_MEDIUM = [(5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    _TRIPLES_HARD = [(8, 15, 17), (20, 21, 29), (9, 40, 41), (12, 35, 37)]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = {
            "easy": self._TRIPLES_EASY,
            "medium": self._TRIPLES_MEDIUM,
            "hard": self._TRIPLES_HARD,
        }[difficulty]
        dx, dy, d = rng.choice(triples)
        # Pick starting point, swap sign patterns
        x1 = rng.randint(-5, 5)
        y1 = rng.randint(-5, 5)
        sx = rng.choice([1, -1])
        sy = rng.choice([1, -1])
        x2 = x1 + sx * dx
        y2 = y1 + sy * dy

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x1, y1, x2, y2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Find the straight-line distance between the points "
                rf"$({x1}, {y1})$ and $({x2}, {y2})$ using the Pythagorean theorem."
            ),
            answer_latex=rf"${d}$",
            hints=[
                (
                    "Compute the horizontal change $\\Delta x$ and the vertical "
                    "change $\\Delta y$ between the two points."
                ),
                (
                    "The distance is the hypotenuse of a right triangle with "
                    "those changes as legs: "
                    r"$d = \sqrt{(\Delta x)^2 + (\Delta y)^2}$."
                ),
            ],
            solution_steps_latex=[
                rf"Horizontal change: $\Delta x = {x2} - {x1} = {x2 - x1}$.",
                rf"Vertical change: $\Delta y = {y2} - {y1} = {y2 - y1}$.",
                rf"Distance: "
                rf"$d = \sqrt{{({x2 - x1})^2 + ({y2 - y1})^2}} = "
                rf"\sqrt{{{(x2 - x1) ** 2} + {(y2 - y1) ** 2}}} = "
                rf"\sqrt{{{(x2 - x1) ** 2 + (y2 - y1) ** 2}}} = {d}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-right-triangles",
                "#topic-analytic-geometry",
            ],
        )


# ===========================================================================
# Topic 4: identities  (pre-calc)
# ===========================================================================


@register
class PythagoreanIdentityApply(Generator):
    """Given sin or cos in a quadrant, find the other using sin^2 + cos^2 = 1.

    Backward: pick a clean rational for sin or cos (e.g. 3/5, 5/13) and a
    quadrant; derive the other one with proper sign.
    """
    generator_id = "pythagorean_identity_apply"
    topic_slug = "identities"
    display_name = "Apply the Pythagorean identity to find sin or cos"
    bank_count_per_difficulty = 24

    # Values from Pythagorean triples, as (known_numerator, denominator, other_numerator).
    # (3/5, 4/5), (5/13, 12/13), (8/17, 15/17), (7/25, 24/25)
    _TRIPLES = [
        (3, 5, 4),
        (4, 5, 3),
        (5, 13, 12),
        (12, 13, 5),
        (8, 17, 15),
        (15, 17, 8),
        (7, 25, 24),
        (24, 25, 7),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        known, den, other = rng.choice(self._TRIPLES)
        given_fn = rng.choice(["sin", "cos"])
        quadrant = rng.choice([1, 2, 3, 4])

        # Sign rules for quadrants:
        # Q1: sin +, cos + ; Q2: sin +, cos - ; Q3: sin -, cos - ; Q4: sin -, cos +
        sin_sign = 1 if quadrant in (1, 2) else -1
        cos_sign = 1 if quadrant in (1, 4) else -1

        if given_fn == "sin":
            # sin given, find cos
            given_value_sign = sin_sign
            other_value_sign = cos_sign
            given_latex = rf"\sin\theta = \dfrac{{{given_value_sign * known}}}{{{den}}}" \
                if given_value_sign > 0 \
                else rf"\sin\theta = -\dfrac{{{known}}}{{{den}}}"
            other_fn = r"\cos\theta"
        else:
            # cos given, find sin
            given_value_sign = cos_sign
            other_value_sign = sin_sign
            given_latex = rf"\cos\theta = \dfrac{{{given_value_sign * known}}}{{{den}}}" \
                if given_value_sign > 0 \
                else rf"\cos\theta = -\dfrac{{{known}}}{{{den}}}"
            other_fn = r"\sin\theta"

        if other_value_sign > 0:
            answer_latex = rf"${other_fn} = \dfrac{{{other}}}{{{den}}}$"
            answer_num = other
        else:
            answer_latex = rf"${other_fn} = -\dfrac{{{other}}}{{{den}}}$"
            answer_num = -other

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (known, den, given_fn, quadrant),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Given that ${given_latex}$ and $\theta$ is in Quadrant "
                rf"${{\rm {['I','II','III','IV'][quadrant-1]}}}$, find ${other_fn}$."
            ),
            answer_latex=answer_latex,
            hints=[
                r"Use the Pythagorean identity $\sin^2\theta + \cos^2\theta = 1$.",
                (
                    "After solving for the squared value, take the square root. "
                    "The sign depends on the quadrant."
                ),
            ],
            solution_steps_latex=[
                rf"Start from $\sin^2\theta + \cos^2\theta = 1$.",
                rf"Substitute ${given_latex}$ and square: "
                rf"$\left(\dfrac{{{known}}}{{{den}}}\right)^2 = "
                rf"\dfrac{{{known * known}}}{{{den * den}}}$.",
                rf"Isolate the other squared value: it equals "
                rf"$1 - \dfrac{{{known * known}}}{{{den * den}}} = "
                rf"\dfrac{{{den * den - known * known}}}{{{den * den}}} = "
                rf"\dfrac{{{other * other}}}{{{den * den}}}$.",
                rf"Take the square root: $\pm\dfrac{{{other}}}{{{den}}}$. "
                rf"In Quadrant "
                rf"${['I', 'II', 'III', 'IV'][quadrant-1]}$, "
                rf"${other_fn}$ is "
                rf"{'positive' if other_value_sign > 0 else 'negative'}.",
                rf"Therefore ${other_fn} = "
                rf"{'' if other_value_sign > 0 else '-'}"
                rf"\dfrac{{{other}}}{{{den}}}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-trig-identities",
            ],
        )


@register
class DoubleAngleApply(Generator):
    """Apply double-angle formulas given sin or cos of theta.

    sin(2t) = 2 sin t cos t
    cos(2t) = 1 - 2 sin^2 t = 2 cos^2 t - 1

    Backward: pick a Pythagorean triple so both sin and cos are clean.
    """
    generator_id = "double_angle_apply"
    topic_slug = "identities"
    display_name = "Apply a double-angle formula to find sin(2t) or cos(2t)"
    bank_count_per_difficulty = 20

    _TRIPLES = [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c = rng.choice(self._TRIPLES)
        # Randomly assign which leg is opposite (sin) vs adjacent (cos).
        if rng.random() < 0.5:
            sin_num, cos_num = a, b
        else:
            sin_num, cos_num = b, a
        den = c

        # Restrict to Quadrant I for cleanness (both positive).
        target = rng.choice(["sin2t", "cos2t"])
        sin_val = Fraction(sin_num, den)
        cos_val = Fraction(cos_num, den)

        if target == "sin2t":
            # sin(2t) = 2 sin t cos t
            result = 2 * sin_val * cos_val
            formula = r"\sin(2\theta) = 2\sin\theta\cos\theta"
            target_latex = r"\sin(2\theta)"
            # Compute expression "2 * (sin) * (cos)"
            numerator_step = 2 * sin_num * cos_num
            denominator_step = den * den
            substitution = (
                rf"{target_latex} = 2 \cdot \dfrac{{{sin_num}}}{{{den}}} "
                rf"\cdot \dfrac{{{cos_num}}}{{{den}}} = "
                rf"\dfrac{{{numerator_step}}}{{{denominator_step}}}"
            )
        else:
            # cos(2t) = cos^2 t - sin^2 t = (cos_num^2 - sin_num^2)/den^2
            result = cos_val * cos_val - sin_val * sin_val
            formula = r"\cos(2\theta) = \cos^2\theta - \sin^2\theta"
            target_latex = r"\cos(2\theta)"
            numerator_step = cos_num * cos_num - sin_num * sin_num
            denominator_step = den * den
            substitution = (
                rf"{target_latex} = \left(\dfrac{{{cos_num}}}{{{den}}}\right)^2 "
                rf"- \left(\dfrac{{{sin_num}}}{{{den}}}\right)^2 = "
                rf"\dfrac{{{cos_num * cos_num} - {sin_num * sin_num}}}{{{den * den}}} = "
                rf"\dfrac{{{numerator_step}}}{{{denominator_step}}}"
            )

        # Simplify result for answer.
        result_num = result.numerator
        result_den = result.denominator
        if result_den == 1:
            answer_latex = rf"${target_latex} = {result_num}$"
        else:
            if result_num < 0:
                answer_latex = rf"${target_latex} = -\dfrac{{{-result_num}}}{{{result_den}}}$"
            else:
                answer_latex = rf"${target_latex} = \dfrac{{{result_num}}}{{{result_den}}}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (sin_num, cos_num, den, target)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Given $\sin\theta = \dfrac{{{sin_num}}}{{{den}}}$ and "
                rf"$\cos\theta = \dfrac{{{cos_num}}}{{{den}}}$ (with $\theta$ "
                rf"in Quadrant I), find ${target_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                rf"Use the double-angle formula: ${formula}$.",
                rf"Substitute the given values of $\sin\theta$ and $\cos\theta$ "
                rf"into the formula.",
            ],
            solution_steps_latex=[
                rf"State the formula: ${formula}$.",
                rf"Substitute: ${substitution}$.",
                rf"Simplify: {answer_latex}.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-trig-identities",
            ],
        )


@register
class SumDifferenceApply(Generator):
    """Apply sum/difference formulas to find sin(75), cos(15), etc. exactly.

    Uses angles expressible as 30+45, 60-45, 45-30, 60+45 etc.
    """
    generator_id = "sum_difference_apply"
    topic_slug = "identities"
    display_name = "Apply a sum/difference formula to find an exact trig value"
    bank_count_per_difficulty = 10

    _CASES = [
        # (target_deg, "sin"/"cos", a_deg, b_deg, op) where op is "+" or "-"
        (75, "sin", 45, 30, "+"),
        (75, "cos", 45, 30, "+"),
        (15, "sin", 45, 30, "-"),
        (15, "cos", 45, 30, "-"),
        (105, "sin", 60, 45, "+"),
        (105, "cos", 60, 45, "+"),
        (15, "sin", 60, 45, "-"),
        (15, "cos", 60, 45, "-"),
        # Alternate splits for the same targets provide additional problem IDs
        # (the split angle pair differs, so the IDs are unique)
        (75, "sin", 30, 45, "+"),
        (75, "cos", 30, 45, "+"),
        (105, "sin", 45, 60, "+"),
        (105, "cos", 45, 60, "+"),
        (165, "sin", 120, 45, "+"),
        (165, "cos", 120, 45, "+"),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        target, fn, a_deg, b_deg, op = rng.choice(self._CASES)

        a = sp.rad(a_deg)
        b = sp.rad(b_deg)
        if op == "+":
            expr_angle = a + b
        else:
            expr_angle = a - b

        if fn == "sin":
            # sin(a +/- b) = sin a cos b +/- cos a sin b
            exact = sp.simplify(sp.sin(expr_angle))
            formula = (
                r"\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta"
                if op == "+"
                else r"\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta"
            )
            target_latex = rf"\sin({target}^\circ)"
        else:
            exact = sp.simplify(sp.cos(expr_angle))
            formula = (
                r"\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta"
                if op == "+"
                else r"\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta"
            )
            target_latex = rf"\cos({target}^\circ)"

        exact_latex = sp.latex(sp.nsimplify(exact, rational=False))

        # Substitution line
        sin_a = sp.latex(sp.nsimplify(sp.sin(a), rational=False))
        cos_a = sp.latex(sp.nsimplify(sp.cos(a), rational=False))
        sin_b = sp.latex(sp.nsimplify(sp.sin(b), rational=False))
        cos_b = sp.latex(sp.nsimplify(sp.cos(b), rational=False))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (target, fn, a_deg, b_deg, op)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Use a sum or difference identity to find the exact value of "
                rf"${target_latex}$. Write ${target}^\circ = {a_deg}^\circ "
                rf"{op} {b_deg}^\circ$."
            ),
            answer_latex=rf"${target_latex} = {exact_latex}$",
            hints=[
                rf"Use the identity: ${formula}$.",
                rf"Substitute $\alpha = {a_deg}^\circ$ and $\beta = {b_deg}^\circ$, "
                rf"then use known exact values at $30^\circ$, $45^\circ$, and "
                rf"$60^\circ$.",
            ],
            solution_steps_latex=[
                rf"State the identity: ${formula}$.",
                rf"Substitute $\alpha = {a_deg}^\circ$, $\beta = {b_deg}^\circ$: "
                rf"values are $\sin({a_deg}^\circ) = {sin_a}$, "
                rf"$\cos({a_deg}^\circ) = {cos_a}$, "
                rf"$\sin({b_deg}^\circ) = {sin_b}$, "
                rf"$\cos({b_deg}^\circ) = {cos_b}$.",
                rf"Combine using the identity and simplify: "
                rf"${target_latex} = {exact_latex}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-trig-identities",
            ],
        )


# ===========================================================================
# Topic 5: trigonometric_equations  (pre-calc)
# ===========================================================================


@register
class TrigEqSinEqualsValue(Generator):
    """Solve sin x = v for x in [0, 2pi) where v is a clean unit-circle value."""
    generator_id = "trig_eq_sin_equals_value"
    topic_slug = "trigonometric_equations"
    display_name = r"Solve $\sin x = v$ for clean unit-circle values"
    # Parameter space: 9 unit-circle values (6 of which are two-solution on easy).
    bank_count_per_difficulty = 6

    # Pre-chosen exact values (sympy-friendly) and their angles in [0, 2pi).
    _VALUES = [
        (sp.Rational(1, 2), "1/2", [(1, 6), (5, 6)]),
        (sp.Rational(-1, 2), "-1/2", [(7, 6), (11, 6)]),
        (sp.sqrt(2) / 2, r"\dfrac{\sqrt{2}}{2}", [(1, 4), (3, 4)]),
        (-sp.sqrt(2) / 2, r"-\dfrac{\sqrt{2}}{2}", [(5, 4), (7, 4)]),
        (sp.sqrt(3) / 2, r"\dfrac{\sqrt{3}}{2}", [(1, 3), (2, 3)]),
        (-sp.sqrt(3) / 2, r"-\dfrac{\sqrt{3}}{2}", [(4, 3), (5, 3)]),
        (sp.Integer(1), "1", [(1, 2)]),
        (sp.Integer(-1), "-1", [(3, 2)]),
        (sp.Integer(0), "0", [(0, 1), (1, 1)]),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        value, value_latex, angles = rng.choice(self._VALUES)
        # Difficulty filtering
        if difficulty == "easy" and len(angles) != 2:
            # Easy: prefer two-solution clean cases
            two_sol_values = [v for v in self._VALUES if len(v[2]) == 2]
            value, value_latex, angles = rng.choice(two_sol_values)

        angles_latex = ", ".join(
            _fmt_pi_fraction(num, den) for (num, den) in angles
        )
        answer_latex = rf"$x = {angles_latex}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (value_latex, tuple(angles))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Solve $\sin x = {value_latex}$ on the interval $[0, 2\pi)$."
            ),
            answer_latex=answer_latex,
            hints=[
                r"Identify the reference angle whose sine has that magnitude.",
                (
                    r"Use the signs of $\sin$ in each quadrant to find all "
                    r"solutions on $[0, 2\pi)$."
                ),
            ],
            solution_steps_latex=[
                rf"We want all $x \in [0, 2\pi)$ with $\sin x = {value_latex}$.",
                (
                    r"On the unit circle, $\sin x$ is the $y$-coordinate. "
                    "Identify the angles whose $y$-coordinate equals this value."
                ),
                rf"The solutions are $x = {angles_latex}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-trig-equations",
                "#topic-unit-circle",
            ],
        )


@register
class TrigEqCosEqualsValue(Generator):
    """Solve cos x = v for x in [0, 2pi) where v is a clean unit-circle value."""
    generator_id = "trig_eq_cos_equals_value"
    topic_slug = "trigonometric_equations"
    display_name = r"Solve $\cos x = v$ for clean unit-circle values"
    # Parameter space: 9 unit-circle values (6 of which are two-solution on easy).
    bank_count_per_difficulty = 6

    _VALUES = [
        (sp.Rational(1, 2), "1/2", [(1, 3), (5, 3)]),
        (sp.Rational(-1, 2), "-1/2", [(2, 3), (4, 3)]),
        (sp.sqrt(2) / 2, r"\dfrac{\sqrt{2}}{2}", [(1, 4), (7, 4)]),
        (-sp.sqrt(2) / 2, r"-\dfrac{\sqrt{2}}{2}", [(3, 4), (5, 4)]),
        (sp.sqrt(3) / 2, r"\dfrac{\sqrt{3}}{2}", [(1, 6), (11, 6)]),
        (-sp.sqrt(3) / 2, r"-\dfrac{\sqrt{3}}{2}", [(5, 6), (7, 6)]),
        (sp.Integer(1), "1", [(0, 1)]),
        (sp.Integer(-1), "-1", [(1, 1)]),
        (sp.Integer(0), "0", [(1, 2), (3, 2)]),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        value, value_latex, angles = rng.choice(self._VALUES)
        if difficulty == "easy" and len(angles) != 2:
            two_sol_values = [v for v in self._VALUES if len(v[2]) == 2]
            value, value_latex, angles = rng.choice(two_sol_values)

        angles_latex = ", ".join(
            _fmt_pi_fraction(num, den) for (num, den) in angles
        )
        answer_latex = rf"$x = {angles_latex}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (value_latex, tuple(angles))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Solve $\cos x = {value_latex}$ on the interval $[0, 2\pi)$."
            ),
            answer_latex=answer_latex,
            hints=[
                r"Find the reference angle whose cosine has that magnitude.",
                (
                    r"Use the signs of $\cos$ in each quadrant to locate all "
                    r"solutions."
                ),
            ],
            solution_steps_latex=[
                rf"We want all $x \in [0, 2\pi)$ with $\cos x = {value_latex}$.",
                (
                    r"On the unit circle, $\cos x$ is the $x$-coordinate. "
                    "Identify angles whose $x$-coordinate equals this value."
                ),
                rf"The solutions are $x = {angles_latex}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-trig-equations",
                "#topic-unit-circle",
            ],
        )


@register
class TrigEqQuadraticInSin(Generator):
    """Solve a quadratic-in-sin equation like 2 sin^2 x - sin x - 1 = 0."""
    generator_id = "trig_eq_quadratic_in_sin"
    topic_slug = "trigonometric_equations"
    display_name = "Solve a quadratic-in-sine trigonometric equation"
    # Parameter space: small number of clean factorable cases.
    bank_count_per_difficulty = 5

    # Each case: (a, b, c) such that a s^2 + b s + c = 0 factors to clean roots
    # where each root is a clean unit-circle sine value.
    # Roots here: sin x in {1, -1, 1/2, -1/2, 0, sqrt(2)/2 etc.}
    _CASES = [
        # 2 s^2 - s - 1 = (2s + 1)(s - 1); roots: 1, -1/2
        (2, -1, -1, [sp.Integer(1), sp.Rational(-1, 2)]),
        # 2 s^2 + s - 1 = (2s - 1)(s + 1); roots: 1/2, -1
        (2, 1, -1, [sp.Rational(1, 2), sp.Integer(-1)]),
        # s^2 - 1 = 0; roots: 1, -1
        (1, 0, -1, [sp.Integer(1), sp.Integer(-1)]),
        # s^2 - s = 0 -> s(s - 1); roots: 0, 1
        (1, -1, 0, [sp.Integer(0), sp.Integer(1)]),
        # 4 s^2 - 1 = 0; roots: 1/2, -1/2
        (4, 0, -1, [sp.Rational(1, 2), sp.Rational(-1, 2)]),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c, roots = rng.choice(self._CASES)

        # Format the LHS
        def fmt_lhs(a: int, b: int, c: int) -> str:
            parts = []
            # a s^2
            if a == 1:
                parts.append(r"\sin^2 x")
            elif a == -1:
                parts.append(r"-\sin^2 x")
            else:
                parts.append(rf"{a}\sin^2 x")
            # b s
            if b != 0:
                if b > 0:
                    if b == 1:
                        parts.append(r" + \sin x")
                    else:
                        parts.append(rf" + {b}\sin x")
                else:
                    if b == -1:
                        parts.append(r" - \sin x")
                    else:
                        parts.append(rf" - {-b}\sin x")
            # c
            if c != 0:
                if c > 0:
                    parts.append(rf" + {c}")
                else:
                    parts.append(rf" - {-c}")
            return "".join(parts)

        lhs = fmt_lhs(a, b, c)

        # Collect unit-circle angles for each root's sine value
        all_angles: list[tuple[int, int]] = []
        root_descriptions = []
        for r in roots:
            angles = _angles_for_sin(r)
            if angles:
                # Deduplicate by LCM-normal form
                for ang in angles:
                    if ang not in all_angles:
                        all_angles.append(ang)
                root_descriptions.append((r, angles))

        # Sort angles numerically (num/den ascending)
        all_angles_sorted = sorted(all_angles, key=lambda nd: nd[0] / nd[1])
        angles_latex = ", ".join(
            _fmt_pi_fraction(n, d) for (n, d) in all_angles_sorted
        )

        answer_latex = rf"$x = {angles_latex}$"

        root_lines = []
        for (r, angs) in root_descriptions:
            r_lat = sp.latex(sp.nsimplify(r, rational=True))
            ang_lat = ", ".join(_fmt_pi_fraction(n, d) for (n, d) in angs)
            root_lines.append(
                rf"$\sin x = {r_lat}$ gives $x = {ang_lat}$."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Solve ${lhs} = 0$ on the interval $[0, 2\pi)$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"Let $u = \sin x$. The equation becomes a quadratic in $u$."
                ),
                (
                    "Factor (or use the quadratic formula) to find the possible "
                    r"values of $\sin x$, then find all $x$ in $[0, 2\pi)$ for "
                    "each."
                ),
            ],
            solution_steps_latex=[
                rf"Substitute $u = \sin x$: ${a}u^2 " +
                (f"+ {b}u" if b > 0 else f"- {-b}u" if b < 0 else "") +
                (f" + {c}" if c > 0 else f" - {-c}" if c < 0 else "") + " = 0$.",
                (
                    r"Factor or apply the quadratic formula to find the values "
                    r"of $u = \sin x$."
                ),
                *root_lines,
                rf"Collect all solutions: $x = {angles_latex}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-trig-equations",
            ],
        )


# ===========================================================================
# Topic 6: sinusoid  (pre-calc)
# ===========================================================================


@register
class SinusoidIdentifyParameters(Generator):
    """Given f(x) = A sin(B(x - h)) + k, identify amplitude, period, phase shift, vertical shift."""
    generator_id = "sinusoid_identify_parameters"
    topic_slug = "sinusoid"
    display_name = "Identify amplitude, period, phase shift, vertical shift of a sinusoid"

    _A_CHOICES = {
        "easy": (2, 3, 4, 5),
        "medium": (2, 3, 4, 5, 6),
        "hard": (2, 3, 4, 5, 6, 7, 8),
    }
    _B_CHOICES = {
        "easy": (1, 2),
        "medium": (1, 2, 3, 4),
        "hard": (1, 2, 3, 4, 6),
    }
    _H_RANGES = {"easy": (-2, 2), "medium": (-4, 4), "hard": (-6, 6)}
    _K_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A = rng.choice(self._A_CHOICES[difficulty])
        B = rng.choice(self._B_CHOICES[difficulty])
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])

        # Render inside argument as B(x - h)
        if h == 0:
            inside = f"{B}x" if B != 1 else "x"
        elif h > 0:
            if B == 1:
                inside = f"x - {h}"
            else:
                inside = f"{B}(x - {h})"
        else:
            if B == 1:
                inside = f"x + {-h}"
            else:
                inside = f"{B}(x + {-h})"

        # Trailing +k
        if k > 0:
            tail = f" + {k}"
        elif k < 0:
            tail = f" - {-k}"
        else:
            tail = ""

        func_latex = rf"f(x) = {A}\sin({inside}){tail}"

        # Period = 2 pi / B
        if B == 1:
            period_latex = r"2\pi"
        else:
            period_latex = rf"\dfrac{{2\pi}}{{{B}}}"

        phase_shift_desc = (
            "no phase shift" if h == 0
            else f"${h}$ units to the right" if h > 0
            else f"${-h}$ units to the left"
        )
        vertical_shift_desc = (
            "no vertical shift" if k == 0
            else f"${k}$ units upward" if k > 0
            else f"${-k}$ units downward"
        )

        answer_latex = (
            rf"Amplitude: $|A| = {A}$; period: ${period_latex}$; "
            rf"phase shift: {phase_shift_desc}; vertical shift: {vertical_shift_desc}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (A, B, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"For the function ${func_latex}$, identify (a) the amplitude, "
                rf"(b) the period, (c) the phase shift, and (d) the vertical shift."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"The general form is $f(x) = A\sin(B(x - h)) + k$. "
                    r"Amplitude $= |A|$, period $= \dfrac{2\pi}{B}$, phase shift "
                    r"$= h$, vertical shift $= k$."
                ),
                r"Read off $A$, $B$, $h$, and $k$ from the given function.",
            ],
            solution_steps_latex=[
                rf"Compare ${func_latex}$ with the template "
                rf"$f(x) = A\sin(B(x - h)) + k$.",
                rf"Read off: $A = {A}$, $B = {B}$, $h = {h}$, $k = {k}$.",
                rf"Amplitude $= |A| = {A}$.",
                rf"Period $= \dfrac{{2\pi}}{{B}} = {period_latex}$.",
                rf"Phase shift: {phase_shift_desc}.",
                rf"Vertical shift: {vertical_shift_desc}.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-functions",
                "#topic-trig-identities",
            ],
        )


@register
class SinusoidMaxMinMidline(Generator):
    """Given amplitude A and vertical shift k, compute max, min, midline."""
    generator_id = "sinusoid_max_min_midline"
    topic_slug = "sinusoid"
    display_name = "Max, min, and midline of a sinusoid"

    _A_CHOICES = {
        "easy": (1, 2, 3, 4, 5),
        "medium": (2, 3, 4, 5, 6, 7, 8),
        "hard": (3, 4, 5, 6, 7, 8, 9, 10),
    }
    _K_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A = rng.choice(self._A_CHOICES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])

        # A is positive; amplitude = A.
        max_val = k + A
        min_val = k - A

        tail = f" + {k}" if k > 0 else f" - {-k}" if k < 0 else ""
        func_latex = rf"f(x) = {A}\sin(x){tail}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"A sinusoidal function has amplitude $A = {A}$ and vertical "
                rf"shift $k = {k}$ (so its form is ${func_latex}$). "
                rf"Find (a) the maximum value, (b) the minimum value, and "
                rf"(c) the equation of the midline."
            ),
            answer_latex=(
                rf"Max: ${max_val}$; min: ${min_val}$; midline: $y = {k}$."
            ),
            hints=[
                (
                    r"The max occurs when $\sin(x) = 1$ and the min when "
                    r"$\sin(x) = -1$."
                ),
                r"The midline is the horizontal line $y = k$.",
            ],
            solution_steps_latex=[
                rf"Maximum: $f_{{\max}} = k + A = {k} + {A} = {max_val}$.",
                rf"Minimum: $f_{{\min}} = k - A = {k} - {A} = {min_val}$.",
                rf"Midline: $y = k = {k}$ (midpoint between max and min).",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-functions",
            ],
        )


@register
class SinusoidFromFeatures(Generator):
    """Given amplitude, period, phase shift, midline, write the sinusoid function."""
    generator_id = "sinusoid_from_features"
    topic_slug = "sinusoid"
    display_name = "Write a sinusoid function from its features"

    _A_CHOICES = {
        "easy": (1, 2, 3),
        "medium": (2, 3, 4, 5),
        "hard": (2, 3, 4, 5, 6, 7),
    }
    _PERIOD_CASES = {
        # (period_latex, B as integer)
        "easy": [(r"2\pi", 1), (r"\pi", 2)],
        "medium": [(r"2\pi", 1), (r"\pi", 2), (r"\dfrac{2\pi}{3}", 3)],
        "hard": [(r"\pi", 2), (r"\dfrac{2\pi}{3}", 3), (r"\dfrac{\pi}{2}", 4)],
    }
    _H_RANGES = {"easy": (-2, 2), "medium": (-4, 4), "hard": (-5, 5)}
    _K_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A = rng.choice(self._A_CHOICES[difficulty])
        period_latex, B = rng.choice(self._PERIOD_CASES[difficulty])
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])

        # Build answer: f(x) = A sin(B(x - h)) + k
        if h == 0:
            inside = f"{B}x" if B != 1 else "x"
        elif h > 0:
            inside = f"{B}(x - {h})" if B != 1 else f"x - {h}"
        else:
            inside = f"{B}(x + {-h})" if B != 1 else f"x + {-h}"

        tail = f" + {k}" if k > 0 else f" - {-k}" if k < 0 else ""
        answer_function = rf"f(x) = {A}\sin({inside}){tail}"

        phase_desc = (
            "no phase shift" if h == 0
            else f"{h} units to the right" if h > 0
            else f"{-h} units to the left"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (A, B, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Write a sinusoidal function of the form "
                rf"$f(x) = A\sin(B(x - h)) + k$ with amplitude ${A}$, "
                rf"period ${period_latex}$, phase shift {phase_desc}, and "
                rf"midline $y = {k}$."
            ),
            answer_latex=rf"${answer_function}$",
            hints=[
                (
                    r"Amplitude gives $|A|$; period gives $B$ via "
                    r"$B = \dfrac{2\pi}{\text{period}}$; phase shift gives $h$; "
                    r"midline gives $k$."
                ),
                r"Plug $A$, $B$, $h$, and $k$ into the template.",
            ],
            solution_steps_latex=[
                rf"From amplitude $= {A}$, take $A = {A}$.",
                rf"From period $= {period_latex}$, solve "
                rf"$\dfrac{{2\pi}}{{B}} = {period_latex}$ to get $B = {B}$.",
                rf"From phase shift {phase_desc}, take $h = {h}$.",
                rf"From midline $y = {k}$, take $k = {k}$.",
                rf"Substitute into the template: ${answer_function}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-functions",
                "#topic-trig-identities",
            ],
        )


# ===========================================================================
# Topic 7: law_of_sines  (pre-calc)
# ===========================================================================


@register
class LawOfSinesFindSide(Generator):
    """AAS/ASA: given two angles and a side, find another side via Law of Sines.

    Backward: pick two clean angles (30/45/60/etc) and a clean side so that the
    answer comes out in a nice form. We'll choose cases where sin of angles are
    clean.
    """
    generator_id = "law_of_sines_find_side"
    topic_slug = "law_of_sines"
    display_name = "Find a side using the Law of Sines (AAS/ASA)"
    bank_count_per_difficulty = 24

    # Case: (A, B, a, b_answer_form)
    # Law of Sines: a/sin A = b/sin B, so b = a * sin B / sin A
    # We pre-pick integer a and clean angles so that b comes out as a clean
    # exact form (integer or integer * known-radical).
    # Setup: (A_deg, B_deg, a, b_exact_latex, b_decimal)
    _CASES = [
        # A=30, B=60, a=10: b = 10 * (sqrt(3)/2) / (1/2) = 10 * sqrt(3)
        (30, 60, 10, r"10\sqrt{3}"),
        (30, 60, 6, r"6\sqrt{3}"),
        (30, 60, 8, r"8\sqrt{3}"),
        # A=45, B=30, a=10: b = 10 * (1/2) / (sqrt(2)/2) = 10/sqrt(2) = 5 sqrt(2)
        (45, 30, 10, r"5\sqrt{2}"),
        (45, 30, 6, r"3\sqrt{2}"),
        # A=45, B=60, a=8: b = 8 * (sqrt(3)/2) / (sqrt(2)/2) = 8 * sqrt(3)/sqrt(2) = 4 sqrt(6)
        (45, 60, 8, r"4\sqrt{6}"),
        (45, 60, 6, r"3\sqrt{6}"),
        # A=30, B=90, a=5: b = 5 * 1 / (1/2) = 10
        (30, 90, 5, r"10"),
        (30, 90, 7, r"14"),
        # A=60, B=30, a=10: b = 10 * (1/2) / (sqrt(3)/2) = 10/sqrt(3) = 10sqrt(3)/3
        (60, 30, 9, r"3\sqrt{3}"),
        # A=90, B=45, a=12: b = 12 * (sqrt(2)/2) / 1 = 6 sqrt(2)
        (90, 45, 12, r"6\sqrt{2}"),
        (90, 30, 10, r"5"),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A_deg, B_deg, a, b_exact = rng.choice(self._CASES)

        sin_A = sp.latex(sp.nsimplify(sp.sin(sp.rad(A_deg)), rational=False))
        sin_B = sp.latex(sp.nsimplify(sp.sin(sp.rad(B_deg)), rational=False))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (A_deg, B_deg, a)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"In triangle $ABC$, angle $A = {A_deg}^\circ$, "
                rf"angle $B = {B_deg}^\circ$, and the side opposite $A$ has "
                rf"length $a = {a}$. Find the length of side $b$ (opposite $B$) "
                rf"using the Law of Sines."
            ),
            answer_latex=rf"$b = {b_exact}$",
            hints=[
                r"The Law of Sines: $\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$.",
                rf"Solve for $b$: $b = a \cdot \dfrac{{\sin B}}{{\sin A}}$.",
            ],
            solution_steps_latex=[
                r"State the Law of Sines: "
                r"$\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$.",
                rf"Substitute the known values: "
                rf"$\dfrac{{{a}}}{{\sin {A_deg}^\circ}} = \dfrac{{b}}{{\sin {B_deg}^\circ}}$.",
                rf"Use exact values: $\sin {A_deg}^\circ = {sin_A}$, "
                rf"$\sin {B_deg}^\circ = {sin_B}$.",
                rf"Solve for $b$: $b = {a} \cdot \dfrac{{{sin_B}}}{{{sin_A}}} "
                rf"= {b_exact}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-laws-of-sines-and-cosines",
            ],
        )


@register
class LawOfSinesFindAngle(Generator):
    """Given SSA (non-ambiguous), find a missing angle via Law of Sines."""
    generator_id = "law_of_sines_find_angle"
    topic_slug = "law_of_sines"
    display_name = "Find an angle using the Law of Sines (SSA, non-ambiguous)"
    # Parameter space: limited by clean unit-circle sine values.
    bank_count_per_difficulty = 7

    # Case (A_deg, a, b, B_deg_exact): we need sin B = b * sin A / a in [0, 1].
    # We pre-build cases where that quotient is a clean unit-circle value.
    _CASES = [
        # A=30, a=10, b=10: sin B = 10 * (1/2)/10 = 1/2 -> B = 30
        (30, 10, 10, 30, "30"),
        # A=30, a=10, b=10 sqrt 3 -> sin B = 10 sqrt 3 *(1/2)/10 = sqrt(3)/2 -> 60
        # but b must be integer input for generator -- use another case
        # A=90, a=10, b=5: sin B = 5 * 1/10 = 1/2 -> B=30
        (90, 10, 5, 30, "30"),
        (90, 12, 6, 30, "30"),
        # A=45, a=10, b=10: sin B = 10 * (sqrt(2)/2)/10 = sqrt(2)/2 -> B = 45
        (45, 10, 10, 45, "45"),
        (45, 8, 8, 45, "45"),
        # A=60, a=10 sqrt(3), b=... must integer. Use: A=30, a=10, b=10 -> B=30 again
        # A=90, a=10, b=5sqrt(3)?? Not integer.
        # Simpler: A=90, a=14, b=7 -> sin B = 7/14 = 1/2 -> 30
        (90, 14, 7, 30, "30"),
        # A=30, a=10, b=5 -> sin B = 5 * 1/2 / 10 = 1/4 -- not unit-circle. skip
        # A=30, a=20, b=10 -> sin B = 10*(1/2)/20 = 1/4. skip
        # We'll stick with the clean cases above; pad with variants:
        (90, 20, 10, 30, "30"),
        (45, 14, 14, 45, "45"),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A_deg, a, b, B_deg, B_str = rng.choice(self._CASES)

        sin_A = sp.latex(sp.nsimplify(sp.sin(sp.rad(A_deg)), rational=False))
        sin_B = sp.latex(sp.nsimplify(sp.sin(sp.rad(B_deg)), rational=False))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (A_deg, a, b)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"In triangle $ABC$, angle $A = {A_deg}^\circ$, side "
                rf"$a = {a}$, and side $b = {b}$. Find angle $B$ (assume the "
                rf"acute-angle solution)."
            ),
            answer_latex=rf"$B = {B_str}^\circ$",
            hints=[
                r"Use the Law of Sines: "
                r"$\dfrac{\sin A}{a} = \dfrac{\sin B}{b}$.",
                rf"Solve for $\sin B$ and identify the angle whose sine matches.",
            ],
            solution_steps_latex=[
                r"Law of Sines: $\dfrac{\sin A}{a} = \dfrac{\sin B}{b}$.",
                rf"Substitute: "
                rf"$\dfrac{{\sin {A_deg}^\circ}}{{{a}}} = \dfrac{{\sin B}}{{{b}}}$.",
                rf"Solve for $\sin B$: "
                rf"$\sin B = \dfrac{{{b} \cdot \sin {A_deg}^\circ}}{{{a}}} "
                rf"= \dfrac{{{b} \cdot {sin_A}}}{{{a}}} = {sin_B}$.",
                rf"The acute angle with that sine is $B = {B_str}^\circ$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-laws-of-sines-and-cosines",
            ],
        )


@register
class LawOfSinesAmbiguousCase(Generator):
    """Classify SSA triangles as 0, 1, or 2 solutions (ambiguous case)."""
    generator_id = "law_of_sines_ambiguous_case"
    topic_slug = "law_of_sines"
    display_name = "Classify SSA: ambiguous case (0, 1, or 2 triangles)"
    bank_count_per_difficulty = 15

    # Each case: (A_deg, a, b) with known classification.
    # Given A (acute), a, b (b opposite B):
    # Compute h = b sin A.
    #   If A is acute:
    #       if a < h -> 0 triangles
    #       if a == h -> 1 triangle (right)
    #       if h < a < b -> 2 triangles
    #       if a >= b -> 1 triangle
    #   If A is obtuse:
    #       if a > b -> 1 triangle; else 0.
    _CASES = [
        # h = b sin A; then compare a
        # A=30, b=10, h=5
        (30, 3, 10, "0"),    # a=3 < 5 -> 0
        (30, 5, 10, "1"),    # a=5 = h -> 1 (right)
        (30, 7, 10, "2"),    # 5 < 7 < 10 -> 2
        (30, 12, 10, "1"),   # a >= b -> 1
        # A=45, b=10, h = 10 * sqrt(2)/2 ~= 7.07
        (45, 5, 10, "0"),
        (45, 9, 10, "2"),
        (45, 12, 10, "1"),
        # A=60, b=8, h = 8 * sqrt(3)/2 ~= 6.93
        (60, 5, 8, "0"),
        (60, 7, 8, "2"),
        (60, 10, 8, "1"),
        # Obtuse cases: A = 120
        (120, 12, 10, "1"),  # a > b -> 1
        (120, 6, 10, "0"),   # a < b, obtuse -> 0
        (120, 8, 10, "0"),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A_deg, a, b, classification = rng.choice(self._CASES)

        # Compute h = b sin A (as a decimal description)
        import math as _math
        h_decimal = b * _math.sin(_math.radians(A_deg))
        h_str = f"{h_decimal:.2f}"

        if classification == "0":
            answer_text = "No triangles exist."
            reason = (
                "Since the height $h$ from $b$ to the opposite side exceeds $a$ "
                "(or $A$ is obtuse with $a \\le b$), no triangle is possible."
            )
        elif classification == "1":
            if A_deg >= 90:
                answer_text = "Exactly one triangle exists."
                reason = (
                    "Since $A$ is obtuse and $a > b$, exactly one triangle is formed."
                )
            elif a >= b:
                answer_text = "Exactly one triangle exists."
                reason = (
                    rf"Since $a = {a} \ge b = {b}$, exactly one triangle is formed."
                )
            else:
                answer_text = "Exactly one triangle exists (a right triangle)."
                reason = (
                    rf"Since $a$ equals the height $h \approx {h_str}$, the "
                    "triangle is right and unique."
                )
        else:  # "2"
            answer_text = "Two triangles exist."
            reason = (
                rf"Since $h < a < b$ (with $h = b\sin A \approx {h_str}$, "
                rf"$a = {a}$, $b = {b}$), two distinct triangles satisfy the "
                "conditions."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (A_deg, a, b, classification),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"You are given angle $A = {A_deg}^\circ$, side $a = {a}$, and "
                rf"side $b = {b}$ in a triangle. How many triangles can be "
                rf"formed with this information?"
            ),
            answer_latex=answer_text,
            hints=[
                (
                    r"Compute the height $h = b \sin A$, then compare $a$ to "
                    r"$h$ and $b$. The classification depends on whether $A$ "
                    r"is acute or obtuse."
                ),
                (
                    "Acute $A$: if $a < h$ then 0; $a = h$ then 1; "
                    "$h < a < b$ then 2; $a \\ge b$ then 1. "
                    "Obtuse $A$: 1 if $a > b$, else 0."
                ),
            ],
            solution_steps_latex=[
                rf"Compute $h = b\sin A = {b}\sin {A_deg}^\circ \approx {h_str}$.",
                rf"Compare: $a = {a}$, $h \approx {h_str}$, $b = {b}$.",
                reason,
                rf"Classification: {answer_text}",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-laws-of-sines-and-cosines",
            ],
        )


# ===========================================================================
# Topic 8: law_of_cosines  (pre-calc)
# ===========================================================================


@register
class LawOfCosinesFindSide(Generator):
    """SAS: given two sides and the included angle, find the third side.

    Use cos(60) = 1/2, cos(120) = -1/2, cos(90) = 0 for clean answers.
    """
    generator_id = "law_of_cosines_find_side"
    topic_slug = "law_of_cosines"
    display_name = "Find a side using the Law of Cosines (SAS)"
    # Parameter space: limited by clean exact-value answer constraints.
    bank_count_per_difficulty = 8

    # Case: (a, b, C_deg, c_exact_latex)
    # c^2 = a^2 + b^2 - 2ab cos C
    _CASES_EASY = [
        (3, 4, 90, "5"),       # Pythagorean triples
        (5, 12, 90, "13"),
        (8, 15, 90, "17"),
        (6, 8, 90, "10"),
        (9, 12, 90, "15"),
        (7, 24, 90, "25"),
        (20, 21, 90, "29"),
        (5, 8, 60, r"7"),      # 25+64-40 = 49
        (3, 5, 120, r"7"),     # 9+25+15 = 49
    ]
    _CASES_MEDIUM = [
        # 60 deg: c^2 = a^2 + b^2 - ab
        (3, 5, 60, r"\sqrt{19}"),
        (4, 6, 60, r"2\sqrt{7}"),
        (5, 8, 60, r"7"),    # 25+64-40=49, c=7
        (7, 8, 60, r"\sqrt{57}"),
        (3, 8, 60, r"7"),    # 9+64-24 = 49
        (4, 5, 60, r"\sqrt{21}"),
        (5, 7, 60, r"\sqrt{39}"),
        # 120 deg: c^2 = a^2 + b^2 + ab
        (3, 5, 120, r"7"),   # 9+25+15 = 49
        (5, 8, 120, r"\sqrt{129}"),
        (4, 5, 120, r"\sqrt{61}"),
        (6, 10, 120, r"14"),     # 36+100+60 = 196
    ]
    _CASES_HARD = [
        (7, 8, 120, r"13"),      # 49+64+56 = 169
        (5, 7, 60, r"\sqrt{39}"),
        (8, 10, 60, r"2\sqrt{21}"),  # 64+100-80=84=4*21
        (9, 10, 120, r"\sqrt{271}"),
        (6, 10, 120, r"14"),     # 36+100+60 = 196
        (4, 7, 60, r"\sqrt{37}"),
        (7, 15, 60, r"13"),      # 49+225-105 = 169
        (8, 15, 60, r"13"),      # 64+225-120 = 169
        (5, 16, 120, r"19"),     # 25+256+80 = 361
        (9, 11, 60, r"\sqrt{103}"),
        (6, 11, 120, r"\sqrt{223}"),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cases = {
            "easy": self._CASES_EASY,
            "medium": self._CASES_MEDIUM,
            "hard": self._CASES_HARD,
        }[difficulty]
        a, b, C_deg, c_exact = rng.choice(cases)

        # cos of the angle as exact
        cos_C = sp.cos(sp.rad(C_deg))
        cos_C_latex = sp.latex(sp.nsimplify(cos_C, rational=True))

        # c^2 = a^2 + b^2 - 2ab cos C
        c_squared = a * a + b * b - 2 * a * b * float(cos_C)
        c_squared_int = round(c_squared)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, C_deg)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"In triangle $ABC$, sides $a = {a}$ and $b = {b}$ meet at "
                rf"angle $C = {C_deg}^\circ$. Find the length of side $c$ "
                rf"(the side opposite $C$) using the Law of Cosines."
            ),
            answer_latex=rf"$c = {c_exact}$",
            hints=[
                r"The Law of Cosines: $c^2 = a^2 + b^2 - 2ab\cos C$.",
                rf"Substitute $a = {a}$, $b = {b}$, and $\cos {C_deg}^\circ "
                rf"= {cos_C_latex}$.",
            ],
            solution_steps_latex=[
                r"Apply the Law of Cosines: $c^2 = a^2 + b^2 - 2ab\cos C$.",
                rf"Substitute: $c^2 = {a}^2 + {b}^2 - 2({a})({b})\cos {C_deg}^\circ$.",
                rf"Use $\cos {C_deg}^\circ = {cos_C_latex}$: "
                rf"$c^2 = {a * a} + {b * b} - 2 \cdot {a} \cdot {b} \cdot {cos_C_latex} = {c_squared_int}$.",
                rf"Take the positive square root: $c = \sqrt{{{c_squared_int}}} = {c_exact}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-laws-of-sines-and-cosines",
            ],
        )


@register
class LawOfCosinesFindAngle(Generator):
    """SSS: given three sides, find an angle using the Law of Cosines.

    Backward: choose sides that give cos(angle) equal to a clean value
    (0, 1/2, -1/2, etc.) so the angle is 30, 60, 90, 120, etc.
    """
    generator_id = "law_of_cosines_find_angle"
    topic_slug = "law_of_cosines"
    display_name = "Find an angle using the Law of Cosines (SSS)"
    # Parameter space: limited by cleanly-computable angle cases.
    bank_count_per_difficulty = 7

    # Reverse cases from find_side:
    # (a, b, c, angle_deg_for_C)
    _CASES = [
        (3, 4, 5, 90),
        (5, 12, 13, 90),
        (8, 15, 17, 90),
        (5, 8, 7, 60),    # from (5,8,60) above, c=7
        (3, 5, 7, 120),   # from (3,5,120), c=7
        (7, 8, 13, 120),  # from (7,8,120), c=13
        (6, 10, 14, 120), # from (6,10,120), c=14
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c, C_deg = rng.choice(self._CASES)

        # cos C = (a^2 + b^2 - c^2) / (2ab)
        numerator = a * a + b * b - c * c
        denominator = 2 * a * b
        from fractions import Fraction as _F
        cos_val = _F(numerator, denominator)
        if cos_val.denominator == 1:
            cos_latex = str(cos_val.numerator)
        else:
            if cos_val.numerator < 0:
                cos_latex = rf"-\dfrac{{{-cos_val.numerator}}}{{{cos_val.denominator}}}"
            else:
                cos_latex = rf"\dfrac{{{cos_val.numerator}}}{{{cos_val.denominator}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"A triangle has sides $a = {a}$, $b = {b}$, and $c = {c}$. "
                rf"Find the angle $C$ opposite side $c$ using the Law of Cosines."
            ),
            answer_latex=rf"$C = {C_deg}^\circ$",
            hints=[
                r"Rearrange the Law of Cosines to solve for $\cos C$: "
                r"$\cos C = \dfrac{a^2 + b^2 - c^2}{2ab}$.",
                "Compute the fraction, then identify the angle whose cosine "
                "equals that value.",
            ],
            solution_steps_latex=[
                r"Apply the Law of Cosines solved for $\cos C$: "
                r"$\cos C = \dfrac{a^2 + b^2 - c^2}{2ab}$.",
                rf"Substitute: $\cos C = "
                rf"\dfrac{{{a}^2 + {b}^2 - {c}^2}}{{2 \cdot {a} \cdot {b}}} "
                rf"= \dfrac{{{a * a} + {b * b} - {c * c}}}{{{2 * a * b}}} "
                rf"= {cos_latex}$.",
                rf"The angle with that cosine is $C = {C_deg}^\circ$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-laws-of-sines-and-cosines",
            ],
        )


@register
class LawOfCosinesSasInteger(Generator):
    """SAS with angle 60 or 120 giving integer answer (a^2+b^2-ab or a^2+b^2+ab)."""
    generator_id = "law_of_cosines_sas_integer"
    topic_slug = "law_of_cosines"
    display_name = "Law of Cosines (SAS): clean 60/120 integer case"
    # Parameter space: limited integer-answer SAS cases.
    bank_count_per_difficulty = 8

    # For C=60: c^2 = a^2 + b^2 - ab; we want c integer.
    # For C=120: c^2 = a^2 + b^2 + ab; we want c integer.
    # Known cases:
    # (5, 8, 60, 7): 25+64-40=49
    # (7, 8, 60, ?): 49+64-56=57 -> not square
    # (3, 8, 60, 7): 9+64-24=49
    # (7, 8, 120, 13): 49+64+56=169
    # (3, 5, 120, 7): 9+25+15=49
    # (5, 8, 120, ?): 25+64+40=129 -> not square
    # (5, 16, 120, 19): 25+256+80=361=19^2
    # (7, 15, 120, 19) -> 49+225+105 = 379 -> no
    # (3, 7, 60, ?): 9+49-21=37 -> no
    # (8, 15, 60, 13): 64+225-120=169
    # (7, 15, 60, 13): 49+225-105=169
    # (8, 15, 120, ?): 64+225+120=409 no
    # (16, 40, 120, ?) -> 256+1600+640=2496 no
    # Confirmed integer cases:
    _CASES = [
        (5, 8, 60, 7),
        (3, 8, 60, 7),
        (7, 15, 60, 13),
        (8, 15, 60, 13),
        (3, 5, 120, 7),
        (7, 8, 120, 13),
        (5, 16, 120, 19),
        (6, 10, 120, 14),
        (5, 3, 60, sp.sqrt(19)),  # fallback if we want variety, else drop
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Restrict to integer-answer cases only
        integer_cases = [c for c in self._CASES if isinstance(c[3], int)]
        a, b, C_deg, c_val = rng.choice(integer_cases)

        cos_C = sp.cos(sp.rad(C_deg))
        cos_C_latex = sp.latex(sp.nsimplify(cos_C, rational=True))

        if C_deg == 60:
            formula_reduction = rf"c^2 = a^2 + b^2 - ab"
            substitution = (
                rf"c^2 = {a}^2 + {b}^2 - ({a})({b}) = "
                rf"{a * a} + {b * b} - {a * b} = {c_val * c_val}"
            )
        else:  # 120
            formula_reduction = rf"c^2 = a^2 + b^2 + ab"
            substitution = (
                rf"c^2 = {a}^2 + {b}^2 + ({a})({b}) = "
                rf"{a * a} + {b * b} + {a * b} = {c_val * c_val}"
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, C_deg)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"In triangle $ABC$, sides $a = {a}$ and $b = {b}$ meet at "
                rf"angle $C = {C_deg}^\circ$. Find the length of side $c$."
            ),
            answer_latex=rf"$c = {c_val}$",
            hints=[
                r"Use the Law of Cosines: $c^2 = a^2 + b^2 - 2ab\cos C$.",
                rf"Since $\cos {C_deg}^\circ = {cos_C_latex}$, the formula "
                rf"simplifies to ${formula_reduction}$.",
            ],
            solution_steps_latex=[
                r"Law of Cosines: $c^2 = a^2 + b^2 - 2ab\cos C$.",
                rf"Substitute $\cos {C_deg}^\circ = {cos_C_latex}$ to get "
                rf"${formula_reduction}$.",
                rf"Compute: ${substitution}$.",
                rf"Take the positive square root: $c = {c_val}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-laws-of-sines-and-cosines",
            ],
        )


# ===========================================================================
# Topic 9: vectors  (pre-calc)
# ===========================================================================


@register
class VectorMagnitude(Generator):
    """Magnitude of a 2D vector: |v| = sqrt(v1^2 + v2^2) using Pythagorean triples."""
    generator_id = "vector_magnitude"
    topic_slug = "vectors"
    display_name = "Magnitude of a 2D vector using Pythagorean triples"
    bank_count_per_difficulty = 30

    _TRIPLES_EASY = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    _TRIPLES_MEDIUM = [(5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    _TRIPLES_HARD = [(8, 15, 17), (20, 21, 29), (9, 40, 41), (12, 35, 37)]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = {
            "easy": self._TRIPLES_EASY,
            "medium": self._TRIPLES_MEDIUM,
            "hard": self._TRIPLES_HARD,
        }[difficulty]
        a, b, c = rng.choice(triples)
        # Randomize signs and order
        if rng.random() < 0.5:
            a, b = b, a
        sx = rng.choice([1, -1])
        sy = rng.choice([1, -1])
        v1 = sx * a
        v2 = sy * b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (v1, v2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Find the magnitude of the vector "
                rf"$\vec{{v}} = \langle {v1}, {v2} \rangle$."
            ),
            answer_latex=rf"$|\vec{{v}}| = {c}$",
            hints=[
                r"The magnitude of $\vec{v} = \langle v_1, v_2 \rangle$ is "
                r"$|\vec{v}| = \sqrt{v_1^2 + v_2^2}$.",
                r"Squaring eliminates the sign of each component.",
            ],
            solution_steps_latex=[
                r"Apply the magnitude formula: "
                r"$|\vec{v}| = \sqrt{v_1^2 + v_2^2}$.",
                rf"Substitute: $|\vec{{v}}| = \sqrt{{({v1})^2 + ({v2})^2}} "
                rf"= \sqrt{{{v1 * v1} + {v2 * v2}}}$.",
                rf"Simplify: $|\vec{{v}}| = \sqrt{{{v1 * v1 + v2 * v2}}} = {c}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-vectors",
            ],
        )


@register
class VectorAdditionAndScalar(Generator):
    """Compute c*u + v for given vectors u, v and scalar c."""
    generator_id = "vector_addition_and_scalar"
    topic_slug = "vectors"
    display_name = "Compute $c\\vec{u} + \\vec{v}$ for given vectors"

    _COMP_RANGES = {
        "easy": (-5, 5),
        "medium": (-8, 8),
        "hard": (-12, 12),
    }
    _SCALAR_RANGES = {
        "easy": (-3, 3),
        "medium": (-5, 5),
        "hard": (-7, 7),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._COMP_RANGES[difficulty]
        u1 = rng.randint(lo, hi)
        u2 = rng.randint(lo, hi)
        v1 = rng.randint(lo, hi)
        v2 = rng.randint(lo, hi)
        s_lo, s_hi = self._SCALAR_RANGES[difficulty]
        c = rng.randint(s_lo, s_hi)
        while c in (0, 1):
            c = rng.randint(s_lo, s_hi)

        # Result
        r1 = c * u1 + v1
        r2 = c * u2 + v2

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (c, u1, u2, v1, v2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Given $\vec{{u}} = \langle {u1}, {u2} \rangle$, "
                rf"$\vec{{v}} = \langle {v1}, {v2} \rangle$, and $c = {c}$, "
                rf"compute $c\vec{{u}} + \vec{{v}}$."
            ),
            answer_latex=rf"$\langle {r1}, {r2} \rangle$",
            hints=[
                (
                    r"Scalar multiplication: $c\vec{u} = \langle c u_1, "
                    r"c u_2 \rangle$."
                ),
                (
                    r"Vector addition: add corresponding components."
                ),
            ],
            solution_steps_latex=[
                rf"Compute $c\vec{{u}} = {c}\langle {u1}, {u2} \rangle "
                rf"= \langle {c * u1}, {c * u2} \rangle$.",
                rf"Add $\vec{{v}}$: $\langle {c * u1}, {c * u2} \rangle "
                rf"+ \langle {v1}, {v2} \rangle "
                rf"= \langle {c * u1} + {v1}, {c * u2} + {v2} \rangle$.",
                rf"Simplify components: $\langle {r1}, {r2} \rangle$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-vectors",
            ],
        )


@register
class VectorPolarToRectangular(Generator):
    """Convert a magnitude + angle to rectangular components.

    Uses exact-value angles (0, 30, 45, 60, 90, 120, 135, 150, 180, ...).
    Backward: pick magnitude that keeps components clean.
    """
    generator_id = "vector_polar_to_rectangular"
    topic_slug = "vectors"
    display_name = "Convert polar (magnitude, angle) to rectangular components"
    bank_count_per_difficulty = 24

    # (angle_deg, mag) that produce clean rectangular components.
    _CASES = [
        (0, 5),
        (0, 10),
        (90, 5),
        (90, 10),
        (180, 5),
        (180, 10),
        (270, 5),
        (30, 2),   # (sqrt(3), 1)
        (30, 4),
        (45, 2),   # (sqrt(2), sqrt(2))
        (45, 4),
        (60, 2),   # (1, sqrt(3))
        (60, 4),
        (120, 2),  # (-1, sqrt(3))
        (135, 2),  # (-sqrt(2), sqrt(2))
        (150, 2),  # (-sqrt(3), 1)
        (210, 2),
        (225, 2),
        (240, 2),
        (300, 2),
        (315, 2),
        (330, 2),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        angle_deg, mag = rng.choice(self._CASES)
        theta = sp.rad(angle_deg)
        x_comp = sp.nsimplify(mag * sp.cos(theta), rational=False)
        y_comp = sp.nsimplify(mag * sp.sin(theta), rational=False)
        x_latex = sp.latex(x_comp)
        y_latex = sp.latex(y_comp)

        cos_lat = sp.latex(sp.nsimplify(sp.cos(theta), rational=False))
        sin_lat = sp.latex(sp.nsimplify(sp.sin(theta), rational=False))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (angle_deg, mag)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"A vector has magnitude $r = {mag}$ and direction angle "
                rf"$\theta = {angle_deg}^\circ$ (measured counterclockwise "
                rf"from the positive $x$-axis). Write the vector in "
                rf"component form $\langle x, y \rangle$."
            ),
            answer_latex=rf"$\langle {x_latex}, {y_latex} \rangle$",
            hints=[
                (
                    r"A vector in polar form $(r, \theta)$ has rectangular "
                    r"form $\langle r\cos\theta, r\sin\theta \rangle$."
                ),
                rf"Use exact values: $\cos {angle_deg}^\circ = {cos_lat}$, "
                rf"$\sin {angle_deg}^\circ = {sin_lat}$.",
            ],
            solution_steps_latex=[
                r"Apply the polar-to-rectangular conversion: "
                r"$\vec{v} = \langle r\cos\theta, r\sin\theta \rangle$.",
                rf"Substitute $r = {mag}$, $\theta = {angle_deg}^\circ$: "
                rf"$\vec{{v}} = \langle {mag}\cos {angle_deg}^\circ, "
                rf"{mag}\sin {angle_deg}^\circ \rangle$.",
                rf"Use exact values: $\cos {angle_deg}^\circ = {cos_lat}$, "
                rf"$\sin {angle_deg}^\circ = {sin_lat}$.",
                rf"Simplify: $\vec{{v}} = \langle {x_latex}, {y_latex} \rangle$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-vectors",
            ],
        )


# ===========================================================================
# Topic 10: dot_product  (pre-calc)
# ===========================================================================


@register
class DotProductCompute(Generator):
    """Compute u . v = u1 v1 + u2 v2 for given vectors."""
    generator_id = "dot_product_compute"
    topic_slug = "dot_product"
    display_name = "Compute the dot product of two 2D vectors"

    _RANGES = {
        "easy": (-6, 6),
        "medium": (-10, 10),
        "hard": (-15, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        u1 = rng.randint(lo, hi)
        u2 = rng.randint(lo, hi)
        v1 = rng.randint(lo, hi)
        v2 = rng.randint(lo, hi)
        result = u1 * v1 + u2 * v2

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (u1, u2, v1, v2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Compute $\vec{{u}} \cdot \vec{{v}}$ for "
                rf"$\vec{{u}} = \langle {u1}, {u2} \rangle$ and "
                rf"$\vec{{v}} = \langle {v1}, {v2} \rangle$."
            ),
            answer_latex=rf"$\vec{{u}} \cdot \vec{{v}} = {result}$",
            hints=[
                r"The dot product of 2D vectors is "
                r"$\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2$.",
                r"Multiply matching components, then add.",
            ],
            solution_steps_latex=[
                r"Apply the formula "
                r"$\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2$.",
                rf"Substitute: $\vec{{u}} \cdot \vec{{v}} = "
                rf"({u1})({v1}) + ({u2})({v2}) = {u1 * v1} + {u2 * v2}$.",
                rf"Simplify: $\vec{{u}} \cdot \vec{{v}} = {result}$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-vectors",
            ],
        )


@register
class DotProductAngleBetween(Generator):
    """Find the angle between two vectors using cos t = (u.v)/(|u||v|).

    Backward: pick two vectors whose cos(angle) is a clean unit-circle value.
    """
    generator_id = "dot_product_angle_between"
    topic_slug = "dot_product"
    display_name = "Angle between two vectors via the dot product"
    bank_count_per_difficulty = 20

    # Cases: (u, v, angle_deg). Chosen so that cos(angle) is clean and magnitudes
    # are Pythagorean-triple clean.
    _CASES = [
        # Perpendicular: 90 deg
        ((3, 4), (-4, 3), 90),
        ((1, 0), (0, 1), 90),
        ((5, 0), (0, 7), 90),
        ((3, 0), (0, -5), 90),
        # Parallel same direction: 0
        ((3, 4), (6, 8), 0),
        ((1, 0), (5, 0), 0),
        ((3, 4), (9, 12), 0),
        # Opposite: 180
        ((3, 4), (-3, -4), 180),
        ((1, 0), (-5, 0), 180),
        # 45 deg via ((1,0),(1,1))
        ((1, 0), (1, 1), 45),  # |u|=1, |v|=sqrt(2), u.v=1 -> cos=1/sqrt(2)
        # 60 deg via ((1,0),(1,sqrt3))? sqrt(3) not integer, skip.
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        u, v, angle_deg = rng.choice(self._CASES)
        u1, u2 = u
        v1, v2 = v
        dot = u1 * v1 + u2 * v2
        mag_u_sq = u1 * u1 + u2 * u2
        mag_v_sq = v1 * v1 + v2 * v2
        # Render magnitudes in LaTeX
        mag_u_lat = sp.latex(sp.sqrt(mag_u_sq))
        mag_v_lat = sp.latex(sp.sqrt(mag_v_sq))

        cos_val = sp.nsimplify(
            sp.Rational(dot, 1) / (sp.sqrt(mag_u_sq) * sp.sqrt(mag_v_sq)),
            rational=False,
        )
        cos_lat = sp.latex(cos_val)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (u1, u2, v1, v2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Find the angle between $\vec{{u}} = \langle {u1}, {u2} \rangle$ "
                rf"and $\vec{{v}} = \langle {v1}, {v2} \rangle$."
            ),
            answer_latex=rf"${angle_deg}^\circ$",
            hints=[
                r"Use the formula "
                r"$\cos\theta = \dfrac{\vec{u} \cdot \vec{v}}"
                r"{|\vec{u}|\,|\vec{v}|}$.",
                r"Compute the dot product and the two magnitudes, then identify "
                r"the angle.",
            ],
            solution_steps_latex=[
                rf"Compute the dot product: "
                rf"$\vec{{u}} \cdot \vec{{v}} = ({u1})({v1}) + ({u2})({v2}) = {dot}$.",
                rf"Compute magnitudes: $|\vec{{u}}| = \sqrt{{{mag_u_sq}}} = {mag_u_lat}$ "
                rf"and $|\vec{{v}}| = \sqrt{{{mag_v_sq}}} = {mag_v_lat}$.",
                rf"Apply $\cos\theta = \dfrac{{\vec{{u}} \cdot \vec{{v}}}}"
                rf"{{|\vec{{u}}|\,|\vec{{v}}|}} "
                rf"= \dfrac{{{dot}}}{{{mag_u_lat} \cdot {mag_v_lat}}} = {cos_lat}$.",
                rf"The angle with that cosine is $\theta = {angle_deg}^\circ$.",
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-vectors",
            ],
        )


@register
class DotProductPerpendicularTest(Generator):
    """Decide if two vectors are perpendicular by checking if their dot product is zero."""
    generator_id = "dot_product_perpendicular_test"
    topic_slug = "dot_product"
    display_name = "Perpendicular test via the dot product"
    bank_count_per_difficulty = 30

    _RANGES = {
        "easy": (-5, 5),
        "medium": (-8, 8),
        "hard": (-12, 12),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        is_perp = rng.random() < 0.5
        if is_perp:
            # Pick u nonzero; set v perpendicular as (-u2, u1) or (u2, -u1)
            while True:
                u1 = rng.randint(lo, hi)
                u2 = rng.randint(lo, hi)
                if (u1, u2) != (0, 0):
                    break
            sign = rng.choice([1, -1])
            v1 = sign * (-u2)
            v2 = sign * u1
            # Optionally scale v
            scale = rng.choice([1, 2, 3])
            v1 *= scale
            v2 *= scale
        else:
            # Pick arbitrary vectors with nonzero dot product
            while True:
                u1 = rng.randint(lo, hi)
                u2 = rng.randint(lo, hi)
                v1 = rng.randint(lo, hi)
                v2 = rng.randint(lo, hi)
                dot_check = u1 * v1 + u2 * v2
                if (u1, u2) != (0, 0) and (v1, v2) != (0, 0) and dot_check != 0:
                    break

        dot = u1 * v1 + u2 * v2
        if dot == 0:
            answer = "Yes, the vectors are perpendicular."
            conclusion = (
                "Since the dot product is $0$, the two vectors are "
                "perpendicular."
            )
        else:
            answer = "No, the vectors are not perpendicular."
            conclusion = (
                rf"Since the dot product is ${dot} \ne 0$, the vectors are not "
                "perpendicular."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (u1, u2, v1, v2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Are the vectors $\vec{{u}} = \langle {u1}, {u2} \rangle$ and "
                rf"$\vec{{v}} = \langle {v1}, {v2} \rangle$ perpendicular?"
            ),
            answer_latex=answer,
            hints=[
                (
                    r"Two nonzero vectors are perpendicular iff their dot "
                    r"product is zero."
                ),
                r"Compute $u_1 v_1 + u_2 v_2$ and check whether it equals $0$.",
            ],
            solution_steps_latex=[
                rf"Compute the dot product: "
                rf"$\vec{{u}} \cdot \vec{{v}} = ({u1})({v1}) + ({u2})({v2}) "
                rf"= {u1 * v1} + {u2 * v2} = {dot}$.",
                conclusion,
            ],
            tags=[
                "#branch-pre-calculus",
                "#topic-vectors",
            ],
        )
