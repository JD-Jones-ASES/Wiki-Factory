"""Triangle congruence generators (Cluster 10).

Topic slug: ``triangle_congruence_criteria``.

Five generators:

- triangle_congruence_identify_criterion: given matching parts, pick SSS/SAS/ASA/AAS/HL
- triangle_congruence_find_missing_side: SAS-congruent triangles, find unknown side
- triangle_congruence_find_missing_angle: ASA-congruent triangles, find unknown angle
- triangle_congruence_not_congruent: AAA or SSA setup; explain why not congruent
- triangle_congruence_proof_step: pick the next justification in a short proof
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "triangle_congruence_criteria"

_CRITERIA = ("SSS", "SAS", "ASA", "AAS", "HL")

_CRITERION_DESCRIPTIONS = {
    "SSS": "three pairs of corresponding sides are congruent",
    "SAS": "two pairs of corresponding sides and the included angle are congruent",
    "ASA": "two pairs of corresponding angles and the included side are congruent",
    "AAS": "two pairs of corresponding angles and a non-included side are congruent",
    "HL": "in right triangles, the hypotenuse and one leg are congruent",
}


# ---------------------------------------------------------------------------

@register
class TriangleCongruenceIdentifyCriterion(Generator):
    """Given a description of matching parts, pick the congruence criterion."""
    generator_id = "triangle_congruence_identify_criterion"
    topic_slug = TOPIC_SLUG
    display_name = "Identify the triangle congruence criterion"
    bank_count_per_difficulty = 18

    _SCENARIOS = {
        "SSS": "all three pairs of sides of the two triangles are marked congruent",
        "SAS": "two pairs of sides and the angle between them (the included angle) are marked congruent",
        "ASA": "two pairs of angles and the side between them (the included side) are marked congruent",
        "AAS": "two pairs of angles and a side that is not between them are marked congruent",
        "HL": "both triangles contain a right angle, and the hypotenuse plus one leg are marked congruent",
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        criterion = rng.choice(_CRITERIA)
        description = self._SCENARIOS[criterion]
        # Add a distinguishing triangle label for uniqueness
        label_a = rng.choice(["ABC", "PQR", "XYZ", "LMN", "JKL", "DEF", "UVW", "GHI"])
        label_b = rng.choice(["DEF", "STU", "GHI", "RST", "MNO", "PQR", "ABC", "XYZ"])
        while label_b == label_a:
            label_b = rng.choice(["DEF", "STU", "GHI", "RST", "MNO", "PQR", "ABC", "XYZ"])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (criterion, label_a, label_b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In triangles $\\triangle {label_a}$ and $\\triangle {label_b}$, {description}. "
                f"Determine which congruence criterion proves the triangles congruent. "
                f"Choose from: SSS, SAS, ASA, AAS, HL."
            ),
            answer_latex=f"${criterion}$",
            hints=[
                r"SSS = three sides; SAS = two sides + included angle; ASA = two angles + included side; AAS = two angles + non-included side; HL = right triangles, hypotenuse and a leg.",
                "Focus on whether the congruent angle is **between** the two congruent sides (SAS) or whether the congruent side is **between** the two congruent angles (ASA).",
                f"Here the given matching parts point to the {criterion} criterion.",
            ],
            solution_steps_latex=[
                f"Read the description: {description}.",
                f"Match this pattern to one of the five congruence criteria.",
                f"The pattern matches ${criterion}$ because {_CRITERION_DESCRIPTIONS[criterion]}.",
            ],
            tags=["#branch-geometry", "#topic-similarity-and-congruence", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class TriangleCongruenceMissingSide(Generator):
    """Two triangles congruent by SAS; find the missing corresponding side."""
    generator_id = "triangle_congruence_find_missing_side"
    topic_slug = TOPIC_SLUG
    display_name = "Find missing side in congruent triangles (SAS)"
    bank_count_per_difficulty = 18

    _RANGES = {"easy": (3, 15), "medium": (5, 30), "hard": (6, 50)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        side_ab = rng.randint(lo, hi)
        side_ac = rng.randint(lo, hi)
        while side_ac == side_ab:
            side_ac = rng.randint(lo, hi)
        # Included angle measure
        angle = rng.choice([30, 45, 60, 75, 90, 105, 120])
        # Which side is asked about?
        ask_side = rng.choice(["DE", "DF"])
        if ask_side == "DE":
            answer = side_ab
            given_side = side_ac
            given_letters = "DF"
        else:
            answer = side_ac
            given_side = side_ab
            given_letters = "DE"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (side_ab, side_ac, angle, ask_side)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Triangles $\\triangle ABC$ and $\\triangle DEF$ are congruent by SAS. "
                f"$AB = {side_ab}$, $AC = {side_ac}$, $\\angle A = {angle}^\\circ$, "
                f"and ${given_letters} = {given_side}$. Determine the length of ${ask_side}$."
            ),
            answer_latex=f"${ask_side} = {answer}$",
            hints=[
                "When two triangles are congruent, corresponding parts are congruent (CPCTC).",
                "Match up the corresponding vertices: $A \\leftrightarrow D$, $B \\leftrightarrow E$, $C \\leftrightarrow F$.",
                f"So ${ask_side}$ corresponds to ${'AB' if ask_side == 'DE' else 'AC'}$.",
            ],
            solution_steps_latex=[
                r"Apply CPCTC (Corresponding Parts of Congruent Triangles are Congruent).",
                f"Since $\\triangle ABC \\cong \\triangle DEF$, matching the vertices in order: "
                f"$A \\leftrightarrow D$, $B \\leftrightarrow E$, $C \\leftrightarrow F$.",
                f"The side ${ask_side}$ corresponds to ${'AB' if ask_side == 'DE' else 'AC'} = {answer}$.",
                f"Therefore ${ask_side} = {answer}$.",
            ],
            tags=["#branch-geometry", "#topic-similarity-and-congruence", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class TriangleCongruenceMissingAngle(Generator):
    """Two triangles congruent by ASA; find the missing corresponding angle."""
    generator_id = "triangle_congruence_find_missing_angle"
    topic_slug = TOPIC_SLUG
    display_name = "Find missing angle in congruent triangles (ASA)"
    bank_count_per_difficulty = 18

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        # Pick two angles whose sum is less than 180
        angle_a = rng.randint(20, 80)
        angle_b = rng.randint(20, 160 - angle_a)
        angle_c = 180 - angle_a - angle_b
        ask = rng.choice(["D", "E", "F"])
        corr_map = {"D": ("A", angle_a), "E": ("B", angle_b), "F": ("C", angle_c)}
        corr_letter, answer = corr_map[ask]
        # Side length (any positive integer)
        side_len = rng.randint(5, 25)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (angle_a, angle_b, side_len, ask)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"Triangles $\\triangle ABC$ and $\\triangle DEF$ are congruent by ASA. "
                f"$\\angle A = {angle_a}^\\circ$, $\\angle B = {angle_b}^\\circ$, and "
                f"$AB = {side_len} = DE$. Determine the measure of $\\angle {ask}$."
            ),
            answer_latex=f"$\\angle {ask} = {answer}^\\circ$",
            hints=[
                "Corresponding angles of congruent triangles are congruent (CPCTC).",
                "Match vertices: $A \\leftrightarrow D$, $B \\leftrightarrow E$, $C \\leftrightarrow F$.",
                r"Use the triangle angle sum: $\angle A + \angle B + \angle C = 180^\circ$ to find any missing angle in $\triangle ABC$ first.",
            ],
            solution_steps_latex=[
                r"The three angles of $\triangle ABC$ sum to $180^\circ$:" +
                f" $\\angle A + \\angle B + \\angle C = {angle_a} + {angle_b} + \\angle C = 180$.",
                f"Solve for $\\angle C = {angle_c}^\\circ$.",
                f"By CPCTC, $\\angle {ask}$ in $\\triangle DEF$ corresponds to $\\angle {corr_letter}$ in $\\triangle ABC$.",
                f"Therefore $\\angle {ask} = {answer}^\\circ$.",
            ],
            tags=["#branch-geometry", "#topic-similarity-and-congruence", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class TriangleCongruenceNotCongruent(Generator):
    """Given AAA or SSA, explain why the triangles are not necessarily congruent."""
    generator_id = "triangle_congruence_not_congruent"
    topic_slug = TOPIC_SLUG
    display_name = "Explain why triangles are not necessarily congruent (AAA / SSA)"
    bank_count_per_difficulty = 18

    _SCENARIOS = [
        ("AAA",
         "three pairs of corresponding angles are congruent",
         "AAA does not guarantee congruence. Triangles with equal angles are similar but can differ in size (scale), so their corresponding sides need not match.",
        ),
        ("SSA",
         "two pairs of corresponding sides and a non-included angle are congruent",
         "SSA is the ambiguous case. Given two sides and a non-included angle, two distinct non-congruent triangles can sometimes be formed, so SSA is not a valid congruence criterion (except HL for right triangles).",
        ),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        tag, desc, explanation = rng.choice(self._SCENARIOS)
        label_a = rng.choice(["ABC", "PQR", "XYZ", "LMN", "JKL", "UVW", "GHI"])
        label_b = rng.choice(["DEF", "STU", "GHI", "RST", "MNO", "PQR"])
        while label_b == label_a:
            label_b = rng.choice(["DEF", "STU", "GHI", "RST", "MNO", "PQR"])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (tag, label_a, label_b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In triangles $\\triangle {label_a}$ and $\\triangle {label_b}$, {desc}. "
                f"Are the triangles necessarily congruent? Explain using the valid congruence criteria."
            ),
            answer_latex=f"No. {tag} is not a valid congruence criterion.",
            hints=[
                "The five valid criteria are SSS, SAS, ASA, AAS, and HL.",
                f"The given configuration ({tag}) is **not** on that list.",
                "Think about whether the given information locks in both the shape and the size.",
            ],
            solution_steps_latex=[
                f"Identify the given configuration: {desc}. This describes the pattern ${tag}$.",
                f"Check the valid criteria: SSS, SAS, ASA, AAS, HL. {tag} is not among them.",
                f"Explain: {explanation}",
                f"Conclude: the triangles are not necessarily congruent.",
            ],
            tags=["#branch-geometry", "#topic-similarity-and-congruence", "#skill-proof-reasoning"],
        )


# ---------------------------------------------------------------------------

@register
class TriangleCongruenceProofStep(Generator):
    """Pick the next justification in a short two-column congruence proof."""
    generator_id = "triangle_congruence_proof_step"
    topic_slug = TOPIC_SLUG
    display_name = "Pick the next justification in a triangle congruence proof"
    bank_count_per_difficulty = 18

    _STEP_SCENARIOS = [
        ("a shared side is used to establish one pair of sides congruent",
         "Reflexive Property of Congruence",
         "A segment is congruent to itself, so a shared side gives one pair of congruent sides for free."),
        ("vertical angles at an intersection are identified as congruent",
         "Vertical Angles Theorem",
         "Vertical angles (the opposite angles formed by intersecting lines) are always congruent."),
        ("two triangles share an angle at the apex",
         "Reflexive Property of Congruence",
         "The shared angle is congruent to itself."),
        ("segment AC is marked as a midpoint divider, so AM = MC",
         "Definition of Midpoint",
         "A midpoint divides a segment into two congruent halves."),
        ("AD bisects angle BAC so the two half-angles are congruent",
         "Definition of Angle Bisector",
         "An angle bisector splits an angle into two congruent angles."),
        ("parallel lines AB and CD are cut by transversal AC forming alternate interior angles",
         "Alternate Interior Angles Theorem",
         "When parallel lines are cut by a transversal, alternate interior angles are congruent."),
    ]

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        setup, theorem, explanation = rng.choice(self._STEP_SCENARIOS)
        label_a = rng.choice(["ABC", "PQR", "XYZ", "LMN", "JKL", "UVW"])
        label_b = rng.choice(["DEF", "STU", "GHI", "RST", "MNO"])

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (setup, theorem, label_a, label_b)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"In a proof that $\\triangle {label_a} \\cong \\triangle {label_b}$, {setup}. "
                f"Give the theorem or definition that justifies this step."
            ),
            answer_latex=f"{theorem}",
            hints=[
                "Common justifications include the Reflexive Property, Vertical Angles Theorem, definition of midpoint, definition of angle bisector, and the Alternate Interior Angles Theorem.",
                "Read the setup carefully and match it to the rule it describes.",
                f"The setup describes: {setup}.",
            ],
            solution_steps_latex=[
                f"Parse the setup: {setup}.",
                f"Match the setup to a known theorem or definition.",
                f"{theorem} applies because {explanation}",
                f"So the justification is: {theorem}.",
            ],
            tags=["#branch-geometry", "#topic-similarity-and-congruence", "#skill-proof-reasoning"],
        )
