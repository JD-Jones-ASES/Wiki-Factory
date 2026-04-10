"""Percent generators (Phase 2c Wave 1).

Canonical topic slug ``finding_a_percent_of_a_number`` at
wiki/topics/pre_algebra/Finding_A_Percent_Of_A_Number.md (Math I Ch 7.3).

- percent_of_number: Find p% of n.
- percent_one_is_of_other: x is what percent of y?
- percent_find_whole: x is p% of what?

All generators keep answers clean (integer or single-decimal) by
constructing problems backward from a known result.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


_EASY_PERCENTS = (5, 10, 20, 25, 50, 75)
_MEDIUM_PERCENTS = (5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80, 90)
_HARD_PERCENTS = (2, 3, 5, 8, 12, 15, 18, 22, 28, 35, 42, 55, 65, 85, 95)


def _percents_for(difficulty: Difficulty) -> tuple[int, ...]:
    return {"easy": _EASY_PERCENTS, "medium": _MEDIUM_PERCENTS, "hard": _HARD_PERCENTS}[difficulty]


# ---------------------------------------------------------------------------

@register
class PercentOfNumber(Generator):
    """Find p% of n. Clean answers by requiring p * n divisible by 100."""
    generator_id = "percent_of_number"
    topic_slug = "finding_a_percent_of_a_number"
    display_name = "Find p% of a number"

    _N_RANGES = {"easy": (10, 200), "medium": (20, 600), "hard": (50, 1500)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._N_RANGES[difficulty]
        percents = _percents_for(difficulty)
        # Construct n so p*n is divisible by 100 for clean answer
        while True:
            p = rng.choice(percents)
            n = rng.randint(lo, hi)
            # Round n to a multiple of 100 / gcd(p, 100) so answer is clean
            import math as _math

            step = 100 // _math.gcd(p, 100)
            n = (n // step) * step
            if n < lo:
                n = step
            result = p * n // 100
            if result > 0:
                break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find ${p}\\%$ of ${n}$.",
            answer_latex=f"${result}$",
            hints=[
                f"Convert ${p}\\%$ to a decimal: ${p}\\% = 0.{p:02d}$ (drop the percent sign, divide by $100$).",
                f"Multiply: $0.{p:02d} \\times {n}$.",
                rf"Equivalently: $\dfrac{{{p}}}{{100}} \times {n} = \dfrac{{{p * n}}}{{100}} = {result}$.",
            ],
            solution_steps_latex=[
                rf"Rewrite the percent as a fraction: ${p}\% = \dfrac{{{p}}}{{100}}$.",
                rf"Multiply by ${n}$: $\dfrac{{{p}}}{{100}} \times {n} = \dfrac{{{p * n}}}{{100}}$.",
                f"Simplify: ${result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-formula-substitution"],
        )


@register
class PercentOneIsOfOther(Generator):
    """x is what percent of y? Construct backward so answer is a clean integer percent."""
    generator_id = "percent_one_is_of_other"
    topic_slug = "finding_a_percent_of_a_number"
    display_name = "x is what percent of y?"

    _Y_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._Y_RANGES[difficulty]
        percents = _percents_for(difficulty)
        import math as _math

        while True:
            p = rng.choice(percents)
            y = rng.randint(lo, hi)
            step = 100 // _math.gcd(p, 100)
            y = (y // step) * step
            if y < lo:
                y = step
            x = p * y // 100
            if x > 0:
                break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${x}$ is what percent of ${y}$?",
            answer_latex=f"${p}\\%$",
            hints=[
                r"Use the relation $\text{part} = \text{percent} \times \text{whole}$, so $\text{percent} = \dfrac{\text{part}}{\text{whole}}$.",
                rf"$\dfrac{{{x}}}{{{y}}} = {x / y:.4f}$",
                f"Multiply by $100$ and add the $\\%$ symbol: ${p}\\%$.",
            ],
            solution_steps_latex=[
                rf"Set up $\dfrac{{\text{{part}}}}{{\text{{whole}}}} = \dfrac{{{x}}}{{{y}}}$.",
                rf"Simplify the fraction: $\dfrac{{{x}}}{{{y}}} = \dfrac{{{p}}}{{100}}$.",
                f"Convert to a percent: ${p}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )


@register
class PercentFindWhole(Generator):
    """x is p% of what number? Answer = 100*x/p, kept as an integer."""
    generator_id = "percent_find_whole"
    topic_slug = "finding_a_percent_of_a_number"
    display_name = "x is p% of what number?"

    _WHOLE_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._WHOLE_RANGES[difficulty]
        percents = _percents_for(difficulty)
        import math as _math

        while True:
            p = rng.choice(percents)
            whole = rng.randint(lo, hi)
            step = 100 // _math.gcd(p, 100)
            whole = (whole // step) * step
            if whole < lo:
                whole = step
            x = p * whole // 100
            if x > 0:
                break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, p)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${x}$ is ${p}\\%$ of what number?",
            answer_latex=f"${whole}$",
            hints=[
                r"Use $\text{part} = \text{percent} \times \text{whole}$.",
                rf"Rewrite ${p}\%$ as $\dfrac{{{p}}}{{100}}$ and call the whole $w$: ${x} = \dfrac{{{p}}}{{100}} \cdot w$.",
                rf"Solve for $w$: $w = {x} \cdot \dfrac{{100}}{{{p}}} = {whole}$.",
            ],
            solution_steps_latex=[
                rf"Translate: ${x} = \dfrac{{{p}}}{{100}} \cdot w$.",
                rf"Multiply both sides by $\dfrac{{100}}{{{p}}}$: $w = {x} \cdot \dfrac{{100}}{{{p}}} = \dfrac{{{100 * x}}}{{{p}}}$.",
                f"Simplify: $w = {whole}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )
