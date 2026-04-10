"""Order of operations generators (Phase 2c Wave 3).

Canonical topic slug ``order_of_operations`` at
wiki/topics/pre_algebra/Order_Of_Operations.md (Math I Ch 1.2).

Generates arithmetic expressions and asks students to evaluate them
following PEMDAS (Parentheses, Exponents, Multiplication/Division,
Addition/Subtraction).

- order_of_ops_basic: 3-term expressions with +, -, *, /
- order_of_ops_with_exponents: includes exponents and parentheses
- order_of_ops_nested_parens: nested grouping symbols
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

@register
class OrderOfOpsBasic(Generator):
    """Evaluate expressions like 3 + 4 * 5 - 2 (no exponents, no parens)."""
    generator_id = "order_of_ops_basic"
    topic_slug = "order_of_operations"
    display_name = "Evaluate with +, -, *, / (PEMDAS)"

    _RANGES = {"easy": (1, 12), "medium": (1, 20), "hard": (1, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Pick a template and fill in numbers so the final answer is a clean integer.
        templates = {
            "easy": [
                "{a} + {b} * {c}",      # multiply first
                "{a} * {b} - {c}",
                "{a} + {b} - {c}",
                "{a} * {b} + {c}",
            ],
            "medium": [
                "{a} + {b} * {c} - {d}",
                "{a} * {b} - {c} + {d}",
                "{a} + {b} * {c} + {d}",
                "{a} * {b} * {c} - {d}",
            ],
            "hard": [
                "{a} + {b} * {c} - {d} * {e}",
                "{a} * {b} + {c} * {d} - {e}",
                "{a} * {b} - {c} + {d} * {e}",
            ],
        }
        template = rng.choice(templates[difficulty])

        params = {}
        for var in "abcde":
            if "{" + var + "}" in template:
                params[var] = rng.randint(lo, hi)

        expr_str = template.format(**params)
        sympy_expr = sp.sympify(expr_str)
        answer = int(sympy_expr)  # integer answer
        # Render with \cdot instead of * for nicer typesetting
        display = expr_str.replace("*", " \\cdot ")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(params.values()) + (template,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${display}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"Remember PEMDAS: **P**arentheses, **E**xponents, **M**ultiplication/**D**ivision (left to right), **A**ddition/**S**ubtraction (left to right).",
                "Do all multiplication and division first (left to right), then all addition and subtraction.",
                f"The answer is ${answer}$.",
            ],
            solution_steps_latex=[
                f"Start with ${display}$.",
                "Handle all multiplication and division before addition and subtraction.",
                f"Working left to right on each level gives ${answer}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


@register
class OrderOfOpsWithExponents(Generator):
    """Evaluate expressions that include exponents and parentheses."""
    generator_id = "order_of_ops_with_exponents"
    topic_slug = "order_of_operations"
    display_name = "Evaluate with parentheses and exponents"

    _RANGES = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 10)}
    _EXP_RANGES = {"easy": (2, 2), "medium": (2, 3), "hard": (2, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        e_lo, e_hi = self._EXP_RANGES[difficulty]

        templates = [
            "({a} + {b})**{e} - {c}",
            "{a}**{e} + {b} * {c}",
            "({a} - {b})**{e} + {c}",
            "{a} * ({b} + {c})**{e}",
            "{a}**{e} - ({b} + {c})",
        ]
        template = rng.choice(templates)
        params = {
            "a": rng.randint(lo, hi),
            "b": rng.randint(lo, hi),
            "c": rng.randint(lo, hi),
            "e": rng.randint(e_lo, e_hi),
        }
        expr_str = template.format(**params)
        sympy_expr = sp.sympify(expr_str)
        answer = int(sympy_expr)
        display = expr_str.replace("*", " \\cdot ").replace("\\cdot \\cdot", "^")
        # Handle the exponent operator ** after the cdot replacement
        display = display.replace(" \\cdot  \\cdot ", "^")
        # Clean up: exponents render best as sympy does
        display = sp.latex(sympy_expr) if "(" not in expr_str else expr_str
        # Better: build LaTeX manually
        latex_str = (
            template
            .replace("**", "^")
            .replace("*", " \\cdot ")
            .format(**params)
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(params.values()) + (template,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${latex_str}$.",
            answer_latex=f"${answer}$",
            hints=[
                r"PEMDAS order: **P**arentheses first, then **E**xponents, then **M**/ **D**, then **A**/ **S**.",
                "Evaluate the contents of any parentheses before applying exponents to them.",
                f"The answer is ${answer}$.",
            ],
            solution_steps_latex=[
                f"Start with ${latex_str}$.",
                "Evaluate each parenthesised group first, then apply the exponent.",
                "Finally do multiplication, then addition/subtraction.",
                f"Simplify to ${answer}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-multi-step"],
        )


@register
class OrderOfOpsNestedParens(Generator):
    """Evaluate expressions with nested parentheses (hardest variant)."""
    generator_id = "order_of_ops_nested_parens"
    topic_slug = "order_of_operations"
    display_name = "Evaluate with nested parentheses"

    _RANGES = {"easy": (1, 6), "medium": (1, 10), "hard": (1, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        templates = [
            "{a} * ({b} + ({c} - {d}))",
            "({a} + {b}) * ({c} - {d})",
            "{a} + {b} * ({c} + {d})",
            "({a} * {b}) + ({c} * {d})",
            "{a} * ({b} - {c}) + {d}",
        ]
        template = rng.choice(templates)
        params = {v: rng.randint(lo, hi) for v in "abcd"}
        expr_str = template.format(**params)
        sympy_expr = sp.sympify(expr_str)
        answer = int(sympy_expr)
        latex_str = expr_str.replace("*", " \\cdot ")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(params.values()) + (template,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${latex_str}$.",
            answer_latex=f"${answer}$",
            hints=[
                "With nested grouping, work from the innermost parentheses outward.",
                "Evaluate the inside first, then the next level out.",
                f"After simplification you should get ${answer}$.",
            ],
            solution_steps_latex=[
                f"Start with ${latex_str}$.",
                "Innermost parentheses first, then work outward.",
                f"Simplify step by step to ${answer}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-multi-step"],
        )
