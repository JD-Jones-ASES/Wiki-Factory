"""Systems-of-equations generators (Phase 2c Wave 2 + Wave B).

Canonical topic slugs:
- solving_systems_by_substitution (Algebra I Ch 5.2)
- systems_of_linear_equations (Wave B)
- solving_systems_by_graphing (Wave B)

Wave B adds:
- solve_system_two_equations_substitution
- classify_system
- solve_system_word_problem
- solve_system_graphing_integer_intersection
- solve_system_graphing_no_solution_detect
- solve_system_graphing_infinite_solutions_detect
- substitution_with_isolated_variable
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
y = sp.Symbol("y")


# ---------------------------------------------------------------------------

@register
class SystemsSubstitutionIsolatedY(Generator):
    """Solve a system where one equation is already y = mx + b."""
    generator_id = "systems_substitution_isolated_y"
    topic_slug = "solving_systems_by_substitution"
    display_name = "Solve a system by substitution (y isolated)"

    _COEF_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        # Pick the solution first
        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # First equation: y = m*x + b
        m = rng.randint(-coef_hi, coef_hi)
        while m == 0:
            m = rng.randint(-coef_hi, coef_hi)
        b1 = y_val - m * x_val

        # Second equation: a*x + c*y = d with integer coefficients
        a = rng.randint(1, coef_hi)
        c = rng.randint(1, coef_hi)
        if rng.random() < 0.5:
            c = -c
        d = a * x_val + c * y_val

        eq1_latex = sp.latex(sp.Eq(y, m * x + b1))
        eq2_latex = sp.latex(sp.Eq(a * x + c * y, d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b1, a, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by substitution:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                r"The first equation gives $y$ directly. Substitute that expression for $y$ into the second equation.",
                f"Replace $y$ with ${sp.latex(m * x + b1)}$ in the second equation.",
                f"Solve the resulting one-variable equation for $x$, then use $x = {x_val}$ to find $y$.",
            ],
            solution_steps_latex=[
                f"First equation: $y = {sp.latex(m * x + b1)}$.",
                f"Substitute into the second equation: ${a}x + ({c})({sp.latex(m * x + b1)}) = {d}$.",
                f"Simplify and solve: $x = {x_val}$.",
                f"Substitute back: $y = ({m})({x_val}) + ({b1}) = {y_val}$.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )


@register
class SystemsSubstitutionIsolatedX(Generator):
    """Solve a system where one equation is already x = ...; substitute into the other."""
    generator_id = "systems_substitution_isolated_x"
    topic_slug = "solving_systems_by_substitution"
    display_name = "Solve a system by substitution (x isolated)"

    _COEF_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 18)}
    _VAR_RANGE = {"easy": (-8, 8), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        coef_lo, coef_hi = self._COEF_RANGE[difficulty]
        var_lo, var_hi = self._VAR_RANGE[difficulty]

        x_val = rng.randint(var_lo, var_hi)
        y_val = rng.randint(var_lo, var_hi)

        # First equation: x = m*y + b
        m = rng.randint(-coef_hi, coef_hi)
        while m == 0:
            m = rng.randint(-coef_hi, coef_hi)
        b1 = x_val - m * y_val

        a = rng.randint(1, coef_hi)
        c = rng.randint(1, coef_hi)
        if rng.random() < 0.5:
            c = -c
        d = a * x_val + c * y_val

        eq1_latex = sp.latex(sp.Eq(x, m * y + b1))
        eq2_latex = sp.latex(sp.Eq(a * x + c * y, d))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b1, a, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve the system by substitution:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$x = {x_val}, \\quad y = {y_val}$",
            hints=[
                r"The first equation gives $x$ directly. Substitute that expression for $x$ into the second equation.",
                f"Replace $x$ with ${sp.latex(m * y + b1)}$ in the second equation.",
                f"Solve the resulting one-variable equation for $y$, then compute $x$.",
            ],
            solution_steps_latex=[
                f"First equation: $x = {sp.latex(m * y + b1)}$.",
                f"Substitute into the second: $({a})({sp.latex(m * y + b1)}) + ({c})y = {d}$.",
                f"Simplify and solve: $y = {y_val}$.",
                f"Substitute back: $x = ({m})({y_val}) + ({b1}) = {x_val}$.",
                f"Solution: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )


# ============================================================================
# Wave B: systems_of_linear_equations
# ============================================================================

@register
class SolveSystemTwoEquationsSubstitution(Generator):
    """Solve a system of two linear equations in standard form via substitution."""
    generator_id = "solve_system_two_equations_substitution"
    topic_slug = "systems_of_linear_equations"
    display_name = "Find (x, y) satisfying a pair of linear equations"

    _COEF = {"easy": (1, 5), "medium": (2, 9), "hard": (2, 14)}
    _VAR = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cl, ch = self._COEF[difficulty]
        vl, vh = self._VAR[difficulty]

        x_val = rng.randint(vl, vh)
        y_val = rng.randint(vl, vh)

        while True:
            a1 = rng.randint(cl, ch)
            b1 = rng.randint(cl, ch)
            a2 = rng.randint(cl, ch)
            b2 = rng.randint(cl, ch)
            # optional sign flips
            if rng.random() < 0.4:
                b1 = -b1
            if rng.random() < 0.4:
                a2 = -a2
            # Non-degenerate: a1*b2 - a2*b1 != 0
            if a1 * b2 - a2 * b1 != 0:
                break

        c1 = a1 * x_val + b1 * y_val
        c2 = a2 * x_val + b2 * y_val

        eq1_latex = sp.latex(sp.Eq(a1 * x + b1 * y, c1))
        eq2_latex = sp.latex(sp.Eq(a2 * x + b2 * y, c2))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a1, b1, c1, a2, b2, c2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Find the $(x, y)$ that satisfies both equations:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$(x, y) = ({x_val}, {y_val})$",
            hints=[
                r"Solve one equation for one variable, then substitute into the other.",
                f"From the first equation you can isolate one variable in terms of the other.",
                f"Solve the resulting single-variable equation, then substitute back.",
            ],
            solution_steps_latex=[
                f"Start with $\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$.",
                f"Solve the first equation for a variable and substitute into the second.",
                f"Solve the resulting single-variable equation; the result is $x = {x_val}$.",
                f"Substitute back to find $y = {y_val}$.",
                f"Solution: $(x, y) = ({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )


@register
class ClassifySystem(Generator):
    """Classify a system as having one solution, no solution, or infinitely many solutions."""
    generator_id = "classify_system"
    topic_slug = "systems_of_linear_equations"
    display_name = "Classify the solution set of a linear system"

    _COEF = {"easy": (1, 6), "medium": (2, 10), "hard": (2, 15)}
    _CONST = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cl, ch = self._COEF[difficulty]
        nl, nh = self._CONST[difficulty]

        classification = rng.choice(["one", "none", "infinite"])

        if classification == "one":
            while True:
                a1 = rng.randint(cl, ch)
                b1 = rng.randint(cl, ch)
                a2 = rng.randint(cl, ch)
                b2 = rng.randint(cl, ch)
                if a1 * b2 - a2 * b1 != 0:
                    break
            c1 = rng.randint(nl, nh)
            c2 = rng.randint(nl, nh)
            answer = "one solution"
            reason = (
                "The slopes are different (the ratio of coefficients on $x$ to $y$ is "
                "not the same), so the lines intersect at exactly one point."
            )

        elif classification == "none":
            # parallel, different intercepts
            a1 = rng.randint(cl, ch)
            b1 = rng.randint(cl, ch)
            scale = rng.choice([2, 3])
            a2 = a1 * scale
            b2 = b1 * scale
            c1 = rng.randint(nl, nh)
            # c2 must NOT equal c1 * scale for the system to be inconsistent
            while True:
                c2 = rng.randint(nl, nh)
                if c2 != c1 * scale:
                    break
            answer = "no solution"
            reason = (
                "Dividing the second equation by the common factor shows the two lines "
                "have the same slope but different constants, so they are parallel and "
                "never intersect."
            )

        else:  # infinite
            a1 = rng.randint(cl, ch)
            b1 = rng.randint(cl, ch)
            scale = rng.choice([2, 3])
            a2 = a1 * scale
            b2 = b1 * scale
            c1 = rng.randint(nl, nh)
            c2 = c1 * scale
            answer = "infinitely many solutions"
            reason = (
                "The second equation is a multiple of the first, so the two equations "
                "represent the same line. Every point on the line is a solution."
            )

        eq1_latex = sp.latex(sp.Eq(a1 * x + b1 * y, c1))
        eq2_latex = sp.latex(sp.Eq(a2 * x + b2 * y, c2))

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a1, b1, c1, a2, b2, c2, classification)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Classify the system as having one solution, no solution, or "
                "infinitely many solutions:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=answer,
            hints=[
                r"Compare the ratios of coefficients. If $\tfrac{a_1}{a_2} = \tfrac{b_1}{b_2} = \tfrac{c_1}{c_2}$, the lines are the same.",
                r"If $\tfrac{a_1}{a_2} = \tfrac{b_1}{b_2}$ but $\neq \tfrac{c_1}{c_2}$, the lines are parallel and there is no solution.",
                r"Otherwise the lines intersect at exactly one point.",
            ],
            solution_steps_latex=[
                f"Start with $\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$.",
                f"Compare the ratios: $\\tfrac{{{a1}}}{{{a2}}}$ and $\\tfrac{{{b1}}}{{{b2}}}$ and $\\tfrac{{{c1}}}{{{c2}}}$.",
                reason,
                f"Classification: {answer}.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-algebraic-manipulation"],
        )


@register
class SolveSystemWordProblem(Generator):
    """Two-variable word problem: ticket prices, item mixes, or rate problems."""
    generator_id = "solve_system_word_problem"
    topic_slug = "systems_of_linear_equations"
    display_name = "Translate and solve a two-variable word problem"
    supports_word_problems = True
    bank_count_per_difficulty = 25

    _SCENARIOS = [
        {
            "name": "Maya",
            "context": "school newspaper",
            "item_a": "full-page ad",
            "item_b": "half-page ad",
            "price_range_a": (40, 80),
            "price_range_b": (15, 35),
            "total_label": "advertising revenue",
            "count_total_label": "total ads sold",
        },
        {
            "name": "Kai",
            "context": "science fair",
            "item_a": "adult ticket",
            "item_b": "student ticket",
            "price_range_a": (6, 15),
            "price_range_b": (2, 6),
            "total_label": "total revenue",
            "count_total_label": "total tickets",
        },
        {
            "name": "Priya",
            "context": "food pantry fundraiser",
            "item_a": "soup bowl",
            "item_b": "salad bowl",
            "price_range_a": (5, 12),
            "price_range_b": (3, 7),
            "total_label": "total collected",
            "count_total_label": "total bowls served",
        },
        {
            "name": "Rohan",
            "context": "local band merch table",
            "item_a": "T-shirt",
            "item_b": "sticker pack",
            "price_range_a": (15, 30),
            "price_range_b": (4, 9),
            "total_label": "total sales",
            "count_total_label": "total items sold",
        },
        {
            "name": "Leilani",
            "context": "coffee shop",
            "item_a": "latte",
            "item_b": "pastry",
            "price_range_a": (4, 8),
            "price_range_b": (2, 5),
            "total_label": "total sales",
            "count_total_label": "total items sold",
        },
    ]

    _COUNT_RANGE = {"easy": (5, 20), "medium": (10, 40), "hard": (15, 60)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COUNT_RANGE[difficulty]
        scenario = rng.choice(self._SCENARIOS)

        price_a = rng.randint(*scenario["price_range_a"])
        price_b = rng.randint(*scenario["price_range_b"])
        while price_a == price_b:
            price_b = rng.randint(*scenario["price_range_b"])

        x_val = rng.randint(c_lo, c_hi)  # number of item_a
        y_val = rng.randint(c_lo, c_hi)  # number of item_b
        total_count = x_val + y_val
        total_money = price_a * x_val + price_b * y_val

        name = scenario["name"]
        ctx = scenario["context"]
        a = scenario["item_a"]
        b = scenario["item_b"]

        statement = (
            f"{name} tallied up the {ctx}. Each {a} sold for $\\${price_a}$, and "
            f"each {b} sold for $\\${price_b}$. In all, ${total_count}$ "
            f"{scenario['count_total_label']} brought in $\\${total_money}$. "
            f"Determine how many of each were sold."
        )

        answer = f"${x_val}$ {a}s and ${y_val}$ {b}s"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (scenario["name"], price_a, price_b, total_count, total_money),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Let $x$ be the number of {a}s and $y$ the number of {b}s.",
                f"Write two equations: one for the total count and one for the total money.",
                f"Total count: $x + y = {total_count}$. Total money: ${price_a}x + {price_b}y = {total_money}$.",
            ],
            solution_steps_latex=[
                f"Let $x$ = number of {a}s, $y$ = number of {b}s.",
                f"Count equation: $x + y = {total_count}$.",
                f"Money equation: ${price_a}x + {price_b}y = {total_money}$.",
                f"Solve the first for $y$: $y = {total_count} - x$.",
                f"Substitute into the money equation: ${price_a}x + {price_b}({total_count} - x) = {total_money}$.",
                f"Expand and simplify: $({price_a - price_b})x + {price_b * total_count} = {total_money}$.",
                f"Solve for $x$: $x = {x_val}$. Then $y = {total_count} - {x_val} = {y_val}$.",
                f"Answer: ${x_val}$ {a}s and ${y_val}$ {b}s.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-systems",
                "#skill-multi-step",
                "#skill-translation",
                "#word-problem-support",
            ],
        )


# ============================================================================
# Wave B: solving_systems_by_graphing
# ============================================================================

@register
class SolveSystemGraphingIntegerIntersection(Generator):
    """Solve a system graphically when both lines are in slope-intercept form and the intersection is integer."""
    generator_id = "solve_system_graphing_integer_intersection"
    topic_slug = "solving_systems_by_graphing"
    display_name = "Solve by graphing (integer intersection)"

    _SLOPE_RANGE = {"easy": (1, 4), "medium": (1, 6), "hard": (1, 9)}
    _X_RANGE = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._SLOPE_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]

        x_val = rng.randint(x_lo, x_hi)
        y_val = rng.randint(x_lo, x_hi)

        # Two distinct slopes
        while True:
            m1 = rng.randint(-m_hi, m_hi)
            if m1 == 0:
                continue
            m2 = rng.randint(-m_hi, m_hi)
            if m2 == 0 or m2 == m1:
                continue
            break

        # y = m*x + b, so b = y_val - m*x_val
        b1 = y_val - m1 * x_val
        b2 = y_val - m2 * x_val

        def _line_latex(m, b):
            if m == 1:
                mx = "x"
            elif m == -1:
                mx = "-x"
            else:
                mx = f"{m}x"
            if b == 0:
                return f"y = {mx}"
            if b > 0:
                return f"y = {mx} + {b}"
            return f"y = {mx} - {abs(b)}"

        eq1 = _line_latex(m1, b1)
        eq2 = _line_latex(m2, b2)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m1, b1, m2, b2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Solve by graphing: ${eq1}$ and ${eq2}$.",
            answer_latex=f"$(x, y) = ({x_val}, {y_val})$",
            hints=[
                r"Graph each line using its slope and y-intercept, then read off the point where they cross.",
                f"Both lines pass through the point $({x_val}, {y_val})$.",
                r"You can verify algebraically by setting the right-hand sides equal.",
            ],
            solution_steps_latex=[
                f"Graph the first line ${eq1}$ and the second line ${eq2}$.",
                f"Set the $y$ values equal: ${m1}x + {b1} = {m2}x + {b2}$.",
                f"Move the $x$-terms together: $({m1 - m2})x = {b2 - b1}$.",
                f"Divide to find $x = {x_val}$.",
                f"Substitute into either equation: $y = {y_val}$.",
                f"Intersection: $({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-visualization"],
        )


@register
class SolveSystemGraphingNoSolutionDetect(Generator):
    """Detect parallel lines (same slope, different intercepts) → no solution."""
    generator_id = "solve_system_graphing_no_solution_detect"
    topic_slug = "solving_systems_by_graphing"
    display_name = "Recognize a no-solution system by graphing"

    _SLOPE_RANGE = {"easy": (1, 5), "medium": (1, 8), "hard": (1, 12)}
    _B_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._SLOPE_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]

        m = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m = -m
        if m == 0:
            m = 1
        b1 = rng.randint(b_lo, b_hi)
        while True:
            b2 = rng.randint(b_lo, b_hi)
            if b2 != b1:
                break

        def _line_latex(m, b):
            if m == 1:
                mx = "x"
            elif m == -1:
                mx = "-x"
            else:
                mx = f"{m}x"
            if b == 0:
                return f"y = {mx}"
            if b > 0:
                return f"y = {mx} + {b}"
            return f"y = {mx} - {abs(b)}"

        eq1 = _line_latex(m, b1)
        eq2 = _line_latex(m, b2)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b1, b2)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine the number of solutions of the system "
                f"${eq1}$ and ${eq2}$ by examining the graphs."
            ),
            answer_latex="no solution",
            hints=[
                r"Compare the slopes and $y$-intercepts of the two lines.",
                r"If the slopes are equal but the $y$-intercepts are different, the lines are parallel.",
                r"Parallel lines never cross, so the system has no solution.",
            ],
            solution_steps_latex=[
                f"Read the slopes: both lines have slope ${m}$.",
                f"Read the $y$-intercepts: ${b1}$ and ${b2}$, which are different.",
                "Equal slopes + different intercepts = parallel lines.",
                "Parallel lines do not intersect, so the system has no solution.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-visualization"],
        )


@register
class SolveSystemGraphingInfiniteSolutionsDetect(Generator):
    """Recognize the same line written two ways → infinitely many solutions."""
    generator_id = "solve_system_graphing_infinite_solutions_detect"
    topic_slug = "solving_systems_by_graphing"
    display_name = "Recognize an infinite-solution system by graphing"

    _COEF = {"easy": (1, 6), "medium": (2, 10), "hard": (2, 15)}
    _CONST = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-35, 35)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        cl, ch = self._COEF[difficulty]
        nl, nh = self._CONST[difficulty]

        a = rng.randint(cl, ch)
        if rng.random() < 0.4:
            a = -a
        if a == 0:
            a = 1
        b = rng.randint(cl, ch)
        if rng.random() < 0.4:
            b = -b
        if b == 0:
            b = 1
        c = rng.randint(nl, nh)

        scale = rng.choice([2, 3, 4])
        a2 = a * scale
        b2 = b * scale
        c2 = c * scale

        eq1 = sp.latex(sp.Eq(a * x + b * y, c))
        eq2 = sp.latex(sp.Eq(a2 * x + b2 * y, c2))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, scale)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Determine the number of solutions of the system by examining the graphs:\n\n"
                f"$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$"
            ),
            answer_latex="infinitely many solutions",
            hints=[
                r"Check whether one equation is a multiple of the other.",
                f"If you divide the second equation by ${scale}$, you get the first equation back.",
                r"Two equations for the same line share every point on the line.",
            ],
            solution_steps_latex=[
                f"Divide the second equation ${eq2}$ by ${scale}$.",
                f"The result is ${eq1}$, the same as the first equation.",
                "Both equations describe the same line.",
                "Every point on the line satisfies both equations, so there are infinitely many solutions.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-visualization"],
        )


# ============================================================================
# Wave B: solving_systems_by_substitution (1 more to reach 3)
# ============================================================================

@register
class SubstitutionWithIsolatedVariable(Generator):
    """System where the first equation already has a variable isolated; direct substitute."""
    generator_id = "substitution_with_isolated_variable"
    topic_slug = "solving_systems_by_substitution"
    display_name = "Substitute an isolated variable into the other equation"

    _SLOPE = {"easy": (1, 5), "medium": (1, 8), "hard": (2, 12)}
    _VAR = {"easy": (-7, 7), "medium": (-12, 12), "hard": (-18, 18)}
    _COEF = {"easy": (1, 6), "medium": (2, 10), "hard": (2, 14)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._SLOPE[difficulty]
        v_lo, v_hi = self._VAR[difficulty]
        c_lo, c_hi = self._COEF[difficulty]

        x_val = rng.randint(v_lo, v_hi)
        y_val = rng.randint(v_lo, v_hi)

        # First equation y = m*x + b, passing through (x_val, y_val)
        m = rng.randint(m_lo, m_hi)
        if rng.random() < 0.5:
            m = -m
        if m == 0:
            m = 1
        b1 = y_val - m * x_val

        # Second equation: a*x + c*y = d, linearly independent from the first
        while True:
            a = rng.randint(c_lo, c_hi)
            c = rng.randint(c_lo, c_hi)
            if rng.random() < 0.4:
                c = -c
            # Avoid the line y = mx + b1 being literally the same as the second line
            # a*x + c*y = d equivalent to y = -(a/c)x + d/c. So slope = -a/c.
            if c != 0 and -a != m * c:
                break
        d = a * x_val + c * y_val

        eq1_latex = sp.latex(sp.Eq(y, m * x + b1))
        eq2_latex = sp.latex(sp.Eq(a * x + c * y, d))
        subst_expr = sp.latex(m * x + b1)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (m, b1, a, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                "Solve by substitution:\n\n"
                f"$$\\begin{{cases}} {eq1_latex} \\\\ {eq2_latex} \\end{{cases}}$$"
            ),
            answer_latex=f"$(x, y) = ({x_val}, {y_val})$",
            hints=[
                r"The first equation already gives $y$ in terms of $x$. Substitute that expression for $y$ into the second equation.",
                f"Replace $y$ with ${subst_expr}$ in the second equation.",
                r"Solve the resulting single-variable equation for $x$, then substitute back to find $y$.",
            ],
            solution_steps_latex=[
                f"First equation: $y = {subst_expr}$ (already solved for $y$).",
                f"Substitute into the second: ${a}x + ({c})({subst_expr}) = {d}$.",
                f"Distribute: ${a}x + {c * m}x + {c * b1} = {d}$.",
                f"Combine like terms: $({a + c * m})x = {d - c * b1}$.",
                f"Solve: $x = {x_val}$.",
                f"Substitute back: $y = ({m})({x_val}) + ({b1}) = {y_val}$.",
                f"Solution: $(x, y) = ({x_val}, {y_val})$.",
            ],
            tags=["#branch-algebra-1", "#topic-systems", "#skill-multi-step"],
        )
