---
title: "Ratios and Equivalent Ratios"
type: topic
aliases: ["Ratio", "Equivalent Ratios", "Simplest Form of a Ratio"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "6", section: "6.1"}
related:
  - "topics/pre_algebra/Unit_Rates"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Applications_Of_Proportional_Reasoning"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
problem_type_ids: []
figures: []
summary: "Compare two quantities, write the comparison three ways, and scale it up or down to find equivalents."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Ratios and Equivalent Ratios

# Ratios and Equivalent Ratios

If a classroom has $12$ desks and $8$ chairs, you could say there are four more desks than chairs — that is a difference. A **ratio** is a different tool. A ratio asks: *how do these two numbers compare by division*? For every chair, how many desks are there?

Ratios are everywhere the moment you look for them. Map scales, paint mixes, gear sizes, screen resolutions, baking recipes, sports statistics. They all rest on the same idea: pin two quantities next to each other and describe how one stacks up against the other. Once you can write a ratio and spot when two ratios describe the same relationship, the rest of proportional reasoning follows naturally.

---

## What it means

A **ratio** compares two quantities using division. Unlike subtraction, which tells you how far apart two numbers are, a ratio tells you how one scales relative to the other.

There are three common ways to write the same ratio, and all three mean exactly the same thing:

- **Word form:** "$3$ to $5$"
- **Colon form:** $3 : 5$
- **Fraction form:** $\dfrac{3}{5}$

Read every one of those as "three compared to five." The colon and the fraction bar are both shorthand for the same comparison.

Two cautions right away:

- **Order matters.** The ratio of apples to oranges is not the same as the ratio of oranges to apples. A $3 : 5$ ratio flipped to $5 : 3$ describes a different situation.
- **A ratio is not a fraction, even when it looks like one.** A fraction names a piece of a single whole ($\tfrac{3}{5}$ of a pizza). A ratio compares two separate quantities that do not have to belong to the same whole ($3$ cats to $5$ dogs). They share notation; they mean different things.

---

## The rule

**Equivalent ratios** are ratios that describe the same comparison at different scales. If you double both parts of $3 : 5$, you get $6 : 10$ — a bigger example of the same relationship, not a new one.

The rule for producing equivalent ratios is short:

> Multiply **both** terms of a ratio by the same nonzero number, or divide **both** terms by the same nonzero number. The result is equivalent to the original.

In symbols, for any nonzero number $n$,

$$
\frac{a}{b} = \frac{a \cdot n}{b \cdot n} \qquad \text{and} \qquad \frac{a}{b} = \frac{a \div n}{b \div n}.
$$

Going up, you scale the ratio to describe more things; going down, you scale it to its **simplest form**, in which the two terms share no common factor beyond $1$.

---

## Why it works

If you have already met [[Equivalent_Fractions_And_Simplifying|equivalent fractions]], this rule should feel familiar — because it is literally the same move. Multiplying the top and bottom of a fraction by the same number does not change its value, and multiplying both parts of a ratio by the same number does not change the comparison it expresses.

Here is the intuition. A ratio of $2 : 3$ means "for every $2$ of the first thing, there are $3$ of the second." If you line up two of those groups, you get $4 : 6$. Three groups gives $9 : 6$, I mean $6 : 9$. The rate at which the two quantities match each other never budges; you are just counting more of them at a time. Going the other direction, dividing both parts by a common factor bundles the groups back up into fewer items per bundle, but the per-bundle comparison is untouched.

---

## Worked examples

### Example 1: Building equivalent ratios

> Write three ratios equivalent to $2 : 3$.

The recipe is to multiply both terms of $2 : 3$ by the same scale factor. Pick three different multipliers — $2$, $3$, and $4$ will do — and run the arithmetic:

- Times $2$: $(2 \cdot 2) : (3 \cdot 2) = 4 : 6$
- Times $3$: $(2 \cdot 3) : (3 \cdot 3) = 6 : 9$
- Times $4$: $(2 \cdot 4) : (3 \cdot 4) = 8 : 12$

So three ratios equivalent to $2 : 3$ are $4 : 6$, $6 : 9$, and $8 : 12$. Each one describes the same "two to three" relationship, counted in larger batches.

### Example 2: Simplifying to lowest terms

> Write the ratio $18 : 24$ in simplest form.

To simplify, find the largest number that divides both terms evenly — the **greatest common factor** — and divide both by it. The factors of $18$ are $1, 2, 3, 6, 9, 18$; the factors of $24$ are $1, 2, 3, 4, 6, 8, 12, 24$. The biggest number on both lists is $6$.

Divide both parts by $6$:

$$
18 : 24 \;=\; \frac{18}{6} : \frac{24}{6} \;=\; 3 : 4
$$

The simplest form of $18 : 24$ is $3 : 4$. Now $3$ and $4$ share no common factor other than $1$, so you cannot shrink it further.

You can double-check by scaling $3 : 4$ back up: $3 : 4$ times $6$ is $18 : 24$. The two ratios describe the same comparison.

### Example 3: A bread recipe

> A bread recipe calls for $4$ cups of flour and $3$ cups of water. What is the flour-to-water ratio? If a baker needs $12$ cups of flour for a larger batch, how much water should they use?

The flour-to-water ratio is $4 : 3$ — pay attention to the order, since "flour to water" means flour comes first.

For the larger batch, you need an equivalent ratio where the flour part is $12$. Ask yourself: what did $4$ get multiplied by to become $12$? The answer is $3$. To keep the ratio equivalent, multiply the water part by the same $3$:

$$
4 : 3 \;=\; (4 \cdot 3) : (3 \cdot 3) \;=\; 12 : 9
$$

The baker needs $9$ cups of water. The dough will come out the same texture because the flour-to-water comparison has not changed — only the batch size.

---

## Common mistakes

- **Adding instead of scaling.** If you want to go from $2 : 3$ to a bigger equivalent ratio, you multiply both parts by the same number. Adding $1$ to each gives $3 : 4$, which is a *different* ratio, not an equivalent one.
- **Scaling only one side.** Doubling the $2$ in $2 : 3$ to get $4 : 3$ breaks the comparison. Whatever you do to one part, do the same thing to the other.
- **Flipping the order.** "Boys to girls" and "girls to boys" are different ratios. When a word problem specifies an order, keep it.
- **Confusing a ratio with a fraction of a whole.** A room with $3$ cats and $5$ dogs has a cat-to-dog ratio of $3 : 5$. That does *not* mean cats are $\tfrac{3}{5}$ of the animals — that would be $\tfrac{3}{8}$, because there are $8$ animals total. A ratio compares parts; a fraction names a part of a whole.
- **Forgetting to check for a common factor.** A ratio like $24 : 36$ looks fine but is not in simplest form. Always divide out the greatest common factor at the end.

---

## Prerequisites

Before you practice ratio problems, make sure you are comfortable with:

- [[Equivalent_Fractions_And_Simplifying]] — the mechanics of multiplying and dividing both terms by the same number.
- [[Integers_And_The_Number_Line]] — basic whole-number arithmetic and factoring.

If either feels shaky, start there and come back.

---

## Problems Involving This Topic

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections stay in this browser. When you are ready, open your [[Vault]] to see them all, view hints and answers, and print a worksheet.

<div class="problem-vault-widget" data-topic-slug="ratios_and_equivalent_ratios"></div>

_More problem types are coming soon._

## See also

- [[Equivalent_Fractions_And_Simplifying]]
- [[Unit_Rates]]
- [[Proportions_And_Cross_Multiplication]]
- [[Applications_Of_Proportional_Reasoning]]
- [[Fractions_Decimals_And_Percents]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]

## Sources in the 

- **Math I** — Chapter 6, Section 6.1: Ratios and Equivalent Ratios
