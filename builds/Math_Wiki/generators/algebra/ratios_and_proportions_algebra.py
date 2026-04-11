"""Algebra-level proportion generators.

History: this module originally targeted a separate ``ratios_and_proportions``
stub topic. In the v2.4 stub cleanup the stub was folded into the live
``Proportions_And_Cross_Multiplication`` topic and the three classes here
had their ``topic_slug`` retargeted accordingly. They remain in ``algebra/``
because they carry algebraic expressions in the proportion (variables on
both sides, similar-triangle side-length solves) rather than the pre-algebra
arithmetic treatment.

Classes:

- ``solve_proportion_with_variable``: solve $\\dfrac{ax + b}{c} = \\dfrac{d}{e}$
  or $\\dfrac{x}{a} = \\dfrac{b}{c}$ forms with algebraic knowns.
- ``proportion_word_problem_scale``: scale-model/map word problem with a
  clean integer scale factor.
- ``similar_figures_proportion``: similar triangles; find the missing
  side via a proportion.
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------


@register
class SolveProportionWithVariable(Generator):
    """Solve a proportion where one side carries an algebraic expression.

    Backward construction: pick integer ``x_val`` first, then build the
    proportion $\\dfrac{x + c}{a} = \\dfrac{b}{d}$ with integer parameters
    chosen so it's satisfied by ``x_val``. Specifically, pick ``a``, ``b``,
    ``d`` with $a \\cdot b = d \\cdot (x_{\\text{val}} + c)$ --- but the
    easiest way is to pick a cross-product value $k$ and derive matching
    sides.
    """
    generator_id = "solve_proportion_with_variable"
    topic_slug = "proportions_and_cross_multiplication"
    display_name = "Solve a proportion with a variable"

    _X = {"easy": (1, 8), "medium": (1, 14), "hard": (2, 22)}
    _C = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}
    _A = {"easy": [2, 3, 4, 5], "medium": [2, 3, 4, 5, 6, 7, 8], "hard": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]}
    _K = {"easy": [1, 2, 3], "medium": [1, 2, 3, 4, 5], "hard": [1, 2, 3, 4, 5, 6, 7]}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X[difficulty]
        c_lo, c_hi = self._C[difficulty]

        # Pure backward construction: pick x_val, c, a, and a multiplier k.
        # Then b = k * (x_val + c) and d = k * a, which guarantees
        # (x_val + c) / a = b / d without any retry loop.
        # We regenerate once if we hit a degenerate (x_val + c == 0) case.
        for _ in range(12):
            x_val = rng.randint(x_lo, x_hi)
            c = rng.randint(c_lo, c_hi)
            if x_val + c != 0:
                break
        else:
            # Force a safe fallback — guaranteed nonzero
            x_val = max(x_lo, 1)
            c = max(c_lo, 1)

        a = rng.choice(self._A[difficulty])
        k = rng.choice(self._K[difficulty])
        b = k * (x_val + c)
        d = k * a
        # b could be negative if x_val + c is negative; that's OK but
        # keep |b| reasonable. If |b| gets absurd, rescale k.
        if abs(b) > 300:
            k = 1
            b = k * (x_val + c)
            d = k * a

        # Format the left side
        if c == 0:
            left_num = "x"
        elif c > 0:
            left_num = f"x + {c}"
        else:
            left_num = f"x - {abs(c)}"

        statement = f"Solve the proportion $\\dfrac{{{left_num}}}{{{a}}} = \\dfrac{{{b}}}{{{d}}}$ for $x$."

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (x_val, c, a, b, d),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {x_val}$",
            hints=[
                "Use the cross-multiplication rule: $\\dfrac{A}{B} = \\dfrac{C}{D}$ means $A \\cdot D = B \\cdot C$.",
                f"Cross-multiplying gives $({left_num}) \\cdot {d} = {a} \\cdot {b}$.",
                f"Simplify, then solve the resulting linear equation for $x$.",
            ],
            solution_steps_latex=[
                f"Start with $\\dfrac{{{left_num}}}{{{a}}} = \\dfrac{{{b}}}{{{d}}}$.",
                f"Cross-multiply: $({left_num}) \\cdot {d} = {a} \\cdot {b}$, i.e., ${d}({left_num}) = {a * b}$.",
                f"Distribute and isolate $x$: $x = {x_val}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-proportional-reasoning",
            ],
        )


@register
class ProportionWordProblemScale(Generator):
    """Map/model scale word problem.

    Backward: pick integer scale factor $s$ (e.g. 1 model unit = $s$ real
    units), pick a real measurement $r$, then the model measurement is
    $r / s$. All kept as integers for clean answers.
    """
    generator_id = "proportion_word_problem_scale"
    topic_slug = "proportions_and_cross_multiplication"
    display_name = "Scale-factor word problem (map, model, blueprint)"

    _SCALE = {"easy": [4, 5, 8, 10], "medium": [6, 8, 10, 12, 15, 20], "hard": [10, 12, 15, 20, 25, 30, 40]}
    _MODEL = {"easy": (3, 12), "medium": (4, 18), "hard": (5, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scale = rng.choice(self._SCALE[difficulty])
        model_lo, model_hi = self._MODEL[difficulty]
        model_measurement = rng.randint(model_lo, model_hi)
        real_measurement = model_measurement * scale

        scenarios = [
            (
                "Mateo",
                "a blueprint of his pop-up book spread",
                "inches",
                "inches",
                "spread",
            ),
            (
                "Priya",
                "a scale model of the school quad",
                "centimeters",
                "meters",
                "courtyard",
            ),
            (
                "Kai",
                "a map of a community garden",
                "centimeters",
                "meters",
                "garden path",
            ),
            (
                "Zoe",
                "a floor plan of a photography studio",
                "inches",
                "feet",
                "studio length",
            ),
            (
                "Leilani",
                "a miniature diorama of a farmer's market",
                "inches",
                "feet",
                "market aisle",
            ),
        ]
        who, thing, model_unit, real_unit, real_thing = rng.choice(scenarios)

        statement = (
            f"{who} is building {thing}. On the model, ${1}$ {model_unit} "
            f"represents ${scale}$ {real_unit} in real life. The model "
            f"{real_thing} measures ${model_measurement}$ {model_unit}. "
            f"Determine the actual length of the {real_thing}."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (scale, model_measurement),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${real_measurement}$ {real_unit}",
            hints=[
                "Set up a proportion: model length to real length equals $1 : $ scale.",
                f"$\\dfrac{{\\text{{real}}}}{{\\text{{model}}}} = \\dfrac{{{scale}}}{{1}}$, so real = model $\\cdot\\;{scale}$.",
                f"Plug in: real = ${model_measurement} \\cdot {scale}$.",
            ],
            solution_steps_latex=[
                f"Set up the proportion $\\dfrac{{\\text{{real}}}}{{{model_measurement}}} = \\dfrac{{{scale}}}{{1}}$.",
                f"Cross-multiply: $\\text{{real}} = {model_measurement} \\cdot {scale} = {real_measurement}$.",
                f"The actual length is ${real_measurement}$ {real_unit}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-numbers-and-operations",
                "#skill-proportional-reasoning",
            ],
        )


@register
class SimilarFiguresProportion(Generator):
    """Similar triangles: given three side lengths (two from one triangle and
    one matching side from the other), find the missing side.

    Backward: pick a scale factor $k$ and three side lengths of triangle A,
    then triangle B sides are $k$ times A. Present three of the four values
    and hide the fourth as $x$.
    """
    generator_id = "similar_figures_proportion"
    topic_slug = "proportions_and_cross_multiplication"
    display_name = "Missing side of similar figures"

    _K = {"easy": [2, 3, 4], "medium": [2, 3, 4, 5, 6], "hard": [2, 3, 4, 5, 6, 7, 8]}
    _SIDE = {"easy": (3, 10), "medium": (4, 15), "hard": (5, 22)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        k = rng.choice(self._K[difficulty])
        s_lo, s_hi = self._SIDE[difficulty]
        a = rng.randint(s_lo, s_hi)
        b = rng.randint(s_lo, s_hi)
        while b == a:
            b = rng.randint(s_lo, s_hi)
        # Triangle A: sides (a, b, ?) ; Triangle B: corresponding sides are (k*a, k*b, ?)
        # Ask: in triangle B, one side corresponds to side a in triangle A.
        # Student is given side 'a' in small triangle, side '?' in small triangle,
        # and the k*a side in the big triangle. Task: find the missing side in big triangle.
        missing_big = k * b  # the side we ask for

        names = ["Maya", "Kai", "Priya", "Rohan", "Zoe", "Emilia", "Mateo", "Leilani"]
        who = rng.choice(names)
        context = rng.choice(
            [
                "studying triangle similarity in a photography class",
                "sketching scaled trusses for a pop-up book stage",
                "designing banner triangles for a school pep rally",
                "cutting corner trim for a community garden signpost",
            ],
        )

        statement = (
            f"{who}, {context}, has two similar triangles. In the smaller "
            f"triangle, two sides measure ${a}$ and ${b}$. In the larger "
            f"triangle, the side corresponding to the ${a}$-side measures "
            f"${k * a}$. Find the length $x$ of the larger triangle's side "
            f"that corresponds to the ${b}$-side."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (k, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$x = {missing_big}$",
            hints=[
                "Similar figures have proportional corresponding sides. Write the ratio of matched sides.",
                f"Set up: $\\dfrac{{{k * a}}}{{{a}}} = \\dfrac{{x}}{{{b}}}$.",
                f"Simplify the left side to ${k}$, then solve for $x$.",
            ],
            solution_steps_latex=[
                f"Set up the proportion: $\\dfrac{{{k * a}}}{{{a}}} = \\dfrac{{x}}{{{b}}}$.",
                f"Simplify the left ratio: $\\dfrac{{{k * a}}}{{{a}}} = {k}$, so ${k} = \\dfrac{{x}}{{{b}}}$.",
                f"Cross-multiply: $x = {k} \\cdot {b} = {missing_big}$.",
                f"The missing side is ${missing_big}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-analytic-geometry",
                "#skill-proportional-reasoning",
            ],
        )
