"""Introductory exponents and powers generators.

Canonical topic slug ``exponents_and_powers`` at
wiki/topics/pre_algebra/Exponents_And_Powers.md (Math I Ch 1.4).

- evaluate_power_small: compute $b^n$ for small $b$ and $n$
- evaluate_power_with_negative_base: distinguish $(-b)^n$ from $-b^n$
- compare_two_powers: decide which of two powers is larger

The compare generator precomputes its table of `close` pairs at import
time via nested loops, so each difficulty gets a deterministic list of
($b_1,n_1,b_2,n_2$) tuples where the two values are different but within
a bounded ratio.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

@register
class EvaluatePowerSmall(Generator):
    """Evaluate $b^n$ with small non-negative integer exponents and bases."""
    generator_id = "evaluate_power_small"
    topic_slug = "exponents_and_powers"
    display_name = "Evaluate a small power"

    _PAIRS: dict[Difficulty, list[tuple[int, int]]] = {
        "easy":   [(b, n) for b in range(2, 9)  for n in range(1, 7)],   # 42 pairs
        "medium": [(b, n) for b in range(2, 12) for n in range(0, 7)],   # 70 pairs
        "hard":   [(b, n) for b in range(2, 14) for n in range(0, 8)],   # 96 pairs
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pairs = self._PAIRS[difficulty]
        b, n = pairs[rng.randrange(len(pairs))]
        result = b ** n

        if n == 0:
            rule_hint = "Any nonzero base raised to the power $0$ equals $1$."
            expansion = f"${b}^0 = 1$ by the zero-exponent rule."
        elif n == 1:
            rule_hint = "Any number to the first power is the number itself."
            expansion = f"${b}^1 = {b}$."
        else:
            factors = r" \times ".join([str(b)] * n)
            rule_hint = (
                f"Recall that ${b}^{{{n}}}$ means ${b}$ multiplied by itself ${n}$ times."
            )
            expansion = f"${b}^{{{n}}} = {factors} = {result}$."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${b}^{{{n}}}$.",
            answer_latex=f"${result}$",
            hints=[
                rule_hint,
                f"The base is ${b}$ and the exponent is ${n}$.",
                expansion,
            ],
            solution_steps_latex=[
                f"Identify the base ${b}$ and exponent ${n}$.",
                expansion,
                f"Therefore ${b}^{{{n}}} = {result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-exponents-and-radicals", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

@register
class EvaluatePowerWithNegativeBase(Generator):
    """Distinguish $(-b)^n$ from $-b^n$ by paying attention to parentheses."""
    generator_id = "evaluate_power_with_negative_base"
    topic_slug = "exponents_and_powers"
    display_name = "Evaluate a power with a negative sign"

    # (b_range, n_range) per difficulty. The two forms double the parameter space.
    # Comfortable headroom above 30 so the coupon-collector dedup loop converges.
    _PARAMS = {
        "easy":   {"b_max": 8,  "n_min": 2, "n_max": 4},   # 7 * 3 * 2 = 42
        "medium": {"b_max": 10, "n_min": 2, "n_max": 5},   # 9 * 4 * 2 = 72
        "hard":   {"b_max": 12, "n_min": 2, "n_max": 6},   # 11 * 5 * 2 = 110
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        b = rng.randint(2, params["b_max"])
        n = rng.randint(params["n_min"], params["n_max"])
        form = rng.choice(["paren", "no_paren"])

        if form == "paren":
            # (-b)^n: sign depends on parity of n
            result = (-b) ** n
            statement = f"Evaluate $(-{b})^{{{n}}}$."
            factors = r" \times ".join([f"(-{b})"] * n)
            if n % 2 == 0:
                sign_explain = f"Because ${n}$ is even, the product of ${n}$ negative factors is positive."
            else:
                sign_explain = f"Because ${n}$ is odd, the product of ${n}$ negative factors is negative."
            expansion = f"$(-{b})^{{{n}}} = {factors} = {result}$."
            group_hint = (
                f"The parentheses around $-{b}$ tell you the negative sign is part of the base."
            )
        else:
            # -b^n: the exponent applies only to b; the minus sign sits outside
            result = -(b ** n)
            statement = f"Evaluate $-{b}^{{{n}}}$."
            factors = r" \times ".join([str(b)] * n)
            sign_explain = (
                f"The exponent applies only to ${b}$, not to the negative sign. "
                f"So first compute ${b}^{{{n}}}$, then negate."
            )
            expansion = f"$-{b}^{{{n}}} = -({factors}) = -{b ** n} = {result}$."
            group_hint = (
                f"There are no parentheses, so the minus sign stays outside the exponent: "
                f"$-{b}^{{{n}}}$ means $-({b}^{{{n}}})$."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, n, form)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${result}$",
            hints=[
                group_hint,
                sign_explain,
                expansion,
            ],
            solution_steps_latex=[
                f"Read the expression carefully: {statement.rstrip('.')}.",
                group_hint,
                expansion,
                f"Final answer: ${result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-exponents-and-radicals", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

def _close_power_pairs(
    b_range: tuple[int, int],
    n_range: tuple[int, int],
    ratio_max: float,
) -> list[tuple[int, int, int, int]]:
    """All ($b_1,n_1,b_2,n_2$) with distinct values within `ratio_max`.

    Pairs are canonical (smaller value first) and deduplicated by value.
    """
    powers: list[tuple[int, int, int]] = []
    for b in range(b_range[0], b_range[1] + 1):
        for n in range(n_range[0], n_range[1] + 1):
            powers.append((b, n, b ** n))
    out: list[tuple[int, int, int, int]] = []
    seen_value_pairs: set[tuple[int, int]] = set()
    for i in range(len(powers)):
        for j in range(i + 1, len(powers)):
            b1, n1, v1 = powers[i]
            b2, n2, v2 = powers[j]
            if v1 == v2:
                continue
            # Canonical order: smaller value first
            if v1 < v2:
                lo_v, hi_v = v1, v2
                pair = (b1, n1, b2, n2)
            else:
                lo_v, hi_v = v2, v1
                pair = (b2, n2, b1, n1)
            if (lo_v, hi_v) in seen_value_pairs:
                continue
            if hi_v / lo_v <= ratio_max:
                seen_value_pairs.add((lo_v, hi_v))
                out.append(pair)
    return out


@register
class CompareTwoPowers(Generator):
    """`Which is larger: $b_1^{n_1}$ or $b_2^{n_2}$?` for close-valued powers."""
    generator_id = "compare_two_powers"
    topic_slug = "exponents_and_powers"
    display_name = "Compare two powers"

    _TABLES: dict[Difficulty, list[tuple[int, int, int, int]]] = {
        "easy":   _close_power_pairs((2, 11), (2, 5), 1.9),
        "medium": _close_power_pairs((2, 13), (2, 6), 1.55),
        "hard":   _close_power_pairs((2, 15), (2, 7), 1.35),
    }

    # Tables may be smaller than the default 30 depending on the ratio filter;
    # set an effective bank cap at roughly 60% of the smallest table length so
    # the coupon-collector dedup loop converges with room to spare.
    bank_count_per_difficulty = max(
        10,
        (min(len(_TABLES["easy"]), len(_TABLES["medium"]), len(_TABLES["hard"])) * 6) // 10,
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        table = self._TABLES[difficulty]
        idx = rng.randrange(len(table))
        b1, n1, b2, n2 = table[idx]
        v1 = b1 ** n1
        v2 = b2 ** n2
        # Present in (b1, n1) vs (b2, n2) order; answer is the larger of the two.
        if rng.random() < 0.5:
            b1, n1, b2, n2 = b2, n2, b1, n1
            v1, v2 = v2, v1

        if v1 > v2:
            larger_expr = f"{b1}^{{{n1}}}"
            larger_value = v1
            smaller_expr = f"{b2}^{{{n2}}}"
            smaller_value = v2
        else:
            larger_expr = f"{b2}^{{{n2}}}"
            larger_value = v2
            smaller_expr = f"{b1}^{{{n1}}}"
            smaller_value = v1

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b1, n1, b2, n2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Which is larger: ${b1}^{{{n1}}}$ or ${b2}^{{{n2}}}$?",
            answer_latex=f"${larger_expr}$",
            hints=[
                "Evaluate each power, then compare the results.",
                f"${b1}^{{{n1}}} = {v1}$ and ${b2}^{{{n2}}} = {v2}$.",
                f"Since ${larger_value} > {smaller_value}$, the larger value is ${larger_expr}$.",
            ],
            solution_steps_latex=[
                f"Compute the first power: ${b1}^{{{n1}}} = {v1}$.",
                f"Compute the second power: ${b2}^{{{n2}}} = {v2}$.",
                f"Compare: ${larger_value} > {smaller_value}$, so the larger value is ${larger_expr}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-exponents-and-radicals", "#skill-multi-step"],
        )
