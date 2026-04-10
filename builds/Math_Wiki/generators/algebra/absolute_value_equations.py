"""Absolute value equation generators (Phase 2c Wave 3).

Canonical topic slug ``absolute_value_equations`` at
wiki/topics/algebra/Absolute_Value_Equations.md (Algebra I Ch 3.4).

- abs_value_basic: solve |ax + b| = c where c > 0 (two solutions)
- abs_value_isolate_first: solve |ax + b| + d = c (isolate the |...| first)
- abs_value_special_cases: recognize "no solution" (c < 0) and "one solution" (c = 0)
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


@register
class AbsValueBasic(Generator):
    """Solve |ax + b| = c with c > 0."""
    generator_id = "abs_value_basic"
    topic_slug = "absolute_value_equations"
    display_name = "Solve |ax + b| = c"

    _A_RANGE = {"easy": (1, 5), "medium": (1, 9), "hard": (1, 15)}
    _X_RANGE = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        # Pick the two solutions first, symmetric around -b/a, derive b and c
        x1 = rng.randint(x_lo, x_hi)
        x2 = rng.randint(x_lo, x_hi)
        while x2 == x1:
            x2 = rng.randint(x_lo, x_hi)
        # Center: -b/a = (x1 + x2)/2 -> b = -a*(x1 + x2)/2. Need this to be integer.
        total = x1 + x2
        if (a * total) % 2 != 0:
            # Fix by nudging x2
            x2 += 1
            total = x1 + x2
        b = -a * total // 2
        # c = |a*x1 + b|
        c = abs(a * x1 + b)
        if c == 0:
            # rare case; nudge
            x2 += 1
            total = x1 + x2
            if (a * total) % 2 != 0:
                x2 += 1
                total = x1 + x2
            b = -a * total // 2
            c = abs(a * x1 + b)
        roots = sorted([x1, x2])

        eq_latex = f"|{sp.latex(a * x + b)}| = {c}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"$|A| = c$ (with $c > 0$) means $A = c$ **or** $A = -c$. You get two equations.",
                f"Split: ${sp.latex(a * x + b)} = {c}$ or ${sp.latex(a * x + b)} = -{c}$.",
                f"Solve each one-variable equation.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Split into two cases: ${sp.latex(a * x + b)} = {c}$ or ${sp.latex(a * x + b)} = -{c}$.",
                f"Case 1: Solve ${sp.latex(a * x + b)} = {c}$.",
                f"Case 2: Solve ${sp.latex(a * x + b)} = -{c}$.",
                f"Solutions: $x = {roots[0]}$ and $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class AbsValueIsolateFirst(Generator):
    """Solve |ax + b| + d = c by isolating the absolute value first."""
    generator_id = "abs_value_isolate_first"
    topic_slug = "absolute_value_equations"
    display_name = "Solve |ax + b| + d = c (isolate first)"
    bank_count_per_difficulty = 25

    _A_RANGE = {"easy": (1, 4), "medium": (1, 7), "hard": (1, 12)}
    _X_RANGE = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-18, 18)}
    _D_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        d_lo, d_hi = self._D_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        x1 = rng.randint(x_lo, x_hi)
        x2 = rng.randint(x_lo, x_hi)
        while x2 == x1:
            x2 = rng.randint(x_lo, x_hi)
        total = x1 + x2
        if (a * total) % 2 != 0:
            x2 += 1
            total = x1 + x2
        b = -a * total // 2
        isolated_c = abs(a * x1 + b)
        if isolated_c == 0:
            x2 += 2
            total = x1 + x2
            if (a * total) % 2 != 0:
                x2 += 1
                total = x1 + x2
            b = -a * total // 2
            isolated_c = abs(a * x1 + b)
        d = rng.randint(d_lo, d_hi)
        while d == 0:
            d = rng.randint(d_lo, d_hi)
        c = isolated_c + d  # we rewrite as |...| + d = c, so |...| = c - d = isolated_c
        roots = sorted([x1, x2])

        eq_latex = f"|{sp.latex(a * x + b)}| + {d} = {c}"
        if d < 0:
            eq_latex = f"|{sp.latex(a * x + b)}| - {abs(d)} = {c}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {roots[0]}$ or $x = {roots[1]}$",
            hints=[
                r"First isolate the absolute value. Move the constant to the other side so the equation reads $|A| = \text{something}$.",
                f"{'Subtract' if d > 0 else 'Add'} ${abs(d)}$ from both sides: $|{sp.latex(a * x + b)}| = {isolated_c}$.",
                f"Now split: ${sp.latex(a * x + b)} = {isolated_c}$ or ${sp.latex(a * x + b)} = -{isolated_c}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Isolate the absolute value: $|{sp.latex(a * x + b)}| = {isolated_c}$.",
                f"Split into two cases: ${sp.latex(a * x + b)} = {isolated_c}$ or ${sp.latex(a * x + b)} = -{isolated_c}$.",
                f"Solve each case: $x = {roots[0]}$ or $x = {roots[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class AbsValueSpecialCases(Generator):
    """Recognize |ax + b| = c where c = 0 (one solution) or c < 0 (no solution)."""
    generator_id = "abs_value_special_cases"
    topic_slug = "absolute_value_equations"
    display_name = "Recognize no-solution or one-solution absolute value equations"
    bank_count_per_difficulty = 20

    _A_RANGE = {"easy": (1, 5), "medium": (1, 9), "hard": (1, 14)}
    _X_RANGE = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(x_lo, x_hi)
        case = rng.choice(["no_solution", "one_solution"])

        if case == "no_solution":
            c = -rng.randint(1, abs(x_hi))  # negative
            eq_latex = f"|{sp.latex(a * x + b)}| = {c}"
            answer_text = "No solution"
            answer_latex = "No solution"
        else:
            c = 0
            eq_latex = f"|{sp.latex(a * x + b)}| = 0"
            # Solve a*x + b = 0 -> x = -b/a
            if b % a == 0:
                x_val = -b // a
                answer_text = f"x = {x_val}"
                answer_latex = f"$x = {x_val}$"
            else:
                # Nudge b to make it divisible by a
                b = a * (b // a)
                if b == 0 and a == 0:
                    b = a
                x_val = -b // a
                eq_latex = f"|{sp.latex(a * x + b)}| = 0"
                answer_text = f"x = {x_val}"
                answer_latex = f"$x = {x_val}$"

        hints = (
            [
                r"Absolute value is never negative, so $|A| = c$ has **no solution** when $c < 0$.",
                f"Here the right side is ${c}$, which is negative.",
            ]
            if case == "no_solution"
            else [
                r"$|A| = 0$ has exactly **one solution**: $A = 0$.",
                f"Solve ${sp.latex(a * x + b)} = 0$.",
            ]
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, case)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=answer_latex,
            hints=hints,
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                "Because absolute values are never negative, $|A| = c$ has no solution if $c < 0$, exactly one solution if $c = 0$ (when $A = 0$), and two solutions if $c > 0$."
                if case == "no_solution"
                else "Because $|A| = 0$ forces $A = 0$, set the expression inside equal to zero.",
                f"Conclusion: {answer_text}.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-proof-reasoning"],
        )
