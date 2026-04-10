"""Fraction addition/subtraction and comparison generators.

Canonical topic slugs:
- ``adding_and_subtracting_fractions`` at wiki/topics/pre_algebra/
  Adding_And_Subtracting_Fractions.md
- ``comparing_and_ordering_fractions`` at wiki/topics/pre_algebra/
  Comparing_And_Ordering_Fractions.md

Generators:

adding_and_subtracting_fractions
    add_fractions_same_denom       a/d + b/d with shared denominator
    add_fractions_unlike_denom     a/d1 + b/d2 with a shared LCM target
    subtract_fractions_unlike_denom a/d1 - b/d2, guaranteed positive

comparing_and_ordering_fractions
    compare_two_fractions          a/b  vs  c/d  via cross multiplication
    order_three_fractions          sort three distinct fractions ascending
    compare_fraction_to_half       compare n/d to 1/2 using the half rule
"""
from __future__ import annotations

import random
from fractions import Fraction
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Helpers

def _lcm(a: int, b: int) -> int:
    """Least common multiple of two positive integers."""
    return a * b // gcd(a, b)


def _fmt_frac(num: int, den: int) -> str:
    """LaTeX fraction, collapsing to an integer when denominator is 1."""
    if den == 1:
        return f"{num}"
    return f"\\frac{{{num}}}{{{den}}}"


def _fmt_tfrac(num: int, den: int) -> str:
    """Compact tfrac form for dense lines like ordering answers."""
    if den == 1:
        return f"{num}"
    return f"\\tfrac{{{num}}}{{{den}}}"


_TAGS_ADDSUB = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_COMPARE = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-conceptual-reasoning",
]


# ---------------------------------------------------------------------------
# Topic 1: adding_and_subtracting_fractions
# ---------------------------------------------------------------------------

@register
class AddFractionsSameDenom(Generator):
    """Compute a/d + b/d: share the denominator, add numerators, simplify."""
    generator_id = "add_fractions_same_denom"
    topic_slug = "adding_and_subtracting_fractions"
    display_name = "Add fractions with the same denominator"

    _D_RANGES = {"easy": (2, 10), "medium": (3, 15), "hard": (4, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        d_lo, d_hi = self._D_RANGES[difficulty]
        d = rng.randint(d_lo, d_hi)
        # Keep the unreduced sum as a proper-ish fraction (1..2d-1 keeps it
        # modestly sized and frequently non-reduced).
        a = rng.randint(1, d - 1 if d > 2 else 1)
        b = rng.randint(1, d)
        sum_num = a + b  # numerator of the unreduced sum

        reduced = Fraction(sum_num, d)
        red_num, red_den = reduced.numerator, reduced.denominator
        was_reducible = (red_num, red_den) != (sum_num, d)

        statement_latex = (
            f"Compute ${_fmt_frac(a, d)} + {_fmt_frac(b, d)}$."
        )

        # Build steps
        steps: list[str] = [
            (
                f"The denominators are the same, so add the numerators and keep "
                f"the denominator: ${_fmt_frac(a, d)} + {_fmt_frac(b, d)} = "
                f"{_fmt_frac(sum_num, d)}$."
            ),
        ]
        if was_reducible:
            g = gcd(sum_num, d)
            steps.append(
                f"Simplify by dividing top and bottom by "
                f"$\\gcd({sum_num}, {d}) = {g}$: "
                f"${_fmt_frac(sum_num, d)} = {_fmt_frac(red_num, red_den)}$."
            )
        else:
            steps.append(
                f"Check whether ${_fmt_frac(sum_num, d)}$ can be simplified. "
                f"$\\gcd({sum_num}, {d}) = 1$, so it is already in lowest terms."
            )
        steps.append(f"Final answer: ${_fmt_frac(red_num, red_den)}$.")

        hints = [
            "When denominators match, add only the numerators.",
            f"${a} + {b} = {sum_num}$, so the sum is ${_fmt_frac(sum_num, d)}$.",
            (
                "Always check whether the result can be simplified."
                if was_reducible
                else "Check for common factors; none here, so the fraction is already simplified."
            ),
        ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=f"${_fmt_frac(red_num, red_den)}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=_TAGS_ADDSUB,
        )


@register
class AddFractionsUnlikeDenom(Generator):
    """Compute a/d1 + b/d2 where d1 != d2 via a common denominator."""
    generator_id = "add_fractions_unlike_denom"
    topic_slug = "adding_and_subtracting_fractions"
    display_name = "Add fractions with unlike denominators"

    _DENOM_POOLS = {
        "easy": [2, 3, 4, 6],
        "medium": [2, 3, 4, 5, 6, 8],
        "hard": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pool = self._DENOM_POOLS[difficulty]
        d1 = rng.choice(pool)
        d2 = rng.choice([d for d in pool if d != d1])
        a = rng.randint(1, d1)
        b = rng.randint(1, d2)

        L = _lcm(d1, d2)
        m1 = L // d1  # multiplier to convert a/d1 -> (a*m1)/L
        m2 = L // d2
        a_conv = a * m1
        b_conv = b * m2
        sum_num = a_conv + b_conv

        reduced = Fraction(sum_num, L)
        red_num, red_den = reduced.numerator, reduced.denominator
        was_reducible = (red_num, red_den) != (sum_num, L)

        statement_latex = (
            f"Compute ${_fmt_frac(a, d1)} + {_fmt_frac(b, d2)}$."
        )

        steps: list[str] = [
            (
                f"The denominators differ. Find a common denominator: "
                f"$\\operatorname{{lcm}}({d1}, {d2}) = {L}$."
            ),
            (
                f"Rewrite each fraction with denominator ${L}$: "
                f"${_fmt_frac(a, d1)} = {_fmt_frac(a_conv, L)}$ and "
                f"${_fmt_frac(b, d2)} = {_fmt_frac(b_conv, L)}$."
            ),
            (
                f"Add the numerators: "
                f"${_fmt_frac(a_conv, L)} + {_fmt_frac(b_conv, L)} = "
                f"{_fmt_frac(sum_num, L)}$."
            ),
        ]
        if was_reducible:
            g = gcd(sum_num, L)
            steps.append(
                f"Simplify: divide top and bottom by "
                f"$\\gcd({sum_num}, {L}) = {g}$, giving "
                f"${_fmt_frac(red_num, red_den)}$."
            )
        steps.append(f"Final answer: ${_fmt_frac(red_num, red_den)}$.")

        hints = [
            (
                "You cannot add fractions until they share a denominator. "
                "Use the least common multiple of the denominators."
            ),
            f"A common denominator is ${L}$ (the LCM of ${d1}$ and ${d2}$).",
            (
                f"Convert, then add. The final answer is "
                f"${_fmt_frac(red_num, red_den)}$."
            ),
        ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, d1, b, d2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=f"${_fmt_frac(red_num, red_den)}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=_TAGS_ADDSUB,
        )


@register
class SubtractFractionsUnlikeDenom(Generator):
    """Compute a/d1 - b/d2 (positive result) via a common denominator."""
    generator_id = "subtract_fractions_unlike_denom"
    topic_slug = "adding_and_subtracting_fractions"
    display_name = "Subtract fractions with unlike denominators"

    _DENOM_POOLS = {
        "easy": [2, 3, 4, 6],
        "medium": [2, 3, 4, 5, 6, 8],
        "hard": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pool = self._DENOM_POOLS[difficulty]
        d1 = rng.choice(pool)
        d2 = rng.choice([d for d in pool if d != d1])
        a = rng.randint(1, d1)
        b = rng.randint(1, d2)

        # Guarantee a positive result: swap so that a/d1 > b/d2.
        if Fraction(a, d1) <= Fraction(b, d2):
            a, b, d1, d2 = b, a, d2, d1
            # After swap the inequality is strict unless the two fractions
            # are equal. Guard that corner case.
            if Fraction(a, d1) == Fraction(b, d2):
                # Nudge b down by one; b >= 1 by construction, so make it
                # b-1 when safe, otherwise change a upward by one (bounded
                # by d1).
                if b > 1:
                    b -= 1
                elif a < d1:
                    a += 1
                else:
                    # Extremely unlikely; adjust denominators instead.
                    d2 = next((d for d in pool if d != d1 and d != d2), d2 + 1)

        L = _lcm(d1, d2)
        m1 = L // d1
        m2 = L // d2
        a_conv = a * m1
        b_conv = b * m2
        diff_num = a_conv - b_conv

        reduced = Fraction(diff_num, L)
        red_num, red_den = reduced.numerator, reduced.denominator
        was_reducible = (red_num, red_den) != (diff_num, L)

        statement_latex = (
            f"Compute ${_fmt_frac(a, d1)} - {_fmt_frac(b, d2)}$."
        )

        steps: list[str] = [
            (
                f"The denominators differ. Find a common denominator: "
                f"$\\operatorname{{lcm}}({d1}, {d2}) = {L}$."
            ),
            (
                f"Rewrite each fraction with denominator ${L}$: "
                f"${_fmt_frac(a, d1)} = {_fmt_frac(a_conv, L)}$ and "
                f"${_fmt_frac(b, d2)} = {_fmt_frac(b_conv, L)}$."
            ),
            (
                f"Subtract the numerators: "
                f"${_fmt_frac(a_conv, L)} - {_fmt_frac(b_conv, L)} = "
                f"{_fmt_frac(diff_num, L)}$."
            ),
        ]
        if was_reducible:
            g = gcd(diff_num, L)
            steps.append(
                f"Simplify: divide top and bottom by "
                f"$\\gcd({diff_num}, {L}) = {g}$, giving "
                f"${_fmt_frac(red_num, red_den)}$."
            )
        steps.append(f"Final answer: ${_fmt_frac(red_num, red_den)}$.")

        hints = [
            "Rewrite both fractions with a common denominator, then subtract.",
            f"The least common multiple of ${d1}$ and ${d2}$ is ${L}$.",
            (
                f"After subtracting, simplify. The result is "
                f"${_fmt_frac(red_num, red_den)}$."
            ),
        ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, d1, b, d2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=f"${_fmt_frac(red_num, red_den)}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=_TAGS_ADDSUB,
        )


# ---------------------------------------------------------------------------
# Topic 2: comparing_and_ordering_fractions
# ---------------------------------------------------------------------------

@register
class CompareTwoFractions(Generator):
    """Decide whether a/b is <, >, or = to c/d using cross-multiplication."""
    generator_id = "compare_two_fractions"
    topic_slug = "comparing_and_ordering_fractions"
    display_name = "Compare two fractions"

    _DENOM_RANGES = {"easy": (2, 9), "medium": (2, 12), "hard": (2, 15)}

    def _pick_distinct_denoms(
        self, rng: random.Random, lo: int, hi: int
    ) -> tuple[int, int]:
        b = rng.randint(lo, hi)
        d = rng.randint(lo, hi)
        while d == b:
            d = rng.randint(lo, hi)
        return b, d

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._DENOM_RANGES[difficulty]
        bucket = rng.random()

        if bucket < 0.2:
            # 20% Equal fractions in disguise: build c/d from a/b by scaling.
            b, _ = self._pick_distinct_denoms(rng, lo, hi)
            a = rng.randint(1, b)
            k = rng.randint(2, 4)
            c = a * k
            d = b * k
            if d == b:  # safety, shouldn't trigger because k >= 2
                d = b * (k + 1)
                c = a * (k + 1)
        elif bucket < 0.6:
            # 40% Close call: numerators chosen so cross-products are within
            # a small delta of each other.
            b, d = self._pick_distinct_denoms(rng, lo, hi)
            a = rng.randint(1, b)
            # Aim for c/d close to a/b. Using the float target then
            # snapping to the nearest valid integer numerator in [1, d].
            target_cross = a * d  # we want c*b ~= a*d
            c_float = target_cross / b
            c = max(1, min(d, round(c_float) + rng.choice([-1, 0, 1])))
            # Nudge so c*b != a*d most of the time (otherwise "close" becomes
            # equal, which we handled in the 20% bucket).
            if c * b == a * d and c < d:
                c += 1
            elif c * b == a * d and c > 1:
                c -= 1
        else:
            # 40% Easy: arbitrary distinct pairs.
            b, d = self._pick_distinct_denoms(rng, lo, hi)
            a = rng.randint(1, b)
            c = rng.randint(1, d)

        fa = Fraction(a, b)
        fc = Fraction(c, d)
        if fa < fc:
            symbol = "<"
            phrase = "is less than"
        elif fa > fc:
            symbol = ">"
            phrase = "is greater than"
        else:
            symbol = "="
            phrase = "is equal to"

        cross_left = a * d
        cross_right = c * b

        statement_latex = (
            f"Which symbol ($<$, $>$, or $=$) makes the statement true? "
            f"${_fmt_frac(a, b)} \\;\\square\\; {_fmt_frac(c, d)}$"
        )

        steps: list[str] = [
            (
                f"Cross multiply: compare ${a} \\times {d}$ with ${c} \\times {b}$."
            ),
            (
                f"${a} \\times {d} = {cross_left}$ and ${c} \\times {b} = {cross_right}$."
            ),
        ]
        if symbol == "<":
            steps.append(
                f"Since ${cross_left} < {cross_right}$, the first fraction is smaller, "
                f"so ${_fmt_frac(a, b)} < {_fmt_frac(c, d)}$."
            )
        elif symbol == ">":
            steps.append(
                f"Since ${cross_left} > {cross_right}$, the first fraction is larger, "
                f"so ${_fmt_frac(a, b)} > {_fmt_frac(c, d)}$."
            )
        else:
            steps.append(
                f"Since ${cross_left} = {cross_right}$, the two fractions are equal, "
                f"so ${_fmt_frac(a, b)} = {_fmt_frac(c, d)}$."
            )

        hints = [
            (
                "To compare fractions with different denominators, use cross "
                "multiplication: compare $a \\times d$ to $c \\times b$."
            ),
            (
                "If $a \\times d < c \\times b$ then $a/b < c/d$; if greater, the "
                "reverse; if equal, the fractions are equal."
            ),
            (
                f"Here $a \\times d = {cross_left}$ and $c \\times b = {cross_right}$, "
                f"so ${_fmt_frac(a, b)}$ {phrase} ${_fmt_frac(c, d)}$."
            ),
        ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=f"${symbol}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=_TAGS_COMPARE,
        )


@register
class OrderThreeFractions(Generator):
    """Sort three distinct fractions from smallest to largest."""
    generator_id = "order_three_fractions"
    topic_slug = "comparing_and_ordering_fractions"
    display_name = "Order three fractions from least to greatest"

    _DENOM_POOLS = {
        "easy": [2, 3, 4, 6, 8],
        "medium": [2, 3, 4, 5, 6, 8, 10, 12],
        "hard": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pool = self._DENOM_POOLS[difficulty]
        # Pick three (possibly repeated) denominators but ensure three
        # distinct fraction values.
        for _ in range(30):
            d_list = [rng.choice(pool) for _ in range(3)]
            n_list = [rng.randint(1, d) for d in d_list]
            fracs = [Fraction(n, d) for n, d in zip(n_list, d_list)]
            if len(set(fracs)) == 3:
                break
        else:
            # Fallback: force distinctness with fixed denominators.
            d_list = [pool[0], pool[1 % len(pool)], pool[2 % len(pool)]]
            n_list = [1, 2, 3]
            fracs = [Fraction(n, d) for n, d in zip(n_list, d_list)]

        # Common denominator for the worked steps.
        L = 1
        for d in d_list:
            L = _lcm(L, d)
        converted = [(n * (L // d), L) for n, d in zip(n_list, d_list)]

        # Sort original pairs by value ascending, remembering their
        # positions for the problem statement.
        indexed = sorted(
            range(3), key=lambda i: fracs[i]
        )
        sorted_pairs = [(n_list[i], d_list[i]) for i in indexed]

        # Statement: fractions shown in their original (unsorted) order.
        frac_strs = [f"{_fmt_frac(n, d)}" for n, d in zip(n_list, d_list)]
        statement_latex = (
            "Arrange the fractions from least to greatest: "
            f"${frac_strs[0]},\\ {frac_strs[1]},\\ {frac_strs[2]}$."
        )

        # Answer line: sorted fractions joined by <.
        sorted_str = " < ".join(_fmt_tfrac(n, d) for n, d in sorted_pairs)
        answer_latex = f"${sorted_str}$"

        conv_strs = [
            f"{_fmt_frac(n, d)} = {_fmt_frac(nc, L)}"
            for (n, d), (nc, _) in zip(zip(n_list, d_list), converted)
        ]
        # Sort the converted numerators ascending for step 3.
        conv_sorted = sorted(range(3), key=lambda i: converted[i][0])
        conv_sorted_str = " < ".join(
            f"{_fmt_frac(converted[i][0], L)}" for i in conv_sorted
        )

        steps = [
            (
                f"Find a common denominator for all three fractions: "
                f"$\\operatorname{{lcm}}({d_list[0]}, {d_list[1]}, {d_list[2]}) = {L}$."
            ),
            "Rewrite each fraction with that denominator: $"
            + ",\\ ".join(conv_strs)
            + "$.",
            (
                f"With the same denominator, just compare numerators: "
                f"${conv_sorted_str}$."
            ),
            f"Therefore the ordered list is ${sorted_str}$.",
        ]

        hints = [
            (
                "Fractions are easy to compare once they share a denominator. "
                "Find the LCM of all three denominators."
            ),
            (
                f"Here the LCM of ${d_list[0]}$, ${d_list[1]}$, and ${d_list[2]}$ is "
                f"${L}$."
            ),
            (
                "After converting, sort by numerator from smallest to largest."
            ),
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (n_list[0], d_list[0], n_list[1], d_list[1], n_list[2], d_list[2]),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=answer_latex,
            hints=hints,
            solution_steps_latex=steps,
            tags=_TAGS_COMPARE,
        )


@register
class CompareFractionToHalf(Generator):
    """Is n/d <, >, or = to 1/2? Uses the halfway-numerator rule."""
    generator_id = "compare_fraction_to_half"
    topic_slug = "comparing_and_ordering_fractions"
    display_name = "Compare a fraction to 1/2"

    _DENOM_RANGES = {"easy": (3, 12), "medium": (3, 20), "hard": (3, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._DENOM_RANGES[difficulty]
        d = rng.randint(lo, hi)
        n = rng.randint(1, d)

        value = Fraction(n, d)
        half = Fraction(1, 2)
        if value < half:
            symbol = "<"
            phrase = "is less than"
        elif value > half:
            symbol = ">"
            phrase = "is greater than"
        else:
            symbol = "="
            phrase = "is equal to"

        statement_latex = (
            f"Is ${_fmt_frac(n, d)}$ less than, greater than, or equal to "
            f"$\\frac{{1}}{{2}}$? Give your answer as $<$, $>$, or $=$."
        )

        if d % 2 == 0:
            half_den = d // 2
            if n < half_den:
                rule_step = (
                    f"Half of ${d}$ is ${half_den}$. Since ${n} < {half_den}$, "
                    f"the numerator is less than half the denominator, so "
                    f"${_fmt_frac(n, d)} < \\frac{{1}}{{2}}$."
                )
            elif n > half_den:
                rule_step = (
                    f"Half of ${d}$ is ${half_den}$. Since ${n} > {half_den}$, "
                    f"the numerator is more than half the denominator, so "
                    f"${_fmt_frac(n, d)} > \\frac{{1}}{{2}}$."
                )
            else:
                rule_step = (
                    f"Half of ${d}$ is ${half_den}$, and ${n} = {half_den}$, so "
                    f"${_fmt_frac(n, d)} = \\frac{{1}}{{2}}$."
                )
        else:
            # Odd denominator: never exactly 1/2. Compare 2n to d instead.
            twice = 2 * n
            if twice < d:
                rule_step = (
                    f"Since ${d}$ is odd, ${_fmt_frac(n, d)}$ cannot equal "
                    f"$\\frac{{1}}{{2}}$. Doubling the numerator: "
                    f"$2 \\times {n} = {twice}$. Because ${twice} < {d}$, "
                    f"${_fmt_frac(n, d)} < \\frac{{1}}{{2}}$."
                )
            else:
                rule_step = (
                    f"Since ${d}$ is odd, ${_fmt_frac(n, d)}$ cannot equal "
                    f"$\\frac{{1}}{{2}}$. Doubling the numerator: "
                    f"$2 \\times {n} = {twice}$. Because ${twice} > {d}$, "
                    f"${_fmt_frac(n, d)} > \\frac{{1}}{{2}}$."
                )

        steps = [
            (
                "Shortcut: compare the numerator to half the denominator, "
                "or equivalently compare $2n$ to $d$."
            ),
            rule_step,
            f"Therefore ${_fmt_frac(n, d)} {symbol} \\frac{{1}}{{2}}$.",
        ]

        hints = [
            (
                "A fraction $n/d$ equals $1/2$ when the numerator is exactly "
                "half the denominator."
            ),
            (
                f"Compare $2 \\times {n} = {2 * n}$ to ${d}$. "
                f"That tells you which side of $\\frac{{1}}{{2}}$ the fraction sits on."
            ),
            (
                f"${_fmt_frac(n, d)}$ {phrase} $\\frac{{1}}{{2}}$."
            ),
        ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=f"${symbol}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=_TAGS_COMPARE,
        )
