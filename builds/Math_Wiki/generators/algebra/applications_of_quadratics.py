"""Applications of quadratics generators (Phase 2c Wave B).

Canonical topic slug ``applications_of_quadratics``.

- projectile_max_height: given $h(t) = -16t^2 + v_0 t + h_0$, find the time
  of maximum height and the maximum height.
- area_quadratic_word_problem: a rectangle has a linear relationship between
  length and width; given the area, solve a quadratic for dimensions.
- quadratic_revenue_or_cost_optimization: maximize $R(p) = p(b - ap)$ for
  optimal price and peak revenue.

All word-problem scenarios are freshly written: t-shirt launchers, pop-up
book hinges, photography-class sun umbrellas, community garden beds, etc.
"""
from __future__ import annotations

import math
import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


t = sp.Symbol("t")
w = sp.Symbol("w")
p = sp.Symbol("p")


# ---------------------------------------------------------------------------

@register
class ProjectileMaxHeight(Generator):
    """Find the time and height of maximum for $h(t) = -16 t^2 + v_0 t + h_0$.

    Backward construction: pick a clean positive integer peak time ``tp`` and
    a non-negative peak height ``hp``. For a parabola $h(t) = -16 t^2 + v_0 t
    + h_0$ with vertex at ``t = tp`` and vertex value ``hp``:

        v_0 = 32 * tp     (since the vertex is at t = v_0 / 32)
        h_0 = hp - 16 * tp^2

    That way the student recovers ``tp`` and ``hp`` cleanly.
    """
    generator_id = "projectile_max_height"
    topic_slug = "applications_of_quadratics"
    display_name = "Projectile: time and value of maximum height"

    _TP = {"easy": (1, 2), "medium": (1, 3), "hard": (2, 4)}
    _HP = {"easy": (20, 60), "medium": (40, 110), "hard": (60, 180)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        tp_lo, tp_hi = self._TP[difficulty]
        hp_lo, hp_hi = self._HP[difficulty]
        tp = rng.randint(tp_lo, tp_hi)
        hp = rng.randint(hp_lo, hp_hi)
        v0 = 32 * tp
        h0 = hp - 16 * tp * tp
        # If h0 comes out negative (physical nonsense for a release height),
        # bump hp so h0 is non-negative.
        if h0 < 0:
            h0 = rng.randint(2, 8)
            hp = h0 + 16 * tp * tp

        scenarios = [
            (
                "Maya uses a t-shirt launcher at a school pep rally",
                "the t-shirt",
                "school pep rally",
            ),
            (
                "Rohan sets up a water fountain feature at a community garden",
                "a jet of water",
                "community garden fountain",
            ),
            (
                "Priya tests a pop-up book hinge that flings a paper star",
                "the paper star",
                "pop-up book hinge",
            ),
            (
                "Kai rigs a confetti cannon for a maker space demo",
                "the confetti cluster",
                "confetti cannon demo",
            ),
            (
                "Zoe photographs a juggling ball for a photography class",
                "the juggling ball",
                "juggling ball toss",
            ),
        ]
        opener, object_name, _ = rng.choice(scenarios)

        statement = (
            f"{opener}. The height of {object_name} in feet, $t$ seconds after "
            f"release, is given by $h(t) = -16t^{{2}} + {v0} t + {h0}$. "
            f"Determine the time at which {object_name} reaches its maximum "
            f"height and the value of that maximum height."
        )

        poly = -16 * t ** 2 + v0 * t + h0
        discriminant = v0 * v0 - 4 * (-16) * h0
        # Quadratic vertex formulas
        vertex_t = sp.Rational(v0, 32)
        vertex_h = poly.subs(t, vertex_t)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (v0, h0)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=(
                f"Maximum at $t = {tp}$ s with height ${hp}$ ft"
            ),
            hints=[
                r"The vertex of $h(t) = at^2 + bt + c$ sits at $t = -\dfrac{b}{2a}$.",
                f"Here $a = -16$ and $b = {v0}$, so $t = -\\dfrac{{{v0}}}{{2(-16)}} = {tp}$ seconds.",
                f"Substitute $t = {tp}$ into the height equation to get the peak height.",
            ],
            solution_steps_latex=[
                f"Read the model: $h(t) = -16t^{{2}} + {v0} t + {h0}$.",
                f"Use the vertex formula $t = -\\dfrac{{b}}{{2a}} = -\\dfrac{{{v0}}}{{-32}} = {tp}$ seconds.",
                f"Substitute: $h({tp}) = -16({tp})^{{2}} + {v0}({tp}) + {h0} = {hp}$ feet.",
                f"Peak at $t = {tp}$ seconds, maximum height ${hp}$ feet.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-quadratics",
                "#skill-modeling",
            ],
        )


@register
class AreaQuadraticWordProblem(Generator):
    """Rectangle with length = width + k, total area A; solve for width.

    Backward: pick integer width `w0 > 0` and offset `k` so length = w0 + k.
    Area A = w0 * (w0 + k). Student solves w^2 + k*w - A = 0.
    """
    generator_id = "area_quadratic_word_problem"
    topic_slug = "applications_of_quadratics"
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
    topic_slug = "applications_of_quadratics"
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
