"""Exponential and logarithm generators (Cluster: exponentials).

Five topic slugs covered:

- exponential_functions (Exponential_Functions.md)
- exponential_equations (Exponential_Equations.md)
- growth_decay_and_applications (Growth_Decay_And_Applications.md)
- introduction_to_exponentials_and_logarithms (Introduction_To_Exponentials_And_Logarithms.md)
- simple_and_compound_interest (Simple_And_Compound_Interest.md)

Each topic has three generators for a total of 15. Backward construction is
used throughout: parameters are chosen so the answer comes out clean
(integer or clean-decimal amounts, integer or nice-fraction exponents, clean
logarithm values), then the statement is rendered.
"""
from __future__ import annotations

import math
import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _format_signed_paren(n: int) -> str:
    """Wrap a negative integer in parentheses so it reads well after an op."""
    return f"({n})" if n < 0 else str(n)


def _format_exp_function(a: int, b: int, name: str = "f") -> str:
    """Render f(x) = a * b^x in LaTeX, hiding a=1 and handling sign cleanly."""
    if a == 1:
        body = f"{b}^{{x}}"
    elif a == -1:
        body = f"-{b}^{{x}}"
    else:
        body = f"{a} \\cdot {b}^{{x}}"
    return f"{name}(x) = {body}"


def _fraction_to_decimal(num: int, den: int, places: int = 4) -> str:
    """Render num/den as a decimal string to `places` places."""
    value = num / den
    return f"{value:.{places}f}"


def _pow_at(a: int, b: int, x: int) -> Fraction:
    """Return a * b^x as an exact Fraction (handles negative x)."""
    if x >= 0:
        return Fraction(a * (b ** x), 1)
    return Fraction(a, b ** (-x))


def _format_power_value(a: int, b: int, x: int) -> str:
    """Render a * b^x as a LaTeX-friendly number or fraction."""
    value = _pow_at(a, b, x)
    if value.denominator == 1:
        return str(value.numerator)
    return rf"\dfrac{{{value.numerator}}}{{{value.denominator}}}"


# ===========================================================================
# Topic 1: exponential_functions
# ===========================================================================


@register
class ExpFunctionEvaluate(Generator):
    """Given f(x) = a * b^x, evaluate at a small integer input.

    Backward construction: pick clean a (integer) and b in {2, 3, 5, 10},
    and a small integer x in the allowed range. Output is exact.
    """
    generator_id = "exp_function_evaluate"
    topic_slug = "exponential_functions"
    display_name = "Evaluate f(x) = a * b^x at a given input"

    _B_CHOICES = (2, 3, 5, 10)
    _A_RANGES = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _X_RANGES = {"easy": (0, 3), "medium": (-1, 4), "hard": (-2, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        x_lo, x_hi = self._X_RANGES[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.choice(self._B_CHOICES)
        x_val = rng.randint(x_lo, x_hi)

        # Skip parameter combos that produce awkward huge numbers at hard.
        if b == 10 and x_val >= 4:
            x_val = 3

        func_latex = _format_exp_function(a, b)
        b_pow = _pow_at(1, b, x_val)  # b^x as a Fraction
        full = _pow_at(a, b, x_val)   # a*b^x as a Fraction

        if b_pow.denominator == 1:
            b_pow_str = str(b_pow.numerator)
        else:
            b_pow_str = rf"\dfrac{{{b_pow.numerator}}}{{{b_pow.denominator}}}"

        if full.denominator == 1:
            answer_value = str(full.numerator)
        else:
            answer_value = rf"\dfrac{{{full.numerator}}}{{{full.denominator}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, x_val)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given ${func_latex}$, find $f({x_val})$."
            ),
            answer_latex=f"$f({x_val}) = {answer_value}$",
            hints=[
                f"Substitute $x = {x_val}$ into the rule for $f$.",
                f"Compute the power ${b}^{{{x_val}}}$ first, then multiply by {a}.",
                (
                    f"Remember: ${b}^{{-n}} = \\dfrac{{1}}{{{b}^{{n}}}}$ "
                    "for negative exponents."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${func_latex}$.",
                (
                    f"Substitute $x = {x_val}$: "
                    f"$f({x_val}) = {a} \\cdot {b}^{{{x_val}}}$."
                ),
                f"Evaluate the power: ${b}^{{{x_val}}} = {b_pow_str}$.",
                f"Multiply by ${a}$: $f({x_val}) = {answer_value}$.",
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-functions"],
        )


@register
class ExpFunctionClassifyGrowthDecay(Generator):
    """Given f(x) = a * b^x, classify as growth or decay and state initial value.

    Backward construction: pick integer a and a base b that is either a
    clean integer > 1 (growth) or a simple fraction in (0, 1) (decay).
    """
    generator_id = "exp_function_classify_growth_decay"
    topic_slug = "exponential_functions"
    display_name = "Classify f(x) = a * b^x as growth or decay and find initial value"

    _A_RANGES = {"easy": (1, 8), "medium": (1, 15), "hard": (1, 25)}
    _GROWTH_B_CHOICES = (2, 3, 4, 5, 6, 10)
    # Decay bases rendered as unreduced fractions (num, den) with num < den.
    _DECAY_B_CHOICES = ((1, 2), (1, 3), (1, 4), (1, 5), (1, 10), (2, 3), (3, 4))

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        a = rng.randint(a_lo, a_hi)
        is_growth = rng.choice([True, False])

        if is_growth:
            b = rng.choice(self._GROWTH_B_CHOICES)
            b_latex = str(b)
            b_display = str(b)
            classification = "growth"
            b_value_desc = f"${b} > 1$"
        else:
            num, den = rng.choice(self._DECAY_B_CHOICES)
            b_latex = rf"\dfrac{{{num}}}{{{den}}}"
            b_display = f"{num}/{den}"
            classification = "decay"
            b_value_desc = f"$0 < \\dfrac{{{num}}}{{{den}}} < 1$"

        if a == 1:
            func_latex = f"f(x) = {b_latex}^{{x}}"
        else:
            func_latex = f"f(x) = {a} \\cdot {b_latex}^{{x}}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, is_growth, b_display)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Classify ${func_latex}$ as exponential growth or exponential "
                f"decay, and state its initial value $f(0)$."
            ),
            answer_latex=(
                f"Exponential {classification}; initial value $f(0) = {a}$."
            ),
            hints=[
                (
                    "For $f(x) = a \\cdot b^x$: if $b > 1$ it is growth; "
                    "if $0 < b < 1$ it is decay."
                ),
                (
                    "The initial value is $f(0) = a \\cdot b^0 = a$, because "
                    "$b^0 = 1$ for any nonzero base."
                ),
            ],
            solution_steps_latex=[
                f"Compare the base ${b_latex}$ to $1$.",
                (
                    f"Because {b_value_desc}, the function is exponential "
                    f"{classification}."
                ),
                (
                    f"The initial value is $f(0) = {a} \\cdot {b_latex}^{{0}} "
                    f"= {a} \\cdot 1 = {a}$."
                ),
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-functions"],
        )


@register
class ExpFunctionFromInitialAndFactor(Generator):
    """Given initial value N and growth/decay factor, write f(x) = N * b^x.

    Mixes growth (integer base) and decay (fraction base) problems.
    """
    generator_id = "exp_function_from_initial_and_factor"
    topic_slug = "exponential_functions"
    display_name = "Write f(x) = N * b^x from initial value and factor"

    _N_RANGES = {"easy": (2, 20), "medium": (5, 80), "hard": (10, 250)}
    _GROWTH_B_CHOICES = (2, 3, 4, 5, 10)
    _DECAY_B_CHOICES = ((1, 2), (1, 3), (1, 4), (1, 5), (1, 10))

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)
        is_growth = rng.choice([True, False])

        if is_growth:
            b = rng.choice(self._GROWTH_B_CHOICES)
            factor_word = "growth factor"
            factor_text = str(b)
            b_latex = str(b)
            answer = f"f(x) = {n} \\cdot {b_latex}^{{x}}"
            kind = "growth"
        else:
            num, den = rng.choice(self._DECAY_B_CHOICES)
            factor_word = "decay factor"
            factor_text = f"{num}/{den}"
            b_latex = rf"\dfrac{{{num}}}{{{den}}}"
            answer = f"f(x) = {n} \\cdot \\left({b_latex}\\right)^{{x}}"
            kind = "decay"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (n, is_growth, factor_text)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A quantity has initial value $N = {n}$ and {factor_word} "
                f"$b = {factor_text}$. Write the exponential function $f(x)$ "
                "that models this quantity."
            ),
            answer_latex=f"${answer}$",
            hints=[
                "The general form is $f(x) = N \\cdot b^x$ where $N$ is the initial value and $b$ is the factor.",
                f"Substitute $N = {n}$ and $b = {factor_text}$ into the template.",
            ],
            solution_steps_latex=[
                "Start with the template $f(x) = N \\cdot b^x$.",
                f"Substitute the initial value $N = {n}$.",
                f"Substitute the {kind} factor $b = {factor_text}$.",
                f"The function is ${answer}$.",
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-functions"],
        )


# ===========================================================================
# Topic 2: exponential_equations
# ===========================================================================


@register
class ExpEqCommonBaseSimple(Generator):
    """Solve b^x = b^n with an integer solution by visual comparison.

    Backward: pick base b in {2, 3, 5, 10}, pick integer x (the solution),
    compute rhs = b^x and present as 'b^x = rhs'.
    """
    generator_id = "exp_eq_common_base_simple"
    topic_slug = "exponential_equations"
    display_name = "Solve b^x = N where both sides share the same base"

    _B_CHOICES = (2, 3, 5, 10)
    _X_RANGES = {"easy": (1, 4), "medium": (1, 5), "hard": (2, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        b = rng.choice(self._B_CHOICES)
        x_lo, x_hi = self._X_RANGES[difficulty]
        x_val = rng.randint(x_lo, x_hi)
        # Avoid astronomical values at hard.
        if b == 10 and x_val > 4:
            x_val = 4
        rhs = b ** x_val

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, x_val)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve for $x$: ${b}^{{x}} = {rhs}$."
            ),
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"Try to write ${rhs}$ as a power of ${b}$.",
                (
                    "If two powers with the same base are equal, then their "
                    "exponents are equal."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Write the right-hand side as a power of ${b}$: "
                    f"${rhs} = {b}^{{{x_val}}}$."
                ),
                (
                    f"So the equation becomes ${b}^{{x}} = {b}^{{{x_val}}}$."
                ),
                "Because the bases match, the exponents must match.",
                f"Therefore $x = {x_val}$.",
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals"],
        )


@register
class ExpEqCommonBaseRewrite(Generator):
    """Solve b1^x = b2^k by rewriting both sides with a common base.

    Backward: pick a prime base p (2 or 3), pick integer exponents e1 and e2
    giving the two sides b1 = p^e1, b2 = p^e2 (not equal to p), and pick
    integer k so the answer is k * e2 / e1 (target: clean integer or clean
    fraction with small denominator). Equation: b1^x = b2^k.
    """
    generator_id = "exp_eq_common_base_rewrite"
    topic_slug = "exponential_equations"
    display_name = "Solve a^x = b^k after rewriting with a common base"

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # (prime, e1, e2) gives b1 = prime^e1, b2 = prime^e2.
        if difficulty == "easy":
            triples = [
                (2, 2, 1),  # 4^x = 2^k
                (2, 1, 2),  # 2^x = 4^k
                (3, 2, 1),  # 9^x = 3^k
                (3, 1, 2),  # 3^x = 9^k
                (2, 3, 1),  # 8^x = 2^k
                (2, 1, 3),  # 2^x = 8^k
            ]
        elif difficulty == "medium":
            triples = [
                (2, 2, 3),   # 4^x = 8^k
                (2, 3, 2),   # 8^x = 4^k
                (2, 2, 5),   # 4^x = 32^k
                (2, 4, 3),   # 16^x = 8^k
                (3, 2, 3),   # 9^x = 27^k
                (3, 3, 2),   # 27^x = 9^k
                (2, 1, 5),   # 2^x = 32^k
            ]
        else:  # hard
            triples = [
                (2, 3, 5),   # 8^x = 32^k
                (2, 5, 3),   # 32^x = 8^k
                (2, 4, 5),   # 16^x = 32^k
                (2, 5, 2),   # 32^x = 4^k
                (3, 4, 3),   # 81^x = 27^k
                (3, 2, 5),   # 9^x = 243^k
                (2, 4, 6),   # 16^x = 64^k
            ]

        prime, e1, e2 = rng.choice(triples)
        # Choose k so the solution k*e2/e1 is clean.
        # Start with small k then scale until clean fraction.
        k_choices = [k for k in range(1, 8) if (k * e2) % math.gcd(k * e2, e1) >= 0]
        k = rng.choice(k_choices[:6]) if k_choices else 1

        b1 = prime ** e1
        b2 = prime ** e2
        # Solve e1 * x = e2 * k  →  x = e2 * k / e1
        num = e2 * k
        den = e1
        g = math.gcd(num, den)
        num //= g
        den //= g

        if den == 1:
            answer_latex = f"$x = {num}$"
            x_display = str(num)
        else:
            answer_latex = rf"$x = \dfrac{{{num}}}{{{den}}}$"
            x_display = rf"\dfrac{{{num}}}{{{den}}}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (prime, e1, e2, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve for $x$: ${b1}^{{x}} = {b2}^{{{k}}}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    f"Notice that both ${b1}$ and ${b2}$ are powers of ${prime}$."
                ),
                (
                    f"Rewrite both sides with base ${prime}$, then equate exponents."
                ),
                (
                    f"You will get $({e1})x = ({e2})({k})$, which solves cleanly."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Write each side as a power of ${prime}$: "
                    f"${b1} = {prime}^{{{e1}}}$ and ${b2} = {prime}^{{{e2}}}$."
                ),
                (
                    f"Substitute: $\\left({prime}^{{{e1}}}\\right)^{{x}} = "
                    f"\\left({prime}^{{{e2}}}\\right)^{{{k}}}$."
                ),
                (
                    f"Apply the power rule $(a^m)^n = a^{{mn}}$: "
                    f"${prime}^{{{e1}x}} = {prime}^{{{e2 * k}}}$."
                ),
                (
                    f"Equate exponents: ${e1}x = {e2 * k}$."
                ),
                f"Solve: $x = {x_display}$.",
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals"],
        )


@register
class ExpEqLogarithmMethod(Generator):
    """Solve b^x = N where the answer is log(N)/log(b).

    Backward: pick an integer base b in {2, 3, 5, 7} and an integer N that is
    not a power of b. The exact answer is log(N)/log(b); a decimal hint is
    included.
    """
    generator_id = "exp_eq_logarithm_method"
    topic_slug = "exponential_equations"
    display_name = "Solve b^x = N using logarithms"

    _B_CHOICES = (2, 3, 5, 7)
    _N_RANGES = {"easy": (5, 30), "medium": (10, 80), "hard": (15, 200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        b = rng.choice(self._B_CHOICES)
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        # Make sure N is NOT a power of b (otherwise use common-base method).
        def is_power(val: int, base: int) -> bool:
            if val < 1 or base < 2:
                return False
            k = 1
            while k < val:
                k *= base
            return k == val

        attempts = 0
        while is_power(n, b) and attempts < 10:
            n = rng.randint(n_lo, n_hi)
            attempts += 1
        if is_power(n, b):
            n += 1  # force non-power

        answer_latex = rf"$x = \dfrac{{\log {n}}}{{\log {b}}}$"
        decimal = math.log(n) / math.log(b)
        decimal_str = f"{decimal:.4f}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve for $x$: ${b}^{{x}} = {n}$. Give an exact answer "
                "using logarithms."
            ),
            answer_latex=answer_latex,
            hints=[
                f"Because ${n}$ is not a clean power of ${b}$, use logarithms.",
                (
                    "Take the logarithm of both sides, then use "
                    "$\\log(a^x) = x \\log a$ to bring $x$ down."
                ),
                (
                    f"Numerically, $\\dfrac{{\\log {n}}}{{\\log {b}}} "
                    f"\\approx {decimal_str}$."
                ),
            ],
            solution_steps_latex=[
                f"Start with ${b}^{{x}} = {n}$.",
                f"Take $\\log$ of both sides: $\\log({b}^{{x}}) = \\log({n})$.",
                (
                    "Apply the power rule for logs: "
                    f"$x \\log({b}) = \\log({n})$."
                ),
                (
                    f"Divide both sides by $\\log({b})$: "
                    f"$x = \\dfrac{{\\log {n}}}{{\\log {b}}}$."
                ),
                f"As a decimal, $x \\approx {decimal_str}$.",
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-logarithms"],
        )


# ===========================================================================
# Topic 3: growth_decay_and_applications
# ===========================================================================


@register
class CompoundInterestDiscrete(Generator):
    """Compound interest: A = P(1 + r/n)^(nt) with clean parameters.

    Backward construction: pick clean P, r, n, t so that the final amount
    rounds to a whole dollar or 2 decimal places with a simple value.
    """
    generator_id = "compound_interest_discrete"
    topic_slug = "growth_decay_and_applications"
    display_name = "Compound interest A = P(1 + r/n)^(nt)"

    # Tuple: (principal, rate (as pct), n (compounding/year), t years)
    _CASES_EASY = [
        (1000, 10, 1, 2),   # 10% annual, 2 years
        (500, 8, 1, 3),
        (2000, 5, 1, 4),
        (1000, 4, 2, 2),    # 4% semi-annual, 2 years
        (800, 10, 1, 3),
        (1500, 6, 1, 2),
        (2500, 8, 1, 2),
        (1200, 5, 2, 2),
        (400, 10, 1, 4),
        (1000, 2, 2, 3),
    ]
    _CASES_MEDIUM = [
        (5000, 6, 2, 3),
        (2000, 8, 4, 2),    # quarterly
        (10000, 4, 4, 2),
        (3000, 5, 2, 4),
        (4000, 10, 2, 3),
        (1500, 12, 2, 4),
        (6000, 8, 2, 5),
        (2500, 6, 4, 3),
        (8000, 4, 2, 4),
        (3500, 10, 1, 5),
    ]
    _CASES_HARD = [
        (10000, 5, 4, 5),
        (15000, 6, 2, 6),
        (20000, 8, 4, 4),
        (8000, 10, 2, 7),
        (12000, 4, 4, 6),
        (5000, 12, 4, 3),
        (25000, 6, 2, 8),
        (7500, 8, 2, 6),
        (18000, 5, 2, 5),
        (6000, 10, 4, 4),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cases = {
            "easy": self._CASES_EASY,
            "medium": self._CASES_MEDIUM,
            "hard": self._CASES_HARD,
        }[difficulty]
        p, r_pct, n, t = rng.choice(cases)

        r = r_pct / 100
        amount = p * (1 + r / n) ** (n * t)
        amount_rounded = round(amount, 2)
        # Format without trailing zeros for whole dollars.
        if amount_rounded == int(amount_rounded):
            amount_str = f"{int(amount_rounded)}"
        else:
            amount_str = f"{amount_rounded:.2f}"

        r_display = f"{r_pct}\\%"
        r_frac = f"{r_pct}/100"
        nt = n * t

        if n == 1:
            compounding_word = "annually"
        elif n == 2:
            compounding_word = "semi-annually"
        elif n == 4:
            compounding_word = "quarterly"
        elif n == 12:
            compounding_word = "monthly"
        else:
            compounding_word = f"{n} times per year"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (p, r_pct, n, t)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A principal of $P = \\${p}$ is invested at an annual "
                f"interest rate of ${r_display}$ compounded {compounding_word} "
                f"for $t = {t}$ years. Using "
                "$A = P\\left(1 + \\dfrac{r}{n}\\right)^{nt}$, compute the "
                "final amount $A$. Round to the nearest cent."
            ),
            answer_latex=f"$A = \\${amount_str}$",
            hints=[
                (
                    f"Identify $P = {p}$, $r = {r_frac} = {r}$, $n = {n}$, "
                    f"$t = {t}$."
                ),
                (
                    f"The exponent is $nt = {n} \\cdot {t} = {nt}$."
                ),
                (
                    f"Compute $\\left(1 + \\dfrac{{{r_pct}}}{{100 \\cdot {n}}}"
                    f"\\right)^{{{nt}}}$, then multiply by ${p}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Substitute into $A = P\\left(1 + \\dfrac{{r}}{{n}}"
                    f"\\right)^{{nt}}$: "
                    f"$A = {p}\\left(1 + \\dfrac{{{r}}}{{{n}}}\\right)^{{{nt}}}$."
                ),
                (
                    f"Simplify inside the parentheses: "
                    f"$1 + \\dfrac{{{r}}}{{{n}}} = {1 + r / n:.5f}$."
                ),
                (
                    f"Raise to the ${nt}$th power: "
                    f"$({1 + r / n:.5f})^{{{nt}}} = {(1 + r / n) ** nt:.5f}$."
                ),
                (
                    f"Multiply by ${p}$: "
                    f"$A = {p} \\cdot {(1 + r / n) ** nt:.5f} \\approx \\${amount_str}$."
                ),
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals"],
        )


@register
class ExpGrowthPopulation(Generator):
    """Population growth: P(t) = P_0 * (1 + r)^t with clean integer output.

    Backward: pick small integer factor b = 1 + r (so r is a nice rate), a
    small integer t, and choose P_0 so that P_0 * b^t is a clean integer.
    """
    generator_id = "exp_growth_population"
    topic_slug = "growth_decay_and_applications"
    display_name = "Population growth P(t) = P_0 * (1 + r)^t"

    # (rate pct, equivalent 1+r as fraction num/den) — clean factor selections.
    _RATE_CHOICES = [
        (100, (2, 1)),   # 100% growth = factor 2
        (50, (3, 2)),    # 50% = 3/2
        (25, (5, 4)),    # 25% = 5/4
        (20, (6, 5)),    # 20% = 6/5
        (10, (11, 10)),  # 10% = 11/10
        (200, (3, 1)),   # 200% = factor 3
    ]

    _BASE_RANGES = {"easy": (1, 10), "medium": (1, 30), "hard": (1, 80)}
    _T_RANGES = {"easy": (1, 3), "medium": (2, 4), "hard": (3, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r_pct, (num, den) = rng.choice(self._RATE_CHOICES)
        t_lo, t_hi = self._T_RANGES[difficulty]
        t = rng.randint(t_lo, t_hi)
        base_lo, base_hi = self._BASE_RANGES[difficulty]
        # To get clean integer output: P_0 must be divisible by den^t.
        denom_t = den ** t
        max_k = max(1, base_hi // denom_t)
        k = rng.randint(1, max_k)
        p0 = k * denom_t
        # Final population = p0 * (num/den)^t = k * num^t
        final_pop = k * (num ** t)

        r_display = f"{r_pct}\\%"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (p0, r_pct, t)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A population starts at $P_0 = {p0}$ and grows at a "
                f"rate of ${r_display}$ per year. Using "
                f"$P(t) = P_0 (1 + r)^{{t}}$, find the population after "
                f"$t = {t}$ years."
            ),
            answer_latex=f"$P({t}) = {final_pop}$",
            hints=[
                (
                    f"Write $1 + r$ as a clean fraction: "
                    f"$1 + {r_pct / 100} = \\dfrac{{{num}}}{{{den}}}$."
                ),
                (
                    f"Substitute $P_0 = {p0}$, $t = {t}$: "
                    f"$P({t}) = {p0} \\cdot \\left(\\dfrac{{{num}}}{{{den}}}"
                    f"\\right)^{{{t}}}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Convert the percent rate to a decimal: "
                    f"$r = {r_pct / 100}$, so $1 + r = \\dfrac{{{num}}}{{{den}}}$."
                ),
                (
                    f"Substitute into $P(t) = P_0 (1 + r)^{{t}}$: "
                    f"$P({t}) = {p0} \\cdot \\left(\\dfrac{{{num}}}{{{den}}}"
                    f"\\right)^{{{t}}}$."
                ),
                (
                    f"Compute $\\left(\\dfrac{{{num}}}{{{den}}}\\right)^{{{t}}} "
                    f"= \\dfrac{{{num ** t}}}{{{den ** t}}}$."
                ),
                (
                    f"Multiply: ${p0} \\cdot \\dfrac{{{num ** t}}}{{{den ** t}}} "
                    f"= {final_pop}$."
                ),
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals"],
        )


@register
class HalfLifeDecay(Generator):
    """Half-life decay: A(t) = A_0 * (1/2)^(t/T) with integer answer.

    Backward: pick integer A_0 divisible by 2^k for some integer k, pick
    half-life T, and set elapsed time t = k*T so that A(t) = A_0 / 2^k.
    """
    generator_id = "half_life_decay"
    topic_slug = "growth_decay_and_applications"
    display_name = "Half-life decay A(t) = A_0 * (1/2)^(t/T)"

    _K_RANGES = {"easy": (1, 4), "medium": (2, 5), "hard": (3, 6)}
    _T_HALF_CHOICES = (2, 3, 4, 5, 6, 10)
    _MULTIPLIER_RANGES = {"easy": (1, 6), "medium": (2, 12), "hard": (3, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        t_half = rng.choice(self._T_HALF_CHOICES)
        mult_lo, mult_hi = self._MULTIPLIER_RANGES[difficulty]
        m = rng.randint(mult_lo, mult_hi)
        a0 = m * (2 ** k)
        elapsed = k * t_half
        remaining = m  # A_0 / 2^k

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a0, t_half, elapsed)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A radioactive sample has initial mass $A_0 = {a0}$ grams "
                f"and a half-life of $T = {t_half}$ years. Using "
                f"$A(t) = A_0 \\left(\\dfrac{{1}}{{2}}\\right)^{{t/T}}$, "
                f"find the remaining mass after $t = {elapsed}$ years."
            ),
            answer_latex=f"$A({elapsed}) = {remaining}$ grams",
            hints=[
                (
                    f"Compute the exponent $t / T = {elapsed} / {t_half} = {k}$."
                ),
                (
                    f"The sample goes through {k} half-lives, so the mass is "
                    f"halved {k} times."
                ),
                (
                    f"${a0} \\cdot \\left(\\dfrac{{1}}{{2}}\\right)^{{{k}}} = "
                    f"\\dfrac{{{a0}}}{{{2 ** k}}} = {remaining}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Compute $\\dfrac{{t}}{{T}} = \\dfrac{{{elapsed}}}{{{t_half}}} "
                    f"= {k}$."
                ),
                (
                    f"Substitute into the decay formula: "
                    f"$A({elapsed}) = {a0} \\cdot \\left(\\dfrac{{1}}{{2}}"
                    f"\\right)^{{{k}}}$."
                ),
                (
                    f"Evaluate $\\left(\\dfrac{{1}}{{2}}\\right)^{{{k}}} = "
                    f"\\dfrac{{1}}{{{2 ** k}}}$."
                ),
                (
                    f"Multiply: $A({elapsed}) = \\dfrac{{{a0}}}{{{2 ** k}}} "
                    f"= {remaining}$ grams."
                ),
            ],
            tags=["#branch-algebra-2", "#topic-exponents-and-radicals"],
        )


# ===========================================================================
# Topic 4: introduction_to_exponentials_and_logarithms
# ===========================================================================


@register
class ExpLogConvertForms(Generator):
    """Convert between exponential form b^y = x and logarithmic form log_b(x) = y.

    Backward: pick base b in {2, 3, 5, 10} and integer y, compute x = b^y.
    Then randomly pick a direction.
    """
    generator_id = "exp_log_convert_forms"
    topic_slug = "introduction_to_exponentials_and_logarithms"
    display_name = "Convert between exponential and logarithmic form"

    _B_CHOICES = (2, 3, 5, 10)
    _Y_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (-3, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        b = rng.choice(self._B_CHOICES)
        y_lo, y_hi = self._Y_RANGES[difficulty]
        y = rng.randint(y_lo, y_hi)
        while y == 0:
            y = rng.randint(y_lo, y_hi)
        if b == 10 and y > 4:
            y = 4

        if y >= 0:
            x_val = b ** y
            x_str = str(x_val)
            x_latex = str(x_val)
        else:
            x_val = Fraction(1, b ** (-y))
            x_str = f"1/{b ** (-y)}"
            x_latex = rf"\dfrac{{1}}{{{b ** (-y)}}}"

        direction = rng.choice(["to_log", "to_exp"])

        if direction == "to_log":
            statement = (
                f"Rewrite the equation ${b}^{{{y}}} = {x_latex}$ in "
                "logarithmic form."
            )
            answer_latex = f"$\\log_{{{b}}}({x_latex}) = {y}$"
            hints = [
                (
                    "The definition $b^y = x$ is equivalent to "
                    "$\\log_b(x) = y$."
                ),
                (
                    f"Here the base is $b = {b}$, the exponent is $y = {y}$, "
                    f"and the result is $x = {x_latex}$."
                ),
            ]
            steps = [
                (
                    "Use the definition of a logarithm: "
                    "$b^y = x \\iff \\log_b(x) = y$."
                ),
                (
                    f"Identify $b = {b}$, $y = {y}$, and $x = {x_latex}$."
                ),
                (
                    f"Rewrite: $\\log_{{{b}}}({x_latex}) = {y}$."
                ),
            ]
        else:
            statement = (
                f"Rewrite the equation $\\log_{{{b}}}({x_latex}) = {y}$ "
                "in exponential form."
            )
            answer_latex = f"${b}^{{{y}}} = {x_latex}$"
            hints = [
                (
                    "The definition $\\log_b(x) = y$ is equivalent to "
                    "$b^y = x$."
                ),
                (
                    f"Here the base is $b = {b}$, the exponent is $y = {y}$, "
                    f"and the result is $x = {x_latex}$."
                ),
            ]
            steps = [
                (
                    "Use the definition of a logarithm: "
                    "$\\log_b(x) = y \\iff b^y = x$."
                ),
                (
                    f"Identify $b = {b}$, $y = {y}$, and $x = {x_latex}$."
                ),
                (
                    f"Rewrite: ${b}^{{{y}}} = {x_latex}$."
                ),
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (b, y, direction)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


@register
class NaturalLogEvaluateCleanPowers(Generator):
    """Evaluate ln(e^n) for integer n, plus ln(1) = 0 and ln(e) = 1.

    Backward: pick integer exponent n and present as ln(e^n). Occasionally
    force n = 0 (ln 1 = 0) and n = 1 (ln e = 1) as special cases.
    """
    generator_id = "natural_log_evaluate_clean_powers"
    topic_slug = "introduction_to_exponentials_and_logarithms"
    display_name = "Evaluate natural log of clean powers of e"

    _N_RANGES = {"easy": (-5, 8), "medium": (-8, 12), "hard": (-12, 18)}
    bank_count_per_difficulty = 12  # parameter space is small; still ~14 per range

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        if n == 0:
            statement = "Evaluate $\\ln(1)$."
            answer_latex = "$0$"
            hints = [
                "Recall that $\\ln x = \\log_e x$.",
                "For any base $b$, $\\log_b(1) = 0$, because $b^0 = 1$.",
            ]
            steps = [
                "Use the identity $\\log_b(1) = 0$ for any valid base $b$.",
                "So $\\ln(1) = 0$.",
            ]
        elif n == 1:
            statement = "Evaluate $\\ln(e)$."
            answer_latex = "$1$"
            hints = [
                "Recall that $\\ln x = \\log_e x$.",
                "For any base $b$, $\\log_b(b) = 1$, because $b^1 = b$.",
            ]
            steps = [
                "Use the identity $\\log_b(b) = 1$ for any valid base.",
                "So $\\ln(e) = 1$.",
            ]
        else:
            arg_latex = f"e^{{{n}}}"
            statement = f"Evaluate $\\ln({arg_latex})$."
            answer_latex = f"${n}$"
            hints = [
                "Recall the identity $\\ln(e^{k}) = k$ for any real number $k$.",
                (
                    f"Here the exponent inside is ${n}$, so the natural log "
                    f"simply extracts it."
                ),
            ]
            steps = [
                (
                    "Apply the identity $\\ln(e^{k}) = k$, which follows "
                    "from $\\log_b(b^{k}) = k$."
                ),
                f"With $k = {n}$, we get $\\ln({arg_latex}) = {n}$.",
            ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


@register
class LogBaseEvaluateClean(Generator):
    """Evaluate log_b(b^n) = n, including log_b(x) where x is a clean power of b.

    Backward: pick base b and integer exponent n, compute x = b^n, present
    as log_b(x). Mixes direct integer x and negative exponents.
    """
    generator_id = "log_base_evaluate_clean"
    topic_slug = "introduction_to_exponentials_and_logarithms"
    display_name = "Evaluate log_b(b^n) for clean bases"

    _B_CHOICES = (2, 3, 4, 5, 10)
    _N_RANGES = {"easy": (1, 4), "medium": (1, 5), "hard": (-4, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        b = rng.choice(self._B_CHOICES)
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)
        while n == 0:
            n = rng.randint(n_lo, n_hi)
        if b == 10 and n > 4:
            n = 4

        if n > 0:
            x_val = b ** n
            x_latex = str(x_val)
        else:
            x_latex = rf"\dfrac{{1}}{{{b ** (-n)}}}"

        statement = f"Evaluate $\\log_{{{b}}}({x_latex})$."
        answer_latex = f"${n}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=[
                (
                    f"Ask: what power of ${b}$ gives ${x_latex}$?"
                ),
                (
                    "Use the identity $\\log_b(b^{k}) = k$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Rewrite the argument as a power of ${b}$: "
                    f"${x_latex} = {b}^{{{n}}}$."
                ),
                (
                    f"Apply $\\log_b(b^{{k}}) = k$: "
                    f"$\\log_{{{b}}}({b}^{{{n}}}) = {n}$."
                ),
                f"So $\\log_{{{b}}}({x_latex}) = {n}$.",
            ],
            tags=["#branch-pre-calculus", "#topic-logarithms"],
        )


# ===========================================================================
# Topic 5: simple_and_compound_interest
# ===========================================================================


@register
class SimpleInterestCompute(Generator):
    """Compute simple interest I = P*r*t with clean integer answer.

    Backward: pick target I as a clean integer, then pick clean P, r, t
    whose product equals I.
    """
    generator_id = "simple_interest_compute"
    topic_slug = "simple_and_compound_interest"
    display_name = "Compute simple interest I = Prt"

    # (principal, rate_pct, time_years) tuples that produce clean-integer I.
    _CASES_EASY = [
        (100, 5, 2),    # I = 100 * 0.05 * 2 = 10
        (200, 10, 1),   # I = 20
        (500, 4, 2),    # I = 40
        (1000, 6, 1),   # I = 60
        (400, 5, 3),    # I = 60
        (300, 10, 2),   # I = 60
        (800, 5, 1),    # I = 40
        (150, 8, 2),    # I = 24
        (250, 4, 3),    # I = 30
        (600, 5, 2),    # I = 60
    ]
    _CASES_MEDIUM = [
        (2000, 6, 5),     # I = 600
        (1500, 8, 4),     # I = 480
        (2500, 4, 3),     # I = 300
        (1200, 10, 5),    # I = 600
        (3000, 5, 4),     # I = 600
        (800, 12, 5),     # I = 480
        (5000, 2, 6),     # I = 600
        (1600, 5, 3),     # I = 240
        (2400, 10, 2),    # I = 480
        (4000, 3, 5),     # I = 600
    ]
    _CASES_HARD = [
        (8000, 6, 5),     # I = 2400
        (10000, 4, 7),    # I = 2800
        (12000, 5, 6),    # I = 3600
        (6000, 8, 4),     # I = 1920
        (15000, 3, 8),    # I = 3600
        (20000, 5, 4),    # I = 4000
        (7500, 8, 5),     # I = 3000
        (9000, 6, 7),     # I = 3780
        (11000, 4, 5),    # I = 2200
        (14000, 5, 3),    # I = 2100
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cases = {
            "easy": self._CASES_EASY,
            "medium": self._CASES_MEDIUM,
            "hard": self._CASES_HARD,
        }[difficulty]
        p, r_pct, t = rng.choice(cases)

        r = Fraction(r_pct, 100)
        interest = p * r * t
        assert interest.denominator == 1, "interest should be integer by construction"
        interest_int = interest.numerator

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (p, r_pct, t)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Compute the simple interest on a principal of $P = \\${p}$ "
                f"at an annual rate of ${r_pct}\\%$ for $t = {t}$ years. "
                "Use $I = Prt$."
            ),
            answer_latex=f"$I = \\${interest_int}$",
            hints=[
                "Convert the percent rate to a decimal first.",
                (
                    f"Substitute $P = {p}$, $r = {r_pct / 100}$, $t = {t}$ "
                    "into $I = Prt$."
                ),
            ],
            solution_steps_latex=[
                f"Convert the rate: $r = {r_pct}\\% = {r_pct / 100}$.",
                (
                    f"Substitute into $I = P r t$: "
                    f"$I = {p} \\cdot {r_pct / 100} \\cdot {t}$."
                ),
                f"Multiply: $I = {interest_int}$.",
                f"So the interest is $\\${interest_int}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations"],
        )


@register
class SimpleInterestFindTimeOrRate(Generator):
    """Given I, P, and either r or t, solve for the missing quantity.

    Backward: pick clean P, r, t so I is integer, then hide either r or t
    and ask for it.
    """
    generator_id = "simple_interest_find_time_or_rate"
    topic_slug = "simple_and_compound_interest"
    display_name = "Find rate or time from simple interest formula"

    _CASES_EASY = [
        (100, 5, 2, 10),
        (200, 10, 1, 20),
        (500, 4, 2, 40),
        (1000, 6, 1, 60),
        (400, 5, 3, 60),
        (300, 10, 2, 60),
        (800, 5, 1, 40),
        (250, 4, 3, 30),
        (600, 5, 2, 60),
        (150, 8, 2, 24),
    ]
    _CASES_MEDIUM = [
        (2000, 6, 5, 600),
        (1500, 8, 4, 480),
        (2500, 4, 3, 300),
        (1200, 10, 5, 600),
        (3000, 5, 4, 600),
        (800, 12, 5, 480),
        (5000, 2, 6, 600),
        (1600, 5, 3, 240),
        (2400, 10, 2, 480),
        (4000, 3, 5, 600),
    ]
    _CASES_HARD = [
        (8000, 6, 5, 2400),
        (10000, 4, 7, 2800),
        (12000, 5, 6, 3600),
        (6000, 8, 4, 1920),
        (15000, 3, 8, 3600),
        (20000, 5, 4, 4000),
        (7500, 8, 5, 3000),
        (11000, 4, 5, 2200),
        (14000, 5, 3, 2100),
        (9000, 2, 5, 900),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cases = {
            "easy": self._CASES_EASY,
            "medium": self._CASES_MEDIUM,
            "hard": self._CASES_HARD,
        }[difficulty]
        p, r_pct, t, i = rng.choice(cases)
        find_rate = rng.choice([True, False])

        if find_rate:
            statement = (
                f"A principal of $P = \\${p}$ earns simple interest of "
                f"$I = \\${i}$ over $t = {t}$ years. Find the annual "
                "interest rate $r$ (as a percent). Use $I = Prt$."
            )
            answer_latex = f"$r = {r_pct}\\%$"
            hints = [
                "Rearrange the formula: $r = \\dfrac{I}{P t}$.",
                (
                    f"Substitute $I = {i}$, $P = {p}$, $t = {t}$ and compute."
                ),
            ]
            steps = [
                "Start with $I = Prt$ and solve for $r$: $r = \\dfrac{I}{Pt}$.",
                (
                    f"Substitute: $r = \\dfrac{{{i}}}{{{p} \\cdot {t}}} "
                    f"= \\dfrac{{{i}}}{{{p * t}}}$."
                ),
                f"Compute: $r = {r_pct / 100}$.",
                f"Convert to percent: $r = {r_pct}\\%$.",
            ]
            params = (p, t, i, "rate")
        else:
            statement = (
                f"A principal of $P = \\${p}$ is invested at an annual rate "
                f"of ${r_pct}\\%$ and earns simple interest of $I = \\${i}$. "
                "Find the time $t$ in years. Use $I = Prt$."
            )
            answer_latex = f"$t = {t}$ years"
            hints = [
                "Rearrange the formula: $t = \\dfrac{I}{P r}$.",
                (
                    f"Substitute $I = {i}$, $P = {p}$, $r = {r_pct / 100}$ "
                    "and compute."
                ),
            ]
            steps = [
                "Start with $I = Prt$ and solve for $t$: $t = \\dfrac{I}{Pr}$.",
                (
                    f"Substitute: $t = \\dfrac{{{i}}}{{{p} \\cdot {r_pct / 100}}} "
                    f"= \\dfrac{{{i}}}{{{p * r_pct / 100}}}$."
                ),
                f"Compute: $t = {t}$ years.",
            ]
            params = (p, r_pct, i, "time")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations"],
        )


@register
class CompoundInterestPreAlgebra(Generator):
    """Middle-school compound interest: small P, small t, small n.

    Backward: pick parameters where A rounds to a clean 2-decimal dollar
    amount. Uses the same formula as CompoundInterestDiscrete but with
    smaller numbers suitable for a first exposure.
    """
    generator_id = "compound_interest_pre_algebra"
    topic_slug = "simple_and_compound_interest"
    display_name = "Compute compound interest (pre-algebra level)"

    _CASES_EASY = [
        (100, 10, 1, 2),   # A = 100 * 1.1^2 = 121
        (200, 5, 1, 2),    # A = 200 * 1.05^2 = 220.50
        (500, 10, 1, 1),   # A = 550
        (100, 20, 1, 2),   # A = 144
        (250, 10, 1, 2),   # A = 302.50
        (100, 5, 1, 3),    # A = 115.7625 → 115.76
        (400, 10, 1, 1),   # A = 440
        (200, 10, 1, 2),   # A = 242
        (300, 10, 1, 1),   # A = 330
        (150, 10, 1, 2),   # A = 181.50
    ]
    _CASES_MEDIUM = [
        (500, 8, 1, 2),    # A = 583.20
        (1000, 5, 1, 3),   # A = 1157.625 → 1157.63
        (800, 10, 1, 2),   # A = 968
        (1200, 5, 1, 2),   # A = 1323
        (1500, 4, 1, 3),   # A = 1687.3... → 1687.30
        (600, 10, 2, 2),   # A = 600 * 1.05^4 = 729.3... → 729.30
        (2000, 10, 1, 2),  # A = 2420
        (1000, 8, 1, 2),   # A = 1166.40
        (400, 5, 2, 2),    # A = 400*1.025^4 ≈ 441.53
        (2500, 4, 1, 2),   # A = 2704
    ]
    _CASES_HARD = [
        (1000, 10, 1, 3),  # A = 1331
        (2000, 5, 1, 4),   # A = 2431.01
        (1500, 8, 2, 2),   # A = 1500*1.04^4 ≈ 1754.68
        (5000, 6, 1, 3),   # A = 5955.08
        (3000, 10, 1, 2),  # A = 3630
        (4000, 5, 2, 3),   # A = 4000*1.025^6 ≈ 4638.75
        (2500, 8, 1, 3),   # A = 3149.28
        (6000, 5, 1, 3),   # A = 6945.75
        (1000, 12, 1, 2),  # A = 1254.40
        (8000, 4, 1, 4),   # A = 9358.97
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cases = {
            "easy": self._CASES_EASY,
            "medium": self._CASES_MEDIUM,
            "hard": self._CASES_HARD,
        }[difficulty]
        p, r_pct, n, t = rng.choice(cases)

        r = r_pct / 100
        amount = p * (1 + r / n) ** (n * t)
        amount_rounded = round(amount, 2)
        if amount_rounded == int(amount_rounded):
            amount_str = f"{int(amount_rounded)}"
        else:
            amount_str = f"{amount_rounded:.2f}"

        if n == 1:
            compounding_word = "annually"
        elif n == 2:
            compounding_word = "semi-annually"
        elif n == 4:
            compounding_word = "quarterly"
        else:
            compounding_word = f"{n} times per year"

        nt = n * t

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (p, r_pct, n, t)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"You deposit $P = \\${p}$ in a savings account earning "
                f"${r_pct}\\%$ interest per year compounded {compounding_word}. "
                f"After $t = {t}$ years, how much is in the account? "
                "Use $A = P\\left(1 + \\dfrac{r}{n}\\right)^{nt}$ and round "
                "to the nearest cent."
            ),
            answer_latex=f"$A = \\${amount_str}$",
            hints=[
                (
                    f"Identify $P = {p}$, $r = {r}$, $n = {n}$, $t = {t}$."
                ),
                (
                    f"Compute the exponent $nt = {nt}$ and the base "
                    f"$1 + \\dfrac{{r}}{{n}} = {1 + r / n}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Substitute the values: "
                    f"$A = {p}\\left(1 + \\dfrac{{{r}}}{{{n}}}\\right)^{{{nt}}}$."
                ),
                (
                    f"Simplify inside the parentheses: "
                    f"$1 + \\dfrac{{{r}}}{{{n}}} = {1 + r / n}$."
                ),
                (
                    f"Raise to the ${nt}$th power: "
                    f"$({1 + r / n})^{{{nt}}} \\approx {(1 + r / n) ** nt:.5f}$."
                ),
                (
                    f"Multiply by ${p}$: $A \\approx \\${amount_str}$."
                ),
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations"],
        )
