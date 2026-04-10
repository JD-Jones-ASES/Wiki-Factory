"""Coordinate plane and scatter-plot generators (Phase 2c, linear cluster extensions).

Covers two canonical topic slugs under algebra:

- ``plotting_points_and_the_coordinate_plane`` --- quadrant/axis identification,
  directional movement from the origin, and distance between two points that
  share a coordinate. These are prerequisites for the general distance formula.
- ``scatter_plots_and_trend_lines`` --- trend-direction classification,
  prediction from a trend line, and slope interpretation in context.

All word-problem phrasing is paraphrased from scratch.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register
from ..latex_helpers import format_point


# ---------------------------------------------------------------------------
# Topic 1: plotting_points_and_the_coordinate_plane
# ---------------------------------------------------------------------------


@register
class PointIdentifyQuadrant(Generator):
    """Identify the quadrant or axis of a given point.

    Backward construction by category: first pick the category (I-IV,
    x-axis, y-axis, or origin) to ensure the bank hits every case, then
    sample signs/values accordingly.
    """
    generator_id = "point_identify_quadrant"
    topic_slug = "plotting_points_and_the_coordinate_plane"
    display_name = "Identify the quadrant or axis of a point"
    bank_count_per_difficulty = 40  # 7 categories, constrained parameter space

    _RANGE = {"easy": (1, 10), "medium": (1, 20), "hard": (1, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        # Weighted category selection: the four quadrants should dominate,
        # with the axes and origin sprinkled in.
        category = rng.choices(
            population=[
                "Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV",
                "x-axis", "y-axis", "origin",
            ],
            weights=[3, 3, 3, 3, 2, 2, 1],
            k=1,
        )[0]

        if category == "Quadrant I":
            x = rng.randint(lo, hi)
            y = rng.randint(lo, hi)
        elif category == "Quadrant II":
            x = -rng.randint(lo, hi)
            y = rng.randint(lo, hi)
        elif category == "Quadrant III":
            x = -rng.randint(lo, hi)
            y = -rng.randint(lo, hi)
        elif category == "Quadrant IV":
            x = rng.randint(lo, hi)
            y = -rng.randint(lo, hi)
        elif category == "x-axis":
            # y = 0, x != 0 (not origin)
            x_raw = rng.randint(lo, hi)
            x = x_raw if rng.random() >= 0.5 else -x_raw
            y = 0
        elif category == "y-axis":
            # x = 0, y != 0 (not origin)
            y_raw = rng.randint(lo, hi)
            y = y_raw if rng.random() >= 0.5 else -y_raw
            x = 0
        else:  # origin
            x, y = 0, 0

        point_latex = format_point(x, y)

        # Reasoning description for the solution steps.
        if category.startswith("Quadrant"):
            sign_x = "positive" if x > 0 else "negative"
            sign_y = "positive" if y > 0 else "negative"
            reason = (
                f"Both coordinates are nonzero, and $x$ is {sign_x} while "
                f"$y$ is {sign_y}."
            )
            rule_line = (
                "Quadrant I: $(+, +)$. Quadrant II: $(-, +)$. "
                "Quadrant III: $(-, -)$. Quadrant IV: $(+, -)$."
            )
        elif category == "x-axis":
            reason = f"The $y$-coordinate is ${y}$, so the point lies on the $x$-axis."
            rule_line = (
                "A point is on the $x$-axis when its $y$-coordinate is $0$."
            )
        elif category == "y-axis":
            reason = f"The $x$-coordinate is ${x}$, so the point lies on the $y$-axis."
            rule_line = (
                "A point is on the $y$-axis when its $x$-coordinate is $0$."
            )
        else:
            reason = "Both coordinates are $0$, so the point is the origin."
            rule_line = (
                "The origin is the point $(0, 0)$, the intersection of both axes."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (x, y),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In which quadrant or on which axis does the point "
                f"${point_latex}$ lie?"
            ),
            answer_latex=category,
            hints=[
                (
                    "Check the signs of the coordinates. If either coordinate "
                    "is zero, the point lies on an axis (or at the origin)."
                ),
                rule_line,
                reason,
            ],
            solution_steps_latex=[
                f"Look at the point ${point_latex}$.",
                reason,
                f"The point lies in/on: {category}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-visualization",
            ],
        )


@register
class PointDescribeFromInstructions(Generator):
    """Translate a 'move X right, move Y up' instruction into a coordinate."""
    generator_id = "point_describe_from_instructions"
    topic_slug = "plotting_points_and_the_coordinate_plane"
    display_name = "Find a point from a movement instruction"

    _RANGE = {"easy": (1, 10), "medium": (1, 20), "hard": (1, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        dx = rng.randint(lo, hi)
        dy = rng.randint(lo, hi)
        horizontal = rng.choice(["right", "left"])
        vertical = rng.choice(["up", "down"])

        x = dx if horizontal == "right" else -dx
        y = dy if vertical == "up" else -dy

        unit_word_h = "unit" if dx == 1 else "units"
        unit_word_v = "unit" if dy == 1 else "units"

        # Randomly pick whether horizontal or vertical comes first in the
        # problem text for variety.
        if rng.random() >= 0.5:
            instruction = (
                f"Starting at the origin, move ${dx}$ {unit_word_h} "
                f"{horizontal} and then ${dy}$ {unit_word_v} {vertical}."
            )
        else:
            instruction = (
                f"Starting at the origin, move ${dy}$ {unit_word_v} "
                f"{vertical} and then ${dx}$ {unit_word_h} {horizontal}."
            )

        point_latex = format_point(x, y)

        x_sign = "positive" if horizontal == "right" else "negative"
        y_sign = "positive" if vertical == "up" else "negative"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (dx, dy, horizontal, vertical),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"{instruction} What point do you land on?",
            answer_latex=f"${point_latex}$",
            hints=[
                (
                    "Horizontal movement changes the $x$-coordinate: right is "
                    "positive, left is negative. Vertical movement changes "
                    "the $y$-coordinate: up is positive, down is negative."
                ),
                (
                    f"Moving {horizontal} ${dx}$ means $x = {x}$ ({x_sign}). "
                    f"Moving {vertical} ${dy}$ means $y = {y}$ ({y_sign})."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Start at the origin $(0, 0)$."
                ),
                (
                    f"Horizontal step: move ${dx}$ {unit_word_h} {horizontal}, "
                    f"so $x = {x}$."
                ),
                (
                    f"Vertical step: move ${dy}$ {unit_word_v} {vertical}, "
                    f"so $y = {y}$."
                ),
                f"The final point is ${point_latex}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-visualization",
            ],
        )


@register
class PointDistanceBetweenOnSameAxis(Generator):
    """Distance between two points that share an $x$- or $y$-coordinate.

    This is a precursor to the general distance formula: on a line parallel
    to an axis, the distance is the absolute difference of the differing
    coordinate. Backward construction picks the shared coordinate and two
    distinct values on the other axis.
    """
    generator_id = "point_distance_between_on_same_axis"
    topic_slug = "plotting_points_and_the_coordinate_plane"
    display_name = "Distance between two points on the same axis"

    _RANGE = {"easy": (-10, 10), "medium": (-20, 20), "hard": (-40, 40)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGE[difficulty]
        orientation = rng.choice(["horizontal", "vertical"])
        shared = rng.randint(lo, hi)
        # Pick two distinct values for the varying coordinate.
        v1 = rng.randint(lo, hi)
        v2 = rng.randint(lo, hi)
        while v2 == v1:
            v2 = rng.randint(lo, hi)

        if orientation == "horizontal":
            # Same y: varying x-coordinate.
            p1 = (v1, shared)
            p2 = (v2, shared)
            changing = "x"
            fixed = "y"
            distance = abs(v2 - v1)
            fixed_val = shared
        else:
            # Same x: varying y-coordinate.
            p1 = (shared, v1)
            p2 = (shared, v2)
            changing = "y"
            fixed = "x"
            distance = abs(v2 - v1)
            fixed_val = shared

        p1_latex = format_point(*p1)
        p2_latex = format_point(*p2)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                (orientation, shared, v1, v2),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Find the distance between the points ${p1_latex}$ and "
                f"${p2_latex}$."
            ),
            answer_latex=f"${distance}$",
            hints=[
                (
                    f"Notice that both points share the same ${fixed}$-coordinate "
                    f"(${fixed_val}$), so they lie on a {orientation} line."
                ),
                (
                    f"When two points share one coordinate, the distance is "
                    f"the absolute difference of the other: "
                    f"$|{v2} - {v1}|$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Both points have ${fixed} = {fixed_val}$, so the segment "
                    f"is {orientation}."
                ),
                (
                    f"Compute the difference of the ${changing}$-coordinates: "
                    f"${v2} - {v1} = {v2 - v1}$."
                ),
                (
                    f"Take the absolute value to get the distance: "
                    f"$|{v2 - v1}| = {distance}$."
                ),
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-procedural-calculation",
            ],
        )


# ---------------------------------------------------------------------------
# Topic 2: scatter_plots_and_trend_lines
# ---------------------------------------------------------------------------


_TREND_TEMPLATES_POSITIVE: tuple[str, ...] = (
    "As the $x$-values increase, the $y$-values also tend to increase.",
    "The data points on the scatter plot generally rise from left to right.",
    "When one variable grows, the other variable tends to grow with it.",
    "The dots form a pattern that climbs upward as you read from left to right.",
)

_TREND_TEMPLATES_NEGATIVE: tuple[str, ...] = (
    "As the $x$-values increase, the $y$-values tend to decrease.",
    "The data points on the scatter plot generally fall from left to right.",
    "When one variable grows, the other variable tends to shrink.",
    "The dots form a pattern that drops downward as you read from left to right.",
)

_TREND_TEMPLATES_NONE: tuple[str, ...] = (
    "The data points on the scatter plot are scattered with no clear pattern.",
    "The values of $y$ seem unrelated to the values of $x$.",
    "The dots are spread out with no obvious trend in either direction.",
    "There is no clear rise or fall as you read the scatter plot from left to right.",
)


@register
class ScatterClassifyTrendDirection(Generator):
    """Classify a scatter plot's trend as positive, negative, or none.

    The problem is presented in one of two forms (picked randomly):
      1. Textual description of the trend.
      2. A small table of (x, y) data points for the student to eyeball.
    """
    generator_id = "scatter_classify_trend_direction"
    topic_slug = "scatter_plots_and_trend_lines"
    display_name = "Classify a scatter plot's trend direction"
    bank_count_per_difficulty = 30

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        form = rng.choice(["description", "table"])
        trend = rng.choice(["positive", "negative", "none"])

        if form == "description":
            if trend == "positive":
                description = rng.choice(_TREND_TEMPLATES_POSITIVE)
                template_idx = _TREND_TEMPLATES_POSITIVE.index(description)
            elif trend == "negative":
                description = rng.choice(_TREND_TEMPLATES_NEGATIVE)
                template_idx = _TREND_TEMPLATES_NEGATIVE.index(description)
            else:
                description = rng.choice(_TREND_TEMPLATES_NONE)
                template_idx = _TREND_TEMPLATES_NONE.index(description)

            statement_latex = (
                f"A scatter plot has this property: {description} "
                "Classify the trend as positive, negative, or none."
            )
            key = ("desc", trend, template_idx)
            reasoning = f'The description says: "{description}"'

        else:
            # Generate 4 data points consistent with the trend.
            n_points = 4
            xs = sorted(rng.sample(range(1, 20), n_points))
            if trend == "positive":
                # y roughly increases with x
                base = rng.randint(1, 6)
                step = rng.randint(1, 4)
                noise = [rng.randint(-1, 1) for _ in range(n_points)]
                ys = [base + step * i + noise[i] for i in range(n_points)]
            elif trend == "negative":
                base = rng.randint(15, 25)
                step = rng.randint(1, 4)
                noise = [rng.randint(-1, 1) for _ in range(n_points)]
                ys = [base - step * i + noise[i] for i in range(n_points)]
            else:
                ys = [rng.randint(1, 20) for _ in range(n_points)]
                # Nudge away from accidental monotonicity.
                if ys[0] < ys[-1] and ys[0] < ys[1] < ys[2]:
                    ys[2] = ys[0]
                if ys[0] > ys[-1] and ys[0] > ys[1] > ys[2]:
                    ys[2] = ys[0] + 5

            pairs_latex = ", ".join(
                f"({x}, {y})" for x, y in zip(xs, ys)
            )
            statement_latex = (
                "Examine this small set of data points from a scatter plot: "
                f"${pairs_latex}$. "
                "Classify the overall trend as positive, negative, or none."
            )
            key = ("table", trend, tuple(xs), tuple(ys))
            if trend == "positive":
                reasoning = (
                    f"Reading the $y$-values in order, they rise (roughly) as "
                    f"$x$ increases: ${ys}$. This is a positive trend."
                )
            elif trend == "negative":
                reasoning = (
                    f"Reading the $y$-values in order, they fall (roughly) as "
                    f"$x$ increases: ${ys}$. This is a negative trend."
                )
            else:
                reasoning = (
                    f"The $y$-values $y = {ys}$ do not rise or fall "
                    f"consistently as $x$ increases, so there is no clear trend."
                )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement_latex,
            answer_latex=trend,
            hints=[
                (
                    "A positive trend means $y$ tends to rise as $x$ rises. "
                    "A negative trend means $y$ tends to fall as $x$ rises. "
                    "If the pattern is scattered, the trend is none."
                ),
                (
                    "Look at the overall direction of the dots (or the "
                    "$y$-values in the table) as $x$ increases."
                ),
            ],
            solution_steps_latex=[
                "Scan the data for an overall up/down pattern.",
                reasoning,
                f"The trend is {trend}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-visualization",
            ],
        )


_SCATTER_CONTEXTS: tuple[tuple[str, str, str], ...] = (
    # (x-label, y-label, units)
    ("study hours", "test scores", "points"),
    ("hours of practice", "free throws made", "free throws"),
    ("minutes exercised", "calories burned", "calories"),
    ("rainfall (in inches)", "plant growth (in cm)", "cm"),
    ("gallons of fuel", "miles driven", "miles"),
    ("pages read", "new words learned", "words"),
    ("ounces of lemonade made", "ounces of sugar needed", "ounces"),
    ("minutes on the phone", "battery percent remaining", "percent"),
)


@register
class ScatterPredictFromTrendLine(Generator):
    """Predict a $y$-value from a trend line $y = mx + b$ at a given $x$.

    Backward construction: pick clean integers ``m``, ``b``, ``x``, so that
    ``y`` is a clean integer. Wrap the problem in a scatter-plot context.
    """
    generator_id = "scatter_predict_from_trend_line"
    topic_slug = "scatter_plots_and_trend_lines"
    display_name = "Predict from a trend line"

    _M_RANGE = {"easy": (1, 10), "medium": (1, 15), "hard": (1, 25)}
    _B_RANGE = {"easy": (0, 30), "medium": (0, 60), "hard": (-50, 100)}
    _X_RANGE = {"easy": (1, 10), "medium": (1, 15), "hard": (1, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        x_lo, x_hi = self._X_RANGE[difficulty]

        m = rng.randint(m_lo, m_hi)
        b = rng.randint(b_lo, b_hi)
        x = rng.randint(x_lo, x_hi)
        y = m * x + b  # guaranteed integer

        x_label, y_label, units = rng.choice(_SCATTER_CONTEXTS)

        # Format "y = m x + b" with sign-aware b.
        if b >= 0:
            line_latex = f"y = {m}x + {b}"
            eval_latex = f"y = {m} \\cdot {x} + {b}"
        else:
            line_latex = f"y = {m}x - {abs(b)}"
            eval_latex = f"y = {m} \\cdot {x} - {abs(b)}"

        statement = (
            f"A scatter plot of {x_label} vs. {y_label} is modeled by the "
            f"trend line ${line_latex}$, where $x$ is the {x_label} and $y$ "
            f"is the {y_label}. Use the trend line to predict the {y_label} "
            f"when $x = {x}$."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (m, b, x, x_label),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${y}$ {units}",
            hints=[
                (
                    "A trend line lets you estimate $y$ for any given $x$. "
                    f"Substitute $x = {x}$ into ${line_latex}$ and simplify."
                ),
                f"Compute ${m} \\cdot {x} = {m * x}$.",
                f"Add the $y$-intercept: ${m * x} + ({b}) = {y}$.",
            ],
            solution_steps_latex=[
                f"Start with the trend line ${line_latex}$.",
                f"Substitute $x = {x}$: ${eval_latex}$.",
                f"Compute: $y = {m * x} + ({b}) = {y}$.",
                f"The predicted {y_label} is ${y}$ {units}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-formula-substitution",
            ],
        )


# For slope interpretation, we keep the template space small and use
# ``bank_count_per_difficulty = 20`` as the prompt specifies.
_SLOPE_INTERP_CONTEXTS: tuple[tuple[str, str, str, str], ...] = (
    # (x_label, y_label, unit_y, unit_x)
    ("items purchased", "total cost", "dollars", "item"),
    ("minutes of talk time", "phone bill", "dollars", "minute"),
    ("hours worked", "dollars earned", "dollars", "hour"),
    ("pages printed", "ink used", "milliliters", "page"),
    ("days since planting", "plant height", "centimeters", "day"),
    ("gallons of gas", "miles driven", "miles", "gallon"),
    ("tickets sold", "revenue", "dollars", "ticket"),
    ("months of membership", "total paid", "dollars", "month"),
)


@register
class ScatterSlopeInterpretation(Generator):
    """Explain the real-world meaning of a trend line's slope in context.

    Answer is a short plain-English sentence. The prompt specifies
    ``bank_count_per_difficulty = 20`` because the template space is small.
    """
    generator_id = "scatter_slope_interpretation"
    topic_slug = "scatter_plots_and_trend_lines"
    display_name = "Interpret the slope of a trend line"
    bank_count_per_difficulty = 20

    _M_RANGE = {"easy": (2, 9), "medium": (2, 15), "hard": (2, 25)}
    _B_RANGE = {"easy": (1, 30), "medium": (1, 60), "hard": (1, 100)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        m_lo, m_hi = self._M_RANGE[difficulty]
        b_lo, b_hi = self._B_RANGE[difficulty]
        m_mag = rng.randint(m_lo, m_hi)
        # About half the time, make the slope negative so students see both
        # directions.
        m = m_mag if rng.random() >= 0.5 else -m_mag
        b = rng.randint(b_lo, b_hi)

        context_idx = rng.randint(0, len(_SLOPE_INTERP_CONTEXTS) - 1)
        x_label, y_label, unit_y, unit_x = _SLOPE_INTERP_CONTEXTS[context_idx]

        if b >= 0:
            line_latex = f"y = {m}x + {b}"
        else:
            line_latex = f"y = {m}x - {abs(b)}"

        direction_word = "increases" if m > 0 else "decreases"
        change_phrase = (
            f"{y_label} {direction_word} by about ${abs(m)}$ {unit_y} for "
            f"each additional {unit_x}"
        )

        interpretation = (
            f"For every additional {unit_x}, the {y_label} {direction_word} "
            f"by about ${abs(m)}$ {unit_y}."
        )

        statement = (
            f"A scatter plot of {x_label} vs. {y_label} is modeled by the "
            f"trend line ${line_latex}$, where $x$ is the number of "
            f"{x_label} and $y$ is the {y_label} in {unit_y}. "
            "In one sentence, interpret the meaning of the slope in context."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (m, b, context_idx),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=interpretation,
            hints=[
                (
                    "In a linear model $y = mx + b$, the slope $m$ is the "
                    "rate of change: how much $y$ changes each time $x$ "
                    "increases by $1$."
                ),
                (
                    f"Here $m = {m}$, so a one-{unit_x} increase in $x$ "
                    f"changes $y$ by ${m}$ {unit_y}. A {'positive' if m > 0 else 'negative'} "
                    f"slope means $y$ {direction_word}."
                ),
            ],
            solution_steps_latex=[
                f"Identify the slope in ${line_latex}$: $m = {m}$.",
                (
                    f"Attach the context's units: for each additional "
                    f"{unit_x}, the {y_label} changes by ${m}$ {unit_y}."
                ),
                f"State the interpretation: {change_phrase}.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-linear",
                "#skill-interpretation",
            ],
        )
