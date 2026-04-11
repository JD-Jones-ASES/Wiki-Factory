"""Scientific notation generators (Wave B).

Canonical topic slug ``scientific_notation`` at
wiki/topics/algebra/Scientific_Notation.md.

- convert_standard_to_scientific: large or small decimal -> a x 10^n
- convert_scientific_to_standard: a x 10^n -> standard decimal
- multiply_or_divide_scientific: combine two scientific-notation values
"""
from __future__ import annotations

import random

from decimal import Decimal

from ..base import Difficulty, Generator, Problem, make_problem_id, register


def _format_decimal_plain(dec: Decimal) -> str:
    """Render a Decimal as a plain-text string without scientific notation."""
    # Normalize to avoid trailing noise from Decimal arithmetic.
    s = format(dec, "f")
    # Strip unnecessary trailing zeros after a decimal point.
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s or "0"


@register
class ConvertStandardToScientific(Generator):
    """Rewrite a standard-form decimal number in scientific notation."""
    generator_id = "convert_standard_to_scientific"
    topic_slug = "scientific_notation"
    display_name = "Write a number in scientific notation"

    _COEF_DIGITS = {"easy": (1, 2), "medium": (2, 3), "hard": (2, 4)}
    _EXPONENT_RANGE = {"easy": (2, 5), "medium": (3, 7), "hard": (4, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        d_lo, d_hi = self._COEF_DIGITS[difficulty]
        e_lo, e_hi = self._EXPONENT_RANGE[difficulty]

        # Build the coefficient: 1 digit to the left of the decimal, 0-2 digits after.
        leading = rng.randint(1, 9)
        decimal_count = rng.randint(0, d_hi - 1)
        if decimal_count == 0:
            coef_str = str(leading)
            coef = Decimal(coef_str)
        else:
            frac_digits = "".join(str(rng.randint(0, 9)) for _ in range(decimal_count))
            coef_str = f"{leading}.{frac_digits}"
            coef = Decimal(coef_str)

        # Pick sign of exponent: positive for large numbers, negative for small.
        sign = rng.choice([1, -1])
        exponent = sign * rng.randint(e_lo, e_hi)

        # Build standard-form value = coef * 10^exponent
        value = coef * (Decimal(10) ** exponent)
        standard_str = _format_decimal_plain(value)

        sci_latex = f"{coef_str} \\times 10^{{{exponent}}}"

        if exponent >= 0:
            steps = [
                f"Start with ${standard_str}$.",
                (
                    f"Move the decimal point **{exponent}** place(s) to the "
                    f"**left** so the coefficient is between $1$ and $10$."
                ),
                f"The coefficient becomes ${coef_str}$, and the exponent is ${exponent}$.",
                f"Scientific notation: ${sci_latex}$.",
            ]
            direction = "left"
        else:
            steps = [
                f"Start with ${standard_str}$.",
                (
                    f"Move the decimal point **{-exponent}** place(s) to the "
                    f"**right** so the coefficient is between $1$ and $10$."
                ),
                f"The coefficient becomes ${coef_str}$, and the exponent is ${exponent}$.",
                f"Scientific notation: ${sci_latex}$.",
            ]
            direction = "right"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (coef_str, exponent, standard_str)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Write ${standard_str}$ in scientific notation.",
            answer_latex=f"${sci_latex}$",
            hints=[
                r"Scientific notation has the form $a \times 10^n$ where $1 \leq |a| < 10$.",
                f"Move the decimal point until the coefficient is between $1$ and $10$ (here, to the {direction}).",
                r"The exponent is positive for large numbers and negative for small numbers.",
            ],
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
            ],
        )


@register
class ConvertScientificToStandard(Generator):
    """Rewrite a scientific-notation value as a standard decimal."""
    generator_id = "convert_scientific_to_standard"
    topic_slug = "scientific_notation"
    display_name = "Write a scientific-notation value in standard form"

    _COEF_DIGITS = {"easy": (1, 2), "medium": (2, 3), "hard": (2, 4)}
    _EXPONENT_RANGE = {"easy": (2, 5), "medium": (3, 7), "hard": (4, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        d_lo, d_hi = self._COEF_DIGITS[difficulty]
        e_lo, e_hi = self._EXPONENT_RANGE[difficulty]

        leading = rng.randint(1, 9)
        decimal_count = rng.randint(0, d_hi - 1)
        if decimal_count == 0:
            coef_str = str(leading)
            coef = Decimal(coef_str)
        else:
            frac_digits = "".join(str(rng.randint(0, 9)) for _ in range(decimal_count))
            coef_str = f"{leading}.{frac_digits}"
            coef = Decimal(coef_str)

        sign = rng.choice([1, -1])
        exponent = sign * rng.randint(e_lo, e_hi)

        value = coef * (Decimal(10) ** exponent)
        standard_str = _format_decimal_plain(value)

        sci_latex = f"{coef_str} \\times 10^{{{exponent}}}"

        if exponent >= 0:
            steps = [
                f"Start with ${sci_latex}$.",
                (
                    f"Because the exponent is positive (${exponent}$), move the decimal "
                    f"point **{exponent}** place(s) to the **right**, "
                    "appending zeros as needed."
                ),
                f"The result is ${standard_str}$.",
            ]
            direction = "right"
        else:
            steps = [
                f"Start with ${sci_latex}$.",
                (
                    f"Because the exponent is negative (${exponent}$), move the decimal "
                    f"point **{-exponent}** place(s) to the **left**, "
                    "prepending zeros as needed."
                ),
                f"The result is ${standard_str}$.",
            ]
            direction = "left"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (coef_str, exponent, standard_str)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Express ${sci_latex}$ as a decimal in standard form.",
            answer_latex=f"${standard_str}$",
            hints=[
                r"A positive exponent means the number is large; move the decimal point right.",
                r"A negative exponent means the number is small; move the decimal point left.",
                f"Here the exponent is ${exponent}$, so move the decimal point {abs(exponent)} place(s) to the {direction}.",
            ],
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
            ],
        )


@register
class MultiplyOrDivideScientific(Generator):
    """Multiply or divide two values in scientific notation."""
    generator_id = "multiply_or_divide_scientific"
    topic_slug = "scientific_notation"
    display_name = "Multiply or divide scientific-notation values"

    _COEF_RANGE = {"easy": (2, 9), "medium": (2, 9), "hard": (2, 9)}
    _EXPONENT_RANGE = {"easy": (2, 4), "medium": (3, 6), "hard": (4, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEF_RANGE[difficulty]
        e_lo, e_hi = self._EXPONENT_RANGE[difficulty]

        operation = rng.choice(["multiply", "divide"])

        if operation == "multiply":
            # Pick coefficients so product is between 1 and 100 (requires at most one normalization)
            a1 = rng.randint(c_lo, c_hi)
            a2 = rng.randint(c_lo, c_hi)
            e1 = rng.randint(e_lo, e_hi)
            if rng.random() < 0.4:
                e1 = -e1
            e2 = rng.randint(e_lo, e_hi)
            if rng.random() < 0.4:
                e2 = -e2

            coef_product = a1 * a2
            exponent = e1 + e2
            # Normalize if coefficient is >= 10
            if coef_product >= 10:
                # Strategy: express coef_product as c * 10^k; k = 1 for 10-99
                k = len(str(coef_product)) - 1  # number of digit shifts
                # New coefficient in a \times 10^n form
                final_coef_int = coef_product  # keep as integer
                # coef_product = final_coef_int * 10^0, rewrite as (coef_product / 10^k) * 10^k
                coef_display = f"{final_coef_int / (10 ** k):g}"
                final_exp = exponent + k
            else:
                coef_display = str(coef_product)
                final_exp = exponent

            sci1 = f"{a1} \\times 10^{{{e1}}}"
            sci2 = f"{a2} \\times 10^{{{e2}}}"
            final_sci = f"{coef_display} \\times 10^{{{final_exp}}}"

            statement = f"Compute $({sci1}) \\times ({sci2})$ and write the result in scientific notation."
            hints = [
                r"Multiply the coefficients and add the exponents of $10$.",
                f"Coefficients: ${a1} \\times {a2} = {coef_product}$. Exponents: ${e1} + {e2} = {exponent}$.",
                r"If the resulting coefficient is $\geq 10$, rewrite it as $a \times 10^k$ where $1 \leq a < 10$ and add $k$ to the exponent.",
            ]
            steps = [
                f"Multiply the coefficients: ${a1} \\times {a2} = {coef_product}$.",
                f"Add the exponents of $10$: ${e1} + ({e2}) = {exponent}$.",
                f"Intermediate result: ${coef_product} \\times 10^{{{exponent}}}$.",
            ]
            if coef_product >= 10:
                steps.append(
                    f"Normalize the coefficient: ${coef_product} = {coef_display} \\times 10^{{{final_exp - exponent}}}$, so the final exponent becomes ${final_exp}$."
                )
            steps.append(f"Answer: ${final_sci}$.")

            params = ("mult", a1, e1, a2, e2)
            answer_latex = f"${final_sci}$"

        else:  # divide
            # Pick coefficients so a1 is divisible by a2 (for a clean integer coefficient),
            # and choose exponents freely.
            a2 = rng.randint(c_lo, c_hi)
            multiple = rng.randint(1, c_hi)
            a1 = a2 * multiple
            e1 = rng.randint(e_lo, e_hi)
            if rng.random() < 0.4:
                e1 = -e1
            e2 = rng.randint(e_lo, e_hi)
            if rng.random() < 0.4:
                e2 = -e2

            coef_quotient = a1 // a2  # integer division is exact by construction
            exponent = e1 - e2

            # Normalize if quotient >= 10
            if coef_quotient >= 10:
                k = len(str(coef_quotient)) - 1
                coef_display = f"{coef_quotient / (10 ** k):g}"
                final_exp = exponent + k
            else:
                coef_display = str(coef_quotient)
                final_exp = exponent

            sci1 = f"{a1} \\times 10^{{{e1}}}"
            sci2 = f"{a2} \\times 10^{{{e2}}}"
            final_sci = f"{coef_display} \\times 10^{{{final_exp}}}"

            statement = (
                f"Compute $\\dfrac{{{sci1}}}{{{sci2}}}$ and write the result in scientific notation."
            )
            hints = [
                r"Divide the coefficients and subtract the exponents of $10$.",
                f"Coefficients: ${a1} \\div {a2} = {coef_quotient}$. Exponents: ${e1} - ({e2}) = {exponent}$.",
                r"If the resulting coefficient is $\geq 10$, rewrite it so $1 \leq a < 10$ and adjust the exponent.",
            ]
            steps = [
                f"Divide the coefficients: $\\dfrac{{{a1}}}{{{a2}}} = {coef_quotient}$.",
                f"Subtract the exponents of $10$: ${e1} - ({e2}) = {exponent}$.",
                f"Intermediate result: ${coef_quotient} \\times 10^{{{exponent}}}$.",
            ]
            if coef_quotient >= 10:
                steps.append(
                    f"Normalize: ${coef_quotient} = {coef_display} \\times 10^{{{final_exp - exponent}}}$, so the final exponent becomes ${final_exp}$."
                )
            steps.append(f"Answer: ${final_sci}$.")

            params = ("div", a1, e1, a2, e2)
            answer_latex = f"${final_sci}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=hints,
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
            ],
        )
