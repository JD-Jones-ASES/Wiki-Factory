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


# ---------------------------------------------------------------------------
# Topic 3: solving_one_step_equations_addition_and_subtraction
# ---------------------------------------------------------------------------


def _linear_term(coef: int, var: str = "x") -> str:
    """Render a coefficient-times-variable cleanly."""
    if coef == 1:
        return var
    if coef == -1:
        return f"-{var}"
    return f"{coef}{var}"


def _plus_constant(const: int) -> str:
    """Render `+ const` or `- |const|` depending on sign; `` if const == 0."""
    if const == 0:
        return ""
    if const > 0:
        return f" + {const}"
    return f" - {abs(const)}"


@register
class SolveOneStepAddSubtract(Generator):
    """Solve a one-step equation of the form x + a = b, x - a = b, or b = x + a.

    Backward construction: pick x and a, compute b. Guaranteed solvable.
    """

    generator_id = "solve_one_step_add_subtract"
    topic_slug = "solving_one_step_equations_addition_and_subtraction"
    display_name = "Solve a one-step addition or subtraction equation"

    _RANGES = {
        "easy":   {"x": (1, 20),   "a": (1, 20)},
        "medium": {"x": (-50, 50), "a": (-50, 50)},
        "hard":   {"x": (-200, 200), "a": (-200, 200)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x_lo, x_hi = r["x"]
        a_lo, a_hi = r["a"]
        x = rng.randint(x_lo, x_hi)
        a = rng.randint(a_lo, a_hi)
        while a == 0:
            a = rng.randint(a_lo, a_hi)

        # Four templates:
        #   0: x + a = b   (b = x + a)
        #   1: x - a = b   (b = x - a)
        #   2: b = x + a   (variable on right)
        #   3: a + x = b   (constant-first form)
        template = rng.randrange(4)

        opener = rng.choice([
            "Determine",
            "Find",
            "Solve for",
            "Compute",
        ])

        if template == 0:
            b = x + a
            eq = f"x + {a} = {b}" if a >= 0 else f"x - {abs(a)} = {b}"
            isolate = (
                f"Subtract ${a}$ from both sides: $x = {b} - ({a}) = {x}$."
                if a >= 0 else
                f"Add ${abs(a)}$ to both sides: $x = {b} + {abs(a)} = {x}$."
            )
            rule_hint = r"To isolate $x$, undo the operation on the left. Subtraction undoes addition and vice versa."
        elif template == 1:
            b = x - a
            eq = f"x - {a} = {b}" if a >= 0 else f"x + {abs(a)} = {b}"
            isolate = (
                f"Add ${a}$ to both sides: $x = {b} + {a} = {x}$."
                if a >= 0 else
                f"Subtract ${abs(a)}$ from both sides: $x = {b} - {abs(a)} = {x}$."
            )
            rule_hint = r"To undo a subtraction, add the same amount to both sides."
        elif template == 2:
            b = x + a
            eq = f"{b} = x + {a}" if a >= 0 else f"{b} = x - {abs(a)}"
            isolate = (
                f"Subtract ${a}$ from both sides: ${b} - ({a}) = x$, so $x = {x}$."
                if a >= 0 else
                f"Add ${abs(a)}$ to both sides: ${b} + {abs(a)} = x$, so $x = {x}$."
            )
            rule_hint = r"The variable can live on either side. Isolate $x$ the same way no matter which side it sits on."
        else:  # template == 3
            b = x + a
            eq = f"{a} + x = {b}" if a >= 0 else f"{abs(a) * -1} + x = {b}"
            # re-render cleanly when a is negative (-3 + x = ...)
            if a < 0:
                eq = f"-{abs(a)} + x = {b}"
            isolate = (
                f"Subtract ${a}$ from both sides: $x = {b} - ({a}) = {x}$."
                if a >= 0 else
                f"Add ${abs(a)}$ to both sides: $x = {b} + {abs(a)} = {x}$."
            )
            rule_hint = r"Commutative property: $a + x$ is the same as $x + a$. Undo the addition the same way."

        statement = f"{opener} $x$ such that ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (template, x, a),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                rule_hint,
                r"Perform the same operation on both sides of the equation so the variable ends up alone.",
                f"After isolating, you should get $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq}$.",
                isolate,
                f"Therefore $x = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class SolveConstantMinusX(Generator):
    """Solve an equation of the form a - x = b where the variable is subtracted.

    Backward: pick x and a, compute b = a - x.
    """

    generator_id = "solve_constant_minus_x"
    topic_slug = "solving_one_step_equations_addition_and_subtraction"
    display_name = "Solve a - x = b (sign-care case)"

    _RANGES = {
        "easy":   {"x": (1, 20),   "a": (1, 30)},
        "medium": {"x": (-30, 30), "a": (-40, 40)},
        "hard":   {"x": (-100, 100), "a": (-150, 150)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x_lo, x_hi = r["x"]
        a_lo, a_hi = r["a"]
        x = rng.randint(x_lo, x_hi)
        a = rng.randint(a_lo, a_hi)
        # Avoid trivial 0 - x = -x
        while a == 0:
            a = rng.randint(a_lo, a_hi)
        b = a - x

        # Display form for a depending on sign
        if a >= 0:
            eq = f"{a} - x = {b}"
        else:
            eq = f"-{abs(a)} - x = {b}"

        opener = rng.choice([
            "Determine $x$",
            "Find $x$",
            "Solve for $x$",
        ])
        statement = f"{opener} such that ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"Move the variable term to the other side so its coefficient becomes positive.",
                f"Add $x$ to both sides to get ${a} = {b} + x$; then subtract ${b}$ from both sides.",
                f"After isolating, $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq}$.",
                f"Add $x$ to both sides: ${a} = {b} + x$.",
                f"Subtract ${b}$ from both sides: ${a} - ({b}) = x$, i.e., $x = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


_ONE_STEP_WORD_CONTEXTS = (
    ("Priya", "stickers", "her brother gave her"),
    ("Kai", "marbles", "his friend handed him"),
    ("Maya", "seedlings", "the gardening class added"),
    ("Rohan", "trading cards", "he bought"),
    ("Zoe", "photographs", "she took in the afternoon, adding"),
    ("Emilia", "sheet music pages", "her jazz band shared"),
    ("the math club", "pencils", "the teacher donated"),
)


@register
class OneStepWordToEquationAdd(Generator):
    """Word problem translating to x + a = b. Backward construction.

    Pick the original quantity x and the added amount a, compute b. Fresh names.
    """

    generator_id = "one_step_word_to_equation_add"
    topic_slug = "solving_one_step_equations_addition_and_subtraction"
    display_name = "Translate a word problem to x + a = b"

    supports_word_problems = True

    _RANGES = {
        "easy":   {"x": (5, 30),   "a": (2, 20)},
        "medium": {"x": (10, 80),  "a": (5, 40)},
        "hard":   {"x": (15, 200), "a": (10, 90)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x = rng.randint(*r["x"])
        a = rng.randint(*r["a"])
        b = x + a
        actor, item, verb_phrase = rng.choice(_ONE_STEP_WORD_CONTEXTS)
        actor_cap = actor[0].upper() + actor[1:]

        if actor.startswith("the"):
            statement = (
                f"{actor_cap} had some {item}. After {verb_phrase} "
                f"${a}$ more, there were ${b}$ {item} in total. "
                f"How many did they start with?"
            )
        else:
            statement = (
                f"{actor_cap} had some {item}. After {verb_phrase} "
                f"${a}$ more, {actor} had ${b}$ {item}. "
                f"How many did {actor} start with?"
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a, actor),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$ {item}",
            hints=[
                f"Let $x$ stand for the starting number of {item}. The equation is $x + {a} = {b}$.",
                f"Subtract ${a}$ from both sides to isolate $x$.",
                f"This gives $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Translate: starting quantity + added amount = final amount, i.e., $x + {a} = {b}$.",
                f"Subtract ${a}$ from both sides: $x = {b} - {a}$.",
                f"Therefore $x = {x}$ {item}.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-translation",
                "#word-problem-support",
                f"#difficulty-{difficulty}",
            ],
        )


# ---------------------------------------------------------------------------
# Topic 4: solving_one_step_equations_multiplication_and_division
# ---------------------------------------------------------------------------


@register
class SolveOneStepMultiply(Generator):
    """Solve ax = b for integer x. Backward: pick x and a, compute b."""

    generator_id = "solve_one_step_multiply"
    topic_slug = "solving_one_step_equations_multiplication_and_division"
    display_name = "Solve a one-step multiplication equation"

    _RANGES = {
        "easy":   {"x": (1, 12),    "a": (2, 10)},
        "medium": {"x": (-20, 20),  "a": (-12, 12)},
        "hard":   {"x": (-40, 40),  "a": (-15, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x_lo, x_hi = r["x"]
        a_lo, a_hi = r["a"]
        x = rng.randint(x_lo, x_hi)
        a = rng.randint(a_lo, a_hi)
        while a == 0 or a == 1 or a == -1:
            a = rng.randint(a_lo, a_hi)
        b = a * x

        opener = rng.choice([
            "Solve for $x$",
            "Determine $x$",
            "Find $x$",
        ])

        # Render the coefficient cleanly
        if a > 0:
            eq = f"{a}x = {b}"
        else:
            eq = f"-{abs(a)}x = {b}"

        statement = f"{opener}: ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"To undo multiplication, divide both sides by the coefficient of $x$.",
                f"Divide both sides by ${a}$: $x = \\dfrac{{{b}}}{{{a}}}$.",
                f"The result is $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq}$.",
                f"Divide both sides by the coefficient ${a}$: $\\dfrac{{{a}x}}{{{a}}} = \\dfrac{{{b}}}{{{a}}}$.",
                f"Therefore $x = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class SolveOneStepDivide(Generator):
    """Solve x/a = b. Backward: pick x and a (divisor), compute b = x/a. Ensure clean integer x/a."""

    generator_id = "solve_one_step_divide"
    topic_slug = "solving_one_step_equations_multiplication_and_division"
    display_name = "Solve a one-step division equation"

    _RANGES = {
        "easy":   {"b": (1, 12),    "a": (2, 10)},
        "medium": {"b": (-15, 15),  "a": (-12, 12)},
        "hard":   {"b": (-25, 25),  "a": (-15, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        b_lo, b_hi = r["b"]
        a_lo, a_hi = r["a"]
        b = rng.randint(b_lo, b_hi)
        a = rng.randint(a_lo, a_hi)
        while a == 0 or a == 1 or a == -1:
            a = rng.randint(a_lo, a_hi)
        # x = a * b so x/a = b exactly.
        x = a * b

        eq = f"\\dfrac{{x}}{{{a}}} = {b}"

        opener = rng.choice([
            "Determine",
            "Find",
            "Solve for",
        ])
        statement = f"{opener} $x$ such that ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"To undo division, multiply both sides by the same divisor.",
                f"Multiply both sides by ${a}$: $x = {a} \\cdot {b}$.",
                f"This gives $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with $\\dfrac{{x}}{{{a}}} = {b}$.",
                f"Multiply both sides by ${a}$: $x = {a} \\cdot ({b})$.",
                f"Compute the product: $x = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class SolveOneStepNegativeCoefficient(Generator):
    """Solve -ax = b. Always displays with a leading minus; sign-care focus."""

    generator_id = "solve_one_step_negative_coefficient"
    topic_slug = "solving_one_step_equations_multiplication_and_division"
    display_name = "Solve -ax = b (sign-care case)"

    _RANGES = {
        "easy":   {"x": (1, 12),   "a": (2, 10)},
        "medium": {"x": (-20, 20), "a": (2, 12)},
        "hard":   {"x": (-40, 40), "a": (2, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x = rng.randint(*r["x"])
        a = rng.randint(*r["a"])  # a > 0 internally so display is clean
        # The coefficient in the problem is -a.
        neg_a = -a
        b = neg_a * x

        eq = f"-{a}x = {b}"

        opener = rng.choice([
            "Find",
            "Determine",
            "Solve for",
        ])
        statement = f"{opener} $x$ for which ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"The coefficient of $x$ is negative. Divide both sides by the negative coefficient.",
                f"Divide both sides by $-{a}$: $x = \\dfrac{{{b}}}{{-{a}}}$.",
                r"A negative divided by a negative is positive; a positive divided by a negative is negative. The result is " + f"$x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with $-{a}x = {b}$.",
                f"Divide both sides by the coefficient $-{a}$: $x = \\dfrac{{{b}}}{{-{a}}}$.",
                f"Simplify the sign: $x = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


# ---------------------------------------------------------------------------
# Topic 5: solving_two_step_equations
# ---------------------------------------------------------------------------


@register
class SolveTwoStepForward(Generator):
    """Solve ax + b = c. Backward: pick x, a, b; compute c."""

    generator_id = "solve_two_step_forward"
    topic_slug = "solving_two_step_equations"
    display_name = "Solve a two-step equation ax + b = c"

    _RANGES = {
        "easy":   {"x": (1, 10),    "a": (2, 8),    "b": (-20, 20)},
        "medium": {"x": (-20, 20),  "a": (-10, 10), "b": (-50, 50)},
        "hard":   {"x": (-40, 40),  "a": (-15, 15), "b": (-100, 100)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x = rng.randint(*r["x"])
        a = rng.randint(*r["a"])
        while a == 0 or a == 1 or a == -1:
            a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        while b == 0:
            b = rng.randint(*r["b"])
        c = a * x + b

        # Display the coefficient and the constant cleanly.
        if a > 0:
            ax_str = f"{a}x"
        else:
            ax_str = f"-{abs(a)}x"
        if b >= 0:
            eq = f"{ax_str} + {b} = {c}"
        else:
            eq = f"{ax_str} - {abs(b)} = {c}"

        # Intermediate value after step 1
        after_sub = c - b  # = a*x

        opener = rng.choice([
            "Determine $x$",
            "Solve for $x$",
            "Find $x$",
        ])
        statement = f"{opener}: ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"First undo the addition or subtraction; then undo the multiplication.",
                (
                    f"Subtract ${b}$ from both sides: ${ax_str} = {after_sub}$."
                    if b >= 0 else
                    f"Add ${abs(b)}$ to both sides: ${ax_str} = {after_sub}$."
                ),
                f"Divide both sides by ${a}$: $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq}$.",
                (
                    f"Subtract ${b}$ from both sides: ${ax_str} = {c} - ({b}) = {after_sub}$."
                    if b >= 0 else
                    f"Add ${abs(b)}$ to both sides: ${ax_str} = {c} + {abs(b)} = {after_sub}$."
                ),
                f"Divide both sides by ${a}$: $x = \\dfrac{{{after_sub}}}{{{a}}} = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                "#skill-multi-step",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class SolveTwoStepWithFractionCoefficient(Generator):
    """Solve (x/a) + b = c. Backward: pick x divisible by a cleanly."""

    generator_id = "solve_two_step_with_fraction_coefficient"
    topic_slug = "solving_two_step_equations"
    display_name = "Solve a two-step equation with a fraction coefficient"

    _RANGES = {
        "easy":   {"q": (1, 10),   "a": (2, 8),  "b": (-15, 15)},
        "medium": {"q": (-15, 15), "a": (2, 12), "b": (-30, 30)},
        "hard":   {"q": (-25, 25), "a": (2, 15), "b": (-60, 60)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        q = rng.randint(*r["q"])  # quotient x/a
        a = rng.randint(*r["a"])
        while a in (0, 1):
            a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        while b == 0:
            b = rng.randint(*r["b"])
        x = a * q  # so x/a = q exactly
        c = q + b

        if b >= 0:
            eq = f"\\dfrac{{x}}{{{a}}} + {b} = {c}"
        else:
            eq = f"\\dfrac{{x}}{{{a}}} - {abs(b)} = {c}"

        opener = rng.choice([
            "Determine $x$",
            "Solve for $x$",
            "Find $x$",
        ])
        statement = f"{opener}: ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (q, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"First isolate the fractional term by undoing the addition or subtraction; then clear the fraction by multiplying.",
                (
                    f"Subtract ${b}$ from both sides: $\\dfrac{{x}}{{{a}}} = {q}$."
                    if b >= 0 else
                    f"Add ${abs(b)}$ to both sides: $\\dfrac{{x}}{{{a}}} = {q}$."
                ),
                f"Multiply both sides by ${a}$: $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq}$.",
                (
                    f"Subtract ${b}$ from both sides: $\\dfrac{{x}}{{{a}}} = {c} - ({b}) = {q}$."
                    if b >= 0 else
                    f"Add ${abs(b)}$ to both sides: $\\dfrac{{x}}{{{a}}} = {c} + {abs(b)} = {q}$."
                ),
                f"Multiply both sides by ${a}$: $x = {a} \\cdot ({q}) = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                "#skill-multi-step",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class SolveTwoStepVariableOnRight(Generator):
    """Solve c = ax + b (same math as forward, variable on right)."""

    generator_id = "solve_two_step_variable_on_right"
    topic_slug = "solving_two_step_equations"
    display_name = "Solve a two-step equation with the variable on the right"

    _RANGES = {
        "easy":   {"x": (1, 10),    "a": (2, 8),    "b": (-20, 20)},
        "medium": {"x": (-20, 20),  "a": (-10, 10), "b": (-50, 50)},
        "hard":   {"x": (-40, 40),  "a": (-15, 15), "b": (-100, 100)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        x = rng.randint(*r["x"])
        a = rng.randint(*r["a"])
        while a in (-1, 0, 1):
            a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        while b == 0:
            b = rng.randint(*r["b"])
        c = a * x + b

        if a > 0:
            ax_str = f"{a}x"
        else:
            ax_str = f"-{abs(a)}x"
        if b >= 0:
            rhs = f"{ax_str} + {b}"
        else:
            rhs = f"{ax_str} - {abs(b)}"
        eq = f"{c} = {rhs}"

        after_sub = c - b

        opener = rng.choice([
            "Determine $x$",
            "Solve for $x$",
            "Find $x$",
        ])
        statement = f"{opener}: ${eq}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x}$",
            hints=[
                r"The variable is on the right; you can isolate it there or flip the equation first. Either way, undo the addition and then the multiplication.",
                (
                    f"Subtract ${b}$ from both sides: ${after_sub} = {ax_str}$."
                    if b >= 0 else
                    f"Add ${abs(b)}$ to both sides: ${after_sub} = {ax_str}$."
                ),
                f"Divide both sides by ${a}$: $x = {x}$.",
            ],
            solution_steps_latex=[
                f"Start with ${eq}$.",
                (
                    f"Subtract ${b}$ from both sides: ${c} - ({b}) = {ax_str}$, i.e., ${after_sub} = {ax_str}$."
                    if b >= 0 else
                    f"Add ${abs(b)}$ to both sides: ${c} + {abs(b)} = {ax_str}$, i.e., ${after_sub} = {ax_str}$."
                ),
                f"Divide both sides by ${a}$: $x = \\dfrac{{{after_sub}}}{{{a}}} = {x}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                "#skill-multi-step",
                f"#difficulty-{difficulty}",
            ],
        )


# ---------------------------------------------------------------------------
# Topic 6: the_distributive_property_with_variables
# ---------------------------------------------------------------------------


@register
class DistributePositiveCoefficient(Generator):
    """Expand a(bx + c) with positive coefficient a."""

    generator_id = "distribute_positive_coefficient"
    topic_slug = "the_distributive_property_with_variables"
    display_name = "Expand a(bx + c) with positive outside"

    _RANGES = {
        "easy":   {"a": (2, 8),  "b": (1, 9),  "c": (1, 10)},
        "medium": {"a": (2, 10), "b": (2, 12), "c": (2, 15)},
        "hard":   {"a": (3, 12), "b": (2, 15), "c": (2, 20)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])
        sign_c = rng.choice([1, -1])
        c_signed = sign_c * c

        # Inner display
        bx_display = "x" if b == 1 else f"{b}x"
        if c_signed >= 0:
            inner = f"{bx_display} + {c_signed}"
        else:
            inner = f"{bx_display} - {abs(c_signed)}"

        out_x = a * b
        out_const = a * c_signed

        if out_x == 1:
            ax_str = "x"
        elif out_x == -1:
            ax_str = "-x"
        else:
            ax_str = f"{out_x}x"

        if out_const >= 0:
            answer = f"{ax_str} + {out_const}"
        else:
            answer = f"{ax_str} - {abs(out_const)}"

        opener = rng.choice(["Expand", "Apply the distributive property to"])
        statement = f"{opener} ${a}({inner})$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c_signed),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer}$",
            hints=[
                r"Multiply the outside factor by each inside term: $a(bx + c) = abx + ac$.",
                f"Compute ${a} \\cdot {b} = {out_x}$ and ${a} \\cdot ({c_signed}) = {out_const}$.",
                f"Combine: ${answer}$.",
            ],
            solution_steps_latex=[
                f"Start with ${a}({inner})$.",
                f"Distribute ${a}$ to the $x$-term: ${a} \\cdot {bx_display} = {ax_str}$.",
                f"Distribute ${a}$ to the constant term: ${a} \\cdot ({c_signed}) = {out_const}$.",
                f"Combine: ${answer}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class DistributeNegativeSign(Generator):
    """Expand -(bx + c) or -(bx - c). Sign-care focus."""

    generator_id = "distribute_negative_sign"
    topic_slug = "the_distributive_property_with_variables"
    display_name = "Expand -(bx + c)"

    _RANGES = {
        "easy":   {"b": (1, 9),  "c": (1, 10)},
        "medium": {"b": (2, 12), "c": (2, 15)},
        "hard":   {"b": (2, 20), "c": (2, 25)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])
        sign_c = rng.choice([1, -1])
        c_signed = sign_c * c

        bx_display = "x" if b == 1 else f"{b}x"
        if c_signed >= 0:
            inner = f"{bx_display} + {c_signed}"
        else:
            inner = f"{bx_display} - {abs(c_signed)}"

        # Result coefficients: flip signs.
        out_x = -b
        out_const = -c_signed

        if out_x == -1:
            ax_str = "-x"
        else:
            ax_str = f"{out_x}x"

        if out_const == 0:
            answer = ax_str
        elif out_const > 0:
            answer = f"{ax_str} + {out_const}"
        else:
            answer = f"{ax_str} - {abs(out_const)}"

        opener = rng.choice(["Expand", "Simplify"])
        statement = f"{opener} $-({inner})$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (b, c_signed),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer}$",
            hints=[
                r"A leading minus sign is the same as multiplying by $-1$. Flip the sign of every term inside the parentheses.",
                f"The $x$-term becomes ${ax_str}$.",
                f"The constant term becomes ${out_const}$. Combined: ${answer}$.",
            ],
            solution_steps_latex=[
                f"Start with $-({inner})$.",
                r"Rewrite as $-1 \cdot (\text{inside})$, then distribute.",
                f"Flip each sign: $-1 \\cdot ({bx_display}) = {ax_str}$ and $-1 \\cdot ({c_signed}) = {out_const}$.",
                f"Combine: ${answer}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                f"#difficulty-{difficulty}",
            ],
        )


@register
class DistributeAndSimplify(Generator):
    """Expand a(bx + c) + dx or a(bx + c) - d; combine like terms after."""

    generator_id = "distribute_and_simplify"
    topic_slug = "the_distributive_property_with_variables"
    display_name = "Distribute and combine like terms"

    _RANGES = {
        "easy":   {"a": (2, 6),  "b": (1, 6),  "c": (1, 9),  "d": (1, 9)},
        "medium": {"a": (2, 9),  "b": (2, 9),  "c": (2, 12), "d": (2, 12)},
        "hard":   {"a": (2, 12), "b": (2, 12), "c": (2, 15), "d": (2, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])
        d = rng.randint(*r["d"])
        sign_c = rng.choice([1, -1])
        c_signed = sign_c * c
        # Template 0: a(bx + c) + dx  (add extra dx term)
        # Template 1: a(bx + c) - d   (subtract constant d)
        template = rng.randrange(2)

        bx_display = "x" if b == 1 else f"{b}x"
        if c_signed >= 0:
            inner = f"{bx_display} + {c_signed}"
        else:
            inner = f"{bx_display} - {abs(c_signed)}"

        # After distribution
        dist_x = a * b
        dist_const = a * c_signed

        if template == 0:
            extra_piece = f" + {d}x"
            final_x = dist_x + d
            final_const = dist_const
        else:
            extra_piece = f" - {d}"
            final_x = dist_x
            final_const = dist_const - d

        if final_x == 1:
            fx_str = "x"
        elif final_x == -1:
            fx_str = "-x"
        elif final_x == 0:
            fx_str = ""
        else:
            fx_str = f"{final_x}x"

        if final_x == 0 and final_const == 0:
            answer = "0"
        elif final_x == 0:
            answer = f"{final_const}"
        elif final_const == 0:
            answer = fx_str
        elif final_const > 0:
            answer = f"{fx_str} + {final_const}"
        else:
            answer = f"{fx_str} - {abs(final_const)}"

        expr = f"{a}({inner}){extra_piece}"

        opener = rng.choice(["Expand and simplify", "Simplify"])
        statement = f"{opener} ${expr}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (template, a, b, c_signed, d),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer}$",
            hints=[
                r"Distribute first, then combine like terms.",
                f"After distributing: ${dist_x}x {'+ ' + str(dist_const) if dist_const >= 0 else '- ' + str(abs(dist_const))}$; now apply the extra term.",
                f"Combine like terms to get ${answer}$.",
            ],
            solution_steps_latex=[
                f"Start with ${expr}$.",
                f"Distribute ${a}$ into the parentheses: ${dist_x}x {'+ ' + str(dist_const) if dist_const >= 0 else '- ' + str(abs(dist_const))}$.",
                f"Now include the extra term: ${dist_x}x {'+ ' + str(dist_const) if dist_const >= 0 else '- ' + str(abs(dist_const))}{extra_piece}$.",
                f"Combine like terms: ${answer}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-linear",
                "#skill-algebraic-manipulation",
                "#skill-multi-step",
                f"#difficulty-{difficulty}",
            ],
        )
