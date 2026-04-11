"""Trigonometry core generators (pre-calculus cluster).

Five topic slugs covered:

- angles (Angles.md)
- circular_functions (Circular_Functions.md)
- the_unit_circle (The_Unit_Circle.md)
- inverse_trigonometric_functions (Inverse_Trigonometric_Functions.md)
- graphs_of_trigonometric_functions (Graphs_Of_Trigonometric_Functions.md)

Fifteen generators total (3 per topic). Backward construction is used
throughout: pick the clean answer first (integer multiples of 30 or 45,
exact unit-circle values, clean amplitude/period), then derive the
statement. Exact values use sympy's Rational and sqrt so every answer
renders as a clean LaTeX fraction or surd.
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


def _format_fraction(num: int, den: int) -> str:
    """Render num/den as a simplified LaTeX fraction (integer if den==1)."""
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    if den == 1:
        return str(num)
    return rf"\dfrac{{{num}}}{{{den}}}"


def _format_pi_fraction(num: int, den: int) -> str:
    """Render (num * pi) / den as a clean LaTeX expression.

    Examples
    --------
    >>> _format_pi_fraction(1, 4)
    '\\\\dfrac{\\\\pi}{4}'
    >>> _format_pi_fraction(0, 1)
    '0'
    >>> _format_pi_fraction(2, 1)
    '2\\\\pi'
    >>> _format_pi_fraction(-3, 4)
    '-\\\\dfrac{3\\\\pi}{4}'
    """
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


def _degrees_to_radians_fraction(deg: int) -> tuple[int, int]:
    """Return (num, den) with the reduced (num*pi)/den radian form for an integer
    degree value. Uses deg/180 -> simplified fraction then multiplied by pi.
    """
    num = deg
    den = 180
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    return num, den


def _radians_to_degrees(num: int, den: int) -> int:
    """Given a radian value (num * pi) / den, return the equivalent degrees
    as an integer (caller guarantees 180*num is divisible by den).
    """
    return (180 * num) // den


def _format_deg(d: int) -> str:
    """Render a degree value with the LaTeX degree symbol."""
    return rf"{d}^{{\circ}}"


# ===========================================================================
# Topic 1: angles
# ===========================================================================


@register
class ConvertDegreesToRadians(Generator):
    """Convert an integer degree value to radians as a clean multiple of pi.

    Backward: pick a common multiple of 30 or 45 degrees so the radian answer
    is a simple fraction of pi. The range widens with difficulty.
    """
    generator_id = "convert_degrees_to_radians"
    topic_slug = "angles"
    display_name = "Convert an angle from degrees to radians"

    _EASY = (30, 45, 60, 90, 120, 135, 150, 180, -30, -45, -60, -90, -120, -135, -150, -180)
    _MEDIUM = (
        15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 210, 225, 240, 270, 300,
        315, 330, 360, -30, -45, -60, -90, -120, -150, -180, -210, -270,
    )
    _HARD = tuple(
        list(range(-360, 0, 15)) + list(range(15, 540 + 15, 15))
    )

    _CHOICES = {"easy": _EASY, "medium": _MEDIUM, "hard": _HARD}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        deg = rng.choice(self._CHOICES[difficulty])
        num, den = _degrees_to_radians_fraction(deg)
        answer_latex = _format_pi_fraction(num, den)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (deg,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Convert ${_format_deg(deg)}$ to radians. Give your answer as an "
                "exact multiple of $\\pi$."
            ),
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"Use the conversion factor $\dfrac{\pi \text{ rad}}{180^{\circ}}$."
                ),
                (
                    r"Multiply the degree measure by $\dfrac{\pi}{180}$ and simplify."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Set up the conversion: ${deg}^{{\circ}} \cdot "
                    rf"\dfrac{{\pi}}{{180^{{\circ}}}}$."
                ),
                (
                    rf"Multiply: $\dfrac{{{deg}\pi}}{{180}}$."
                ),
                (
                    rf"Simplify the fraction: ${answer_latex}$ radians."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class ConvertRadiansToDegrees(Generator):
    """Convert a radian value (as a multiple of pi) to degrees.

    Backward: pick a clean (num*pi/den) form that lands on an integer degree.
    """
    generator_id = "convert_radians_to_degrees"
    topic_slug = "angles"
    display_name = "Convert an angle from radians to degrees"

    _EASY = (
        (1, 6), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (5, 6), (1, 1),
        (-1, 6), (-1, 4), (-1, 3), (-1, 2), (-2, 3), (-3, 4), (-5, 6), (-1, 1),
    )
    _MEDIUM = _EASY + (
        (7, 6), (5, 4), (4, 3), (3, 2), (5, 3), (7, 4), (11, 6), (2, 1),
        (-7, 6), (-5, 4), (-4, 3), (-3, 2), (-5, 3), (-7, 4), (-11, 6), (-2, 1),
    )
    _HARD = _MEDIUM + (
        (1, 12), (5, 12), (7, 12), (11, 12), (13, 6), (5, 2), (7, 3),
        (-1, 12), (-5, 12), (-7, 12), (-11, 12), (-13, 6), (-5, 2), (-7, 3),
        (3, 1), (-3, 1),
    )

    _CHOICES = {"easy": _EASY, "medium": _MEDIUM, "hard": _HARD}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        num, den = rng.choice(self._CHOICES[difficulty])
        rad_latex = _format_pi_fraction(num, den)
        deg = _radians_to_degrees(num, den)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (num, den)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Convert ${rad_latex}$ radians to degrees."
            ),
            answer_latex=f"${_format_deg(deg)}$",
            hints=[
                (
                    r"Use the conversion factor $\dfrac{180^{\circ}}{\pi \text{ rad}}$."
                ),
                (
                    r"Multiply the radian measure by $\dfrac{180}{\pi}$. The $\pi$ "
                    "factors will cancel."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Set up the conversion: ${rad_latex} \cdot "
                    rf"\dfrac{{180^{{\circ}}}}{{\pi}}$."
                ),
                (
                    rf"Cancel $\pi$ from numerator and denominator."
                ),
                (
                    rf"Simplify: ${_format_deg(deg)}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class CoterminalAngle(Generator):
    """Given an angle, find a coterminal angle in [0, 360) degrees or [0, 2pi)
    radians. Backward: pick the target coterminal angle first, then add a
    multiple of a full rotation.
    """
    generator_id = "coterminal_angle"
    topic_slug = "angles"
    display_name = "Find a coterminal angle in the standard interval"

    _DEG_STANDARD = (0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330)
    _RAD_STANDARD = (
        (0, 1), (1, 6), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (5, 6),
        (1, 1), (7, 6), (5, 4), (4, 3), (3, 2), (5, 3), (7, 4), (11, 6),
    )
    _K_RANGES = {"easy": (1, 2), "medium": (1, 3), "hard": (1, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        use_degrees = rng.choice([True, False])
        k_lo, k_hi = self._K_RANGES[difficulty]
        k_mag = rng.randint(k_lo, k_hi)
        direction = rng.choice([-1, 1])
        k = direction * k_mag

        if use_degrees:
            target = rng.choice(self._DEG_STANDARD)
            given = target + 360 * k
            given_latex = _format_deg(given)
            answer_latex = _format_deg(target)
            full_rotation = "360^{\\circ}"
            interval = r"[0^{\circ},\ 360^{\circ})"
            unit = "degrees"
        else:
            num, den = rng.choice(self._RAD_STANDARD)
            # target radian value = num*pi/den; add k*2*pi = (2k*den)*pi/den.
            new_num = num + 2 * k * den
            given_latex = _format_pi_fraction(new_num, den)
            answer_latex = _format_pi_fraction(num, den)
            full_rotation = "2\\pi"
            interval = r"[0,\ 2\pi)"
            unit = "radians"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (use_degrees, target if use_degrees else (num, den), k),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the angle in ${interval}$ that is coterminal with "
                f"${given_latex}$ {unit}."
            ),
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    "Two angles are coterminal when they differ by a whole number of "
                    f"full rotations, ${full_rotation}$."
                ),
                (
                    f"Add or subtract ${full_rotation}$ repeatedly until the angle "
                    f"lies in ${interval}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Start with the given angle ${given_latex}$."
                ),
                (
                    f"Add or subtract multiples of ${full_rotation}$ to reach the "
                    f"interval ${interval}$."
                ),
                (
                    f"The coterminal angle in ${interval}$ is ${answer_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


# ===========================================================================
# Topic 2: circular_functions
# ===========================================================================


# Clean unit-circle points used by the circ_fn_from_unit_circle_point generator.
# Every point satisfies x^2 + y^2 = 1 and has a clean tan value (y/x).
_CLEAN_POINTS = (
    # Axis points
    ((1, 1), (0, 1)),   # (1, 0)
    ((0, 1), (1, 1)),   # (0, 1)
    ((-1, 1), (0, 1)),  # (-1, 0)
    ((0, 1), (-1, 1)),  # (0, -1)
    # 30/60 family (sqrt(3)/2, 1/2) etc. represented as ("sqrt3_over_2", "half")
)


@register
class CircFnFromUnitCirclePoint(Generator):
    """Given a point (x, y) on the unit circle, state cos(theta)=x, sin(theta)=y
    and compute tan(theta)=y/x. Backward: pick clean points.

    Points drawn from the 16 standard unit-circle terminal points.
    """
    generator_id = "circ_fn_from_unit_circle_point"
    topic_slug = "circular_functions"
    display_name = "Read sine, cosine, tangent from a unit circle point"

    # Each point is represented as (x_sym, y_sym) sympy Rationals / surds.
    _POINTS = None  # populated in __init__

    bank_count_per_difficulty = 12  # only 12 distinct non-axis clean points

    def __init__(self) -> None:
        r2 = sp.sqrt(2) / 2
        r3_2 = sp.sqrt(3) / 2
        half = sp.Rational(1, 2)
        # 12 points where tan is defined (x != 0) and all three values are clean.
        self._POINTS = (
            (r3_2, half),
            (r2, r2),
            (half, r3_2),
            (-half, r3_2),
            (-r2, r2),
            (-r3_2, half),
            (-r3_2, -half),
            (-r2, -r2),
            (-half, -r3_2),
            (half, -r3_2),
            (r2, -r2),
            (r3_2, -half),
        )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._POINTS))
        x_sym, y_sym = self._POINTS[idx]

        cos_latex = sp.latex(x_sym)
        sin_latex = sp.latex(y_sym)
        tan_val = sp.simplify(y_sym / x_sym)
        tan_latex = sp.latex(tan_val)

        point_latex = f"\\left({cos_latex},\\ {sin_latex}\\right)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"The terminal side of an angle $\\theta$ meets the unit circle at "
                f"the point ${point_latex}$. Find $\\cos\\theta$, $\\sin\\theta$, "
                "and $\\tan\\theta$."
            ),
            answer_latex=(
                f"$\\cos\\theta = {cos_latex},\\ "
                f"\\sin\\theta = {sin_latex},\\ "
                f"\\tan\\theta = {tan_latex}$"
            ),
            hints=[
                (
                    r"On the unit circle, the coordinates of a point on the terminal "
                    r"side are $(\cos\theta,\ \sin\theta)$."
                ),
                (
                    r"Once you know $\sin\theta$ and $\cos\theta$, use "
                    r"$\tan\theta = \dfrac{\sin\theta}{\cos\theta}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read the coordinates directly: $\\cos\\theta = {cos_latex}$ "
                    f"and $\\sin\\theta = {sin_latex}$."
                ),
                (
                    f"Compute $\\tan\\theta = \\dfrac{{\\sin\\theta}}{{\\cos\\theta}} "
                    f"= \\dfrac{{{sin_latex}}}{{{cos_latex}}} = {tan_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class CircFnSignInQuadrant(Generator):
    """Given a quadrant I/II/III/IV, state the signs of sin, cos, tan there.

    Multi-part answer. The parameter space is small (difficulty * quadrant),
    so bank_count_per_difficulty is capped at 20.
    """
    generator_id = "circ_fn_sign_in_quadrant"
    topic_slug = "circular_functions"
    display_name = "State the signs of sin, cos, tan in a given quadrant"

    bank_count_per_difficulty = 20

    # Quadrants: I (x>0,y>0); II (x<0,y>0); III (x<0,y<0); IV (x>0,y<0)
    _TABLE = {
        "I":   ("+", "+", "+"),
        "II":  ("+", "-", "-"),
        "III": ("-", "-", "+"),
        "IV":  ("-", "+", "-"),
    }

    _DESCRIPTIONS = {
        "I":   "positive $x$, positive $y$",
        "II":  "negative $x$, positive $y$",
        "III": "negative $x$, negative $y$",
        "IV":  "positive $x$, negative $y$",
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        quadrant = rng.choice(list(self._TABLE.keys()))
        style = rng.choice(["sin", "cos", "tan", "all"])

        sin_sign, cos_sign, tan_sign = self._TABLE[quadrant]
        x_sign = "+" if quadrant in ("I", "IV") else "-"
        y_sign = "+" if quadrant in ("I", "II") else "-"

        if style == "sin":
            target = "\\sin\\theta"
            answer = sin_sign
            reason = (
                r"$\sin\theta$ equals the $y$-coordinate of the terminal point, "
                f"and in quadrant {quadrant} the $y$-coordinate is {y_sign}."
            )
        elif style == "cos":
            target = "\\cos\\theta"
            answer = cos_sign
            reason = (
                r"$\cos\theta$ equals the $x$-coordinate of the terminal point, "
                f"and in quadrant {quadrant} the $x$-coordinate is {x_sign}."
            )
        elif style == "tan":
            target = "\\tan\\theta"
            answer = tan_sign
            reason = (
                r"$\tan\theta = y/x$, and in quadrant "
                f"{quadrant} that ratio is {tan_sign}."
            )
        else:  # all
            target = "$\\sin\\theta$, $\\cos\\theta$, and $\\tan\\theta$"
            answer = (
                f"$\\sin\\theta$: {sin_sign}; "
                f"$\\cos\\theta$: {cos_sign}; "
                f"$\\tan\\theta$: {tan_sign}"
            )
            reason = (
                f"Use the signs of $(x, y)$ in quadrant {quadrant}: "
                f"{self._DESCRIPTIONS[quadrant]}. Then apply the definitions "
                r"$\sin\theta = y$, $\cos\theta = x$, $\tan\theta = y/x$."
            )

        if style == "all":
            statement = (
                f"If $\\theta$ lies in quadrant {quadrant}, state the sign "
                f"(+ or -) of $\\sin\\theta$, $\\cos\\theta$, and $\\tan\\theta$."
            )
            answer_latex = answer
        else:
            statement = (
                f"If $\\theta$ lies in quadrant {quadrant}, is ${target}$ positive "
                "or negative?"
            )
            word = "positive" if answer == "+" else "negative"
            answer_latex = f"${target}$ is {word} (${answer}$)"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (quadrant, style)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=[
                (
                    r"Remember the mnemonic 'All Students Take Calculus' (ASTC): "
                    r"Quadrant I $\to$ all positive; II $\to$ sine; "
                    r"III $\to$ tangent; IV $\to$ cosine."
                ),
                (
                    f"In quadrant {quadrant}, the terminal point has "
                    f"{self._DESCRIPTIONS[quadrant]}."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the signs of $(x, y)$ in quadrant {quadrant}: "
                    f"{self._DESCRIPTIONS[quadrant]}."
                ),
                reason,
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class CircFnReciprocalEvaluate(Generator):
    """Given sin(theta) or cos(theta), compute the reciprocal (csc, sec, cot).

    Backward: pick clean sin/cos values on the unit circle (including
    non-axis values like 1/2, sqrt(2)/2, sqrt(3)/2). Reciprocal is formed
    by inverting and rationalising where needed.
    """
    generator_id = "circ_fn_reciprocal_evaluate"
    topic_slug = "circular_functions"
    display_name = "Compute reciprocal trig values (csc, sec, cot)"

    def __init__(self) -> None:
        half = sp.Rational(1, 2)
        r2 = sp.sqrt(2) / 2
        r3 = sp.sqrt(3) / 2
        # (symbol value, "sin" or "cos")
        self._SIN_VALUES = [half, -half, r2, -r2, r3, -r3, sp.Integer(1), sp.Integer(-1)]
        self._COS_VALUES = list(self._SIN_VALUES)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        source_fn = rng.choice(["sin", "cos"])
        values = self._SIN_VALUES if source_fn == "sin" else self._COS_VALUES
        val = rng.choice(values)

        val_latex = sp.latex(val)

        if source_fn == "sin":
            given_latex = rf"\sin\theta = {val_latex}"
            target_name = r"\csc\theta"
            target_word = "cosecant"
        else:
            given_latex = rf"\cos\theta = {val_latex}"
            target_name = r"\sec\theta"
            target_word = "secant"

        reciprocal = sp.simplify(1 / val)
        reciprocal_rat = sp.nsimplify(reciprocal, rational=False)
        reciprocal_rat = sp.simplify(sp.sqrtdenest(reciprocal_rat))
        reciprocal_latex = sp.latex(reciprocal_rat)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (source_fn, str(val))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"If ${given_latex}$, find ${target_name}$. Simplify and "
                "rationalise denominators."
            ),
            answer_latex=f"${target_name} = {reciprocal_latex}$",
            hints=[
                (
                    rf"The {target_word} function is the reciprocal of "
                    rf"{'sine' if source_fn == 'sin' else 'cosine'}: "
                    rf"${target_name} = \dfrac{{1}}{{\{'sin' if source_fn == 'sin' else 'cos'}\theta}}$."
                ),
                (
                    r"After inverting, rationalise any $\sqrt{\ }$ that appears in "
                    r"the denominator by multiplying numerator and denominator by "
                    r"the surd."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Start with ${given_latex}$."
                ),
                (
                    rf"Take the reciprocal: ${target_name} = "
                    rf"\dfrac{{1}}{{{val_latex}}}$."
                ),
                (
                    rf"Simplify: ${target_name} = {reciprocal_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


# ===========================================================================
# Topic 3: the_unit_circle
# ===========================================================================


# The 16 standard unit-circle angles: every multiple of pi/6 or pi/4 in [0, 2pi).
# Each entry: (numerator, denominator) for num*pi/denominator.
_UNIT_CIRCLE_ANGLES = (
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


def _unit_circle_cos_sin(num: int, den: int) -> tuple[sp.Expr, sp.Expr]:
    """Return (cos, sin) of the angle num*pi/den as sympy exact values."""
    angle = sp.Rational(num, den) * sp.pi
    return sp.cos(angle), sp.sin(angle)


@register
class UnitCircleExactValue(Generator):
    """Given a standard unit-circle angle, compute sin or cos exactly.

    The 16 special angles cover 0, pi/6, pi/4, pi/3, pi/2, ..., 11*pi/6.
    With two target functions (sin and cos), the parameter space is 32.
    The bank cap per request is 16 to avoid duplicate-free problems.
    """
    generator_id = "unit_circle_exact_value"
    topic_slug = "the_unit_circle"
    display_name = "Compute sin or cos of a standard unit-circle angle"

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        num, den = rng.choice(_UNIT_CIRCLE_ANGLES)
        target = rng.choice(["sin", "cos"])
        angle_latex = _format_pi_fraction(num, den)

        cos_val, sin_val = _unit_circle_cos_sin(num, den)
        val = sin_val if target == "sin" else cos_val
        val_latex = sp.latex(sp.simplify(val))

        fn_latex = f"\\{target}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (num, den, target)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Compute the exact value of ${fn_latex}\\!\\left({angle_latex}\\right)$."
            ),
            answer_latex=f"${fn_latex}\\!\\left({angle_latex}\\right) = {val_latex}$",
            hints=[
                (
                    f"Locate the angle ${angle_latex}$ on the unit circle. Its "
                    r"terminal point has coordinates $(\cos\theta,\ \sin\theta)$."
                ),
                (
                    f"Read off the "
                    f"{'y' if target == 'sin' else 'x'}"
                    f"-coordinate of the terminal point."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The angle ${angle_latex}$ corresponds to a standard point on "
                    "the unit circle."
                ),
                (
                    f"Its terminal point is $(\\cos\\theta,\\ \\sin\\theta) = "
                    f"({sp.latex(cos_val)},\\ {sp.latex(sin_val)})$."
                ),
                (
                    f"Therefore ${fn_latex}\\!\\left({angle_latex}\\right) = {val_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class UnitCircleReferenceAngle(Generator):
    """Given an angle in any quadrant, find its reference angle.

    The reference angle is the acute positive angle from the terminal side to
    the nearest x-axis. Backward: pick an angle from the standard 16, then
    compute its reference via quadrant rules.
    """
    generator_id = "unit_circle_reference_angle"
    topic_slug = "the_unit_circle"
    display_name = "Find the reference angle of a standard angle"

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Pick angle from the 16 standard angles; at medium and hard we may
        # also use angles outside [0, 2pi) to require coterminal reduction.
        if difficulty == "easy":
            num, den = rng.choice(_UNIT_CIRCLE_ANGLES)
            shift_k = 0
        elif difficulty == "medium":
            num, den = rng.choice(_UNIT_CIRCLE_ANGLES)
            shift_k = rng.choice([-1, 0, 0, 1])
        else:
            num, den = rng.choice(_UNIT_CIRCLE_ANGLES)
            shift_k = rng.choice([-2, -1, 0, 1, 2])

        given_num = num + 2 * shift_k * den  # add full rotations
        given_latex = _format_pi_fraction(given_num, den)

        # Compute reference angle as num*pi/den reduced into [0, 2pi), then
        # mapped into [0, pi/2].
        reduced_num = num % (2 * den)
        q_den = den
        # Determine quadrant for reduced angle
        # angle = reduced_num * pi / q_den
        # Quadrant I: 0 <= reduced_num * pi / q_den < pi/2  -> reduced_num * 2 < q_den
        # Quadrant II: pi/2 <= angle < pi
        # Quadrant III: pi <= angle < 3pi/2
        # Quadrant IV: 3pi/2 <= angle < 2pi
        a2 = reduced_num * 2  # so angle = (a2 / (2*q_den)) * pi
        if a2 < q_den:  # Quadrant I
            ref_num = reduced_num
            ref_den = q_den
            quadrant = 1
        elif a2 < 2 * q_den:  # Quadrant II: ref = pi - angle = (q_den - reduced_num) * pi / q_den
            # (q_den - reduced_num) may be expressed over q_den; reduce via common gcd later.
            ref_num = q_den - reduced_num
            ref_den = q_den
            quadrant = 2
        elif a2 < 3 * q_den:  # Quadrant III: ref = angle - pi
            ref_num = reduced_num - q_den
            ref_den = q_den
            quadrant = 3
        else:  # Quadrant IV: ref = 2*pi - angle
            ref_num = 2 * q_den - reduced_num
            ref_den = q_den
            quadrant = 4

        ref_latex = _format_pi_fraction(ref_num, ref_den)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (num, den, shift_k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the reference angle of ${given_latex}$."
            ),
            answer_latex=f"${ref_latex}$",
            hints=[
                (
                    r"First, if the angle is outside $[0,\ 2\pi)$, add or subtract "
                    r"$2\pi$ until it lies in that interval."
                ),
                (
                    r"Then compute the acute positive angle between the terminal side "
                    r"and the nearest part of the $x$-axis."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Reduce ${given_latex}$ to an angle in $[0,\\ 2\\pi)$: "
                    f"${_format_pi_fraction(reduced_num, q_den)}$."
                ),
                (
                    f"This angle is in quadrant {quadrant}."
                ),
                (
                    f"The reference angle is ${ref_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class UnitCircleCoordinateFromAngle(Generator):
    """Given one of the 16 special angles, state the (x, y) terminal point
    on the unit circle.
    """
    generator_id = "unit_circle_coordinate_from_angle"
    topic_slug = "the_unit_circle"
    display_name = "State the (x, y) terminal point for a standard angle"

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        num, den = rng.choice(_UNIT_CIRCLE_ANGLES)
        angle_latex = _format_pi_fraction(num, den)
        cos_val, sin_val = _unit_circle_cos_sin(num, den)

        cos_latex = sp.latex(cos_val)
        sin_latex = sp.latex(sin_val)
        point_latex = f"\\left({cos_latex},\\ {sin_latex}\\right)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (num, den)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"What are the coordinates of the point where the terminal side of "
                f"the angle ${angle_latex}$ meets the unit circle?"
            ),
            answer_latex=f"${point_latex}$",
            hints=[
                (
                    r"On the unit circle, the terminal point for angle $\theta$ is "
                    r"$(\cos\theta,\ \sin\theta)$."
                ),
                (
                    f"Use the standard value table for multiples of $\\pi/6$ and "
                    r"$\pi/4$ to look up the coordinates."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the angle ${angle_latex}$ on the unit circle."
                ),
                (
                    f"Read the terminal coordinates: $\\cos\\theta = {cos_latex}$ "
                    f"and $\\sin\\theta = {sin_latex}$."
                ),
                (
                    f"The terminal point is ${point_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


# ===========================================================================
# Topic 4: inverse_trigonometric_functions
# ===========================================================================


# Standard inverse-trig "clean" values. Each entry is (sympy input value,
# answer as (num, den) for num*pi/den).
_ARCSIN_TABLE = (
    (sp.Integer(-1),          (-1, 2)),   # arcsin(-1) = -pi/2
    (-sp.sqrt(3) / 2,          (-1, 3)),   # arcsin(-sqrt(3)/2) = -pi/3
    (-sp.sqrt(2) / 2,          (-1, 4)),   # arcsin(-sqrt(2)/2) = -pi/4
    (-sp.Rational(1, 2),       (-1, 6)),   # arcsin(-1/2) = -pi/6
    (sp.Integer(0),            (0, 1)),    # arcsin(0) = 0
    (sp.Rational(1, 2),        (1, 6)),    # arcsin(1/2) = pi/6
    (sp.sqrt(2) / 2,           (1, 4)),    # arcsin(sqrt(2)/2) = pi/4
    (sp.sqrt(3) / 2,           (1, 3)),    # arcsin(sqrt(3)/2) = pi/3
    (sp.Integer(1),            (1, 2)),    # arcsin(1) = pi/2
)

_ARCCOS_TABLE = (
    (sp.Integer(1),            (0, 1)),    # arccos(1) = 0
    (sp.sqrt(3) / 2,           (1, 6)),    # arccos(sqrt(3)/2) = pi/6
    (sp.sqrt(2) / 2,           (1, 4)),    # arccos(sqrt(2)/2) = pi/4
    (sp.Rational(1, 2),        (1, 3)),    # arccos(1/2) = pi/3
    (sp.Integer(0),            (1, 2)),    # arccos(0) = pi/2
    (-sp.Rational(1, 2),       (2, 3)),    # arccos(-1/2) = 2pi/3
    (-sp.sqrt(2) / 2,          (3, 4)),    # arccos(-sqrt(2)/2) = 3pi/4
    (-sp.sqrt(3) / 2,          (5, 6)),    # arccos(-sqrt(3)/2) = 5pi/6
    (sp.Integer(-1),           (1, 1)),    # arccos(-1) = pi
)

_ARCTAN_TABLE = (
    (-sp.sqrt(3),              (-1, 3)),   # arctan(-sqrt(3)) = -pi/3
    (-sp.Integer(1),           (-1, 4)),   # arctan(-1) = -pi/4
    (-sp.sqrt(3) / 3,          (-1, 6)),   # arctan(-sqrt(3)/3) = -pi/6
    (sp.Integer(0),            (0, 1)),    # arctan(0) = 0
    (sp.sqrt(3) / 3,           (1, 6)),    # arctan(sqrt(3)/3) = pi/6
    (sp.Integer(1),            (1, 4)),    # arctan(1) = pi/4
    (sp.sqrt(3),               (1, 3)),    # arctan(sqrt(3)) = pi/3
)


def _inverse_trig_problem(
    gen_id: str,
    topic_slug: str,
    display_name: str,
    fn_name: str,           # 'sin^{-1}' or 'cos^{-1}' or 'tan^{-1}'
    fn_word: str,           # 'inverse sine', etc.
    base_fn: str,           # 'sin', 'cos', 'tan'
    table: tuple,
    range_latex: str,
    difficulty: Difficulty,
    rng: random.Random,
) -> Problem:
    """Build a single inverse-trig evaluation problem from a table entry.

    Separated out so arcsin/arccos/arctan generators share identical logic.
    """
    idx = rng.randrange(len(table))
    val, (ans_num, ans_den) = table[idx]
    val_latex = sp.latex(val)
    answer_latex = _format_pi_fraction(ans_num, ans_den)

    statement = (
        f"Find the exact value of ${fn_name}\\!\\left({val_latex}\\right)$. "
        f"Give your answer in the range ${range_latex}$."
    )

    return Problem(
        id=make_problem_id(gen_id, difficulty, (idx,)),
        generator_id=gen_id,
        topic_slug=topic_slug,
        difficulty=difficulty,
        statement_latex=statement,
        answer_latex=f"${fn_name}\\!\\left({val_latex}\\right) = {answer_latex}$",
        hints=[
            (
                f"${fn_name}(x) = \\theta$ means $\\{base_fn}\\theta = x$, with "
                f"$\\theta$ restricted to the principal range ${range_latex}$."
            ),
            (
                f"Find the angle in ${range_latex}$ whose {fn_word.split()[-1]} "
                f"equals ${val_latex}$."
            ),
        ],
        solution_steps_latex=[
            (
                f"Let $\\theta = {fn_name}\\!\\left({val_latex}\\right)$. Then "
                f"$\\{base_fn}\\theta = {val_latex}$."
            ),
            (
                f"The angle in ${range_latex}$ with this {base_fn} value is "
                f"$\\theta = {answer_latex}$."
            ),
            (
                f"Therefore ${fn_name}\\!\\left({val_latex}\\right) = {answer_latex}$."
            ),
        ],
        tags=["#branch-pre-calculus", "#topic-unit-circle"],
    )


@register
class ArcsinExactValue(Generator):
    """Evaluate arcsin at a clean value. Principal range [-pi/2, pi/2]."""
    generator_id = "arcsin_exact_value"
    topic_slug = "inverse_trigonometric_functions"
    display_name = "Evaluate arcsin at an exact value"

    # Table has 9 entries; the tight range limits the parameter space.
    bank_count_per_difficulty = 9

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        return _inverse_trig_problem(
            gen_id=self.generator_id,
            topic_slug=self.topic_slug,
            display_name=self.display_name,
            fn_name=r"\sin^{-1}",
            fn_word="inverse sine",
            base_fn="sin",
            table=_ARCSIN_TABLE,
            range_latex=r"\left[-\dfrac{\pi}{2},\ \dfrac{\pi}{2}\right]",
            difficulty=difficulty,
            rng=rng,
        )


@register
class ArccosExactValue(Generator):
    """Evaluate arccos at a clean value. Principal range [0, pi]."""
    generator_id = "arccos_exact_value"
    topic_slug = "inverse_trigonometric_functions"
    display_name = "Evaluate arccos at an exact value"

    # Table has 9 entries; the tight range limits the parameter space.
    bank_count_per_difficulty = 9

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        return _inverse_trig_problem(
            gen_id=self.generator_id,
            topic_slug=self.topic_slug,
            display_name=self.display_name,
            fn_name=r"\cos^{-1}",
            fn_word="inverse cosine",
            base_fn="cos",
            table=_ARCCOS_TABLE,
            range_latex=r"\left[0,\ \pi\right]",
            difficulty=difficulty,
            rng=rng,
        )


@register
class ArctanExactValue(Generator):
    """Evaluate arctan at a clean value. Principal range (-pi/2, pi/2)."""
    generator_id = "arctan_exact_value"
    topic_slug = "inverse_trigonometric_functions"
    display_name = "Evaluate arctan at an exact value"

    # Table has 7 entries; arctan has no clean values beyond these.
    bank_count_per_difficulty = 7

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        return _inverse_trig_problem(
            gen_id=self.generator_id,
            topic_slug=self.topic_slug,
            display_name=self.display_name,
            fn_name=r"\tan^{-1}",
            fn_word="inverse tangent",
            base_fn="tan",
            table=_ARCTAN_TABLE,
            range_latex=r"\left(-\dfrac{\pi}{2},\ \dfrac{\pi}{2}\right)",
            difficulty=difficulty,
            rng=rng,
        )


# ===========================================================================
# Topic 5: graphs_of_trigonometric_functions
# ===========================================================================


@register
class TrigPeriodAmplitude(Generator):
    """Given y = A * sin(B*x) or y = A * cos(B*x), state amplitude and period.

    Amplitude = |A|; period = 2*pi / |B|. Backward: pick integer A and
    integer B (or simple fraction), so period is a clean multiple of pi.
    """
    generator_id = "trig_period_amplitude"
    topic_slug = "graphs_of_trigonometric_functions"
    display_name = "Find amplitude and period of y = A sin(Bx) or A cos(Bx)"

    _A_CHOICES = {
        "easy": (1, 2, 3, 4, 5),
        "medium": (-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6),
        "hard": (-7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8),
    }
    _B_CHOICES = {
        "easy": (1, 2, 3),
        "medium": (1, 2, 3, 4, 6),
        "hard": (1, 2, 3, 4, 5, 6, 8),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A = rng.choice(self._A_CHOICES[difficulty])
        B = rng.choice(self._B_CHOICES[difficulty])
        fn = rng.choice(["sin", "cos"])

        # Build function string
        if A == 1:
            a_str = ""
        elif A == -1:
            a_str = "-"
        else:
            a_str = str(A)
        if B == 1:
            bx_str = "x"
        else:
            bx_str = f"{B}x"
        fn_latex = f"y = {a_str}\\{fn}\\!\\left({bx_str}\\right)"

        amplitude = abs(A)
        period_num, period_den = 2, B
        period_latex = _format_pi_fraction(period_num, period_den)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, B, fn)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the function ${fn_latex}$, state the amplitude and the period."
            ),
            answer_latex=(
                f"Amplitude $= {amplitude}$; period $= {period_latex}$"
            ),
            hints=[
                (
                    r"For $y = A\sin(Bx)$ or $y = A\cos(Bx)$, the amplitude is $|A|$ "
                    r"and the period is $\dfrac{2\pi}{|B|}$."
                ),
                (
                    f"Here $A = {A}$ and $B = {B}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read the coefficients from ${fn_latex}$: $A = {A}$, $B = {B}$."
                ),
                (
                    f"Amplitude $= |A| = |{A}| = {amplitude}$."
                ),
                (
                    f"Period $= \\dfrac{{2\\pi}}{{|B|}} = \\dfrac{{2\\pi}}{{{B}}} = "
                    f"{period_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class TrigGraphIntercepts(Generator):
    """Find the x-intercepts of y = A sin(Bx) or A cos(Bx) in [0, 2pi].

    Backward: pick B small so the intercepts are clean multiples of pi. A
    is included in the parameter tuple to expand the pool (intercepts are
    independent of A, but each (A, B, fn) still yields a visually distinct
    problem statement).
    """
    generator_id = "trig_graph_intercepts"
    topic_slug = "graphs_of_trigonometric_functions"
    display_name = "Find x-intercepts of a basic sinusoid in [0, 2pi]"

    _A_CHOICES = {
        "easy": (1, 2, 3, 4),
        "medium": (1, 2, 3, 4, 5, 6),
        "hard": (1, 2, 3, 4, 5, 6, 7, 8),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        if difficulty == "easy":
            B = rng.choice((1, 2))
        elif difficulty == "medium":
            B = rng.choice((1, 2, 3))
        else:
            B = rng.choice((1, 2, 3, 4))
        A = rng.choice(self._A_CHOICES[difficulty])
        fn = rng.choice(["sin", "cos"])

        # sin(Bx) = 0 when Bx = k*pi -> x = k*pi/B. Collect x in [0, 2pi].
        # cos(Bx) = 0 when Bx = (2k+1)*pi/2 -> x = (2k+1)*pi/(2B). Collect x in [0, 2pi].
        intercepts_frac: list[tuple[int, int]] = []
        if fn == "sin":
            k = 0
            while True:
                num, den = k, B  # k*pi/B
                # check if k*pi/B <= 2*pi, i.e. k/B <= 2, i.e. k <= 2B
                if k > 2 * B:
                    break
                intercepts_frac.append((num, den))
                k += 1
        else:
            k = 0
            while True:
                num, den = 2 * k + 1, 2 * B  # (2k+1)*pi/(2B)
                # check <= 2*pi -> (2k+1)/(2B) <= 2 -> 2k+1 <= 4B -> k <= (4B-1)/2
                if 2 * k + 1 > 4 * B:
                    break
                intercepts_frac.append((num, den))
                k += 1

        # Limit to at most 5 intercepts so the problem reads cleanly.
        intercepts_frac = intercepts_frac[:5]
        formatted = [_format_pi_fraction(n, d) for (n, d) in intercepts_frac]
        intercept_list_latex = ",\\ ".join(f"x = {s}" for s in formatted)

        if B == 1:
            bx = "x"
        else:
            bx = f"{B}x"
        if A == 1:
            a_str = ""
        elif A == -1:
            a_str = "-"
        else:
            a_str = str(A)
        fn_latex = f"y = {a_str}\\{fn}\\!\\left({bx}\\right)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, B, fn)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find all $x$-intercepts of ${fn_latex}$ on the interval "
                r"$[0,\ 2\pi]$."
            ),
            answer_latex=f"${intercept_list_latex}$",
            hints=[
                (
                    r"An $x$-intercept occurs where $y = 0$. "
                    f"Set $\\{fn}\\!\\left({bx}\\right) = 0$ and solve for $x$."
                ),
                (
                    r"Remember that $\sin\theta = 0$ at $\theta = 0,\ \pi,\ 2\pi,\dots$ "
                    r"and $\cos\theta = 0$ at $\theta = \dfrac{\pi}{2},\ "
                    r"\dfrac{3\pi}{2},\dots$"
                ),
            ],
            solution_steps_latex=[
                (
                    f"Set $\\{fn}\\!\\left({bx}\\right) = 0$."
                ),
                (
                    f"Solve for $x$ in the interval $[0,\\ 2\\pi]$."
                ),
                (
                    f"The intercepts are ${intercept_list_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )


@register
class TrigIdentifyFunctionFromFeatures(Generator):
    """Given a verbal description (amplitude, period, phase, initial behaviour),
    identify the matching function from a small template list.
    """
    generator_id = "trig_identify_function_from_features"
    topic_slug = "graphs_of_trigonometric_functions"
    display_name = "Identify a trig function from its amplitude, period, and initial behaviour"

    bank_count_per_difficulty = 18

    # Each template: (A, B, fn, description tuple).
    # description: (amplitude, period_num, period_den, passes_origin, behaviour_at_origin)
    _TEMPLATES = (
        (1, 1, "sin", "amplitude $1$, period $2\\pi$, passes through the origin, increasing at $x = 0$"),
        (1, 1, "cos", "amplitude $1$, period $2\\pi$, passes through $(0,\\ 1)$"),
        (2, 1, "sin", "amplitude $2$, period $2\\pi$, passes through the origin, increasing at $x = 0$"),
        (2, 1, "cos", "amplitude $2$, period $2\\pi$, passes through $(0,\\ 2)$"),
        (3, 1, "sin", "amplitude $3$, period $2\\pi$, passes through the origin, increasing at $x = 0$"),
        (3, 2, "sin", "amplitude $3$, period $\\pi$, passes through the origin, increasing at $x = 0$"),
        (1, 2, "sin", "amplitude $1$, period $\\pi$, passes through the origin, increasing at $x = 0$"),
        (1, 2, "cos", "amplitude $1$, period $\\pi$, passes through $(0,\\ 1)$"),
        (4, 1, "cos", "amplitude $4$, period $2\\pi$, passes through $(0,\\ 4)$"),
        (5, 2, "sin", "amplitude $5$, period $\\pi$, passes through the origin, increasing at $x = 0$"),
        (1, 3, "sin", "amplitude $1$, period $\\dfrac{2\\pi}{3}$, passes through the origin, increasing at $x = 0$"),
        (2, 3, "cos", "amplitude $2$, period $\\dfrac{2\\pi}{3}$, passes through $(0,\\ 2)$"),
        (-1, 1, "sin", "amplitude $1$, period $2\\pi$, passes through the origin, decreasing at $x = 0$"),
        (-2, 1, "cos", "amplitude $2$, period $2\\pi$, passes through $(0,\\ -2)$"),
        (1, 4, "sin", "amplitude $1$, period $\\dfrac{\\pi}{2}$, passes through the origin, increasing at $x = 0$"),
        (3, 4, "cos", "amplitude $3$, period $\\dfrac{\\pi}{2}$, passes through $(0,\\ 3)$"),
        (2, 2, "cos", "amplitude $2$, period $\\pi$, passes through $(0,\\ 2)$"),
        (1, 6, "sin", "amplitude $1$, period $\\dfrac{\\pi}{3}$, passes through the origin, increasing at $x = 0$"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._TEMPLATES))
        A, B, fn, description = self._TEMPLATES[idx]

        if A == 1:
            a_str = ""
        elif A == -1:
            a_str = "-"
        else:
            a_str = str(A)
        if B == 1:
            bx_str = "x"
        else:
            bx_str = f"{B}x"
        fn_latex = f"y = {a_str}\\{fn}\\!\\left({bx_str}\\right)"

        period_latex = _format_pi_fraction(2, B)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A sinusoidal function has {description}. Write the function."
            ),
            answer_latex=f"${fn_latex}$",
            hints=[
                (
                    r"Use the template $y = A\sin(Bx)$ or $y = A\cos(Bx)$. Amplitude "
                    r"gives $|A|$; period gives $B$ via $B = \dfrac{2\pi}{\text{period}}$."
                ),
                (
                    r"Behaviour at $x = 0$ distinguishes sine from cosine: sine passes "
                    r"through the origin; cosine passes through $(0,\ A)$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Choose the base function: "
                    f"{'sine (passes through origin)' if fn == 'sin' else 'cosine (passes through (0, A))'}."
                ),
                (
                    f"Set $|A| = {abs(A)}$ from the stated amplitude, with sign "
                    f"determined by the behaviour at $x = 0$: $A = {A}$."
                ),
                (
                    f"Compute $B$ from the period: "
                    f"$\\dfrac{{2\\pi}}{{B}} = {period_latex}$ gives $B = {B}$."
                ),
                (
                    f"The function is ${fn_latex}$."
                ),
            ],
            tags=["#branch-pre-calculus", "#topic-unit-circle"],
        )
