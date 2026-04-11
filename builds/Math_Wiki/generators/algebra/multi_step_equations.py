"""Multi-step equation generators (Phase 2c Wave 2).

Canonical topic slug ``multi_step_equations`` at
wiki/topics/algebra/Multi_Step_Equations.md (Algebra I Ch 2.2).

- multi_step_eq_two_step: solve ax + b = c
- multi_step_eq_distribution: solve a(x + b) = c
- multi_step_eq_variables_both_sides: solve ax + b = cx + d

Wave B extensions:
- solve_vars_both_sides_integer: ax + b = cx + d with clean integer x
- solve_vars_both_sides_with_distribution: a(x + b) = cx + d
- solve_vars_both_sides_word_problem: translated word problem
- solve_formula_for_other_variable: literal equations on standard formulas
- solve_formula_with_numeric_subst: literal rearrangement with substitution
- rearrange_simple_two_step_literal: symbolic ax + b = c for x
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")


# ---------------------------------------------------------------------------

@register
class MultiStepTwoStep(Generator):
    """Solve ax + b = c for clean integer x."""
    generator_id = "multi_step_eq_two_step"
    topic_slug = "multi_step_equations"
    display_name = "Solve ax + b = c"

    _RANGES = {"easy": (2, 10), "medium": (2, 20), "hard": (2, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        x_val = rng.randint(-hi, hi)
        b = rng.randint(-hi, hi)
        c = a * x_val + b  # guarantees clean integer x

        eq_latex = sp.latex(sp.Eq(a * x + b, c))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"First, isolate the $x$ term by moving the constant to the other side.",
                f"Subtract ${b}$ from both sides: ${a}x = {c - b}$.",
                f"Then divide both sides by ${a}$: $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Subtract ${b}$ from both sides: ${a}x = {c} - ({b}) = {c - b}$.",
                f"Divide both sides by ${a}$: $x = \\dfrac{{{c - b}}}{{{a}}} = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class MultiStepDistribution(Generator):
    """Solve a(x + b) = c by distributing then solving."""
    generator_id = "multi_step_eq_distribution"
    topic_slug = "multi_step_equations"
    display_name = "Solve a(x + b) = c"

    _A_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 20)}
    _X_RANGE = {"easy": (-10, 10), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        x_val = rng.randint(x_lo, x_hi)
        b = rng.randint(x_lo, x_hi)
        # a(x + b) = a*x_val + a*b = c when x = x_val
        c = a * (x_val + b)

        eq_latex = sp.latex(sp.Eq(a * (x + b), c))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"First, distribute the ${a}$ across the parentheses.",
                f"You get ${a}x + {a * b} = {c}$.",
                f"Now solve as a two-step equation: $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Distribute: ${a}x + ({a})({b}) = {c}$, which gives ${a}x + {a * b} = {c}$.",
                f"Subtract ${a * b}$ from both sides: ${a}x = {c - a * b}$.",
                f"Divide by ${a}$: $x = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class MultiStepVariablesBothSides(Generator):
    """Solve ax + b = cx + d (variables on both sides)."""
    generator_id = "multi_step_eq_variables_both_sides"
    topic_slug = "multi_step_equations"
    display_name = "Solve ax + b = cx + d"

    _COEF_RANGE = {"easy": (2, 9), "medium": (2, 15), "hard": (2, 25)}
    _CONST_RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        const_lo, const_hi = self._CONST_RANGE[difficulty]
        # Pick a, c different so (a - c) != 0
        while True:
            a = rng.randint(coef_lo, coef_hi)
            c = rng.randint(coef_lo, coef_hi)
            if a != c:
                break
        x_val = rng.randint(const_lo, const_hi)
        b = rng.randint(const_lo, const_hi)
        # d = a*x_val + b - c*x_val
        d = a * x_val + b - c * x_val

        eq_latex = sp.latex(sp.Eq(a * x + b, c * x + d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${eq_latex}$ for $x$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                r"When $x$ appears on both sides, get all $x$ terms to one side.",
                f"Subtract ${c}x$ from both sides to clear the right side: $({a - c})x + {b} = {d}$.",
                f"Then subtract ${b}$: $({a - c})x = {d - b}$. Divide by $({a - c})$: $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Subtract ${c}x$ from both sides: $({a - c})x + {b} = {d}$.",
                f"Subtract ${b}$ from both sides: $({a - c})x = {d - b}$.",
                f"Divide by $({a - c})$: $x = \\dfrac{{{d - b}}}{{{a - c}}} = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


# ============================================================================
# Wave B: equations_with_variables_on_both_sides
# ============================================================================

@register
class SolveVarsBothSidesInteger(Generator):
    """Solve ax + b = cx + d for integer x (topic variant for Wave B)."""
    generator_id = "solve_vars_both_sides_integer"
    topic_slug = "equations_with_variables_on_both_sides"
    display_name = "Determine x when variables appear on both sides"

    _A_RANGE = {"easy": (1, 5), "medium": (2, 9), "hard": (2, 14)}
    _X_RANGE = {"easy": (-10, 10), "medium": (-15, 15), "hard": (-25, 25)}
    _B_RANGE = {"easy": (-20, 20), "medium": (-30, 30), "hard": (-45, 45)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        while True:
            a = rng.randint(a_lo, a_hi)
            c = rng.randint(a_lo, a_hi)
            if difficulty == "hard":
                if rng.random() < 0.5:
                    a = -a
                if rng.random() < 0.5:
                    c = -c
            if a != c:
                break

        x_val = rng.randint(x_lo, x_hi)
        b = rng.randint(b_lo, b_hi)
        d = (a - c) * x_val + b

        eq_latex = sp.latex(sp.Eq(a * x + b, c * x + d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Determine $x$: ${eq_latex}$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                r"Collect the $x$-terms on one side and the constants on the other.",
                f"Subtract ${c}x$ from both sides to get $({a - c})x + {b} = {d}$.",
                f"Then subtract ${b}$ and divide by $({a - c})$ to find $x = {x_val}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Subtract ${c}x$ from both sides: $({a - c})x + {b} = {d}$.",
                f"Subtract ${b}$ from both sides: $({a - c})x = {d - b}$.",
                f"Divide both sides by $({a - c})$: $x = \\dfrac{{{d - b}}}{{{a - c}}} = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class SolveVarsBothSidesWithDistribution(Generator):
    """Solve a(x + b) = cx + d by distributing then collecting like terms."""
    generator_id = "solve_vars_both_sides_with_distribution"
    topic_slug = "equations_with_variables_on_both_sides"
    display_name = "Determine x after distributing across parentheses"

    _A_RANGE = {"easy": (2, 5), "medium": (2, 9), "hard": (2, 12)}
    _X_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}
    _B_RANGE = {"easy": (-8, 8), "medium": (-14, 14), "hard": (-22, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        while True:
            a = rng.randint(a_lo, a_hi)
            c = rng.randint(1, a_hi)
            if difficulty == "hard" and rng.random() < 0.4:
                c = -c
            if a != c:
                break

        x_val = rng.randint(x_lo, x_hi)
        b = rng.randint(b_lo, b_hi)
        # a(x_val + b) = a*x_val + a*b; rhs c*x_val + d must match: d = a*(x_val + b) - c*x_val
        d = a * (x_val + b) - c * x_val

        eq_latex = sp.latex(sp.Eq(a * (x + b), c * x + d))
        dist_lhs = sp.latex(sp.expand(a * (x + b)))
        after_coef = a - c
        # distribute value: a*b becomes new constant on LHS after distribution
        const_on_lhs = a * b

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Determine $x$: ${eq_latex}$.",
            answer_latex=f"$x = {x_val}$",
            hints=[
                f"Distribute the ${a}$ across the parentheses first.",
                f"After distributing, the equation becomes ${dist_lhs} = {c}x + {d}$.",
                r"Then move the $x$-terms to one side and the constants to the other.",
            ],
            solution_steps_latex=[
                f"Start with ${eq_latex}$.",
                f"Distribute ${a}$: ${dist_lhs} = {c}x + {d}$.",
                f"Subtract ${c}x$ from both sides: $({after_coef})x + {const_on_lhs} = {d}$.",
                f"Subtract ${const_on_lhs}$ from both sides: $({after_coef})x = {d - const_on_lhs}$.",
                f"Divide by $({after_coef})$: $x = \\dfrac{{{d - const_on_lhs}}}{{{after_coef}}} = {x_val}$.",
            ],
            tags=["#branch-algebra-1", "#topic-linear", "#skill-multi-step"],
        )


@register
class SolveVarsBothSidesWordProblem(Generator):
    """Word problem that translates to ax + b = cx + d."""
    generator_id = "solve_vars_both_sides_word_problem"
    topic_slug = "equations_with_variables_on_both_sides"
    display_name = "Translate a word problem with variables on both sides"
    supports_word_problems = True
    bank_count_per_difficulty = 25

    _SCENARIOS = [
        {
            "name": "Maya",
            "context": "community garden",
            "label_left": "weekly membership plus per-plot fee",
            "label_right": "flat seasonal rate plus smaller per-plot fee",
            "left_word": "weekly cost",
            "right_word": "seasonal cost",
            "quantity": "plots",
            "x_name": "number of plots",
        },
        {
            "name": "Kai",
            "context": "school newspaper",
            "label_left": "print plan: base fee plus per-page cost",
            "label_right": "digital plan: higher base fee plus lower per-page cost",
            "left_word": "print charge",
            "right_word": "digital charge",
            "quantity": "pages",
            "x_name": "number of pages",
        },
        {
            "name": "Priya",
            "context": "coffee shop",
            "label_left": "loyalty plan: startup fee plus per-drink cost",
            "label_right": "pay-as-you-go: no fee but higher per-drink cost",
            "left_word": "loyalty total",
            "right_word": "regular total",
            "quantity": "drinks",
            "x_name": "number of drinks",
        },
        {
            "name": "Rohan",
            "context": "tutoring center",
            "label_left": "monthly pass plus per-session fee",
            "label_right": "no pass but larger per-session fee",
            "left_word": "pass plan total",
            "right_word": "drop-in total",
            "quantity": "sessions",
            "x_name": "number of sessions",
        },
        {
            "name": "Zoe",
            "context": "maker space",
            "label_left": "member rate: flat fee plus per-hour cost",
            "label_right": "non-member rate: no flat fee but higher per-hour cost",
            "left_word": "member cost",
            "right_word": "non-member cost",
            "quantity": "hours",
            "x_name": "number of hours",
        },
    ]

    _A_RANGE = {"easy": (2, 6), "medium": (3, 10), "hard": (4, 15)}
    _X_RANGE = {"easy": (2, 12), "medium": (3, 18), "hard": (5, 25)}
    _B_RANGE = {"easy": (5, 30), "medium": (10, 60), "hard": (15, 100)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        scenario = rng.choice(self._SCENARIOS)
        x_val = rng.randint(x_lo, x_hi)

        # Plan A: flat fee b, per-unit rate a (higher flat, lower rate)
        # Plan B: flat fee d, per-unit rate c (lower flat, higher rate)
        a = rng.randint(a_lo, a_hi // 2 + 1)
        c = rng.randint(a + 1, a_hi + 2)
        b = rng.randint(b_lo, b_hi)
        # At x = x_val, both costs are equal: a*x_val + b = c*x_val + d
        d = a * x_val + b - c * x_val

        # Guard: require d >= 0 so the scenario reads cleanly
        while d < 0:
            b += 5
            d = a * x_val + b - c * x_val

        name = scenario["name"]
        ctx = scenario["context"]
        qty = scenario["quantity"]
        x_name = scenario["x_name"]

        statement = (
            f"{name} is comparing two plans at the {ctx}. "
            f"Plan A charges $\\${b}$ plus $\\${a}$ per {qty[:-1]}. "
            f"Plan B charges $\\${d}$ plus $\\${c}$ per {qty[:-1]}. "
            f"Determine the {x_name} for which the two plans cost the same."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (scenario["name"], a, b, c, d)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${x_val}$ {qty}",
            hints=[
                f"Let $x$ be the {x_name}. Write an expression for each plan's total cost.",
                f"Plan A: ${a}x + {b}$. Plan B: ${c}x + {d}$.",
                r"Set the two expressions equal and solve for $x$.",
            ],
            solution_steps_latex=[
                f"Let $x$ = {x_name}.",
                f"Plan A costs ${a}x + {b}$ dollars; Plan B costs ${c}x + {d}$ dollars.",
                f"Set them equal: ${a}x + {b} = {c}x + {d}$.",
                f"Subtract ${a}x$ from both sides: ${b} = {c - a}x + {d}$.",
                f"Subtract ${d}$: ${b - d} = {c - a}x$.",
                f"Divide by $({c - a})$: $x = {x_val}$. The plans cost the same at ${x_val}$ {qty}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-multi-step",
                "#skill-translation",
                "#word-problem-support",
            ],
        )


# ============================================================================
# Wave B: literal_equations_and_formulas
# ============================================================================

@register
class SolveFormulaForOtherVariable(Generator):
    """Solve a standard formula for a different variable (literal equation)."""
    generator_id = "solve_formula_for_other_variable"
    topic_slug = "literal_equations_and_formulas"
    display_name = "Solve a formula for a named variable"
    bank_count_per_difficulty = 20

    # Each entry: (formula_latex, target_variable, answer_latex, description, hints, steps)
    _FORMULAS = [
        {
            "name": "rectangle_perimeter_l",
            "formula": "P = 2l + 2w",
            "target": "l",
            "answer": r"l = \dfrac{P - 2w}{2}",
            "hint_lead": r"$P$ is on one side; isolate the term containing $l$.",
            "steps": [
                r"Start with $P = 2l + 2w$.",
                r"Subtract $2w$ from both sides: $P - 2w = 2l$.",
                r"Divide both sides by $2$: $l = \dfrac{P - 2w}{2}$.",
            ],
        },
        {
            "name": "rectangle_perimeter_w",
            "formula": "P = 2l + 2w",
            "target": "w",
            "answer": r"w = \dfrac{P - 2l}{2}",
            "hint_lead": r"Subtract the $2l$ term and then divide by $2$.",
            "steps": [
                r"Start with $P = 2l + 2w$.",
                r"Subtract $2l$ from both sides: $P - 2l = 2w$.",
                r"Divide both sides by $2$: $w = \dfrac{P - 2l}{2}$.",
            ],
        },
        {
            "name": "triangle_area_b",
            "formula": r"A = \tfrac{1}{2} b h",
            "target": "b",
            "answer": r"b = \dfrac{2A}{h}",
            "hint_lead": r"Clear the fraction by multiplying both sides by $2$.",
            "steps": [
                r"Start with $A = \dfrac{1}{2} b h$.",
                r"Multiply both sides by $2$: $2A = bh$.",
                r"Divide both sides by $h$: $b = \dfrac{2A}{h}$.",
            ],
        },
        {
            "name": "triangle_area_h",
            "formula": r"A = \tfrac{1}{2} b h",
            "target": "h",
            "answer": r"h = \dfrac{2A}{b}",
            "hint_lead": r"Clear the fraction, then divide by the coefficient of $h$.",
            "steps": [
                r"Start with $A = \dfrac{1}{2} b h$.",
                r"Multiply both sides by $2$: $2A = bh$.",
                r"Divide both sides by $b$: $h = \dfrac{2A}{b}$.",
            ],
        },
        {
            "name": "circle_circumference_r",
            "formula": r"C = 2 \pi r",
            "target": "r",
            "answer": r"r = \dfrac{C}{2\pi}",
            "hint_lead": r"Divide both sides by $2\pi$ to isolate $r$.",
            "steps": [
                r"Start with $C = 2\pi r$.",
                r"Divide both sides by $2\pi$: $r = \dfrac{C}{2\pi}$.",
            ],
        },
        {
            "name": "distance_rate_time_r",
            "formula": "d = rt",
            "target": "r",
            "answer": r"r = \dfrac{d}{t}",
            "hint_lead": r"Divide both sides by $t$.",
            "steps": [
                r"Start with $d = rt$.",
                r"Divide both sides by $t$: $r = \dfrac{d}{t}$.",
            ],
        },
        {
            "name": "distance_rate_time_t",
            "formula": "d = rt",
            "target": "t",
            "answer": r"t = \dfrac{d}{r}",
            "hint_lead": r"Divide both sides by $r$.",
            "steps": [
                r"Start with $d = rt$.",
                r"Divide both sides by $r$: $t = \dfrac{d}{r}$.",
            ],
        },
        {
            "name": "interest_P",
            "formula": "I = Prt",
            "target": "P",
            "answer": r"P = \dfrac{I}{rt}",
            "hint_lead": r"Divide both sides by $rt$.",
            "steps": [
                r"Start with $I = Prt$.",
                r"Divide both sides by $rt$: $P = \dfrac{I}{rt}$.",
            ],
        },
        {
            "name": "interest_r",
            "formula": "I = Prt",
            "target": "r",
            "answer": r"r = \dfrac{I}{Pt}",
            "hint_lead": r"Divide both sides by $Pt$.",
            "steps": [
                r"Start with $I = Prt$.",
                r"Divide both sides by $Pt$: $r = \dfrac{I}{Pt}$.",
            ],
        },
        {
            "name": "temperature_C",
            "formula": r"F = \tfrac{9}{5} C + 32",
            "target": "C",
            "answer": r"C = \tfrac{5}{9} (F - 32)",
            "hint_lead": r"Subtract $32$ first, then multiply by $\tfrac{5}{9}$.",
            "steps": [
                r"Start with $F = \dfrac{9}{5}C + 32$.",
                r"Subtract $32$ from both sides: $F - 32 = \dfrac{9}{5}C$.",
                r"Multiply both sides by $\dfrac{5}{9}$: $C = \dfrac{5}{9}(F - 32)$.",
            ],
        },
        {
            "name": "linear_eq_y",
            "formula": "Ax + By = C",
            "target": "y",
            "answer": r"y = \dfrac{C - Ax}{B}",
            "hint_lead": r"Move the $Ax$ term, then divide by $B$.",
            "steps": [
                r"Start with $Ax + By = C$.",
                r"Subtract $Ax$ from both sides: $By = C - Ax$.",
                r"Divide both sides by $B$: $y = \dfrac{C - Ax}{B}$.",
            ],
        },
        {
            "name": "linear_eq_x",
            "formula": "Ax + By = C",
            "target": "x",
            "answer": r"x = \dfrac{C - By}{A}",
            "hint_lead": r"Move the $By$ term, then divide by $A$.",
            "steps": [
                r"Start with $Ax + By = C$.",
                r"Subtract $By$ from both sides: $Ax = C - By$.",
                r"Divide both sides by $A$: $x = \dfrac{C - By}{A}$.",
            ],
        },
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._FORMULAS))
        f = self._FORMULAS[idx]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (f["name"],)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${f['formula']}$ for ${f['target']}$.",
            answer_latex=f"${f['answer']}$",
            hints=[
                r"Treat every letter except the target variable as a constant.",
                f["hint_lead"],
                f"Your goal is to end with ${f['target']} = $ (something).",
            ],
            solution_steps_latex=f["steps"],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class SolveFormulaWithNumericSubst(Generator):
    """Rearrange a formula then substitute given numeric values."""
    generator_id = "solve_formula_with_numeric_subst"
    topic_slug = "literal_equations_and_formulas"
    display_name = "Rearrange and substitute into a formula"

    _RANGES = {
        "easy": {"P": (20, 60), "w": (3, 15), "t": (2, 10), "r": (2, 10), "b": (3, 12)},
        "medium": {"P": (30, 120), "w": (5, 25), "t": (3, 20), "r": (3, 15), "b": (4, 20)},
        "hard": {"P": (40, 200), "w": (5, 40), "t": (5, 30), "r": (5, 25), "b": (6, 30)},
    }

    _CASES = [
        "rectangle_l",
        "triangle_h",
        "distance_r",
        "distance_t",
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        case = rng.choice(self._CASES)

        if case == "rectangle_l":
            # P = 2l + 2w, given P and w, find l
            l_val = rng.randint(3, 25 if difficulty == "hard" else 15)
            w = rng.randint(*r["w"])
            P = 2 * l_val + 2 * w
            statement = (
                f"The perimeter of a rectangle is given by $P = 2l + 2w$. "
                f"If $P = {P}$ and $w = {w}$, determine $l$."
            )
            answer = f"$l = {l_val}$"
            hints = [
                r"Solve $P = 2l + 2w$ for $l$ first, then substitute the numbers.",
                f"Rearranged: $l = \\dfrac{{P - 2w}}{{2}}$.",
                f"Plug in $P = {P}$ and $w = {w}$.",
            ]
            steps = [
                r"Solve for $l$: $l = \dfrac{P - 2w}{2}$.",
                f"Substitute $P = {P}$ and $w = {w}$: $l = \\dfrac{{{P} - 2({w})}}{{2}}$.",
                f"Simplify: $l = \\dfrac{{{P - 2 * w}}}{{2}} = {l_val}$.",
            ]
            params = ("rect_l", P, w, l_val)

        elif case == "triangle_h":
            # A = (1/2) b h, given A and b, find h (choose h so A integer)
            b = rng.randint(*r["b"])
            h_val = rng.randint(3, 20)
            # ensure b*h is even
            if (b * h_val) % 2 == 1:
                h_val += 1
            A = (b * h_val) // 2
            statement = (
                f"The area of a triangle is $A = \\tfrac{{1}}{{2}} b h$. "
                f"If $A = {A}$ and $b = {b}$, determine $h$."
            )
            answer = f"$h = {h_val}$"
            hints = [
                r"Solve $A = \tfrac{1}{2} bh$ for $h$ first.",
                r"Clearing the fraction gives $2A = bh$, so $h = \dfrac{2A}{b}$.",
                f"Substitute $A = {A}$ and $b = {b}$.",
            ]
            steps = [
                r"Multiply both sides by $2$: $2A = bh$.",
                r"Divide by $b$: $h = \dfrac{2A}{b}$.",
                f"Substitute $A = {A}$, $b = {b}$: $h = \\dfrac{{2({A})}}{{{b}}} = \\dfrac{{{2 * A}}}{{{b}}} = {h_val}$.",
            ]
            params = ("tri_h", A, b, h_val)

        elif case == "distance_r":
            # d = r t, given d and t, find r
            r_val = rng.randint(*r["r"])
            t = rng.randint(*r["t"])
            d = r_val * t
            statement = (
                f"The distance formula is $d = rt$. "
                f"If $d = {d}$ and $t = {t}$, determine $r$."
            )
            answer = f"$r = {r_val}$"
            hints = [
                r"Solve $d = rt$ for $r$ first.",
                r"Dividing by $t$ gives $r = \dfrac{d}{t}$.",
                f"Substitute $d = {d}$ and $t = {t}$.",
            ]
            steps = [
                r"Divide both sides of $d = rt$ by $t$: $r = \dfrac{d}{t}$.",
                f"Substitute $d = {d}$ and $t = {t}$: $r = \\dfrac{{{d}}}{{{t}}} = {r_val}$.",
            ]
            params = ("dist_r", d, t, r_val)

        else:  # distance_t
            r_val = rng.randint(*r["r"])
            t = rng.randint(*r["t"])
            d = r_val * t
            statement = (
                f"The distance formula is $d = rt$. "
                f"If $d = {d}$ and $r = {r_val}$, determine $t$."
            )
            answer = f"$t = {t}$"
            hints = [
                r"Solve $d = rt$ for $t$ first.",
                r"Dividing by $r$ gives $t = \dfrac{d}{r}$.",
                f"Substitute $d = {d}$ and $r = {r_val}$.",
            ]
            steps = [
                r"Divide both sides of $d = rt$ by $r$: $t = \dfrac{d}{r}$.",
                f"Substitute $d = {d}$ and $r = {r_val}$: $t = \\dfrac{{{d}}}{{{r_val}}} = {t}$.",
            ]
            params = ("dist_t", d, r_val, t)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-formula-substitution",
                "#skill-algebraic-manipulation",
            ],
        )


@register
class RearrangeSimpleTwoStepLiteral(Generator):
    """Solve ax + b = c for x, treating a, b, c as symbols (literal two-step equation)."""
    generator_id = "rearrange_simple_two_step_literal"
    topic_slug = "literal_equations_and_formulas"
    display_name = "Solve a literal two-step equation for x"
    bank_count_per_difficulty = 8

    # Each case: equation latex, target variable, answer latex, description, steps
    _CASES = [
        {
            "eq": "ax + b = c",
            "target": "x",
            "answer": r"x = \dfrac{c - b}{a}",
            "steps": [
                r"Start with $ax + b = c$.",
                r"Subtract $b$ from both sides: $ax = c - b$.",
                r"Divide by $a$: $x = \dfrac{c - b}{a}$.",
            ],
        },
        {
            "eq": "mx - n = p",
            "target": "x",
            "answer": r"x = \dfrac{p + n}{m}",
            "steps": [
                r"Start with $mx - n = p$.",
                r"Add $n$ to both sides: $mx = p + n$.",
                r"Divide by $m$: $x = \dfrac{p + n}{m}$.",
            ],
        },
        {
            "eq": "py + q = r",
            "target": "y",
            "answer": r"y = \dfrac{r - q}{p}",
            "steps": [
                r"Start with $py + q = r$.",
                r"Subtract $q$ from both sides: $py = r - q$.",
                r"Divide by $p$: $y = \dfrac{r - q}{p}$.",
            ],
        },
        {
            "eq": r"\dfrac{x}{k} + h = j",
            "target": "x",
            "answer": r"x = k(j - h)",
            "steps": [
                r"Start with $\dfrac{x}{k} + h = j$.",
                r"Subtract $h$: $\dfrac{x}{k} = j - h$.",
                r"Multiply both sides by $k$: $x = k(j - h)$.",
            ],
        },
        {
            "eq": r"a(x - b) = c",
            "target": "x",
            "answer": r"x = \dfrac{c}{a} + b",
            "steps": [
                r"Start with $a(x - b) = c$.",
                r"Divide both sides by $a$: $x - b = \dfrac{c}{a}$.",
                r"Add $b$: $x = \dfrac{c}{a} + b$.",
            ],
        },
        {
            "eq": r"a(x + b) = c",
            "target": "x",
            "answer": r"x = \dfrac{c}{a} - b",
            "steps": [
                r"Start with $a(x + b) = c$.",
                r"Divide both sides by $a$: $x + b = \dfrac{c}{a}$.",
                r"Subtract $b$: $x = \dfrac{c}{a} - b$.",
            ],
        },
        {
            "eq": r"\dfrac{x - p}{q} = s",
            "target": "x",
            "answer": r"x = qs + p",
            "steps": [
                r"Start with $\dfrac{x - p}{q} = s$.",
                r"Multiply both sides by $q$: $x - p = qs$.",
                r"Add $p$: $x = qs + p$.",
            ],
        },
        {
            "eq": r"k - mx = n",
            "target": "x",
            "answer": r"x = \dfrac{k - n}{m}",
            "steps": [
                r"Start with $k - mx = n$.",
                r"Subtract $k$: $-mx = n - k$.",
                r"Divide by $-m$: $x = \dfrac{k - n}{m}$.",
            ],
        },
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._CASES))
        case = self._CASES[idx]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx, case["target"])),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve ${case['eq']}$ for ${case['target']}$. "
                "Treat the other letters as constants."
            ),
            answer_latex=f"${case['answer']}$",
            hints=[
                r"Every letter except the target variable is treated as a constant.",
                r"Undo the operations around the target variable in reverse order.",
                f"Isolate ${case['target']}$ and simplify the result.",
            ],
            solution_steps_latex=case["steps"],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-algebraic-manipulation",
            ],
        )
