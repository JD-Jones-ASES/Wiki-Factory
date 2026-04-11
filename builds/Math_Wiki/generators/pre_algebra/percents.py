"""Percent generators.

Phase 2c Wave 1 originally housed the three generators for
``finding_a_percent_of_a_number`` at
wiki/topics/pre_algebra/Finding_A_Percent_Of_A_Number.md (Math I Ch 7.3).

- percent_of_number: Find p% of n.
- percent_one_is_of_other: x is what percent of y?
- percent_find_whole: x is p% of what?

A later wave added conversion and percent-equation generators for three
sibling topics:

- ``fractions_decimals_and_percents`` --- convert fraction/decimal/percent
  * convert_fraction_to_decimal
  * convert_decimal_to_percent
  * convert_percent_to_fraction

- ``understanding_percents`` --- interpret percents as parts per hundred
  * percent_of_whole_single_digit
  * percent_identify_from_shaded_description
  * percent_estimate_simple

- ``the_percent_equation`` --- the part = rate x whole formula
  * percent_eq_find_part
  * percent_eq_find_percent
  * percent_eq_find_whole

All generators keep answers clean (integer or single-decimal) by
constructing problems backward from a known result.
"""
from __future__ import annotations

import math as _math
import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


_EASY_PERCENTS = (5, 10, 20, 25, 50, 75)
_MEDIUM_PERCENTS = (5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80, 90)
_HARD_PERCENTS = (2, 3, 5, 8, 12, 15, 18, 22, 28, 35, 42, 55, 65, 85, 95)


def _percents_for(difficulty: Difficulty) -> tuple[int, ...]:
    return {"easy": _EASY_PERCENTS, "medium": _MEDIUM_PERCENTS, "hard": _HARD_PERCENTS}[difficulty]


# ---------------------------------------------------------------------------

@register
class PercentOfNumber(Generator):
    """Find p% of n. Clean answers by requiring p * n divisible by 100."""
    generator_id = "percent_of_number"
    topic_slug = "finding_a_percent_of_a_number"
    display_name = "Find p% of a number"

    _N_RANGES = {"easy": (10, 200), "medium": (20, 600), "hard": (50, 1500)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._N_RANGES[difficulty]
        percents = _percents_for(difficulty)
        # Construct n so p*n is divisible by 100 for clean answer
        while True:
            p = rng.choice(percents)
            n = rng.randint(lo, hi)
            # Round n to a multiple of 100 / gcd(p, 100) so answer is clean
            import math as _math

            step = 100 // _math.gcd(p, 100)
            n = (n // step) * step
            if n < lo:
                n = step
            result = p * n // 100
            if result > 0:
                break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (p, n)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Find ${p}\\%$ of ${n}$.",
            answer_latex=f"${result}$",
            hints=[
                f"Convert ${p}\\%$ to a decimal: ${p}\\% = 0.{p:02d}$ (drop the percent sign, divide by $100$).",
                f"Multiply: $0.{p:02d} \\times {n}$.",
                rf"Equivalently: $\dfrac{{{p}}}{{100}} \times {n} = \dfrac{{{p * n}}}{{100}} = {result}$.",
            ],
            solution_steps_latex=[
                rf"Rewrite the percent as a fraction: ${p}\% = \dfrac{{{p}}}{{100}}$.",
                rf"Multiply by ${n}$: $\dfrac{{{p}}}{{100}} \times {n} = \dfrac{{{p * n}}}{{100}}$.",
                f"Simplify: ${result}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-formula-substitution"],
        )


@register
class PercentOneIsOfOther(Generator):
    """x is what percent of y? Construct backward so answer is a clean integer percent."""
    generator_id = "percent_one_is_of_other"
    topic_slug = "finding_a_percent_of_a_number"
    display_name = "x is what percent of y?"

    _Y_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._Y_RANGES[difficulty]
        percents = _percents_for(difficulty)
        import math as _math

        while True:
            p = rng.choice(percents)
            y = rng.randint(lo, hi)
            step = 100 // _math.gcd(p, 100)
            y = (y // step) * step
            if y < lo:
                y = step
            x = p * y // 100
            if x > 0:
                break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, y)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${x}$ is what percent of ${y}$?",
            answer_latex=f"${p}\\%$",
            hints=[
                r"Use the relation $\text{part} = \text{percent} \times \text{whole}$, so $\text{percent} = \dfrac{\text{part}}{\text{whole}}$.",
                rf"$\dfrac{{{x}}}{{{y}}} = {x / y:.4f}$",
                f"Multiply by $100$ and add the $\\%$ symbol: ${p}\\%$.",
            ],
            solution_steps_latex=[
                rf"Set up $\dfrac{{\text{{part}}}}{{\text{{whole}}}} = \dfrac{{{x}}}{{{y}}}$.",
                rf"Simplify the fraction: $\dfrac{{{x}}}{{{y}}} = \dfrac{{{p}}}{{100}}$.",
                f"Convert to a percent: ${p}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )


@register
class PercentFindWhole(Generator):
    """x is p% of what number? Answer = 100*x/p, kept as an integer."""
    generator_id = "percent_find_whole"
    topic_slug = "finding_a_percent_of_a_number"
    display_name = "x is p% of what number?"

    _WHOLE_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._WHOLE_RANGES[difficulty]
        percents = _percents_for(difficulty)
        import math as _math

        while True:
            p = rng.choice(percents)
            whole = rng.randint(lo, hi)
            step = 100 // _math.gcd(p, 100)
            whole = (whole // step) * step
            if whole < lo:
                whole = step
            x = p * whole // 100
            if x > 0:
                break

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (x, p)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${x}$ is ${p}\\%$ of what number?",
            answer_latex=f"${whole}$",
            hints=[
                r"Use $\text{part} = \text{percent} \times \text{whole}$.",
                rf"Rewrite ${p}\%$ as $\dfrac{{{p}}}{{100}}$ and call the whole $w$: ${x} = \dfrac{{{p}}}{{100}} \cdot w$.",
                rf"Solve for $w$: $w = {x} \cdot \dfrac{{100}}{{{p}}} = {whole}$.",
            ],
            solution_steps_latex=[
                rf"Translate: ${x} = \dfrac{{{p}}}{{100}} \cdot w$.",
                rf"Multiply both sides by $\dfrac{{100}}{{{p}}}$: $w = {x} \cdot \dfrac{{100}}{{{p}}} = \dfrac{{{100 * x}}}{{{p}}}$.",
                f"Simplify: $w = {whole}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )


# ===========================================================================
# Conversion helpers: fraction <-> decimal <-> percent
# ===========================================================================


def _format_terminating_decimal(num: int, den: int) -> str:
    """Render a reduced terminating fraction num/den as a decimal string.

    Assumes the fraction terminates (den is 2^a * 5^b after reduction).
    """
    g = _math.gcd(abs(num), den)
    num //= g
    den //= g
    # Factor den into powers of 2 and 5
    twos = 0
    fives = 0
    d = den
    while d % 2 == 0:
        d //= 2
        twos += 1
    while d % 5 == 0:
        d //= 5
        fives += 1
    if d != 1:
        raise ValueError(f"{num}/{den} is not a terminating decimal")
    k = max(twos, fives)
    if k == 0:
        return str(num)
    multiplier = (10 ** k) // den
    scaled = num * multiplier
    sign = ""
    if scaled < 0:
        sign = "-"
        scaled = -scaled
    s = str(scaled).zfill(k + 1)
    return f"{sign}{s[:-k]}.{s[-k:]}"


def _terminating_fractions_up_to(max_den: int) -> list[tuple[int, int]]:
    """All reduced fractions num/den with 1 <= num < den <= max_den that terminate."""
    out: list[tuple[int, int]] = []
    for den in range(2, max_den + 1):
        d = den
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        if d != 1:
            continue
        for num in range(1, den):
            if _math.gcd(num, den) == 1:
                out.append((num, den))
    return out


_FRAC_DEC_TABLES: dict[Difficulty, list[tuple[int, int]]] = {
    "easy": _terminating_fractions_up_to(25),
    "medium": _terminating_fractions_up_to(50),
    "hard": _terminating_fractions_up_to(100),
}


# ---------------------------------------------------------------------------

@register
class ConvertFractionToDecimal(Generator):
    """Convert a reduced fraction $\\tfrac{p}{q}$ to its terminating decimal."""
    generator_id = "convert_fraction_to_decimal"
    topic_slug = "fractions_decimals_and_percents"
    display_name = "Write a fraction as a decimal"

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        table = _FRAC_DEC_TABLES[difficulty]
        num, den = table[rng.randrange(len(table))]
        decimal_str = _format_terminating_decimal(num, den)

        # Factor the denominator for the worked solution.
        twos = 0
        fives = 0
        d = den
        while d % 2 == 0:
            d //= 2
            twos += 1
        while d % 5 == 0:
            d //= 5
            fives += 1
        k = max(twos, fives)
        power_of_ten = 10 ** k
        scaled_num = num * (power_of_ten // den)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (num, den)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Write $\\tfrac{{{num}}}{{{den}}}$ as a decimal.",
            answer_latex=f"${decimal_str}$",
            hints=[
                "Every terminating decimal comes from a fraction whose denominator is a product of $2$s and $5$s.",
                rf"Rewrite $\tfrac{{{num}}}{{{den}}}$ with a denominator of $10^{{{k}}} = {power_of_ten}$.",
                rf"$\tfrac{{{num}}}{{{den}}} = \tfrac{{{scaled_num}}}{{{power_of_ten}}} = {decimal_str}$.",
            ],
            solution_steps_latex=[
                rf"Start with $\tfrac{{{num}}}{{{den}}}$.",
                rf"Multiply top and bottom so the denominator becomes $10^{{{k}}} = {power_of_ten}$: "
                rf"$\tfrac{{{num}}}{{{den}}} = \tfrac{{{scaled_num}}}{{{power_of_ten}}}$.",
                f"Read the decimal directly: ${decimal_str}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

@register
class ConvertDecimalToPercent(Generator):
    """Write a terminating decimal as a percent by multiplying by $100$."""
    generator_id = "convert_decimal_to_percent"
    topic_slug = "fractions_decimals_and_percents"
    display_name = "Write a decimal as a percent"

    # Integer "cents" ranges: the decimal is cents/100.
    _RANGES = {"easy": (1, 99), "medium": (1, 199), "hard": (1, 995)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        if difficulty == "hard":
            # Hard: allow thousandths, so decimals like 0.125 appear.
            cents = rng.randint(lo, hi)
            decimal_str = _format_terminating_decimal(cents, 1000)
            percent_str = _format_terminating_decimal(cents, 10)
        else:
            cents = rng.randint(lo, hi)
            decimal_str = _format_terminating_decimal(cents, 100)
            percent_str = str(cents)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (cents,)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Write ${decimal_str}$ as a percent.",
            answer_latex=f"${percent_str}\\%$",
            hints=[
                "To convert a decimal to a percent, multiply by $100$ and attach the $\\%$ symbol.",
                "Multiplying by $100$ shifts the decimal point two places to the right.",
                f"${decimal_str} \\times 100 = {percent_str}$, so the answer is ${percent_str}\\%$.",
            ],
            solution_steps_latex=[
                f"Start with ${decimal_str}$.",
                f"Multiply by $100$ (shift the decimal point two places right): ${percent_str}$.",
                f"Attach the percent sign: ${percent_str}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


# ---------------------------------------------------------------------------

# Fractions whose percent form is a whole number (denom divides 100).
_PERCENT_FRAC_EASY = [
    (num, den)
    for (num, den) in _terminating_fractions_up_to(100)
    if 100 % den == 0
]
# Add .5-percent and .25-percent denominators (8, 16, 40).
_PERCENT_FRAC_MEDIUM = [
    (num, den)
    for (num, den) in _terminating_fractions_up_to(100)
    if 100 % den == 0 or den in (8, 40)
]
_PERCENT_FRAC_HARD = [
    (num, den)
    for (num, den) in _terminating_fractions_up_to(200)
    if 100 % den == 0 or den in (8, 16, 40, 80)
]

_PERCENT_FRAC_TABLES: dict[Difficulty, list[tuple[int, int]]] = {
    "easy": _PERCENT_FRAC_EASY,
    "medium": _PERCENT_FRAC_MEDIUM,
    "hard": _PERCENT_FRAC_HARD,
}


@register
class ConvertPercentToFraction(Generator):
    """Convert a percent (possibly with one or two decimal places) to a reduced fraction."""
    generator_id = "convert_percent_to_fraction"
    topic_slug = "fractions_decimals_and_percents"
    display_name = "Write a percent as a fraction"

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        table = _PERCENT_FRAC_TABLES[difficulty]
        num, den = table[rng.randrange(len(table))]
        # Percent value as a reduced rational (percent_num / percent_den).
        pnum = 100 * num
        pden = den
        g = _math.gcd(pnum, pden)
        pnum //= g
        pden //= g
        # Format percent as decimal string.
        if pden == 1:
            percent_str = str(pnum)
        else:
            percent_str = _format_terminating_decimal(pnum, pden)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (num, den)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Write ${percent_str}\\%$ as a fraction in simplest form.",
            answer_latex=f"$\\tfrac{{{num}}}{{{den}}}$",
            hints=[
                r"A percent means 'per hundred' --- divide by $100$ to strip the $\%$ symbol.",
                rf"${percent_str}\% = \dfrac{{{percent_str}}}{{100}}$.",
                r"Simplify the resulting fraction by dividing the numerator and denominator by their greatest common factor.",
            ],
            solution_steps_latex=[
                rf"Rewrite ${percent_str}\%$ as a fraction over $100$: $\dfrac{{{percent_str}}}{{100}}$.",
                rf"Clear any decimal and reduce to lowest terms: $\tfrac{{{num}}}{{{den}}}$.",
                rf"The simplest form is $\tfrac{{{num}}}{{{den}}}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation"],
        )


# ===========================================================================
# Topic: understanding_percents
# ===========================================================================

_UNDERSTANDING_PCT_EASY = (10, 20, 25, 40, 50, 60, 75, 80)
_UNDERSTANDING_PCT_MEDIUM = (5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80)
_UNDERSTANDING_PCT_HARD = (2, 4, 8, 15, 18, 22, 28, 35, 42, 55, 65, 85, 95)


def _clean_whole_for_percent(p: int, lo: int, hi: int, rng: random.Random) -> int:
    """Return a whole-number 'whole' in [lo, hi] where p% of it is an integer."""
    step = 100 // _math.gcd(p, 100)
    lo_adj = max(lo, step)
    count = (hi - lo_adj) // step + 1
    k = rng.randint(0, max(0, count - 1))
    return lo_adj + k * step


@register
class PercentOfWholeSingleDigit(Generator):
    """``{part} is what percent of {whole}?`` with a small, clean percent answer."""
    generator_id = "percent_of_whole_single_digit"
    topic_slug = "understanding_percents"
    display_name = "part is what percent of whole"

    _RANGES = {"easy": (10, 100), "medium": (20, 400), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        percents_pool = {
            "easy": _UNDERSTANDING_PCT_EASY,
            "medium": _UNDERSTANDING_PCT_MEDIUM,
            "hard": _UNDERSTANDING_PCT_HARD,
        }[difficulty]
        pct = rng.choice(percents_pool)
        whole = _clean_whole_for_percent(pct, lo, hi, rng)
        part = pct * whole // 100

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (part, whole)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${part}$ is what percent of ${whole}$?",
            answer_latex=f"${pct}\\%$",
            hints=[
                r"`Percent` means `per hundred`: think of the question as $\dfrac{\text{part}}{\text{whole}}$ times $100$.",
                rf"Set up the ratio: $\dfrac{{{part}}}{{{whole}}}$.",
                f"Multiply by $100\\%$ to read the answer as a percent: ${pct}\\%$.",
            ],
            solution_steps_latex=[
                rf"Compute the ratio $\dfrac{{\text{{part}}}}{{\text{{whole}}}} = \dfrac{{{part}}}{{{whole}}}$.",
                rf"Simplify: $\dfrac{{{part}}}{{{whole}}} = \dfrac{{{pct}}}{{100}}$.",
                f"Read off the answer: ${pct}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )


@register
class PercentIdentifyFromShadedDescription(Generator):
    """A grid description: ``N squares, K shaded, what percent?``."""
    generator_id = "percent_identify_from_shaded_description"
    topic_slug = "understanding_percents"
    display_name = "Percent from a shaded-grid description"

    # Allowed (grid_size, percents) pairs per difficulty.
    _GRID_SETS = {
        "easy": [
            (100, (1, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 99)),
            (50,  (2, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 98)),
        ],
        "medium": [
            (100, tuple(range(1, 100))),
            (50,  (2, 4, 6, 8, 12, 14, 16, 20, 24, 30, 40, 50, 60, 70, 76, 80, 88, 92)),
            (200, (1, 2, 5, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 85, 90, 95, 99)),
        ],
        "hard": [
            (100, tuple(range(1, 100))),
            (200, tuple(range(1, 100))),
            (500, tuple(range(2, 100, 2))),
            (25,  (4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96)),
        ],
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        options = self._GRID_SETS[difficulty]
        grid_size, allowed_pcts = options[rng.randrange(len(options))]
        pct = rng.choice(allowed_pcts)
        shaded = pct * grid_size // 100

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (grid_size, shaded)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"A grid is divided into ${grid_size}$ equal squares. "
                f"${shaded}$ of the squares are shaded. What percent of the grid is shaded?"
            ),
            answer_latex=f"${pct}\\%$",
            hints=[
                r"`Percent of the grid shaded` means `shaded squares divided by total squares, times $100$`.",
                rf"Set up: $\dfrac{{{shaded}}}{{{grid_size}}}$.",
                f"Multiply by $100\\%$: ${pct}\\%$.",
            ],
            solution_steps_latex=[
                rf"Write the ratio of shaded to total: $\dfrac{{{shaded}}}{{{grid_size}}}$.",
                rf"Rescale to a denominator of $100$: $\dfrac{{{shaded}}}{{{grid_size}}} = \dfrac{{{pct}}}{{100}}$.",
                f"Read the percent: ${pct}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-visualization"],
        )


@register
class PercentEstimateSimple(Generator):
    """Estimation: `about what percent of W is P?` where P is near pct*W/100."""
    generator_id = "percent_estimate_simple"
    topic_slug = "understanding_percents"
    display_name = "Estimate a percent of a whole"

    # Benchmark percents for each difficulty (these are the answers).
    _ESTIMATE_PCT = {
        "easy": (10, 25, 50, 75),
        "medium": (10, 20, 25, 33, 50, 66, 75, 80, 90),
        "hard": (5, 10, 15, 20, 25, 33, 40, 50, 60, 66, 75, 80, 90),
    }
    _WHOLE_RANGES = {"easy": (20, 120), "medium": (40, 400), "hard": (50, 1000)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        pct_pool = self._ESTIMATE_PCT[difficulty]
        pct = rng.choice(pct_pool)
        lo, hi = self._WHOLE_RANGES[difficulty]
        # Pick a whole where the exact pct*whole/100 is an integer; use that as the anchor.
        # For 33 and 66 we approximate as 1/3 and 2/3, so W should be a multiple of 3.
        if pct in (33, 66):
            W_lo = max(lo, 3)
            W = W_lo + 3 * rng.randint(0, (hi - W_lo) // 3)
            if pct == 33:
                anchor = W // 3
            else:
                anchor = 2 * W // 3
        else:
            W = _clean_whole_for_percent(pct, lo, hi, rng)
            anchor = pct * W // 100
        # Jitter the part within a small window so the nearest benchmark is still `pct`.
        # Window size: at most 4% of W.
        jitter_max = max(1, min(4, anchor // 10))
        j = rng.randint(-jitter_max, jitter_max)
        part = max(1, anchor + j)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (part, W, pct)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"About what percent of ${W}$ is ${part}$? Give your answer to the nearest benchmark percent."
            ),
            answer_latex=f"${pct}\\%$",
            hints=[
                "Round the ratio to a benchmark percent like $10\\%, 25\\%, 50\\%, 75\\%,$ or $100\\%$.",
                rf"Compare $\dfrac{{{part}}}{{{W}}}$ to the nearest benchmark fraction.",
                f"The ratio is closest to $\\dfrac{{{pct}}}{{100}}$, so the answer is about ${pct}\\%$.",
            ],
            solution_steps_latex=[
                rf"Write the ratio $\dfrac{{{part}}}{{{W}}}$.",
                rf"Compare with benchmark fractions $\tfrac{{1}}{{10}}, \tfrac{{1}}{{4}}, \tfrac{{1}}{{2}}, \tfrac{{3}}{{4}}$, etc.",
                f"The closest benchmark is ${pct}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-estimation"],
        )


# ===========================================================================
# Topic: the_percent_equation (P = r * W)
# ===========================================================================


@register
class PercentEqFindPart(Generator):
    """Percent equation: given percent and whole, find the part."""
    generator_id = "percent_eq_find_part"
    topic_slug = "the_percent_equation"
    display_name = "Percent equation: find the part"

    _W_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1500)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._W_RANGES[difficulty]
        percents = _percents_for(difficulty)
        pct = rng.choice(percents)
        whole = _clean_whole_for_percent(pct, lo, hi, rng)
        part = pct * whole // 100

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (pct, whole)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"What is ${pct}\\%$ of ${whole}$?",
            answer_latex=f"${part}$",
            hints=[
                r"The percent equation is $\text{part} = \text{rate} \times \text{whole}$, where the rate is the percent written as a decimal.",
                rf"Rewrite ${pct}\%$ as the decimal $\tfrac{{{pct}}}{{100}}$.",
                rf"Multiply: $\tfrac{{{pct}}}{{100}} \times {whole} = {part}$.",
            ],
            solution_steps_latex=[
                rf"Apply the percent equation: $\text{{part}} = \tfrac{{{pct}}}{{100}} \cdot {whole}$.",
                rf"Compute the product: $\tfrac{{{pct}}}{{100}} \cdot {whole} = \tfrac{{{pct * whole}}}{{100}}$.",
                f"Simplify: $\\text{{part}} = {part}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-formula-substitution"],
        )


@register
class PercentEqFindPercent(Generator):
    """Percent equation: given part and whole, find the percent (rate)."""
    generator_id = "percent_eq_find_percent"
    topic_slug = "the_percent_equation"
    display_name = "Percent equation: find the percent"

    _W_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._W_RANGES[difficulty]
        percents = _percents_for(difficulty)
        pct = rng.choice(percents)
        whole = _clean_whole_for_percent(pct, lo, hi, rng)
        part = pct * whole // 100

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (part, whole)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${part}$ is what percent of ${whole}$?",
            answer_latex=f"${pct}\\%$",
            hints=[
                r"The percent equation is $\text{part} = r \cdot \text{whole}$. Solve for the rate $r$.",
                rf"$r = \dfrac{{\text{{part}}}}{{\text{{whole}}}} = \dfrac{{{part}}}{{{whole}}}$.",
                f"Convert $r$ to a percent by multiplying by $100\\%$: ${pct}\\%$.",
            ],
            solution_steps_latex=[
                rf"Start with the percent equation: ${part} = r \cdot {whole}$.",
                rf"Divide both sides by ${whole}$: $r = \dfrac{{{part}}}{{{whole}}} = \dfrac{{{pct}}}{{100}}$.",
                f"Write the rate as a percent: ${pct}\\%$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )


@register
class PercentEqFindWhole(Generator):
    """Percent equation: given part and percent, find the whole."""
    generator_id = "percent_eq_find_whole"
    topic_slug = "the_percent_equation"
    display_name = "Percent equation: find the whole"

    _W_RANGES = {"easy": (10, 200), "medium": (20, 500), "hard": (50, 1200)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._W_RANGES[difficulty]
        percents = _percents_for(difficulty)
        pct = rng.choice(percents)
        whole = _clean_whole_for_percent(pct, lo, hi, rng)
        part = pct * whole // 100

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (part, pct)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"${part}$ is ${pct}\\%$ of what number?",
            answer_latex=f"${whole}$",
            hints=[
                r"Use $\text{part} = r \cdot \text{whole}$ and solve for the whole.",
                rf"${part} = \tfrac{{{pct}}}{{100}} \cdot W$.",
                rf"Multiply both sides by $\tfrac{{100}}{{{pct}}}$ to isolate $W$.",
            ],
            solution_steps_latex=[
                rf"Write the percent equation: ${part} = \tfrac{{{pct}}}{{100}} \cdot W$.",
                rf"Solve for $W$: $W = {part} \cdot \tfrac{{100}}{{{pct}}} = \tfrac{{{100 * part}}}{{{pct}}}$.",
                f"Simplify: $W = {whole}$.",
            ],
            tags=["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-algebraic-manipulation"],
        )
