"""Advanced-functions generators (Phase 2c Cluster — transformations II,
rational graphs, exotic, and intro rationals).

Five topic slugs covered, 3 generators each (15 total):

- transformations_ii_stretches_compressions_and_combined
- graphing_rational_functions_part_1
- graphing_rational_functions_part_2
- more_exotic_functions
- introduction_to_rational_functions (pre-calculus branch)

All generators use backward construction: pick clean parameters first,
then render the statement. Rational-function generators choose the
asymptotes or holes up front and assemble the function around them,
guaranteeing integer outputs and tidy factorings.
"""
from __future__ import annotations

import random
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared tag bundles
# ---------------------------------------------------------------------------


ALG2_TRANSFORM_TAGS = [
    "#branch-algebra-2",
    "#topic-functions",
    "#topic-transformations",
]

ALG2_RATIONAL_TAGS = [
    "#branch-algebra-2",
    "#topic-functions",
    "#topic-rational-expressions",
]

ALG2_EXOTIC_TAGS = [
    "#branch-algebra-2",
    "#topic-functions",
]

PRECALC_RATIONAL_TAGS = [
    "#branch-pre-calculus",
    "#topic-functions",
    "#topic-rational-expressions",
]


# ---------------------------------------------------------------------------
# Shared formatting helpers
# ---------------------------------------------------------------------------


def _signed_paren(n: int) -> str:
    """Wrap a negative integer in parentheses so it reads well after an op."""
    return f"({n})" if n < 0 else str(n)


def _format_linear(var: str, h: int) -> str:
    """Render (var - h) with clean signs: '(x - 3)', '(x + 2)', or 'x'."""
    if h == 0:
        return var
    if h > 0:
        return f"({var} - {h})"
    return f"({var} + {-h})"


def _format_linear_body(var: str, h: int) -> str:
    """Render 'var - h' (no outer parens). Returns bare 'x' if h == 0."""
    if h == 0:
        return var
    if h > 0:
        return f"{var} - {h}"
    return f"{var} + {-h}"


def _format_trailing_const(k: int) -> str:
    """Render a trailing '+ k' term, handling sign and zero."""
    if k == 0:
        return ""
    if k > 0:
        return f" + {k}"
    return f" - {-k}"


def _format_a_coef(a: int) -> str:
    """Render a leading coefficient, hiding 1 and -1."""
    if a == 1:
        return ""
    if a == -1:
        return "-"
    return str(a)


# ===========================================================================
# Topic 1: transformations_ii_stretches_compressions_and_combined
# ===========================================================================


@register
class VerticalStretchCompressClassify(Generator):
    """Classify g(x) = a*f(x) as a vertical stretch or compression, plus
    reflection status.

    Backward: pick a as a nonzero rational (integer or 1/integer) so the
    classification is unambiguous. |a| > 1 => stretch; 0 < |a| < 1 =>
    compression; a < 0 adds a reflection across the x-axis.
    """
    generator_id = "vertical_stretch_compress_classify"
    topic_slug = "transformations_ii_stretches_compressions_and_combined"
    display_name = "Classify g(x) = a*f(x) as vertical stretch or compression"
    # Parameter space is small (2 categories x 2 reflections x a few mags).
    bank_count_per_difficulty = 20

    # For stretches: a is an integer with |a| >= 2.
    # For compressions: a = 1/d for integer d >= 2.
    _STRETCH_MAGS = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    }
    _COMPRESS_DENS = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Pick category first (backward construction).
        kind = rng.choice(["stretch", "compress"])
        reflect = rng.choice([True, False])

        if kind == "stretch":
            mag = rng.choice(self._STRETCH_MAGS[difficulty])
            a_num = mag
            a_den = 1
            a_latex = f"-{mag}" if reflect else str(mag)
            factor_phrase = f"factor of ${mag}$"
            classification_core = f"vertical stretch by a factor of ${mag}$"
            magnitude_gt_1_phrase = (
                rf"$|a| = {mag} > 1$, so the transformation is a **vertical stretch**."
            )
        else:
            den = rng.choice(self._COMPRESS_DENS[difficulty])
            a_num = 1
            a_den = den
            a_latex = rf"-\frac{{1}}{{{den}}}" if reflect else rf"\frac{{1}}{{{den}}}"
            factor_phrase = rf"factor of $\frac{{1}}{{{den}}}$"
            classification_core = (
                rf"vertical compression by a factor of $\frac{{1}}{{{den}}}$"
            )
            magnitude_gt_1_phrase = (
                rf"$|a| = \frac{{1}}{{{den}}} < 1$, so the transformation is a "
                r"**vertical compression**."
            )

        if reflect:
            reflection_phrase = "yes (reflection across the x-axis because $a < 0$)"
            full_answer = (
                f"{classification_core}; reflection across the x-axis."
            )
        else:
            reflection_phrase = "no"
            full_answer = f"{classification_core}; no reflection."

        # Build a display string for g(x).
        g_latex = f"g(x) = {a_latex} f(x)"
        # Unique param tuple for deterministic ids.
        params = (a_num, a_den, 1 if reflect else 0)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${g_latex}$, classify the transformation applied to "
                f"$f(x)$. Is it a vertical stretch or compression, and is "
                f"there a reflection across the x-axis?"
            ),
            answer_latex=full_answer,
            hints=[
                r"Compare $g(x) = a \cdot f(x)$ with the parent $f(x)$. The constant $a$ acts vertically.",
                r"If $|a| > 1$ the graph stretches vertically; if $0 < |a| < 1$ it compresses.",
                "A negative value of $a$ flips the graph across the x-axis on top of the stretch/compression.",
            ],
            solution_steps_latex=[
                rf"Identify the vertical factor: $a = {a_latex}$.",
                magnitude_gt_1_phrase,
                (
                    "Since $a < 0$, the graph is also reflected across the x-axis."
                    if reflect
                    else "Since $a > 0$, there is no reflection."
                ),
                f"Final classification: {classification_core} with a {factor_phrase}, reflection: {reflection_phrase}.",
            ],
            tags=list(ALG2_TRANSFORM_TAGS),
        )


@register
class HorizontalStretchCompressClassify(Generator):
    """Classify g(x) = f(bx) as a horizontal stretch or compression, plus
    reflection status.

    Backward: pick b as a nonzero rational. |b| > 1 => horizontal
    compression by 1/|b|; 0 < |b| < 1 => horizontal stretch by 1/|b|;
    b < 0 adds a reflection across the y-axis.
    """
    generator_id = "horizontal_stretch_compress_classify"
    topic_slug = "transformations_ii_stretches_compressions_and_combined"
    display_name = "Classify g(x) = f(bx) as horizontal stretch or compression"
    # Parameter space is small (2 categories x 2 reflections x a few mags).
    bank_count_per_difficulty = 20

    _INT_MAGS = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    }
    _FRAC_DENS = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        kind = rng.choice(["compress", "stretch"])  # horizontal
        reflect = rng.choice([True, False])

        if kind == "compress":
            # |b| > 1 => horizontal compression by factor 1/|b|.
            mag = rng.choice(self._INT_MAGS[difficulty])
            b_num = mag
            b_den = 1
            b_latex = f"-{mag}" if reflect else str(mag)
            factor_latex = rf"\frac{{1}}{{{mag}}}"
            classification_core = (
                rf"horizontal compression by a factor of $\frac{{1}}{{{mag}}}$"
            )
            magnitude_phrase = (
                rf"$|b| = {mag} > 1$, so the transformation is a "
                r"**horizontal compression**."
            )
        else:
            # |b| < 1 => horizontal stretch by factor 1/|b| = den.
            den = rng.choice(self._FRAC_DENS[difficulty])
            b_num = 1
            b_den = den
            b_latex = rf"-\frac{{1}}{{{den}}}" if reflect else rf"\frac{{1}}{{{den}}}"
            factor_latex = str(den)
            classification_core = (
                f"horizontal stretch by a factor of ${den}$"
            )
            magnitude_phrase = (
                rf"$|b| = \frac{{1}}{{{den}}} < 1$, so the transformation is a "
                r"**horizontal stretch**."
            )

        if reflect:
            reflection_line = (
                "Since $b < 0$, the graph is also reflected across the y-axis."
            )
            full_answer = (
                f"{classification_core}; reflection across the y-axis."
            )
        else:
            reflection_line = "Since $b > 0$, there is no reflection."
            full_answer = f"{classification_core}; no reflection."

        g_latex = f"g(x) = f({b_latex} x)"
        params = (b_num, b_den, 1 if reflect else 0)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${g_latex}$, classify the transformation applied to "
                f"$f(x)$. Is it a horizontal stretch or compression, and is "
                f"there a reflection across the y-axis?"
            ),
            answer_latex=full_answer,
            hints=[
                r"Compare $g(x) = f(bx)$ with the parent $f(x)$. The constant $b$ acts horizontally but **opposite** to what it looks like.",
                r"If $|b| > 1$ the graph is compressed horizontally by $\frac{1}{|b|}$; if $0 < |b| < 1$ it is stretched by $\frac{1}{|b|}$.",
                "A negative value of $b$ flips the graph across the y-axis on top of the stretch/compression.",
            ],
            solution_steps_latex=[
                rf"Identify the horizontal factor: $b = {b_latex}$.",
                magnitude_phrase,
                rf"The horizontal factor is $\frac{{1}}{{|b|}} = {factor_latex}$.",
                reflection_line,
                f"Final classification: {classification_core}.",
            ],
            tags=list(ALG2_TRANSFORM_TAGS),
        )


@register
class CombinedTransformationParabola(Generator):
    """Describe all four transformations taking f(x) = x^2 to
    g(x) = a(x - h)^2 + k.

    Backward: pick a in a small set (including negatives for reflection
    and fractions for compression), then pick integer h and k. Describe
    (1) horizontal shift, (2) vertical stretch/compression, (3) reflection
    across the x-axis, (4) vertical shift.
    """
    generator_id = "combined_transformation_parabola"
    topic_slug = "transformations_ii_stretches_compressions_and_combined"
    display_name = "Describe all transformations from f(x) = x^2 to a(x - h)^2 + k"

    # Choices include integers (stretches) and fraction markers (compressions).
    # Each choice is stored as (num, den, sign) where the actual value is
    # sign * num / den. sign in {1, -1}.
    _A_CHOICES = {
        "easy": [
            (2, 1, 1), (2, 1, -1), (3, 1, 1), (3, 1, -1),
            (1, 2, 1), (1, 2, -1), (1, 3, 1), (1, 3, -1),
        ],
        "medium": [
            (2, 1, 1), (2, 1, -1), (3, 1, 1), (3, 1, -1),
            (4, 1, 1), (4, 1, -1), (5, 1, 1), (5, 1, -1),
            (1, 2, 1), (1, 2, -1), (1, 3, 1), (1, 3, -1),
            (1, 4, 1), (1, 4, -1),
        ],
        "hard": [
            (2, 1, 1), (2, 1, -1), (3, 1, 1), (3, 1, -1),
            (4, 1, 1), (4, 1, -1), (5, 1, 1), (5, 1, -1),
            (6, 1, 1), (6, 1, -1), (7, 1, 1), (7, 1, -1),
            (1, 2, 1), (1, 2, -1), (1, 3, 1), (1, 3, -1),
            (1, 4, 1), (1, 4, -1), (1, 5, 1), (1, 5, -1),
        ],
    }
    _H_RANGES = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-10, 10)}
    _K_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_num, a_den, sign = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        # Avoid degenerate no-shift case so all four pieces are interesting.
        if h == 0 and k == 0:
            h = rng.choice([-2, -1, 1, 2])

        # Build the LaTeX for a.
        if a_den == 1:
            a_latex = f"-{a_num}" if sign < 0 else str(a_num)
            a_abs_latex = str(a_num)
        else:
            if sign < 0:
                a_latex = rf"-\frac{{{a_num}}}{{{a_den}}}"
            else:
                a_latex = rf"\frac{{{a_num}}}{{{a_den}}}"
            a_abs_latex = rf"\frac{{{a_num}}}{{{a_den}}}"

        # Build the function LaTeX: a(x - h)^2 + k.
        inside = _format_linear("x", h)
        if a_den == 1 and a_num == 1:
            body_core = f"{inside}^2"
        else:
            body_core = rf"{a_latex}{inside}^2"
        if sign < 0 and a_num == 1 and a_den == 1:
            body_core = f"-{inside}^2"
        func_latex = f"g(x) = {body_core}{_format_trailing_const(k)}"

        # Classify |a| vs 1.
        # |a| = a_num / a_den; compare to 1.
        is_stretch = a_num * 1 > a_den  # a_num/a_den > 1
        is_compress = a_num * 1 < a_den  # a_num/a_den < 1
        # (With a_num >= 1 and a_den >= 1, they can't be equal given our lists.)
        if is_stretch:
            vert_kind_phrase = (
                f"vertical stretch by a factor of ${a_abs_latex}$"
            )
        elif is_compress:
            vert_kind_phrase = (
                f"vertical compression by a factor of ${a_abs_latex}$"
            )
        else:
            vert_kind_phrase = "no vertical stretch or compression"

        # Horizontal shift description.
        if h == 0:
            h_desc = "no horizontal shift"
        elif h > 0:
            h_desc = f"horizontal shift {h} units to the right"
        else:
            h_desc = f"horizontal shift {-h} units to the left"

        # Vertical shift description.
        if k == 0:
            k_desc = "no vertical shift"
        elif k > 0:
            k_desc = f"vertical shift {k} units upward"
        else:
            k_desc = f"vertical shift {-k} units downward"

        # Reflection description.
        if sign < 0:
            reflect_desc = "reflection across the x-axis"
        else:
            reflect_desc = "no reflection"

        full_answer = (
            f"(1) {h_desc}; (2) {vert_kind_phrase}; "
            f"(3) {reflect_desc}; (4) {k_desc}."
        )

        params = (a_num, a_den, sign, h, k)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe all of the transformations that take $f(x) = x^2$ "
                f"to ${func_latex}$. Give (1) the horizontal shift, "
                f"(2) the vertical stretch or compression, (3) any "
                f"reflection, and (4) the vertical shift."
            ),
            answer_latex=full_answer,
            hints=[
                r"The general vertex form is $g(x) = a(x - h)^2 + k$ where $h$, $k$ shift the graph and $a$ controls vertical stretch/compression and reflection.",
                r"Compare term by term with the parent $f(x) = x^2$.",
                f"Read off $a = {a_latex}$, $h = {h}$, $k = {k}$ from the expression.",
            ],
            solution_steps_latex=[
                (
                    r"Match the given function against the template "
                    r"$g(x) = a(x - h)^2 + k$."
                ),
                rf"Read off $a = {a_latex}$, $h = {h}$, and $k = {k}$.",
                f"(1) Horizontal: {h_desc} because $h = {h}$.",
                f"(2) Vertical size: {vert_kind_phrase} because $|a| = {a_abs_latex}$.",
                f"(3) Reflection: {reflect_desc} because $a {'<' if sign < 0 else '>'} 0$.",
                f"(4) Vertical: {k_desc} because $k = {k}$.",
            ],
            tags=list(ALG2_TRANSFORM_TAGS),
        )


# ===========================================================================
# Topic 2: graphing_rational_functions_part_1
# ===========================================================================


@register
class RationalVerticalAsymptotes(Generator):
    """Given a rational function, find the vertical asymptotes.

    Backward: pick two distinct integer roots r1, r2 for the denominator
    and an integer numerator constant A that doesn't vanish at either root.
    The resulting function is A / ((x - r1)(x - r2)), with vertical
    asymptotes x = r1 and x = r2.
    """
    generator_id = "rational_vertical_asymptotes"
    topic_slug = "graphing_rational_functions_part_1"
    display_name = "Find vertical asymptotes of a rational function"

    _ROOT_RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}
    _NUM_RANGES = {"easy": (1, 8), "medium": (1, 14), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ROOT_RANGES[difficulty]
        n_lo, n_hi = self._NUM_RANGES[difficulty]
        while True:
            r1 = rng.randint(-hi, hi)
            r2 = rng.randint(-hi, hi)
            if r1 == r2:
                continue
            if abs(r1) < lo or abs(r2) < lo:
                continue
            break
        A = rng.randint(n_lo, n_hi)
        if rng.random() < 0.5:
            A = -A

        # Expand denominator: (x - r1)(x - r2) = x^2 - (r1 + r2)x + r1*r2
        b_coef = -(r1 + r2)
        c_const = r1 * r2

        def _render_quad(b: int, c: int) -> str:
            parts = ["x^2"]
            if b != 0:
                if b > 0:
                    parts.append(f" + {b}x" if b != 1 else " + x")
                else:
                    parts.append(f" - {-b}x" if b != -1 else " - x")
            if c != 0:
                if c > 0:
                    parts.append(f" + {c}")
                else:
                    parts.append(f" - {-c}")
            return "".join(parts)

        denom_latex = _render_quad(b_coef, c_const)
        func_latex = rf"f(x) = \dfrac{{{A}}}{{{denom_latex}}}"

        # Answer: sort roots ascending.
        r_small, r_big = sorted([r1, r2])
        answer_text = f"$x = {r_small}$ and $x = {r_big}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, r1, r2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find all vertical asymptotes of ${func_latex}$."
            ),
            answer_latex=answer_text,
            hints=[
                "Vertical asymptotes occur where the denominator is zero (and the numerator is nonzero).",
                "Factor the denominator, then set each factor equal to zero.",
                f"The numerator ${A}$ is a nonzero constant, so nothing cancels.",
            ],
            solution_steps_latex=[
                f"Set the denominator equal to zero: ${denom_latex} = 0$.",
                (
                    f"Factor: ${denom_latex} = {_format_linear('x', r1)}{_format_linear('x', r2)}$."
                ),
                f"Solve each factor: $x = {r1}$ or $x = {r2}$.",
                f"The numerator is the nonzero constant ${A}$, so neither root cancels.",
                f"Vertical asymptotes: {answer_text}.",
            ],
            tags=list(ALG2_RATIONAL_TAGS),
        )


@register
class RationalHorizontalAsymptoteDegree(Generator):
    """Given a rational function, determine the horizontal asymptote via the
    degree comparison rule.

    Backward: pick a category (numerator degree less, equal, or greater
    than denominator degree) and construct polynomials accordingly. For
    equal degree the HA is the ratio of leading coefficients; less gives
    y = 0; greater gives "no horizontal asymptote" (may have a slant).
    """
    generator_id = "rational_horizontal_asymptote_degree"
    topic_slug = "graphing_rational_functions_part_1"
    display_name = "Find the horizontal asymptote via the degree rule"

    _RANGES = {"easy": (1, 7), "medium": (1, 12), "hard": (1, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        category = rng.choice(["less", "equal", "greater"])

        def _render_quad(a: int, b: int, c: int) -> str:
            parts: list[str] = []
            if a == 1:
                parts.append("x^2")
            elif a == -1:
                parts.append("-x^2")
            else:
                parts.append(f"{a}x^2")
            if b != 0:
                if b > 0:
                    parts.append(f" + {b}x" if b != 1 else " + x")
                else:
                    parts.append(f" - {-b}x" if b != -1 else " - x")
            if c != 0:
                if c > 0:
                    parts.append(f" + {c}")
                else:
                    parts.append(f" - {-c}")
            return "".join(parts)

        def _render_linear(a: int, b: int) -> str:
            parts: list[str] = []
            if a == 1:
                parts.append("x")
            elif a == -1:
                parts.append("-x")
            else:
                parts.append(f"{a}x")
            if b != 0:
                if b > 0:
                    parts.append(f" + {b}")
                else:
                    parts.append(f" - {-b}")
            return "".join(parts)

        def _render_cubic(a: int, const: int) -> str:
            parts: list[str] = []
            if a == 1:
                parts.append("x^3")
            elif a == -1:
                parts.append("-x^3")
            else:
                parts.append(f"{a}x^3")
            if const != 0:
                if const > 0:
                    parts.append(f" + {const}")
                else:
                    parts.append(f" - {-const}")
            return "".join(parts)

        if category == "less":
            # Numerator linear, denominator quadratic. HA: y = 0.
            a_num = rng.randint(1, hi)
            b_num = rng.randint(-hi, hi)
            a_den = rng.randint(1, hi)
            b_den = rng.randint(-hi, hi)
            c_den = rng.randint(-hi, hi)
            if c_den == 0:
                c_den = 1
            numer_latex = _render_linear(a_num, b_num)
            denom_latex = _render_quad(a_den, b_den, c_den)
            degree_numer = 1
            degree_denom = 2
            ha_latex = "$y = 0$"
            reason = (
                "Numerator degree is less than denominator degree, so the horizontal "
                "asymptote is $y = 0$."
            )
            params = ("less", a_num, b_num, a_den, b_den, c_den)
        elif category == "equal":
            # Both degree 2. HA: ratio of leading coefficients.
            a_num = rng.randint(1, hi)
            b_num = rng.randint(-hi, hi)
            c_num = rng.randint(-hi, hi)
            if c_num == 0:
                c_num = 2
            a_den = rng.randint(1, hi)
            b_den = rng.randint(-hi, hi)
            c_den = rng.randint(-hi, hi)
            if c_den == 0:
                c_den = 3
            # Randomly flip sign of a_num for variety.
            if rng.random() < 0.4:
                a_num = -a_num
            numer_latex = _render_quad(a_num, b_num, c_num)
            denom_latex = _render_quad(a_den, b_den, c_den)
            degree_numer = 2
            degree_denom = 2
            # Simplify a_num/a_den to lowest terms.
            g = gcd(abs(a_num), abs(a_den))
            rn = a_num // g
            rd = a_den // g
            if rd < 0:
                rn, rd = -rn, -rd
            if rd == 1:
                ha_latex = f"$y = {rn}$"
                ratio_latex = str(rn)
            else:
                ha_latex = rf"$y = \frac{{{rn}}}{{{rd}}}$"
                ratio_latex = rf"\frac{{{rn}}}{{{rd}}}"
            reason = (
                "Numerator and denominator have equal degree, so the horizontal "
                f"asymptote is the ratio of leading coefficients: $y = {ratio_latex}$."
            )
            params = ("equal", a_num, b_num, c_num, a_den, b_den, c_den)
        else:
            # Numerator cubic, denominator quadratic. No HA.
            a_num = rng.randint(1, hi)
            const_num = rng.randint(-hi, hi)
            a_den = rng.randint(1, hi)
            b_den = rng.randint(-hi, hi)
            c_den = rng.randint(-hi, hi)
            if c_den == 0:
                c_den = 1
            numer_latex = _render_cubic(a_num, const_num)
            denom_latex = _render_quad(a_den, b_den, c_den)
            degree_numer = 3
            degree_denom = 2
            ha_latex = "no horizontal asymptote"
            reason = (
                "Numerator degree is greater than denominator degree, so there is "
                "**no horizontal asymptote** (the function may have a slant asymptote instead)."
            )
            params = ("greater", a_num, const_num, a_den, b_den, c_den)

        func_latex = rf"f(x) = \dfrac{{{numer_latex}}}{{{denom_latex}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the horizontal asymptote of ${func_latex}$ (or state "
                f"that none exists)."
            ),
            answer_latex=ha_latex,
            hints=[
                r"Compare the degree of the numerator $p(x)$ to the degree of the denominator $q(x)$.",
                r"If $\deg p < \deg q$: $y = 0$. If $\deg p = \deg q$: ratio of leading coefficients. If $\deg p > \deg q$: no horizontal asymptote.",
                f"Here numerator degree is ${degree_numer}$ and denominator degree is ${degree_denom}$.",
            ],
            solution_steps_latex=[
                f"Numerator: ${numer_latex}$ has degree ${degree_numer}$.",
                f"Denominator: ${denom_latex}$ has degree ${degree_denom}$.",
                reason,
            ],
            tags=list(ALG2_RATIONAL_TAGS),
        )


@register
class RationalHolesAndIntercepts(Generator):
    """Given a rational function, find any holes (shared linear factors) and
    the x- and y-intercepts.

    Backward: pick factors so the numerator is (x - r1)(x - r_common) and
    the denominator is (x - r2)(x - r_common). The shared (x - r_common)
    gives a hole at x = r_common. The x-intercept is r1 and the y-intercept
    is computed at x = 0.
    """
    generator_id = "rational_holes_and_intercepts"
    topic_slug = "graphing_rational_functions_part_1"
    display_name = "Find holes and intercepts of a rational function"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick three distinct nonzero integers.
        while True:
            r_common = rng.randint(-hi, hi)
            r1 = rng.randint(-hi, hi)
            r2 = rng.randint(-hi, hi)
            if 0 in (r_common, r1, r2):
                continue
            if r_common == r1 or r_common == r2 or r1 == r2:
                continue
            # Also require x = 0 is in the domain (denominator nonzero at 0).
            # Denominator after factoring = (x - r2)(x - r_common).
            # At x=0: (-r2)(-r_common) = r2 * r_common, always nonzero given nonzero r.
            break

        # Expand numerator and denominator.
        # Numerator: (x - r1)(x - r_common) = x^2 - (r1 + r_common)x + r1*r_common
        n_b = -(r1 + r_common)
        n_c = r1 * r_common
        # Denominator: (x - r2)(x - r_common)
        d_b = -(r2 + r_common)
        d_c = r2 * r_common

        def _render_quad(b: int, c: int) -> str:
            parts = ["x^2"]
            if b != 0:
                if b > 0:
                    parts.append(f" + {b}x" if b != 1 else " + x")
                else:
                    parts.append(f" - {-b}x" if b != -1 else " - x")
            if c != 0:
                if c > 0:
                    parts.append(f" + {c}")
                else:
                    parts.append(f" - {-c}")
            return "".join(parts)

        numer_latex = _render_quad(n_b, n_c)
        denom_latex = _render_quad(d_b, d_c)
        func_latex = rf"f(x) = \dfrac{{{numer_latex}}}{{{denom_latex}}}"

        # After cancellation, simplified function = (x - r1)/(x - r2).
        # x-intercept: (x - r1) = 0 => x = r1.
        # y-intercept: plug x = 0 into simplified (or original). At x=0:
        # numerator = r1*r_common, denominator = r2*r_common -> = r1/r2 after canceling.
        y_num = r1
        y_den = r2
        g = gcd(abs(y_num), abs(y_den))
        rn = y_num // g
        rd = y_den // g
        if rd < 0:
            rn, rd = -rn, -rd
        if rd == 1:
            y_int_latex = f"$y = {rn}$"
        else:
            y_int_latex = rf"$y = \frac{{{rn}}}{{{rd}}}$"

        hole_latex = f"hole at $x = {r_common}$"
        x_int_latex = f"$x = {r1}$"

        answer = (
            f"Hole: $x = {r_common}$; x-intercept: $x = {r1}$; y-intercept: {y_int_latex}."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (r1, r2, r_common)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the rational function ${func_latex}$, find any holes "
                f"and the x- and y-intercepts."
            ),
            answer_latex=answer,
            hints=[
                "Factor both the numerator and the denominator.",
                "A common factor that appears in both produces a hole (not a vertical asymptote).",
                "The x-intercept occurs where the simplified numerator is zero; the y-intercept is found by substituting $x = 0$.",
            ],
            solution_steps_latex=[
                (
                    f"Factor: ${numer_latex} = {_format_linear('x', r1)}{_format_linear('x', r_common)}$ "
                    f"and ${denom_latex} = {_format_linear('x', r2)}{_format_linear('x', r_common)}$."
                ),
                (
                    f"Cancel the common factor ${_format_linear('x', r_common)}$: "
                    f"this produces a **{hole_latex}**."
                ),
                (
                    f"Simplified form: $\\dfrac{{{_format_linear_body('x', r1)}}}{{{_format_linear_body('x', r2)}}}$."
                ),
                f"x-intercept: set the simplified numerator to zero: {x_int_latex}.",
                f"y-intercept: substitute $x = 0$: $f(0) = \\dfrac{{{-r1}}}{{{-r2}}}$ = {y_int_latex}.",
            ],
            tags=list(ALG2_RATIONAL_TAGS),
        )


# ===========================================================================
# Topic 3: graphing_rational_functions_part_2
# ===========================================================================


@register
class SlantAsymptoteFromDivision(Generator):
    """Given a rational function where deg(p) = deg(q) + 1, find the slant
    asymptote.

    Backward: pick the slant line y = mx + b and a linear denominator
    (x - d). Construct numerator = (x - d)(mx + b) + r, where r is a small
    nonzero remainder. Then long division recovers y = mx + b with remainder
    r / (x - d).
    """
    generator_id = "slant_asymptote_from_division"
    topic_slug = "graphing_rational_functions_part_2"
    display_name = "Find the slant asymptote via polynomial long division"
    bank_count_per_difficulty = 25

    _M_RANGES = {"easy": (1, 4), "medium": (1, 6), "hard": (1, 8)}
    _B_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _D_RANGES = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-10, 10)}
    _R_RANGES = {"easy": (1, 5), "medium": (1, 9), "hard": (1, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        d_lo, d_hi = self._D_RANGES[difficulty]
        r_lo, r_hi = self._R_RANGES[difficulty]
        m = rng.randint(m_lo, m_hi)
        b_line = rng.randint(b_lo, b_hi)
        d = rng.randint(d_lo, d_hi)
        while d == 0:
            d = rng.randint(d_lo, d_hi)
        r = rng.randint(r_lo, r_hi)
        if rng.random() < 0.5:
            r = -r

        # Numerator = (x - d)(mx + b_line) + r
        # = m*x^2 + (b_line - m*d)*x + (-d * b_line + r)
        n_a = m
        n_b = b_line - m * d
        n_c = -d * b_line + r

        def _render_quad(a: int, bb: int, cc: int) -> str:
            parts: list[str] = []
            if a == 1:
                parts.append("x^2")
            elif a == -1:
                parts.append("-x^2")
            else:
                parts.append(f"{a}x^2")
            if bb != 0:
                if bb > 0:
                    parts.append(f" + {bb}x" if bb != 1 else " + x")
                else:
                    parts.append(f" - {-bb}x" if bb != -1 else " - x")
            if cc != 0:
                if cc > 0:
                    parts.append(f" + {cc}")
                else:
                    parts.append(f" - {-cc}")
            return "".join(parts)

        numer_latex = _render_quad(n_a, n_b, n_c)
        denom_latex = _format_linear_body("x", d)
        func_latex = rf"f(x) = \dfrac{{{numer_latex}}}{{{denom_latex}}}"

        # Slant line LaTeX: y = m*x + b_line.
        line_parts: list[str] = []
        if m == 1:
            line_parts.append("x")
        elif m == -1:
            line_parts.append("-x")
        else:
            line_parts.append(f"{m}x")
        if b_line != 0:
            if b_line > 0:
                line_parts.append(f" + {b_line}")
            else:
                line_parts.append(f" - {-b_line}")
        line_latex = "".join(line_parts)
        answer_latex = f"$y = {line_latex}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b_line, d, r)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the slant (oblique) asymptote of ${func_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                "Since the degree of the numerator is exactly one more than the degree of the denominator, there is a slant asymptote.",
                "Use polynomial long division: divide the numerator by the denominator.",
                "The quotient (ignoring the remainder) is the equation of the slant asymptote.",
            ],
            solution_steps_latex=[
                f"Divide ${numer_latex}$ by ${denom_latex}$ using polynomial long division.",
                (
                    f"The quotient is ${line_latex}$ with remainder ${r}$."
                ),
                (
                    rf"So $f(x) = {line_latex} + \dfrac{{{r}}}{{{denom_latex}}}$."
                ),
                (
                    r"As $x \to \pm\infty$, the remainder term approaches $0$, "
                    f"so the slant asymptote is $y = {line_latex}$."
                ),
            ],
            tags=list(ALG2_RATIONAL_TAGS),
        )


@register
class RationalSignAnalysisThreeIntervals(Generator):
    """Given a simple factored rational, determine the sign of f on each of
    the intervals separated by the two critical x-values.

    Backward: pick two distinct integer critical values p < q. Build
    f(x) = (x - p)/(x - q). (Always has exactly two critical values,
    thus three intervals.) Determine the sign on each interval by
    testing a representative point.
    """
    generator_id = "rational_sign_analysis_three_intervals"
    topic_slug = "graphing_rational_functions_part_2"
    display_name = "Sign analysis of a rational on three intervals"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-13, 13)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick two distinct nonzero integers.
        while True:
            p = rng.randint(lo, hi)
            q = rng.randint(lo, hi)
            if p == q:
                continue
            if p == 0 or q == 0:
                continue
            break
        if p > q:
            p, q = q, p

        numer_latex = _format_linear_body("x", p)
        denom_latex = _format_linear_body("x", q)
        func_latex = rf"f(x) = \dfrac{{{numer_latex}}}{{{denom_latex}}}"

        # Three intervals: (-inf, p), (p, q), (q, inf).
        # Test one value in each.
        test1 = p - 1  # strictly less than p
        test2_candidates = [v for v in range(p + 1, q)]
        if test2_candidates:
            test2 = test2_candidates[len(test2_candidates) // 2]
        else:
            # Shouldn't occur since p != q, but as a safeguard.
            test2 = (p + q) / 2
        test3 = q + 1  # strictly greater than q

        def sign(xv: float) -> str:
            num = xv - p
            den = xv - q
            if den == 0 or num == 0:
                return "undefined"
            return "positive" if num * den > 0 else "negative"

        s1 = sign(test1)
        s2 = sign(test2)
        s3 = sign(test3)

        intervals_latex = [
            f"$(-\\infty, {p})$",
            f"$({p}, {q})$",
            f"$({q}, \\infty)$",
        ]
        answer = (
            f"On $(-\\infty, {p})$: {s1}; on $({p}, {q})$: {s2}; on $({q}, \\infty)$: {s3}."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Perform a sign analysis of ${func_latex}$. The critical x-values "
                f"are $x = {p}$ (numerator zero) and $x = {q}$ (denominator zero, "
                f"vertical asymptote). State the sign of $f$ on each of the three "
                f"intervals separated by these values."
            ),
            answer_latex=answer,
            hints=[
                "Identify the critical x-values: where the numerator is zero and where the denominator is zero.",
                "These values partition the real line into three intervals.",
                "Pick a test value in each interval and determine the sign of the numerator and denominator separately.",
            ],
            solution_steps_latex=[
                f"Critical values: $x = {p}$ (numerator zero) and $x = {q}$ (denominator zero).",
                f"Intervals: {intervals_latex[0]}, {intervals_latex[1]}, {intervals_latex[2]}.",
                (
                    f"Test $x = {test1}$: numerator ${_format_linear_body('x', p)} = {test1 - p}$, "
                    f"denominator ${_format_linear_body('x', q)} = {test1 - q}$; "
                    f"quotient is **{s1}**."
                ),
                (
                    f"Test $x = {test2}$: numerator ${_format_linear_body('x', p)} = {test2 - p if isinstance(test2, int) else 'positive'}$, "
                    f"denominator ${_format_linear_body('x', q)} = {test2 - q if isinstance(test2, int) else 'negative'}$; "
                    f"quotient is **{s2}**."
                ),
                (
                    f"Test $x = {test3}$: numerator ${_format_linear_body('x', p)} = {test3 - p}$, "
                    f"denominator ${_format_linear_body('x', q)} = {test3 - q}$; "
                    f"quotient is **{s3}**."
                ),
                f"Sign summary — {answer}",
            ],
            tags=list(ALG2_RATIONAL_TAGS),
        )


@register
class RationalCompleteFeatureList(Generator):
    """Given a rational function, list: vertical asymptotes, horizontal
    asymptote, x-intercepts, y-intercept.

    Backward: build f(x) = A*(x - x_int)/((x - v1)(x - v2)) with distinct
    integers v1, v2 and an integer x-intercept distinct from both. The
    numerator is linear and the denominator is quadratic, so HA is y = 0.
    """
    generator_id = "rational_complete_feature_list"
    topic_slug = "graphing_rational_functions_part_2"
    display_name = "List complete features of a rational function"
    bank_count_per_difficulty = 25

    _RANGES = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _A_CHOICES = {
        "easy": (1, 2),
        "medium": (1, 2, 3, -1, -2),
        "hard": (1, 2, 3, 4, -1, -2, -3),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        while True:
            v1 = rng.randint(-hi, hi)
            v2 = rng.randint(-hi, hi)
            x_int = rng.randint(-hi, hi)
            if 0 in (v1, v2):  # ensure x=0 is in the domain
                continue
            if v1 == v2:
                continue
            if x_int in (v1, v2):  # not canceling any asymptote
                continue
            break
        A = rng.choice(self._A_CHOICES[difficulty])

        # f(x) = A*(x - x_int) / ((x - v1)(x - v2))
        d_b = -(v1 + v2)
        d_c = v1 * v2

        # Render numerator: A*(x - x_int).
        if x_int == 0:
            if A == 1:
                numer_latex = "x"
            elif A == -1:
                numer_latex = "-x"
            else:
                numer_latex = f"{A}x"
        else:
            if A == 1:
                numer_latex = _format_linear_body("x", x_int)
            elif A == -1:
                # -(x - x_int) = -x + x_int
                if x_int > 0:
                    numer_latex = f"-x + {x_int}"
                else:
                    numer_latex = f"-x - {-x_int}"
            else:
                ax = f"{A}x"
                const = -A * x_int
                if const == 0:
                    numer_latex = ax
                elif const > 0:
                    numer_latex = f"{ax} + {const}"
                else:
                    numer_latex = f"{ax} - {-const}"

        def _render_quad(bb: int, cc: int) -> str:
            parts = ["x^2"]
            if bb != 0:
                if bb > 0:
                    parts.append(f" + {bb}x" if bb != 1 else " + x")
                else:
                    parts.append(f" - {-bb}x" if bb != -1 else " - x")
            if cc != 0:
                if cc > 0:
                    parts.append(f" + {cc}")
                else:
                    parts.append(f" - {-cc}")
            return "".join(parts)

        denom_latex = _render_quad(d_b, d_c)
        func_latex = rf"f(x) = \dfrac{{{numer_latex}}}{{{denom_latex}}}"

        # Features:
        v_small, v_big = sorted([v1, v2])
        va_latex = f"$x = {v_small}$ and $x = {v_big}$"
        ha_latex = "$y = 0$"  # numerator degree 1 < denominator degree 2
        x_int_latex = f"$x = {x_int}$"
        # y-intercept: f(0) = A*(0 - x_int)/(v1*v2) = -A*x_int / (v1*v2)
        y_num = -A * x_int
        y_den = v1 * v2
        g = gcd(abs(y_num), abs(y_den)) if y_num != 0 else y_den
        if y_num == 0:
            y_int_latex = "$y = 0$"
        else:
            rn = y_num // g
            rd = y_den // g
            if rd < 0:
                rn, rd = -rn, -rd
            if rd == 1:
                y_int_latex = f"$y = {rn}$"
            else:
                y_int_latex = rf"$y = \frac{{{rn}}}{{{rd}}}$"

        answer = (
            f"Vertical asymptotes: {va_latex}; "
            f"horizontal asymptote: {ha_latex}; "
            f"x-intercept: {x_int_latex}; "
            f"y-intercept: {y_int_latex}."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (A, x_int, v1, v2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the rational function ${func_latex}$, list (a) all vertical "
                f"asymptotes, (b) the horizontal asymptote, (c) any x-intercepts, "
                f"and (d) the y-intercept."
            ),
            answer_latex=answer,
            hints=[
                "Factor the denominator to find vertical asymptotes (where the denominator is zero and the numerator is not).",
                "Compare degrees of numerator and denominator to find the horizontal asymptote.",
                "Set the numerator equal to zero for x-intercepts; substitute $x = 0$ for the y-intercept.",
            ],
            solution_steps_latex=[
                f"Factor the denominator: ${denom_latex} = {_format_linear('x', v1)}{_format_linear('x', v2)}$.",
                f"(a) Vertical asymptotes at: {va_latex}.",
                (
                    "(b) Numerator has degree $1$, denominator has degree $2$, so the horizontal "
                    f"asymptote is {ha_latex}."
                ),
                f"(c) Set the numerator ${numer_latex} = 0$: x-intercept at {x_int_latex}.",
                (
                    f"(d) Substitute $x = 0$: $f(0) = \\dfrac{{{-A * x_int}}}{{{v1 * v2}}}$ = {y_int_latex}."
                ),
            ],
            tags=list(ALG2_RATIONAL_TAGS),
        )


# ===========================================================================
# Topic 4: more_exotic_functions
# ===========================================================================


@register
class EvaluatePiecewise(Generator):
    """Given a piecewise function with 2 or 3 pieces and a list of inputs,
    evaluate each.

    Backward: pick a split point s (and optionally a second split t > s for
    3-piece problems). Choose linear expressions for each piece. Choose
    input values that fall cleanly into each region.
    """
    generator_id = "evaluate_piecewise"
    topic_slug = "more_exotic_functions"
    display_name = "Evaluate a piecewise function at several inputs"
    bank_count_per_difficulty = 25

    _S_RANGES = {"easy": (-3, 3), "medium": (-6, 6), "hard": (-9, 9)}
    _COEF_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}
    _CONST_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _linear_latex(self, m: int, b: int) -> str:
        parts: list[str] = []
        if m == 0:
            return str(b)
        if m == 1:
            parts.append("x")
        elif m == -1:
            parts.append("-x")
        else:
            parts.append(f"{m}x")
        if b != 0:
            if b > 0:
                parts.append(f" + {b}")
            else:
                parts.append(f" - {-b}")
        return "".join(parts)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        s_lo, s_hi = self._S_RANGES[difficulty]
        c_lo, c_hi = self._COEF_RANGES[difficulty]
        k_lo, k_hi = self._CONST_RANGES[difficulty]
        n_pieces = rng.choice([2, 3])

        s = rng.randint(s_lo, s_hi)

        # Piece 1: for x < s
        m1 = rng.randint(c_lo, c_hi)
        b1 = rng.randint(k_lo, k_hi)
        # Piece 2: for s <= x (2-piece) or s <= x < t (3-piece)
        m2 = rng.randint(c_lo, c_hi)
        b2 = rng.randint(k_lo, k_hi)

        if n_pieces == 3:
            # Pick t > s
            t = s + rng.randint(2, max(3, s_hi - s_lo))
            m3 = rng.randint(c_lo, c_hi)
            b3 = rng.randint(k_lo, k_hi)
        else:
            t = None
            m3 = 0
            b3 = 0

        # Ensure at least one nonzero coefficient among the pieces for interest.
        if m1 == 0 and m2 == 0 and (n_pieces == 2 or m3 == 0):
            m1 = 1

        # Pick three input values: one in each piece.
        # For 2-piece, two values < s and one >= s, or similar.
        inputs: list[int] = []
        # Input 1: strictly less than s.
        inputs.append(s - rng.choice([1, 2, 3]))
        # Input 2: >= s (and < t if 3-piece)
        if n_pieces == 2:
            inputs.append(s + rng.choice([0, 1, 2]))
            inputs.append(s + rng.choice([3, 4, 5]))
        else:
            assert t is not None
            # Middle piece value: between s (inclusive) and t (exclusive)
            mid_span = max(1, t - s - 1)
            inputs.append(s + (mid_span // 2 if mid_span > 1 else 0))
            # Third piece value: >= t
            inputs.append(t + rng.choice([0, 1, 2]))

        # Compute outputs using the piecewise rule.
        def f(xv: int) -> tuple[int, int]:
            """Return (piece_index, f(xv)). Piece index is 1/2/3."""
            if xv < s:
                return (1, m1 * xv + b1)
            if n_pieces == 2 or t is None or xv < t:
                return (2, m2 * xv + b2)
            return (3, m3 * xv + b3)

        results = [(xv, *f(xv)) for xv in inputs]

        # Build the piecewise LaTeX using \begin{cases}.
        piece1_latex = self._linear_latex(m1, b1)
        piece2_latex = self._linear_latex(m2, b2)
        if n_pieces == 2:
            cases_rows = [
                rf"{piece1_latex} & \text{{if }} x < {s} \\",
                rf"{piece2_latex} & \text{{if }} x \geq {s}",
            ]
        else:
            piece3_latex = self._linear_latex(m3, b3)
            cases_rows = [
                rf"{piece1_latex} & \text{{if }} x < {s} \\",
                rf"{piece2_latex} & \text{{if }} {s} \leq x < {t} \\",
                rf"{piece3_latex} & \text{{if }} x \geq {t}",
            ]
        cases_body = " ".join(cases_rows)
        func_latex = rf"f(x) = \begin{{cases}} {cases_body} \end{{cases}}"

        # Build the statement request and the answer.
        inputs_prose = ", ".join([f"$f({xv})$" for xv, _, _ in results])
        answer = "; ".join([f"$f({xv}) = {val}$" for xv, _, val in results])

        # Build solution steps (one per input).
        steps: list[str] = [f"The function has {n_pieces} pieces."]
        for xv, piece_idx, val in results:
            if n_pieces == 2:
                region = (
                    rf"$x < {s}$" if piece_idx == 1 else rf"$x \geq {s}$"
                )
            else:
                if piece_idx == 1:
                    region = rf"$x < {s}$"
                elif piece_idx == 2:
                    region = rf"${s} \leq x < {t}$"
                else:
                    region = rf"$x \geq {t}$"
            if piece_idx == 1:
                piece_expr = piece1_latex
                mv, bv = m1, b1
            elif piece_idx == 2:
                piece_expr = piece2_latex
                mv, bv = m2, b2
            else:
                piece_expr = self._linear_latex(m3, b3)
                mv, bv = m3, b3
            steps.append(
                f"For $x = {xv}$: since {region}, use piece {piece_idx}, "
                f"which is ${piece_expr}$. Compute $f({xv}) = ({mv})({xv}) + ({bv}) = {val}$."
            )

        params = (n_pieces, s, m1, b1, m2, b2, t if t is not None else 0, m3, b3)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $${func_latex}.$$ "
                f"Compute {inputs_prose}."
            ),
            answer_latex=answer,
            hints=[
                "Decide which piece applies for each input by checking which inequality the input satisfies.",
                "Then substitute the input into that piece's formula.",
                "Different inputs may use different pieces, so check each one independently.",
            ],
            solution_steps_latex=steps,
            tags=list(ALG2_EXOTIC_TAGS),
        )


@register
class IdentifyPieceAtInput(Generator):
    """Given a piecewise function and a single input, state which piece
    applies (without necessarily evaluating).

    Backward: pick a 3-piece setup with two split points s and t, pick a
    single input in one of the three regions, and ask which piece applies.
    """
    generator_id = "identify_piece_at_input"
    topic_slug = "more_exotic_functions"
    display_name = "Identify which piece of a piecewise function applies"
    bank_count_per_difficulty = 25

    _S_RANGES = {"easy": (-3, 3), "medium": (-6, 6), "hard": (-9, 9)}
    _COEF_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}
    _CONST_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-14, 14)}

    def _linear_latex(self, m: int, b: int) -> str:
        if m == 0:
            return str(b)
        parts: list[str] = []
        if m == 1:
            parts.append("x")
        elif m == -1:
            parts.append("-x")
        else:
            parts.append(f"{m}x")
        if b != 0:
            if b > 0:
                parts.append(f" + {b}")
            else:
                parts.append(f" - {-b}")
        return "".join(parts)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        s_lo, s_hi = self._S_RANGES[difficulty]
        c_lo, c_hi = self._COEF_RANGES[difficulty]
        k_lo, k_hi = self._CONST_RANGES[difficulty]
        # Build a 3-piece function.
        s = rng.randint(s_lo, s_hi)
        t = s + rng.randint(2, max(3, s_hi - s_lo + 2))
        m1 = rng.randint(c_lo, c_hi)
        b1 = rng.randint(k_lo, k_hi)
        m2 = rng.randint(c_lo, c_hi)
        b2 = rng.randint(k_lo, k_hi)
        m3 = rng.randint(c_lo, c_hi)
        b3 = rng.randint(k_lo, k_hi)
        # Pick region for the target input.
        region = rng.choice([1, 2, 3])
        if region == 1:
            xv = s - rng.choice([1, 2, 3])
            region_desc = rf"$x < {s}$"
            piece_num = 1
            piece_latex = self._linear_latex(m1, b1)
            inequality_check = f"${xv} < {s}$ is true"
        elif region == 2:
            # In [s, t)
            mid = max(1, t - s - 1)
            xv = s + rng.randint(0, mid - 1 if mid > 1 else 0)
            region_desc = rf"${s} \leq x < {t}$"
            piece_num = 2
            piece_latex = self._linear_latex(m2, b2)
            inequality_check = f"${s} \\leq {xv} < {t}$ is true"
        else:
            xv = t + rng.choice([0, 1, 2])
            region_desc = rf"$x \geq {t}$"
            piece_num = 3
            piece_latex = self._linear_latex(m3, b3)
            inequality_check = f"${xv} \\geq {t}$ is true"

        piece1_latex = self._linear_latex(m1, b1)
        piece2_latex = self._linear_latex(m2, b2)
        piece3_latex = self._linear_latex(m3, b3)
        cases_body = " ".join(
            [
                rf"{piece1_latex} & \text{{if }} x < {s} \\",
                rf"{piece2_latex} & \text{{if }} {s} \leq x < {t} \\",
                rf"{piece3_latex} & \text{{if }} x \geq {t}",
            ]
        )
        func_latex = rf"f(x) = \begin{{cases}} {cases_body} \end{{cases}}"

        answer = (
            f"Piece {piece_num} applies: ${piece_latex}$ (because {region_desc})."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (s, t, m1, b1, m2, b2, m3, b3, xv)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For $${func_latex},$$ "
                f"which piece applies when $x = {xv}$? State the piece and the expression "
                f"to use."
            ),
            answer_latex=answer,
            hints=[
                "Test the input against each piece's condition.",
                "The correct piece is the one whose inequality the input satisfies.",
                "You do not need to compute $f(x)$; just name the piece and its expression.",
            ],
            solution_steps_latex=[
                f"Test $x = {xv}$ against each piece's condition.",
                f"Check condition {piece_num}: {inequality_check}.",
                f"So piece {piece_num} applies; the expression to use is ${piece_latex}$.",
            ],
            tags=list(ALG2_EXOTIC_TAGS),
        )


@register
class FloorFunctionEvaluate(Generator):
    """Evaluate the floor function ⌊x⌋ at various inputs, including negatives
    and half-integers.

    Backward: pick a category from {positive_half, positive_int,
    negative_half, negative_int, zero_neighborhood}, then pick a specific
    input. The parameter tuple encodes (category_id, numerator, denominator).
    Inputs are rendered as fractions when non-integer.
    """
    generator_id = "floor_function_evaluate"
    topic_slug = "more_exotic_functions"
    display_name = "Evaluate the floor function at various inputs"
    bank_count_per_difficulty = 25

    _POS_INT_RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (1, 25)}
    _NEG_INT_RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (1, 25)}
    _POS_HALF_RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (1, 25)}
    _NEG_HALF_RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Weight categories so negative half-integers appear often (they
        # trip the "round down" rule, which is the learning objective).
        category = rng.choice(
            [
                "positive_int",
                "positive_half",
                "negative_int",
                "negative_half",
                "negative_half",  # double weight — pedagogically critical
            ]
        )

        if category == "positive_int":
            lo, hi = self._POS_INT_RANGES[difficulty]
            n = rng.randint(lo, hi)
            input_latex = str(n)
            input_prose = str(n)
            output = n
            reasoning = f"${n}$ is already an integer, so $\\lfloor {n} \\rfloor = {n}$."
        elif category == "positive_half":
            lo, hi = self._POS_HALF_RANGES[difficulty]
            n = rng.randint(lo, hi)
            # n + 1/2
            input_latex = rf"\frac{{{2 * n + 1}}}{{2}}"
            input_prose = f"{n}.5"
            output = n
            reasoning = (
                rf"${input_latex}$ lies between ${n}$ and ${n + 1}$. "
                rf"The greatest integer that does not exceed it is ${n}$, "
                rf"so $\lfloor {input_latex} \rfloor = {n}$."
            )
        elif category == "negative_int":
            lo, hi = self._NEG_INT_RANGES[difficulty]
            n = rng.randint(lo, hi)
            input_latex = f"-{n}"
            input_prose = f"-{n}"
            output = -n
            reasoning = f"$-{n}$ is already an integer, so $\\lfloor -{n} \\rfloor = -{n}$."
        else:  # negative_half
            lo, hi = self._NEG_HALF_RANGES[difficulty]
            n = rng.randint(lo, hi)
            # -(n - 1/2) written as -(2n-1)/2
            input_latex = rf"-\frac{{{2 * n + 1}}}{{2}}"
            input_prose = f"-{n}.5"
            # -n.5 lies between -(n+1) and -n; floor rounds DOWN to -(n+1)
            output = -(n + 1)
            reasoning = (
                rf"${input_latex}$ lies between $-{n + 1}$ and $-{n}$. "
                rf"The floor function rounds **down** (toward $-\infty$), "
                rf"so $\lfloor {input_latex} \rfloor = -{n + 1}$, **not** $-{n}$."
            )

        # Encode category into the param tuple for deterministic IDs.
        cat_id = {
            "positive_int": 1,
            "positive_half": 2,
            "negative_int": 3,
            "negative_half": 4,
        }[category]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (cat_id, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Evaluate the floor function: $\lfloor {input_latex} \rfloor$."
            ),
            answer_latex=rf"$\lfloor {input_latex} \rfloor = {output}$",
            hints=[
                r"The floor function $\lfloor x \rfloor$ returns the greatest integer less than or equal to $x$.",
                r"For positive inputs, this is just the integer part. For negative non-integer inputs, you must round **toward** $-\infty$, not toward zero.",
                f"Locate ${input_latex}$ on the number line and pick the nearest integer to its left.",
            ],
            solution_steps_latex=[
                rf"Recall: $\lfloor x \rfloor$ is the greatest integer that is $\leq x$.",
                reasoning,
                rf"Therefore $\lfloor {input_latex} \rfloor = {output}$.",
            ],
            tags=list(ALG2_EXOTIC_TAGS),
        )


# ===========================================================================
# Topic 5: introduction_to_rational_functions (pre-calculus)
# ===========================================================================


@register
class ReciprocalFunctionDomain(Generator):
    """Given f(x) = k/(x - h), state the domain in interval notation.

    Backward: pick integer k (nonzero) and integer h. Domain is all reals
    except x = h.
    """
    generator_id = "reciprocal_function_domain"
    topic_slug = "introduction_to_rational_functions"
    display_name = "Find the domain of f(x) = k/(x - h)"

    _K_RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (1, 25)}
    _H_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        h_lo, h_hi = self._H_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        if rng.random() < 0.4:
            k = -k
        h = rng.randint(h_lo, h_hi)

        denom_latex = _format_linear_body("x", h)
        func_latex = rf"f(x) = \dfrac{{{k}}}{{{denom_latex}}}"

        # Domain: all reals except x = h. Interval form: (-inf, h) U (h, inf).
        interval_latex = (
            f"(-\\infty, {h}) \\cup ({h}, \\infty)"
        )
        set_builder = f"\\{{x \\in \\mathbb{{R}} : x \\ne {h}\\}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, h)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the domain of ${func_latex}$ in interval notation."
            ),
            answer_latex=f"${interval_latex}$",
            hints=[
                "A rational function is undefined wherever its denominator is zero.",
                "Set the denominator equal to zero and solve for $x$.",
                "Exclude that value from the real numbers.",
            ],
            solution_steps_latex=[
                f"Set the denominator equal to zero: ${denom_latex} = 0$, giving $x = {h}$.",
                f"This is the only value where $f$ is undefined.",
                (
                    "The domain is all real numbers except $x = "
                    f"{h}$: ${interval_latex}$ (or equivalently ${set_builder}$)."
                ),
            ],
            tags=list(PRECALC_RATIONAL_TAGS),
        )


@register
class ReciprocalShiftedAsymptotes(Generator):
    """Given f(x) = k/(x - h) + c, state both asymptotes.

    Backward: pick integer k, h, c (all nonzero where relevant). The
    vertical asymptote is x = h and the horizontal asymptote is y = c.
    """
    generator_id = "reciprocal_shifted_asymptotes"
    topic_slug = "introduction_to_rational_functions"
    display_name = "State the asymptotes of f(x) = k/(x - h) + c"

    _K_RANGES = {"easy": (1, 8), "medium": (1, 14), "hard": (1, 22)}
    _H_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _C_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        h_lo, h_hi = self._H_RANGES[difficulty]
        c_lo, c_hi = self._C_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        if rng.random() < 0.4:
            k = -k
        h = rng.randint(h_lo, h_hi)
        c = rng.randint(c_lo, c_hi)

        denom_latex = _format_linear_body("x", h)
        frac_latex = rf"\dfrac{{{k}}}{{{denom_latex}}}"
        func_latex = f"f(x) = {frac_latex}{_format_trailing_const(c)}"

        va_latex = f"$x = {h}$"
        ha_latex = f"$y = {c}$"
        answer = f"Vertical: {va_latex}; horizontal: {ha_latex}."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, h, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find both the vertical asymptote and the horizontal asymptote "
                f"of ${func_latex}$."
            ),
            answer_latex=answer,
            hints=[
                r"The form $f(x) = \dfrac{k}{x - h} + c$ is a shifted reciprocal function.",
                "The vertical asymptote is where the denominator is zero.",
                r"As $x \to \pm\infty$, the fraction tends to $0$, so $f(x) \to c$; that gives the horizontal asymptote.",
            ],
            solution_steps_latex=[
                (
                    f"Set the denominator equal to zero: ${denom_latex} = 0$, "
                    f"so the vertical asymptote is $x = {h}$."
                ),
                (
                    rf"As $x \to \pm\infty$, $\dfrac{{{k}}}{{{denom_latex}}} \to 0$, "
                    rf"so $f(x) \to {c}$. The horizontal asymptote is $y = {c}$."
                ),
                f"Final: vertical asymptote {va_latex}, horizontal asymptote {ha_latex}.",
            ],
            tags=list(PRECALC_RATIONAL_TAGS),
        )


@register
class ReciprocalEvaluate(Generator):
    """Evaluate f(x) = k/(x - h) + c at a specific input, yielding an integer.

    Backward: pick k, h, c and a nonzero integer divisor d of k. Set the
    input = h + d so that x - h = d and k/d is an integer. Output is
    k/d + c.
    """
    generator_id = "reciprocal_evaluate"
    topic_slug = "introduction_to_rational_functions"
    display_name = "Evaluate f(x) = k/(x - h) + c at a given input"

    _K_CANDIDATES = {
        "easy": (2, 3, 4, 6, 8, 12),
        "medium": (2, 3, 4, 6, 8, 10, 12, 15, 18, 20, 24),
        "hard": (2, 3, 4, 6, 8, 10, 12, 15, 18, 20, 24, 30, 36, 48),
    }
    _H_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-13, 13)}
    _C_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_choices = self._K_CANDIDATES[difficulty]
        h_lo, h_hi = self._H_RANGES[difficulty]
        c_lo, c_hi = self._C_RANGES[difficulty]
        k = rng.choice(k_choices)
        if rng.random() < 0.4:
            k = -k
        h = rng.randint(h_lo, h_hi)
        c = rng.randint(c_lo, c_hi)

        # Pick a nonzero divisor of |k|.
        divisors = [d for d in range(1, abs(k) + 1) if abs(k) % d == 0]
        # Allow negative divisors too.
        divisors_signed = divisors + [-d for d in divisors]
        d = rng.choice(divisors_signed)

        input_val = h + d
        # k / d is an integer because d divides k.
        frac_value = k // d
        output = frac_value + c

        denom_latex = _format_linear_body("x", h)
        frac_latex = rf"\dfrac{{{k}}}{{{denom_latex}}}"
        func_latex = f"f(x) = {frac_latex}{_format_trailing_const(c)}"

        # Substituted fraction
        if h == 0:
            sub_inside = str(input_val)
        elif h > 0:
            sub_inside = f"{input_val} - {h}"
        else:
            sub_inside = f"{input_val} + {-h}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, h, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, find $f({input_val})$."
            ),
            answer_latex=f"$f({input_val}) = {output}$",
            hints=[
                f"Substitute $x = {input_val}$ into the expression for $f$.",
                f"Simplify the denominator first: ${sub_inside} = {d}$.",
                rf"Then compute $\dfrac{{{k}}}{{{d}}} = {frac_value}$ and add ${c}$.",
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {input_val}$: "
                    f"$f({input_val}) = \\dfrac{{{k}}}{{{sub_inside}}}{_format_trailing_const(c)}$."
                ),
                (
                    f"Simplify the denominator: $\\dfrac{{{k}}}{{{d}}}{_format_trailing_const(c)}$."
                ),
                (
                    f"Divide: ${frac_value}{_format_trailing_const(c)} = {output}$."
                ),
            ],
            tags=list(PRECALC_RATIONAL_TAGS),
        )
