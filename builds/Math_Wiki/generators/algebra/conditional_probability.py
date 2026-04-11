"""Conditional probability generators (Wave D algebra gap topics).

Canonical topic slug ``conditional_probability``.

- cond_prob_from_two_way_table: P(A|B) from a 2x2 category table.
- cond_prob_multiplication_rule: P(A and B) = P(A) * P(B|A).
- cond_prob_independence_check: compare P(A and B) to P(A) * P(B).
"""
from __future__ import annotations

import random
from fractions import Fraction
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


def _frac_latex(num: int, den: int) -> str:
    if den == 0:
        raise ValueError("zero denominator")
    g = gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den == 1:
        return f"{num}"
    return rf"\frac{{{num}}}{{{den}}}"


# Contexts for 2-way tables: (category row label, col label, yes_row, no_row, yes_col, no_col)
_TWO_WAY_CONTEXTS: tuple[dict, ...] = (
    {
        "scenario": (
            "Maya surveys her classmates about whether they watched the "
            "school play and whether they enjoyed it"
        ),
        "row": "Watched the play",
        "not_row": "Did not watch the play",
        "col": "Enjoyed the evening",
        "not_col": "Did not enjoy the evening",
    },
    {
        "scenario": (
            "Kai records whether each customer at a juice stand ordered a "
            "smoothie and whether they added a granola topping"
        ),
        "row": "Ordered a smoothie",
        "not_row": "Did not order a smoothie",
        "col": "Added granola",
        "not_col": "No granola",
    },
    {
        "scenario": (
            "Priya asks library visitors whether they borrowed a novel and "
            "whether they stayed past noon"
        ),
        "row": "Borrowed a novel",
        "not_row": "No novel borrowed",
        "col": "Stayed past noon",
        "not_col": "Left before noon",
    },
    {
        "scenario": (
            "Rohan tracks whether members of a hiking club brought a map "
            "and whether they finished the loop trail"
        ),
        "row": "Brought a map",
        "not_row": "No map",
        "col": "Finished the loop",
        "not_col": "Did not finish",
    },
    {
        "scenario": (
            "Zoe polls students about whether they took the early bus and "
            "whether they ate breakfast at school"
        ),
        "row": "Took the early bus",
        "not_row": "Did not take the early bus",
        "col": "Ate breakfast at school",
        "not_col": "Did not eat breakfast at school",
    },
    {
        "scenario": (
            "Mateo surveys gardeners about whether they watered daily and "
            "whether their tomato plants produced fruit"
        ),
        "row": "Watered daily",
        "not_row": "Did not water daily",
        "col": "Plants fruited",
        "not_col": "Plants did not fruit",
    },
    {
        "scenario": (
            "Leilani interviews beach joggers about whether they wore "
            "sunscreen and whether they finished their planned route"
        ),
        "row": "Wore sunscreen",
        "not_row": "No sunscreen",
        "col": "Finished the route",
        "not_col": "Stopped early",
    },
    {
        "scenario": (
            "Emilia collects data from a photography club about whether "
            "members used tripods and whether their photos turned out sharp"
        ),
        "row": "Used a tripod",
        "not_row": "No tripod",
        "col": "Sharp photos",
        "not_col": "Blurry photos",
    },
)


@register
class CondProbFromTwoWayTable(Generator):
    """Compute P(A|B) from a 2x2 category table.

    Backward construction: pick the probability (a/b) first, then generate
    row/column counts that produce exactly those numerator/denominator values.
    """
    generator_id = "cond_prob_from_two_way_table"
    topic_slug = "conditional_probability"
    display_name = "Conditional probability from a two-way table"

    _A_RANGE = {"easy": (1, 6), "medium": (2, 10), "hard": (3, 15)}
    _B_RANGE = {"easy": (8, 15), "medium": (12, 25), "hard": (20, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_TWO_WAY_CONTEXTS)

        a_lo, a_hi = self._A_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        # Pick "given category" total (this will be the denominator of P(A|B)).
        given_total = rng.randint(b_lo, b_hi)
        # Pick the "both A and B" count strictly less than given_total.
        both = rng.randint(a_lo, min(a_hi, given_total - 1))

        # Build the rest of the table. We'll think of the "given" category as
        # one column, and compute the counts in the other column too.
        not_given_total = rng.randint(b_lo, b_hi)
        # How many of the "not given" rows are "yes for A"?
        yes_not_given = rng.randint(1, not_given_total - 1)

        # Convention: rows = A (yes_row / not_row), cols = B (yes_col / not_col).
        # given_total = yes_col total; yes_col = both + (not_row with yes_col)
        yes_col_yes_row = both
        yes_col_not_row = given_total - both
        not_col_yes_row = yes_not_given
        not_col_not_row = not_given_total - yes_not_given

        # Row totals
        row_yes_total = yes_col_yes_row + not_col_yes_row
        row_not_total = yes_col_not_row + not_col_not_row
        grand_total = row_yes_total + row_not_total

        prob_latex = _frac_latex(both, given_total)

        # Build a readable table as LaTeX array
        table = (
            r"\begin{array}{l|cc|c} "
            f"& \\text{{{ctx['col']}}} & \\text{{{ctx['not_col']}}} & "
            r"\text{Total} \\ \hline "
            f"\\text{{{ctx['row']}}} & {yes_col_yes_row} & {not_col_yes_row} & "
            f"{row_yes_total} \\\\ "
            f"\\text{{{ctx['not_row']}}} & {yes_col_not_row} & "
            f"{not_col_not_row} & {row_not_total} \\\\ \\hline "
            f"\\text{{Total}} & {given_total} & {not_given_total} & "
            f"{grand_total} "
            r"\end{array}"
        )

        # Compute simplified version for the answer
        # prob = both / given_total
        statement = (
            f"{ctx['scenario']}. The results are shown below. $${table}$$ "
            f"Given that a randomly chosen person is in the "
            f"\"{ctx['col']}\" group, what is the probability that the "
            f"person is also in the \"{ctx['row']}\" group?"
        )

        key = (ctx["row"][:10], both, given_total, not_given_total, yes_not_given)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$P = {prob_latex}$",
            hints=[
                (
                    r"Conditional probability: $P(A \mid B) = "
                    r"\dfrac{\text{count(A and B)}}{\text{count(B)}}$."
                ),
                (
                    f"Here $B$ is \"{ctx['col']}\" (total {given_total}) and "
                    f"$A \\cap B$ is the count in the row "
                    f"\"{ctx['row']}\" under that column ({both})."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The condition is that the person is in the "
                    f"\"{ctx['col']}\" column. That column has total "
                    f"{given_total} people."
                ),
                (
                    f"Of those {given_total}, the number who are also in the "
                    f"\"{ctx['row']}\" row is {both}."
                ),
                (
                    rf"$P(\text{{row}} \mid \text{{column}}) = "
                    rf"\dfrac{{{both}}}{{{given_total}}} = {prob_latex}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-probability",
                "#skill-procedural-calculation",
            ],
        )


# ---------------------------------------------------------------------------


_SEQUENTIAL_CONTEXTS: tuple[dict, ...] = (
    {
        "scenario": (
            "Maya reaches into a fruit crate holding 10 pieces of fruit, of "
            "which 4 are mangoes"
        ),
        "a_event": "the first piece drawn is a mango",
        "b_event": "the second piece drawn is also a mango",
        "p_a_num": 4, "p_a_den": 10,
        "p_b_given_a_num": 3, "p_b_given_a_den": 9,
    },
    {
        "scenario": (
            "Kai spins a wheel with 12 wedges, 5 of which are blue, then "
            "draws a card from a shuffled 8-card deck containing 3 gold cards"
        ),
        "a_event": "the wheel lands on blue",
        "b_event": "the card drawn is gold",
        "p_a_num": 5, "p_a_den": 12,
        "p_b_given_a_num": 3, "p_b_given_a_den": 8,
    },
    {
        "scenario": (
            "Priya picks a marble from a jar of 15 marbles (6 red), then "
            "without replacing it picks a second marble"
        ),
        "a_event": "the first marble is red",
        "b_event": "the second marble is also red",
        "p_a_num": 6, "p_a_den": 15,
        "p_b_given_a_num": 5, "p_b_given_a_den": 14,
    },
    {
        "scenario": (
            "Rohan chooses a book from a shelf of 20 books (8 are "
            "biographies), then without replacing it picks a second book"
        ),
        "a_event": "the first book is a biography",
        "b_event": "the second book is also a biography",
        "p_a_num": 8, "p_a_den": 20,
        "p_b_given_a_num": 7, "p_b_given_a_den": 19,
    },
    {
        "scenario": (
            "Zoe draws a tile from a bag of 9 alphabet tiles (3 vowels), "
            "then draws a second tile without replacement"
        ),
        "a_event": "the first tile is a vowel",
        "b_event": "the second tile is also a vowel",
        "p_a_num": 3, "p_a_den": 9,
        "p_b_given_a_num": 2, "p_b_given_a_den": 8,
    },
    {
        "scenario": (
            "Mateo rolls a fair 6-sided die and then flips a coin weighted "
            "so that heads comes up with probability 2/5"
        ),
        "a_event": "the die shows a 4 or higher",
        "b_event": "the coin lands heads",
        "p_a_num": 3, "p_a_den": 6,
        "p_b_given_a_num": 2, "p_b_given_a_den": 5,
    },
    {
        "scenario": (
            "Leilani picks a shell from a bucket of 16 shells (4 are "
            "spiral), then picks a second shell without replacement"
        ),
        "a_event": "the first shell is a spiral",
        "b_event": "the second shell is also a spiral",
        "p_a_num": 4, "p_a_den": 16,
        "p_b_given_a_num": 3, "p_b_given_a_den": 15,
    },
    {
        "scenario": (
            "Emilia draws a lens from a case of 10 camera lenses (3 are "
            "wide-angle), then draws a second lens without replacement"
        ),
        "a_event": "the first lens is wide-angle",
        "b_event": "the second lens is also wide-angle",
        "p_a_num": 3, "p_a_den": 10,
        "p_b_given_a_num": 2, "p_b_given_a_den": 9,
    },
)


@register
class CondProbMultiplicationRule(Generator):
    """Use P(A and B) = P(A) * P(B|A) with clean fractions.

    Backward: each context ships with P(A) and P(B|A) as exact fractions,
    so the product simplifies to a clean answer.
    """
    generator_id = "cond_prob_multiplication_rule"
    topic_slug = "conditional_probability"
    display_name = "Multiplication rule for conditional probability"
    bank_count_per_difficulty = 8

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_SEQUENTIAL_CONTEXTS)

        p_a = Fraction(ctx["p_a_num"], ctx["p_a_den"])
        p_b_given_a = Fraction(ctx["p_b_given_a_num"], ctx["p_b_given_a_den"])
        p_and = p_a * p_b_given_a

        p_a_latex = _frac_latex(ctx["p_a_num"], ctx["p_a_den"])
        p_b_given_a_latex = _frac_latex(
            ctx["p_b_given_a_num"], ctx["p_b_given_a_den"]
        )
        p_and_latex = _frac_latex(p_and.numerator, p_and.denominator)

        statement = (
            f"{ctx['scenario']}. Let $A$ be the event that {ctx['a_event']}, "
            f"and let $B$ be the event that {ctx['b_event']}. "
            f"Given $P(A) = {p_a_latex}$ and $P(B \\mid A) = "
            f"{p_b_given_a_latex}$, find $P(A \\text{{ and }} B)$."
        )

        key = (
            ctx["a_event"][:10],
            ctx["p_a_num"],
            ctx["p_a_den"],
            ctx["p_b_given_a_num"],
            ctx["p_b_given_a_den"],
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$P(A \\text{{ and }} B) = {p_and_latex}$",
            hints=[
                (
                    r"Multiplication rule: $P(A \text{ and } B) = "
                    r"P(A) \cdot P(B \mid A)$."
                ),
                (
                    f"Substitute $P(A) = {p_a_latex}$ and "
                    f"$P(B \\mid A) = {p_b_given_a_latex}$."
                ),
            ],
            solution_steps_latex=[
                r"Apply the formula $P(A \text{ and } B) = P(A) \cdot P(B \mid A)$.",
                (
                    rf"Substitute: $P(A \text{{ and }} B) = {p_a_latex} \cdot "
                    rf"{p_b_given_a_latex}$."
                ),
                (
                    rf"Multiply numerators and denominators: "
                    rf"$\dfrac{{{ctx['p_a_num'] * ctx['p_b_given_a_num']}}}{{"
                    rf"{ctx['p_a_den'] * ctx['p_b_given_a_den']}}}$."
                ),
                f"Simplify to get $P(A \\text{{ and }} B) = {p_and_latex}$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-probability",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------


# Independence check cases: each ships with P(A), P(B), P(A and B).
# Some are independent (P(A and B) == P(A)*P(B)) and some are not.
_INDEPENDENCE_CASES: tuple[dict, ...] = (
    # Independent cases: product equals P(A and B)
    {
        "scenario": (
            "Maya rolls a fair number cube and independently spins a 4-color "
            "wheel"
        ),
        "a_name": "rolling an even number", "b_name": "spinning red",
        "p_a_num": 1, "p_a_den": 2,
        "p_b_num": 1, "p_b_den": 4,
        "p_and_num": 1, "p_and_den": 8,
    },
    {
        "scenario": (
            "Kai flips a fair coin and independently draws a card from a "
            "shuffled deck of 10 cards (3 are aces)"
        ),
        "a_name": "the coin lands heads", "b_name": "the card is an ace",
        "p_a_num": 1, "p_a_den": 2,
        "p_b_num": 3, "p_b_den": 10,
        "p_and_num": 3, "p_and_den": 20,
    },
    {
        "scenario": (
            "Priya picks a marble from bag X (3 of 12 are blue), then "
            "independently picks a marble from bag Y (2 of 5 are blue)"
        ),
        "a_name": "bag X produces blue", "b_name": "bag Y produces blue",
        "p_a_num": 3, "p_a_den": 12,
        "p_b_num": 2, "p_b_den": 5,
        "p_and_num": 1, "p_and_den": 10,
    },
    {
        "scenario": (
            "Rohan spins a spinner split in thirds (2 green, 1 yellow) and "
            "independently rolls a fair 6-sided die"
        ),
        "a_name": "the spinner shows green", "b_name": "the die shows a 1",
        "p_a_num": 2, "p_a_den": 3,
        "p_b_num": 1, "p_b_den": 6,
        "p_and_num": 1, "p_and_den": 9,
    },
    # Dependent cases: product does NOT equal P(A and B)
    {
        "scenario": (
            "Zoe draws two cards in a row from a small deck (without "
            "replacement)"
        ),
        "a_name": "the first card is red", "b_name": "the second card is red",
        "p_a_num": 1, "p_a_den": 2,
        "p_b_num": 1, "p_b_den": 2,
        "p_and_num": 2, "p_and_den": 9,  # ≠ 1/4
    },
    {
        "scenario": (
            "Mateo surveys students about whether they study daily and "
            "whether they play a musical instrument"
        ),
        "a_name": "a student studies daily", "b_name": "a student plays an instrument",
        "p_a_num": 3, "p_a_den": 5,
        "p_b_num": 2, "p_b_den": 5,
        "p_and_num": 1, "p_and_den": 4,  # 0.25 ≠ 0.24
    },
    {
        "scenario": (
            "Leilani tracks whether beachgoers brought a towel and whether "
            "they brought sunscreen"
        ),
        "a_name": "a person brought a towel", "b_name": "a person brought sunscreen",
        "p_a_num": 7, "p_a_den": 10,
        "p_b_num": 3, "p_b_den": 5,
        "p_and_num": 1, "p_and_den": 2,  # ≠ 21/50
    },
    {
        "scenario": (
            "Emilia studies weather data and finds both cloudy mornings and "
            "afternoon rain"
        ),
        "a_name": "a morning is cloudy", "b_name": "the afternoon has rain",
        "p_a_num": 2, "p_a_den": 5,
        "p_b_num": 1, "p_b_den": 4,
        "p_and_num": 1, "p_and_den": 8,  # ≠ 1/10
    },
)


@register
class CondProbIndependenceCheck(Generator):
    """Decide whether two events are independent.

    Given P(A), P(B), P(A and B), check if P(A and B) == P(A)*P(B).
    """
    generator_id = "cond_prob_independence_check"
    topic_slug = "conditional_probability"
    display_name = "Check if two events are independent"
    bank_count_per_difficulty = 8

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(_INDEPENDENCE_CASES)

        p_a = Fraction(case["p_a_num"], case["p_a_den"])
        p_b = Fraction(case["p_b_num"], case["p_b_den"])
        p_and = Fraction(case["p_and_num"], case["p_and_den"])

        product = p_a * p_b
        independent = (product == p_and)

        p_a_latex = _frac_latex(case["p_a_num"], case["p_a_den"])
        p_b_latex = _frac_latex(case["p_b_num"], case["p_b_den"])
        p_and_latex = _frac_latex(case["p_and_num"], case["p_and_den"])
        product_latex = _frac_latex(product.numerator, product.denominator)

        if independent:
            answer = "Yes, the events are independent."
            comparison = (
                f"$P(A) \\cdot P(B) = {p_a_latex} \\cdot {p_b_latex} = "
                f"{product_latex} = P(A \\text{{ and }} B)$, so the events "
                "are independent."
            )
        else:
            answer = "No, the events are not independent."
            comparison = (
                f"$P(A) \\cdot P(B) = {p_a_latex} \\cdot {p_b_latex} = "
                f"{product_latex}$, but $P(A \\text{{ and }} B) = "
                f"{p_and_latex}$. Since these are not equal, the events "
                "are not independent."
            )

        statement = (
            f"{case['scenario']}. Let $A$ be the event that "
            f"{case['a_name']}, and let $B$ be the event that "
            f"{case['b_name']}. Suppose $P(A) = {p_a_latex}$, "
            f"$P(B) = {p_b_latex}$, and $P(A \\text{{ and }} B) = "
            f"{p_and_latex}$. Are $A$ and $B$ independent? Answer yes or no."
        )

        key = (
            case["a_name"][:10],
            case["p_a_num"], case["p_a_den"],
            case["p_b_num"], case["p_b_den"],
            case["p_and_num"], case["p_and_den"],
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Two events $A$ and $B$ are independent exactly when "
                    r"$P(A \text{ and } B) = P(A) \cdot P(B)$."
                ),
                (
                    "Compute the product $P(A) \\cdot P(B)$ and compare it "
                    "to the given joint probability."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Compute $P(A) \cdot P(B) = {p_a_latex} \cdot "
                    rf"{p_b_latex} = {product_latex}$."
                ),
                (
                    rf"Compare with $P(A \text{{ and }} B) = {p_and_latex}$."
                ),
                comparison,
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-probability",
                "#skill-multi-step",
            ],
        )
