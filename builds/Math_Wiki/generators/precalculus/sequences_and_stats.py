"""Sequences, series, probability, and statistics generators (Cluster 8).

Nine topic slugs covered, three generators each (27 total):

- arithmetic_sequences_and_linear_patterns (pre-algebra)
- sequences                                (algebra-2)
- summation                                (pre-calculus)
- probability_of_simple_and_compound_events (pre-algebra)
- binomial                                 (pre-calculus)
- induction                                (pre-calculus)
- mean_median_mode_and_range               (pre-algebra)
- data_displays                            (pre-algebra)
- data_displays_and_measures_of_spread     (pre-algebra)

Backward construction throughout: pick clean parameters first so the answer
is a small integer or simple fraction, then render the statement. Probability
generators use sympy's Rational for exact fractions. Sum formulas use sympy
for exact arithmetic and render with ``\\dfrac``.
"""
from __future__ import annotations

import math
import random
from fractions import Fraction
from statistics import mean, median

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _signed_term(coeff: int, is_first: bool = False) -> str:
    """Return a signed term for a sum display. is_first drops the leading '+'."""
    if is_first:
        return str(coeff)
    if coeff >= 0:
        return f"+ {coeff}"
    return f"- {abs(coeff)}"


def _render_frac(num: int, den: int) -> str:
    """Render num/den as a LaTeX fraction (integer if den==1). Simplifies."""
    if den == 0:
        raise ValueError("denominator cannot be zero")
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    if den == 1:
        return str(num)
    return rf"\dfrac{{{num}}}{{{den}}}"


def _render_rational(r: sp.Rational) -> str:
    """Render a sympy Rational as a LaTeX fraction (or integer if denom==1)."""
    if r.q == 1:
        return str(r.p)
    sign = "-" if r.p < 0 else ""
    return rf"{sign}\dfrac{{{abs(r.p)}}}{{{r.q}}}"


def _format_list(values: list[int]) -> str:
    """Render a comma-separated list of values for a statement, e.g. "3, 7, 11, 15"."""
    return ", ".join(str(v) for v in values)


# ===========================================================================
# Topic 1: arithmetic_sequences_and_linear_patterns  (pre-algebra)
# ===========================================================================


PREALG_SEQ_TAGS = ["#branch-pre-algebra", "#topic-sequences-and-series"]


@register
class ArithSeqNthTerm(Generator):
    """Given $a_1$ and $d$, compute $a_n$ for a specific $n$.

    Backward: pick clean $a_1$, $d$, and $n$, compute $a_n$ exactly.
    """
    generator_id = "arith_seq_nth_term"
    topic_slug = "arithmetic_sequences_and_linear_patterns"
    display_name = "Find the nth term of an arithmetic sequence from a1 and d"

    _A1_RANGES = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-40, 40)}
    _D_RANGES = {"easy": (1, 8), "medium": (-12, 12), "hard": (-18, 18)}
    _N_RANGES = {"easy": (4, 12), "medium": (6, 20), "hard": (10, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a1_lo, a1_hi = self._A1_RANGES[difficulty]
        d_lo, d_hi = self._D_RANGES[difficulty]
        n_lo, n_hi = self._N_RANGES[difficulty]

        a1 = rng.randint(a1_lo, a1_hi)
        d = rng.randint(d_lo, d_hi)
        while d == 0:
            d = rng.randint(d_lo, d_hi)
        n = rng.randint(n_lo, n_hi)

        an = a1 + (n - 1) * d

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, d, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"An arithmetic sequence has first term $a_1 = {a1}$ and common "
                f"difference $d = {d}$. Find $a_{{{n}}}$."
            ),
            answer_latex=f"$a_{{{n}}} = {an}$",
            hints=[
                "The explicit formula for an arithmetic sequence is $a_n = a_1 + (n - 1)d$.",
                f"Substitute $a_1 = {a1}$, $d = {d}$, and $n = {n}$, then simplify.",
            ],
            solution_steps_latex=[
                "Start with the explicit formula $a_n = a_1 + (n - 1)d$.",
                (
                    f"Substitute the known values: "
                    f"$a_{{{n}}} = {a1} + ({n} - 1)({d})$."
                ),
                (
                    f"Simplify the factor: $a_{{{n}}} = {a1} + ({n - 1})({d}) "
                    f"= {a1} + {(n - 1) * d}$."
                ),
                f"Add: $a_{{{n}}} = {an}$.",
            ],
            tags=PREALG_SEQ_TAGS,
        )


@register
class ArithSeqFindFormula(Generator):
    """Given the first few terms of an arithmetic sequence, write $a_n = a_1 + (n-1)d$.

    Backward: pick $a_1$ and $d$, list the first four terms, ask for the formula.
    """
    generator_id = "arith_seq_find_formula"
    topic_slug = "arithmetic_sequences_and_linear_patterns"
    display_name = "Write the explicit formula from the first terms of an arithmetic sequence"

    _A1_RANGES = {"easy": (-8, 12), "medium": (-15, 20), "hard": (-30, 35)}
    _D_RANGES = {"easy": (1, 9), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a1_lo, a1_hi = self._A1_RANGES[difficulty]
        d_lo, d_hi = self._D_RANGES[difficulty]

        a1 = rng.randint(a1_lo, a1_hi)
        d = rng.randint(d_lo, d_hi)
        while d == 0:
            d = rng.randint(d_lo, d_hi)

        terms = [a1 + k * d for k in range(4)]

        # Render the explicit formula in the "a_n = a_1 + (n-1)d" simplified form:
        # a_n = a1 + d*(n-1)  -->  a_n = (a1 - d) + d*n
        slope = d
        intercept = a1 - d
        if slope == 1:
            slope_n = "n"
        elif slope == -1:
            slope_n = "-n"
        else:
            slope_n = f"{slope}n"
        if intercept == 0:
            closed = slope_n
        elif intercept > 0:
            closed = f"{slope_n} + {intercept}"
        else:
            closed = f"{slope_n} - {abs(intercept)}"

        # Canonical form requested by the problem statement.
        if d == 1:
            d_display = ""
            formula_canonical = f"{a1} + (n - 1)"
        elif d == -1:
            d_display = "-"
            formula_canonical = f"{a1} - (n - 1)"
        else:
            d_display = str(d)
            if d > 0:
                formula_canonical = f"{a1} + {d}(n - 1)"
            else:
                formula_canonical = f"{a1} - {abs(d)}(n - 1)"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find an explicit formula for the arithmetic sequence whose first "
                f"four terms are ${_format_list(terms)}, \\ldots$"
            ),
            answer_latex=f"$a_n = {formula_canonical}$",
            hints=[
                "Subtract consecutive terms to find the common difference $d$.",
                (
                    "Use the explicit formula $a_n = a_1 + (n - 1)d$ with the "
                    "first term and your value of $d$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Check the differences: $a_2 - a_1 = {terms[1] - terms[0]}$, "
                    f"$a_3 - a_2 = {terms[2] - terms[1]}$, $a_4 - a_3 = {terms[3] - terms[2]}$."
                ),
                f"The common difference is $d = {d}$ and the first term is $a_1 = {a1}$.",
                (
                    "Substitute into $a_n = a_1 + (n - 1)d$: "
                    f"$a_n = {formula_canonical}$."
                ),
                f"Expanding gives $a_n = {closed}$.",
            ],
            tags=PREALG_SEQ_TAGS,
        )


@register
class ArithSeqCommonDifference(Generator):
    """Given two non-consecutive terms $a_j$ and $a_k$, find the common difference $d$.

    Backward: pick clean $a_1$ and $d$, then pick $j < k$ and compute $a_j$ and $a_k$.
    The student recovers $d = (a_k - a_j)/(k - j)$.
    """
    generator_id = "arith_seq_common_difference"
    topic_slug = "arithmetic_sequences_and_linear_patterns"
    display_name = "Find the common difference from two non-consecutive terms"

    _A1_RANGES = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-40, 40)}
    _D_RANGES = {"easy": (1, 7), "medium": (-10, 10), "hard": (-15, 15)}
    _N_RANGES = {"easy": (3, 10), "medium": (4, 16), "hard": (5, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a1_lo, a1_hi = self._A1_RANGES[difficulty]
        d_lo, d_hi = self._D_RANGES[difficulty]
        n_lo, n_hi = self._N_RANGES[difficulty]

        a1 = rng.randint(a1_lo, a1_hi)
        d = rng.randint(d_lo, d_hi)
        while d == 0:
            d = rng.randint(d_lo, d_hi)
        j = rng.randint(n_lo, n_hi - 2)
        k = rng.randint(j + 2, n_hi)

        aj = a1 + (j - 1) * d
        ak = a1 + (k - 1) * d
        diff_terms = ak - aj
        gap = k - j

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, d, j, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In an arithmetic sequence, $a_{{{j}}} = {aj}$ and $a_{{{k}}} = {ak}$. "
                "Find the common difference $d$."
            ),
            answer_latex=f"$d = {d}$",
            hints=[
                (
                    f"The jump from $a_{{{j}}}$ to $a_{{{k}}}$ is ${k - j}$ "
                    f"common differences."
                ),
                "Use $a_k - a_j = (k - j) \\cdot d$ and solve for $d$.",
            ],
            solution_steps_latex=[
                (
                    f"Use the relationship $a_{{{k}}} - a_{{{j}}} = ({k} - {j}) d$."
                ),
                (
                    f"Substitute: ${ak} - ({aj}) = {gap} d$, so ${diff_terms} = {gap} d$."
                ),
                (
                    f"Divide: $d = \\dfrac{{{diff_terms}}}{{{gap}}} = {d}$."
                ),
            ],
            tags=PREALG_SEQ_TAGS,
        )


# ===========================================================================
# Topic 2: sequences  (algebra-2)
# ===========================================================================


ALG2_SEQ_TAGS = ["#branch-algebra-2", "#topic-sequences-and-series"]


@register
class GeometricSeqNthTerm(Generator):
    """Given $a_1$ and $r$, compute $a_n$.

    Backward: pick clean $a_1$, a small integer or simple fraction $r$, and $n$.
    """
    generator_id = "geometric_seq_nth_term"
    topic_slug = "sequences"
    display_name = "Find the nth term of a geometric sequence from a1 and r"

    _A1_CHOICES = {
        "easy": (1, 2, 3, 4, 5, 6, 8, 10, -1, -2, -3),
        "medium": (1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, -1, -2, -3, -4, -5),
        "hard": tuple(range(-20, 21)) + (24, 25, 27, 30, -24, -25),
    }
    _R_INT = ((2,), (3,), (-2,), (-3,), (2, 3, -2, -3, 4, -4, 5, -5), (2, 3, -2, -3, 4, -4, 5, -5, 6, -6))
    _R_FRAC = (
        sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(-1, 2), sp.Rational(-1, 3),
        sp.Rational(2, 3), sp.Rational(3, 2),
    )
    _N_RANGES = {"easy": (3, 6), "medium": (4, 8), "hard": (5, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a1 = rng.choice(self._A1_CHOICES[difficulty])
        # Pick r: either a small integer or a simple fraction
        use_frac = (difficulty != "easy") and (rng.random() < 0.35)
        if use_frac:
            r = rng.choice(self._R_FRAC)
        else:
            if difficulty == "easy":
                r_int = rng.choice((2, 3, -2, -3))
            elif difficulty == "medium":
                r_int = rng.choice((2, 3, -2, -3, 4, -4, 5))
            else:
                r_int = rng.choice((2, 3, -2, -3, 4, -4, 5, -5))
            r = sp.Rational(r_int, 1)

        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        # Clamp to keep magnitude sane
        if abs(r.p) >= 4 and n >= 8:
            n = 6

        an = sp.Rational(a1) * r ** (n - 1)
        # Ensure not absurdly large
        if abs(float(an)) > 10**8:
            n = max(n - 2, n_lo)
            an = sp.Rational(a1) * r ** (n - 1)

        r_latex = sp.latex(r)
        an_latex = _render_rational(sp.Rational(an))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, r.p, r.q, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A geometric sequence has first term $a_1 = {a1}$ and common "
                f"ratio $r = {r_latex}$. Find $a_{{{n}}}$."
            ),
            answer_latex=f"$a_{{{n}}} = {an_latex}$",
            hints=[
                "The explicit formula for a geometric sequence is $a_n = a_1 \\cdot r^{n-1}$.",
                f"Raise $r$ to the power ${n - 1}$, then multiply by $a_1 = {a1}$.",
            ],
            solution_steps_latex=[
                "Start with the explicit formula $a_n = a_1 \\cdot r^{n-1}$.",
                (
                    f"Substitute: $a_{{{n}}} = {a1} \\cdot \\left({r_latex}\\right)^{{{n - 1}}}$."
                ),
                (
                    f"Evaluate the power and multiply: $a_{{{n}}} = {an_latex}$."
                ),
            ],
            tags=ALG2_SEQ_TAGS,
        )


@register
class ArithSeqSum(Generator):
    """Given an arithmetic sequence's $a_1$, $a_n$, and $n$, compute $S_n$.

    Backward: pick clean $a_1$, $d$, $n$; compute $a_n$ and $S_n$.
    """
    generator_id = "arith_seq_sum"
    topic_slug = "sequences"
    display_name = "Compute the sum of an arithmetic sequence"

    _A1_RANGES = {"easy": (1, 12), "medium": (-10, 20), "hard": (-30, 35)}
    _D_RANGES = {"easy": (1, 6), "medium": (-8, 10), "hard": (-14, 14)}
    _N_RANGES = {"easy": (5, 12), "medium": (6, 20), "hard": (10, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a1_lo, a1_hi = self._A1_RANGES[difficulty]
        d_lo, d_hi = self._D_RANGES[difficulty]
        n_lo, n_hi = self._N_RANGES[difficulty]

        a1 = rng.randint(a1_lo, a1_hi)
        d = rng.randint(d_lo, d_hi)
        while d == 0:
            d = rng.randint(d_lo, d_hi)
        n = rng.randint(n_lo, n_hi)

        an = a1 + (n - 1) * d
        # Exact integer sum (pairs symmetry)
        total = sp.Rational(n * (a1 + an), 2)
        total_latex = _render_rational(total)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, d, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"An arithmetic sequence has $a_1 = {a1}$, $a_{{{n}}} = {an}$, and "
                f"$n = {n}$ terms. Compute the sum $S_{{{n}}}$."
            ),
            answer_latex=f"$S_{{{n}}} = {total_latex}$",
            hints=[
                (
                    "Use the sum formula for an arithmetic sequence: "
                    r"$S_n = \dfrac{n(a_1 + a_n)}{2}$."
                ),
                f"Substitute the given values for $n$, $a_1$, and $a_{{{n}}}$.",
            ],
            solution_steps_latex=[
                r"Write the sum formula: $S_n = \dfrac{n(a_1 + a_n)}{2}$.",
                (
                    f"Substitute: $S_{{{n}}} = \\dfrac{{{n}\\,({a1} + {an})}}{{2}}$."
                ),
                (
                    f"Simplify the parenthesis: $S_{{{n}}} = "
                    f"\\dfrac{{{n} \\cdot {a1 + an}}}{{2}} = \\dfrac{{{n * (a1 + an)}}}{{2}}$."
                ),
                f"Divide: $S_{{{n}}} = {total_latex}$.",
            ],
            tags=ALG2_SEQ_TAGS,
        )


@register
class GeometricSeqSum(Generator):
    """Given $a_1$, $r$, $n$, compute $S_n = a_1(1-r^n)/(1-r)$ for $r \\neq 1$.

    Backward: pick clean small-integer $a_1$, $r$ in {-3,-2,2,3,4,1/2,1/3},
    and small $n$ so the output is exact.
    """
    generator_id = "geometric_seq_sum"
    topic_slug = "sequences"
    display_name = "Compute the sum of a geometric sequence"

    _A1_CHOICES = {
        "easy": (1, 2, 3, 4, 5, 6, -1, -2, -3),
        "medium": (1, 2, 3, 4, 5, 6, 8, 10, -1, -2, -3, -4, -5, -6),
        "hard": tuple(range(-15, 16)) + (18, 20, -18, -20),
    }
    _R_CHOICES_EASY = (sp.Rational(2), sp.Rational(3), sp.Rational(-2))
    _R_CHOICES_MED = (
        sp.Rational(2), sp.Rational(3), sp.Rational(-2), sp.Rational(-3),
        sp.Rational(1, 2), sp.Rational(1, 3),
    )
    _R_CHOICES_HARD = (
        sp.Rational(2), sp.Rational(3), sp.Rational(4),
        sp.Rational(-2), sp.Rational(-3),
        sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(-1, 2),
        sp.Rational(2, 3),
    )
    _N_RANGES = {"easy": (3, 5), "medium": (3, 6), "hard": (4, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a1_raw = rng.choice(self._A1_CHOICES[difficulty])
        a1 = sp.Rational(a1_raw)
        r_choices = {
            "easy": self._R_CHOICES_EASY,
            "medium": self._R_CHOICES_MED,
            "hard": self._R_CHOICES_HARD,
        }[difficulty]
        r = rng.choice(r_choices)
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        # Formula: S_n = a1*(1 - r^n)/(1 - r)
        total = a1 * (1 - r ** n) / (1 - r)
        total = sp.Rational(total)

        # Keep magnitudes sane
        if abs(float(total)) > 10**7:
            n = n_lo
            total = sp.Rational(a1 * (1 - r ** n) / (1 - r))

        total_latex = _render_rational(total)
        r_latex = sp.latex(r)
        one_minus_r_n = sp.Rational(1 - r ** n)
        one_minus_r = sp.Rational(1 - r)
        one_minus_r_n_latex = _render_rational(one_minus_r_n)
        one_minus_r_latex = _render_rational(one_minus_r)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1.p, a1.q, r.p, r.q, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A geometric sequence has first term $a_1 = {sp.latex(a1)}$ and "
                f"common ratio $r = {r_latex}$. Compute the sum of the first "
                f"${n}$ terms, $S_{{{n}}}$."
            ),
            answer_latex=f"$S_{{{n}}} = {total_latex}$",
            hints=[
                (
                    "Use the sum formula "
                    r"$S_n = \dfrac{a_1 (1 - r^n)}{1 - r}$, valid for $r \neq 1$."
                ),
                f"Compute $r^{{{n}}}$ first, then plug in and simplify.",
            ],
            solution_steps_latex=[
                (
                    r"Apply the geometric sum formula: "
                    r"$S_n = \dfrac{a_1 (1 - r^n)}{1 - r}$."
                ),
                (
                    f"Substitute: $S_{{{n}}} = \\dfrac{{{sp.latex(a1)} "
                    f"\\left(1 - ({r_latex})^{{{n}}}\\right)}}{{1 - ({r_latex})}}$."
                ),
                (
                    f"Simplify the numerator factor and denominator: "
                    f"$1 - r^{{{n}}} = {one_minus_r_n_latex}$ and "
                    f"$1 - r = {one_minus_r_latex}$."
                ),
                f"Combine and reduce: $S_{{{n}}} = {total_latex}$.",
            ],
            tags=ALG2_SEQ_TAGS,
        )


# ===========================================================================
# Topic 3: summation  (pre-calculus)
# ===========================================================================


PRECALC_SEQ_TAGS = ["#branch-pre-calculus", "#topic-sequences-and-series"]


@register
class SigmaExpand(Generator):
    """Expand $\\sum_{k=1}^{n} (a k + b)$ to the explicit sum.

    Backward: pick small $n$ (2-5), small $a$ and $b$, list the terms.
    """
    generator_id = "sigma_expand"
    topic_slug = "summation"
    display_name = "Expand a sigma notation into its explicit sum"

    _A_RANGES = {"easy": (1, 5), "medium": (-6, 6), "hard": (-9, 9)}
    _B_RANGES = {"easy": (0, 8), "medium": (-8, 10), "hard": (-12, 12)}
    _N_RANGES = {"easy": (3, 4), "medium": (3, 5), "hard": (4, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGES[difficulty]
        b_lo, b_hi = self._B_RANGES[difficulty]
        n_lo, n_hi = self._N_RANGES[difficulty]

        a = rng.randint(a_lo, a_hi)
        while a == 0:
            a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)
        n = rng.randint(n_lo, n_hi)

        # Render (a k + b) in the summand with clean signs
        if a == 1:
            ak = "k"
        elif a == -1:
            ak = "-k"
        else:
            ak = f"{a}k"
        if b == 0:
            summand = ak
        elif b > 0:
            summand = f"{ak} + {b}"
        else:
            summand = f"{ak} - {abs(b)}"

        # Build the list of values of (a k + b) for k = 1..n
        terms = [a * k + b for k in range(1, n + 1)]
        total = sum(terms)

        # Render the expanded sum: (t1) + (t2) + ... + (tn)
        def _paren(v: int) -> str:
            return f"({v})" if v < 0 else str(v)
        expanded = " + ".join(_paren(v) for v in terms)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Expand the sigma notation and compute the sum: "
                f"$\\displaystyle\\sum_{{k=1}}^{{{n}}} ({summand})$."
            ),
            answer_latex=f"$\\displaystyle\\sum_{{k=1}}^{{{n}}} ({summand}) = {total}$",
            hints=[
                (
                    "Substitute $k = 1, 2, \\ldots$ up to the upper limit, one at a time."
                ),
                "List the resulting values, then add them together.",
            ],
            solution_steps_latex=[
                (
                    f"Substitute each value of $k$ from $1$ to ${n}$ into "
                    f"$({summand})$."
                ),
                (
                    "The terms are "
                    + ", ".join(f"${summand}\\big|_{{k={k}}} = {a * k + b}$"
                                for k in range(1, n + 1))
                    + "."
                ),
                f"Add the terms: ${expanded} = {total}$.",
            ],
            tags=PRECALC_SEQ_TAGS,
        )


@register
class SigmaClosedFormLinear(Generator):
    """Compute $\\sum_{k=1}^{n} k$ via the closed form $n(n+1)/2$.

    Backward: pick clean integer $n$ in the appropriate range.
    """
    generator_id = "sigma_closed_form_linear"
    topic_slug = "summation"
    display_name = "Compute sum of k from 1 to n using n(n+1)/2"

    _N_RANGES = {"easy": (5, 20), "medium": (10, 40), "hard": (20, 70)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        product = n * (n + 1)
        total = product // 2

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use the closed-form formula to compute "
                f"$\\displaystyle\\sum_{{k=1}}^{{{n}}} k$."
            ),
            answer_latex=(
                f"$\\displaystyle\\sum_{{k=1}}^{{{n}}} k = {total}$"
            ),
            hints=[
                r"The closed form is $\sum_{k=1}^{n} k = \dfrac{n(n+1)}{2}$.",
                f"Substitute $n = {n}$ into that formula and simplify.",
            ],
            solution_steps_latex=[
                (
                    r"Start with the closed-form identity "
                    r"$\displaystyle\sum_{k=1}^{n} k = \dfrac{n(n+1)}{2}$."
                ),
                (
                    f"Substitute $n = {n}$: "
                    rf"$\dfrac{{{n}({n} + 1)}}{{2}} = \dfrac{{{n} \cdot {n + 1}}}{{2}}$."
                ),
                (
                    rf"Multiply the numerator: $\dfrac{{{product}}}{{2}}$."
                ),
                f"Divide: ${total}$.",
            ],
            tags=PRECALC_SEQ_TAGS,
        )


@register
class SigmaClosedFormQuadratic(Generator):
    """Compute $\\sum_{k=1}^{n} k^2$ via $n(n+1)(2n+1)/6$.

    Backward: pick clean integer $n$ in a reasonable range.
    """
    generator_id = "sigma_closed_form_quadratic"
    topic_slug = "summation"
    display_name = "Compute sum of k squared from 1 to n"

    _N_RANGES = {"easy": (4, 14), "medium": (8, 25), "hard": (12, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        prod = n * (n + 1) * (2 * n + 1)
        total = prod // 6

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use the closed-form formula to compute "
                f"$\\displaystyle\\sum_{{k=1}}^{{{n}}} k^2$."
            ),
            answer_latex=(
                f"$\\displaystyle\\sum_{{k=1}}^{{{n}}} k^2 = {total}$"
            ),
            hints=[
                r"The closed form is $\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}$.",
                f"Substitute $n = {n}$ and simplify.",
            ],
            solution_steps_latex=[
                (
                    r"Start with the closed-form identity "
                    r"$\displaystyle\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}$."
                ),
                (
                    rf"Substitute $n = {n}$: "
                    rf"$\dfrac{{{n}({n + 1})({2 * n + 1})}}{{6}}$."
                ),
                (
                    rf"Multiply the numerator: $\dfrac{{{prod}}}{{6}}$."
                ),
                f"Divide: ${total}$.",
            ],
            tags=PRECALC_SEQ_TAGS,
        )


# ===========================================================================
# Topic 4: probability_of_simple_and_compound_events  (pre-algebra)
# ===========================================================================


PROB_TAGS = ["#branch-pre-algebra", "#topic-probability"]


@register
class ProbSimpleEventFromRatio(Generator):
    """Given a sample space (fair die, standard deck, bag of marbles), compute
    the probability of a simple event as a reduced fraction.

    Backward: pick a scenario and an event; compute favorable/total.
    """
    generator_id = "prob_simple_event_from_ratio"
    topic_slug = "probability_of_simple_and_compound_events"
    display_name = "Probability of a simple event from a described sample space"
    supports_word_problems = True

    # Scenario templates: (name, total, favorable_options)
    _SCENARIOS = {
        "easy": [
            ("die_even", "A fair six-sided die is rolled.", 6, [("rolling an even number", 3)]),
            ("die_odd", "A fair six-sided die is rolled.", 6, [("rolling an odd number", 3)]),
            ("die_le_2", "A fair six-sided die is rolled.", 6, [("rolling a number less than 3", 2)]),
            ("die_ge_5", "A fair six-sided die is rolled.", 6, [("rolling a number greater than 4", 2)]),
            ("die_exact_1", "A fair six-sided die is rolled.", 6, [("rolling a 1", 1)]),
            ("die_exact_2", "A fair six-sided die is rolled.", 6, [("rolling a 2", 1)]),
            ("die_exact_3", "A fair six-sided die is rolled.", 6, [("rolling a 3", 1)]),
            ("die_exact_4", "A fair six-sided die is rolled.", 6, [("rolling a 4", 1)]),
            ("die_exact_5", "A fair six-sided die is rolled.", 6, [("rolling a 5", 1)]),
            ("die_exact_6", "A fair six-sided die is rolled.", 6, [("rolling a 6", 1)]),
            ("die_prime", "A fair six-sided die is rolled.", 6, [("rolling a prime number", 3)]),
            ("die_div3", "A fair six-sided die is rolled.", 6, [("rolling a multiple of 3", 2)]),
            ("die_le_4", "A fair six-sided die is rolled.", 6, [("rolling a number at most 4", 4)]),
            ("coin_h", "A fair coin is flipped.", 2, [("landing on heads", 1)]),
            ("coin_t", "A fair coin is flipped.", 2, [("landing on tails", 1)]),
        ],
        "medium": [
            ("deck_heart", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a heart", 13)]),
            ("deck_face", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a face card (jack, queen, or king)", 12)]),
            ("deck_red", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a red card", 26)]),
            ("deck_black", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a black card", 26)]),
            ("deck_ace", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing an ace", 4)]),
            ("deck_king", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a king", 4)]),
            ("deck_queen", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a queen", 4)]),
            ("deck_jack", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a jack", 4)]),
            ("deck_black_face", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a black face card", 6)]),
            ("deck_spade_or_ace", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a spade or an ace", 16)]),
            ("deck_club", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a club", 13)]),
            ("deck_diamond", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a diamond", 13)]),
            ("deck_number_card", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a numbered card from 2 through 10", 36)]),
            ("die_even", "A fair six-sided die is rolled.", 6, [("rolling an even number", 3)]),
            ("die_prime", "A fair six-sided die is rolled.", 6, [("rolling a prime number", 3)]),
        ],
        "hard": [
            ("marble_r", "A jar contains 4 red, 6 blue, and 10 green marbles. A marble is drawn at random.", 20, [("drawing a red marble", 4)]),
            ("marble_b", "A jar contains 4 red, 6 blue, and 10 green marbles. A marble is drawn at random.", 20, [("drawing a blue marble", 6)]),
            ("marble_g", "A jar contains 4 red, 6 blue, and 10 green marbles. A marble is drawn at random.", 20, [("drawing a green marble", 10)]),
            ("marble_rb", "A jar contains 4 red, 6 blue, and 10 green marbles. A marble is drawn at random.", 20, [("drawing a red or blue marble", 10)]),
            ("pdie_even", "A fair 12-sided die is rolled.", 12, [("rolling an even number", 6)]),
            ("pdie_p3", "A fair 12-sided die is rolled.", 12, [("rolling a multiple of 3", 4)]),
            ("pdie_p4", "A fair 12-sided die is rolled.", 12, [("rolling a multiple of 4", 3)]),
            ("deck_heart", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a heart", 13)]),
            ("deck_face", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a face card", 12)]),
            ("deck_not_face", "A card is drawn at random from a standard 52-card deck.", 52, [("drawing a non-face card", 40)]),
            ("bag_vowel", "A letter is selected at random from the English alphabet (26 letters).", 26, [("selecting a vowel (A, E, I, O, or U)", 5)]),
            ("bag_cons", "A letter is selected at random from the English alphabet (26 letters).", 26, [("selecting a consonant", 21)]),
        ],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scenarios = self._SCENARIOS[difficulty]
        key, scene, total, events = rng.choice(scenarios)
        event_text, favorable = rng.choice(events)

        prob = sp.Rational(favorable, total)
        prob_latex = _render_rational(prob)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (key, event_text)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{scene} Find the probability of {event_text}. "
                "Give your answer as a fraction in lowest terms."
            ),
            answer_latex=f"${prob_latex}$",
            hints=[
                (
                    "Probability of a simple event equals the number of favorable "
                    "outcomes divided by the total number of outcomes."
                ),
                f"Count how many outcomes give the event, then divide by ${total}$.",
            ],
            solution_steps_latex=[
                (
                    f"Identify the total number of equally likely outcomes: ${total}$."
                ),
                (
                    f"Count the outcomes that correspond to the event "
                    f"({event_text}): ${favorable}$."
                ),
                (
                    f"Form the ratio: "
                    rf"$P(\text{{event}}) = \dfrac{{{favorable}}}{{{total}}}$."
                ),
                f"Reduce to lowest terms: ${prob_latex}$.",
            ],
            tags=PROB_TAGS,
        )


@register
class ProbAndIndependent(Generator):
    """Given two independent events with individual probabilities, compute
    $P(A \\text{ and } B) = P(A) \\cdot P(B)$.

    Backward: pick simple $P(A)$ and $P(B)$ as clean fractions.
    """
    generator_id = "prob_and_independent"
    topic_slug = "probability_of_simple_and_compound_events"
    display_name = "Probability of A and B for independent events"
    supports_word_problems = True

    # Each scenario: (label, text_template, P(A), P(B))
    _SCENARIOS = [
        (
            "coin_die",
            "A fair coin is flipped and a fair six-sided die is rolled. What is "
            "the probability of flipping heads AND rolling an even number?",
            sp.Rational(1, 2), sp.Rational(1, 2),
        ),
        (
            "two_dice_3",
            "Two fair six-sided dice are rolled. What is the probability that "
            "the first die shows a 3 AND the second die shows a 4?",
            sp.Rational(1, 6), sp.Rational(1, 6),
        ),
        (
            "coin_coin",
            "A fair coin is flipped twice. What is the probability of flipping "
            "heads on the first toss AND tails on the second toss?",
            sp.Rational(1, 2), sp.Rational(1, 2),
        ),
        (
            "spinner_card",
            "A spinner with 4 equal sections labeled 1, 2, 3, 4 is spun, and a "
            "card is drawn from a standard 52-card deck (then replaced). What is "
            "the probability the spinner shows a 2 AND the card drawn is a spade?",
            sp.Rational(1, 4), sp.Rational(1, 4),
        ),
        (
            "bag_bag",
            "A bag contains 3 red and 7 blue marbles; a separate bag contains "
            "2 gold and 3 silver coins. One marble and one coin are each drawn "
            "at random. What is the probability of drawing a red marble AND a "
            "gold coin?",
            sp.Rational(3, 10), sp.Rational(2, 5),
        ),
        (
            "die_die_prime",
            "Two fair six-sided dice are rolled. What is the probability that "
            "the first die is a prime number AND the second die is a 6?",
            sp.Rational(1, 2), sp.Rational(1, 6),
        ),
        (
            "two_coins_two_tails",
            "Two fair coins are flipped. What is the probability that the first "
            "lands heads AND the second lands heads?",
            sp.Rational(1, 2), sp.Rational(1, 2),
        ),
        (
            "card_die",
            "A card is drawn from a standard 52-card deck (then replaced), and a "
            "fair six-sided die is rolled. What is the probability of drawing a "
            "face card AND rolling a 1?",
            sp.Rational(3, 13), sp.Rational(1, 6),
        ),
        (
            "die_coin_4",
            "A fair coin is flipped and a fair six-sided die is rolled. What is "
            "the probability of flipping tails AND rolling a number less than 4?",
            sp.Rational(1, 2), sp.Rational(1, 2),
        ),
        (
            "marble_spinner",
            "A jar contains 5 red and 15 yellow marbles, and a spinner has 3 equal "
            "sections. One marble is drawn and the spinner is spun. What is the "
            "probability of drawing a red marble AND landing on the first section?",
            sp.Rational(1, 4), sp.Rational(1, 3),
        ),
        (
            "two_dice_even_5",
            "Two fair six-sided dice are rolled. What is the probability the "
            "first die is even AND the second die is a 5?",
            sp.Rational(1, 2), sp.Rational(1, 6),
        ),
        (
            "weather_bus",
            "On a given weekday, the probability it rains is $1/4$ and the "
            "probability the bus arrives late is $1/5$. Assuming the two events "
            "are independent, what is the probability it rains AND the bus "
            "arrives late on the same day?",
            sp.Rational(1, 4), sp.Rational(1, 5),
        ),
        (
            "class_hw",
            "A student has a $3/5$ chance of finishing homework on time and a "
            "$1/2$ chance of packing the correct textbook, and the two events "
            "are independent. What is the probability of finishing homework on "
            "time AND packing the correct textbook?",
            sp.Rational(3, 5), sp.Rational(1, 2),
        ),
        (
            "red_green",
            "Two different spinners are spun. The first is red $2/3$ of the "
            "time. The second is green $1/4$ of the time. Assuming independence, "
            "what is the probability of red on the first spinner AND green on "
            "the second?",
            sp.Rational(2, 3), sp.Rational(1, 4),
        ),
        (
            "phone_call",
            "At a certain call center, each call is independent. The probability "
            "an incoming call is a sales inquiry is $2/5$, and the probability a "
            "call lasts more than one minute is $1/2$. What is the probability "
            "a random call is a sales inquiry AND lasts more than one minute?",
            sp.Rational(2, 5), sp.Rational(1, 2),
        ),
        (
            "cards_replaced",
            "A card is drawn from a standard deck and then replaced. A second "
            "card is then drawn. What is the probability both draws produce "
            "hearts?",
            sp.Rational(1, 4), sp.Rational(1, 4),
        ),
    ]

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randint(0, len(self._SCENARIOS) - 1)
        key, text, pa, pb = self._SCENARIOS[idx]

        product = pa * pb
        pa_latex = _render_rational(pa)
        pb_latex = _render_rational(pb)
        product_latex = _render_rational(product)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (key,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=text,
            answer_latex=f"${product_latex}$",
            hints=[
                (
                    "When events $A$ and $B$ are independent, "
                    r"$P(A \text{ and } B) = P(A) \cdot P(B)$."
                ),
                "Find each individual probability, then multiply the two fractions.",
            ],
            solution_steps_latex=[
                (
                    f"Let $A$ be the first event and $B$ the second. Then "
                    f"$P(A) = {pa_latex}$ and $P(B) = {pb_latex}$."
                ),
                (
                    r"Because the events are independent, "
                    r"$P(A \text{ and } B) = P(A) \cdot P(B)$."
                ),
                (
                    rf"Multiply: $P(A \text{{ and }} B) = {pa_latex} \cdot "
                    rf"{pb_latex} = {product_latex}$."
                ),
            ],
            tags=PROB_TAGS,
        )


@register
class ProbOrMutuallyExclusive(Generator):
    """Compute $P(A \\text{ or } B) = P(A) + P(B)$ for mutually exclusive events.

    Backward: pick $P(A)$ and $P(B)$ so the sum is a clean fraction or $\\le 1$.
    """
    generator_id = "prob_or_mutually_exclusive"
    topic_slug = "probability_of_simple_and_compound_events"
    display_name = "Probability of A or B for mutually exclusive events"
    supports_word_problems = True

    _SCENARIOS = [
        (
            "die_1_or_2",
            "A fair six-sided die is rolled. What is the probability of rolling "
            "a 1 OR a 2?",
            sp.Rational(1, 6), sp.Rational(1, 6),
        ),
        (
            "die_even_or_5",
            "A fair six-sided die is rolled. What is the probability of rolling "
            "an even number OR a 5?",
            sp.Rational(1, 2), sp.Rational(1, 6),
        ),
        (
            "deck_heart_or_spade",
            "A card is drawn from a standard 52-card deck. What is the probability "
            "of drawing a heart OR a spade?",
            sp.Rational(1, 4), sp.Rational(1, 4),
        ),
        (
            "deck_king_or_queen",
            "A card is drawn from a standard 52-card deck. What is the probability "
            "of drawing a king OR a queen?",
            sp.Rational(1, 13), sp.Rational(1, 13),
        ),
        (
            "deck_ace_or_jack",
            "A card is drawn from a standard 52-card deck. What is the probability "
            "of drawing an ace OR a jack?",
            sp.Rational(1, 13), sp.Rational(1, 13),
        ),
        (
            "bag_r_or_b",
            "A bag contains 3 red, 5 blue, and 2 yellow marbles. One marble is "
            "drawn at random. What is the probability of drawing a red OR a blue "
            "marble?",
            sp.Rational(3, 10), sp.Rational(1, 2),
        ),
        (
            "bag_r_or_y",
            "A bag contains 3 red, 5 blue, and 2 yellow marbles. One marble is "
            "drawn at random. What is the probability of drawing a red OR a yellow "
            "marble?",
            sp.Rational(3, 10), sp.Rational(1, 5),
        ),
        (
            "bag_b_or_y",
            "A bag contains 3 red, 5 blue, and 2 yellow marbles. One marble is "
            "drawn at random. What is the probability of drawing a blue OR a "
            "yellow marble?",
            sp.Rational(1, 2), sp.Rational(1, 5),
        ),
        (
            "spinner_1_or_3",
            "A spinner has 5 equal sections labeled 1 through 5. What is the "
            "probability the spinner lands on 1 OR 3?",
            sp.Rational(1, 5), sp.Rational(1, 5),
        ),
        (
            "spinner_2_or_4_or_alt",
            "A spinner has 8 equal sections labeled 1 through 8. What is the "
            "probability the spinner lands on a number less than 3 OR on 8?",
            sp.Rational(1, 4), sp.Rational(1, 8),
        ),
        (
            "month_pick",
            "A month of the year is chosen at random. What is the probability "
            "the month is January OR December?",
            sp.Rational(1, 12), sp.Rational(1, 12),
        ),
        (
            "lottery_like",
            "A ticket numbered from 1 to 20 is drawn at random. What is the "
            "probability the ticket number is 5 OR 15?",
            sp.Rational(1, 20), sp.Rational(1, 20),
        ),
        (
            "dice_roll_2_or_12",
            "Two fair six-sided dice are rolled. What is the probability the sum "
            "is 2 OR 12?",
            sp.Rational(1, 36), sp.Rational(1, 36),
        ),
        (
            "deck_spade_or_heart",
            "A card is drawn from a standard 52-card deck. What is the probability "
            "the card is a spade OR a heart?",
            sp.Rational(1, 4), sp.Rational(1, 4),
        ),
        (
            "deck_ace_or_king",
            "A card is drawn from a standard 52-card deck. What is the probability "
            "the card is an ace OR a king?",
            sp.Rational(1, 13), sp.Rational(1, 13),
        ),
        (
            "letter_a_or_e",
            "A letter is selected at random from the English alphabet. What is "
            "the probability the letter is A OR E?",
            sp.Rational(1, 26), sp.Rational(1, 26),
        ),
    ]

    bank_count_per_difficulty = 16

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randint(0, len(self._SCENARIOS) - 1)
        key, text, pa, pb = self._SCENARIOS[idx]

        total = pa + pb
        pa_latex = _render_rational(pa)
        pb_latex = _render_rational(pb)
        total_latex = _render_rational(total)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (key,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=text,
            answer_latex=f"${total_latex}$",
            hints=[
                (
                    "When events $A$ and $B$ are mutually exclusive (they cannot "
                    r"both happen), $P(A \text{ or } B) = P(A) + P(B)$."
                ),
                "Find each probability, then add the fractions using a common denominator.",
            ],
            solution_steps_latex=[
                (
                    f"Identify the two probabilities: $P(A) = {pa_latex}$ and "
                    f"$P(B) = {pb_latex}$."
                ),
                (
                    "Because the events are mutually exclusive, "
                    r"$P(A \text{ or } B) = P(A) + P(B)$."
                ),
                (
                    rf"Add: $P(A \text{{ or }} B) = {pa_latex} + {pb_latex} = "
                    rf"{total_latex}$."
                ),
            ],
            tags=PROB_TAGS,
        )


# ===========================================================================
# Topic 5: binomial  (pre-calculus)
# ===========================================================================


BINOMIAL_TAGS = ["#branch-pre-calculus", "#topic-sequences-and-series"]


@register
class BinomialCoefficientCompute(Generator):
    """Compute $\\binom{n}{k}$ for small integer $n$ and $k$.

    Backward: pick small $n$ and $k$, compute via the definition.
    """
    generator_id = "binomial_coefficient_compute"
    topic_slug = "binomial"
    display_name = "Compute a binomial coefficient C(n, k)"

    _N_RANGES = {"easy": (3, 6), "medium": (5, 9), "hard": (7, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)
        k = rng.randint(1, n - 1)

        value = math.comb(n, k)
        nk_factorial = math.factorial(n - k)
        k_factorial = math.factorial(k)
        n_factorial = math.factorial(n)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Compute the binomial coefficient $\\dbinom{{{n}}}{{{k}}}$."
            ),
            answer_latex=f"$\\dbinom{{{n}}}{{{k}}} = {value}$",
            hints=[
                r"Use the definition $\dbinom{n}{k} = \dfrac{n!}{k!(n-k)!}$.",
                "Expand only the factors needed and cancel before multiplying.",
            ],
            solution_steps_latex=[
                (
                    rf"Start with the definition: "
                    rf"$\dbinom{{{n}}}{{{k}}} = \dfrac{{{n}!}}{{{k}!({n - k})!}}$."
                ),
                (
                    rf"Substitute the factorials: "
                    rf"$\dfrac{{{n_factorial}}}{{{k_factorial} \cdot {nk_factorial}}}$."
                ),
                (
                    rf"Divide: $\dfrac{{{n_factorial}}}{{{k_factorial * nk_factorial}}} "
                    rf"= {value}$."
                ),
            ],
            tags=BINOMIAL_TAGS,
        )


@register
class BinomialExpandSmallPower(Generator):
    """Expand $(ax + b)^n$ for small $n$ using sympy's expand.

    Backward: pick small integer $a$, $b$, and $n \\in \\{2, 3, 4\\}$.
    """
    generator_id = "binomial_expand_small_power"
    topic_slug = "binomial"
    display_name = "Expand (a x + b)^n for small n"

    _A_CHOICES = {"easy": (1, 2), "medium": (1, 2, 3), "hard": (1, 2, 3, -1, -2)}
    _B_CHOICES = {
        "easy": (1, 2, 3, -1, -2),
        "medium": (1, 2, 3, 4, -1, -2, -3),
        "hard": (1, 2, 3, 4, 5, -1, -2, -3, -4),
    }
    _N_CHOICES = {"easy": (2,), "medium": (2, 3), "hard": (2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_CHOICES[difficulty])
        b = rng.choice(self._B_CHOICES[difficulty])
        n = rng.choice(self._N_CHOICES[difficulty])

        x = sp.Symbol("x")
        expr = (a * x + b) ** n
        expanded = sp.expand(expr)
        expanded_latex = sp.latex(expanded)

        # Render the original in LaTeX
        if a == 1:
            ax = "x"
        elif a == -1:
            ax = "-x"
        else:
            ax = f"{a}x"
        if b >= 0:
            orig = f"({ax} + {b})^{{{n}}}"
        else:
            orig = f"({ax} - {abs(b)})^{{{n}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Expand ${orig}$ using the binomial theorem. Write the answer "
                "in standard form (descending powers of $x$)."
            ),
            answer_latex=f"${expanded_latex}$",
            hints=[
                (
                    r"The binomial theorem states "
                    r"$(p + q)^n = \sum_{k=0}^{n} \dbinom{n}{k} p^{n-k} q^k$."
                ),
                (
                    f"Let $p = {ax}$ and $q = {b}$, then compute each term for "
                    f"$k = 0, 1, \\ldots, {n}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Let $p = {ax}$ and $q = {b}$. The binomial theorem gives "
                    rf"$(p + q)^{{{n}}} = \sum_{{k=0}}^{{{n}}} \dbinom{{{n}}}{{k}} p^{{{n}-k}} q^{{k}}$."
                ),
                (
                    f"Apply to ${orig}$: expand each term using the binomial "
                    "coefficients."
                ),
                f"Combine like terms to obtain ${expanded_latex}$.",
            ],
            tags=BINOMIAL_TAGS,
        )


@register
class BinomialSpecificTerm(Generator):
    """Given $(x + b)^n$ and a term number, find just that term using
    $T_{k+1} = \\binom{n}{k} x^{n-k} b^k$ (1-indexed term number).

    Backward: pick clean $n$ (4-8), small integer $b$ (avoiding $b = 0$),
    and term index.
    """
    generator_id = "binomial_specific_term"
    topic_slug = "binomial"
    display_name = "Find a specific term in the expansion of (x + b)^n"

    _N_RANGES = {"easy": (4, 6), "medium": (5, 8), "hard": (6, 10)}
    _B_CHOICES = {
        "easy": (1, 2, 3, -1, -2),
        "medium": (1, 2, 3, 4, -1, -2, -3),
        "hard": (1, 2, 3, 4, 5, -1, -2, -3, -4),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)
        b = rng.choice(self._B_CHOICES[difficulty])
        # term index (1-indexed): 2..n
        term_idx = rng.randint(2, n)
        k = term_idx - 1  # exponent of b in this term

        binom = math.comb(n, k)
        b_power = b ** k
        coef = binom * b_power
        x_exp = n - k

        # Render the term
        if x_exp == 0:
            x_latex = ""
        elif x_exp == 1:
            x_latex = "x"
        else:
            x_latex = f"x^{{{x_exp}}}"
        if coef == 1 and x_latex:
            term_latex = x_latex
        elif coef == -1 and x_latex:
            term_latex = f"-{x_latex}"
        elif x_latex:
            term_latex = f"{coef}{x_latex}"
        else:
            term_latex = f"{coef}"

        # Ordinal word for term index
        ordinals = {
            2: "second", 3: "third", 4: "fourth", 5: "fifth",
            6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth",
        }
        ord_word = ordinals.get(term_idx, f"{term_idx}th")

        if b >= 0:
            expr_latex = f"(x + {b})^{{{n}}}"
        else:
            expr_latex = f"(x - {abs(b)})^{{{n}}}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, b, term_idx)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the {ord_word} term in the expansion of ${expr_latex}$ "
                "(arranged in descending powers of $x$)."
            ),
            answer_latex=f"${term_latex}$",
            hints=[
                (
                    r"The general term is $T_{k+1} = \dbinom{n}{k} x^{n-k} b^{k}$ "
                    r"when expanding $(x + b)^n$."
                ),
                (
                    f"For the {ord_word} term, set $k = {k}$ (since $T_{{k+1}}$ "
                    f"is the $(k+1)$th term)."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Use $T_{k+1} = \dbinom{n}{k} x^{n-k} b^{k}$."
                ),
                (
                    f"For the {ord_word} term, $k = {k}$, so "
                    f"$T_{{{term_idx}}} = \\dbinom{{{n}}}{{{k}}} x^{{{x_exp}}} "
                    f"({b})^{{{k}}}$."
                ),
                (
                    f"Compute the pieces: $\\dbinom{{{n}}}{{{k}}} = {binom}$ and "
                    f"$({b})^{{{k}}} = {b_power}$."
                ),
                f"Multiply: $T_{{{term_idx}}} = {term_latex}$.",
            ],
            tags=BINOMIAL_TAGS,
        )


# ===========================================================================
# Topic 6: induction  (pre-calculus)
# ===========================================================================


@register
class InductionBaseCaseCheck(Generator):
    """Given a claimed sum formula and a base value, compute both sides and verify.

    Backward: pick a known-true closed form (sum of k, sum of odd k, sum of k^2),
    a small base value, and show the two sides agree.
    """
    generator_id = "induction_base_case_check"
    topic_slug = "induction"
    display_name = "Verify the base case of a sum identity"

    # Each template: (key, statement_lhs_latex, formula_latex_of_n, compute_lhs(n), compute_rhs(n))
    _TEMPLATES = [
        (
            "sum_k",
            r"\sum_{k=1}^{n} k",
            r"\dfrac{n(n+1)}{2}",
            lambda n: sum(range(1, n + 1)),
            lambda n: n * (n + 1) // 2,
        ),
        (
            "sum_odd",
            r"\sum_{k=1}^{n} (2k - 1)",
            r"n^{2}",
            lambda n: sum(2 * k - 1 for k in range(1, n + 1)),
            lambda n: n ** 2,
        ),
        (
            "sum_k_squared",
            r"\sum_{k=1}^{n} k^{2}",
            r"\dfrac{n(n+1)(2n+1)}{6}",
            lambda n: sum(k * k for k in range(1, n + 1)),
            lambda n: n * (n + 1) * (2 * n + 1) // 6,
        ),
        (
            "sum_k_cubed",
            r"\sum_{k=1}^{n} k^{3}",
            r"\left(\dfrac{n(n+1)}{2}\right)^{2}",
            lambda n: sum(k ** 3 for k in range(1, n + 1)),
            lambda n: (n * (n + 1) // 2) ** 2,
        ),
        (
            "sum_2k",
            r"\sum_{k=1}^{n} 2k",
            r"n(n+1)",
            lambda n: sum(2 * k for k in range(1, n + 1)),
            lambda n: n * (n + 1),
        ),
    ]

    _N_CHOICES = {"easy": (1, 2), "medium": (1, 2, 3), "hard": (1, 2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randint(0, len(self._TEMPLATES) - 1)
        key, lhs_latex, rhs_latex, lhs_fn, rhs_fn = self._TEMPLATES[idx]
        n = rng.choice(self._N_CHOICES[difficulty])

        lhs_val = lhs_fn(n)
        rhs_val = rhs_fn(n)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (key, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Verify the base case $n = {n}$ for the statement "
                f"${lhs_latex} = {rhs_latex}$ by computing both sides."
            ),
            answer_latex=(
                f"Both sides equal ${lhs_val}$, so the base case holds."
            ),
            hints=[
                (
                    "The base case of a proof by induction is computing both sides "
                    "of the claimed identity for the smallest allowed value of $n$."
                ),
                f"Substitute $n = {n}$ into the left-hand sum and the right-hand formula, then compare.",
            ],
            solution_steps_latex=[
                (
                    f"Left side with $n = {n}$: ${lhs_latex}\\big|_{{n={n}}} = {lhs_val}$."
                ),
                (
                    f"Right side with $n = {n}$: ${rhs_latex}\\big|_{{n={n}}} = {rhs_val}$."
                ),
                (
                    f"Since ${lhs_val} = {rhs_val}$, the base case $n = {n}$ is verified."
                ),
            ],
            tags=PRECALC_SEQ_TAGS,
        )


@register
class InductionInductiveStepSetup(Generator):
    """Given a statement $P(n)$ (a sum identity), write what $P(k+1)$ looks like
    by substituting $n = k+1$. Multi-part: state the LHS and the RHS of $P(k+1)$.
    """
    generator_id = "induction_inductive_step_setup"
    topic_slug = "induction"
    display_name = "Write P(k+1) for a sum-identity induction statement"

    bank_count_per_difficulty = 10

    _TEMPLATES = [
        (
            "sum_k",
            r"\sum_{i=1}^{n} i",
            r"\dfrac{n(n+1)}{2}",
            r"\sum_{i=1}^{k+1} i",
            r"\dfrac{(k+1)(k+2)}{2}",
        ),
        (
            "sum_odd",
            r"\sum_{i=1}^{n} (2i - 1)",
            r"n^{2}",
            r"\sum_{i=1}^{k+1} (2i - 1)",
            r"(k+1)^{2}",
        ),
        (
            "sum_k_squared",
            r"\sum_{i=1}^{n} i^{2}",
            r"\dfrac{n(n+1)(2n+1)}{6}",
            r"\sum_{i=1}^{k+1} i^{2}",
            r"\dfrac{(k+1)(k+2)(2k+3)}{6}",
        ),
        (
            "sum_k_cubed",
            r"\sum_{i=1}^{n} i^{3}",
            r"\left(\dfrac{n(n+1)}{2}\right)^{2}",
            r"\sum_{i=1}^{k+1} i^{3}",
            r"\left(\dfrac{(k+1)(k+2)}{2}\right)^{2}",
        ),
        (
            "sum_2k",
            r"\sum_{i=1}^{n} 2i",
            r"n(n+1)",
            r"\sum_{i=1}^{k+1} 2i",
            r"(k+1)(k+2)",
        ),
        (
            "sum_three_k",
            r"\sum_{i=1}^{n} 3i",
            r"\dfrac{3n(n+1)}{2}",
            r"\sum_{i=1}^{k+1} 3i",
            r"\dfrac{3(k+1)(k+2)}{2}",
        ),
        (
            "sum_4k",
            r"\sum_{i=1}^{n} 4i",
            r"2n(n+1)",
            r"\sum_{i=1}^{k+1} 4i",
            r"2(k+1)(k+2)",
        ),
        (
            "sum_5k",
            r"\sum_{i=1}^{n} 5i",
            r"\dfrac{5n(n+1)}{2}",
            r"\sum_{i=1}^{k+1} 5i",
            r"\dfrac{5(k+1)(k+2)}{2}",
        ),
        (
            "sum_2_pow_i",
            r"\sum_{i=1}^{n} 2^{i}",
            r"2^{n+1} - 2",
            r"\sum_{i=1}^{k+1} 2^{i}",
            r"2^{k+2} - 2",
        ),
        (
            "sum_3_pow_i",
            r"\sum_{i=1}^{n} 3^{i}",
            r"\dfrac{3^{n+1} - 3}{2}",
            r"\sum_{i=1}^{k+1} 3^{i}",
            r"\dfrac{3^{k+2} - 3}{2}",
        ),
        (
            "sum_two_i_plus_1",
            r"\sum_{i=1}^{n} (2i + 1)",
            r"n(n + 2)",
            r"\sum_{i=1}^{k+1} (2i + 1)",
            r"(k + 1)(k + 3)",
        ),
        (
            "sum_three_i_minus_2",
            r"\sum_{i=1}^{n} (3i - 2)",
            r"\dfrac{n(3n - 1)}{2}",
            r"\sum_{i=1}^{k+1} (3i - 2)",
            r"\dfrac{(k + 1)(3k + 2)}{2}",
        ),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randint(0, len(self._TEMPLATES) - 1)
        key, lhs_n, rhs_n, lhs_k1, rhs_k1 = self._TEMPLATES[idx]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (key, difficulty)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $P(n)$ be the statement ${lhs_n} = {rhs_n}$. Write the "
                "statement $P(k+1)$ by substituting $n = k+1$."
            ),
            answer_latex=f"$P(k+1)$: ${lhs_k1} = {rhs_k1}$",
            hints=[
                (
                    "To get $P(k+1)$, replace every occurrence of $n$ in $P(n)$ with $k+1$."
                ),
                (
                    "Update both the upper limit of the sum AND the right-hand formula."
                ),
            ],
            solution_steps_latex=[
                (
                    f"$P(n)$ is ${lhs_n} = {rhs_n}$."
                ),
                (
                    r"Substitute $n \to k+1$ on both sides."
                ),
                (
                    f"Left side becomes ${lhs_k1}$ and right side becomes ${rhs_k1}$."
                ),
                (
                    f"Therefore $P(k+1)$ is ${lhs_k1} = {rhs_k1}$."
                ),
            ],
            tags=PRECALC_SEQ_TAGS,
        )


@register
class InductionComputeSumViaFormula(Generator):
    """Given a claimed sum formula, compute the direct sum and the formula for a
    specific $n$ and verify they agree.
    """
    generator_id = "induction_compute_sum_via_formula"
    topic_slug = "induction"
    display_name = "Verify a sum identity at a specific n"

    bank_count_per_difficulty = 15

    _TEMPLATES = [
        (
            "sum_k",
            r"\sum_{k=1}^{n} k",
            r"\dfrac{n(n+1)}{2}",
            lambda n: sum(range(1, n + 1)),
            lambda n: n * (n + 1) // 2,
        ),
        (
            "sum_odd",
            r"\sum_{k=1}^{n} (2k - 1)",
            r"n^{2}",
            lambda n: sum(2 * k - 1 for k in range(1, n + 1)),
            lambda n: n ** 2,
        ),
        (
            "sum_k_squared",
            r"\sum_{k=1}^{n} k^{2}",
            r"\dfrac{n(n+1)(2n+1)}{6}",
            lambda n: sum(k * k for k in range(1, n + 1)),
            lambda n: n * (n + 1) * (2 * n + 1) // 6,
        ),
    ]

    _N_RANGES = {"easy": (3, 7), "medium": (4, 9), "hard": (5, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randint(0, len(self._TEMPLATES) - 1)
        key, lhs_latex, rhs_latex, lhs_fn, rhs_fn = self._TEMPLATES[idx]
        n_lo, n_hi = self._N_RANGES[difficulty]
        n = rng.randint(n_lo, n_hi)

        direct = lhs_fn(n)
        via_formula = rhs_fn(n)

        # Show the expanded terms for the direct sum
        if key == "sum_k":
            expansion = " + ".join(str(k) for k in range(1, n + 1))
        elif key == "sum_odd":
            expansion = " + ".join(str(2 * k - 1) for k in range(1, n + 1))
        else:
            expansion = " + ".join(f"{k}^{{2}}" for k in range(1, n + 1))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (key, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For $n = {n}$, verify that ${lhs_latex} = {rhs_latex}$ by "
                "computing both the direct sum and the closed-form formula."
            ),
            answer_latex=(
                f"Both sides equal ${direct}$, so the identity holds for $n = {n}$."
            ),
            hints=[
                (
                    f"Compute the left-hand side by adding the ${n}$ terms one at a time."
                ),
                (
                    f"Compute the right-hand side by plugging $n = {n}$ into the formula."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Direct sum: ${lhs_latex}\\big|_{{n={n}}} = {expansion} = {direct}$."
                ),
                (
                    f"Formula: ${rhs_latex}\\big|_{{n={n}}} = {via_formula}$."
                ),
                (
                    f"Both give ${direct}$, so the identity is verified for $n = {n}$."
                ),
            ],
            tags=PRECALC_SEQ_TAGS,
        )


# ===========================================================================
# Topic 7: mean_median_mode_and_range  (pre-algebra)
# ===========================================================================


STATS_TAGS = ["#branch-pre-algebra", "#topic-statistics"]


def _mode_value(values: list[int]) -> int | None:
    """Return the unique mode, or None if no unique mode exists.

    If multiple values share the highest frequency, returns None.
    """
    counts: dict[int, int] = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    max_count = max(counts.values())
    if max_count == 1:
        return None  # all distinct
    modes = [v for v, c in counts.items() if c == max_count]
    if len(modes) == 1:
        return modes[0]
    return None


@register
class MMMComputeFromList(Generator):
    """Given a list of 5-8 numbers, compute mean, median, mode, and range.

    Backward: pick the list so that the mean is an integer (choose values that
    sum to a multiple of the list length), the median is well-defined, and the
    list has a unique mode.
    """
    generator_id = "mmm_compute_from_list"
    topic_slug = "mean_median_mode_and_range"
    display_name = "Compute mean, median, mode, and range from a data set"

    _LEN_CHOICES = {"easy": (5, 7), "medium": (5, 7), "hard": (6, 8)}
    _VAL_RANGES = {"easy": (2, 15), "medium": (5, 25), "hard": (1, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        length_choices = self._LEN_CHOICES[difficulty]
        val_lo, val_hi = self._VAL_RANGES[difficulty]

        attempts = 0
        while attempts < 50:
            attempts += 1
            length = rng.choice(length_choices)
            # Build list with a forced duplicate so mode is unique
            values: list[int] = []
            dup = rng.randint(val_lo, val_hi)
            values.append(dup)
            values.append(dup)
            while len(values) < length:
                v = rng.randint(val_lo, val_hi)
                if values.count(v) < 2 and v != dup:
                    values.append(v)

            mean_val = sum(values) / length
            if mean_val != int(mean_val):
                continue  # require integer mean
            mean_int = int(mean_val)
            mode = _mode_value(values)
            if mode is None:
                continue
            break
        else:
            # Fallback: simple 5-element list
            values = [2, 3, 3, 4, 8]
            length = 5
            mean_int = 4
            mode = 3

        sorted_vals = sorted(values)
        median_val = median(sorted_vals)
        range_val = max(values) - min(values)
        # Render median cleanly (integer or halved integer)
        if length % 2 == 1:
            median_latex = str(sorted_vals[length // 2])
        else:
            a = sorted_vals[length // 2 - 1]
            b = sorted_vals[length // 2]
            if (a + b) % 2 == 0:
                median_latex = str((a + b) // 2)
            else:
                median_latex = _render_frac(a + b, 2)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(values)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "For the data set "
                f"$\\{{{_format_list(values)}\\}}$, find the mean, median, "
                "mode, and range."
            ),
            answer_latex=(
                f"mean $= {mean_int}$, median $= {median_latex}$, "
                f"mode $= {mode}$, range $= {range_val}$"
            ),
            hints=[
                "Sort the values. Mean = sum divided by count. Median = middle value (or average of two middles). Mode = most frequent value. Range = max minus min.",
                f"The sum of the data set is ${sum(values)}$ and it has ${length}$ values.",
            ],
            solution_steps_latex=[
                (
                    f"Sort: $\\{{{_format_list(sorted_vals)}\\}}$."
                ),
                (
                    f"Mean: $\\dfrac{{{sum(values)}}}{{{length}}} = {mean_int}$."
                ),
                (
                    f"Median: the middle of the sorted list is ${median_latex}$."
                ),
                (
                    f"Mode (most frequent value): ${mode}$."
                ),
                (
                    f"Range: $\\max - \\min = {max(values)} - {min(values)} = {range_val}$."
                ),
            ],
            tags=STATS_TAGS,
        )


@register
class MMMIdentifyOutlierImpact(Generator):
    """Given a small baseline data set and a new (outlier) value, compare how
    the mean changes vs how the median changes when the value is added.

    Backward: pick a baseline whose mean and median are integers; pick an
    outlier well outside the baseline range.
    """
    generator_id = "mmm_identify_outlier_impact"
    topic_slug = "mean_median_mode_and_range"
    display_name = "Compare how an outlier affects the mean vs the median"

    # Baseline lists engineered to have integer mean and median
    _BASELINES_EASY = [
        ([4, 5, 6, 7, 8], 6, 6),  # mean 6, median 6
        ([3, 4, 5, 6, 7], 5, 5),
        ([10, 11, 12, 13, 14], 12, 12),
        ([2, 4, 6, 8, 10], 6, 6),
        ([5, 6, 7, 8, 9], 7, 7),
    ]
    _BASELINES_MED = [
        ([8, 10, 12, 14, 16], 12, 12),
        ([1, 3, 5, 7, 9], 5, 5),
        ([20, 22, 24, 26, 28], 24, 24),
        ([4, 6, 8, 10, 12], 8, 8),
        ([15, 17, 19, 21, 23], 19, 19),
        ([6, 9, 12, 15, 18], 12, 12),
    ]
    _BASELINES_HARD = [
        ([12, 14, 16, 18, 20, 22, 24], 18, 18),
        ([5, 8, 11, 14, 17, 20, 23], 14, 14),
        ([10, 15, 20, 25, 30, 35, 40], 25, 25),
        ([4, 6, 8, 10, 12, 14, 16], 10, 10),
        ([25, 27, 29, 31, 33, 35, 37], 31, 31),
    ]

    # Outlier pools (well outside typical baselines above)
    _OUTLIERS = (80, 90, 100, 120, 150, 200)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        baselines = {
            "easy": self._BASELINES_EASY,
            "medium": self._BASELINES_MED,
            "hard": self._BASELINES_HARD,
        }[difficulty]
        idx = rng.randint(0, len(baselines) - 1)
        base, base_mean, base_median = baselines[idx]
        outlier = rng.choice(self._OUTLIERS)

        new_list = sorted(base + [outlier])
        new_length = len(new_list)
        new_mean_exact = sp.Rational(sum(new_list), new_length)
        if new_length % 2 == 1:
            new_median = new_list[new_length // 2]
        else:
            a = new_list[new_length // 2 - 1]
            b = new_list[new_length // 2]
            new_median = sp.Rational(a + b, 2)

        new_mean_latex = _render_rational(new_mean_exact)
        new_median_latex = (
            str(new_median) if isinstance(new_median, int) else _render_rational(new_median)
        )
        mean_diff = new_mean_exact - base_mean
        median_diff_numeric = (new_median - base_median) if isinstance(new_median, int) else (new_median - sp.Rational(base_median))
        mean_diff_latex = _render_rational(sp.Rational(mean_diff))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (tuple(base), outlier)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A small data set is $\\{{{_format_list(base)}\\}}$. A new "
                f"value of ${outlier}$ is added to the set. Compare the change "
                f"in the mean with the change in the median, and explain which "
                "is more affected by the outlier."
            ),
            answer_latex=(
                f"Original mean $= {base_mean}$; new mean $= {new_mean_latex}$; "
                f"original median $= {base_median}$; new median $= {new_median_latex}$. "
                f"The mean increases by ${mean_diff_latex}$, while the median "
                "changes only slightly. The mean is more affected by the outlier."
            ),
            hints=[
                "Compute the mean and median of the original set, then do the same after adding the new value.",
                "A single extreme value pulls the mean strongly but typically moves the median by only one position in the sorted list.",
            ],
            solution_steps_latex=[
                (
                    f"Original set $\\{{{_format_list(base)}\\}}$: mean "
                    f"$= {base_mean}$, median $= {base_median}$."
                ),
                (
                    f"New set $\\{{{_format_list(new_list)}\\}}$ has "
                    f"${new_length}$ values summing to ${sum(new_list)}$, "
                    f"so the new mean is $\\dfrac{{{sum(new_list)}}}{{{new_length}}} "
                    f"= {new_mean_latex}$."
                ),
                (
                    f"New median: the middle of the sorted list is ${new_median_latex}$."
                ),
                (
                    f"The mean changed by ${mean_diff_latex}$, while the median "
                    f"only shifted slightly. The outlier pulled the mean strongly."
                ),
            ],
            tags=STATS_TAGS,
        )


@register
class MMMFindMissingValueForTargetMean(Generator):
    """Given $n-1$ values and a target mean, find the missing $n$th value.

    Backward: pick target mean and $n-1$ values first so the missing value is
    a clean integer.
    """
    generator_id = "mmm_find_missing_value_for_target_mean"
    topic_slug = "mean_median_mode_and_range"
    display_name = "Find the missing value needed to reach a target mean"

    _LEN_CHOICES = {"easy": (4, 5), "medium": (5, 6), "hard": (6, 7)}
    _VAL_RANGES = {"easy": (1, 15), "medium": (2, 25), "hard": (5, 40)}
    _MEAN_RANGES = {"easy": (5, 12), "medium": (8, 20), "hard": (10, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        length_choices = self._LEN_CHOICES[difficulty]
        val_lo, val_hi = self._VAL_RANGES[difficulty]
        mean_lo, mean_hi = self._MEAN_RANGES[difficulty]

        attempts = 0
        while attempts < 60:
            attempts += 1
            n = rng.choice(length_choices)
            mean_target = rng.randint(mean_lo, mean_hi)
            known = [rng.randint(val_lo, val_hi) for _ in range(n - 1)]
            missing = n * mean_target - sum(known)
            if 1 <= missing <= max(val_hi * 3, 60):
                break
        else:
            # Safe fallback
            n = 5
            mean_target = 10
            known = [8, 9, 11, 12]
            missing = 10

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (tuple(known), n, mean_target)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A student's first ${n - 1}$ quiz scores are "
                f"$\\{{{_format_list(known)}\\}}$. What score must the student "
                f"earn on the ${n}$th quiz so the mean of all ${n}$ quizzes is "
                f"${mean_target}$?"
            ),
            answer_latex=f"${missing}$",
            hints=[
                "If the mean of $n$ values equals $M$, then the total must be $n \\cdot M$.",
                f"Compute the required total and subtract the sum of the ${n - 1}$ known values.",
            ],
            solution_steps_latex=[
                (
                    f"Required total for ${n}$ values with mean ${mean_target}$: "
                    f"${n} \\cdot {mean_target} = {n * mean_target}$."
                ),
                (
                    f"Sum of the known values: ${_format_list(known)}$ gives ${sum(known)}$."
                ),
                (
                    f"Missing value: ${n * mean_target} - {sum(known)} = {missing}$."
                ),
            ],
            tags=STATS_TAGS,
        )


# ===========================================================================
# Topic 8: data_displays  (pre-algebra)
# ===========================================================================


DATA_DISPLAY_TAGS = ["#branch-pre-algebra", "#topic-statistics"]


@register
class BarGraphReadValues(Generator):
    """Given a described bar graph (as a text table of categories and values),
    ask for a specific reading (max, min, total, difference between two bars,
    or the value for one category).
    """
    generator_id = "bar_graph_read_values"
    topic_slug = "data_displays"
    display_name = "Read a value from a bar graph described in a table"

    _CATEGORY_POOLS = [
        ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"),
        ("January", "February", "March", "April"),
        ("Red", "Blue", "Green", "Yellow"),
        ("Math", "Science", "English", "History"),
        ("Apples", "Bananas", "Pears", "Oranges"),
        ("Soccer", "Baseball", "Football", "Tennis"),
    ]

    _THEMES = {
        "Monday": "customers visiting the ice-cream shop",
        "Red": "students wearing each color shirt",
        "January": "books borrowed each month",
        "Math": "students choosing each subject as their favorite",
        "Apples": "pieces of fruit sold that day",
        "Soccer": "students signed up for each sport",
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pool = rng.choice(self._CATEGORY_POOLS)
        first = pool[0]
        scenario = self._THEMES.get(first, "items in each category")
        categories = list(pool)
        # Pick integer values in a reasonable range
        if difficulty == "easy":
            values = [rng.randint(3, 15) for _ in categories]
        elif difficulty == "medium":
            values = [rng.randint(5, 40) for _ in categories]
        else:
            values = [rng.randint(8, 80) for _ in categories]

        # Force them distinct enough
        while len(set(values)) < len(values):
            values = [v + rng.randint(0, 2) for v in values]

        # Render the graph as a text description
        rows = "; ".join(f"{c}: {v}" for c, v in zip(categories, values))

        # Choose a question type
        qtype = rng.choice(["max", "min", "total", "diff", "specific"])
        if qtype == "max":
            answer = max(values)
            cat = categories[values.index(answer)]
            q = f"Which category has the greatest value, and what is that value?"
            ans_latex = f"{cat} with a value of {answer}"
            step = f"The largest value in the list is ${answer}$, which belongs to {cat}."
        elif qtype == "min":
            answer = min(values)
            cat = categories[values.index(answer)]
            q = f"Which category has the smallest value, and what is that value?"
            ans_latex = f"{cat} with a value of {answer}"
            step = f"The smallest value in the list is ${answer}$, which belongs to {cat}."
        elif qtype == "total":
            answer = sum(values)
            q = "What is the total across all categories shown?"
            ans_latex = f"${answer}$"
            step = f"Add every value: ${' + '.join(str(v) for v in values)} = {answer}$."
        elif qtype == "diff":
            a_idx, b_idx = rng.sample(range(len(categories)), 2)
            cat_a = categories[a_idx]
            cat_b = categories[b_idx]
            diff = abs(values[a_idx] - values[b_idx])
            q = f"How much more is {cat_a} than {cat_b}? (Give the absolute difference.)"
            ans_latex = f"${diff}$"
            step = f"Compute $|{values[a_idx]} - {values[b_idx]}| = {diff}$."
        else:  # specific
            spec_idx = rng.randint(0, len(categories) - 1)
            q = f"What is the value for {categories[spec_idx]}?"
            ans_latex = f"${values[spec_idx]}$"
            step = f"Read the bar for {categories[spec_idx]}: the value is ${values[spec_idx]}$."

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (tuple(categories), tuple(values), qtype),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A bar graph shows the number of {scenario}. The bars are as "
                f"follows (category: height): {rows}. {q}"
            ),
            answer_latex=ans_latex,
            hints=[
                "Read each bar by matching it to the table of values described.",
                "Think about whether the question asks for a single value, a total, a difference, or an extreme.",
            ],
            solution_steps_latex=[
                (
                    f"List the values: {rows}."
                ),
                step,
            ],
            tags=DATA_DISPLAY_TAGS,
        )


@register
class PieChartPercentToCount(Generator):
    """Given a pie-chart slice as a percentage and a total, compute the count.

    Backward: pick total and percentage so the count is a whole number.
    """
    generator_id = "pie_chart_percent_to_count"
    topic_slug = "data_displays"
    display_name = "Convert a pie-chart percentage to a count"

    _PERCENT_CHOICES = (5, 10, 20, 25, 40, 50, 75)
    _TOTAL_CHOICES = {
        "easy": (20, 40, 50, 80, 100, 200),
        "medium": (120, 150, 160, 180, 240, 300, 360, 400),
        "hard": (250, 320, 500, 600, 720, 800, 1000, 1200),
    }

    _CATEGORIES = (
        ("students", "preferred the library"),
        ("shoppers", "chose the blue product"),
        ("voters", "picked candidate A"),
        ("survey participants", "watch sports on weekends"),
        ("books", "were nonfiction"),
        ("movies", "were comedies"),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        totals = self._TOTAL_CHOICES[difficulty]
        # Loop until (percent/100)*total is an integer
        attempts = 0
        while attempts < 50:
            attempts += 1
            pct = rng.choice(self._PERCENT_CHOICES)
            total = rng.choice(totals)
            if (pct * total) % 100 == 0:
                break
        else:
            pct = 25
            total = 100
        count = (pct * total) // 100

        entity, clause = rng.choice(self._CATEGORIES)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (pct, total, entity, clause)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A pie chart shows that ${pct}\\%$ of ${total}$ {entity} {clause}. "
                f"How many {entity} does that slice represent?"
            ),
            answer_latex=f"${count}$",
            hints=[
                f"Convert ${pct}\\%$ to a decimal or fraction, then multiply by the total.",
                f"${pct}\\% \\text{{ of }} {total} = \\dfrac{{{pct}}}{{100}} \\cdot {total}$.",
            ],
            solution_steps_latex=[
                (
                    rf"Write the percentage as a fraction: ${pct}\% = \dfrac{{{pct}}}{{100}}$."
                ),
                (
                    rf"Multiply by the total: "
                    rf"$\dfrac{{{pct}}}{{100}} \cdot {total} = \dfrac{{{pct * total}}}{{100}} = {count}$."
                ),
                f"So the slice represents ${count}$ {entity}.",
            ],
            tags=DATA_DISPLAY_TAGS,
        )


@register
class StemLeafCountInRange(Generator):
    """Given a stem-and-leaf plot described in text, count values in a given range.

    Backward: pick stems and leaves, choose a numeric range, count the matches.
    """
    generator_id = "stem_leaf_count_in_range"
    topic_slug = "data_displays"
    display_name = "Count values in a range from a stem-and-leaf plot"

    bank_count_per_difficulty = 18

    _STEM_POOLS = {
        "easy": [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)],
        "medium": [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), (4, 5, 6, 7)],
        "hard": [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7)],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        stems = rng.choice(self._STEM_POOLS[difficulty])
        plot: dict[int, list[int]] = {}
        all_values: list[int] = []
        for s in stems:
            leaf_count = rng.randint(3, 6)
            leaves: list[int] = []
            while len(leaves) < leaf_count:
                leaf = rng.randint(0, 9)
                leaves.append(leaf)
            leaves.sort()
            plot[s] = leaves
            for leaf in leaves:
                all_values.append(10 * s + leaf)

        # Pick a range [low, high]
        lo_val = min(all_values) + rng.randint(0, 5)
        hi_val = lo_val + rng.randint(5, 25)
        count_in = sum(1 for v in all_values if lo_val <= v <= hi_val)

        # Render plot as text lines
        plot_lines = "; ".join(
            f"stem {s}: leaves {' '.join(str(l) for l in plot[s])}"
            for s in stems
        )
        values_list = _format_list(sorted(all_values))

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (stems, tuple(tuple(plot[s]) for s in stems), lo_val, hi_val),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A stem-and-leaf plot (stems on the left, leaves on the right) "
                f"has the following rows: {plot_lines}. How many data values fall "
                f"in the range from ${lo_val}$ to ${hi_val}$ (inclusive)?"
            ),
            answer_latex=f"${count_in}$",
            hints=[
                (
                    "A stem-leaf entry like stem $3$, leaves $2\\ 5\\ 8$ represents "
                    "the data values $32$, $35$, $38$."
                ),
                f"Convert every stem-leaf row to its values, then count those in $[{lo_val}, {hi_val}]$.",
            ],
            solution_steps_latex=[
                (
                    "Expand every row to its underlying values by pasting each "
                    "leaf after its stem digit."
                ),
                (
                    f"The full data set is $\\{{{values_list}\\}}$."
                ),
                (
                    f"Count how many lie in $[{lo_val}, {hi_val}]$: the answer is ${count_in}$."
                ),
            ],
            tags=DATA_DISPLAY_TAGS,
        )


# ===========================================================================
# Topic 9: data_displays_and_measures_of_spread  (pre-algebra)
# ===========================================================================


SPREAD_TAGS = ["#branch-pre-algebra", "#topic-statistics"]


def _five_number_summary(values: list[int]) -> tuple[int, sp.Rational | int, sp.Rational | int, sp.Rational | int, int]:
    """Compute (min, Q1, median, Q3, max) using the exclusive method.

    For a sorted list of n values:
      - Median is the middle (or average of the two middles).
      - Q1 is the median of the lower half (not including the overall median if n is odd).
      - Q3 is the median of the upper half (not including the overall median if n is odd).
    Returns Q1, Q2, Q3 as ints if exact, otherwise as sympy Rationals.
    """
    n = len(values)
    sorted_vals = sorted(values)

    def _med(arr: list[int]) -> sp.Rational | int:
        m = len(arr)
        if m % 2 == 1:
            return arr[m // 2]
        a = arr[m // 2 - 1]
        b = arr[m // 2]
        if (a + b) % 2 == 0:
            return (a + b) // 2
        return sp.Rational(a + b, 2)

    if n % 2 == 0:
        lower = sorted_vals[: n // 2]
        upper = sorted_vals[n // 2:]
    else:
        lower = sorted_vals[: n // 2]
        upper = sorted_vals[n // 2 + 1:]

    q1 = _med(lower)
    q2 = _med(sorted_vals)
    q3 = _med(upper)
    return sorted_vals[0], q1, q2, q3, sorted_vals[-1]


def _fmt_quartile(q: sp.Rational | int) -> str:
    if isinstance(q, int):
        return str(q)
    return _render_rational(q)


@register
class FiveNumberSummary(Generator):
    """Given a sorted list of 7, 9, or 11 values, compute the five-number summary.

    Backward: pick the list so min/max are integers and Q1, median, Q3 are
    integers (the list length is odd so we use the exclusive method).
    """
    generator_id = "five_number_summary"
    topic_slug = "data_displays_and_measures_of_spread"
    display_name = "Compute the five-number summary of a data set"

    _LEN_CHOICES = {"easy": (7, 9), "medium": (7, 9, 11), "hard": (9, 11)}
    _VAL_RANGES = {"easy": (2, 25), "medium": (5, 40), "hard": (5, 60)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        length_choices = self._LEN_CHOICES[difficulty]
        val_lo, val_hi = self._VAL_RANGES[difficulty]

        attempts = 0
        while attempts < 60:
            attempts += 1
            length = rng.choice(length_choices)
            # Build odd-length list to guarantee integer quartiles in lower/upper halves
            if length % 2 == 0:
                length = length + 1  # force odd for clean quartiles
            # Generate distinct values
            pool = rng.sample(range(val_lo, val_hi + 1), length)
            pool.sort()
            min_v, q1, med, q3, max_v = _five_number_summary(pool)
            # Require all quartiles are integers
            if not (isinstance(q1, int) and isinstance(med, int) and isinstance(q3, int)):
                continue
            break
        else:
            pool = [3, 5, 8, 10, 12, 14, 17]
            min_v, q1, med, q3, max_v = _five_number_summary(pool)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, tuple(pool)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the sorted data set $\\{{{_format_list(pool)}\\}}$, find "
                "the five-number summary (min, $Q_1$, median, $Q_3$, max)."
            ),
            answer_latex=(
                f"min $= {min_v}$, $Q_1 = {_fmt_quartile(q1)}$, median $= {_fmt_quartile(med)}$, "
                f"$Q_3 = {_fmt_quartile(q3)}$, max $= {max_v}$"
            ),
            hints=[
                "Sort the list, then find the median. $Q_1$ is the median of the lower half, $Q_3$ is the median of the upper half.",
                "For an odd-length list, exclude the overall median when finding $Q_1$ and $Q_3$.",
            ],
            solution_steps_latex=[
                (
                    f"The data are already sorted: $\\{{{_format_list(pool)}\\}}$."
                ),
                (
                    f"Minimum is ${min_v}$ and maximum is ${max_v}$."
                ),
                (
                    f"The overall median is ${_fmt_quartile(med)}$."
                ),
                (
                    f"$Q_1$ is the median of the lower half: ${_fmt_quartile(q1)}$."
                ),
                (
                    f"$Q_3$ is the median of the upper half: ${_fmt_quartile(q3)}$."
                ),
            ],
            tags=SPREAD_TAGS,
        )


@register
class IQRCompute(Generator):
    """Given Q1 and Q3 directly, or a small sorted list, compute IQR = Q3 - Q1.

    Backward: pick Q1 and Q3 so IQR is a clean positive integer.
    """
    generator_id = "iqr_compute"
    topic_slug = "data_displays_and_measures_of_spread"
    display_name = "Compute the interquartile range (IQR)"

    _Q1_RANGES = {"easy": (2, 15), "medium": (5, 25), "hard": (5, 40)}
    _IQR_RANGES = {"easy": (3, 12), "medium": (5, 20), "hard": (6, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        mode = rng.choice(["direct", "list"])
        q1_lo, q1_hi = self._Q1_RANGES[difficulty]
        iqr_lo, iqr_hi = self._IQR_RANGES[difficulty]
        q1 = rng.randint(q1_lo, q1_hi)
        iqr = rng.randint(iqr_lo, iqr_hi)
        q3 = q1 + iqr

        if mode == "direct":
            statement = (
                f"A data set has $Q_1 = {q1}$ and $Q_3 = {q3}$. Compute the "
                "interquartile range (IQR)."
            )
            step_one = f"Recall that $\\text{{IQR}} = Q_3 - Q_1$."
            step_two = f"Substitute: $\\text{{IQR}} = {q3} - {q1} = {iqr}$."
        else:
            # Build an odd-length list whose Q1 and Q3 match the picked values
            median_val = q1 + iqr // 2
            if median_val <= q1:
                median_val = q1 + 1
            if median_val >= q3:
                median_val = q3 - 1
            # Lower half around q1
            low1 = q1 - 1
            low2 = q1 + 1
            hi1 = q3 - 1
            hi2 = q3 + 1
            # 7-element list: low1, q1, low2, median, hi1, q3, hi2
            data = [low1, q1, low2, median_val, hi1, q3, hi2]
            data_sorted = sorted(data)
            statement = (
                f"For the sorted data set $\\{{{_format_list(data_sorted)}\\}}$, "
                "find the interquartile range (IQR)."
            )
            step_one = (
                f"Find the median (middle value), then $Q_1$ and $Q_3$ as the "
                f"medians of the lower and upper halves. Here $Q_1 = {q1}$ and "
                f"$Q_3 = {q3}$."
            )
            step_two = f"IQR $= Q_3 - Q_1 = {q3} - {q1} = {iqr}$."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (mode, q1, q3)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$\\text{{IQR}} = {iqr}$",
            hints=[
                r"The interquartile range is $\text{IQR} = Q_3 - Q_1$.",
                "Identify $Q_1$ and $Q_3$ first, then subtract.",
            ],
            solution_steps_latex=[
                step_one,
                step_two,
            ],
            tags=SPREAD_TAGS,
        )


@register
class OutlierCheckIQRRule(Generator):
    """Given $Q_1$, $Q_3$, and a candidate value, determine whether the value is
    an outlier using the 1.5 times IQR rule.

    Backward: pick $Q_1$ and $Q_3$ so 1.5 * IQR is an integer (IQR even), then
    choose a candidate value either inside or outside the fences.
    """
    generator_id = "outlier_check_iqr_rule"
    topic_slug = "data_displays_and_measures_of_spread"
    display_name = "Decide whether a value is an outlier using the 1.5 x IQR rule"

    _Q1_RANGES = {"easy": (2, 15), "medium": (5, 25), "hard": (10, 40)}
    # IQR restricted to even values so 1.5*IQR is an integer
    _EVEN_IQR = {
        "easy": (4, 6, 8, 10, 12),
        "medium": (6, 8, 10, 12, 14, 16, 20),
        "hard": (8, 10, 12, 14, 16, 18, 20, 24),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        q1_lo, q1_hi = self._Q1_RANGES[difficulty]
        q1 = rng.randint(q1_lo, q1_hi)
        iqr = rng.choice(self._EVEN_IQR[difficulty])
        q3 = q1 + iqr
        fence_lower = q1 - (3 * iqr) // 2
        fence_upper = q3 + (3 * iqr) // 2

        # Decide whether the candidate is an outlier
        make_outlier = rng.choice([True, False])
        if make_outlier:
            if rng.choice([True, False]):
                # Below lower fence
                candidate = fence_lower - rng.randint(1, 5)
            else:
                # Above upper fence
                candidate = fence_upper + rng.randint(1, 5)
            is_outlier = True
        else:
            # Pick a value safely inside the fences (not equal to the fence)
            candidate = rng.randint(fence_lower + 1, fence_upper - 1)
            is_outlier = False

        verdict = "is an outlier" if is_outlier else "is NOT an outlier"
        rule_msg = (
            f"because ${candidate}$ lies outside the interval "
            f"$[{fence_lower}, {fence_upper}]$"
            if is_outlier
            else f"because ${candidate}$ lies inside the interval "
            f"$[{fence_lower}, {fence_upper}]$"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (q1, q3, candidate, is_outlier)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A data set has $Q_1 = {q1}$ and $Q_3 = {q3}$. Using the "
                f"$1.5 \\times \\text{{IQR}}$ rule, decide whether the value "
                f"${candidate}$ is an outlier."
            ),
            answer_latex=f"${candidate}$ {verdict} {rule_msg}.",
            hints=[
                (
                    r"The $1.5 \times \text{IQR}$ rule labels a point an outlier "
                    r"if it is below $Q_1 - 1.5\,\text{IQR}$ or above $Q_3 + 1.5\,\text{IQR}$."
                ),
                f"Compute $\\text{{IQR}} = Q_3 - Q_1 = {iqr}$, then find the two fences.",
            ],
            solution_steps_latex=[
                f"Compute $\\text{{IQR}} = {q3} - {q1} = {iqr}$.",
                (
                    rf"Compute $1.5 \cdot \text{{IQR}} = 1.5 \cdot {iqr} = {(3 * iqr) // 2}$."
                ),
                (
                    f"Lower fence: $Q_1 - 1.5\\,\\text{{IQR}} = {q1} - {(3 * iqr) // 2} "
                    f"= {fence_lower}$."
                ),
                (
                    f"Upper fence: $Q_3 + 1.5\\,\\text{{IQR}} = {q3} + {(3 * iqr) // 2} "
                    f"= {fence_upper}$."
                ),
                (
                    f"The fences give the interval $[{fence_lower}, {fence_upper}]$, "
                    f"so ${candidate}$ {verdict}."
                ),
            ],
            tags=SPREAD_TAGS,
        )
