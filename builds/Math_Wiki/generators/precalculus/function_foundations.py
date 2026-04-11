"""Function foundations generators (Wave C pre-calculus).

Five topic slugs covered across introductory function / graph material:

- algebraic_functions                (Algebraic_Functions.md)
- cartesian_plane                    (Cartesian_Plane.md)
- graphs_of_equations                (Graphs_Of_Equations.md)
- graphs_of_functions                (Graphs_Of_Functions.md)
- introduction_to_functions          (Introduction_To_Functions.md)

Fifteen generators total (3 per topic). Backward construction is used
throughout: parameters are chosen so that the answer is a clean small
integer or interval, and the statement is derived from those choices.
SymPy is used for symbolic substitution, exact interval endpoints, and
closed-form evaluation wherever arithmetic is required.
"""
from __future__ import annotations

import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Tag bundles
# ---------------------------------------------------------------------------

FUNCTION_TAGS = ["#branch-pre-calculus", "#topic-functions"]
ANALYTIC_TAGS = ["#branch-pre-calculus", "#topic-analytic-geometry"]

SKILL_PROCEDURAL = "#skill-procedural-calculation"
SKILL_ALGEBRAIC = "#skill-algebraic-manipulation"
SKILL_VISUALIZATION = "#skill-visualization"
SKILL_MULTI_STEP = "#skill-multi-step"
SKILL_FORMULA_SUB = "#skill-formula-substitution"


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _signed_const(n: int) -> str:
    """Render a signed constant for use inside polynomial expressions.

    Examples
    --------
    >>> _signed_const(3)
    '+ 3'
    >>> _signed_const(-5)
    '- 5'
    """
    if n >= 0:
        return f"+ {n}"
    return f"- {abs(n)}"


def _linear_latex(a: int, b: int) -> str:
    """Render the linear expression ``a*x + b`` with correct signs.

    Assumes ``a != 0`` for a proper linear expression, though any integer
    ``a`` is allowed.
    """
    if a == 1:
        lead = "x"
    elif a == -1:
        lead = "-x"
    else:
        lead = f"{a}x"
    if b == 0:
        return lead
    return f"{lead} {_signed_const(b)}"


def _quadratic_latex(a: int, b: int, c: int) -> str:
    """Render the quadratic expression ``a*x^2 + b*x + c`` with correct signs."""
    if a == 1:
        out = "x^2"
    elif a == -1:
        out = "-x^2"
    else:
        out = f"{a}x^2"
    if b != 0:
        if b == 1:
            out += " + x"
        elif b == -1:
            out += " - x"
        else:
            out += f" {_signed_const(b)}x"
    if c != 0:
        out += f" {_signed_const(c)}"
    return out


# ===========================================================================
# Topic 1: algebraic_functions
# ===========================================================================


@register
class ClassifyFunctionAlgebraicOrTranscendental(Generator):
    """Classify a function as algebraic or transcendental.

    Backward: pick a function description and its known classification.
    Algebraic = polynomial, rational, or involves roots. Transcendental =
    exponential, logarithmic, or trigonometric.
    """

    generator_id = "classify_function_algebraic_or_transcendental"
    topic_slug = "algebraic_functions"
    display_name = "Classify a function as algebraic or transcendental"

    bank_count_per_difficulty = 15

    # (latex_expression, label, short_reason)
    _FUNCTIONS = (
        (r"f(x) = 3x^4 - 2x + 1", "algebraic", "a polynomial"),
        (r"f(x) = \sqrt{x - 2}", "algebraic", "an even root of a polynomial"),
        (r"f(x) = \dfrac{1}{x + 3}", "algebraic", "a rational function"),
        (r"f(x) = \dfrac{2x}{x^2 + 1}", "algebraic", "a rational function"),
        (r"f(x) = \sqrt[3]{x} + 5", "algebraic", "a root of a polynomial"),
        (r"f(x) = 7x^{2/3}", "algebraic", "a rational-exponent power"),
        (r"f(x) = (x - 1)^{5}", "algebraic", "a polynomial written in factored power form"),
        (r"f(x) = e^{x}", "transcendental", "an exponential"),
        (r"f(x) = 2^{x}", "transcendental", "an exponential"),
        (r"f(x) = \ln x", "transcendental", "a logarithm"),
        (r"f(x) = \log_{10}(x + 1)", "transcendental", "a logarithm"),
        (r"f(x) = \sin x", "transcendental", "a trigonometric function"),
        (r"f(x) = \cos(2x)", "transcendental", "a trigonometric function"),
        (r"f(x) = \tan x", "transcendental", "a trigonometric function"),
        (r"f(x) = 3e^{-x}", "transcendental", "an exponential"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._FUNCTIONS))
        expr_latex, label, reason = self._FUNCTIONS[idx]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Classify ${expr_latex}$ as an algebraic or a transcendental function."
            ),
            answer_latex=f"{label.capitalize()}",
            hints=[
                (
                    "Algebraic functions are built from polynomials, rational "
                    "expressions, and roots using only +, -, x, /, and integer or "
                    "rational powers."
                ),
                (
                    "Transcendental functions include exponentials $a^{x}$ or "
                    r"$e^{x}$, logarithms $\log_{a} x$, and trigonometric "
                    "functions such as $\\sin$, $\\cos$, $\\tan$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Look at the structure of ${expr_latex}$."
                ),
                (
                    f"Because the function is {reason}, it is a {label} function."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_PROCEDURAL],
        )


@register
class DomainOfRadicalExpression(Generator):
    """Find the domain of $f(x) = \\sqrt{x - k}$.

    Backward: pick integer ``k``; domain is ``x >= k``.
    """

    generator_id = "domain_of_radical_expression"
    topic_slug = "algebraic_functions"
    display_name = "Determine the domain of a square-root function"

    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        # Half the time use the form sqrt(x - k); the rest use sqrt(k - x)
        # only for medium/hard, and even there we stick with sqrt(x - k) to
        # keep the answer uniformly x >= k.
        inner_latex = f"x {_signed_const(-k)}" if k != 0 else "x"
        expr_latex = rf"\sqrt{{{inner_latex}}}"

        answer_latex = f"$x \\geq {k}$"
        interval_latex = rf"[{k},\ \infty)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Give the domain of $f(x) = {expr_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "For a real square root, the expression inside the radical "
                    "must be non-negative."
                ),
                (
                    f"Set $x {_signed_const(-k)} \\geq 0$ and solve for $x$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Require the radicand to be non-negative: "
                    f"$x {_signed_const(-k)} \\geq 0$."
                ),
                (
                    f"Solve for $x$: $x \\geq {k}$."
                ),
                (
                    f"In interval notation the domain is ${interval_latex}$."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_ALGEBRAIC],
        )


@register
class DomainOfRationalExpression(Generator):
    """Find the excluded values of a rational function $1/(x - k)$ or $1/((x-a)(x-b))$.

    Backward: pick integer denominator roots.
    """

    generator_id = "domain_of_rational_expression"
    topic_slug = "algebraic_functions"
    display_name = "Determine the domain of a rational function"

    _K_RANGES = {"easy": (-7, 7), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]

        if difficulty == "easy":
            roots = [rng.randint(k_lo, k_hi)]
        else:
            roots = [rng.randint(k_lo, k_hi), rng.randint(k_lo, k_hi)]
            while roots[1] == roots[0]:
                roots[1] = rng.randint(k_lo, k_hi)

        if len(roots) == 1:
            k = roots[0]
            denom_latex = f"x {_signed_const(-k)}" if k != 0 else "x"
            expr_latex = rf"\dfrac{{1}}{{{denom_latex}}}"
            excluded = [k]
        else:
            a, b = roots
            left = f"(x {_signed_const(-a)})" if a != 0 else "x"
            right = f"(x {_signed_const(-b)})" if b != 0 else "x"
            expr_latex = rf"\dfrac{{1}}{{{left}{right}}}"
            excluded = sorted(roots)

        if len(excluded) == 1:
            excluded_latex = f"$x \\ne {excluded[0]}$"
            domain_words = (
                f"all real numbers except $x = {excluded[0]}$"
            )
        else:
            excluded_latex = (
                f"$x \\ne {excluded[0]}$ and $x \\ne {excluded[1]}$"
            )
            domain_words = (
                f"all real numbers except $x = {excluded[0]}$ and $x = {excluded[1]}$"
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(roots)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the domain of $f(x) = {expr_latex}$."
            ),
            answer_latex=excluded_latex,
            hints=[
                (
                    "A rational function is undefined wherever its denominator "
                    "equals zero."
                ),
                (
                    "Set the denominator equal to zero and solve; remove those "
                    "values from the real numbers."
                ),
            ],
            solution_steps_latex=[
                (
                    "Find the zeros of the denominator by setting it equal to zero."
                ),
                (
                    f"Solve to find the excluded values: "
                    f"{', '.join(f'$x = {r}$' for r in excluded)}."
                ),
                (
                    f"The domain is {domain_words}."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_ALGEBRAIC],
        )


# ===========================================================================
# Topic 2: cartesian_plane
# ===========================================================================


@register
class IdentifyInterceptsFromEquation(Generator):
    """Find x- and y-intercepts of a linear or factorable quadratic.

    Backward: for linear ``y = m x + b``, x-intercept is $-b/m$. To avoid
    fractions, pick ``b`` divisible by ``m``. For quadratic, pick two
    integer roots and expand.
    """

    generator_id = "identify_intercepts_from_equation"
    topic_slug = "cartesian_plane"
    display_name = "Identify x- and y-intercepts from an equation"

    _M_RANGES = {"easy": (1, 4), "medium": (1, 6), "hard": (1, 8)}
    _ROOT_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        shape = rng.choice(["linear", "quadratic"])

        if shape == "linear":
            m_lo, m_hi = self._M_RANGES[difficulty]
            m = rng.choice([-1, 1]) * rng.randint(m_lo, m_hi)
            x_int = rng.randint(-6, 6)
            b = -m * x_int  # so y = m(x - x_int) => y-int at (0, -m*x_int) = (0, b)
            y_int = b
            equation_latex = f"y = {_linear_latex(m, b)}"
            x_int_point = f"({x_int},\\ 0)"
            y_int_point = f"(0,\\ {y_int})"
            answer_latex = (
                f"$x$-intercept: ${x_int_point}$; $y$-intercept: ${y_int_point}$"
            )
            steps = [
                (
                    f"To find the $y$-intercept, set $x = 0$: "
                    f"$y = {m}(0) {_signed_const(b)} = {y_int}$."
                ),
                (
                    f"To find the $x$-intercept, set $y = 0$ and solve "
                    f"${_linear_latex(m, b)} = 0$."
                ),
                (
                    f"Solving gives $x = {x_int}$. The intercepts are "
                    f"${x_int_point}$ and ${y_int_point}$."
                ),
            ]
            params = ("lin", m, b)
        else:
            r_lo, r_hi = self._ROOT_RANGES[difficulty]
            r1 = rng.randint(r_lo, r_hi)
            r2 = rng.randint(r_lo, r_hi)
            while r2 == r1:
                r2 = rng.randint(r_lo, r_hi)
            # y = (x - r1)(x - r2) = x^2 - (r1 + r2) x + r1*r2
            b = -(r1 + r2)
            c = r1 * r2
            equation_latex = f"y = {_quadratic_latex(1, b, c)}"
            x_ints = sorted([r1, r2])
            y_int = c
            x_int_point_1 = f"({x_ints[0]},\\ 0)"
            x_int_point_2 = f"({x_ints[1]},\\ 0)"
            y_int_point = f"(0,\\ {y_int})"
            answer_latex = (
                f"$x$-intercepts: ${x_int_point_1}$, ${x_int_point_2}$; "
                f"$y$-intercept: ${y_int_point}$"
            )
            steps = [
                (
                    f"For the $y$-intercept, set $x = 0$: "
                    f"$y = 0^2 {_signed_const(b) if b != 0 else ''} "
                    f"{_signed_const(c)} = {y_int}$."
                ),
                (
                    f"For the $x$-intercepts, set $y = 0$ and factor: "
                    f"$(x - ({r1}))(x - ({r2})) = 0$."
                ),
                (
                    f"So $x = {x_ints[0]}$ or $x = {x_ints[1]}$, giving "
                    f"intercepts ${x_int_point_1}$, ${x_int_point_2}$, and "
                    f"${y_int_point}$."
                ),
            ]
            params = ("quad", r1, r2)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Identify the $x$- and $y$-intercepts of ${equation_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                "The $y$-intercept is found by substituting $x = 0$.",
                "The $x$-intercepts are found by setting $y = 0$ and solving for $x$.",
            ],
            solution_steps_latex=steps,
            tags=ANALYTIC_TAGS + [SKILL_MULTI_STEP],
        )


@register
class CheckSymmetryFromEquation(Generator):
    """Test a simple equation for symmetry across the $x$-axis, $y$-axis, or origin.

    Backward: pick an equation from a small catalogue whose symmetry is known.
    """

    generator_id = "check_symmetry_from_equation"
    topic_slug = "cartesian_plane"
    display_name = "Test an equation for axis or origin symmetry"

    bank_count_per_difficulty = 15

    # (equation, symmetry_label, short_reason)
    # symmetry_label is one of "x-axis", "y-axis", "origin", "both axes", "none"
    _CASES = (
        (r"y = x^2", "y-axis", "replacing $x$ with $-x$ yields $y = (-x)^2 = x^2$, the same equation"),
        (r"y = x^2 - 4", "y-axis", "replacing $x$ with $-x$ leaves $y = x^2 - 4$ unchanged"),
        (r"y = x^3", "origin", "replacing $(x, y)$ with $(-x, -y)$ gives $-y = -x^3$, which is the same equation"),
        (r"y = x^3 - x", "origin", "replacing $(x, y)$ with $(-x, -y)$ leaves the equation unchanged"),
        (r"x^2 + y^2 = 9", "both axes", "the equation is unchanged when $x \\to -x$ or $y \\to -y$"),
        (r"x^2 + y^2 = 25", "both axes", "the equation is unchanged under $x \\to -x$ and under $y \\to -y$"),
        (r"y = |x|", "y-axis", "$|{-x}| = |x|$, so replacing $x$ with $-x$ gives the same equation"),
        (r"x = y^2", "x-axis", "replacing $y$ with $-y$ gives $x = (-y)^2 = y^2$, unchanged"),
        (r"y = x", "origin", "replacing $(x, y)$ with $(-x, -y)$ yields $-y = -x$, which is the same equation"),
        (r"y = 2x^4 + 1", "y-axis", "even powers of $x$ mean $x \\to -x$ leaves the equation unchanged"),
        (r"y = -x^3 + 2x", "origin", "every term has odd degree in $x$, so $(x, y) \\to (-x, -y)$ leaves the equation unchanged"),
        (r"y = x + 1", "none", "none of the three symmetry tests leave the equation unchanged"),
        (r"y^2 = x + 3", "x-axis", "replacing $y$ with $-y$ gives $(-y)^2 = x + 3$, which is the same equation"),
        (r"x^2 - y^2 = 1", "both axes", "the equation is unchanged under both $x \\to -x$ and $y \\to -y$"),
        (r"y = \dfrac{1}{x}", "origin", "replacing $(x, y)$ with $(-x, -y)$ gives $-y = -1/x$, the same equation"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._CASES))
        equation_latex, sym_label, reason = self._CASES[idx]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Test ${equation_latex}$ for symmetry about the $x$-axis, the "
                "$y$-axis, and the origin."
            ),
            answer_latex=f"Symmetry: {sym_label}",
            hints=[
                (
                    r"$y$-axis symmetry: replace $x$ with $-x$; if the equation is "
                    "unchanged, the graph is symmetric about the $y$-axis."
                ),
                (
                    r"$x$-axis: replace $y$ with $-y$. Origin: replace "
                    r"$(x, y)$ with $(-x, -y)$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Apply each symmetry test to ${equation_latex}$."
                ),
                (
                    f"The graph is symmetric about the {sym_label}: {reason}."
                ),
            ],
            tags=ANALYTIC_TAGS + [SKILL_VISUALIZATION],
        )


@register
class ReflectPointAcrossAxisOrOrigin(Generator):
    """Reflect a point across the $x$-axis, the $y$-axis, or the origin.

    Backward: pick integer coordinates and the reflection type.
    """

    generator_id = "reflect_point_across_axis_or_origin"
    topic_slug = "cartesian_plane"
    display_name = "Reflect a point across an axis or the origin"

    _COORD_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._COORD_RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        while a == 0 and b == 0:
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)

        mode = rng.choice(["x-axis", "y-axis", "origin"])
        if mode == "x-axis":
            reflected = (a, -b)
            rule = r"$(x,\ y) \to (x,\ -y)$"
        elif mode == "y-axis":
            reflected = (-a, b)
            rule = r"$(x,\ y) \to (-x,\ y)$"
        else:
            reflected = (-a, -b)
            rule = r"$(x,\ y) \to (-x,\ -y)$"

        given_point = f"({a},\\ {b})"
        answer_point = f"({reflected[0]},\\ {reflected[1]})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, mode)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the reflection of the point $({a},\\ {b})$ across the "
                f"{mode}."
            ),
            answer_latex=f"${answer_point}$",
            hints=[
                (
                    f"Reflection across the {mode} follows the rule {rule}."
                ),
                (
                    "Apply the rule to each coordinate separately."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Reflection across the {mode} sends $(x, y)$ to "
                    f"{rule[1:-1]}."
                ),
                (
                    f"Substitute $x = {a}$, $y = {b}$ into the rule."
                ),
                (
                    f"The image is ${answer_point}$."
                ),
            ],
            tags=ANALYTIC_TAGS + [SKILL_VISUALIZATION],
        )


# ===========================================================================
# Topic 3: graphs_of_equations
# ===========================================================================


@register
class VerifyPointOnEquation(Generator):
    """Check whether a given point lies on a linear or quadratic curve.

    Backward: pick a curve and a candidate point; deliberately mix in points
    that do satisfy the equation and points that do not.
    """

    generator_id = "verify_point_on_equation"
    topic_slug = "graphs_of_equations"
    display_name = "Verify whether a point lies on an equation's graph"

    _A_RANGES = {"easy": (1, 4), "medium": (1, 6), "hard": (-6, 6)}
    _B_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        shape = rng.choice(["linear", "quadratic"])
        a_lo, a_hi = self._A_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]

        a = rng.randint(a_lo, a_hi)
        while a == 0:
            a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        x_val = rng.randint(-5, 5)

        if shape == "linear":
            y_on = a * x_val + b
            equation_latex = f"y = {_linear_latex(a, b)}"
            eqn_sym = sp.Eq(sp.Symbol("y"), a * sp.Symbol("x") + b)
        else:
            # use y = a*x^2 + b to keep it simple
            y_on = a * x_val * x_val + b
            equation_latex = f"y = {_quadratic_latex(a, 0, b)}"
            eqn_sym = sp.Eq(sp.Symbol("y"), a * sp.Symbol("x") ** 2 + b)

        satisfies = rng.choice([True, False])
        if satisfies:
            y_val = y_on
        else:
            delta = rng.choice([-3, -2, -1, 1, 2, 3])
            y_val = y_on + delta

        x_sym, y_sym = sp.symbols("x y")
        substituted_lhs = y_val
        substituted_rhs = a * x_val + b if shape == "linear" else a * x_val * x_val + b
        check_passes = substituted_lhs == substituted_rhs

        answer_word = "Yes" if check_passes else "No"
        answer_latex = (
            f"{answer_word}, the point does {'' if check_passes else 'not '}lie on the graph."
        )

        b_tail = f" {_signed_const(b)}" if b != 0 else ""
        if shape == "linear":
            rhs_after_sub = f"{a}({x_val}){b_tail} = {substituted_rhs}"
        else:
            rhs_after_sub = f"{a}({x_val})^2{b_tail} = {substituted_rhs}"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (shape, a, b, x_val, y_val),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Does the point $({x_val},\\ {y_val})$ lie on the graph of "
                f"${equation_latex}$?"
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Substitute the point's $x$- and $y$-values into the equation."
                ),
                (
                    "If the resulting statement is true, the point lies on the graph; "
                    "otherwise it does not."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Substitute $x = {x_val}$ into the right side: {rhs_after_sub}."
                ),
                (
                    f"Compare to the point's $y$-value: "
                    f"${y_val} {'=' if check_passes else r'\ne'} {substituted_rhs}$."
                ),
                (
                    f"Therefore the point does {'' if check_passes else 'not '}"
                    f"lie on the graph."
                ),
            ],
            tags=ANALYTIC_TAGS + [SKILL_PROCEDURAL],
        )


@register
class FindXInterceptsQuadratic(Generator):
    """Find the $x$-intercepts of a factorable quadratic $y = a(x - r_1)(x - r_2)$.

    Backward: pick roots and a nonzero leading coefficient.
    """

    generator_id = "find_x_intercepts_quadratic"
    topic_slug = "graphs_of_equations"
    display_name = "Find the x-intercepts of a factorable quadratic"

    _ROOT_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _A_CHOICES = {"easy": (1,), "medium": (1, 2, -1), "hard": (1, 2, 3, -1, -2)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ROOT_RANGES[difficulty]
        a = rng.choice(self._A_CHOICES[difficulty])
        r1 = rng.randint(lo, hi)
        r2 = rng.randint(lo, hi)
        while r2 == r1:
            r2 = rng.randint(lo, hi)
        roots = sorted([r1, r2])

        # Expand: a*(x - r1)*(x - r2) = a*x^2 - a*(r1+r2)*x + a*r1*r2
        b_coef = -a * (r1 + r2)
        c_coef = a * r1 * r2

        equation_latex = f"y = {_quadratic_latex(a, b_coef, c_coef)}"
        if a == 1:
            lead_factor = ""
        elif a == -1:
            lead_factor = "-"
        else:
            lead_factor = str(a)
        factored_latex = (
            f"y = {lead_factor}"
            f"(x {_signed_const(-r1)})(x {_signed_const(-r2)})"
        )
        intercept_latex = (
            f"$({roots[0]},\\ 0)$ and $({roots[1]},\\ 0)$"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, r1, r2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find all $x$-intercepts of ${equation_latex}$."
            ),
            answer_latex=intercept_latex,
            hints=[
                (
                    "The $x$-intercepts occur where $y = 0$, so factor the "
                    "quadratic and set each factor equal to zero."
                ),
                (
                    f"After factoring the leading coefficient, look for two "
                    f"integers whose product is ${r1 * r2}$ and whose sum is "
                    f"${r1 + r2}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Set $y = 0$: ${_quadratic_latex(a, b_coef, c_coef)} = 0$."
                ),
                (
                    f"Factor: ${factored_latex}$."
                ),
                (
                    f"Set each factor equal to zero: $x = {r1}$ or $x = {r2}$."
                ),
                (
                    f"The $x$-intercepts are {intercept_latex}."
                ),
            ],
            tags=ANALYTIC_TAGS + [SKILL_ALGEBRAIC],
        )


@register
class MatchEquationToCurveDescription(Generator):
    """Match a verbal description of a curve to the correct equation.

    Backward: pick a description and the matching equation (plus distractors
    are implicit, since the statement names the description).
    """

    generator_id = "match_equation_to_curve_description"
    topic_slug = "graphs_of_equations"
    display_name = "Match a verbal curve description to its equation"

    bank_count_per_difficulty = 15

    # (description, equation, explanation)
    _CASES = (
        ("a parabola opening upward with vertex at the origin", r"y = x^2", "the simplest upward parabola"),
        ("a parabola opening downward with vertex at the origin", r"y = -x^2", "a downward parabola with vertex $(0, 0)$"),
        ("a horizontal line through $y = 3$", r"y = 3", "a constant function"),
        ("a vertical line through $x = -2$", r"x = -2", "a vertical line has the form $x = c$"),
        ("a line through the origin with slope $2$", r"y = 2x", "slope-intercept form with $b = 0$"),
        ("a line through the origin with slope $-1$", r"y = -x", "slope $-1$, $y$-intercept $0$"),
        ("a circle of radius $4$ centred at the origin", r"x^2 + y^2 = 16", "standard form $x^2 + y^2 = r^2$ with $r = 4$"),
        ("a circle of radius $1$ centred at the origin", r"x^2 + y^2 = 1", "the unit circle"),
        ("a parabola opening upward with vertex at $(0, -5)$", r"y = x^2 - 5", "$y = x^2 + k$ shifts vertex to $(0, k)$"),
        ("a cubic that passes through the origin with no other intercepts", r"y = x^3", "the simplest cubic"),
        ("a line with slope $3$ and $y$-intercept $-2$", r"y = 3x - 2", "slope-intercept form $y = mx + b$"),
        ("a parabola with vertex at $(2, 0)$ opening upward", r"y = (x - 2)^2", "vertex form shifted right by $2$"),
        ("a horizontal line through the origin", r"y = 0", "the $x$-axis"),
        ("a vertical line through the origin", r"x = 0", "the $y$-axis"),
        ("a line with slope $-1/2$ through the origin", r"y = -\dfrac{1}{2}x", "slope-intercept form with $b = 0$"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._CASES))
        description, equation, reason = self._CASES[idx]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Give an equation whose graph is {description}."
            ),
            answer_latex=f"${equation}$",
            hints=[
                (
                    "Recognise common curve families: lines $y = mx + b$, parabolas "
                    "$y = ax^2 + bx + c$, circles $x^2 + y^2 = r^2$."
                ),
                (
                    "Match key features (slope, vertex, radius, intercepts) to the "
                    "parameters in the standard form."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the curve family from the description: "
                    f"{description}."
                ),
                (
                    f"Choose parameters so the description matches — {reason}."
                ),
                (
                    f"The equation is ${equation}$."
                ),
            ],
            tags=ANALYTIC_TAGS + [SKILL_VISUALIZATION],
        )


# ===========================================================================
# Topic 4: graphs_of_functions
# ===========================================================================


@register
class VerticalLineTestApply(Generator):
    """Given a relation, decide whether it is a function via the vertical line test.

    Backward: pick a relation description (set of ordered pairs, or described
    graph) and whether it passes the vertical line test.
    """

    generator_id = "vertical_line_test_apply"
    topic_slug = "graphs_of_functions"
    display_name = "Apply the vertical line test to decide if a relation is a function"

    bank_count_per_difficulty = 15

    # (description, is_function, reason)
    _CASES = (
        ("the set $\\{(1, 2), (2, 4), (3, 6), (4, 8)\\}$", True, "each $x$-value appears only once"),
        ("the set $\\{(1, 2), (1, 3), (2, 4)\\}$", False, "$x = 1$ is paired with two different $y$-values"),
        ("the set $\\{(-2, 5), (-1, 5), (0, 5), (1, 5)\\}$", True, "each $x$-value has exactly one $y$-value"),
        ("the set $\\{(0, 1), (0, -1), (1, 0), (-1, 0)\\}$", False, "$x = 0$ is paired with $y = 1$ and $y = -1$"),
        ("the graph $y = x^2$", True, "every vertical line hits the parabola at most once"),
        ("the graph $x^2 + y^2 = 9$", False, "a vertical line through $x = 0$ meets the circle at two points"),
        ("the graph $y = \\sqrt{x}$", True, "every vertical line meets the upper half of the sideways parabola at most once"),
        ("the graph $x = y^2$", False, "a vertical line through $x = 4$ meets the sideways parabola at $y = 2$ and $y = -2$"),
        ("the set $\\{(3, 7), (4, 7), (5, 7)\\}$", True, "each input $x$ has exactly one output $y$"),
        ("the graph $y = 2x + 1$", True, "a line that is not vertical passes the vertical line test"),
        ("the graph $x = 5$", False, "the vertical line $x = 5$ meets itself at infinitely many points"),
        ("the set $\\{(1, 1), (2, 4), (3, 9), (2, 8)\\}$", False, "$x = 2$ is paired with both $y = 4$ and $y = 8$"),
        ("the graph $y = |x|$", True, "the V-shaped graph is crossed by each vertical line at most once"),
        ("the set $\\{(-3, 0), (-2, 1), (-1, 2), (0, 3)\\}$", True, "each $x$-value is used exactly once"),
        ("the graph $y^2 = x + 1$", False, "for $x = 0$ both $y = 1$ and $y = -1$ satisfy the equation"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._CASES))
        description, is_function, reason = self._CASES[idx]

        answer_latex = (
            "Yes, it is a function." if is_function
            else "No, it is not a function."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine whether {description} defines $y$ as a function of $x$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "A relation is a function if and only if each $x$-value is "
                    "paired with exactly one $y$-value."
                ),
                (
                    "For a graph, apply the vertical line test: if any vertical "
                    "line crosses the graph more than once, it is not a function."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Inspect the relation: {description}."
                ),
                (
                    f"Check whether each $x$-value has a unique $y$-value — "
                    f"{reason}."
                ),
                (
                    f"Conclusion: it {'is' if is_function else 'is not'} a function."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_VISUALIZATION],
        )


@register
class FindDomainAndRangeFromGraph(Generator):
    """Given a described curve, state domain and range.

    Backward: pick a described function and its known domain/range.
    """

    generator_id = "find_domain_and_range_from_graph"
    topic_slug = "graphs_of_functions"
    display_name = "State domain and range from a described graph"

    bank_count_per_difficulty = 15

    # (description, domain_latex, range_latex)
    _CASES = (
        ("a parabola with vertex at $(0, 0)$ opening upward", r"(-\infty,\ \infty)", r"[0,\ \infty)"),
        ("a parabola with vertex at $(2, -3)$ opening upward", r"(-\infty,\ \infty)", r"[-3,\ \infty)"),
        ("a parabola with vertex at $(0, 4)$ opening downward", r"(-\infty,\ \infty)", r"(-\infty,\ 4]"),
        ("a parabola with vertex at $(-1, 5)$ opening downward", r"(-\infty,\ \infty)", r"(-\infty,\ 5]"),
        ("the graph $f(x) = \\sqrt{x}$", r"[0,\ \infty)", r"[0,\ \infty)"),
        ("the graph $f(x) = \\sqrt{x - 2}$", r"[2,\ \infty)", r"[0,\ \infty)"),
        ("the horizontal line $f(x) = 5$", r"(-\infty,\ \infty)", r"\{5\}"),
        ("the absolute value $f(x) = |x|$", r"(-\infty,\ \infty)", r"[0,\ \infty)"),
        ("the absolute value $f(x) = |x| - 2$", r"(-\infty,\ \infty)", r"[-2,\ \infty)"),
        ("the cubing function $f(x) = x^3$", r"(-\infty,\ \infty)", r"(-\infty,\ \infty)"),
        ("the line $f(x) = 2x + 1$", r"(-\infty,\ \infty)", r"(-\infty,\ \infty)"),
        ("a semicircle $f(x) = \\sqrt{4 - x^2}$", r"[-2,\ 2]", r"[0,\ 2]"),
        ("the reciprocal $f(x) = 1/x$", r"(-\infty,\ 0) \cup (0,\ \infty)", r"(-\infty,\ 0) \cup (0,\ \infty)"),
        ("the exponential $f(x) = 2^x$", r"(-\infty,\ \infty)", r"(0,\ \infty)"),
        ("the parabola with vertex at $(3, 1)$ opening upward", r"(-\infty,\ \infty)", r"[1,\ \infty)"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._CASES))
        description, domain, rng_latex = self._CASES[idx]

        answer_latex = f"Domain: ${domain}$; range: ${rng_latex}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Give the domain and range of {description}."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Domain is the set of all $x$-values the graph actually reaches; "
                    "range is the set of all $y$-values."
                ),
                (
                    "For a parabola opening upward with vertex $(h, k)$, the domain "
                    "is all real numbers and the range is $[k, \\infty)$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Visualise {description}."
                ),
                (
                    f"Project the graph onto the $x$-axis to read off the domain: "
                    f"${domain}$."
                ),
                (
                    f"Project the graph onto the $y$-axis to read off the range: "
                    f"${rng_latex}$."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_VISUALIZATION],
        )


@register
class IdentifyIncreasingDecreasingInterval(Generator):
    """For a described function, identify where it is increasing and decreasing.

    Backward: pick a function and the known increasing/decreasing intervals.
    """

    generator_id = "identify_increasing_decreasing_interval"
    topic_slug = "graphs_of_functions"
    display_name = "Identify increasing and decreasing intervals of a function"

    _H_RANGES = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-10, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        shape = rng.choice(["up_parabola", "down_parabola"])
        h_lo, h_hi = self._H_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(h_lo, h_hi)

        if shape == "up_parabola":
            equation_latex = (
                f"f(x) = (x {_signed_const(-h)})^2 {_signed_const(k)}"
                if k != 0
                else f"f(x) = (x {_signed_const(-h)})^2"
            )
            dec_interval = rf"(-\infty,\ {h})"
            inc_interval = rf"({h},\ \infty)"
            vertex_word = "minimum"
        else:
            equation_latex = (
                f"f(x) = -(x {_signed_const(-h)})^2 {_signed_const(k)}"
                if k != 0
                else f"f(x) = -(x {_signed_const(-h)})^2"
            )
            inc_interval = rf"(-\infty,\ {h})"
            dec_interval = rf"({h},\ \infty)"
            vertex_word = "maximum"

        answer_latex = (
            f"Increasing on ${inc_interval}$; decreasing on ${dec_interval}$"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (shape, h, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Identify the intervals on which ${equation_latex}$ is "
                "increasing and on which it is decreasing."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    f"A parabola has a single {vertex_word} at its vertex, and the "
                    "function changes from increasing to decreasing (or vice versa) "
                    "there."
                ),
                (
                    f"Read off the vertex from the equation: it is at "
                    f"$({h},\\ {k})$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The vertex of ${equation_latex}$ is at $({h},\\ {k})$."
                ),
                (
                    f"Because the parabola opens "
                    f"{'upward' if shape == 'up_parabola' else 'downward'}, the "
                    f"function attains its {vertex_word} at the vertex."
                ),
                (
                    f"Increasing on ${inc_interval}$ and decreasing on "
                    f"${dec_interval}$."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_VISUALIZATION],
        )


# ===========================================================================
# Topic 5: introduction_to_functions
# ===========================================================================


@register
class EvaluateFunctionAtPoint(Generator):
    """Evaluate a linear or simple quadratic at a given integer input.

    Backward: pick coefficients and input so the value is a small integer.
    """

    generator_id = "evaluate_function_at_point"
    topic_slug = "introduction_to_functions"
    display_name = "Evaluate a function at a specified input"

    _A_RANGES = {"easy": (1, 5), "medium": (-6, 6), "hard": (-10, 10)}
    _B_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _C_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        shape = rng.choice(["linear", "quadratic"])
        a_lo, a_hi = self._A_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        c_lo, c_hi = self._C_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]

        a = rng.randint(a_lo, a_hi)
        while a == 0:
            a = rng.randint(a_lo, a_hi)
        k = rng.randint(k_lo, k_hi)

        if shape == "linear":
            b = rng.randint(b_lo, b_hi)
            value = a * k + b
            f_latex = f"f(x) = {_linear_latex(a, b)}"
            sub_latex = (
                f"{a}({k}) {_signed_const(b) if b != 0 else ''}".strip()
            )
            params = ("lin", a, b, k)
        else:
            b = rng.randint(b_lo, b_hi)
            c = rng.randint(c_lo, c_hi)
            value = a * k * k + b * k + c
            f_latex = f"f(x) = {_quadratic_latex(a, b, c)}"
            quad_part = f"{a}({k})^2"
            lin_part = (
                f" {_signed_const(b)}({k})" if b != 0 else ""
            )
            const_part = f" {_signed_const(c)}" if c != 0 else ""
            sub_latex = f"{quad_part}{lin_part}{const_part}".strip()
            params = ("quad", a, b, c, k)

        answer_latex = f"$f({k}) = {value}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For ${f_latex}$, compute $f({k})$."
            ),
            answer_latex=answer_latex,
            hints=[
                "Substitute the input directly for every $x$ in the function rule.",
                "Evaluate the resulting arithmetic expression carefully, respecting order of operations.",
            ],
            solution_steps_latex=[
                (
                    f"Substitute $x = {k}$: $f({k}) = {sub_latex}$."
                ),
                (
                    f"Simplify: $f({k}) = {value}$."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_FORMULA_SUB],
        )


@register
class IdentifyFunctionFromOrderedPairs(Generator):
    """Given a set of ordered pairs, decide whether it defines a function.

    Backward: rotate through a small catalogue of pair-sets with known status.
    """

    generator_id = "identify_function_from_ordered_pairs"
    topic_slug = "introduction_to_functions"
    display_name = "Decide whether a set of ordered pairs defines a function"

    bank_count_per_difficulty = 15

    # (pair_set_latex, is_function, reason)
    _CASES = (
        (r"\{(1, 2), (2, 4), (3, 6), (4, 8)\}", True, "each $x$-value appears only once"),
        (r"\{(1, 2), (1, 5), (2, 4)\}", False, "$x = 1$ is paired with $y = 2$ and $y = 5$"),
        (r"\{(0, 0), (1, 1), (2, 8), (3, 27)\}", True, "no repeated $x$-values"),
        (r"\{(-1, 3), (0, 3), (1, 3), (2, 3)\}", True, "every $x$ has exactly one $y$"),
        (r"\{(2, 5), (2, -5), (3, 7), (4, 9)\}", False, "$x = 2$ maps to both $5$ and $-5$"),
        (r"\{(5, 1), (6, 2), (7, 3), (5, 4)\}", False, "$x = 5$ appears twice with different outputs"),
        (r"\{(-3, 9), (-2, 4), (-1, 1), (0, 0)\}", True, "each $x$-value has a unique $y$"),
        (r"\{(1, 1), (2, 4), (3, 9), (-1, 1)\}", True, "each $x$-value is used once (the repeated $y$ is allowed)"),
        (r"\{(0, 1), (1, 2), (2, 3), (0, 4)\}", False, "$x = 0$ is paired with both $1$ and $4$"),
        (r"\{(10, 100), (20, 400), (30, 900)\}", True, "three distinct inputs, three distinct outputs"),
        (r"\{(-5, 2), (-4, 3), (-3, 4), (-4, 7)\}", False, "$x = -4$ has two different $y$-values"),
        (r"\{(7, 7), (8, 8), (9, 9)\}", True, "each $x$ has a unique output"),
        (r"\{(0, -1), (1, 0), (0, 1)\}", False, "$x = 0$ maps to $-1$ and to $1$"),
        (r"\{(-2, 5), (-1, 4), (0, 3), (1, 2), (2, 1)\}", True, "every $x$ has exactly one $y$"),
        (r"\{(3, 5), (4, 6), (5, 7), (4, 6)\}", True, "the pair $(4, 6)$ is repeated but still pairs $x = 4$ with only $y = 6$"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._CASES))
        pair_latex, is_function, reason = self._CASES[idx]

        answer_latex = (
            "Yes, the relation is a function." if is_function
            else "No, the relation is not a function."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine whether the relation ${pair_latex}$ is a function."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "A relation is a function when each $x$-value is paired with "
                    "exactly one $y$-value."
                ),
                (
                    "Scan the ordered pairs for any repeated $x$-value with "
                    "different $y$-values."
                ),
            ],
            solution_steps_latex=[
                (
                    f"List the $x$-values of the relation ${pair_latex}$."
                ),
                (
                    f"Check for repeated $x$-values: {reason}."
                ),
                (
                    f"Therefore the relation "
                    f"{'is' if is_function else 'is not'} a function."
                ),
            ],
            tags=FUNCTION_TAGS + [SKILL_PROCEDURAL],
        )


@register
class FunctionNotationSubstitution(Generator):
    """Given $f(x) = 2x + 5$ (or similar), compute $f(a + 1)$ or $f(-3)$ symbolically.

    Backward: pick coefficients and substitution target; SymPy handles the
    symbolic simplification.
    """

    generator_id = "function_notation_substitution"
    topic_slug = "introduction_to_functions"
    display_name = "Substitute an expression into a function rule"

    _A_RANGES = {"easy": (1, 5), "medium": (-6, 6), "hard": (-8, 8)}
    _B_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]

        a = rng.randint(a_lo, a_hi)
        while a == 0:
            a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        # Substitution target: either an integer (numeric) or a + k (symbolic)
        mode = rng.choice(["numeric", "symbolic"])
        x = sp.Symbol("x")
        a_sym = sp.Symbol("a")
        f_expr = a * x + b

        if mode == "numeric":
            k = rng.randint(-6, 6)
            target_latex = str(k)
            sub_expr = f_expr.subs(x, k)
            answer_sym = sp.simplify(sub_expr)
            steps = [
                (
                    f"Substitute $x = {k}$ into $f(x) = {_linear_latex(a, b)}$: "
                    f"$f({k}) = {a}({k}) {_signed_const(b) if b != 0 else ''}$."
                ),
                (
                    f"Simplify: $f({k}) = {sp.latex(answer_sym)}$."
                ),
            ]
            statement = (
                f"Given $f(x) = {_linear_latex(a, b)}$, compute $f({k})$."
            )
            params = ("num", a, b, k)
        else:
            k = rng.randint(-5, 5)
            if k == 0:
                target = a_sym
                target_latex = "a"
            else:
                target = a_sym + k
                target_latex = (
                    f"a {_signed_const(k)}"
                )
            sub_expr = f_expr.subs(x, target)
            answer_sym = sp.expand(sub_expr)
            steps = [
                (
                    f"Replace every $x$ in $f(x) = {_linear_latex(a, b)}$ with "
                    f"$({target_latex})$: "
                    f"$f({target_latex}) = {a}({target_latex}) "
                    f"{_signed_const(b) if b != 0 else ''}$."
                ),
                (
                    f"Distribute and simplify: "
                    f"$f({target_latex}) = {sp.latex(answer_sym)}$."
                ),
            ]
            statement = (
                f"Given $f(x) = {_linear_latex(a, b)}$, express "
                f"$f({target_latex})$ in simplified form."
            )
            params = ("sym", a, b, k)

        answer_latex = f"$f({target_latex}) = {sp.latex(answer_sym)}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=[
                (
                    "To evaluate $f$ at any expression, replace every $x$ in the "
                    "rule with that expression (wrapped in parentheses)."
                ),
                (
                    "After substitution, simplify using the distributive property."
                ),
            ],
            solution_steps_latex=steps,
            tags=FUNCTION_TAGS + [SKILL_ALGEBRAIC],
        )
