"""Parent function family generators (Algebra 2).

Four topic slugs covered:

- absolute_value_functions (Absolute_Value_Functions.md)
- power_functions (Power_Functions.md)
- polynomial_functions_and_graphs (Polynomial_Functions_And_Graphs.md)
- transformations_i_shifts_and_reflections (Transformations_I_Shifts_And_Reflections.md)

Each topic has three generators for a total of 12. Backward construction is
used throughout: parameters are chosen so the answer comes out clean
(integer outputs, integer vertices, integer roots), then the statement is
rendered.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _format_signed_paren(n: int) -> str:
    """Wrap a negative integer in parentheses so it reads well after an op."""
    return f"({n})" if n < 0 else str(n)


def _format_shift_paren(h: int, var: str = "x") -> str:
    """Render (x - h) with clean signs, or just x when h = 0."""
    if h == 0:
        return var
    if h > 0:
        return f"{var} - {h}"
    return f"{var} + {-h}"


def _format_trailing_constant(k: int) -> str:
    """Render a trailing + k constant, handling sign and zero."""
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


def _format_abs_function(a: int, h: int, k: int, name: str = "f") -> str:
    """Render f(x) = a|x - h| + k in LaTeX with clean signs."""
    a_str = _format_a_coef(a)
    inside = _format_shift_paren(h)
    abs_body = f"\\left|{inside}\\right|"
    tail = _format_trailing_constant(k)
    return f"{name}(x) = {a_str}{abs_body}{tail}"


def _format_power_function(k_coef: int, n: int, name: str = "f") -> str:
    """Render f(x) = k * x^n with clean signs; n is an integer (may be negative)."""
    if n == 0:
        # k * x^0 = k (rare for our problems, but handle it)
        return f"{name}(x) = {k_coef}"
    # Build x^n part
    if n == 1:
        x_part = "x"
    else:
        x_part = f"x^{{{n}}}"
    # Leading coefficient
    if k_coef == 1:
        return f"{name}(x) = {x_part}"
    if k_coef == -1:
        return f"{name}(x) = -{x_part}"
    return f"{name}(x) = {k_coef}{x_part}"


# ===========================================================================
# Topic 1: absolute_value_functions
# ===========================================================================


@register
class AbsValFunctionEvaluate(Generator):
    """Given f(x) = a|x - h| + k, evaluate at a specific input.

    Backward construction: pick a, h, k, and an input x0. Output is
    a * |x0 - h| + k, which is automatically an integer.
    """
    generator_id = "abs_val_function_evaluate"
    topic_slug = "absolute_value_functions"
    display_name = "Evaluate f(x) = a|x - h| + k at a given input"

    _A_CHOICES = {
        "easy": (1, 2, -1),
        "medium": (1, 2, 3, -1, -2),
        "hard": (1, 2, 3, 4, -1, -2, -3),
    }
    _H_RANGES = {"easy": (-4, 4), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _X_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        x0 = rng.randint(x_lo, x_hi)

        inside = x0 - h
        abs_inside = abs(inside)
        value = a * abs_inside + k

        func_latex = _format_abs_function(a, h, k)

        # Substituted inside expression (pre-simplification)
        if h == 0:
            sub_inside = f"{x0}"
        elif h > 0:
            sub_inside = f"{x0} - {h}"
        else:
            sub_inside = f"{x0} + {-h}"

        a_prefix = _format_a_coef(a)
        k_tail = _format_trailing_constant(k)
        a_times = a * abs_inside

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, h, k, x0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, find $f({x0})$."
            ),
            answer_latex=f"$f({x0}) = {value}$",
            hints=[
                f"Substitute $x = {x0}$ into every occurrence of $x$.",
                r"Simplify what's inside the absolute value bars first, then take $|\cdot|$.",
                f"Remember $\\left|{inside}\\right| = {abs_inside}$.",
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {x0}$: "
                    f"$f({x0}) = {a_prefix}\\left|{sub_inside}\\right|{k_tail}$."
                ),
                (
                    f"Simplify inside the bars: "
                    f"$f({x0}) = {a_prefix}\\left|{inside}\\right|{k_tail} "
                    f"= {a_prefix}({abs_inside}){k_tail}$."
                ),
                (
                    f"Multiply and add: "
                    f"$f({x0}) = {a_times}{k_tail} = {value}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-formula-substitution",
            ],
        )


@register
class AbsValFunctionFindVertex(Generator):
    """Given f(x) = a|x - h| + k, identify vertex (h, k) and opening direction."""
    generator_id = "abs_val_function_find_vertex"
    topic_slug = "absolute_value_functions"
    display_name = "Find the vertex of f(x) = a|x - h| + k"

    _A_CHOICES = {
        "easy": (1, -1, 2, -2),
        "medium": (1, -1, 2, -2, 3, -3),
        "hard": (1, -1, 2, -2, 3, -3, 4, -4),
    }
    _H_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        # Avoid the degenerate case (a=1, h=0, k=0) which is just |x|.
        while a == 1 and h == 0 and k == 0:
            a = rng.choice(self._A_CHOICES[difficulty])
            h = rng.randint(h_lo, h_hi)
            k = rng.randint(k_lo, k_hi)

        direction = "upward" if a > 0 else "downward"
        func_latex = _format_abs_function(a, h, k)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, h, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Identify the vertex of ${func_latex}$ and state whether the "
                "graph opens upward or downward."
            ),
            answer_latex=(
                f"Vertex $({h}, {k})$; opens {direction}."
            ),
            hints=[
                r"An absolute-value function in the form $f(x) = a|x - h| + k$ has its vertex at $(h, k)$.",
                "Read $h$ off the inside of the bars. Watch the sign: a minus gives $h$ directly, a plus flips the sign.",
                r"The graph opens upward when $a > 0$ and downward when $a < 0$.",
            ],
            solution_steps_latex=[
                (
                    f"Match ${func_latex}$ against the template "
                    r"$f(x) = a|x - h| + k$."
                ),
                f"Read off $h = {h}$ and $k = {k}$, so the vertex is $({h}, {k})$.",
                (
                    f"Since $a = {a}$ is "
                    f"{'positive' if a > 0 else 'negative'}, the graph opens {direction}."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-visualization",
            ],
        )


@register
class AbsValFunctionFromVertexAndDirection(Generator):
    """Given a vertex and direction, write f(x) = a|x - h| + k."""
    generator_id = "abs_val_function_from_vertex_and_direction"
    topic_slug = "absolute_value_functions"
    display_name = "Write f(x) = a|x - h| + k from vertex and direction"

    _A_CHOICES = {
        "easy": (1, -1, 2, -2),
        "medium": (1, -1, 2, -2, 3, -3),
        "hard": (1, -1, 2, -2, 3, -3, 4, -4),
    }
    _H_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)

        direction = "upward" if a > 0 else "downward"
        direction_phrase = (
            "opens upward" if a > 0 else "opens downward"
        )
        stretch_phrase = (
            "1" if abs(a) == 1 else str(abs(a))
        )
        func_latex = _format_abs_function(a, h, k)

        # Construct the statement: describe vertex, direction, and stretch factor.
        if abs(a) == 1:
            scale_desc = f"the graph {direction_phrase} with no vertical stretch"
        else:
            scale_desc = (
                f"the graph {direction_phrase} with a vertical stretch factor of {abs(a)}"
            )

        # Shifted expression for the solution
        if h == 0:
            inside_desc = "x"
        elif h > 0:
            inside_desc = f"x - {h}"
        else:
            inside_desc = f"x + {-h}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, h, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write the equation of the absolute-value function whose "
                f"vertex is $({h}, {k})$, where {scale_desc}. Use the form "
                r"$f(x) = a|x - h| + k$."
            ),
            answer_latex=f"${func_latex}$",
            hints=[
                r"Start from the vertex form $f(x) = a|x - h| + k$.",
                "The vertex gives you $h$ and $k$ directly (watch the sign on $h$).",
                "The sign of $a$ controls direction; its magnitude controls the vertical stretch.",
            ],
            solution_steps_latex=[
                r"Use the vertex form $f(x) = a|x - h| + k$.",
                f"The vertex is $({h}, {k})$, so $h = {h}$ and $k = {k}$.",
                (
                    f"The graph {direction_phrase} and has vertical stretch factor "
                    f"{stretch_phrase}, so $a = {a}$."
                ),
                (
                    f"Substitute into the template: $f(x) = {a if a not in (1,-1) else ('' if a==1 else '-')}"
                    f"\\left|{inside_desc}\\right|{_format_trailing_constant(k)}$, i.e. ${func_latex}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-procedural-calculation",
            ],
        )


# ===========================================================================
# Topic 2: power_functions
# ===========================================================================


@register
class PowerFunctionEvaluate(Generator):
    """Given f(x) = k * x^n, evaluate at a specific input.

    Backward construction: pick k, exponent n (can be negative), and an input
    x0. For negative n (reciprocal-style), we pick x0 so x0^|n| divides k
    cleanly to yield an integer answer. For positive n, any integer x0 works.
    """
    generator_id = "power_function_evaluate"
    topic_slug = "power_functions"
    display_name = "Evaluate f(x) = k * x^n at a given input"

    _POS_N = {
        "easy": (1, 2, 3),
        "medium": (1, 2, 3, 4),
        "hard": (1, 2, 3, 4, 5),
    }
    _NEG_N = {"easy": (-1, -2), "medium": (-1, -2, -3), "hard": (-1, -2, -3)}
    _POS_X = {
        "easy": (-4, -3, -2, 2, 3, 4),
        "medium": (-5, -4, -3, -2, 2, 3, 4, 5),
        "hard": (-6, -5, -4, -3, -2, 2, 3, 4, 5, 6),
    }
    # For negative n we want x^|n| to divide k; use small bases.
    _NEG_X = {
        "easy": (-2, -1, 1, 2),
        "medium": (-3, -2, -1, 1, 2, 3),
        "hard": (-4, -3, -2, -1, 1, 2, 3, 4),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Pick whether this instance uses positive or negative n.
        use_negative = rng.random() < 0.33
        if use_negative:
            n = rng.choice(self._NEG_N[difficulty])
            x0 = rng.choice(self._NEG_X[difficulty])
            # We need x0 != 0 (already enforced), and we pick k as a multiple of x0^|n|
            # so the answer k * x0^n = k / x0^|n| is an integer.
            base = x0 ** abs(n)  # positive
            # Pick a small integer multiplier for k
            mult_mag = rng.randint(1, 5)
            sign = rng.choice([-1, 1])
            k_coef = sign * mult_mag * base
            # Ensure k != 0
            if k_coef == 0:
                k_coef = base
            value = k_coef // base  # exact integer division: k * x0^n
            if x0 ** abs(n) < 0:
                value = -value
            # Sanity: recompute via exact arithmetic for verification
            # k * x0^n where n is negative means k / x0^|n|, but signs matter.
            # Since x0^|n| is positive when |n| even, but can be negative when |n| odd.
            # Above we set base = x0**|n|; Python handles negative bases correctly.
            # Recompute cleanly:
            real_base = x0 ** abs(n)
            value = k_coef // real_base
        else:
            n = rng.choice(self._POS_N[difficulty])
            x0 = rng.choice(self._POS_X[difficulty])
            k_coef = rng.choice([-3, -2, -1, 1, 2, 3])
            value = k_coef * (x0 ** n)

        func_latex = _format_power_function(k_coef, n)

        # Build the substituted expression for the solution
        x0_paren = _format_signed_paren(x0)
        if n == 1:
            x_power_sub = x0_paren
            x_power_val = x0
        else:
            x_power_sub = f"{x0_paren}^{{{n}}}"
            x_power_val = x0 ** n  # may be fractional conceptually for negative n

        # For display of evaluated power:
        if n >= 0:
            x_power_numeric = str(x0 ** n)
        else:
            # x0^{-|n|} = 1 / x0^{|n|}
            denom = x0 ** abs(n)
            x_power_numeric = f"\\dfrac{{1}}{{{denom}}}"

        # Coefficient prefix for writing out k * x0^n
        if k_coef == 1:
            coef_prefix = ""
        elif k_coef == -1:
            coef_prefix = "-"
        else:
            coef_prefix = f"{_format_signed_paren(k_coef)} \\cdot "

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k_coef, n, x0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, find $f({x0})$."
            ),
            answer_latex=f"$f({x0}) = {value}$",
            hints=[
                f"Substitute $x = {x0}$ into the function.",
                (
                    "A negative exponent means take the reciprocal: "
                    r"$x^{-n} = \dfrac{1}{x^n}$."
                    if n < 0
                    else "Raise the input to the indicated power, then multiply by the coefficient."
                ),
                f"Compute ${x0_paren}^{{{n if n != 1 else 1}}}$ carefully --- mind the sign on negative bases.",
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {x0}$: "
                    f"$f({x0}) = {coef_prefix}{x_power_sub}$."
                ),
                (
                    f"Evaluate the power: ${x_power_sub} = {x_power_numeric}$."
                ),
                (
                    f"Multiply by the coefficient: "
                    f"$f({x0}) = {value}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


@register
class PowerFunctionClassifyEndBehavior(Generator):
    """Given f(x) = k * x^n, classify end behavior as x -> +/- infinity.

    The parameter space is a 4-way combination (sign of k x parity of n),
    so we cap bank size.
    """
    generator_id = "power_function_classify_end_behavior"
    topic_slug = "power_functions"
    display_name = "Classify end behavior of f(x) = k * x^n"
    bank_count_per_difficulty = 24

    _K_CHOICES = {
        "easy": (1, -1, 2, -2),
        "medium": (1, -1, 2, -2, 3, -3),
        "hard": (1, -1, 2, -2, 3, -3, 4, -4, 5, -5),
    }
    _N_CHOICES = {
        "easy": (2, 3, 4, 5),
        "medium": (2, 3, 4, 5, 6),
        "hard": (2, 3, 4, 5, 6, 7),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_coef = rng.choice(self._K_CHOICES[difficulty])
        n = rng.choice(self._N_CHOICES[difficulty])

        # Classify end behavior. For positive n:
        # - n even, k > 0: both ends -> +inf
        # - n even, k < 0: both ends -> -inf
        # - n odd,  k > 0: x -> -inf => y -> -inf; x -> +inf => y -> +inf
        # - n odd,  k < 0: x -> -inf => y -> +inf; x -> +inf => y -> -inf
        is_even = (n % 2 == 0)
        if is_even:
            if k_coef > 0:
                right_limit = r"+\infty"
                left_limit = r"+\infty"
            else:
                right_limit = r"-\infty"
                left_limit = r"-\infty"
        else:
            if k_coef > 0:
                right_limit = r"+\infty"
                left_limit = r"-\infty"
            else:
                right_limit = r"-\infty"
                left_limit = r"+\infty"

        parity_word = "even" if is_even else "odd"
        sign_word = "positive" if k_coef > 0 else "negative"
        func_latex = _format_power_function(k_coef, n)

        answer = (
            f"As $x \\to +\\infty$, $y \\to {right_limit}$; "
            f"as $x \\to -\\infty$, $y \\to {left_limit}$."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k_coef, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe the end behavior of ${func_latex}$. State what "
                r"happens to $y$ as $x \to +\infty$ and as $x \to -\infty$."
            ),
            answer_latex=answer,
            hints=[
                "For a power function, look at two things: the sign of the leading coefficient and the parity of the exponent.",
                r"If $n$ is even, both ends head the same direction. If $n$ is odd, the ends head opposite directions.",
                r"The sign of $k$ flips the whole graph across the $x$-axis.",
            ],
            solution_steps_latex=[
                f"Identify the pieces: $k = {k_coef}$ ({sign_word}) and $n = {n}$ ({parity_word}).",
                (
                    f"Because $n = {n}$ is {parity_word}, "
                    + (
                        "both arms of the graph go in the same direction."
                        if is_even
                        else "the arms of the graph go in opposite directions."
                    )
                ),
                (
                    f"Because $k = {k_coef}$ is {sign_word}, "
                    + (
                        "the graph is not reflected."
                        if k_coef > 0
                        else "the graph is reflected across the $x$-axis."
                    )
                ),
                (
                    f"Therefore as $x \\to +\\infty$, $y \\to {right_limit}$; "
                    f"and as $x \\to -\\infty$, $y \\to {left_limit}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-visualization",
            ],
        )


@register
class PowerFunctionDomainByExponent(Generator):
    """Given f(x) = x^n for various n, state the domain.

    Four categories: positive integer, negative integer, 1/2 (square root),
    1/3 (cube root). To hit the minimum unique-bank size we also vary the
    variable name used in the function.
    """
    generator_id = "power_function_domain_by_exponent"
    topic_slug = "power_functions"
    display_name = "Find the domain of f(x) = x^n for integer/rational n"
    bank_count_per_difficulty = 20

    _POS_INT = {
        "easy": (1, 2, 3, 4, 5),
        "medium": (1, 2, 3, 4, 5, 6, 7),
        "hard": (1, 2, 3, 4, 5, 6, 7, 8, 9),
    }
    _NEG_INT = {
        "easy": (-1, -2, -3),
        "medium": (-1, -2, -3, -4),
        "hard": (-1, -2, -3, -4, -5),
    }
    _VAR_NAMES = ("x", "t", "s")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        category = rng.choice(["pos_int", "neg_int", "half", "third"])
        var = rng.choice(self._VAR_NAMES)

        if category == "pos_int":
            n = rng.choice(self._POS_INT[difficulty])
            exp_latex = str(n)
            n_tag = str(n)
            domain_latex = r"\text{all real numbers } \mathbb{R}"
            reason = (
                f"Raising any real number to a positive integer power "
                f"like ${n}$ is always defined, so the domain is all real "
                "numbers."
            )
        elif category == "neg_int":
            n = rng.choice(self._NEG_INT[difficulty])
            exp_latex = str(n)
            n_tag = str(n)
            domain_latex = (
                r"\{" + var + r" \in \mathbb{R} : " + var + r" \neq 0\}"
            )
            reason = (
                f"A negative integer exponent like ${n}$ means ${var}^{{{n}}} = "
                f"\\dfrac{{1}}{{{var}^{{{abs(n)}}}}}$, which is undefined when "
                f"${var} = 0$. The domain is all real numbers except $0$."
            )
        elif category == "half":
            exp_latex = r"\tfrac{1}{2}"
            n_tag = "half"
            domain_latex = (
                r"\{" + var + r" \in \mathbb{R} : " + var + r" \geq 0\}"
            )
            reason = (
                r"The exponent $\tfrac{1}{2}$ is the square root, "
                "which is only defined for nonnegative real numbers. The "
                f"domain is ${var} \\geq 0$."
            )
        else:  # third
            exp_latex = r"\tfrac{1}{3}"
            n_tag = "third"
            domain_latex = r"\text{all real numbers } \mathbb{R}"
            reason = (
                r"The exponent $\tfrac{1}{3}$ is the cube root, which "
                "is defined for every real number (positive, negative, or "
                "zero). The domain is all real numbers."
            )

        func_latex = f"f({var}) = {var}^{{{exp_latex}}}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (category, n_tag, var)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the domain of ${func_latex}$."
            ),
            answer_latex=f"${domain_latex}$",
            hints=[
                "Ask whether there is any real number that would make the expression undefined.",
                "Division by zero and even roots of negatives are the usual obstructions.",
                "Positive integer powers and odd roots are defined on all of the real line.",
            ],
            solution_steps_latex=[
                f"Examine the exponent: ${var}^{{{exp_latex}}}$.",
                reason,
                f"Therefore the domain of $f$ is ${domain_latex}$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-exponents-and-radicals",
            ],
        )


# ===========================================================================
# Topic 3: polynomial_functions_and_graphs
# ===========================================================================


def _format_polynomial_standard(coeffs: list[int]) -> str:
    """Render a polynomial given its coefficients from highest to lowest degree.

    Example: [2, 0, -3, 1] -> "2x^3 - 3x + 1".
    """
    degree = len(coeffs) - 1
    parts: list[str] = []
    for i, c in enumerate(coeffs):
        power = degree - i
        if c == 0:
            continue
        # Build the x^power piece
        if power == 0:
            x_part = ""
        elif power == 1:
            x_part = "x"
        else:
            x_part = f"x^{{{power}}}"
        # Leading (first nonzero) term
        if not parts:
            if c == 1 and x_part:
                parts.append(x_part)
            elif c == -1 and x_part:
                parts.append(f"-{x_part}")
            else:
                parts.append(f"{c}{x_part}")
        else:
            if c > 0:
                sign = " + "
            else:
                sign = " - "
            mag = abs(c)
            if mag == 1 and x_part:
                parts.append(f"{sign}{x_part}")
            else:
                parts.append(f"{sign}{mag}{x_part}")
    if not parts:
        return "0"
    return "".join(parts)


@register
class PolynomialEndBehavior(Generator):
    """Given a polynomial in standard form, classify its end behavior.

    Backward construction: pick degree d and leading sign, then random
    lower-order coefficients. The end behavior depends only on (d parity,
    leading sign).
    """
    generator_id = "polynomial_end_behavior"
    topic_slug = "polynomial_functions_and_graphs"
    display_name = "Determine end behavior of a polynomial"

    _DEGREE_CHOICES = {
        "easy": (2, 3, 4),
        "medium": (2, 3, 4, 5),
        "hard": (3, 4, 5, 6),
    }
    _LOWER_RANGES = {
        "easy": (-5, 5),
        "medium": (-10, 10),
        "hard": (-15, 15),
    }
    _LEADING_CHOICES = {
        "easy": (1, -1, 2, -2),
        "medium": (1, -1, 2, -2, 3, -3),
        "hard": (1, -1, 2, -2, 3, -3, 4, -4),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        degree = rng.choice(self._DEGREE_CHOICES[difficulty])
        leading = rng.choice(self._LEADING_CHOICES[difficulty])
        lo, hi = self._LOWER_RANGES[difficulty]
        # Build coefficients: index 0 is the leading coefficient.
        coeffs = [leading]
        for _ in range(degree):
            coeffs.append(rng.randint(lo, hi))

        is_even = (degree % 2 == 0)
        if is_even:
            if leading > 0:
                right_limit = r"+\infty"
                left_limit = r"+\infty"
            else:
                right_limit = r"-\infty"
                left_limit = r"-\infty"
        else:
            if leading > 0:
                right_limit = r"+\infty"
                left_limit = r"-\infty"
            else:
                right_limit = r"-\infty"
                left_limit = r"+\infty"

        parity_word = "even" if is_even else "odd"
        sign_word = "positive" if leading > 0 else "negative"
        poly_latex = _format_polynomial_standard(coeffs)
        func_latex = f"p(x) = {poly_latex}"

        answer = (
            f"As $x \\to +\\infty$, $p(x) \\to {right_limit}$; "
            f"as $x \\to -\\infty$, $p(x) \\to {left_limit}$."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (degree, leading, tuple(coeffs))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe the end behavior of ${func_latex}$."
            ),
            answer_latex=answer,
            hints=[
                "End behavior depends only on the leading term of the polynomial.",
                r"If the degree is even, both ends of the graph go in the same direction. If the degree is odd, the ends go opposite ways.",
                r"A positive leading coefficient leaves the graph un-flipped; a negative leading coefficient reflects it.",
            ],
            solution_steps_latex=[
                f"Identify the leading term: ${leading}x^{{{degree}}}$.",
                f"The degree is ${degree}$ ({parity_word}) and the leading coefficient is ${leading}$ ({sign_word}).",
                (
                    f"Because the degree is {parity_word}, "
                    + (
                        "both ends of the graph head the same way."
                        if is_even
                        else "the ends head in opposite directions."
                    )
                ),
                (
                    f"Because the leading coefficient is {sign_word}, "
                    + (
                        "the graph is not reflected."
                        if leading > 0
                        else "the graph is reflected across the $x$-axis."
                    )
                ),
                (
                    f"Therefore as $x \\to +\\infty$, $p(x) \\to {right_limit}$; "
                    f"and as $x \\to -\\infty$, $p(x) \\to {left_limit}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-polynomials",
                "#topic-functions",
            ],
        )


@register
class PolynomialRootsFromFactored(Generator):
    """Given a polynomial in factored form, list zeros and multiplicities.

    Backward construction: pick three distinct integer roots r1, r2, r3 and
    a multiplicity for r1 (either 1 or 2). For each zero also classify as
    "crosses" (odd multiplicity) or "bounces" (even multiplicity).
    """
    generator_id = "polynomial_roots_from_factored"
    topic_slug = "polynomial_functions_and_graphs"
    display_name = "Find zeros and multiplicities from a factored polynomial"

    _R_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _LEADING_CHOICES = {
        "easy": (1,),
        "medium": (1, -1, 2),
        "hard": (1, -1, 2, -2, 3),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]
        # Pick three distinct integer roots
        candidates = list(range(lo, hi + 1))
        rng.shuffle(candidates)
        r1, r2, r3 = candidates[0], candidates[1], candidates[2]
        # Multiplicity of r1 is either 1 or 2
        m1 = rng.choice([1, 2])
        leading = rng.choice(self._LEADING_CHOICES[difficulty])

        # Build factored form: leading * (x - r1)^m1 * (x - r2) * (x - r3)
        def factor(r: int, mult: int = 1) -> str:
            if r == 0:
                base = "x"
            elif r > 0:
                base = f"(x - {r})"
            else:
                base = f"(x + {-r})"
            if mult == 1:
                return base
            # Add explicit parentheses for bare x so "x^2" reads clean
            if r == 0:
                return f"x^{{{mult}}}"
            return f"{base}^{{{mult}}}"

        # Prefix
        if leading == 1:
            prefix = ""
        elif leading == -1:
            prefix = "-"
        else:
            prefix = f"{leading}"

        f1 = factor(r1, m1)
        f2 = factor(r2, 1)
        f3 = factor(r3, 1)
        func_latex = f"p(x) = {prefix}{f1}{f2}{f3}"

        def behavior(mult: int) -> str:
            return "crosses the $x$-axis" if mult % 2 == 1 else "bounces off the $x$-axis"

        roots_summary: list[tuple[int, int]] = [(r1, m1), (r2, 1), (r3, 1)]
        # Sort for deterministic display order
        roots_summary.sort()

        parts: list[str] = []
        for r, m in roots_summary:
            parts.append(f"$x = {r}$ (multiplicity ${m}$, {behavior(m)})")
        answer = "; ".join(parts) + "."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (leading, r1, r2, r3, m1)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"List the zeros of ${func_latex}$ together with their "
                "multiplicities. For each zero, say whether the graph "
                "crosses or bounces off the $x$-axis."
            ),
            answer_latex=answer,
            hints=[
                "Set each factor equal to $0$ and solve for $x$.",
                "The exponent on each factor is that zero's multiplicity.",
                r"Odd multiplicity $\Rightarrow$ the graph crosses; even multiplicity $\Rightarrow$ the graph bounces.",
            ],
            solution_steps_latex=[
                "Set each factor equal to zero.",
                (
                    f"From $(x - ({r1}))^{{{m1}}} = 0$ we get $x = {r1}$ with "
                    f"multiplicity ${m1}$ (the graph "
                    f"{behavior(m1)}). "
                    f"From $(x - ({r2})) = 0$ we get $x = {r2}$ with "
                    f"multiplicity $1$ (crosses). "
                    f"From $(x - ({r3})) = 0$ we get $x = {r3}$ with "
                    f"multiplicity $1$ (crosses)."
                ),
                f"The zeros with multiplicities are: {answer}",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-polynomials",
                "#topic-functions",
            ],
        )


@register
class PolynomialCountFeatures(Generator):
    """Given a polynomial, state max x-intercepts and max turning points.

    Backward construction: pick degree, then pick coefficients. The
    maximum number of x-intercepts equals the degree; the maximum number
    of turning points equals degree - 1.
    """
    generator_id = "polynomial_count_features"
    topic_slug = "polynomial_functions_and_graphs"
    display_name = "Count max x-intercepts and turning points of a polynomial"

    _DEGREE_CHOICES = {
        "easy": (2, 3, 4),
        "medium": (3, 4, 5),
        "hard": (4, 5, 6, 7),
    }
    _LOWER_RANGES = {
        "easy": (-5, 5),
        "medium": (-10, 10),
        "hard": (-15, 15),
    }
    _LEADING_CHOICES = {
        "easy": (1, -1, 2, -2),
        "medium": (1, -1, 2, -2, 3, -3),
        "hard": (1, -1, 2, -2, 3, -3, 4, -4),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        degree = rng.choice(self._DEGREE_CHOICES[difficulty])
        leading = rng.choice(self._LEADING_CHOICES[difficulty])
        lo, hi = self._LOWER_RANGES[difficulty]
        coeffs = [leading]
        for _ in range(degree):
            coeffs.append(rng.randint(lo, hi))

        poly_latex = _format_polynomial_standard(coeffs)
        func_latex = f"p(x) = {poly_latex}"
        max_intercepts = degree
        max_turning = degree - 1

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (degree, leading, tuple(coeffs))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Consider ${func_latex}$. State (a) the maximum possible "
                "number of $x$-intercepts and (b) the maximum possible number "
                "of turning points."
            ),
            answer_latex=(
                f"(a) at most ${max_intercepts}$ $x$-intercepts; "
                f"(b) at most ${max_turning}$ turning points."
            ),
            hints=[
                "The degree of a polynomial caps the number of real zeros.",
                "A polynomial of degree $n$ can have at most $n - 1$ turning points.",
                f"Here the degree is ${degree}$.",
            ],
            solution_steps_latex=[
                f"Read the degree from the leading term: degree $= {degree}$.",
                (
                    f"(a) A polynomial can have at most as many $x$-intercepts "
                    f"as its degree, so at most ${max_intercepts}$."
                ),
                (
                    f"(b) A polynomial can have at most $\\text{{degree}} - 1$ "
                    f"turning points, so at most ${max_turning}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-polynomials",
                "#topic-functions",
            ],
        )


# ===========================================================================
# Topic 4: transformations_i_shifts_and_reflections
# ===========================================================================


@register
class IdentifyShiftsFromFormula(Generator):
    """Given g(x) = f(x - h) + k, identify horizontal and vertical shifts."""
    generator_id = "identify_shifts_from_formula"
    topic_slug = "transformations_i_shifts_and_reflections"
    display_name = "Identify horizontal and vertical shifts from g(x) = f(x - h) + k"

    _H_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _K_RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        # Avoid the degenerate no-shift case.
        while h == 0 and k == 0:
            h = rng.randint(h_lo, h_hi)
            k = rng.randint(k_lo, k_hi)

        # Build g(x) LaTeX
        if h == 0:
            inside = "x"
        elif h > 0:
            inside = f"x - {h}"
        else:
            inside = f"x + {-h}"
        tail = _format_trailing_constant(k)
        g_latex = f"g(x) = f\\left({inside}\\right){tail}"

        if h == 0:
            h_desc = "no horizontal shift"
            h_direction = "none"
        elif h > 0:
            h_desc = f"horizontal shift of ${h}$ units to the right"
            h_direction = "right"
        else:
            h_desc = f"horizontal shift of ${-h}$ units to the left"
            h_direction = "left"

        if k == 0:
            k_desc = "no vertical shift"
            k_direction = "none"
        elif k > 0:
            k_desc = f"vertical shift of ${k}$ units upward"
            k_direction = "upward"
        else:
            k_desc = f"vertical shift of ${-k}$ units downward"
            k_direction = "downward"

        answer = f"(a) {h_desc}; (b) {k_desc}."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (h, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"The function ${g_latex}$ is a shifted version of $f$. "
                "Describe (a) the horizontal shift and (b) the vertical shift."
            ),
            answer_latex=answer,
            hints=[
                r"The template $g(x) = f(x - h) + k$ shifts the graph of $f$ by $h$ horizontally and $k$ vertically.",
                r"A minus sign inside the argument, $f(x - h)$, shifts to the right by $|h|$; a plus sign shifts to the left.",
                r"Adding $k$ outside the function shifts up; subtracting shifts down.",
            ],
            solution_steps_latex=[
                (
                    r"Compare $g(x)$ to the template "
                    r"$g(x) = f(x - h) + k$."
                ),
                f"Read off $h = {h}$ and $k = {k}$.",
                (
                    f"(a) Since $h = {h}$, the horizontal shift is "
                    f"{h_desc}."
                ),
                (
                    f"(b) Since $k = {k}$, the vertical shift is "
                    f"{k_desc}."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-transformations",
            ],
        )


@register
class IdentifyReflectionFromFormula(Generator):
    """Given g(x) = -f(x) or g(x) = f(-x), classify the reflection."""
    generator_id = "identify_reflection_from_formula"
    topic_slug = "transformations_i_shifts_and_reflections"
    display_name = "Identify reflection across x-axis or y-axis from formula"
    bank_count_per_difficulty = 20

    # We use different parent function names to diversify the bank.
    _PARENTS = ("f", "p", "q", "r", "h", "g")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Pick which reflection type (x-axis or y-axis)
        reflect_type = rng.choice(["x_axis", "y_axis"])
        # Pick a parent name and a new name for g
        parent = rng.choice(self._PARENTS)
        new_name = "g" if parent != "g" else "h"

        if reflect_type == "x_axis":
            g_latex = f"{new_name}(x) = -{parent}(x)"
            answer = "reflection across the $x$-axis"
            reason = (
                f"Negating the output, ${new_name}(x) = -{parent}(x)$, flips "
                f"every $y$-value of ${parent}$ to its opposite. That is a "
                "reflection across the $x$-axis."
            )
        else:
            g_latex = f"{new_name}(x) = {parent}(-x)"
            answer = "reflection across the $y$-axis"
            reason = (
                f"Negating the input, ${new_name}(x) = {parent}(-x)$, swaps "
                "every input with its opposite. That flips the graph across "
                "the $y$-axis."
            )

        # Throw in some difficulty by varying the problem wording on harder levels
        if difficulty == "hard":
            statement_prefix = (
                f"Given the parent function ${parent}$, the new function "
            )
        else:
            statement_prefix = "The function "

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (reflect_type, parent, new_name)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{statement_prefix}${g_latex}$ is a reflection of "
                f"${parent}$. Which reflection is it: across the $x$-axis or "
                "across the $y$-axis?"
            ),
            answer_latex=answer.capitalize() + ".",
            hints=[
                r"A minus sign on the *outside* of the function, $-f(x)$, negates $y$-values and reflects across the $x$-axis.",
                r"A minus sign on the *inside* of the function, $f(-x)$, negates $x$-values and reflects across the $y$-axis.",
                "Look carefully at where the minus sign is placed.",
            ],
            solution_steps_latex=[
                f"Compare ${g_latex}$ to the two reflection templates "
                r"$-f(x)$ (across $x$-axis) and $f(-x)$ (across $y$-axis).",
                reason,
                f"Therefore ${new_name}$ is a {answer}.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-transformations",
            ],
        )


@register
class DescribeTransformationCombined(Generator):
    """Given g(x) = -|x + 3| - 2 (or similar), describe all transformations.

    Backward construction: pick a parent (|x|, x^2, sqrt(x), x^3), pick
    reflection sign, horizontal shift h, and vertical shift k. Build g(x)
    and describe the transformations in the conventional order: horizontal
    shift, reflection, vertical shift.
    """
    generator_id = "describe_transformation_combined"
    topic_slug = "transformations_i_shifts_and_reflections"
    display_name = "Describe all transformations of a parent function"

    _PARENTS = (
        ("abs", r"|x|", "|{inside}|", "absolute-value"),
        ("sq", r"x^2", "({inside})^2", "squaring"),
        ("sqrt", r"\sqrt{x}", r"\sqrt{{{inside}}}", "square-root"),
        ("cube", r"x^3", "({inside})^3", "cubing"),
    )
    _H_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _K_RANGES = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        parent_code, parent_latex, body_template, parent_word = rng.choice(self._PARENTS)
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        reflect = rng.choice([1, -1])
        # Avoid fully-degenerate case
        while reflect == 1 and h == 0 and k == 0:
            h = rng.randint(h_lo, h_hi)
            k = rng.randint(k_lo, k_hi)
            reflect = rng.choice([1, -1])

        # Build inside expression (x - h)
        if h == 0:
            inside = "x"
        elif h > 0:
            inside = f"x - {h}"
        else:
            inside = f"x + {-h}"
        body = body_template.format(inside=inside)

        prefix = "-" if reflect == -1 else ""
        tail = _format_trailing_constant(k)
        g_latex = f"g(x) = {prefix}{body}{tail}"
        f_latex = f"f(x) = {parent_latex}"

        # Horizontal shift description
        if h == 0:
            h_desc = "no horizontal shift"
        elif h > 0:
            h_desc = f"horizontal shift {h} units to the right"
        else:
            h_desc = f"horizontal shift {-h} units to the left"

        # Reflection description
        if reflect == -1:
            reflect_desc = "reflection across the $x$-axis"
        else:
            reflect_desc = "no reflection"

        # Vertical shift description
        if k == 0:
            k_desc = "no vertical shift"
        elif k > 0:
            k_desc = f"vertical shift {k} units upward"
        else:
            k_desc = f"vertical shift {-k} units downward"

        answer = (
            f"(a) {h_desc}; (b) {reflect_desc}; (c) {k_desc}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (parent_code, reflect, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Starting from the parent function ${f_latex}$, describe the "
                f"transformations that produce ${g_latex}$. Give (a) any "
                "horizontal shift, (b) any reflection, and (c) any vertical "
                "shift."
            ),
            answer_latex=answer,
            hints=[
                "Work from the inside out: first the argument tells you the horizontal shift, then an outer minus sign flips across the $x$-axis, then the outside constant shifts vertically.",
                r"A minus sign inside the argument shifts right; a plus sign inside shifts left.",
                r"A minus sign outside the entire expression reflects across the $x$-axis.",
            ],
            solution_steps_latex=[
                (
                    f"Identify the parent function ${f_latex}$ inside the "
                    "formula for $g$."
                ),
                (
                    f"(a) The inside of the {parent_word} is "
                    f"$({inside})$, which means " + (
                        "no horizontal shift."
                        if h == 0
                        else (
                            f"a horizontal shift {h} units to the right."
                            if h > 0
                            else f"a horizontal shift {-h} units to the left."
                        )
                    )
                ),
                (
                    f"(b) The leading sign is "
                    f"'{'negative' if reflect == -1 else 'positive'}', so "
                    f"there is {reflect_desc}."
                ),
                (
                    f"(c) The trailing constant is ${k}$, giving "
                    + (
                        "no vertical shift."
                        if k == 0
                        else (
                            f"a vertical shift of {k} units upward."
                            if k > 0
                            else f"a vertical shift of {-k} units downward."
                        )
                    )
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#topic-transformations",
            ],
        )
