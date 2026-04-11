---
title: "Solving Multi-Step Inequalities"
type: topic
aliases: ["Multi-Step Inequalities", "Solving Linear Inequalities"]
tags: ["#branch-algebra-1", "#topic-inequalities", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "3", section: "3.2"}
  - {book: "math_2", chapter: "5", section: "5.3"}
related:
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/pre_algebra/Solving_One_Step_And_Two_Step_Inequalities"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/algebra/Systems_Of_Linear_Inequalities"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/One_Step_Equations"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/The_Distributive_Property"
problem_type_ids: []
figures: []
summary: "Use the same moves as an equation, with one extra rule: flip the symbol whenever you multiply or divide by a negative."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Multi-Step Inequalities

# Solving Multi-Step Inequalities

Solving a multi-step inequality feels almost identical to solving a multi-step equation. You distribute, you combine like terms, you undo operations one layer at a time, and you keep the variable on one side and the constant on the other. The only genuinely new rule — and it is a rule you cannot afford to forget — is the **sign flip**: any time a negative scale factor lands on both sides (as a multiplier or a divisor), the inequality arrow turns around and points the other way.

Every step you take has to preserve the truth of the sentence. That is what the *properties of inequality* guarantee.

---

## The rules, in plain English

There are two families of moves you are allowed to make. The first is quiet and harmless; the second has a twist.

### Addition and subtraction preserve the symbol

If you add the same number to both sides, or subtract the same number from both sides, the inequality keeps pointing the same direction.

$$
a < b \quad\Longrightarrow\quad a + c < b + c
$$

$$
a < b \quad\Longrightarrow\quad a - c < b - c
$$

The same pattern holds for $>$, $\leq$, and $\geq$. The intuition: sliding both numbers by the same amount on the number line cannot change which one is on the left and which one is on the right.

### Multiplication and division: watch the sign of the scale factor

Multiplying both sides by a **positive** number is safe — the direction is preserved, exactly like for equations:

$$
\text{If}\ c > 0:\quad a < b \ \Longrightarrow\ ac < bc \ \ \text{and}\ \ \dfrac{a}{c} < \dfrac{b}{c}
$$

But multiplying or dividing by a **negative** number is a reflection, not a stretch. Every value jumps to the opposite side of zero, and the old "less than" becomes a "greater than":

$$
\text{If}\ c < 0:\quad a < b \ \Longrightarrow\ ac > bc \ \ \text{and}\ \ \dfrac{a}{c} > \dfrac{b}{c}
$$

That flip is the heart of this topic. To see why it has to happen, try it with numbers you trust. Start with the obvious truth $2 < 5$. Multiply both sides by $-1$. You get $-2$ and $-5$, and now $-2$ is the *larger* one: $-2 > -5$. The symbol had to flip or the sentence would turn into a lie.

### Strategy: mirror your equation-solving steps

In practice, the routine looks like this:

1. If parentheses are in the way, use [[The_Distributive_Property]] to clear them.
2. Combine like terms on each side.
3. Use addition or subtraction to gather the variable on one side and the constants on the other.
4. Divide or multiply to isolate the variable, and **if you divided or multiplied by a negative number, flip the symbol.**
5. Write the final answer and (optionally) sketch the solution set on a number line.

---

## Example 1: a two-step inequality

> Solve $4x - 9 < 11$.

The variable is trapped under a subtraction and a multiplication. Peel those layers off in reverse order of operations, just like an equation.

Add $9$ to both sides to undo the $-9$:

$$
4x - 9 + 9 < 11 + 9
$$

$$
4x < 20
$$

Divide both sides by $4$. Because $4$ is positive, the symbol stays the same:

$$
\dfrac{4x}{4} < \dfrac{20}{4}
$$

$$
x < 5
$$

**Solution.** Any value strictly less than $5$ works. As a check, try $x = 0$: the original becomes $4(0) - 9 = -9$, and $-9 < 11$ is true. As a counter-check, try $x = 5$: $4(5) - 9 = 11$, and $11 < 11$ is false — so $5$ is correctly excluded. On a number line, place an **open** circle at $5$ and shade left. In interval notation: $(-\infty,\, 5)$.

---

## Example 2: distribution plus combining like terms

> Solve $3(2x + 4) - x \geq 22$.

There is a set of parentheses, a loose $x$ outside them, and everything is compared to $22$. Distribute the $3$ first:

$$
3(2x + 4) - x \geq 22
$$

$$
6x + 12 - x \geq 22
$$

Combine the $x$ terms on the left: $6x - x = 5x$.

$$
5x + 12 \geq 22
$$

Subtract $12$ from both sides to isolate the variable term. Subtraction is a "safe" move — the symbol does not change:

$$
5x \geq 10
$$

Divide by $5$ (positive, so symbol keeps its direction):

$$
x \geq 2
$$

**Solution.** The solution set is "$2$ and everything to the right of $2$." Graph it with a **closed** circle at $2$ and shade right. In interval notation: $[2,\, \infty)$.

Quick check with $x = 2$: the original becomes $3(4 + 4) - 2 = 3(8) - 2 = 22$, and $22 \geq 22$ is true because equality is allowed. With $x = 5$: $3(10 + 4) - 5 = 42 - 5 = 37$, and $37 \geq 22$ holds. With $x = 0$ (outside the region): $3(0 + 4) - 0 = 12$, and $12 \geq 22$ is false, as expected.

---

## Example 3: dividing by a negative (the sign flip)

> Solve $-5x + 8 > 23$.

This is the classic problem where students lose half their marks if they are not careful. Start by subtracting $8$ from both sides. That move is addition-family, so the symbol is untouched:

$$
-5x + 8 - 8 > 23 - 8
$$

$$
-5x > 15
$$

Now the only layer left around $x$ is a factor of $-5$. To undo it, divide both sides by $-5$. The divisor is negative, so the symbol **must flip** from $>$ to $<$:

$$
\dfrac{-5x}{-5} < \dfrac{15}{-5}
$$

$$
x < -3
$$

**Solution.** The solution set is "every number strictly less than $-3$." Graph it with an **open** circle at $-3$ and shading to the left. Interval notation: $(-\infty,\, -3)$.

Always test the answer on the *original* inequality, not the one after the flip, because the flip is precisely the step most likely to go wrong. Try $x = -4$: $-5(-4) + 8 = 20 + 8 = 28$, and $28 > 23$ is true — so values below $-3$ really do work. Try $x = 0$ (which should *not* work): $-5(0) + 8 = 8$, and $8 > 23$ is false, as expected. The flip was correct.

Notice what would have happened without the flip: we would have written $x > -3$, which would say $0$ is a solution — and you just saw that $0$ makes the left side equal to $8$, nowhere near being larger than $23$. The flip is not an arbitrary formality; it is what keeps the sentence honest.

---

## A word problem to tie it together

> A streaming service charges a flat fee of $\$12$ per month plus $\$0.40$ per additional episode over the included bundle. A competing service charges a flat $\$20$ per month with unlimited episodes. For how many extra episodes $e$ per month is the first plan cheaper than the second?

Translate the question into an inequality. The first plan's cost is $12 + 0.40e$, and "cheaper than the second" means that cost should be strictly less than $20$:

$$
12 + 0.40e < 20
$$

Subtract $12$ from both sides:

$$
0.40e < 8
$$

Divide by $0.40$ — a positive number, so the symbol stays:

$$
e < 20
$$

So the first plan is cheaper whenever you watch fewer than $20$ extra episodes per month. At exactly $20$ the two plans tie at $\$20$; beyond that, the flat-rate plan pulls ahead. Inequalities are the natural language for "cheaper than," "at most," "at least," and every other comparison you meet in real budgeting.

---

## Common pitfalls

- **Forgetting the sign flip.** This is the single most common error in the entire algebra-1 curriculum. Any time a $-$ appears in front of your variable, circle it as a reminder. When the last step divides or multiplies both sides by a negative, the symbol reverses — no exceptions.
- **Flipping when you shouldn't.** The flip only happens because of a negative *scale factor*. Adding or subtracting a negative constant — like adding $-7$ to both sides to undo a $+7$ — does **not** flip the symbol.
- **Flipping twice.** Some students flip when distributing a negative factor, and then flip again when dividing by a negative later. Only the multiplication or division step flips. Distribution on its own does not.
- **Mixing up the endpoint rule in the graph.** After you solve, remember to match the symbol to the circle type: $<$ or $>$ gives an open circle; $\leq$ or $\geq$ gives a closed one. If you reversed the symbol mid-solve, the new symbol is the one that determines the circle.
- **Trusting the flipped inequality for your check.** Always substitute your candidate back into the *original* problem, not the simplified one. If the flip was wrong, only the original will expose the error.
- **Dropping a negative when distributing.** When you distribute $-3$ across $(x - 4)$, the second term becomes $+12$, not $-12$. This is an arithmetic slip, not an inequality rule, but it shows up constantly in multi-step problems.

---

## Prerequisites

You will build on several skills at once. Make sure each of these is solid:

- [[One_Step_Equations]] — the inverse-operation idea is the same, just applied to a comparison
- [[Multi_Step_Equations]] — distribution, combining like terms, and moving variables across the equals sign all carry over
- [[Integers_And_The_Number_Line]] — every answer lives on a number line, and negatives are where most of the traps are
- [[Multiplying_And_Dividing_Integers]] — so the sign flip actually feels reasonable instead of scary
- [[The_Distributive_Property]] — for clearing parentheses in step 1 of most problems

---

## Problems Involving Solving Multi-Step Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_multi_step_inequalities"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Inequalities_And_Their_Graphs]]
- [[Solving_One_Step_And_Two_Step_Inequalities]]
- [[Compound_Inequalities]]
- [[Absolute_Value_Inequalities]]
- [[Systems_Of_Linear_Inequalities]]
- [[Multi_Step_Equations]]
- [[Linear_Functions]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
