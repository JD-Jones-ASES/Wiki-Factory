"""Set notation and the real numbers generators.

Canonical topic slug ``set_notation_and_the_real_numbers`` at
``wiki/topics/algebra/Set_Notation_And_The_Real_Numbers.md``.

Three generators:

- ``inequality_to_interval_notation``: given an inequality, rewrite it in
  interval notation (six flavors total).
- ``interval_notation_to_inequality``: the inverse conversion.
- ``classify_number_set_membership``: given a specific number, list which of
  natural / whole / integer / rational / irrational / real it belongs to.

``classify_number_set_membership`` uses a fixed scenario table, so it sets
``bank_count_per_difficulty = 12``. The conversion generators have a large
parameter space and rely on the default.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "set_notation_and_the_real_numbers"

_TAGS_CONVERT = [
    "#branch-algebra-2",
    "#topic-numbers-and-operations",
    "#skill-translation",
]
_TAGS_CLASSIFY = [
    "#branch-algebra-2",
    "#topic-numbers-and-operations",
    "#skill-visualization",
]


# ---------------------------------------------------------------------------

# Six inequality "forms" and their interval counterparts.
# (form_id, inequality_tex, interval_tex_template)
#
# Codes used for backward construction and problem-id determinism:
#   "both_closed":   a \le x \le b   -> [a, b]
#   "both_open":     a < x < b       -> (a, b)
#   "left_closed":   a \le x < b     -> [a, b)
#   "right_closed":  a < x \le b     -> (a, b]
#   "upper_ray_cl":  x \ge a         -> [a, \infty)
#   "upper_ray_op":  x > a           -> (a, \infty)
#   "lower_ray_cl":  x \le b         -> (-\infty, b]
#   "lower_ray_op":  x < b           -> (-\infty, b)
_BOUNDED_FORMS = ("both_closed", "both_open", "left_closed", "right_closed")
_RAY_FORMS = ("upper_ray_cl", "upper_ray_op", "lower_ray_cl", "lower_ray_op")
_ALL_FORMS = _BOUNDED_FORMS + _RAY_FORMS


def _format_inequality(form_id: str, a: int, b: int) -> str:
    """Render the LaTeX for the inequality form."""
    if form_id == "both_closed":
        return f"{a} \\le x \\le {b}"
    if form_id == "both_open":
        return f"{a} < x < {b}"
    if form_id == "left_closed":
        return f"{a} \\le x < {b}"
    if form_id == "right_closed":
        return f"{a} < x \\le {b}"
    if form_id == "upper_ray_cl":
        return f"x \\ge {a}"
    if form_id == "upper_ray_op":
        return f"x > {a}"
    if form_id == "lower_ray_cl":
        return f"x \\le {b}"
    if form_id == "lower_ray_op":
        return f"x < {b}"
    raise ValueError(f"unknown form_id: {form_id}")


def _format_interval(form_id: str, a: int, b: int) -> str:
    """Render the LaTeX interval notation for the given form."""
    if form_id == "both_closed":
        return f"[{a}, {b}]"
    if form_id == "both_open":
        return f"({a}, {b})"
    if form_id == "left_closed":
        return f"[{a}, {b})"
    if form_id == "right_closed":
        return f"({a}, {b}]"
    if form_id == "upper_ray_cl":
        return f"[{a}, \\infty)"
    if form_id == "upper_ray_op":
        return f"({a}, \\infty)"
    if form_id == "lower_ray_cl":
        return f"(-\\infty, {b}]"
    if form_id == "lower_ray_op":
        return f"(-\\infty, {b})"
    raise ValueError(f"unknown form_id: {form_id}")


def _form_endpoint_description(form_id: str) -> str:
    """One-line note on which endpoints are included / excluded."""
    if form_id == "both_closed":
        return "Both endpoints are included, so both brackets are square."
    if form_id == "both_open":
        return "Both endpoints are excluded, so both brackets are parentheses."
    if form_id == "left_closed":
        return "The left endpoint is included and the right endpoint is excluded."
    if form_id == "right_closed":
        return "The left endpoint is excluded and the right endpoint is included."
    if form_id == "upper_ray_cl":
        return "The left endpoint is included; the ray extends to positive infinity."
    if form_id == "upper_ray_op":
        return "The left endpoint is excluded; the ray extends to positive infinity."
    if form_id == "lower_ray_cl":
        return "The right endpoint is included; the ray extends to negative infinity."
    if form_id == "lower_ray_op":
        return "The right endpoint is excluded; the ray extends to negative infinity."
    raise ValueError(f"unknown form_id: {form_id}")


# ---------------------------------------------------------------------------

@register
class InequalityToIntervalNotation(Generator):
    """Given an inequality, rewrite it in interval notation."""
    generator_id = "inequality_to_interval_notation"
    topic_slug = TOPIC_SLUG
    display_name = "Convert inequality to interval notation"

    _RANGES = {
        "easy":   (-10, 10),
        "medium": (-20, 20),
        "hard":   (-50, 50),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        form_id = rng.choice(_ALL_FORMS)

        if form_id in _BOUNDED_FORMS:
            a = rng.randint(lo, hi - 2)
            offset = rng.randint(1, max(1, hi - a))
            b = a + offset
            # If b exceeds hi, clamp; keep a < b.
            if b > hi:
                b = hi
            if a >= b:
                a, b = b - 1, b
        else:
            a = rng.randint(lo, hi)
            b = a  # unused by rays, but keep value stable for the id

        ineq_latex = _format_inequality(form_id, a, b)
        interval_latex = _format_interval(form_id, a, b)
        note = _form_endpoint_description(form_id)

        statement = (
            f"Express the inequality ${ineq_latex}$ in interval notation."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (form_id, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${interval_latex}$",
            hints=[
                (
                    r"In interval notation, $[\,\cdot\,]$ marks a closed "
                    r"(included) endpoint and $(\,\cdot\,)$ marks an open "
                    r"(excluded) endpoint. Infinity is always written with "
                    r"a parenthesis because infinity is not a real number."
                ),
                (
                    r"A strict inequality ($<$ or $>$) corresponds to an "
                    r"open endpoint; a non-strict inequality ($\leq$ or "
                    r"$\geq$) corresponds to a closed endpoint."
                ),
                note,
            ],
            solution_steps_latex=[
                f"Read the inequality ${ineq_latex}$ and identify each endpoint.",
                note,
                f"Write the matching interval: ${interval_latex}$.",
            ],
            tags=list(_TAGS_CONVERT),
        )


# ---------------------------------------------------------------------------

@register
class IntervalNotationToInequality(Generator):
    """Given an interval, rewrite it as an inequality."""
    generator_id = "interval_notation_to_inequality"
    topic_slug = TOPIC_SLUG
    display_name = "Convert interval notation to inequality"

    _RANGES = {
        "easy":   (-10, 10),
        "medium": (-20, 20),
        "hard":   (-50, 50),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        form_id = rng.choice(_ALL_FORMS)

        if form_id in _BOUNDED_FORMS:
            a = rng.randint(lo, hi - 2)
            offset = rng.randint(1, max(1, hi - a))
            b = a + offset
            if b > hi:
                b = hi
            if a >= b:
                a, b = b - 1, b
        else:
            a = rng.randint(lo, hi)
            b = a

        ineq_latex = _format_inequality(form_id, a, b)
        interval_latex = _format_interval(form_id, a, b)
        note = _form_endpoint_description(form_id)

        statement = (
            f"Express the interval ${interval_latex}$ as an inequality in $x$."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (form_id, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${ineq_latex}$",
            hints=[
                (
                    r"A square bracket $[\,\cdot\,]$ corresponds to $\leq$ "
                    r"or $\geq$ (included endpoint). A parenthesis "
                    r"$(\,\cdot\,)$ corresponds to $<$ or $>$ (excluded endpoint)."
                ),
                (
                    r"$\pm\infty$ on either end of an interval drops out of "
                    r"the inequality and just becomes a one-sided bound on $x$."
                ),
                note,
            ],
            solution_steps_latex=[
                f"Read the interval ${interval_latex}$ from left to right.",
                note,
                f"Write the matching inequality: ${ineq_latex}$.",
            ],
            tags=list(_TAGS_CONVERT),
        )


# ---------------------------------------------------------------------------

# Hand-curated number list. Each entry is
#   (latex_number, membership_tuple, justification)
# where membership_tuple is a tuple of set-name strings in canonical
# ascending containment order: natural subset of whole subset of integer
# subset of rational subset of real; irrational is disjoint from rational
# but still subset of real.
#
# Canonical output order when rendering the answer:
#   natural, whole, integer, rational, irrational, real
_NUMBER_CLASSIFY: tuple[tuple[str, tuple[str, ...], str], ...] = (
    ("5",        ("natural", "whole", "integer", "rational", "real"),
     "$5$ is a counting number, so every containment set applies."),
    ("0",        ("whole", "integer", "rational", "real"),
     "$0$ is a whole number and an integer. It is rational (equal to $0/1$) and real, but not natural."),
    ("-7",       ("integer", "rational", "real"),
     "$-7$ is a negative integer; integers are rational and real."),
    (r"\dfrac{5}{3}",  ("rational", "real"),
     "A ratio of two integers is rational, hence real; it is not an integer."),
    (r"-\dfrac{11}{4}", ("rational", "real"),
     "A negative ratio of integers is still a rational real number."),
    ("0.75",     ("rational", "real"),
     "A terminating decimal equals $3/4$, a ratio of integers."),
    (r"0.\overline{6}", ("rational", "real"),
     "A repeating decimal equals a ratio of integers, so it is rational."),
    (r"\sqrt{2}", ("irrational", "real"),
     "$\\sqrt{2}$ cannot be written as a ratio of integers, so it is irrational and real."),
    (r"\sqrt{11}", ("irrational", "real"),
     "$\\sqrt{11}$ is irrational because $11$ is not a perfect square."),
    (r"\pi",     ("irrational", "real"),
     "$\\pi$ is a classic irrational constant."),
    (r"\sqrt{16}", ("natural", "whole", "integer", "rational", "real"),
     "$\\sqrt{16} = 4$, which is a natural number; every containment set applies."),
    (r"-\sqrt{3}", ("irrational", "real"),
     "The negative of an irrational number is still irrational and real."),
)


@register
class ClassifyNumberSet(Generator):
    """Given a specific number, list every set it belongs to.

    The parameter space is the fixed ``_NUMBER_CLASSIFY`` table with 12
    curated scenarios. Because the space is small, this generator sets
    ``bank_count_per_difficulty = 12``.
    """
    generator_id = "classify_number_set_membership"
    topic_slug = TOPIC_SLUG
    display_name = "Classify a number by set membership"
    bank_count_per_difficulty = 12

    _CANONICAL_ORDER = ("natural", "whole", "integer", "rational", "irrational", "real")

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        idx = rng.randint(0, len(_NUMBER_CLASSIFY) - 1)
        latex_num, membership, justification = _NUMBER_CLASSIFY[idx]

        # Render the membership list in canonical order.
        ordered = [s for s in self._CANONICAL_ORDER if s in membership]
        if len(ordered) == 1:
            list_phrase = ordered[0]
        elif len(ordered) == 2:
            list_phrase = f"{ordered[0]} and {ordered[1]}"
        else:
            list_phrase = ", ".join(ordered[:-1]) + f", and {ordered[-1]}"

        answer_latex = list_phrase

        statement = (
            f"Classify the number ${latex_num}$ as natural, whole, integer, "
            f"rational, irrational, or real. Select all that apply."
        )

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (idx,),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer_latex,
            hints=[
                (
                    "Natural numbers are the positive counting numbers "
                    "$\\{1, 2, 3, \\ldots\\}$. Whole numbers add zero. "
                    "Integers add the negatives."
                ),
                (
                    "A rational number can be written as a ratio of two "
                    "integers $p/q$ with $q \\ne 0$. Irrational numbers "
                    "cannot. Both sets are subsets of the real numbers."
                ),
                justification,
            ],
            solution_steps_latex=[
                f"Examine the number ${latex_num}$.",
                justification,
                f"The number belongs to: {list_phrase}.",
            ],
            tags=list(_TAGS_CLASSIFY),
        )
