---
title: "Solving One-Step and Two-Step Inequalities"
type: topic
aliases: ["One-Step Inequalities", "Two-Step Inequalities"]
tags: ["#branch-pre-algebra", "#topic-inequalities"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "5", section: "5.2"}
related:
  - "topics/pre_algebra/Writing_And_Graphing_Inequalities"
  - "topics/pre_algebra/Solving_One_Step_Equations_Addition_And_Subtraction"
  - "topics/pre_algebra/Solving_One_Step_Equations_Multiplication_And_Division"
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Writing_And_Graphing_Inequalities"
  - "topics/pre_algebra/Solving_One_Step_Equations_Addition_And_Subtraction"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
problem_type_ids: []
figures: []
summary: "Isolate the variable just like in an equation, with one crucial twist: flip the inequality whenever you multiply or divide both sides by a negative."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Solving One-Step and Two-Step Inequalities

# Solving One-Step and Two-Step Inequalities

Solving an inequality looks almost identical to solving an equation. You still undo addition with subtraction, multiplication with division, and so on, one step at a time, with the goal of getting the variable alone on one side. The answer is the set of every value that makes the sentence true.

The only surprise — and it is the rule that gets forgotten in half the mistakes you will see — is what happens when you multiply or divide both sides by a negative number. The inequality **flips**. We will return to this again and again.

---

## Add or subtract: the easy rule

Adding the same number to both sides of an inequality, or subtracting the same number from both sides, does not change the direction of the inequality. If $a < b$, then $a + 7 < b + 7$, and $a - 3 < b - 3$. The same is true for $>$, $\leq$, and $\geq$. You can picture both sides of the inequality sliding along a number line by the same distance, in the same direction — they keep their relative order.

So for a one-step inequality like $x + 5 < 12$, you undo the $+5$ by subtracting $5$ from both sides, exactly as you would if this were an equation, and the symbol stays pointing the same way.

---

## Multiply or divide: the twist

Multiplying or dividing both sides by a **positive** number is also harmless. If $a < b$ and $c > 0$, then $ac < bc$: scaling both sides by a positive factor preserves their order.

A **negative** factor is different. Think about what happens to two numbers on the number line when you negate them. If $3 < 5$, the numbers $3$ and $5$ keep their relative spacing when you subtract $4$ from each ($-1 < 1$, still). But multiply both by $-1$, and you get $-3$ and $-5$: the order reverses, because $-5$ is actually to the left of $-3$ on the number line. So $-3 > -5$. The inequality has flipped.

The rule is the same whenever a negative factor multiplies or divides both sides:

$$
\text{If } a < b \text{ and } c < 0, \text{ then } ac > bc.
$$

Every textbook, every test, every puzzle involving inequalities hinges on this one move. When you see a negative coefficient on your variable, your alarm should go off: "if I divide, I need to flip."

---

## Two-step inequalities

A two-step inequality has two operations blocking the variable — usually a multiplication and an addition, as in $3x - 7 > 5$. You clear them in the reverse of the order of operations: undo the addition or subtraction first, and then undo the multiplication or division last. This is the same game plan used for two-step equations, with the added discipline of checking whether any of your moves involves a negative coefficient that would flip the symbol.

---

## Example 1: a one-step inequality with subtraction

> Solve $y - 6 \geq 2$ and describe the graph.

There is one thing in the way of $y$: the $-6$. Add $6$ to both sides:

$$
y - 6 \geq 2
$$

$$
y - 6 + 6 \geq 2 + 6
$$

$$
y \geq 8
$$

The solution is every number from $8$ onward. On a number line, draw a closed circle at $8$ (because the symbol is $\geq$, the boundary is included) and shade to the right.

**Check.** Try $y = 10$. Then $10 - 6 = 4$, and $4 \geq 2$ is true. Good.

---

## Example 2: dividing by a negative (the sign flip)

> Solve $-4x < 20$.

The coefficient on $x$ is $-4$. To isolate $x$, divide both sides by $-4$. Because $-4$ is negative, the inequality must **reverse** — the $<$ becomes $>$:

$$
-4x < 20
$$

$$
\dfrac{-4x}{-4} > \dfrac{20}{-4}
$$

$$
x > -5
$$

So every value greater than $-5$ is a solution. Note that if you had forgotten to flip, you would have written $x < -5$, which is exactly the wrong half of the number line.

**Check.** Try $x = 0$, which should satisfy $x > -5$. Substitute into the original: $-4(0) = 0$, and $0 < 20$ is true. Now try a value that should fail — say $x = -6$, which is not greater than $-5$. Then $-4(-6) = 24$, and $24 < 20$ is false, so $-6$ is correctly excluded. The flipped symbol gave the right answer.

Any time a negative number touches both sides of an inequality through multiplication or division, the symbol flips. Every time. No exceptions.

---

## Example 3: a two-step inequality

> Solve $5n + 3 \leq 23$.

Two operations sit between $n$ and the goal of standing alone: the $\cdot 5$ and the $+3$. Peel them off in reverse. First, subtract $3$ from both sides to get rid of the constant term:

$$
5n + 3 \leq 23
$$

$$
5n + 3 - 3 \leq 23 - 3
$$

$$
5n \leq 20
$$

Now divide both sides by $5$. Since $5$ is positive, the symbol stays the same:

$$
\dfrac{5n}{5} \leq \dfrac{20}{5}
$$

$$
n \leq 4
$$

Every number $4$ or smaller is a solution. The graph is a closed circle at $4$ shaded to the left.

**Check.** Try $n = 4$: $5(4) + 3 = 23 \leq 23$. True. Try $n = 0$: $5(0) + 3 = 3 \leq 23$. Also true. The solution checks out.

---

## Example 4: a two-step inequality with a negative coefficient

> Solve $-2x + 9 > 1$.

Start by subtracting $9$ from both sides to isolate the $x$-term. Adding or subtracting does **not** flip the inequality:

$$
-2x + 9 > 1
$$

$$
-2x > 1 - 9
$$

$$
-2x > -8
$$

Now divide both sides by $-2$. This is the flip step — the $>$ becomes $<$:

$$
\dfrac{-2x}{-2} < \dfrac{-8}{-2}
$$

$$
x < 4
$$

**Check.** Pick a value that should work, say $x = 0$: $-2(0) + 9 = 9$, and $9 > 1$. True. Pick a value that should fail, say $x = 5$: $-2(5) + 9 = -1$, and $-1 > 1$ is false. The answer checks out on both sides.

If you forget to flip at the division step, you end up with $x > 4$, which is the exact opposite solution set. That is why the sign flip is drilled so heavily — one slip reverses the entire answer.

---

## Common pitfalls

- **Forgetting to flip when dividing or multiplying by a negative.** Far and away the number-one mistake in this whole topic. Any time you scale both sides by a negative number, the inequality symbol reverses. Make a habit of asking "is this factor negative?" before you divide.
- **Flipping when you should not.** The flip only applies to multiplication and division by a negative. Adding or subtracting a negative number — say, adding $-3$ to both sides — does **not** flip the symbol. The rule is about scaling, not about signs in general.
- **Treating $-x$ as if it were a positive variable.** If you end up at $-x < 7$, the variable still has a negative coefficient. Multiply both sides by $-1$ (flipping the symbol) to get $x > -7$, not $x < -7$.
- **Messing up the order of undoing operations.** On a two-step problem, undo addition and subtraction first, then multiplication and division. Doing it in the opposite order can turn a clean two-step problem into a messy fraction mess.

---

## Prerequisites

Before tackling practice problems, make sure you are solid on:

- [[Writing_And_Graphing_Inequalities]] — you have to be able to read the symbols and picture the solution before you solve anything
- [[Solving_One_Step_Equations_Addition_And_Subtraction]] — the inverse-operation technique is the same; only the symbol rule is new
- [[Multiplying_And_Dividing_Integers]] — so the signs involved in the flip-step never catch you off guard

---

## Problems Involving Solving One-Step and Two-Step Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_one_step_and_two_step_inequalities"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Writing_And_Graphing_Inequalities]]
- [[Inequalities_And_Their_Graphs]]
- [[Solving_Multi_Step_Inequalities]]
- [[Compound_Inequalities]]
- [[Absolute_Value_Inequalities]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
