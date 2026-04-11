"""Unit-of-measurement conversion generators.

Three generators for the ``units_of_measurement_and_conversion`` topic:

- ``length_conversion``: convert between length units (inches<->feet,
  feet<->yards, feet<->miles, cm<->m, m<->km, inches<->cm).
- ``time_conversion``: convert between time units (seconds<->minutes,
  minutes<->hours, hours<->days).
- ``mass_or_weight_conversion``: convert between mass/weight units
  (ounces<->pounds, pounds<->tons, grams<->kilograms, mg<->g).

Each generator uses backward construction: pick the result first (in
the target unit), then derive the starting quantity so the answer is
always a clean integer.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "units_of_measurement_and_conversion"


# ---------------------------------------------------------------------------

# Each table entry: (small_unit, small_unit_plural, large_unit, large_unit_plural, ratio)
# meaning ``ratio`` small_units = ``1`` large_unit.
_LENGTH_TABLE: tuple[tuple[str, str, str, str, int], ...] = (
    ("inch", "inches", "foot", "feet", 12),
    ("foot", "feet", "yard", "yards", 3),
    ("foot", "feet", "mile", "miles", 5280),
    ("centimeter", "centimeters", "meter", "meters", 100),
    ("meter", "meters", "kilometer", "kilometers", 1000),
    ("millimeter", "millimeters", "centimeter", "centimeters", 10),
)


@register
class LengthConversion(Generator):
    """Convert between units of length (all integer answers).

    Backward construction: pick the answer in the target unit, then
    derive the starting quantity. Both conversion directions are
    supported by choosing which unit is the "starting" unit.
    """
    generator_id = "length_conversion"
    topic_slug = TOPIC_SLUG
    display_name = "Convert between units of length"

    _COUNT_RANGES = {"easy": (2, 12), "medium": (3, 22), "hard": (4, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        small, smalls, large, larges, ratio = rng.choice(_LENGTH_TABLE)
        direction = rng.choice(("small_to_large", "large_to_small"))
        lo, hi = self._COUNT_RANGES[difficulty]
        n = rng.randint(lo, hi)

        if direction == "small_to_large":
            # Answer is n large units; starting quantity is n*ratio small.
            start_value = n * ratio
            start_unit_plural = smalls
            answer_value = n
            answer_unit = larges if n != 1 else large
            ratio_phrase = (
                f"${ratio}\\text{{ {smalls}}} = 1\\text{{ {large}}}$"
            )
            statement = (
                f"Convert ${start_value}$ {start_unit_plural} to {larges}."
            )
            solution_steps = [
                (
                    f"Recall that {ratio_phrase}."
                ),
                (
                    f"To convert {smalls} to {larges}, divide by ${ratio}$: "
                    f"$\\dfrac{{{start_value}}}{{{ratio}}}$."
                ),
                (
                    f"Simplify: $\\dfrac{{{start_value}}}{{{ratio}}} = "
                    f"{answer_value}$ {answer_unit}."
                ),
            ]
            hints = [
                (
                    f"There are ${ratio}$ {smalls} in $1$ {large}."
                ),
                (
                    f"Divide the number of {smalls} by ${ratio}$ to get "
                    f"the number of {larges}."
                ),
                (
                    f"Compute $\\dfrac{{{start_value}}}{{{ratio}}}$."
                ),
            ]
        else:
            # Answer is n*ratio small units; starting quantity is n large.
            start_value = n
            start_unit_plural = larges if n != 1 else large
            answer_value = n * ratio
            answer_unit = smalls
            ratio_phrase = (
                f"$1\\text{{ {large}}} = {ratio}\\text{{ {smalls}}}$"
            )
            statement = (
                f"Convert ${start_value}$ {start_unit_plural} to {smalls}."
            )
            solution_steps = [
                (
                    f"Recall that {ratio_phrase}."
                ),
                (
                    f"To convert {larges} to {smalls}, multiply by ${ratio}$: "
                    f"${start_value} \\cdot {ratio}$."
                ),
                (
                    f"Simplify: ${start_value} \\cdot {ratio} = "
                    f"{answer_value}$ {answer_unit}."
                ),
            ]
            hints = [
                (
                    f"There are ${ratio}$ {smalls} in $1$ {large}."
                ),
                (
                    f"Multiply the number of {larges} by ${ratio}$ to get "
                    f"the number of {smalls}."
                ),
                (
                    f"Compute ${start_value} \\cdot {ratio}$."
                ),
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (small, large, direction, n),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_value}$ {answer_unit}",
            hints=hints,
            solution_steps_latex=solution_steps,
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

_TIME_TABLE: tuple[tuple[str, str, str, str, int], ...] = (
    ("second", "seconds", "minute", "minutes", 60),
    ("minute", "minutes", "hour", "hours", 60),
    ("hour", "hours", "day", "days", 24),
    ("day", "days", "week", "weeks", 7),
)


@register
class TimeConversion(Generator):
    """Convert between units of time (all integer answers)."""
    generator_id = "time_conversion"
    topic_slug = TOPIC_SLUG
    display_name = "Convert between units of time"

    _COUNT_RANGES = {"easy": (2, 10), "medium": (3, 18), "hard": (4, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        small, smalls, large, larges, ratio = rng.choice(_TIME_TABLE)
        direction = rng.choice(("small_to_large", "large_to_small"))
        lo, hi = self._COUNT_RANGES[difficulty]
        n = rng.randint(lo, hi)

        if direction == "small_to_large":
            start_value = n * ratio
            start_unit_plural = smalls
            answer_value = n
            answer_unit = larges if n != 1 else large
            ratio_phrase = (
                f"${ratio}\\text{{ {smalls}}} = 1\\text{{ {large}}}$"
            )
            statement = (
                f"Convert ${start_value}$ {start_unit_plural} to {larges}."
            )
            solution_steps = [
                (
                    f"Recall that {ratio_phrase}."
                ),
                (
                    f"Divide the number of {smalls} by ${ratio}$: "
                    f"$\\dfrac{{{start_value}}}{{{ratio}}}$."
                ),
                (
                    f"Simplify: $\\dfrac{{{start_value}}}{{{ratio}}} = "
                    f"{answer_value}$ {answer_unit}."
                ),
            ]
            hints = [
                (
                    f"There are ${ratio}$ {smalls} in $1$ {large}."
                ),
                (
                    f"Divide by ${ratio}$ to change {smalls} to {larges}."
                ),
                (
                    f"Compute $\\dfrac{{{start_value}}}{{{ratio}}}$."
                ),
            ]
        else:
            start_value = n
            start_unit_plural = larges if n != 1 else large
            answer_value = n * ratio
            answer_unit = smalls
            ratio_phrase = (
                f"$1\\text{{ {large}}} = {ratio}\\text{{ {smalls}}}$"
            )
            statement = (
                f"Convert ${start_value}$ {start_unit_plural} to {smalls}."
            )
            solution_steps = [
                (
                    f"Recall that {ratio_phrase}."
                ),
                (
                    f"Multiply the number of {larges} by ${ratio}$: "
                    f"${start_value} \\cdot {ratio}$."
                ),
                (
                    f"Simplify: ${start_value} \\cdot {ratio} = "
                    f"{answer_value}$ {answer_unit}."
                ),
            ]
            hints = [
                (
                    f"There are ${ratio}$ {smalls} in $1$ {large}."
                ),
                (
                    f"Multiply by ${ratio}$ to change {larges} to {smalls}."
                ),
                (
                    f"Compute ${start_value} \\cdot {ratio}$."
                ),
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (small, large, direction, n),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_value}$ {answer_unit}",
            hints=hints,
            solution_steps_latex=solution_steps,
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------

_MASS_TABLE: tuple[tuple[str, str, str, str, int], ...] = (
    ("ounce", "ounces", "pound", "pounds", 16),
    ("pound", "pounds", "ton", "tons", 2000),
    ("gram", "grams", "kilogram", "kilograms", 1000),
    ("milligram", "milligrams", "gram", "grams", 1000),
)


@register
class MassOrWeightConversion(Generator):
    """Convert between units of mass or weight (all integer answers)."""
    generator_id = "mass_or_weight_conversion"
    topic_slug = TOPIC_SLUG
    display_name = "Convert between units of mass or weight"

    _COUNT_RANGES = {"easy": (2, 10), "medium": (3, 18), "hard": (4, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        small, smalls, large, larges, ratio = rng.choice(_MASS_TABLE)
        direction = rng.choice(("small_to_large", "large_to_small"))
        lo, hi = self._COUNT_RANGES[difficulty]
        n = rng.randint(lo, hi)

        if direction == "small_to_large":
            start_value = n * ratio
            start_unit_plural = smalls
            answer_value = n
            answer_unit = larges if n != 1 else large
            ratio_phrase = (
                f"${ratio}\\text{{ {smalls}}} = 1\\text{{ {large}}}$"
            )
            statement = (
                f"Convert ${start_value}$ {start_unit_plural} to {larges}."
            )
            solution_steps = [
                (
                    f"Recall that {ratio_phrase}."
                ),
                (
                    f"Divide by ${ratio}$: $\\dfrac{{{start_value}}}"
                    f"{{{ratio}}}$."
                ),
                (
                    f"Simplify: $\\dfrac{{{start_value}}}{{{ratio}}} = "
                    f"{answer_value}$ {answer_unit}."
                ),
            ]
            hints = [
                (
                    f"There are ${ratio}$ {smalls} in $1$ {large}."
                ),
                (
                    f"Divide by ${ratio}$ to change {smalls} to {larges}."
                ),
                (
                    f"Compute $\\dfrac{{{start_value}}}{{{ratio}}}$."
                ),
            ]
        else:
            start_value = n
            start_unit_plural = larges if n != 1 else large
            answer_value = n * ratio
            answer_unit = smalls
            ratio_phrase = (
                f"$1\\text{{ {large}}} = {ratio}\\text{{ {smalls}}}$"
            )
            statement = (
                f"Convert ${start_value}$ {start_unit_plural} to {smalls}."
            )
            solution_steps = [
                (
                    f"Recall that {ratio_phrase}."
                ),
                (
                    f"Multiply by ${ratio}$: ${start_value} \\cdot {ratio}$."
                ),
                (
                    f"Simplify: ${start_value} \\cdot {ratio} = "
                    f"{answer_value}$ {answer_unit}."
                ),
            ]
            hints = [
                (
                    f"There are ${ratio}$ {smalls} in $1$ {large}."
                ),
                (
                    f"Multiply by ${ratio}$ to change {larges} to {smalls}."
                ),
                (
                    f"Compute ${start_value} \\cdot {ratio}$."
                ),
            ]

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (small, large, direction, n),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_value}$ {answer_unit}",
            hints=hints,
            solution_steps_latex=solution_steps,
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-formula-substitution",
            ],
        )
