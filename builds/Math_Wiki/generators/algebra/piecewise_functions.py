"""Piecewise-function generators (Wave D algebra gap topics).

Canonical topic slug ``piecewise_functions``.

- piecewise_evaluate_at_point: given a 2- or 3-piece function, compute f(x).
- piecewise_match_formula_to_graph: pick the matching formula from a list.
- piecewise_domain_and_range: state domain (union of intervals) and range.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


def _linear_eval(m: int, b: int, x: int) -> int:
    return m * x + b


def _format_linear(m: int, b: int) -> str:
    """Format mx + b with sign-aware b."""
    if m == 0:
        return f"{b}"
    if m == 1:
        mx = "x"
    elif m == -1:
        mx = "-x"
    else:
        mx = f"{m}x"
    if b == 0:
        return mx
    if b > 0:
        return f"{mx} + {b}"
    return f"{mx} - {abs(b)}"


def _format_interval_condition(
    lo: int | None,
    hi: int | None,
    lo_inclusive: bool,
    hi_inclusive: bool,
) -> str:
    """Return a LaTeX inequality like 'x < 2' or '1 \\le x < 5'."""
    if lo is None and hi is not None:
        op = r"\le" if hi_inclusive else "<"
        return f"x {op} {hi}"
    if hi is None and lo is not None:
        op = r"\ge" if lo_inclusive else ">"
        return f"x {op} {lo}"
    # Bounded interval.
    lop = r"\le" if lo_inclusive else "<"
    hop = r"\le" if hi_inclusive else "<"
    return f"{lo} {lop} x {hop} {hi}"


def _interval_contains(
    x: int,
    lo: int | None,
    hi: int | None,
    lo_inclusive: bool,
    hi_inclusive: bool,
) -> bool:
    if lo is not None:
        if lo_inclusive:
            if x < lo:
                return False
        else:
            if x <= lo:
                return False
    if hi is not None:
        if hi_inclusive:
            if x > hi:
                return False
        else:
            if x >= hi:
                return False
    return True


# ---------------------------------------------------------------------------


@register
class PiecewiseEvaluateAtPoint(Generator):
    """Evaluate a 2- or 3-piece function at a chosen x.

    Backward construction: pick the piece first, choose an x clearly inside
    that piece's interval, then compute f(x) from that piece's formula.
    """
    generator_id = "piecewise_evaluate_at_point"
    topic_slug = "piecewise_functions"
    display_name = "Evaluate a piecewise function at a point"

    _M_RANGE = {"easy": (1, 4), "medium": (1, 6), "hard": (1, 8)}
    _B_RANGE = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _SPLIT_RANGE = {"easy": (-3, 3), "medium": (-5, 5), "hard": (-8, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        split_lo, split_hi = self._SPLIT_RANGE[difficulty]

        num_pieces = 2 if difficulty == "easy" else rng.choice([2, 3])

        # Build distinct split points
        if num_pieces == 2:
            split1 = rng.randint(split_lo, split_hi)
            splits = [split1]
        else:
            s1 = rng.randint(split_lo, split_hi - 2)
            s2 = rng.randint(s1 + 2, split_hi + 2)
            splits = [s1, s2]

        # Build one linear formula per piece
        pieces = []
        for _ in range(num_pieces):
            m = rng.choice([-1, 1]) * rng.randint(m_lo, m_hi)
            b = rng.randint(b_lo, b_hi)
            pieces.append((m, b))

        # Pick which piece we'll evaluate in, then choose x inside that piece.
        piece_idx = rng.randint(0, num_pieces - 1)
        if num_pieces == 2:
            s1 = splits[0]
            if piece_idx == 0:
                # x < s1 (strict)
                x = rng.randint(s1 - 5, s1 - 1)
            else:
                # x >= s1 (inclusive)
                x = rng.randint(s1, s1 + 5)
        else:
            s1, s2 = splits
            if piece_idx == 0:
                x = rng.randint(s1 - 5, s1 - 1)
            elif piece_idx == 1:
                x = rng.randint(s1, s2 - 1)
            else:
                x = rng.randint(s2, s2 + 5)

        m_p, b_p = pieces[piece_idx]
        answer = _linear_eval(m_p, b_p, x)

        # Build the display: for 2-piece we use x < s1 and x >= s1; for
        # 3-piece: x < s1, s1 <= x < s2, x >= s2.
        rows: list[str] = []
        for i, (m, b) in enumerate(pieces):
            expr = _format_linear(m, b)
            if num_pieces == 2:
                if i == 0:
                    cond = f"x < {splits[0]}"
                else:
                    cond = rf"x \ge {splits[0]}"
            else:
                if i == 0:
                    cond = f"x < {splits[0]}"
                elif i == 1:
                    cond = rf"{splits[0]} \le x < {splits[1]}"
                else:
                    cond = rf"x \ge {splits[1]}"
            rows.append(f"{expr}, & {cond}")

        piecewise_latex = (
            r"f(x) = \begin{cases} "
            + r" \\ ".join(rows)
            + r" \end{cases}"
        )

        # Solution steps
        chosen_expr = _format_linear(m_p, b_p)
        eval_steps: list[str] = [
            f"The piecewise function is $${piecewise_latex}$$.",
        ]
        # Identify piece condition
        if num_pieces == 2:
            piece_desc = (
                f"$x < {splits[0]}$" if piece_idx == 0 else rf"$x \ge {splits[0]}$"
            )
        else:
            if piece_idx == 0:
                piece_desc = f"$x < {splits[0]}$"
            elif piece_idx == 1:
                piece_desc = rf"${splits[0]} \le x < {splits[1]}$"
            else:
                piece_desc = rf"$x \ge {splits[1]}$"

        eval_steps.append(
            f"Check where $x = {x}$ falls. Since $x = {x}$ satisfies {piece_desc}, "
            f"use the formula $f(x) = {chosen_expr}$."
        )
        eval_steps.append(
            f"Substitute $x = {x}$: $f({x}) = {chosen_expr.replace('x', f'({x})')}$."
        )
        eval_steps.append(f"Simplify to get $f({x}) = {answer}$.")

        key = (num_pieces, tuple(splits), tuple(pieces), x)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $${piecewise_latex}$$. Find $f({x})$."
            ),
            answer_latex=f"$f({x}) = {answer}$",
            hints=[
                (
                    "A piecewise function uses different formulas on different "
                    "intervals. First figure out which interval contains your "
                    "input, then plug into that piece's formula."
                ),
                (
                    f"Check each condition with $x = {x}$. The interval that "
                    "contains your $x$ tells you which rule to use."
                ),
                f"You should use the piece with formula ${chosen_expr}$.",
            ],
            solution_steps_latex=eval_steps,
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-formula-substitution",
            ],
        )


# ---------------------------------------------------------------------------


_PIECEWISE_GRAPH_BANK: tuple[dict, ...] = (
    {
        "description": (
            "a graph made of two line segments joined at $x = 2$: on the "
            "left, $f(x) = x + 1$, and on the right, $f(x) = 2x - 1$"
        ),
        "correct": r"f(x) = \begin{cases} x + 1, & x < 2 \\ 2x - 1, & x \ge 2 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} x - 1, & x < 2 \\ 2x + 1, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} 2x - 1, & x < 2 \\ x + 1, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} x + 1, & x \le 2 \\ 2x + 1, & x > 2 \end{cases}",
        ),
    },
    {
        "description": (
            "a step function with a jump at $x = 0$: $f(x) = -3$ for "
            "negative $x$ and $f(x) = 4$ for $x \\ge 0$"
        ),
        "correct": r"f(x) = \begin{cases} -3, & x < 0 \\ 4, & x \ge 0 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} 4, & x < 0 \\ -3, & x \ge 0 \end{cases}",
            r"f(x) = \begin{cases} -3, & x \le 0 \\ 4, & x > 0 \end{cases}",
            r"f(x) = \begin{cases} 3, & x < 0 \\ -4, & x \ge 0 \end{cases}",
        ),
    },
    {
        "description": (
            "a V-shaped graph made of two rays meeting at the origin: for "
            "$x < 0$ the graph follows $y = -x$, and for $x \\ge 0$ it "
            "follows $y = x$"
        ),
        "correct": r"f(x) = \begin{cases} -x, & x < 0 \\ x, & x \ge 0 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} x, & x < 0 \\ -x, & x \ge 0 \end{cases}",
            r"f(x) = \begin{cases} -x + 1, & x < 0 \\ x - 1, & x \ge 0 \end{cases}",
            r"f(x) = \begin{cases} -2x, & x < 0 \\ 2x, & x \ge 0 \end{cases}",
        ),
    },
    {
        "description": (
            "a three-piece graph with breaks at $x = 0$ and $x = 3$: a flat "
            "segment $y = 2$ on the left, a rising segment $y = x + 2$ in "
            "the middle, and a flat segment $y = 5$ on the right"
        ),
        "correct": (
            r"f(x) = \begin{cases} 2, & x < 0 \\ x + 2, & 0 \le x < 3 "
            r"\\ 5, & x \ge 3 \end{cases}"
        ),
        "distractors": (
            r"f(x) = \begin{cases} 2, & x < 0 \\ x - 2, & 0 \le x < 3 "
            r"\\ 5, & x \ge 3 \end{cases}",
            r"f(x) = \begin{cases} 5, & x < 0 \\ x + 2, & 0 \le x < 3 "
            r"\\ 2, & x \ge 3 \end{cases}",
            r"f(x) = \begin{cases} 2, & x \le 0 \\ x + 2, & 0 < x < 3 "
            r"\\ 5, & x > 3 \end{cases}",
        ),
    },
    {
        "description": (
            "a graph with a step at $x = 1$: a line with slope $3$ passing "
            "through the origin for $x < 1$, and a horizontal line at $y = 6$ "
            "for $x \\ge 1$"
        ),
        "correct": r"f(x) = \begin{cases} 3x, & x < 1 \\ 6, & x \ge 1 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} 3x, & x < 1 \\ 3, & x \ge 1 \end{cases}",
            r"f(x) = \begin{cases} 6, & x < 1 \\ 3x, & x \ge 1 \end{cases}",
            r"f(x) = \begin{cases} 3x + 1, & x < 1 \\ 6, & x \ge 1 \end{cases}",
        ),
    },
    {
        "description": (
            "a two-piece graph joined at $x = -1$: a line $y = x + 4$ on the "
            "left and a line $y = 2x + 5$ on the right"
        ),
        "correct": (
            r"f(x) = \begin{cases} x + 4, & x < -1 \\ 2x + 5, & x \ge -1 \end{cases}"
        ),
        "distractors": (
            r"f(x) = \begin{cases} 2x + 5, & x < -1 \\ x + 4, & x \ge -1 \end{cases}",
            r"f(x) = \begin{cases} x - 4, & x < -1 \\ 2x - 5, & x \ge -1 \end{cases}",
            r"f(x) = \begin{cases} x + 4, & x \le -1 \\ 2x + 5, & x > -1 \end{cases}",
        ),
    },
    {
        "description": (
            "a three-piece graph with a dip: $y = -x$ on the left, a flat "
            "$y = 0$ segment between $x = 0$ and $x = 2$, and $y = x - 2$ on "
            "the right"
        ),
        "correct": (
            r"f(x) = \begin{cases} -x, & x < 0 \\ 0, & 0 \le x < 2 "
            r"\\ x - 2, & x \ge 2 \end{cases}"
        ),
        "distractors": (
            r"f(x) = \begin{cases} x, & x < 0 \\ 0, & 0 \le x < 2 "
            r"\\ x - 2, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} -x, & x < 0 \\ 1, & 0 \le x < 2 "
            r"\\ x - 2, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} -x, & x \le 0 \\ 0, & 0 < x < 2 "
            r"\\ x + 2, & x > 2 \end{cases}",
        ),
    },
    {
        "description": (
            "two horizontal segments forming a step: $y = -2$ for $x < 4$ "
            "and $y = 1$ for $x \\ge 4$"
        ),
        "correct": r"f(x) = \begin{cases} -2, & x < 4 \\ 1, & x \ge 4 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} 1, & x < 4 \\ -2, & x \ge 4 \end{cases}",
            r"f(x) = \begin{cases} -2, & x \le 4 \\ 1, & x > 4 \end{cases}",
            r"f(x) = \begin{cases} 2, & x < 4 \\ -1, & x \ge 4 \end{cases}",
        ),
    },
    {
        "description": (
            "a line $y = x + 3$ for $x \\le 1$ and a parabola-like rising "
            "segment $y = 4x$ for $x > 1$"
        ),
        "correct": (
            r"f(x) = \begin{cases} x + 3, & x \le 1 \\ 4x, & x > 1 \end{cases}"
        ),
        "distractors": (
            r"f(x) = \begin{cases} 4x, & x \le 1 \\ x + 3, & x > 1 \end{cases}",
            r"f(x) = \begin{cases} x + 3, & x < 1 \\ 4x, & x \ge 1 \end{cases}",
            r"f(x) = \begin{cases} x - 3, & x \le 1 \\ 4x, & x > 1 \end{cases}",
        ),
    },
    {
        "description": (
            "a three-piece graph: $y = 2x$ on $x < -2$, a horizontal "
            "$y = -4$ from $x = -2$ to $x = 2$, and $y = 2x$ on $x \\ge 2$"
        ),
        "correct": (
            r"f(x) = \begin{cases} 2x, & x < -2 \\ -4, & -2 \le x < 2 "
            r"\\ 2x, & x \ge 2 \end{cases}"
        ),
        "distractors": (
            r"f(x) = \begin{cases} -2x, & x < -2 \\ -4, & -2 \le x < 2 "
            r"\\ -2x, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} 2x, & x < -2 \\ 4, & -2 \le x < 2 "
            r"\\ 2x, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} 2x, & x \le -2 \\ -4, & -2 < x < 2 "
            r"\\ 2x, & x > 2 \end{cases}",
        ),
    },
    {
        "description": (
            "a line $y = -x + 5$ on the left and a horizontal $y = 3$ on the "
            "right, meeting at $x = 2$"
        ),
        "correct": r"f(x) = \begin{cases} -x + 5, & x < 2 \\ 3, & x \ge 2 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} 3, & x < 2 \\ -x + 5, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} -x - 5, & x < 2 \\ 3, & x \ge 2 \end{cases}",
            r"f(x) = \begin{cases} x + 5, & x < 2 \\ 3, & x \ge 2 \end{cases}",
        ),
    },
    {
        "description": (
            "a rising line $y = x$ for $x \\le 0$ and a falling line "
            "$y = -x$ for $x > 0$ (an upside-down V)"
        ),
        "correct": r"f(x) = \begin{cases} x, & x \le 0 \\ -x, & x > 0 \end{cases}",
        "distractors": (
            r"f(x) = \begin{cases} -x, & x \le 0 \\ x, & x > 0 \end{cases}",
            r"f(x) = \begin{cases} x, & x < 0 \\ -x, & x \ge 0 \end{cases}",
            r"f(x) = \begin{cases} x + 1, & x \le 0 \\ -x + 1, & x > 0 \end{cases}",
        ),
    },
)


@register
class PiecewiseMatchFormulaToGraph(Generator):
    """Pick the formula that matches a described piecewise graph.

    The bank is small on purpose: we rotate through a curated list of
    handcrafted (description, correct, distractors) tuples.
    """
    generator_id = "piecewise_match_formula_to_graph"
    topic_slug = "piecewise_functions"
    display_name = "Match a formula to a described piecewise graph"
    bank_count_per_difficulty = 12

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        entry = rng.choice(_PIECEWISE_GRAPH_BANK)
        description = entry["description"]
        correct = entry["correct"]
        distractors = list(entry["distractors"])

        # Shuffle options and label A..D
        options = distractors + [correct]
        rng.shuffle(options)
        labels = ["A", "B", "C", "D"]
        correct_label = labels[options.index(correct)]

        option_lines = [f"({lbl}) $${opt}$$" for lbl, opt in zip(labels, options)]
        options_text = " ".join(option_lines)

        key = (description[:30], correct_label)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A graph of $f(x)$ looks like {description}. Which formula "
                f"matches the graph? {options_text}"
            ),
            answer_latex=f"({correct_label}) $${correct}$$",
            hints=[
                (
                    "Match each piece of the graph to a rule. Check which "
                    "formulas apply on the left versus the right side, and "
                    "whether the breakpoint is included or excluded."
                ),
                (
                    "Eliminate options whose pieces are swapped, whose "
                    "intervals miss a key value, or whose formulas don't "
                    "match the described lines."
                ),
            ],
            solution_steps_latex=[
                f"Read the graph description: {description}.",
                (
                    "Compare each option's pieces to the described segments, "
                    "checking both the formulas and where each piece applies."
                ),
                f"Option ({correct_label}) matches the described graph exactly.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-visualization",
            ],
        )


# ---------------------------------------------------------------------------


# Curated small rotation of domain/range setups. Each entry is a fully
# self-contained piecewise function with a known domain and range.
_DOMAIN_RANGE_BANK: tuple[dict, ...] = (
    {
        "latex": (
            r"f(x) = \begin{cases} x + 1, & -3 \le x < 0 "
            r"\\ 2x, & 0 \le x \le 4 \end{cases}"
        ),
        "description": (
            "f(x) = x + 1 for -3 <= x < 0 and f(x) = 2x for 0 <= x <= 4"
        ),
        # Piece 1: x in [-3, 0), f = x + 1 → f in [-2, 1)
        # Piece 2: x in [0, 4], f = 2x → f in [0, 8]
        # Domain: [-3, 4]; Range: [-2, 1) ∪ [0, 8] = [-2, 8]
        "domain": r"[-3, 4]",
        "range": r"[-2, 8]",
    },
    {
        "latex": (
            r"f(x) = \begin{cases} -x, & -4 \le x < 0 "
            r"\\ 3, & 0 \le x \le 5 \end{cases}"
        ),
        "description": (
            "f(x) = -x on [-4, 0) and f(x) = 3 on [0, 5]"
        ),
        # Piece 1: f in (0, 4]; Piece 2: f = {3}
        # Domain: [-4, 5]; Range: {3} ∪ (0, 4] = (0, 4]
        "domain": r"[-4, 5]",
        "range": r"(0, 4]",
    },
    {
        "latex": (
            r"f(x) = \begin{cases} 2, & -5 \le x < -1 "
            r"\\ x + 3, & -1 \le x \le 2 \end{cases}"
        ),
        "description": (
            "f(x) = 2 on [-5, -1) and f(x) = x + 3 on [-1, 2]"
        ),
        # Piece 1: f = {2}; Piece 2: f in [2, 5]
        # Domain: [-5, 2]; Range: {2} ∪ [2, 5] = [2, 5]
        "domain": r"[-5, 2]",
        "range": r"[2, 5]",
    },
    {
        "latex": (
            r"f(x) = \begin{cases} x, & 0 \le x \le 3 "
            r"\\ -x + 6, & 3 < x \le 6 \end{cases}"
        ),
        "description": (
            "f(x) = x on [0, 3] and f(x) = -x + 6 on (3, 6]"
        ),
        # Piece 1: f in [0, 3]; Piece 2: f in [0, 3)
        # Domain: [0, 6]; Range: [0, 3]
        "domain": r"[0, 6]",
        "range": r"[0, 3]",
    },
    {
        "latex": (
            r"f(x) = \begin{cases} x^2, & -2 \le x \le 0 "
            r"\\ x, & 0 < x \le 3 \end{cases}"
        ),
        "description": (
            "f(x) = x^2 on [-2, 0] and f(x) = x on (0, 3]"
        ),
        # Piece 1: x^2 on [-2, 0] gives [0, 4]; Piece 2: x on (0, 3] gives (0, 3]
        # Domain: [-2, 3]; Range: [0, 4]
        "domain": r"[-2, 3]",
        "range": r"[0, 4]",
    },
    {
        "latex": (
            r"f(x) = \begin{cases} -2, & -6 \le x \le -2 "
            r"\\ 1, & -2 < x \le 1 "
            r"\\ 4, & 1 < x \le 4 \end{cases}"
        ),
        "description": (
            "f(x) = -2 on [-6, -2], f(x) = 1 on (-2, 1], f(x) = 4 on (1, 4]"
        ),
        "domain": r"[-6, 4]",
        "range": r"\{-2, 1, 4\}",
    },
)


@register
class PiecewiseDomainAndRange(Generator):
    """State the domain and range of a piecewise function.

    Small curated rotation: each entry ships with its correct domain and range.
    """
    generator_id = "piecewise_domain_and_range"
    topic_slug = "piecewise_functions"
    display_name = "Find the domain and range of a piecewise function"
    bank_count_per_difficulty = 6

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        entry = rng.choice(_DOMAIN_RANGE_BANK)
        latex = entry["latex"]
        description = entry["description"]
        domain = entry["domain"]
        range_ = entry["range"]

        key = (description, domain, range_)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Consider the piecewise function $${latex}$$. Find its "
                "domain and range, writing each in interval (or set) "
                "notation."
            ),
            answer_latex=(
                f"Domain: ${domain}$. Range: ${range_}$."
            ),
            hints=[
                (
                    "The domain is the union of all the x-intervals on which "
                    "the function is defined. The range is the set of all "
                    "y-values the function can actually produce."
                ),
                (
                    "For the range, evaluate each piece over its interval "
                    "and combine the resulting y-sets."
                ),
            ],
            solution_steps_latex=[
                (
                    "List each piece's interval of definition and take their "
                    "union to get the domain."
                ),
                (
                    "For each piece, figure out what y-values it produces on "
                    "its interval."
                ),
                (
                    "Combine the y-value sets to get the overall range."
                ),
                f"Domain: ${domain}$. Range: ${range_}$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-functions",
                "#skill-multi-step",
            ],
        )
