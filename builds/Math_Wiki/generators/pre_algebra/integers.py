"""Integer arithmetic generators (Phase 2c Wave 3).

Canonical topic slug ``adding_and_subtracting_integers`` at
wiki/topics/pre_algebra/Adding_And_Subtracting_Integers.md (Math I Ch 2.3).

- add_two_integers: a + b (with negatives)
- subtract_two_integers: a - b (with negatives)
- integer_sum_chain: a + b - c (three-term chain)
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


def _fmt_integer(n: int) -> str:
    """Format an integer, wrapping negatives in parentheses for clarity."""
    return f"({n})" if n < 0 else f"{n}"


# ---------------------------------------------------------------------------

@register
class AddTwoIntegers(Generator):
    """Add two signed integers."""
    generator_id = "add_two_integers"
    topic_slug = "adding_and_subtracting_integers"
    display_name = "Add two integers"

    _RANGES = {"easy": (-20, 20), "medium": (-50, 50), "hard": (-120, 120)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        result = a + b

        statement = f"${_fmt_integer(a)} + {_fmt_integer(b)}$"

        # Build solution text based on sign combination
        if a >= 0 and b >= 0:
            rule = "Both numbers are positive: add normally."
        elif a < 0 and b < 0:
            rule = r"Both numbers are negative: add their absolute values and keep the sign negative."
        else:
            rule = r"The signs are different: subtract the smaller absolute value from the larger, and keep the sign of the larger."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute {statement}.",
            answer_latex=f"${result}$",
            hints=[
                rule,
                f"$|{a}| = {abs(a)}$ and $|{b}| = {abs(b)}$.",
                f"The result is ${result}$.",
            ],
            solution_steps_latex=[
                f"Compute ${_fmt_integer(a)} + {_fmt_integer(b)}$.",
                rule,
                f"Final answer: ${result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


@register
class SubtractTwoIntegers(Generator):
    """Subtract two signed integers."""
    generator_id = "subtract_two_integers"
    topic_slug = "adding_and_subtracting_integers"
    display_name = "Subtract two integers"

    _RANGES = {"easy": (-20, 20), "medium": (-50, 50), "hard": (-120, 120)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        result = a - b

        statement = f"${_fmt_integer(a)} - {_fmt_integer(b)}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute {statement}.",
            answer_latex=f"${result}$",
            hints=[
                r"To subtract, change subtraction to addition of the opposite: $a - b = a + (-b)$.",
                f"Rewrite: ${a} + ({-b})$.",
                f"Now apply the integer addition rules. The answer is ${result}$.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                f"Subtract by adding the opposite: ${a} + ({-b})$.",
                f"Apply integer addition. The result is ${result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


@register
class IntegerSumChain(Generator):
    """Compute a + b - c (three-term chain with signed integers)."""
    generator_id = "integer_sum_chain"
    topic_slug = "adding_and_subtracting_integers"
    display_name = "Compute a + b - c (chain of integer operations)"

    _RANGES = {"easy": (-15, 15), "medium": (-40, 40), "hard": (-100, 100)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        # Randomize the middle operator for variety
        op1 = rng.choice(["+", "-"])
        op2 = rng.choice(["+", "-"])
        intermediate = a + b if op1 == "+" else a - b
        result = intermediate + c if op2 == "+" else intermediate - c

        statement = f"${_fmt_integer(a)} {op1} {_fmt_integer(b)} {op2} {_fmt_integer(c)}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, op1, b, op2, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute {statement}.",
            answer_latex=f"${result}$",
            hints=[
                "Work left to right when you only have addition and subtraction.",
                f"First compute ${_fmt_integer(a)} {op1} {_fmt_integer(b)} = {intermediate}$.",
                f"Then compute ${intermediate} {op2} {_fmt_integer(c)} = {result}$.",
            ],
            solution_steps_latex=[
                f"Start with ${statement}$.",
                f"Left to right: ${_fmt_integer(a)} {op1} {_fmt_integer(b)} = {intermediate}$.",
                f"Then: ${intermediate} {op2} {_fmt_integer(c)} = {result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-multi-step"],
        )
