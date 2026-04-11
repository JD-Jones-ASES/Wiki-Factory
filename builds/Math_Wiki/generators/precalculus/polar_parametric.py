"""Polar graphs and parametric equations (pre-calculus Wave C).

Six generators total covering two topic slugs:

Polar graphs (``polar_graphs``):
- IdentifyPolarCurveType: classify r = a, r = a*cos(theta), r = a(1 +/- cos theta),
  r = a*cos(n*theta) as circle, cardioid, rose, or limacon. Rotation.
  ``bank_count_per_difficulty = 12``.
- PolarToCartesianPoint: convert (r, theta) to (x, y) using clean angles.
- CartesianToPolarPoint: convert (x, y) to (r, theta) with theta in
  [0, 2*pi), using exact-value angles.

Parametric (``parametric``):
- EliminateParameterToCartesian: eliminate t from $x = f(t), y = g(t)$
  to get a Cartesian equation.
- ParametricPointAtTValue: plug a specific $t$ into a parametric pair
  and report $(x, y)$.
- ParametricDescribeOrientation: determine the direction of traversal
  (left-to-right, right-to-left, up, down) from a parametric pair.

Backward construction throughout: all answers are built from clean
unit-circle values and small integers so nothing escapes to approximate
decimals.
"""
from __future__ import annotations

import math
import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Tag bundles
# ---------------------------------------------------------------------------


POLAR_TAGS = [
    "#branch-pre-calculus",
    "#topic-analytic-geometry",
    "#skill-visualization",
]

POLAR_CONVERT_TAGS = [
    "#branch-pre-calculus",
    "#topic-analytic-geometry",
    "#skill-formula-substitution",
]

PARAMETRIC_TAGS = [
    "#branch-pre-calculus",
    "#topic-analytic-geometry",
    "#skill-multi-step",
]


def _format_pi_fraction(num: int, den: int) -> str:
    """Render (num*pi)/den as clean LaTeX (matches trig_core helper)."""
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


def _format_point(x, y) -> str:
    return f"({x},\\ {y})"


# ===========================================================================
# Generator 1: identify_polar_curve_type
# ===========================================================================


@register
class IdentifyPolarCurveType(Generator):
    """Classify common polar curves by inspecting the form of $r(\\theta)$.

    Rotation generator. Six families:
    - $r = a$               : circle centred at origin of radius $|a|$.
    - $r = a\\cos\\theta$   : circle through origin (diameter $|a|$).
    - $r = a\\sin\\theta$   : circle through origin (diameter $|a|$).
    - $r = a(1 + \\cos\\theta)$ (or variants with $\\pm$ and $\\sin$): cardioid.
    - $r = a\\cos(n\\theta)$ with integer $n \\ge 2$: rose.
    - $r = a + b\\cos\\theta$ with $|a| > |b| > 0$ (or similar): limacon.
    """
    generator_id = "identify_polar_curve_type"
    topic_slug = "polar_graphs"
    display_name = "Classify a polar curve as circle, cardioid, rose, or limacon"

    bank_count_per_difficulty = 12

    _FAMILIES = (
        "circle_origin",
        "circle_origin_shifted",
        "cardioid",
        "rose",
        "limacon",
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        family = rng.choice(self._FAMILIES)
        a = rng.choice([c for c in range(-6, 7) if c != 0])

        if family == "circle_origin":
            equation_latex = f"r = {a}"
            classification = "Circle"
            reason = (
                f"A constant polar equation $r = {a}$ describes a circle "
                f"centred at the origin with radius $|{a}| = {abs(a)}$."
            )
        elif family == "circle_origin_shifted":
            func = rng.choice(["\\cos", "\\sin"])
            coeff = "" if a == 1 else ("-" if a == -1 else f"{a}")
            equation_latex = f"r = {coeff}{func}\\theta"
            classification = "Circle (off-origin)"
            reason = (
                f"An equation of the form $r = a\\,{func}\\theta$ traces a "
                f"circle of diameter $|a| = {abs(a)}$ that passes through the "
                "origin."
            )
        elif family == "cardioid":
            func = rng.choice(["\\cos", "\\sin"])
            op = rng.choice(["+", "-"])
            coeff = "" if abs(a) == 1 else f"{abs(a)}"
            sign = "" if a > 0 else "-"
            equation_latex = f"r = {sign}{coeff}(1 {op} {func}\\theta)"
            classification = "Cardioid"
            reason = (
                f"The form $r = a(1 \\pm {func}\\theta)$ with equal magnitudes "
                "on the constant and trig term produces a heart-shaped "
                "cardioid."
            )
        elif family == "rose":
            n = rng.randint(2, 5)
            func = rng.choice(["\\cos", "\\sin"])
            coeff = "" if abs(a) == 1 else f"{abs(a)}"
            sign = "" if a > 0 else "-"
            equation_latex = f"r = {sign}{coeff}{func}({n}\\theta)"
            classification = f"Rose (with {'n' if n % 2 else '2n'} petals)"
            petal_count = n if n % 2 == 1 else 2 * n
            reason = (
                f"The equation $r = a\\,{func}(n\\theta)$ with integer $n \\ge 2$ "
                f"is a rose curve. With $n = {n}$, it has {petal_count} petals."
            )
        else:  # limacon
            func = rng.choice(["\\cos", "\\sin"])
            # Pick distinct non-equal |a|, |b| so it is NOT a cardioid.
            a_val = rng.choice([c for c in range(-6, 7) if c != 0])
            b_val = rng.choice([c for c in range(-6, 7) if c != 0 and abs(c) != abs(a_val)])
            if b_val > 0:
                equation_latex = f"r = {a_val} + {b_val}{func}\\theta"
            else:
                equation_latex = f"r = {a_val} - {abs(b_val)}{func}\\theta"
            classification = "Limacon"
            reason = (
                f"An equation $r = a + b\\,{func}\\theta$ with $|a| \\ne |b|$ is "
                "a limacon (a loop- or dimple-shaped curve). Equal magnitudes "
                "would instead give a cardioid."
            )
            a = a_val  # keep a reference for the parameter tuple

        answer_latex = f"**{classification}**"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (family, a)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Classify the polar curve ${equation_latex}$ as a circle, "
                "cardioid, rose, or limacon."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Look at the overall form: is it a constant, a single "
                    "trig term, a $1 \\pm \\text{trig}$ combination, or an "
                    "$a \\pm b\\text{trig}$ with unequal coefficients?"
                ),
                (
                    "Circles: $r = a$ or $r = a\\cos\\theta$ (or $\\sin$). "
                    "Cardioid: $r = a(1 \\pm \\cos\\theta)$. "
                    "Rose: $r = a\\cos(n\\theta)$ with $n \\ge 2$. "
                    "Limacon: $r = a \\pm b\\cos\\theta$ with $|a| \\ne |b|$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Examine ${equation_latex}$ and match it against the "
                    "standard polar families."
                ),
                reason,
                f"Classification: {answer_latex}.",
            ],
            tags=POLAR_TAGS,
        )


# ===========================================================================
# Generator 2: polar_to_cartesian_point
# ===========================================================================


# (theta_num, theta_den, cos_symbolic, sin_symbolic) — clean unit-circle angles
_POLAR_ANGLE_TABLE: tuple[tuple[int, int, sp.Expr, sp.Expr], ...] = (
    (0, 1, sp.Integer(1), sp.Integer(0)),
    (1, 6, sp.sqrt(3) / 2, sp.Rational(1, 2)),
    (1, 4, sp.sqrt(2) / 2, sp.sqrt(2) / 2),
    (1, 3, sp.Rational(1, 2), sp.sqrt(3) / 2),
    (1, 2, sp.Integer(0), sp.Integer(1)),
    (2, 3, sp.Rational(-1, 2), sp.sqrt(3) / 2),
    (3, 4, -sp.sqrt(2) / 2, sp.sqrt(2) / 2),
    (5, 6, -sp.sqrt(3) / 2, sp.Rational(1, 2)),
    (1, 1, sp.Integer(-1), sp.Integer(0)),
    (7, 6, -sp.sqrt(3) / 2, sp.Rational(-1, 2)),
    (5, 4, -sp.sqrt(2) / 2, -sp.sqrt(2) / 2),
    (4, 3, sp.Rational(-1, 2), -sp.sqrt(3) / 2),
    (3, 2, sp.Integer(0), sp.Integer(-1)),
    (5, 3, sp.Rational(1, 2), -sp.sqrt(3) / 2),
    (7, 4, sp.sqrt(2) / 2, -sp.sqrt(2) / 2),
    (11, 6, sp.sqrt(3) / 2, sp.Rational(-1, 2)),
)


@register
class PolarToCartesianPoint(Generator):
    """Convert a polar point $(r, \\theta)$ to Cartesian $(x, y)$.

    Backward: pick $r$ and $\\theta$ from clean unit-circle angles so
    $x = r\\cos\\theta$ and $y = r\\sin\\theta$ land on exact values.
    """
    generator_id = "polar_to_cartesian_point"
    topic_slug = "polar_graphs"
    display_name = "Convert a polar point to Cartesian coordinates"

    _R_CHOICES = {
        "easy": (1, 2, 3, 4),
        "medium": (1, 2, 3, 4, 5, 6),
        "hard": (1, 2, 3, 4, 5, 6, 7, 8, 10),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = rng.choice(self._R_CHOICES[difficulty])
        num, den, cos_val, sin_val = rng.choice(_POLAR_ANGLE_TABLE)

        x_sym = sp.simplify(r * cos_val)
        y_sym = sp.simplify(r * sin_val)

        theta_latex = _format_pi_fraction(num, den)
        x_latex = sp.latex(x_sym)
        y_latex = sp.latex(y_sym)
        cos_latex = sp.latex(cos_val)
        sin_latex = sp.latex(sin_val)

        point_latex = f"\\left({x_latex},\\ {y_latex}\\right)"
        polar_latex = f"\\left({r},\\ {theta_latex}\\right)"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (r, num, den)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Convert the polar point ${polar_latex}$ to rectangular "
                "coordinates $(x,\\ y)$."
            ),
            answer_latex=f"${point_latex}$",
            hints=[
                (
                    r"Use $x = r\cos\theta$ and $y = r\sin\theta$."
                ),
                (
                    f"Evaluate the trig values at $\\theta = {theta_latex}$ "
                    "using the unit circle, then multiply by $r$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Recall $x = r\\cos\\theta$ and $y = r\\sin\\theta$."
                ),
                (
                    f"At $\\theta = {theta_latex}$: $\\cos\\theta = {cos_latex}$ "
                    f"and $\\sin\\theta = {sin_latex}$."
                ),
                (
                    f"Multiply by $r = {r}$: $x = {r} \\cdot {cos_latex} "
                    f"= {x_latex}$ and $y = {r} \\cdot {sin_latex} = {y_latex}$."
                ),
                f"Therefore $(x,\\ y) = {point_latex}$.",
            ],
            tags=POLAR_CONVERT_TAGS,
        )


# ===========================================================================
# Generator 3: cartesian_to_polar_point
# ===========================================================================


# Each entry: (x_sym, y_sym, r_int, theta_num, theta_den)
_CARTESIAN_TABLE: tuple[tuple[sp.Expr, sp.Expr, int, int, int], ...] = (
    (sp.Integer(1), sp.Integer(0), 1, 0, 1),
    (sp.Integer(0), sp.Integer(1), 1, 1, 2),
    (sp.Integer(-1), sp.Integer(0), 1, 1, 1),
    (sp.Integer(0), sp.Integer(-1), 1, 3, 2),
    (sp.Integer(1), sp.Integer(1), sp.sqrt(2), 1, 4),  # handled specially
    (sp.Integer(-1), sp.Integer(1), sp.sqrt(2), 3, 4),
    (sp.Integer(-1), sp.Integer(-1), sp.sqrt(2), 5, 4),
    (sp.Integer(1), sp.Integer(-1), sp.sqrt(2), 7, 4),
    (sp.Integer(2), sp.Integer(0), 2, 0, 1),
    (sp.Integer(0), sp.Integer(3), 3, 1, 2),
    (sp.Integer(-4), sp.Integer(0), 4, 1, 1),
    (sp.Integer(0), sp.Integer(-5), 5, 3, 2),
    (sp.Integer(3), sp.Integer(3), 3 * sp.sqrt(2), 1, 4),
    (sp.Integer(-2), sp.Integer(2), 2 * sp.sqrt(2), 3, 4),
)


@register
class CartesianToPolarPoint(Generator):
    """Convert Cartesian $(x, y)$ to polar $(r, \\theta)$ with $\\theta \\in [0, 2\\pi)$.

    Uses only points that produce exact unit-circle angles and clean $r$.
    """
    generator_id = "cartesian_to_polar_point"
    topic_slug = "polar_graphs"
    display_name = "Convert a Cartesian point to polar coordinates"

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(_CARTESIAN_TABLE))
        x_sym, y_sym, r_sym, num, den = _CARTESIAN_TABLE[idx]

        x_latex = sp.latex(x_sym)
        y_latex = sp.latex(y_sym)
        point_latex = f"({x_latex},\\ {y_latex})"

        if isinstance(r_sym, int):
            r_latex = str(r_sym)
        else:
            r_latex = sp.latex(sp.sympify(r_sym))

        theta_latex = _format_pi_fraction(num, den)
        polar_latex = f"\\left({r_latex},\\ {theta_latex}\\right)"

        # Justification for the particular angle
        x_val = float(x_sym)
        y_val = float(y_sym)
        if x_val > 0 and y_val == 0:
            quadrant = "positive $x$-axis"
        elif x_val < 0 and y_val == 0:
            quadrant = "negative $x$-axis"
        elif x_val == 0 and y_val > 0:
            quadrant = "positive $y$-axis"
        elif x_val == 0 and y_val < 0:
            quadrant = "negative $y$-axis"
        elif x_val > 0 and y_val > 0:
            quadrant = "quadrant I"
        elif x_val < 0 and y_val > 0:
            quadrant = "quadrant II"
        elif x_val < 0 and y_val < 0:
            quadrant = "quadrant III"
        else:
            quadrant = "quadrant IV"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Express the Cartesian point ${point_latex}$ in polar form "
                f"$(r,\\ \\theta)$ with $r > 0$ and $\\theta \\in [0,\\ 2\\pi)$."
            ),
            answer_latex=f"${polar_latex}$",
            hints=[
                (
                    r"Use $r = \sqrt{x^2 + y^2}$ and $\tan\theta = y/x$, then "
                    "identify the correct quadrant."
                ),
                (
                    "Sketch the point first; the quadrant tells you how to "
                    "interpret the reference angle."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute $r = \\sqrt{{x^2 + y^2}} = \\sqrt{{"
                    f"{sp.latex(sp.simplify(x_sym ** 2))}"
                    f" + {sp.latex(sp.simplify(y_sym ** 2))}}} = {r_latex}$."
                ),
                (
                    f"The point ${point_latex}$ lies on the {quadrant}."
                ),
                (
                    f"Choose the angle in $[0,\\ 2\\pi)$ whose terminal side "
                    f"passes through ${point_latex}$: $\\theta = {theta_latex}$."
                ),
                f"Therefore $(r,\\ \\theta) = {polar_latex}$.",
            ],
            tags=POLAR_CONVERT_TAGS,
        )


# ===========================================================================
# Topic: parametric
# ===========================================================================


# ---------------------------------------------------------------------------
# Generator 4: eliminate_parameter_to_cartesian
# ---------------------------------------------------------------------------


@register
class EliminateParameterToCartesian(Generator):
    """Eliminate $t$ from $x = f(t), y = g(t)$ to obtain a Cartesian equation.

    Backward: two cases.
    - Linear: $x = at + p$, $y = bt + q$, both with nonzero $a$. Solving
      the first for $t$ and substituting yields a linear $y = mx + c$ with
      $m = b/a$.
    - Quadratic: $x = t + p$, $y = t^2 + q$. Substituting $t = x - p$
      produces a parabola $y = (x - p)^2 + q$.
    """
    generator_id = "eliminate_parameter_to_cartesian"
    topic_slug = "parametric"
    display_name = "Eliminate the parameter to get a Cartesian equation"

    _MODES = ("linear", "quadratic")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        mode = rng.choice(self._MODES)
        t = sp.symbols("t")
        x_sym, y_sym = sp.symbols("x y")

        if mode == "linear":
            # x = a*t + p, y = b*t + q with a | b for clean slope (b/a integer)
            a = rng.choice([1, 2, 3, 4])
            # Pick b so that b/a is an integer for clean slope
            mult = rng.choice([-3, -2, -1, 1, 2, 3])
            b = a * mult
            p = rng.randint(-6, 6)
            q = rng.randint(-6, 6)
            while b == 0:
                mult = rng.choice([-3, -2, -1, 1, 2, 3])
                b = a * mult

            xt = a * t + p
            yt = b * t + q
            # Solve x = a t + p for t: t = (x - p)/a, then y = b*(x - p)/a + q
            slope = sp.Rational(b, a)
            intercept = sp.Rational(q) - slope * p
            cart_expr = slope * x_sym + intercept
            cart_latex = sp.latex(sp.simplify(cart_expr))
            answer_latex = f"$y = {cart_latex}$"

            x_latex = sp.latex(xt)
            y_latex = sp.latex(yt)
            step_lines = [
                (
                    f"Solve the first equation for $t$: "
                    f"$t = \\dfrac{{x - ({p})}}{{{a}}}$."
                ),
                (
                    f"Substitute into $y = {y_latex}$: "
                    f"$y = {b}\\cdot\\dfrac{{x - ({p})}}{{{a}}} + ({q})$."
                ),
                (
                    f"Simplify the coefficient $\\dfrac{{{b}}}{{{a}}} = "
                    f"{sp.latex(slope)}$ and distribute."
                ),
                f"The Cartesian equation is $y = {cart_latex}$.",
            ]
            params = (mode, a, b, p, q)

        else:
            # x = t + p, y = t^2 + q
            p = rng.randint(-5, 5)
            q = rng.randint(-8, 8)
            xt = t + p
            yt = t ** 2 + q

            cart_expr = (x_sym - p) ** 2 + q
            cart_latex = sp.latex(sp.simplify(cart_expr))
            answer_latex = f"$y = {cart_latex}$"

            x_latex = sp.latex(xt)
            y_latex = sp.latex(yt)
            step_lines = [
                (
                    f"Solve the first equation for $t$: $t = x - ({p})$."
                ),
                (
                    f"Substitute into $y = {y_latex}$: $y = (x - {p})^2 + ({q})$."
                ),
                (
                    f"That is already in Cartesian form: $y = {cart_latex}$."
                ),
            ]
            params = (mode, p, q)

        x_latex = sp.latex(xt)
        y_latex = sp.latex(yt)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Eliminate the parameter $t$ and express the curve "
                f"$\\begin{{cases}} x = {x_latex} \\\\ y = {y_latex} "
                "\\end{cases}$ as a Cartesian equation in $x$ and $y$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Solve one of the equations (usually the simpler one) for "
                    "$t$, then substitute into the other."
                ),
                (
                    "After substitution you should have only $x$ and $y$ "
                    "remaining. Simplify to standard form."
                ),
            ],
            solution_steps_latex=step_lines,
            tags=PARAMETRIC_TAGS,
        )


# ---------------------------------------------------------------------------
# Generator 5: parametric_point_at_t_value
# ---------------------------------------------------------------------------


@register
class ParametricPointAtTValue(Generator):
    """Evaluate $x(t)$ and $y(t)$ at a specific value of $t$.

    Backward: pick $t_0$ and simple polynomial expressions so the
    resulting point is an integer pair.
    """
    generator_id = "parametric_point_at_t_value"
    topic_slug = "parametric"
    display_name = "Evaluate a parametric curve at a specific parameter value"

    _T_RANGES = {"easy": (-3, 3), "medium": (-5, 5), "hard": (-7, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        t_lo, t_hi = self._T_RANGES[difficulty]
        t0 = rng.randint(t_lo, t_hi)

        # x(t) = a*t + b, y(t) = c*t^2 + d*t + e (small coefficients)
        a = rng.choice([c for c in range(-4, 5) if c != 0])
        b = rng.randint(-5, 5)
        c = rng.choice([c for c in range(-3, 4) if c != 0])
        d = rng.randint(-5, 5)
        e = rng.randint(-5, 5)

        t_sym = sp.symbols("t")
        xt = a * t_sym + b
        yt = c * t_sym ** 2 + d * t_sym + e

        x_val = int(xt.subs(t_sym, t0))
        y_val = int(yt.subs(t_sym, t0))

        x_latex = sp.latex(xt)
        y_latex = sp.latex(yt)

        point_latex = f"({x_val},\\ {y_val})"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, d, e, t0)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "For the parametric curve $\\begin{cases} "
                f"x = {x_latex} \\\\ y = {y_latex} \\end{{cases}}$, find the "
                f"point $(x,\\ y)$ when $t = {t0}$."
            ),
            answer_latex=f"${point_latex}$",
            hints=[
                (
                    "Substitute the given $t$-value into both parametric "
                    "equations."
                ),
                (
                    "Compute $x(t)$ and $y(t)$ independently, then write the "
                    "result as an ordered pair."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Substitute $t = {t0}$ into $x(t) = {x_latex}$: "
                    f"$x = {x_val}$."
                ),
                (
                    f"Substitute $t = {t0}$ into $y(t) = {y_latex}$: "
                    f"$y = {y_val}$."
                ),
                f"The point is ${point_latex}$.",
            ],
            tags=PARAMETRIC_TAGS,
        )


# ---------------------------------------------------------------------------
# Generator 6: parametric_describe_orientation
# ---------------------------------------------------------------------------


@register
class ParametricDescribeOrientation(Generator):
    """Describe the direction of traversal for a parametric curve.

    Backward: pick coefficients so that $dx/dt$ and $dy/dt$ at the given
    $t$ land on clean nonzero values. Direction is classified from the
    signs of those derivatives.
    """
    generator_id = "parametric_describe_orientation"
    topic_slug = "parametric"
    display_name = "Describe the direction of traversal of a parametric curve"

    bank_count_per_difficulty = 15

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        t_sym = sp.symbols("t")

        # Two styles: linear in t (global direction) or time-varying (point-specific).
        style = rng.choice(["linear", "quadratic"])

        if style == "linear":
            a = rng.choice([c for c in range(-4, 5) if c != 0])
            b = rng.choice([c for c in range(-4, 5) if c != 0])
            xt = a * t_sym
            yt = b * t_sym
            t_star = rng.randint(-3, 3)
            dx_dt = a
            dy_dt = b
            descriptor = "for the entire curve"
        else:
            a = rng.choice([c for c in range(-3, 4) if c != 0])
            b = rng.choice([c for c in range(-3, 4) if c != 0])
            xt = a * t_sym
            yt = b * t_sym ** 2
            t_star = rng.choice([-3, -2, -1, 1, 2, 3])
            dx_dt = a
            dy_dt = int((sp.diff(yt, t_sym)).subs(t_sym, t_star))
            descriptor = f"at $t = {t_star}$"

        # Compose direction words from (sign dx, sign dy)
        sx = (dx_dt > 0) - (dx_dt < 0)
        sy = (dy_dt > 0) - (dy_dt < 0)
        pairs = {
            (1, 1): "up and to the right",
            (1, 0): "to the right",
            (1, -1): "down and to the right",
            (0, 1): "straight up",
            (0, -1): "straight down",
            (-1, 1): "up and to the left",
            (-1, 0): "to the left",
            (-1, -1): "down and to the left",
        }
        direction_text = pairs[(sx, sy)]

        x_latex = sp.latex(xt)
        y_latex = sp.latex(yt)
        answer_latex = f"**{direction_text}**"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (style, a, b, t_star)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "For the parametric curve $\\begin{cases} "
                f"x = {x_latex} \\\\ y = {y_latex} \\end{{cases}}$, describe "
                f"the direction of traversal {descriptor} (e.g. up and to the "
                "right, down, to the left, etc.)."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Examine how $x$ and $y$ change with $t$. A positive rate "
                    "for $x$ means moving right; a positive rate for $y$ means "
                    "moving up."
                ),
                (
                    "Combine the two signed rates to describe the overall "
                    "direction."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute $dx/dt = {dx_dt}$ and $dy/dt = {dy_dt}$ "
                    f"{descriptor}."
                ),
                (
                    f"The signs ${'+' if dx_dt > 0 else ('-' if dx_dt < 0 else '0')}$ "
                    f"and ${'+' if dy_dt > 0 else ('-' if dy_dt < 0 else '0')}$ "
                    "give the direction."
                ),
                f"The curve is moving {direction_text}.",
            ],
            tags=PARAMETRIC_TAGS,
        )
