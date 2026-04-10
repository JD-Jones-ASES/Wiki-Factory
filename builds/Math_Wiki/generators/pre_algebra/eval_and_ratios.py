"""Expression evaluation and ratios generators (Cluster 1 Wave 3).

Two canonical topic slugs covered here:

- ``evaluating_expressions`` at
  wiki/topics/pre_algebra/Evaluating_Expressions.md

  Generators:
    * evaluate_linear_expression       --- compute ax + b at a given x
    * evaluate_expression_with_exponent --- compute expressions containing x^2
                                           (exercises the parenthesization trap)
    * evaluate_two_variable_expression --- compute expressions in two variables

- ``ratios_and_equivalent_ratios`` at
  wiki/topics/pre_algebra/Ratios_And_Equivalent_Ratios.md

  Generators:
    * simplify_ratio             --- reduce ka : kb to p : q
    * find_equivalent_ratio      --- given a : b, find an equivalent with a
                                     specified first or second term
    * scale_ratio_to_context     --- real-world scaling (recipe / paint / mix)

All generators use backward construction: pick a clean answer first, then
derive the presented parameters. Sympy ``Rational`` is used where exact
arithmetic matters; integer-only cases stay in Python's native ints.
"""
from __future__ import annotations

import math
import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Symbols used when rendering expressions via sympy.latex.
x = sp.Symbol("x")
a_sym = sp.Symbol("a")
b_sym = sp.Symbol("b")


# Shared tag sets.
_TAGS_PROCEDURAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_MULTISTEP = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-multi-step",
]
_TAGS_REASONING = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-conceptual-reasoning",
]


def _fmt_signed(n: int) -> str:
    """Render an integer wrapping negatives in parentheses so it substitutes cleanly.

    Example: _fmt_signed(-3) -> "(-3)", _fmt_signed(5) -> "5".
    """
    return f"({n})" if n < 0 else f"{n}"


def _fmt_coefficient_term(coeff: int, var_latex: str) -> str:
    """Render ``coeff * var`` as a LaTeX term, suppressing the coefficient when |coeff|=1.

    Used to keep expressions looking natural: write ``x`` instead of ``1x`` and
    ``-x`` instead of ``-1x``.
    """
    if coeff == 1:
        return var_latex
    if coeff == -1:
        return f"-{var_latex}"
    return f"{coeff}{var_latex}"


def _fmt_linear(a: int, var_latex: str, b: int) -> str:
    """Render $ax + b$ as a clean LaTeX expression.

    Drops the constant when ``b == 0`` and uses ``- k`` instead of ``+ -k``.
    """
    lead = _fmt_coefficient_term(a, var_latex)
    if b == 0:
        return lead
    if b > 0:
        return f"{lead} + {b}"
    return f"{lead} - {abs(b)}"


def _random_coprime_pair(rng: random.Random, max_val: int) -> tuple[int, int]:
    """Return a coprime pair (p, q) with 1 <= p, q <= max_val and p != q.

    Useful for picking the lowest-terms ratio before scaling up by a multiplier.
    """
    for _ in range(200):
        p = rng.randint(1, max_val)
        q = rng.randint(2, max_val)
        if p == q:
            continue
        if math.gcd(p, q) == 1:
            return p, q
    return 1, 2  # pragma: no cover --- fallback should never trigger in practice


# ===========================================================================
# Topic 1: evaluating_expressions
# ===========================================================================

@register
class EvaluateLinearExpression(Generator):
    """Evaluate $ax + b$ at a specified value of $x$."""
    generator_id = "evaluate_linear_expression"
    topic_slug = "evaluating_expressions"
    display_name = "Evaluate a linear expression at a given value"

    # Easy stays non-negative; medium and hard allow negatives on every term.
    _PARAMS = {
        "easy":   {"a_range": (1, 10),  "b_range": (0, 10),  "x_range": (0, 10)},
        "medium": {"a_range": (-10, 10), "b_range": (-10, 10), "x_range": (-10, 10)},
        "hard":   {"a_range": (-20, 20), "b_range": (-20, 20), "x_range": (-20, 20)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        a = rng.randint(*params["a_range"])
        if a == 0:
            a = 1  # keep the expression genuinely linear in x
        b = rng.randint(*params["b_range"])
        x_val = rng.randint(*params["x_range"])
        result = a * x_val + b

        expr_latex = _fmt_linear(a, "x", b)
        ax_val = a * x_val

        # Build the substitution line. Show the wrapping of a negative x.
        sub_expr = _fmt_linear(a, _fmt_signed(x_val), b)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, x_val)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${expr_latex}$ when $x = {x_val}$.",
            answer_latex=f"${result}$",
            hints=[
                f"Substitute ${x_val}$ in place of $x$.",
                f"The expression becomes ${sub_expr}$.",
                f"Multiply first, then add: ${a} \\cdot {_fmt_signed(x_val)} = {ax_val}$, "
                f"and ${ax_val} + ({b}) = {result}$.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                f"Substitute $x = {x_val}$: ${sub_expr}$.",
                f"Multiply: ${a} \\cdot {_fmt_signed(x_val)} = {ax_val}$.",
                f"Add the constant: ${ax_val} + ({b}) = {result}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class EvaluateExpressionWithExponent(Generator):
    """Evaluate an expression containing $x^2$ at a specified value of $x$.

    The generator deliberately exercises the parenthesization trap:
    $(-2)^2 = 4$, not $-4$. Both positive and negative $x$ values appear so
    students see how the parentheses matter.
    """
    generator_id = "evaluate_expression_with_exponent"
    topic_slug = "evaluating_expressions"
    display_name = "Evaluate an expression with x^2"

    # a * x^2 + c. Easy keeps a positive and |x| small; harder versions
    # include negative leading coefficients and larger magnitudes.
    _PARAMS = {
        "easy":   {"a_range": (1, 5),   "c_range": (-10, 10), "x_range": (-6, 6)},
        "medium": {"a_range": (-6, 6),  "c_range": (-15, 15), "x_range": (-8, 8)},
        "hard":   {"a_range": (-10, 10), "c_range": (-25, 25), "x_range": (-12, 12)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        a = rng.randint(*params["a_range"])
        if a == 0:
            a = 1  # must have an x^2 term
        c = rng.randint(*params["c_range"])
        x_val = rng.randint(*params["x_range"])

        # Compute step by step so the worked solution can echo the arithmetic.
        x_squared = x_val * x_val
        a_times_xsq = a * x_squared
        result = a_times_xsq + c

        # Build the displayed expression: "a x^2 + c" or variants.
        lead = _fmt_coefficient_term(a, "x^2")
        if c == 0:
            expr_latex = lead
        elif c > 0:
            expr_latex = f"{lead} + {c}"
        else:
            expr_latex = f"{lead} - {abs(c)}"

        # Substitution line highlighting the parentheses wrapper.
        lead_sub = _fmt_coefficient_term(a, f"({x_val})^2")
        if c == 0:
            sub_expr = lead_sub
        elif c > 0:
            sub_expr = f"{lead_sub} + {c}"
        else:
            sub_expr = f"{lead_sub} - {abs(c)}"

        # Extra explanatory clause when x is negative --- this is THE point of the problem.
        if x_val < 0:
            sign_note = (
                rf"Because ${x_val}$ is negative, wrap it in parentheses: "
                rf"$({x_val})^2 = ({x_val}) \cdot ({x_val}) = {x_squared}$. "
                rf"Without the parentheses you would incorrectly compute $-{abs(x_val) ** 2}$."
            )
        else:
            sign_note = (
                rf"$({x_val})^2 = {x_val} \cdot {x_val} = {x_squared}$."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, c, x_val)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${expr_latex}$ when $x = {x_val}$.",
            answer_latex=f"${result}$",
            hints=[
                rf"Substitute $({x_val})$ for $x$, with parentheses around the value.",
                rf"Evaluate the exponent first: $({x_val})^2 = {x_squared}$.",
                rf"Multiply by the coefficient, then add the constant: "
                rf"${a} \cdot {x_squared} + ({c}) = {result}$.",
            ],
            solution_steps_latex=[
                f"Start with ${expr_latex}$.",
                f"Substitute $x = {x_val}$ with parentheses: ${sub_expr}$.",
                sign_note,
                rf"Multiply: ${a} \cdot {x_squared} = {a_times_xsq}$.",
                f"Add the constant: ${a_times_xsq} + ({c}) = {result}$.",
            ],
            tags=_TAGS_MULTISTEP + [f"#difficulty-{difficulty}"],
        )


@register
class EvaluateTwoVariableExpression(Generator):
    """Evaluate an expression in two variables at specified values of $a$ and $b$.

    Easy mode: a pure linear combination $m\\,a + n\\,b$.
    Medium/hard: one term is squared, i.e. $a^2 + n\\,b$ or $m\\,a + b^2$.
    """
    generator_id = "evaluate_two_variable_expression"
    topic_slug = "evaluating_expressions"
    display_name = "Evaluate a two-variable expression"

    _PARAMS = {
        "easy":   {"coef_range": (1, 8),    "val_range": (1, 10)},
        "medium": {"coef_range": (-8, 8),   "val_range": (-8, 8)},
        "hard":   {"coef_range": (-12, 12), "val_range": (-12, 12)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        m = rng.randint(*params["coef_range"])
        if m == 0:
            m = 2
        n = rng.randint(*params["coef_range"])
        if n == 0:
            n = 3
        a_val = rng.randint(*params["val_range"])
        b_val = rng.randint(*params["val_range"])

        if difficulty == "easy":
            # Form: m*a + n*b (pure linear combination)
            form = "linear"
            term1 = _fmt_coefficient_term(m, "a")
            term2 = _fmt_coefficient_term(n, "b")
            # Join with proper +/- handling.
            if n >= 0:
                expr_latex = f"{term1} + {term2}"
            else:
                expr_latex = f"{term1} - {_fmt_coefficient_term(abs(n), 'b')}"
            t1_val = m * a_val
            t2_val = n * b_val
            result = t1_val + t2_val
            sub_line = (
                f"{_fmt_coefficient_term(m, _fmt_signed(a_val))} "
                f"{'+' if n >= 0 else '-'} "
                f"{_fmt_coefficient_term(abs(n), _fmt_signed(b_val))}"
            )
            step_lines = [
                f"Start with ${expr_latex}$.",
                f"Substitute $a = {a_val}$ and $b = {b_val}$: ${sub_line}$.",
                rf"Compute each term: ${m} \cdot {_fmt_signed(a_val)} = {t1_val}$ and ${n} \cdot {_fmt_signed(b_val)} = {t2_val}$.",
                f"Add the results: ${t1_val} + ({t2_val}) = {result}$.",
            ]
        else:
            # Pick whether to square a or b.
            square_a = rng.choice([True, False])
            if square_a:
                form = "a_squared"
                # Expression: a^2 + n*b
                a_sq = a_val * a_val
                t2_val = n * b_val
                result = a_sq + t2_val
                if n >= 0:
                    expr_latex = f"a^2 + {_fmt_coefficient_term(n, 'b')}"
                else:
                    expr_latex = f"a^2 - {_fmt_coefficient_term(abs(n), 'b')}"
                sub_line = (
                    f"({a_val})^2 "
                    f"{'+' if n >= 0 else '-'} "
                    f"{_fmt_coefficient_term(abs(n), _fmt_signed(b_val))}"
                )
                step_lines = [
                    f"Start with ${expr_latex}$.",
                    f"Substitute $a = {a_val}$ and $b = {b_val}$: ${sub_line}$.",
                    rf"Apply the exponent first: $({a_val})^2 = {a_sq}$.",
                    rf"Compute the other term: ${n} \cdot {_fmt_signed(b_val)} = {t2_val}$.",
                    f"Add: ${a_sq} + ({t2_val}) = {result}$.",
                ]
            else:
                form = "b_squared"
                # Expression: m*a + b^2
                t1_val = m * a_val
                b_sq = b_val * b_val
                result = t1_val + b_sq
                expr_latex = f"{_fmt_coefficient_term(m, 'a')} + b^2"
                sub_line = (
                    f"{_fmt_coefficient_term(m, _fmt_signed(a_val))} + ({b_val})^2"
                )
                step_lines = [
                    f"Start with ${expr_latex}$.",
                    f"Substitute $a = {a_val}$ and $b = {b_val}$: ${sub_line}$.",
                    rf"Apply the exponent first: $({b_val})^2 = {b_sq}$.",
                    rf"Compute the other term: ${m} \cdot {_fmt_signed(a_val)} = {t1_val}$.",
                    f"Add: ${t1_val} + {b_sq} = {result}$.",
                ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (form, m, n, a_val, b_val)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Evaluate ${expr_latex}$ when $a = {a_val}$ and $b = {b_val}$.",
            answer_latex=f"${result}$",
            hints=[
                f"Substitute $a = {a_val}$ and $b = {b_val}$ wherever those variables appear.",
                "Wrap negative values in parentheses before multiplying or squaring.",
                "Follow the order of operations: exponents first, then multiplication, then addition.",
            ],
            solution_steps_latex=step_lines,
            tags=_TAGS_MULTISTEP + [f"#difficulty-{difficulty}"],
        )


# ===========================================================================
# Topic 2: ratios_and_equivalent_ratios
# ===========================================================================

@register
class SimplifyRatio(Generator):
    """Reduce a ratio $kp : kq$ to lowest terms $p : q$."""
    generator_id = "simplify_ratio"
    topic_slug = "ratios_and_equivalent_ratios"
    display_name = "Simplify a ratio to lowest terms"

    _PARAMS = {
        "easy":   {"max_val": 9,  "k_range": (2, 6)},
        "medium": {"max_val": 14, "k_range": (2, 10)},
        "hard":   {"max_val": 20, "k_range": (3, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        p, q = _random_coprime_pair(rng, params["max_val"])
        k = rng.randint(*params["k_range"])
        left = k * p
        right = k * q

        statement = f"Simplify the ratio ${left} : {right}$ to lowest terms."
        answer = f"${p} : {q}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (left, right)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Find the greatest common divisor (GCD) of ${left}$ and ${right}$.",
                f"The GCD is ${k}$, so divide both terms by ${k}$.",
                f"${left} \\div {k} = {p}$ and ${right} \\div {k} = {q}$, so the ratio is ${p} : {q}$.",
            ],
            solution_steps_latex=[
                f"Start with the ratio ${left} : {right}$.",
                f"Compute $\\gcd({left}, {right}) = {k}$.",
                f"Divide both terms by ${k}$: ${left} \\div {k} = {p}$ and ${right} \\div {k} = {q}$.",
                f"The simplified ratio is ${p} : {q}$. Verify: $\\gcd({p}, {q}) = 1$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class FindEquivalentRatio(Generator):
    """Given a ratio $p : q$, find an equivalent ratio with a specified first or second term."""
    generator_id = "find_equivalent_ratio"
    topic_slug = "ratios_and_equivalent_ratios"
    display_name = "Find an equivalent ratio with a given term"

    _PARAMS = {
        "easy":   {"max_val": 9,  "k_range": (2, 6)},
        "medium": {"max_val": 12, "k_range": (2, 10)},
        "hard":   {"max_val": 16, "k_range": (3, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        p, q = _random_coprime_pair(rng, params["max_val"])
        k = rng.randint(*params["k_range"])
        ask_first = rng.choice([True, False])

        if ask_first:
            # Known first term is k*p, student finds the second term k*q.
            known = k * p
            missing = k * q
            statement = (
                f"What ratio is equivalent to ${p} : {q}$ and has first term ${known}$?"
            )
            scale_hint = (
                f"The first term went from ${p}$ to ${known}$, "
                f"which is a factor of ${known} \\div {p} = {k}$."
            )
            compute_hint = (
                f"Multiply the second term by ${k}$: ${q} \\times {k} = {missing}$."
            )
            answer_ratio = f"{known} : {missing}"
            params_key = ("first", p, q, k)
        else:
            # Known second term is k*q, student finds the first term k*p.
            known = k * q
            missing = k * p
            statement = (
                f"What ratio is equivalent to ${p} : {q}$ and has second term ${known}$?"
            )
            scale_hint = (
                f"The second term went from ${q}$ to ${known}$, "
                f"which is a factor of ${known} \\div {q} = {k}$."
            )
            compute_hint = (
                f"Multiply the first term by ${k}$: ${p} \\times {k} = {missing}$."
            )
            answer_ratio = f"{missing} : {known}"
            params_key = ("second", p, q, k)

        answer = f"${answer_ratio}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params_key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                "Equivalent ratios are formed by multiplying both terms by the same factor.",
                scale_hint,
                compute_hint,
            ],
            solution_steps_latex=[
                f"Start with ${p} : {q}$ and the target term ${known}$.",
                f"Find the scaling factor.",
                scale_hint,
                f"Apply the same factor to the other term.",
                compute_hint,
                f"The equivalent ratio is ${answer_ratio}$.",
            ],
            tags=_TAGS_PROCEDURAL + [f"#difficulty-{difficulty}"],
        )


@register
class ScaleRatioToContext(Generator):
    """Real-world ratio scaling word problem (recipe, paint, mix)."""
    generator_id = "scale_ratio_to_context"
    topic_slug = "ratios_and_equivalent_ratios"
    display_name = "Scale a ratio to fit a real-world quantity"
    supports_word_problems = True

    # Each context picks (item_A, item_B, unit). All items are countable / unit-bearing.
    _CONTEXTS = [
        {
            "name": "recipe",
            "lead_in": "A recipe uses a ${p} : {q}$ ratio of {a_name} to {b_name}.",
            "items": [
                ("sugar", "flour", "cups"),
                ("butter", "flour", "cups"),
                ("rice", "water", "cups"),
                ("milk", "flour", "cups"),
                ("oats", "raisins", "cups"),
            ],
        },
        {
            "name": "paint",
            "lead_in": "A paint color is mixed in a ${p} : {q}$ ratio of {a_name} to {b_name}.",
            "items": [
                ("blue", "white", "ounces"),
                ("red", "yellow", "ounces"),
                ("green", "white", "ounces"),
                ("black", "white", "ounces"),
            ],
        },
        {
            "name": "mix",
            "lead_in": "A concrete mix uses a ${p} : {q}$ ratio of {a_name} to {b_name}.",
            "items": [
                ("sand", "cement", "pounds"),
                ("gravel", "cement", "pounds"),
                ("water", "cement", "gallons"),
            ],
        },
        {
            "name": "fuel",
            "lead_in": "A 2-stroke fuel mix uses a ${p} : {q}$ ratio of {a_name} to {b_name}.",
            "items": [
                ("gasoline", "oil", "ounces"),
            ],
        },
    ]

    _PARAMS = {
        "easy":   {"max_val": 7,  "k_range": (2, 6)},
        "medium": {"max_val": 11, "k_range": (2, 9)},
        "hard":   {"max_val": 15, "k_range": (3, 12)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        p, q = _random_coprime_pair(rng, params["max_val"])
        k = rng.randint(*params["k_range"])

        context = rng.choice(self._CONTEXTS)
        a_name, b_name, unit = rng.choice(context["items"])

        # Randomize whether the known quantity is the first (A) or second (B) item.
        ask_second = rng.choice([True, False])
        if ask_second:
            # Given k*p units of A, find units of B.
            known_amount = k * p
            missing_amount = k * q
            known_name = a_name
            missing_name = b_name
            known_part = p
            missing_part = q
        else:
            # Given k*q units of B, find units of A.
            known_amount = k * q
            missing_amount = k * p
            known_name = b_name
            missing_name = a_name
            known_part = q
            missing_part = p

        lead_in = context["lead_in"].format(p=p, q=q, a_name=a_name, b_name=b_name)
        question = (
            f"If you use ${known_amount}$ {unit} of {known_name}, "
            f"how many {unit} of {missing_name} do you need?"
        )
        statement = f"{lead_in} {question}"
        answer = f"${missing_amount}$ {unit}"

        scale_hint = (
            f"The amount of {known_name} scaled from ${known_part}$ to ${known_amount}$, "
            f"which is a factor of ${known_amount} \\div {known_part} = {k}$."
        )
        compute_hint = (
            f"Multiply the other part of the ratio by ${k}$: "
            f"${missing_part} \\times {k} = {missing_amount}$."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (context["name"], a_name, b_name, p, q, k, ask_second),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"The ratio ${p} : {q}$ means ${p}$ {unit} of {a_name} for every ${q}$ {unit} of {b_name}.",
                scale_hint,
                compute_hint,
            ],
            solution_steps_latex=[
                f"Identify the ratio and the known quantity: ${p} : {q}$ with ${known_amount}$ {unit} of {known_name}.",
                scale_hint,
                f"Apply the same scaling factor to the other part.",
                compute_hint,
                f"Answer: ${missing_amount}$ {unit} of {missing_name}.",
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )
