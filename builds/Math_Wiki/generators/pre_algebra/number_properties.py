"""Properties of addition and multiplication (commutative, associative, etc.).

Canonical topic slug ``properties_of_addition_and_multiplication`` at
wiki/topics/pre_algebra/Properties_Of_Addition_And_Multiplication.md.

- identify_arithmetic_property: given an equation, name the property
- apply_commutative_rewrite: rewrite $a + b$ (or $a \\cdot b$) commutatively
- apply_distributive_rewrite: rewrite $a(b + c)$ as $ab + ac$

The identify generator uses a fixed scenario list (like the cube
cross-section generator): nine properties, each paired with a randomly
chosen numeric instance so the combined parameter space comfortably
exceeds the $10$-unique floor.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "properties_of_addition_and_multiplication"

_TAGS_VISUAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-visualization",
]
_TAGS_PROCEDURAL = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]


# ---------------------------------------------------------------------------
# Scenario table for identify_arithmetic_property.
#
# Each entry: (scenario_key, statement_template, answer_label).
# The statement_template uses ``.format(**vals)`` where ``vals`` comes from
# ``_scenario_values`` below — every scenario has its own variable set.
# ---------------------------------------------------------------------------

_PROPERTY_SCENARIOS: list[tuple[str, str, str]] = [
    (
        "commutative_add",
        "Which property of real numbers is shown by the equation "
        "${a} + {b} = {b} + {a}$?",
        "commutative property of addition",
    ),
    (
        "commutative_mult",
        "Which property of real numbers is shown by the equation "
        "${a} \\cdot {b} = {b} \\cdot {a}$?",
        "commutative property of multiplication",
    ),
    (
        "associative_add",
        "Which property of real numbers is shown by the equation "
        "$({a} + {b}) + {c} = {a} + ({b} + {c})$?",
        "associative property of addition",
    ),
    (
        "associative_mult",
        "Which property of real numbers is shown by the equation "
        "$({a} \\cdot {b}) \\cdot {c} = {a} \\cdot ({b} \\cdot {c})$?",
        "associative property of multiplication",
    ),
    (
        "identity_add",
        "Which property of real numbers is shown by the equation "
        "${a} + 0 = {a}$?",
        "identity property of addition",
    ),
    (
        "identity_mult",
        "Which property of real numbers is shown by the equation "
        "${a} \\cdot 1 = {a}$?",
        "identity property of multiplication",
    ),
    (
        "inverse_add",
        "Which property of real numbers is shown by the equation "
        "${a} + ({neg_a}) = 0$?",
        "inverse property of addition",
    ),
    (
        "inverse_mult",
        "Which property of real numbers is shown by the equation "
        "${a} \\cdot \\dfrac{{1}}{{{a}}} = 1$?",
        "inverse property of multiplication",
    ),
    (
        "distributive",
        "Which property of real numbers is shown by the equation "
        "${a}({b} + {c}) = {a} \\cdot {b} + {a} \\cdot {c}$?",
        "distributive property",
    ),
]


def _scenario_values(
    scenario_key: str, rng: random.Random, difficulty: str
) -> dict[str, str]:
    """Pick random numeric values for a scenario template.

    Returns a dict that covers every placeholder the template may use.
    The numerical ranges widen with difficulty.
    """
    ranges = {
        "easy":   (2, 9),
        "medium": (3, 15),
        "hard":   (5, 25),
    }
    lo, hi = ranges[difficulty]

    a = rng.randint(lo, hi)
    b = rng.randint(lo, hi)
    c = rng.randint(lo, hi)
    # Inverse-addition requires the negative of ``a`` — render with leading minus.
    neg_a = f"-{a}"

    return {
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "neg_a": neg_a,
    }


def _scenario_param_key(
    scenario_key: str, vals: dict[str, str]
) -> tuple:
    """Compact params tuple for ``make_problem_id``.

    Only the values that actually appear in the scenario's template are
    included, so two problems with the same rendered statement map to
    the same problem ID — even if ``_generate_one`` picked different
    unused values for the other placeholders.
    """
    # Which placeholders each scenario actually uses in its template.
    used: dict[str, tuple[str, ...]] = {
        "commutative_add":   ("a", "b"),
        "commutative_mult":  ("a", "b"),
        "associative_add":   ("a", "b", "c"),
        "associative_mult":  ("a", "b", "c"),
        "identity_add":      ("a",),
        "identity_mult":     ("a",),
        "inverse_add":       ("a",),
        "inverse_mult":      ("a",),
        "distributive":      ("a", "b", "c"),
    }
    keys = used.get(scenario_key, ("a", "b", "c"))
    return (scenario_key,) + tuple(vals[k] for k in keys)


# ---------------------------------------------------------------------------

@register
class IdentifyArithmeticProperty(Generator):
    """Given an equation, identify which arithmetic property it demonstrates."""
    generator_id = "identify_arithmetic_property"
    topic_slug = TOPIC_SLUG
    display_name = "Identify the property shown in an equation"

    # 9 scenarios * (hi - lo + 1)^3 numeric variations guarantees a wide space.
    # Easy: 9 * 8^3 = 4608. Safely above the 10-unique floor.

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(_PROPERTY_SCENARIOS))
        scenario_key, template, label = _PROPERTY_SCENARIOS[idx]
        vals = _scenario_values(scenario_key, rng, difficulty)
        statement = template.format(**vals)
        params = _scenario_param_key(scenario_key, vals)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=label,
            hints=[
                (
                    r"The core properties of addition and multiplication are: "
                    r"commutative (order can switch), associative (grouping "
                    r"can shift), identity ($+0$ or $\times 1$), inverse "
                    r"(pairs that cancel to $0$ or $1$), and distributive "
                    r"(multiplication distributes over addition)."
                ),
                (
                    r"Look for the structural signature: rearranging order = "
                    r"commutative; regrouping with parentheses = associative; "
                    r"a neutral element ($0$ or $1$) on one side = identity; "
                    r"cancelling to $0$ or $1$ = inverse; a single factor "
                    r"multiplied across a sum = distributive."
                ),
                f"Compare the structure of the given equation to those signatures. Here it matches the {label}.",
            ],
            solution_steps_latex=[
                r"Read the left-hand side and the right-hand side of the equation carefully.",
                (
                    r"Decide which structural move transformed the left side into "
                    r"the right side: a swap of order, a shift of grouping, the "
                    r"introduction of a neutral element, a cancellation pair, or "
                    r"a multiplication spread across a sum."
                ),
                f"Match that move to its named property: the {label}.",
            ],
            tags=list(_TAGS_VISUAL),
        )


# ---------------------------------------------------------------------------

@register
class ApplyCommutativeRewrite(Generator):
    """Rewrite $a + b$ or $a \\cdot b$ using the commutative property."""
    generator_id = "apply_commutative_rewrite"
    topic_slug = TOPIC_SLUG
    display_name = "Rewrite an expression using the commutative property"

    _RANGES = {
        "easy":   (2, 20),
        "medium": (5, 50),
        "hard":   (10, 99),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        # Make sure a != b so the swap is visually obvious.
        if a == b:
            b = b + 1 if b < hi else b - 1
        op_choice = rng.choice(["add", "mult"])

        if op_choice == "add":
            op_latex = "+"
            op_word = "addition"
            statement = (
                f"Rewrite ${a} + {b}$ using the commutative property of addition."
            )
            answer = f"${b} + {a}$"
            structure_explain = (
                r"The commutative property of addition says $x + y = y + x$."
            )
        else:
            op_latex = r"\cdot"
            op_word = "multiplication"
            statement = (
                f"Rewrite ${a} \\cdot {b}$ using the commutative property of multiplication."
            )
            answer = f"${b} \\cdot {a}$"
            structure_explain = (
                r"The commutative property of multiplication says $x \cdot y = y \cdot x$."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (op_choice, a, b)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                structure_explain,
                f"Swap the order of the two operands around the ${op_latex}$ sign.",
                f"The result is ${b} {op_latex} {a}$.",
            ],
            solution_steps_latex=[
                structure_explain,
                f"Identify the two operands: ${a}$ and ${b}$.",
                f"Write them in the swapped order: ${b} {op_latex} {a}$.",
            ],
            tags=list(_TAGS_PROCEDURAL),
        )


# ---------------------------------------------------------------------------

@register
class ApplyDistributiveRewrite(Generator):
    """Rewrite $a(b + c)$ as $ab + ac$ using the distributive property.

    The inner term ``b`` is randomly either a variable or an integer.
    When ``b`` is a variable, the rewrite shows $ab + ac$ with a literal
    coefficient on the variable; when ``b`` is an integer, both terms
    become pure integers (no evaluation — still in rewritten form).
    """
    generator_id = "apply_distributive_rewrite"
    topic_slug = TOPIC_SLUG
    display_name = "Rewrite an expression using the distributive property"

    _A_RANGE = {"easy": (2, 6),  "medium": (2, 9),  "hard": (3, 12)}
    _C_RANGE = {"easy": (1, 12), "medium": (2, 18), "hard": (3, 25)}
    _B_INT_RANGE = {"easy": (1, 10), "medium": (2, 15), "hard": (3, 20)}

    _VARS = ("x", "y", "m", "n", "p")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.randint(*self._A_RANGE[difficulty])
        c = rng.randint(*self._C_RANGE[difficulty])
        b_is_var = rng.choice([True, False])

        if b_is_var:
            var = rng.choice(self._VARS)
            b_display = var
            ab_term = var if a == 1 else f"{a}{var}"
            ac_term = f"{a * c}"
            b_key = f"var:{var}"
        else:
            b_int = rng.randint(*self._B_INT_RANGE[difficulty])
            b_display = f"{b_int}"
            ab_term = f"{a * b_int}"
            ac_term = f"{a * c}"
            b_key = f"int:{b_int}"

        statement = (
            f"Rewrite ${a}({b_display} + {c})$ by applying the distributive property."
        )
        answer = f"${ab_term} + {ac_term}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b_key, c)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"The distributive property says "
                    r"$a(b + c) = a \cdot b + a \cdot c$."
                ),
                (
                    f"Multiply the outside factor ${a}$ by each term inside "
                    f"the parentheses: ${b_display}$ and ${c}$."
                ),
                f"This yields ${ab_term}$ from the first product and ${ac_term}$ from the second.",
            ],
            solution_steps_latex=[
                (
                    r"Apply the distributive property: "
                    r"$a(b + c) = a \cdot b + a \cdot c$."
                ),
                (
                    f"Multiply ${a}$ by ${b_display}$ to get ${ab_term}$, "
                    f"and ${a}$ by ${c}$ to get ${ac_term}$."
                ),
                f"Combine the two products: ${ab_term} + {ac_term}$.",
            ],
            tags=list(_TAGS_PROCEDURAL),
        )
