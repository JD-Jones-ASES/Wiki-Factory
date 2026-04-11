"""Product, power, and quotient rules for exponents (pre-algebra level).

Canonical topic slug ``product_power_and_quotient_rules`` at
wiki/topics/pre_algebra/Product_Power_And_Quotient_Rules.md.

- product_rule_single_base: $x^a \\cdot x^b = x^{a+b}$
- power_rule_single_base: $(x^a)^b = x^{ab}$
- quotient_rule_single_base: $\\dfrac{x^a}{x^b} = x^{a-b}$ with $a > b$

All three generators work over a common pool of base-variables and
positive-integer exponents. Backward construction: pick the answer's
exponent or target exponent first, then realise the operands.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "product_power_and_quotient_rules"

_BASES = ("x", "y", "m", "a", "p")

_TAGS = [
    "#branch-pre-algebra",
    "#topic-exponents-and-radicals",
    "#skill-algebraic-manipulation",
]


def _power_latex(base: str, exponent: int) -> str:
    """Render a single-base power, collapsing to the bare base when $n=1$."""
    if exponent == 1:
        return base
    return f"{base}^{{{exponent}}}"


# ---------------------------------------------------------------------------

@register
class ProductRuleSingleBase(Generator):
    """Simplify $x^a \\cdot x^b$ using the product rule."""
    generator_id = "product_rule_single_base"
    topic_slug = TOPIC_SLUG
    display_name = "Simplify a product of powers with the same base"

    _RANGES = {
        "easy":   {"a": (1, 6),  "b": (1, 6)},   # 5 bases * 36 = 180
        "medium": {"a": (2, 10), "b": (2, 10)},  # 5 * 81 = 405
        "hard":   {"a": (3, 14), "b": (3, 14)},  # 5 * 144 = 720
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        base = rng.choice(_BASES)
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        total = a + b

        left_latex = _power_latex(base, a)
        right_latex = _power_latex(base, b)
        answer = _power_latex(base, total)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${left_latex} \\cdot {right_latex}$.",
            answer_latex=f"${answer}$",
            hints=[
                (
                    r"When multiplying powers with the same base, keep the "
                    r"base and **add** the exponents: "
                    r"$x^m \cdot x^n = x^{m+n}$."
                ),
                f"Here the common base is ${base}$, with exponents ${a}$ and ${b}$.",
                f"Add the exponents: ${a} + {b} = {total}$.",
            ],
            solution_steps_latex=[
                (
                    r"Apply the product rule for exponents: "
                    r"$x^m \cdot x^n = x^{m+n}$."
                ),
                f"Add the exponents: ${a} + {b} = {total}$.",
                f"Therefore ${left_latex} \\cdot {right_latex} = {answer}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class PowerRuleSingleBase(Generator):
    """Simplify $(x^a)^b$ using the power-of-a-power rule."""
    generator_id = "power_rule_single_base"
    topic_slug = TOPIC_SLUG
    display_name = "Simplify a power raised to a power"

    _RANGES = {
        "easy":   {"a": (2, 6),  "b": (2, 5)},   # 5 * 20 = 100
        "medium": {"a": (2, 9),  "b": (2, 7)},   # 5 * 48 = 240
        "hard":   {"a": (2, 12), "b": (2, 9)},   # 5 * 88 = 440
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        base = rng.choice(_BASES)
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        product = a * b

        inner_latex = _power_latex(base, a)
        answer = _power_latex(base, product)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify $({inner_latex})^{{{b}}}$.",
            answer_latex=f"${answer}$",
            hints=[
                (
                    r"When raising a power to another power, keep the base "
                    r"and **multiply** the exponents: $(x^m)^n = x^{mn}$."
                ),
                f"Here the base is ${base}$ with inner exponent ${a}$ and outer exponent ${b}$.",
                f"Multiply the exponents: ${a} \\cdot {b} = {product}$.",
            ],
            solution_steps_latex=[
                (
                    r"Apply the power-of-a-power rule: "
                    r"$(x^m)^n = x^{mn}$."
                ),
                f"Multiply the exponents: ${a} \\cdot {b} = {product}$.",
                f"Therefore $({inner_latex})^{{{b}}} = {answer}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class QuotientRuleSingleBase(Generator):
    """Simplify $\\dfrac{x^a}{x^b}$ with $a > b$ using the quotient rule."""
    generator_id = "quotient_rule_single_base"
    topic_slug = TOPIC_SLUG
    display_name = "Simplify a quotient of powers with the same base"

    # diff = a - b is the answer exponent; pick diff and b, then a = b + diff.
    _RANGES = {
        "easy":   {"diff": (1, 5),  "b": (1, 6)},   # 5 bases * 30 = 150
        "medium": {"diff": (2, 8),  "b": (2, 9)},   # 5 * 56 = 280
        "hard":   {"diff": (3, 11), "b": (3, 12)},  # 5 * 90 = 450
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        base = rng.choice(_BASES)
        diff = rng.randint(*r["diff"])
        b = rng.randint(*r["b"])
        a = b + diff  # ensures a > b strictly

        top_latex = _power_latex(base, a)
        bot_latex = _power_latex(base, b)
        answer = _power_latex(base, diff)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (base, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify $\\dfrac{{{top_latex}}}{{{bot_latex}}}$.",
            answer_latex=f"${answer}$",
            hints=[
                (
                    r"When dividing powers with the same base, keep the base "
                    r"and **subtract** the exponents: "
                    r"$\dfrac{x^m}{x^n} = x^{m-n}$."
                ),
                f"Here the common base is ${base}$, with exponents ${a}$ on top and ${b}$ on bottom.",
                f"Subtract the exponents: ${a} - {b} = {diff}$.",
            ],
            solution_steps_latex=[
                (
                    r"Apply the quotient rule for exponents: "
                    r"$\dfrac{x^m}{x^n} = x^{m-n}$."
                ),
                f"Subtract the exponents: ${a} - {b} = {diff}$.",
                f"Therefore $\\dfrac{{{top_latex}}}{{{bot_latex}}} = {answer}$.",
            ],
            tags=list(_TAGS),
        )
