"""Unit rate and proportion generators (Phase 2c Wave 3).

Canonical topic slugs:
- ``unit_rates`` at wiki/topics/pre_algebra/Unit_Rates.md
- ``proportions_and_cross_multiplication`` at
  wiki/topics/pre_algebra/Proportions_And_Cross_Multiplication.md

Generators:

unit_rates
    compute_unit_price     "$12 for 4 pounds" -> $3 per pound
    compute_unit_speed     "180 miles in 3 hours" -> 60 mph
    compare_better_buy     Two package options -> which is cheaper per unit

proportions_and_cross_multiplication
    solve_proportion_for_unknown  a/b = c/x (or similar), solve for x
    scale_with_proportion_word    Word-problem scaling with a proportion
    verify_is_proportion          Are a/b and c/d equivalent? Yes/No
"""
from __future__ import annotations

import random
from fractions import Fraction
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


_TAGS = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
]


def _tags_for(difficulty: Difficulty) -> list[str]:
    return [*_TAGS, f"#difficulty-{difficulty}"]


# ---------------------------------------------------------------------------
# Topic 1: unit_rates
# ---------------------------------------------------------------------------


_PRICE_CONTEXTS = (
    ("apples", "pound", "pounds"),
    ("rice", "pound", "pounds"),
    ("bananas", "pound", "pounds"),
    ("cereal", "box", "boxes"),
    ("juice", "bottle", "bottles"),
    ("notebooks", "notebook", "notebooks"),
    ("pencils", "pencil", "pencils"),
    ("yogurt", "cup", "cups"),
)


def _fmt_money(cents: int) -> str:
    """Format a cents amount as a dollar string without currency wrap-up.

    ``cents`` is an integer number of cents. Returns something like
    ``12.00`` (no leading dollar sign, so callers decide how to escape).
    """
    whole, frac = divmod(cents, 100)
    return f"{whole}.{frac:02d}"


@register
class ComputeUnitPrice(Generator):
    """Compute unit price: given total cost and quantity, find price per unit.

    Backward construction: pick unit price (in cents, clean), pick quantity,
    compute total cost. Guarantees the per-unit answer is a clean dollar
    or dollar-and-cents value.
    """
    generator_id = "compute_unit_price"
    topic_slug = "unit_rates"
    display_name = "Compute a unit price"

    # Unit prices are stored in cents to avoid float drift.
    _UNIT_PRICES_CENTS = {
        "easy": (100, 150, 200, 250, 300, 400, 500),       # whole dollars / nice halves
        "medium": (75, 125, 175, 225, 275, 325, 375, 450, 550, 625, 750, 875),
        "hard": (65, 85, 115, 145, 195, 235, 265, 295, 315, 365, 425, 485, 535, 595),
    }
    _QUANTITIES = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (3, 4, 5, 6, 7, 8, 9, 10, 12),
        "hard": (4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        unit_cents = rng.choice(self._UNIT_PRICES_CENTS[difficulty])
        quantity = rng.choice(self._QUANTITIES[difficulty])
        total_cents = unit_cents * quantity
        item, unit_sing, unit_plur = rng.choice(_PRICE_CONTEXTS)
        unit_label = unit_plur if quantity != 1 else unit_sing

        total_str = _fmt_money(total_cents)
        unit_str = _fmt_money(unit_cents)

        statement = (
            f"A bag of {item} costs \\${total_str} for {quantity} {unit_label}. "
            f"What is the unit price per {unit_sing}?"
        )

        answer = f"$\\${unit_str}$ per {unit_sing}"

        hints = [
            (
                "The unit price is the total cost divided by the number of units: "
                f"$\\text{{unit price}} = \\dfrac{{\\text{{total cost}}}}{{\\text{{quantity}}}}$."
            ),
            (
                f"Divide the total by the quantity: "
                f"$\\dfrac{{\\${total_str}}}{{{quantity}}}$."
            ),
            (
                f"This gives $\\${unit_str}$ per {unit_sing}."
            ),
        ]

        steps = [
            (
                f"Set up the division: "
                f"$\\dfrac{{\\${total_str}}}{{{quantity}\\ \\text{{{unit_plur}}}}}$."
            ),
            (
                f"Divide: $\\${total_str} \\div {quantity} = \\${unit_str}$."
            ),
            (
                f"The unit price is $\\${unit_str}$ per {unit_sing}."
            ),
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (unit_cents, quantity, item),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=_tags_for(difficulty),
        )


_SPEED_VEHICLES = (
    ("car", "drives"),
    ("truck", "drives"),
    ("train", "travels"),
    ("cyclist", "rides"),
    ("bus", "travels"),
    ("motorcyclist", "rides"),
)


@register
class ComputeUnitSpeed(Generator):
    """Compute unit speed: distance divided by time, in miles per hour.

    Backward: pick a clean integer speed (mph), pick time in hours, compute
    total distance. Answer is an integer mph.
    """
    generator_id = "compute_unit_speed"
    topic_slug = "unit_rates"
    display_name = "Compute a unit speed"

    _SPEEDS_MPH = {
        "easy": (20, 25, 30, 35, 40, 45, 50, 55, 60),
        "medium": (15, 22, 28, 33, 38, 42, 48, 52, 58, 62, 65, 68, 72, 75),
        "hard": (12, 18, 24, 31, 37, 43, 47, 53, 57, 61, 67, 71, 73, 78, 82, 85, 88, 92),
    }
    _TIMES_HR = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9, 10),
        "hard": (3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        speed = rng.choice(self._SPEEDS_MPH[difficulty])
        time = rng.choice(self._TIMES_HR[difficulty])
        distance = speed * time
        vehicle, verb = rng.choice(_SPEED_VEHICLES)
        hour_label = "hour" if time == 1 else "hours"

        statement = (
            f"A {vehicle} {verb} ${distance}$ miles in ${time}$ {hour_label}. "
            "What is its speed in miles per hour?"
        )

        answer = f"${speed}$ mph"

        hints = [
            (
                r"Speed is distance divided by time: "
                r"$\text{speed} = \dfrac{\text{distance}}{\text{time}}$."
            ),
            (
                f"Divide: $\\dfrac{{{distance} \\text{{ mi}}}}{{{time} \\text{{ hr}}}}$."
            ),
            (
                f"$\\dfrac{{{distance}}}{{{time}}} = {speed}$, so the speed is ${speed}$ mph."
            ),
        ]

        steps = [
            (
                f"Set up the rate: "
                f"$\\dfrac{{{distance} \\text{{ miles}}}}{{{time} \\text{{ hours}}}}$."
            ),
            (
                f"Divide numerator by denominator: "
                f"${distance} \\div {time} = {speed}$."
            ),
            (
                f"The unit speed is ${speed}$ miles per hour."
            ),
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (speed, time, vehicle),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=_tags_for(difficulty),
        )


_BETTER_BUY_CONTEXTS = (
    ("cereal", "oz"),
    ("yogurt", "oz"),
    ("juice", "oz"),
    ("shampoo", "oz"),
    ("rice", "oz"),
    ("chips", "oz"),
    ("soap", "oz"),
    ("coffee", "oz"),
)


@register
class CompareBetterBuy(Generator):
    """Compare two package options and decide which has the lower unit price.

    Backward: pick two distinct unit prices (in cents), pick two quantities,
    compute the two totals. Answer identifies the cheaper package by label.
    """
    generator_id = "compare_better_buy"
    topic_slug = "unit_rates"
    display_name = "Which is the better buy?"

    _UNIT_PRICES_CENTS = {
        "easy": (15, 20, 25, 30, 40, 50),
        "medium": (12, 18, 22, 28, 32, 38, 45, 55),
        "hard": (11, 17, 23, 29, 31, 37, 41, 47, 53, 59, 61, 67),
    }
    _QUANTITIES = {
        "easy": (4, 6, 8, 10, 12, 15, 16, 20),
        "medium": (4, 6, 8, 9, 10, 12, 14, 16, 18, 20, 24),
        "hard": (5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 25, 30),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pool = self._UNIT_PRICES_CENTS[difficulty]
        qpool = self._QUANTITIES[difficulty]
        item, unit = rng.choice(_BETTER_BUY_CONTEXTS)

        # Pick two distinct unit prices; one will be the better buy.
        p1 = rng.choice(pool)
        p2 = rng.choice([p for p in pool if p != p1])
        q1 = rng.choice(qpool)
        q2 = rng.choice([q for q in qpool if q != q1])

        # Randomly assign which sticker is Option A vs Option B.
        if rng.random() < 0.5:
            price_a, qty_a = p1, q1
            price_b, qty_b = p2, q2
        else:
            price_a, qty_a = p2, q2
            price_b, qty_b = p1, q1

        total_a = price_a * qty_a
        total_b = price_b * qty_b

        # Better buy = lower unit price.
        better = "Option A" if price_a < price_b else "Option B"

        total_a_str = _fmt_money(total_a)
        total_b_str = _fmt_money(total_b)
        unit_a_str = _fmt_money(price_a)
        unit_b_str = _fmt_money(price_b)

        statement = (
            f"Two packages of {item} are on sale.\\\\"
            f"Option A: ${qty_a}$ {unit} for \\${total_a_str}.\\\\"
            f"Option B: ${qty_b}$ {unit} for \\${total_b_str}.\\\\"
            "Which option is the better buy (lower price per ounce)?"
        )

        answer = f"{better}"

        hints = [
            (
                "To compare, find each option's unit price: divide total cost by the "
                "number of ounces."
            ),
            (
                f"Option A: $\\${total_a_str} \\div {qty_a} = \\${unit_a_str}$ per {unit}. "
                f"Option B: $\\${total_b_str} \\div {qty_b} = \\${unit_b_str}$ per {unit}."
            ),
            (
                f"The cheaper unit price wins, so {better} is the better buy."
            ),
        ]

        steps = [
            (
                f"Option A unit price: "
                f"$\\dfrac{{\\${total_a_str}}}{{{qty_a}\\ \\text{{{unit}}}}} = "
                f"\\${unit_a_str}$ per {unit}."
            ),
            (
                f"Option B unit price: "
                f"$\\dfrac{{\\${total_b_str}}}{{{qty_b}\\ \\text{{{unit}}}}} = "
                f"\\${unit_b_str}$ per {unit}."
            ),
            (
                f"Compare: $\\${unit_a_str}$ vs. $\\${unit_b_str}$. "
                f"The lower price per {unit} is the better buy, so the answer is {better}."
            ),
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (price_a, qty_a, price_b, qty_b, item),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=_tags_for(difficulty),
        )


# ---------------------------------------------------------------------------
# Topic 2: proportions_and_cross_multiplication
# ---------------------------------------------------------------------------


@register
class SolveProportionForUnknown(Generator):
    """Given three of four terms in a proportion, solve for the unknown.

    Backward: pick a clean integer answer ``x``, then pick ``a, b, c`` so
    cross multiplication produces ``x`` exactly. The unknown position is
    rotated among all four slots so the student sees every arrangement.
    """
    generator_id = "solve_proportion_for_unknown"
    topic_slug = "proportions_and_cross_multiplication"
    display_name = "Solve a proportion for the unknown"

    _SMALL_INT_RANGES = {
        "easy": (2, 9),
        "medium": (2, 12),
        "hard": (2, 15),
    }
    _SCALE_RANGES = {
        "easy": (2, 6),
        "medium": (2, 8),
        "hard": (2, 10),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._SMALL_INT_RANGES[difficulty]
        slo, shi = self._SCALE_RANGES[difficulty]

        # Start from a "base" ratio a/b. Multiply both by k to get c/d.
        # So a/b = c/d where c = a*k, d = b*k.
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        while b == a:
            b = rng.randint(lo, hi)
        k = rng.randint(slo, shi)
        c = a * k
        d = b * k

        # Pick which position is the unknown. Position 0 means a is hidden,
        # 1 means b, 2 means c, 3 means d.
        hidden = rng.randint(0, 3)

        if hidden == 0:
            # a/? -> shown: ?/b = c/d, answer = a
            x_val = a
            shown_a = "x"
            shown_b = str(b)
            shown_c = str(c)
            shown_d = str(d)
            left_num, left_den = "x", b
            right_num, right_den = c, d
            # Cross multiply: x * d = b * c, so x = b*c / d.
            lhs = b * c
            rhs_den = d
        elif hidden == 1:
            x_val = b
            shown_a = str(a)
            shown_b = "x"
            shown_c = str(c)
            shown_d = str(d)
            left_num, left_den = a, "x"
            right_num, right_den = c, d
            # a * d = x * c, so x = a*d / c.
            lhs = a * d
            rhs_den = c
        elif hidden == 2:
            x_val = c
            shown_a = str(a)
            shown_b = str(b)
            shown_c = "x"
            shown_d = str(d)
            left_num, left_den = a, b
            right_num, right_den = "x", d
            # a * d = b * x, so x = a*d / b.
            lhs = a * d
            rhs_den = b
        else:  # hidden == 3
            x_val = d
            shown_a = str(a)
            shown_b = str(b)
            shown_c = str(c)
            shown_d = "x"
            left_num, left_den = a, b
            right_num, right_den = c, "x"
            # a * x = b * c, so x = b*c / a.
            lhs = b * c
            rhs_den = a

        prop_latex = (
            f"\\dfrac{{{left_num}}}{{{left_den}}} = "
            f"\\dfrac{{{right_num}}}{{{right_den}}}"
        )

        statement = f"Solve for $x$: ${prop_latex}$."

        answer = f"$x = {x_val}$"

        # Build the cross-multiplication step strings concretely.
        # Cross product: left_num * right_den = right_num * left_den.
        # Substituting x into its spot, the two products should equal.
        cross_left_expr = f"{left_num} \\cdot {right_den}"
        cross_right_expr = f"{right_num} \\cdot {left_den}"

        hints = [
            (
                "A proportion means two ratios are equal. Cross multiply to "
                "clear the denominators."
            ),
            (
                f"Cross multiplying gives ${cross_left_expr} = {cross_right_expr}$."
            ),
            (
                f"Solving gives $x = {x_val}$."
            ),
        ]

        steps = [
            (
                f"Write the proportion: ${prop_latex}$."
            ),
            (
                f"Cross multiply: ${cross_left_expr} = {cross_right_expr}$."
            ),
            (
                f"Substitute the known numbers and solve: "
                f"${lhs} = {rhs_den}x$, so $x = \\dfrac{{{lhs}}}{{{rhs_den}}} = {x_val}$."
            ),
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, k, hidden),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=_tags_for(difficulty),
        )


_SCALE_CONTEXTS = (
    ("textbooks", "weigh", "pounds"),
    ("books", "weigh", "pounds"),
    ("apples", "weigh", "pounds"),
    ("water bottles", "hold", "cups"),
    ("boxes", "contain", "items"),
    ("bags", "hold", "marbles"),
    ("jars", "contain", "cookies"),
    ("crates", "hold", "oranges"),
)


@register
class ScaleWithProportionWord(Generator):
    """Word problem: scale a known ratio to find an unknown total.

    Format: "If {a} {items} {verb} {b} {unit}, how much/many do {c} {items}
    {verb}?" Backward: pick a per-item value (integer), derive the visible
    quantities so the final answer is a clean integer.
    """
    generator_id = "scale_with_proportion_word"
    topic_slug = "proportions_and_cross_multiplication"
    display_name = "Scale with a proportion (word problem)"

    _PER_ITEM = {
        "easy": (2, 3, 4, 5, 6),
        "medium": (2, 3, 4, 5, 6, 7, 8, 9),
        "hard": (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    }
    _BASE_COUNTS = {
        "easy": (2, 3, 4, 5),
        "medium": (2, 3, 4, 5, 6, 8, 10),
        "hard": (3, 4, 5, 6, 7, 8, 9, 10, 12, 15),
    }
    _SCALE_COUNTS = {
        "easy": (2, 3, 4, 5, 6, 7, 8, 10),
        "medium": (3, 4, 5, 6, 8, 10, 12, 15, 20),
        "hard": (4, 5, 6, 8, 10, 12, 15, 18, 20, 24, 25, 30),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        item, verb, unit = rng.choice(_SCALE_CONTEXTS)
        per_item = rng.choice(self._PER_ITEM[difficulty])

        # Base count a: items mentioned in the first clause.
        a = rng.choice(self._BASE_COUNTS[difficulty])
        # Scaled count c: items to solve for. Must be distinct from a to
        # avoid a trivial problem.
        scale_pool = [s for s in self._SCALE_COUNTS[difficulty] if s != a]
        c = rng.choice(scale_pool)

        # Base output b and scaled output x.
        b = per_item * a
        x = per_item * c

        prop_latex = f"\\dfrac{{{a}}}{{{b}}} = \\dfrac{{{c}}}{{x}}"

        statement = (
            f"If ${a}$ {item} {verb} ${b}$ {unit}, how many {unit} do ${c}$ "
            f"{item} {verb}?"
        )

        answer = f"${x}$ {unit}"

        hints = [
            (
                "Set up a proportion. The ratio of items to "
                f"{unit} should be the same on both sides."
            ),
            (
                f"Using the first clause, the ratio is $\\dfrac{{{a}\\ \\text{{{item}}}}}{{{b}\\ \\text{{{unit}}}}}$. "
                f"Match it with $\\dfrac{{{c}\\ \\text{{{item}}}}}{{x\\ \\text{{{unit}}}}}$."
            ),
            (
                f"Cross multiply and solve for $x$: $x = {x}$."
            ),
        ]

        steps = [
            (
                f"Write the proportion: ${prop_latex}$."
            ),
            (
                f"Cross multiply: ${a} \\cdot x = {b} \\cdot {c}$, i.e., "
                f"${a}x = {b * c}$."
            ),
            (
                f"Divide both sides by ${a}$: "
                f"$x = \\dfrac{{{b * c}}}{{{a}}} = {x}$."
            ),
            (
                f"So ${c}$ {item} {verb} ${x}$ {unit}."
            ),
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (per_item, a, c, item),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=_tags_for(difficulty),
        )


@register
class VerifyIsProportion(Generator):
    """Given two ratios, decide whether they form a true proportion.

    Backward: pick a base ratio a/b. With 50% probability, create an
    equivalent ratio by scaling; with 50% probability, create a near-miss
    by nudging one component by 1 or 2. Use cross multiplication to
    justify the verdict.
    """
    generator_id = "verify_is_proportion"
    topic_slug = "proportions_and_cross_multiplication"
    display_name = "Do two ratios form a proportion?"

    _NUM_RANGES = {
        "easy": (2, 9),
        "medium": (2, 12),
        "hard": (3, 15),
    }
    _DEN_RANGES = {
        "easy": (2, 9),
        "medium": (2, 12),
        "hard": (3, 15),
    }
    _SCALE_RANGES = {
        "easy": (2, 5),
        "medium": (2, 7),
        "hard": (2, 9),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        nlo, nhi = self._NUM_RANGES[difficulty]
        dlo, dhi = self._DEN_RANGES[difficulty]
        slo, shi = self._SCALE_RANGES[difficulty]

        # Pick a base ratio a/b with a and b distinct and coprime-ish.
        a = rng.randint(nlo, nhi)
        b = rng.randint(dlo, dhi)
        while a == b:
            b = rng.randint(dlo, dhi)

        k = rng.randint(slo, shi)
        is_true = rng.random() < 0.5

        if is_true:
            c = a * k
            d = b * k
            verdict = "Yes"
        else:
            # Near-miss: scale then perturb one component.
            c = a * k
            d = b * k
            # Perturb by +/- 1 or 2 on either c or d.
            delta = rng.choice([-2, -1, 1, 2])
            which = rng.choice(["c", "d"])
            if which == "c":
                c += delta
                if c <= 0:
                    c = a * k + abs(delta)
            else:
                d += delta
                if d <= 0:
                    d = b * k + abs(delta)
            # Safety: make sure the near-miss is not accidentally a true
            # proportion (can happen if perturbation hits a multiple).
            if a * d == b * c:
                d += 1
            verdict = "No"

        cross_left = a * d
        cross_right = b * c

        statement = (
            f"Do the ratios $\\dfrac{{{a}}}{{{b}}}$ and $\\dfrac{{{c}}}{{{d}}}$ "
            "form a proportion? Answer Yes or No."
        )

        answer = verdict

        if verdict == "Yes":
            step_conclusion = (
                f"Since ${cross_left} = {cross_right}$, the two ratios are equal, "
                f"so they form a proportion. Answer: Yes."
            )
            hint_conclusion = (
                f"Because ${cross_left} = {cross_right}$, the ratios match. Yes."
            )
        else:
            step_conclusion = (
                f"Since ${cross_left} \\ne {cross_right}$, the two ratios are not "
                f"equal, so they do not form a proportion. Answer: No."
            )
            hint_conclusion = (
                f"Because ${cross_left} \\ne {cross_right}$, the ratios are "
                "different. No."
            )

        hints = [
            (
                "Two ratios form a proportion when their cross products are "
                "equal: $a \\cdot d = b \\cdot c$."
            ),
            (
                f"Cross multiply: ${a} \\cdot {d} = {cross_left}$ and "
                f"${b} \\cdot {c} = {cross_right}$."
            ),
            hint_conclusion,
        ]

        steps = [
            (
                f"Cross multiply the two ratios: compare ${a} \\cdot {d}$ with "
                f"${b} \\cdot {c}$."
            ),
            (
                f"Compute the cross products: ${a} \\cdot {d} = {cross_left}$ and "
                f"${b} \\cdot {c} = {cross_right}$."
            ),
            step_conclusion,
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, d, verdict),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=_tags_for(difficulty),
        )
