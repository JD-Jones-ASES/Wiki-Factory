"""Radical function generators (Algebra 2, radical-functions cluster).

Two topic slugs covered:

- square_root_functions (Square_Root_Functions.md)
- cube_root_and_other_radical_functions (Cube_Root_And_Other_Radical_Functions.md)

Each topic has three generators for a total of six. Backward construction
is used throughout: parameters are chosen so the answer comes out clean
(integer domain bounds, integer outputs, perfect squares/cubes), then the
statement is rendered.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _format_linear_inside(coef: int, h: int, var: str = "x") -> str:
    """Render the argument of a radical: coef*x - coef*h, simplified.

    coef must be a positive integer. h is an integer (the "shift").
    Examples::

        _format_linear_inside(1, 3)   ->  "x - 3"
        _format_linear_inside(1, -2)  ->  "x + 2"
        _format_linear_inside(2, 5)   ->  "2x - 10"
        _format_linear_inside(1, 0)   ->  "x"
    """
    if coef == 1:
        lead = var
    else:
        lead = f"{coef}{var}"
    shifted = coef * h
    if shifted == 0:
        return lead
    if shifted > 0:
        return f"{lead} - {shifted}"
    return f"{lead} + {-shifted}"


def _format_a_coef(a: int) -> str:
    """Render a leading coefficient of a radical term, hiding 1 and -1."""
    if a == 1:
        return ""
    if a == -1:
        return "-"
    return str(a)


def _format_shift_paren(h: int, var: str = "x") -> str:
    """Render (x - h) with clean signs, or just x when h = 0."""
    if h == 0:
        return var
    if h > 0:
        return f"({var} - {h})"
    return f"({var} + {-h})"


def _format_trailing_constant(k: int) -> str:
    """Render a trailing + k constant, handling sign and zero."""
    if k == 0:
        return ""
    if k > 0:
        return f" + {k}"
    return f" - {-k}"


def _format_sqrt_function(a: int, h: int, k: int, name: str = "f") -> str:
    """Render f(x) = a*sqrt(x - h) + k in LaTeX, hiding 1-coefficients."""
    a_str = _format_a_coef(a)
    inside = _format_shift_paren(h)
    if inside == "x":
        radical = r"\sqrt{x}"
    else:
        radical = rf"\sqrt{{{_format_linear_inside(1, h)}}}"
    body = f"{a_str}{radical}{_format_trailing_constant(k)}"
    return f"{name}(x) = {body}"


def _format_cbrt_function(a: int, h: int, k: int, name: str = "f") -> str:
    """Render f(x) = a*cbrt(x - h) + k in LaTeX, hiding 1-coefficients."""
    a_str = _format_a_coef(a)
    if h == 0:
        radical = r"\sqrt[3]{x}"
    else:
        radical = rf"\sqrt[3]{{{_format_linear_inside(1, h)}}}"
    body = f"{a_str}{radical}{_format_trailing_constant(k)}"
    return f"{name}(x) = {body}"


def _format_signed_paren(n: int) -> str:
    """Wrap a negative integer in parentheses so it reads well after an op."""
    return f"({n})" if n < 0 else str(n)


# ===========================================================================
# Topic 1: square_root_functions
# ===========================================================================


@register
class SqrtFunctionDomain(Generator):
    """State the domain of f(x) = sqrt(expression).

    Backward construction: pick the desired domain lower bound L (so that
    the domain is x >= L), pick a positive leading coefficient for the
    argument, and build the radicand coef*x - coef*L.
    """
    generator_id = "sqrt_function_domain"
    topic_slug = "square_root_functions"
    display_name = "Find the domain of f(x) = sqrt(expression)"

    _L_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _COEF_CHOICES = {
        "easy": (1,),
        "medium": (1, 2, 3),
        "hard": (1, 2, 3, 4, 5),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        l_lo, l_hi = self._L_RANGES[difficulty]
        lower_bound = rng.randint(l_lo, l_hi)
        coef = rng.choice(self._COEF_CHOICES[difficulty])

        radicand = _format_linear_inside(coef, lower_bound)
        function_latex = rf"f(x) = \sqrt{{{radicand}}}"

        # Inequality to solve: coef*x - coef*L >= 0  ->  x >= L
        setup_ineq = f"{radicand} \\geq 0"
        if coef == 1:
            divide_step = ""
        else:
            divide_step = (
                f"Divide both sides by {coef}: $x \\geq {lower_bound}$."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (coef, lower_bound)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the domain of ${function_latex}$. "
                "Give your answer as an inequality in $x$."
            ),
            answer_latex=f"$x \\geq {lower_bound}$",
            hints=[
                "A square root is defined only when its radicand is greater than or equal to 0.",
                f"Set the inside of the radical greater than or equal to 0: ${setup_ineq}$.",
                "Solve that inequality for $x$.",
            ],
            solution_steps_latex=[
                (
                    "The square-root function $\\sqrt{\\;\\;}$ is only defined for "
                    "nonnegative inputs."
                ),
                (
                    f"Set the radicand greater than or equal to 0: "
                    f"${setup_ineq}$."
                ),
                (
                    f"Add ${coef * lower_bound}$ to both sides: "
                    f"${coef}x \\geq {coef * lower_bound}$."
                )
                if coef != 1
                else f"Add ${lower_bound}$ to both sides: $x \\geq {lower_bound}$.",
                divide_step or f"The domain is $x \\geq {lower_bound}$.",
                f"So the domain of $f$ is $x \\geq {lower_bound}$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


@register
class SqrtFunctionEvaluate(Generator):
    """Evaluate f(x) = a*sqrt(x - h) + k at an input that yields an integer.

    Backward construction: pick a, h, k, and a nonneg integer n; the input is
    h + n^2 so that sqrt(input - h) = n, and the output is a*n + k.
    """
    generator_id = "sqrt_function_evaluate"
    topic_slug = "square_root_functions"
    display_name = "Evaluate f(x) = a*sqrt(x - h) + k at a given input"

    _A_CHOICES = {
        "easy": (1, 2),
        "medium": (1, 2, 3, -1, -2),
        "hard": (1, 2, 3, 4, -1, -2, -3),
    }
    _H_RANGES = {"easy": (-4, 4), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _N_CHOICES = {
        "easy": (0, 1, 2, 3),
        "medium": (0, 1, 2, 3, 4, 5),
        "hard": (0, 1, 2, 3, 4, 5, 6, 7),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        n = rng.choice(self._N_CHOICES[difficulty])

        input_val = h + n * n
        output_val = a * n + k

        func_latex = _format_sqrt_function(a, h, k)
        inside_val = input_val - h  # equals n^2

        # Format the substituted radical expression
        if h == 0:
            sub_inside = f"{input_val}"
        elif h > 0:
            sub_inside = f"{input_val} - {h}"
        else:
            sub_inside = f"{input_val} + {-h}"

        a_prefix = _format_a_coef(a)
        k_tail = _format_trailing_constant(k)
        a_times_n = a * n

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, h, k, n)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, find $f({input_val})$."
            ),
            answer_latex=f"$f({input_val}) = {output_val}$",
            hints=[
                f"Substitute $x = {input_val}$ into the expression for $f(x)$.",
                f"Simplify the radicand first: ${sub_inside} = {inside_val}$.",
                f"Then $\\sqrt{{{inside_val}}} = {n}$ because ${n}^2 = {inside_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {input_val}$: "
                    f"$f({input_val}) = {a_prefix}\\sqrt{{{sub_inside}}}{k_tail}$."
                ),
                (
                    f"Simplify the radicand: "
                    f"$f({input_val}) = {a_prefix}\\sqrt{{{inside_val}}}{k_tail}$."
                ),
                (
                    f"Take the square root: "
                    f"$f({input_val}) = {a_prefix}({n}){k_tail}$."
                ),
                (
                    f"Multiply and add: "
                    f"$f({input_val}) = {a_times_n}{k_tail} = {output_val}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


@register
class SqrtFunctionTransformationIdentify(Generator):
    """Identify horizontal shift, vertical shift, and reflection of sqrt(x).

    Given f(x) = a*sqrt(x - h) + k, describe the transformation from the
    parent function sqrt(x). Multi-part answer.
    """
    generator_id = "sqrt_function_transformation_identify"
    topic_slug = "square_root_functions"
    display_name = "Identify transformations of f(x) = a*sqrt(x - h) + k from sqrt(x)"

    _A_CHOICES = {
        "easy": (1, -1),
        "medium": (1, -1, 2, -2),
        "hard": (1, -1, 2, -2, 3, -3),
    }
    _H_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        # Avoid the degenerate all-zero transformation (a=1, h=0, k=0)
        while a == 1 and h == 0 and k == 0:
            a = rng.choice(self._A_CHOICES[difficulty])
            h = rng.randint(h_lo, h_hi)
            k = rng.randint(k_lo, k_hi)

        func_latex = _format_sqrt_function(a, h, k)

        # Horizontal shift description
        if h == 0:
            h_desc = "no horizontal shift"
        elif h > 0:
            h_desc = f"a horizontal shift {h} units to the right"
        else:
            h_desc = f"a horizontal shift {-h} units to the left"

        # Vertical shift description
        if k == 0:
            k_desc = "no vertical shift"
        elif k > 0:
            k_desc = f"a vertical shift {k} units upward"
        else:
            k_desc = f"a vertical shift {-k} units downward"

        # Reflection / orientation description
        if a > 0:
            reflect_desc = "no reflection (the graph opens upward to the right)"
        else:
            reflect_desc = "a reflection across the x-axis (the graph opens downward to the right)"

        opens_phrase = "upward" if a > 0 else "downward (reflected across the x-axis)"

        answer = (
            f"Horizontal: {h_desc}; vertical: {k_desc}; orientation: {reflect_desc}."
        )

        # Build a natural reading of how we deduce each piece.
        h_reasoning = (
            "Since $h = 0$, the graph stays at the parent position horizontally."
            if h == 0
            else (
                f"Since $h = {h} > 0$, the inside becomes $x - {h}$ and the graph "
                f"shifts ${h}$ units to the right."
                if h > 0
                else f"Since $h = {h} < 0$, the inside becomes $x + {-h}$ and the graph "
                f"shifts ${-h}$ units to the left."
            )
        )
        k_reasoning = (
            "Since $k = 0$, there is no vertical shift."
            if k == 0
            else (
                f"Since $k = {k} > 0$, the graph shifts ${k}$ units upward."
                if k > 0
                else f"Since $k = {k} < 0$, the graph shifts ${-k}$ units downward."
            )
        )
        a_reasoning = (
            "Since $a > 0$, the graph is not reflected and opens upward to the right."
            if a > 0
            else "Since $a < 0$, the graph is reflected across the x-axis and opens downward to the right."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe the transformations that take the parent function "
                f"$y = \\sqrt{{x}}$ to ${func_latex}$. Give (a) the horizontal "
                "shift, (b) the vertical shift, and (c) whether the graph is "
                "reflected or opens {opening direction}."
            ),
            answer_latex=answer,
            hints=[
                r"The general form is $f(x) = a\sqrt{x - h} + k$ where $h$ and $k$ shift the graph and $a$ controls stretch/reflection.",
                "Compare term by term with the parent $y = \\sqrt{x}$.",
                f"The sign of $a$ tells you whether the graph is reflected; here $a = {a}$.",
            ],
            solution_steps_latex=[
                (
                    r"Match the given function against the template "
                    r"$f(x) = a\sqrt{x - h} + k$."
                ),
                f"Read off $a = {a}$, $h = {h}$, and $k = {k}$.",
                h_reasoning,
                k_reasoning,
                a_reasoning,
                (
                    f"Summary: {h_desc}, {k_desc}, and the graph opens "
                    f"{opens_phrase}."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


# ===========================================================================
# Topic 2: cube_root_and_other_radical_functions
# ===========================================================================


@register
class CubeRootEvaluate(Generator):
    """Evaluate f(x) = a*cbrt(x - h) + k at an input yielding an integer.

    Backward construction: pick a, h, k and an integer cube root m.
    The input is h + m^3, and the output is a*m + k. Cube roots handle
    negatives just fine, so m may be negative.
    """
    generator_id = "cube_root_evaluate"
    topic_slug = "cube_root_and_other_radical_functions"
    display_name = "Evaluate f(x) = a*cbrt(x - h) + k at a given input"
    # Parameter space is tight because clean cube inputs are limited.
    bank_count_per_difficulty = 20

    _A_CHOICES = {
        "easy": (1, -1),
        "medium": (1, -1, 2, -2),
        "hard": (1, -1, 2, -2, 3, -3),
    }
    _H_RANGES = {"easy": (-4, 4), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-18, 18)}
    # m gives the cube root; m^3 gives the input offset. Keep |m| small.
    _M_CHOICES = {
        "easy": (-2, -1, 0, 1, 2, 3),
        "medium": (-3, -2, -1, 0, 1, 2, 3, 4),
        "hard": (-4, -3, -2, -1, 0, 1, 2, 3, 4, 5),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        m = rng.choice(self._M_CHOICES[difficulty])

        input_val = h + m * m * m
        inside_val = m * m * m  # equals input_val - h
        output_val = a * m + k

        func_latex = _format_cbrt_function(a, h, k)

        if h == 0:
            sub_inside = f"{input_val}"
        elif h > 0:
            sub_inside = f"{input_val} - {h}"
        else:
            sub_inside = f"{input_val} + {-h}"

        a_prefix = _format_a_coef(a)
        k_tail = _format_trailing_constant(k)
        a_times_m = a * m

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, h, k, m)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, find $f({input_val})$."
            ),
            answer_latex=f"$f({input_val}) = {output_val}$",
            hints=[
                f"Substitute $x = {input_val}$ into $f(x)$.",
                f"Simplify the radicand first: ${sub_inside} = {inside_val}$.",
                (
                    f"Cube roots are defined for negatives. Here "
                    f"$\\sqrt[3]{{{inside_val}}} = {m}$ because "
                    f"${_format_signed_paren(m)}^3 = {inside_val}$."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {input_val}$: "
                    f"$f({input_val}) = {a_prefix}\\sqrt[3]{{{sub_inside}}}{k_tail}$."
                ),
                (
                    f"Simplify the radicand: "
                    f"$f({input_val}) = {a_prefix}\\sqrt[3]{{{inside_val}}}{k_tail}$."
                ),
                (
                    f"Take the cube root: "
                    f"$f({input_val}) = {a_prefix}({m}){k_tail}$."
                ),
                (
                    f"Multiply and add: "
                    f"$f({input_val}) = {a_times_m}{k_tail} = {output_val}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


@register
class NthRootDomain(Generator):
    """State the domain of f(x) = nth_root(expression).

    Even index: the radicand must be >= 0, so the domain is restricted.
    Odd index: cube roots, fifth roots, etc. accept all real inputs.
    """
    generator_id = "nth_root_domain"
    topic_slug = "cube_root_and_other_radical_functions"
    display_name = "Find the domain of f(x) = nth-root(expression)"
    # Small parameter space: only a few (index, expression) combinations
    # yield distinct clean problems per difficulty.
    bank_count_per_difficulty = 24

    _EVEN_INDICES = {
        "easy": (2,),
        "medium": (2, 4),
        "hard": (2, 4, 6),
    }
    _ODD_INDICES = {
        "easy": (3,),
        "medium": (3, 5),
        "hard": (3, 5, 7),
    }
    _L_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        category = rng.choice(["even", "odd"])
        l_lo, l_hi = self._L_RANGES[difficulty]
        lower_bound = rng.randint(l_lo, l_hi)

        if category == "even":
            n = rng.choice(self._EVEN_INDICES[difficulty])
        else:
            n = rng.choice(self._ODD_INDICES[difficulty])

        # Build the radicand as x - lower_bound (coefficient 1 keeps it clean).
        radicand = _format_linear_inside(1, lower_bound)

        if n == 2:
            radical = rf"\sqrt{{{radicand}}}"
        else:
            radical = rf"\sqrt[{n}]{{{radicand}}}"
        function_latex = f"f(x) = {radical}"

        if category == "even":
            answer = f"$x \\geq {lower_bound}$"
            explain_hint = (
                f"An even-index radical (here index {n}) is defined only when "
                "the radicand is greater than or equal to 0."
            )
            conclude = (
                f"Since the index ${n}$ is even, set the radicand $\\geq 0$ and "
                "solve for $x$."
            )
            solve_step = (
                f"Set ${radicand} \\geq 0$ and add ${lower_bound}$ to both "
                f"sides: $x \\geq {lower_bound}$."
            )
            final = f"The domain of $f$ is $x \\geq {lower_bound}$."
        else:  # odd
            answer = r"$x \in \mathbb{R}$ (all real numbers)"
            explain_hint = (
                f"An odd-index radical (here index {n}) is defined for every "
                "real number input because odd roots of negatives are real."
            )
            conclude = (
                f"Since the index ${n}$ is odd, the radical accepts every real "
                "number, so there is no restriction on $x$."
            )
            solve_step = (
                "No inequality is needed: all real $x$ are allowed."
            )
            final = r"The domain of $f$ is all real numbers, $x \in \mathbb{R}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (category, n, lower_bound)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the domain of ${function_latex}$."
            ),
            answer_latex=answer,
            hints=[
                "The domain depends on whether the index of the radical is even or odd.",
                explain_hint,
                f"Here the index is ${n}$.",
            ],
            solution_steps_latex=[
                f"Identify the index of the radical: ${n}$.",
                conclude,
                solve_step,
                final,
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


@register
class CubeRootTransformation(Generator):
    """Identify transformations of f(x) = a*cbrt(x - h) + k from cbrt(x).

    Multi-part answer: horizontal shift, vertical shift, and reflection.
    """
    generator_id = "cube_root_transformation"
    topic_slug = "cube_root_and_other_radical_functions"
    display_name = "Identify transformations of f(x) = a*cbrt(x - h) + k from cbrt(x)"

    _A_CHOICES = {
        "easy": (1, -1),
        "medium": (1, -1, 2, -2),
        "hard": (1, -1, 2, -2, 3, -3),
    }
    _H_RANGES = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        # Avoid the degenerate all-zero transformation.
        while a == 1 and h == 0 and k == 0:
            a = rng.choice(self._A_CHOICES[difficulty])
            h = rng.randint(h_lo, h_hi)
            k = rng.randint(k_lo, k_hi)

        func_latex = _format_cbrt_function(a, h, k)

        if h == 0:
            h_desc = "no horizontal shift"
        elif h > 0:
            h_desc = f"a horizontal shift {h} units to the right"
        else:
            h_desc = f"a horizontal shift {-h} units to the left"

        if k == 0:
            k_desc = "no vertical shift"
        elif k > 0:
            k_desc = f"a vertical shift {k} units upward"
        else:
            k_desc = f"a vertical shift {-k} units downward"

        if a > 0:
            reflect_desc = "no reflection"
        else:
            reflect_desc = "a reflection across the x-axis"

        answer = (
            f"Horizontal: {h_desc}; vertical: {k_desc}; orientation: {reflect_desc}."
        )

        h_reasoning = (
            "Since $h = 0$, the graph stays at the parent position horizontally."
            if h == 0
            else (
                f"Since $h = {h} > 0$, the graph shifts ${h}$ units to the right."
                if h > 0
                else f"Since $h = {h} < 0$, the graph shifts ${-h}$ units to the left."
            )
        )
        k_reasoning = (
            "Since $k = 0$, there is no vertical shift."
            if k == 0
            else (
                f"Since $k = {k} > 0$, the graph shifts ${k}$ units upward."
                if k > 0
                else f"Since $k = {k} < 0$, the graph shifts ${-k}$ units downward."
            )
        )
        a_reasoning = (
            "Since $a > 0$, the graph is not reflected across the x-axis."
            if a > 0
            else "Since $a < 0$, the graph is reflected across the x-axis."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe the transformations that take the parent function "
                f"$y = \\sqrt[3]{{x}}$ to ${func_latex}$. Give (a) the "
                "horizontal shift, (b) the vertical shift, and (c) whether "
                "the graph is reflected across the x-axis."
            ),
            answer_latex=answer,
            hints=[
                r"The general form is $f(x) = a\sqrt[3]{x - h} + k$ where $h$ and $k$ shift the graph and $a$ controls stretch/reflection.",
                r"Compare term by term with the parent $y = \sqrt[3]{x}$.",
                f"The sign of $a$ tells you whether the graph is reflected; here $a = {a}$.",
            ],
            solution_steps_latex=[
                (
                    r"Match the given function against the template "
                    r"$f(x) = a\sqrt[3]{x - h} + k$."
                ),
                f"Read off $a = {a}$, $h = {h}$, and $k = {k}$.",
                h_reasoning,
                k_reasoning,
                a_reasoning,
                (
                    f"Summary: {h_desc}, {k_desc}, and {reflect_desc}."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )
