"""Quadratic functions and graphing generators (Phase 2c Cluster 3).

Four topic slugs covered:

- the_discriminant (The_Discriminant.md)
- graphing_quadratic_functions (Graphing_Quadratic_Functions.md)
- quadratic_functions (Quadratic_Functions.md)
- applications_of_quadratic_functions (Applications_Of_Quadratic_Functions.md)

Each topic has three generators for a total of 12. Backward construction
is used throughout so answers come out clean (integer vertices, integer
projectile maxima, integer roots). Word-problem generators draw scenario
templates from small lists so each problem reads like fresh prose.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
t_sym = sp.Symbol("t")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _format_quadratic_expr(a: int, b: int, c: int, var: str = "x") -> str:
    """Render ax^2 + bx + c as LaTeX with clean signs. Hides 1-coefficients."""
    parts: list[str] = []
    # Leading a*x^2 term
    if a == 1:
        parts.append(f"{var}^2")
    elif a == -1:
        parts.append(f"-{var}^2")
    else:
        parts.append(f"{a}{var}^2")
    # bx term
    if b != 0:
        if b > 0:
            sign = " + "
        else:
            sign = " - "
        mag = abs(b)
        if mag == 1:
            parts.append(f"{sign}{var}")
        else:
            parts.append(f"{sign}{mag}{var}")
    # c term
    if c != 0:
        if c > 0:
            parts.append(f" + {c}")
        else:
            parts.append(f" - {abs(c)}")
    return "".join(parts)


def _format_quadratic_equation(a: int, b: int, c: int) -> str:
    """Render ax^2 + bx + c = 0 with clean signs."""
    return f"{_format_quadratic_expr(a, b, c)} = 0"


def _format_quadratic_function(a: int, b: int, c: int, name: str = "f") -> str:
    """Render f(x) = ax^2 + bx + c with clean signs."""
    return f"{name}(x) = {_format_quadratic_expr(a, b, c)}"


def _format_signed_paren(n: int) -> str:
    """Wrap a negative number in parentheses for display after a minus sign."""
    return f"({n})" if n < 0 else str(n)


def _format_vertex_form(a: int, h: int, k: int) -> str:
    """Render a(x - h)^2 + k with clean signs. Handles a in {1, -1, other}."""
    # (x - h) or (x + |h|)
    if h == 0:
        inside = "x"
    elif h > 0:
        inside = f"(x - {h})"
    else:
        inside = f"(x + {-h})"
    # Leading a
    if h == 0:
        if a == 1:
            leading = "x^2"
        elif a == -1:
            leading = "-x^2"
        else:
            leading = f"{a}x^2"
    else:
        if a == 1:
            leading = f"{inside}^2"
        elif a == -1:
            leading = f"-{inside}^2"
        else:
            leading = f"{a}{inside}^2"
    # + k
    if k == 0:
        return leading
    if k > 0:
        return f"{leading} + {k}"
    return f"{leading} - {-k}"


def _format_function_vertex(a: int, h: int, k: int, name: str = "f") -> str:
    """Render f(x) = a(x - h)^2 + k."""
    return f"{name}(x) = {_format_vertex_form(a, h, k)}"


# ===========================================================================
# Topic 1: the_discriminant
# ===========================================================================

@register
class DiscriminantCompute(Generator):
    """Given ax^2 + bx + c = 0, compute the discriminant b^2 - 4ac."""
    generator_id = "discriminant_compute"
    topic_slug = "the_discriminant"
    display_name = "Compute the discriminant b^2 - 4ac"

    _A_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (1, 8)}
    _B_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}
    _C_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        c_lo, c_hi = self._C_RANGES[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)
        c = rng.randint(c_lo, c_hi)
        discriminant = b * b - 4 * a * c

        eq_latex = _format_quadratic_equation(a, b, c)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Compute the discriminant of the quadratic equation "
                f"${eq_latex}$."
            ),
            answer_latex=f"$\\Delta = {discriminant}$",
            hints=[
                r"The discriminant is $\Delta = b^2 - 4ac$.",
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                f"Square $b$: ${_format_signed_paren(b)}^2 = {b * b}$.",
            ],
            solution_steps_latex=[
                f"Identify the coefficients: $a = {a}$, $b = {b}$, $c = {c}$.",
                (
                    f"Apply $\\Delta = b^2 - 4ac = {_format_signed_paren(b)}^2 "
                    f"- 4({a})({_format_signed_paren(c)})$."
                ),
                f"Simplify: $\\Delta = {b * b} - {4 * a * c} = {discriminant}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-procedural-calculation"],
        )


@register
class DiscriminantClassifyRootCount(Generator):
    """Compute discriminant and classify: two real, one repeated, or no real roots."""
    generator_id = "discriminant_classify_root_count"
    topic_slug = "the_discriminant"
    display_name = "Classify root count via the discriminant"

    _A_RANGES = {"easy": (1, 3), "medium": (1, 4), "hard": (1, 6)}
    _K_RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        # Backward-construct by picking the category first.
        category = rng.choice(["positive", "zero", "negative"])

        if category == "zero":
            # Δ = 0 means (x - r)^2 = 0 up to scaling, so b = -2ar, c = a*r^2.
            a = rng.randint(a_lo, a_hi)
            r = rng.randint(-k_hi, k_hi)
            b = -2 * a * r
            c = a * r * r
        elif category == "positive":
            # Δ > 0: pick two distinct integer roots r1, r2, expand a(x-r1)(x-r2).
            a = rng.randint(a_lo, a_hi)
            r1 = rng.randint(-k_hi, k_hi)
            r2 = rng.randint(-k_hi, k_hi)
            while r2 == r1:
                r2 = rng.randint(-k_hi, k_hi)
            b = -a * (r1 + r2)
            c = a * r1 * r2
        else:  # negative
            # Pick a, b freely, then choose c large enough to force Δ < 0.
            a = rng.randint(a_lo, a_hi)
            b = rng.randint(-k_hi, k_hi)
            # Need 4ac > b^2 → c > b^2 / (4a). Take c = floor(b^2/(4a)) + k (positive).
            min_c = (b * b) // (4 * a) + 1
            c_bump = rng.randint(k_lo, k_hi)
            c = min_c + c_bump

        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            classification = "two distinct real roots"
        elif discriminant == 0:
            classification = "one repeated real root"
        else:
            classification = "no real roots"

        eq_latex = _format_quadratic_equation(a, b, c)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Compute the discriminant of ${eq_latex}$ and use it to "
                "decide whether the equation has two distinct real roots, "
                "one repeated real root, or no real roots."
            ),
            answer_latex=f"$\\Delta = {discriminant}$; {classification}.",
            hints=[
                r"Start by finding $\Delta = b^2 - 4ac$.",
                r"If $\Delta > 0$: two distinct real roots. If $\Delta = 0$: one repeated real root. If $\Delta < 0$: no real roots.",
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
            ],
            solution_steps_latex=[
                f"From ${eq_latex}$, read off $a = {a}$, $b = {b}$, $c = {c}$.",
                (
                    f"Compute $\\Delta = {_format_signed_paren(b)}^2 - 4({a})"
                    f"({_format_signed_paren(c)}) = {b * b} - {4 * a * c} = {discriminant}$."
                ),
                f"Because $\\Delta = {discriminant}$, the equation has {classification}.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-procedural-calculation"],
        )


@register
class DiscriminantFromGraphDescription(Generator):
    """Given verbal x-axis behavior, decide if the discriminant is positive, zero, or negative."""
    generator_id = "discriminant_from_graph_description"
    topic_slug = "the_discriminant"
    display_name = "Determine the sign of the discriminant from a graph description"
    bank_count_per_difficulty = 20  # textual parameter space is small

    # Each template: (description, expected sign of Delta)
    _TEMPLATES_POSITIVE = [
        "a parabola that crosses the x-axis at two different points",
        "a parabola whose graph intersects the x-axis twice",
        "a parabola that cuts through the x-axis at two distinct points",
        "a parabola with two different x-intercepts",
    ]
    _TEMPLATES_ZERO = [
        "a parabola that just touches the x-axis at a single point",
        "a parabola that is tangent to the x-axis",
        "a parabola whose vertex sits exactly on the x-axis",
        "a parabola that meets the x-axis at exactly one point",
    ]
    _TEMPLATES_NEGATIVE = [
        "a parabola that never touches the x-axis",
        "a parabola that stays entirely above the x-axis",
        "a parabola that stays entirely below the x-axis",
        "a parabola with no x-intercepts",
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        category = rng.choice(["positive", "zero", "negative"])
        if category == "positive":
            description = rng.choice(self._TEMPLATES_POSITIVE)
            answer = "positive"
            reason = (
                "two different real x-intercepts correspond to two distinct real "
                "roots, which only happens when $\\Delta > 0$"
            )
        elif category == "zero":
            description = rng.choice(self._TEMPLATES_ZERO)
            answer = "zero"
            reason = (
                "a single x-intercept corresponds to one repeated real root, "
                "which only happens when $\\Delta = 0$"
            )
        else:
            description = rng.choice(self._TEMPLATES_NEGATIVE)
            answer = "negative"
            reason = (
                "no x-intercepts means the corresponding equation has no real "
                "roots, which only happens when $\\Delta < 0$"
            )

        sign_symbol = {"positive": ">", "zero": "=", "negative": "<"}[category]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (category, description)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"The graph of $y = ax^2 + bx + c$ is {description}. "
                "Is the discriminant $\\Delta$ positive, zero, or negative?"
            ),
            answer_latex=f"$\\Delta$ is {answer} ($\\Delta {sign_symbol} 0$).",
            hints=[
                "Count the number of times the parabola meets the x-axis.",
                r"Two hits mean $\Delta > 0$, one hit means $\Delta = 0$, and no hits mean $\Delta < 0$.",
            ],
            solution_steps_latex=[
                "The x-intercepts of $y = ax^2 + bx + c$ are the real solutions of $ax^2 + bx + c = 0$.",
                f"Here the parabola is {description}, so {reason}.",
                f"Therefore $\\Delta {sign_symbol} 0$, meaning the discriminant is {answer}.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-visualization"],
        )


# ===========================================================================
# Topic 2: graphing_quadratic_functions
# ===========================================================================

@register
class FindVertexFromStandardForm(Generator):
    """Given y = ax^2 + bx + c in standard form, find the vertex (h, k)."""
    generator_id = "find_vertex_from_standard_form"
    topic_slug = "graphing_quadratic_functions"
    display_name = "Find the vertex of y = ax^2 + bx + c"

    _H_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _A_CHOICES = {"easy": (-2, -1, 1, 2), "medium": (-3, -2, -1, 1, 2, 3), "hard": (-4, -3, -2, -1, 1, 2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        # Backward construct: pick integer vertex (h, k) and nonzero a,
        # expand a(x - h)^2 + k = a x^2 - 2ah x + (a h^2 + k).
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        a = rng.choice(self._A_CHOICES[difficulty])
        b = -2 * a * h
        c = a * h * h + k

        eq_latex = _format_quadratic_equation(a, b, c).replace(" = 0", "")
        eq_latex = f"y = {eq_latex}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the vertex of the parabola ${eq_latex}$."
            ),
            answer_latex=f"$({h}, {k})$",
            hints=[
                r"The x-coordinate of the vertex is $x = -\dfrac{b}{2a}$.",
                r"Once you have $x$, compute $y$ by substituting back into the original equation.",
                f"Here $a = {a}$ and $b = {b}$.",
            ],
            solution_steps_latex=[
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                (
                    f"Compute the vertex x-coordinate: "
                    f"$x = -\\dfrac{{b}}{{2a}} = -\\dfrac{{{b}}}{{2({a})}} = {h}$."
                ),
                (
                    f"Substitute $x = {h}$ into the equation: "
                    f"$y = ({a})({h})^2 + ({b})({h}) + ({c}) = {k}$."
                ),
                f"The vertex is $({h}, {k})$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-formula-substitution"],
        )


@register
class AxisOfSymmetryFromStandardForm(Generator):
    """Given y = ax^2 + bx + c, state the axis of symmetry as x = -b/(2a)."""
    generator_id = "axis_of_symmetry_from_standard_form"
    topic_slug = "graphing_quadratic_functions"
    display_name = "Find the axis of symmetry of y = ax^2 + bx + c"

    _H_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _A_CHOICES = {"easy": (-2, -1, 1, 2), "medium": (-3, -2, -1, 1, 2, 3), "hard": (-4, -3, -2, -1, 1, 2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        # Backward construct with integer axis h.
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        a = rng.choice(self._A_CHOICES[difficulty])
        b = -2 * a * h
        c = a * h * h + k

        eq_latex = _format_quadratic_expr(a, b, c)
        eq_latex = f"y = {eq_latex}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the equation of the axis of symmetry of ${eq_latex}$."
            ),
            answer_latex=f"$x = {h}$",
            hints=[
                r"The axis of symmetry of a parabola in standard form is the vertical line $x = -\dfrac{b}{2a}$.",
                f"Here $a = {a}$ and $b = {b}$.",
            ],
            solution_steps_latex=[
                f"Read off $a = {a}$ and $b = {b}$ from the equation.",
                (
                    f"Apply the formula: $x = -\\dfrac{{b}}{{2a}} = "
                    f"-\\dfrac{{{b}}}{{2({a})}} = {h}$."
                ),
                f"The axis of symmetry is the vertical line $x = {h}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-formula-substitution"],
        )


@register
class IdentifyParabolaFeatures(Generator):
    """Given a quadratic, identify direction, y-intercept, and vertex."""
    generator_id = "identify_parabola_features"
    topic_slug = "graphing_quadratic_functions"
    display_name = "Identify direction, y-intercept, and vertex of a parabola"

    _H_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _A_CHOICES = {"easy": (-2, -1, 1, 2), "medium": (-3, -2, -1, 1, 2, 3), "hard": (-4, -3, -2, -1, 1, 2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        a = rng.choice(self._A_CHOICES[difficulty])
        b = -2 * a * h
        c = a * h * h + k

        direction = "upward" if a > 0 else "downward"
        eq_latex = _format_quadratic_expr(a, b, c)
        eq_latex = f"y = {eq_latex}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the parabola ${eq_latex}$: (a) does it open upward or "
                "downward? (b) What is its y-intercept? (c) What is its vertex?"
            ),
            answer_latex=(
                f"(a) {direction}; (b) $y$-intercept $= {c}$; "
                f"(c) vertex $= ({h}, {k})$."
            ),
            hints=[
                "The parabola opens upward when the leading coefficient $a$ is positive and downward when it is negative.",
                r"The $y$-intercept is the constant term $c$.",
                r"The vertex has $x = -\dfrac{b}{2a}$; substitute back to get $y$.",
            ],
            solution_steps_latex=[
                f"Identify $a = {a}$, $b = {b}$, $c = {c}$.",
                (
                    f"(a) Because $a = {a}$ is {'positive' if a > 0 else 'negative'}, "
                    f"the parabola opens {direction}."
                ),
                f"(b) The y-intercept equals the constant term, so $y = {c}$.",
                (
                    f"(c) Vertex x-coordinate: $-\\dfrac{{{b}}}{{2({a})}} = {h}$. "
                    f"Substitute: $y = ({a})({h})^2 + ({b})({h}) + ({c}) = {k}$. "
                    f"Vertex $= ({h}, {k})$."
                ),
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-multi-step"],
        )


# ===========================================================================
# Topic 3: quadratic_functions
# ===========================================================================

@register
class EvaluateQuadraticFunction(Generator):
    """Given f(x) = ax^2 + bx + c, evaluate f(k) for a single input."""
    generator_id = "evaluate_quadratic_function"
    topic_slug = "quadratic_functions"
    display_name = "Evaluate f(x) = ax^2 + bx + c at a given input"

    _A_CHOICES = {"easy": (1, 1, 2, -1), "medium": (1, 2, -1, -2, 3), "hard": (1, 2, 3, -2, -3, 4)}
    _B_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _C_RANGES = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}
    _K_RANGES = {"easy": (-4, 5), "medium": (-6, 7), "hard": (-8, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        b_lo, b_hi = self._B_RANGES[difficulty]
        c_lo, c_hi = self._C_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        b = rng.randint(b_lo, b_hi)
        c = rng.randint(c_lo, c_hi)
        k = rng.randint(k_lo, k_hi)

        value = a * k * k + b * k + c

        func_latex = _format_quadratic_function(a, b, c)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given $f(x) = {_format_quadratic_expr(a, b, c)}$, find $f({k})$."
            ),
            answer_latex=f"$f({k}) = {value}$",
            hints=[
                f"Substitute $x = {k}$ into every occurrence of $x$ in the function.",
                f"Be careful with squaring a negative: $({k})^2 = {k * k}$.",
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {k}$: "
                    f"$f({k}) = ({a})({k})^2 + ({b})({k}) + ({c})$."
                ),
                (
                    f"Simplify: $f({k}) = ({a})({k * k}) + ({b * k}) + ({c}) = "
                    f"{a * k * k} + ({b * k}) + ({c}) = {value}$."
                ),
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-formula-substitution"],
        )


@register
class VertexFormIdentifyVertex(Generator):
    """Given f(x) = a(x - h)^2 + k in vertex form, state the vertex and direction."""
    generator_id = "vertex_form_identify_vertex"
    topic_slug = "quadratic_functions"
    display_name = "Identify the vertex of f(x) = a(x - h)^2 + k"

    _H_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _A_CHOICES = {"easy": (-2, -1, 1, 2), "medium": (-3, -2, -1, 1, 2, 3), "hard": (-4, -3, -2, -1, 1, 2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        a = rng.choice(self._A_CHOICES[difficulty])
        while h == 0 and k == 0:
            # avoid degenerate f(x) = ax^2 where both shifts are zero; still valid but dull
            h = rng.randint(h_lo, h_hi)
            k = rng.randint(k_lo, k_hi)

        direction = "upward" if a > 0 else "downward"
        func_latex = _format_function_vertex(a, h, k)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, h, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the vertex of ${func_latex}$ and whether the parabola "
                "opens upward or downward."
            ),
            answer_latex=f"Vertex $({h}, {k})$; opens {direction}.",
            hints=[
                r"Vertex form is $f(x) = a(x - h)^2 + k$. The vertex is $(h, k)$.",
                "Watch the sign inside the parentheses --- a minus sign gives $h$ directly, a plus sign flips the sign.",
                f"The parabola opens upward if $a > 0$ and downward if $a < 0$.",
            ],
            solution_steps_latex=[
                (
                    f"Match ${func_latex}$ to the template "
                    f"$f(x) = a(x - h)^2 + k$."
                ),
                f"Read off $h = {h}$ and $k = {k}$, so the vertex is $({h}, {k})$.",
                (
                    f"Since $a = {a}$ is "
                    f"{'positive' if a > 0 else 'negative'}, the parabola opens {direction}."
                ),
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-visualization"],
        )


@register
class StandardToVertexFormCompletingSquare(Generator):
    """Convert f(x) = x^2 + bx + c to vertex form f(x) = (x - h)^2 + k by completing the square."""
    generator_id = "standard_to_vertex_form_via_completing_square"
    topic_slug = "quadratic_functions"
    display_name = "Convert x^2 + bx + c to vertex form by completing the square"

    _H_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        # Backward construct: pick integer h, k; then (x - h)^2 + k = x^2 - 2hx + (h^2 + k).
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        while h == 0:
            # avoid the trivial case where no shift is needed
            h = rng.randint(h_lo, h_hi)
        b = -2 * h  # always even; constraint satisfied
        c = h * h + k

        standard_latex = _format_quadratic_function(1, b, c)
        vertex_latex = _format_function_vertex(1, h, k)
        half_b = b // 2
        half_b_sq = half_b * half_b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Rewrite ${standard_latex}$ in vertex form by completing the "
                "square."
            ),
            answer_latex=f"${vertex_latex}$",
            hints=[
                r"Take half of the $x$-coefficient, square it, then add and subtract that value.",
                f"Half of ${b}$ is ${half_b}$. Its square is ${half_b_sq}$.",
                r"Group the perfect-square trinomial into $(x - h)^2$ and combine the remaining constants.",
            ],
            solution_steps_latex=[
                f"Begin with ${standard_latex}$.",
                (
                    f"Half of the $x$-coefficient: $\\dfrac{{{b}}}{{2}} = {half_b}$. "
                    f"Its square: $({half_b})^2 = {half_b_sq}$."
                ),
                (
                    f"Add and subtract ${half_b_sq}$: "
                    f"$f(x) = x^2 + ({b})x + {half_b_sq} - {half_b_sq} + ({c})$."
                ),
                (
                    f"Group the perfect square: "
                    f"$f(x) = (x + ({half_b}))^2 + ({c - half_b_sq})$."
                ),
                f"Simplify signs: ${vertex_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 4: applications_of_quadratic_functions
# ===========================================================================

# Projectile scenario templates: (subject, launch_phrase)
_PROJECTILE_SCENARIOS = [
    ("toy rocket", "launched from the top of a {h0}-foot cliff"),
    ("firework", "set off from a platform {h0} feet above the ground"),
    ("cannonball", "fired from a wall {h0} feet high"),
    ("kicked ball", "launched from a rooftop {h0} feet above the field"),
    ("signal flare", "released from a ship deck {h0} feet above the water"),
    ("water balloon", "tossed from a balcony {h0} feet off the ground"),
]

# Rectangle scenario templates: (setting, perimeter_phrase)
_RECT_SCENARIOS_CLOSED = [
    ("vegetable garden", "enclose a rectangular vegetable garden"),
    ("dog pen", "build a rectangular dog pen"),
    ("playground", "fence in a rectangular playground"),
    ("patio", "border a rectangular patio"),
]
_RECT_SCENARIOS_WALL = [
    ("garden along a barn wall", "enclose a rectangular garden using an existing barn wall as one side"),
    ("dog run against a house", "build a rectangular dog run with the side of the house serving as one wall"),
    ("field beside a cliff", "fence off a rectangular field using a cliff face as one side"),
    ("chicken coop against a fence", "enclose a rectangular chicken coop using an existing fence as one side"),
]


@register
class ProjectileMaxHeight(Generator):
    """Find the maximum height of h(t) = -16t^2 + v0*t + h0."""
    generator_id = "projectile_max_height"
    topic_slug = "applications_of_quadratic_functions"
    display_name = "Find the maximum height of a projectile"
    supports_word_problems = True

    # v0 must be a multiple of 16 so t_max = v0 / 32 is clean (integer or half-integer);
    # picking even multiples of 16 (i.e., multiples of 32) makes t_max an integer.
    _V0_CHOICES = {
        "easy": (32, 64, 96),
        "medium": (32, 64, 96, 128, 160),
        "hard": (64, 96, 128, 160, 192, 224),
    }
    _H0_RANGES = {"easy": (0, 40), "medium": (0, 120), "hard": (20, 240)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        v0 = rng.choice(self._V0_CHOICES[difficulty])
        h0_lo, h0_hi = self._H0_RANGES[difficulty]
        h0 = rng.randint(h0_lo, h0_hi)

        t_max = v0 // 32  # integer because v0 is a multiple of 32
        max_height = h0 + (v0 * v0) // 64  # integer because v0^2 divisible by 64

        subject, launch_phrase = rng.choice(_PROJECTILE_SCENARIOS)
        launch_phrase = launch_phrase.format(h0=h0)

        model_latex = f"h(t) = -16t^2 + {v0}t + {h0}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (v0, h0, subject)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {subject} is {launch_phrase} with an initial upward "
                f"velocity of ${v0}$ feet per second. Its height above the "
                f"ground in feet after $t$ seconds is ${model_latex}$. "
                "Find the maximum height the projectile reaches and the time "
                "at which it occurs."
            ),
            answer_latex=(
                f"Maximum height ${max_height}$ feet, reached at $t = {t_max}$ seconds."
            ),
            hints=[
                r"The maximum of $h(t) = at^2 + bt + c$ occurs at $t = -\dfrac{b}{2a}$.",
                f"Here $a = -16$ and $b = {v0}$.",
                r"Once you know the time, substitute back into $h(t)$ to get the height.",
            ],
            solution_steps_latex=[
                f"Read off $a = -16$, $b = {v0}$, $c = {h0}$ from ${model_latex}$.",
                (
                    f"Time of maximum: $t = -\\dfrac{{b}}{{2a}} = "
                    f"-\\dfrac{{{v0}}}{{2(-16)}} = -\\dfrac{{{v0}}}{{-32}} = {t_max}$ seconds."
                ),
                (
                    f"Maximum height: $h({t_max}) = -16({t_max})^2 + {v0}({t_max}) + {h0} "
                    f"= {-16 * t_max * t_max} + {v0 * t_max} + {h0} = {max_height}$ feet."
                ),
                f"The {subject} reaches a peak of ${max_height}$ feet after ${t_max}$ seconds.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-modeling"],
        )


@register
class ProjectileTimeToGround(Generator):
    """Find the positive root of h(t) = -16t^2 + v0*t + h0 = 0."""
    generator_id = "projectile_time_to_ground"
    topic_slug = "applications_of_quadratic_functions"
    display_name = "Find when a projectile hits the ground"
    supports_word_problems = True

    # Backward construct: pick integer t_ground and a second root r < 0 such that the
    # sum of roots and product of roots give integer v0, h0.
    # -16 t^2 + v0 t + h0 = 0  <=>  16 t^2 - v0 t - h0 = 0
    # Roots t_g, r satisfy: t_g + r = v0/16, t_g * r = -h0/16.
    # Pick r = -t_g / j for small integer j, or simpler: pick r as a negative integer.
    # Then v0 = 16*(t_g + r) and h0 = -16*t_g*r. We need v0 > 0, h0 >= 0.
    _T_CHOICES = {
        "easy": (2, 3, 4, 5),
        "medium": (3, 4, 5, 6, 7),
        "hard": (4, 5, 6, 7, 8, 9, 10),
    }
    # Negative companion roots (kept small so coefficients stay friendly).
    _R_CHOICES = {
        "easy": (-1, -2),
        "medium": (-1, -2, -3),
        "hard": (-1, -2, -3, -4),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        t_ground = rng.choice(self._T_CHOICES[difficulty])
        r = rng.choice(self._R_CHOICES[difficulty])
        # v0 = 16 (t_g + r), h0 = -16 t_g r.
        # We need v0 > 0 -> t_g + r > 0 (always true since |t_g| > |r|).
        v0 = 16 * (t_ground + r)
        h0 = -16 * t_ground * r  # positive since r < 0

        subject, launch_phrase = rng.choice(_PROJECTILE_SCENARIOS)
        launch_phrase = launch_phrase.format(h0=h0)

        model_latex = f"h(t) = -16t^2 + {v0}t + {h0}"
        # Simpler factoring form: -16 t^2 + v0 t + h0 = -16 (t - t_g)(t - r)
        # After dividing -16t^2 + v0*t + h0 = 0 by -16: t^2 - (v0/16) t - (h0/16) = 0.
        sum_roots = t_ground + r
        prod_roots = t_ground * r

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (v0, h0, subject)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A {subject} is {launch_phrase} with an initial upward "
                f"velocity of ${v0}$ feet per second. Its height is modeled "
                f"by ${model_latex}$, where $t$ is in seconds. Find the time "
                "when the projectile hits the ground."
            ),
            answer_latex=f"$t = {t_ground}$ seconds",
            hints=[
                r"The projectile hits the ground when $h(t) = 0$.",
                r"Solve the resulting quadratic using the quadratic formula or by factoring.",
                "Discard any negative solution, since time must be non-negative.",
            ],
            solution_steps_latex=[
                (
                    f"Set $h(t) = 0$: $-16t^2 + {v0}t + {h0} = 0$."
                ),
                (
                    f"Divide both sides by $-16$ (flipping signs): "
                    f"$t^2 - {sum_roots}t - {prod_roots} = 0$."
                ),
                (
                    f"Factor: $(t - {t_ground})(t - ({r})) = 0$, so "
                    f"$t = {t_ground}$ or $t = {r}$."
                ),
                f"Since time must be non-negative, $t = {t_ground}$ seconds.",
            ],
            tags=["#branch-algebra-1", "#topic-quadratics", "#skill-modeling"],
        )


@register
class RectangleMaxArea(Generator):
    """Maximize the area of a rectangle given a fixed amount of fencing."""
    generator_id = "rectangle_max_area"
    topic_slug = "applications_of_quadratic_functions"
    display_name = "Maximize the area of a rectangle with fixed fencing"
    supports_word_problems = True

    # For the closed case (4 sides), P must be a multiple of 4 so P/4 is integer.
    # For the wall case (3 sides), P must be a multiple of 4 so P/4 is integer width.
    _P_CHOICES_CLOSED = {
        "easy": (20, 24, 28, 32, 40),
        "medium": (40, 48, 60, 72, 80, 96),
        "hard": (80, 100, 120, 140, 160, 200),
    }
    _P_CHOICES_WALL = {
        "easy": (20, 24, 28, 40, 48),
        "medium": (40, 48, 60, 80, 100),
        "hard": (100, 120, 160, 200, 240),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(["closed", "wall"])

        if case == "closed":
            P = rng.choice(self._P_CHOICES_CLOSED[difficulty])
            setting, perimeter_phrase = rng.choice(_RECT_SCENARIOS_CLOSED)
            side = P // 4  # optimal L = W = P/4
            area = side * side
            return Problem(
                id=make_problem_id(self.generator_id, difficulty, (P, "closed", setting)),
                generator_id=self.generator_id,
                topic_slug=self.topic_slug,
                difficulty=difficulty,
                statement_latex=(
                    f"You have ${P}$ feet of fencing and want to "
                    f"{perimeter_phrase}. What dimensions will maximize "
                    "the enclosed area, and what is that maximum area?"
                ),
                answer_latex=(
                    f"$L = W = {side}$ feet; maximum area $= {area}$ square feet."
                ),
                hints=[
                    r"Let $L$ and $W$ be the length and width. The perimeter constraint is $2L + 2W = P$.",
                    r"Solve for one variable and substitute into $A = LW$ to get a quadratic in a single variable.",
                    r"The maximum of $A(W) = -W^2 + (P/2) W$ occurs at the vertex.",
                ],
                solution_steps_latex=[
                    (
                        f"Set up the perimeter: $2L + 2W = {P}$, so $L = {P // 2} - W$."
                    ),
                    (
                        f"Area: $A(W) = LW = ({P // 2} - W) W = -W^2 + {P // 2} W$."
                    ),
                    (
                        f"Vertex W-coordinate: $W = -\\dfrac{{b}}{{2a}} = "
                        f"-\\dfrac{{{P // 2}}}{{2(-1)}} = {side}$."
                    ),
                    (
                        f"Then $L = {P // 2} - {side} = {side}$, so both sides equal "
                        f"${side}$ feet."
                    ),
                    f"Maximum area: $A = {side} \\cdot {side} = {area}$ square feet.",
                ],
                tags=["#branch-algebra-1", "#topic-quadratics", "#skill-modeling"],
            )
        else:
            P = rng.choice(self._P_CHOICES_WALL[difficulty])
            setting, perimeter_phrase = rng.choice(_RECT_SCENARIOS_WALL)
            # Fencing covers L + 2W = P. Optimal W = P/4, L = P/2.
            W = P // 4
            L = P // 2
            area = L * W
            return Problem(
                id=make_problem_id(self.generator_id, difficulty, (P, "wall", setting)),
                generator_id=self.generator_id,
                topic_slug=self.topic_slug,
                difficulty=difficulty,
                statement_latex=(
                    f"You have ${P}$ feet of fencing and want to "
                    f"{perimeter_phrase}, so only three sides need fencing. "
                    "What dimensions will maximize the enclosed area, and "
                    "what is that maximum area?"
                ),
                answer_latex=(
                    f"Length $= {L}$ feet (parallel to the wall), width $= {W}$ feet; "
                    f"maximum area $= {area}$ square feet."
                ),
                hints=[
                    r"Let $L$ be parallel to the wall and $W$ perpendicular to it. Only three sides are fenced: $L + 2W = P$.",
                    r"Substitute $L = P - 2W$ into $A = L W$ to get a quadratic in $W$.",
                    r"The vertex of $A(W) = -2W^2 + P W$ gives the optimal width.",
                ],
                solution_steps_latex=[
                    (
                        f"Fencing constraint: $L + 2W = {P}$, so $L = {P} - 2W$."
                    ),
                    (
                        f"Area: $A(W) = L W = ({P} - 2W) W = -2W^2 + {P} W$."
                    ),
                    (
                        f"Vertex: $W = -\\dfrac{{b}}{{2a}} = "
                        f"-\\dfrac{{{P}}}{{2(-2)}} = \\dfrac{{{P}}}{{4}} = {W}$."
                    ),
                    (
                        f"Then $L = {P} - 2({W}) = {L}$."
                    ),
                    f"Maximum area: $A = {L} \\cdot {W} = {area}$ square feet.",
                ],
                tags=["#branch-algebra-1", "#topic-quadratics", "#skill-modeling"],
            )
