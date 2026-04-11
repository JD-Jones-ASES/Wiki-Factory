"""Variables and expressions generators (Wave B).

Canonical topic slug ``variables_and_expressions`` at
wiki/topics/algebra/Variables_And_Expressions.md.

- evaluate_expression_at_integer: evaluate ax^2 + bx + c at integer x
- translate_phrase_to_expression: English phrase -> algebraic expression
- identify_terms_and_coefficients: list terms, coefficients, and constants of an expression
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

def _format_linear(a: int, b: int, var: str = "x") -> str:
    """Format ax + b with correct signs."""
    if a == 1:
        head = var
    elif a == -1:
        head = f"-{var}"
    elif a == 0:
        head = ""
    else:
        head = f"{a}{var}"
    if b == 0:
        return head if head else "0"
    if not head:
        return str(b)
    if b > 0:
        return f"{head} + {b}"
    return f"{head} - {abs(b)}"


def _format_quadratic(a: int, b: int, c: int, var: str = "x") -> str:
    """Format ax^2 + bx + c with correct signs."""
    if a == 0:
        return _format_linear(b, c, var)
    if a == 1:
        head = f"{var}^2"
    elif a == -1:
        head = f"-{var}^2"
    else:
        head = f"{a}{var}^2"

    if b == 0:
        pass
    elif b == 1:
        head = f"{head} + {var}"
    elif b == -1:
        head = f"{head} - {var}"
    elif b > 0:
        head = f"{head} + {b}{var}"
    else:
        head = f"{head} - {abs(b)}{var}"

    if c == 0:
        return head
    if c > 0:
        return f"{head} + {c}"
    return f"{head} - {abs(c)}"


@register
class EvaluateExpressionAtInteger(Generator):
    """Evaluate a linear or quadratic expression at an integer value of x."""
    generator_id = "evaluate_expression_at_integer"
    topic_slug = "variables_and_expressions"
    display_name = "Evaluate an expression at an integer"

    _COEF_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _X_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEF_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]

        form = rng.choice(["linear", "quadratic"]) if difficulty != "easy" else "linear"
        x_val = rng.randint(x_lo, x_hi)

        if form == "linear":
            a = rng.randint(c_lo, c_hi)
            while a == 0:
                a = rng.randint(c_lo, c_hi)
            b = rng.randint(c_lo, c_hi)
            expr = _format_linear(a, b)
            result = a * x_val + b
            steps = [
                f"Substitute $x = {x_val}$ into ${expr}$.",
                f"${a}({x_val}) + ({b})$.",
                f"$= {a * x_val} + ({b}) = {result}$.",
            ]
            params = ("linear", a, b, x_val)
        else:
            a = rng.randint(-5, 5)
            while a == 0:
                a = rng.randint(-5, 5)
            b = rng.randint(c_lo, c_hi)
            c = rng.randint(c_lo, c_hi)
            expr = _format_quadratic(a, b, c)
            result = a * x_val * x_val + b * x_val + c
            steps = [
                f"Substitute $x = {x_val}$ into ${expr}$.",
                f"${a}({x_val})^2 + ({b})({x_val}) + ({c})$.",
                f"$= {a}({x_val * x_val}) + ({b * x_val}) + ({c})$.",
                f"$= {a * x_val * x_val} + ({b * x_val}) + ({c}) = {result}$.",
            ]
            params = ("quadratic", a, b, c, x_val)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${expr}$ when $x = {x_val}$.",
            answer_latex=f"${result}$",
            hints=[
                r"Replace every $x$ in the expression with the given value.",
                r"Use the correct order of operations (exponents first, then multiply, then add).",
                f"The final answer is ${result}$.",
            ],
            solution_steps_latex=steps,
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-formula-substitution",
            ],
        )


@register
class TranslatePhraseToExpression(Generator):
    """Translate a verbal phrase into an algebraic expression."""
    generator_id = "translate_phrase_to_expression"
    topic_slug = "variables_and_expressions"
    display_name = "Translate a phrase into an algebraic expression"
    bank_count_per_difficulty = 20

    _PHRASES = [
        {
            "template": "the sum of $x$ and {n}",
            "answer": "x + {n}",
            "reasoning": r"\"Sum\" indicates addition.",
        },
        {
            "template": "{n} more than $x$",
            "answer": "x + {n}",
            "reasoning": r"\"More than\" adds to $x$.",
        },
        {
            "template": "{n} less than $x$",
            "answer": "x - {n}",
            "reasoning": r"\"Less than\" subtracts from $x$, and the number comes after.",
        },
        {
            "template": "the difference of $x$ and {n}",
            "answer": "x - {n}",
            "reasoning": r"\"Difference\" means subtraction in the stated order.",
        },
        {
            "template": "the product of {n} and $x$",
            "answer": "{n}x",
            "reasoning": r"\"Product\" indicates multiplication.",
        },
        {
            "template": "{n} times $x$",
            "answer": "{n}x",
            "reasoning": r"\"Times\" indicates multiplication.",
        },
        {
            "template": "the quotient of $x$ and {n}",
            "answer": r"\dfrac{{x}}{{{n}}}",
            "reasoning": r"\"Quotient\" indicates division in the stated order.",
        },
        {
            "template": "twice $x$ increased by {n}",
            "answer": "2x + {n}",
            "reasoning": r"\"Twice\" doubles $x$, then \"increased by\" adds.",
        },
        {
            "template": "twice $x$ decreased by {n}",
            "answer": "2x - {n}",
            "reasoning": r"\"Twice\" doubles $x$, then \"decreased by\" subtracts.",
        },
        {
            "template": "{n} less than three times $x$",
            "answer": "3x - {n}",
            "reasoning": r"\"Three times\" triples $x$, then \"less than\" subtracts.",
        },
        {
            "template": "{n} more than twice $x$",
            "answer": "2x + {n}",
            "reasoning": r"\"Twice\" doubles $x$, then \"more than\" adds.",
        },
        {
            "template": "half of $x$ plus {n}",
            "answer": r"\dfrac{{x}}{{2}} + {n}",
            "reasoning": r"\"Half\" divides $x$ by two, then \"plus\" adds.",
        },
        {
            "template": "the square of $x$ increased by {n}",
            "answer": "x^2 + {n}",
            "reasoning": r"\"Square\" means $x^2$, then \"increased by\" adds.",
        },
        {
            "template": "{n} decreased by $x$",
            "answer": "{n} - x",
            "reasoning": r"\"Decreased by\" subtracts $x$ from {n}.",
        },
    ]

    _N_RANGE = {"easy": (2, 10), "medium": (2, 15), "hard": (2, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_lo, n_hi = self._N_RANGE[difficulty]
        idx = rng.randrange(len(self._PHRASES))
        p = self._PHRASES[idx]
        n = rng.randint(n_lo, n_hi)

        phrase = p["template"].format(n=n)
        answer_expr = p["answer"].format(n=n)
        reasoning = p["reasoning"].format(n=n)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Write an algebraic expression for the phrase: "
                f"\"{phrase}\"."
            ),
            answer_latex=f"${answer_expr}$",
            hints=[
                r"Identify the operation words (sum, difference, product, quotient, times, more than, less than).",
                reasoning,
                f"The expression is ${answer_expr}$.",
            ],
            solution_steps_latex=[
                f"Read the phrase carefully: \"{phrase}\".",
                reasoning,
                f"Write the expression: ${answer_expr}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-translation",
            ],
        )


@register
class IdentifyTermsAndCoefficients(Generator):
    """Given a polynomial expression, list its terms, coefficients, and constant."""
    generator_id = "identify_terms_and_coefficients"
    topic_slug = "variables_and_expressions"
    display_name = "Identify terms, coefficients, and constant"

    _COEF_RANGE = {"easy": (1, 9), "medium": (2, 12), "hard": (2, 18)}
    _CONST_RANGE = {"easy": (-12, 12), "medium": (-20, 20), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEF_RANGE[difficulty]
        n_lo, n_hi = self._CONST_RANGE[difficulty]

        # Build ax^2 + bx + c, with a = 0 occasionally for variety (degree 1).
        include_quadratic = rng.random() < 0.6
        if include_quadratic:
            a = rng.randint(c_lo, c_hi)
            if rng.random() < 0.35:
                a = -a
        else:
            a = 0
        b = rng.randint(c_lo, c_hi)
        if rng.random() < 0.35:
            b = -b
        c = rng.randint(n_lo, n_hi)

        # Avoid the all-zero pathology
        if a == 0 and b == 0:
            b = rng.randint(2, c_hi)

        expr_latex = _format_quadratic(a, b, c)

        terms: list[str] = []
        coeffs: list[int] = []
        if a != 0:
            terms.append(f"${a}x^2$" if a not in (1, -1) else ("$x^2$" if a == 1 else "$-x^2$"))
            coeffs.append(a)
        if b != 0:
            terms.append(f"${b}x$" if b not in (1, -1) else ("$x$" if b == 1 else "$-x$"))
            coeffs.append(b)
        if c != 0:
            terms.append(f"${c}$")

        terms_str = ", ".join(terms) if terms else "(none)"
        coeffs_str = ", ".join(str(ci) for ci in coeffs) if coeffs else "(none)"
        const_str = str(c) if c != 0 else "0"

        answer = (
            f"Terms: {terms_str}. Coefficients: {coeffs_str}. "
            f"Constant: ${const_str}$."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Identify the terms, coefficients, and constant in the expression "
                f"${expr_latex}$."
            ),
            answer_latex=answer,
            hints=[
                r"A **term** is a single part of the expression separated by $+$ or $-$ signs.",
                r"A **coefficient** is the numerical factor in front of a variable term.",
                r"The **constant** is the term without a variable.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                f"Separate into terms at the $+$ and $-$ signs: {terms_str}.",
                f"List the numerical coefficients of the variable terms: {coeffs_str}.",
                f"The term without a variable is the constant: ${const_str}$.",
                answer,
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-algebraic-manipulation",
            ],
        )
