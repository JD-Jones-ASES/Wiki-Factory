---
title: "Proportions and Cross Multiplication"
type: topic
aliases: ["Proportion", "Cross Multiplication", "Cross Products"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "6", section: "6.3"}
related:
  - "topics/pre_algebra/Ratios_And_Equivalent_Ratios"
  - "topics/pre_algebra/Unit_Rates"
  - "topics/pre_algebra/Applications_Of_Proportional_Reasoning"
  - "topics/pre_algebra/Ratios_Rates_And_Proportions"
  - "topics/pre_algebra/Proportions_In_Similar_Figures"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Ratios_And_Equivalent_Ratios"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "An equation between two ratios, solved with the cross-product shortcut."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Proportions and Cross Multiplication

# Proportions and Cross Multiplication

A proportion shows up any time the same relationship has to hold at two different scales. A map uses "1 inch represents 50 miles." A recipe uses "3 cups of flour for every 2 eggs." A blueprint uses "1 foot on paper equals 12 feet in real life." In each case, a single ratio describes a rule, and that rule has to stay the same no matter how much you scale the problem up or down.

Proportions are the tool for working with those scaling problems, and cross multiplication is the shortcut that turns them into simple algebra.

---

## What it means

A **proportion** is an equation that sets two ratios equal to each other. In symbols:

$$
\frac{a}{b} = \frac{c}{d}
$$

where $b$ and $d$ are both nonzero (you cannot divide by zero). In words, you say that the first ratio matches the second one. The two ratios are equivalent, meaning they express the same comparison using different numbers — just like $\frac{1}{2}$ and $\frac{3}{6}$ express the same fraction.

A proportion lets you write "this is the rule, and it applies here too." Once you know three of the four numbers, the fourth is determined. Finding that fourth number is the central skill.

---

## The rule

If two ratios are equal, their **cross products** are equal. That is, if

$$
\frac{a}{b} = \frac{c}{d}
$$

then

$$
a \cdot d = b \cdot c
$$

This property is called **cross multiplication**, and it works in both directions. If you are handed two ratios and the cross products come out equal, the ratios form a proportion. If you are handed a proportion with one unknown value, you can cross multiply to produce a single equation and solve it.

---

## Why it works

Cross multiplication is not magic. It is a compact way of clearing both denominators at once, and you can derive it from ordinary algebra. Start with:

$$
\frac{a}{b} = \frac{c}{d}
$$

Multiply both sides by $b \cdot d$:

$$
\frac{a}{b} \cdot b \cdot d = \frac{c}{d} \cdot b \cdot d
$$

On the left, the $b$ in the numerator and the $b$ in the denominator cancel, leaving $a \cdot d$. On the right, the $d$s cancel, leaving $b \cdot c$. The result is:

$$
a \cdot d = b \cdot c
$$

So "cross multiplying" is really just clearing both denominators at once. If you ever forget the shortcut, you can always fall back on this derivation.

---

## Worked examples

### Example 1: Solving for an unknown

> Solve the proportion $\dfrac{x}{12} = \dfrac{5}{4}$.

Cross multiply to clear the fractions:

$$
x \cdot 4 = 12 \cdot 5
$$

$$
4x = 60
$$

Divide both sides by 4:

$$
x = \frac{60}{4} = 15
$$

So $x = 15$. You can verify by plugging it back in: $\frac{15}{12}$ simplifies to $\frac{5}{4}$, which matches the right side of the original equation.

### Example 2: Scaling a real-world quantity

> A box of 6 hardcover books weighs 15 pounds. If the books are all identical, how much do 14 of the same books weigh?

The rule is "books to weight," and it has to hold for both the original crate and the new pile. Write a proportion with books on top and pounds on the bottom:

$$
\frac{6}{15} = \frac{14}{w}
$$

Cross multiply:

$$
6 \cdot w = 15 \cdot 14
$$

$$
6w = 210
$$

Divide both sides by 6:

$$
w = \frac{210}{6} = 35
$$

So 14 of those books weigh **35 pounds**. A quick reasonableness check: 14 books is a little more than twice 6 books, and 35 pounds is a little more than twice 15 pounds, so the answer lines up with the rule.

### Example 3: Scaling a recipe

> A muffin recipe uses 2 cups of oats for every 3 cups of flour. If a baker wants to use 12 cups of flour, how many cups of oats should she use?

Set up the proportion with oats on top and flour on the bottom — keeping the quantities in corresponding positions is critical:

$$
\frac{2}{3} = \frac{n}{12}
$$

Cross multiply:

$$
2 \cdot 12 = 3 \cdot n
$$

$$
24 = 3n
$$

Divide both sides by 3:

$$
n = 8
$$

The baker needs **8 cups of oats**. Sanity check: she quadrupled the flour (3 cups became 12), so the oats should also quadruple (2 cups become 8).

---

## Common mistakes

- **Mismatched corresponding parts.** When you set up a proportion, the units in the top of the first ratio must match the units on top of the second ratio, and the same for the bottoms. If Example 2 had put weight on top of one ratio and books on top of the other, the answer would be nonsense.
- **Multiplying straight across instead of across the equals sign.** Cross multiplication goes diagonally: top of the left times bottom of the right, and vice versa. Multiplying top-left by top-right is a different operation and does not solve the equation.
- **Forgetting to divide at the end.** After cross multiplying you get a simple equation like $4x = 60$. You still need to divide both sides by the coefficient to isolate the variable.
- **Using cross multiplication on more than two fractions.** The shortcut only applies when there is exactly one fraction on each side of the equals sign. For more complicated equations, clear denominators the long way.

---

## Prerequisites

Before working with proportions, make sure you are comfortable with:

- [[Ratios_And_Equivalent_Ratios|Ratios and equivalent ratios]] — a proportion is just two equivalent ratios written as an equation
- [[Equivalent_Fractions_And_Simplifying|Equivalent fractions and simplifying]] — the same algebra that governs equal fractions powers cross multiplication

---

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="proportions_and_cross_multiplication"></div>

_More problem types are coming soon._

---

## See also

- [[Unit_Rates]]
- [[Applications_Of_Proportional_Reasoning]]
- [[Ratios_Rates_And_Proportions]]
- [[Proportions_In_Similar_Figures]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]

---

## Sources in the 

- **Math I** — Chapter 6 (Ratios, Rates, and Proportions), Section 6.3: Proportions and Cross Multiplication
