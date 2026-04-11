"""Word-to-algebra translation generators.

Canonical topic slug ``translating_words_to_algebraic_expressions`` at
wiki/topics/pre_algebra/Translating_Words_To_Algebraic_Expressions.md.

Generators (backward construction: pick the target expression first, then
generate the English phrasing):

- translate_basic_operation        --- single-operation phrase -> expression
- translate_multi_step             --- two-operation phrase -> expression
- translate_word_problem_to_equation --- full scenario -> equation (not solved)
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


_TAGS_BASE = [
    "#branch-pre-algebra",
    "#topic-linear",
    "#skill-translation",
    "#word-problem-support",
]


def _tags(difficulty: Difficulty) -> list[str]:
    return [*_TAGS_BASE, f"#difficulty-{difficulty}"]


def _coef_with_var(coef: int, var: str) -> str:
    if coef == 1:
        return var
    if coef == -1:
        return f"-{var}"
    return f"{coef}{var}"


# ---------------------------------------------------------------------------
# Generator 1: translate a single-operation phrase
# ---------------------------------------------------------------------------


@register
class TranslateBasicOperation(Generator):
    """Translate a phrase with one operation into an algebraic expression.

    Parameter space is small (a dozen templates x a handful of numbers),
    so we cap bank_count_per_difficulty at 25.
    """

    generator_id = "translate_basic_operation"
    topic_slug = "translating_words_to_algebraic_expressions"
    display_name = "Translate a basic operation phrase"

    supports_word_problems = True
    bank_count_per_difficulty = 25

    _RANGES = {
        "easy":   (2, 9),
        "medium": (2, 15),
        "hard":   (2, 25),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        k = rng.randint(lo, hi)

        # 10 templates rotated by id. We include the template id in the
        # params tuple to get plenty of unique problems per difficulty.
        template = rng.randrange(10)

        if template == 0:
            phrase = f"the sum of a number $x$ and {k}"
            answer = f"x + {k}"
            note = r"'The sum of A and B' becomes $A + B$."
        elif template == 1:
            phrase = f"the difference of a number $x$ and {k}"
            answer = f"x - {k}"
            note = r"'The difference of A and B' becomes $A - B$ (first minus second)."
        elif template == 2:
            phrase = f"the product of {k} and a number $x$"
            answer = _coef_with_var(k, "x")
            note = r"'The product of A and B' becomes $A \cdot B$."
        elif template == 3:
            phrase = f"the quotient of a number $x$ and {k}"
            answer = f"\\dfrac{{x}}{{{k}}}"
            note = r"'The quotient of A and B' becomes $\dfrac{A}{B}$."
        elif template == 4:
            phrase = "twice a number $x$"
            answer = "2x"
            note = r"'Twice a number' means multiplied by $2$."
        elif template == 5:
            phrase = "half of a number $x$"
            answer = r"\dfrac{x}{2}"
            note = r"'Half of $x$' is $\dfrac{x}{2}$ (or equivalently $\dfrac{1}{2}x$)."
        elif template == 6:
            phrase = f"{k} more than a number $x$"
            answer = f"x + {k}"
            note = r"'K more than x' is $x + K$; 'more than' adds to whatever follows."
        elif template == 7:
            phrase = f"{k} less than a number $x$"
            answer = f"x - {k}"
            note = r"**Order matters:** 'K less than x' is $x - K$, not $K - x$."
        elif template == 8:
            phrase = f"a number $x$ increased by {k}"
            answer = f"x + {k}"
            note = r"'Increased by K' means add $K$."
        else:  # template == 9
            phrase = f"a number $x$ decreased by {k}"
            answer = f"x - {k}"
            note = r"'Decreased by K' means subtract $K$."

        opener = rng.choice([
            "Write an algebraic expression for",
            "Translate into algebra",
            "Express in symbols",
        ])
        statement = f"{opener}: {phrase}."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (template, k),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer}$",
            hints=[
                note,
                r"Identify the operation word (sum, difference, product, quotient, more, less, twice, half) and the numbers involved.",
                f"Write it in symbols: ${answer}$.",
            ],
            solution_steps_latex=[
                f"Read the phrase: {phrase}.",
                note,
                f"Convert directly to symbols: ${answer}$.",
            ],
            tags=_tags(difficulty),
        )


# ---------------------------------------------------------------------------
# Generator 2: translate a multi-step phrase
# ---------------------------------------------------------------------------


@register
class TranslateMultiStep(Generator):
    """Translate a two-operation phrase into an algebraic expression.

    Backward: pick the target expression (coefficient and constant), then
    generate English phrasing.
    """

    generator_id = "translate_multi_step"
    topic_slug = "translating_words_to_algebraic_expressions"
    display_name = "Translate a multi-step phrase"

    supports_word_problems = True
    bank_count_per_difficulty = 25

    _RANGES = {
        "easy":   {"k": (2, 9),  "j": (2, 9)},
        "medium": {"k": (2, 15), "j": (2, 15)},
        "hard":   {"k": (2, 20), "j": (2, 25)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        k = rng.randint(*r["k"])
        j = rng.randint(*r["j"])
        template = rng.randrange(8)

        if template == 0:
            # "J more than the product of K and x" -> Kx + J
            phrase = f"{j} more than the product of {k} and a number $x$"
            answer = f"{k}x + {j}"
            note = r"'J more than Kx' is $Kx + J$."
        elif template == 1:
            # "J less than the product of K and x" -> Kx - J
            phrase = f"{j} less than the product of {k} and a number $x$"
            answer = f"{k}x - {j}"
            note = r"**Watch the order:** 'J less than Kx' is $Kx - J$, not $J - Kx$."
        elif template == 2:
            # "The product of K and x, plus J" -> Kx + J
            phrase = f"the product of {k} and a number $x$, plus {j}"
            answer = f"{k}x + {j}"
            note = r"Multiplication comes first, then the addition."
        elif template == 3:
            # "Twice a number x, minus J" -> 2x - J
            phrase = f"twice a number $x$, minus {j}"
            answer = f"2x - {j}"
            note = r"Double the number, then subtract."
        elif template == 4:
            # "K times the sum of x and J" -> K(x + J)
            phrase = f"{k} times the sum of a number $x$ and {j}"
            answer = f"{k}(x + {j})"
            note = r"The 'sum of $x$ and $J$' is inside parentheses because it's multiplied as a whole."
        elif template == 5:
            # "K times the difference of x and J" -> K(x - J)
            phrase = f"{k} times the difference of a number $x$ and {j}"
            answer = f"{k}(x - {j})"
            note = r"Keep 'the difference of $x$ and $J$' grouped in parentheses."
        elif template == 6:
            # "The quotient of x + J and K" -> (x + J)/K
            phrase = f"the quotient of the sum of a number $x$ and {j}, and {k}"
            answer = f"\\dfrac{{x + {j}}}{{{k}}}"
            note = r"The whole sum is divided by $K$, so keep the numerator grouped."
        else:  # template == 7
            # "J less than twice a number x" -> 2x - J
            phrase = f"{j} less than twice a number $x$"
            answer = f"2x - {j}"
            note = r"First translate 'twice a number' as $2x$, then 'J less than' subtracts $J$: $2x - J$."

        opener = rng.choice([
            "Write an algebraic expression for",
            "Translate into algebra",
            "Express in symbols",
        ])
        statement = f"{opener}: {phrase}."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (template, k, j),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer}$",
            hints=[
                note,
                r"Build the expression one operation at a time. When a phrase names a 'sum' or 'difference', group it in parentheses if another operation is applied to the whole thing.",
                f"Putting it together: ${answer}$.",
            ],
            solution_steps_latex=[
                f"Read the phrase: {phrase}.",
                note,
                f"Assemble the pieces: ${answer}$.",
            ],
            tags=_tags(difficulty),
        )


# ---------------------------------------------------------------------------
# Generator 3: translate a word problem scenario into an equation
# ---------------------------------------------------------------------------


# (actor, item, add_gerund, remove_gerund)
# add_gerund = verb phrase for adding more items ("buying", "collecting", ...)
# remove_gerund = verb phrase for removing items ("giving away", "using", ...)
_WORD_PROBLEM_CONTEXTS = (
    ("Maya", "candies", "buying", "giving away"),
    ("Kai", "baseball cards", "collecting", "trading away"),
    ("Priya", "library books", "borrowing", "returning"),
    ("Rohan", "garden plants", "adding", "transplanting away"),
    ("Zoe", "photographs", "printing", "deleting"),
    ("Emilia", "sheet music pages", "writing", "removing"),
    ("the math club", "pencils", "receiving", "using"),
    ("the photography class", "memory cards", "ordering", "distributing"),
    ("the jazz band", "songbooks", "receiving", "sharing out"),
)


@register
class TranslateWordProblemToEquation(Generator):
    """Translate a word scenario into an equation in x (do not solve).

    Backward: pick the starting quantity x and the change a, plus the
    final total b = x + a (or b = x - a). Write the scenario, answer
    is the equation.
    """

    generator_id = "translate_word_problem_to_equation"
    topic_slug = "translating_words_to_algebraic_expressions"
    display_name = "Translate a word problem to an equation"

    supports_word_problems = True

    _RANGES = {
        "easy":   {"x": (5, 25),  "a": (3, 20)},
        "medium": {"x": (8, 60),  "a": (5, 40)},
        "hard":   {"x": (10, 150), "a": (5, 90)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x = rng.randint(*r["x"])
        a = rng.randint(*r["a"])
        actor, item, add_gerund, remove_gerund = rng.choice(_WORD_PROBLEM_CONTEXTS)
        # Two templates:
        #   0: starts with x, adds a, ends at b. Equation: x + a = b
        #   1: starts with x, loses a, ends at b. Equation: x - a = b
        template = rng.randrange(2)

        actor_cap = actor[0].upper() + actor[1:]
        group = actor.startswith("the")

        # Keep the removal scenario plausible: ensure x > a.
        if template == 1 and x - a <= 0:
            template = 0

        if template == 0:
            b = x + a
            if group:
                phrase = (
                    f"{actor_cap} has some {item}. After {add_gerund} "
                    f"${a}$ more, there are ${b}$ {item} in total. "
                    f"Write an equation for the number $x$ the group started with."
                )
            else:
                phrase = (
                    f"{actor_cap} has some {item}. After {add_gerund} "
                    f"${a}$ more, {actor} has ${b}$ {item}. "
                    f"Write an equation for the number $x$ {actor} started with."
                )
            equation = f"x + {a} = {b}"
            note = r"Starting amount plus the change equals the final amount."
        else:
            b = x - a
            if group:
                phrase = (
                    f"{actor_cap} has some {item}. After {remove_gerund} "
                    f"${a}$ of them, there are ${b}$ {item} left. "
                    f"Write an equation for the number $x$ the group started with."
                )
            else:
                phrase = (
                    f"{actor_cap} has some {item}. After {remove_gerund} "
                    f"${a}$ of them, {actor} has ${b}$ {item} left. "
                    f"Write an equation for the number $x$ {actor} started with."
                )
            equation = f"x - {a} = {b}"
            note = r"Starting amount minus the change equals the final amount."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (template, x, a, actor),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=phrase,
            answer_latex=f"${equation}$",
            hints=[
                f"Let $x$ stand for the unknown starting number of {item}.",
                note,
                f"The equation is ${equation}$.",
            ],
            solution_steps_latex=[
                f"Define the variable: let $x$ be the starting number of {item}.",
                note,
                f"Writing the equation in symbols gives ${equation}$.",
            ],
            tags=_tags(difficulty),
        )
