"""Percent application generators (Phase 2c Wave B).

Canonical topic slug ``percent_applications``.

- percent_change_with_algebra: net percent change after a p% increase
  followed by a q% decrease.
- sales_tax_or_tip_algebra: solve algebraically for the pre-tax or pre-tip
  amount given the total and the rate.
- word_problem_two_step_percent: chained percent operations
  (markup, then markdown, etc.).
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------


def _fmt_money(value: Fraction, unit: str = "dollars") -> str:
    """Render a money amount with 2-decimal precision if needed."""
    if value.denominator == 1:
        return f"${int(value)}$ {unit}"
    # Two decimals
    val = float(value)
    return f"${val:.2f}$ {unit}"


def _fmt_percent(value: Fraction) -> str:
    """Render a percent as either integer or 1-decimal."""
    if value.denominator == 1:
        return f"{int(value)}\\%"
    val = float(value)
    if abs(val - round(val, 1)) < 1e-9:
        return f"{val:.1f}\\%"
    return f"{val:.2f}\\%"


@register
class PercentChangeWithAlgebra(Generator):
    """Net percent change: start X, increase by p%, then decrease by q%.

    Backward: pick integer p and q (each multiples of 5) so the net change
    is a clean rational number.
    """
    generator_id = "percent_change_with_algebra"
    topic_slug = "percent_applications"
    display_name = "Net percent change after two successive changes"

    _P = {"easy": [10, 15, 20, 25], "medium": [10, 15, 20, 25, 30, 40], "hard": [15, 20, 25, 30, 40, 50]}
    _Q = {"easy": [10, 15, 20, 25], "medium": [10, 15, 20, 25, 30, 40], "hard": [15, 20, 25, 30, 40, 50]}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        p_pct = rng.choice(self._P[difficulty])
        q_pct = rng.choice(self._Q[difficulty])

        # Net multiplier: (1 + p/100)(1 - q/100)
        p_frac = Fraction(p_pct, 100)
        q_frac = Fraction(q_pct, 100)
        net_mult = (1 + p_frac) * (1 - q_frac)
        net_change_frac = net_mult - 1  # positive -> increase, negative -> decrease
        net_pct = net_change_frac * 100

        scenarios = [
            ("Maya", "a subscription box"),
            ("Kai", "a ticket to the school pep rally"),
            ("Priya", "a photography class supply kit"),
            ("Rohan", "a maker space monthly pass"),
            ("Zoe", "a farmer's market tote bag"),
        ]
        who, item = rng.choice(scenarios)

        statement = (
            f"{who} tracks the price of {item} across two changes. "
            f"First the price goes **up** by ${p_pct}\\%$; then the new price "
            f"goes **down** by ${q_pct}\\%$. Express the overall percent "
            f"change from the original price as a single percent."
        )

        if net_pct >= 0:
            direction = "increase"
            magnitude = net_pct
        else:
            direction = "decrease"
            magnitude = -net_pct

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p_pct, q_pct)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=(
                f"Net ${_fmt_percent(magnitude)}$ {direction}"
            ),
            hints=[
                "Represent successive percent changes as multiplication of the corresponding factors applied to the original price.",
                f"An increase of ${p_pct}\\%$ multiplies by $1 + \\dfrac{{{p_pct}}}{{100}}$; a decrease of ${q_pct}\\%$ multiplies by $1 - \\dfrac{{{q_pct}}}{{100}}$.",
                f"Multiply the two factors, then subtract $1$ and convert back to a percent.",
            ],
            solution_steps_latex=[
                f"Let the original price be $P$. After the first change: $P \\cdot \\left(1 + \\dfrac{{{p_pct}}}{{100}}\\right)$.",
                f"After the second change: $P \\cdot \\left(1 + \\dfrac{{{p_pct}}}{{100}}\\right)\\left(1 - \\dfrac{{{q_pct}}}{{100}}\\right)$.",
                f"Simplify the product of the two factors: ${net_mult}$.",
                f"Subtract $1$ and convert to a percent: ${_fmt_percent(net_pct)}$ (a {direction}).",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-proportional-reasoning",
            ],
        )


@register
class SalesTaxOrTipAlgebra(Generator):
    """Given a total that includes tax/tip and the rate, solve for the pre-tax
    amount algebraically.

    Backward: pick the pre-tax amount $P$ (an integer number of dollars) and
    the tax rate $r$ (as an integer percent that gives a clean total).
    """
    generator_id = "sales_tax_or_tip_algebra"
    topic_slug = "percent_applications"
    display_name = "Solve for the pre-tax amount given total + rate"

    _P = {"easy": (10, 60), "medium": (15, 150), "hard": (20, 300)}
    # Rates chosen so total is often a clean dollar amount.
    _R = {"easy": [5, 10, 20, 25], "medium": [5, 6, 8, 10, 15, 20, 25], "hard": [4, 5, 6, 8, 10, 12, 15, 20, 25]}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        p_lo, p_hi = self._P[difficulty]
        rate = rng.choice(self._R[difficulty])
        pre_tax = rng.randint(p_lo, p_hi)
        rate_frac = Fraction(rate, 100)
        total = Fraction(pre_tax) * (1 + rate_frac)

        scenarios = [
            ("Mateo", "at a farmer's market", "sales tax", "meal"),
            ("Leilani", "after a maker space workshop", "service fee", "workshop fee"),
            ("Priya", "at a school pep rally concession", "sales tax", "food order"),
            ("Emilia", "after a photography class supply run", "sales tax", "supplies"),
            ("Kai", "at a community garden plant sale", "sales tax", "plant order"),
        ]
        who, where, label, item = rng.choice(scenarios)

        statement = (
            f"{who} pays {_fmt_money(total)} total {where}, which includes a "
            f"${rate}\\%$ {label} on top of the price of the {item}. "
            f"Compute the price of the {item} before the {label}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (pre_tax, rate),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${pre_tax}$ dollars",
            hints=[
                "Let $P$ be the pre-tax price. The total equals $P$ plus ${rate}\\%$ of $P$.",
                r"Write the equation: $P \cdot \left(1 + \dfrac{r}{100}\right) = \text{total}$.",
                f"Here $1 + \\dfrac{{{rate}}}{{100}} = {1 + rate_frac}$. Divide the total by this factor to get $P$.",
            ],
            solution_steps_latex=[
                f"Let $P$ be the pre-tax amount. Set up the equation: $P \\cdot \\left(1 + \\dfrac{{{rate}}}{{100}}\\right) = {total}$.",
                f"Simplify the factor: $1 + \\dfrac{{{rate}}}{{100}} = {1 + rate_frac}$.",
                f"Divide both sides by ${1 + rate_frac}$: $P = \\dfrac{{{total}}}{{{1 + rate_frac}}} = {pre_tax}$.",
                f"The pre-tax amount is ${pre_tax}$ dollars.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-proportional-reasoning",
            ],
        )


@register
class WordProblemTwoStepPercent(Generator):
    """Original price -> p% markup -> q% discount -> final price.

    Backward: pick an integer original price, integer p (markup), and integer
    q (discount) so all arithmetic is clean.
    """
    generator_id = "word_problem_two_step_percent"
    topic_slug = "percent_applications"
    display_name = "Chained markup and markdown"

    _P0 = {"easy": (20, 60), "medium": (30, 120), "hard": (40, 250)}
    _M = {"easy": [10, 20, 25], "medium": [10, 15, 20, 25, 30, 40], "hard": [10, 15, 20, 25, 30, 40, 50]}
    _D = {"easy": [10, 20, 25], "medium": [10, 15, 20, 25, 30, 40], "hard": [10, 15, 20, 25, 30, 40, 50]}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        p0_lo, p0_hi = self._P0[difficulty]
        p0 = rng.randint(p0_lo, p0_hi)
        markup = rng.choice(self._M[difficulty])
        discount = rng.choice(self._D[difficulty])

        marked_up = Fraction(p0) * (1 + Fraction(markup, 100))
        final = marked_up * (1 - Fraction(discount, 100))

        scenarios = [
            (
                "Emilia",
                "a handmade bookshelf",
                "the community craft fair",
            ),
            (
                "Rohan",
                "a screen-printed tote",
                "a maker space showcase",
            ),
            (
                "Zoe",
                "a matted photo print",
                "a photography class pop-up shop",
            ),
            (
                "Mateo",
                "a basil seedling tray",
                "a community garden sale",
            ),
            (
                "Leilani",
                "a paper sculpture",
                "a school art night",
            ),
        ]
        who, item, event = rng.choice(scenarios)

        statement = (
            f"{who} lists {item} for ${p0}$ dollars at {event}. Before the "
            f"event, the price is **raised** by ${markup}\\%$; at the end of "
            f"the day, the new price is **discounted** by ${discount}\\%$. "
            f"Find the final selling price."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (p0, markup, discount),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=_fmt_money(final),
            hints=[
                "Chain the two percent changes: multiply the original price by $(1 + \\text{markup}/100)$ first, then by $(1 - \\text{discount}/100)$.",
                f"After the markup: ${p0} \\cdot \\left(1 + \\dfrac{{{markup}}}{{100}}\\right) = {marked_up}$.",
                f"Then apply the discount: multiply by $1 - \\dfrac{{{discount}}}{{100}}$.",
            ],
            solution_steps_latex=[
                f"Start price: ${p0}$ dollars.",
                f"Apply the markup: ${p0} \\cdot \\left(1 + \\dfrac{{{markup}}}{{100}}\\right) = {marked_up}$.",
                f"Apply the discount: ${marked_up} \\cdot \\left(1 - \\dfrac{{{discount}}}{{100}}\\right) = {final}$.",
                f"Final price: {_fmt_money(final)}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-proportional-reasoning",
            ],
        )
