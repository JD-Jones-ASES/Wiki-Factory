"""Fraction basics generators (Cluster 1).

Two canonical topic slugs covered here:

- ``equivalent_fractions_and_simplifying`` at
  wiki/topics/pre_algebra/Equivalent_Fractions_And_Simplifying.md

  Generators:
    * simplify_fraction           --- reduce a non-reduced fraction
    * find_equivalent_fraction    --- fill in a missing numerator / denominator
    * equivalent_or_not           --- decide whether two fractions are equal

- ``mixed_numbers_and_improper_fractions`` at
  wiki/topics/pre_algebra/Mixed_Numbers_And_Improper_Fractions.md

  Generators:
    * improper_to_mixed           --- convert improper fraction to mixed number
    * mixed_to_improper           --- convert mixed number to improper fraction
    * classify_fraction           --- label as proper, improper, or whole

All generators use backward construction: pick a clean answer first, then
derive the presented parameters. Answers are exact integers or reduced
fractions --- never floating point.
"""
from __future__ import annotations

import math
import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# Shared tag sets (same tags apply to every fraction basics generator).
_TAGS_SIMPLIFY = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]
_TAGS_REASONING = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-conceptual-reasoning",
]


def _random_coprime_pair(rng: random.Random, max_val: int) -> tuple[int, int]:
    """Return (a, b) with 1 <= a, b <= max_val, a != b, gcd(a, b) == 1.

    The rejection loop converges quickly because coprime pairs are dense
    among small integers. ``max_val`` is assumed to be at least 3.
    """
    for _ in range(200):
        a = rng.randint(1, max_val)
        b = rng.randint(2, max_val)  # denominator must be at least 2
        if a == b:
            continue
        if math.gcd(a, b) == 1:
            return a, b
    # Extremely unlikely; fall back to a guaranteed-coprime pair.
    return 1, 2


# ===========================================================================
# Topic 1: equivalent_fractions_and_simplifying
# ===========================================================================

@register
class SimplifyFraction(Generator):
    """Reduce a non-reduced fraction $kp/kq$ to lowest terms $p/q$."""
    generator_id = "simplify_fraction"
    topic_slug = "equivalent_fractions_and_simplifying"
    display_name = "Simplify a fraction"

    # max_val limits the reduced numerator/denominator; k_range scales the multiplier.
    _PARAMS = {
        "easy":   {"max_val": 9,  "k_range": (2, 6)},
        "medium": {"max_val": 14, "k_range": (2, 10)},
        "hard":   {"max_val": 20, "k_range": (3, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        p, q = _random_coprime_pair(rng, params["max_val"])
        k = rng.randint(*params["k_range"])
        num = k * p
        den = k * q

        statement = rf"Simplify the fraction $\dfrac{{{num}}}{{{den}}}$ to lowest terms."
        answer = rf"$\dfrac{{{p}}}{{{q}}}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (num, den)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Find the greatest common divisor (GCD) of ${num}$ and ${den}$.",
                f"The GCD is ${k}$, so divide the numerator and denominator by ${k}$.",
                rf"$\dfrac{{{num} \div {k}}}{{{den} \div {k}}} = \dfrac{{{p}}}{{{q}}}$.",
            ],
            solution_steps_latex=[
                rf"Start with $\dfrac{{{num}}}{{{den}}}$.",
                f"Compute $\\gcd({num}, {den}) = {k}$.",
                rf"Divide top and bottom by ${k}$: $\dfrac{{{num} \div {k}}}{{{den} \div {k}}} = \dfrac{{{p}}}{{{q}}}$.",
                f"Check: $\\gcd({p}, {q}) = 1$, so the fraction is fully reduced.",
            ],
            tags=_TAGS_SIMPLIFY + [f"#difficulty-{difficulty}"],
        )


@register
class FindEquivalentFraction(Generator):
    """Given a reduced fraction $a/b$, find the missing part of an equivalent fraction.

    Presents either ``a/b = ?/kb`` (ask for the numerator) or ``a/b = ka/?``
    (ask for the denominator).
    """
    generator_id = "find_equivalent_fraction"
    topic_slug = "equivalent_fractions_and_simplifying"
    display_name = "Find the missing part of an equivalent fraction"

    _PARAMS = {
        "easy":   {"max_val": 9,  "k_range": (2, 6)},
        "medium": {"max_val": 14, "k_range": (2, 10)},
        "hard":   {"max_val": 20, "k_range": (3, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        a, b = _random_coprime_pair(rng, params["max_val"])
        k = rng.randint(*params["k_range"])
        ask_numerator = rng.choice([True, False])

        if ask_numerator:
            # Given denominator kb, find numerator ka.
            known_den = k * b
            missing = k * a
            statement = (
                rf"Find the missing numerator: $\dfrac{{{a}}}{{{b}}} = \dfrac{{?}}{{{known_den}}}$."
            )
            unknown_desc = "numerator"
            scale_hint = (
                rf"The denominator went from ${b}$ to ${known_den}$, "
                rf"which is a factor of $\dfrac{{{known_den}}}{{{b}}} = {k}$."
            )
            compute_hint = rf"Multiply the numerator by ${k}$: ${a} \times {k} = {missing}$."
            params_key = ("num", a, b, k)
        else:
            # Given numerator ka, find denominator kb.
            known_num = k * a
            missing = k * b
            statement = (
                rf"Find the missing denominator: $\dfrac{{{a}}}{{{b}}} = \dfrac{{{known_num}}}{{?}}$."
            )
            unknown_desc = "denominator"
            scale_hint = (
                rf"The numerator went from ${a}$ to ${known_num}$, "
                rf"which is a factor of $\dfrac{{{known_num}}}{{{a}}} = {k}$."
            )
            compute_hint = rf"Multiply the denominator by ${k}$: ${b} \times {k} = {missing}$."
            params_key = ("den", a, b, k)

        answer = f"${missing}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params_key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Equivalent fractions are created by multiplying the top and bottom by the same number.",
                scale_hint,
                compute_hint,
            ],
            solution_steps_latex=[
                f"Identify the scaling factor by comparing the known parts.",
                scale_hint,
                f"Apply the same factor to the {unknown_desc}.",
                compute_hint,
                f"The missing value is ${missing}$.",
            ],
            tags=_TAGS_SIMPLIFY + [f"#difficulty-{difficulty}"],
        )


@register
class EquivalentOrNot(Generator):
    """Decide whether two fractions are equivalent.

    Half the time we produce a genuine equivalent pair ($a/b$ and $ka/kb$).
    Half the time we produce a near-miss by adding 1 to the numerator or
    denominator of the second fraction.
    """
    generator_id = "equivalent_or_not"
    topic_slug = "equivalent_fractions_and_simplifying"
    display_name = "Are two fractions equivalent?"

    _PARAMS = {
        "easy":   {"max_val": 9,  "k_range": (2, 6)},
        "medium": {"max_val": 14, "k_range": (2, 10)},
        "hard":   {"max_val": 20, "k_range": (3, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        a, b = _random_coprime_pair(rng, params["max_val"])
        k = rng.randint(*params["k_range"])
        num2 = k * a
        den2 = k * b
        is_equivalent = rng.choice([True, False])

        if not is_equivalent:
            # Break equivalence by nudging the numerator or denominator.
            nudge_num = rng.choice([True, False])
            delta = rng.choice([-1, 1])
            if nudge_num:
                num2 = num2 + delta
                if num2 <= 0:
                    num2 = k * a + 1  # fall back to +1 to stay positive
            else:
                den2 = den2 + delta
                if den2 <= 1:
                    den2 = k * b + 1
            # Guard against accidental equivalence after the nudge.
            if a * den2 == b * num2:
                num2 += 1  # forces inequality

        answer_word = "Yes" if (a * den2 == b * num2) else "No"
        params_key = (a, b, num2, den2)

        statement = (
            rf"Are $\dfrac{{{a}}}{{{b}}}$ and $\dfrac{{{num2}}}{{{den2}}}$ equivalent? "
            rf"Answer $\text{{Yes}}$ or $\text{{No}}$."
        )

        # Cross-multiplication check phrased the same way regardless of outcome.
        cross_left = a * den2
        cross_right = b * num2
        check_line = (
            rf"Cross multiply: ${a} \times {den2} = {cross_left}$ "
            rf"and ${b} \times {num2} = {cross_right}$."
        )
        if answer_word == "Yes":
            conclusion = (
                rf"Both products equal ${cross_left}$, so the fractions are equivalent."
            )
        else:
            conclusion = (
                rf"${cross_left} \ne {cross_right}$, so the fractions are not equivalent."
            )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params_key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${answer_word}$",
            hints=[
                r"Two fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ are equivalent when $a \cdot d = b \cdot c$.",
                check_line,
                conclusion,
            ],
            solution_steps_latex=[
                rf"Compare $\dfrac{{{a}}}{{{b}}}$ with $\dfrac{{{num2}}}{{{den2}}}$.",
                check_line,
                conclusion,
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )


# ===========================================================================
# Topic 2: mixed_numbers_and_improper_fractions
# ===========================================================================

@register
class ImproperToMixed(Generator):
    """Convert an improper fraction $(wd + r)/d$ to the mixed number $w \\tfrac{r}{d}$."""
    generator_id = "improper_to_mixed"
    topic_slug = "mixed_numbers_and_improper_fractions"
    display_name = "Convert improper fraction to mixed number"

    # w = whole part, d = denominator; r is chosen in [1, d-1] for a proper fractional part.
    _PARAMS = {
        "easy":   {"w_range": (1, 6),  "d_range": (2, 8)},
        "medium": {"w_range": (2, 12), "d_range": (3, 12)},
        "hard":   {"w_range": (3, 20), "d_range": (4, 16)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        w = rng.randint(*params["w_range"])
        d = rng.randint(*params["d_range"])
        r = rng.randint(1, d - 1)  # ensures r/d is a proper, non-zero fraction
        improper_num = w * d + r

        statement = rf"Convert the improper fraction $\dfrac{{{improper_num}}}{{{d}}}$ to a mixed number."
        answer = rf"${w}\tfrac{{{r}}}{{{d}}}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (improper_num, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Divide ${improper_num}$ by ${d}$ using long division.",
                f"${improper_num} \\div {d} = {w}$ with a remainder of ${r}$.",
                f"The quotient ${w}$ becomes the whole part and the remainder ${r}$ stays over ${d}$.",
            ],
            solution_steps_latex=[
                rf"Divide numerator by denominator: ${improper_num} \div {d}$.",
                f"Quotient: ${w}$. Remainder: ${r}$.",
                rf"Write as $\text{{quotient}}\tfrac{{\text{{remainder}}}}{{\text{{divisor}}}} = {w}\tfrac{{{r}}}{{{d}}}$.",
            ],
            tags=_TAGS_SIMPLIFY + [f"#difficulty-{difficulty}"],
        )


@register
class MixedToImproper(Generator):
    """Convert the mixed number $w \\tfrac{r}{d}$ to the improper fraction $(wd + r)/d$."""
    generator_id = "mixed_to_improper"
    topic_slug = "mixed_numbers_and_improper_fractions"
    display_name = "Convert mixed number to improper fraction"

    _PARAMS = {
        "easy":   {"w_range": (1, 6),  "d_range": (2, 8)},
        "medium": {"w_range": (2, 12), "d_range": (3, 12)},
        "hard":   {"w_range": (3, 20), "d_range": (4, 16)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        w = rng.randint(*params["w_range"])
        d = rng.randint(*params["d_range"])
        r = rng.randint(1, d - 1)
        improper_num = w * d + r

        statement = rf"Convert the mixed number ${w}\tfrac{{{r}}}{{{d}}}$ to an improper fraction."
        answer = rf"$\dfrac{{{improper_num}}}{{{d}}}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (w, r, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                f"Multiply the whole part ${w}$ by the denominator ${d}$.",
                f"${w} \\times {d} = {w * d}$. Then add the numerator ${r}$.",
                rf"${w * d} + {r} = {improper_num}$, and the denominator stays ${d}$.",
            ],
            solution_steps_latex=[
                rf"Multiply whole times denominator: ${w} \times {d} = {w * d}$.",
                rf"Add the numerator: ${w * d} + {r} = {improper_num}$.",
                rf"Keep the original denominator: $\dfrac{{{improper_num}}}{{{d}}}$.",
            ],
            tags=_TAGS_SIMPLIFY + [f"#difficulty-{difficulty}"],
        )


@register
class ClassifyFraction(Generator):
    """Classify a fraction as ``proper``, ``improper``, or ``whole``.

    Proper : numerator < denominator.
    Whole  : numerator is a positive multiple of the denominator (>= 1 whole).
    Improper (strict): numerator >= denominator and NOT a multiple of it.
    """
    generator_id = "classify_fraction"
    topic_slug = "mixed_numbers_and_improper_fractions"
    display_name = "Classify a fraction (proper, improper, or whole)"

    _PARAMS = {
        "easy":   {"max_num": 15, "max_den": 9},
        "medium": {"max_num": 30, "max_den": 12},
        "hard":   {"max_num": 60, "max_den": 18},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        params = self._PARAMS[difficulty]
        max_num = params["max_num"]
        max_den = params["max_den"]
        # Rotate through the three categories roughly evenly.
        category = rng.choice(["proper", "improper", "whole"])

        if category == "proper":
            d = rng.randint(3, max_den)
            n = rng.randint(1, d - 1)
        elif category == "whole":
            d = rng.randint(2, max_den)
            mult = rng.randint(1, max(2, max_num // d))
            n = mult * d
        else:  # improper (strict, non-whole)
            d = rng.randint(2, max_den)
            # Start one above the denominator, then skip multiples.
            for _ in range(50):
                n = rng.randint(d + 1, max(d + 2, max_num))
                if n % d != 0:
                    break
            else:
                # Fallback: d + 1 is guaranteed improper non-whole for d >= 2.
                n = d + 1

        # Determine the correct classification from the numbers (source of truth).
        if n < d:
            answer_word = "proper"
            classification_sentence = (
                f"Since ${n} < {d}$, the numerator is smaller than the denominator, so the fraction is **proper**."
            )
        elif n % d == 0:
            whole_val = n // d
            answer_word = "whole"
            classification_sentence = (
                rf"Since ${n} \div {d} = {whole_val}$ with no remainder, the fraction equals a whole number, so it is classified as **whole**."
            )
        else:
            answer_word = "improper"
            classification_sentence = (
                f"Since ${n} > {d}$ and ${n}$ is not a multiple of ${d}$, the fraction is **improper**."
            )

        statement = (
            rf"Classify the fraction $\dfrac{{{n}}}{{{d}}}$ as $\text{{proper}}$, "
            rf"$\text{{improper}}$, or $\text{{whole}}$."
        )

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (n, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_word,
            hints=[
                "Proper: numerator is smaller than the denominator.",
                "Whole: numerator is an exact multiple of the denominator (no remainder).",
                "Improper (strict): numerator is larger than the denominator but not an exact multiple.",
            ],
            solution_steps_latex=[
                f"Compare numerator ${n}$ with denominator ${d}$.",
                f"Check whether ${n}$ is divisible by ${d}$: ${n} \\div {d}$ leaves a remainder of ${n % d}$.",
                classification_sentence,
            ],
            tags=_TAGS_REASONING + [f"#difficulty-{difficulty}"],
        )
