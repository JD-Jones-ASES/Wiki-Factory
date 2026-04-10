"""Algebraic intro generators (Cluster 1 Wave 3).

Two canonical topic slugs covered here:

- ``the_distributive_property`` at
  wiki/topics/pre_algebra/The_Distributive_Property.md

  Generators:
    * distribute_numerical                --- compute a(b + c) with positives
    * distribute_with_negative            --- a(b - c) or -a(b + c) with sign tracking
    * distribute_expression_with_variable --- distribute a(x + b) or a(bx + c)

- ``variables_and_algebraic_expressions`` at
  wiki/topics/pre_algebra/Variables_And_Algebraic_Expressions.md

  Generators:
    * identify_coefficient           --- pick out the coefficient of x (or y) in an expression
    * count_terms                    --- count how many terms are in an expression
    * translate_word_to_expression   --- convert English phrase into an algebraic expression

All generators use backward construction where applicable (pick clean
parameters, derive the expression) to guarantee well-formed problems and
correct answers.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Shared tag sets --- every generator in this module gets the same
# branch/topic tags plus a per-difficulty tag.
def _tags(difficulty: Difficulty) -> list[str]:
    return [
        "#branch-pre-algebra",
        "#topic-numbers-and-operations",
        f"#difficulty-{difficulty}",
    ]


def _fmt_signed(n: int) -> str:
    """Format a signed integer, wrapping negatives in parentheses."""
    return f"({n})" if n < 0 else f"{n}"


def _term_with_sign(coef: int, var: str) -> str:
    """Render a signed coefficient in front of a variable: '3x', '-x', 'x'."""
    if coef == 1:
        return var
    if coef == -1:
        return f"-{var}"
    return f"{coef}{var}"


def _join_signed(first: str, rest: list[tuple[int, str]]) -> str:
    """Join ``first`` with a list of (signed-coef, tail) terms, inserting +/-
    based on the sign of each coefficient. ``tail`` should already render the
    absolute value only (e.g. '4x' for +4x and for -4x alike).
    """
    out = [first]
    for coef, tail in rest:
        if coef >= 0:
            out.append(f" + {tail}")
        else:
            out.append(f" - {tail}")
    return "".join(out)


# ---------------------------------------------------------------------------
# Topic 1: the_distributive_property
# ---------------------------------------------------------------------------


@register
class DistributeNumerical(Generator):
    """Compute ``a(b + c)`` numerically with positive values.

    Shows both paths in the solution: the direct path $a \\cdot (b+c)$ and
    the distributive path $ab + ac$.
    """

    generator_id = "distribute_numerical"
    topic_slug = "the_distributive_property"
    display_name = "Apply the distributive property (numerical)"

    _RANGES = {
        "easy":   {"a": (2, 9),  "b": (1, 9),  "c": (1, 9)},
        "medium": {"a": (3, 12), "b": (2, 15), "c": (2, 15)},
        "hard":   {"a": (4, 15), "b": (3, 25), "c": (3, 25)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])
        inner_sum = b + c
        ab = a * b
        ac = a * c
        answer = a * inner_sum

        statement = f"Compute ${a}({b} + {c})$ using the distributive property."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer}$",
            hints=[
                r"The distributive property says $a(b + c) = a \cdot b + a \cdot c$.",
                f"Multiply: ${a} \\cdot {b} = {ab}$ and ${a} \\cdot {c} = {ac}$.",
                f"Add the two products: ${ab} + {ac} = {answer}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a}({b} + {c})$.",
                f"Direct path: add inside the parentheses first, ${b} + {c} = {inner_sum}$, then ${a} \\cdot {inner_sum} = {answer}$.",
                f"Distributive path: ${a} \\cdot {b} + {a} \\cdot {c} = {ab} + {ac} = {answer}$.",
                f"Both paths agree: the answer is ${answer}$.",
            ],
            tags=_tags(difficulty),
        )


@register
class DistributeWithNegative(Generator):
    """Compute ``a(b - c)`` or ``-a(b + c)`` --- distribution with a sign."""

    generator_id = "distribute_with_negative"
    topic_slug = "the_distributive_property"
    display_name = "Distribute across a signed expression"

    _RANGES = {
        "easy":   {"a": (2, 9),  "b": (1, 9),  "c": (1, 9)},
        "medium": {"a": (3, 12), "b": (2, 15), "c": (2, 15)},
        "hard":   {"a": (4, 15), "b": (3, 20), "c": (3, 20)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])

        # Four templates; each has a distinct sign configuration so two
        # identical (a, b, c) tuples with different templates still differ.
        #   0: a(b - c)     answer = a*b - a*c
        #   1: a(-b + c)    answer = -a*b + a*c
        #   2: -a(b + c)    answer = -a*b - a*c
        #   3: -a(b - c)    answer = -a*b + a*c
        template = rng.randrange(4)

        if template == 0:
            stmt = f"${a}({b} - {c})$"
            ab, ac = a * b, a * c
            answer = ab - ac
            steps = [
                f"Start with ${a}({b} - {c})$.",
                f"Direct path: inside the parentheses, ${b} - {c} = {b - c}$, so ${a} \\cdot ({b - c}) = {answer}$.",
                f"Distributive path: ${a} \\cdot {b} - {a} \\cdot {c} = {ab} - {ac} = {answer}$.",
                f"Both paths give ${answer}$.",
            ]
            rule = r"Apply $a(b - c) = a b - a c$. Keep the subtraction sign through the distribution."
        elif template == 1:
            stmt = f"${a}(-{b} + {c})$"
            ab, ac = a * b, a * c
            answer = -ab + ac
            steps = [
                f"Start with ${a}(-{b} + {c})$.",
                f"Direct path: inside the parentheses, $-{b} + {c} = {-b + c}$, so ${a} \\cdot ({-b + c}) = {answer}$.",
                f"Distributive path: ${a} \\cdot (-{b}) + {a} \\cdot {c} = -{ab} + {ac} = {answer}$.",
                f"Answer: ${answer}$.",
            ]
            rule = r"Distribute $a$ over each term. The sign of the term stays with it: $a(-b + c) = -ab + ac$."
        elif template == 2:
            stmt = f"$-{a}({b} + {c})$"
            ab, ac = a * b, a * c
            answer = -ab - ac
            steps = [
                f"Start with $-{a}({b} + {c})$.",
                f"Direct path: ${b} + {c} = {b + c}$, so $(-{a}) \\cdot ({b + c}) = {answer}$.",
                f"Distributive path: $(-{a}) \\cdot {b} + (-{a}) \\cdot {c} = -{ab} - {ac} = {answer}$.",
                f"Answer: ${answer}$.",
            ]
            rule = r"A negative outside distributes a negative onto every inside term: $-a(b + c) = -ab - ac$."
        else:  # template == 3
            stmt = f"$-{a}({b} - {c})$"
            ab, ac = a * b, a * c
            answer = -ab + ac
            steps = [
                f"Start with $-{a}({b} - {c})$.",
                f"Direct path: ${b} - {c} = {b - c}$, so $(-{a}) \\cdot ({b - c}) = {answer}$.",
                f"Distributive path: $(-{a}) \\cdot {b} + (-{a}) \\cdot (-{c}) = -{ab} + {ac} = {answer}$.",
                f"Watch the signs: negative times negative is positive. Answer: ${answer}$.",
            ]
            rule = r"Distribute $-a$ across each term, tracking signs: $-a(b - c) = -ab + ac$ (negative times negative is positive)."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (template, a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Compute {stmt} using the distributive property.",
            answer_latex=f"${answer}$",
            hints=[
                rule,
                r"Multiply the factor outside by each term inside, keeping each term's sign with it.",
                f"After simplifying you should get ${answer}$.",
            ],
            solution_steps_latex=steps,
            tags=_tags(difficulty),
        )


@register
class DistributeExpressionWithVariable(Generator):
    """Distribute ``a(x + b)`` or ``a(bx + c)``. Answer is a linear expression."""

    generator_id = "distribute_expression_with_variable"
    topic_slug = "the_distributive_property"
    display_name = "Distribute into an expression with x"

    _RANGES = {
        "easy":   {"a": (2, 8),  "b": (1, 9),  "c": (1, 9)},
        "medium": {"a": (2, 10), "b": (2, 12), "c": (2, 12)},
        "hard":   {"a": (3, 12), "b": (2, 15), "c": (2, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])
        # Randomly negate coefficients to get variety.
        sign_b = rng.choice([1, -1])
        sign_c = rng.choice([1, -1])
        has_inner_coef = rng.choice([False, True])  # if True: a(bx + c); else a(x + b)

        if not has_inner_coef:
            # Form: a(x + b)   (ignore c entirely)
            inner_coef = 1
            constant = sign_b * b
            # Problem statement rendering
            if constant >= 0:
                stmt_inner = f"x + {constant}"
            else:
                stmt_inner = f"x - {abs(constant)}"
            template_tag = 0
        else:
            # Form: a(bx + c) where bx coefficient is signed
            inner_coef = sign_b * b
            if inner_coef == 1:
                bx_str = "x"
            elif inner_coef == -1:
                bx_str = "-x"
            else:
                bx_str = f"{inner_coef}x"
            constant = sign_c * c
            if constant >= 0:
                stmt_inner = f"{bx_str} + {constant}"
            else:
                stmt_inner = f"{bx_str} - {abs(constant)}"
            template_tag = 1

        # Result: a * inner_coef * x + a * constant
        out_coef = a * inner_coef
        out_const = a * constant

        # Pretty answer assembly
        if out_coef == 1:
            ax_str = "x"
        elif out_coef == -1:
            ax_str = "-x"
        else:
            ax_str = f"{out_coef}x"

        if out_const == 0:
            answer_body = ax_str
        elif out_const > 0:
            answer_body = f"{ax_str} + {out_const}"
        else:
            answer_body = f"{ax_str} - {abs(out_const)}"

        statement = f"Distribute ${a}({stmt_inner})$."

        # Solution steps
        step_a_inner = f"${a} \\cdot ({'' if inner_coef == 1 else ('-' if inner_coef == -1 else str(inner_coef) + ' \\cdot ')}x) = {ax_str}$"
        # clean display for the inner constant product
        a_times_constant = f"${a} \\cdot ({constant}) = {out_const}$" if constant < 0 else f"${a} \\cdot {constant} = {out_const}$"

        steps = [
            f"Start with ${a}({stmt_inner})$.",
            r"Distribute $a$ to every term inside the parentheses.",
            f"First term: {step_a_inner}.",
            f"Second term: {a_times_constant}.",
            f"Combine: ${answer_body}$.",
        ]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (template_tag, a, inner_coef, constant),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_body}$",
            hints=[
                r"Use the distributive property: $a(bx + c) = a b x + a c$.",
                f"Multiply ${a}$ by the $x$-term and by the constant separately.",
                f"The simplified expression is ${answer_body}$.",
            ],
            solution_steps_latex=steps,
            tags=_tags(difficulty),
        )


# ---------------------------------------------------------------------------
# Topic 2: variables_and_algebraic_expressions
# ---------------------------------------------------------------------------


@register
class IdentifyCoefficient(Generator):
    """Given a multi-term expression, identify the coefficient of a target variable."""

    generator_id = "identify_coefficient"
    topic_slug = "variables_and_algebraic_expressions"
    display_name = "Identify the coefficient of a variable"

    _RANGES = {
        "easy":   (2, 9),
        "medium": (2, 15),
        "hard":   (2, 25),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]

        # Pick the target variable and a second variable (different letter).
        target = rng.choice(["x", "y"])
        other = "y" if target == "x" else "x"

        # Target coefficient: can be positive, negative, or implicit +/- 1.
        # Use a richer set of possible values so we get plenty of unique problems.
        coef_choices = list(range(-hi, 0)) + list(range(1, hi + 1))
        target_coef = rng.choice(coef_choices)

        # Other-variable coefficient (always nonzero so the term appears).
        other_coef = rng.choice([v for v in range(-hi, hi + 1) if v != 0])
        constant = rng.choice([v for v in range(-hi, hi + 1) if v != 0])

        # Ordering variants so problems aren't always written "target first".
        order = rng.randrange(3)
        target_term = _term_with_sign(target_coef, target)
        other_term = _term_with_sign(other_coef, other)

        # Build display string. We lead with the first term's value as-is
        # (including any leading minus) and then join the rest with +/-.
        if order == 0:
            first = target_term
            rest: list[tuple[int, str]] = [
                (other_coef, _term_with_sign(abs(other_coef), other)),
                (constant, f"{abs(constant)}"),
            ]
        elif order == 1:
            first = other_term
            rest = [
                (target_coef, _term_with_sign(abs(target_coef), target)),
                (constant, f"{abs(constant)}"),
            ]
        else:
            first = f"{constant}" if constant < 0 else f"{constant}"
            # If the constant is negative, normalise: drop the sign from the
            # printed first token and let the joiner add the "-".
            if constant < 0:
                first = f"-{abs(constant)}"
            rest = [
                (target_coef, _term_with_sign(abs(target_coef), target)),
                (other_coef, _term_with_sign(abs(other_coef), other)),
            ]

        expression = _join_signed(first, rest)

        statement = f"What is the coefficient of ${target}$ in the expression ${expression}$?"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (order, target, target_coef, other_coef, constant),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${target_coef}$",
            hints=[
                "The coefficient is the number multiplying the variable. For ${target}$, look for the ${target}$-term.".replace("{target}", target),
                f"If the term is written as just ${target}$, the coefficient is $1$; if it is $-{target}$, the coefficient is $-1$.",
                "Ignore the sign-free magnitude --- remember to include the sign.",
            ],
            solution_steps_latex=[
                f"Look at each term of ${expression}$.",
                f"The term that contains ${target}$ is ${_term_with_sign(target_coef, target)}$.",
                f"The coefficient (the number multiplying ${target}$) is ${target_coef}$.",
            ],
            tags=_tags(difficulty),
        )


@register
class CountTerms(Generator):
    """Given an expression, count how many terms it contains.

    This is a pure counting question: do NOT combine like terms. A term is
    a chunk separated by a top-level ``+`` or ``-``.
    """

    generator_id = "count_terms"
    topic_slug = "variables_and_algebraic_expressions"
    display_name = "Count the terms in an expression"

    _RANGES = {
        "easy":   {"terms": (2, 3), "coef": (1, 9)},
        "medium": {"terms": (3, 5), "coef": (1, 15)},
        "hard":   {"terms": (4, 6), "coef": (1, 20)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cfg = self._RANGES[difficulty]
        t_lo, t_hi = cfg["terms"]
        c_lo, c_hi = cfg["coef"]
        num_terms = rng.randint(t_lo, t_hi)

        # Build each term. A term is one of:
        #   - a*x (a*y, a*n) possibly signed
        #   - just x / -x (implicit coefficient +/-1)
        #   - a pure constant
        # At least one term should be a variable term; at least one should be
        # a constant most of the time.
        var_choices = ["x", "y", "n"]

        pieces: list[tuple[int, str]] = []  # (signed-coef, absolute-tail-string)
        # First term's sign is applied directly to the printed output.
        signs_picked: list[int] = []
        tails: list[str] = []

        for i in range(num_terms):
            kind = rng.randrange(3)  # 0 const, 1 var-with-coef, 2 implicit +/-1 var
            sign = rng.choice([1, -1])
            if kind == 0:
                mag = rng.randint(c_lo, c_hi)
                tails.append(f"{mag}")
                signs_picked.append(sign)
            elif kind == 1:
                mag = rng.randint(c_lo, c_hi)
                var = rng.choice(var_choices)
                if mag == 1:
                    tails.append(var)
                else:
                    tails.append(f"{mag}{var}")
                signs_picked.append(sign)
            else:
                var = rng.choice(var_choices)
                tails.append(var)
                signs_picked.append(sign)

        # Build the display string: leading sign attached to first term only
        # if negative, subsequent terms separated by " + " / " - ".
        first = tails[0] if signs_picked[0] == 1 else f"-{tails[0]}"
        rest = list(zip(signs_picked[1:], tails[1:]))
        expression = _join_signed(first, rest)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (num_terms, tuple(signs_picked), tuple(tails)),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"How many terms are in the expression ${expression}$?",
            answer_latex=f"${num_terms}$",
            hints=[
                r"A **term** is a part of the expression separated by $+$ or $-$ at the top level. Do not combine like terms --- this is a counting question.",
                r"Count each chunk between plus or minus signs. A leading minus sign still counts as one term (with a negative coefficient).",
                f"There are ${num_terms}$ terms.",
            ],
            solution_steps_latex=[
                f"Look at ${expression}$.",
                "Separate it at every $+$ or $-$ at the top level; each piece is a term.",
                f"Counting the pieces gives ${num_terms}$ terms.",
            ],
            tags=_tags(difficulty),
        )


@register
class TranslateWordToExpression(Generator):
    """Translate an English phrase into an algebraic expression.

    Covers the common patterns: "N more than", "N less than", "twice a number",
    "N times a number plus/minus K", etc. The target variable is ``n``.

    The critical trap is "K less than n" = $n - K$ (not $K - n$).
    """

    generator_id = "translate_word_to_expression"
    topic_slug = "variables_and_algebraic_expressions"
    display_name = "Translate a phrase to an algebraic expression"

    supports_word_problems = True

    _RANGES = {
        "easy":   (2, 9),
        "medium": (2, 15),
        "hard":   (2, 25),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        k = rng.randint(lo, hi)
        j = rng.randint(lo, hi)

        # Templates: (template_id, phrase, answer, hint_note)
        # Each is picked uniformly; the template id contributes to the param
        # tuple so we get plenty of unique problems per difficulty.
        template = rng.randrange(10)

        if template == 0:
            # "K more than a number n"
            phrase = f"{k} more than a number $n$"
            answer = f"n + {k}"
            note = r"'more than' means addition: 'K more than n' becomes $n + K$."
        elif template == 1:
            # "K less than a number n"  --- TRAP: n - K, not K - n
            phrase = f"{k} less than a number $n$"
            answer = f"n - {k}"
            note = r"**Watch the order!** 'K less than n' means $n - K$, not $K - n$. The number you start with is $n$, then you take $K$ away."
        elif template == 2:
            # "The sum of a number n and K"
            phrase = f"the sum of a number $n$ and {k}"
            answer = f"n + {k}"
            note = r"'The sum of A and B' is $A + B$."
        elif template == 3:
            # "The difference of a number n and K"
            phrase = f"the difference of a number $n$ and {k}"
            answer = f"n - {k}"
            note = r"'The difference of A and B' is $A - B$ (first minus second)."
        elif template == 4:
            # "Twice a number n"
            phrase = "twice a number $n$"
            answer = "2n"
            note = r"'Twice' means multiplied by $2$."
        elif template == 5:
            # "Three times a number n"
            phrase = "three times a number $n$"
            answer = "3n"
            note = r"'Three times' means multiplied by $3$."
        elif template == 6:
            # "K times a number n, plus J"
            phrase = f"{k} times a number $n$, plus {j}"
            answer = f"{k}n + {j}"
            note = r"'K times n' is $Kn$; adding $J$ gives $Kn + J$."
        elif template == 7:
            # "K times a number n, minus J"
            phrase = f"{k} times a number $n$, minus {j}"
            answer = f"{k}n - {j}"
            note = r"Translate the multiplication first, then the subtraction: $Kn - J$."
        elif template == 8:
            # "J more than twice a number n"
            phrase = f"{j} more than twice a number $n$"
            answer = f"2n + {j}"
            note = r"'More than' adds to the thing that comes after it: 'J more than twice n' becomes $2n + J$."
        else:  # template == 9
            # "J less than K times a number n"  --- again the order trap
            phrase = f"{j} less than {k} times a number $n$"
            answer = f"{k}n - {j}"
            note = r"'J less than Kn' is $Kn - J$, not $J - Kn$. Subtraction order matters."

        statement = f"Write the expression for: {phrase}."

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
                r"Translate each word phrase into a math symbol: 'more than' $\to +$, 'less than' $\to -$ (watch the order), 'times' $\to \cdot$.",
                f"The final expression is ${answer}$.",
            ],
            solution_steps_latex=[
                f"Identify the operation words in the phrase: {phrase}.",
                note,
                f"Writing it in symbols gives ${answer}$.",
            ],
            tags=_tags(difficulty),
        )
