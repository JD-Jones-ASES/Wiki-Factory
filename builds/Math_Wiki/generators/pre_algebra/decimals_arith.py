"""Decimal arithmetic generators (Phase 2c, Cluster 1 Wave 2).

Two canonical topic slugs covered here:

- ``adding_and_subtracting_decimals`` at
  wiki/topics/pre_algebra/Adding_And_Subtracting_Decimals.md

  Generators:
    * add_two_decimals              --- a + b, 1-3 decimal places
    * subtract_two_decimals         --- a - b with a > b, borrowing scenarios
    * decimal_chain_add_subtract    --- a + b - c three-term chain

- ``multiplying_decimals`` at
  wiki/topics/pre_algebra/Multiplying_Decimals.md

  Generators:
    * multiply_two_decimals         --- a x b with decimal factors
    * multiply_decimal_by_whole     --- n x a (integer x decimal)
    * multiply_decimal_by_power_of_ten  --- a x 10^k, k in {-2,-1,1,2,3}

All generators use ``decimal.Decimal`` for exact arithmetic --- NEVER float.
Backward construction is used throughout: pick a clean target or clean
factors, then derive the presented parameters.
"""
from __future__ import annotations

import random
from decimal import Decimal, getcontext

from ..base import Difficulty, Generator, Problem, make_problem_id, register

# High precision so Decimal arithmetic never introduces rounding quirks
# across compound operations (chain sums, power-of-ten shifts, etc.).
getcontext().prec = 20


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

_TAGS_PROCEDURAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_MULTISTEP = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-multi-step",
]


def _decimal_from_parts(integer_part: int, fractional_digits: list[int]) -> Decimal:
    """Build an exact Decimal from an integer part and list of fractional digits.

    Example: (3, [1, 4]) -> Decimal("3.14").
             (0, [2, 5, 0]) -> Decimal("0.250")  (trailing zero preserved).
    """
    if not fractional_digits:
        return Decimal(integer_part)
    frac_str = "".join(str(d) for d in fractional_digits)
    return Decimal(f"{integer_part}.{frac_str}")


def _random_decimal(rng: random.Random, int_max: int, decimal_places: int) -> Decimal:
    """Draw a positive Decimal with integer part in [0, int_max] and exactly
    ``decimal_places`` fractional digits."""
    integer_part = rng.randint(0, int_max)
    fractional_digits = [rng.randint(0, 9) for _ in range(decimal_places)]
    # Avoid the degenerate all-zero case (e.g., "0.000" which is just 0).
    if integer_part == 0 and all(d == 0 for d in fractional_digits):
        fractional_digits[-1] = rng.randint(1, 9)
    return _decimal_from_parts(integer_part, fractional_digits)


def _fmt_decimal(d: Decimal) -> str:
    """Render a Decimal for LaTeX. Preserves trailing zeros from construction
    (so 1.20 stays 1.20) and ensures values < 1 have a leading zero."""
    s = format(d, "f")  # non-scientific, preserves trailing zeros
    if s.startswith("."):
        s = "0" + s
    if s.startswith("-."):
        s = "-0" + s[1:]
    return s


# ===========================================================================
# Topic 1: adding_and_subtracting_decimals
# ===========================================================================

@register
class AddTwoDecimals(Generator):
    """Compute $a + b$ where both are positive decimals (1-3 decimal places)."""
    generator_id = "add_two_decimals"
    topic_slug = "adding_and_subtracting_decimals"
    display_name = "Add two decimals"

    # int_max = max integer part; dp_choices = allowed decimal-place counts per operand.
    _PARAMS = {
        "easy":   {"int_max": 9,   "dp_choices": (1, 2)},
        "medium": {"int_max": 49,  "dp_choices": (1, 2, 3)},
        "hard":   {"int_max": 199, "dp_choices": (2, 3)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        dp_a = rng.choice(params["dp_choices"])
        dp_b = rng.choice(params["dp_choices"])
        a = _random_decimal(rng, params["int_max"], dp_a)
        b = _random_decimal(rng, params["int_max"], dp_b)
        result = a + b

        a_str = _fmt_decimal(a)
        b_str = _fmt_decimal(b)
        result_str = _fmt_decimal(result)

        statement = f"Compute ${a_str} + {b_str}$."

        # Alignment explanation: match the longer decimal place count.
        max_dp = max(dp_a, dp_b)
        align_note = (
            f"Line up the decimal points. Pad the shorter number to ${max_dp}$ "
            f"decimal place{'s' if max_dp != 1 else ''} with trailing zeros if needed."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, b_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result_str}$",
            hints=[
                align_note,
                f"Add column by column from right to left, carrying as needed: ${a_str} + {b_str}$.",
                f"The sum is ${result_str}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a_str} + {b_str}$.",
                align_note,
                f"Add the digits column by column and bring down the decimal point.",
                f"Result: ${a_str} + {b_str} = {result_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class SubtractTwoDecimals(Generator):
    """Compute $a - b$ with $a > b$ (positive result). Includes borrowing cases."""
    generator_id = "subtract_two_decimals"
    topic_slug = "adding_and_subtracting_decimals"
    display_name = "Subtract two decimals"

    _PARAMS = {
        "easy":   {"int_max": 9,   "dp_choices": (1, 2)},
        "medium": {"int_max": 49,  "dp_choices": (1, 2, 3)},
        "hard":   {"int_max": 199, "dp_choices": (2, 3)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        # Draw two candidates then assign the larger to a so a - b > 0.
        for _ in range(60):
            dp_a = rng.choice(params["dp_choices"])
            dp_b = rng.choice(params["dp_choices"])
            # Force a mix of decimal place counts often enough to exercise borrowing.
            if rng.random() < 0.6 and dp_a == dp_b and len(params["dp_choices"]) > 1:
                choices = [dp for dp in params["dp_choices"] if dp != dp_a]
                if choices:
                    dp_b = rng.choice(choices)
            x = _random_decimal(rng, params["int_max"], dp_a)
            y = _random_decimal(rng, params["int_max"], dp_b)
            if x == y:
                continue
            if x > y:
                a, b = x, y
                dp_larger, dp_smaller = dp_a, dp_b
            else:
                a, b = y, x
                dp_larger, dp_smaller = dp_b, dp_a
            break
        else:
            # Extremely unlikely fallback.
            a = Decimal("2.50")
            b = Decimal("1.35")
            dp_larger, dp_smaller = 2, 2

        result = a - b
        a_str = _fmt_decimal(a)
        b_str = _fmt_decimal(b)
        result_str = _fmt_decimal(result)

        statement = f"Compute ${a_str} - {b_str}$."

        max_dp = max(dp_larger, dp_smaller)
        align_note = (
            f"Line up the decimal points. Pad the shorter number to ${max_dp}$ "
            f"decimal place{'s' if max_dp != 1 else ''} with trailing zeros if needed."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, b_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result_str}$",
            hints=[
                align_note,
                f"Subtract column by column from right to left, borrowing from the next column when needed.",
                f"The difference is ${result_str}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a_str} - {b_str}$.",
                align_note,
                f"Subtract digits column by column, borrowing when a top digit is smaller than the bottom.",
                f"Result: ${a_str} - {b_str} = {result_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class DecimalChainAddSubtract(Generator):
    """Compute a three-term decimal chain $a + b - c$ with a positive final result."""
    generator_id = "decimal_chain_add_subtract"
    topic_slug = "adding_and_subtracting_decimals"
    display_name = "Compute a + b - c with decimals"

    _PARAMS = {
        "easy":   {"int_max": 9,  "dp_choices": (1, 2)},
        "medium": {"int_max": 29, "dp_choices": (1, 2)},
        "hard":   {"int_max": 99, "dp_choices": (1, 2)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        # Backward-ish construction: pick a and b freely, then pick c small enough
        # to keep the final result positive.
        for _ in range(80):
            dp_a = rng.choice(params["dp_choices"])
            dp_b = rng.choice(params["dp_choices"])
            dp_c = rng.choice(params["dp_choices"])
            a = _random_decimal(rng, params["int_max"], dp_a)
            b = _random_decimal(rng, params["int_max"], dp_b)
            partial = a + b
            # Draw c in [0.1, partial * 0.9] so the result stays positive and non-trivial.
            upper_int = max(1, int(partial) )
            c = _random_decimal(rng, upper_int, dp_c)
            if c < partial and c > 0:
                result = partial - c
                if result > 0:
                    break
        else:
            a = Decimal("5.25")
            b = Decimal("3.10")
            c = Decimal("2.40")
            partial = a + b
            result = partial - c
            dp_a, dp_b, dp_c = 2, 2, 2

        a_str = _fmt_decimal(a)
        b_str = _fmt_decimal(b)
        c_str = _fmt_decimal(c)
        partial_str = _fmt_decimal(partial)
        result_str = _fmt_decimal(result)

        statement = (
            rf"Compute ${a_str} + {b_str} - {c_str}$."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, b_str, c_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result_str}$",
            hints=[
                "With only addition and subtraction, work from left to right.",
                f"First add: ${a_str} + {b_str} = {partial_str}$.",
                f"Then subtract: ${partial_str} - {c_str} = {result_str}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a_str} + {b_str} - {c_str}$.",
                f"Step 1 (add): ${a_str} + {b_str} = {partial_str}$.",
                f"Step 2 (subtract): ${partial_str} - {c_str} = {result_str}$.",
                f"Final answer: ${result_str}$.",
            ],
            tags=_TAGS_MULTISTEP + [f"#difficulty-{difficulty}"],
        )


# ===========================================================================
# Topic 2: multiplying_decimals
# ===========================================================================

@register
class MultiplyTwoDecimals(Generator):
    """Compute $a \\times b$ where both factors are decimals.

    Backward construction: pick integer factors $p$ and $q$, then place decimal
    points. The digit count in the product equals the sum of the factor digit
    counts, so answers are always exact.
    """
    generator_id = "multiply_two_decimals"
    topic_slug = "multiplying_decimals"
    display_name = "Multiply two decimals"

    # p_range / q_range are integer factors before decimal-point placement.
    # dp_choices = decimal places to insert per factor.
    _PARAMS = {
        "easy":   {"p_range": (2, 9),  "q_range": (2, 9),  "dp_a_choices": (1,),    "dp_b_choices": (1,)},
        "medium": {"p_range": (2, 19), "q_range": (2, 19), "dp_a_choices": (1, 2),  "dp_b_choices": (1, 2)},
        "hard":   {"p_range": (3, 39), "q_range": (3, 39), "dp_a_choices": (1, 2),  "dp_b_choices": (2,)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        p = rng.randint(*params["p_range"])
        q = rng.randint(*params["q_range"])
        dp_a = rng.choice(params["dp_a_choices"])
        dp_b = rng.choice(params["dp_b_choices"])

        # Build decimal factors by shifting the integer factor right by dp places.
        # Example: p=12, dp_a=1 -> 1.2 ;  p=12, dp_a=2 -> 0.12.
        a = Decimal(p) / (Decimal(10) ** dp_a)
        b = Decimal(q) / (Decimal(10) ** dp_b)
        # Re-express with preserved trailing zeros using string construction,
        # so the presentation matches the decimal-place intent.
        a = Decimal(_shift_to_string(p, dp_a))
        b = Decimal(_shift_to_string(q, dp_b))
        result = a * b

        a_str = _fmt_decimal(a)
        b_str = _fmt_decimal(b)
        result_str = _fmt_decimal(result)
        total_dp = dp_a + dp_b

        statement = rf"Compute ${a_str} \times {b_str}$."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, b_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result_str}$",
            hints=[
                "Multiply as if the numbers were whole numbers (ignore the decimal points for a moment).",
                (
                    rf"${a_str}$ has ${dp_a}$ decimal place{'s' if dp_a != 1 else ''} and "
                    rf"${b_str}$ has ${dp_b}$, so the product will have ${total_dp}$ decimal places."
                ),
                rf"${p} \times {q} = {p * q}$, then place the decimal point: ${result_str}$.",
            ],
            solution_steps_latex=[
                rf"Start with ${a_str} \times {b_str}$.",
                rf"Ignore the decimal points: ${p} \times {q} = {p * q}$.",
                (
                    rf"Count decimal places in the factors: ${dp_a} + {dp_b} = {total_dp}$ "
                    rf"place{'s' if total_dp != 1 else ''}."
                ),
                rf"Place the decimal point ${total_dp}$ position{'s' if total_dp != 1 else ''} from the right: ${result_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class MultiplyDecimalByWhole(Generator):
    """Compute $n \\times a$ where $n$ is a positive integer and $a$ is a decimal."""
    generator_id = "multiply_decimal_by_whole"
    topic_slug = "multiplying_decimals"
    display_name = "Multiply a decimal by a whole number"

    _PARAMS = {
        "easy":   {"n_range": (2, 9),  "p_range": (2, 19),  "dp_choices": (1,)},
        "medium": {"n_range": (2, 15), "p_range": (2, 49),  "dp_choices": (1, 2)},
        "hard":   {"n_range": (3, 25), "p_range": (2, 199), "dp_choices": (1, 2)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        n = rng.randint(*params["n_range"])
        p = rng.randint(*params["p_range"])
        dp = rng.choice(params["dp_choices"])

        a = Decimal(_shift_to_string(p, dp))
        result = Decimal(n) * a

        a_str = _fmt_decimal(a)
        result_str = _fmt_decimal(result)
        raw_product = n * p

        statement = rf"Compute ${n} \times {a_str}$."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, a_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result_str}$",
            hints=[
                f"Multiply as if ${a_str}$ were the whole number ${p}$.",
                rf"${n} \times {p} = {raw_product}$.",
                (
                    rf"The factor ${a_str}$ has ${dp}$ decimal place{'s' if dp != 1 else ''}, "
                    rf"so place the decimal point ${dp}$ from the right: ${result_str}$."
                ),
            ],
            solution_steps_latex=[
                rf"Start with ${n} \times {a_str}$.",
                rf"Ignore the decimal point and compute ${n} \times {p} = {raw_product}$.",
                (
                    rf"Count the decimal places in the factors: ${dp}$ total "
                    rf"place{'s' if dp != 1 else ''}."
                ),
                rf"Place the decimal point: ${result_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class MultiplyDecimalByPowerOfTen(Generator):
    """Compute $a \\times 10^k$ for $k \\in \\{-2, -1, 1, 2, 3\\}$.

    Positive $k$ is presented as $a \\times 10^k$ (or $\\times 10$, $\\times 100$, etc.).
    Negative $k$ is presented as a division ($a \\div 10$, $a \\div 100$).
    """
    generator_id = "multiply_decimal_by_power_of_ten"
    topic_slug = "multiplying_decimals"
    display_name = "Multiply or divide a decimal by a power of ten"

    _PARAMS = {
        "easy":   {"p_range": (2, 99),   "dp_choices": (1, 2), "k_choices": (-1, 1, 2)},
        "medium": {"p_range": (2, 999),  "dp_choices": (1, 2), "k_choices": (-2, -1, 1, 2, 3)},
        "hard":   {"p_range": (2, 9999), "dp_choices": (2, 3), "k_choices": (-2, -1, 1, 2, 3)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        p = rng.randint(*params["p_range"])
        dp = rng.choice(params["dp_choices"])
        k = rng.choice(params["k_choices"])

        a = Decimal(_shift_to_string(p, dp))
        # a * 10^k computed exactly.
        if k >= 0:
            result = a * (Decimal(10) ** k)
            op_symbol = r"\times"
            op_rhs = _power_of_ten_label(k)
            direction_word = "right"
            shift_count = k
        else:
            result = a / (Decimal(10) ** (-k))
            op_symbol = r"\div"
            op_rhs = _power_of_ten_label(-k)
            direction_word = "left"
            shift_count = -k

        a_str = _fmt_decimal(a)
        result_str = _fmt_decimal(result)

        statement = rf"Compute ${a_str} {op_symbol} {op_rhs}$."

        if k >= 0:
            rule_hint = (
                f"Multiplying by a power of ten shifts the decimal point to the "
                f"right by the number of zeros in the multiplier."
            )
            shift_hint = (
                f"${op_rhs}$ has ${shift_count}$ zero{'s' if shift_count != 1 else ''}, "
                f"so move the decimal point ${shift_count}$ place{'s' if shift_count != 1 else ''} to the right."
            )
        else:
            rule_hint = (
                f"Dividing by a power of ten shifts the decimal point to the "
                f"left by the number of zeros in the divisor."
            )
            shift_hint = (
                f"${op_rhs}$ has ${shift_count}$ zero{'s' if shift_count != 1 else ''}, "
                f"so move the decimal point ${shift_count}$ place{'s' if shift_count != 1 else ''} to the left."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result_str}$",
            hints=[
                rule_hint,
                shift_hint,
                f"Starting from ${a_str}$, shift the decimal to get ${result_str}$.",
            ],
            solution_steps_latex=[
                rf"Start with ${a_str} {op_symbol} {op_rhs}$.",
                rule_hint,
                (
                    f"Move the decimal point ${shift_count}$ "
                    f"place{'s' if shift_count != 1 else ''} to the {direction_word}."
                ),
                rf"Result: ${result_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


# ---------------------------------------------------------------------------
# Private helpers for backward-construction of decimal factors
# ---------------------------------------------------------------------------

def _shift_to_string(p: int, dp: int) -> str:
    """Convert an integer ``p`` into a decimal string with ``dp`` decimal places.

    Examples:
        _shift_to_string(12, 0) -> "12"
        _shift_to_string(12, 1) -> "1.2"
        _shift_to_string(12, 2) -> "0.12"
        _shift_to_string(12, 3) -> "0.012"
        _shift_to_string(7,  2) -> "0.07"

    The result is passed directly to ``Decimal(...)`` so it preserves the
    intended precision exactly.
    """
    if dp == 0:
        return str(p)
    s = str(p)
    if len(s) > dp:
        # Decimal point goes len(s)-dp from the left.
        cut = len(s) - dp
        return s[:cut] + "." + s[cut:]
    # Need leading zero(s): "0." + padding + s
    pad = "0" * (dp - len(s))
    return "0." + pad + s


def _power_of_ten_label(exp: int) -> str:
    """Render 10^exp as a human-friendly LaTeX string.

    exp=1 -> '10', exp=2 -> '100', exp=3 -> '1000'. For larger exponents
    fall back to '10^{exp}' (not expected for our current k choices).
    """
    if exp == 1:
        return "10"
    if exp == 2:
        return "100"
    if exp == 3:
        return "1000"
    if exp == 4:
        return "10000"
    return rf"10^{{{exp}}}"
