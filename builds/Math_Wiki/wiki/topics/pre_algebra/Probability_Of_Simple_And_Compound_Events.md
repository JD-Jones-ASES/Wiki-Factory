---
title: "Probability of Simple and Compound Events"
type: topic
aliases: ["Probability", "Compound Probability", "Simple and Compound Events"]
tags: ["#branch-pre-algebra", "#topic-probability"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "9", section: "9.4"}
related:
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "Count favorable outcomes, divide by total outcomes, and use AND/OR rules for compound events."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Probability of Simple and Compound Events

# Probability of Simple and Compound Events

**Probability** is a number that measures how likely something is to happen. When every outcome of an experiment has the same chance of occurring, the probability of an event $E$ is the count of outcomes that would make $E$ true, divided by the total count of outcomes that could occur:

$$
P(E) = \dfrac{\text{(outcomes where } E \text{ happens)}}{\text{(all possible outcomes)}}
$$

Every probability is a number between $0$ and $1$. A probability of $0$ means the event cannot happen. A probability of $1$ means it is guaranteed. A probability of $1/2$ means the event is just as likely to happen as not. The scale is simply a fraction turned into a measurement of chance.

---

## Simple events versus compound events

A **simple event** is one outcome from one experiment — rolling a $4$ on a single die, pulling one card from a deck, landing on blue on one spin. You count favorable outcomes, count total outcomes, and write the fraction.

A **compound event** combines two or more events. Two new patterns appear here, and deciding which to use is the whole pedagogical point of this topic:

- If the events are linked by the word **AND** and neither one affects the other (flipping a coin and rolling a die — the coin doesn't care what the die does), the events are **independent**, and you *multiply* their probabilities:
  $$P(A \text{ and } B) = P(A) \cdot P(B)$$
- If the events are linked by the word **OR** and the two cannot both happen at once (rolling a $2$ or a $3$ — you can't roll both in one toss), the events are **mutually exclusive**, and you *add* their probabilities:
  $$P(A \text{ or } B) = P(A) + P(B)$$

**The shortcut:** AND usually means multiply, OR usually means add. Get that instinct wired in and compound events become routine arithmetic.

---

## The complement rule

Sometimes it is easier to count what you *don't* want than what you do. If $P(A)$ is the chance an event happens, then the chance it does not happen is

$$
P(\text{not } A) = 1 - P(A).
$$

This is the **complement rule**, and it often saves serious work. If the weather app says there is a $0.35$ chance of rain, the chance of a dry day is $1 - 0.35 = 0.65$.

---

## Example 1: a single roll of a die (simple event)

> A regular six-sided die is rolled once. How likely is it that the number showing is greater than $4$?

The outcomes greater than $4$ are $5$ and $6$, so there are $2$ favorable outcomes. There are $6$ total outcomes in all, since any of $1, 2, 3, 4, 5, 6$ could land face-up.

$$
P(\text{number} > 4) = \dfrac{2}{6} = \dfrac{1}{3}
$$

About one roll in three should land on a number bigger than $4$. Notice the final answer is reduced — probabilities written as fractions should always be in lowest terms.

---

## Example 2: two coin flips (AND, independent events)

> A fair coin is flipped two times in a row. What is the chance of getting heads on both flips?

The two flips are independent: the first flip does nothing to the coin before the second flip. Each flip by itself has probability $1/2$ of landing heads. Because the word **and** connects two independent events, multiply:

$$
P(\text{heads and heads}) = \dfrac{1}{2} \cdot \dfrac{1}{2} = \dfrac{1}{4}
$$

Out of four equally likely two-flip sequences — HH, HT, TH, TT — exactly one is "heads both times," and $1/4$ matches the count.

You can extend the multiplication trick to three or more independent events the same way. Rolling a six three times in a row would have probability $(1/6)(1/6)(1/6) = 1/216$.

---

## Example 3: rolling a 2 or a 3 (OR, mutually exclusive)

> A single die is rolled. Compute the likelihood that the result is a $2$ or a $3$.

You cannot roll a $2$ and a $3$ at the same time on one die, so the two events do not overlap — they are mutually exclusive. Each has probability $1/6$. Because the word **or** connects two mutually exclusive events, add:

$$
P(2 \text{ or } 3) = \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{2}{6} = \dfrac{1}{3}
$$

Double-check by counting directly: out of $6$ equally likely outcomes, $2$ of them ($2$ and $3$) work, so the probability is $2/6 = 1/3$. Match.

Now mix both rules. If you roll a die and flip a coin, what is the chance of rolling a $3$ AND getting tails? The die and coin are independent, so multiply: $(1/6)(1/2) = 1/12$. One compound question, one clean answer.

---

## Common pitfalls

- **Forgetting to reduce.** A probability of $4/12$ should be written $1/3$. Leaving it unreduced is not wrong numerically, but it looks sloppy and can hide matches with textbook answers.
- **Adding when you should multiply (and vice versa).** "AND" is your multiply signal; "OR" (for non-overlapping events) is your add signal. Circle the word in the problem before computing.
- **Treating dependent events as independent.** The multiplication rule $P(A \text{ and } B) = P(A) \cdot P(B)$ is only valid when $A$ does not shift the odds of $B$. Drawing two cards *without replacement* changes the deck between draws — the rule still has a version, but it is not the simple multiply.
- **Forgetting the complement trick.** If you are asked "what is the chance it does *not* happen," compute $1 - P(\text{happens})$ instead of listing every failing outcome.
- **Counting outcomes inconsistently.** Every outcome you list in the denominator has to be equally likely. Counting "rain, no rain" as $2$ equal outcomes and declaring $P(\text{rain}) = 1/2$ is wrong — rain and no rain are not equally likely every day.

---

## Prerequisites

Make sure you are comfortable with:

- [[Multiplying_Fractions]] — the AND rule is just fraction multiplication wearing a new hat.
- [[Equivalent_Fractions_And_Simplifying]] — so final answers can be reduced cleanly.
- [[Fractions_Decimals_And_Percents]] — probabilities are often reported as percents ($1/4 = 25\%$), and being fluent in all three forms is expected.

---

## Problems Involving Probability of Simple and Compound Events

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="probability_of_simple_and_compound_events"></div>

---

## See Also

- [[Multiplying_Fractions]]
- [[Fractions_Decimals_And_Percents]]
- [[Data_Displays_And_Measures_Of_Spread]]
- [[Mean_Median_Mode_And_Range]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
