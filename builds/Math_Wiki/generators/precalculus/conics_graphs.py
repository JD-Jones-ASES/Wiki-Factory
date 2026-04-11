"""Introduction to conics (pre-calculus Wave C).

Three generators for the ``introduction_to_conics`` topic slug:

- ClassifyConicFromEquation: given $Ax^2 + Bxy + Cy^2 + ... = 0$ decide
  whether the locus is a circle, ellipse, parabola, or hyperbola based
  on the coefficients. Rotation-heavy, ``bank_count_per_difficulty = 15``.
- IdentifyCenterAndRadiusCircle: read the center and radius from a
  circle in standard form $(x - h)^2 + (y - k)^2 = r^2$. Backward.
- VertexOfParabolaStandard: read the vertex of a parabola written in
  either vertex form $y = a(x - h)^2 + k$ or expanded form
  $y = ax^2 + bx + c$.

Backward construction: pick the defining parameters (center, radius,
vertex) first so the answer is a clean integer tuple, then render the
statement. SymPy is used for algebraic verification.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers / tags
# ---------------------------------------------------------------------------


CONIC_INTRO_TAGS = [
    "#branch-pre-calculus",
    "#topic-conic-sections",
    "#skill-visualization",
]

CONIC_CIRCLE_TAGS = [
    "#branch-pre-calculus",
    "#topic-conic-sections",
    "#skill-formula-substitution",
]

CONIC_PARABOLA_TAGS = [
    "#branch-pre-calculus",
    "#topic-conic-sections",
    "#skill-procedural-calculation",
]


def _shift_expr(var: str, shift: int) -> str:
    """Render $(var - shift)$ with correct sign handling, or `var` for shift=0."""
    if shift == 0:
        return var
    op = "-" if shift > 0 else "+"
    return f"({var} {op} {abs(shift)})"


def _format_point(x, y) -> str:
    """Render an ordered pair as `(x, y)`."""
    return f"({x},\\ {y})"


# ===========================================================================
# Generator 1: classify_conic_from_equation
# ===========================================================================


@register
class ClassifyConicFromEquation(Generator):
    """Classify a conic by the signs and equality of its squared-term coefficients.

    We only use axis-aligned equations ($B = 0$), so the classification
    reduces to:

    - $A = C$ and same sign and both nonzero  ==>  circle
    - $A \\ne C$, same sign, both nonzero     ==>  ellipse
    - $A$ and $C$ opposite signs, both nonzero ==>  hyperbola
    - exactly one of $A$ and $C$ is zero       ==>  parabola
    """

    generator_id = "classify_conic_from_equation"
    topic_slug = "introduction_to_conics"
    display_name = "Classify a conic section from its general-form equation"

    # Small parameter space: four classes × modest coefficient range.
    bank_count_per_difficulty = 15

    _CLASSES = ("circle", "ellipse", "parabola", "hyperbola")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cls = rng.choice(self._CLASSES)
        coeff_cap = {"easy": 4, "medium": 6, "hard": 9}[difficulty]
        linear_cap = {"easy": 6, "medium": 10, "hard": 15}[difficulty]

        def rand_coeff() -> int:
            """Small nonzero coefficient."""
            return rng.choice([c for c in range(-coeff_cap, coeff_cap + 1) if c != 0])

        def rand_linear() -> int:
            return rng.randint(-linear_cap, linear_cap)

        if cls == "circle":
            # A = C, same sign, nonzero
            a_sq = rng.randint(1, coeff_cap)
            sign = rng.choice([1, -1])
            A = sign * a_sq
            C = sign * a_sq
        elif cls == "ellipse":
            # Same sign but magnitudes differ
            sign = rng.choice([1, -1])
            mag_a = rng.randint(1, coeff_cap)
            mag_c = rng.randint(1, coeff_cap)
            while mag_c == mag_a:
                mag_c = rng.randint(1, coeff_cap)
            A = sign * mag_a
            C = sign * mag_c
        elif cls == "hyperbola":
            # Opposite signs
            mag_a = rng.randint(1, coeff_cap)
            mag_c = rng.randint(1, coeff_cap)
            sign = rng.choice([1, -1])
            A = sign * mag_a
            C = -sign * mag_c
        else:  # parabola
            # exactly one of A or C is zero
            if rng.choice([True, False]):
                A = rand_coeff()
                C = 0
            else:
                A = 0
                C = rand_coeff()

        D = rand_linear()
        E = rand_linear()
        F = rng.randint(-20, 20)

        # Render the equation in Ax^2 + Cy^2 + Dx + Ey + F = 0 form.
        x, y = sp.symbols("x y")
        expr = A * x ** 2 + C * y ** 2 + D * x + E * y + F
        expr = sp.expand(expr)
        equation_latex = f"{sp.latex(expr)} = 0"

        # Classification rule for the solution steps.
        if cls == "circle":
            rule = (
                f"Both $x^2$ and $y^2$ appear with the SAME nonzero coefficient "
                f"(${A}$), which is the signature of a circle."
            )
        elif cls == "ellipse":
            rule = (
                f"Both squared terms are present with the same sign but "
                f"different magnitudes (${A}$ vs ${C}$), so the conic is an "
                "ellipse."
            )
        elif cls == "hyperbola":
            rule = (
                f"The squared terms have opposite signs (${A}$ and ${C}$), "
                "which is the hallmark of a hyperbola."
            )
        else:
            rule = (
                "Exactly one of the squared terms is missing (either $x^2$ or "
                "$y^2$ has coefficient $0$), so the conic is a parabola."
            )

        answer_latex = f"**{cls.title()}**"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (cls, A, C, D, E, F)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Classify the conic section defined by ${equation_latex}$. "
                "(Circle, ellipse, parabola, or hyperbola.)"
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Look at the coefficients of $x^2$ and $y^2$. Compare their "
                    "signs, their magnitudes, and whether either is zero."
                ),
                (
                    "Circle: same nonzero coefficient. Ellipse: same sign, "
                    "different magnitudes. Hyperbola: opposite signs. "
                    "Parabola: exactly one squared term missing."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the squared-term coefficients in ${equation_latex}$: "
                    f"$A = {A}$ (for $x^2$) and $C = {C}$ (for $y^2$)."
                ),
                rule,
                f"Therefore the conic is a **{cls}**.",
            ],
            tags=CONIC_INTRO_TAGS,
        )


# ===========================================================================
# Generator 2: identify_center_and_radius_circle
# ===========================================================================


@register
class IdentifyCenterAndRadiusCircle(Generator):
    """Read the center and radius of a circle in standard form.

    Backward: pick integer center $(h, k)$ and positive integer radius
    $r$, render $(x - h)^2 + (y - k)^2 = r^2$.
    """

    generator_id = "identify_center_and_radius_circle"
    topic_slug = "introduction_to_conics"
    display_name = "Identify the center and radius of a circle in standard form"

    _H_RANGES = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-12, 12)}
    _R_RANGES = {"easy": (1, 7), "medium": (2, 10), "hard": (3, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])
        r = rng.randint(*self._R_RANGES[difficulty])

        lhs = f"{_shift_expr('x', h)}^2 + {_shift_expr('y', k)}^2"
        rhs = f"{r ** 2}"
        equation_latex = f"{lhs} = {rhs}"

        center_latex = _format_point(h, k)
        answer_latex = f"Center: ${center_latex}$; radius: $r = {r}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k, r)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given the circle ${equation_latex}$, state its center and "
                "radius."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"A circle in standard form is $(x - h)^2 + (y - k)^2 = r^2$, "
                    r"with center $(h,\ k)$ and radius $r$."
                ),
                (
                    f"Match the given equation term-by-term against the standard "
                    f"form. The right-hand side is $r^2 = {r ** 2}$, so take the "
                    "square root to get $r$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compare ${equation_latex}$ to the standard form "
                    r"$(x - h)^2 + (y - k)^2 = r^2$."
                ),
                (
                    f"Read off $h = {h}$ and $k = {k}$, giving center "
                    f"$(h,\\ k) = {center_latex}$."
                ),
                (
                    f"From $r^2 = {r ** 2}$, take the positive square root: "
                    f"$r = {r}$."
                ),
                f"Therefore: {answer_latex}.",
            ],
            tags=CONIC_CIRCLE_TAGS,
        )


# ===========================================================================
# Generator 3: vertex_of_parabola_standard
# ===========================================================================


@register
class VertexOfParabolaStandard(Generator):
    """Find the vertex of $y = a(x - h)^2 + k$ or $y = ax^2 + bx + c$.

    Backward: pick $a$, $h$, $k$ first, then either render in vertex form
    directly or expand to $y = ax^2 + bx + c$ and ask the student to
    complete the square (or use $h = -b/(2a)$).
    """

    generator_id = "vertex_of_parabola_standard"
    topic_slug = "introduction_to_conics"
    display_name = "Find the vertex of a parabola given in vertex or standard form"

    _A_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 7)}
    _H_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-9, 9), "hard": (-14, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.randint(*self._A_RANGES[difficulty]) * rng.choice([-1, 1])
        h = rng.randint(*self._H_RANGES[difficulty])
        k = rng.randint(*self._K_RANGES[difficulty])

        form = rng.choice(["vertex", "standard"])

        vertex_latex = _format_point(h, k)

        if form == "vertex":
            # y = a(x - h)^2 + k
            a_prefix = "" if a == 1 else ("-" if a == -1 else f"{a}")
            shift = _shift_expr("x", h)
            if k == 0:
                equation_latex = f"y = {a_prefix}{shift}^2"
            elif k > 0:
                equation_latex = f"y = {a_prefix}{shift}^2 + {k}"
            else:
                equation_latex = f"y = {a_prefix}{shift}^2 - {abs(k)}"
            step_lines = [
                (
                    f"Compare ${equation_latex}$ to the vertex form "
                    r"$y = a(x - h)^2 + k$."
                ),
                (
                    f"Read off $h = {h}$ and $k = {k}$, so the vertex is "
                    f"$(h,\\ k) = {vertex_latex}$."
                ),
            ]
        else:
            # y = a x^2 + b x + c where b = -2 a h and c = a h^2 + k
            b = -2 * a * h
            c = a * h ** 2 + k
            x = sp.symbols("x")
            expanded = sp.expand(a * (x - h) ** 2 + k)
            equation_latex = f"y = {sp.latex(expanded)}"
            step_lines = [
                (
                    f"Use the vertex formula "
                    r"$h = -\dfrac{b}{2a}$ for a quadratic $y = ax^2 + bx + c$."
                ),
                (
                    f"Here $a = {a}$ and $b = {b}$, so "
                    f"$h = -\\dfrac{{{b}}}{{2 \\cdot {a}}} = {h}$."
                ),
                (
                    f"Substitute $x = {h}$ into the equation to get "
                    f"$k = y({h}) = {k}$."
                ),
                (
                    f"Therefore the vertex is $(h,\\ k) = {vertex_latex}$."
                ),
            ]

        answer_latex = f"Vertex: ${vertex_latex}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (form, a, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the vertex of the parabola ${equation_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"In vertex form $y = a(x - h)^2 + k$, the vertex is "
                    r"$(h,\ k)$ — just read it off."
                ),
                (
                    r"In standard form $y = ax^2 + bx + c$, use "
                    r"$h = -\dfrac{b}{2a}$, then compute $k = y(h)$."
                ),
            ],
            solution_steps_latex=step_lines,
            tags=CONIC_PARABOLA_TAGS,
        )
