"""Absolute-value equation generators (Phase 2c Wave 3).

Canonical topic slug ``absolute_value_equations`` at
wiki/topics/algebra/Absolute_Value_Equations.md (Algebra I Ch 3.4).

- abs_val_eq_simple: |x| = c, or |x + b| = c
- abs_val_eq_linear: |ax + b| = c
- abs_val_eq_no_solution: |ax + b| = -c (student must recognize no solution)
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

@register
class AbsValEqSimple(Generator):
    """Solve |x + b| = c where c > 0 (two solutions)."""
    generator_id = "abs_val_eq_simple"
    topic_slug = "absolute_value_equations"
    display_name = "Solve |x + b| = c"

    _B_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-30, 30)}
    _C_RANGE = {"easy": (1, 12), "medium": (1, 25), "hard": (1, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        b_lo, b_hi = self._B_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]
        b = rng.randint(b_lo, b_hi)
        c = rng.randint(c_lo, c_hi)
        # Two solutions: x + b = c → x = c - b, or x + b = -c → x = -c - b
        x1 = c - b
        x2 = -c - b
        xs = sorted([x1, x2])

        b_str = f"x + {b}" if b >= 0 else f"x - {abs(b)}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve $|{b_str}| = {c}$.",
            answer_latex=f"$x = {xs[0]}$ or $x = {xs[1]}$",
            hints=[
                r"An absolute-value equation $|\text{expression}| = c$ (with $c > 0$) means the expression inside equals either $c$ or $-c$.",
                f"Split into two equations: ${b_str} = {c}$ and ${b_str} = {-c}$.",
                f"Solve each to get $x = {xs[0]}$ or $x = {xs[1]}$.",
            ],
            solution_steps_latex=[
                f"Write two cases: ${b_str} = {c}$ or ${b_str} = {-c}$.",
                f"Case 1: solve ${b_str} = {c}$ to get $x = {x1}$.",
                f"Case 2: solve ${b_str} = {-c}$ to get $x = {x2}$.",
                f"The two solutions are $x = {xs[0]}$ and $x = {xs[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class AbsValEqLinear(Generator):
    """Solve |ax + b| = c (with integer solutions by construction)."""
    generator_id = "abs_val_eq_linear"
    topic_slug = "absolute_value_equations"
    display_name = "Solve |ax + b| = c"

    _A_RANGE = {"easy": (2, 6), "medium": (2, 10), "hard": (2, 15)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-20, 20)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(var_lo, var_hi)
        # Pick a positive x that gives clean integer solutions on both branches
        x_val = rng.randint(1, var_hi)
        inside_plus = a * x_val + b
        c = abs(inside_plus) if inside_plus != 0 else a
        # The two solutions
        x1 = (c - b) / a
        x2 = (-c - b) / a
        # Ensure both are integers
        if int(x1) != x1 or int(x2) != x2:
            # Adjust b so that both branches produce integers
            b = rng.choice([0, a, -a])
            x_val = rng.randint(2, var_hi)
            inside_plus = a * x_val + b
            c = abs(inside_plus)
            x1 = (c - b) // a
            x2 = (-c - b) // a
        else:
            x1 = int(x1)
            x2 = int(x2)

        xs = sorted([x1, x2])
        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        if b == 0:
            inside = f"{a}x"
        else:
            inside = f"{a}x {b_str}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve $|{inside}| = {c}$.",
            answer_latex=f"$x = {xs[0]}$ or $x = {xs[1]}$",
            hints=[
                r"Split into two linear equations: the inside equals $+c$ or $-c$.",
                f"Case 1: ${inside} = {c}$. Case 2: ${inside} = {-c}$.",
                "Solve each linear equation for $x$.",
            ],
            solution_steps_latex=[
                f"Case 1: solve ${inside} = {c}$.",
                f"Subtract $({b})$ and divide by ${a}$: $x = {x1}$.",
                f"Case 2: solve ${inside} = {-c}$.",
                f"Subtract $({b})$ and divide by ${a}$: $x = {x2}$.",
                f"Solutions: $x = {xs[0]}$ or $x = {xs[1]}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class AbsValEqNoSolution(Generator):
    """Recognize that |ax + b| = negative has no real solution (trick question)."""
    generator_id = "abs_val_eq_no_solution"
    topic_slug = "absolute_value_equations"
    display_name = "Identify when |ax + b| = c has no solution"
    bank_count_per_difficulty = 25

    _A_RANGE = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}
    _VAR_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-25, 25)}
    _C_RANGE = {"easy": (1, 12), "medium": (1, 20), "hard": (1, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(var_lo, var_hi)
        c_neg = -rng.randint(c_lo, c_hi)  # guaranteed negative

        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        if a == 1:
            inside = f"x {b_str}" if b != 0 else "x"
        else:
            inside = f"{a}x {b_str}" if b != 0 else f"{a}x"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c_neg)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve $|{inside}| = {c_neg}$.",
            answer_latex="No solution",
            hints=[
                r"The absolute value of any real number is **never negative**. If the equation sets $|\text{expression}|$ equal to a negative number, there is no real solution.",
                f"Here the right side is ${c_neg} < 0$.",
            ],
            solution_steps_latex=[
                r"Recall that $|\text{anything}| \geq 0$ for all real values.",
                f"The equation says $|{inside}| = {c_neg}$, but the left side cannot be negative.",
                "Therefore there is **no solution**.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-visualization"],
        )
