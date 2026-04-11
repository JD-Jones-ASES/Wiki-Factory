"""Convert repeating decimals to fractions in lowest terms.

Canonical topic slug ``repeating_decimals_as_fractions`` at
wiki/topics/pre_algebra/Repeating_Decimals_As_Fractions.md.

- single_period_repeating_to_fraction: $0.\\overline{d}$ for $d \\in \\{1..8\\}$
- two_digit_repeating_to_fraction: $0.\\overline{ab}$ for clean two-digit periods
- mixed_repeating_to_fraction: $0.a\\overline{b}$ (one non-repeating, one repeating)

All conversions use Python's ``fractions.Fraction`` for auto-simplification,
then render the result with ``\\dfrac``. Backward construction picks the
numerator digits directly; the conversion formulae are exact so no
round-trip verification is needed.
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "repeating_decimals_as_fractions"

_TAGS = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-algebraic-manipulation",
]


def _fraction_latex(frac: Fraction) -> str:
    """Render a positive Fraction as a LaTeX ``\\dfrac`` or bare integer."""
    if frac.denominator == 1:
        return f"{frac.numerator}"
    return f"\\dfrac{{{frac.numerator}}}{{{frac.denominator}}}"


# ---------------------------------------------------------------------------

@register
class SinglePeriodRepeatingToFraction(Generator):
    """Convert $0.\\overline{d}$ to a fraction in lowest terms for $d \\in 1..8$.

    Only 8 distinct values exist, so ``bank_count_per_difficulty`` is set
    to 8 (pytest's floor is 5, ceiling collapses to min(10, 8) = 8).
    """
    generator_id = "single_period_repeating_to_fraction"
    topic_slug = TOPIC_SLUG
    display_name = "Convert a single-digit repeating decimal to a fraction"

    bank_count_per_difficulty = 8

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        d = rng.randint(1, 8)
        frac = Fraction(d, 9)  # Fraction auto-simplifies
        answer_latex = _fraction_latex(frac)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (d,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Express $0.\\overline{{{d}}}$ as a fraction in lowest terms."
            ),
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"Let $x = 0.\overline{d}$. Multiply both sides by $10$ "
                    r"so one full period moves to the left of the decimal point."
                ),
                (
                    r"Subtract the original equation from the multiplied one. "
                    r"The repeating tails cancel, leaving $9x = d$."
                ),
                f"Here $d = {d}$, so $x = \\dfrac{{{d}}}{{9}}$, which simplifies to ${answer_latex}$.",
            ],
            solution_steps_latex=[
                f"Let $x = 0.\\overline{{{d}}}$.",
                f"Multiply by $10$: $10x = {d}.\\overline{{{d}}}$.",
                f"Subtract: $10x - x = {d}.\\overline{{{d}}} - 0.\\overline{{{d}}}$, so $9x = {d}$.",
                f"Solve: $x = \\dfrac{{{d}}}{{9}} = {answer_latex}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

def _valid_two_digit_periods(lo: int, hi: int) -> list[int]:
    """All integers in ``[lo, hi]`` whose period is genuinely two digits.

    Skips multiples of $11$ (they simplify to a single-digit repeating
    form: e.g. $0.\\overline{22} = 2/9 = 0.\\overline{2}$), so the student
    always sees a true two-period problem.
    """
    return [n for n in range(lo, hi + 1) if n % 11 != 0]


@register
class TwoDigitRepeatingToFraction(Generator):
    """Convert $0.\\overline{ab}$ to a fraction in lowest terms.

    Method: $x = 0.\\overline{ab}$, $100x = ab.\\overline{ab}$, so
    $99x = ab$ and $x = ab/99$. Then auto-simplify.
    """
    generator_id = "two_digit_repeating_to_fraction"
    topic_slug = TOPIC_SLUG
    display_name = "Convert a two-digit repeating decimal to a fraction"

    _TABLES = {
        "easy":   _valid_two_digit_periods(10, 49),
        "medium": _valid_two_digit_periods(15, 75),
        "hard":   _valid_two_digit_periods(10, 98),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        table = self._TABLES[difficulty]
        n = table[rng.randrange(len(table))]
        period = f"{n:02d}"  # ensures two-digit rendering, e.g. '09' or '27'
        frac = Fraction(n, 99)
        answer_latex = _fraction_latex(frac)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Express $0.\\overline{{{period}}}$ as a fraction in lowest terms."
            ),
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"Let $x = 0.\overline{ab}$. The period has two digits, "
                    r"so multiply by $100$ to shift one full period."
                ),
                (
                    r"Subtract the original equation from the multiplied one. "
                    r"The tails cancel, leaving $99x = ab$."
                ),
                f"Here the two-digit period is ${period}$, so $x = \\dfrac{{{n}}}{{99}}$, "
                f"which simplifies to ${answer_latex}$.",
            ],
            solution_steps_latex=[
                f"Let $x = 0.\\overline{{{period}}}$.",
                f"Multiply by $100$: $100x = {period}.\\overline{{{period}}}$.",
                f"Subtract: $100x - x = {period}.\\overline{{{period}}} - 0.\\overline{{{period}}}$, "
                f"so $99x = {n}$.",
                f"Solve: $x = \\dfrac{{{n}}}{{99}} = {answer_latex}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class MixedRepeatingToFraction(Generator):
    """Convert $0.a\\overline{b}$ (one non-repeating digit, one repeating).

    Method: let $x = 0.a\\overline{b}$, then
    $10x = a.\\overline{b}$ and $100x = \\overline{ab}.\\overline{b}$, so
    $100x - 10x = 90x = ab - a$, giving $x = (ab - a)/90$.
    Parameter space: $a \\in 0..4$ (5 values) and $b \\in 1..8$ (8 values)
    gives $40$ combinations, well above the $10$ floor.
    """
    generator_id = "mixed_repeating_to_fraction"
    topic_slug = TOPIC_SLUG
    display_name = "Convert a mixed (one-digit delayed) repeating decimal"

    bank_count_per_difficulty = 20

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.randint(0, 4)  # non-repeating leading digit after the point
        b = rng.randint(1, 8)  # repeating digit (not 0, not 9)
        ab = 10 * a + b  # the two-digit integer `ab`
        numerator = ab - a  # by the derivation above
        frac = Fraction(numerator, 90)
        answer_latex = _fraction_latex(frac)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Express $0.{a}\\overline{{{b}}}$ as a fraction in lowest terms."
            ),
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"One digit is non-repeating and one digit repeats, so "
                    r"multiply by $10$ to shift past the non-repeating digit, "
                    r"and multiply by $100$ to shift a full period."
                ),
                (
                    f"Setting $x = 0.{a}\\overline{{{b}}}$, we get "
                    f"$10x = {a}.\\overline{{{b}}}$ and "
                    f"$100x = {ab}.\\overline{{{b}}}$."
                ),
                (
                    f"Subtract: $100x - 10x = {ab} - {a}$, so "
                    f"$90x = {numerator}$ and $x = \\dfrac{{{numerator}}}{{90}}$, "
                    f"which simplifies to ${answer_latex}$."
                ),
            ],
            solution_steps_latex=[
                f"Let $x = 0.{a}\\overline{{{b}}}$.",
                f"Multiply by $10$ to clear the non-repeating digit: "
                f"$10x = {a}.\\overline{{{b}}}$.",
                f"Multiply by $100$ to shift one full period: "
                f"$100x = {ab}.\\overline{{{b}}}$.",
                f"Subtract: $100x - 10x = {ab} - {a}$, giving $90x = {numerator}$.",
                f"Solve: $x = \\dfrac{{{numerator}}}{{90}} = {answer_latex}$.",
            ],
            tags=list(_TAGS),
        )
