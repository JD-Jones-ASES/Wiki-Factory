"""Exponent rule generators (Phase 2c Wave 3).

Canonical topic slug ``properties_of_exponents`` at
wiki/topics/algebra/Properties_Of_Exponents.md (Algebra I Ch 6.1).

- exponent_product_rule: x^a * x^b = x^(a+b)
- exponent_quotient_rule: x^a / x^b = x^(a-b)
- exponent_power_rule: (x^a)^b = x^(a*b)
- exponent_power_of_product: (xy)^n = x^n y^n
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


def _fmt_power(base: str, exp: int) -> str:
    """Render base^exp in LaTeX, dropping the exponent if 1 and the whole thing if 0."""
    if exp == 0:
        return "1"
    if exp == 1:
        return base
    return f"{base}^{{{exp}}}"


# ---------------------------------------------------------------------------

@register
class ExponentProductRule(Generator):
    """Simplify x^a * x^b = x^(a+b)."""
    generator_id = "exponent_product_rule"
    topic_slug = "properties_of_exponents"
    display_name = "Simplify x^a * x^b"

    _RANGES = {"easy": (1, 7), "medium": (1, 12), "hard": (1, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        base = rng.choice(["x", "y", "a", "b", "t"])

        statement = f"{_fmt_power(base, a)} \\cdot {_fmt_power(base, b)}"
        result = a + b
        answer = _fmt_power(base, result)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Product rule: $x^a \cdot x^b = x^{a+b}$. When multiplying powers with the same base, add the exponents.",
                f"Add the exponents: ${a} + {b} = {result}$.",
            ],
            solution_steps_latex=[
                r"Apply the product rule: $x^a \cdot x^b = x^{a+b}$.",
                f"${_fmt_power(base, a)} \\cdot {_fmt_power(base, b)} = {_fmt_power(base, a)}^{{{a}+{b}}} = {answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-formula-substitution"],
        )


@register
class ExponentQuotientRule(Generator):
    """Simplify x^a / x^b = x^(a-b)."""
    generator_id = "exponent_quotient_rule"
    topic_slug = "properties_of_exponents"
    display_name = "Simplify x^a / x^b"

    _RANGES = {"easy": (1, 9), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        # Ensure a > b on easy/medium so answer is a positive power; allow any on hard
        if difficulty != "hard" and b >= a:
            a, b = b + 1, a
        base = rng.choice(["x", "y", "a", "b"])
        result = a - b
        answer = _fmt_power(base, result) if result >= 0 else f"\\dfrac{{1}}{{{_fmt_power(base, -result)}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                rf"Simplify $\dfrac{{{_fmt_power(base, a)}}}{{{_fmt_power(base, b)}}}$. "
                "Leave your answer with only positive exponents."
            ),
            answer_latex=f"${answer}$",
            hints=[
                r"Quotient rule: $\dfrac{x^a}{x^b} = x^{a-b}$. Subtract the exponent on the bottom from the exponent on the top.",
                f"Subtract: ${a} - {b} = {result}$.",
                "If the result is negative, rewrite with a positive exponent in the denominator.",
            ],
            solution_steps_latex=[
                r"Apply the quotient rule: $\dfrac{x^a}{x^b} = x^{a-b}$.",
                f"Subtract exponents: ${a} - {b} = {result}$.",
                f"The simplified form is ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-formula-substitution"],
        )


@register
class ExponentPowerRule(Generator):
    """Simplify (x^a)^b = x^(a*b)."""
    generator_id = "exponent_power_rule"
    topic_slug = "properties_of_exponents"
    display_name = "Simplify (x^a)^b"

    _RANGES = {"easy": (2, 6), "medium": (2, 8), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        base = rng.choice(["x", "y", "a", "b", "t"])

        statement = f"\\left({_fmt_power(base, a)}\\right)^{{{b}}}"
        result = a * b
        answer = _fmt_power(base, result)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Power of a power rule: $(x^a)^b = x^{a \cdot b}$. When raising a power to another power, multiply the exponents.",
                f"Multiply: ${a} \\cdot {b} = {result}$.",
            ],
            solution_steps_latex=[
                r"Apply the power rule: $(x^a)^b = x^{ab}$.",
                f"Multiply the exponents: ${a} \\cdot {b} = {result}$.",
                f"Simplified: ${answer}$.",
            ],
            tags=["#branch-algebra-1", "#topic-exponents-and-radicals", "#skill-formula-substitution"],
        )
