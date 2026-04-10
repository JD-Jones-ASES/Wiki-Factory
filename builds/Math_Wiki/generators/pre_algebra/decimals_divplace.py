"""Decimal division and place-value generators (Phase 2c, Cluster 1 Wave 2).

Two canonical topic slugs covered here:

- ``dividing_decimals`` at wiki/topics/pre_algebra/Dividing_Decimals.md
  Generators:
    * divide_decimal_by_whole       --- a / n where a is decimal, n is small int
    * divide_decimal_by_decimal     --- a / b where both are decimals
    * divide_decimal_by_power_of_ten --- a / 10^k for k in {1, 2, 3}

- ``decimal_place_value_and_comparing_decimals`` at
  wiki/topics/pre_algebra/Decimal_Place_Value_And_Comparing_Decimals.md
  Generators:
    * compare_two_decimals          --- decide <, >, or = for two decimals
    * identify_place_value          --- name the digit in a given place
    * round_decimal                 --- round a decimal to a target place

All generators use ``decimal.Decimal`` for exact arithmetic --- never float.
Backward construction is used everywhere possible: pick a clean answer first,
then derive the presented parameters.
"""
from __future__ import annotations

import random
from decimal import Decimal, ROUND_HALF_UP, getcontext

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Ensure enough precision for all backward constructions we do here.
getcontext().prec = 28


# Shared tag sets.
_TAGS_PROCEDURAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_REASONING = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-conceptual-reasoning",
]


# ---------------------------------------------------------------------------
# Decimal formatting helpers
# ---------------------------------------------------------------------------

def _fmt_dec(d: Decimal) -> str:
    """Format a Decimal as a plain string without trailing zeros or scientific notation.

    Examples:
        Decimal("0.400") -> "0.4"
        Decimal("1.0")   -> "1"
        Decimal("8")     -> "8"
        Decimal("0.050") -> "0.05"
    """
    # Normalize removes trailing zeros but can produce scientific notation for
    # large/small values; we walk the string back to plain notation.
    s = format(d.normalize(), "f")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
        if s == "" or s == "-":
            s = s + "0"
    return s if s else "0"


def _fmt_dec_places(d: Decimal, places: int) -> str:
    """Format a Decimal with exactly `places` digits after the decimal point."""
    if places <= 0:
        return str(int(d))
    quant = Decimal(1).scaleb(-places)  # 10^-places
    q = d.quantize(quant, rounding=ROUND_HALF_UP)
    return format(q, "f")


# ===========================================================================
# Topic 1: dividing_decimals
# ===========================================================================

@register
class DivideDecimalByWhole(Generator):
    """Divide a decimal by a small whole number.

    Backward construction: pick a clean quotient ``q`` (e.g., 0.4, 1.25),
    pick divisor ``n``, compute dividend ``a = q * n``.
    """
    generator_id = "divide_decimal_by_whole"
    topic_slug = "dividing_decimals"
    display_name = "Divide a decimal by a whole number"

    _PARAMS = {
        # q_tenths: quotient values in tenths, e.g. 0.1 .. 1.9
        "easy":   {"q_places": 1, "q_tenths_range": (2, 19), "n_range": (2, 9)},
        "medium": {"q_places": 1, "q_tenths_range": (5, 49), "n_range": (3, 12)},
        "hard":   {"q_places": 2, "q_hundredths_range": (10, 199), "n_range": (4, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        if params["q_places"] == 1:
            q_int = rng.randint(*params["q_tenths_range"])
            q = Decimal(q_int) / Decimal(10)
        else:
            q_int = rng.randint(*params["q_hundredths_range"])
            q = Decimal(q_int) / Decimal(100)

        n = rng.randint(*params["n_range"])
        a = q * Decimal(n)

        a_str = _fmt_dec(a)
        n_str = str(n)
        q_str = _fmt_dec(q)

        statement = f"Compute ${a_str} \\div {n_str}$."
        answer = f"${q_str}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "When dividing a decimal by a whole number, set up long division with the decimal point in the quotient lined up over the decimal point in the dividend.",
                f"Divide as if ${a_str}$ were a whole number, then place the decimal point directly above.",
                f"${a_str} \\div {n_str} = {q_str}$.",
            ],
            solution_steps_latex=[
                f"Set up long division: ${a_str} \\div {n_str}$.",
                f"Place the decimal point in the quotient directly above the decimal point in the dividend.",
                f"Divide the digits of ${a_str}$ by ${n_str}$ step by step.",
                f"Result: ${a_str} \\div {n_str} = {q_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class DivideDecimalByDecimal(Generator):
    """Divide a decimal by another decimal.

    Backward construction: pick clean quotient ``q``, pick divisor ``b``
    (a decimal), compute dividend ``a = q * b`` exactly with Decimal.
    """
    generator_id = "divide_decimal_by_decimal"
    topic_slug = "dividing_decimals"
    display_name = "Divide a decimal by a decimal"

    _PARAMS = {
        "easy": {
            "q_tenths_range": (2, 19),
            "b_places": 1,
            "b_tenths_range": (2, 9),
        },
        "medium": {
            "q_tenths_range": (5, 39),
            "b_places": 1,
            "b_tenths_range": (2, 19),
        },
        "hard": {
            "q_hundredths_range": (10, 99),
            "b_places": 2,
            "b_hundredths_range": (5, 99),
        },
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        if difficulty == "hard":
            q_int = rng.randint(*params["q_hundredths_range"])
            q = Decimal(q_int) / Decimal(100)
            b_int = rng.randint(*params["b_hundredths_range"])
            b = Decimal(b_int) / Decimal(100)
            shift = 2
        else:
            q_int = rng.randint(*params["q_tenths_range"])
            q = Decimal(q_int) / Decimal(10)
            b_int = rng.randint(*params["b_tenths_range"])
            b = Decimal(b_int) / Decimal(10)
            shift = 1

        a = q * b

        a_str = _fmt_dec(a)
        b_str = _fmt_dec(b)
        q_str = _fmt_dec(q)

        # Values after shifting decimal points (b -> whole number).
        shifted_a = a * (Decimal(10) ** shift)
        shifted_b = b * (Decimal(10) ** shift)
        shifted_a_str = _fmt_dec(shifted_a)
        shifted_b_str = _fmt_dec(shifted_b)

        statement = f"Compute ${a_str} \\div {b_str}$."
        answer = f"${q_str}$"

        shift_word = "one place" if shift == 1 else f"{shift} places"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, b_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "To divide by a decimal, shift the decimal point in the divisor until it becomes a whole number, then shift the decimal point in the dividend by the same number of places.",
                f"Move the decimal point {shift_word} to the right in both ${a_str}$ and ${b_str}$, giving ${shifted_a_str} \\div {shifted_b_str}$.",
                f"${shifted_a_str} \\div {shifted_b_str} = {q_str}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a_str} \\div {b_str}$.",
                f"Shift the decimal point in the divisor ${b_str}$ {shift_word} to the right: ${shifted_b_str}$.",
                f"Shift the decimal point in the dividend ${a_str}$ the same {shift_word}: ${shifted_a_str}$.",
                f"Now divide: ${shifted_a_str} \\div {shifted_b_str} = {q_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class DivideDecimalByPowerOfTen(Generator):
    """Divide a decimal by a power of ten (10, 100, or 1000).

    Shortcut: shift the decimal point left by the number of zeros in the
    power of ten.
    """
    generator_id = "divide_decimal_by_power_of_ten"
    topic_slug = "dividing_decimals"
    display_name = "Divide a decimal by a power of 10"

    _PARAMS = {
        # a_int / 10^a_places gives the starting decimal.
        "easy":   {"a_places": 1, "a_int_range": (10, 999),    "k_choices": (1, 2)},
        "medium": {"a_places": 2, "a_int_range": (100, 9999),  "k_choices": (1, 2, 3)},
        "hard":   {"a_places": 3, "a_int_range": (1000, 99999), "k_choices": (1, 2, 3)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        a_int = rng.randint(*params["a_int_range"])
        a = Decimal(a_int) / (Decimal(10) ** params["a_places"])
        k = rng.choice(params["k_choices"])

        divisor = 10 ** k
        result = a / Decimal(divisor)

        a_str = _fmt_dec(a)
        result_str = _fmt_dec(result)

        places_word = {1: "one place", 2: "two places", 3: "three places"}[k]

        statement = f"Compute ${a_str} \\div {divisor}$."
        answer = f"${result_str}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Dividing by ${divisor}$ is the same as moving the decimal point {places_word} to the left.",
                f"If needed, add leading zeros so that every place is filled.",
                f"${a_str} \\div {divisor} = {result_str}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a_str} \\div {divisor}$.",
                f"Count the zeros in ${divisor}$: that's ${k}$ zero" + ("s" if k != 1 else "") + ".",
                f"Move the decimal point {places_word} to the left.",
                f"Result: ${a_str} \\div {divisor} = {result_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


# ===========================================================================
# Topic 2: decimal_place_value_and_comparing_decimals
# ===========================================================================

@register
class CompareTwoDecimals(Generator):
    """Compare two decimals and return <, >, or =.

    Backward construction: first pick the answer, then construct a matching
    pair of decimals with possibly different numbers of places.
    """
    generator_id = "compare_two_decimals"
    topic_slug = "decimal_place_value_and_comparing_decimals"
    display_name = "Compare two decimals (<, >, or =)"

    _PARAMS = {
        "easy":   {"max_places": 2, "int_part_range": (0, 9)},
        "medium": {"max_places": 3, "int_part_range": (0, 19)},
        "hard":   {"max_places": 4, "int_part_range": (0, 49)},
    }

    def _random_decimal(self, rng: random.Random, max_places: int, int_max: int) -> Decimal:
        """Return a random Decimal with 1..max_places digits after the point."""
        int_part = rng.randint(0, int_max)
        places = rng.randint(1, max_places)
        frac = rng.randint(0, 10 ** places - 1)
        # Compose as Decimal so we never lose precision.
        total_int = int_part * (10 ** places) + frac
        return Decimal(total_int) / (Decimal(10) ** places)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        max_places = params["max_places"]
        int_max = params["int_part_range"][1]

        # Decide the target answer. Bias: ~45% <, ~45% >, ~10% equal.
        r = rng.random()
        if r < 0.10:
            target = "="
        elif r < 0.55:
            target = "<"
        else:
            target = ">"

        if target == "=":
            # Construct a numerically equal pair with different trailing zeros.
            base = self._random_decimal(rng, max_places, int_max)
            a = base
            # Pad b with extra trailing zeros up to max_places.
            extra_places = rng.randint(1, max(1, max_places))
            b = base.quantize(Decimal(10) ** -max_places)
            # Shift a to have fewer places by normalizing.
            a_str = _fmt_dec(a)
            b_str = format(b, "f")
            # Guard against b_str being identical to a_str after formatting.
            if a_str == b_str:
                # Force extra trailing zeros on b by padding manually.
                if "." not in b_str:
                    b_str = b_str + "." + "0" * extra_places
                else:
                    # Add extra trailing zeros (never changes value).
                    b_str = b_str + "0" * extra_places
            a_val = Decimal(a_str)
            b_val = Decimal(b_str)
        else:
            # Produce two distinct decimals.
            for _ in range(50):
                a_val = self._random_decimal(rng, max_places, int_max)
                b_val = self._random_decimal(rng, max_places, int_max)
                if a_val == b_val:
                    continue
                if (a_val < b_val and target == "<") or (a_val > b_val and target == ">"):
                    break
                # Otherwise swap to match target.
                if (a_val > b_val and target == "<") or (a_val < b_val and target == ">"):
                    a_val, b_val = b_val, a_val
                    break
            a_str = _fmt_dec(a_val)
            b_str = _fmt_dec(b_val)

        # Determine the symbol from the actual values (source of truth).
        if a_val < b_val:
            symbol = "<"
            symbol_word = "less than"
        elif a_val > b_val:
            symbol = ">"
            symbol_word = "greater than"
        else:
            symbol = "="
            symbol_word = "equal to"

        statement = (
            f"Compare ${a_str}$ and ${b_str}$. "
            f"Answer with $<$, $>$, or $=$."
        )
        answer = f"${symbol}$"

        # Pad both to the same number of places for the comparison hint.
        max_p = max(_places_of(a_str), _places_of(b_str))
        a_padded = _pad_decimal_str(a_str, max_p)
        b_padded = _pad_decimal_str(b_str, max_p)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a_str, b_str)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "To compare two decimals, first make sure they have the same number of digits after the decimal point by padding with trailing zeros.",
                f"Pad both numbers to ${max_p}$ decimal place" + ("s" if max_p != 1 else "") + f": ${a_padded}$ and ${b_padded}$.",
                f"Now compare place by place from left to right. ${a_str}$ is {symbol_word} ${b_str}$.",
            ],
            solution_steps_latex=[
                f"Write both numbers with the same number of decimal places: ${a_padded}$ vs ${b_padded}$.",
                f"Compare digits from left to right (ones, tenths, hundredths, ...).",
                f"Conclusion: ${a_str} {symbol} {b_str}$.",
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )


@register
class IdentifyPlaceValue(Generator):
    """Ask which digit is in a specified place of a decimal number."""
    generator_id = "identify_place_value"
    topic_slug = "decimal_place_value_and_comparing_decimals"
    display_name = "Identify a digit at a specified place value"

    # Place names and their offsets from the ones place.
    # Positive = left of decimal, negative = right of decimal.
    _PLACE_NAMES = {
        "ones":              0,
        "tenths":           -1,
        "hundredths":       -2,
        "thousandths":      -3,
        "ten-thousandths":  -4,
    }

    _PARAMS = {
        "easy": {
            "int_range": (1, 99),
            "max_decimal_places": 2,
            "place_choices": ("ones", "tenths", "hundredths"),
        },
        "medium": {
            "int_range": (10, 999),
            "max_decimal_places": 3,
            "place_choices": ("ones", "tenths", "hundredths", "thousandths"),
        },
        "hard": {
            "int_range": (10, 9999),
            "max_decimal_places": 4,
            "place_choices": ("ones", "tenths", "hundredths", "thousandths", "ten-thousandths"),
        },
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        int_part = rng.randint(*params["int_range"])
        places = params["max_decimal_places"]
        # Generate a fractional part with the full number of places, potentially
        # including zeros, so the student must handle embedded zeros correctly.
        frac_digits = [rng.randint(0, 9) for _ in range(places)]
        frac_str = "".join(str(d) for d in frac_digits)

        number_str = f"{int_part}.{frac_str}"

        place_name = rng.choice(params["place_choices"])
        offset = self._PLACE_NAMES[place_name]

        int_str = str(int_part)
        if offset == 0:
            # Ones digit = last digit of the integer part.
            digit = int(int_str[-1])
        else:
            # offset is negative: -1 means first frac digit, etc.
            idx = -offset - 1
            digit = frac_digits[idx] if idx < len(frac_digits) else 0

        statement = (
            f"In the number ${number_str}$, what digit is in the {place_name} place?"
        )
        answer = f"${digit}$"

        # Build a place-value breakdown hint that labels each digit.
        breakdown = _place_value_breakdown(int_str, frac_digits)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (number_str, place_name)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "Each digit has a place value. To the left of the decimal point: ones, tens, hundreds, ... To the right: tenths, hundredths, thousandths, ten-thousandths.",
                f"Place-value breakdown of ${number_str}$: {breakdown}.",
                f"The digit in the {place_name} place is ${digit}$.",
            ],
            solution_steps_latex=[
                f"Identify each digit's place in ${number_str}$.",
                f"Breakdown: {breakdown}.",
                f"The digit in the {place_name} place is ${digit}$.",
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )


@register
class RoundDecimal(Generator):
    """Round a decimal to a specified place.

    Uses ``ROUND_HALF_UP`` to match the typical "5 or more rounds up" rule.
    Handles the carry edge case automatically via Decimal quantize.
    """
    generator_id = "round_decimal"
    topic_slug = "decimal_place_value_and_comparing_decimals"
    display_name = "Round a decimal to a specified place"

    # Target places: "nearest whole", "nearest tenth", "nearest hundredth", "nearest thousandth"
    _TARGETS = {
        "whole":      0,
        "tenth":      1,
        "hundredth":  2,
        "thousandth": 3,
    }

    _PARAMS = {
        "easy": {
            "int_range": (1, 19),
            "num_places": 2,
            "target_choices": ("whole", "tenth"),
        },
        "medium": {
            "int_range": (1, 99),
            "num_places": 3,
            "target_choices": ("whole", "tenth", "hundredth"),
        },
        "hard": {
            "int_range": (1, 999),
            "num_places": 4,
            "target_choices": ("tenth", "hundredth", "thousandth"),
        },
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        int_part = rng.randint(*params["int_range"])
        num_places = params["num_places"]
        frac_digits = [rng.randint(0, 9) for _ in range(num_places)]
        # Occasionally nudge a "4" to "5" or "5" to "5" at the boundary to
        # force either a round-up or a carry, so students see both cases.
        target = rng.choice(params["target_choices"])
        target_place = self._TARGETS[target]

        # To ensure we see carries, sometimes set the digit at target_place
        # to 9 and the digit after it to 5-9.
        force_carry = rng.random() < 0.2
        if force_carry and target_place < num_places:
            frac_digits[target_place] = 9
            if target_place + 1 < num_places:
                frac_digits[target_place + 1] = rng.randint(5, 9)

        frac_str = "".join(str(d) for d in frac_digits)
        number_str = f"{int_part}.{frac_str}"
        number_dec = Decimal(number_str)

        # Quantize to the target place.
        if target_place == 0:
            quant = Decimal("1")
        else:
            quant = Decimal("1").scaleb(-target_place)
        rounded = number_dec.quantize(quant, rounding=ROUND_HALF_UP)

        if target_place == 0:
            rounded_str = str(int(rounded))
        else:
            rounded_str = format(rounded, "f")

        target_place_name = {
            "whole": "whole number",
            "tenth": "nearest tenth",
            "hundredth": "nearest hundredth",
            "thousandth": "nearest thousandth",
        }[target]

        statement = f"Round ${number_str}$ to the {target_place_name}."
        answer = f"${rounded_str}$"

        # Identify the "deciding digit": the digit just to the right of the target place.
        decide_idx = target_place  # 0 -> first frac digit, 1 -> second, etc.
        if decide_idx < num_places:
            deciding_digit = frac_digits[decide_idx]
        else:
            deciding_digit = 0

        if deciding_digit >= 5:
            direction_sentence = (
                f"Since the deciding digit is ${deciding_digit}$ (which is $5$ or more), round up."
            )
        else:
            direction_sentence = (
                f"Since the deciding digit is ${deciding_digit}$ (which is less than $5$), round down (keep the digit)."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (number_str, target)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Find the digit in the {target_place_name} place.",
                f"Look one place to the right. If that digit is $5$ or more, round up; otherwise round down.",
                f"${number_str}$ rounded to the {target_place_name} is ${rounded_str}$.",
            ],
            solution_steps_latex=[
                f"Start with ${number_str}$ and focus on the {target_place_name}.",
                direction_sentence,
                f"Final answer: ${rounded_str}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


# ---------------------------------------------------------------------------
# Module-level helpers used by generators above
# ---------------------------------------------------------------------------

def _places_of(s: str) -> int:
    """Return the number of digits after the decimal point in a string."""
    if "." not in s:
        return 0
    return len(s.split(".", 1)[1])


def _pad_decimal_str(s: str, target_places: int) -> str:
    """Pad a decimal string with trailing zeros to reach `target_places`."""
    if target_places <= 0:
        return s.split(".", 1)[0] if "." in s else s
    if "." not in s:
        return s + "." + "0" * target_places
    int_part, frac_part = s.split(".", 1)
    if len(frac_part) >= target_places:
        return s
    return int_part + "." + frac_part + "0" * (target_places - len(frac_part))


_PLACE_LABELS_INT = ["ones", "tens", "hundreds", "thousands", "ten-thousands"]
_PLACE_LABELS_FRAC = ["tenths", "hundredths", "thousandths", "ten-thousandths"]


def _place_value_breakdown(int_str: str, frac_digits: list[int]) -> str:
    """Build a compact 'digit=place' breakdown string for a decimal number."""
    parts: list[str] = []
    # Integer part: rightmost digit is ones, next is tens, etc.
    int_len = len(int_str)
    for i, ch in enumerate(int_str):
        # Position from right: int_len - 1 - i
        pos = int_len - 1 - i
        if pos < len(_PLACE_LABELS_INT):
            label = _PLACE_LABELS_INT[pos]
            parts.append(f"${ch}$ = {label}")
    # Fractional part.
    for i, d in enumerate(frac_digits):
        if i < len(_PLACE_LABELS_FRAC):
            label = _PLACE_LABELS_FRAC[i]
            parts.append(f"${d}$ = {label}")
    return ", ".join(parts)
