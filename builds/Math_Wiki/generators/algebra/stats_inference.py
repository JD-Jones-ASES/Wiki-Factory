"""Statistical inference generators (Wave D algebra gap topics).

Topic slugs covered:
- ``margin_of_error_and_confidence_intervals``
  * margin_of_error_interval_construct
  * margin_of_error_interpret_claim
  * margin_of_error_shrink_with_sample_size
- ``sampling_methods_and_bias``
  * sampling_classify_method
  * sampling_identify_bias_source
  * sampling_generalizability_check
"""
from __future__ import annotations

import math
import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


# ---------------------------------------------------------------------------
# Topic: margin_of_error_and_confidence_intervals
# ---------------------------------------------------------------------------


_MOE_CONTEXTS: tuple[dict, ...] = (
    {
        "scenario": (
            "Maya polled a random sample of 500 high-school students about "
            "whether they prefer e-books over printed books"
        ),
        "quantity": "the proportion of students who prefer e-books",
    },
    {
        "scenario": (
            "Kai surveyed a random sample of 800 city residents about "
            "whether they bike to work"
        ),
        "quantity": "the proportion of residents who bike to work",
    },
    {
        "scenario": (
            "Priya surveyed a random sample of 300 gym members about "
            "whether they attend yoga classes"
        ),
        "quantity": "the proportion of members who attend yoga",
    },
    {
        "scenario": (
            "Rohan collected data from a random sample of 600 farmers about "
            "whether they plant cover crops in the winter"
        ),
        "quantity": "the proportion of farmers who plant cover crops",
    },
    {
        "scenario": (
            "Zoe surveyed a random sample of 450 college students about "
            "whether they work a part-time job"
        ),
        "quantity": "the proportion of students with a part-time job",
    },
    {
        "scenario": (
            "Mateo interviewed a random sample of 350 festival attendees "
            "about whether they bought food at the event"
        ),
        "quantity": "the proportion of attendees who bought food",
    },
    {
        "scenario": (
            "Leilani tracked a random sample of 250 library card holders "
            "to see whether they had used the e-audiobook service"
        ),
        "quantity": "the proportion of card holders using e-audiobooks",
    },
    {
        "scenario": (
            "Emilia polled a random sample of 700 grocery shoppers about "
            "whether they brought reusable bags"
        ),
        "quantity": "the proportion of shoppers with reusable bags",
    },
)


@register
class MarginOfErrorIntervalConstruct(Generator):
    """Given p-hat and margin m, write the confidence interval."""
    generator_id = "margin_of_error_interval_construct"
    topic_slug = "margin_of_error_and_confidence_intervals"
    display_name = "Construct a confidence interval from p-hat and margin"

    _P_RANGE = {"easy": (30, 70), "medium": (20, 80), "hard": (10, 90)}
    _M_RANGE = {"easy": (2, 6), "medium": (1, 8), "hard": (1, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_MOE_CONTEXTS)

        p_lo, p_hi = self._P_RANGE[difficulty]
        m_lo, m_hi = self._M_RANGE[difficulty]

        # p_hat as an integer percent; interval stays within [0, 100]
        p_hat_pct = rng.randint(p_lo, p_hi)
        m_pct = rng.randint(m_lo, m_hi)
        # Make sure we don't cross the 0 or 100 boundary
        while p_hat_pct - m_pct < 0 or p_hat_pct + m_pct > 100:
            p_hat_pct = rng.randint(p_lo, p_hi)
            m_pct = rng.randint(m_lo, m_hi)

        lower = p_hat_pct - m_pct
        upper = p_hat_pct + m_pct

        p_hat_frac = p_hat_pct / 100
        m_frac = m_pct / 100
        lower_frac = lower / 100
        upper_frac = upper / 100

        statement = (
            f"{ctx['scenario']}. The sample proportion is "
            f"$\\hat p = {p_hat_frac:.2f}$, and the margin of error is "
            f"$m = {m_frac:.2f}$. Write a confidence interval for "
            f"{ctx['quantity']}."
        )

        answer = f"$({lower_frac:.2f},\\ {upper_frac:.2f})$"

        key = (ctx["scenario"][:12], p_hat_pct, m_pct)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"A confidence interval built from a sample proportion "
                    r"and a margin of error has the form "
                    r"$(\hat p - m,\ \hat p + m)$."
                ),
                (
                    f"Subtract the margin from $\\hat p$ to get the lower "
                    f"bound, and add it to get the upper bound."
                ),
            ],
            solution_steps_latex=[
                rf"Write the interval formula: $(\hat p - m,\ \hat p + m)$.",
                (
                    rf"Substitute $\hat p = {p_hat_frac:.2f}$ and "
                    rf"$m = {m_frac:.2f}$: $({p_hat_frac:.2f} - {m_frac:.2f},"
                    rf"\ {p_hat_frac:.2f} + {m_frac:.2f})$."
                ),
                f"Simplify to get $({lower_frac:.2f},\\ {upper_frac:.2f})$.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-statistics",
                "#skill-formula-substitution",
            ],
        )


@register
class MarginOfErrorInterpretClaim(Generator):
    """Given a claim and a confidence interval, decide if the claim is consistent."""
    generator_id = "margin_of_error_interpret_claim"
    topic_slug = "margin_of_error_and_confidence_intervals"
    display_name = "Check whether a claim is consistent with a confidence interval"

    _P_RANGE = {"easy": (30, 70), "medium": (20, 80), "hard": (10, 90)}
    _M_RANGE = {"easy": (3, 7), "medium": (2, 8), "hard": (2, 10)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        ctx = rng.choice(_MOE_CONTEXTS)

        p_lo, p_hi = self._P_RANGE[difficulty]
        m_lo, m_hi = self._M_RANGE[difficulty]

        p_hat_pct = rng.randint(p_lo, p_hi)
        m_pct = rng.randint(m_lo, m_hi)
        while p_hat_pct - m_pct < 0 or p_hat_pct + m_pct > 100:
            p_hat_pct = rng.randint(p_lo, p_hi)
            m_pct = rng.randint(m_lo, m_hi)

        lower = p_hat_pct - m_pct
        upper = p_hat_pct + m_pct

        # Pick a claimed value: half the time inside, half outside.
        inside = rng.random() < 0.5
        if inside:
            claim_pct = rng.randint(lower, upper)
            consistent = True
            verdict = "Yes, the claim is consistent with the interval."
        else:
            # Pick outside by an honest margin
            if rng.random() < 0.5:
                claim_pct = max(0, lower - rng.randint(1, 5))
                if claim_pct >= lower:
                    claim_pct = max(0, lower - 1)
            else:
                claim_pct = min(100, upper + rng.randint(1, 5))
                if claim_pct <= upper:
                    claim_pct = min(100, upper + 1)
            consistent = (lower <= claim_pct <= upper)
            if consistent:
                verdict = "Yes, the claim is consistent with the interval."
            else:
                verdict = "No, the claim is not consistent with the interval."

        lower_f = lower / 100
        upper_f = upper / 100
        claim_f = claim_pct / 100

        statement = (
            f"{ctx['scenario']}. Based on the sample, a confidence interval "
            f"for {ctx['quantity']} is $({lower_f:.2f},\\ {upper_f:.2f})$. "
            f"A researcher claims the true proportion is ${claim_f:.2f}$. "
            "Is this claim consistent with the confidence interval? "
            "Answer yes or no."
        )

        if consistent:
            explanation = (
                f"The claimed value ${claim_f:.2f}$ lies between ${lower_f:.2f}$ "
                f"and ${upper_f:.2f}$, so the interval does not contradict the "
                "claim."
            )
        else:
            explanation = (
                f"The claimed value ${claim_f:.2f}$ does not lie between "
                f"${lower_f:.2f}$ and ${upper_f:.2f}$, so the interval is not "
                "consistent with the claim."
            )

        key = (ctx["scenario"][:12], p_hat_pct, m_pct, claim_pct)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=verdict,
            hints=[
                (
                    "A claim is consistent with a confidence interval when "
                    "the claimed value lies inside the interval."
                ),
                (
                    f"Check whether ${claim_f:.2f}$ falls between "
                    f"${lower_f:.2f}$ and ${upper_f:.2f}$."
                ),
            ],
            solution_steps_latex=[
                f"Identify the claimed value: ${claim_f:.2f}$.",
                (
                    f"Identify the confidence interval: "
                    f"$({lower_f:.2f},\\ {upper_f:.2f})$."
                ),
                (
                    f"Check whether ${claim_f:.2f}$ is in the interval: "
                    f"${lower_f:.2f} \\le {claim_f:.2f} \\le {upper_f:.2f}$ "
                    f"is {'true' if consistent else 'false'}."
                ),
                explanation,
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-statistics",
                "#skill-multi-step",
            ],
        )


@register
class MarginOfErrorShrinkWithSampleSize(Generator):
    """Qualitative: new margin after scaling sample size.

    The margin of error scales like $1/\\sqrt{n}$. Multiplying $n$ by $k$
    multiplies the margin by $1/\\sqrt{k}$.
    """
    generator_id = "margin_of_error_shrink_with_sample_size"
    topic_slug = "margin_of_error_and_confidence_intervals"
    display_name = "Find the new margin after scaling the sample size"
    bank_count_per_difficulty = 15

    _N_CHOICES = (200, 300, 400, 500, 600, 800, 1000)
    _M_CHOICES = (2, 3, 4, 5, 6, 8)
    # k values: 2 (doubling), 4 (quadrupling), 9 (9x), 16 (16x)
    _K_CHOICES = (2, 4, 9, 16)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        n_old = rng.choice(self._N_CHOICES)
        m_old_pct = rng.choice(self._M_CHOICES)
        k = rng.choice(self._K_CHOICES)

        # New margin = m_old / sqrt(k). We choose k values so sqrt(k) is clean.
        scale = 1 / math.sqrt(k)
        m_new_pct = m_old_pct * scale  # could be non-integer decimal

        n_new = n_old * k

        # Round to two decimals
        m_old_frac = m_old_pct / 100
        m_new_frac = m_new_pct / 100

        statement = (
            f"A survey of $n = {n_old}$ people produced a margin of error of "
            f"${m_old_frac:.2f}$ for a population proportion. Suppose a new "
            f"survey uses the same methodology but with a sample of "
            f"${n_new}$ people ($n$ is multiplied by ${k}$). The margin of "
            f"error scales like $\\dfrac{{1}}{{\\sqrt n}}$. Approximate the "
            "new margin of error, rounded to two decimal places."
        )

        answer = f"$\\approx {m_new_frac:.2f}$"

        key = (n_old, m_old_pct, k)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Because the margin of error is proportional to "
                    r"$\dfrac{1}{\sqrt n}$, multiplying $n$ by $k$ multiplies "
                    r"the margin by $\dfrac{1}{\sqrt k}$."
                ),
                (
                    f"Here $k = {k}$, so divide the old margin by "
                    f"$\\sqrt{{{k}}} = {math.sqrt(k):.4g}$."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Start with the old margin $m_{{\text{{old}}}} = "
                    rf"{m_old_frac:.2f}$ and the scaling factor $k = {k}$."
                ),
                (
                    rf"Apply the rule: $m_{{\text{{new}}}} = "
                    rf"\dfrac{{m_{{\text{{old}}}}}}{{\sqrt k}} = "
                    rf"\dfrac{{{m_old_frac:.2f}}}{{\sqrt{{{k}}}}}$."
                ),
                (
                    rf"Compute $\sqrt{{{k}}} = {math.sqrt(k):.4g}$, so "
                    rf"$m_{{\text{{new}}}} \approx {m_new_frac:.2f}$."
                ),
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-statistics",
                "#skill-estimation",
            ],
        )


# ---------------------------------------------------------------------------
# Topic: sampling_methods_and_bias
# ---------------------------------------------------------------------------


_SAMPLING_METHOD_CASES: tuple[dict, ...] = (
    # Simple random
    {
        "method": "simple random",
        "scenario": (
            "Maya assigns each of the 1000 members of a community center a "
            "unique ID number and uses a random number generator to select "
            "80 IDs for a survey"
        ),
        "rationale": (
            "every member has the same chance of being chosen, and the "
            "selection is made by random draw from the complete list"
        ),
    },
    {
        "method": "simple random",
        "scenario": (
            "Kai places all 240 employee names in a drum, mixes them "
            "thoroughly, and draws 30 at random"
        ),
        "rationale": (
            "every employee has an equal chance of being drawn and the "
            "selection uses a single random process"
        ),
    },
    {
        "method": "simple random",
        "scenario": (
            "Priya uses a spreadsheet function to pick 25 students at "
            "random from a complete roster of 400 seventh graders"
        ),
        "rationale": (
            "each student is equally likely and the choice is made by a "
            "single random function over the whole list"
        ),
    },
    # Stratified
    {
        "method": "stratified",
        "scenario": (
            "Rohan divides 600 marathon runners into three groups by age "
            "(teen, adult, senior) and randomly picks 10 runners from each "
            "age group"
        ),
        "rationale": (
            "the population is first split into non-overlapping subgroups "
            "(strata), then random samples are drawn from each subgroup"
        ),
    },
    {
        "method": "stratified",
        "scenario": (
            "Zoe separates a 450-student school into four grade levels and "
            "then randomly selects 20 students from each grade"
        ),
        "rationale": (
            "the population is broken into grade-level strata and a random "
            "sample is taken from each stratum"
        ),
    },
    # Cluster
    {
        "method": "cluster",
        "scenario": (
            "Mateo randomly picks 5 of the 40 third-grade classrooms in a "
            "district and surveys every student in those chosen classrooms"
        ),
        "rationale": (
            "the population is grouped into natural clusters (classrooms), "
            "a few clusters are chosen at random, and every member of the "
            "chosen clusters is included"
        ),
    },
    {
        "method": "cluster",
        "scenario": (
            "Leilani randomly chooses 3 apartment buildings from a list of "
            "50 in a city and interviews every resident of those buildings"
        ),
        "rationale": (
            "the population splits into clusters (buildings), a few clusters "
            "are picked at random, and everyone in the chosen clusters is "
            "surveyed"
        ),
    },
    # Systematic
    {
        "method": "systematic",
        "scenario": (
            "Emilia stands at the entrance of a grocery store and surveys "
            "every 12th shopper who walks in"
        ),
        "rationale": (
            "a starting point is chosen and then every $k$th individual is "
            "selected on a fixed interval, rather than by a fresh random draw"
        ),
    },
    {
        "method": "systematic",
        "scenario": (
            "Maya picks every 10th name on an alphabetical list of 500 "
            "gym members for a survey"
        ),
        "rationale": (
            "members are selected at a fixed interval from an ordered list"
        ),
    },
    # Convenience
    {
        "method": "convenience",
        "scenario": (
            "Kai asks the first 50 students who happen to walk past the "
            "library to complete a short questionnaire"
        ),
        "rationale": (
            "the sample consists of whoever is easiest to reach rather than "
            "a randomly selected group"
        ),
    },
    {
        "method": "convenience",
        "scenario": (
            "Priya surveys her own friends and teammates about their "
            "reading habits"
        ),
        "rationale": (
            "the respondents are selected because they are easy to reach, "
            "not by any random process"
        ),
    },
    {
        "method": "convenience",
        "scenario": (
            "Rohan polls people who respond to a flyer posted outside his "
            "classroom about their lunch preferences"
        ),
        "rationale": (
            "the sample is made up of whoever self-selects, not a randomly "
            "drawn group"
        ),
    },
    # Extra cases to support bank_count_per_difficulty = 15
    {
        "method": "stratified",
        "scenario": (
            "Emilia divides a town into three neighborhoods and randomly "
            "selects 40 households from each neighborhood"
        ),
        "rationale": (
            "the town is partitioned into neighborhood strata and a random "
            "sample is taken from each"
        ),
    },
    {
        "method": "systematic",
        "scenario": (
            "Leilani selects every 8th customer who enters a food truck "
            "between noon and 2 PM for a short taste test"
        ),
        "rationale": (
            "customers are chosen at a fixed interval from the arrival "
            "order, not by a fresh random draw"
        ),
    },
    {
        "method": "cluster",
        "scenario": (
            "Zoe randomly picks 4 of the 25 after-school dance studios in "
            "the district and surveys every student enrolled in those four "
            "studios"
        ),
        "rationale": (
            "the population is split into clusters (dance studios), a few "
            "clusters are randomly chosen, and every member of the chosen "
            "clusters is surveyed"
        ),
    },
    {
        "method": "simple random",
        "scenario": (
            "Mateo uses a random draw from a complete list of 1200 "
            "subscribers to choose 50 for a focus group"
        ),
        "rationale": (
            "the whole list is available and selections are made by a "
            "single random draw"
        ),
    },
)

_SAMPLING_METHOD_OPTIONS = (
    "simple random",
    "stratified",
    "cluster",
    "systematic",
    "convenience",
)


@register
class SamplingClassifyMethod(Generator):
    """Identify the sampling method used in a scenario."""
    generator_id = "sampling_classify_method"
    topic_slug = "sampling_methods_and_bias"
    display_name = "Classify a described sampling method"
    bank_count_per_difficulty = 15

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(_SAMPLING_METHOD_CASES)
        method = case["method"]

        # Build the options in a stable display order.
        options_text = " | ".join(_SAMPLING_METHOD_OPTIONS)

        key = (case["scenario"][:30], method)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{case['scenario']}. Which sampling method best describes "
                f"this procedure? Choose one: {options_text}."
            ),
            answer_latex=method,
            hints=[
                (
                    "Simple random = equal chance for everyone by direct "
                    "random draw. Stratified = split into subgroups first, "
                    "then randomly sample within each. Cluster = randomly "
                    "pick whole groups, include everyone in those groups. "
                    "Systematic = pick every $k$th person from a list. "
                    "Convenience = whoever is easy to reach."
                ),
                f"Look for the key phrase: {case['rationale']}.",
            ],
            solution_steps_latex=[
                (
                    "Match each sampling method's definition to the "
                    "described procedure."
                ),
                f"Here, {case['rationale']}.",
                f"Therefore, this is a {method} sample.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-statistics",
                "#word-problem-support",
            ],
        )


# ---------------------------------------------------------------------------


_BIAS_CASES: tuple[dict, ...] = (
    {
        "scenario": (
            "Maya wants to estimate how many teens read for fun, so she "
            "surveys only the students who show up to a book club meeting"
        ),
        "bias": "selection",
        "rationale": (
            "she sampled a group already expected to like reading, so her "
            "sample is not representative of all teens"
        ),
    },
    {
        "scenario": (
            "Kai asks, \"Don't you agree that loud music ruins the park "
            "experience?\" when polling people about park rules"
        ),
        "bias": "response",
        "rationale": (
            "the question is worded to push respondents toward a particular "
            "answer, distorting their true opinions"
        ),
    },
    {
        "scenario": (
            "Priya mails 1000 surveys about local grocery prices, and only "
            "the 120 angriest customers return the forms"
        ),
        "bias": "non-response",
        "rationale": (
            "most of the chosen sample never answered, so the data reflects "
            "only the highly motivated subgroup"
        ),
    },
    {
        "scenario": (
            "Rohan tries to measure the average age of adults in his city "
            "by calling numbers in an old landline phone book"
        ),
        "bias": "sampling frame",
        "rationale": (
            "the list of people he can even reach (the sampling frame) "
            "excludes mobile-only households, skewing the sample"
        ),
    },
    {
        "scenario": (
            "Zoe posts an online poll about school uniforms on a club "
            "website and accepts only replies from club members"
        ),
        "bias": "selection",
        "rationale": (
            "only a narrow subgroup can respond, so the sample is not "
            "representative of the whole school"
        ),
    },
    {
        "scenario": (
            "Mateo asks, \"Wouldn't you rather see our team win the "
            "championship with more practice hours?\" when polling parents"
        ),
        "bias": "response",
        "rationale": (
            "the leading wording biases respondents toward one answer"
        ),
    },
    {
        "scenario": (
            "Leilani emails 500 members of an alumni association, but only "
            "45 of them respond to her survey"
        ),
        "bias": "non-response",
        "rationale": (
            "the vast majority did not respond, so only a small self-selected "
            "group's views are captured"
        ),
    },
    {
        "scenario": (
            "Emilia wants to learn about all city commuters but her list "
            "comes only from the bus pass registry, leaving out drivers, "
            "bikers, and walkers"
        ),
        "bias": "sampling frame",
        "rationale": (
            "the sampling frame (the list of people who could be selected) "
            "misses entire groups of commuters"
        ),
    },
    {
        "scenario": (
            "Maya surveys only students who stay after school, then claims "
            "her results describe all students"
        ),
        "bias": "selection",
        "rationale": (
            "the sampled group is not representative of the whole student "
            "body, so the selection itself is biased"
        ),
    },
    {
        "scenario": (
            "Kai sends a public-opinion poll, but only 10 of the 400 "
            "recipients fill it out"
        ),
        "bias": "non-response",
        "rationale": (
            "the responses come from a tiny, self-selected portion of the "
            "intended sample"
        ),
    },
    {
        "scenario": (
            "Priya asks, \"Most responsible citizens vote. Do you vote?\" "
            "when polling voting habits"
        ),
        "bias": "response",
        "rationale": (
            "the wording pressures respondents toward agreeing, skewing "
            "their answers"
        ),
    },
    {
        "scenario": (
            "Rohan draws his random sample from a directory that lists "
            "only homeowners, but wants to generalize to all residents"
        ),
        "bias": "sampling frame",
        "rationale": (
            "renters are excluded from the sampling frame, so the eligible "
            "list does not match the target population"
        ),
    },
)

_BIAS_OPTIONS = ("selection", "response", "non-response", "sampling frame")


@register
class SamplingIdentifyBiasSource(Generator):
    """Identify the most likely source of bias in a scenario."""
    generator_id = "sampling_identify_bias_source"
    topic_slug = "sampling_methods_and_bias"
    display_name = "Identify the source of sampling bias"
    bank_count_per_difficulty = 12

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(_BIAS_CASES)
        bias = case["bias"]

        options_text = " | ".join(_BIAS_OPTIONS)
        key = (case["scenario"][:30], bias)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=(
                f"{case['scenario']}. Which type of bias is most likely "
                f"affecting this survey? Choose one: {options_text}."
            ),
            answer_latex=f"{bias} bias",
            hints=[
                (
                    "Selection bias = who you pick is already slanted. "
                    "Response bias = the way you ask distorts answers. "
                    "Non-response bias = most chosen people don't answer. "
                    "Sampling frame bias = your list of possible respondents "
                    "is missing part of the population."
                ),
                f"Key clue: {case['rationale']}.",
            ],
            solution_steps_latex=[
                (
                    "Consider the four main types of sampling bias and "
                    "match the scenario to the closest fit."
                ),
                f"Here, {case['rationale']}.",
                f"So the best answer is {bias} bias.",
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-statistics",
                "#word-problem-support",
            ],
        )


# ---------------------------------------------------------------------------


_GENERALIZABILITY_CASES: tuple[dict, ...] = (
    {
        "scenario": (
            "Maya randomly selects 200 middle-school students from all "
            "eight middle schools in her district"
        ),
        "conclusion": (
            "Her conclusions describe middle-school students in her "
            "district."
        ),
        "answer": "yes",
        "rationale": (
            "the sample was randomly drawn from the full target population "
            "of district middle schoolers"
        ),
    },
    {
        "scenario": (
            "Kai surveys only members of his chess club"
        ),
        "conclusion": (
            "He uses the results to draw conclusions about all students at "
            "his high school."
        ),
        "answer": "no",
        "rationale": (
            "chess club members are not representative of the whole student "
            "body, so his sample is not generalizable"
        ),
    },
    {
        "scenario": (
            "Priya takes a stratified random sample of library members by "
            "age group"
        ),
        "conclusion": (
            "She draws conclusions about all library members in the city."
        ),
        "answer": "yes",
        "rationale": (
            "a stratified random sample from all age groups should "
            "generalize to the city library's members"
        ),
    },
    {
        "scenario": (
            "Rohan polls only the people in line for a popular rock "
            "concert"
        ),
        "conclusion": (
            "He uses the responses to describe music preferences of people "
            "in the whole city."
        ),
        "answer": "no",
        "rationale": (
            "concert-goers are a self-selected group of rock fans, not a "
            "representative cross-section of the city"
        ),
    },
    {
        "scenario": (
            "Zoe randomly selects 150 of the 900 families enrolled in a "
            "neighborhood youth program"
        ),
        "conclusion": (
            "She makes claims about families in that program."
        ),
        "answer": "yes",
        "rationale": (
            "the sample was random and drawn from the exact target "
            "population she is describing"
        ),
    },
    {
        "scenario": (
            "Mateo asks only adults who happen to be at the downtown "
            "coffee shop on a Monday morning"
        ),
        "conclusion": (
            "He claims his results describe the opinions of all adults in "
            "the city."
        ),
        "answer": "no",
        "rationale": (
            "Monday-morning coffee-shop visitors are a convenience sample, "
            "not representative of all adults"
        ),
    },
    {
        "scenario": (
            "Leilani uses a random number generator to pick 75 of the 500 "
            "seventh graders at her school"
        ),
        "conclusion": (
            "She draws conclusions about seventh graders at her school."
        ),
        "answer": "yes",
        "rationale": (
            "a simple random sample from the full target population "
            "supports a generalization to that population"
        ),
    },
    {
        "scenario": (
            "Emilia surveys only the students in her own class period"
        ),
        "conclusion": (
            "She uses the data to describe the average study habits of all "
            "students in the district."
        ),
        "answer": "no",
        "rationale": (
            "one class is not a random or representative sample of the "
            "whole district"
        ),
    },
    {
        "scenario": (
            "Maya randomly picks 50 shoppers from a complete shopper "
            "registry at a single store"
        ),
        "conclusion": (
            "She claims her results describe shoppers at that store."
        ),
        "answer": "yes",
        "rationale": (
            "the sample is random and drawn from the target population "
            "(shoppers at that store)"
        ),
    },
    {
        "scenario": (
            "Kai polls 30 people who volunteered to take an online poll "
            "about school food"
        ),
        "conclusion": (
            "He uses the results to describe the views of all students."
        ),
        "answer": "no",
        "rationale": (
            "voluntary response samples tend to over-represent people with "
            "strong opinions and do not generalize well"
        ),
    },
    {
        "scenario": (
            "Priya randomly selects 5 of the 20 classrooms in a school "
            "and surveys every student in each selected classroom"
        ),
        "conclusion": (
            "She draws conclusions about students in that school."
        ),
        "answer": "yes",
        "rationale": (
            "a properly executed cluster sample with randomly chosen "
            "classrooms can generalize to the school"
        ),
    },
    {
        "scenario": (
            "Rohan interviews only senior citizens at a retirement home"
        ),
        "conclusion": (
            "He claims his findings apply to all adults in the country."
        ),
        "answer": "no",
        "rationale": (
            "one narrow age group at one location is not representative of "
            "the national adult population"
        ),
    },
)


@register
class SamplingGeneralizabilityCheck(Generator):
    """Decide whether a sample's conclusion can be generalized."""
    generator_id = "sampling_generalizability_check"
    topic_slug = "sampling_methods_and_bias"
    display_name = "Decide whether results can be generalized"
    bank_count_per_difficulty = 12

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        case = rng.choice(_GENERALIZABILITY_CASES)
        answer = case["answer"]
        verdict = (
            "Yes, the conclusion can reasonably be generalized."
            if answer == "yes"
            else "No, the conclusion cannot reasonably be generalized."
        )

        statement = (
            f"{case['scenario']}. {case['conclusion']} Can these findings "
            "be reasonably generalized to the described population? Answer "
            "yes or no."
        )

        key = (case["scenario"][:30], answer)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, key),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=verdict,
            hints=[
                (
                    "A sample's results can be generalized when the sample "
                    "is random AND drawn from the same population the "
                    "conclusion targets."
                ),
                (
                    "Ask: is the sampling procedure random? And does the "
                    "sampled group match the population the conclusion "
                    "is about?"
                ),
            ],
            solution_steps_latex=[
                (
                    "Compare the sampling method and the described "
                    "population to the population in the conclusion."
                ),
                f"Here, {case['rationale']}.",
                verdict,
            ],
            tags=[
                "#branch-algebra-2",
                "#topic-statistics",
                "#skill-multi-step",
            ],
        )
