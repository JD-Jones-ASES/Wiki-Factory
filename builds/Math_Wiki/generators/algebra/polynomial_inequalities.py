"""Polynomial inequality generators.

Canonical topic slug ``polynomial_inequalities`` at
``wiki/topics/algebra/Polynomial_Inequalities.md``.

Three generators cover the standard progression:

- ``quadratic_inequality_standard_form``: solve $ax^2 + bx + c \\text{ op } 0$
  with two distinct integer roots. Backward: pick roots first, expand.
- ``cubic_inequality_factored_form``: solve an already-factored cubic
  $(x - r_1)(x - r_2)(x - r_3) \\text{ op } 0$. Sign chart with three
  critical points.
- ``quadratic_inequality_nonzero_rhs``: solve $ax^2 + bx + c \\text{ op } k$
  for nonzero $k$. Student must move everything to one side first, then
  factor and sign-chart.

Every answer is expressed in interval notation and derived via pure backward
construction — no retry loops.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "polynomial_inequalities"
_TAGS = [
    "#branch-algebra-2",
    "#topic-inequalities",
    "#skill-algebraic-manipulation",
]


# Relations plus their LaTeX and "between/outside" role in the quadratic case.
# For a quadratic (x - r1)(x - r2) with r1 < r2 and positive leading coefficient:
#   > 0  -> (-inf, r1) U (r2, inf)          (strict outside)
#   >= 0 -> (-inf, r1] U [r2, inf)          (non-strict outside)
#   < 0  -> (r1, r2)                        (strict between)
#   <= 0 -> [r1, r2]                        (non-strict between)
_REL_LATEX = {
    "gt":  ">",
    "ge":  r"\ge",
    "lt":  "<",
    "le":  r"\le",
}
_REL_STRICT = {"gt": True, "ge": False, "lt": True, "le": False}


def _fmt_quadratic_expr(r1: int, r2: int) -> str:
    """Expand (x - r1)(x - r2) as ``x^2 + bx + c`` LaTeX with sign handling.

    ``r1`` and ``r2`` are integers (allowed negatives). Coefficient of $x^2$
    is always 1 so the inequality direction is preserved without a flip.
    """
    b = -(r1 + r2)
    c = r1 * r2
    if b == 0:
        b_part = ""
    elif b == 1:
        b_part = " + x"
    elif b == -1:
        b_part = " - x"
    elif b > 0:
        b_part = f" + {b}x"
    else:
        b_part = f" - {abs(b)}x"

    if c == 0:
        c_part = ""
    elif c > 0:
        c_part = f" + {c}"
    else:
        c_part = f" - {abs(c)}"

    return f"x^2{b_part}{c_part}"


def _fmt_factor(root: int) -> str:
    """Render ``(x - root)`` with sign normalization: (x + 2) instead of (x - -2)."""
    if root == 0:
        return "x"
    if root > 0:
        return f"(x - {root})"
    return f"(x + {abs(root)})"


def _fmt_endpoint_minus(a: int) -> str:
    """Render an interval endpoint as LaTeX (handles negatives cleanly)."""
    return str(a)


def _interval_outside_quadratic(r1: int, r2: int, strict: bool) -> str:
    """Format the solution set for a quadratic > 0 / >= 0.

    Returns e.g. "(-\\infty, 2) \\cup (3, \\infty)" (strict) or
    "(-\\infty, 2] \\cup [3, \\infty)" (non-strict). Requires r1 < r2.
    """
    lo, hi = (r1, r2) if r1 < r2 else (r2, r1)
    left_br = ")" if strict else "]"
    right_br = "(" if strict else "["
    return (
        f"(-\\infty, {_fmt_endpoint_minus(lo)}{left_br} "
        f"\\cup {right_br}{_fmt_endpoint_minus(hi)}, \\infty)"
    )


def _interval_between_quadratic(r1: int, r2: int, strict: bool) -> str:
    """Format the solution set for a quadratic < 0 / <= 0."""
    lo, hi = (r1, r2) if r1 < r2 else (r2, r1)
    left = "(" if strict else "["
    right = ")" if strict else "]"
    return f"{left}{_fmt_endpoint_minus(lo)}, {_fmt_endpoint_minus(hi)}{right}"


# ---------------------------------------------------------------------------

@register
class QuadraticInequalityStandardForm(Generator):
    """Solve $x^2 + bx + c \\text{ op } 0$ with two distinct integer roots.

    Backward construction: pick integer roots ``r1 < r2`` and a relation.
    Expand, then render the student-facing inequality and the interval answer.
    """
    generator_id = "quadratic_inequality_standard_form"
    topic_slug = TOPIC_SLUG
    display_name = "Solve a quadratic inequality in standard form"

    _R_RANGES = {
        "easy":   (-6, 6),
        "medium": (-10, 10),
        "hard":   (-15, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]
        # Backward: pick two distinct roots in [lo, hi].
        r1 = rng.randint(lo, hi)
        offset = rng.randint(1, max(1, hi - lo - 1))
        r2 = r1 + offset
        if r2 > hi:
            # Mirror the offset below r1 instead of above.
            r2 = r1 - offset
        # Ensure r1 < r2.
        if r1 > r2:
            r1, r2 = r2, r1

        rel_key = rng.choice(("gt", "ge", "lt", "le"))
        rel_latex = _REL_LATEX[rel_key]
        strict = _REL_STRICT[rel_key]

        expr_latex = _fmt_quadratic_expr(r1, r2)
        factored_latex = f"{_fmt_factor(r1)}{_fmt_factor(r2)}"

        if rel_key in ("gt", "ge"):
            interval = _interval_outside_quadratic(r1, r2, strict)
            shape_hint = (
                "the parabola is positive outside its roots, so the solution "
                "is two rays away from the roots."
            )
            conclusion = (
                "The expression is positive outside the roots. "
                "Apply strict or non-strict brackets based on the given symbol."
            )
        else:
            interval = _interval_between_quadratic(r1, r2, strict)
            shape_hint = (
                "the parabola is negative between its roots, so the solution "
                "is a single interval between them."
            )
            conclusion = (
                "The expression is negative between the roots. "
                "Apply strict or non-strict brackets based on the given symbol."
            )

        statement = (
            f"Find all real $x$ satisfying ${expr_latex} {rel_latex} 0$. "
            f"Express your answer in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (r1, r2, rel_key),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${interval}$",
            hints=[
                (
                    "First factor the left-hand side as a product of two linear "
                    r"factors: ${factored_latex} {rel_latex} 0$.".format(
                        factored_latex=factored_latex, rel_latex=rel_latex
                    )
                ),
                (
                    f"The critical values are $x = {r1}$ and $x = {r2}$. "
                    f"Set up a sign chart with these two points."
                ),
                (
                    f"Because the leading coefficient is positive, {shape_hint}"
                ),
            ],
            solution_steps_latex=[
                f"Factor: ${factored_latex} {rel_latex} 0$.",
                f"Critical values: $x = {r1}$ and $x = {r2}$.",
                (
                    "Sign chart: sign of each factor in each interval "
                    f"$(-\\infty, {r1})$, $({r1}, {r2})$, $({r2}, \\infty)$. "
                    "The product is positive on the outer intervals and "
                    "negative on the middle interval."
                ),
                conclusion,
                f"Answer: ${interval}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class CubicInequalityFromFactoredForm(Generator):
    """Solve an already-factored cubic inequality $(x-a)(x-b)(x-c) \\text{ op } 0$.

    Backward: pick three distinct integer roots. Build the sign chart by
    checking the sign in each of the four intervals (alternating starting
    from a definite reference point). Express the result in interval notation.
    """
    generator_id = "cubic_inequality_factored_form"
    topic_slug = TOPIC_SLUG
    display_name = "Solve a factored cubic inequality"

    _R_RANGES = {
        "easy":   (-5, 5),
        "medium": (-9, 9),
        "hard":   (-14, 14),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]
        # Pick 3 distinct roots in [lo, hi] by choosing 3 distinct offsets.
        roots_set: set[int] = set()
        attempts = 0
        while len(roots_set) < 3 and attempts < 50:
            roots_set.add(rng.randint(lo, hi))
            attempts += 1
        if len(roots_set) < 3:
            # Deterministic fallback: spread three values in the range.
            roots_set = {lo, (lo + hi) // 2, hi}
        roots = sorted(roots_set)
        r1, r2, r3 = roots

        rel_key = rng.choice(("gt", "ge", "lt", "le"))
        rel_latex = _REL_LATEX[rel_key]
        strict = _REL_STRICT[rel_key]

        # Sign of the product on each interval. With leading coefficient
        # +1 and three simple roots r1 < r2 < r3, the sign pattern is:
        #   (-inf, r1): negative
        #   (r1, r2):   positive
        #   (r2, r3):   negative
        #   (r3, inf):  positive
        # Collect the union based on relation.
        interval_signs = (
            ((float("-inf"), r1), "neg"),
            ((r1,           r2), "pos"),
            ((r2,           r3), "neg"),
            ((r3, float("inf")), "pos"),
        )
        want = "pos" if rel_key in ("gt", "ge") else "neg"
        include_endpoints = not strict

        # Build a list of interval LaTeX fragments and union them.
        pieces: list[str] = []
        for (a, b), sign in interval_signs:
            if sign != want:
                continue
            # Left bracket
            if a == float("-inf"):
                l = "(-\\infty"
            else:
                l = f"[{a}" if include_endpoints else f"({a}"
            # Right bracket
            if b == float("inf"):
                r = "\\infty)"
            else:
                r = f"{b}]" if include_endpoints else f"{b})"
            pieces.append(f"{l}, {r}")

        # If non-strict, adjacent pieces at the same interior root should
        # NOT be merged — at an interior root both sides are included but
        # the expression equals zero there in only one spot, and we keep
        # union pieces separate because they might straddle roots of the
        # opposite sign. That's fine: [-2, 1] U [3, inf) is a valid form.
        answer_interval = " \\cup ".join(pieces) if pieces else r"\varnothing"

        expr_latex = f"{_fmt_factor(r1)}{_fmt_factor(r2)}{_fmt_factor(r3)}"
        statement = (
            f"Give the solution set of ${expr_latex} {rel_latex} 0$. "
            f"Express your answer in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (r1, r2, r3, rel_key),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_interval}$",
            hints=[
                (
                    f"The expression is already factored. The critical values "
                    f"are $x = {r1}$, $x = {r2}$, and $x = {r3}$."
                ),
                (
                    "Draw a sign chart with these three points, splitting the "
                    "real line into four intervals."
                ),
                (
                    "In each interval, pick a test value and evaluate the sign "
                    "of each factor. Multiply the signs together to get the "
                    "sign of the whole expression."
                ),
            ],
            solution_steps_latex=[
                f"Identify the critical values: $x = {r1}, {r2}, {r3}$.",
                (
                    "Sign chart over four intervals "
                    f"$(-\\infty, {r1})$, $({r1}, {r2})$, $({r2}, {r3})$, "
                    f"$({r3}, \\infty)$: the signs alternate as negative, "
                    "positive, negative, positive from left to right."
                ),
                (
                    f"Select the intervals where the sign matches the relation "
                    f"${rel_latex} 0$. "
                    + ("Include the roots where the expression equals zero."
                       if include_endpoints
                       else "Exclude the roots (strict inequality).")
                ),
                f"Answer: ${answer_interval}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class QuadraticInequalityVertexEndpoint(Generator):
    """Solve $x^2 + bx + c \\text{ op } k$ for nonzero constant $k$.

    Backward: pick the desired quadratic roots ``r1 < r2`` of
    $x^2 + bx + (c - k) = 0$, then derive $c = r_1 r_2 + k$ and
    $b = -(r_1 + r_2)$. The student must first move $k$ to the
    left-hand side, then factor and sign-chart.
    """
    generator_id = "quadratic_inequality_nonzero_rhs"
    topic_slug = TOPIC_SLUG
    display_name = "Solve quadratic inequality with nonzero RHS"

    _R_RANGES = {
        "easy":   (-5, 5),
        "medium": (-9, 9),
        "hard":   (-14, 14),
    }
    _K_RANGES = {
        "easy":   (-6, 6),
        "medium": (-12, 12),
        "hard":   (-20, 20),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]
        k_lo, k_hi = self._K_RANGES[difficulty]

        r1 = rng.randint(lo, hi)
        offset = rng.randint(1, max(1, hi - lo - 1))
        r2 = r1 + offset
        if r2 > hi:
            r2 = r1 - offset
        if r1 > r2:
            r1, r2 = r2, r1

        # Pick a nonzero k.
        k = rng.randint(k_lo, k_hi)
        if k == 0:
            k = 1

        rel_key = rng.choice(("gt", "ge", "lt", "le"))
        rel_latex = _REL_LATEX[rel_key]
        strict = _REL_STRICT[rel_key]

        # x^2 + bx + (c) op k where
        #   quadratic x^2 + bx + (c - k) factors as (x - r1)(x - r2).
        b_coeff = -(r1 + r2)
        c_shifted = r1 * r2  # this is (c - k)
        c_coeff = c_shifted + k

        # Build LaTeX for the original (non-shifted) expression.
        lhs_latex = _build_monic_quadratic_latex(b_coeff, c_coeff)
        # And for the shifted zero-on-right form.
        shifted_latex = _fmt_quadratic_expr(r1, r2)

        if rel_key in ("gt", "ge"):
            interval = _interval_outside_quadratic(r1, r2, strict)
            shape_note = (
                "outside the roots (the parabola is above the $x$-axis there)."
            )
        else:
            interval = _interval_between_quadratic(r1, r2, strict)
            shape_note = (
                "between the roots (the parabola dips below the $x$-axis there)."
            )

        statement = (
            f"Find all real $x$ such that ${lhs_latex} {rel_latex} {k}$. "
            f"Express your answer in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (r1, r2, k, rel_key),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${interval}$",
            hints=[
                (
                    f"Subtract ${k}$ from both sides so the right-hand side "
                    f"becomes $0$: ${shifted_latex} {rel_latex} 0$."
                ),
                (
                    f"Factor the new left side into "
                    f"${_fmt_factor(r1)}{_fmt_factor(r2)}$."
                ),
                (
                    f"Build a sign chart with critical values $x = {r1}$ and "
                    f"$x = {r2}$. The solution lies " + shape_note
                ),
            ],
            solution_steps_latex=[
                f"Start with ${lhs_latex} {rel_latex} {k}$.",
                (
                    f"Move ${k}$ to the left: ${shifted_latex} {rel_latex} 0$."
                ),
                (
                    f"Factor: ${_fmt_factor(r1)}{_fmt_factor(r2)} {rel_latex} 0$."
                ),
                (
                    f"Critical values $x = {r1}$ and $x = {r2}$ split the number "
                    f"line into three intervals. Sign-chart the product."
                ),
                f"Answer: ${interval}$.",
            ],
            tags=list(_TAGS),
        )


def _build_monic_quadratic_latex(b: int, c: int) -> str:
    """Render ``x^2 + bx + c`` with natural sign handling."""
    if b == 0:
        b_part = ""
    elif b == 1:
        b_part = " + x"
    elif b == -1:
        b_part = " - x"
    elif b > 0:
        b_part = f" + {b}x"
    else:
        b_part = f" - {abs(b)}x"

    if c == 0:
        c_part = ""
    elif c > 0:
        c_part = f" + {c}"
    else:
        c_part = f" - {abs(c)}"

    return f"x^2{b_part}{c_part}"
