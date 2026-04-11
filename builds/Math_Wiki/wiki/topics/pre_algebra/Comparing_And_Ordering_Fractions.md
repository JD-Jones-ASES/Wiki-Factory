---
title: "Comparing and Ordering Fractions"
type: topic
aliases: ["Fraction Comparison", "Comparing Fractions", "Ordering Fractions"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "3", section: "3.4"}
related:
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
  - "topics/pre_algebra/Mixed_Numbers_And_Improper_Fractions"
  - "topics/pre_algebra/Comparing_And_Ordering_Rational_Numbers"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Greatest_Common_Factor_And_Least_Common_Multiple"
problem_type_ids: []
figures: []
summary: "Deciding which of two fractions is larger, and putting a list of fractions in order."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Comparing and Ordering Fractions

# Comparing and Ordering Fractions

It is easy to tell that $\frac{7}{12}$ is bigger than $\frac{5}{12}$ — both fractions count pieces of the same size, so whichever has more pieces wins. The interesting case is when the denominators disagree, because then the pieces themselves are different sizes, and a larger numerator no longer guarantees a larger fraction. There are two reliable techniques for untangling that situation, and both trace back to the same core idea.

## What it means

A fraction is really two pieces of information glued together: how big each slice is (the denominator) and how many slices you have (the numerator). To stack two fractions against each other, you need a fair playing field — either equal slice sizes, or a trick that sidesteps the size disagreement.

Imagine comparing $\frac{2}{3}$ of a chocolate bar to $\frac{5}{8}$ of a different chocolate bar of the same total length. Two-thirds feels slightly bigger, but you need more than intuition. If you re-slice both bars into twenty-fourths, the first gives $\frac{16}{24}$ and the second gives $\frac{15}{24}$. Now they share a scale, and the winner is obvious.

The alternative is to skip rewriting and just ask: "Does scaling the first numerator by the second denominator beat scaling the second numerator by the first denominator?" That question turns out to be the same as asking which fraction is bigger, and the arithmetic is often faster. We call that technique **cross multiplication**.

## The rule

**Method 1 — Common denominator.** Given two fractions, build the least common denominator (the least common multiple of the denominators), rewrite each fraction with that denominator, and compare numerators. The one with the larger numerator is the larger fraction.

**Method 2 — Cross multiplication.** Given two positive fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ with $b, d > 0$, compute the two cross products $a \cdot d$ and $b \cdot c$.

$$
\frac{a}{b} \;?\; \frac{c}{d} \quad \Longleftrightarrow \quad a \cdot d \;?\; b \cdot c
$$

The same inequality (or equality) that holds between the cross products also holds between the original fractions.

For **mixed numbers**, first compare the whole-number parts. If they differ, you're done: the one with the larger whole part is larger. If they tie, compare only the fractional parts using either method above.

To **order** three or more fractions, pick one LCD that works for every denominator in the list, convert each fraction once, and then read them off in sorted order.

## Why it works

The common-denominator method works because once the denominators agree, the two fractions count equal-sized pieces, and comparing numerators is just comparing counts. The cross-multiplication trick works because writing the fractions over the common denominator $bd$ gives

$$
\frac{a}{b} = \frac{a d}{b d}, \qquad \frac{c}{d} = \frac{b c}{b d}
$$

and both fractions now share the denominator $bd$. Comparing those two equivalent forms reduces to comparing $a \cdot d$ with $b \cdot c$ — the cross products. The denominator simply cancels out of the comparison.

## Worked examples

### Example 1: comparing two fractions with cross multiplication
Is $\dfrac{4}{9}$ bigger than, smaller than, or equal to $\dfrac{3}{7}$?

**Solution.** The denominators are $9$ and $7$, which are both positive, so cross multiplication is safe.

Compute the two cross products.

$$
4 \cdot 7 = 28
$$

$$
9 \cdot 3 = 27
$$

Since $28 > 27$, the first cross product is larger, which means the first fraction is larger.

$$
\frac{4}{9} > \frac{3}{7}
$$

As a sanity check, rewrite both over a common denominator of $63$. You get $\frac{28}{63}$ and $\frac{27}{63}$, and of course $\frac{28}{63}$ is the larger one.

### Example 2: ordering three fractions with a common denominator
Put $\dfrac{5}{8}$, $\dfrac{7}{10}$, and $\dfrac{2}{5}$ in order from least to greatest.

**Solution.** Find a denominator that works for $8$, $10$, and $5$ all at once. The least common multiple of $8$ and $10$ is $40$, and $5$ already divides $40$, so the LCD is $40$.

Convert each fraction:

$$
\frac{5}{8} = \frac{5 \cdot 5}{8 \cdot 5} = \frac{25}{40}
$$

$$
\frac{7}{10} = \frac{7 \cdot 4}{10 \cdot 4} = \frac{28}{40}
$$

$$
\frac{2}{5} = \frac{2 \cdot 8}{5 \cdot 8} = \frac{16}{40}
$$

Now the comparison is pure numerator arithmetic: $16 < 25 < 28$. Read the original fractions in that same order to get the final answer.

$$
\frac{2}{5} < \frac{5}{8} < \frac{7}{10}
$$

### Example 3: comparing mixed numbers
Which is larger, $2\tfrac{3}{4}$ or $2\tfrac{5}{7}$?

**Solution.** Start with the whole parts. Both are $2$, so the tie is broken by the fractional parts: you need to decide whether $\frac{3}{4}$ or $\frac{5}{7}$ is bigger.

Use cross multiplication.

$$
3 \cdot 7 = 21
$$

$$
4 \cdot 5 = 20
$$

Since $21 > 20$, the first fraction wins: $\frac{3}{4} > \frac{5}{7}$. Attaching the (equal) whole parts back on, the answer is

$$
2\tfrac{3}{4} > 2\tfrac{5}{7}
$$

## Common mistakes

- Comparing numerators without first matching the denominators. A larger numerator does not mean a larger fraction when the pieces themselves are different sizes.
- Cross-multiplying with a negative denominator. The cross-multiplication rule stated above assumes both denominators are positive; negatives flip the inequality and cause errors. When negatives are involved, rewrite the fractions with positive denominators first.
- Forgetting to compare whole parts first on a mixed-number problem. If the whole numbers already differ, the fractional parts never enter the comparison.
- Choosing a common denominator that is too big. Any common multiple works, but using the least common multiple keeps the numbers smaller and the arithmetic faster.
- Reading the final ordered list in the wrong direction. Always label your answer "least to greatest" or "greatest to least" to avoid reversing it at the last step.

## Prerequisites

- [[Equivalent_Fractions_And_Simplifying]]
- [[Greatest_Common_Factor_And_Least_Common_Multiple]]

You need to be able to rebuild a fraction with a new denominator and to find the least common multiple of two small numbers without slowing down; those skills are the engine room of every comparison below.

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="comparing_and_ordering_fractions"></div>

_More problem types are coming soon._

## See also

- [[Adding_And_Subtracting_Fractions]]
- [[Mixed_Numbers_And_Improper_Fractions]]
- [[Comparing_And_Ordering_Rational_Numbers]]
- [[Equivalent_Fractions_And_Simplifying]]
- [[Middle_School_Math|Middle School Math]]
- [[_overview|Home]]

## Sources in the 

- **Math I** — Chapter 3, Section 3.4: Comparing and Ordering Fractions
