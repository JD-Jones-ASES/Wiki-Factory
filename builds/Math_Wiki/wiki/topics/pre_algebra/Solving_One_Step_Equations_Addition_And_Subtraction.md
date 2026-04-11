---
title: "Solving One-Step Equations (Addition and Subtraction)"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-linear", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Solving_One_Step_Equations_Multiplication_And_Division"
  - "topics/pre_algebra/Solving_Two_Step_Equations"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "Undo addition with subtraction, undo subtraction with addition, and keep the equation balanced the whole way."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Solving One-Step Equations (Addition and Subtraction)

# Solving One-Step Equations (Addition and Subtraction)

The first equations you ever meet in algebra look almost embarrassingly simple: $x + 7 = 12$. Almost anyone can see the answer by inspection. The point of writing these out step by step is not that the arithmetic is hard — it is that the *move* you make to turn $x + 7 = 12$ into $x = 5$ is the same move you will use later on equations where inspection is impossible. The habit has to be built on easy problems or it will never show up on the hard ones.

Every equation in this lesson has exactly one variable and exactly one operation glued to it, and that operation is either addition or subtraction. Your job is to peel that operation off using its inverse so that the variable is left alone on one side.

## The balance idea

Picture an old-fashioned two-pan balance scale. On one pan sits the left side of the equation, on the other pan sits the right side. An equals sign is a claim that the two pans weigh exactly the same. If you change one pan in any way — add weight, remove weight, double its contents — the pans will tip. The only changes that keep the scale level are the ones you make to **both** pans at once.

Solving an equation is just this balancing game. You want to clear everything off one pan except the variable, and the rule is that every move you make to clear the pan must also be made to the other pan so the two sides stay equal. Keep the equation balanced at every step and whatever final value you read off on the right-hand side is the solution.

## How to do it

Addition and subtraction are **inverse operations**. Addition undoes subtraction; subtraction undoes addition. That is the whole lever you need.

**Case 1: the variable has something added to it.** The equation looks like $x + b = c$. Subtract $b$ from each side. The $+b$ on the left gets cancelled by $-b$, leaving $x$ alone, and the right side updates from $c$ to $c - b$.

$$
x + b = c \quad \Longrightarrow \quad x = c - b
$$

**Case 2: the variable has something subtracted from it.** The equation looks like $x - b = c$. Add $b$ to each side. The $-b$ on the left is cancelled by $+b$, leaving $x$ alone, and the right side updates from $c$ to $c + b$.

$$
x - b = c \quad \Longrightarrow \quad x = c + b
$$

After any solve, substitute the answer back into the original equation. If both sides come out equal, the answer is correct. That check is not optional — it catches sign flips and arithmetic slips cheaply.

## Why it works

The equals sign is not a command ("compute this"); it is a statement ("these two things are the same number"). If two things are the same number and you add the same amount to each, they are still the same number. If you remove the same amount from each, they are still the same number. This is the **addition property of equality**: for any numbers $a$, $b$, $c$, if $a = b$ then $a + c = b + c$. The subtraction property is its twin.

Those properties say that whatever change keeps the scale balanced is legal. The particular change that helps is the one that cancels the operation attached to the variable — subtraction cancels addition, and addition cancels subtraction. That is why you pick the inverse.

## Worked examples

### Example 1: undoing addition

Determine the value of $x$ that makes $x + 9 = 23$ a true statement.

The variable has $9$ added to it. To peel the $9$ off, use the inverse of addition, which is subtraction. Remove $9$ from each side at once:

$$
x + 9 - 9 = 23 - 9
$$

The left side collapses: $9 - 9 = 0$, leaving just $x$. The right side simplifies to $14$:

$$
x = 14
$$

Check by returning to the original equation and substituting: $14 + 9 = 23$. Both sides match, so the answer stands.

### Example 2: undoing subtraction

Find the value of $x$ for which $x - 14 = 5$.

Now the variable has $14$ taken away from it. The inverse of subtraction is addition, so raise each side by $14$:

$$
x - 14 + 14 = 5 + 14
$$

On the left, $-14 + 14 = 0$, so $x$ is left alone. On the right, $5 + 14 = 19$:

$$
x = 19
$$

Check: $19 - 14 = 5$. Confirmed.

A sanity check that is worth running: does the answer make physical sense? The equation says "$x$ minus $14$ is only $5$," which tells you $x$ must be bigger than $14$. It is — $19$ is — so the answer passes the plausibility test even before the arithmetic check.

### Example 3: variable on the right side

What is the value of $x$ for which $18 = x + 6$?

Do not be thrown off by the variable sitting on the right. An equation reads the same both ways; $18 = x + 6$ says exactly what $x + 6 = 18$ says. Subtract $6$ from each side to strip the $+6$ off the variable:

$$
18 - 6 = x + 6 - 6
$$

The right side collapses to $x$, and the left side simplifies to $12$:

$$
12 = x
$$

which is usually rewritten as $x = 12$. Check by substituting: $x + 6 = 12 + 6 = 18$. The answer works.

This example matters because real problems — especially word problems — do not always hand you the variable on the left. Get comfortable operating on whichever side it lives on, and rewrite at the end for readability.

## Common pitfalls

- **Applying the operation to only one side.** If you subtract $7$ from the left, you must subtract $7$ from the right. Doing just one tips the scale and poisons every later step.
- **Picking the same operation as the one attached to the variable.** If the equation shows $x + 9 = 23$, adding $9$ to each side does not help — it only piles more on top. You need the **inverse**: subtraction.
- **Losing the sign on the variable side.** In $x - 14 = 5$, the $14$ is being subtracted, not added. Students sometimes write "$x = 5 - 14 = -9$" by accident. The inverse of $-14$ is $+14$, so the answer is $x = 19$, not $x = -9$.
- **Skipping the substitution check.** A thirty-second substitution catches almost every arithmetic slip. Not checking is the single most expensive habit in early algebra.

## Problems Involving Solving One-Step Equations (Addition and Subtraction)

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_one_step_equations_addition_and_subtraction"></div>

## See Also

- [[Solving_One_Step_Equations_Multiplication_And_Division]]
- [[Solving_Two_Step_Equations]]
- [[Variables_And_Algebraic_Expressions]]
- [[Adding_And_Subtracting_Integers]]
- [[One_Step_Equations|One-Step Equations (Algebra 1)]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
