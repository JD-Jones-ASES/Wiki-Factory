"""Radical and exponent generators (Phase 2c Wave 4).

Five topics, three generators each (15 total):

Topic 1: zero_and_negative_exponents
  - zero_exponent_simplify
  - negative_exponent_rewrite
  - combined_zero_negative_exponents

Topic 2: rational_exponents
  - rational_exponent_to_radical
  - radical_to_rational_exponent
  - rational_exponent_evaluate

Topic 3: simplifying_radical_expressions
  - simplify_sqrt_perfect_factor
  - simplify_sqrt_with_variable
  - rationalize_single_radical_denom

Topic 4: operations_with_radicals
  - add_like_radicals_after_simplify
  - multiply_radicals_product_rule
  - divide_radicals_quotient_rule

Topic 5: the_distance_formula
  - distance_formula_integer_answer
  - distance_formula_radical_answer
  - distance_check_right_triangle

All generators use backward construction so the answers are clean.
"""
from __future__ import annotations

import math
import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Small shared helpers
# ---------------------------------------------------------------------------

def _nonzero(rng: random.Random, lo: int, hi: int) -> int:
    """Return a random integer in [lo, hi] that is never zero."""
    while True:
        n = rng.randint(lo, hi)
        if n != 0:
            return n


def _squarefree_part(n: int) -> tuple[int, int]:
    """Decompose n = a^2 * b with b squarefree. Returns (a, b)."""
    if n <= 0:
        return 1, n
    a = 1
    b = n
    i = 2
    while i * i <= b:
        while b % (i * i) == 0:
            a *= i
            b //= i * i
        i += 1
    return a, b


def _sqrt_latex(coefficient: int, radicand: int) -> str:
    """Format c*sqrt(r) with simplifications for r=1, c=1, c=0."""
    if coefficient == 0:
        return "0"
    if radicand == 1:
        return str(coefficient)
    if coefficient == 1:
        return rf"\sqrt{{{radicand}}}"
    if coefficient == -1:
        return rf"-\sqrt{{{radicand}}}"
    return rf"{coefficient}\sqrt{{{radicand}}}"


# ===========================================================================
# TOPIC 1: zero_and_negative_exponents
# ===========================================================================


@register
class ZeroExponentSimplify(Generator):
    """Evaluate an expression like 5*x^0 + 3*y^0 - 7 where x^0 = y^0 = 1."""
    generator_id = "zero_exponent_simplify"
    topic_slug = "zero_and_negative_exponents"
    display_name = "Evaluate expressions with zero exponents"

    _RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (2, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Three terms: a*v1^0  (sign s1), b*v2^0 (sign s2), plain constant c.
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        s1 = rng.choice([1, -1])
        s2 = rng.choice([1, -1])
        s3 = rng.choice([1, -1])
        v1, v2 = rng.sample(["x", "y", "a", "b", "m", "n", "t"], 2)

        # Build statement using sign-aware formatting.
        first = f"{s1 * a}{v1}^0"  # leading term may have - sign
        if s1 == 1:
            first = f"{a}{v1}^0"
        else:
            first = f"-{a}{v1}^0"

        def signed_term(sign: int, coef: int, var: str | None) -> str:
            op = "+" if sign > 0 else "-"
            body = f"{coef}{var}^0" if var else f"{coef}"
            return f" {op} {body}"

        statement_inner = first + signed_term(s2, b, v2) + signed_term(s3, c, None)

        # Compute the answer: v^0 = 1 for nonzero v (assume given).
        value = s1 * a + s2 * b + s3 * c

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (s1, a, v1, s2, b, v2, s3, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Evaluate ${statement_inner}$, assuming ${v1} \\ne 0$ and ${v2} \\ne 0$."
            ),
            answer_latex=f"${value}$",
            hints=[
                r"The zero exponent rule says $a^0 = 1$ for every nonzero base $a$.",
                f"So ${v1}^0 = 1$ and ${v2}^0 = 1$ (both variables are nonzero).",
                "Replace each variable power with $1$ and then combine like terms.",
            ],
            solution_steps_latex=[
                r"Apply the zero exponent rule: $a^0 = 1$ for any nonzero base $a$.",
                f"Substitute: ${statement_inner} = {s1 * a}(1) {'+' if s2 > 0 else '-'} {b}(1) {'+' if s3 > 0 else '-'} {c}$.",
                f"Simplify: ${s1 * a} {'+' if s2 > 0 else '-'} {b} {'+' if s3 > 0 else '-'} {c} = {value}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class NegativeExponentRewrite(Generator):
    """Rewrite expressions with negative exponents as positive exponents.

    Two flavors, chosen randomly:
      (a) c * v^(-n)   -> c / v^n
      (b) c / v^(-n)   -> c * v^n
    """
    generator_id = "negative_exponent_rewrite"
    topic_slug = "zero_and_negative_exponents"
    display_name = "Rewrite negative exponents as positive"

    _RANGES = {"easy": (2, 6), "medium": (2, 10), "hard": (3, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        c = rng.randint(lo, hi)
        n = rng.randint(2, hi)
        var = rng.choice(["x", "y", "a", "b", "m", "n", "t"])
        flavor = rng.choice(["numer", "denom"])

        if flavor == "numer":
            statement = f"{c}{var}^{{-{n}}}"
            answer = rf"\dfrac{{{c}}}{{{var}^{{{n}}}}}"
            rationale_src = f"{c} \\cdot {var}^{{-{n}}}"
            rationale_mid = f"{c} \\cdot \\dfrac{{1}}{{{var}^{{{n}}}}}"
        else:
            statement = rf"\dfrac{{{c}}}{{{var}^{{-{n}}}}}"
            answer = f"{c}{var}^{{{n}}}"
            rationale_src = rf"\dfrac{{{c}}}{{{var}^{{-{n}}}}}"
            rationale_mid = f"{c} \\cdot {var}^{{{n}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (c, n, var, flavor)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Rewrite ${statement}$ using only positive exponents. Assume ${var} \\ne 0$."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"The negative exponent rule says $a^{-n} = \dfrac{1}{a^n}$, and equivalently $\dfrac{1}{a^{-n}} = a^n$.",
                "A negative exponent on top moves to the bottom (and vice versa) and becomes positive.",
                f"Apply the rule to the factor ${var}^{{{'-' if flavor == 'numer' else '-'}{n}}}$.",
            ],
            solution_steps_latex=[
                r"Use $a^{-n} = \dfrac{1}{a^n}$.",
                f"Rewrite: ${rationale_src} = {rationale_mid}$.",
                f"Combine: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class CombinedZeroNegativeExponents(Generator):
    """Simplify a compound expression like (p * a^(-m) * b^k) / (q * c^0 * a^(-j))."""
    generator_id = "combined_zero_negative_exponents"
    topic_slug = "zero_and_negative_exponents"
    display_name = "Simplify expressions with zero and negative exponents"

    _RANGES = {"easy": (2, 5), "medium": (2, 8), "hard": (3, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        p = rng.randint(2, hi)
        q = rng.randint(2, hi)
        # Make p/q cancel cleanly: pick q to divide p when possible, else multiply p by q.
        if p % q != 0:
            p = p * q  # now p/q = original p
        coef = p // q

        m = rng.randint(2, hi)   # exponent on a in numerator (negative)
        k = rng.randint(2, hi)   # exponent on b in numerator (positive)
        j = rng.randint(1, m - 1)  # exponent on a in denominator (negative), strictly less than m

        # Numerator:   p * a^(-m) * b^k
        # Denominator: q * c^0 * a^(-j)
        # Simplify step-by-step:
        #   c^0 = 1.
        #   a^(-m) / a^(-j) = a^(-m - (-j)) = a^(j - m)   (negative since j < m)
        #   = 1 / a^(m - j)
        # Final: (p/q) * b^k / a^(m - j) = coef * b^k / a^(m - j)
        a_final_exp = m - j  # positive

        stmt = (
            rf"\dfrac{{{p}a^{{-{m}}} b^{{{k}}}}}{{{q} \cdot c^0 \cdot a^{{-{j}}}}}"
        )
        # Build answer LaTeX
        if coef == 1:
            answer = rf"\dfrac{{b^{{{k}}}}}{{a^{{{a_final_exp}}}}}"
        else:
            answer = rf"\dfrac{{{coef}b^{{{k}}}}}{{a^{{{a_final_exp}}}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, q, m, k, j)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Simplify ${stmt}$ so that the answer has only positive exponents. "
                "Assume $a, b, c$ are nonzero."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Start by using $c^0 = 1$ to remove the $c$ factor from the denominator.",
                r"Combine the $a$ powers using $\dfrac{a^p}{a^r} = a^{p-r}$.",
                r"Any remaining negative exponent $a^{-n}$ becomes $\dfrac{1}{a^n}$.",
            ],
            solution_steps_latex=[
                f"Replace $c^0$ with $1$: ${stmt} = \\dfrac{{{p}a^{{-{m}}} b^{{{k}}}}}{{{q} a^{{-{j}}}}}$.",
                f"Reduce the numeric coefficient: $\\dfrac{{{p}}}{{{q}}} = {coef}$.",
                f"Combine the $a$ powers: $\\dfrac{{a^{{-{m}}}}}{{a^{{-{j}}}}} = a^{{-{m} - (-{j})}} = a^{{{j - m}}}$.",
                f"Rewrite the negative exponent: $a^{{{j - m}}} = \\dfrac{{1}}{{a^{{{a_final_exp}}}}}$.",
                f"Combine all factors: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# TOPIC 2: rational_exponents
# ===========================================================================


@register
class RationalExponentToRadical(Generator):
    """Rewrite a^(m/n) as an nth root."""
    generator_id = "rational_exponent_to_radical"
    topic_slug = "rational_exponents"
    display_name = "Convert rational exponent to radical form"

    _RANGES = {"easy": (2, 6), "medium": (2, 10), "hard": (2, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        base_sym = rng.choice(["x", "y", "a", "b", "t"])
        m = rng.randint(2, hi)
        n = rng.randint(2, 5)
        # Ensure m/n is not an integer (so the radical form is non-trivial).
        while m % n == 0:
            m = rng.randint(2, hi + 1)

        # Expression: base^(m/n)
        stmt = f"{base_sym}^{{{m}/{n}}}"
        # Standard answer: nth root of base^m
        if n == 2:
            answer = rf"\sqrt{{{base_sym}^{{{m}}}}}"
        else:
            answer = rf"\sqrt[{n}]{{{base_sym}^{{{m}}}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base_sym, m, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Rewrite ${stmt}$ as a radical. Assume ${base_sym} \\ge 0$.",
            answer_latex=f"${answer}$",
            hints=[
                r"The rational exponent rule: $a^{m/n} = \sqrt[n]{a^m}$.",
                r"The denominator of the exponent becomes the index of the radical; the numerator stays as the power inside.",
                f"Here the denominator is ${n}$ and the numerator is ${m}$.",
            ],
            solution_steps_latex=[
                r"Use $a^{m/n} = \sqrt[n]{a^m}$.",
                f"Match $m = {m}$ and $n = {n}$.",
                f"Substitute: ${stmt} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class RadicalToRationalExponent(Generator):
    """Rewrite nth-root of a^m as a^(m/n)."""
    generator_id = "radical_to_rational_exponent"
    topic_slug = "rational_exponents"
    display_name = "Convert radical form to rational exponent"

    _RANGES = {"easy": (2, 6), "medium": (2, 10), "hard": (2, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        base_sym = rng.choice(["x", "y", "a", "b", "t"])
        m = rng.randint(2, hi)
        n = rng.randint(2, 5)
        while m % n == 0:
            m = rng.randint(2, hi + 1)

        if n == 2:
            stmt = rf"\sqrt{{{base_sym}^{{{m}}}}}"
        else:
            stmt = rf"\sqrt[{n}]{{{base_sym}^{{{m}}}}}"
        answer = f"{base_sym}^{{{m}/{n}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base_sym, m, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Rewrite ${stmt}$ as a rational exponent. Assume ${base_sym} \\ge 0$.",
            answer_latex=f"${answer}$",
            hints=[
                r"The rational exponent rule: $\sqrt[n]{a^m} = a^{m/n}$.",
                r"The index of the radical becomes the denominator of the exponent; the power inside becomes the numerator.",
                f"Here the index is ${n}$ and the inner power is ${m}$.",
            ],
            solution_steps_latex=[
                r"Use $\sqrt[n]{a^m} = a^{m/n}$.",
                f"Identify $m = {m}$ (the power under the radical) and $n = {n}$ (the index).",
                f"Substitute: ${stmt} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class RationalExponentEvaluate(Generator):
    """Evaluate base^(m/n) where base is a perfect n-th power.

    Backward construction: pick a small integer k and an index n.
    Let base = k^n.  Then base^(1/n) = k, and base^(m/n) = k^m.
    Ensure the final answer is a clean integer and that the problem
    is not trivial (m != n, so the original exponent is not 1).
    """
    generator_id = "rational_exponent_evaluate"
    topic_slug = "rational_exponents"
    display_name = "Evaluate a^(m/n) with a perfect power base"
    bank_count_per_difficulty = 30

    # (k_hi, n_hi, m_hi): controls the magnitude of the generated numbers.
    _RANGES = {
        "easy":   (4, 3, 5),   # k in 2..4, n in 2..3, m in 2..5
        "medium": (5, 4, 6),
        "hard":   (6, 5, 8),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_hi, n_hi, m_hi = self._RANGES[difficulty]
        while True:
            k = rng.randint(2, k_hi)
            n = rng.randint(2, n_hi)
            m = rng.randint(2, m_hi)
            if m == n:
                continue
            base = k ** n
            # Keep the result reasonable in size.
            if base <= 1024 and (k ** m) <= 10_000:
                break

        answer_val = k ** m

        if n == 2:
            radical_latex = rf"\sqrt{{{base}}}"
        else:
            radical_latex = rf"\sqrt[{n}]{{{base}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, n, m)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${base}^{{{m}/{n}}}$.",
            answer_latex=f"${answer_val}$",
            hints=[
                r"Rewrite as a radical: $a^{m/n} = \left(\sqrt[n]{a}\right)^m$.",
                f"First take the ${n}$-th root: $\\sqrt[{n}]{{{base}}} = {k}$ because ${k}^{{{n}}} = {base}$.",
                f"Then raise to the ${m}$-th power: ${k}^{{{m}}} = {answer_val}$.",
            ],
            solution_steps_latex=[
                rf"Use $a^{{m/n}} = \left(\sqrt[n]{{a}}\right)^m$.",
                f"Compute the root first: ${radical_latex} = {k}$ because ${k}^{{{n}}} = {base}$.",
                f"Raise to the numerator power: $\\left({k}\\right)^{{{m}}} = {answer_val}$.",
                f"So ${base}^{{{m}/{n}}} = {answer_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-procedural-calculation"],
        )


# ===========================================================================
# TOPIC 3: simplifying_radical_expressions
# ===========================================================================


@register
class SimplifySqrtPerfectFactor(Generator):
    """Simplify sqrt(n) by pulling out a perfect-square factor.

    Backward: pick a >= 2 (the coefficient to pull out) and b squarefree >= 2
    (so the result is a true simplification). Problem shows sqrt(a^2 * b),
    answer is a * sqrt(b).
    """
    generator_id = "simplify_sqrt_perfect_factor"
    topic_slug = "simplifying_radical_expressions"
    display_name = "Simplify a square root with a perfect-square factor"
    bank_count_per_difficulty = 30

    # Squarefree values of b used as the radicand remainder.
    _SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]

    _A_RANGES = {"easy": (2, 5), "medium": (2, 9), "hard": (3, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.choice(self._SQUAREFREE)
        n = (a * a) * b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify $\\sqrt{{{n}}}$.",
            answer_latex=f"${a}\\sqrt{{{b}}}$",
            hints=[
                r"Look for a perfect-square factor of the radicand.",
                f"Try to write ${n}$ as $k^2 \\cdot m$ with $m$ having no remaining perfect-square factors.",
                f"Check: ${a}^2 = {a * a}$ divides ${n}$, since ${n} = {a * a} \\cdot {b}$.",
            ],
            solution_steps_latex=[
                f"Factor the radicand: ${n} = {a * a} \\cdot {b} = {a}^2 \\cdot {b}$.",
                rf"Use $\sqrt{{x^2 y}} = x\sqrt{{y}}$ for $x \ge 0$:",
                f"$\\sqrt{{{n}}} = \\sqrt{{{a}^2 \\cdot {b}}} = {a}\\sqrt{{{b}}}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class SimplifySqrtWithVariable(Generator):
    """Simplify sqrt(c^2 * v^(2p+r)) where v is a variable.

    Backward: pick c (coefficient), p (even-power portion), r in {0, 1}
    (remainder 0 gives a clean variable power, 1 leaves a v under the root).
    """
    generator_id = "simplify_sqrt_with_variable"
    topic_slug = "simplifying_radical_expressions"
    display_name = "Simplify a square root containing a variable"
    bank_count_per_difficulty = 30

    _C_RANGES = {"easy": (2, 5), "medium": (2, 9), "hard": (3, 14)}
    _P_RANGES = {"easy": (1, 3), "medium": (1, 5), "hard": (2, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._C_RANGES[difficulty]
        p_lo, p_hi = self._P_RANGES[difficulty]
        c = rng.randint(c_lo, c_hi)
        p = rng.randint(p_lo, p_hi)
        r = rng.choice([0, 1])  # leftover under the radical
        var = rng.choice(["x", "y", "a", "b"])
        inside_exp = 2 * p + r  # total exponent under the radical
        c_sq = c * c

        # LaTeX for the input radical
        if inside_exp == 1:
            inside = var
        else:
            inside = f"{var}^{{{inside_exp}}}"
        if c_sq == 1:
            stmt = rf"\sqrt{{{inside}}}"
        else:
            stmt = rf"\sqrt{{{c_sq}{inside}}}"

        # LaTeX for answer coefficient * variable^p [ * sqrt(var) if r == 1 ]
        if p == 0:
            outside_var = ""
        elif p == 1:
            outside_var = var
        else:
            outside_var = f"{var}^{{{p}}}"
        outside_coef = "" if c == 1 else str(c)
        left = f"{outside_coef}{outside_var}"
        if left == "":
            left = "1"
        if r == 1:
            answer = f"{left}\\sqrt{{{var}}}"
        else:
            answer = left

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (c, p, r, var)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Simplify ${stmt}$, assuming ${var} \\ge 0$."
            ),
            answer_latex=f"${answer}$",
            hints=[
                rf"Separate the square root: $\sqrt{{{c_sq}{inside}}} = \sqrt{{{c_sq}}} \cdot \sqrt{{{inside}}}$.",
                rf"Use $\sqrt{{{c_sq}}} = {c}$ and $\sqrt{{x^{{2p}}}} = x^{{p}}$ for $x \ge 0$.",
                f"Any remaining odd power of ${var}$ leaves a single ${var}$ under the radical.",
            ],
            solution_steps_latex=[
                f"Factor the radicand: ${c_sq}{inside} = {c}^2 \\cdot {var}^{{{2 * p}}} \\cdot {var}^{{{r}}}$.",
                rf"Pull out perfect squares: $\sqrt{{{c}^2}} = {c}$ and $\sqrt{{{var}^{{{2 * p}}}}} = {var}^{{{p}}}$.",
                f"Combine: ${stmt} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class RationalizeSingleRadicalDenom(Generator):
    """Rationalize a denominator of the form k / sqrt(n)."""
    generator_id = "rationalize_single_radical_denom"
    topic_slug = "simplifying_radical_expressions"
    display_name = "Rationalize a single radical denominator"
    bank_count_per_difficulty = 30

    # Use squarefree n so the radical doesn't simplify further.
    _SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]
    _K_RANGES = {"easy": (2, 8), "medium": (2, 15), "hard": (3, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        n = rng.choice(self._SQUAREFREE)

        # k / sqrt(n) = k * sqrt(n) / n
        num_coef = k
        denom = n
        g = math.gcd(num_coef, denom)
        reduced_num = num_coef // g
        reduced_denom = denom // g

        # Build the LaTeX answer.
        if reduced_denom == 1:
            answer = f"{reduced_num}\\sqrt{{{n}}}"
        elif reduced_num == 1:
            answer = rf"\dfrac{{\sqrt{{{n}}}}}{{{reduced_denom}}}"
        else:
            answer = rf"\dfrac{{{reduced_num}\sqrt{{{n}}}}}{{{reduced_denom}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (k, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Rationalize the denominator of $\\dfrac{{{k}}}{{\\sqrt{{{n}}}}}$ and simplify."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"To rationalize $\dfrac{k}{\sqrt{n}}$, multiply top and bottom by $\sqrt{n}$.",
                rf"Because $\sqrt{{n}} \cdot \sqrt{{n}} = n$, the denominator becomes an integer.",
                "If possible, reduce the resulting fraction.",
            ],
            solution_steps_latex=[
                rf"Multiply numerator and denominator by $\sqrt{{{n}}}$: $\dfrac{{{k}}}{{\sqrt{{{n}}}}} \cdot \dfrac{{\sqrt{{{n}}}}}{{\sqrt{{{n}}}}} = \dfrac{{{k}\sqrt{{{n}}}}}{{{n}}}$.",
                f"Reduce the fraction: $\\gcd({num_coef}, {n}) = {g}$, so the simplified result is ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# TOPIC 4: operations_with_radicals
# ===========================================================================


@register
class AddLikeRadicalsAfterSimplify(Generator):
    """Add two radicals that become like after simplification.

    Backward: pick squarefree b, and coefficients a1, a2. Then
      sqrt((a1^2)*b) + sqrt((a2^2)*b) = a1*sqrt(b) + a2*sqrt(b) = (a1+a2)*sqrt(b).
    Occasionally subtract (50%).
    """
    generator_id = "add_like_radicals_after_simplify"
    topic_slug = "operations_with_radicals"
    display_name = "Add or subtract like radicals after simplification"
    bank_count_per_difficulty = 30

    _SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]
    _A_RANGES = {"easy": (2, 5), "medium": (2, 8), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        b = rng.choice(self._SQUAREFREE)
        a1 = rng.randint(a_lo, a_hi)
        a2 = rng.randint(a_lo, a_hi)
        while a1 == a2:
            a2 = rng.randint(a_lo, a_hi)
        op = rng.choice(["+", "-"])

        n1 = (a1 * a1) * b
        n2 = (a2 * a2) * b
        statement = rf"\sqrt{{{n1}}} {op} \sqrt{{{n2}}}"

        total_coef = a1 + a2 if op == "+" else a1 - a2
        answer = _sqrt_latex(total_coef, b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, a2, b, op)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement}$.",
            answer_latex=f"${answer}$",
            hints=[
                "Simplify each square root by pulling out a perfect-square factor.",
                f"$\\sqrt{{{n1}}} = {a1}\\sqrt{{{b}}}$ and $\\sqrt{{{n2}}} = {a2}\\sqrt{{{b}}}$.",
                f"Now the two terms are like radicals; combine their coefficients.",
            ],
            solution_steps_latex=[
                f"Simplify each radical: $\\sqrt{{{n1}}} = \\sqrt{{{a1}^2 \\cdot {b}}} = {a1}\\sqrt{{{b}}}$ and $\\sqrt{{{n2}}} = \\sqrt{{{a2}^2 \\cdot {b}}} = {a2}\\sqrt{{{b}}}$.",
                f"Combine like radicals: ${a1}\\sqrt{{{b}}} {op} {a2}\\sqrt{{{b}}} = ({a1} {op} {a2})\\sqrt{{{b}}} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class MultiplyRadicalsProductRule(Generator):
    """Apply sqrt(a) * sqrt(b) = sqrt(a*b) and then simplify.

    Backward: pick c >= 1 and a squarefree m so the intended answer is
    c * sqrt(m).  Then split c^2 * m into two factors u * v (with u, v >= 2)
    and present sqrt(u) * sqrt(v) to the student.
    """
    generator_id = "multiply_radicals_product_rule"
    topic_slug = "operations_with_radicals"
    display_name = "Multiply radicals using the product rule"
    bank_count_per_difficulty = 30

    _SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]
    _C_RANGES = {"easy": (2, 4), "medium": (2, 6), "hard": (2, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._C_RANGES[difficulty]
        c = rng.randint(c_lo, c_hi)
        m = rng.choice(self._SQUAREFREE)
        product = (c * c) * m  # this is what's under the single merged radical

        # Pick a factor u of `product` with 2 <= u <= product // 2. Ensure u != product.
        divisors = [d for d in range(2, product) if product % d == 0]
        if not divisors:
            # Fallback: use product itself (rare; force a trivial factorisation).
            u = product
            v = 1
        else:
            u = rng.choice(divisors)
            v = product // u
            # Prefer u <= v for display stability (not required).
            if u > v:
                u, v = v, u

        answer = _sqrt_latex(c, m)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (u, v, c, m)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify $\\sqrt{{{u}}} \\cdot \\sqrt{{{v}}}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Use the product rule for radicals: $\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}$.",
                f"Multiply under one radical: $\\sqrt{{{u}}} \\cdot \\sqrt{{{v}}} = \\sqrt{{{product}}}$.",
                "Then pull out any perfect-square factors from the radicand.",
            ],
            solution_steps_latex=[
                rf"Apply the product rule: $\sqrt{{{u}}} \cdot \sqrt{{{v}}} = \sqrt{{{u} \cdot {v}}} = \sqrt{{{product}}}$.",
                f"Factor the radicand: ${product} = {c}^2 \\cdot {m}$.",
                f"Pull the perfect square out: $\\sqrt{{{product}}} = \\sqrt{{{c}^2}} \\cdot \\sqrt{{{m}}} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


@register
class DivideRadicalsQuotientRule(Generator):
    """Apply sqrt(a)/sqrt(b) = sqrt(a/b) and simplify.

    Backward: pick squarefree m and an integer k >= 1. The intended simplified
    answer is k*sqrt(m). Choose b, then a = b * k^2 * m so that
    sqrt(a)/sqrt(b) = sqrt(k^2 * m) = k*sqrt(m).
    """
    generator_id = "divide_radicals_quotient_rule"
    topic_slug = "operations_with_radicals"
    display_name = "Divide radicals using the quotient rule"
    bank_count_per_difficulty = 30

    _SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]
    _K_RANGES = {"easy": (1, 4), "medium": (2, 6), "hard": (2, 10)}
    _B_RANGES = {"easy": (2, 6), "medium": (2, 9), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k_lo, k_hi = self._K_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        k = rng.randint(k_lo, k_hi)
        m = rng.choice(self._SQUAREFREE)
        b = rng.randint(b_lo, b_hi)
        a = b * (k * k) * m  # a / b = k^2 * m

        answer = _sqrt_latex(k, m)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, k, m)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify $\\dfrac{{\\sqrt{{{a}}}}}{{\\sqrt{{{b}}}}}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Use the quotient rule: $\dfrac{\sqrt{a}}{\sqrt{b}} = \sqrt{\dfrac{a}{b}}$.",
                f"First divide inside: $\\dfrac{{{a}}}{{{b}}} = {(k * k) * m}$.",
                "Then simplify the resulting square root by pulling out any perfect-square factor.",
            ],
            solution_steps_latex=[
                rf"Apply the quotient rule: $\dfrac{{\sqrt{{{a}}}}}{{\sqrt{{{b}}}}} = \sqrt{{\dfrac{{{a}}}{{{b}}}}} = \sqrt{{{(k * k) * m}}}$.",
                f"Factor the radicand: ${(k * k) * m} = {k}^2 \\cdot {m}$.",
                f"Pull out the perfect square: $\\sqrt{{{(k * k) * m}}} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# TOPIC 5: the_distance_formula
# ===========================================================================


# Pythagorean triples used for integer-answer distance problems.
_TRIPLES: list[tuple[int, int, int]] = [
    (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
    (6, 8, 10), (9, 12, 15), (9, 40, 41), (20, 21, 29),
]


@register
class DistanceFormulaIntegerAnswer(Generator):
    """Two points whose separation forms a Pythagorean triple (integer distance)."""
    generator_id = "distance_formula_integer_answer"
    topic_slug = "the_distance_formula"
    display_name = "Distance formula with integer answer"
    bank_count_per_difficulty = 30

    _ORIGIN_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ORIGIN_RANGES[difficulty]
        a, b, c = rng.choice(_TRIPLES)
        # Randomly swap legs so horizontal/vertical orientations vary.
        if rng.random() < 0.5:
            a, b = b, a
        # Random sign on each leg
        sx = rng.choice([1, -1])
        sy = rng.choice([1, -1])
        x1 = rng.randint(lo, hi)
        y1 = rng.randint(lo, hi)
        x2 = x1 + sx * a
        y2 = y1 + sy * b
        dx = x2 - x1
        dy = y2 - y1
        squared = dx * dx + dy * dy  # should equal c*c

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the distance between the points $({x1}, {y1})$ and $({x2}, {y2})$."
            ),
            answer_latex=f"$d = {c}$",
            hints=[
                r"Distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
                f"Compute $x_2 - x_1 = {x2} - ({x1}) = {dx}$ and $y_2 - y_1 = {y2} - ({y1}) = {dy}$.",
                f"Square and add: ${dx}^2 + {dy}^2 = {dx * dx} + {dy * dy} = {squared}$.",
                f"Take the square root: $\\sqrt{{{squared}}} = {c}$.",
            ],
            solution_steps_latex=[
                r"Apply the distance formula $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
                f"Substitute: $d = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}} = \\sqrt{{{dx}^2 + {dy}^2}}$.",
                f"Compute inside: ${dx * dx} + {dy * dy} = {squared}$.",
                f"Take the square root: $d = \\sqrt{{{squared}}} = {c}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )


@register
class DistanceFormulaRadicalAnswer(Generator):
    """Two points whose separation is a non-triple, giving a radical distance."""
    generator_id = "distance_formula_radical_answer"
    topic_slug = "the_distance_formula"
    display_name = "Distance formula with radical answer"
    bank_count_per_difficulty = 30

    _LEG_RANGES = {"easy": (1, 5), "medium": (1, 8), "hard": (2, 12)}
    _ORIGIN_RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._LEG_RANGES[difficulty]
        olo, ohi = self._ORIGIN_RANGES[difficulty]

        # Pick legs so the resulting hypotenuse is NOT an integer, giving a radical answer.
        for _ in range(50):
            a = rng.randint(lo, hi)
            b = rng.randint(lo, hi)
            squared = a * a + b * b
            root = math.isqrt(squared)
            if root * root == squared:
                continue  # integer distance, reject
            if squared == 0:
                continue
            break
        else:
            a, b = 1, 2  # guaranteed non-square (sqrt(5))
            squared = 5

        # Simplify sqrt(squared) = k*sqrt(r)
        k, r = _squarefree_part(squared)

        sx = rng.choice([1, -1])
        sy = rng.choice([1, -1])
        x1 = rng.randint(olo, ohi)
        y1 = rng.randint(olo, ohi)
        x2 = x1 + sx * a
        y2 = y1 + sy * b
        dx = x2 - x1
        dy = y2 - y1

        answer_inner = _sqrt_latex(k, r)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x1, y1, x2, y2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the exact distance between the points $({x1}, {y1})$ and $({x2}, {y2})$. "
                "Leave your answer in simplified radical form."
            ),
            answer_latex=f"$d = {answer_inner}$",
            hints=[
                r"Distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
                f"Compute $x_2 - x_1 = {dx}$ and $y_2 - y_1 = {dy}$.",
                f"Add the squares: ${dx}^2 + {dy}^2 = {squared}$.",
                "Then simplify $\\sqrt{" f"{squared}" "}$ by pulling out any perfect-square factor.",
            ],
            solution_steps_latex=[
                r"Apply the distance formula $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
                f"Substitute: $d = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}} = \\sqrt{{{dx}^2 + {dy}^2}}$.",
                f"Compute inside: ${dx * dx} + {dy * dy} = {squared}$.",
                f"Simplify the radical: $\\sqrt{{{squared}}} = {answer_inner}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-analytic-geometry", "#skill-formula-substitution"],
        )


@register
class DistanceCheckRightTriangle(Generator):
    """Given three points, compute side lengths and test whether it is right.

    Backward construction:
      - With probability 1/2, build a right triangle using a Pythagorean triple
        placed with legs along the axes at a random origin.
      - Otherwise, perturb one vertex by (+1, +1) so that the triangle is no
        longer right (verified by the Pythagorean converse).
    """
    generator_id = "distance_check_right_triangle"
    topic_slug = "the_distance_formula"
    display_name = "Check if three points form a right triangle"
    bank_count_per_difficulty = 30

    _ORIGIN_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ORIGIN_RANGES[difficulty]
        make_right = rng.random() < 0.5

        attempts = 0
        while True:
            attempts += 1
            a, b, c = rng.choice(_TRIPLES)
            ox = rng.randint(lo, hi)
            oy = rng.randint(lo, hi)
            # Base right triangle at (ox, oy), (ox + a, oy), (ox, oy + b)
            p1 = (ox, oy)
            p2 = (ox + a, oy)
            p3 = (ox, oy + b)
            if not make_right:
                # Perturb p3 so it's not a right triangle and none are degenerate.
                p3 = (ox + rng.choice([1, -1]), oy + b + rng.choice([1, -1]))

            # Compute side lengths squared
            def d2(pa, pb):
                return (pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2

            s1_sq = d2(p1, p2)
            s2_sq = d2(p2, p3)
            s3_sq = d2(p1, p3)
            sq_sides = sorted([s1_sq, s2_sq, s3_sq])
            if 0 in sq_sides:
                continue  # degenerate
            is_right = sq_sides[0] + sq_sides[1] == sq_sides[2]
            if is_right == make_right:
                break
            if attempts > 40:
                # Give up cleanly on this attempt; caller will retry with a new seed.
                break

        answer = "right triangle" if is_right else "not a right triangle"

        # Simplified LaTeX for each side using _squarefree_part.
        def side_latex(sq: int) -> str:
            k, r = _squarefree_part(sq)
            return _sqrt_latex(k, r)

        s1_latex = side_latex(s1_sq)
        s2_latex = side_latex(s2_sq)
        s3_latex = side_latex(s3_sq)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p1, p2, p3)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given the points $A{p1}$, $B{p2}$, and $C{p3}$, determine whether triangle $ABC$ is a right triangle."
            ),
            answer_latex=answer,
            hints=[
                r"Compute each side length using the distance formula $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
                "Square each side length (you can compare squared lengths directly, which avoids radicals).",
                r"Test the Pythagorean converse: a triangle is right if and only if the two smaller squared side lengths sum to the largest.",
            ],
            solution_steps_latex=[
                f"Side $AB$: squared length is ${s1_sq}$, so $|AB| = {s1_latex}$.",
                f"Side $BC$: squared length is ${s2_sq}$, so $|BC| = {s2_latex}$.",
                f"Side $AC$: squared length is ${s3_sq}$, so $|AC| = {s3_latex}$.",
                (
                    f"Check: ${sq_sides[0]} + {sq_sides[1]} = {sq_sides[0] + sq_sides[1]}$ "
                    f"{'=' if is_right else '\\ne'} ${sq_sides[2]}$, so the triangle is {answer}."
                ),
            ],
            tags=["#branch-pre-algebra", "#topic-analytic-geometry", "#skill-procedural-calculation"],
        )
