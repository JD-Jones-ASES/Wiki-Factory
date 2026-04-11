"""Polynomial division generators (Phase 2c Wave B).

Canonical topic slug ``polynomial_division`` at
wiki/topics/algebra/Polynomial_Division.md.

- long_divide_polynomial_no_remainder: P(x) / (x - c) with remainder 0.
- long_divide_polynomial_with_remainder: P(x) / (x - c) with a numeric remainder.
- synthetic_division_by_linear: synthetic division of P(x) by (x - c).

All generators use backward construction: pick the quotient ``Q(x)``, the
divisor ``(x - c)``, and (optionally) the integer remainder ``r`` first, then
assemble the dividend as ``Q(x) * (x - c) + r`` so the arithmetic is clean by
construction.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


def _format_linear_divisor(c: int) -> str:
    """Format $(x - c)$ with the correct sign for display."""
    if c >= 0:
        return f"(x - {c})"
    return f"(x + {abs(c)})"


# ---------------------------------------------------------------------------
# Topic: polynomial_division
# ---------------------------------------------------------------------------


@register
class LongDividePolynomialNoRemainder(Generator):
    """Divide a polynomial by a linear divisor with remainder 0.

    Backward construction:
        1. Pick a quotient polynomial Q(x) of chosen degree.
        2. Pick an integer root ``c`` for the divisor ``(x - c)``.
        3. Dividend = Q(x) * (x - c) (expanded).
    """
    generator_id = "long_divide_polynomial_no_remainder"
    topic_slug = "polynomial_division"
    display_name = "Long divide a polynomial (no remainder)"
    bank_count_per_difficulty = 25

    _C_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _Q_COEF = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _Q_DEG = {"easy": 1, "medium": 2, "hard": 2}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._C_RANGE[difficulty]
        q_lo, q_hi = self._Q_COEF[difficulty]
        q_deg = self._Q_DEG[difficulty]

        # Divisor root c, non-zero to keep things interesting.
        c = 0
        while c == 0:
            c = rng.randint(c_lo, c_hi)
        # Quotient coefficients (leading term non-zero).
        q_coefs: list[int] = []
        while True:
            lead = rng.randint(q_lo, q_hi)
            if lead != 0:
                q_coefs = [lead]
                break
        for _ in range(q_deg):
            q_coefs.append(rng.randint(q_lo, q_hi))

        quotient_expr = sum(q_coefs[i] * x ** (q_deg - i) for i in range(q_deg + 1))
        divisor_expr = x - c
        dividend_expr = sp.expand(quotient_expr * divisor_expr)

        dividend_latex = sp.latex(dividend_expr)
        divisor_latex = _format_linear_divisor(c)
        quotient_latex = sp.latex(sp.expand(quotient_expr))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (c, tuple(q_coefs)),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Divide ${dividend_latex}$ by ${divisor_latex}$ using polynomial long division."
            ),
            answer_latex=f"${quotient_latex}$",
            hints=[
                "Set up the long division just as you would with whole numbers. Write the dividend under the long-division bar in descending powers of $x$.",
                f"Divide the leading term of the dividend by the leading term of the divisor ($x$). That gives the first term of the quotient: ${sp.latex(q_coefs[0] * x ** q_deg)}$.",
                "Multiply the divisor by that first term, subtract, bring down the next term, and repeat until the remainder is zero.",
            ],
            solution_steps_latex=[
                f"Set up long division of ${dividend_latex}$ by ${divisor_latex}$.",
                f"Divide the leading terms: ${sp.latex(q_coefs[0] * x ** q_deg)} \\cdot {divisor_latex}$ is subtracted from the dividend.",
                "Repeat: bring down each lower-degree term and divide again, so every step cancels cleanly.",
                f"The quotient is ${quotient_latex}$ with remainder $0$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-polynomials",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class LongDividePolynomialWithRemainder(Generator):
    """Divide a polynomial by a linear divisor with a non-zero remainder.

    Backward construction: pick Q(x), c, and a small integer remainder r.
    Dividend = Q(x) * (x - c) + r.
    """
    generator_id = "long_divide_polynomial_with_remainder"
    topic_slug = "polynomial_division"
    display_name = "Long divide a polynomial (with remainder)"

    _C_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _Q_COEF = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _R_RANGE = {"easy": (-9, 9), "medium": (-15, 15), "hard": (-25, 25)}
    _Q_DEG = {"easy": 1, "medium": 2, "hard": 2}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._C_RANGE[difficulty]
        q_lo, q_hi = self._Q_COEF[difficulty]
        r_lo, r_hi = self._R_RANGE[difficulty]
        q_deg = self._Q_DEG[difficulty]

        c = 0
        while c == 0:
            c = rng.randint(c_lo, c_hi)
        q_coefs: list[int] = []
        while True:
            lead = rng.randint(q_lo, q_hi)
            if lead != 0:
                q_coefs = [lead]
                break
        for _ in range(q_deg):
            q_coefs.append(rng.randint(q_lo, q_hi))
        # Non-zero remainder.
        r = 0
        while r == 0:
            r = rng.randint(r_lo, r_hi)

        quotient_expr = sum(q_coefs[i] * x ** (q_deg - i) for i in range(q_deg + 1))
        divisor_expr = x - c
        dividend_expr = sp.expand(quotient_expr * divisor_expr + r)

        dividend_latex = sp.latex(dividend_expr)
        divisor_latex = _format_linear_divisor(c)
        quotient_latex = sp.latex(sp.expand(quotient_expr))
        answer = (
            f"{quotient_latex} + \\dfrac{{{r}}}{{{divisor_latex[1:-1]}}}"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (c, tuple(q_coefs), r),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Divide ${dividend_latex}$ by ${divisor_latex}$ using polynomial long division. "
                f"Give the quotient and remainder."
            ),
            answer_latex=f"$\\text{{Quotient: }} {quotient_latex}, \\; \\text{{Remainder: }} {r}$",
            hints=[
                "Set up long division with the dividend in descending powers of $x$.",
                "Divide leading terms, multiply the divisor by the new quotient term, subtract, and bring down the next term.",
                "Keep going until what remains has lower degree than the divisor. That is your remainder.",
            ],
            solution_steps_latex=[
                f"Set up long division of ${dividend_latex}$ by ${divisor_latex}$.",
                f"Divide leading term by leading term repeatedly to build the quotient ${quotient_latex}$.",
                f"After the last subtraction, the remainder is ${r}$ (a constant, so division stops).",
                f"Express the result: ${answer}$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-polynomials",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class SyntheticDivisionByLinear(Generator):
    """Synthetic division of P(x) by (x - c).

    Backward: pick Q(x), c, optional small remainder r; dividend is
    Q(x) * (x - c) + r. Synthetic division recovers the Q(x) coefficients
    (and r as the final entry in the bottom row).
    """
    generator_id = "synthetic_division_by_linear"
    topic_slug = "polynomial_division"
    display_name = "Synthetic division of a polynomial by (x - c)"

    _C_RANGE = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-11, 11)}
    _Q_COEF = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _R_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-14, 14)}
    _Q_DEG = {"easy": 1, "medium": 2, "hard": 2}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._C_RANGE[difficulty]
        q_lo, q_hi = self._Q_COEF[difficulty]
        r_lo, r_hi = self._R_RANGE[difficulty]
        q_deg = self._Q_DEG[difficulty]

        c = 0
        while c == 0:
            c = rng.randint(c_lo, c_hi)
        while True:
            lead = rng.randint(q_lo, q_hi)
            if lead != 0:
                q_coefs = [lead]
                break
        for _ in range(q_deg):
            q_coefs.append(rng.randint(q_lo, q_hi))
        r = rng.randint(r_lo, r_hi)

        quotient_expr = sum(q_coefs[i] * x ** (q_deg - i) for i in range(q_deg + 1))
        divisor_expr = x - c
        dividend_expr = sp.expand(quotient_expr * divisor_expr + r)

        dividend_latex = sp.latex(dividend_expr)
        divisor_latex = _format_linear_divisor(c)
        quotient_latex = sp.latex(sp.expand(quotient_expr))

        # Build a tidy display of the bottom row of the synthetic division
        # so the student can see the result shape.
        bottom_row = " \\; | \\; ".join(str(v) for v in (*q_coefs, r))

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (c, tuple(q_coefs), r),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use synthetic division to divide ${dividend_latex}$ by ${divisor_latex}$. "
                f"State the quotient and the remainder."
            ),
            answer_latex=f"$\\text{{Quotient: }} {quotient_latex}, \\; \\text{{Remainder: }} {r}$",
            hints=[
                "Synthetic division uses the value $c$ from the divisor $(x - c)$ (not the full binomial).",
                f"Here the divisor is ${divisor_latex}$, so use $c = {c}$.",
                "Write the coefficients of the dividend in a row. Bring down the first, multiply by $c$, add to the next, and repeat. The final entry is the remainder.",
            ],
            solution_steps_latex=[
                f"Identify $c = {c}$ from the divisor ${divisor_latex}$.",
                f"Write the dividend coefficients in a row: the synthetic division table for ${dividend_latex}$.",
                f"Carry out the algorithm. The bottom row ends up as $\\left[\\; {bottom_row} \\;\\right]$.",
                f"Read off the answer: quotient ${quotient_latex}$, remainder ${r}$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-polynomials",
                "#skill-algebraic-manipulation",
            ],
        )
