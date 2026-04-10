"""Inequality generators (Phase 2c Cluster 2).

Five topic slugs matching wiki/topics/algebra/:

- inequalities_and_their_graphs (Ch 3.1)
- solving_multi_step_inequalities (Ch 3.3)
- compound_inequalities (Ch 3.4)
- absolute_value_inequalities (Ch 3.5)
- systems_of_linear_inequalities (Ch 4.6)

15 generators, 3 per topic. Backward construction throughout: pick the
critical x-value or solution set first, then derive the parameters so
the algebra is always clean.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


# Shared helpers ------------------------------------------------------------

_SYMBOLS = ("<", ">", r"\leq", r"\geq")
_PHRASE_FORWARD = {
    "<": "is less than",
    ">": "is greater than",
    r"\leq": "is at most",
    r"\geq": "is at least",
}
# When we flip the inequality (multiply/divide by negative), map old -> new.
_FLIP = {
    "<": ">",
    ">": "<",
    r"\leq": r"\geq",
    r"\geq": r"\leq",
}


def _signed_constant(n: int) -> str:
    """Format a constant for use on the RHS of an inequality (just the value)."""
    return str(n)


def _linear_term(coef: int, const: int) -> str:
    """Render ax + b with correct sign handling."""
    if coef == 1:
        lhs = "x"
    elif coef == -1:
        lhs = "-x"
    else:
        lhs = f"{coef}x"
    if const == 0:
        return lhs
    if const > 0:
        return f"{lhs} + {const}"
    return f"{lhs} - {abs(const)}"


def _linear_term_with_var(coef: int, const: int, var: str) -> str:
    """Render a*var + b where var is a letter like x or y."""
    if coef == 1:
        lhs = var
    elif coef == -1:
        lhs = f"-{var}"
    else:
        lhs = f"{coef}{var}"
    if const == 0:
        return lhs
    if const > 0:
        return f"{lhs} + {const}"
    return f"{lhs} - {abs(const)}"


# ============================================================================
# Topic 1: inequalities_and_their_graphs
# ============================================================================

@register
class InequalityClassifyFromSymbol(Generator):
    """Translate between inequality symbol and English phrase.

    Two directions: phrase -> symbol, or symbol -> phrase. Four inequality
    types. Values chosen from a wide integer range for bank diversity.
    """
    generator_id = "inequality_classify_from_symbol"
    topic_slug = "inequalities_and_their_graphs"
    display_name = "Translate inequality phrase <-> symbol"

    _RANGES = {"easy": (-10, 10), "medium": (-25, 25), "hard": (-60, 60)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        symbol = rng.choice(list(_SYMBOLS))
        value = rng.randint(lo, hi)
        direction = rng.choice(["phrase_to_symbol", "symbol_to_phrase"])
        phrase = _PHRASE_FORWARD[symbol]

        if direction == "phrase_to_symbol":
            statement = (
                f"Write the inequality described by the phrase: "
                f"\"$x$ {phrase} {value}\"."
            )
            answer = f"$x {symbol} {value}$"
            hints = [
                r"Each inequality symbol corresponds to a specific phrase.",
                r"$>$ means \"is greater than\". $<$ means \"is less than\". "
                r"$\geq$ means \"is at least\" (or \"is greater than or equal to\"). "
                r"$\leq$ means \"is at most\" (or \"is less than or equal to\").",
                f"The phrase \"{phrase}\" matches the symbol ${symbol}$.",
            ]
            steps = [
                f"Identify the phrase: \"{phrase}\".",
                f"Match the phrase to its inequality symbol: ${symbol}$.",
                f"Write the inequality with $x$ on the left: $x {symbol} {value}$.",
            ]
        else:  # symbol_to_phrase
            statement = f"Describe the inequality $x {symbol} {value}$ in words."
            answer = f"$x$ {phrase} {value}"
            hints = [
                r"Each inequality symbol corresponds to a specific phrase.",
                r"$>$ means \"is greater than\". $<$ means \"is less than\". "
                r"$\geq$ means \"is at least\" (or \"is greater than or equal to\"). "
                r"$\leq$ means \"is at most\" (or \"is less than or equal to\").",
                f"The symbol ${symbol}$ corresponds to the phrase \"{phrase}\".",
            ]
            steps = [
                f"Read the symbol ${symbol}$.",
                f"Translate ${symbol}$ into English: \"{phrase}\".",
                f"Write the full statement: \"$x$ {phrase} {value}\".",
            ]

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (symbol, value, direction)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-visualization"],
        )


@register
class InequalityCheckSolution(Generator):
    """Given $ax + b \\text{ op } c$ and a candidate value, test whether it satisfies."""
    generator_id = "inequality_check_solution"
    topic_slug = "inequalities_and_their_graphs"
    display_name = "Check whether a value is a solution to an inequality"

    _A_RANGE = {"easy": (1, 5), "medium": (1, 9), "hard": (1, 15)}
    _RHS_RANGE = {"easy": (-12, 12), "medium": (-25, 25), "hard": (-50, 50)}
    _VAL_RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        rhs_lo, rhs_hi = self._RHS_RANGE[difficulty]
        v_lo, v_hi = self._VAL_RANGE[difficulty]
        a = rng.randint(a_lo, a_hi)
        b = rng.randint(rhs_lo, rhs_hi)
        c = rng.randint(rhs_lo, rhs_hi)
        x_test = rng.randint(v_lo, v_hi)
        symbol = rng.choice(list(_SYMBOLS))

        lhs_value = a * x_test + b
        comparisons = {
            "<": lhs_value < c,
            ">": lhs_value > c,
            r"\leq": lhs_value <= c,
            r"\geq": lhs_value >= c,
        }
        is_solution = comparisons[symbol]
        answer_text = "solution" if is_solution else "not a solution"

        lhs_str = _linear_term(a, b)
        ineq_latex = f"{lhs_str} {symbol} {c}"
        # Substituted LHS expression, preserving parentheses around the substituted value.
        sub_expr = f"{a}({x_test}) + ({b})" if b < 0 else f"{a}({x_test}) + {b}"
        if a == 1:
            sub_expr = f"({x_test}) + ({b})" if b < 0 else f"({x_test}) + {b}"
        if b == 0:
            sub_expr = f"{a}({x_test})" if a != 1 else f"({x_test})"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, x_test, symbol)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Is $x = {x_test}$ a solution of the inequality ${ineq_latex}$? "
                "Answer \"solution\" or \"not a solution\"."
            ),
            answer_latex=answer_text,
            hints=[
                f"Substitute $x = {x_test}$ into the left side of the inequality.",
                f"Simplify the left side to a single number.",
                f"Compare that number to ${c}$ using the symbol ${symbol}$.",
            ],
            solution_steps_latex=[
                f"Substitute $x = {x_test}$ into ${lhs_str}$: ${sub_expr}$.",
                f"Simplify the left side: ${sub_expr} = {lhs_value}$.",
                f"Compare: is ${lhs_value} {symbol} {c}$? "
                + ("Yes." if is_solution else "No."),
                f"Therefore $x = {x_test}$ is {answer_text}.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-formula-substitution"],
        )


@register
class InequalityGraphOpenClosed(Generator):
    """Describe the number-line graph of $x \\text{ op } k$ in words."""
    generator_id = "inequality_graph_open_closed"
    topic_slug = "inequalities_and_their_graphs"
    display_name = "Describe the graph of a one-variable inequality"

    _RANGES = {"easy": (-10, 10), "medium": (-25, 25), "hard": (-60, 60)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        symbol = rng.choice(list(_SYMBOLS))
        k = rng.randint(lo, hi)

        is_closed = symbol in (r"\leq", r"\geq")
        circle = "closed" if is_closed else "open"
        direction = "right" if symbol in (">", r"\geq") else "left"
        answer = f"{circle} circle at {k}, arrow pointing {direction}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (symbol, k)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Describe the graph of $x {symbol} {k}$ on a number line. "
                "State whether the circle at the critical value is open or "
                "closed, and which direction the arrow points."
            ),
            answer_latex=answer,
            hints=[
                r"A strict inequality ($<$ or $>$) uses an **open** circle because "
                r"the critical value is not included.",
                r"A non-strict inequality ($\leq$ or $\geq$) uses a **closed** "
                r"circle because the critical value is included.",
                r"For $>$ or $\geq$ the arrow points **right** (larger values). "
                r"For $<$ or $\leq$ the arrow points **left** (smaller values).",
            ],
            solution_steps_latex=[
                f"The critical value is ${k}$.",
                f"The symbol ${symbol}$ is "
                + ("non-strict, so the circle is closed." if is_closed
                   else "strict, so the circle is open."),
                f"The symbol ${symbol}$ points "
                + ("right (values greater than or equal to the critical value)."
                   if symbol in (">", r"\geq")
                   else "left (values less than or equal to the critical value)."),
                f"Graph: {answer}.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-visualization"],
        )


# ============================================================================
# Topic 2: solving_multi_step_inequalities
# ============================================================================

@register
class MultiStepIneqTwoStep(Generator):
    """Solve $ax + b \\text{ op } c$ for $x$, with occasional sign flips."""
    generator_id = "multi_step_ineq_two_step"
    topic_slug = "solving_multi_step_inequalities"
    display_name = "Solve ax + b <op> c"

    _A_MAG = {"easy": (1, 6), "medium": (2, 12), "hard": (2, 20)}
    _X_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _B_RANGE = {"easy": (-12, 12), "medium": (-25, 25), "hard": (-50, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_MAG[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        a_mag = rng.randint(a_lo, a_hi)
        # Sign-flip happens when a is negative. ~1/3 of the time.
        flip = rng.random() < 0.33
        a = -a_mag if flip else a_mag
        if a == 0:
            a = 1

        x_val = rng.randint(x_lo, x_hi)
        b = rng.randint(b_lo, b_hi)
        c = a * x_val + b  # clean integer critical point

        symbol = rng.choice(list(_SYMBOLS))
        # When we divide by negative a, the symbol flips.
        final_symbol = _FLIP[symbol] if a < 0 else symbol

        lhs_str = _linear_term(a, b)
        problem_latex = f"{lhs_str} {symbol} {c}"

        # Intermediate: ax (op) (c - b)
        after_sub = c - b
        # Division step: x (final_op) (after_sub / a)
        # By construction after_sub = a * x_val, so division gives x_val exactly.

        hints = [
            f"Isolate the $x$ term: subtract ${b}$ from both sides.",
            (
                f"Then divide both sides by ${a}$. "
                "Because you are dividing by a negative number, **flip** the "
                "inequality symbol."
                if a < 0
                else f"Then divide both sides by ${a}$."
            ),
            f"The solution is $x {final_symbol} {x_val}$.",
        ]

        steps = [
            f"Start with ${problem_latex}$.",
            f"Subtract ${b}$ from both sides: ${a}x {symbol} {after_sub}$.",
        ]
        if a < 0:
            steps.append(
                f"Divide both sides by ${a}$. Because ${a} < 0$, flip the symbol: "
                f"$x {final_symbol} \\dfrac{{{after_sub}}}{{{a}}}$."
            )
        else:
            steps.append(
                f"Divide both sides by ${a}$: "
                f"$x {final_symbol} \\dfrac{{{after_sub}}}{{{a}}}$."
            )
        steps.append(f"Simplify: $x {final_symbol} {x_val}$.")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, symbol)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${problem_latex}$ for $x$.",
            answer_latex=f"$x {final_symbol} {x_val}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class MultiStepIneqDistribution(Generator):
    """Solve $a(bx + c) \\text{ op } d$ by distributing first."""
    generator_id = "multi_step_ineq_distribution"
    topic_slug = "solving_multi_step_inequalities"
    display_name = "Solve a(bx + c) <op> d"

    _A_MAG = {"easy": (2, 5), "medium": (2, 8), "hard": (2, 12)}
    _B_MAG = {"easy": (1, 4), "medium": (1, 7), "hard": (1, 10)}
    _X_RANGE = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _C_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_MAG[difficulty]
        b_lo, b_hi = self._B_MAG[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]

        a_mag = rng.randint(a_lo, a_hi)
        b_mag = rng.randint(b_lo, b_hi)
        # Sign-flip on a ~1/3 of the time. Inner b is always positive here
        # so the flip logic is localized to the outer coefficient.
        flip = rng.random() < 0.33
        a = -a_mag if flip else a_mag
        b = b_mag  # positive for clarity
        x_val = rng.randint(x_lo, x_hi)
        c = rng.randint(c_lo, c_hi)
        # d = a*(b*x_val + c)
        d = a * (b * x_val + c)

        symbol = rng.choice(list(_SYMBOLS))
        # After we distribute the signed a, the effective coefficient of x
        # becomes a*b. The sign flip only happens when we later divide by (a*b).
        full_coef = a * b
        final_symbol = _FLIP[symbol] if full_coef < 0 else symbol

        inner = _linear_term_with_var(b, c, "x")
        statement_latex = f"{a}({inner}) {symbol} {d}"
        # Distributed form: (a*b)x + (a*c)
        dist_lhs = _linear_term(full_coef, a * c)

        hints = [
            f"First distribute the ${a}$ across the parentheses.",
            f"After distributing you get ${dist_lhs} {symbol} {d}$.",
            (
                "When dividing by a negative coefficient, flip the inequality."
                if full_coef < 0
                else "Now solve it like a standard two-step inequality."
            ),
        ]

        after_sub = d - a * c  # the RHS after subtracting a*c from both sides
        steps = [
            f"Start with ${statement_latex}$.",
            f"Distribute ${a}$: ${dist_lhs} {symbol} {d}$.",
            f"Subtract ${a * c}$ from both sides: ${full_coef}x {symbol} {after_sub}$.",
        ]
        if full_coef < 0:
            steps.append(
                f"Divide both sides by ${full_coef}$. Because ${full_coef} < 0$, "
                f"flip the symbol: $x {final_symbol} \\dfrac{{{after_sub}}}{{{full_coef}}}$."
            )
        else:
            steps.append(
                f"Divide both sides by ${full_coef}$: "
                f"$x {final_symbol} \\dfrac{{{after_sub}}}{{{full_coef}}}$."
            )
        steps.append(f"Simplify: $x {final_symbol} {x_val}$.")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, symbol)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${statement_latex}$ for $x$.",
            answer_latex=f"$x {final_symbol} {x_val}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class MultiStepIneqVariablesBothSides(Generator):
    """Solve $ax + b \\text{ op } cx + d$ (variables on both sides)."""
    generator_id = "multi_step_ineq_variables_both_sides"
    topic_slug = "solving_multi_step_inequalities"
    display_name = "Solve ax + b <op> cx + d"

    _COEF = {"easy": (1, 8), "medium": (2, 12), "hard": (2, 18)}
    _CONST = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-30, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF[difficulty]
        const_lo, const_hi = self._CONST[difficulty]

        # Pick a, c with a != c so the net coefficient (a - c) != 0.
        # Allow sign flip ~1/3 of the time: that means after moving cx to the
        # left we get a negative net coefficient.
        while True:
            a = rng.randint(coef_lo, coef_hi)
            c = rng.randint(coef_lo, coef_hi)
            if a == c:
                continue
            net = a - c
            flip_desired = rng.random() < 0.33
            if flip_desired and net > 0:
                # swap to force net negative
                a, c = c, a
                net = a - c
            if net != 0:
                break

        x_val = rng.randint(const_lo, const_hi)
        b = rng.randint(const_lo, const_hi)
        # d = a*x_val + b - c*x_val  (makes equality at x_val)
        d = a * x_val + b - c * x_val

        symbol = rng.choice(list(_SYMBOLS))
        final_symbol = _FLIP[symbol] if net < 0 else symbol

        lhs_str = _linear_term(a, b)
        rhs_str = _linear_term(c, d)
        problem_latex = f"{lhs_str} {symbol} {rhs_str}"

        after_sub_rhs = d - b  # after subtracting b from both sides and cx from both sides

        hints = [
            "Get all $x$ terms on one side and all constants on the other.",
            f"Subtract ${c}x$ from both sides: ${net}x + {b} {symbol} {d}$.",
            (
                f"Then subtract ${b}$ and divide by ${net}$. "
                "Remember to flip the inequality when dividing by a negative."
                if net < 0
                else f"Then subtract ${b}$ and divide by ${net}$."
            ),
        ]

        steps = [
            f"Start with ${problem_latex}$.",
            f"Subtract ${c}x$ from both sides: ${net}x + {b} {symbol} {d}$.",
            f"Subtract ${b}$ from both sides: ${net}x {symbol} {after_sub_rhs}$.",
        ]
        if net < 0:
            steps.append(
                f"Divide both sides by ${net}$. Because ${net} < 0$, flip the symbol: "
                f"$x {final_symbol} \\dfrac{{{after_sub_rhs}}}{{{net}}}$."
            )
        else:
            steps.append(
                f"Divide both sides by ${net}$: "
                f"$x {final_symbol} \\dfrac{{{after_sub_rhs}}}{{{net}}}$."
            )
        steps.append(f"Simplify: $x {final_symbol} {x_val}$.")

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, symbol)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${problem_latex}$ for $x$.",
            answer_latex=f"$x {final_symbol} {x_val}$",
            hints=hints,
            solution_steps_latex=steps,
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


# ============================================================================
# Topic 3: compound_inequalities
# ============================================================================

@register
class CompoundIneqAndThreePart(Generator):
    """Solve a three-part \"between\" compound inequality $L < ax + b < U$."""
    generator_id = "compound_ineq_and_three_part"
    topic_slug = "compound_inequalities"
    display_name = "Solve L < ax + b < U"

    _A_RANGE = {"easy": (1, 5), "medium": (2, 8), "hard": (2, 12)}
    _X_RANGE = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-18, 18)}
    _B_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _WIDTH = {"easy": (2, 6), "medium": (3, 10), "hard": (4, 16)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        w_lo, w_hi = self._WIDTH[difficulty]

        a = rng.randint(a_lo, a_hi)  # positive only (keeps symbol behavior simple)
        x_low = rng.randint(x_lo, x_hi)
        width = rng.randint(w_lo, w_hi)
        x_high = x_low + width
        b = rng.randint(b_lo, b_hi)

        L = a * x_low + b
        U = a * x_high + b

        # Pick strict/non-strict independently for left and right bounds.
        left_strict = rng.choice([True, False])
        right_strict = rng.choice([True, False])
        left_sym = "<" if left_strict else r"\leq"
        right_sym = "<" if right_strict else r"\leq"

        lhs_str = _linear_term(a, b)
        problem_latex = f"{L} {left_sym} {lhs_str} {right_sym} {U}"
        final_latex = f"{x_low} {left_sym} x {right_sym} {x_high}"

        # Intermediate after subtracting b from all three parts
        mid_L = L - b
        mid_U = U - b

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, x_low, x_high, left_sym, right_sym),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve the compound inequality ${problem_latex}$.",
            answer_latex=f"${final_latex}$",
            hints=[
                "Isolate $x$ by doing the same operation to all three parts.",
                f"Subtract ${b}$ from all three parts: ${mid_L} {left_sym} {a}x {right_sym} {mid_U}$.",
                f"Divide all three parts by ${a}$: ${final_latex}$.",
            ],
            solution_steps_latex=[
                f"Start with ${problem_latex}$.",
                f"Subtract ${b}$ from all three parts: ${mid_L} {left_sym} {a}x {right_sym} {mid_U}$.",
                f"Divide all three parts by ${a}$: ${final_latex}$.",
                f"Solution: ${final_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class CompoundIneqAndTwoParts(Generator):
    """Solve an AND compound like $x + p > q$ and $rx < s$, take the intersection."""
    generator_id = "compound_ineq_and_two_parts"
    topic_slug = "compound_inequalities"
    display_name = "Solve a compound AND inequality"

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _COEF = {"easy": (1, 5), "medium": (2, 8), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        c_lo, c_hi = self._COEF[difficulty]

        # Build the final answer: x_low < x < x_high (or with <=).
        x_low = rng.randint(lo, hi - 2)
        x_high = rng.randint(x_low + 1, hi + 1)

        # Left part: x + p op1 q  with solution x > x_low (or x >= x_low).
        p = rng.randint(lo, hi)
        left_strict = rng.choice([True, False])
        left_sym = ">" if left_strict else r"\geq"
        # x + p > q  =>  x > q - p, so pick q so q - p = x_low
        q = x_low + p

        # Right part: r*x op2 s with solution x < x_high.
        r = rng.randint(c_lo, c_hi)  # positive r so no symbol flip
        right_strict = rng.choice([True, False])
        right_sym = "<" if right_strict else r"\leq"
        # r*x < s  =>  x < s/r, so pick s = r * x_high
        s = r * x_high

        part1 = _linear_term(1, p)  # "x + p"
        part2 = _linear_term(r, 0)  # "rx"
        problem_latex = (
            f"{part1} {left_sym} {q} \\text{{ and }} {part2} {right_sym} {s}"
        )
        intersection_sym_left = ">" if left_strict else r"\geq"
        intersection_sym_right = "<" if right_strict else r"\leq"
        # Combined compound form: x_low (flip of left_sym) x (right_sym) x_high
        # "x > x_low" is the same as "x_low < x"
        combined_left = "<" if left_strict else r"\leq"
        final_latex = f"{x_low} {combined_left} x {intersection_sym_right} {x_high}"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (p, q, r, s, left_sym, right_sym),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve the compound inequality ${problem_latex}$ "
                "and write the solution as a single compound statement."
            ),
            answer_latex=f"${final_latex}$",
            hints=[
                r"Solve each inequality separately, then take the **intersection** "
                r"(the values that satisfy **both** parts).",
                f"First part: ${part1} {left_sym} {q}$ gives $x {intersection_sym_left} {x_low}$.",
                f"Second part: ${part2} {right_sym} {s}$ gives $x {intersection_sym_right} {x_high}$.",
            ],
            solution_steps_latex=[
                f"Solve the first part: ${part1} {left_sym} {q}$. Subtract ${p}$: "
                f"$x {intersection_sym_left} {x_low}$.",
                f"Solve the second part: ${part2} {right_sym} {s}$. Divide by ${r}$: "
                f"$x {intersection_sym_right} {x_high}$.",
                f"The intersection requires both: $x {intersection_sym_left} {x_low}$ "
                f"and $x {intersection_sym_right} {x_high}$.",
                f"Write as a single compound: ${final_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class CompoundIneqOr(Generator):
    """Solve an OR compound $ax + b < c$ or $dx + e > f$, take the union."""
    generator_id = "compound_ineq_or"
    topic_slug = "compound_inequalities"
    display_name = "Solve a compound OR inequality"

    _RANGES = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _COEF = {"easy": (1, 5), "medium": (2, 8), "hard": (2, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        c_lo, c_hi = self._COEF[difficulty]

        # For an OR union that is not all reals, we want left-part solution
        # x < x_low and right-part solution x > x_high with x_low < x_high.
        x_low = rng.randint(lo, hi - 2)
        x_high = rng.randint(x_low + 1, hi + 1)

        # Left: a*x + b < c with solution x < x_low
        a = rng.randint(c_lo, c_hi)  # positive
        b = rng.randint(lo, hi)
        c = a * x_low + b

        # Right: d*x + e > f with solution x > x_high
        d = rng.randint(c_lo, c_hi)
        e = rng.randint(lo, hi)
        f = d * x_high + e

        left_strict = rng.choice([True, False])
        right_strict = rng.choice([True, False])
        left_sym = "<" if left_strict else r"\leq"
        right_sym = ">" if right_strict else r"\geq"

        part1 = _linear_term(a, b)
        part2 = _linear_term(d, e)
        problem_latex = (
            f"{part1} {left_sym} {c} \\text{{ or }} {part2} {right_sym} {f}"
        )
        final_latex = (
            f"x {left_sym} {x_low} \\text{{ or }} x {right_sym} {x_high}"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, c, d, e, f, left_sym, right_sym),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve the compound inequality ${problem_latex}$ "
                "and write the solution as a union."
            ),
            answer_latex=f"${final_latex}$",
            hints=[
                r"Solve each inequality separately, then take the **union** "
                r"(the values that satisfy **either** part).",
                f"First part: ${part1} {left_sym} {c}$ gives $x {left_sym} {x_low}$.",
                f"Second part: ${part2} {right_sym} {f}$ gives $x {right_sym} {x_high}$.",
            ],
            solution_steps_latex=[
                f"Solve the first part: ${part1} {left_sym} {c}$. Subtract ${b}$ "
                f"and divide by ${a}$: $x {left_sym} {x_low}$.",
                f"Solve the second part: ${part2} {right_sym} {f}$. Subtract ${e}$ "
                f"and divide by ${d}$: $x {right_sym} {x_high}$.",
                f"Union: values that satisfy either part: ${final_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


# ============================================================================
# Topic 4: absolute_value_inequalities
# ============================================================================

@register
class AbsValIneqLessThan(Generator):
    """Solve $|ax + b| < c$ (becomes a compound AND). Positive $c$."""
    generator_id = "abs_val_ineq_less_than"
    topic_slug = "absolute_value_inequalities"
    display_name = "Solve |ax + b| < c"

    _A_RANGE = {"easy": (1, 5), "medium": (2, 8), "hard": (2, 12)}
    _X_HALF = {"easy": (1, 6), "medium": (2, 12), "hard": (3, 20)}
    _B_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-30, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        h_lo, h_hi = self._X_HALF[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        a = rng.randint(a_lo, a_hi)  # positive
        # Pick a symmetric interval around x_center of half-width h.
        h = rng.randint(h_lo, h_hi)
        x_center = rng.randint(b_lo // 2, b_hi // 2)
        x_low = x_center - h
        x_high = x_center + h
        # Choose b so that ax + b = 0 at x = x_center means b = -a*x_center
        b = -a * x_center
        # c = a*h (half-width scaled by a)
        c = a * h

        strict = rng.choice([True, False])
        sym = "<" if strict else r"\leq"
        compound_sym_left = "<" if strict else r"\leq"
        compound_sym_right = "<" if strict else r"\leq"

        inside = _linear_term(a, b)
        problem_latex = f"|{inside}| {sym} {c}"
        split_latex = f"{-c} {compound_sym_left} {inside} {compound_sym_right} {c}"
        final_latex = f"{x_low} {compound_sym_left} x {compound_sym_right} {x_high}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, sym)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${problem_latex}$.",
            answer_latex=f"${final_latex}$",
            hints=[
                r"When $|E| < c$ with $c > 0$, rewrite as the compound inequality "
                r"$-c < E < c$ (an AND).",
                f"Here the split is: ${split_latex}$.",
                f"Solve the three-part inequality for $x$ to get ${final_latex}$.",
            ],
            solution_steps_latex=[
                f"Start with ${problem_latex}$.",
                f"Rewrite as a three-part compound (AND): ${split_latex}$.",
                f"Subtract ${b}$ from all three parts: "
                f"${-c - b} {compound_sym_left} {a}x {compound_sym_right} {c - b}$.",
                f"Divide all three parts by ${a}$: ${final_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class AbsValIneqGreaterThan(Generator):
    """Solve $|ax + b| > c$ (becomes a compound OR). Positive $c$."""
    generator_id = "abs_val_ineq_greater_than"
    topic_slug = "absolute_value_inequalities"
    display_name = "Solve |ax + b| > c"

    _A_RANGE = {"easy": (1, 5), "medium": (2, 8), "hard": (2, 12)}
    _X_HALF = {"easy": (1, 6), "medium": (2, 12), "hard": (3, 20)}
    _B_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-30, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        h_lo, h_hi = self._X_HALF[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        a = rng.randint(a_lo, a_hi)  # positive
        h = rng.randint(h_lo, h_hi)
        x_center = rng.randint(b_lo // 2, b_hi // 2)
        x_low = x_center - h
        x_high = x_center + h
        b = -a * x_center
        c = a * h

        strict = rng.choice([True, False])
        sym = ">" if strict else r"\geq"
        out_sym_left = "<" if strict else r"\leq"
        out_sym_right = ">" if strict else r"\geq"

        inside = _linear_term(a, b)
        problem_latex = f"|{inside}| {sym} {c}"
        split_case1 = f"{inside} {out_sym_left} {-c}"
        split_case2 = f"{inside} {out_sym_right} {c}"
        final_latex = (
            f"x {out_sym_left} {x_low} \\text{{ or }} x {out_sym_right} {x_high}"
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, sym)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve ${problem_latex}$.",
            answer_latex=f"${final_latex}$",
            hints=[
                r"When $|E| > c$ with $c > 0$, rewrite as the compound inequality "
                r"$E < -c$ OR $E > c$.",
                f"Here the split is: ${split_case1}$ or ${split_case2}$.",
                f"Solve each part for $x$ to get ${final_latex}$.",
            ],
            solution_steps_latex=[
                f"Start with ${problem_latex}$.",
                f"Rewrite as a compound (OR): ${split_case1}$ or ${split_case2}$.",
                f"Case 1: ${split_case1}$. Subtract ${b}$ and divide by ${a}$: "
                f"$x {out_sym_left} {x_low}$.",
                f"Case 2: ${split_case2}$. Subtract ${b}$ and divide by ${a}$: "
                f"$x {out_sym_right} {x_high}$.",
                f"Union: ${final_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-multi-step"],
        )


@register
class AbsValIneqEdgeCases(Generator):
    """Recognize edge cases: $|E| \\geq 0$, $|E| < \\text{neg}$, $|E| > \\text{neg}$."""
    generator_id = "abs_val_ineq_edge_cases"
    topic_slug = "absolute_value_inequalities"
    display_name = "Edge cases: all real numbers or no solution"
    bank_count_per_difficulty = 18

    _A_RANGE = {"easy": (1, 4), "medium": (1, 7), "hard": (1, 10)}
    _B_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _C_RANGE = {"easy": (1, 8), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        c_lo, c_hi = self._C_RANGE[difficulty]

        a = rng.randint(a_lo, a_hi)
        b = rng.randint(b_lo, b_hi)

        # Four edge-case categories (all produce all-reals or no-solution):
        # 1. |E| > -c  (any |E|, always >=0 > -c, so all reals)
        # 2. |E| < -c  (absolute value cannot be negative, no solution)
        # 3. |E| >= -c (all reals)
        # 4. |E| <= -c (no solution)
        # 5. |E| >= 0  (all reals; |anything| >= 0)
        # 6. |E| > 0   (all reals except where inside = 0; we avoid this one)
        category = rng.choice([
            "gt_neg", "lt_neg", "geq_neg", "leq_neg", "geq_zero"
        ])

        inside = _linear_term(a, b)

        if category == "gt_neg":
            c = -rng.randint(c_lo, c_hi)
            sym = ">"
            answer = "all real numbers"
            reason = (
                f"$|{inside}|$ is always $\\geq 0$, which is greater than any "
                f"negative number like ${c}$."
            )
        elif category == "lt_neg":
            c = -rng.randint(c_lo, c_hi)
            sym = "<"
            answer = "no solution"
            reason = (
                f"$|{inside}|$ is always $\\geq 0$, so it cannot be less than "
                f"the negative number ${c}$."
            )
        elif category == "geq_neg":
            c = -rng.randint(c_lo, c_hi)
            sym = r"\geq"
            answer = "all real numbers"
            reason = (
                f"$|{inside}|$ is always $\\geq 0$, which is $\\geq$ any negative "
                f"number like ${c}$."
            )
        elif category == "leq_neg":
            c = -rng.randint(c_lo, c_hi)
            sym = r"\leq"
            answer = "no solution"
            reason = (
                f"$|{inside}|$ is always $\\geq 0$, so it cannot be $\\leq$ the "
                f"negative number ${c}$."
            )
        else:  # geq_zero
            c = 0
            sym = r"\geq"
            answer = "all real numbers"
            reason = (
                f"The absolute value of any real number is always $\\geq 0$, "
                f"so $|{inside}| \\geq 0$ holds for every value of $x$."
            )

        problem_latex = f"|{inside}| {sym} {c}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, sym, category)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Solve ${problem_latex}$. Answer \"all real numbers\" or "
                "\"no solution\"."
            ),
            answer_latex=answer,
            hints=[
                r"Recall: $|E| \geq 0$ for every real value of $E$.",
                r"Compare the right side to $0$. If the inequality is satisfied "
                r"regardless of the value of $E$, the answer is \"all real numbers\". "
                r"If it can never be satisfied, the answer is \"no solution\".",
                reason,
            ],
            solution_steps_latex=[
                f"Start with ${problem_latex}$.",
                r"Apply the fact that $|\text{expression}| \geq 0$ for every real input.",
                reason,
                f"Therefore the solution set is: {answer}.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-visualization"],
        )


# ============================================================================
# Topic 5: systems_of_linear_inequalities
# ============================================================================

@register
class SystemLinIneqTestPoint(Generator):
    """Given two linear inequalities and a point, check whether the point is in the solution region."""
    generator_id = "system_lin_ineq_test_point"
    topic_slug = "systems_of_linear_inequalities"
    display_name = "Is a point in the solution region of a system?"

    _M_RANGE = {"easy": (1, 4), "medium": (1, 7), "hard": (1, 10)}
    _B_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}
    _PT_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        p_lo, p_hi = self._PT_RANGE[difficulty]

        m1 = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m1 = -m1
        b1 = rng.randint(b_lo, b_hi)
        m2 = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m2 = -m2
        b2 = rng.randint(b_lo, b_hi)

        sym1 = rng.choice(list(_SYMBOLS))
        sym2 = rng.choice(list(_SYMBOLS))

        x_pt = rng.randint(p_lo, p_hi)
        y_pt = rng.randint(p_lo, p_hi)

        lhs1 = y_pt
        rhs1 = m1 * x_pt + b1
        lhs2 = y_pt
        rhs2 = m2 * x_pt + b2

        def evaluate(lhs: int, rhs: int, sym: str) -> bool:
            return {
                "<": lhs < rhs,
                ">": lhs > rhs,
                r"\leq": lhs <= rhs,
                r"\geq": lhs >= rhs,
            }[sym]

        ok1 = evaluate(lhs1, rhs1, sym1)
        ok2 = evaluate(lhs2, rhs2, sym2)
        in_region = ok1 and ok2
        answer = "in the solution region" if in_region else "not in the solution region"

        rhs1_str = _linear_term_with_var(m1, b1, "x")
        rhs2_str = _linear_term_with_var(m2, b2, "x")
        system_latex = f"\\begin{{cases}} y {sym1} {rhs1_str} \\\\ y {sym2} {rhs2_str} \\end{{cases}}"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (m1, b1, sym1, m2, b2, sym2, x_pt, y_pt),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Is the point $({x_pt}, {y_pt})$ in the solution region of the "
                f"system ${system_latex}$? Answer \"in the solution region\" "
                "or \"not in the solution region\"."
            ),
            answer_latex=answer,
            hints=[
                "Substitute the point into each inequality separately.",
                "The point is in the solution region only if **both** "
                "inequalities are satisfied.",
                f"Check the first: is ${y_pt} {sym1} {rhs1}$? "
                + ("Yes." if ok1 else "No."),
            ],
            solution_steps_latex=[
                f"Substitute $({x_pt}, {y_pt})$ into the first inequality: "
                f"${y_pt} {sym1} {rhs1_str}$ becomes ${y_pt} {sym1} {rhs1}$. "
                + ("True." if ok1 else "False."),
                f"Substitute into the second inequality: "
                f"${y_pt} {sym2} {rhs2_str}$ becomes ${y_pt} {sym2} {rhs2}$. "
                + ("True." if ok2 else "False."),
                (
                    "Both inequalities are satisfied, so the point is in the solution region."
                    if in_region
                    else "At least one inequality is not satisfied, so the point is not in the solution region."
                ),
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-formula-substitution"],
        )


@register
class SystemLinIneqIdentifyInequality(Generator):
    """From a half-plane description (line, solid/dashed, above/below), write the inequality."""
    generator_id = "system_lin_ineq_identify_inequality"
    topic_slug = "systems_of_linear_inequalities"
    display_name = "Write the inequality for a half-plane description"

    _M_RANGE = {"easy": (1, 5), "medium": (1, 10), "hard": (1, 15)}
    _B_RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        m = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m = -m
        b = rng.randint(b_lo, b_hi)

        boundary = rng.choice(["solid", "dashed"])
        shading = rng.choice(["above", "below"])

        if boundary == "dashed" and shading == "above":
            sym = ">"
        elif boundary == "dashed" and shading == "below":
            sym = "<"
        elif boundary == "solid" and shading == "above":
            sym = r"\geq"
        else:  # solid + below
            sym = r"\leq"

        rhs_str = _linear_term_with_var(m, b, "x")
        line_latex = f"y = {rhs_str}"
        answer = f"$y {sym} {rhs_str}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b, boundary, shading)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A half-plane has boundary line ${line_latex}$ drawn as a "
                f"**{boundary}** line, with shading **{shading}** the line. "
                "Write the inequality whose graph is this half-plane."
            ),
            answer_latex=answer,
            hints=[
                r"A **dashed** boundary means a strict inequality ($<$ or $>$). "
                r"A **solid** boundary means a non-strict inequality ($\leq$ or $\geq$).",
                r"Shading **above** the line means $y$ is greater ($>$ or $\geq$). "
                r"Shading **below** the line means $y$ is less ($<$ or $\leq$).",
                f"Combine: {boundary} + {shading} gives the symbol ${sym}$.",
            ],
            solution_steps_latex=[
                f"Identify the boundary line: ${line_latex}$.",
                f"The line is {boundary}, so the inequality is "
                + ("strict ($<$ or $>$)." if boundary == "dashed"
                   else r"non-strict ($\leq$ or $\geq$)."),
                f"The shading is {shading}, so $y$ is "
                + ("greater than the right side."
                   if shading == "above"
                   else "less than the right side."),
                f"Therefore the inequality is {answer}.",
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-visualization"],
        )


@register
class SystemLinIneqSlopeInterceptForm(Generator):
    """Given a system of two inequalities, identify slope, y-intercept, and boundary style for each."""
    generator_id = "system_lin_ineq_slope_intercept_form"
    topic_slug = "systems_of_linear_inequalities"
    display_name = "Identify slopes and boundaries of a system"

    _M_RANGE = {"easy": (1, 5), "medium": (1, 9), "hard": (1, 15)}
    _B_RANGE = {"easy": (-9, 9), "medium": (-18, 18), "hard": (-30, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        m1 = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m1 = -m1
        b1 = rng.randint(b_lo, b_hi)
        m2 = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m2 = -m2
        b2 = rng.randint(b_lo, b_hi)

        sym1 = rng.choice(list(_SYMBOLS))
        sym2 = rng.choice(list(_SYMBOLS))

        def boundary_kind(sym: str) -> str:
            return "dashed" if sym in ("<", ">") else "solid"

        kind1 = boundary_kind(sym1)
        kind2 = boundary_kind(sym2)

        rhs1 = _linear_term_with_var(m1, b1, "x")
        rhs2 = _linear_term_with_var(m2, b2, "x")
        system_latex = f"\\begin{{cases}} y {sym1} {rhs1} \\\\ y {sym2} {rhs2} \\end{{cases}}"

        answer = (
            f"Line 1: slope ${m1}$, y-intercept ${b1}$, {kind1}. "
            f"Line 2: slope ${m2}$, y-intercept ${b2}$, {kind2}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (m1, b1, sym1, m2, b2, sym2),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"For the system ${system_latex}$, identify the slope and "
                "y-intercept of each boundary line, and state whether each "
                "boundary is solid or dashed."
            ),
            answer_latex=answer,
            hints=[
                r"In slope-intercept form $y = mx + b$, $m$ is the slope and $b$ "
                r"is the y-intercept.",
                r"A strict inequality ($<$ or $>$) has a **dashed** boundary. A "
                r"non-strict inequality ($\leq$ or $\geq$) has a **solid** boundary.",
                f"Compare each line to $y = mx + b$ and read off $m$ and $b$.",
            ],
            solution_steps_latex=[
                f"Line 1: $y {sym1} {rhs1}$. Matching with $y = mx + b$, the "
                f"slope is ${m1}$ and the y-intercept is ${b1}$. The symbol "
                f"${sym1}$ is "
                + ("strict, so the boundary is dashed." if kind1 == "dashed"
                   else "non-strict, so the boundary is solid."),
                f"Line 2: $y {sym2} {rhs2}$. Matching with $y = mx + b$, the "
                f"slope is ${m2}$ and the y-intercept is ${b2}$. The symbol "
                f"${sym2}$ is "
                + ("strict, so the boundary is dashed." if kind2 == "dashed"
                   else "non-strict, so the boundary is solid."),
                answer,
            ],
            tags=["#branch-algebra-1", "#topic-inequalities", "#skill-visualization"],
        )
