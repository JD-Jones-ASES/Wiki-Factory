"""Nonlinear systems (pre-calculus Wave C).

Three generators for the ``nonlinear_systems`` topic slug:

- ParabolaMeetsLineSubstitution: pick two intersection points, derive
  the parabola and line that pass through them, ask the student to
  solve by substitution.
- CircleMeetsLineSubstitution: pick a Pythagorean-triple radius and two
  intersection points on the circle, derive the line, ask to solve.
- NonlinearSystemCountSolutions: classify the number of real solutions
  (0, 1, or 2) of a small nonlinear system. Rotation generator with
  ``bank_count_per_difficulty = 12``.

Backward construction throughout: build the answer first, then derive
the question so SymPy verification is unnecessary (though we still use
it for the count-solutions case).
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


NONLINEAR_TAGS = [
    "#branch-pre-calculus",
    "#topic-systems",
    "#skill-multi-step",
]


def _format_point(x, y) -> str:
    """Render an ordered pair as `(x, y)`."""
    return f"({x},\\ {y})"


def _shift_expr(var: str, shift: int) -> str:
    if shift == 0:
        return var
    op = "-" if shift > 0 else "+"
    return f"({var} {op} {abs(shift)})"


# ===========================================================================
# Generator 1: parabola_meets_line_substitution
# ===========================================================================


@register
class ParabolaMeetsLineSubstitution(Generator):
    """Solve $y = ax^2 + bx + c$ and $y = mx + d$ by substitution.

    Backward: pick two integer intersection points $(x_1, y_1)$ and
    $(x_2, y_2)$ with $x_1 < x_2$, pick a nonzero leading coefficient
    $a$, then build a parabola and a line that both pass through the
    two points. Use SymPy to construct the coefficients and verify.
    """
    generator_id = "parabola_meets_line_substitution"
    topic_slug = "nonlinear_systems"
    display_name = "Solve a parabola/line system by substitution"

    _X_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}
    _A_RANGES = {"easy": (1, 2), "medium": (1, 3), "hard": (1, 4)}
    _T_RANGES = {"easy": (-3, 3), "medium": (-5, 5), "hard": (-6, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        x_lo, x_hi = self._X_RANGES[difficulty]
        a_lo, a_hi = self._A_RANGES[difficulty]
        t_lo, t_hi = self._T_RANGES[difficulty]

        # Pick two distinct roots r1 < r2, then extra parameters.
        while True:
            x1 = rng.randint(x_lo, x_hi)
            x2 = rng.randint(x_lo, x_hi)
            if x1 != x2:
                break
        if x1 > x2:
            x1, x2 = x2, x1

        # Build parabola y = a*(x - r1)*(x - r2) + line(x) where line(x) = m*x + d.
        # Actually easier: pick a nonzero a, pick m and d freely, then define
        # the parabola coefficients so the parabola passes through (x1, y1) and
        # (x2, y2) where y_i = m*x_i + d. Choose a value t such that
        # parabola(x) - line(x) = a*(x - x1)*(x - x2).
        a = rng.randint(a_lo, a_hi) * rng.choice([-1, 1])
        m = rng.randint(t_lo, t_hi)
        d = rng.randint(t_lo, t_hi)

        x = sp.symbols("x")
        parabola_expr = sp.expand(a * (x - x1) * (x - x2) + m * x + d)
        line_expr = sp.expand(m * x + d)

        y1 = int(line_expr.subs(x, x1))
        y2 = int(line_expr.subs(x, x2))

        parabola_latex = f"y = {sp.latex(parabola_expr)}"
        line_latex = f"y = {sp.latex(line_expr)}"

        point1_latex = _format_point(x1, y1)
        point2_latex = _format_point(x2, y2)
        answer_latex = f"${point1_latex},\\ {point2_latex}$"

        quad_factored_latex = sp.latex(sp.expand(a * (x - x1) * (x - x2)))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, x1, x2, m, d)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by substitution and give every intersection "
                f"point: $\\begin{{cases}} {parabola_latex} \\\\ {line_latex} "
                "\\end{cases}$"
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Set the two expressions for $y$ equal to each other and "
                    "collect everything on one side."
                ),
                (
                    "You should get a quadratic in $x$. Factor or use the "
                    "quadratic formula to find the two $x$-values, then "
                    "substitute back into the line to recover $y$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Set the right-hand sides equal: "
                    f"${sp.latex(parabola_expr)} = {sp.latex(line_expr)}$."
                ),
                (
                    "Move everything to one side: "
                    f"${quad_factored_latex} = 0$."
                ),
                (
                    f"Factor: ${a} {_shift_expr('x', x1)}{_shift_expr('x', x2)} = 0$, "
                    f"so $x = {x1}$ or $x = {x2}$."
                ),
                (
                    f"Substitute back into the line: "
                    f"at $x = {x1}$, $y = {y1}$; at $x = {x2}$, $y = {y2}$."
                ),
                f"The intersection points are ${point1_latex}$ and ${point2_latex}$.",
            ],
            tags=NONLINEAR_TAGS,
        )


# ===========================================================================
# Generator 2: circle_meets_line_substitution
# ===========================================================================


_CIRCLE_TRIPLES = (
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
)


@register
class CircleMeetsLineSubstitution(Generator):
    """Solve $x^2 + y^2 = r^2$ and a horizontal/vertical line by substitution.

    Backward: pick a Pythagorean triple $(p, q, r)$ so the circle
    $x^2 + y^2 = r^2$ passes through integer points $(\\pm p, \\pm q)$
    and $(\\pm q, \\pm p)$. Then pick a horizontal or vertical line that
    intersects the circle at two clean integer points.
    """
    generator_id = "circle_meets_line_substitution"
    topic_slug = "nonlinear_systems"
    display_name = "Solve a circle/line system by substitution"
    bank_count_per_difficulty = 8

    _TRIPLES_BY_DIFFICULTY = {
        "easy": ((3, 4, 5),),
        "medium": ((3, 4, 5), (5, 12, 13)),
        "hard": _CIRCLE_TRIPLES,
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        triple = rng.choice(self._TRIPLES_BY_DIFFICULTY[difficulty])
        p, q, r = triple

        # Decide whether the line is horizontal (y = k) or vertical (x = k).
        mode = rng.choice(["horizontal", "vertical"])
        # Decide which of the two integers (p or q) will lie on the line's
        # axis so both intersection points come out integer.
        value_for_line = rng.choice([p, -p, q, -q])

        r_sq = r * r

        if mode == "horizontal":
            # y = value_for_line, so x^2 = r^2 - value_for_line^2
            k = value_for_line
            x_sq = r_sq - k * k
            x_val = int(round(x_sq ** 0.5))
            # x_val could be p or q depending on which we picked.
            assert x_val * x_val == x_sq, "Pythagorean integer check failed"
            point1 = (-x_val, k)
            point2 = (x_val, k)
            line_latex = f"y = {k}"
            substitution_step = (
                f"Substitute $y = {k}$ into $x^2 + y^2 = {r_sq}$: "
                f"$x^2 + ({k})^2 = {r_sq}$, so $x^2 = {r_sq} - {k * k} = {x_sq}$."
            )
            solve_step = (
                f"Take square roots: $x = \\pm{x_val}$."
            )
        else:
            k = value_for_line
            y_sq = r_sq - k * k
            y_val = int(round(y_sq ** 0.5))
            assert y_val * y_val == y_sq, "Pythagorean integer check failed"
            point1 = (k, -y_val)
            point2 = (k, y_val)
            line_latex = f"x = {k}"
            substitution_step = (
                f"Substitute $x = {k}$ into $x^2 + y^2 = {r_sq}$: "
                f"$({k})^2 + y^2 = {r_sq}$, so $y^2 = {r_sq} - {k * k} = {y_sq}$."
            )
            solve_step = (
                f"Take square roots: $y = \\pm{y_val}$."
            )

        point1_latex = _format_point(*point1)
        point2_latex = _format_point(*point2)
        answer_latex = f"${point1_latex},\\ {point2_latex}$"

        circle_latex = f"x^2 + y^2 = {r_sq}"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (triple, mode, value_for_line)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by substitution and list all intersection "
                f"points: $\\begin{{cases}} {circle_latex} \\\\ {line_latex} "
                "\\end{cases}$"
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Substitute the expression for the fixed variable into the "
                    "circle's equation."
                ),
                (
                    "Solve for the remaining variable by isolating its square, "
                    "then taking $\\pm$ the square root."
                ),
            ],
            solution_steps_latex=[
                substitution_step,
                solve_step,
                (
                    f"The two intersection points are ${point1_latex}$ and "
                    f"${point2_latex}$."
                ),
            ],
            tags=NONLINEAR_TAGS,
        )


# ===========================================================================
# Generator 3: nonlinear_system_count_solutions
# ===========================================================================


@register
class NonlinearSystemCountSolutions(Generator):
    """Count the real solutions of a parabola/line or circle/line system.

    Rotation generator: pick a scenario family, then set the discriminant
    (or the distance from centre to line) so the answer is 0, 1, or 2.
    The parameter space is small, so we cap the bank at 12 per difficulty.
    """
    generator_id = "nonlinear_system_count_solutions"
    topic_slug = "nonlinear_systems"
    display_name = "Count real solutions of a nonlinear system"

    bank_count_per_difficulty = 12

    _COUNTS = (0, 1, 2)
    _FAMILIES = ("parabola_line", "circle_line")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        family = rng.choice(self._FAMILIES)
        target_count = rng.choice(self._COUNTS)

        x, y = sp.symbols("x y")

        if family == "parabola_line":
            # y = x^2 + c, y = k. Difference is x^2 + (c - k) = 0.
            # Number of real x's: 2 if c - k < 0, 1 if c - k == 0, 0 if > 0.
            k = rng.randint(-6, 6)
            if target_count == 0:
                c = k + rng.randint(1, 6)
            elif target_count == 1:
                c = k
            else:
                c = k - rng.randint(1, 6)
            parabola_latex = f"y = x^2 + {c}" if c >= 0 else f"y = x^2 - {abs(c)}"
            # adjust sign rendering for c = 0
            if c == 0:
                parabola_latex = "y = x^2"
            line_latex = f"y = {k}"

            disc_value = k - c  # x^2 = k - c
            if disc_value > 0:
                solve_explanation = (
                    f"Setting $y$-values equal: $x^2 + {c} = {k}$, so "
                    f"$x^2 = {disc_value}$. Two real solutions for $x$."
                )
            elif disc_value == 0:
                solve_explanation = (
                    f"Setting $y$-values equal: $x^2 + {c} = {k}$, so "
                    f"$x^2 = 0$. Exactly one real solution ($x = 0$)."
                )
            else:
                solve_explanation = (
                    f"Setting $y$-values equal: $x^2 + {c} = {k}$, so "
                    f"$x^2 = {disc_value}$. A negative value on the right gives "
                    "no real solutions."
                )

            system_latex = (
                f"\\begin{{cases}} {parabola_latex} \\\\ {line_latex} \\end{{cases}}"
            )
            params = (family, c, k)

        else:  # circle_line
            # x^2 + y^2 = r^2, line y = k (horizontal).
            # Distance from origin to line is |k|. Number of intersections:
            # 2 if |k| < r, 1 if |k| == r, 0 if |k| > r.
            if difficulty == "easy":
                r = rng.choice([3, 5])
            else:
                r = rng.choice([3, 5, 13])
            r_sq = r * r
            if target_count == 2:
                k = rng.randint(-(r - 1), r - 1)
            elif target_count == 1:
                k = rng.choice([r, -r])
            else:
                k = rng.randint(r + 1, r + 4) * rng.choice([-1, 1])

            circle_latex = f"x^2 + y^2 = {r_sq}"
            line_latex = f"y = {k}"

            abs_k = abs(k)
            if abs_k < r:
                solve_explanation = (
                    f"The line's distance from the origin is $|{k}| = {abs_k}$, "
                    f"which is less than $r = {r}$, so the line crosses the "
                    "circle at TWO points."
                )
            elif abs_k == r:
                solve_explanation = (
                    f"The line's distance from the origin equals $r = {r}$, "
                    "so the line is tangent and meets the circle at exactly ONE "
                    "point."
                )
            else:
                solve_explanation = (
                    f"The line's distance from the origin is $|{k}| = {abs_k}$, "
                    f"which exceeds $r = {r}$, so the line MISSES the circle "
                    "entirely (no real solutions)."
                )
            system_latex = (
                f"\\begin{{cases}} {circle_latex} \\\\ {line_latex} \\end{{cases}}"
            )
            params = (family, r, k)

        # Compose answer
        if target_count == 0:
            answer_latex = "$0$ real solutions"
        elif target_count == 1:
            answer_latex = "$1$ real solution"
        else:
            answer_latex = "$2$ real solutions"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"How many real solutions does the system ${system_latex}$ have? "
                "Answer $0$, $1$, or $2$."
            ),
            answer_latex=answer_latex,
            hints=[
                (
                    "Combine the equations to get a single equation in one "
                    "variable."
                ),
                (
                    "For a quadratic, check the sign of the discriminant. For a "
                    "circle and line, compare the line's distance from the "
                    "centre to the radius."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Write the system: ${system_latex}$."
                ),
                solve_explanation,
                f"Answer: {answer_latex}.",
            ],
            tags=NONLINEAR_TAGS,
        )
