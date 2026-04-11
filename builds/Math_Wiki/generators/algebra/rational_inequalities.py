"""Rational inequality generators.

Canonical topic slug ``rational_inequalities`` at
``wiki/topics/algebra/Rational_Inequalities.md``.

Three generators:

- ``simple_rational_inequality_linear_over_linear``: solve
  $\\dfrac{x - a}{x - b} \\text{ op } 0$. Two critical points, careful
  handling of the denominator root (always excluded).
- ``rational_inequality_constant_rhs``: solve $\\dfrac{x}{x - b} \\text{ op } k$
  for nonzero constant $k$. Student must combine over a common denominator
  first, then sign-chart.
- ``quadratic_over_linear_rational_inequality``: solve
  $\\dfrac{(x - r_1)(x - r_2)}{x - b} \\text{ op } 0$. Three critical
  points, four intervals, one excluded from the solution.

Backward construction throughout: pick the critical values, then compose
the inequality. No retry loops.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "rational_inequalities"
_TAGS = [
    "#branch-algebra-2",
    "#topic-rational-expressions",
    "#skill-algebraic-manipulation",
]


_REL_LATEX = {
    "gt":  ">",
    "ge":  r"\ge",
    "lt":  "<",
    "le":  r"\le",
}
_REL_STRICT = {"gt": True, "ge": False, "lt": True, "le": False}


def _fmt_factor(root: int) -> str:
    """Render ``(x - root)`` with sign normalization."""
    if root == 0:
        return "x"
    if root > 0:
        return f"(x - {root})"
    return f"(x + {abs(root)})"


def _bare_shift(var: str, root: int) -> str:
    """Render ``x - root`` without outer parentheses."""
    if root == 0:
        return var
    if root > 0:
        return f"{var} - {root}"
    return f"{var} + {abs(root)}"


# ---------------------------------------------------------------------------

@register
class SimpleRationalInequality(Generator):
    """Solve $\\dfrac{x - a}{x - b} \\text{ op } 0$.

    Backward: pick integer ``a`` (numerator zero) and ``b`` (denominator
    zero) with $a \\ne b$. Two critical points, one included conditionally
    and one always excluded.
    """
    generator_id = "simple_rational_inequality_linear_over_linear"
    topic_slug = TOPIC_SLUG
    display_name = "Solve a linear-over-linear rational inequality"

    _A_RANGES = {
        "easy":   (-6, 6),
        "medium": (-10, 10),
        "hard":   (-15, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._A_RANGES[difficulty]

        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        if a == b:
            b = a + 1 if a + 1 <= hi else a - 1

        rel_key = rng.choice(("gt", "ge", "lt", "le"))
        rel_latex = _REL_LATEX[rel_key]
        strict = _REL_STRICT[rel_key]

        # Order critical points on the number line.
        lo_cp, hi_cp = (a, b) if a < b else (b, a)
        # Determine sign of (x - a)/(x - b) on each of the three intervals.
        # Strategy: test at lo_cp - 10, midpoint (lo_cp + hi_cp)/2, hi_cp + 10.
        def _sign(x_test: int) -> int:
            num = x_test - a
            den = x_test - b
            if num == 0 or den == 0:
                # Shouldn't happen with the chosen test points, but guard anyway.
                return 0
            return 1 if num * den > 0 else -1

        tests = (lo_cp - 10, (lo_cp + hi_cp) // 2 if lo_cp + 1 < hi_cp else lo_cp, hi_cp + 10)
        # Ensure tests hit each interval exactly:
        t_left = lo_cp - 10
        # Middle: if lo_cp + 1 < hi_cp, pick something in between; otherwise
        # push test to lo_cp + 0.5 by using a float — but we need integers.
        # Guarantee gap by construction: if lo_cp + 1 == hi_cp (they are
        # adjacent integers), we still can't pick an integer strictly between
        # them, so shift b by +1 to create a gap.
        if lo_cp + 1 >= hi_cp:
            # Force at least one integer between the critical points.
            # Since lo_cp = min(a,b), hi_cp = max(a,b), a==b is impossible,
            # so |a - b| >= 1. If |a - b| == 1, regenerate by widening b.
            # Instead of looping, just push b further away.
            if a < b:
                b = a + 2
            else:
                b = a - 2
            lo_cp, hi_cp = (a, b) if a < b else (b, a)

        t_mid = (lo_cp + hi_cp) // 2
        if t_mid == lo_cp:
            t_mid = lo_cp + 1
        t_right = hi_cp + 10

        sign_left = _sign(t_left)
        sign_mid = _sign(t_mid)
        sign_right = _sign(t_right)

        want = 1 if rel_key in ("gt", "ge") else -1

        # Build the interval union. The numerator critical value ``a`` is
        # included iff not strict. The denominator critical value ``b`` is
        # NEVER included (division by zero).
        intervals: list[tuple[str, str]] = []
        # Left interval: (-inf, lo_cp). Left bracket always "(" (infinity).
        if sign_left == want:
            left_cp_included = (not strict) and (lo_cp == a)
            right = f"{lo_cp}]" if left_cp_included else f"{lo_cp})"
            intervals.append(("(-\\infty", right))
        # Middle interval: (lo_cp, hi_cp)
        if sign_mid == want:
            left_inc = (not strict) and (lo_cp == a)
            right_inc = (not strict) and (hi_cp == a)
            left = f"[{lo_cp}" if left_inc else f"({lo_cp}"
            right = f"{hi_cp}]" if right_inc else f"{hi_cp})"
            intervals.append((left, right))
        # Right interval: (hi_cp, inf)
        if sign_right == want:
            right_cp_included = (not strict) and (hi_cp == a)
            left = f"[{hi_cp}" if right_cp_included else f"({hi_cp}"
            intervals.append((left, "\\infty)"))

        if intervals:
            pieces = [f"{l}, {r}" for (l, r) in intervals]
            answer_interval = " \\cup ".join(pieces)
        else:
            answer_interval = r"\varnothing"

        num_latex = _bare_shift("x", a)
        den_latex = _bare_shift("x", b)
        statement = (
            f"Give the solution set of $\\dfrac{{{num_latex}}}{{{den_latex}}} "
            f"{rel_latex} 0$. Express your answer in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, rel_key),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_interval}$",
            hints=[
                (
                    f"The numerator is zero when $x = {a}$, and the denominator "
                    f"is zero when $x = {b}$. Both are critical values for the "
                    f"sign chart."
                ),
                (
                    f"The denominator zero $x = {b}$ is **always excluded** "
                    f"from the solution (division by zero)."
                ),
                (
                    "Build a sign chart across three intervals, test a point in "
                    "each, and keep the intervals where the rational expression "
                    "has the required sign."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Critical values: $x = {a}$ (numerator zero) and "
                    f"$x = {b}$ (denominator zero, always excluded)."
                ),
                (
                    "Test a point in each of the three intervals formed by "
                    "these critical values and record the sign of the rational "
                    "expression."
                ),
                (
                    f"Collect the intervals where the expression is "
                    + ("positive" if want == 1 else "negative")
                    + ". "
                    + ("Include $x = " + str(a) + "$ (expression equals zero). "
                       if not strict else "Exclude $x = " + str(a) + "$ (strict). ")
                    + f"Always exclude $x = {b}$."
                ),
                f"Answer: ${answer_interval}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class RationalInequalityWithConstantOnRight(Generator):
    """Solve $\\dfrac{x - a}{x - b} \\text{ op } k$ for nonzero constant $k$.

    Backward: pick integers ``a``, ``b`` (with $a \\ne b$) and a nonzero
    integer ``k``, then subtract $k$ from both sides and combine:
        (x - a)/(x - b) - k = ((x - a) - k(x - b)) / (x - b)
                            = ((1 - k)x + (kb - a)) / (x - b).

    For guaranteed clean critical points we specialise: pick ``k = 1`` or
    ``k = -1``. Then the combined numerator simplifies drastically (the
    $x$ term vanishes for $k = 1$, and doubles for $k = -1$). This keeps
    the problem tractable for every difficulty.
    """
    generator_id = "rational_inequality_constant_rhs"
    topic_slug = TOPIC_SLUG
    display_name = "Solve a rational inequality with a constant on the right"

    _A_RANGES = {
        "easy":   (-5, 5),
        "medium": (-10, 10),
        "hard":   (-15, 15),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._A_RANGES[difficulty]

        # Pick k in {-1, 1}. For k = 1, f(x) - 1 = (b - a)/(x - b).
        # For k = -1, f(x) + 1 = ((2x - a - b))/(x - b) and the new
        # numerator has a clean integer root (a + b)/2 only when a + b
        # is even — so we restrict k = -1 to even-parity (a + b).
        k = rng.choice((1, -1))

        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        if a == b:
            b = a + 1 if a + 1 <= hi else a - 1

        if k == -1 and (a + b) % 2 != 0:
            # Shift b by one to even the parity. We already guaranteed a != b,
            # and shifting by 1 preserves that unless it equals a, in which
            # case shift by 2.
            new_b = b + 1 if b + 1 <= hi else b - 1
            if new_b == a:
                new_b = b - 1 if b - 1 >= lo else b + 1
            if new_b == a:
                # Extreme fallback: both directions collide. Flip k to +1.
                k = 1
            else:
                b = new_b

        rel_key = rng.choice(("gt", "ge", "lt", "le"))
        rel_latex = _REL_LATEX[rel_key]
        strict = _REL_STRICT[rel_key]

        # Left-hand-side LaTeX of the original problem.
        num_latex = _bare_shift("x", a)
        den_latex = _bare_shift("x", b)

        if k == 1:
            # After combining: (b - a) / (x - b) [op] 0
            const_num = b - a  # This is a nonzero integer since a != b.
            # The only critical value is x = b; numerator has no x-term.
            # Sign of expression:
            #   if const_num > 0: sign = sign of 1/(x-b) = +1 when x > b, -1 when x < b
            #   if const_num < 0: sign = -1 when x > b, +1 when x < b
            # The expression is never zero.
            intervals: list[tuple[str, str]] = []
            want = 1 if rel_key in ("gt", "ge") else -1

            # Evaluate sign on (-inf, b) and (b, inf).
            # Sample: x = b - 10 (left), x = b + 10 (right).
            left_sign = 1 if const_num * (-1) > 0 else -1  # denom at b-10 is negative
            right_sign = 1 if const_num * (1) > 0 else -1  # denom at b+10 is positive
            if left_sign == want:
                intervals.append(("(-\\infty", f"{b})"))
            if right_sign == want:
                intervals.append((f"({b}", "\\infty)"))
            answer_interval = (
                " \\cup ".join(f"{l}, {r}" for l, r in intervals)
                if intervals
                else r"\varnothing"
            )

            combined_latex = (
                f"\\dfrac{{{const_num}}}{{{den_latex}}} {rel_latex} 0"
            )
            combined_step = (
                f"$\\dfrac{{{num_latex}}}{{{den_latex}}} - 1 "
                f"= \\dfrac{{({num_latex}) - ({den_latex})}}{{{den_latex}}} "
                f"= \\dfrac{{{const_num}}}{{{den_latex}}}$"
            )
            critical_values_note = (
                f"The combined expression has no numerator zero and is undefined "
                f"at $x = {b}$."
            )
        else:
            # k = -1. Combining: (x - a)/(x - b) + 1 = (2x - a - b)/(x - b).
            # Numerator zero at x = (a + b)/2, which is an integer by construction.
            num_zero = (a + b) // 2
            # The critical values are x = num_zero (possibly included) and
            # x = b (always excluded).
            lo_cp, hi_cp = (num_zero, b) if num_zero < b else (b, num_zero)
            # Ensure a gap for sign testing.
            if lo_cp + 1 >= hi_cp:
                # Rare: need an integer gap. Shift b +/- 2 carefully without
                # making parity collide.
                if b < num_zero:
                    b -= 2
                else:
                    b += 2
                num_zero = (a + b) // 2
                lo_cp, hi_cp = (num_zero, b) if num_zero < b else (b, num_zero)

            # Sign analysis for (2x - a - b)/(x - b).
            def _sign(x_test: int) -> int:
                num = 2 * x_test - a - b
                den = x_test - b
                if num == 0 or den == 0:
                    return 0
                return 1 if num * den > 0 else -1

            t_left = lo_cp - 10
            t_mid = (lo_cp + hi_cp) // 2
            if t_mid == lo_cp:
                t_mid = lo_cp + 1
            t_right = hi_cp + 10
            sign_left = _sign(t_left)
            sign_mid = _sign(t_mid)
            sign_right = _sign(t_right)
            want = 1 if rel_key in ("gt", "ge") else -1

            intervals = []
            # Left interval: (-inf, lo_cp)
            if sign_left == want:
                left_inc = (not strict) and (lo_cp == num_zero)
                right = f"{lo_cp}]" if left_inc else f"{lo_cp})"
                intervals.append(("(-\\infty", right))
            if sign_mid == want:
                l_inc = (not strict) and (lo_cp == num_zero)
                r_inc = (not strict) and (hi_cp == num_zero)
                left = f"[{lo_cp}" if l_inc else f"({lo_cp}"
                right = f"{hi_cp}]" if r_inc else f"{hi_cp})"
                intervals.append((left, right))
            if sign_right == want:
                right_inc = (not strict) and (hi_cp == num_zero)
                left = f"[{hi_cp}" if right_inc else f"({hi_cp}"
                intervals.append((left, "\\infty)"))
            answer_interval = (
                " \\cup ".join(f"{l}, {r}" for l, r in intervals)
                if intervals
                else r"\varnothing"
            )

            # Build the combined-numerator LaTeX with sign handling for (a+b).
            neg_ab = -(a + b)
            if neg_ab == 0:
                combined_num_latex = "2x"
            elif neg_ab > 0:
                combined_num_latex = f"2x + {neg_ab}"
            else:
                combined_num_latex = f"2x - {abs(neg_ab)}"
            combined_latex = (
                f"\\dfrac{{{combined_num_latex}}}{{{den_latex}}} {rel_latex} 0"
            )
            combined_step = (
                f"$\\dfrac{{{num_latex}}}{{{den_latex}}} + 1 "
                f"= \\dfrac{{({num_latex}) + ({den_latex})}}{{{den_latex}}} "
                f"= \\dfrac{{{combined_num_latex}}}{{{den_latex}}}$"
            )
            critical_values_note = (
                f"The combined numerator is zero at $x = {num_zero}$, and the "
                f"expression is undefined at $x = {b}$."
            )

        statement = (
            f"Give the solution set of $\\dfrac{{{num_latex}}}{{{den_latex}}} "
            f"{rel_latex} {k}$. Express your answer in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, k, rel_key),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_interval}$",
            hints=[
                (
                    f"Subtract ${k}$ from both sides so the right-hand side is "
                    f"$0$: the inequality becomes a rational expression on the "
                    f"left compared to $0$."
                ),
                (
                    f"Combine over the common denominator ${den_latex}$: "
                    + combined_step
                    + "."
                ),
                (
                    critical_values_note
                    + " Build a sign chart from these critical values."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Start with $\\dfrac{{{num_latex}}}{{{den_latex}}} "
                    f"{rel_latex} {k}$."
                ),
                (
                    f"Move ${k}$ to the left-hand side and combine over a common "
                    f"denominator: ${combined_latex}$."
                ),
                critical_values_note,
                (
                    f"Sign-chart the combined expression. The solution is the "
                    f"union of intervals where the sign matches ${rel_latex} 0$, "
                    f"excluding any denominator zero."
                ),
                f"Answer: ${answer_interval}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class QuadraticOverLinearRationalInequality(Generator):
    """Solve $\\dfrac{(x - r_1)(x - r_2)}{x - b} \\text{ op } 0$.

    Backward: pick three distinct integer critical values. The three
    points split the number line into four intervals; the sign of the
    expression alternates across them starting from a known sign on
    the rightmost ray.
    """
    generator_id = "quadratic_over_linear_rational_inequality"
    topic_slug = TOPIC_SLUG
    display_name = "Solve a quadratic-over-linear rational inequality"

    _R_RANGES = {
        "easy":   (-5, 5),
        "medium": (-9, 9),
        "hard":   (-13, 13),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._R_RANGES[difficulty]

        # Pick three distinct integers: two numerator roots and one denominator root.
        picks: set[int] = set()
        attempts = 0
        while len(picks) < 3 and attempts < 50:
            picks.add(rng.randint(lo, hi))
            attempts += 1
        if len(picks) < 3:
            picks = {lo, (lo + hi) // 2, hi}
        picks_list = sorted(picks)
        # Ensure at least a gap of 1 between each consecutive pair (already
        # guaranteed by integer spacing).
        # Assign two of the three to the numerator and one to the denominator.
        # We shuffle the assignment so which of the three is the denominator
        # varies across problems.
        denom_pos = rng.randint(0, 2)
        denom_root = picks_list[denom_pos]
        num_roots = [picks_list[i] for i in range(3) if i != denom_pos]
        r1, r2 = num_roots  # r1 < r2 by the sort above.
        b = denom_root

        rel_key = rng.choice(("gt", "ge", "lt", "le"))
        rel_latex = _REL_LATEX[rel_key]
        strict = _REL_STRICT[rel_key]

        # Sign analysis: the expression has numerator (x - r1)(x - r2) and
        # denominator (x - b). For x larger than all three, each factor is
        # positive, so the expression is positive. As we cross each critical
        # point, the sign flips. The signs on the four intervals
        # (-inf, p1), (p1, p2), (p2, p3), (p3, inf)
        # are therefore: -, +, -, + (in this order) when p1 < p2 < p3.
        signs = ["neg", "pos", "neg", "pos"]
        ordered = picks_list  # already sorted ascending

        want = "pos" if rel_key in ("gt", "ge") else "neg"
        # Numerator roots are included iff non-strict. Denominator root always excluded.
        include_num_roots = not strict

        # Build intervals.
        intervals: list[tuple[str, str]] = []
        # We'll iterate through the four intervals, checking sign and
        # endpoint inclusion.
        # Interval 0: (-inf, ordered[0])
        if signs[0] == want:
            right_cp = ordered[0]
            right_inc = include_num_roots and (right_cp != b)
            right = f"{right_cp}]" if right_inc else f"{right_cp})"
            intervals.append(("(-\\infty", right))
        # Interval 1: (ordered[0], ordered[1])
        if signs[1] == want:
            l_cp = ordered[0]
            r_cp = ordered[1]
            l_inc = include_num_roots and (l_cp != b)
            r_inc = include_num_roots and (r_cp != b)
            left = f"[{l_cp}" if l_inc else f"({l_cp}"
            right = f"{r_cp}]" if r_inc else f"{r_cp})"
            intervals.append((left, right))
        # Interval 2: (ordered[1], ordered[2])
        if signs[2] == want:
            l_cp = ordered[1]
            r_cp = ordered[2]
            l_inc = include_num_roots and (l_cp != b)
            r_inc = include_num_roots and (r_cp != b)
            left = f"[{l_cp}" if l_inc else f"({l_cp}"
            right = f"{r_cp}]" if r_inc else f"{r_cp})"
            intervals.append((left, right))
        # Interval 3: (ordered[2], inf)
        if signs[3] == want:
            l_cp = ordered[2]
            l_inc = include_num_roots and (l_cp != b)
            left = f"[{l_cp}" if l_inc else f"({l_cp}"
            intervals.append((left, "\\infty)"))

        answer_interval = (
            " \\cup ".join(f"{l}, {r}" for (l, r) in intervals)
            if intervals
            else r"\varnothing"
        )

        num_latex = f"{_fmt_factor(r1)}{_fmt_factor(r2)}"
        den_latex = _bare_shift("x", b)
        statement = (
            f"Give the solution set of $\\dfrac{{{num_latex}}}{{{den_latex}}} "
            f"{rel_latex} 0$. Express your answer in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (r1, r2, b, rel_key),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_interval}$",
            hints=[
                (
                    f"The numerator zeros are $x = {r1}$ and $x = {r2}$. "
                    f"The denominator zero is $x = {b}$."
                ),
                (
                    f"The denominator zero $x = {b}$ is always excluded. "
                    f"Numerator zeros are included only when the inequality "
                    f"is non-strict."
                ),
                (
                    "Build a sign chart over the four intervals formed by the "
                    "three critical values. Remember that crossing any simple "
                    "root flips the sign of the expression."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the critical values: "
                    f"$x = {r1}, {r2}$ (numerator) and $x = {b}$ (denominator)."
                ),
                (
                    f"On $(-\\infty, {ordered[0]})$, $({ordered[0]}, {ordered[1]})$, "
                    f"$({ordered[1]}, {ordered[2]})$, and $({ordered[2]}, \\infty)$, "
                    "test one point in each and record the sign."
                ),
                (
                    f"Collect the intervals whose sign matches "
                    f"${rel_latex} 0$, excluding $x = {b}$."
                ),
                f"Answer: ${answer_interval}$.",
            ],
            tags=list(_TAGS),
        )
