"""Relations and functions (pre-calculus Wave C).

Three generators for the ``relations`` topic slug:

- IsRelationAFunction: given a set of ordered pairs, decide whether the
  relation is a function (no repeated first coordinate with different
  second coordinate). Rotation. ``bank_count_per_difficulty = 15``.
- DescribeRelationGraph: given a verbal description of a graph,
  identify whether it is a line, half-plane, curve, region, or similar.
  Rotation. ``bank_count_per_difficulty = 12``.
- FunctionVsRelationFromEquation: given an equation, decide whether it
  defines $y$ as a function of $x$ (vertical line test equivalents).

Backward construction throughout: scenarios are pre-classified and
parameters chosen so answers are clean and unambiguous.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


RELATION_TAGS = [
    "#branch-pre-calculus",
    "#topic-functions",
    "#skill-procedural-calculation",
]

RELATION_VIS_TAGS = [
    "#branch-pre-calculus",
    "#topic-functions",
    "#skill-visualization",
]

RELATION_EQN_TAGS = [
    "#branch-pre-calculus",
    "#topic-functions",
    "#skill-multi-step",
]


# ===========================================================================
# Generator 1: is_relation_a_function
# ===========================================================================


@register
class IsRelationAFunction(Generator):
    """Decide whether a small set of ordered pairs is a function.

    A relation is a function iff no $x$-value is paired with two distinct
    $y$-values. Backward: decide the answer, then build a pair list that
    supports it.
    """
    generator_id = "is_relation_a_function"
    topic_slug = "relations"
    display_name = "Decide whether a set of ordered pairs is a function"

    bank_count_per_difficulty = 15

    _N_RANGES = {"easy": (3, 4), "medium": (4, 5), "hard": (5, 6)}
    _X_RANGES = {"easy": (-5, 5), "medium": (-7, 7), "hard": (-9, 9)}
    _Y_RANGES = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n = rng.randint(*self._N_RANGES[difficulty])
        x_lo, x_hi = self._X_RANGES[difficulty]
        y_lo, y_hi = self._Y_RANGES[difficulty]
        make_function = rng.choice([True, False])

        pool = list(range(x_lo, x_hi + 1))
        rng.shuffle(pool)

        if make_function:
            # Choose n distinct x-values so every x is unique.
            xs = pool[:n]
            ys = [rng.randint(y_lo, y_hi) for _ in range(n)]
            pairs = list(zip(xs, ys))
            answer = "Yes, it is a function."
            reason = (
                "Every $x$-value in the list appears exactly once, so no input "
                "is paired with two different outputs."
            )
            duplicate_x = None
        else:
            # Reuse one x-value with two different y-values.
            repeat_x = pool[0]
            xs_rest = pool[1:n - 1]
            y1 = rng.randint(y_lo, y_hi)
            y2 = rng.randint(y_lo, y_hi)
            while y2 == y1:
                y2 = rng.randint(y_lo, y_hi)
            xs = [repeat_x] + xs_rest + [repeat_x]
            ys = [y1] + [rng.randint(y_lo, y_hi) for _ in xs_rest] + [y2]
            pairs = list(zip(xs, ys))
            rng.shuffle(pairs)
            answer = "No, it is NOT a function."
            reason = (
                f"The $x$-value ${repeat_x}$ appears twice with two different "
                f"$y$-values (${y1}$ and ${y2}$), violating the definition of a "
                "function."
            )
            duplicate_x = repeat_x

        pair_strs = ", ".join(f"({x},\\ {y})" for x, y in pairs)
        relation_latex = f"$\\{{{pair_strs}\\}}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (make_function, tuple(pairs))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine whether the relation {relation_latex} defines $y$ "
                "as a function of $x$."
            ),
            answer_latex=answer,
            hints=[
                (
                    "A relation is a function when every $x$-value has exactly "
                    "one $y$-value."
                ),
                (
                    "Check for any $x$ that appears more than once. If it is "
                    "paired with two different $y$-values, the relation is not "
                    "a function."
                ),
            ],
            solution_steps_latex=[
                (
                    f"List the ordered pairs: {relation_latex}."
                ),
                (
                    "Scan the $x$-values for repeats and, for each repeat, "
                    "verify whether the $y$-values match."
                ),
                reason,
                f"Conclusion: {answer}",
            ],
            tags=RELATION_TAGS,
        )


# ===========================================================================
# Generator 2: describe_relation_graph
# ===========================================================================


@register
class DescribeRelationGraph(Generator):
    """Given a verbal description, identify the graph type.

    Rotation over a small pool of verbal scenarios. Categories include
    line, half-plane, circle, parabola, and region.
    """
    generator_id = "describe_relation_graph"
    topic_slug = "relations"
    display_name = "Identify a graph type from a verbal description"

    bank_count_per_difficulty = 12

    _SCENARIOS: tuple[tuple[str, str, str], ...] = (
        (
            "Every point satisfies the equation $y = 2x - 3$, which when plotted "
            "produces infinitely many collinear points sloping upward.",
            "Line",
            "A linear equation of the form $y = mx + b$ graphs to a straight "
            "line.",
        ),
        (
            "The set of points satisfies $y > x + 1$, producing a shaded region "
            "on one side of a dashed boundary line.",
            "Half-plane",
            "A strict linear inequality fills the half of the plane on one "
            "side of the boundary line; the boundary itself is dashed because "
            "it is not included.",
        ),
        (
            "Every point $(x, y)$ obeys $x^2 + y^2 = 9$, giving a closed curve "
            "at a fixed distance from the origin.",
            "Circle",
            "$x^2 + y^2 = r^2$ is the standard equation of a circle centred at "
            "the origin with radius $r$.",
        ),
        (
            "The relation is $y = x^2 - 4$, producing a U-shaped curve with a "
            "minimum at $(0, -4)$.",
            "Parabola",
            "A quadratic $y = ax^2 + bx + c$ graphs as a parabola; the sign of "
            "$a$ determines whether it opens up or down.",
        ),
        (
            "Every point $(x, y)$ satisfies both $y \\leq 2x + 1$ and $y \\geq "
            "-x - 2$, producing the intersection of two half-planes.",
            "Region (intersection of half-planes)",
            "Two simultaneous linear inequalities describe the overlap of two "
            "half-planes, yielding a wedge-shaped region bounded by two lines.",
        ),
        (
            "The relation $y = \\sqrt{x}$ plots a curve that starts at the "
            "origin and rises gently to the right.",
            "Half of a parabola",
            "Taking the principal square root yields only the upper branch of "
            "a sideways parabola.",
        ),
        (
            "A single equation $x = 4$ is satisfied by all points with first "
            "coordinate $4$ regardless of their second coordinate.",
            "Vertical line",
            "$x = c$ is always a vertical line; it is not a function because "
            "one $x$ pairs with every $y$.",
        ),
        (
            "Every point satisfies $|x| + |y| = 3$, drawing a diamond shape "
            "with corners on the axes.",
            "Rhombus (diamond)",
            "Absolute-value sums define a square rotated $45^{\\circ}$, a.k.a. "
            "a rhombus with axis-aligned diagonals.",
        ),
        (
            "The relation $y \\geq 0$ picks out all points on or above the "
            "$x$-axis.",
            "Half-plane (upper)",
            "A single-variable inequality in $y$ defines a horizontal "
            "half-plane.",
        ),
        (
            "Points satisfy $y = -x + 5$, producing a straight line descending "
            "from left to right.",
            "Line",
            "Linear equations graph as lines; the negative slope makes it "
            "descend.",
        ),
        (
            "The set of points obeys the disk inequality $x^2 + y^2 \\leq 16$, "
            "filling in the interior and boundary of a circle.",
            "Disk (closed region)",
            "A non-strict inequality on $x^2 + y^2$ produces the filled disk "
            "inside the bounding circle, including the circle itself.",
        ),
        (
            "Every point satisfies $y = \\dfrac{1}{x}$, which has two branches "
            "that hug the axes without touching them.",
            "Hyperbola (rectangular)",
            "The reciprocal function graphs as a rectangular hyperbola with "
            "the $x$- and $y$-axes as asymptotes.",
        ),
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randrange(len(self._SCENARIOS))
        scenario, classification, reason = self._SCENARIOS[idx]

        answer_latex = f"**{classification}**"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A relation is described as follows: {scenario} What kind of "
                "graph is this?"
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Pay attention to whether the relation involves an "
                    "equation (curve or line) or an inequality (region)."
                ),
                (
                    "Look for the highest power of $x$ and $y$ and whether "
                    "absolute values or square roots are involved."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Re-read the description: {scenario}"
                ),
                reason,
                f"Graph type: {answer_latex}.",
            ],
            tags=RELATION_VIS_TAGS,
        )


# ===========================================================================
# Generator 3: function_vs_relation_from_equation
# ===========================================================================


@register
class FunctionVsRelationFromEquation(Generator):
    """Given an equation, decide whether $y$ is a function of $x$.

    Backward: pick a form that is (or is not) a function of $x$:

    Function of $x$: $y = ax^2 + b$, $y = ax + b$, $y = \\sqrt{x - h}$ (with
      principal root), $y = |x - h| + k$, etc.
    Not a function of $x$: $x = ay^2 + b$, $x^2 + y^2 = r^2$ (circle),
      $|y| = x - h$ (two-branch), $x = |y|$, etc.
    """
    generator_id = "function_vs_relation_from_equation"
    topic_slug = "relations"
    display_name = "Decide whether an equation defines y as a function of x"

    _FORMS_FUNCTION = (
        "y_linear",
        "y_quadratic",
        "y_principal_sqrt",
        "y_abs",
    )
    _FORMS_NOT_FUNCTION = (
        "x_quadratic",
        "circle",
        "abs_y",
        "x_of_y_sqrt",
    )

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        is_function = rng.choice([True, False])
        if is_function:
            form = rng.choice(self._FORMS_FUNCTION)
        else:
            form = rng.choice(self._FORMS_NOT_FUNCTION)

        a = rng.choice([c for c in range(-5, 6) if c != 0])
        b = rng.randint(-6, 6)
        r = rng.randint(2, 9)
        h = rng.randint(-4, 4)
        k = rng.randint(-4, 4)

        if form == "y_linear":
            equation_latex = f"y = {a}x + {b}" if b >= 0 else f"y = {a}x - {abs(b)}"
            reason = (
                "A linear equation solved for $y$ gives exactly one $y$-value "
                "for every $x$, so it is a function."
            )
        elif form == "y_quadratic":
            equation_latex = f"y = {a}x^2 + {b}" if b >= 0 else f"y = {a}x^2 - {abs(b)}"
            reason = (
                "A parabola that opens up or down passes the vertical line "
                "test: each $x$ gives one $y$, so it defines $y$ as a function "
                "of $x$."
            )
        elif form == "y_principal_sqrt":
            shift = b
            if shift == 0:
                equation_latex = r"y = \sqrt{x}"
            elif shift > 0:
                equation_latex = rf"y = \sqrt{{x - {shift}}}"
            else:
                equation_latex = rf"y = \sqrt{{x + {abs(shift)}}}"
            reason = (
                "The principal square root is single-valued, so each $x$ in "
                "the domain yields exactly one $y$. It is a function."
            )
        elif form == "y_abs":
            shift = h
            if shift == 0:
                inner = "x"
            elif shift > 0:
                inner = f"x - {shift}"
            else:
                inner = f"x + {abs(shift)}"
            if k == 0:
                equation_latex = rf"y = \left|{inner}\right|"
            elif k > 0:
                equation_latex = rf"y = \left|{inner}\right| + {k}"
            else:
                equation_latex = rf"y = \left|{inner}\right| - {abs(k)}"
            reason = (
                "Absolute value is single-valued, so each $x$ gives one $y$. "
                "It is a function."
            )
        elif form == "x_quadratic":
            equation_latex = (
                f"x = {a}y^2 + {b}" if b >= 0 else f"x = {a}y^2 - {abs(b)}"
            )
            reason = (
                "Solving for $y$ introduces a $\\pm$ square root, so a single "
                "$x$ can give two $y$-values. It is NOT a function of $x$."
            )
        elif form == "circle":
            equation_latex = f"x^2 + y^2 = {r ** 2}"
            reason = (
                "Circles fail the vertical line test: most vertical lines cross "
                "the circle twice. It is NOT a function of $x$."
            )
        elif form == "abs_y":
            if h == 0:
                equation_latex = r"|y| = x"
            elif h > 0:
                equation_latex = rf"|y| = x - {h}"
            else:
                equation_latex = rf"|y| = x + {abs(h)}"
            reason = (
                "$|y| = \\text{something non-negative}$ yields $y = \\pm$ that "
                "value, so most $x$'s give two $y$'s. It is NOT a function."
            )
        else:  # x_of_y_sqrt
            if h == 0:
                equation_latex = r"x = y^2"
            elif h > 0:
                equation_latex = rf"x = y^2 + {h}"
            else:
                equation_latex = rf"x = y^2 - {abs(h)}"
            reason = (
                "This is a sideways parabola. Solving for $y$ gives "
                "$y = \\pm\\sqrt{x - c}$, so a single $x$ gives two $y$'s. It "
                "is NOT a function of $x$."
            )

        answer_latex = (
            "**Yes**, it defines $y$ as a function of $x$."
            if is_function
            else "**No**, it does NOT define $y$ as a function of $x$."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (is_function, form, a, b, r, h, k)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Does the equation ${equation_latex}$ define $y$ as a "
                "function of $x$? Answer yes or no."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Try to solve the equation for $y$. If you end up with a "
                    "single expression, it is a function; if you need "
                    "$y = \\pm \\ldots$, it is not."
                ),
                (
                    "Equivalent test: apply the vertical line test. A vertical "
                    "line that meets the graph more than once means the "
                    "equation is not a function of $x$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Inspect the equation ${equation_latex}$."
                ),
                reason,
                f"Conclusion: {answer_latex}",
            ],
            tags=RELATION_EQN_TAGS,
        )
