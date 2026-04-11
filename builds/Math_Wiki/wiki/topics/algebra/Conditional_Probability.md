---
title: "Conditional Probability"
type: topic
aliases: []
tags: ["#branch-algebra-2", "#topic-probability", "#skill-formula-substitution", "#skill-translation", "#skill-multi-step", "#key-topic", "#word-problem-support", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Ratios_And_Equivalent_Ratios"
  - "topics/algebra/Function_Basics"
  - "topics/pre_algebra/Data_Displays"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Ratios_And_Equivalent_Ratios"
  - "topics/pre_algebra/Data_Displays"
problem_type_ids: []
figures: ["algebra/two_way_table.svg"]
summary: "Update a probability once you learn one of the pieces of information by restricting attention to the part of the sample space where that information holds."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Conditional Probability

# Conditional Probability

Every probability you compute assumes some background — the set of outcomes you think are possible. A **conditional probability** is what you get when that background changes because you learned a piece of information. You were about to make a prediction across a whole population; now someone tells you the individual you are looking at belongs to a particular group. You do not throw away your reasoning — you restrict it. The sample space shrinks to just the group you now know you are in, and the probability recalculates over that smaller world.

Imagine that Kai is picking a student at random from their homeroom to hand out a math worksheet. Before knowing anything else, the probability that the chosen student is on the track team might be $12/30$. But if Kai mentions "I already know the chosen student takes the early bus," and you know something about the ridership of the early bus, your estimate should change — maybe there are proportionally more (or fewer) track-team members on that bus than in the homeroom overall. Conditional probability is the bookkeeping for exactly that kind of update.

![[two_way_table.svg|A two-way table organizing events by two simultaneous attributes]]

---

## What it means

Write $P(A \mid B)$ for the probability of event $A$ given that event $B$ has happened. The bar inside the notation is read "given." It is the tool for answering questions that start "what fraction of the $B$'s are also $A$'s?" — not "what fraction of everything is $A$ and $B$?"

The defining formula is

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.
$$

Every piece of this equation is doing work. The numerator $P(A \cap B)$ asks how much of the sample space is in **both** events at once. The denominator $P(B)$ is the total size of the restricted world you are now working inside. Dividing gives the fraction of that restricted world that is also in $A$ — exactly the probability you want.

Notice that $P(A \mid B)$ is generally **not** equal to $P(B \mid A)$. The two conditional probabilities have the same numerator $P(A \cap B)$ but different denominators, so swapping the direction of the bar swaps the meaning entirely. "The probability that a student plays guitar given that they play a string instrument" is a very different number from "the probability that a student plays a string instrument given that they play guitar" — one of those two is actually 100 percent.

### Two-way tables are the natural home for this

The cleanest way to learn conditional probability is with a **two-way table** (sometimes called a contingency table). A two-way table is just a rectangle of counts indexed by two simultaneous attributes. Rows label one attribute; columns label the other; row and column totals sit on the margins.

|            | Column A holds | Column A fails | Row total |
|------------|---------------:|---------------:|----------:|
| **Row B holds**  | a              | b              | a + b     |
| **Row B fails**  | c              | d              | c + d     |
| **Col total**    | a + c          | b + d          | N         |

Once you have a table like this, conditional probabilities become pure division. $P(A \mid B)$ is the count in the "$A$ and $B$" cell, divided by the row total for $B$. You are literally walking into the $B$-row and asking what fraction of it is in the $A$-column.

---

## How it works: reading the table

Here is the step-by-step for computing $P(A \mid B)$ from a two-way table.

1. **Identify the condition.** The event after the bar is the group you are restricting to. Find its row (or column) in the table.
2. **Find the row (or column) total.** That number is your new denominator — the size of the restricted world.
3. **Find the count of people who are in the restricted world and also satisfy the other event.** That is the numerator.
4. **Divide.** The result is the conditional probability, a number between $0$ and $1$.

This procedure is resistant to confusion because it keeps the meaning of "given" concrete. You never accidentally divide by the grand total $N$, because you are physically looking at a row (or column) total, not the full table total. That is the single most common mistake students make when first meeting the topic.

### The multiplication rule

Rearranging the definition gives the **multiplication rule**, which is useful when you know $P(B)$ and $P(A \mid B)$ and want to find the joint probability:

$$
P(A \cap B) = P(B) \cdot P(A \mid B).
$$

Read in words: the chance that both happen equals the chance that $B$ happens, times the chance that $A$ happens once you know $B$ has. This is often the more natural direction when a probability is presented as a tree of decisions — each branch of the tree multiplies another conditional probability in.

### Independence versus dependence

Two events $A$ and $B$ are **independent** when knowing whether $B$ happened does not change your estimate of $A$. In formula terms,

$$
P(A \mid B) = P(A).
$$

If this equation fails — if learning $B$ moves the probability of $A$ up or down — the events are **dependent**. Another way to test independence is to check whether $P(A \cap B) = P(A) \cdot P(B)$; equivalent condition, different arithmetic route. These definitions are worth memorizing, because test questions love to ask you to classify a pair of events as independent or dependent from a table of counts.

---

## Why it works

The intuition is simpler than the formula looks. Every probability is built from a set of equally likely (or at least well-defined) outcomes. When you are told "B has happened," the outcomes where $B$ did not happen are no longer under consideration. The remaining outcomes are exactly the ones in $B$, and among them, the ones you still care about are the ones also in $A$ — that is $A \cap B$. The probability is the fraction of the survivors that match, which is the numerator count divided by the denominator count. The formula $P(A \cap B) / P(B)$ is just the algebraic spelling of that count-the-survivors operation when your probabilities are presented as fractions of a whole rather than as raw counts.

The reason the two-way table is such a good teaching tool is that it lets you *see* the restriction happen. Circling a row is literally narrowing your attention, and then asking "what fraction of this row is in the target column?" is the rest of the work. The formula is only the shortcut notation for something you are already doing with your finger on the page.

---

## Worked examples

**Example 1.** Priya runs the school gardening club. She kept track of the $80$ members across two attributes: whether they signed up for the spring planting day (Yes/No) and whether they prefer vegetables or flowers (Veg/Flow). The counts are:

|               | Yes to planting | No to planting | Total |
|---------------|----------------:|---------------:|------:|
| **Vegetables**| $28$            | $12$           | $40$  |
| **Flowers**   | $22$            | $18$           | $40$  |
| **Total**     | $50$            | $30$           | $80$  |

(a) What is the probability that a randomly chosen member said yes to the planting day given that they prefer vegetables? (b) What is the probability that a randomly chosen member prefers vegetables given that they said yes to the planting day? (c) Are the two answers the same, and why or why not?

(a) The condition "prefers vegetables" restricts to the first row, which has row total $40$. Of those $40$, the cell in the "Yes to planting" column contains $28$. So

$$
P(\text{Yes} \mid \text{Veg}) = \frac{28}{40} = 0.70.
$$

Seven out of every ten vegetable-preferring members signed up for the planting day.

(b) Now the condition is "said yes to the planting day," which restricts to the first column, with column total $50$. Of those $50$, the cell in the "Vegetables" row contains $28$. So

$$
P(\text{Veg} \mid \text{Yes}) = \frac{28}{50} = 0.56.
$$

Among members who said yes, $56\%$ prefer vegetables.

(c) The two conditional probabilities share the same numerator of $28$ (the "yes and vegetables" cell), but the denominators are different — $40$ versus $50$ — because the conditioning restricts to different slices of the table. The question "what fraction of vegetable-fans came?" and the question "what fraction of the attendees like vegetables?" are not the same question, and the table makes this visible. That is the lesson to carry forward: $P(A \mid B) \neq P(B \mid A)$ in general.

**Example 2.** Rohan is running a small two-stage game for a school fundraiser. The first stage is to draw a marble from a bag that contains $6$ red marbles and $4$ blue marbles. Whatever color is drawn is set aside. The second stage is to draw a second marble from the same bag without replacement. Determine the probability that both draws come out red, using the multiplication rule.

Let $R_1$ be the event "the first draw is red," and $R_2$ be the event "the second draw is red." We want $P(R_1 \cap R_2)$, which the multiplication rule writes as

$$
P(R_1 \cap R_2) = P(R_1) \cdot P(R_2 \mid R_1).
$$

The first factor is straightforward: the bag starts with $10$ marbles, $6$ of them red, so $P(R_1) = 6/10 = 3/5$.

For the second factor, imagine you are now standing at the moment right after the first red has been set aside. The bag holds $9$ marbles, and only $5$ of them are red (because one red already left). So $P(R_2 \mid R_1) = 5/9$.

Multiply:

$$
P(R_1 \cap R_2) = \frac{3}{5} \cdot \frac{5}{9} = \frac{15}{45} = \frac{1}{3}.
$$

The probability of two reds in a row is $1/3$, or about $33.3\%$. The critical conceptual move is that the second factor had to be conditional — the bag changed between the two draws, and pretending the draws were independent would have given the wrong answer of $(3/5)(3/5) = 9/25 = 0.36$.

**Example 3.** Zoe's statistics class has $50$ students, split across two categories: whether or not a student completed the online homework (Yes/No) and whether or not they passed the midterm (Pass/Fail). The counts are: $24$ completed and passed, $6$ completed and failed, $8$ did not complete and passed, $12$ did not complete and failed. Determine whether completing the homework and passing the midterm are independent events.

First, fill out the table to make sure the counts add correctly.

|               | Passed | Failed | Total |
|---------------|-------:|-------:|------:|
| **Completed** | $24$   | $6$    | $30$  |
| **Not**       | $8$    | $12$   | $20$  |
| **Total**     | $32$   | $18$   | $50$  |

Compute the unconditional probability of passing, and the probability of passing given that homework was completed.

$$
P(\text{Pass}) = \frac{32}{50} = 0.64.
$$

$$
P(\text{Pass} \mid \text{Completed}) = \frac{24}{30} = 0.80.
$$

Because $0.80 \neq 0.64$, the two events are **dependent**. Learning that a student completed the homework pushes the probability that they passed from $64\%$ up to $80\%$. That upward shift is exactly what the word "dependent" is measuring — the condition moved the probability, so the information mattered.

For completeness, the other direction tells the same story: $P(\text{Pass} \mid \text{Not}) = 8/20 = 0.40$, far below the unconditional $0.64$, so not completing the homework moves the probability the opposite way. The two conditional probabilities bracket the unconditional one, which is what happens whenever the events are dependent.

---

## Common pitfalls

- Dividing by the grand total instead of the row (or column) total. That division gives you $P(A \cap B)$, not $P(A \mid B)$. The "given" event tells you which total to use, and it is almost never $N$.
- Swapping $P(A \mid B)$ and $P(B \mid A)$ because they look similar. They almost always have different values; the bar has a direction and the direction matters.
- Treating two dependent events as if they were independent, so you multiply $P(A) \cdot P(B)$ instead of $P(A) \cdot P(B \mid A)$. The multiplication rule requires the second factor to be conditional unless you have verified independence.
- Forgetting to reduce the bag, deck, or population size after a without-replacement step. The second draw lives in a smaller world than the first, and the conditional probability reflects that smaller world.
- Reading a two-way table as if the column headers were the conditioning event. Until you decide which event is after the bar, the table is just counts — the "given" label comes from the question, not from the table layout.

---

## Problems Involving Conditional Probability

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="conditional_probability"></div>

## See Also

- [[Probability_Of_Simple_And_Compound_Events]] — the unconditional probability base that conditional probability extends
- [[Fractions_Decimals_And_Percents]] — conditional probabilities are usually reported in all three forms and you should be fluent in converting them
- [[Ratios_And_Equivalent_Ratios]] — a conditional probability is a ratio of a favorable count to a restricted total, and reducing it works like any other ratio
- [[Data_Displays]] — the broader topic that includes two-way tables and other joint displays
- [[Function_Basics]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
