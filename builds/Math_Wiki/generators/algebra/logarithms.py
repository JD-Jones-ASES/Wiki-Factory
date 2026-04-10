"""Logarithm and exponential application generators.

Five topic slugs covered:

- logarithms (Logarithms.md, Algebra 2)
- logarithmic_functions (Logarithmic_Functions.md, Algebra 2)
- logarithmic_equations (Logarithmic_Equations.md, Algebra 2)
- properties_of_logarithms (Properties_Of_Logarithms.md, pre-calculus)
- applications_of_exponentials_and_logarithms
    (Applications_Of_Exponentials_And_Logarithms.md, pre-calculus)

Fifteen generators total (3 per topic). Backward construction is used
throughout: pick the clean answer first, then derive the statement.
"""
from __future__ import annotations

import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _log_base(base: int, x: int | str) -> str:
    """Render log_b(x) in LaTeX."""
    return rf"\log_{{{base}}}\!\left({x}\right)"


def _log_common(x: int | str) -> str:
    """Render common log (base 10) in LaTeX."""
    return rf"\log\!\left({x}\right)"


def _log_natural(x: int | str) -> str:
    """Render natural log (base e) in LaTeX."""
    return rf"\ln\!\left({x}\right)"


def _fmt_signed(n: int) -> str:
    """Return '+n' or '-n' for n != 0, '' for 0."""
    if n == 0:
        return ""
    if n > 0:
        return f" + {n}"
    return f" - {-n}"


def _fmt_shift_inside(h: int, var: str = "x") -> str:
    """Render (x - h) inside a log argument."""
    if h == 0:
        return var
    if h > 0:
        return f"{var} - {h}"
    return f"{var} + {-h}"


def _fmt_a_coef(a: int) -> str:
    """Hide 1 and -1 leading coefficients."""
    if a == 1:
        return ""
    if a == -1:
        return "-"
    return str(a)


# ===========================================================================
# Topic 1: logarithms
# ===========================================================================


@register
class LogEvaluateCleanBase(Generator):
    """Evaluate log_b(x) where x = b^n so the answer is a small integer.

    Backward: pick base b in {2, 3, 4, 5, 6, 7} and integer exponent n >= 1;
    compute the argument b^n.
    """
    generator_id = "log_evaluate_clean_base"
    topic_slug = "logarithms"
    display_name = "Evaluate log_b(b^n) for clean integer base and exponent"

    _BASE_CHOICES = {
        "easy": (2, 3, 5),
        "medium": (2, 3, 4, 5, 6, 7),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10),
    }
    _N_RANGES = {
        "easy": (1, 4),
        "medium": (1, 5),
        "hard": (2, 6),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        base = rng.choice(self._BASE_CHOICES[difficulty])
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        arg = base ** n
        statement_inner = _log_base(base, arg)
        answer = str(n)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (base, n)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${statement_inner}$.",
            answer_latex=f"${answer}$",
            hints=[
                (
                    r"By definition, $\log_b(x) = y$ means $b^y = x$. Ask yourself: "
                    "to what power must $b$ be raised to give $x$?"
                ),
                f"Rewrite the argument as a power of {base}: ${arg} = {base}^{{{n}}}$.",
                f"The exponent is the value of the log.",
            ],
            solution_steps_latex=[
                f"Start with ${statement_inner}$.",
                f"Write the argument as a power of the base: ${arg} = {base}^{{{n}}}$.",
                f"So ${statement_inner} = \\log_{{{base}}}({base}^{{{n}}}) = {n}$.",
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


@register
class LogEvaluateNaturalAndCommon(Generator):
    """Evaluate common log (base 10) and natural log (base e) at clean powers.

    Backward: pick whether we use log or ln and pick an integer exponent.
    For log, argument is 10^n (e.g., 1000); for ln, argument is e^n (e.g.,
    e^4). Also includes the ln(1) = 0 and log(1) = 0 base cases.
    """
    generator_id = "log_evaluate_natural_and_common"
    topic_slug = "logarithms"
    display_name = "Evaluate common logs and natural logs at clean powers"
    # Small parameter space: 2 kinds * ~10 exponent values max.
    bank_count_per_difficulty = 16

    _N_RANGES = {
        "easy": (0, 5),
        "medium": (-3, 5),
        "hard": (-5, 7),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        kind = rng.choice(["log", "ln"])
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        if kind == "log":
            # log(10^n) = n
            if n == 0:
                arg_latex = "1"
                reason = "Since $10^0 = 1$,"
            elif n >= 1:
                arg_latex = str(10 ** n)
                reason = f"Since $10^{{{n}}} = {10 ** n}$,"
            else:
                # negative exponent -> 10^-n form
                arg_latex = rf"10^{{{n}}}"
                reason = f"Since $10^{{{n}}}$ is already in power form,"
            statement_inner = _log_common(arg_latex)
            answer = str(n)
            hint_def = (
                r"The common log $\log(x)$ is log base 10: $\log(x) = y$ "
                r"means $10^y = x$."
            )
            power_line = (
                rf"Rewrite the argument as a power of 10: "
                rf"${arg_latex if n < 0 else str(10 ** n)} = 10^{{{n}}}$."
                if n != 0
                else r"The argument is $1 = 10^0$."
            )
        else:  # ln
            if n == 0:
                arg_latex = "1"
                reason = "Since $e^0 = 1$,"
            else:
                arg_latex = f"e^{{{n}}}" if n != 1 else "e"
                reason = f"Since $\\ln$ and $e$ are inverses,"
            statement_inner = _log_natural(arg_latex)
            answer = str(n)
            hint_def = (
                r"The natural log $\ln(x)$ is log base $e$: $\ln(x) = y$ "
                r"means $e^y = x$."
            )
            power_line = (
                r"The argument is $1 = e^0$, so the value is $0$."
                if n == 0
                else f"The argument is already a power of $e$: $e^{{{n}}}$."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (kind, n)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${statement_inner}$.",
            answer_latex=f"${answer}$",
            hints=[
                hint_def,
                f"{reason} the exponent gives the log value directly.",
            ],
            solution_steps_latex=[
                f"Start with ${statement_inner}$.",
                power_line,
                f"Therefore ${statement_inner} = {answer}$.",
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


@register
class LogConvertToExponentialForm(Generator):
    """Convert between logarithmic and exponential form.

    Two directions (picked randomly):

    1. Given log_b(x) = y, rewrite as b^y = x.
    2. Given b^y = x, rewrite as log_b(x) = y.
    """
    generator_id = "log_convert_to_exponential_form"
    topic_slug = "logarithms"
    display_name = "Convert between log form and exponential form"

    _BASE_CHOICES = {
        "easy": (2, 3, 5),
        "medium": (2, 3, 4, 5, 6, 7, 10),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10),
    }
    _Y_RANGES = {
        "easy": (1, 4),
        "medium": (1, 5),
        "hard": (-3, 6),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        direction = rng.choice(["log_to_exp", "exp_to_log"])
        base = rng.choice(self._BASE_CHOICES[difficulty])
        y_lo, y_hi = self._Y_RANGES[difficulty]
        y = rng.randint(y_lo, y_hi)
        while y == 0:
            y = rng.randint(y_lo, y_hi)

        # Compute x = b^y as an exact sympy number, then render cleanly.
        if y >= 0:
            x_val = base ** y
            x_latex = str(x_val)
        else:
            x_val_frac = Fraction(1, base ** (-y))
            x_latex = rf"\frac{{1}}{{{base ** (-y)}}}"

        if direction == "log_to_exp":
            statement_inner = f"{_log_base(base, x_latex)} = {y}"
            answer = f"{base}^{{{y}}} = {x_latex}"
            hints = [
                (
                    r"Use the definition $\log_b(x) = y \iff b^y = x$. The base of the "
                    "log becomes the base of the exponential, and the log value "
                    "becomes the exponent."
                ),
                f"Here $b = {base}$, $y = {y}$, and $x = {x_latex}$.",
            ]
            steps = [
                f"Start with ${statement_inner}$.",
                r"Apply the definition $\log_b(x) = y \iff b^y = x$.",
                f"Rewrite: ${base}^{{{y}}} = {x_latex}$.",
            ]
            statement_text = (
                f"Rewrite ${statement_inner}$ in exponential form."
            )
        else:  # exp_to_log
            statement_inner = f"{base}^{{{y}}} = {x_latex}"
            answer = f"{_log_base(base, x_latex)} = {y}"
            hints = [
                (
                    r"Use the definition $b^y = x \iff \log_b(x) = y$. The base of the "
                    "exponential becomes the base of the log, the exponent becomes "
                    "the log value, and the result becomes the argument."
                ),
                f"Here $b = {base}$, $y = {y}$, and $x = {x_latex}$.",
            ]
            steps = [
                f"Start with ${statement_inner}$.",
                r"Apply the definition $b^y = x \iff \log_b(x) = y$.",
                f"Rewrite: ${_log_base(base, x_latex)} = {y}$.",
            ]
            statement_text = (
                f"Rewrite ${statement_inner}$ in logarithmic form."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (direction, base, y)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_text,
            answer_latex=f"${answer}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


# ===========================================================================
# Topic 2: logarithmic_functions
# ===========================================================================


@register
class LogFunctionDomain(Generator):
    """State the domain of f(x) = log_b(x - h).

    Backward construction: pick the lower bound h so the domain is x > h.
    """
    generator_id = "log_function_domain"
    topic_slug = "logarithmic_functions"
    display_name = "Find the domain of f(x) = log_b(x - h)"

    _BASE_CHOICES = {
        "easy": (2, 10, "e"),
        "medium": (2, 3, 5, 10, "e"),
        "hard": (2, 3, 4, 5, 6, 7, 10, "e"),
    }
    _H_RANGES = {
        "easy": (-6, 6),
        "medium": (-12, 12),
        "hard": (-20, 20),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        base = rng.choice(self._BASE_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)

        inside = _fmt_shift_inside(h)

        if base == "e":
            log_latex = rf"\ln\!\left({inside}\right)"
        elif base == 10:
            log_latex = rf"\log\!\left({inside}\right)"
        else:
            log_latex = rf"\log_{{{base}}}\!\left({inside}\right)"

        function_latex = f"f(x) = {log_latex}"
        answer = f"$x > {h}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (str(base), h)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the domain of ${function_latex}$. "
                "Give your answer as an inequality in $x$."
            ),
            answer_latex=answer,
            hints=[
                (
                    r"A logarithm is only defined when its argument is strictly "
                    "positive. Set the argument $> 0$ and solve."
                ),
                f"Set up the inequality: ${inside} > 0$.",
                f"Solve for $x$: $x > {h}$.",
            ],
            solution_steps_latex=[
                r"Logarithms require a positive argument: $\text{argument} > 0$.",
                f"Set ${inside} > 0$.",
                (
                    f"Add ${h}$ to both sides: $x > {h}$."
                    if h > 0
                    else (
                        f"Subtract ${-h}$ from both sides: $x > {h}$."
                        if h < 0
                        else r"The inequality simplifies directly to $x > 0$."
                    )
                ),
                f"The domain is $x > {h}$.",
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


@register
class LogFunctionEvaluate(Generator):
    """Evaluate f(x) = a * log_b(x - h) + k at an input where the argument
    is a clean power of b.

    Backward: pick a, b, h, k, and an integer exponent n. The input is
    h + b^n so that log_b(input - h) = n. Output = a*n + k.
    """
    generator_id = "log_function_evaluate"
    topic_slug = "logarithmic_functions"
    display_name = "Evaluate f(x) = a * log_b(x - h) + k at a clean input"

    _A_CHOICES = {
        "easy": (1, 2),
        "medium": (1, 2, 3, -1, -2),
        "hard": (1, 2, 3, 4, -1, -2, -3),
    }
    _BASE_CHOICES = {
        "easy": (2, 3),
        "medium": (2, 3, 5, 10),
        "hard": (2, 3, 4, 5, 10),
    }
    _H_RANGES = {
        "easy": (-4, 4),
        "medium": (-8, 8),
        "hard": (-12, 12),
    }
    _K_RANGES = {
        "easy": (-6, 6),
        "medium": (-12, 12),
        "hard": (-20, 20),
    }
    _N_CHOICES = {
        "easy": (0, 1, 2, 3),
        "medium": (0, 1, 2, 3, 4),
        "hard": (0, 1, 2, 3, 4, 5),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        base = rng.choice(self._BASE_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        k = rng.randint(k_lo, k_hi)
        n = rng.choice(self._N_CHOICES[difficulty])

        input_val = h + base ** n
        output_val = a * n + k

        a_prefix = _fmt_a_coef(a)
        inside_expr = _fmt_shift_inside(h)
        k_tail = _fmt_signed(k)

        # Pretty print: if base == 10 use log, if coefficient etc.
        if base == 10:
            log_expr = rf"\log\!\left({inside_expr}\right)"
        else:
            log_expr = rf"\log_{{{base}}}\!\left({inside_expr}\right)"
        func_latex = f"f(x) = {a_prefix}{log_expr}{k_tail}"

        # Build the substituted version
        if h == 0:
            sub_inside = f"{input_val}"
        elif h > 0:
            sub_inside = f"{input_val} - {h}"
        else:
            sub_inside = f"{input_val} + {-h}"

        inside_val = input_val - h  # equals base**n
        if base == 10:
            log_sub = rf"\log({sub_inside})"
            log_simp = rf"\log({inside_val})"
        else:
            log_sub = rf"\log_{{{base}}}({sub_inside})"
            log_simp = rf"\log_{{{base}}}({inside_val})"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, base, h, k, n)
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
                (
                    f"Simplify the argument: ${sub_inside} = {inside_val}$. "
                    f"Then ${inside_val} = {base}^{{{n}}}$, so "
                    f"$\\log_{{{base}}}({inside_val}) = {n}$."
                ),
                f"Multiply by $a = {a}$ and add $k = {k}$.",
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {input_val}$: "
                    f"$f({input_val}) = {a_prefix}{log_sub}{k_tail}$."
                ),
                (
                    f"Simplify the argument: "
                    f"$f({input_val}) = {a_prefix}{log_simp}{k_tail}$."
                ),
                (
                    f"Write the argument as a power of the base: "
                    f"${inside_val} = {base}^{{{n}}}$, so the log value is ${n}$."
                ),
                (
                    f"Multiply and add: "
                    f"$f({input_val}) = {a * n}{k_tail} = {output_val}$."
                ),
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


@register
class LogFunctionKeyFeatures(Generator):
    """Identify vertical asymptote, x-intercept, and direction of
    f(x) = a * log_b(x - h) + k.

    - Vertical asymptote: x = h.
    - x-intercept: solve a*log_b(x - h) + k = 0 => log_b(x-h) = -k/a =>
      x = h + b^(-k/a). We pick k so that -k/a is a small integer so
      the x-intercept is clean.
    - Direction: increasing if a > 0 (and b > 1), decreasing if a < 0.
    """
    generator_id = "log_function_key_features"
    topic_slug = "logarithmic_functions"
    display_name = "Key features (asymptote, x-intercept, direction) of a log function"
    # Parameter space is tight because we need clean intercepts.
    bank_count_per_difficulty = 25

    _A_CHOICES = {
        "easy": (1, 2, -1, -2),
        "medium": (1, 2, 3, -1, -2, -3),
        "hard": (1, 2, 3, 4, -1, -2, -3, -4),
    }
    _BASE_CHOICES = {
        "easy": (2, 3, 10),
        "medium": (2, 3, 5, 10),
        "hard": (2, 3, 4, 5, 6, 10),
    }
    _H_RANGES = {
        "easy": (-4, 4),
        "medium": (-8, 8),
        "hard": (-12, 12),
    }
    # We need -k/a to be a small integer in {-2,-1,0,1,2}. That means
    # k ∈ {-2a, -a, 0, a, 2a}.
    _M_CHOICES = {
        "easy": (-1, 0, 1, 2),
        "medium": (-2, -1, 0, 1, 2),
        "hard": (-2, -1, 0, 1, 2, 3),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        base = rng.choice(self._BASE_CHOICES[difficulty])
        h_lo, h_hi = self._H_RANGES[difficulty]
        h = rng.randint(h_lo, h_hi)
        m = rng.choice(self._M_CHOICES[difficulty])  # m = -k/a, so k = -m*a
        k = -m * a

        # x-intercept satisfies a*log_b(x-h) + k = 0 => log_b(x-h) = -k/a = m
        # => x = h + b^m
        x_intercept = h + base ** m

        a_prefix = _fmt_a_coef(a)
        inside_expr = _fmt_shift_inside(h)
        k_tail = _fmt_signed(k)

        if base == 10:
            log_expr = rf"\log\!\left({inside_expr}\right)"
        else:
            log_expr = rf"\log_{{{base}}}\!\left({inside_expr}\right)"
        func_latex = f"f(x) = {a_prefix}{log_expr}{k_tail}"

        direction = "increasing" if a > 0 else "decreasing"

        answer = (
            f"Vertical asymptote: $x = {h}$; "
            f"$x$-intercept: $({x_intercept}, 0)$; "
            f"direction: {direction}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, base, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, identify (a) the vertical asymptote, "
                "(b) the $x$-intercept, and (c) whether the function is "
                "increasing or decreasing."
            ),
            answer_latex=answer,
            hints=[
                (
                    r"The vertical asymptote of $f(x) = a\log_b(x-h) + k$ is at "
                    r"$x = h$ --- where the argument would be zero."
                ),
                (
                    r"To find the $x$-intercept, set $f(x) = 0$ and solve. "
                    r"You will get $\log_b(x - h) = -k/a$, so $x - h = b^{-k/a}$."
                ),
                (
                    "The direction is controlled by the sign of $a$. Since the base "
                    "$b > 1$, positive $a$ means increasing, negative $a$ means "
                    "decreasing."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$. Read off $a = {a}$, $b = {base}$, "
                f"$h = {h}$, $k = {k}$.",
                (
                    f"(a) The vertical asymptote is where the log argument hits "
                    f"zero: $x - ({h}) = 0 \\Rightarrow x = {h}$."
                ),
                (
                    f"(b) For the $x$-intercept, set $f(x) = 0$: "
                    f"${a_prefix}{log_expr}{k_tail} = 0$, so "
                    f"$\\log_{{{base}}}({inside_expr}) = {m}$."
                ),
                (
                    f"Convert to exponential form: ${inside_expr} = {base}^{{{m}}} "
                    f"= {base ** m}$, giving $x = {h} + {base ** m} = {x_intercept}$."
                ),
                (
                    f"(c) Since $a = {a}$ and the base is greater than 1, $f$ is "
                    f"{direction}."
                ),
                answer,
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


# ===========================================================================
# Topic 3: logarithmic_equations
# ===========================================================================


@register
class LogEqSingleLog(Generator):
    """Solve log_b(x) = c, which converts to x = b^c.

    Backward: pick b and a small integer c; the answer is x = b^c.
    """
    generator_id = "log_eq_single_log"
    topic_slug = "logarithmic_equations"
    display_name = "Solve log_b(x) = c"

    _BASE_CHOICES = {
        "easy": (2, 3, 10, "e"),
        "medium": (2, 3, 4, 5, 10, "e"),
        "hard": (2, 3, 4, 5, 6, 7, 10, "e"),
    }
    _C_RANGES = {
        "easy": (1, 4),
        "medium": (1, 5),
        "hard": (-2, 5),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        base = rng.choice(self._BASE_CHOICES[difficulty])
        c_lo, c_hi = self._C_RANGES[difficulty]
        c = rng.randint(c_lo, c_hi)
        while c == 0:
            c = rng.randint(c_lo, c_hi)

        if base == "e":
            base_num = sp.E
            base_display = "e"
            log_latex = rf"\ln(x)"
            if c >= 1:
                x_latex = f"e^{{{c}}}" if c != 1 else "e"
            else:
                x_latex = f"e^{{{c}}}"
            x_val_latex = x_latex
        else:
            base_num = base
            base_display = str(base)
            if base == 10:
                log_latex = rf"\log(x)"
            else:
                log_latex = rf"\log_{{{base}}}(x)"
            if c >= 0:
                x_val = base ** c
                x_val_latex = str(x_val)
            else:
                x_val_latex = rf"\frac{{1}}{{{base ** (-c)}}}"

        statement_inner = f"{log_latex} = {c}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (str(base), c)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve for $x$: ${statement_inner}$.",
            answer_latex=f"$x = {x_val_latex}$",
            hints=[
                (
                    r"Convert to exponential form: $\log_b(x) = c$ becomes "
                    r"$x = b^c$."
                ),
                f"Here the base is ${base_display}$ and the log value is ${c}$, "
                f"so $x = {base_display}^{{{c}}}$.",
            ],
            solution_steps_latex=[
                f"Start with ${statement_inner}$.",
                (
                    r"Apply the definition $\log_b(x) = c \iff x = b^c$."
                ),
                f"Substitute: $x = {base_display}^{{{c}}} = {x_val_latex}$.",
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


@register
class LogEqCombineLogs(Generator):
    """Solve log(x) + log(x - a) = c by combining with the product rule,
    converting to exponential form, and solving the resulting quadratic.

    Backward construction:
      Pick a positive integer x (the desired root), a positive offset a
      with a < x, and a base b. Compute the product p = x(x - a), then
      c = log_b(p). Choose parameters so c is a small integer.
    """
    generator_id = "log_eq_combine_logs"
    topic_slug = "logarithmic_equations"
    display_name = "Solve a log equation using the product rule"
    # Tight construction: few clean (x, a, b) triples land on integer c.
    bank_count_per_difficulty = 20

    # Curated lists of (base, x, a) triples where x*(x-a) is a clean power of base.
    _TRIPLES_EASY = [
        (10, 5, 3),    # 5*2 = 10 = 10^1
        (10, 25, 21),  # 25*4 = 100 = 10^2
        (2, 4, 2),     # 4*2 = 8 = 2^3
        (2, 8, 6),     # 8*2 = 16 = 2^4
        (3, 3, 2),     # 3*1 = 3 = 3^1
        (3, 9, 8),     # 9*1 = 9 = 3^2
        (5, 5, 4),     # 5*1 = 5 = 5^1
        (5, 25, 24),   # 25*1 = 25 = 5^2
        (4, 4, 3),     # 4*1 = 4 = 4^1
        (4, 16, 15),   # 16*1 = 16 = 4^2
        (6, 6, 5),     # 6*1 = 6 = 6^1
        (7, 7, 6),     # 7*1 = 7 = 7^1
    ]
    _TRIPLES_MEDIUM = _TRIPLES_EASY + [
        (10, 20, 15),  # 20*5 = 100 = 10^2
        (10, 50, 48),  # 50*2 = 100 = 10^2
        (10, 100, 99), # 100*1 = 100 = 10^2
        (2, 16, 14),   # 16*2 = 32 = 2^5
        (2, 32, 30),   # 32*2 = 64 = 2^6
        (3, 27, 26),   # 27*1 = 27 = 3^3
        (5, 125, 124), # 125*1 = 125 = 5^3
        (4, 4, 3),     # 4*1 = 4 = 4^1
        (4, 16, 15),   # 16*1 = 16 = 4^2
        (6, 6, 5),     # 6*1 = 6 = 6^1
        (6, 36, 35),   # 36*1 = 36 = 6^2
    ]
    _TRIPLES_HARD = _TRIPLES_MEDIUM + [
        (2, 32, 28),   # 32*4 = 128 = 2^7
        (2, 64, 62),   # 64*2 = 128 = 2^7
        (3, 27, 24),   # 27*3 = 81 = 3^4
        (10, 25, 21),  # 100 = 10^2 (dup insurance)
        (7, 7, 6),     # 7*1 = 7 = 7^1
        (7, 49, 48),   # 49*1 = 49 = 7^2
        (10, 125, 117),# 125*8 = 1000 = 10^3
    ]

    _TRIPLE_SETS = {
        "easy": _TRIPLES_EASY,
        "medium": _TRIPLES_MEDIUM,
        "hard": _TRIPLES_HARD,
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = self._TRIPLE_SETS[difficulty]
        base, x_val, a = rng.choice(triples)
        product = x_val * (x_val - a)
        # Compute exponent c such that base^c = product
        c = int(round(sp.log(product, base)))
        # Sanity check (should always hold for curated triples)
        assert base ** c == product, f"bad triple: {base}, {x_val}, {a}"

        if base == 10:
            log_l = r"\log"
        else:
            log_l = rf"\log_{{{base}}}"

        # Build the equation: log_b(x) + log_b(x - a) = c
        statement_inner = (
            rf"{log_l}(x) + {log_l}(x - {a}) = {c}"
        )

        # Solve the quadratic: x*(x-a) = base^c -> x^2 - a*x - base^c = 0
        # The positive root is x_val.
        quad_expr = f"x^2 - {a}x - {product} = 0"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (base, x_val, a)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve for $x$: ${statement_inner}$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                (
                    r"Use the product rule: $\log_b(M) + \log_b(N) = \log_b(MN)$."
                ),
                (
                    f"Combine to get ${log_l}(x(x - {a})) = {c}$, then convert "
                    f"to exponential form."
                ),
                (
                    "After exponentiating, you will get a quadratic. Solve it and "
                    "reject any root that makes a log argument $\\leq 0$."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${statement_inner}$.",
                (
                    rf"Apply the product rule: ${log_l}\bigl(x(x - {a})\bigr) = {c}$."
                ),
                (
                    rf"Convert to exponential form: "
                    rf"$x(x - {a}) = {base}^{{{c}}} = {product}$."
                ),
                f"Expand and rearrange: ${quad_expr}$.",
                (
                    f"Solving this quadratic gives $x = {x_val}$ (the other root "
                    f"is negative and rejected, since $\\log$ requires a positive "
                    "argument)."
                ),
                f"Verify: $x = {x_val}$ gives positive arguments $x = {x_val}$ "
                f"and $x - {a} = {x_val - a}$, both positive, so the answer is "
                f"$x = {x_val}$.",
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


@register
class LogEqExtraneousSolution(Generator):
    """Construct an equation where solving mechanically gives two candidate
    roots, one of which is valid and the other extraneous (makes a log
    argument nonpositive).

    Strategy: start from log_b(x^2 - a*x) = c where the quadratic
    x^2 - a*x - base^c = 0 has roots r1 > 0 > r2. The valid solution is r1;
    r2 is extraneous because it makes x or x - a (and hence the radicand)
    nonpositive.

    Actually we use log_b(x) + log_b(x - a) = c and choose a > 0 such that
    solving via substitution gives a negative candidate root as the
    companion to the positive one. With x^2 - a*x - base^c = 0, the roots
    are (a +/- sqrt(a^2 + 4*base^c))/2. The "+" root is positive; the "-"
    root is negative for any a > 0, base^c > 0. Perfect --- the negative
    root makes log_b(x) undefined.
    """
    generator_id = "log_eq_extraneous_solution"
    topic_slug = "logarithmic_equations"
    display_name = "Solve a log equation and reject the extraneous root"
    bank_count_per_difficulty = 20

    # Each triple: (base, a, product) where product is the clean power of base
    # and the quadratic x^2 - a*x - product = 0 has integer positive root and
    # negative extraneous root.
    _TRIPLES_EASY = [
        # (b, a, product) => positive root computed. Choose discriminant perfect square.
        (10, 5, 6),      # D = 25 + 24 = 49; roots = (5 +/- 7)/2 = 6 or -1; 6*1=6? no 6*(6-5)=6 yes
        (2, 3, 4),       # D = 9 + 16 = 25; roots = (3 +/- 5)/2 = 4 or -1; 4*(4-3)=4=2^2
        (2, 1, 6),       # D = 1 + 24 = 25; roots = (1 +/- 5)/2 = 3 or -2; 3*(3-1)=6 -- but 6 is not power of 2. Fixme
    ]
    # Revalidate trip #3 above: need base^c = product.
    # Let me do this more carefully with computed verification below.

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Build a curated list in __init__-style but inside the method so we
        # can recompute deterministically. Each entry: (base, a, pos_root).
        # We require (pos_root)*(pos_root - a) to be a power of base.
        candidates_easy = [
            # (base, a, pos_root)
            (10, 5, 5),   # 5*0 = 0  -- invalid argument 0. Skip.
        ]
        # Use a verified list instead.
        triples_easy = [
            (2, 2, 4),    # 4*(4-2)=8=2^3
            (3, 2, 3),    # 3*(3-2)=3=3^1
            (5, 4, 5),    # 5*(5-4)=5=5^1
            (10, 9, 10),  # 10*(10-9)=10=10^1
            (10, 99, 100),# 100*(100-99)=100=10^2
            (2, 6, 8),    # 8*(8-6)=16=2^4
            (2, 14, 16),  # 16*(16-14)=32=2^5
            (3, 6, 9),    # 9*(9-6)=27=3^3
            (3, 8, 9),    # 9*(9-8)=9=3^2
            (5, 24, 25),  # 25*(25-24)=25=5^2
            (6, 5, 6),    # 6*(6-5)=6=6^1
            (6, 35, 36),  # 36*(36-35)=36=6^2
        ]
        triples_medium = triples_easy + [
            (2, 4, 8),    # 8*(8-4)=32=2^5
            (2, 30, 32),  # 32*(32-30)=64=2^6
            (2, 62, 64),  # 64*(64-62)=128=2^7
            (3, 24, 27),  # 27*(27-24)=81=3^4
            (4, 15, 16),  # 16*(16-15)=16=4^2
            (5, 124, 125),# 125*(125-124)=125=5^3
            (7, 48, 49),  # 49*(49-48)=49=7^2
            (10, 999, 1000),# 1000*1=1000=10^3
        ]
        triples_hard = triples_medium + [
            (2, 126, 128),# 128*(128-126)=256=2^8
            (3, 80, 81),  # 81*(81-80)=81=3^4
            (8, 7, 8),    # 8*(8-7)=8=8^1
            (9, 8, 9),    # 9*(9-8)=9=9^1
            (10, 9, 10),  # already, harmless
        ]
        table = {
            "easy": triples_easy,
            "medium": triples_medium,
            "hard": triples_hard,
        }[difficulty]

        base, a, pos_root = rng.choice(table)

        product = pos_root * (pos_root - a)
        # Confirm product is a positive power of base.
        if product <= 0:
            # Fall back to the first known-good easy triple
            base, a, pos_root = (2, 2, 4)
            product = pos_root * (pos_root - a)

        c = int(round(sp.log(product, base)))
        # Hard assertion so a bad curated triple fails loudly instead of shipping.
        assert base ** c == product, (
            f"bad extraneous triple: base={base}, a={a}, pos={pos_root}, "
            f"product={product}"
        )

        # Compute the negative candidate root from the quadratic
        # x^2 - a*x - product = 0. Positive root is pos_root by construction;
        # negative root is sum_of_roots - pos_root = a - pos_root (Vieta).
        neg_root = a - pos_root  # sum = a

        # Verify Vieta: product of roots = -product => pos_root * neg_root = -product
        assert pos_root * neg_root == -product, (
            f"Vieta check failed: {pos_root} * {neg_root} != -{product}"
        )
        # Also verify that neg_root makes an argument nonpositive.
        assert neg_root <= 0 or (neg_root - a) <= 0, (
            "extraneous root does not actually invalidate a log argument"
        )

        if base == 10:
            log_l = r"\log"
        else:
            log_l = rf"\log_{{{base}}}"

        statement_inner = (
            rf"{log_l}(x) + {log_l}(x - {a}) = {c}"
        )

        quad_expr = f"x^2 - {a}x - {product} = 0"

        # Craft the rejection explanation using the actual extraneous value.
        rejection_reason = (
            f"The candidate $x = {neg_root}$ is rejected because substituting "
            f"it back makes $\\log(x)$ undefined (argument $\\leq 0$)."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (base, a, pos_root)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve for $x$: ${statement_inner}$. "
                "State all candidate solutions, identify any extraneous ones, "
                "and give the valid solution."
            ),
            answer_latex=(
                f"$x = {pos_root}$ (candidate $x = {neg_root}$ rejected as extraneous)"
            ),
            hints=[
                (
                    r"Combine the logs with the product rule: "
                    r"$\log_b(M) + \log_b(N) = \log_b(MN)$."
                ),
                (
                    f"After combining and converting to exponential form, you "
                    f"will get ${quad_expr}$."
                ),
                (
                    "Solve the quadratic, then check each candidate: logs are "
                    "undefined at nonpositive arguments, so reject any root that "
                    "makes $x$ or $x - a$ less than or equal to zero."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${statement_inner}$.",
                (
                    rf"Apply the product rule: "
                    rf"${log_l}\bigl(x(x - {a})\bigr) = {c}$."
                ),
                (
                    rf"Convert to exponential form: "
                    rf"$x(x - {a}) = {base}^{{{c}}} = {product}$."
                ),
                f"Expand: ${quad_expr}$.",
                (
                    f"Solve the quadratic. The two candidates are $x = {pos_root}$ "
                    f"and $x = {neg_root}$."
                ),
                (
                    f"Check the candidates in the original equation. $x = {pos_root}$ "
                    f"gives positive arguments $x = {pos_root}$ and "
                    f"$x - {a} = {pos_root - a}$, so it is valid."
                ),
                rejection_reason,
                f"The only valid solution is $x = {pos_root}$.",
            ],
            tags=["#branch-algebra-2", "#topic-logarithms"],
        )


# ===========================================================================
# Topic 4: properties_of_logarithms
# ===========================================================================


@register
class LogProductRuleExpandContract(Generator):
    """Expand log_b(xy) into log_b(x) + log_b(y), or contract the sum.

    Two directions, picked randomly. Backward: pick base and two variables.
    """
    generator_id = "log_product_rule_expand_contract"
    topic_slug = "properties_of_logarithms"
    display_name = "Expand or contract log_b(xy) using the product rule"

    _BASE_CHOICES = {
        "easy": (2, 10, "e"),
        "medium": (2, 3, 5, 10, "e"),
        "hard": (2, 3, 4, 5, 6, 7, 10, "e"),
    }
    _VAR_PAIRS = [
        ("x", "y"),
        ("a", "b"),
        ("m", "n"),
        ("p", "q"),
        ("u", "v"),
        ("s", "t"),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        direction = rng.choice(["expand", "contract"])
        base = rng.choice(self._BASE_CHOICES[difficulty])
        v1, v2 = rng.choice(self._VAR_PAIRS)

        if base == "e":
            def L(arg: str) -> str:
                return rf"\ln({arg})"
            base_display = "$\\ln$"
        elif base == 10:
            def L(arg: str) -> str:
                return rf"\log({arg})"
            base_display = "$\\log$"
        else:
            def L(arg: str) -> str:
                return rf"\log_{{{base}}}({arg})"
            base_display = f"$\\log_{{{base}}}$"

        combined = L(f"{v1}{v2}")
        expanded = f"{L(v1)} + {L(v2)}"

        if direction == "expand":
            statement = f"Expand ${combined}$ using the product rule."
            answer = f"${expanded}$"
            steps = [
                f"Start with ${combined}$.",
                (
                    r"Apply the product rule: $\log_b(MN) = \log_b(M) + \log_b(N)$."
                ),
                f"Rewrite: ${expanded}$.",
            ]
        else:  # contract
            statement = f"Write ${expanded}$ as a single logarithm."
            answer = f"${combined}$"
            steps = [
                f"Start with ${expanded}$.",
                (
                    r"Apply the product rule in reverse: "
                    r"$\log_b(M) + \log_b(N) = \log_b(MN)$."
                ),
                f"Rewrite: ${combined}$.",
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (direction, str(base), v1, v2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Product rule: $\log_b(MN) = \log_b(M) + \log_b(N)$. A product "
                    "inside a log becomes a sum of two logs."
                ),
                f"Both logs must have the same base ({base_display}).",
            ],
            solution_steps_latex=steps,
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


@register
class LogPowerRuleExpandContract(Generator):
    """Expand log_b(x^n) into n * log_b(x), or contract n log_b(x) into
    log_b(x^n). Two directions.
    """
    generator_id = "log_power_rule_expand_contract"
    topic_slug = "properties_of_logarithms"
    display_name = "Expand or contract log_b(x^n) using the power rule"

    _BASE_CHOICES = {
        "easy": (2, 10, "e"),
        "medium": (2, 3, 5, 10, "e"),
        "hard": (2, 3, 4, 5, 6, 7, 10, "e"),
    }
    _N_RANGES = {
        "easy": (2, 5),
        "medium": (2, 8),
        "hard": (2, 12),
    }
    _VAR_CHOICES = ("x", "y", "a", "b", "t", "u", "p", "q")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        direction = rng.choice(["expand", "contract"])
        base = rng.choice(self._BASE_CHOICES[difficulty])
        v = rng.choice(self._VAR_CHOICES)
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        if base == "e":
            def L(arg: str) -> str:
                return rf"\ln({arg})"
            base_display = "natural log"
        elif base == 10:
            def L(arg: str) -> str:
                return rf"\log({arg})"
            base_display = "common log"
        else:
            def L(arg: str) -> str:
                return rf"\log_{{{base}}}({arg})"
            base_display = f"log base {base}"

        power_form = L(f"{v}^{{{n}}}")
        expanded = f"{n} {L(v)}"

        if direction == "expand":
            statement = f"Expand ${power_form}$ using the power rule."
            answer = f"${expanded}$"
            steps = [
                f"Start with ${power_form}$.",
                (
                    r"Apply the power rule: $\log_b(M^n) = n \log_b(M)$."
                ),
                f"Move the exponent ${n}$ in front: ${expanded}$.",
            ]
        else:  # contract
            statement = f"Write ${expanded}$ as a single logarithm."
            answer = f"${power_form}$"
            steps = [
                f"Start with ${expanded}$.",
                (
                    r"Apply the power rule in reverse: "
                    r"$n \log_b(M) = \log_b(M^n)$."
                ),
                f"Move the coefficient ${n}$ to the exponent: ${power_form}$.",
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (direction, str(base), v, n)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Power rule: $\log_b(M^n) = n \log_b(M)$. An exponent inside "
                    "a log becomes a coefficient in front."
                ),
                f"The log is a {base_display}.",
            ],
            solution_steps_latex=steps,
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


@register
class LogChangeOfBase(Generator):
    """Rewrite log_b(x) using the change-of-base formula.

    Two directions are available at random:
    - Rewrite log_b(x) as log(x)/log(b) or ln(x)/ln(b).
    - (Harder) Compute an approximate value using the formula.
    """
    generator_id = "log_change_of_base"
    topic_slug = "properties_of_logarithms"
    display_name = "Change of base: rewrite log_b(x) using log or ln"
    bank_count_per_difficulty = 20

    _BASE_CHOICES = {
        "easy": (3, 5, 7),
        "medium": (3, 4, 5, 6, 7, 8, 9),
        "hard": (3, 4, 5, 6, 7, 8, 9, 11, 12, 13),
    }
    _X_RANGES = {
        "easy": (2, 20),
        "medium": (2, 50),
        "hard": (2, 100),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        target_base = rng.choice(["log", "ln"])
        base = rng.choice(self._BASE_CHOICES[difficulty])
        x_lo, x_hi = self._X_RANGES[difficulty]
        x = rng.randint(x_lo, x_hi)
        # Prefer x != base and x != 1 to avoid trivial answers.
        while x == base or x == 1:
            x = rng.randint(x_lo, x_hi)

        original = rf"\log_{{{base}}}({x})"

        if target_base == "log":
            rewritten = rf"\frac{{\log({x})}}{{\log({base})}}"
            target_name = "common log"
            target_symbol = r"\log"
        else:
            rewritten = rf"\frac{{\ln({x})}}{{\ln({base})}}"
            target_name = "natural log"
            target_symbol = r"\ln"

        # Compute a decimal approximation.
        value = sp.N(sp.log(x, base), 6)
        approx = str(value)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (target_base, base, x)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Rewrite ${original}$ using the change-of-base formula "
                f"with {target_name}. Then give a decimal approximation rounded "
                "to four places."
            ),
            answer_latex=(
                f"${original} = {rewritten} \\approx {round(float(value), 4)}$"
            ),
            hints=[
                (
                    r"Change-of-base formula: "
                    r"$\log_b(x) = \frac{\log_k(x)}{\log_k(b)}$ "
                    "for any valid base $k$."
                ),
                (
                    f"Pick $k$ to be the {target_name} (${target_symbol}$), since "
                    "those are on most calculators."
                ),
                f"Numerator: ${target_symbol}({x})$. Denominator: ${target_symbol}({base})$.",
            ],
            solution_steps_latex=[
                f"Start with ${original}$.",
                (
                    r"Apply the change-of-base formula: "
                    rf"$\log_{{{base}}}({x}) = \frac{{{target_symbol}({x})}}"
                    rf"{{{target_symbol}({base})}}$."
                ),
                f"Compute on a calculator: the value is approximately {round(float(value), 4)}.",
                f"So ${original} = {rewritten} \\approx {round(float(value), 4)}$.",
            ],
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


# ===========================================================================
# Topic 5: applications_of_exponentials_and_logarithms
# ===========================================================================


@register
class ContinuousCompoundInterest(Generator):
    """Compute A = P * e^(rt) for clean P, r, t.

    Backward: pick P, r, t so that r*t is a small rational (e.g. 1, 2, 0.5)
    and P is a round number. Give an exact answer using e and a decimal
    approximation.
    """
    generator_id = "continuous_compound_interest"
    topic_slug = "applications_of_exponentials_and_logarithms"
    display_name = "Continuous compound interest: A = P e^(rt)"
    bank_count_per_difficulty = 25

    _P_CHOICES = {
        "easy": (500, 1000, 2000, 5000),
        "medium": (500, 1000, 1500, 2000, 2500, 3000, 5000, 10000),
        "hard": (250, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 7500, 10000),
    }
    # (r as percent, t in years) pairs where rt is clean.
    # r written as decimal: e.g. (5, 10) means r=0.05, t=10, rt=0.5
    _RT_CHOICES = {
        "easy": [
            (5, 10),   # rt = 0.5
            (10, 10),  # rt = 1
            (4, 25),   # rt = 1
            (2, 50),   # rt = 1
            (5, 20),   # rt = 1
            (10, 20),  # rt = 2
        ],
        "medium": [
            (5, 10),
            (10, 10),
            (5, 20),
            (4, 25),
            (2, 50),
            (5, 30),   # rt = 1.5
            (10, 20),
            (4, 50),   # rt = 2
            (3, 100),  # rt = 3
            (8, 25),   # rt = 2
            (4, 10),   # rt = 0.4
            (5, 6),    # rt = 0.3
        ],
        "hard": [
            (5, 10),
            (10, 10),
            (5, 20),
            (4, 25),
            (2, 50),
            (5, 30),
            (10, 20),
            (4, 50),
            (3, 100),
            (8, 25),
            (6, 50),   # rt = 3
            (2, 100),  # rt = 2
            (7, 100),  # rt = 7 -- huge, skip
            (1, 100),  # rt = 1
        ],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        P = rng.choice(self._P_CHOICES[difficulty])
        r_pct, t = rng.choice(self._RT_CHOICES[difficulty])
        r = sp.Rational(r_pct, 100)
        rt = r * t

        # Exact: A = P * e^(rt)
        amount_exact = sp.Mul(P, sp.exp(rt), evaluate=False)
        amount_value = P * sp.exp(rt)
        amount_decimal = round(float(sp.N(amount_value)), 2)

        rt_latex = sp.latex(rt)
        # Render exact answer like "1000 e^{1/2}" or "1000 e^{1}"
        if rt == 1:
            exp_latex = "e"
        elif rt == 0:
            exp_latex = "1"
        else:
            exp_latex = rf"e^{{{rt_latex}}}"
        exact_latex = f"{P} {exp_latex}" if rt != 0 else str(P)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (P, r_pct, t)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A principal of \\${P} is invested at an annual interest rate "
                f"of {r_pct}\\% compounded continuously. Use "
                r"$A = P e^{rt}$ "
                f"to find the amount after ${t}$ years. Give both an exact "
                "expression and a decimal approximation rounded to the nearest "
                "cent."
            ),
            answer_latex=(
                f"$A = {exact_latex} \\approx \\${amount_decimal:,.2f}$"
            ),
            hints=[
                (
                    r"Continuous compounding uses $A = P e^{rt}$ where $P$ is "
                    "principal, $r$ is the decimal interest rate, and $t$ is "
                    "time in years."
                ),
                (
                    f"Convert the rate: $r = {r_pct}\\% = {sp.latex(r)}$. Then "
                    f"$rt = {rt_latex}$."
                ),
                f"Plug into the formula: $A = {P} \\cdot e^{{{rt_latex}}}$.",
            ],
            solution_steps_latex=[
                r"Use the formula $A = P e^{rt}$.",
                (
                    f"Identify $P = {P}$, $r = {r_pct}\\% = {sp.latex(r)}$, and "
                    f"$t = {t}$."
                ),
                f"Compute the exponent: $rt = ({sp.latex(r)})({t}) = {rt_latex}$.",
                f"Substitute: $A = {P} e^{{{rt_latex}}}$.",
                f"Approximate: $A \\approx \\${amount_decimal:,.2f}$.",
            ],
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


@register
class ExponentialModelSolveForTime(Generator):
    """Given A(t) = A_0 * e^(rt) and a target A, solve for t using logs.

    Backward: pick A_0, r, and a clean integer (or simple fraction) t.
    Then A = A_0 * e^(rt). The student's job is to solve for t.
    """
    generator_id = "exponential_model_solve_for_time"
    topic_slug = "applications_of_exponentials_and_logarithms"
    display_name = "Solve A_0 e^(rt) = A for t"

    _A0_CHOICES = {
        "easy": (100, 200, 500, 1000),
        "medium": (50, 100, 150, 200, 300, 500, 1000, 2000),
        "hard": (25, 50, 100, 200, 300, 500, 800, 1000, 1500, 2000, 5000),
    }
    _R_PCT_CHOICES = {
        "easy": (5, 10, 20),
        "medium": (2, 3, 4, 5, 8, 10, 15, 20),
        "hard": (2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25),
    }
    # Pick t so that rt is clean (small integer after multiplying).
    _T_CHOICES = {
        "easy": (5, 10, 20),
        "medium": (5, 10, 15, 20, 25, 30),
        "hard": (5, 10, 15, 20, 25, 30, 40, 50),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        A0 = rng.choice(self._A0_CHOICES[difficulty])
        r_pct = rng.choice(self._R_PCT_CHOICES[difficulty])
        t = rng.choice(self._T_CHOICES[difficulty])
        r = sp.Rational(r_pct, 100)
        rt = r * t

        # A = A0 * e^(rt). Present A symbolically as a multiple of A0.
        # For display, A = A0 * (decimal e^rt). We give exact A = A0 * e^rt.
        # But: the student solves log(A/A_0) = rt -> t = ln(A/A_0)/r.
        # So instead, we present A = A0 * e^rt numerically for a nicer
        # question. Better strategy: tell the student directly that A = A0 e^rt
        # with specific A. Pick A as A0 * e^rt (symbolic) so their work is
        # t = ln(A/A0)/r = rt/r = t (confirms). Present A in exact form with e.
        A_latex = f"{A0} e^{{{sp.latex(rt)}}}"
        # Answer: t as sympy rational or integer
        t_latex = sp.latex(sp.Rational(t))
        rt_latex = sp.latex(rt)
        ratio_latex = rf"e^{{{rt_latex}}}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (A0, r_pct, t)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A population grows according to "
                f"$A(t) = {A0} e^{{{sp.latex(r)} t}}$, where $t$ is measured in "
                f"years. Find the time $t$ at which the population reaches "
                f"$A = {A_latex}$. Give $t$ exactly."
            ),
            answer_latex=f"$t = {t_latex}$ years",
            hints=[
                (
                    r"To solve $A_0 e^{rt} = A$ for $t$, divide both sides by "
                    r"$A_0$ and take $\ln$."
                ),
                (
                    r"Step 1: $e^{rt} = A/A_0$. "
                    r"Step 2: $rt = \ln(A/A_0)$. "
                    r"Step 3: $t = \ln(A/A_0)/r$."
                ),
                (
                    f"Here $A/A_0 = {ratio_latex}$, and $\\ln\\!\\left({ratio_latex}"
                    f"\\right) = {rt_latex}$."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${A0} e^{{{sp.latex(r)} t}} = {A_latex}$.",
                (
                    rf"Divide both sides by ${A0}$: "
                    rf"$e^{{{sp.latex(r)} t}} = {ratio_latex}$."
                ),
                (
                    rf"Take $\ln$ of both sides: "
                    rf"${sp.latex(r)} t = \ln\!\left({ratio_latex}\right) = {rt_latex}$."
                ),
                (
                    rf"Divide by ${sp.latex(r)}$: "
                    rf"$t = \frac{{{rt_latex}}}{{{sp.latex(r)}}} = {t_latex}$."
                ),
                f"The time is $t = {t_latex}$ years.",
            ],
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


@register
class RichterOrPhOrDecibelScale(Generator):
    """A log-scale word problem. Randomly picks one of three scenarios:

    1. Richter scale magnitude difference.
    2. pH from hydrogen ion concentration.
    3. Decibel level from intensity.

    Each scenario has a small curated parameter table so answers stay clean.
    """
    generator_id = "richter_or_ph_or_decibel_scale"
    topic_slug = "applications_of_exponentials_and_logarithms"
    display_name = "Log-scale word problems (Richter, pH, decibel)"
    bank_count_per_difficulty = 18

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scenario = rng.choice(["richter", "ph", "decibel"])

        if scenario == "richter":
            # How many times stronger is a magnitude M1 quake than M2? 10^(M1-M2)
            if difficulty == "easy":
                M1, M2 = rng.choice([(7, 5), (6, 4), (5, 3), (8, 6), (7, 4)])
            elif difficulty == "medium":
                M1, M2 = rng.choice([
                    (7, 5), (6, 4), (8, 4), (9, 5), (7, 3), (8, 5),
                    (9, 6), (6, 2),
                ])
            else:  # hard
                M1, M2 = rng.choice([
                    (9, 4), (9, 3), (8, 2), (9, 2), (7, 1), (8, 1),
                    (9, 1), (7, 2),
                ])
            diff = M1 - M2
            ratio = 10 ** diff

            return Problem(
                id=make_problem_id(
                    self.generator_id, difficulty, ("richter", M1, M2)
                ),
                generator_id=self.generator_id,
                topic_slug=self.topic_slug,
                difficulty=difficulty,
                statement_latex=(
                    f"The Richter scale magnitude $M$ of an earthquake is defined "
                    r"so that an increase of 1 in $M$ corresponds to a 10-fold "
                    r"increase in ground-wave amplitude. An earthquake of "
                    f"magnitude ${M1}$ strikes one region, while another strikes "
                    f"with magnitude ${M2}$. How many times greater is the "
                    f"amplitude of the first earthquake compared to the second?"
                ),
                answer_latex=f"${ratio:,}$ times greater",
                hints=[
                    (
                        "On the Richter scale, each whole-number increase in "
                        "magnitude multiplies the amplitude by 10."
                    ),
                    (
                        f"The difference in magnitudes is ${M1} - {M2} = {diff}$, "
                        f"so the amplitude ratio is $10^{{{diff}}}$."
                    ),
                ],
                solution_steps_latex=[
                    (
                        r"Let $A_1$ and $A_2$ be the amplitudes. The Richter "
                        r"definition gives $M = \log_{10}(A)$, so "
                        r"$A = 10^M$."
                    ),
                    (
                        rf"Compute the ratio: "
                        rf"$\frac{{A_1}}{{A_2}} = \frac{{10^{{{M1}}}}}"
                        rf"{{10^{{{M2}}}}} = 10^{{{M1} - {M2}}} = 10^{{{diff}}}$."
                    ),
                    f"So the first earthquake's amplitude is ${ratio:,}$ times "
                    f"greater than the second.",
                ],
                tags=["#branch-pre-calculus", "#topic-logarithms"],
            )

        elif scenario == "ph":
            # pH = -log10([H+]). Pick [H+] = 10^(-n) for integer n.
            n_choices = {
                "easy": (3, 4, 5, 6),
                "medium": (1, 2, 3, 4, 5, 6, 7, 8, 9),
                "hard": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
            }
            n = rng.choice(n_choices[difficulty])
            pH = n  # -log10(10^-n) = n

            return Problem(
                id=make_problem_id(
                    self.generator_id, difficulty, ("ph", n)
                ),
                generator_id=self.generator_id,
                topic_slug=self.topic_slug,
                difficulty=difficulty,
                statement_latex=(
                    r"The pH of a solution is defined by $\mathrm{pH} = "
                    r"-\log_{10}[\mathrm{H}^+]$, where $[\mathrm{H}^+]$ is the "
                    r"hydrogen-ion concentration in moles per liter. A solution "
                    rf"has $[\mathrm{{H}}^+] = 10^{{-{n}}}$ mol/L. Find its pH."
                ),
                answer_latex=f"$\\mathrm{{pH}} = {pH}$",
                hints=[
                    (
                        r"Use $\mathrm{pH} = -\log_{10}[\mathrm{H}^+]$. Substitute "
                        r"the given concentration."
                    ),
                    (
                        rf"Since $\log_{{10}}(10^{{-{n}}}) = -{n}$, the negative "
                        rf"of that is $+{n}$."
                    ),
                ],
                solution_steps_latex=[
                    (
                        rf"Start with the definition "
                        rf"$\mathrm{{pH}} = -\log_{{10}}[\mathrm{{H}}^+]$."
                    ),
                    (
                        rf"Substitute $[\mathrm{{H}}^+] = 10^{{-{n}}}$: "
                        rf"$\mathrm{{pH}} = -\log_{{10}}(10^{{-{n}}})$."
                    ),
                    (
                        rf"Simplify the log: $\log_{{10}}(10^{{-{n}}}) = -{n}$, so "
                        rf"$\mathrm{{pH}} = -(-{n}) = {n}$."
                    ),
                    f"The pH is ${pH}$.",
                ],
                tags=["#branch-pre-calculus", "#topic-logarithms"],
            )

        else:  # decibel
            # Decibel level L = 10 log10(I/I_0) where I_0 = 10^-12 W/m^2.
            # Pick I = 10^k * I_0 so L = 10k dB.
            k_choices = {
                "easy": (5, 6, 7, 8, 9, 10),
                "medium": (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                "hard": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
            }
            k = rng.choice(k_choices[difficulty])
            # I in W/m^2 = 10^(k - 12)
            I_exp = k - 12
            L = 10 * k  # decibels

            return Problem(
                id=make_problem_id(
                    self.generator_id, difficulty, ("decibel", k)
                ),
                generator_id=self.generator_id,
                topic_slug=self.topic_slug,
                difficulty=difficulty,
                statement_latex=(
                    r"The loudness of a sound in decibels is given by "
                    r"$L = 10 \log_{10}(I / I_0)$, where $I$ is the sound's "
                    r"intensity and $I_0 = 10^{-12}$ W/m$^2$ is the threshold of "
                    r"hearing. Find $L$ for a sound with intensity "
                    rf"$I = 10^{{{I_exp}}}$ W/m$^2$."
                ),
                answer_latex=f"$L = {L}$ dB",
                hints=[
                    (
                        r"Compute the ratio $I/I_0$ first. Dividing $10^{I_exp}$ "
                        r"by $10^{-12}$ subtracts exponents."
                    ),
                    (
                        rf"$I/I_0 = 10^{{{I_exp}}}/10^{{-12}} = 10^{{{k}}}$, so "
                        rf"$\log_{{10}}(I/I_0) = {k}$ and $L = 10 \cdot {k}$."
                    ),
                ],
                solution_steps_latex=[
                    r"Start with $L = 10 \log_{10}(I / I_0)$.",
                    (
                        rf"Compute the ratio: $I/I_0 = "
                        rf"\frac{{10^{{{I_exp}}}}}{{10^{{-12}}}} = 10^{{{k}}}$."
                    ),
                    (
                        rf"Take the log: $\log_{{10}}(10^{{{k}}}) = {k}$."
                    ),
                    f"Multiply by 10: $L = 10 \\cdot {k} = {L}$ dB.",
                ],
                tags=["#branch-pre-calculus", "#topic-logarithms"],
            )
