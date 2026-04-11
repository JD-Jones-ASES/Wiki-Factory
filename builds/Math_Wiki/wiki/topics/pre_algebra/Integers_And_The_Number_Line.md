---
title: "Integers and the Number Line"
type: topic
aliases: ["Integers", "Number Line", "Signed Whole Numbers"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "2", section: "2.1"}
related:
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Order_Of_Operations_With_Integers"
  - "topics/pre_algebra/Absolute_Value"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
problem_type_ids: []
figures: ["pre_algebra/number_line.svg"]
summary: "Whole numbers together with their negatives, arranged in order on a line."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Integers and the Number Line

# Integers and the Number Line

The counting numbers $1, 2, 3, \dots$ run out of room the moment you owe someone money, walk downstairs, or measure a temperature in winter. The **integers** fix that. They are the counting numbers, their mirror images on the other side of zero, and zero itself. Once you picture them on a line, arithmetic with them stops being a guessing game about which sign wins and becomes a matter of simple geography — some numbers live on the left, some live on the right, and you always know which is which.

![[number_line.svg|Integers on the number line]]

## What it means

An **integer** is any number you can reach by starting at zero and stepping a whole number of units left or right. The full set looks like this:

$$
\dots, -4, -3, -2, -1, 0, 1, 2, 3, 4, \dots
$$

The dots on each end say the list never ends. There is no largest integer and no smallest integer. Three pieces make up the whole collection:

- The **positive integers**: $1, 2, 3, 4, \dots$ — whole numbers bigger than zero. A plus sign in front of them is optional and almost never written.
- The **negative integers**: $-1, -2, -3, -4, \dots$ — each one is the mirror image of a positive integer. The dash is mandatory; it is what makes the number negative.
- **Zero**: neither positive nor negative. It is the anchor that the positives and negatives are measured from.

Fractions and decimals like $\tfrac{1}{2}$ or $3.7$ are **not** integers. Integers step, they do not slide between.

A **number line** is a horizontal line with zero in the middle, positives marching off to the right, and negatives marching off to the left. Tick marks at evenly spaced intervals label each integer. The distance between any two neighbors — say between $3$ and $4$, or between $-2$ and $-1$ — is always the same. That constant spacing is the whole reason the line is useful: it converts "which is bigger?" into "which is farther right?"

## The rule

Three facts about the number line do almost all of the work at this level.

**Order from left to right.** If two integers sit on the number line, the one farther to the right is greater. In symbols:

$$
a < b \quad \text{exactly when $a$ lies to the left of $b$ on the number line.}
$$

This rule applies everywhere, including among negative numbers. $-2$ is to the right of $-5$, so $-5 < -2$. Among negatives, the number with the smaller-looking magnitude is actually the larger number.

**Opposites.** Every integer has a twin called its **opposite**. The twin sits at the same distance from zero but on the far side. So $7$ pairs with $-7$; $-12$ pairs with $12$; and zero is its own partner. Another name for this twin is the **additive inverse**, a phrase that makes sense once you notice adding a number to its pair always produces zero: for instance, $5 + (-5) = 0$.

**Absolute value.** The **absolute value** of an integer is its distance from zero on the number line, measured in steps. Distance is never negative, so the absolute value is always zero or positive. The notation is a pair of vertical bars:

$$
|{-4}| = 4, \qquad |{7}| = 7, \qquad |{0}| = 0.
$$

You can read $|n|$ as "throw away the sign." A full treatment of absolute value lives at [[Absolute_Value]].

## Why it works

The number line is not a decoration. It is the geometric reason the ordering rule holds up. Positive integers extend to the right because they represent "more than nothing," and each step rightward adds one more unit. Negative integers extend to the left because they represent debts or deficits — each step leftward subtracts one more unit. Zero is the balance point where there is neither more nor less.

Opposites work because the line is symmetric around zero. Take any integer, reflect it across zero as if zero were a mirror, and you land on its opposite. The two points sit at the same distance from zero, just on different sides, which is exactly why their sum is zero — one cancels the other.

Absolute value is just distance without direction. Walking four steps left of zero and walking four steps right of zero both cover four steps. When all you care about is how far, the minus sign is noise.

## Worked examples

### Example 1: Opposite and absolute value

Find the opposite of $-7$ and the absolute value of $-4$.

**Opposite of $-7$.** The opposite is the integer the same distance from zero but on the other side. $-7$ sits seven steps left of zero, so its opposite sits seven steps right of zero, which is $7$. Another quick check: add the number to its proposed opposite. $-7 + 7 = 0$, so $7$ is indeed the opposite.

**Absolute value of $-4$.** The absolute value is the distance from zero, ignoring direction. $-4$ is four steps from zero, so:

$$
|{-4}| = 4.
$$

Answer: the opposite of $-7$ is $7$, and $|{-4}| = 4$.

### Example 2: Ordering a mixed list

Arrange the integers $-3,\ 5,\ 0,\ -8,\ 2$ from least to greatest.

Picture the number line and mentally place each value. $-8$ is the farthest left. $-3$ is to its right but still left of zero. Zero is the center. $2$ is to the right of zero, and $5$ is farther right still.

Reading the line from left to right gives the order:

$$
-8,\ -3,\ 0,\ 2,\ 5.
$$

A common tripwire is the pair $-8$ and $-3$. Looking only at the numbers without their signs, $8$ is larger than $3$, which might fool you into writing $-3$ first. On the number line, though, $-8$ is farther left, so it is the smaller value. Among negatives, the bigger the raw digits, the smaller the number.

Answer: $-8 < -3 < 0 < 2 < 5$.

## Common mistakes

- **Ranking negatives backwards.** Writing $-3 < -8$ because "$3$ is less than $8$." The rule is position on the line, not the size of the digits.
- **Forgetting zero is an integer.** Zero sits squarely in the set; it is neither positive nor negative, but it is an integer.
- **Confusing the opposite with the absolute value.** The opposite of $-5$ is $5$; the absolute value of $-5$ is also $5$, but the opposite of $5$ is $-5$ while the absolute value of $5$ is still $5$. Opposite flips direction; absolute value strips it away.
- **Reading $|{-4}|$ as $-4$.** The bars do not mean multiplication by $-1$; they mean distance from zero. The result is never negative.
- **Treating fractions as integers.** $\tfrac{1}{2}$ is a rational number and a real number, but it is not an integer. Integers are whole steps only.

## Prerequisites

Before practicing problems on this page, make sure you are comfortable with:

- [[Place_Value_Rounding_And_Estimation]] — the foundation for reading and comparing whole-number magnitudes.

If place value is shaky, start there and return here afterward.

## Problems Involving This Topic

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections stay in this browser. When you are ready, open your [[Vault]] to see them all, view hints and answers, and print a worksheet.

<div class="problem-vault-widget" data-topic-slug="integers_and_the_number_line"></div>

_More problem types are coming soon._

## See also

- [[Adding_And_Subtracting_Integers]]
- [[Multiplying_And_Dividing_Integers]]
- [[Order_Of_Operations_With_Integers]]
- [[Absolute_Value]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[Vault|Your Practice Vault]]
- [[_overview|Home]]

## Sources in the 

- **Math I**, Chapter 2, Section 2.1 — introduction to integers and the number line.
