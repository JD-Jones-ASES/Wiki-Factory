"""Statistical display generators (Wave D algebra gap topics).

Canonical topic slug ``histograms_and_box_plots``.

- box_plot_five_number_summary: compute min, Q1, median, Q3, max.
- box_plot_iqr_and_outliers: compute IQR and check a candidate value.
- histogram_read_frequency: total count in a described histogram range.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


def _median_of(sorted_list: list[int]) -> float:
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_list[mid])
    return (sorted_list[mid - 1] + sorted_list[mid]) / 2


def _q1_q3(sorted_list: list[int]) -> tuple[float, float]:
    """Inclusive halves method: for odd n, median is excluded from both halves."""
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        lower = sorted_list[:mid]
        upper = sorted_list[mid + 1:]
    else:
        lower = sorted_list[:mid]
        upper = sorted_list[mid:]
    return _median_of(lower), _median_of(upper)


def _fmt_num(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return f"{value:.1f}"


# ---------------------------------------------------------------------------


_BOX_PLOT_CONTEXTS: tuple[dict, ...] = (
    {
        "scenario": "Maya records the number of pages she reads each day for a week",
        "unit": "pages",
    },
    {
        "scenario": "Kai tracks the number of minutes he spends stretching each evening",
        "unit": "minutes",
    },
    {
        "scenario": "Priya logs the number of customers her craft booth served each day at a fair",
        "unit": "customers",
    },
    {
        "scenario": "Rohan counts the number of laps he swims during each practice",
        "unit": "laps",
    },
    {
        "scenario": "Zoe records the number of photos she takes each weekend afternoon",
        "unit": "photos",
    },
    {
        "scenario": "Mateo keeps track of how many songs he hears on his morning walk each day",
        "unit": "songs",
    },
    {
        "scenario": "Leilani logs the number of shells she collects on each beach walk",
        "unit": "shells",
    },
    {
        "scenario": "Emilia counts the number of puzzles her cousin finishes each weekend",
        "unit": "puzzles",
    },
)


@register
class BoxPlotFiveNumberSummary(Generator):
    """Compute the five-number summary of a small invented dataset.

    Backward construction: pick clean five-number summary targets, then
    build a small dataset whose sorted values match them exactly.
    """
    generator_id = "box_plot_five_number_summary"
    topic_slug = "histograms_and_box_plots"
    display_name = "Five-number summary of a small dataset"

    _SIZES = (7, 9, 11)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_BOX_PLOT_CONTEXTS)
        n = rng.choice(self._SIZES)

        # Build a strictly increasing dataset: min, ..., max.
        base = rng.randint(2, 10)
        # Use small increments so values stay readable; ensure uniqueness.
        values: list[int] = [base]
        for _ in range(n - 1):
            values.append(values[-1] + rng.randint(1, 4))

        # Shuffle display order to force the student to sort.
        display = values[:]
        rng.shuffle(display)

        sorted_vals = sorted(values)
        minimum = sorted_vals[0]
        maximum = sorted_vals[-1]
        median = _median_of(sorted_vals)
        q1, q3 = _q1_q3(sorted_vals)

        data_latex = ", ".join(str(v) for v in display)

        answer = (
            f"Min = ${minimum}$, Q1 = ${_fmt_num(q1)}$, "
            f"Median = ${_fmt_num(median)}$, Q3 = ${_fmt_num(q3)}$, "
            f"Max = ${maximum}$"
        )

        key = (ctx["scenario"][:12], n, tuple(display))

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{ctx['scenario']}, producing these values (in {ctx['unit']}): "
                f"${data_latex}$. Find the five-number summary."
            ),
            answer_latex=answer,
            hints=[
                (
                    "The five-number summary is min, Q1, median, Q3, max. "
                    "Sort the data first, then split it around the median "
                    "to locate Q1 and Q3."
                ),
                (
                    "Q1 is the median of the lower half; Q3 is the median "
                    "of the upper half. For an odd-sized list, exclude the "
                    "middle value from both halves."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Sort the data in increasing order: "
                    f"${', '.join(str(v) for v in sorted_vals)}$."
                ),
                f"The minimum is the first value: ${minimum}$.",
                f"The maximum is the last value: ${maximum}$.",
                f"Find the median of the sorted list: ${_fmt_num(median)}$.",
                (
                    f"The lower half's median is Q1 = ${_fmt_num(q1)}$; "
                    f"the upper half's median is Q3 = ${_fmt_num(q3)}$."
                ),
                answer,
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-statistics",
                "#skill-procedural-calculation",
            ],
        )


# ---------------------------------------------------------------------------


@register
class BoxPlotIqrAndOutliers(Generator):
    """Compute IQR and check whether a test value is an outlier via 1.5*IQR.

    Backward construction: pick Q1 and Q3, compute IQR and the fences,
    then choose a test value that sits clearly inside or outside.
    """
    generator_id = "box_plot_iqr_and_outliers"
    topic_slug = "histograms_and_box_plots"
    display_name = "IQR and the 1.5 x IQR outlier rule"

    _Q1_RANGE = {"easy": (5, 15), "medium": (5, 25), "hard": (5, 40)}
    _IQR_RANGE = {"easy": (4, 10), "medium": (4, 16), "hard": (4, 25)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_BOX_PLOT_CONTEXTS)

        q1_lo, q1_hi = self._Q1_RANGE[difficulty]
        iqr_lo, iqr_hi = self._IQR_RANGE[difficulty]

        # Constrain IQR to even integers so 1.5*IQR stays clean.
        iqr = rng.randint(iqr_lo // 2, iqr_hi // 2) * 2
        if iqr < 4:
            iqr = 4
        q1 = rng.randint(q1_lo, q1_hi)
        q3 = q1 + iqr

        fence_step = 1.5 * iqr  # can be a half-integer if iqr is odd, but we forced even
        lower_fence = q1 - fence_step
        upper_fence = q3 + fence_step

        # Pick a test value. Half the time outside, half inside.
        if rng.random() < 0.5:
            # Inside (between fences, typically near median)
            test_value = rng.randint(
                max(int(lower_fence) + 1, q1 - 2),
                min(int(upper_fence) - 1, q3 + 2),
            )
            is_outlier = False
        else:
            # Outside (clearly above upper fence)
            if rng.random() < 0.5:
                test_value = int(upper_fence) + rng.randint(2, 8)
                is_outlier = test_value > upper_fence
            else:
                test_value = int(lower_fence) - rng.randint(2, 8)
                is_outlier = test_value < lower_fence

        # Final check with actual floats
        is_outlier = (test_value < lower_fence) or (test_value > upper_fence)

        verdict = (
            f"IQR = ${iqr}$. The value ${test_value}$ "
            + ("is an outlier." if is_outlier else "is not an outlier.")
        )

        statement = (
            f"{ctx['scenario']}. The first quartile is $Q_1 = {q1}$ "
            f"{ctx['unit']} and the third quartile is $Q_3 = {q3}$ "
            f"{ctx['unit']}. "
            f"Compute the interquartile range (IQR) and decide whether the "
            f"value ${test_value}$ {ctx['unit']} is an outlier using the "
            f"$1.5 \\times \\text{{IQR}}$ rule."
        )

        key = (ctx["scenario"][:12], q1, q3, test_value)

        # Human-readable fence numbers
        lower_fence_str = _fmt_num(lower_fence)
        upper_fence_str = _fmt_num(upper_fence)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=verdict,
            hints=[
                (
                    r"The interquartile range is $\text{IQR} = Q_3 - Q_1$. "
                    r"A value is an outlier if it is below "
                    r"$Q_1 - 1.5 \cdot \text{IQR}$ or above "
                    r"$Q_3 + 1.5 \cdot \text{IQR}$."
                ),
                (
                    f"Compute the lower fence $Q_1 - 1.5 \\cdot {iqr}$ and "
                    f"the upper fence $Q_3 + 1.5 \\cdot {iqr}$."
                ),
            ],
            solution_steps_latex=[
                f"Compute IQR: $Q_3 - Q_1 = {q3} - {q1} = {iqr}$.",
                (
                    f"Compute $1.5 \\cdot \\text{{IQR}} = 1.5 \\cdot {iqr} = "
                    f"{_fmt_num(fence_step)}$."
                ),
                (
                    f"Lower fence: $Q_1 - 1.5 \\cdot \\text{{IQR}} = "
                    f"{q1} - {_fmt_num(fence_step)} = {lower_fence_str}$."
                ),
                (
                    f"Upper fence: $Q_3 + 1.5 \\cdot \\text{{IQR}} = "
                    f"{q3} + {_fmt_num(fence_step)} = {upper_fence_str}$."
                ),
                (
                    f"Check ${test_value}$ against the fences: "
                    + (
                        f"it is outside $[{lower_fence_str}, "
                        f"{upper_fence_str}]$, so it is an outlier."
                        if is_outlier
                        else f"it lies inside $[{lower_fence_str}, "
                        f"{upper_fence_str}]$, so it is not an outlier."
                    )
                ),
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-statistics",
                "#skill-multi-step",
            ],
        )


# ---------------------------------------------------------------------------


_HISTOGRAM_CONTEXTS: tuple[dict, ...] = (
    {
        "scenario": "Maya records the ages of the people at a community art class",
        "x_label": "age",
        "unit": "years",
    },
    {
        "scenario": "Kai counts the number of minutes each runner took to finish a 5K",
        "x_label": "finish time",
        "unit": "minutes",
    },
    {
        "scenario": "Priya tracks the prices of used bicycles in an online marketplace",
        "x_label": "price",
        "unit": "dollars",
    },
    {
        "scenario": "Rohan gathers the weekly step counts of members of a hiking group",
        "x_label": "steps per week",
        "unit": "thousand steps",
    },
    {
        "scenario": "Zoe surveys how many books each student in her grade read over a summer",
        "x_label": "books read",
        "unit": "books",
    },
    {
        "scenario": "Mateo measures the height of saplings in a greenhouse",
        "x_label": "height",
        "unit": "centimeters",
    },
    {
        "scenario": "Leilani records the temperature at noon on 40 random days",
        "x_label": "temperature",
        "unit": "degrees",
    },
    {
        "scenario": "Emilia records the scores on a 100-point trivia quiz",
        "x_label": "score",
        "unit": "points",
    },
)


@register
class HistogramReadFrequency(Generator):
    """Compute the total count in a specified range of a described histogram."""
    generator_id = "histogram_read_frequency"
    topic_slug = "histograms_and_box_plots"
    display_name = "Read total frequency from a histogram range"

    _NUM_BARS = (4, 5)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_HISTOGRAM_CONTEXTS)
        num_bars = rng.choice(self._NUM_BARS)

        # Build bin edges starting at a small positive integer.
        start = rng.randint(0, 10) * 5
        bin_width = rng.choice([5, 10])
        edges = [start + i * bin_width for i in range(num_bars + 1)]

        # Build heights (counts). Bigger on medium/hard.
        if rng.random() < 0.5:
            heights = [rng.randint(2, 12) for _ in range(num_bars)]
        else:
            heights = [rng.randint(5, 20) for _ in range(num_bars)]

        # Describe each bar in prose
        bar_descriptions = ", ".join(
            f"{edges[i]}\u2013{edges[i+1]} {ctx['unit']} has {heights[i]}"
            for i in range(num_bars)
        )

        # Choose a contiguous range of bars to sum (at least 2, at most all).
        start_idx = rng.randint(0, num_bars - 2)
        end_idx = rng.randint(start_idx + 1, num_bars - 1)
        range_total = sum(heights[start_idx:end_idx + 1])

        range_lo = edges[start_idx]
        range_hi = edges[end_idx + 1]

        statement = (
            f"{ctx['scenario']} and groups the data into a histogram with "
            f"{num_bars} bars. The bars represent the {ctx['x_label']} "
            f"ranges (in {ctx['unit']}) and their heights (frequencies) "
            f"are: {bar_descriptions}. How many data values fall in the "
            f"overall range from {range_lo} to {range_hi} {ctx['unit']}?"
        )

        answer = f"${range_total}$ values"

        key = (
            ctx["scenario"][:12],
            tuple(edges),
            tuple(heights),
            start_idx,
            end_idx,
        )

        bar_list_steps = [
            f"Bar {i+1}: {edges[i]}\u2013{edges[i+1]} has height ${heights[i]}$."
            for i in range(num_bars)
        ]
        summed_bars = " + ".join(
            str(heights[i]) for i in range(start_idx, end_idx + 1)
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "Each bar's height is the count of data values in that "
                    "bin. To count values over a range of bins, add the "
                    "heights of the bins inside that range."
                ),
                (
                    f"Add the heights of the bars covering "
                    f"{range_lo}\u2013{range_hi} {ctx['unit']}."
                ),
            ],
            solution_steps_latex=[
                "List the height of each bar:",
                *bar_list_steps,
                (
                    f"Identify the bars whose ranges lie inside "
                    f"{range_lo}\u2013{range_hi}: bars "
                    f"{start_idx + 1} through {end_idx + 1}."
                ),
                (
                    f"Sum their heights: ${summed_bars} = {range_total}$."
                ),
                f"The total count is ${range_total}$.",
            ],
            tags=[
                "#branch-algebra-1",
                "#topic-statistics",
                "#skill-visualization",
            ],
        )
