"""Applications of proportional reasoning (pre-algebra).

Canonical topic slug ``applications_of_proportional_reasoning`` at
``wiki/topics/pre_algebra/Applications_Of_Proportional_Reasoning.md``.

Three word-problem generators:

- ``recipe_scaling_proportion_word_problem``: scale a recipe up or down by a
  clean factor. Backward construction picks the per-serving amount and the
  original / target batch sizes first.
- ``currency_or_rate_conversion_word_problem``: currency or rate conversion
  built on an integer "for every A of X you get B of Y" premise.
- ``shadow_height_similar_triangles_word_problem``: similar-triangle shadow
  problem. Backward: pick the target object height and the reference
  person + shadow ratio first.

All three generators use the Math_Wiki approved-name pool (Maya, Kai,
Priya, Rohan, Zoe, Emilia, Mateo, Leilani) and avoid textbook openers.
"""
from __future__ import annotations

import random
from fractions import Fraction

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "applications_of_proportional_reasoning"
_TAGS = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-translation",
    "#word-problem-support",
]


_NAMES = ("Maya", "Kai", "Priya", "Rohan", "Zoe", "Emilia", "Mateo", "Leilani")


def _fmt_fraction_latex(num: int, den: int) -> str:
    """Render num/den as LaTeX, collapsing to an integer when possible."""
    if den == 0:
        raise ValueError("denominator cannot be zero")
    if num % den == 0:
        return str(num // den)
    # Keep it improper — students should be comfortable with mixed/improper fractions.
    return rf"\dfrac{{{num}}}{{{den}}}"


# ---------------------------------------------------------------------------

@register
class RecipeScalingProblem(Generator):
    """Scale a recipe up or down using a proportion.

    Backward construction: pick the per-serving ingredient amount as a
    clean fraction (e.g. ``1/16`` cup per cookie), pick original and
    target batch sizes, then the original amount is
    ``per_serving * original_batch`` and the final answer is
    ``per_serving * target_batch``. Both values come out as clean fractions.
    """
    generator_id = "recipe_scaling_proportion_word_problem"
    topic_slug = TOPIC_SLUG
    display_name = "Scale a recipe by a proportion"

    _SCENARIOS: tuple[tuple[str, str, str, str], ...] = (
        ("Maya",   "baking",            "cookies",       "cup of flour"),
        ("Kai",    "community-garden",  "smoothies",     "cup of oat milk"),
        ("Priya",  "school-newspaper",  "slices of pizza", "cup of tomato sauce"),
        ("Rohan",  "study-group",       "muffins",       "cup of sugar"),
        ("Zoe",    "photography-club",  "granola bars",  "cup of rolled oats"),
        ("Emilia", "drama-club",        "pancakes",      "cup of buttermilk"),
        ("Mateo",  "pop-up-book",       "cupcakes",      "cup of cocoa powder"),
        ("Leilani","farmers-market",    "loaves of bread", "cup of whole-wheat flour"),
    )

    # Each difficulty picks a per-serving fraction from this pool and a
    # (original, target) batch-size pair. Parameter space: scenarios * fracs * pairs.
    _PER_SERVING: dict[str, tuple[tuple[int, int], ...]] = {
        "easy":   (( 1, 12), ( 1,  8), ( 1,  6), ( 1,  4)),
        "medium": (( 1, 16), ( 1, 12), ( 1,  8), ( 3, 16), ( 1,  6)),
        "hard":   (( 1, 24), ( 3, 32), ( 1, 12), ( 5, 48), ( 3, 16), ( 2,  9)),
    }
    _BATCH_PAIRS: dict[str, tuple[tuple[int, int], ...]] = {
        "easy":   ((12, 24), (12, 36), ( 6, 24), ( 8, 32), (10, 30)),
        "medium": ((12, 30), (18, 45), (24, 60), (16, 40), (15, 35), (20, 50)),
        "hard":   ((24, 60), (30, 75), (36, 96), (28, 63), (45, 120), (48, 108)),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scenario_idx = rng.randint(0, len(self._SCENARIOS) - 1)
        who, context, noun, ingredient = self._SCENARIOS[scenario_idx]

        frac_pool = self._PER_SERVING[difficulty]
        frac_idx = rng.randint(0, len(frac_pool) - 1)
        p_num, p_den = frac_pool[frac_idx]

        batch_pool = self._BATCH_PAIRS[difficulty]
        batch_idx = rng.randint(0, len(batch_pool) - 1)
        original, target = batch_pool[batch_idx]

        # Per serving is p_num/p_den. Original uses p_num*original/p_den;
        # Target uses p_num*target/p_den.
        orig_num = p_num * original
        orig_den = p_den
        # Reduce
        g_o = _gcd(orig_num, orig_den)
        orig_num //= g_o
        orig_den //= g_o

        ans_num = p_num * target
        ans_den = p_den
        g_a = _gcd(ans_num, ans_den)
        ans_num //= g_a
        ans_den //= g_a

        orig_latex = _fmt_fraction_latex(orig_num, orig_den)
        answer_latex = _fmt_fraction_latex(ans_num, ans_den)
        per_serving_latex = _fmt_fraction_latex(p_num, p_den)

        # "cup" vs "cups" wording on the original amount.
        unit_name = ingredient  # already contains "cup of ..." singular phrasing
        # Build a small grammatical tweak: if original amount is an integer >= 2,
        # pluralize "cup" -> "cups". Otherwise leave the fraction-with-"cup".
        orig_is_int = orig_den == 1
        orig_plural = (orig_is_int and orig_num >= 2)
        orig_unit = unit_name.replace("cup of", "cups of") if orig_plural else unit_name

        ans_is_int = ans_den == 1
        ans_plural = (ans_is_int and ans_num >= 2)
        ans_unit = unit_name.replace("cup of", "cups of") if ans_plural else unit_name

        statement = (
            f"A {context.replace('-', ' ')} recipe that makes ${original}$ {noun} "
            f"calls for ${orig_latex}$ {orig_unit}. {who} wants to make "
            f"${target}$ {noun} instead. Determine the amount of "
            f"{ingredient.split(' of ', 1)[1]} {who} needs."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (scenario_idx, frac_idx, batch_idx),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_latex}$ {ans_unit}",
            hints=[
                (
                    "Set up a proportion relating the original batch to the new batch: "
                    r"$\dfrac{\text{ingredient}_{\text{new}}}{\text{servings}_{\text{new}}} "
                    r"= \dfrac{\text{ingredient}_{\text{old}}}{\text{servings}_{\text{old}}}$."
                ),
                (
                    f"Here that becomes $\\dfrac{{x}}{{{target}}} = "
                    f"\\dfrac{{{orig_latex}}}{{{original}}}$."
                ),
                (
                    "Multiply both sides by the new number of servings to isolate $x$, "
                    "then simplify the resulting fraction."
                ),
            ],
            solution_steps_latex=[
                (
                    f"First find the per-serving amount: "
                    f"$\\dfrac{{{orig_latex}}}{{{original}}} = {per_serving_latex}$ "
                    f"{ingredient} per {noun[:-1] if noun.endswith('s') else noun}."
                ),
                (
                    f"Multiply the per-serving amount by the new batch size: "
                    f"${per_serving_latex} \\cdot {target}$."
                ),
                f"Simplify: ${answer_latex}$ {ans_unit}.",
            ],
            tags=list(_TAGS),
        )


def _gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a or 1


# ---------------------------------------------------------------------------

@register
class CurrencyOrRateConversion(Generator):
    """Currency or rate conversion word problem.

    Backward construction: pick the clean answer first, then the input
    value, and derive a matching integer rate so cross-multiplication
    produces the exact answer with no rounding.

    Two flavors:
    - currency: "${A}$ of currency X buys ${B}$ of currency Y" conversions
    - rate: "${A}$ units of X covers ${B}$ units of Y" (mileage, wages, etc.)
    """
    generator_id = "currency_or_rate_conversion_word_problem"
    topic_slug = TOPIC_SLUG
    display_name = "Currency / rate conversion via proportion"

    # Each scenario is (who, setup_phrase, unit_x, unit_y, flavor).
    # flavor = "currency" or "rate"
    _SCENARIOS: tuple[tuple[str, str, str, str, str], ...] = (
        ("Maya",    "is budgeting for an exchange trip",           "US dollars",  "euros",          "currency"),
        ("Rohan",   "is planning a family visit overseas",          "US dollars",  "British pounds", "currency"),
        ("Priya",   "is ordering art supplies from abroad",         "US dollars",  "Canadian dollars","currency"),
        ("Emilia",  "is comparing prices at a craft fair",          "US dollars",  "Mexican pesos",  "currency"),
        ("Kai",     "is tracking fuel for a community-garden run",  "miles",       "gallons",        "rate"),
        ("Zoe",     "is planning a photography road trip",          "miles",       "gallons",        "rate"),
        ("Mateo",   "is paid an hourly studio rate",                "hours",       "dollars",        "rate"),
        ("Leilani", "earns a set amount per farmers-market shift",  "shifts",      "dollars",        "rate"),
    )

    # (base_x, base_y): "base_x units of X corresponds to base_y units of Y"
    _RATES: dict[str, tuple[tuple[int, int], ...]] = {
        "easy":   ((1, 2), (1, 3), (2, 5), (1, 4), (3, 5)),
        "medium": ((4, 9), (5, 11), (3, 8), (7, 10), (2, 9), (5, 7)),
        "hard":   ((7, 12), (8, 15), (11, 18), (9, 14), (6, 13), (13, 25)),
    }
    # Multiplier for the "given value": given_x = base_x * k, then
    # the answer is base_y * k (both clean integers).
    _MULTIPLIERS: dict[str, tuple[int, ...]] = {
        "easy":   (3, 4, 5, 6, 8, 10),
        "medium": (4, 6, 7, 9, 11, 12, 15),
        "hard":   (7, 9, 12, 14, 18, 21, 25),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scenario_idx = rng.randint(0, len(self._SCENARIOS) - 1)
        who, phrase, unit_x, unit_y, flavor = self._SCENARIOS[scenario_idx]

        rate_pool = self._RATES[difficulty]
        rate_idx = rng.randint(0, len(rate_pool) - 1)
        base_x, base_y = rate_pool[rate_idx]

        mult_pool = self._MULTIPLIERS[difficulty]
        k = rng.choice(mult_pool)

        given_x = base_x * k
        answer_y = base_y * k

        # Statement is phrased naturally per flavor.
        if flavor == "currency":
            statement = (
                f"{who} {phrase}. The current exchange rate is "
                f"${base_x}$ {unit_x} to ${base_y}$ {unit_y}. "
                f"Determine how many {unit_y} {who} will receive in exchange for "
                f"${given_x}$ {unit_x}."
            )
        elif unit_y == "dollars":
            statement = (
                f"{who} {phrase}: every ${base_x}$ {unit_x} of work is paid "
                f"${base_y}$ dollars. Determine how much {who} earns after "
                f"${given_x}$ {unit_x}."
            )
        else:  # miles / gallons
            statement = (
                f"{who} {phrase}. A vehicle covers ${base_x}$ {unit_x} "
                f"on every ${base_y}$ {unit_y}. Determine how many {unit_y} "
                f"the vehicle uses to cover ${given_x}$ {unit_x}."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (scenario_idx, rate_idx, k),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_y}$ {unit_y}",
            hints=[
                (
                    r"Set up a proportion matching the two units: "
                    r"$\dfrac{\text{unit X}}{\text{unit Y}} = \dfrac{\text{unit X}}{\text{unit Y}}$."
                ),
                (
                    f"Here: $\\dfrac{{{base_x}}}{{{base_y}}} = "
                    f"\\dfrac{{{given_x}}}{{x}}$."
                ),
                "Cross-multiply and solve for $x$.",
            ],
            solution_steps_latex=[
                (
                    f"Write the proportion with matching units: "
                    f"$\\dfrac{{{base_x}\\;{unit_x}}}{{{base_y}\\;{unit_y}}} "
                    f"= \\dfrac{{{given_x}\\;{unit_x}}}{{x\\;{unit_y}}}$."
                ),
                (
                    f"Cross-multiply: ${base_x} \\cdot x = {base_y} \\cdot {given_x}$, "
                    f"so ${base_x}x = {base_y * given_x}$."
                ),
                (
                    f"Divide both sides by ${base_x}$: "
                    f"$x = \\dfrac{{{base_y * given_x}}}{{{base_x}}} = {answer_y}$."
                ),
                f"So the answer is ${answer_y}$ {unit_y}.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class ShadowOrHeightSimilarTriangles(Generator):
    """Similar-triangles word problem: shadow or height.

    Backward construction: pick the target (tree / flagpole) height as a
    clean integer, pick an integer reference person height and an integer
    reference shadow length such that person_height / person_shadow is a
    clean ratio, then the target shadow follows from
    target_shadow = target_height * person_shadow / person_height.

    To guarantee integer answers throughout, we only pick parameter
    combinations where target_shadow divides cleanly. The generator picks
    the *person* side lengths first, then a multiplier that makes the
    target a clean integer.
    """
    generator_id = "shadow_similar_triangles_word_problem"
    topic_slug = TOPIC_SLUG
    display_name = "Similar triangles shadow / height word problem"

    _SCENARIOS: tuple[tuple[str, str, str], ...] = (
        ("Maya",    "on a photography class field trip",        "oak tree"),
        ("Kai",     "measuring objects near the community garden","garden flagpole"),
        ("Priya",   "on a school newspaper assignment",          "school flagpole"),
        ("Rohan",   "helping survey a park",                     "lamp post"),
        ("Zoe",     "scouting a shoot location",                 "statue"),
        ("Emilia",  "on a drama club scenery trip",              "stage backdrop"),
        ("Mateo",   "sketching buildings for a pop-up book",     "clock tower"),
        ("Leilani", "at a farmers market pavilion",              "flagpole"),
    )

    # (person_height_ft, person_shadow_ft) with person_height // person_shadow exact.
    # Kept as simple ratios like 6:4 = 3:2, 5:4, 6:3 = 2:1, 5:2, 4:3, 6:5.
    _PERSON_PAIRS: dict[str, tuple[tuple[int, int], ...]] = {
        "easy":   ((6, 4), (6, 3), (5, 2), (4, 2), (6, 2)),
        "medium": ((6, 5), (5, 4), (7, 4), (6, 4), (8, 3), (5, 3)),
        "hard":   ((5, 2), (8, 5), (7, 4), (9, 4), (7, 3), (11, 5)),
    }
    # Target heights (in feet) — picked so target_height is a multiple
    # of person_height for a clean shadow.
    _MULTIPLIERS: dict[str, tuple[int, ...]] = {
        "easy":   (2, 3, 4, 5),
        "medium": (3, 4, 5, 6, 7, 8),
        "hard":   (5, 6, 7, 8, 9, 10, 12),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        scenario_idx = rng.randint(0, len(self._SCENARIOS) - 1)
        who, context, target_name = self._SCENARIOS[scenario_idx]

        pair_pool = self._PERSON_PAIRS[difficulty]
        pair_idx = rng.randint(0, len(pair_pool) - 1)
        ph, ps = pair_pool[pair_idx]

        mult_pool = self._MULTIPLIERS[difficulty]
        k = rng.choice(mult_pool)

        target_height = ph * k
        target_shadow = ps * k

        # Flip a coin: student either solves for target_height given the
        # shadow, or for target_shadow given the height.
        ask_for_height = rng.random() < 0.5

        if ask_for_height:
            statement = (
                f"{who}, {context}, is {ph} feet tall and casts a shadow ${ps}$ "
                f"feet long. At the same moment, a nearby {target_name} casts a "
                f"shadow ${target_shadow}$ feet long. Determine the height of "
                f"the {target_name}."
            )
            answer = f"${target_height}$ feet"
            unknown_letter = "h"
            step_proportion = (
                f"$\\dfrac{{{ph}}}{{{ps}}} = \\dfrac{{{unknown_letter}}}{{{target_shadow}}}$"
            )
            cross_multiply = (
                f"${ps} \\cdot {unknown_letter} = {ph} \\cdot {target_shadow}$, "
                f"so ${ps}\\,{unknown_letter} = {ph * target_shadow}$."
            )
            final_step = (
                f"Divide both sides by ${ps}$: "
                f"${unknown_letter} = \\dfrac{{{ph * target_shadow}}}{{{ps}}} = {target_height}$."
            )
        else:
            statement = (
                f"{who}, {context}, is ${ph}$ feet tall and casts a shadow ${ps}$ "
                f"feet long. At the same moment, a nearby {target_name} is "
                f"${target_height}$ feet tall. Determine the length of the "
                f"{target_name}'s shadow."
            )
            answer = f"${target_shadow}$ feet"
            unknown_letter = "s"
            step_proportion = (
                f"$\\dfrac{{{ph}}}{{{ps}}} = \\dfrac{{{target_height}}}{{{unknown_letter}}}$"
            )
            cross_multiply = (
                f"${ph} \\cdot {unknown_letter} = {ps} \\cdot {target_height}$, "
                f"so ${ph}\\,{unknown_letter} = {ps * target_height}$."
            )
            final_step = (
                f"Divide both sides by ${ph}$: "
                f"${unknown_letter} = \\dfrac{{{ps * target_height}}}{{{ph}}} = {target_shadow}$."
            )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (scenario_idx, pair_idx, k, ask_for_height),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "At the same moment of day, the sun's rays strike every object "
                    "at the same angle, so a person and a tall object form two "
                    "similar right triangles."
                ),
                (
                    r"Set the ratio of (height) to (shadow length) equal for both "
                    r"triangles: $\dfrac{\text{person height}}{\text{person shadow}} "
                    r"= \dfrac{\text{object height}}{\text{object shadow}}$."
                ),
                (
                    f"Substitute the known values to get {step_proportion}, "
                    f"then cross-multiply."
                ),
            ],
            solution_steps_latex=[
                (
                    "Identify the similar triangles formed by the person, the "
                    f"{target_name}, and their shadows."
                ),
                f"Write the proportion {step_proportion}.",
                f"Cross-multiply: {cross_multiply}",
                final_step,
            ],
            tags=list(_TAGS),
        )
