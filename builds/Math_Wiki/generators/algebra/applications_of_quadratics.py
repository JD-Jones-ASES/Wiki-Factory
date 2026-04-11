"""Application generators that extend the live ``applications_of_quadratic_functions`` topic.

History: this module originally targeted a separate ``applications_of_quadratics``
stub topic. In the v2.4 stub cleanup the stub was merged into the live
``Applications_Of_Quadratic_Functions.md`` topic, the duplicate
``projectile_max_height`` class (which collided with the canonical one in
``quadratic_functions.py`` and was never actually registered) was deleted,
and the two surviving classes had their ``topic_slug`` retargeted to the
live slug.

Surviving classes:

- ``area_quadratic_word_problem``: a rectangle has a linear relationship
  between length and width; given the area, solve a quadratic for the
  dimensions.
- ``quadratic_revenue_or_cost_optimization``: maximize $R(p) = p(b - ap)$
  for the optimal price and peak revenue.

All word-problem scenarios are freshly written (community garden beds,
science-fair poster boards, farmer's-market candles, etc.).
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------

@register
class AreaQuadraticWordProblem(Generator):
    """Rectangle with length = width + k, total area A; solve for width.

    Backward: pick integer width `w0 > 0` and offset `k` so length = w0 + k.
    Area A = w0 * (w0 + k). Student solves w^2 + k*w - A = 0.
    """
    generator_id = "area_quadratic_word_problem"
    topic_slug = "applications_of_quadratic_functions"
    display_name = "Rectangle dimensions from area (quadratic)"

    _W = {"easy": (3, 9), "medium": (4, 14), "hard": (6, 20)}
    _K = {"easy": (2, 6), "medium": (2, 9), "hard": (3, 13)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        w_lo, w_hi = self._W[difficulty]
        k_lo, k_hi = self._K[difficulty]
        width = rng.randint(w_lo, w_hi)
        k = rng.randint(k_lo, k_hi)
        length = width + k
        area = width * length

        scenarios = [
            ("Mateo", "a community garden bed", "meters"),
            ("Leilani", "a photo-booth backdrop", "feet"),
            ("Emilia", "a science-fair poster board", "inches"),
            ("Priya", "a maker-space workbench top", "feet"),
            ("Kai", "a school mural panel", "meters"),
        ]
        who, thing, unit = rng.choice(scenarios)

        statement = (
            f"{who} is designing {thing}. The length is ${k}$ {unit} more than the "
            f"width, and the total area must be ${area}$ square {unit}. "
            f"Find the width and length of the rectangle."
        )

        # Quadratic: w^2 + k*w - area = 0
        a_coef = 1
        b_coef = k
        c_coef = -area

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (width, k, area),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=(
                f"Width ${width}$ {unit}, length ${length}$ {unit}"
            ),
            hints=[
                f"Let $w$ be the width. Then the length is $w + {k}$.",
                f"Area equals length times width: $w(w + {k}) = {area}$.",
                f"Expand and solve the quadratic $w^{{2}} + {k}w - {area} = 0$. Discard the negative root.",
            ],
            solution_steps_latex=[
                f"Let $w$ be the width in {unit}. Then the length is $w + {k}$ {unit}.",
                f"Set up the area equation: $w(w + {k}) = {area}$.",
                f"Expand: $w^{{2}} + {k}w - {area} = 0$.",
                f"Solve: $w = {width}$ (the positive root).",
                f"So the width is ${width}$ {unit} and the length is ${length}$ {unit}.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-quadratics",
                "#skill-modeling",
            ],
        )


@register
class QuadraticRevenueOrCostOptimization(Generator):
    """Maximize $R(p) = p(b - a p)$ (revenue model) for the optimal price.

    Backward construction: pick positive integers ``a`` and ``b`` with
    ``b`` divisible by ``2a`` so the optimal price is a clean integer and
    the peak revenue is also an integer.

    Optimal price: $p^* = b / (2a)$. Peak revenue: $R(p^*) = b^2 / (4a)$.
    """
    generator_id = "quadratic_revenue_or_cost_optimization"
    topic_slug = "applications_of_quadratic_functions"
    display_name = "Optimal price for a quadratic revenue model"

    _A = {"easy": (1, 3), "medium": (1, 4), "hard": (2, 5)}
    _P = {"easy": (3, 8), "medium": (4, 12), "hard": (5, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a_lo, a_hi = self._A[difficulty]
        p_lo, p_hi = self._P[difficulty]
        a = rng.randint(a_lo, a_hi)
        p_opt = rng.randint(p_lo, p_hi)
        b = 2 * a * p_opt  # ensures the vertex is at p = p_opt
        peak = p_opt * (b - a * p_opt)

        scenarios = [
            (
                "Leilani runs a booth at a farmer's market selling hand-poured candles",
                "candles",
                "dollars",
            ),
            (
                "Mateo sells handmade zines at a maker space pop-up",
                "zines",
                "dollars",
            ),
            (
                "Zoe prices photo prints for a photography class fundraiser",
                "prints",
                "dollars",
            ),
            (
                "Kai sells pressed-flower cards at a community garden event",
                "cards",
                "dollars",
            ),
            (
                "Priya runs a concession at a school pep rally",
                "snack packs",
                "dollars",
            ),
        ]
        opener, item, unit = rng.choice(scenarios)

        statement = (
            f"{opener}. When the price is $p$ {unit}, the daily revenue "
            f"(in {unit}) is modeled by $R(p) = p\\,({b} - {a} p)$. "
            f"Find the price that maximizes revenue and compute the maximum "
            f"revenue."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=(
                f"Optimal price $p = {p_opt}$ {unit}; peak revenue ${peak}$ {unit}"
            ),
            hints=[
                r"Expand $R(p)$ to put it in the form $-a p^{2} + b p$, then use the vertex formula.",
                f"Expanded: $R(p) = -{a} p^{{2}} + {b} p$.",
                r"Vertex price: $p^* = -\dfrac{b}{2a}$ (with $a$ the quadratic coefficient), then substitute to get the peak revenue.",
            ],
            solution_steps_latex=[
                f"Start with $R(p) = p({b} - {a}p) = -{a}p^{{2}} + {b}p$.",
                f"The vertex of $R$ is at $p^* = \\dfrac{{{b}}}{{2 \\cdot {a}}} = {p_opt}$ {unit}.",
                f"Peak revenue: $R({p_opt}) = {p_opt}({b} - {a}({p_opt})) = {peak}$ {unit}.",
                f"Optimal price: ${p_opt}$ {unit}. Peak revenue: ${peak}$ {unit}.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-quadratics",
                "#skill-modeling",
            ],
        )
