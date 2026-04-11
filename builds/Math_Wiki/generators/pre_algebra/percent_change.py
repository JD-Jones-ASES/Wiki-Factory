"""Percent increase/decrease generators (Phase 2c Wave 2).

Canonical topic slug ``percent_increase_and_decrease`` at
wiki/topics/pre_algebra/Percent_Increase_And_Decrease.md (covered by both
Math I and Math II -- a 2x source topic).

- percent_change_find_percent: given old and new, find the percent change
- percent_change_find_new_value: given old and percent change, find the new value
- percent_change_find_original: given new value and percent change, find the original
"""
from __future__ import annotations

import random
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Percent change values that produce clean results when paired with compatible bases.
_PERCENT_CHOICES = {
    "easy": (5, 10, 20, 25, 50, 75),
    "medium": (5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80),
    "hard": (4, 6, 8, 12, 15, 18, 22, 25, 28, 35, 45, 55, 65, 85),
}


def _compatible_old(percent: int, rng: random.Random, base_range: tuple[int, int]) -> int:
    """Return an 'old' value divisible by (100 / gcd(percent, 100)) so the change is integer."""
    step = 100 // gcd(percent, 100)
    lo, hi = base_range
    lo = max(lo, step)
    # Multiples of step within [lo, hi]
    count = (hi - lo) // step + 1
    k = rng.randint(0, max(0, count - 1))
    return lo + k * step


# ---------------------------------------------------------------------------

@register
class PercentChangeFindPercent(Generator):
    """Given old and new values, find the percent change (with direction)."""
    generator_id = "percent_change_find_percent"
    topic_slug = "percent_increase_and_decrease"
    display_name = "Find the percent change"

    _OLD_RANGE = {"easy": (20, 200), "medium": (40, 500), "hard": (60, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        percent = rng.choice(_PERCENT_CHOICES[difficulty])
        direction = rng.choice(["increase", "decrease"])
        old_value = _compatible_old(percent, rng, self._OLD_RANGE[difficulty])
        delta = old_value * percent // 100
        new_value = old_value + delta if direction == "increase" else old_value - delta

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (old_value, new_value)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A value changes from ${old_value}$ to ${new_value}$. "
                "What is the percent change? State whether it is an increase or a decrease."
            ),
            answer_latex=f"${percent}\\%$ {direction}",
            hints=[
                r"Percent change formula: $\dfrac{\text{new} - \text{old}}{\text{old}} \times 100\%$. A positive result is an increase, negative is a decrease.",
                f"Compute the difference: ${new_value} - {old_value} = {new_value - old_value}$.",
                rf"Divide by the old value: $\dfrac{{{new_value - old_value}}}{{{old_value}}} = {(new_value - old_value) / old_value:.4f}$. Multiply by $100\%$.",
            ],
            solution_steps_latex=[
                rf"Apply the percent change formula: $\dfrac{{{new_value} - {old_value}}}{{{old_value}}}$.",
                rf"Compute: $\dfrac{{{new_value - old_value}}}{{{old_value}}}$.",
                f"Multiply by $100\\%$: ${percent}\\%$ (and the sign says {direction}).",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-multi-step"],
        )


@register
class PercentChangeFindNewValue(Generator):
    """Given old value and percent change, find the new value."""
    generator_id = "percent_change_find_new_value"
    topic_slug = "percent_increase_and_decrease"
    display_name = "Find the new value after a percent change"

    _OLD_RANGE = {"easy": (20, 200), "medium": (40, 500), "hard": (60, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        percent = rng.choice(_PERCENT_CHOICES[difficulty])
        direction = rng.choice(["increase", "decrease"])
        old_value = _compatible_old(percent, rng, self._OLD_RANGE[difficulty])
        delta = old_value * percent // 100
        new_value = old_value + delta if direction == "increase" else old_value - delta

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (old_value, percent, direction)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A value of ${old_value}$ {direction}s by ${percent}\\%$. "
                "What is the new value?"
            ),
            answer_latex=f"${new_value}$",
            hints=[
                f"Compute the change: ${percent}\\%$ of ${old_value}$ is ${delta}$.",
                f"For an increase, add. For a decrease, subtract.",
                f"${old_value} {'+' if direction == 'increase' else '-'} {delta} = {new_value}$.",
            ],
            solution_steps_latex=[
                rf"Compute the change: $\dfrac{{{percent}}}{{100}} \cdot {old_value} = {delta}$.",
                f"{'Add' if direction == 'increase' else 'Subtract'} the change {'to' if direction == 'increase' else 'from'} the original: "
                f"${old_value} {'+' if direction == 'increase' else '-'} {delta} = {new_value}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-formula-substitution"],
        )


@register
class PercentChangeFindOriginal(Generator):
    """Given new value and percent change, find the original value."""
    generator_id = "percent_change_find_original"
    topic_slug = "percent_increase_and_decrease"
    display_name = "Find the original value from a percent change"

    _OLD_RANGE = {"easy": (20, 200), "medium": (40, 500), "hard": (60, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        percent = rng.choice(_PERCENT_CHOICES[difficulty])
        direction = rng.choice(["increase", "decrease"])
        old_value = _compatible_old(percent, rng, self._OLD_RANGE[difficulty])
        delta = old_value * percent // 100
        new_value = old_value + delta if direction == "increase" else old_value - delta

        if direction == "increase":
            factor_description = f"100\\% + {percent}\\% = {100 + percent}\\%"
            factor = 100 + percent
        else:
            factor_description = f"100\\% - {percent}\\% = {100 - percent}\\%"
            factor = 100 - percent

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (new_value, percent, direction)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"After {'an' if direction == 'increase' else 'a'} {percent}\\% {direction}, a value is now ${new_value}$. "
                "What was the original value?"
            ),
            answer_latex=f"${old_value}$",
            hints=[
                rf"After a {percent}\% {direction}, the new value is {factor_description} of the original.",
                rf"So $\text{{new}} = \dfrac{{{factor}}}{{100}} \cdot \text{{original}}$.",
                rf"Solve for the original: $\text{{original}} = \text{{new}} \cdot \dfrac{{100}}{{{factor}}}$.",
            ],
            solution_steps_latex=[
                rf"Set up the equation: ${new_value} = \dfrac{{{factor}}}{{100}} \cdot \text{{original}}$.",
                rf"Solve: $\text{{original}} = {new_value} \cdot \dfrac{{100}}{{{factor}}} = \dfrac{{{100 * new_value}}}{{{factor}}}$.",
                f"Simplify: $\\text{{original}} = {old_value}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Applications: tax, tip, discount, and simple interest
# (topic_slug: applications_tax_tip_discount_and_simple_interest)
# ===========================================================================


# Fresh names and locations so the wording never touches textbook verbatim.
_TIP_SCENARIOS = (
    ("A meal at Blue Heron Bistro", "leave a tip of"),
    ("Dinner at the Foxglove Diner", "add a tip of"),
    ("A lunch order at Mavis Street Cafe", "leave a tip of"),
    ("A brunch tab at the Red Kestrel Lounge", "add a gratuity of"),
)
_TAX_SCENARIOS = (
    ("A new backpack at Ridgewater Outfitters", "charge a sales tax of"),
    ("A board game at Ember Park Games", "apply a sales tax of"),
    ("A guitar stand at Willow Bend Music", "add a sales tax of"),
    ("A notebook at Olmstead Stationery", "charge a sales tax of"),
)

_DISCOUNT_SCENARIOS = (
    ("a sweater at Larkspur Knit Co.", "sweater"),
    ("a mountain bike at Driftpine Cycles", "bike"),
    ("a calculator at Corvid Books", "calculator"),
    ("a backpack at Blue Heron Outfitters", "backpack"),
    ("a puzzle at Ember Park Games", "puzzle"),
)

_INTEREST_SCENARIOS = (
    ("A savings account at Ridgewater Credit Union", "deposit"),
    ("A bond held at Foxglove Financial", "investment"),
    ("A certificate of deposit at Willow Bend Bank", "principal"),
    ("A deposit at Olmstead Savings", "deposit"),
)


def _pick_clean_bill(pct: int, rng: random.Random, lo: int, hi: int) -> int:
    """Return a whole-dollar bill in [lo, hi] so pct*bill is divisible by 100."""
    step = 100 // gcd(pct, 100)
    lo_adj = max(lo, step)
    count = (hi - lo_adj) // step + 1
    k = rng.randint(0, max(0, count - 1))
    return lo_adj + k * step


# ---------------------------------------------------------------------------

@register
class SalesTaxOrTip(Generator):
    """Add a tax or tip percentage to a bill and report the total."""
    generator_id = "sales_tax_or_tip"
    topic_slug = "applications_tax_tip_discount_and_simple_interest"
    display_name = "Sales tax or tip total"

    supports_word_problems = True

    _PERCENTS = {
        "easy":   (5, 10, 15, 20),
        "medium": (5, 8, 10, 12, 15, 18, 20),
        "hard":   (4, 6, 7, 8, 9, 11, 13, 15, 17, 22),
    }
    _BILL_RANGES = {"easy": (10, 80), "medium": (20, 200), "hard": (50, 500)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pct = rng.choice(self._PERCENTS[difficulty])
        lo, hi = self._BILL_RANGES[difficulty]
        bill = _pick_clean_bill(pct, rng, lo, hi)
        extra = pct * bill // 100
        total = bill + extra

        scenario_type = rng.choice(["tip", "tax"])
        if scenario_type == "tip":
            location, verb = _TIP_SCENARIOS[rng.randrange(len(_TIP_SCENARIOS))]
            statement = (
                f"{location} costs $\\${bill}$. If the diners {verb} "
                f"${pct}\\%$ of the bill, what is the total paid?"
            )
            label = "tip"
        else:
            location, verb = _TAX_SCENARIOS[rng.randrange(len(_TAX_SCENARIOS))]
            statement = (
                f"{location} is priced at $\\${bill}$. The store must "
                f"{verb} ${pct}\\%$. What is the total amount paid?"
            )
            label = "sales tax"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (bill, pct, scenario_type)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$\\${total}$",
            hints=[
                f"Compute the {label}: ${pct}\\%$ of $\\${bill}$.",
                rf"$\tfrac{{{pct}}}{{100}} \cdot {bill} = {extra}$, so the {label} is $\${extra}$.",
                f"Add the {label} to the bill: $\\${bill} + \\${extra} = \\${total}$.",
            ],
            solution_steps_latex=[
                f"Find ${pct}\\%$ of $\\${bill}$.",
                rf"$\tfrac{{{pct}}}{{100}} \cdot {bill} = \tfrac{{{pct * bill}}}{{100}} = {extra}$.",
                f"Add the {label}: $\\${bill} + \\${extra} = \\${total}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
                "#word-problem-support",
            ],
        )


# ---------------------------------------------------------------------------

@register
class PercentDiscount(Generator):
    """Find the sale price after a percent discount."""
    generator_id = "percent_discount"
    topic_slug = "applications_tax_tip_discount_and_simple_interest"
    display_name = "Sale price after a percent discount"

    supports_word_problems = True

    _PERCENTS = {
        "easy":   (10, 20, 25, 50),
        "medium": (5, 10, 15, 20, 25, 30, 40, 50),
        "hard":   (12, 15, 18, 22, 28, 35, 45, 55, 60, 65),
    }
    _PRICE_RANGES = {"easy": (20, 120), "medium": (30, 300), "hard": (60, 900)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pct = rng.choice(self._PERCENTS[difficulty])
        lo, hi = self._PRICE_RANGES[difficulty]
        original = _pick_clean_bill(pct, rng, lo, hi)
        savings = pct * original // 100
        sale_price = original - savings

        scenario, noun = _DISCOUNT_SCENARIOS[rng.randrange(len(_DISCOUNT_SCENARIOS))]
        statement = (
            f"The original price of {scenario} is $\\${original}$. "
            f"During a sale, the {noun} is marked down by ${pct}\\%$. "
            f"What is the sale price?"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (original, pct)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$\\${sale_price}$",
            hints=[
                rf"First compute the discount: ${pct}\% \cdot \${original}$.",
                rf"The discount is $\${savings}$, so subtract from the original price.",
                f"$\\${original} - \\${savings} = \\${sale_price}$.",
            ],
            solution_steps_latex=[
                rf"Compute the discount amount: $\tfrac{{{pct}}}{{100}} \cdot {original} = {savings}$.",
                f"Subtract the discount from the original price: $\\${original} - \\${savings} = \\${sale_price}$.",
                f"The sale price is $\\${sale_price}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-multi-step",
                "#word-problem-support",
            ],
        )


# ---------------------------------------------------------------------------

@register
class SimpleInterestCalc(Generator):
    """Compute simple interest $I = Prt$ for a principal, rate, and time."""
    generator_id = "simple_interest_calc"
    topic_slug = "applications_tax_tip_discount_and_simple_interest"
    display_name = "Simple interest (I = Prt)"

    supports_word_problems = True

    _RATES = {
        "easy":   (2, 4, 5, 10),
        "medium": (3, 4, 5, 6, 8, 10, 12),
        "hard":   (2, 3, 5, 6, 7, 8, 9, 11, 12, 15),
    }
    _TIMES = {
        "easy":   (1, 2, 3),
        "medium": (1, 2, 3, 4, 5),
        "hard":   (2, 3, 4, 5, 6, 7, 8, 10),
    }
    _PRINCIPAL_RANGES = {
        "easy":   (100, 800),
        "medium": (200, 3000),
        "hard":   (500, 8000),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        rate = rng.choice(self._RATES[difficulty])
        t = rng.choice(self._TIMES[difficulty])
        lo, hi = self._PRINCIPAL_RANGES[difficulty]
        principal = _pick_clean_bill(rate, rng, lo, hi)
        interest = principal * rate * t // 100

        location, noun = _INTEREST_SCENARIOS[rng.randrange(len(_INTEREST_SCENARIOS))]
        year_word = "year" if t == 1 else "years"
        statement = (
            f"{location} holds a {noun} of $\\${principal}$. "
            f"The simple annual interest rate is ${rate}\\%$. "
            f"Find the interest earned after ${t}$ {year_word}."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (principal, rate, t)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$\\${interest}$",
            hints=[
                r"Use the simple interest formula $I = P \cdot r \cdot t$ with $r$ written as a decimal.",
                rf"Substitute: $I = {principal} \cdot \tfrac{{{rate}}}{{100}} \cdot {t}$.",
                rf"Multiply in any order: $I = \${interest}$.",
            ],
            solution_steps_latex=[
                r"Write the simple interest formula: $I = Prt$.",
                rf"Substitute the values: $I = {principal} \cdot \tfrac{{{rate}}}{{100}} \cdot {t}$.",
                rf"Compute: $I = \tfrac{{{principal * rate * t}}}{{100}} = \${interest}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
                "#word-problem-support",
            ],
        )
