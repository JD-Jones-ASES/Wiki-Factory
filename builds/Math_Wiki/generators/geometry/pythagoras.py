"""Pythagorean theorem generators (Phase 2c Wave 1).

Canonical topic slug ``the_pythagorean_theorem`` at
wiki/topics/pre_algebra/The_Pythagorean_Theorem.md (Math II Ch 7).

- find_hypotenuse: given legs a, b, find c. Uses Pythagorean triples for
  clean integer answers on easy/medium; allows sqrt on hard.
- find_leg: given hypotenuse and one leg, find the other.
- check_right_triangle: given three sides, is it a right triangle?
"""
from __future__ import annotations

import math
import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Pythagorean triples keyed by c (hypotenuse). Good source of clean integer answers.
_TRIPLES: list[tuple[int, int, int]] = [
    (3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17),
    (9, 12, 15), (9, 40, 41), (10, 24, 26), (11, 60, 61), (12, 16, 20),
    (12, 35, 37), (13, 84, 85), (14, 48, 50), (15, 20, 25), (15, 36, 39),
    (16, 30, 34), (18, 24, 30), (20, 21, 29), (20, 48, 52), (21, 28, 35),
    (24, 32, 40), (27, 36, 45), (30, 40, 50), (33, 44, 55),
]

_TRIPLES_BY_DIFFICULTY = {
    "easy": [(a, b, c) for (a, b, c) in _TRIPLES if c <= 20],
    "medium": [(a, b, c) for (a, b, c) in _TRIPLES if 10 <= c <= 40],
    "hard": [(a, b, c) for (a, b, c) in _TRIPLES if c > 20],
}


# ---------------------------------------------------------------------------

@register
class PythagorasFindHypotenuse(Generator):
    """Given legs a and b, find hypotenuse c (from a Pythagorean triple)."""
    generator_id = "pythagoras_find_hypotenuse"
    topic_slug = "the_pythagorean_theorem"
    display_name = "Find hypotenuse given legs"
    bank_count_per_difficulty = 25  # small triple pool

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = _TRIPLES_BY_DIFFICULTY[difficulty]
        a, b, c = rng.choice(triples)
        # Occasionally swap a and b
        if rng.random() < 0.5:
            a, b = b, a

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A right triangle has legs of length ${a}$ and ${b}$. "
                "Find the length of the hypotenuse."
            ),
            answer_latex=f"$c = {c}$",
            hints=[
                r"The Pythagorean theorem: $a^2 + b^2 = c^2$.",
                f"Compute $a^2 + b^2 = {a}^2 + {b}^2 = {a * a} + {b * b} = {a * a + b * b}$.",
                f"Take the square root: $c = \\sqrt{{{a * a + b * b}}} = {c}$.",
            ],
            solution_steps_latex=[
                r"Apply the Pythagorean theorem: $a^2 + b^2 = c^2$.",
                f"Substitute the legs: ${a}^2 + {b}^2 = c^2$.",
                f"Compute: ${a * a} + {b * b} = c^2$, so $c^2 = {a * a + b * b}$.",
                f"Take the positive square root: $c = \\sqrt{{{a * a + b * b}}} = {c}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-right-triangles", "#skill-formula-substitution"],
        )


@register
class PythagorasFindLeg(Generator):
    """Given hypotenuse and one leg, find the other leg."""
    generator_id = "pythagoras_find_leg"
    topic_slug = "the_pythagorean_theorem"
    display_name = "Find a leg given hypotenuse and other leg"
    bank_count_per_difficulty = 25  # small triple pool

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triples = _TRIPLES_BY_DIFFICULTY[difficulty]
        a, b, c = rng.choice(triples)
        # Hide either a or b; student finds the hidden one
        if rng.random() < 0.5:
            known_leg, unknown_leg = a, b
            leg_name = "a"
        else:
            known_leg, unknown_leg = b, a
            leg_name = "b"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (known_leg, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A right triangle has hypotenuse of length ${c}$ and one leg of length ${known_leg}$. "
                "Find the length of the other leg."
            ),
            answer_latex=f"${leg_name} = {unknown_leg}$",
            hints=[
                r"The Pythagorean theorem: $a^2 + b^2 = c^2$.",
                f"Solve for the unknown leg: $b^2 = c^2 - a^2 = {c}^2 - {known_leg}^2 = {c * c} - {known_leg * known_leg} = {c * c - known_leg * known_leg}$.",
                f"Take the square root: $b = \\sqrt{{{c * c - known_leg * known_leg}}} = {unknown_leg}$.",
            ],
            solution_steps_latex=[
                r"Start with $a^2 + b^2 = c^2$.",
                f"Substitute what you know: ${known_leg}^2 + b^2 = {c}^2$.",
                f"Solve for $b^2$: $b^2 = {c * c} - {known_leg * known_leg} = {c * c - known_leg * known_leg}$.",
                f"Take the positive square root: $b = {unknown_leg}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-right-triangles", "#skill-algebraic-manipulation"],
        )


@register
class PythagorasCheckRightTriangle(Generator):
    """Given three side lengths, decide if they form a right triangle."""
    generator_id = "pythagoras_check_right_triangle"
    topic_slug = "the_pythagorean_theorem"
    display_name = "Is a triangle a right triangle?"
    bank_count_per_difficulty = 40

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # 50/50 right vs not-right
        is_right = rng.random() < 0.5
        if is_right:
            a, b, c = rng.choice(_TRIPLES_BY_DIFFICULTY[difficulty])
        else:
            # Perturb a triple so it's no longer right
            base = rng.choice(_TRIPLES_BY_DIFFICULTY[difficulty])
            offsets = [1, 2, 3, -1, -2, -3]
            while True:
                delta = rng.choice(offsets)
                a, b = base[0], base[1]
                c = base[2] + delta
                if c > max(a, b) and a * a + b * b != c * c:
                    break
        # Present sides as (a, b, c) where c is presented as "longest"
        sides = sorted([a, b, c])
        longest = sides[2]
        other = sides[0], sides[1]

        sum_squares_legs = other[0] ** 2 + other[1] ** 2
        square_longest = longest ** 2
        answer = "Yes, it is a right triangle." if sum_squares_legs == square_longest else "No, it is not a right triangle."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (sides[0], sides[1], sides[2])),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A triangle has sides of length ${sides[0]}$, ${sides[1]}$, and ${sides[2]}$. "
                "Is it a right triangle?"
            ),
            answer_latex=answer,
            hints=[
                r"A triangle is a right triangle if and only if the squares of the two shorter sides sum to the square of the longest side: $a^2 + b^2 = c^2$.",
                f"The longest side is ${longest}$, so check: ${other[0]}^2 + {other[1]}^2 \\stackrel{{?}}{{=}} {longest}^2$.",
                f"Compute: ${other[0] ** 2} + {other[1] ** 2} = {sum_squares_legs}$ and ${longest ** 2}$.",
            ],
            solution_steps_latex=[
                f"Identify the longest side (the hypotenuse candidate): ${longest}$.",
                f"Compute the sum of squares of the other two sides: ${other[0]}^2 + {other[1]}^2 = {other[0] ** 2} + {other[1] ** 2} = {sum_squares_legs}$.",
                f"Compute the square of the longest side: ${longest}^2 = {square_longest}$.",
                f"Compare: $ {sum_squares_legs} {'=' if sum_squares_legs == square_longest else '\\ne'} {square_longest}$, so {answer.lower()}",
            ],
            tags=["#branch-pre-algebra", "#topic-right-triangles", "#skill-procedural-calculation"],
        )
