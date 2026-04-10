"""Fraction multiplication and division generators (Phase 2c, Cluster 1).

Canonical topic slugs:
- ``multiplying_fractions`` at wiki/topics/pre_algebra/Multiplying_Fractions.md (Math I Ch 4.1)
- ``dividing_fractions`` at wiki/topics/pre_algebra/Dividing_Fractions.md (Math I Ch 4.3)

Multiplying fractions:
- multiply_fractions_simple: (a/b) x (c/d)
- multiply_fraction_by_whole: n x (a/b)
- multiply_three_fractions: (a/b) x (c/d) x (e/f)

Dividing fractions:
- divide_fractions_simple: (a/b) / (c/d), keep-change-flip
- divide_fraction_by_whole: (a/b) / n
- divide_whole_by_fraction: n / (a/b)

All generators use fractions.Fraction for exact arithmetic and construct
problems by picking clean parameters (no backward construction needed here
since rationals are already clean by construction).
"""
from __future__ import annotations

import random
from fractions import Fraction
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# LaTeX helpers
# ---------------------------------------------------------------------------

def _frac_latex(f: Fraction) -> str:
    """Render a Fraction as LaTeX. Whole numbers render as-is, mixed numbers
    render with \\tfrac, proper/improper fractions use \\frac.
    """
    if f.denominator == 1:
        return str(f.numerator)
    n, d = f.numerator, f.denominator
    if n < 0:
        return rf"-\frac{{{-n}}}{{{d}}}"
    return rf"\frac{{{n}}}{{{d}}}"


def _frac_raw(n: int, d: int) -> str:
    """Render an arbitrary numerator/denominator pair as LaTeX (no simplification)."""
    if d == 1:
        return str(n)
    if n < 0:
        return rf"-\frac{{{-n}}}{{{d}}}"
    return rf"\frac{{{n}}}{{{d}}}"


def _mixed_latex(f: Fraction) -> str:
    """Render an improper Fraction as a mixed number in LaTeX.

    For negative fractions, the whole part carries the sign.
    For proper fractions, falls back to plain _frac_latex.
    """
    if f.denominator == 1:
        return str(f.numerator)
    if abs(f.numerator) < f.denominator:
        return _frac_latex(f)
    whole = f.numerator // f.denominator if f.numerator >= 0 else -((-f.numerator) // f.denominator)
    remainder = f.numerator - whole * f.denominator
    if remainder == 0:
        return str(whole)
    # Normalize: |whole| + |remainder|/d with the sign on whole
    abs_remainder = abs(remainder)
    d = f.denominator
    return rf"{whole}\tfrac{{{abs_remainder}}}{{{d}}}"


def _answer_latex(f: Fraction) -> str:
    """Format a Fraction as a $-wrapped answer, using mixed numbers when useful."""
    if f.denominator == 1:
        return f"${f.numerator}$"
    if abs(f.numerator) > f.denominator:
        return f"${_mixed_latex(f)}$"
    return f"${_frac_latex(f)}$"


# ---------------------------------------------------------------------------
# Topic: multiplying_fractions
# ---------------------------------------------------------------------------

@register
class MultiplyFractionsSimple(Generator):
    """Compute (a/b) x (c/d). Both unreduced and simplified forms shown."""
    generator_id = "multiply_fractions_simple"
    topic_slug = "multiplying_fractions"
    display_name = "Multiply two fractions: (a/b) x (c/d)"

    # (num_lo, num_hi, den_lo, den_hi)
    _RANGES = {
        "easy": (1, 6, 2, 8),
        "medium": (1, 10, 2, 12),
        "hard": (1, 14, 2, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi, d_lo, d_hi = self._RANGES[difficulty]
        a = rng.randint(n_lo, n_hi)
        b = rng.randint(d_lo, d_hi)
        c = rng.randint(n_lo, n_hi)
        d = rng.randint(d_lo, d_hi)

        raw_num = a * c
        raw_den = b * d
        result = Fraction(raw_num, raw_den)

        statement = rf"{_frac_raw(a, b)} \times {_frac_raw(c, d)}"

        unreduced_latex = _frac_raw(raw_num, raw_den)

        if result.denominator == raw_den and result.numerator == raw_num:
            # Already in lowest terms
            simplify_line = f"${unreduced_latex}$ is already in lowest terms."
        else:
            simplify_line = (
                f"Simplify: ${unreduced_latex} = {_frac_latex(result)}$."
            )

        answer = _answer_latex(result)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute ${statement}$.",
            answer_latex=answer,
            hints=[
                r"Multiply straight across: multiply the numerators together and the denominators together.",
                rf"Numerator: ${a} \times {c} = {raw_num}$. Denominator: ${b} \times {d} = {raw_den}$.",
                rf"So ${statement} = {unreduced_latex}$. Reduce to lowest terms if possible.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                rf"Multiply numerators and denominators: $\frac{{{a} \times {c}}}{{{b} \times {d}}} = {unreduced_latex}$.",
                simplify_line,
                f"Final answer: {answer}.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class MultiplyFractionByWhole(Generator):
    """Compute n x (a/b). Shows n/1 framing and converts to mixed if > 1."""
    generator_id = "multiply_fraction_by_whole"
    topic_slug = "multiplying_fractions"
    display_name = "Multiply a whole number by a fraction: n x (a/b)"

    _RANGES = {
        "easy": (2, 8, 1, 6, 2, 8),    # n_lo, n_hi, a_lo, a_hi, b_lo, b_hi
        "medium": (2, 15, 1, 9, 2, 12),
        "hard": (3, 25, 1, 12, 2, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi, a_lo, a_hi, b_lo, b_hi = self._RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        raw_num = n * a
        result = Fraction(raw_num, b)

        statement = rf"{n} \times {_frac_raw(a, b)}"
        unreduced = _frac_raw(raw_num, b)

        # Did it simplify?
        if result.denominator == b and result.numerator == raw_num:
            simplify_line = f"${unreduced}$ is already in lowest terms."
        else:
            simplify_line = rf"Simplify: ${unreduced} = {_frac_latex(result)}$."

        # Mixed-number conversion for improper results
        mixed_line = None
        if result.denominator != 1 and abs(result.numerator) > result.denominator:
            mixed_line = rf"Convert to a mixed number: ${_frac_latex(result)} = {_mixed_latex(result)}$."

        answer = _answer_latex(result)

        steps = [
            f"Start with ${statement}$.",
            rf"Write ${n}$ as a fraction: ${n} = \frac{{{n}}}{{1}}$.",
            rf"Multiply straight across: $\frac{{{n}}}{{1}} \times \frac{{{a}}}{{{b}}} = \frac{{{n} \times {a}}}{{1 \times {b}}} = {unreduced}$.",
            simplify_line,
        ]
        if mixed_line is not None:
            steps.append(mixed_line)
        steps.append(f"Final answer: {answer}.")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute ${statement}$.",
            answer_latex=answer,
            hints=[
                rf"Any whole number can be written as a fraction over $1$: ${n} = \frac{{{n}}}{{1}}$.",
                rf"Then multiply straight across: $\frac{{{n}}}{{1}} \times \frac{{{a}}}{{{b}}} = \frac{{{n * a}}}{{{b}}}$.",
                r"Simplify the result, and convert to a mixed number if it is improper.",
            ],
            solution_steps_latex=steps,
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class MultiplyThreeFractions(Generator):
    """Compute (a/b) x (c/d) x (e/f). Cross-cancellation hinted."""
    generator_id = "multiply_three_fractions"
    topic_slug = "multiplying_fractions"
    display_name = "Multiply three fractions: (a/b) x (c/d) x (e/f)"

    _RANGES = {
        "easy": (1, 4, 2, 6),
        "medium": (1, 6, 2, 9),
        "hard": (1, 8, 2, 12),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi, d_lo, d_hi = self._RANGES[difficulty]
        a = rng.randint(n_lo, n_hi)
        b = rng.randint(d_lo, d_hi)
        c = rng.randint(n_lo, n_hi)
        d = rng.randint(d_lo, d_hi)
        e = rng.randint(n_lo, n_hi)
        f = rng.randint(d_lo, d_hi)

        raw_num = a * c * e
        raw_den = b * d * f
        result = Fraction(raw_num, raw_den)

        statement = rf"{_frac_raw(a, b)} \times {_frac_raw(c, d)} \times {_frac_raw(e, f)}"
        unreduced = _frac_raw(raw_num, raw_den)

        if result.denominator == raw_den and result.numerator == raw_num:
            simplify_line = f"${unreduced}$ is already in lowest terms."
        else:
            simplify_line = rf"Simplify: ${unreduced} = {_frac_latex(result)}$."

        answer = _answer_latex(result)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, e, f)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute ${statement}$.",
            answer_latex=answer,
            hints=[
                r"Multiply all three numerators together and all three denominators together.",
                r"Tip: cross-cancel common factors between any numerator and any denominator before multiplying to keep numbers small.",
                rf"Numerator: ${a} \times {c} \times {e} = {raw_num}$. Denominator: ${b} \times {d} \times {f} = {raw_den}$.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                rf"Multiply straight across: $\frac{{{a} \times {c} \times {e}}}{{{b} \times {d} \times {f}}} = {unreduced}$.",
                simplify_line,
                f"Final answer: {answer}.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-multi-step",
                f"#difficulty-{difficulty}",
            ],
        )


# ---------------------------------------------------------------------------
# Topic: dividing_fractions
# ---------------------------------------------------------------------------

@register
class DivideFractionsSimple(Generator):
    """Compute (a/b) / (c/d) via keep-change-flip."""
    generator_id = "divide_fractions_simple"
    topic_slug = "dividing_fractions"
    display_name = "Divide two fractions: (a/b) / (c/d)"

    _RANGES = {
        "easy": (1, 6, 2, 8),
        "medium": (1, 10, 2, 12),
        "hard": (1, 14, 2, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi, d_lo, d_hi = self._RANGES[difficulty]
        a = rng.randint(n_lo, n_hi)
        b = rng.randint(d_lo, d_hi)
        # c cannot be zero; keep >= 1
        c = rng.randint(max(1, n_lo), n_hi)
        d = rng.randint(d_lo, d_hi)

        raw_num = a * d
        raw_den = b * c
        result = Fraction(raw_num, raw_den)

        statement = rf"{_frac_raw(a, b)} \div {_frac_raw(c, d)}"
        reciprocal_latex = _frac_raw(d, c)
        after_flip = rf"{_frac_raw(a, b)} \times {reciprocal_latex}"
        unreduced = _frac_raw(raw_num, raw_den)

        if result.denominator == raw_den and result.numerator == raw_num:
            simplify_line = f"${unreduced}$ is already in lowest terms."
        else:
            simplify_line = rf"Simplify: ${unreduced} = {_frac_latex(result)}$."

        mixed_line = None
        if result.denominator != 1 and abs(result.numerator) > result.denominator:
            mixed_line = rf"As a mixed number: ${_frac_latex(result)} = {_mixed_latex(result)}$."

        answer = _answer_latex(result)

        steps = [
            f"Start with ${statement}$.",
            rf"Apply keep-change-flip: keep the first fraction, change $\div$ to $\times$, and flip the second fraction to its reciprocal: ${after_flip}$.",
            rf"Multiply straight across: $\frac{{{a} \times {d}}}{{{b} \times {c}}} = {unreduced}$.",
            simplify_line,
        ]
        if mixed_line is not None:
            steps.append(mixed_line)
        steps.append(f"Final answer: {answer}.")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute ${statement}$.",
            answer_latex=answer,
            hints=[
                r"To divide by a fraction, multiply by its reciprocal (keep-change-flip).",
                rf"The reciprocal of ${_frac_raw(c, d)}$ is ${reciprocal_latex}$, so the problem becomes ${after_flip}$.",
                r"Now multiply straight across and simplify the result.",
            ],
            solution_steps_latex=steps,
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class DivideFractionByWhole(Generator):
    """Compute (a/b) / n. Reciprocal of n is 1/n, so answer is a/(bn)."""
    generator_id = "divide_fraction_by_whole"
    topic_slug = "dividing_fractions"
    display_name = "Divide a fraction by a whole number: (a/b) / n"

    _RANGES = {
        "easy": (1, 6, 2, 8, 2, 6),    # a_lo, a_hi, b_lo, b_hi, n_lo, n_hi
        "medium": (1, 10, 2, 12, 2, 9),
        "hard": (1, 14, 2, 15, 2, 12),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi, b_lo, b_hi, n_lo, n_hi = self._RANGES[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)
        n = rng.randint(n_lo, n_hi)

        raw_num = a
        raw_den = b * n
        result = Fraction(raw_num, raw_den)

        statement = rf"{_frac_raw(a, b)} \div {n}"
        reciprocal_latex = rf"\frac{{1}}{{{n}}}"
        after_flip = rf"{_frac_raw(a, b)} \times {reciprocal_latex}"
        unreduced = _frac_raw(raw_num, raw_den)

        if result.denominator == raw_den and result.numerator == raw_num:
            simplify_line = f"${unreduced}$ is already in lowest terms."
        else:
            simplify_line = rf"Simplify: ${unreduced} = {_frac_latex(result)}$."

        answer = _answer_latex(result)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute ${statement}$.",
            answer_latex=answer,
            hints=[
                rf"Write the whole number as a fraction: ${n} = \frac{{{n}}}{{1}}$. Its reciprocal is $\frac{{1}}{{{n}}}$.",
                rf"Intuition: cutting ${_frac_raw(a, b)}$ of a pie into ${n}$ equal pieces gives a smaller slice --- each slice is ${_frac_raw(a, b)} \div {n} = {_frac_raw(a, b)} \times \frac{{1}}{{{n}}}$.",
                rf"So ${statement} = {after_flip} = {unreduced}$. Then simplify.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                rf"The reciprocal of ${n}$ is $\frac{{1}}{{{n}}}$, so keep-change-flip gives ${after_flip}$.",
                rf"Multiply straight across: $\frac{{{a} \times 1}}{{{b} \times {n}}} = {unreduced}$.",
                simplify_line,
                f"Final answer: {answer}.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class DivideWholeByFraction(Generator):
    """Compute n / (a/b). Reciprocal is b/a, answer is nb/a."""
    generator_id = "divide_whole_by_fraction"
    topic_slug = "dividing_fractions"
    display_name = "Divide a whole number by a fraction: n / (a/b)"

    _RANGES = {
        "easy": (2, 8, 1, 6, 2, 8),    # n_lo, n_hi, a_lo, a_hi, b_lo, b_hi
        "medium": (2, 15, 1, 9, 2, 12),
        "hard": (3, 25, 1, 12, 2, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi, a_lo, a_hi, b_lo, b_hi = self._RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)
        # a cannot be zero
        a = rng.randint(max(1, a_lo), a_hi)
        b = rng.randint(b_lo, b_hi)

        raw_num = n * b
        raw_den = a
        result = Fraction(raw_num, raw_den)

        statement = rf"{n} \div {_frac_raw(a, b)}"
        reciprocal_latex = _frac_raw(b, a)
        after_flip = rf"{n} \times {reciprocal_latex}"
        unreduced = _frac_raw(raw_num, raw_den)

        if result.denominator == raw_den and result.numerator == raw_num:
            simplify_line = f"${unreduced}$ is already in lowest terms."
        else:
            simplify_line = rf"Simplify: ${unreduced} = {_frac_latex(result)}$."

        mixed_line = None
        if result.denominator != 1 and abs(result.numerator) > result.denominator:
            mixed_line = rf"As a mixed number: ${_frac_latex(result)} = {_mixed_latex(result)}$."

        answer = _answer_latex(result)

        steps = [
            f"Start with ${statement}$.",
            rf"Write ${n}$ as $\frac{{{n}}}{{1}}$ and flip the divisor: $\frac{{{n}}}{{1}} \times {reciprocal_latex} = {after_flip}$.",
            rf"Multiply straight across: $\frac{{{n} \times {b}}}{{1 \times {a}}} = {unreduced}$.",
            simplify_line,
        ]
        if mixed_line is not None:
            steps.append(mixed_line)
        steps.append(f"Final answer: {answer}.")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute ${statement}$.",
            answer_latex=answer,
            hints=[
                r"To divide by a fraction, multiply by its reciprocal.",
                rf"Intuition: how many ${_frac_raw(a, b)}$-sized pieces fit inside ${n}$ wholes? For example, ${n} \div \frac{{1}}{{4}} = {4 * n}$ because ${4 * n}$ quarters fit in ${n}$ wholes.",
                rf"Here, ${statement} = {after_flip} = {unreduced}$. Then simplify.",
            ],
            solution_steps_latex=steps,
            tags=[
                "#branch-pre-algebra",
                "#topic-numbers-and-operations",
                "#skill-procedural-calculation",
                f"#difficulty-{difficulty}",
            ],
        )
