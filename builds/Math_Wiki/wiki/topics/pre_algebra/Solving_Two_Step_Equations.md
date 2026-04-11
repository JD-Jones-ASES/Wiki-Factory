---
title: "Solving Two-Step Equations"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-linear", "#skill-algebraic-manipulation", "#skill-multi-step", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Solving_One_Step_Equations_Addition_And_Subtraction"
  - "topics/pre_algebra/Solving_One_Step_Equations_Multiplication_And_Division"
  - "topics/pre_algebra/Order_Of_Operations"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Solving_One_Step_Equations_Addition_And_Subtraction"
  - "topics/pre_algebra/Solving_One_Step_Equations_Multiplication_And_Division"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "Unwrap the variable in the reverse order of operations: undo addition or subtraction first, then undo the multiplication or division."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Solving Two-Step Equations

# Solving Two-Step Equations

A **two-step equation** is exactly what its name says: it takes two inverse moves to get the variable alone. The most common shape is $ax + b = c$. Here two different things are happening to the variable — it is first being multiplied by $a$, and then $b$ is being added to the result. To work back to $x$ by itself, you have to undo both.

The interesting move is the order. When you compute $ax + b$ with a given value of $x$, you multiply first and then add: that is what the order of operations tells you to do. When you *reverse* that chain to solve for $x$, you unwind it in the opposite order — undo the addition first, then undo the multiplication. Getting the order right is the entire trick of two-step equations, and almost every wrong answer you see in this lesson comes from ignoring it.

## The idea: unwrap inside-out

Imagine the variable as a present buried inside two layers of wrapping. The inner layer is "$x$ has been multiplied by $a$." The outer layer is "and then $b$ was added." If you want to get to the present, you take off the **outer** wrapper first. So you undo the addition first — strip off the $+b$ — and only then do you undo the multiplication by $a$.

In shorthand: evaluate outside-in, solve inside-out. It is the same rule you use to untie a pair of shoes — you loosen the last knot you tied, not the first one.

The four most common shapes are all handled the same way:

- $ax + b = c$: undo the addition, then undo the multiplication.
- $ax - b = c$: undo the subtraction (add $b$), then undo the multiplication.
- $\tfrac{x}{a} + b = c$: undo the addition, then undo the division (multiply by $a$).
- $b - ax = c$: undo the $b$ (subtract $b$), then undo the multiplication by $-a$.

In every case the first move pulls a constant off the side holding the variable, and the second move peels a coefficient off the variable itself.

## How to do it

1. Identify the variable and look at the operations attached to it.
2. Find the constant term on the same side as the variable. Move it to the other side by applying its inverse to both sides. That step leaves the variable's term alone on one side.
3. Look at the coefficient now stuck to the variable. Apply its inverse to both sides — divide if it is multiplying, multiply if it is dividing.
4. Read off the answer as $x = \text{something}$, then substitute it back into the original equation as a check.

If the equation is more tangled than this — parentheses, variables on both sides, like terms needing to be combined — the same basic order still applies, but you may have to do some cleanup first before this two-step routine kicks in.

## Why it works

The reason you undo operations in reverse order is the same reason you put shoes on before tying them. Multiplication is an "inner" operation on the variable (it touches $x$ directly), and the constant term is "outer" (it sits alongside a thing already built from $x$). The order of operations wraps these layers in a fixed way. If you try to undo the inner wrapper first, you end up fighting the outer one, and your work multiplies in complexity.

Undoing addition first strips the equation down to a one-step equation of the form $ax = k$, which you already know how to handle from the previous lesson on [[Solving_One_Step_Equations_Multiplication_And_Division]]. That is really the secret: a two-step equation is just a warm-up layer on top of a one-step equation. Remove the warm-up, solve the one-step problem underneath, done.

## Worked examples

### Example 1: $ax + b = c$

Determine the value of $x$ for which $3x - 4 = 11$.

The variable has two things happening to it: multiplication by $3$ and subtraction of $4$. The subtraction is the outer layer, so address it first. Add $4$ to each side to neutralise the $-4$:

$$
3x - 4 + 4 = 11 + 4
$$

which simplifies to

$$
3x = 15.
$$

Now only the multiplication is left. Divide each side by $3$:

$$
\frac{3x}{3} = \frac{15}{3}
$$

$$
x = 5
$$

Check by substituting back into the original equation: $3 \cdot 5 - 4 = 15 - 4 = 11$. Both sides match, so $x = 5$ is correct.

### Example 2: a fractional coefficient

Find the value of $x$ for which $\dfrac{x}{2} + 7 = 13$.

Two operations again. The $7$ is the constant being added, so it is the outer layer — undo it first. Remove $7$ from each side:

$$
\frac{x}{2} + 7 - 7 = 13 - 7
$$

$$
\frac{x}{2} = 6
$$

That leaves a one-step equation where $x$ is divided by $2$. The inverse of division is multiplication, so multiply each side by $2$:

$$
2 \cdot \frac{x}{2} = 2 \cdot 6
$$

$$
x = 12
$$

Check by substitution: $\tfrac{12}{2} + 7 = 6 + 7 = 13$. The value of $x$ is confirmed.

A classic mistake here is to try to "clear the fraction" immediately by multiplying everything by $2$ before dealing with the $+7$. That does work, but it forces you to distribute the $2$ carefully across the whole left side. Handling the constant first keeps the arithmetic cleaner.

### Example 3: watch for sign traps

Determine all $x$ satisfying $5 - 2x = 1$.

This equation has a subtle twist: the variable's term is $-2x$, not $2x$. That minus sign has to travel with the $2$. The constant on the variable's side is the $5$, sitting out front. Remove it by subtracting $5$ from both sides:

$$
5 - 2x - 5 = 1 - 5
$$

$$
-2x = -4
$$

Now the variable is being multiplied by $-2$, so divide each side by $-2$ — including the sign:

$$
\frac{-2x}{-2} = \frac{-4}{-2}
$$

$$
x = 2
$$

Check: $5 - 2 \cdot 2 = 5 - 4 = 1$. The answer is correct. If you had divided by $2$ instead of $-2$ in the last step, you would have ended up with $-x = -2$, which is one extra move away from the real answer. Getting the sign right on the first try saves you that extra work and prevents the most common slip in this kind of problem.

## Common pitfalls

- **Dividing before subtracting the constant.** If you divide $3x - 4 = 11$ by $3$ first, you have to remember that the $-4$ also gets divided, which is easy to miss. Undo the addition or subtraction first; then handle the coefficient.
- **Dropping the sign on the variable term.** In $5 - 2x = 1$, the variable's coefficient is $-2$, not $2$. Treat the minus as part of the number.
- **Changing only one side.** Every operation — every single one — has to be performed on both sides at once. Otherwise the equation stops being true and every later step is working on a fake equation.
- **Stopping too early.** An equation is not solved until you can write $x = \text{something}$. Lines like $-x = 6$ need one more step (multiply each side by $-1$) before you have the answer.
- **Forgetting the check.** A substitution check is the single most effective debugger you have. Skipping it is skipping the cheapest insurance in math.

## Problems Involving Solving Two-Step Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_two_step_equations"></div>

## See Also

- [[Solving_One_Step_Equations_Addition_And_Subtraction]]
- [[Solving_One_Step_Equations_Multiplication_And_Division]]
- [[Order_Of_Operations]]
- [[Variables_And_Algebraic_Expressions]]
- [[Multi_Step_Equations|Multi-Step Equations (Algebra 1)]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
