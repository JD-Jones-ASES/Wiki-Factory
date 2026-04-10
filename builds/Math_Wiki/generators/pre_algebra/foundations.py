"""Pre-algebra foundations generators (Phase 2c Wave 3).

Two canonical topic slugs covered here:

- ``place_value_rounding_and_estimation`` at
  wiki/topics/pre_algebra/Place_Value_Rounding_And_Estimation.md

  Generators:
    * identify_digit_place_value   --- value of a specific digit
    * round_whole_number           --- round to nearest 10/100/1000/10000
    * estimate_sum_by_rounding     --- round each addend, then add

- ``square_roots_and_cube_roots`` at
  wiki/topics/pre_algebra/Square_Roots_And_Cube_Roots.md

  Generators:
    * square_root_of_perfect_square --- sqrt of n^2
    * cube_root_of_perfect_cube     --- cube root of n^3 (signed)
    * estimate_square_root          --- trap non-perfect square between integers

All generators use backward construction: pick the clean answer first,
then derive the presented parameters.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared tag sets
# ---------------------------------------------------------------------------

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
# LaTeX formatting helpers
# ---------------------------------------------------------------------------

def _fmt_comma(n: int) -> str:
    """Format a non-negative integer with LaTeX-safe comma grouping.

    Uses ``{,}`` so KaTeX renders proper thousands spacing without the
    default comma-as-punctuation extra space.
    """
    if n < 0:
        return f"-{_fmt_comma(-n)}"
    return f"{n:,}".replace(",", "{,}")


_PLACE_NAMES = {
    0: "ones",
    1: "tens",
    2: "hundreds",
    3: "thousands",
    4: "ten thousands",
    5: "hundred thousands",
}

_PLACE_VALUES = {
    0: 1,
    1: 10,
    2: 100,
    3: 1000,
    4: 10000,
    5: 100000,
}


# ===========================================================================
# Topic 1: place_value_rounding_and_estimation
# ===========================================================================

@register
class IdentifyDigitPlaceValue(Generator):
    """Given a whole number, state the place value of a specific digit.

    Backward construction: pick the target place index and the non-zero
    digit that will live there, then draw the other digits.
    """
    generator_id = "identify_digit_place_value"
    topic_slug = "place_value_rounding_and_estimation"
    display_name = "Identify the place value of a digit"

    # (min_places, max_places) where places are counted in digits.
    _PARAMS = {
        "easy": {"min_digits": 3, "max_digits": 4},
        "medium": {"min_digits": 4, "max_digits": 5},
        "hard": {"min_digits": 5, "max_digits": 6},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        num_digits = rng.randint(params["min_digits"], params["max_digits"])
        # Target position: 0 = ones, num_digits - 1 = leading digit
        target_pos = rng.randint(0, num_digits - 1)
        # Target digit: non-zero so the value is visible and non-trivial.
        target_digit = rng.randint(1, 9)

        # Fill other positions. Leading (highest) position must be non-zero.
        digits: list[int] = [0] * num_digits  # index 0 = ones, num_digits-1 = leading
        digits[target_pos] = target_digit
        for i in range(num_digits):
            if i == target_pos:
                continue
            if i == num_digits - 1:
                digits[i] = rng.randint(1, 9)
            else:
                digits[i] = rng.randint(0, 9)

        # Assemble the integer
        number = 0
        for i in range(num_digits):
            number += digits[i] * (10 ** i)

        value = target_digit * _PLACE_VALUES[target_pos]
        place_name = _PLACE_NAMES[target_pos]

        statement = (
            f"In the number ${_fmt_comma(number)}$, what is the value of the digit ${target_digit}$?"
        )
        answer = f"${_fmt_comma(value)}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (number, target_digit, target_pos)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "Each digit's value depends on its position: ones, tens, hundreds, thousands, and so on.",
                f"The digit ${target_digit}$ sits in the {place_name} place.",
                f"Its value is ${target_digit} \\times {_fmt_comma(_PLACE_VALUES[target_pos])} = {_fmt_comma(value)}$.",
            ],
            solution_steps_latex=[
                f"Locate the digit ${target_digit}$ inside ${_fmt_comma(number)}$.",
                f"Count the position from the right: the {place_name} place has a value of ${_fmt_comma(_PLACE_VALUES[target_pos])}$.",
                f"Multiply the digit by its place value: ${target_digit} \\times {_fmt_comma(_PLACE_VALUES[target_pos])} = {_fmt_comma(value)}$.",
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )


@register
class RoundWholeNumber(Generator):
    """Round a whole number to the nearest 10, 100, 1000, or 10000.

    Backward construction: pick the place, pick a base number with the
    appropriate magnitude, then optionally add a "nudge" (including
    cases where rounding carries into the next place).
    """
    generator_id = "round_whole_number"
    topic_slug = "place_value_rounding_and_estimation"
    display_name = "Round a whole number to a given place"

    # (min_digits, max_digits, allowed_places) --- place is the exponent of 10
    _PARAMS = {
        "easy": {"min_digits": 3, "max_digits": 4, "places": (1, 2)},           # tens / hundreds
        "medium": {"min_digits": 4, "max_digits": 5, "places": (2, 3)},         # hundreds / thousands
        "hard": {"min_digits": 5, "max_digits": 6, "places": (3, 4)},           # thousands / ten thousands
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        num_digits = rng.randint(params["min_digits"], params["max_digits"])
        place_exp = rng.choice(params["places"])
        place_val = 10 ** place_exp
        place_name = _PLACE_NAMES[place_exp]

        # Pick a random number in [10^(num_digits-1), 10^num_digits - 1]
        lo = 10 ** (num_digits - 1)
        hi = 10 ** num_digits - 1
        number = rng.randint(lo, hi)

        # Standard "round half up" rounding. We must be careful: bankers
        # rounding would confuse students; use the schoolbook rule.
        remainder = number % place_val
        down = number - remainder
        up = down + place_val
        if remainder * 2 >= place_val:
            rounded = up
        else:
            rounded = down

        # For easy problems, avoid the exact-half edge case
        if difficulty == "easy" and remainder * 2 == place_val:
            number += 1
            remainder = number % place_val
            down = number - remainder
            up = down + place_val
            rounded = up if remainder * 2 >= place_val else down

        # Digit check: the tie-breaker digit at position place_exp - 1 (if any)
        if place_exp >= 1:
            tiebreak_digit = (number // (place_val // 10)) % 10
        else:
            tiebreak_digit = 0

        if tiebreak_digit >= 5:
            round_rule = (
                f"The digit immediately to the right of the {place_name} place is ${tiebreak_digit}$, "
                f"which is $5$ or greater, so round up."
            )
        else:
            round_rule = (
                f"The digit immediately to the right of the {place_name} place is ${tiebreak_digit}$, "
                f"which is less than $5$, so round down."
            )

        statement = f"Round ${_fmt_comma(number)}$ to the nearest ${_fmt_comma(place_val)}$."
        answer = f"${_fmt_comma(rounded)}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (number, place_exp)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Find the digit in the {place_name} place of ${_fmt_comma(number)}$.",
                "Look at the digit immediately to the right of that place: $0$-$4$ means round down, $5$-$9$ means round up.",
                round_rule,
            ],
            solution_steps_latex=[
                f"Identify the {place_name} place in ${_fmt_comma(number)}$ (value ${_fmt_comma(place_val)}$).",
                round_rule,
                f"Replace every digit to the right of the {place_name} place with $0$ and apply the rule: ${_fmt_comma(number)} \\to {_fmt_comma(rounded)}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class EstimateSumByRounding(Generator):
    """Estimate $a + b$ by rounding each addend to the same place, then adding.

    Backward construction: pick the rounding place first, then pick two
    numbers whose rounded values differ from the exact sum by a
    reasonable amount (so students see the benefit of estimation).
    """
    generator_id = "estimate_sum_by_rounding"
    topic_slug = "place_value_rounding_and_estimation"
    display_name = "Estimate a sum by rounding each addend"

    _PARAMS = {
        "easy": {"place_exp": 1, "lo": 20, "hi": 99},            # round to tens, two-digit numbers
        "medium": {"place_exp": 2, "lo": 200, "hi": 999},        # round to hundreds, three-digit numbers
        "hard": {"place_exp": 3, "lo": 2000, "hi": 9999},        # round to thousands, four-digit numbers
    }

    def _round_half_up(self, n: int, place_val: int) -> int:
        remainder = n % place_val
        down = n - remainder
        up = down + place_val
        return up if remainder * 2 >= place_val else down

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        place_exp = params["place_exp"]
        place_val = 10 ** place_exp
        place_name = _PLACE_NAMES[place_exp]

        a = rng.randint(params["lo"], params["hi"])
        b = rng.randint(params["lo"], params["hi"])

        a_rounded = self._round_half_up(a, place_val)
        b_rounded = self._round_half_up(b, place_val)
        estimated = a_rounded + b_rounded
        actual = a + b

        statement = (
            f"Estimate ${_fmt_comma(a)} + {_fmt_comma(b)}$ by rounding each number to the nearest "
            f"${_fmt_comma(place_val)}$."
        )
        answer = f"${_fmt_comma(estimated)}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, place_exp)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Round each number to the nearest ${_fmt_comma(place_val)}$ ({place_name}) first.",
                f"${_fmt_comma(a)}$ rounds to ${_fmt_comma(a_rounded)}$ and ${_fmt_comma(b)}$ rounds to ${_fmt_comma(b_rounded)}$.",
                f"Then add the rounded values: ${_fmt_comma(a_rounded)} + {_fmt_comma(b_rounded)} = {_fmt_comma(estimated)}$. The exact sum is ${_fmt_comma(actual)}$ for reference.",
            ],
            solution_steps_latex=[
                f"Round ${_fmt_comma(a)}$ to the nearest ${_fmt_comma(place_val)}$: ${_fmt_comma(a)} \\to {_fmt_comma(a_rounded)}$.",
                f"Round ${_fmt_comma(b)}$ to the nearest ${_fmt_comma(place_val)}$: ${_fmt_comma(b)} \\to {_fmt_comma(b_rounded)}$.",
                f"Add the rounded numbers: ${_fmt_comma(a_rounded)} + {_fmt_comma(b_rounded)} = {_fmt_comma(estimated)}$.",
                f"Estimated sum: ${_fmt_comma(estimated)}$ (exact sum is ${_fmt_comma(actual)}$).",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


# ===========================================================================
# Topic 2: square_roots_and_cube_roots
# ===========================================================================

@register
class SquareRootOfPerfectSquare(Generator):
    """Given $n^2$, find $n$. Backward construction: pick $n$, present $n^2$.

    Small parameter spaces: easy has 12 values (n in [1, 12]), medium 20,
    hard 30. ``bank_count_per_difficulty`` caps the batch size accordingly.
    """
    generator_id = "square_root_of_perfect_square"
    topic_slug = "square_roots_and_cube_roots"
    display_name = "Square root of a perfect square"
    bank_count_per_difficulty = 12  # easy only has 12 perfect squares

    _PARAMS = {
        "easy": {"n_lo": 1, "n_hi": 12},
        "medium": {"n_lo": 1, "n_hi": 20},
        "hard": {"n_lo": 1, "n_hi": 30},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        n = rng.randint(params["n_lo"], params["n_hi"])
        square = n * n

        statement = f"Compute $\\sqrt{{{_fmt_comma(square)}}}$."
        answer = f"${n}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "The square root of a number is the value whose square equals that number.",
                f"Ask: what positive integer squared equals ${_fmt_comma(square)}$?",
                f"${n} \\times {n} = {_fmt_comma(square)}$, so $\\sqrt{{{_fmt_comma(square)}}} = {n}$.",
            ],
            solution_steps_latex=[
                f"We want the number whose square is ${_fmt_comma(square)}$.",
                f"Check: ${n}^2 = {n} \\times {n} = {_fmt_comma(square)}$.",
                f"Therefore $\\sqrt{{{_fmt_comma(square)}}} = {n}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class CubeRootOfPerfectCube(Generator):
    """Given $n^3$, find $n$. Includes negative cube roots since $(-n)^3 = -n^3$.

    Easy: |n| in [1, 5] plus sign -> 10 unique values.
    Hard: |n| in [1, 10] plus sign -> 20 unique values.
    """
    generator_id = "cube_root_of_perfect_cube"
    topic_slug = "square_roots_and_cube_roots"
    display_name = "Cube root of a perfect cube"
    bank_count_per_difficulty = 10  # easy only has 10 signed cubes

    _PARAMS = {
        "easy": {"n_max": 5},
        "medium": {"n_max": 8},
        "hard": {"n_max": 10},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        magnitude = rng.randint(1, params["n_max"])
        sign = rng.choice([-1, 1])
        n = sign * magnitude
        cube = n ** 3  # signed cube

        if cube < 0:
            cube_latex = f"-{_fmt_comma(-cube)}"
        else:
            cube_latex = _fmt_comma(cube)

        statement = f"Compute $\\sqrt[3]{{{cube_latex}}}$."
        answer = f"${n}$"

        if n < 0:
            sign_note = (
                "The cube root of a negative number is negative, since a negative number cubed is negative."
            )
        else:
            sign_note = "The cube of a positive number is positive."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "The cube root of a number is the value whose cube equals that number.",
                sign_note,
                f"$({n})^3 = {n} \\times {n} \\times {n} = {cube_latex}$, so $\\sqrt[3]{{{cube_latex}}} = {n}$.",
            ],
            solution_steps_latex=[
                f"We want the number whose cube is ${cube_latex}$.",
                sign_note,
                f"Check: $({n})^3 = {n} \\times {n} \\times {n} = {cube_latex}$.",
                f"Therefore $\\sqrt[3]{{{cube_latex}}} = {n}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class EstimateSquareRoot(Generator):
    """Given a non-perfect square $m$, find consecutive integers $n, n+1$ with $n^2 < m < (n+1)^2$.

    Backward construction: pick $n$, then pick $m$ strictly between
    $n^2$ and $(n+1)^2$.
    """
    generator_id = "estimate_square_root"
    topic_slug = "square_roots_and_cube_roots"
    display_name = "Estimate a square root between two consecutive integers"

    _PARAMS = {
        "easy": {"n_lo": 2, "n_hi": 9},      # target integer between 2 and 9
        "medium": {"n_lo": 4, "n_hi": 15},   # target integer between 4 and 15
        "hard": {"n_lo": 6, "n_hi": 25},     # target integer between 6 and 25
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        n = rng.randint(params["n_lo"], params["n_hi"])
        low_sq = n * n
        high_sq = (n + 1) * (n + 1)
        # Pick m strictly between n^2 and (n+1)^2
        m = rng.randint(low_sq + 1, high_sq - 1)

        statement = (
            f"The number ${_fmt_comma(m)}$ is not a perfect square. "
            f"Between which two consecutive positive integers does $\\sqrt{{{_fmt_comma(m)}}}$ lie?"
        )
        answer = f"${n} < \\sqrt{{{_fmt_comma(m)}}} < {n + 1}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Find the largest perfect square that is less than ${_fmt_comma(m)}$, and the smallest perfect square that is greater than ${_fmt_comma(m)}$.",
                f"${n}^2 = {_fmt_comma(low_sq)}$ and ${n + 1}^2 = {_fmt_comma(high_sq)}$, so ${_fmt_comma(m)}$ falls between them.",
                f"Since ${_fmt_comma(low_sq)} < {_fmt_comma(m)} < {_fmt_comma(high_sq)}$, the square root satisfies ${n} < \\sqrt{{{_fmt_comma(m)}}} < {n + 1}$.",
            ],
            solution_steps_latex=[
                f"List perfect squares near ${_fmt_comma(m)}$: ${n}^2 = {_fmt_comma(low_sq)}$ and ${n + 1}^2 = {_fmt_comma(high_sq)}$.",
                f"Check: ${_fmt_comma(low_sq)} < {_fmt_comma(m)} < {_fmt_comma(high_sq)}$.",
                f"Taking square roots preserves the inequality: $\\sqrt{{{_fmt_comma(low_sq)}}} < \\sqrt{{{_fmt_comma(m)}}} < \\sqrt{{{_fmt_comma(high_sq)}}}$.",
                f"Therefore ${n} < \\sqrt{{{_fmt_comma(m)}}} < {n + 1}$.",
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )
