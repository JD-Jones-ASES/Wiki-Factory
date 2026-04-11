"""Polynomial foundations generators (Wave C pre-calculus).

Three topic slugs covered:

- graphs_of_polynomials                  (Graphs_Of_Polynomials.md)
- real_zeros_of_polynomials              (Real_Zeros_Of_Polynomials.md)
- real_zeros_of_polynomials_advanced     (Real_Zeros_Of_Polynomials_Advanced.md)

Nine generators total (3 per topic). Backward construction: for every
problem we pick the polynomial's zeros (or sign pattern, or leading term)
first and then derive the student-facing statement. SymPy handles exact
coefficient expansion, Descartes' rule of signs scanning, and synthetic
division so answers are always self-consistent.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Tag bundles
# ---------------------------------------------------------------------------

POLY_TAGS = ["#branch-pre-calculus", "#topic-polynomials"]

SKILL_PROCEDURAL = "#skill-procedural-calculation"
SKILL_ALGEBRAIC = "#skill-algebraic-manipulation"
SKILL_VISUALIZATION = "#skill-visualization"
SKILL_MULTI_STEP = "#skill-multi-step"
SKILL_FORMULA_SUB = "#skill-formula-substitution"


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _signed_const(n: int) -> str:
    """Render a signed constant for polynomial display."""
    if n >= 0:
        return f"+ {n}"
    return f"- {abs(n)}"


def _factor_pairs(n: int) -> list[int]:
    """Return sorted list of positive divisors of |n| (including 1 and |n|).

    ``_factor_pairs(12)`` -> ``[1, 2, 3, 4, 6, 12]``.
    ``_factor_pairs(0)`` -> ``[]`` (used as sentinel; caller handles n=0).
    """
    if n == 0:
        return []
    n = abs(n)
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def _poly_latex_from_coeffs(coeffs: list[int]) -> str:
    """Render a polynomial ``a_n x^n + ... + a_0`` from highest-degree to constant.

    Zero coefficients are dropped. Signs are rendered as ``+`` or ``-``.
    Leading term carries no leading ``+``.
    """
    n = len(coeffs) - 1
    parts: list[str] = []
    for i, c in enumerate(coeffs):
        power = n - i
        if c == 0:
            continue
        is_first = len(parts) == 0
        sign = "-" if c < 0 else ("" if is_first else "+")
        mag = abs(c)
        if power == 0:
            term = f"{mag}"
        elif power == 1:
            term = "x" if mag == 1 else f"{mag}x"
        else:
            term = f"x^{{{power}}}" if mag == 1 else f"{mag}x^{{{power}}}"
        if is_first:
            if sign == "-":
                parts.append(f"-{term}")
            else:
                parts.append(term)
        else:
            parts.append(f"{sign} {term}")
    if not parts:
        return "0"
    return " ".join(parts)


# ===========================================================================
# Topic 6: graphs_of_polynomials
# ===========================================================================


@register
class EndBehaviorFromLeadingTerm(Generator):
    """Given a leading term $a x^n$, describe end behaviour.

    Backward: pick integer $a \\ne 0$ and integer $n \\ge 1$. The four
    possible end-behaviour labels depend on the sign of $a$ and the parity
    of $n$.
    """

    generator_id = "end_behavior_from_leading_term"
    topic_slug = "graphs_of_polynomials"
    display_name = "Describe end behaviour from a polynomial's leading term"

    bank_count_per_difficulty = 15

    # (coefficient, degree) pairs; spans both parities and signs.
    _CASES = (
        (1, 2), (3, 2), (2, 4), (5, 4), (7, 6),
        (1, 3), (2, 3), (4, 5), (6, 5), (3, 7),
        (-1, 2), (-2, 4), (-3, 6), (-2, 3), (-5, 3),
        (-4, 5), (-1, 7), (-6, 2), (-3, 4), (-2, 6),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, n = rng.choice(self._CASES)
        even_degree = (n % 2 == 0)

        # Describe the leading term
        if a == 1:
            lead_latex = f"x^{{{n}}}"
        elif a == -1:
            lead_latex = f"-x^{{{n}}}"
        else:
            lead_latex = f"{a}x^{{{n}}}"

        if even_degree:
            if a > 0:
                answer_latex = (
                    r"As $x \to -\infty$, $f(x) \to +\infty$; "
                    r"as $x \to +\infty$, $f(x) \to +\infty$."
                )
                short = "up / up"
            else:
                answer_latex = (
                    r"As $x \to -\infty$, $f(x) \to -\infty$; "
                    r"as $x \to +\infty$, $f(x) \to -\infty$."
                )
                short = "down / down"
        else:
            if a > 0:
                answer_latex = (
                    r"As $x \to -\infty$, $f(x) \to -\infty$; "
                    r"as $x \to +\infty$, $f(x) \to +\infty$."
                )
                short = "down / up"
            else:
                answer_latex = (
                    r"As $x \to -\infty$, $f(x) \to +\infty$; "
                    r"as $x \to +\infty$, $f(x) \to -\infty$."
                )
                short = "up / down"

        parity_word = "even" if even_degree else "odd"
        sign_word = "positive" if a > 0 else "negative"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A polynomial has leading term ${lead_latex}$. Describe its "
                "end behaviour."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "End behaviour of a polynomial depends only on its leading "
                    "term: the sign of the leading coefficient and the parity of "
                    "the degree."
                ),
                (
                    "Even degree: both ends match; odd degree: ends go opposite "
                    "ways. Positive lead: right end rises; negative lead: right "
                    "end falls."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The leading term ${lead_latex}$ has {sign_word} coefficient "
                    f"and {parity_word} degree."
                ),
                (
                    f"So the graph's end behaviour is {short}."
                ),
                answer_latex,
            ],
            tags=POLY_TAGS + [SKILL_VISUALIZATION],
        )


@register
class MaxTurningPoints(Generator):
    """Given a polynomial of degree $n$, state the maximum number of turning
    points, $n - 1$.

    Backward: pick $n$ (as the given degree), compute $n - 1$.
    """

    generator_id = "max_turning_points"
    topic_slug = "graphs_of_polynomials"
    display_name = "Maximum number of turning points from degree"

    bank_count_per_difficulty = 10

    _DEGREES = (2, 3, 4, 5, 6, 7, 8, 9, 10, 12)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n = rng.choice(self._DEGREES)
        max_turns = n - 1

        # Build a representative polynomial of the chosen degree for flavour.
        coeffs = [1] + [0] * (n - 1) + [-1]  # x^n - 1
        poly_latex = _poly_latex_from_coeffs(coeffs)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the maximum number of turning points of a polynomial "
                f"of degree ${n}$ such as $p(x) = {poly_latex}$."
            ),
            answer_latex=f"${max_turns}$ turning points",
            hints=[
                (
                    "A polynomial of degree $n$ has at most $n - 1$ turning points."
                ),
                (
                    "This follows because the derivative of a degree-$n$ polynomial "
                    "has degree $n - 1$ and therefore at most $n - 1$ real roots."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The degree of $p(x)$ is ${n}$."
                ),
                (
                    f"Apply the turning-point bound: maximum is $n - 1 = {n} - 1 "
                    f"= {max_turns}$."
                ),
                (
                    f"So the graph has at most ${max_turns}$ turning points."
                ),
            ],
            tags=POLY_TAGS + [SKILL_PROCEDURAL],
        )


@register
class FactorAndFindZeros(Generator):
    """Given a factorable polynomial $(x - a)(x - b)(x - c)$ (expanded or not),
    find the real zeros.

    Backward: pick the three integer zeros.
    """

    generator_id = "factor_and_find_zeros"
    topic_slug = "graphs_of_polynomials"
    display_name = "Find the real zeros of a factorable polynomial"

    _ROOT_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}
    _DEGREE_CHOICES = {"easy": (2,), "medium": (2, 3), "hard": (3,)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ROOT_RANGES[difficulty]
        degree = rng.choice(self._DEGREE_CHOICES[difficulty])
        roots: list[int] = []
        while len(roots) < degree:
            r = rng.randint(lo, hi)
            if r not in roots:
                roots.append(r)
        roots.sort()

        x = sp.Symbol("x")
        product = sp.Integer(1)
        for r in roots:
            product *= (x - r)
        expanded = sp.expand(product)
        coeffs = sp.Poly(expanded, x).all_coeffs()
        coeffs_int = [int(c) for c in coeffs]
        poly_latex = _poly_latex_from_coeffs(coeffs_int)

        factored_latex = " ".join(
            f"(x {_signed_const(-r)})" for r in roots
        )

        roots_latex = ", ".join(f"$x = {r}$" for r in roots)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(roots)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find all real zeros of $p(x) = {poly_latex}$."
            ),
            answer_latex=roots_latex,
            hints=[
                (
                    "Try to factor the polynomial over the integers by testing "
                    "small integer roots or recognising common factored forms."
                ),
                (
                    "Once $p(x)$ is factored, set each factor equal to zero and "
                    "solve for $x$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Factor the polynomial: $p(x) = {factored_latex}$."
                ),
                (
                    f"Set each factor equal to zero and solve: "
                    f"{'; '.join(f'$x - ({r}) = 0$' for r in roots)}."
                ),
                (
                    f"The real zeros are {roots_latex}."
                ),
            ],
            tags=POLY_TAGS + [SKILL_ALGEBRAIC],
        )


# ===========================================================================
# Topic 7: real_zeros_of_polynomials
# ===========================================================================


@register
class RationalRootCandidatesList(Generator):
    """List the candidate rational roots $\\pm p/q$ from the constant and leading
    coefficients.

    Backward: pick a small constant ``c`` and leading ``a``, compute the
    Cartesian-product candidate set.
    """

    generator_id = "rational_root_candidates_list"
    topic_slug = "real_zeros_of_polynomials"
    display_name = "List rational root candidates for a polynomial"

    _C_CHOICES = {"easy": (2, 3, 4, 6), "medium": (6, 8, 10, 12), "hard": (12, 15, 18, 20, 24)}
    _A_CHOICES = {"easy": (1,), "medium": (1, 2), "hard": (1, 2, 3)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c = rng.choice(self._C_CHOICES[difficulty])
        a = rng.choice(self._A_CHOICES[difficulty])

        # Build a simple degree-2 polynomial for flavour; actual test uses p/q.
        # Choose a random middle coefficient.
        b = rng.randint(-6, 6)
        coeffs = [a, b, c]
        poly_latex = _poly_latex_from_coeffs(coeffs)

        p_factors = _factor_pairs(c)
        q_factors = _factor_pairs(a)

        # Build candidate set p/q with both signs, reduced.
        candidates: set[sp.Rational] = set()
        for p in p_factors:
            for q in q_factors:
                candidates.add(sp.Rational(p, q))
                candidates.add(sp.Rational(-p, q))
        sorted_candidates = sorted(
            candidates, key=lambda r: (float(r), -int(r.q))
        )

        def _cand_latex(r: sp.Rational) -> str:
            if r.q == 1:
                return f"{r.p}"
            sign = "-" if r.p < 0 else ""
            return rf"{sign}\dfrac{{{abs(r.p)}}}{{{r.q}}}"

        cand_latex_list = ", ".join(_cand_latex(c_) for c_ in sorted_candidates)
        answer_latex = f"${cand_latex_list}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"List every possible rational zero of $p(x) = {poly_latex}$ "
                "according to the Rational Root Theorem."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    r"The Rational Root Theorem says any rational zero must have "
                    r"the form $\pm p/q$, where $p$ divides the constant term and "
                    r"$q$ divides the leading coefficient."
                ),
                (
                    f"List the positive divisors of the constant term (${c}$) and "
                    f"of the leading coefficient (${a}$), then form all signed "
                    "ratios."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The constant term is ${c}$ and the leading coefficient is "
                    f"${a}$."
                ),
                (
                    f"Positive divisors of ${c}$: "
                    f"{', '.join(str(p) for p in p_factors)}. "
                    f"Positive divisors of ${a}$: "
                    f"{', '.join(str(q) for q in q_factors)}."
                ),
                (
                    f"Form all ratios $\\pm p/q$ and reduce duplicates: "
                    f"{answer_latex}."
                ),
            ],
            tags=POLY_TAGS + [SKILL_PROCEDURAL],
        )


@register
class VerifyRationalRoot(Generator):
    """Plug a candidate value into $p(x)$ and decide whether it is a zero.

    Backward: pick roots and a candidate; the candidate is a genuine root
    roughly half the time and a near-miss the rest of the time.
    """

    generator_id = "verify_rational_root"
    topic_slug = "real_zeros_of_polynomials"
    display_name = "Verify whether a candidate value is a root"

    _ROOT_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ROOT_RANGES[difficulty]
        r1 = rng.randint(lo, hi)
        r2 = rng.randint(lo, hi)
        while r2 == r1:
            r2 = rng.randint(lo, hi)

        x = sp.Symbol("x")
        poly = sp.expand((x - r1) * (x - r2))
        coeffs = [int(c) for c in sp.Poly(poly, x).all_coeffs()]
        poly_latex = _poly_latex_from_coeffs(coeffs)

        will_be_root = rng.choice([True, False])
        if will_be_root:
            candidate = rng.choice([r1, r2])
        else:
            # Pick a near-miss candidate: r1 plus or minus a small shift,
            # ensuring it's not a root.
            shift = rng.choice([-2, -1, 1, 2])
            candidate = r1 + shift
            while candidate in (r1, r2):
                shift += 1
                candidate = r1 + shift

        value = poly.subs(x, candidate)
        value_int = int(value)
        is_root = value_int == 0

        answer_latex = (
            f"Yes, $x = {candidate}$ is a root." if is_root
            else f"No, $p({candidate}) = {value_int} \\ne 0$."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (r1, r2, candidate)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine whether $x = {candidate}$ is a root of "
                f"$p(x) = {poly_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "A value $x = r$ is a root of $p(x)$ if and only if $p(r) = 0$."
                ),
                (
                    f"Substitute $x = {candidate}$ into $p(x)$ and simplify."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Substitute $x = {candidate}$ into "
                    f"$p(x) = {poly_latex}$."
                ),
                (
                    f"Evaluate: $p({candidate}) = {value_int}$."
                ),
                (
                    f"Since ${value_int} {'=' if is_root else r'\ne'} 0$, "
                    f"the value {'is' if is_root else 'is not'} a root."
                ),
            ],
            tags=POLY_TAGS + [SKILL_FORMULA_SUB],
        )


@register
class SyntheticDivisionQuotient(Generator):
    """Given $p(x)$ and a known root $r$, use synthetic division to find the quotient.

    Backward: pick roots $r$, $r_2$, $r_3$ (possibly only two), form
    $p(x) = (x - r) \\cdot q(x)$ where $q(x)$ is the expected quotient.
    """

    generator_id = "synthetic_division_quotient"
    topic_slug = "real_zeros_of_polynomials"
    display_name = "Use synthetic division to find the quotient after dividing by (x - r)"

    _ROOT_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ROOT_RANGES[difficulty]
        # divisor root
        r = rng.randint(lo, hi)
        # quotient's roots (1 for degree-2 dividend on easy, 2 for degree-3 otherwise)
        if difficulty == "easy":
            q_roots = [rng.randint(lo, hi)]
            while q_roots[0] == r:
                q_roots[0] = rng.randint(lo, hi)
        else:
            q_roots = [rng.randint(lo, hi), rng.randint(lo, hi)]
            while q_roots[0] == r:
                q_roots[0] = rng.randint(lo, hi)
            while q_roots[1] == r or q_roots[1] == q_roots[0]:
                q_roots[1] = rng.randint(lo, hi)

        x = sp.Symbol("x")
        # Quotient polynomial and dividend polynomial.
        quot = sp.Integer(1)
        for qr in q_roots:
            quot *= (x - qr)
        quot = sp.expand(quot)
        dividend = sp.expand((x - r) * quot)

        dividend_coeffs = [int(c) for c in sp.Poly(dividend, x).all_coeffs()]
        dividend_latex = _poly_latex_from_coeffs(dividend_coeffs)

        quot_coeffs = [int(c) for c in sp.Poly(quot, x).all_coeffs()]
        quot_latex = _poly_latex_from_coeffs(quot_coeffs)

        # Build the synthetic division display as a tabulated list.
        # Synthetic division: carry first coefficient, multiply by r, add, etc.
        carry = [dividend_coeffs[0]]
        for c_ in dividend_coeffs[1:]:
            carry.append(c_ + carry[-1] * r)
        # The last entry should be the remainder (0 since r is a root).
        remainder = carry[-1]

        answer_latex = f"Quotient: ${quot_latex}$; remainder: ${remainder}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (r, tuple(q_roots))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use synthetic division to divide $p(x) = {dividend_latex}$ "
                f"by $(x - ({r}))$, and give the quotient."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    f"Write the coefficients of $p(x)$ in a row and bring down "
                    f"the leading coefficient: {dividend_coeffs[0]}."
                ),
                (
                    f"Multiply each running total by ${r}$ and add to the next "
                    "coefficient; the final entry is the remainder."
                ),
            ],
            solution_steps_latex=[
                (
                    f"List the coefficients of $p(x)$: "
                    f"{', '.join(str(c_) for c_ in dividend_coeffs)}."
                ),
                (
                    f"Carry down the leading coefficient and apply synthetic "
                    f"division with divisor root ${r}$, producing running totals: "
                    f"{', '.join(str(c_) for c_ in carry)}."
                ),
                (
                    f"The first ${len(carry) - 1}$ entries are the coefficients of "
                    f"the quotient, and the last entry is the remainder."
                ),
                (
                    f"Quotient: ${quot_latex}$; remainder: ${remainder}$."
                ),
            ],
            tags=POLY_TAGS + [SKILL_MULTI_STEP],
        )


# ===========================================================================
# Topic 8: real_zeros_of_polynomials_advanced
# ===========================================================================


def _count_sign_changes(coeffs: list[int]) -> int:
    """Count sign changes in a coefficient sequence, ignoring zeros."""
    filtered = [c for c in coeffs if c != 0]
    changes = 0
    for prev, curr in zip(filtered, filtered[1:]):
        if prev * curr < 0:
            changes += 1
    return changes


def _sign_sequence_latex(coeffs: list[int]) -> str:
    """Render the sign pattern for a coefficient list as a plus/minus string."""
    parts: list[str] = []
    for c in coeffs:
        if c > 0:
            parts.append("+")
        elif c < 0:
            parts.append("-")
        else:
            parts.append("0")
    return ", ".join(parts)


@register
class DescartesPositiveSigns(Generator):
    """Count sign changes in $p(x)$ to bound the number of positive real zeros.

    Backward: pick coefficients directly to control the number of sign changes.
    """

    generator_id = "descartes_positive_signs"
    topic_slug = "real_zeros_of_polynomials_advanced"
    display_name = "Use Descartes' rule of signs for positive real zeros"

    _DEGREE_CHOICES = {"easy": (3,), "medium": (3, 4), "hard": (4, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        degree = rng.choice(self._DEGREE_CHOICES[difficulty])
        # Generate coefficients with guaranteed sign rotation.
        coeffs: list[int] = []
        for i in range(degree + 1):
            mag = rng.randint(1, 6)
            sign = 1 if rng.random() < 0.6 else -1
            coeffs.append(sign * mag)
        # Ensure leading coefficient nonzero.
        if coeffs[0] == 0:
            coeffs[0] = 1

        poly_latex = _poly_latex_from_coeffs(coeffs)
        sign_changes = _count_sign_changes(coeffs)

        possibilities: list[int] = []
        k = sign_changes
        while k >= 0:
            possibilities.append(k)
            k -= 2
        possibilities_latex = ", ".join(str(p) for p in possibilities)

        answer_latex = (
            f"Possible number of positive real zeros: {possibilities_latex}"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(coeffs)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use Descartes' Rule of Signs to list the possible numbers of "
                f"positive real zeros of $p(x) = {poly_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Count the number of sign changes in the coefficients of "
                    "$p(x)$, reading left to right and ignoring zero coefficients."
                ),
                (
                    "The number of positive real zeros is that count, or the "
                    "count minus $2$, minus $4$, and so on, down to $0$ or $1$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read the sign pattern of the coefficients of $p(x)$: "
                    f"${_sign_sequence_latex(coeffs)}$."
                ),
                (
                    f"Count sign changes: there are ${sign_changes}$."
                ),
                (
                    f"So the number of positive real zeros is one of "
                    f"${possibilities_latex}$."
                ),
            ],
            tags=POLY_TAGS + [SKILL_PROCEDURAL],
        )


@register
class DescartesNegativeSigns(Generator):
    """Count sign changes in $p(-x)$ for a bound on negative real zeros.

    Backward: pick coefficients directly and flip signs of odd-degree terms
    to construct $p(-x)$ exactly.
    """

    generator_id = "descartes_negative_signs"
    topic_slug = "real_zeros_of_polynomials_advanced"
    display_name = "Use Descartes' rule of signs for negative real zeros"

    _DEGREE_CHOICES = {"easy": (3,), "medium": (3, 4), "hard": (4, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        degree = rng.choice(self._DEGREE_CHOICES[difficulty])
        coeffs: list[int] = []
        for i in range(degree + 1):
            mag = rng.randint(1, 6)
            sign = 1 if rng.random() < 0.6 else -1
            coeffs.append(sign * mag)
        if coeffs[0] == 0:
            coeffs[0] = 1

        poly_latex = _poly_latex_from_coeffs(coeffs)

        # p(-x): flip the sign of every term whose power is odd. Powers run
        # from ``degree`` down to ``0`` so power[i] = degree - i.
        neg_coeffs = [
            c if (degree - i) % 2 == 0 else -c
            for i, c in enumerate(coeffs)
        ]
        neg_poly_latex = _poly_latex_from_coeffs(neg_coeffs)

        sign_changes = _count_sign_changes(neg_coeffs)
        possibilities: list[int] = []
        k = sign_changes
        while k >= 0:
            possibilities.append(k)
            k -= 2
        possibilities_latex = ", ".join(str(p) for p in possibilities)

        answer_latex = (
            f"Possible number of negative real zeros: {possibilities_latex}"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(coeffs)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Use Descartes' Rule of Signs applied to $p(-x)$ to list the "
                f"possible numbers of negative real zeros of "
                f"$p(x) = {poly_latex}$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Substitute $-x$ for $x$ in $p(x)$ and simplify; odd-degree "
                    "terms change sign while even-degree terms stay the same."
                ),
                (
                    "Then count the sign changes in $p(-x)$ and deduce the "
                    "possible counts by subtracting $2$ repeatedly."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Form $p(-x) = {neg_poly_latex}$ by flipping the sign of "
                    "every odd-degree term."
                ),
                (
                    f"Sign pattern of $p(-x)$: "
                    f"${_sign_sequence_latex(neg_coeffs)}$. "
                    f"Sign changes: ${sign_changes}$."
                ),
                (
                    f"Therefore the number of negative real zeros is one of "
                    f"${possibilities_latex}$."
                ),
            ],
            tags=POLY_TAGS + [SKILL_PROCEDURAL],
        )


@register
class CombineRationalAndSignToNarrowSearch(Generator):
    """Combine the Rational Root Theorem with Descartes' Rule of Signs to produce
    a narrowed candidate list.

    Backward: pick a polynomial with integer roots so the rational root list
    is short, and pick sign patterns so Descartes gives a small bound.
    """

    generator_id = "combine_rational_and_sign_to_narrow_search"
    topic_slug = "real_zeros_of_polynomials_advanced"
    display_name = "Combine the Rational Root Theorem with Descartes' Rule"

    bank_count_per_difficulty = 5

    _ROOT_CHOICES = {
        "easy": (
            (1, -1, 2),
            (1, 2, -3),
            (-1, -2, 3),
            (1, -2, 3),
            (-1, 2, 3),
            (1, 2, 3),
            (-1, -2, -3),
        ),
        "medium": (
            (1, -1, 2, -2),
            (1, 2, -3, -4),
            (1, -1, 3, -3),
            (-1, 2, -3, 4),
            (1, -2, 3, -4),
            (2, -2, 3, -3),
            (1, 3, -2, -4),
        ),
        "hard": (
            (1, -2, 3, -4, 5),
            (1, -1, 2, -2, 3),
            (-1, 2, -3, 4, -5),
            (1, 2, -3, 4, -5),
            (-1, -2, 3, -4, 5),
            (1, -1, -2, 3, -4),
            (2, -3, 4, -5, 6),
        ),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        roots = rng.choice(self._ROOT_CHOICES[difficulty])

        x = sp.Symbol("x")
        poly = sp.Integer(1)
        for r in roots:
            poly *= (x - r)
        poly = sp.expand(poly)
        coeffs = [int(c) for c in sp.Poly(poly, x).all_coeffs()]
        poly_latex = _poly_latex_from_coeffs(coeffs)

        constant = coeffs[-1]
        leading = coeffs[0]

        p_factors = _factor_pairs(constant)
        q_factors = _factor_pairs(leading)

        # Build rational root candidates (p/q, both signs, reduced).
        candidates: set[sp.Rational] = set()
        for p in p_factors:
            for q in q_factors:
                candidates.add(sp.Rational(p, q))
                candidates.add(sp.Rational(-p, q))
        sorted_candidates = sorted(
            candidates, key=lambda r: (float(r), -int(r.q))
        )

        # Descartes' counts
        pos_changes = _count_sign_changes(coeffs)
        neg_coeffs = [
            c if (len(coeffs) - 1 - i) % 2 == 0 else -c
            for i, c in enumerate(coeffs)
        ]
        neg_changes = _count_sign_changes(neg_coeffs)

        # Actual positive and negative roots for comparison.
        actual_pos = sum(1 for r in roots if r > 0)
        actual_neg = sum(1 for r in roots if r < 0)

        def _cand_latex(r: sp.Rational) -> str:
            if r.q == 1:
                return f"{r.p}"
            sign = "-" if r.p < 0 else ""
            return rf"{sign}\dfrac{{{abs(r.p)}}}{{{r.q}}}"

        cand_latex_list = ", ".join(_cand_latex(c_) for c_ in sorted_candidates)

        confirmed_pos = [r for r in roots if r > 0]
        confirmed_neg = [r for r in roots if r < 0]
        confirmed_all = sorted(set(roots))
        confirmed_latex = ", ".join(f"$x = {r}$" for r in confirmed_all)

        answer_latex = (
            f"Rational root candidates: ${cand_latex_list}$. "
            f"Descartes: up to ${pos_changes}$ positive, up to ${neg_changes}$ "
            f"negative. Confirmed zeros: {confirmed_latex}."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(roots)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For $p(x) = {poly_latex}$, list the rational root candidates, "
                "apply Descartes' Rule of Signs to bound the positive and "
                "negative real zeros, and then confirm the real zeros."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Start with the Rational Root Theorem: candidates are "
                    r"$\pm p/q$ where $p$ divides the constant term and $q$ "
                    "divides the leading coefficient."
                ),
                (
                    "Then use Descartes' Rule of Signs on $p(x)$ and $p(-x)$ to "
                    "narrow how many candidates can actually be positive or "
                    "negative roots."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Rational root candidates (from $\\pm p/q$): "
                    f"${cand_latex_list}$."
                ),
                (
                    f"Count sign changes in $p(x)$: ${pos_changes}$, so at most "
                    f"${pos_changes}$ positive real zeros."
                ),
                (
                    f"Count sign changes in $p(-x)$: ${neg_changes}$, so at most "
                    f"${neg_changes}$ negative real zeros."
                ),
                (
                    f"Test candidates consistent with those bounds and confirm "
                    f"the zeros: {confirmed_latex}."
                ),
            ],
            tags=POLY_TAGS + [SKILL_MULTI_STEP],
        )
