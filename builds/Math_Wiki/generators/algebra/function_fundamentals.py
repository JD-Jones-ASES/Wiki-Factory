"""Function fundamentals generators (Phase 2c Wave 4).

Five topics covering the core ideas of functions:

- relations_and_functions (Algebra I): is it a function, vertical line test,
  finite domain and range.
- function_basics (Algebra II): evaluation, domain of rational and radical
  functions.
- function_notation (Pre-Calculus): numeric evaluation, algebraic input
  substitution, difference quotient.
- function_arithmetic_and_composition (Algebra II): sum/difference, numeric
  composition, symbolic composition.
- inverse_functions (Algebra II): find inverse of a linear function, verify
  by composition, horizontal line test classification.
"""
from __future__ import annotations

import random
from fractions import Fraction

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


x = sp.Symbol("x")
h_sym = sp.Symbol("h")
t_sym = sp.Symbol("t")
k_sym = sp.Symbol("k")


# ===========================================================================
# Topic 1: relations_and_functions
# ===========================================================================

@register
class IsItAFunctionFromPairs(Generator):
    """Given 4-6 ordered pairs, decide whether the relation is a function."""
    generator_id = "is_it_a_function_from_pairs"
    topic_slug = "relations_and_functions"
    display_name = "Is this set of ordered pairs a function?"

    _RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _SIZES = {"easy": (4, 5), "medium": (5, 6), "hard": (5, 6)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        size_lo, size_hi = self._SIZES[difficulty]
        n = rng.randint(size_lo, size_hi)

        # Backward construction: decide yes/no first, then build pairs.
        is_function = rng.choice([True, False])

        if is_function:
            # All x-values distinct.
            xs: list[int] = []
            while len(xs) < n:
                candidate = rng.randint(lo, hi)
                if candidate not in xs:
                    xs.append(candidate)
            pairs = [(xi, rng.randint(lo, hi)) for xi in xs]
        else:
            # Put in a repeated x with different y values, then fill around it.
            x_repeat = rng.randint(lo, hi)
            y1 = rng.randint(lo, hi)
            y2 = rng.randint(lo, hi)
            while y2 == y1:
                y2 = rng.randint(lo, hi)
            pairs = [(x_repeat, y1), (x_repeat, y2)]
            remaining = [v for v in range(lo, hi + 1) if v != x_repeat]
            rng.shuffle(remaining)
            for xi in remaining[: n - 2]:
                pairs.append((xi, rng.randint(lo, hi)))
            rng.shuffle(pairs)

        pairs_latex = ",\\ ".join(f"({a}, {b})" for a, b in pairs)
        answer = "Yes, this is a function." if is_function else "No, this is not a function."

        # Identify the offending x-value for the solution (if applicable).
        seen: dict[int, int] = {}
        dup_x = None
        dup_ys: tuple[int, int] | None = None
        for a, b in pairs:
            if a in seen and seen[a] != b:
                dup_x = a
                dup_ys = (seen[a], b)
                break
            seen[a] = b

        if is_function:
            reason_step = "Every input (first coordinate) appears at most once, so each input maps to exactly one output. The relation is a function."
        else:
            reason_step = (
                f"The input $x = {dup_x}$ appears twice, once paired with ${dup_ys[0]}$ "
                f"and once with ${dup_ys[1]}$. A function cannot assign two different outputs "
                f"to the same input, so this is not a function."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(sum(pairs, ()))),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Determine whether the following set of ordered pairs represents a function: "
                f"$\\{{{pairs_latex}\\}}$."
            ),
            answer_latex=answer,
            hints=[
                "A relation is a function if and only if every input (first coordinate) is paired with exactly one output.",
                "Scan the pairs and check whether any input value appears more than once.",
                "If a repeated input has two different outputs, the relation is NOT a function.",
            ],
            solution_steps_latex=[
                "List the first coordinates (inputs) of the pairs and look for repeats.",
                reason_step,
                f"Conclusion: {answer}",
            ],
            tags=["#branch-algebra-1", "#topic-functions", "#skill-visualization"],
        )


@register
class ApplyVerticalLineTest(Generator):
    """Given a verbal description of a graph, apply the vertical line test."""
    generator_id = "apply_vertical_line_test"
    topic_slug = "relations_and_functions"
    display_name = "Apply the vertical line test (verbal descriptions)"
    bank_count_per_difficulty = 25  # fixed template pool

    # (description, is_function, reason)
    _SHAPES = [
        (
            "a straight line going up and to the right (non-vertical)",
            True,
            "A non-vertical line passes every vertical line at exactly one point.",
        ),
        (
            "a straight horizontal line",
            True,
            "A horizontal line meets every vertical line exactly once.",
        ),
        (
            "a straight vertical line",
            False,
            "A vertical line IS a vertical line test failure: the line itself crosses infinitely many points with the same x-value.",
        ),
        (
            "a parabola opening upward (like a bowl)",
            True,
            "An upward-opening parabola crosses every vertical line at most once.",
        ),
        (
            "a parabola opening downward",
            True,
            "A downward-opening parabola crosses every vertical line at most once.",
        ),
        (
            "a sideways parabola opening to the right",
            False,
            "A sideways parabola has two y-values for most x-values, so vertical lines can cross it twice.",
        ),
        (
            "a sideways parabola opening to the left",
            False,
            "A sideways parabola has two y-values for most x-values, so vertical lines can cross it twice.",
        ),
        (
            "a circle centered at the origin",
            False,
            "A circle has two y-values for most x-values inside its diameter, so vertical lines cross it twice.",
        ),
        (
            "an ellipse centered at the origin",
            False,
            "An ellipse has two y-values for most x-values, so vertical lines cross it twice.",
        ),
        (
            "the upper half of a circle",
            True,
            "The upper half of a circle has exactly one y-value for each x-value in its domain.",
        ),
        (
            "the right half of a sideways parabola (only points with y >= 0)",
            True,
            "Restricting to y >= 0 leaves a single y-value per x, so it passes the vertical line test.",
        ),
        (
            "a cubic curve that passes through the origin (shaped like a tilted S)",
            True,
            "A standard cubic crosses every vertical line exactly once.",
        ),
        (
            "an absolute value V-shape opening upward",
            True,
            "An absolute value graph has exactly one y-value for each x-value.",
        ),
        (
            "a square-root curve starting at the origin",
            True,
            "A square-root curve gives exactly one y-value for each x in its domain.",
        ),
        (
            "a cube-root curve passing through the origin",
            True,
            "A cube-root curve has exactly one y-value for each x-value.",
        ),
        (
            "the exponential curve y = 2^x",
            True,
            "Exponential curves assign exactly one y-value to each x-value.",
        ),
        (
            "a horizontal ellipse wider than it is tall",
            False,
            "An ellipse has two y-values for most x-values, so vertical lines cross it twice.",
        ),
        (
            "a hyperbola with two branches opening left and right",
            False,
            "Each branch has two y-values for most x-values in its domain, so vertical lines can cross twice.",
        ),
        (
            "a hyperbola with two branches opening up and down",
            True,
            "Up-down hyperbolas have only one y-value per x-value on each branch, combined they still pass the vertical line test.",
        ),
        (
            "the graph of y = 1/x (two curved branches)",
            True,
            "y = 1/x assigns exactly one y-value to every non-zero x.",
        ),
        (
            "a wavy sine curve going left to right",
            True,
            "A sine curve has exactly one y-value for each x-value.",
        ),
        (
            "a closed loop shaped like a heart",
            False,
            "A closed loop has two y-values for most x-values, so vertical lines cross it twice.",
        ),
        (
            "a graph made of two disconnected horizontal line segments at different heights over different x-intervals",
            True,
            "Disjoint horizontal segments over disjoint x-intervals give one y-value per x.",
        ),
        (
            "a graph made of two vertical line segments at x = 1 and x = 4",
            False,
            "Any piece that runs vertically has infinitely many y-values at a single x-value.",
        ),
        (
            "the graph of y = x^3 - x",
            True,
            "Any polynomial in x gives exactly one y-value per x.",
        ),
        (
            "a filled-in disk (solid circle region)",
            False,
            "A disk has many y-values for each interior x-value, so vertical lines cross it many times.",
        ),
        (
            "a diagonal line plus a horizontal line that cross at one point",
            False,
            "At the crossing point the graph is fine, but away from it many x-values get two y-values (one from each line).",
        ),
    ]

    _DIFFICULTY_POOLS = {
        "easy": (0, 10),     # straightforward shapes
        "medium": (4, 22),   # mix in trickier ones
        "hard": (10, 27),    # requires more reasoning
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._DIFFICULTY_POOLS[difficulty]
        idx = rng.randint(lo, min(hi, len(self._SHAPES) - 1))
        description, is_function, reason = self._SHAPES[idx]

        answer = (
            "Yes, this IS the graph of a function."
            if is_function
            else "No, this is NOT the graph of a function."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Imagine the graph of {description}. Using the vertical line test, "
                "determine whether this graph is the graph of a function."
            ),
            answer_latex=answer,
            hints=[
                "The vertical line test: if any vertical line crosses the graph in more than one point, the graph is NOT the graph of a function.",
                "Sketch or picture the shape, then imagine sliding a vertical line across it.",
                "If every vertical line hits the shape at most once, it IS a function.",
            ],
            solution_steps_latex=[
                f"Picture the described graph: {description}.",
                f"Imagine sliding a vertical line left to right. {reason}",
                f"Conclusion: {answer}",
            ],
            tags=["#branch-algebra-1", "#topic-functions", "#skill-visualization"],
        )


@register
class FindDomainAndRangeFinite(Generator):
    """Given a finite relation, list the domain and range as sets."""
    generator_id = "find_domain_and_range_finite"
    topic_slug = "relations_and_functions"
    display_name = "Find domain and range of a finite relation"

    _RANGES = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-15, 15)}
    _SIZES = {"easy": 4, "medium": 5, "hard": 6}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        n = self._SIZES[difficulty]

        # Backward construction: pick distinct xs for clarity, pick ys freely.
        xs: list[int] = []
        while len(xs) < n:
            candidate = rng.randint(lo, hi)
            if candidate not in xs:
                xs.append(candidate)
        ys = [rng.randint(lo, hi) for _ in range(n)]
        pairs = list(zip(xs, ys))

        domain_sorted = sorted(set(xs))
        range_sorted = sorted(set(ys))

        pairs_latex = ",\\ ".join(f"({a}, {b})" for a, b in pairs)
        domain_latex = "\\{" + ",\\ ".join(str(v) for v in domain_sorted) + "\\}"
        range_latex = "\\{" + ",\\ ".join(str(v) for v in range_sorted) + "\\}"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, tuple(sum(pairs, ()))),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"State the domain and range of the relation "
                f"$\\{{{pairs_latex}\\}}$."
            ),
            answer_latex=f"Domain: ${domain_latex}$. Range: ${range_latex}$.",
            hints=[
                "The domain is the set of all first coordinates (inputs).",
                "The range is the set of all second coordinates (outputs).",
                "List each value only once, in increasing order.",
            ],
            solution_steps_latex=[
                f"Collect the first coordinates: ${', '.join(str(a) for a, _ in pairs)}$. "
                f"Remove duplicates and sort: domain $= {domain_latex}$.",
                f"Collect the second coordinates: ${', '.join(str(b) for _, b in pairs)}$. "
                f"Remove duplicates and sort: range $= {range_latex}$.",
            ],
            tags=["#branch-algebra-1", "#topic-functions", "#skill-visualization"],
        )


# ===========================================================================
# Topic 2: function_basics
# ===========================================================================

@register
class EvaluateFunctionAtInteger(Generator):
    """Given f(x) = ax + b or f(x) = ax^2 + bx + c, evaluate at an integer input."""
    generator_id = "evaluate_function_at_integer"
    topic_slug = "function_basics"
    display_name = "Evaluate f(x) at an integer input"

    _COEF_RANGE = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _INPUT_RANGE = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        ilo, ihi = self._INPUT_RANGE[difficulty]

        # Mix linear and quadratic forms.
        use_quadratic = rng.choice([False, True, True])  # bias slightly quadratic
        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)
        c = rng.randint(clo, chi) if use_quadratic else 0
        input_val = rng.randint(ilo, ihi)

        if use_quadratic:
            f_expr = a * x**2 + b * x + c
        else:
            f_expr = a * x + b

        output_val = int(f_expr.subs(x, input_val))
        f_latex = sp.latex(f_expr)

        input_sub = f"({input_val})"
        substituted = f_expr.subs(x, sp.Symbol(input_sub)) if False else None  # placeholder

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, input_val, int(use_quadratic))
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"If $f(x) = {f_latex}$, find $f({input_val})$."
            ),
            answer_latex=f"$f({input_val}) = {output_val}$",
            hints=[
                f"Substitute $x = {input_val}$ into the expression for $f(x)$.",
                "Use parentheses around negative inputs when you substitute.",
                "Simplify using order of operations (exponents, then multiplication, then addition).",
            ],
            solution_steps_latex=[
                f"Start with $f(x) = {f_latex}$.",
                f"Replace every $x$ with ${input_val}$: $f({input_val}) = "
                + sp.latex(f_expr.subs(x, sp.Integer(input_val)))
                + "$.",
                f"Simplify to get $f({input_val}) = {output_val}$.",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-formula-substitution"],
        )


@register
class FindDomainDenominator(Generator):
    """Given a rational function, find the value excluded from the domain."""
    generator_id = "find_domain_denominator"
    topic_slug = "function_basics"
    display_name = "Find the domain of a rational function"

    _NUMER_RANGE = {"easy": (1, 8), "medium": (1, 15), "hard": (1, 25)}
    _COEF_RANGE = {"easy": (1, 8), "medium": (1, 12), "hard": (1, 20)}
    _CONST_RANGE = {"easy": (-9, 9), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        nlo, nhi = self._NUMER_RANGE[difficulty]
        clo, chi = self._COEF_RANGE[difficulty]
        const_lo, const_hi = self._CONST_RANGE[difficulty]

        # Backward construction: pick the excluded x-value, then build (ax + b).
        numer = rng.randint(nlo, nhi)
        # Pick coefficient a (positive 1..chi)
        a = rng.randint(clo, chi)
        # Pick excluded x-value; ensure it's rational-friendly so b is integer
        # x_excluded = -b / a, so choose b so division is clean.
        b_choices = list(range(const_lo, const_hi + 1))
        b = rng.choice(b_choices)
        # Excluded value:
        excluded = sp.Rational(-b, a)

        denom_expr = a * x + b
        numer_expr = sp.Integer(numer)
        f_expr = numer_expr / denom_expr

        f_latex = sp.latex(f_expr)
        excluded_latex = sp.latex(excluded)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (numer, a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the value of $x$ that must be excluded from the domain of "
                f"$f(x) = {f_latex}$."
            ),
            answer_latex=f"$x = {excluded_latex}$ (all real numbers except this value)",
            hints=[
                "The domain of a rational function excludes any value that makes the denominator equal to zero.",
                "Set the denominator equal to zero and solve for $x$.",
                f"Solve ${sp.latex(sp.Eq(denom_expr, 0))}$.",
            ],
            solution_steps_latex=[
                f"The function $f(x) = {f_latex}$ is undefined when its denominator equals zero.",
                f"Solve ${sp.latex(sp.Eq(denom_expr, 0))}$: "
                f"subtract ${b}$ from both sides, then divide by ${a}$.",
                f"$x = {excluded_latex}$, so the domain is all real numbers except $x = {excluded_latex}$.",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-algebraic-manipulation"],
        )


@register
class FindDomainSqrt(Generator):
    """Given f(x) = sqrt(ax + b), find the domain as an inequality."""
    generator_id = "find_domain_sqrt"
    topic_slug = "function_basics"
    display_name = "Find the domain of a square-root function"

    _COEF_RANGE = {"easy": (1, 5), "medium": (1, 10), "hard": (1, 15)}
    _CONST_RANGE = {"easy": (-10, 10), "medium": (-18, 18), "hard": (-30, 30)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        const_lo, const_hi = self._CONST_RANGE[difficulty]

        a = rng.randint(clo, chi)
        b = rng.randint(const_lo, const_hi)
        # The inside of the radical must be >= 0: a*x + b >= 0 => x >= -b/a
        lower = sp.Rational(-b, a)

        inside = a * x + b
        f_expr = sp.sqrt(inside)
        f_latex = sp.latex(f_expr)
        lower_latex = sp.latex(lower)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find the domain of $f(x) = {f_latex}$.",
            answer_latex=f"$x \\geq {lower_latex}$",
            hints=[
                "Inside a square root, the expression must be greater than or equal to zero for the output to be a real number.",
                f"Set up the inequality ${sp.latex(inside)} \\geq 0$ and solve for $x$.",
                f"Subtract ${b}$ from both sides, then divide by ${a}$.",
            ],
            solution_steps_latex=[
                f"For $f(x) = {f_latex}$ to give a real output, the radicand must be non-negative.",
                f"Solve ${sp.latex(inside)} \\geq 0$: "
                f"${sp.latex(a * x)} \\geq {-b}$, then $x \\geq {lower_latex}$.",
                f"Domain: $\\{{ x \\mid x \\geq {lower_latex} \\}}$ or in interval notation, "
                f"$[{lower_latex},\\ \\infty)$.",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 3: function_notation
# ===========================================================================

@register
class FunctionNotationEvaluateNumeric(Generator):
    """Given f(x) = ax^2 + bx + c, evaluate at a numeric input."""
    generator_id = "function_notation_evaluate_numeric"
    topic_slug = "function_notation"
    display_name = "Evaluate f(x) = ax^2 + bx + c at a number"

    _COEF_RANGE = {"easy": (-5, 5), "medium": (-10, 10), "hard": (-18, 18)}
    _INPUT_RANGE = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        ilo, ihi = self._INPUT_RANGE[difficulty]

        # Backward construction is less natural here since picking a, b, c, x
        # directly already yields a clean integer output. Do forward with
        # guardrails to keep a != 0.
        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)
        c = rng.randint(clo, chi)
        input_val = rng.randint(ilo, ihi)

        f_expr = a * x**2 + b * x + c
        output_val = int(f_expr.subs(x, input_val))
        f_latex = sp.latex(f_expr)

        step_sub = sp.latex(
            sp.Integer(a) * sp.Integer(input_val) ** 2
            + sp.Integer(b) * sp.Integer(input_val)
            + sp.Integer(c)
        )
        intermediate = a * input_val * input_val + b * input_val + c  # should equal output_val

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, input_val)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $f(x) = {f_latex}$. Find $f({input_val})$."
            ),
            answer_latex=f"$f({input_val}) = {output_val}$",
            hints=[
                f"Substitute $x = {input_val}$ into $f(x)$. Wrap negative numbers in parentheses before applying the exponent.",
                f"Compute ${input_val}^2$ first, then multiply by the leading coefficient, then add the rest.",
                "Order of operations: exponents, multiplications, additions.",
            ],
            solution_steps_latex=[
                f"Start with $f(x) = {f_latex}$.",
                f"Substitute $x = {input_val}$: $f({input_val}) = {a}({input_val})^2 + {b}({input_val}) + {c}$.",
                f"Evaluate powers: $({input_val})^2 = {input_val * input_val}$, so "
                f"$f({input_val}) = {a} \\cdot {input_val * input_val} + {b} \\cdot {input_val} + {c} "
                f"= {a * input_val * input_val} + {b * input_val} + {c} = {output_val}$.",
            ],
            tags=["#branch-pre-calculus", "#topic-functions", "#skill-formula-substitution"],
        )


@register
class FunctionNotationWithAlgebraicInput(Generator):
    """Given f(x) = ax + b and an algebraic input, substitute and simplify."""
    generator_id = "function_notation_with_algebraic_input"
    topic_slug = "function_notation"
    display_name = "Evaluate f at an algebraic expression like f(t + 3)"

    _COEF_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-18, 18)}
    _SHIFT_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        slo, shi = self._SHIFT_RANGE[difficulty]

        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)

        # Choose the algebraic input: (m * var + k)
        var = rng.choice([t_sym, k_sym])
        m = rng.choice([1, 1, 2, -1, 3])  # bias toward 1
        k = rng.randint(slo, shi)

        input_expr = m * var + k
        f_of_input = sp.expand(a * input_expr + b)

        f_latex = sp.latex(a * x + b)
        input_latex = sp.latex(input_expr)
        answer_latex = sp.latex(f_of_input)

        var_name = "t" if var is t_sym else "k"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, m, k, var_name)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"If $f(x) = {f_latex}$, find $f({input_latex})$ and simplify."
            ),
            answer_latex=f"$f({input_latex}) = {answer_latex}$",
            hints=[
                f"Wherever you see $x$ in the expression for $f$, replace it with $({input_latex})$.",
                "Distribute any outside coefficient carefully.",
                "Combine like terms at the end.",
            ],
            solution_steps_latex=[
                f"Replace $x$ with $({input_latex})$ in $f(x) = {f_latex}$: "
                f"$f({input_latex}) = {a}({input_latex}) + {b}$.",
                f"Distribute the ${a}$: ${sp.latex(sp.expand(a * input_expr))} + {b}$.",
                f"Combine like terms: $f({input_latex}) = {answer_latex}$.",
            ],
            tags=["#branch-pre-calculus", "#topic-functions", "#skill-algebraic-manipulation"],
        )


@register
class FunctionNotationDifferenceQuotient(Generator):
    """Compute the difference quotient (f(x+h) - f(x))/h for f(x) = ax^2 + bx + c."""
    generator_id = "function_notation_difference_quotient"
    topic_slug = "function_notation"
    display_name = "Difference quotient of a quadratic function"
    bank_count_per_difficulty = 20  # small parameter space

    _A_VALUES = {"easy": [1, 2], "medium": [1, 2, 3, -1, -2], "hard": [1, 2, 3, 4, -1, -2, -3]}
    _B_RANGE = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-10, 10)}
    _C_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-15, 15)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a = rng.choice(self._A_VALUES[difficulty])
        b = rng.randint(*self._B_RANGE[difficulty])
        c = rng.randint(*self._C_RANGE[difficulty])

        f_expr = a * x**2 + b * x + c
        f_x_plus_h = a * (x + h_sym) ** 2 + b * (x + h_sym) + c
        diff = sp.expand(f_x_plus_h - f_expr)
        # diff should be 2*a*x*h + a*h^2 + b*h
        quotient = sp.simplify(diff / h_sym)
        quotient_expanded = sp.expand(quotient)

        f_latex = sp.latex(f_expr)
        diff_latex = sp.latex(diff)
        quotient_latex = sp.latex(quotient_expanded)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $f(x) = {f_latex}$. Compute and simplify the difference quotient "
                r"$\dfrac{f(x + h) - f(x)}{h}$."
            ),
            answer_latex=f"${quotient_latex}$",
            hints=[
                "First compute $f(x + h)$ by substituting $(x + h)$ for $x$ everywhere in $f$.",
                "Subtract $f(x)$ from $f(x + h)$ and simplify.",
                "Factor $h$ out of the numerator, then cancel it with the $h$ in the denominator.",
            ],
            solution_steps_latex=[
                f"Compute $f(x + h) = {a}(x + h)^2 + {b}(x + h) + {c}$.",
                f"Expand: $f(x + h) = {sp.latex(sp.expand(f_x_plus_h))}$.",
                f"Subtract $f(x)$: $f(x + h) - f(x) = {diff_latex}$.",
                f"Divide by $h$ (every term has a factor of $h$): "
                f"$\\dfrac{{f(x + h) - f(x)}}{{h}} = {quotient_latex}$.",
            ],
            tags=["#branch-pre-calculus", "#topic-functions", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 4: function_arithmetic_and_composition
# ===========================================================================

@register
class FunctionArithmeticAddSubtract(Generator):
    """Given two linear functions, compute (f+g)(a) or (f-g)(a)."""
    generator_id = "function_arithmetic_add_subtract"
    topic_slug = "function_arithmetic_and_composition"
    display_name = "Compute (f+g)(a) or (f-g)(a)"

    _COEF_RANGE = {"easy": (-6, 6), "medium": (-12, 12), "hard": (-20, 20)}
    _INPUT_RANGE = {"easy": (-5, 5), "medium": (-8, 8), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        ilo, ihi = self._INPUT_RANGE[difficulty]

        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)
        c = rng.randint(clo, chi)
        while c == 0:
            c = rng.randint(clo, chi)
        d = rng.randint(clo, chi)
        input_val = rng.randint(ilo, ihi)
        op = rng.choice(["add", "sub"])

        f_expr = a * x + b
        g_expr = c * x + d
        f_val = int(f_expr.subs(x, input_val))
        g_val = int(g_expr.subs(x, input_val))

        if op == "add":
            combined_expr = sp.expand(f_expr + g_expr)
            combined_val = f_val + g_val
            combined_label = "(f + g)"
            op_symbol = "+"
        else:
            combined_expr = sp.expand(f_expr - g_expr)
            combined_val = f_val - g_val
            combined_label = "(f - g)"
            op_symbol = "-"

        f_latex = sp.latex(f_expr)
        g_latex = sp.latex(g_expr)
        combined_latex = sp.latex(combined_expr)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, d, input_val, op)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $f(x) = {f_latex}$ and $g(x) = {g_latex}$. "
                f"Find ${combined_label}({input_val})$."
            ),
            answer_latex=f"${combined_label}({input_val}) = {combined_val}$",
            hints=[
                f"${combined_label}(x) = f(x) {op_symbol} g(x)$.",
                f"One approach: evaluate $f({input_val})$ and $g({input_val})$ separately, then combine.",
                f"Another approach: first simplify ${combined_label}(x) = {combined_latex}$, then substitute.",
            ],
            solution_steps_latex=[
                f"$f({input_val}) = {f_val}$ and $g({input_val}) = {g_val}$.",
                f"${combined_label}({input_val}) = f({input_val}) {op_symbol} g({input_val}) "
                f"= {f_val} {op_symbol} ({g_val}) = {combined_val}$.",
                f"(Alternative: ${combined_label}(x) = {combined_latex}$, "
                f"then substitute $x = {input_val}$ to get ${combined_val}$.)",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-algebraic-manipulation"],
        )


@register
class FunctionCompositionEvaluate(Generator):
    """Given f and g, compute (f o g)(a) = f(g(a)) at a specific input."""
    generator_id = "function_composition_evaluate"
    topic_slug = "function_arithmetic_and_composition"
    display_name = "Evaluate a composition at a number: f(g(a))"

    _COEF_RANGE = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-15, 15)}
    _INPUT_RANGE = {"easy": (-4, 4), "medium": (-7, 7), "hard": (-10, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        ilo, ihi = self._INPUT_RANGE[difficulty]

        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)
        c = rng.randint(clo, chi)
        while c == 0:
            c = rng.randint(clo, chi)
        d = rng.randint(clo, chi)
        input_val = rng.randint(ilo, ihi)

        f_expr = a * x + b        # f linear for simplicity
        g_expr = c * x + d        # g linear
        g_val = int(g_expr.subs(x, input_val))
        final_val = int(f_expr.subs(x, g_val))

        f_latex = sp.latex(f_expr)
        g_latex = sp.latex(g_expr)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, d, input_val)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $f(x) = {f_latex}$ and $g(x) = {g_latex}$. "
                f"Find $(f \\circ g)({input_val})$."
            ),
            answer_latex=f"$(f \\circ g)({input_val}) = {final_val}$",
            hints=[
                r"$(f \circ g)(a)$ means $f(g(a))$: evaluate $g$ first, then feed the result into $f$.",
                f"Step 1: compute $g({input_val})$.",
                f"Step 2: plug that output into $f$.",
            ],
            solution_steps_latex=[
                f"Compute $g({input_val}) = {c}({input_val}) + ({d}) = {g_val}$.",
                f"Now compute $f(g({input_val})) = f({g_val}) = {a}({g_val}) + ({b}) = {final_val}$.",
                f"Therefore $(f \\circ g)({input_val}) = {final_val}$.",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-multi-step"],
        )


@register
class FunctionCompositionSymbolic(Generator):
    """Given f(x) = ax + b and g(x) = cx + d, write (f o g)(x) as a simplified expression."""
    generator_id = "function_composition_symbolic"
    topic_slug = "function_arithmetic_and_composition"
    display_name = "Symbolic composition (f o g)(x)"

    _COEF_RANGE = {"easy": (-6, 6), "medium": (-10, 10), "hard": (-18, 18)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]

        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)
        c = rng.randint(clo, chi)
        while c == 0:
            c = rng.randint(clo, chi)
        d = rng.randint(clo, chi)

        f_expr = a * x + b
        g_expr = c * x + d
        composed = sp.expand(f_expr.subs(x, g_expr))

        f_latex = sp.latex(f_expr)
        g_latex = sp.latex(g_expr)
        composed_latex = sp.latex(composed)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Given $f(x) = {f_latex}$ and $g(x) = {g_latex}$, "
                f"write $(f \\circ g)(x) = f(g(x))$ as a simplified expression."
            ),
            answer_latex=f"$(f \\circ g)(x) = {composed_latex}$",
            hints=[
                r"To compute $f(g(x))$, substitute the entire expression for $g(x)$ wherever $x$ appears in $f$.",
                f"So $f(g(x)) = {a}(g(x)) + ({b}) = {a}({g_latex}) + ({b})$.",
                "Distribute and combine like terms.",
            ],
            solution_steps_latex=[
                f"Start with $f(x) = {f_latex}$ and $g(x) = {g_latex}$.",
                f"Substitute $g(x)$ in place of $x$ inside $f$: "
                f"$f(g(x)) = {a}({g_latex}) + ({b})$.",
                f"Distribute: ${sp.latex(sp.expand(a * g_expr))} + ({b})$.",
                f"Combine like terms: $(f \\circ g)(x) = {composed_latex}$.",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Topic 5: inverse_functions
# ===========================================================================

@register
class FindInverseLinear(Generator):
    """Given f(x) = ax + b, find f^{-1}(x) = (x - b)/a."""
    generator_id = "find_inverse_linear"
    topic_slug = "inverse_functions"
    display_name = "Find the inverse of a linear function"

    _COEF_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        a = rng.randint(clo, chi)
        while a == 0:
            a = rng.randint(clo, chi)
        b = rng.randint(clo, chi)

        f_expr = a * x + b
        f_latex = sp.latex(f_expr)

        # Inverse: solve y = ax + b for x -> x = (y - b)/a
        inverse_expr = sp.Rational(1, a) * (x - b) if a != 0 else x
        inverse_simplified = sp.simplify(inverse_expr)
        inverse_latex = sp.latex(inverse_simplified)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find the inverse of $f(x) = {f_latex}$.",
            answer_latex=f"$f^{{-1}}(x) = {inverse_latex}$",
            hints=[
                "To find an inverse, replace $f(x)$ with $y$, swap $x$ and $y$, then solve for $y$.",
                f"Start with $y = {f_latex}$. Swap: $x = {sp.latex(a * sp.Symbol('y') + b)}$.",
                f"Solve for $y$: subtract ${b}$, then divide by ${a}$.",
            ],
            solution_steps_latex=[
                f"Write $y = {f_latex}$.",
                f"Swap $x$ and $y$: $x = {a}y + ({b})$.",
                f"Subtract ${b}$ from both sides: $x - ({b}) = {a}y$.",
                f"Divide by ${a}$: $y = \\dfrac{{x - ({b})}}{{{a}}} = {inverse_latex}$.",
                f"So $f^{{-1}}(x) = {inverse_latex}$.",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-algebraic-manipulation"],
        )


@register
class VerifyInverseByComposition(Generator):
    """Given f and g, determine whether they are inverses by checking f(g(x)) = x."""
    generator_id = "verify_inverse_by_composition"
    topic_slug = "inverse_functions"
    display_name = "Verify inverses using composition"

    _COEF_RANGE = {"easy": (2, 8), "medium": (2, 12), "hard": (2, 20)}
    _CONST_RANGE = {"easy": (-8, 8), "medium": (-15, 15), "hard": (-25, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        clo, chi = self._COEF_RANGE[difficulty]
        const_lo, const_hi = self._CONST_RANGE[difficulty]

        a = rng.randint(clo, chi)
        if rng.random() < 0.5:
            a = -a
        b = rng.randint(const_lo, const_hi)

        f_expr = a * x + b

        # Decide yes/no
        are_inverses = rng.choice([True, False])

        if are_inverses:
            # True inverse: g(x) = (x - b)/a, but keep it as a nice form.
            # To keep integers, force a to divide 1 (so a in {-1, 1}) OR
            # express g symbolically as a fraction.
            g_expr = sp.Rational(1, a) * (x - b)
        else:
            # Build a g that is NOT the inverse, by perturbing one coefficient.
            perturb = rng.choice(["coef", "const"])
            if perturb == "coef":
                alt_a = sp.Rational(1, a) + rng.choice([1, -1, 2, -2])
                g_expr = alt_a * (x - b)
            else:
                alt_shift = b + rng.choice([1, -1, 2, -2])
                g_expr = sp.Rational(1, a) * (x - alt_shift)

        # Compute f(g(x)) and simplify
        fg_expr = sp.simplify(f_expr.subs(x, g_expr))
        fg_expanded = sp.expand(fg_expr)

        is_actually_inverse = sp.simplify(fg_expanded - x) == 0

        answer = (
            "Yes, $f$ and $g$ are inverses (because $f(g(x)) = x$)."
            if is_actually_inverse
            else f"No, $f$ and $g$ are NOT inverses (because $f(g(x)) = {sp.latex(fg_expanded)} \\neq x$)."
        )

        f_latex = sp.latex(f_expr)
        g_latex = sp.latex(g_expr)
        fg_latex = sp.latex(fg_expanded)

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, str(g_expr)),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Let $f(x) = {f_latex}$ and $g(x) = {g_latex}$. "
                r"Determine whether $f$ and $g$ are inverses by computing $f(g(x))$."
            ),
            answer_latex=answer,
            hints=[
                r"Two functions $f$ and $g$ are inverses if $f(g(x)) = x$ for all $x$ in the domain (and $g(f(x)) = x$).",
                f"Substitute $g(x) = {g_latex}$ into $f$ wherever you see $x$.",
                "Expand and simplify. If the result is $x$, they are inverses.",
            ],
            solution_steps_latex=[
                f"Compute $f(g(x))$ by replacing $x$ in $f$ with $g(x) = {g_latex}$: "
                f"$f(g(x)) = {a}({g_latex}) + ({b})$.",
                f"Simplify: $f(g(x)) = {fg_latex}$.",
                f"Compare to $x$. {answer}",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-multi-step"],
        )


@register
class HorizontalLineTestClassify(Generator):
    """Given a verbal description of a function, classify it as one-to-one or not."""
    generator_id = "horizontal_line_test_classify"
    topic_slug = "inverse_functions"
    display_name = "One-to-one classification (horizontal line test)"
    bank_count_per_difficulty = 20  # fixed template pool

    # (description, is_one_to_one, reason)
    _ITEMS = [
        (
            "$f(x) = 3x + 5$ on all real numbers",
            True,
            "A non-constant linear function is strictly monotonic, so it passes the horizontal line test.",
        ),
        (
            "$f(x) = x^2$ on all real numbers",
            False,
            "$x^2$ gives the same output for $x$ and $-x$ (for example $f(2) = f(-2) = 4$), so a horizontal line above the vertex crosses twice.",
        ),
        (
            r"$f(x) = x^2$ restricted to $x \geq 0$",
            True,
            "Restricting to $x \\geq 0$ makes the parabola strictly increasing, so it passes the horizontal line test.",
        ),
        (
            r"$f(x) = x^2$ restricted to $x \leq 0$",
            True,
            "Restricting to $x \\leq 0$ makes the parabola strictly decreasing, so it passes the horizontal line test.",
        ),
        (
            "$f(x) = x^3$ on all real numbers",
            True,
            "A cube function is strictly increasing on all real numbers, so every horizontal line crosses exactly once.",
        ),
        (
            "$f(x) = |x|$ on all real numbers",
            False,
            "Absolute value is symmetric about the y-axis, so any horizontal line above $0$ crosses the graph twice.",
        ),
        (
            r"$f(x) = \sqrt{x}$ on its natural domain",
            True,
            "Square-root is strictly increasing on its domain, so no horizontal line crosses it twice.",
        ),
        (
            "a constant function $f(x) = 7$",
            False,
            "Every input gives the same output, so the horizontal line $y = 7$ crosses the graph infinitely many times.",
        ),
        (
            "$f(x) = 2^x$",
            True,
            "Exponential functions with base $> 1$ are strictly increasing, so no horizontal line crosses the graph twice.",
        ),
        (
            r"$f(x) = \sin(x)$ on all real numbers",
            False,
            "Sine is periodic, so horizontal lines like $y = 0$ cross the graph infinitely many times.",
        ),
        (
            r"$f(x) = \sin(x)$ restricted to $[-\pi/2, \pi/2]$",
            True,
            "On $[-\\pi/2, \\pi/2]$ sine is strictly increasing, so it passes the horizontal line test.",
        ),
        (
            "$f(x) = 1/x$ on all nonzero reals",
            True,
            "$1/x$ is strictly decreasing on $(-\\infty, 0)$ and on $(0, \\infty)$, and never takes the same value twice overall.",
        ),
        (
            r"$f(x) = (x - 3)^2$ on all reals",
            False,
            "A parabola is symmetric about its axis ($x = 3$), so horizontal lines above the vertex cross the graph twice.",
        ),
        (
            r"$f(x) = (x - 3)^2$ restricted to $x \geq 3$",
            True,
            "On $x \\geq 3$ the parabola is strictly increasing, so it passes the horizontal line test.",
        ),
        (
            "$f(x) = -2x + 9$ on all reals",
            True,
            "A non-constant linear function is strictly monotonic; this one is strictly decreasing.",
        ),
        (
            r"$f(x) = x^2 - 4$ on all reals",
            False,
            "Shifted parabola: $f(2) = f(-2) = 0$, so a horizontal line at $y = 0$ crosses twice.",
        ),
        (
            "$f(x) = x^5$ on all reals",
            True,
            "$x^5$ is strictly increasing on all reals, so it passes the horizontal line test.",
        ),
        (
            "$f(x) = x^4$ on all reals",
            False,
            "Like $x^2$, $x^4$ is symmetric about the y-axis ($f(1) = f(-1) = 1$), so it fails the horizontal line test.",
        ),
        (
            r"$f(x) = \ln(x)$ on its natural domain",
            True,
            "Natural log is strictly increasing on $(0, \\infty)$, so it passes the horizontal line test.",
        ),
        (
            "the floor function $f(x) = \\lfloor x \\rfloor$",
            False,
            "The floor function is constant on each interval $[n, n+1)$, so horizontal lines like $y = 1$ cross the graph along an entire segment.",
        ),
        (
            r"$f(x) = \sqrt{x - 2}$ on $x \geq 2$",
            True,
            "A shifted square-root is strictly increasing, so it passes the horizontal line test.",
        ),
        (
            "$f(x) = 3$ on all reals",
            False,
            "A constant function gives the same output to every input, so every horizontal line at that value crosses the graph infinitely often.",
        ),
    ]

    _DIFFICULTY_POOLS = {
        "easy": (0, 10),
        "medium": (3, 16),
        "hard": (7, 21),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._DIFFICULTY_POOLS[difficulty]
        idx = rng.randint(lo, min(hi, len(self._ITEMS) - 1))
        description, is_one_to_one, reason = self._ITEMS[idx]

        if is_one_to_one:
            answer = "Yes, this function IS one-to-one, so it has an inverse."
        else:
            answer = "No, this function is NOT one-to-one, so it does not have an inverse on the given domain."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (idx,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Consider {description}. Is this function one-to-one? "
                r"(Equivalently: does it pass the horizontal line test, so that an inverse function exists?)"
            ),
            answer_latex=answer,
            hints=[
                "A function is one-to-one if no two different inputs give the same output.",
                "Equivalently, every horizontal line crosses the graph at most once (the horizontal line test).",
                "If the function is strictly increasing OR strictly decreasing on its whole domain, it is one-to-one.",
            ],
            solution_steps_latex=[
                f"Picture (or analyze) the function: {description}.",
                f"{reason}",
                f"Conclusion: {answer}",
            ],
            tags=["#branch-algebra-2", "#topic-functions", "#skill-visualization"],
        )
