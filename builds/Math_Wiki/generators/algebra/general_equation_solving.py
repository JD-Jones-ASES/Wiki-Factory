"""General one-variable equation solving generators (Wave B).

Canonical topic slug ``solving_equations_in_one_variable`` at
wiki/topics/algebra/Solving_Equations_In_One_Variable.md.

- general_linear_equation: rotation of one-step, two-step, and vars-both-sides
- simple_radical_equation: sqrt(ax + b) = c
- simple_rational_equation: a/(x + c) = b or a/x = b
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


# ---------------------------------------------------------------------------

@register
class GeneralLinearEquation(Generator):
    """Rotates between one-step, two-step, distributive, and vars-both-sides patterns."""
    generator_id = "general_linear_equation"
    topic_slug = "solving_equations_in_one_variable"
    display_name = "Solve a linear equation"
    bank_count_per_difficulty = 30

    _X_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-28, 28)}
    _COEF = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _CONST = {"easy": (-15, 15), "medium": (-25, 25), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X_RANGE[difficulty]
        a_lo, a_hi = self._COEF[difficulty]
        c_lo, c_hi = self._CONST[difficulty]

        x_val = rng.randint(x_lo, x_hi)
        pattern = rng.choice(["one_step_add", "two_step", "distributive", "vars_both"])

        if pattern == "one_step_add":
            b = rng.randint(c_lo, c_hi)
            c = x_val + b
            eq_latex = sp.latex(sp.Eq(x + b, c))
            hints = [
                r"The equation is a one-step equation. Isolate $x$ by undoing the addition.",
                f"Subtract ${b}$ from both sides.",
                f"That gives $x = {x_val}$.",
            ]
            steps = [
                f"Start with ${eq_latex}$.",
                f"Subtract ${b}$ from both sides: $x = {c} - ({b}) = {x_val}$.",
            ]
            params = ("one_step_add", b, c)

        elif pattern == "two_step":
            a = rng.randint(a_lo, a_hi)
            b = rng.randint(c_lo, c_hi)
            c = a * x_val + b
            eq_latex = sp.latex(sp.Eq(a * x + b, c))
            hints = [
                r"The equation is a two-step equation: isolate $x$ in two steps.",
                f"Subtract ${b}$ from both sides: ${a}x = {c - b}$.",
                f"Divide by ${a}$: $x = {x_val}$.",
            ]
            steps = [
                f"Start with ${eq_latex}$.",
                f"Subtract ${b}$ from both sides: ${a}x = {c - b}$.",
                f"Divide both sides by ${a}$: $x = {x_val}$.",
            ]
            params = ("two_step", a, b, c)

        elif pattern == "distributive":
            a = rng.randint(a_lo, a_hi)
            b = rng.randint(c_lo, c_hi)
            c = a * (x_val + b)
            eq_latex = sp.latex(sp.Eq(a * (x + b), c))
            dist_lhs = sp.latex(sp.expand(a * (x + b)))
            hints = [
                f"Distribute the ${a}$ across the parentheses first.",
                f"The equation becomes ${dist_lhs} = {c}$.",
                r"Solve the resulting two-step equation.",
            ]
            steps = [
                f"Start with ${eq_latex}$.",
                f"Distribute: ${dist_lhs} = {c}$.",
                f"Subtract ${a * b}$: ${a}x = {c - a * b}$.",
                f"Divide by ${a}$: $x = {x_val}$.",
            ]
            params = ("distributive", a, b, c)

        else:  # vars_both
            while True:
                a = rng.randint(a_lo, a_hi)
                cc = rng.randint(a_lo, a_hi)
                if a != cc:
                    break
            b = rng.randint(c_lo, c_hi)
            d = (a - cc) * x_val + b
            eq_latex = sp.latex(sp.Eq(a * x + b, cc * x + d))
            hints = [
                r"Variables appear on both sides. Collect the $x$-terms on one side.",
                f"Subtract ${cc}x$ from both sides: $({a - cc})x + {b} = {d}$.",
                f"Then isolate $x$ to get $x = {x_val}$.",
            ]
            steps = [
                f"Start with ${eq_latex}$.",
                f"Subtract ${cc}x$ from both sides: $({a - cc})x + {b} = {d}$.",
                f"Subtract ${b}$ from both sides: $({a - cc})x = {d - b}$.",
                f"Divide by $({a - cc})$: $x = {x_val}$.",
            ]
            params = ("vars_both", a, b, cc, d)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Determine $x$: ${eq_latex}$.",
            answer_latex=f"$x = {x_val}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class SimpleRadicalEquation(Generator):
    """Solve sqrt(ax + b) = c for integer x (with clean radicand)."""
    generator_id = "simple_radical_equation"
    topic_slug = "solving_equations_in_one_variable"
    display_name = "Solve a simple radical equation"

    _A_RANGE = {"easy": (1, 4), "medium": (1, 6), "hard": (1, 9)}
    _C_RANGE = {"easy": (2, 6), "medium": (3, 9), "hard": (4, 12)}
    _B_RANGE = {"easy": (-6, 10), "medium": (-12, 18), "hard": (-20, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        # Pick c (the radical's target), then compute radicand = c^2.
        # Then choose a and compute b so that a*x + b = c^2 with integer x.
        while True:
            c = rng.randint(c_lo, c_hi)
            radicand = c * c
            a = rng.randint(a_lo, a_hi)
            b = rng.randint(b_lo, b_hi)
            remainder = radicand - b
            if remainder % a == 0:
                x_val = remainder // a
                # Ensure nonzero, avoid trivial cases
                if x_val != 0:
                    break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find all $x$: $\\sqrt{{{a}x + {b}}} = {c}$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                r"To remove the square root, square both sides of the equation.",
                f"Squaring gives ${a}x + {b} = {c ** 2}$.",
                r"Then solve the resulting linear equation.",
            ],
            solution_steps_latex=[
                f"Start with $\\sqrt{{{a}x + {b}}} = {c}$.",
                f"Square both sides: ${a}x + {b} = {c ** 2}$.",
                f"Subtract ${b}$ from both sides: ${a}x = {c ** 2 - b}$.",
                f"Divide by ${a}$: $x = {x_val}$.",
                f"Check: $\\sqrt{{{a}({x_val}) + {b}}} = \\sqrt{{{c ** 2}}} = {c}$. Valid.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-exponents-and-radicals",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class SimpleRationalEquation(Generator):
    """Solve a/(x + c) = b or a/x = b for integer x."""
    generator_id = "simple_rational_equation"
    topic_slug = "solving_equations_in_one_variable"
    display_name = "Solve a simple rational equation"

    _X_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _B_RANGE = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}
    _C_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]

        form = rng.choice(["simple", "shifted"])

        if form == "simple":
            # a/x = b, with x != 0 and x | a cleanly
            while True:
                x_val = rng.randint(x_lo, x_hi)
                if x_val == 0:
                    continue
                b = rng.randint(b_lo, b_hi)
                if rng.random() < 0.5:
                    b = -b
                if b == 0:
                    continue
                a = b * x_val
                if a != 0:
                    break

            statement = f"Find all $x$: $\\dfrac{{{a}}}{{x}} = {b}$."
            hints = [
                r"Multiply both sides by $x$ to clear the denominator.",
                f"You get ${a} = {b} x$.",
                f"Divide by ${b}$: $x = {x_val}$.",
            ]
            steps = [
                f"Start with $\\dfrac{{{a}}}{{x}} = {b}$ (with $x \\neq 0$).",
                f"Multiply both sides by $x$: ${a} = {b} x$.",
                f"Divide both sides by ${b}$: $x = \\dfrac{{{a}}}{{{b}}} = {x_val}$.",
            ]
            params = ("simple", a, b, x_val)

        else:
            # a/(x + c) = b, with x + c != 0
            while True:
                x_val = rng.randint(x_lo, x_hi)
                c = rng.randint(c_lo, c_hi)
                if x_val + c == 0:
                    continue
                b = rng.randint(b_lo, b_hi)
                if rng.random() < 0.5:
                    b = -b
                if b == 0:
                    continue
                a = b * (x_val + c)
                if a != 0:
                    break

            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            statement = f"Find all $x$: $\\dfrac{{{a}}}{{x {c_str}}} = {b}$."
            hints = [
                r"Multiply both sides by the denominator to clear the fraction.",
                f"You get ${a} = {b}(x {c_str})$.",
                r"Distribute, then solve for $x$.",
            ]
            steps = [
                f"Start with $\\dfrac{{{a}}}{{x {c_str}}} = {b}$ (with $x {c_str} \\neq 0$).",
                f"Multiply both sides by $x {c_str}$: ${a} = {b}(x {c_str})$.",
                f"Distribute: ${a} = {b}x + {b * c}$.",
                f"Subtract ${b * c}$ from both sides: ${a - b * c} = {b}x$.",
                f"Divide by ${b}$: $x = {x_val}$.",
            ]
            params = ("shifted", a, b, c, x_val)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x_val}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-algebraic-manipulation",
            ],
        )
