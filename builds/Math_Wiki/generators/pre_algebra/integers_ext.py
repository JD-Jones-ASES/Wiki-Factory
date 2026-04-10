"""Integer extension generators (Cluster 1 Wave 2).

Two canonical topic slugs covered here:

- ``integers_and_the_number_line`` at
  wiki/topics/pre_algebra/Integers_And_The_Number_Line.md

  Generators:
    * find_opposite_integer       --- find the additive inverse of an integer
    * absolute_value              --- compute |n|
    * order_integers_ascending    --- sort a list of integers smallest to largest

- ``multiplying_and_dividing_integers`` at
  wiki/topics/pre_algebra/Multiplying_And_Dividing_Integers.md

  Generators:
    * multiply_two_integers           --- signed integer multiplication
    * divide_two_integers             --- signed integer division (exact)
    * multiply_three_integers_sign_chain --- three-term product, sign-rule practice

All generators use backward construction where applicable (divide generator
picks the quotient first, then multiplies) to guarantee clean integer answers
and avoid mid-problem rejection loops.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Shared tag sets (mirror the pattern used in fractions_basics.py).
_TAGS_PROCEDURAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_CONCEPTUAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-conceptual-reasoning",
]


def _fmt_integer(n: int) -> str:
    """Format an integer, wrapping negatives in parentheses for clarity.

    Matches the convention established in ``integers.py``.
    """
    return f"({n})" if n < 0 else f"{n}"


def _sign_label(n: int) -> str:
    """Return '(+)' for non-negative, '(-)' for negative (for sign-rule hints)."""
    return "(-)" if n < 0 else "(+)"


# ===========================================================================
# Topic 1: integers_and_the_number_line
# ===========================================================================

@register
class FindOppositeInteger(Generator):
    """Given an integer $n$, find its opposite (additive inverse) $-n$."""
    generator_id = "find_opposite_integer"
    topic_slug = "integers_and_the_number_line"
    display_name = "Find the opposite of an integer"

    _RANGES = {"easy": (-20, 20), "medium": (-75, 75), "hard": (-200, 200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Roughly one in eleven problems uses zero so the student meets
        # the edge case without it dominating the bank.
        if rng.randint(1, 11) == 1:
            n = 0
        else:
            n = rng.randint(lo, hi)
            while n == 0:
                n = rng.randint(lo, hi)
        opposite = -n

        statement = f"Find the opposite of ${_fmt_integer(n)}$."
        answer = f"${opposite}$"

        if n == 0:
            rule_hint = "The opposite of $0$ is $0$ itself."
            zero_line = "Zero is its own opposite on the number line."
            step_line = "The opposite of $0$ is $0$."
        elif n > 0:
            rule_hint = (
                "The opposite of a positive integer is its negative counterpart "
                "(the same distance from zero on the other side of the number line)."
            )
            zero_line = (
                f"On a number line, ${n}$ is ${n}$ units to the right of $0$, "
                f"so its opposite is ${n}$ units to the left of $0$."
            )
            step_line = f"Flip the sign: ${n} \\rightarrow {opposite}$."
        else:
            rule_hint = (
                "The opposite of a negative integer is its positive counterpart "
                "(the same distance from zero on the other side of the number line)."
            )
            zero_line = (
                f"On a number line, ${n}$ is ${abs(n)}$ units to the left of $0$, "
                f"so its opposite is ${abs(n)}$ units to the right of $0$."
            )
            step_line = f"Flip the sign: ${_fmt_integer(n)} \\rightarrow {opposite}$."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "The opposite of an integer $n$ is $-n$ --- the number the same distance from $0$ on the other side.",
                rule_hint,
                f"The answer is ${opposite}$.",
            ],
            solution_steps_latex=[
                f"Start with ${_fmt_integer(n)}$.",
                zero_line,
                step_line,
                f"The opposite is ${opposite}$.",
            ],
            tags=_TAGS_CONCEPTUAL + [f"#difficulty-{difficulty}"],
        )


@register
class AbsoluteValue(Generator):
    """Compute the absolute value $|n|$ of an integer."""
    generator_id = "absolute_value"
    topic_slug = "integers_and_the_number_line"
    display_name = "Compute the absolute value of an integer"

    # Nonzero throughout --- |0| = 0 is trivial and not instructive.
    _RANGES = {"easy": (-25, 25), "medium": (-100, 100), "hard": (-400, 400)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # For easy, allow some non-negative values so the student sees |n| = n.
        # For medium/hard, bias toward negatives since that's the substantive case.
        if difficulty == "easy":
            n = rng.randint(lo, hi)
            while n == 0:
                n = rng.randint(lo, hi)
        else:
            # 70% negative, 30% positive (never zero).
            if rng.random() < 0.7:
                n = rng.randint(lo, -1)
            else:
                n = rng.randint(1, hi)
        result = abs(n)

        statement = f"Compute $|{_fmt_integer(n)}|$."
        answer = f"${result}$"

        if n >= 0:
            rule_hint = (
                "The absolute value of a non-negative number is the number itself."
            )
            distance_hint = f"${n}$ is already ${n}$ units from zero."
            step_line = f"$|{n}| = {n}$."
        else:
            rule_hint = (
                "The absolute value of a negative number is its positive counterpart."
            )
            distance_hint = (
                f"${n}$ is ${result}$ units to the left of zero, "
                f"so its distance from zero is ${result}$."
            )
            step_line = f"$|{_fmt_integer(n)}| = {result}$."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "Absolute value measures the distance from $0$ on the number line --- it is never negative.",
                rule_hint,
                distance_hint,
            ],
            solution_steps_latex=[
                f"Identify the number inside the bars: ${_fmt_integer(n)}$.",
                distance_hint,
                step_line,
            ],
            tags=_TAGS_CONCEPTUAL + [f"#difficulty-{difficulty}"],
        )


@register
class OrderIntegersAscending(Generator):
    """Sort a list of 4-5 integers in ascending (smallest to largest) order."""
    generator_id = "order_integers_ascending"
    topic_slug = "integers_and_the_number_line"
    display_name = "Order integers from smallest to largest"

    _PARAMS = {
        "easy":   {"n_items": 4, "lo": -15, "hi": 15},
        "medium": {"n_items": 5, "lo": -40, "hi": 40},
        "hard":   {"n_items": 5, "lo": -150, "hi": 150},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        n_items = params["n_items"]
        lo = params["lo"]
        hi = params["hi"]

        # Sample without replacement to avoid ties (sorted ties are fine
        # but less pedagogically interesting).
        values: list[int] = []
        attempts = 0
        while len(values) < n_items and attempts < 200:
            attempts += 1
            v = rng.randint(lo, hi)
            if v not in values:
                values.append(v)
        # Fallback: pad with unique values outside the current set.
        fallback = lo
        while len(values) < n_items:
            if fallback not in values:
                values.append(fallback)
            fallback += 1

        sorted_values = sorted(values)

        # Build the presentation and answer strings.
        unsorted_str = ", ".join(_fmt_integer(v) for v in values)
        sorted_str = ", ".join(str(v) for v in sorted_values)
        statement = (
            f"Order these integers from smallest to largest: ${unsorted_str}$."
        )
        answer = f"${sorted_str}$"

        # Identify useful reference points for the hints/steps.
        smallest = sorted_values[0]
        largest = sorted_values[-1]
        negatives = [v for v in sorted_values if v < 0]
        non_negatives = [v for v in sorted_values if v >= 0]
        if negatives and non_negatives:
            split_hint = (
                f"Negatives first (in order): "
                f"${', '.join(str(v) for v in negatives)}$. "
                f"Then non-negatives: ${', '.join(str(v) for v in non_negatives)}$."
            )
        elif negatives:
            split_hint = "All values are negative --- the one with the largest absolute value is smallest."
        else:
            split_hint = "All values are non-negative --- order as you would on the counting number line."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(values)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "On a number line, values further to the left are smaller and values further to the right are larger.",
                "Any negative integer is smaller than any non-negative integer.",
                split_hint,
            ],
            solution_steps_latex=[
                f"List the integers: ${unsorted_str}$.",
                f"The smallest value is ${smallest}$ and the largest is ${largest}$.",
                split_hint,
                f"In ascending order: ${sorted_str}$.",
            ],
            tags=_TAGS_CONCEPTUAL + [f"#difficulty-{difficulty}"],
        )


# ===========================================================================
# Topic 2: multiplying_and_dividing_integers
# ===========================================================================

@register
class MultiplyTwoIntegers(Generator):
    """Compute $a \\times b$ with signed integers (at least one negative)."""
    generator_id = "multiply_two_integers"
    topic_slug = "multiplying_and_dividing_integers"
    display_name = "Multiply two signed integers"

    # Absolute value ranges; actual sign is assigned per-factor below.
    _PARAMS = {
        "easy":   {"abs_max": 12},
        "medium": {"abs_max": 20},
        "hard":   {"abs_max": 30},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        abs_max = self._PARAMS[difficulty]["abs_max"]
        a_mag = rng.randint(2, abs_max)
        b_mag = rng.randint(2, abs_max)

        # Assign signs with at least one negative so sign rules are exercised.
        # Pick one of three patterns: (-, +), (+, -), (-, -), weighted equally.
        pattern = rng.choice(["neg_pos", "pos_neg", "neg_neg"])
        if pattern == "neg_pos":
            a = -a_mag
            b = b_mag
        elif pattern == "pos_neg":
            a = a_mag
            b = -b_mag
        else:
            a = -a_mag
            b = -b_mag

        result = a * b
        neg_count = (1 if a < 0 else 0) + (1 if b < 0 else 0)

        statement = f"Compute ${_fmt_integer(a)} \\times {_fmt_integer(b)}$."
        answer = f"${result}$"

        if neg_count == 2:
            sign_rule = r"$(-) \times (-) = (+)$: a negative times a negative gives a positive."
            sign_conclusion = "Both factors are negative, so the product is positive."
        else:
            sign_rule = r"$(-) \times (+) = (-)$ and $(+) \times (-) = (-)$: one negative gives a negative product."
            sign_conclusion = "Exactly one factor is negative, so the product is negative."

        abs_product = abs(a) * abs(b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "First multiply the absolute values, then determine the sign of the product.",
                sign_rule,
                f"$|{a}| \\times |{b}| = {abs(a)} \\times {abs(b)} = {abs_product}$. "
                f"{sign_conclusion} The answer is ${result}$.",
            ],
            solution_steps_latex=[
                f"Start with ${_fmt_integer(a)} \\times {_fmt_integer(b)}$.",
                f"Multiply absolute values: ${abs(a)} \\times {abs(b)} = {abs_product}$.",
                f"Apply the sign rule. {sign_rule}",
                f"{sign_conclusion} Final answer: ${result}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class DivideTwoIntegers(Generator):
    """Compute $a \\div b$ with signed integers. Clean quotient via backward construction."""
    generator_id = "divide_two_integers"
    topic_slug = "multiplying_and_dividing_integers"
    display_name = "Divide two signed integers"

    # Ranges control the absolute values of the quotient and divisor;
    # the dividend is derived from their product.
    _PARAMS = {
        "easy":   {"q_max": 10, "b_max": 10},
        "medium": {"q_max": 15, "b_max": 12},
        "hard":   {"q_max": 25, "b_max": 20},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        # Backward construction: pick the quotient and divisor first, then derive the dividend.
        q_mag = rng.randint(2, params["q_max"])
        b_mag = rng.randint(2, params["b_max"])

        # Assign signs so at least one of the dividend/divisor is negative.
        pattern = rng.choice(["neg_pos", "pos_neg", "neg_neg"])
        if pattern == "neg_pos":
            a = -(q_mag * b_mag)
            b = b_mag
            q = -q_mag
        elif pattern == "pos_neg":
            a = q_mag * b_mag
            b = -b_mag
            q = -q_mag
        else:  # neg_neg
            a = -(q_mag * b_mag)
            b = -b_mag
            q = q_mag

        # Sanity check: q is the exact quotient of a / b by construction.
        assert a == q * b, "Backward construction invariant failed"
        neg_count = (1 if a < 0 else 0) + (1 if b < 0 else 0)

        statement = f"Compute ${_fmt_integer(a)} \\div {_fmt_integer(b)}$."
        answer = f"${q}$"

        if neg_count == 2:
            sign_rule = r"$(-) \div (-) = (+)$: a negative divided by a negative gives a positive."
            sign_conclusion = "Both values are negative, so the quotient is positive."
        else:
            sign_rule = r"$(-) \div (+) = (-)$ and $(+) \div (-) = (-)$: one negative gives a negative quotient."
            sign_conclusion = "Exactly one value is negative, so the quotient is negative."

        abs_quotient = abs(a) // abs(b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "Division follows the same sign rules as multiplication.",
                sign_rule,
                f"$|{a}| \\div |{b}| = {abs(a)} \\div {abs(b)} = {abs_quotient}$. "
                f"{sign_conclusion} The answer is ${q}$.",
            ],
            solution_steps_latex=[
                f"Start with ${_fmt_integer(a)} \\div {_fmt_integer(b)}$.",
                f"Divide absolute values: ${abs(a)} \\div {abs(b)} = {abs_quotient}$.",
                f"Apply the sign rule. {sign_rule}",
                f"{sign_conclusion} Final answer: ${q}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class MultiplyThreeIntegersSignChain(Generator):
    """Compute $a \\times b \\times c$ --- sign-rule practice for a chain of factors."""
    generator_id = "multiply_three_integers_sign_chain"
    topic_slug = "multiplying_and_dividing_integers"
    display_name = "Multiply three integers (sign chain)"

    # Keep magnitudes modest so the resulting product stays readable.
    _PARAMS = {
        "easy":   {"abs_max": 7},
        "medium": {"abs_max": 10},
        "hard":   {"abs_max": 14},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        abs_max = self._PARAMS[difficulty]["abs_max"]
        a_mag = rng.randint(2, abs_max)
        b_mag = rng.randint(2, abs_max)
        c_mag = rng.randint(2, abs_max)

        # Pick how many factors are negative (0-3). All four options
        # are roughly equally likely so the student sees every parity case.
        neg_count_target = rng.choice([0, 1, 2, 3])
        # Randomly pick which factor positions get the negative signs.
        positions = [0, 1, 2]
        rng.shuffle(positions)
        neg_positions = set(positions[:neg_count_target])

        a = -a_mag if 0 in neg_positions else a_mag
        b = -b_mag if 1 in neg_positions else b_mag
        c = -c_mag if 2 in neg_positions else c_mag

        result = a * b * c
        actual_neg_count = sum(1 for x in (a, b, c) if x < 0)
        # Intermediate product (we still compute left-to-right for the worked solution).
        intermediate = a * b

        statement = (
            f"Compute ${_fmt_integer(a)} \\times {_fmt_integer(b)} \\times {_fmt_integer(c)}$."
        )
        answer = f"${result}$"

        if actual_neg_count % 2 == 0:
            parity_rule = (
                "An even number of negative factors gives a positive product."
            )
        else:
            parity_rule = (
                "An odd number of negative factors gives a negative product."
            )
        shortcut_hint = (
            f"Shortcut: count the negatives. Here there are ${actual_neg_count}$ negative factors, "
            f"which is {'even' if actual_neg_count % 2 == 0 else 'odd'}, "
            f"so the product is {'positive' if actual_neg_count % 2 == 0 else 'negative'}."
        )
        absolute_product = abs(a) * abs(b) * abs(c)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "Multiply left to right, or use the sign-counting shortcut.",
                parity_rule,
                shortcut_hint,
                f"The absolute value of the product is ${abs(a)} \\times {abs(b)} \\times {abs(c)} = {absolute_product}$, "
                f"so the final answer is ${result}$.",
            ],
            solution_steps_latex=[
                f"Start with ${_fmt_integer(a)} \\times {_fmt_integer(b)} \\times {_fmt_integer(c)}$.",
                f"First product: ${_fmt_integer(a)} \\times {_fmt_integer(b)} = {intermediate}$.",
                f"Then: ${_fmt_integer(intermediate)} \\times {_fmt_integer(c)} = {result}$.",
                f"Verification via sign counting: {shortcut_hint}",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )
