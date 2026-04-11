---
title: "Adding and Subtracting Integers"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Order_Of_Operations"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Absolute_Value_And_Opposites"
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
problem_type_ids: []
figures: []
summary: "Add and subtract signed whole numbers by walking the number line instead of memorizing sign rules."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Adding and Subtracting Integers

# Adding and Subtracting Integers

Most students learn sign rules the hard way — as a chant. "Two negatives make a positive, different signs means subtract, same signs means add..." The chant works often enough to get through a worksheet, but it leaves the reasoning buried. There is a much better way. Picture the number line. Every addition is a walk to the right or to the left, every subtraction is the same walk in reverse, and every strange-looking sign combination reduces to "which direction was I facing?" Once you can see the walks, the sign rules fall out on their own.

## What it means

An **integer** is any whole number, positive or negative, plus zero. Adding and subtracting integers is the pre-algebra skill of combining two of these signed whole numbers into a single signed whole number. The difficult part is not the arithmetic — it is keeping track of what the sign of the answer should be.

Two quantities are doing the work behind the scenes:

- The **magnitude** of an integer is how far from zero it sits, with the sign stripped off. Magnitude is what $|{-7}| = 7$ is measuring — how many units of distance $-7$ represents. Another name for magnitude is **absolute value**.
- The **direction** of an integer is whether it lives on the positive side of zero (to the right on the number line) or the negative side (to the left). The sign is just a compass.

With those two ingredients, addition and subtraction turn into trips along the number line. A positive number is a step to the right. A negative number is a step to the left. Adding means take the step. Subtracting means take the opposite step.

The formal summary looks like this. For addition of two integers $a$ and $b$:

$$
a + b \;=\; \text{start at } a, \text{ then walk } b \text{ steps (right if } b>0, \text{ left if } b<0)
$$

For subtraction, rewrite it as "add the opposite" and you are back to addition:

$$
a - b \;=\; a + (-b)
$$

That second line is the single most important equation on this page. Every subtraction problem, no matter how ugly, collapses into an addition once you flip the sign of the number being taken away.

## How it works

Here is the rule written in plain English, derived from the number line:

- **Same direction.** If both numbers point the same way (both positive or both negative), you are stacking two walks in the same direction. Add the magnitudes and keep the shared sign. So $4 + 9 = 13$ and $(-4) + (-9) = -13$.
- **Opposite directions.** If the numbers point opposite ways (one positive, one negative), they are partially canceling. Subtract the smaller magnitude from the larger, and carry the sign of whichever number had the larger magnitude. So $9 + (-4) = 5$ (positive because $9$ is bigger in magnitude than $4$), and $(-9) + 4 = -5$ (negative because $9$ is bigger).
- **Subtract by flipping the sign.** To compute $a - b$, change it to $a + (-b)$ and fall back to the two addition rules above. Subtracting $3$ becomes adding $-3$. Subtracting $-3$ becomes adding $+3$.

## Why it works

The number-line picture is the whole justification. A positive integer like $+5$ represents a displacement of five units to the right of wherever you are. A negative integer like $-5$ represents a displacement of five units to the left. When you add two displacements, you chain them — take the first walk, then take the second — and land wherever the chained walks end. If the walks go in the same direction, they accumulate. If they go in opposite directions, part of one walk cancels part of the other, and only the leftover survives. That is exactly the "subtract and carry the larger sign" rule.

Subtraction is trickier only because the word hides the motion. When you "subtract $b$," you undo the walk that $b$ would have asked for. Undoing a walk to the right is the same as walking to the left, and undoing a walk to the left is the same as walking to the right. That is the content of the $a - b = a + (-b)$ identity — and it is why subtracting a negative number ends up pushing you in the positive direction.

## Worked examples

### Example 1

Compute $-7 + 12$.

The two addends point in opposite directions. Start by comparing their magnitudes: $|-7| = 7$ and $|12| = 12$. The positive number has the larger magnitude, so the final answer will be positive. Subtract the smaller magnitude from the larger:

$$
12 - 7 = 5
$$

Attach the positive sign: $-7 + 12 = 5$. Number-line check: start at $-7$, take twelve steps to the right. After seven steps you arrive at zero; five more steps carry you to $+5$. Same answer.

### Example 2

A hiking club member starts the weekend with $\$45$ in her wallet, spends $\$18$ on snacks at the trailhead store, and is handed a $\$10$ refund for a trip fee that was accidentally charged twice. What does her wallet look like after the refund?

Write the running total as an integer expression. Spending is a subtraction; a refund is addition:

$$
45 - 18 + 10
$$

Evaluate left to right. First, $45 - 18$. Rewrite as $45 + (-18)$. Opposite directions, so subtract magnitudes: $45 - 18 = 27$, and since $45$ had the larger magnitude, the answer keeps the positive sign. So the first step gives $27$. Then add $10$: $27 + 10 = 37$. Her wallet now holds $\$37$.

### Example 3

Compute $-6 - (-11)$.

This is the classic "double negative" setup, and the $a - b = a + (-b)$ identity dissolves it in one line. The number being subtracted is $-11$, and the opposite of $-11$ is $+11$. Rewrite:

$$
-6 - (-11) = -6 + 11
$$

Now it is an ordinary opposite-direction addition. Magnitudes $6$ and $11$, with the positive winning the size contest, so the answer will be positive. Subtract: $11 - 6 = 5$. Attach the positive sign: $-6 - (-11) = 5$. On the number line: start at $-6$, take eleven steps to the right, and land at $+5$. The two descriptions agree.

## Common pitfalls

- **Treating a stray minus sign as a subtraction.** In an expression like $-7 + 12$, the first minus is part of the number, not an operation. Some students read it as "zero minus seven plus twelve" and get confused about whether the sign goes with the $7$ or floats. When in doubt, group the number with its sign: $(-7) + 12$.
- **Rushing the double-negative rewrite.** The identity $a - (-b) = a + b$ is guaranteed safe, but only if you change the operation and the sign of $b$ at the same time. Dropping only one of the two changes is the leading source of sign errors.
- **Carrying the wrong sign on opposite-direction sums.** The sign of the answer is determined by the addend with the larger magnitude, not by which addend was written first. $-12 + 5$ is negative because $12$ beats $5$ in size, regardless of the order.
- **Forgetting that zero is the tie-breaker.** If the two addends have the same magnitude but opposite signs — say $-8 + 8$ — the walks cancel exactly and the answer is zero. That is not a special case; it is the opposite-direction rule when neither side wins.

## Problems Involving Adding and Subtracting Integers

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="adding_and_subtracting_integers"></div>

## See Also

- [[Integers_And_The_Number_Line]]
- [[Multiplying_And_Dividing_Integers]]
- [[Order_Of_Operations]]
- [[Absolute_Value_And_Opposites]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
