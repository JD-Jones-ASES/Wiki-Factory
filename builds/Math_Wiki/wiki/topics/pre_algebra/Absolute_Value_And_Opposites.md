---
title: "Absolute Value and Opposites"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
problem_type_ids: []
figures: []
summary: "Two related ideas: the twin on the other side of zero, and the raw distance from zero."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Absolute Value and Opposites

# Absolute Value and Opposites

Once a number line has negatives on it, two natural questions come up almost immediately. First: if I pick a number, what is its mirror image on the other side of zero? Second: if I forget whether the number is positive or negative, how far is it from zero? These two questions have their own names — **opposite** and **absolute value** — and once you learn to keep them separate, a lot of sign-heavy arithmetic gets simpler. Both ideas lean on the same picture: the number line as a road with zero in the middle and equal steps running left and right.

## What it means

The **opposite** of a number $n$ is the number with the same magnitude but the other sign. Written with a minus sign in front, the opposite of $n$ is:

$$
-n
$$

So the opposite of $9$ is $-9$, the opposite of $-12$ is $12$, and the opposite of $0$ is $0$ itself — zero is its own opposite because it is the only point that sits on the dividing line. A quick sanity check: a number and its opposite always add to zero.

$$
n + (-n) = 0
$$

That is why the opposite is sometimes called the **additive inverse** — adding it undoes the number.

The **absolute value** of a number $n$ is how far from zero that number sits on the number line, with no regard for which side. It is written with a pair of vertical bars:

$$
|n|
$$

Read as "the absolute value of $n$." Because distance cannot be negative, the result of $|n|$ is always either zero or a positive number. Three quick examples make the picture clear:

$$
|8| = 8, \qquad |{-8}| = 8, \qquad |0| = 0.
$$

Both $8$ and $-8$ are the same eight steps away from zero, so they share the same absolute value. Zero is zero steps from itself, so its absolute value is zero.

## How it works

To find the opposite of a number, flip its sign. If the number is positive, stick a minus in front. If the number is already negative, drop the minus (or think of it as another flip that cancels the first). Numerically, $-(-6) = 6$, because flipping twice returns you to where you started.

To find the absolute value of a number, throw away any minus sign and keep the digits. Formally you can write it as a case-by-case rule:

$$
|n| = \begin{cases} n & \text{if } n \geq 0 \\ -n & \text{if } n < 0 \end{cases}
$$

The second line looks strange at first because it says "use $-n$." But if $n$ is already negative — say $n = -7$ — then $-n = -(-7) = 7$, which is exactly the positive version you want. The rule is just math-speak for "strip the sign."

When a problem asks you to solve $|x| = 4$, it is asking: which numbers sit exactly four steps from zero? There are two — the positive one and its opposite — so the answer is $x = 4$ or $x = -4$. This is a common source of confusion: absolute value equations almost always produce two answers instead of one.

## Why it works

The number line is symmetric around zero. Reflect any point across that zero mark and you land on a point the same distance away but on the other side — that reflection is exactly what "opposite" means. Adding a number to its reflection moves you the same distance in opposite directions, so you always return to zero, which is why a number plus its opposite equals zero.

Absolute value is just the raw distance — how many steps, ignoring which direction. Since distance has no direction, the sign drops out, and since distance is never a debt, the result is never negative.

## Worked examples

**Example 1.** Compute the opposite of $-13$ and the absolute value of $-13$. Are they the same?

The opposite of $-13$ is the number on the other side of zero, the same distance away: $13$. You can check it: $-13 + 13 = 0$, so $13$ is indeed the additive inverse.

The absolute value of $-13$ is its distance from zero, regardless of side:

$$
|{-13}| = 13.
$$

So yes — in this case the opposite and the absolute value are the same number, $13$. That happens whenever you start with a negative number. For a positive number, the two ideas pull apart: the opposite of $5$ is $-5$, but $|5| = 5$.

**Example 2.** Simplify $|{-15}| - |7| + |{-2}|$.

Evaluate each absolute value first, then combine.

$$
|{-15}| = 15
$$

$$
|7| = 7
$$

$$
|{-2}| = 2
$$

Now substitute back into the expression:

$$
15 - 7 + 2 = 10.
$$

A common slip here is to try to bring the minus sign inside the bars — for example, writing $|{-15}| = -15$. The bars always produce a non-negative number. Evaluate the absolute values first, then worry about the signs sitting outside them.

**Example 3.** Maya is tracking the daily temperature change in her town over a week. On Monday the temperature drops $7$ degrees, and on Tuesday it rises $4$ degrees. She records Monday as $-7$ and Tuesday as $+4$. Which day had the bigger **size** of change, and how much?

The question is about size, not direction, so it calls for absolute value. Compare:

$$
|{-7}| = 7 \quad \text{and} \quad |4| = 4.
$$

Monday's change has the bigger size, $7$ degrees. Tuesday's change is smaller, $4$ degrees. The difference between the sizes is $7 - 4 = 3$ degrees. Notice that if Maya just added the signed values, $-7 + 4 = -3$, she would be answering a different question — the net change over the two days, rather than the bigger daily swing.

## Common pitfalls

- **Thinking $|{-5}| = -5$.** The bars strip the sign; they never produce a negative result. Reading $|{-5}|$ as $5$ is correct.
- **Confusing opposite with absolute value for positive numbers.** The opposite of $5$ is $-5$, but $|5| = 5$. The two operations only agree when the input is negative or zero.
- **Forgetting the second answer to $|x| = k$.** When $k > 0$, there are two values that sit $k$ steps from zero: $k$ itself and $-k$. Always list both.
- **Dropping the bars too early.** In an expression like $3 + |{-2 \cdot 5}|$, finish the arithmetic inside the bars first: $|{-10}| = 10$, so the answer is $3 + 10 = 13$.

## Problems Involving Absolute Value and Opposites

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="absolute_value_and_opposites"></div>

## See Also

- [[Integers_And_The_Number_Line]]
- [[Adding_And_Subtracting_Integers]]
- [[Multiplying_And_Dividing_Integers]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
