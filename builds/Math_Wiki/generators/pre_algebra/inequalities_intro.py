"""Intro-inequality generators (Phase 2c / linear cluster extension).

Covers two canonical topic slugs under pre-algebra:

- ``writing_and_graphing_inequalities`` --- translate phrases to inequality
  symbols, describe graphs, and read inequalities from graph descriptions.
- ``solving_one_step_and_two_step_inequalities`` --- solve one- and two-step
  inequalities with clean integer bounds, including sign-flip cases that
  arise when multiplying or dividing by a negative number.

All phrasing in this file is paraphrased from scratch --- no text is lifted
from source books.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Topic 1: writing_and_graphing_inequalities
# ---------------------------------------------------------------------------


# Each phrase template maps an English keyword to (symbol, latex_symbol,
# describe) and whether it inverts the inequality direction (``swap``).
#
# "at most" / "no more than"   -> x <= k
# "at least" / "no less than"  -> x >= k
# "greater than" / "more than" -> x >  k
# "less than" / "fewer than"   -> x <  k
#
# Each template is (phrase_template, latex_symbol). The ``phrase_template``
# uses ``{var}`` and ``{k}`` placeholders.
_PHRASE_TEMPLATES: tuple[tuple[str, str], ...] = (
    ("{var} is at most {k}", r"\leq"),
    ("{var} is no more than {k}", r"\leq"),
    ("{var} is at least {k}", r"\geq"),
    ("{var} is no less than {k}", r"\geq"),
    ("{var} is greater than {k}", r">"),
    ("{var} is more than {k}", r">"),
    ("{var} is less than {k}", r"<"),
    ("{var} is fewer than {k}", r"<"),
)

_VAR_POOL = ("x", "y", "z", "n", "t")


@register
class WriteInequalityFromPhrase(Generator):
    """Translate an English phrase into an inequality.

    Backward construction: pick a variable, a bound ``k``, and a phrase
    template. Render the phrase and emit the matching inequality.
    """
    generator_id = "write_inequality_from_phrase"
    topic_slug = "writing_and_graphing_inequalities"
    display_name = "Write an inequality from a phrase"

    _K_RANGE = {"easy": (-10, 10), "medium": (-25, 25), "hard": (-50, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        var = rng.choice(_VAR_POOL)
        k_lo, k_hi = self._K_RANGE[difficulty]
        k = rng.randint(k_lo, k_hi)
        template, symbol = rng.choice(_PHRASE_TEMPLATES)

        # Render k as-is; for negatives, keep the sign inline so the phrase
        # reads naturally (e.g., "x is at most -3").
        phrase = template.format(var=var, k=k)
        inequality_latex = f"{var} {symbol} {k}"

        # Identify the keyword driving the symbol for the explanation.
        keyword_map = {
            "at most": "at most",
            "no more than": "no more than",
            "at least": "at least",
            "no less than": "no less than",
            "greater than": "greater than",
            "more than": "more than",
            "less than": "less than",
            "fewer than": "fewer than",
        }
        keyword_used = next(kw for kw in keyword_map if kw in template)

        symbol_meaning = {
            r"\leq": "less than or equal to (the bound is included)",
            r"\geq": "greater than or equal to (the bound is included)",
            r">": "strictly greater than (the bound is not included)",
            r"<": "strictly less than (the bound is not included)",
        }[symbol]

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (var, k, template),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f'Write an inequality that says "{phrase}".'
            ),
            answer_latex=f"${inequality_latex}$",
            hints=[
                (
                    f'The phrase "{keyword_used}" translates to a specific '
                    f'inequality symbol.'
                ),
                f'"{keyword_used}" means {symbol_meaning}.',
                f"Combine the variable and the bound: ${inequality_latex}$.",
            ],
            solution_steps_latex=[
                (
                    f'Identify the keyword in the phrase: "{keyword_used}".'
                ),
                (
                    f'The keyword "{keyword_used}" corresponds to ${symbol}$.'
                ),
                f"Write the inequality: ${inequality_latex}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-inequalities",
                "#skill-translation",
            ],
        )


# The four inequality symbols with metadata used by the graph-description
# generators. ``circle`` is the visual marker (open or closed) and ``dir``
# is the shading direction on a number line.
_SYMBOL_INFO: tuple[tuple[str, str, str, str], ...] = (
    # (latex_symbol, circle, direction, english_phrase)
    (r"<",     "open",   "left",  "strictly less than"),
    (r">",     "open",   "right", "strictly greater than"),
    (r"\leq",  "closed", "left",  "less than or equal to"),
    (r"\geq",  "closed", "right", "greater than or equal to"),
)


@register
class GraphInequalityDescribe(Generator):
    """Given an inequality, describe its number-line graph in words."""
    generator_id = "graph_inequality_describe"
    topic_slug = "writing_and_graphing_inequalities"
    display_name = "Describe the graph of an inequality"

    _K_RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        var = rng.choice(_VAR_POOL)
        k_lo, k_hi = self._K_RANGE[difficulty]
        k = rng.randint(k_lo, k_hi)
        symbol, circle, direction, phrase = rng.choice(_SYMBOL_INFO)

        inequality_latex = f"{var} {symbol} {k}"

        answer_text = (
            f"{circle} circle at ${k}$, shaded ray going {direction}"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (var, k, symbol),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe the graph of ${inequality_latex}$ on a number line. "
                f"Specify the circle type (open or closed), the location, and "
                f"the direction of shading."
            ),
            answer_latex=answer_text,
            hints=[
                (
                    "A strict inequality ($<$ or $>$) uses an open circle "
                    "because the endpoint is **not** included. An 'or equal' "
                    "inequality ($\\leq$ or $\\geq$) uses a closed circle "
                    "because the endpoint **is** included."
                ),
                (
                    "The inequality symbol tells you which way to shade: "
                    "$<$ or $\\leq$ shades to the left (smaller values); "
                    "$>$ or $\\geq$ shades to the right (larger values)."
                ),
                (
                    f'Here ${symbol}$ means "{phrase}", so use a {circle} circle '
                    f"and shade the ray going {direction}."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read the inequality: ${inequality_latex}$. The bound is at ${k}$."
                ),
                (
                    f'Pick the circle. ${symbol}$ is "{phrase}", so draw a '
                    f"{circle} circle at ${k}$."
                ),
                (
                    f"Pick the shading direction. Values that satisfy "
                    f"${inequality_latex}$ are to the {direction}, so shade "
                    f"the ray going {direction}."
                ),
                f"Final description: {answer_text}.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-inequalities",
                "#skill-visualization",
            ],
        )


@register
class ReadInequalityFromGraphDescription(Generator):
    """Given a verbal graph description, write the matching inequality."""
    generator_id = "read_inequality_from_graph_description"
    topic_slug = "writing_and_graphing_inequalities"
    display_name = "Write an inequality from a graph description"

    _K_RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        var = rng.choice(_VAR_POOL)
        k_lo, k_hi = self._K_RANGE[difficulty]
        k = rng.randint(k_lo, k_hi)
        symbol, circle, direction, phrase = rng.choice(_SYMBOL_INFO)

        inequality_latex = f"{var} {symbol} {k}"
        description = (
            f"A number line has a {circle} circle at ${k}$ and a shaded ray "
            f"going {direction}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (var, k, symbol),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{description} Write the inequality (in terms of ${var}$) "
                f"that this graph represents."
            ),
            answer_latex=f"${inequality_latex}$",
            hints=[
                (
                    "Look at the circle first. A closed circle means the "
                    "endpoint is included (use $\\leq$ or $\\geq$). An open "
                    "circle means the endpoint is not included (use $<$ or $>$)."
                ),
                (
                    "Look at the shading direction. Shading going right means "
                    "larger values ($>$ or $\\geq$). Shading going left means "
                    "smaller values ($<$ or $\\leq$)."
                ),
                (
                    f'Combining the {circle} circle and the {direction}-going '
                    f"shading gives ${symbol}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"The circle is {circle}, so the inequality "
                    f'{"includes" if circle == "closed" else "excludes"} '
                    f'the endpoint.'
                ),
                (
                    f"The shading goes {direction}, which corresponds to "
                    f'{"larger" if direction == "right" else "smaller"} '
                    f"values."
                ),
                (
                    f'Together this matches ${symbol}$ ("{phrase}").'
                ),
                f"Write the inequality: ${inequality_latex}$.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-inequalities",
                "#skill-visualization",
            ],
        )


# ---------------------------------------------------------------------------
# Topic 2: solving_one_step_and_two_step_inequalities
# ---------------------------------------------------------------------------


def _ineq_symbol(kind: str) -> str:
    """Helper: map a short kind tag to its LaTeX symbol."""
    return {"lt": r"<", "gt": r">", "le": r"\leq", "ge": r"\geq"}[kind]


def _flip_symbol(kind: str) -> str:
    """Flip an inequality symbol's direction (used when mul/div by negative)."""
    return {"lt": "gt", "gt": "lt", "le": "ge", "ge": "le"}[kind]


@register
class OneStepInequalityAddSub(Generator):
    """Solve $x + a$ or $x - a$ (one-step, add/subtract) inequalities.

    Backward construction: pick the final bound ``x_bound``, pick a constant
    ``a`` (positive), pick an inequality kind, then compute the right-hand
    side. The student's job is to undo the add/subtract.
    """
    generator_id = "one_step_ineq_addsub"
    topic_slug = "solving_one_step_and_two_step_inequalities"
    display_name = "Solve a one-step add/subtract inequality"

    _X_RANGE = {"easy": (-12, 12), "medium": (-25, 25), "hard": (-60, 60)}
    _A_RANGE = {"easy": (1, 12), "medium": (1, 25), "hard": (1, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X_RANGE[difficulty]
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_bound = rng.randint(x_lo, x_hi)
        a = rng.randint(a_lo, a_hi)
        kind = rng.choice(["lt", "gt", "le", "ge"])
        op = rng.choice(["add", "sub"])
        symbol = _ineq_symbol(kind)

        if op == "add":
            # x + a symbol b  ->  x symbol (b - a), so b = x_bound + a.
            b = x_bound + a
            left_latex = f"x + {a}"
            step_latex = (
                f"Subtract ${a}$ from both sides: $x {symbol} {b} - {a}$."
            )
            arithmetic_latex = f"$x {symbol} {x_bound}$"
        else:
            # x - a symbol b  ->  x symbol (b + a), so b = x_bound - a.
            b = x_bound - a
            left_latex = f"x - {a}"
            step_latex = (
                f"Add ${a}$ to both sides: $x {symbol} {b} + {a}$."
            )
            arithmetic_latex = f"$x {symbol} {x_bound}$"

        statement_latex = f"Solve ${left_latex} {symbol} {b}$ for $x$."
        answer_latex = f"$x {symbol} {x_bound}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x_bound, a, kind, op),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=answer_latex,
            hints=[
                (
                    "Isolate $x$ by undoing the addition or subtraction on the "
                    "left side. The inequality symbol does **not** flip for "
                    "adding or subtracting."
                ),
                step_latex,
                f"Simplify the right side to get {answer_latex}.",
            ],
            solution_steps_latex=[
                f"Start with ${left_latex} {symbol} {b}$.",
                step_latex,
                f"Simplify: {arithmetic_latex}.",
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-inequalities",
                "#skill-multi-step",
            ],
        )


@register
class OneStepInequalityMulDiv(Generator):
    """Solve $ax$ or $x/a$ (one-step, multiply/divide) inequalities.

    About 40% of problems use a negative coefficient, which triggers the
    sign-flip rule. Backward construction: pick ``x_bound``, pick ``a``
    (allowing negatives), pick an inequality kind, then compute the RHS.
    """
    generator_id = "one_step_ineq_muldiv"
    topic_slug = "solving_one_step_and_two_step_inequalities"
    display_name = "Solve a one-step multiply/divide inequality (sign-flip)"

    _X_RANGE = {"easy": (-10, 10), "medium": (-15, 15), "hard": (-25, 25)}
    _A_POS_RANGE = {"easy": (2, 9), "medium": (2, 12), "hard": (2, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X_RANGE[difficulty]
        a_lo, a_hi = self._A_POS_RANGE[difficulty]
        x_bound = rng.randint(x_lo, x_hi)
        a_mag = rng.randint(a_lo, a_hi)
        # Negative about 40% of the time.
        a = a_mag if rng.random() >= 0.4 else -a_mag
        kind = rng.choice(["lt", "gt", "le", "ge"])
        op = rng.choice(["mul", "div"])
        symbol = _ineq_symbol(kind)

        if op == "mul":
            # a*x symbol b  <=> x symbol' b/a. Pick b = a*x_bound so division
            # is exact.
            b = a * x_bound
            left_latex = f"{a}x"
            undo_verb = "Divide"
            undo_by = a
        else:
            # x/a symbol b  <=> x symbol' b*a. Pick b = x_bound / a, requiring
            # x_bound divisible by a. Adjust x_bound to a multiple.
            # Work around divisibility by multiplying: pick a quotient.
            quotient = rng.randint(x_lo, x_hi)
            x_bound = a * quotient  # new x_bound is a * quotient
            # Recompute b so the step is exact.
            b = quotient
            left_latex = f"\\dfrac{{x}}{{{a}}}"
            undo_verb = "Multiply"
            undo_by = a

        # Determine final symbol after potential flip.
        if a < 0:
            final_kind = _flip_symbol(kind)
            flipped = True
        else:
            final_kind = kind
            flipped = False
        final_symbol = _ineq_symbol(final_kind)

        statement_latex = f"Solve ${left_latex} {symbol} {b}$ for $x$."
        answer_latex = f"$x {final_symbol} {x_bound}$"

        flip_note = (
            "Because you are dividing by a negative number, you must **flip** "
            "the inequality symbol."
            if (op == "mul" and a < 0)
            else (
                "Because you are multiplying by a negative number, you must "
                "**flip** the inequality symbol."
                if (op == "div" and a < 0)
                else (
                    "Multiplying or dividing by a **positive** number does "
                    "**not** change the inequality symbol."
                )
            )
        )

        if op == "mul":
            step_line = f"{undo_verb} both sides by ${undo_by}$."
        else:
            step_line = f"{undo_verb} both sides by ${undo_by}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x_bound, a, kind, op),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=answer_latex,
            hints=[
                (
                    "To isolate $x$, undo the multiplication or division on "
                    "the left. Watch the sign of the coefficient: dividing or "
                    "multiplying by a **negative** number flips the inequality."
                ),
                flip_note,
                f"After the step, you should get {answer_latex}.",
            ],
            solution_steps_latex=[
                f"Start with ${left_latex} {symbol} {b}$.",
                step_line,
                flip_note,
                (
                    f"Simplify: {answer_latex}."
                    + (" (Symbol flipped.)" if flipped else "")
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-inequalities",
                "#skill-multi-step",
            ],
        )


@register
class TwoStepInequality(Generator):
    """Solve ``ax + b <op> c`` two-step inequalities, including sign flips.

    About 1/3 of problems have a negative leading coefficient, which triggers
    the sign-flip rule during the division step.
    """
    generator_id = "two_step_ineq"
    topic_slug = "solving_one_step_and_two_step_inequalities"
    display_name = "Solve a two-step inequality"

    _X_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-30, 30)}
    _A_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _B_RANGE = {"easy": (-12, 12), "medium": (-25, 25), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X_RANGE[difficulty]
        a_lo, a_hi = self._A_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        x_bound = rng.randint(x_lo, x_hi)
        a_mag = rng.randint(a_lo, a_hi)
        # Negative coefficient about 1/3 of the time.
        a = a_mag if rng.random() >= (1.0 / 3.0) else -a_mag
        b = rng.randint(b_lo, b_hi)
        kind = rng.choice(["lt", "gt", "le", "ge"])
        symbol = _ineq_symbol(kind)

        # ax + b symbol c <=> ax symbol (c - b) <=> x symbol' (c-b)/a
        # Pick c so the intermediate and final are clean: c = a*x_bound + b.
        c = a * x_bound + b

        # Render "ax + b" with sign-aware formatting for b.
        if b >= 0:
            left_latex = f"{a}x + {b}"
        else:
            left_latex = f"{a}x - {abs(b)}"

        # Final symbol after flip.
        if a < 0:
            final_kind = _flip_symbol(kind)
            flipped = True
        else:
            final_kind = kind
            flipped = False
        final_symbol = _ineq_symbol(final_kind)

        statement_latex = f"Solve ${left_latex} {symbol} {c}$ for $x$."
        answer_latex = f"$x {final_symbol} {x_bound}$"

        sub_step = (
            f"Subtract ${b}$ from both sides" if b >= 0
            else f"Add ${abs(b)}$ to both sides"
        )
        middle_latex = f"{a}x {symbol} {c - b}"

        if a < 0:
            flip_note = (
                "Dividing by a negative number **flips** the inequality symbol."
            )
        else:
            flip_note = (
                "Dividing by a positive number keeps the inequality symbol "
                "the same."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x_bound, a, b, kind),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=answer_latex,
            hints=[
                (
                    "Treat this like a two-step equation: first undo the "
                    "constant, then undo the coefficient. Watch the sign of "
                    "the coefficient in the second step."
                ),
                f"{sub_step}: ${middle_latex}$.",
                flip_note + f" Final answer: {answer_latex}.",
            ],
            solution_steps_latex=[
                f"Start with ${left_latex} {symbol} {c}$.",
                f"{sub_step}: ${middle_latex}$.",
                f"Divide both sides by ${a}$. " + flip_note,
                (
                    f"{answer_latex}"
                    + (" (Symbol flipped.)" if flipped else "")
                ),
            ],
            tags=[
                "#branch-pre-algebra",
                "#topic-inequalities",
                "#skill-multi-step",
            ],
        )
