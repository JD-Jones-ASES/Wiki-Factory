---
title: "One-Step Equations"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-linear", "#key-technique", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Equations_With_Variables_On_Both_Sides"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Translating_Words_To_Algebraic_Expressions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "Uncover the value of x by doing the single opposite operation to both sides."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > One-Step Equations

# One-Step Equations

Picture an equation as a balance scale. On the left pan sits a mystery weight called $x$, maybe joined by a known weight or scaled up by a factor. On the right pan sits a number. The scale is perfectly level because the two pans weigh the same. Your job is to strip away everything that is clinging to $x$ so that the left pan shows $x$ alone — and whatever ends up on the right pan is the mystery weight's value. For a **one-step equation**, that stripping away takes exactly one move.

The single move always has the same flavor. Look at what is happening to $x$ on the left pan — is a number being added to it, subtracted from it, multiplied onto it, or dividing into it? Then perform the opposite operation on **both pans** at once. The opposite undoes the original, the variable comes out alone, and whatever remains on the other pan is your answer. The reason this works is that doing the same thing to both pans keeps the scale level, and the opposite operation is the one that cancels out the original.

## What it means / The idea

A one-step equation is any equation that can be solved with a single inverse operation. The four shapes you meet most often are

$$
x + a = b, \qquad x - a = b, \qquad ax = b, \qquad \frac{x}{a} = b.
$$

In each case, something is being done to $x$ and your goal is to cancel it. The four inverse operations pair up neatly: addition and subtraction undo each other, and multiplication and division undo each other. That pairing gives you a one-move plan for every shape you will see.

| Equation shape | What is happening to $x$ | Inverse move |
|---|---|---|
| $x + a = b$ | $a$ was added | subtract $a$ from both sides |
| $x - a = b$ | $a$ was subtracted | add $a$ to both sides |
| $ax = b$ | $x$ was multiplied by $a$ | divide both sides by $a$ |
| $x/a = b$ | $x$ was divided by $a$ | multiply both sides by $a$ |

You never need more than one inverse for this topic. If the equation has two things clinging to $x$ at the same time — say $3x + 5 = 20$ — that is a **two-step** problem and belongs on the [[Multi_Step_Equations]] page.

## How it works / The procedure

1. **Read the equation.** Identify which single operation is wrapped around $x$.
2. **Pick the inverse.** Pair up from the table above.
3. **Apply the inverse to both sides at once.** Writing the move explicitly on each side is a habit that pays off later when equations get longer.
4. **Simplify each side.** You should now see $x$ standing alone on one side and a number on the other.
5. **Check your work.** Substitute your answer back into the original equation and verify both sides agree.

The last step is optional but highly recommended while you are learning. Catching a sign error or a bad division takes seconds; finding out on a test that you have been making the same mistake for three months takes longer.

## Why it works

Every equation is a statement that two expressions name the same number. If you do the same operation to both sides, the statement stays true — you have not changed what the sides equal, only how they are written. Choose that operation to be the inverse of whatever was done to $x$, and the left side collapses down to $x$ by itself. In short: equality is preserved under same-operation-both-sides, and inverses cancel. Those two ideas together let you drag $x$ out into the open.

## Worked examples

### Example 1

Maya is tallying up the mileage she logged with her hiking club. She knows the equation $3x = 18$ describes the unknown number of weekend hikes $x$ (each hike is $3$ miles) that produced $18$ miles total. Determine $x$.

On the left side, $x$ is being multiplied by $3$. The inverse of multiplying by $3$ is dividing by $3$, so divide both sides by $3$:

$$
\frac{3x}{3} = \frac{18}{3}
$$

$$
x = 6.
$$

Maya went on $6$ hikes. A quick check: $3 \cdot 6 = 18$, which matches the original equation.

### Example 2

At a photography class, Kai was told that after giving away $7$ of his printed photos he had $12$ left. If $x$ is the number of prints he started with, the relationship is $x - 7 = 12$. What is $x$?

On the left side, $7$ is being subtracted from $x$. The inverse of subtracting $7$ is adding $7$, so add $7$ to both sides:

$$
x - 7 + 7 = 12 + 7
$$

$$
x = 19.
$$

Kai started with $19$ prints. Check: $19 - 7 = 12$. The original equation holds.

### Example 3

Priya is splitting a large tray of brownies from the school bakery into four equal portions, and each portion has $5$ brownies in it. If $x$ is the total number of brownies in the tray, then $x/4 = 5$. Compute $x$.

On the left side, $x$ is being divided by $4$. The inverse of dividing by $4$ is multiplying by $4$, so multiply both sides by $4$:

$$
4 \cdot \frac{x}{4} = 4 \cdot 5
$$

$$
x = 20.
$$

The tray holds $20$ brownies. Check: $20/4 = 5$. 

## Common pitfalls

- **Applying the inverse to only one side.** The equation is a balanced scale. If you subtract a number from the left pan and forget to subtract it from the right pan, the scale tips and your answer will be wrong. Write the move on both sides every time.
- **Picking the wrong inverse.** If the equation is $x + 9 = 2$, the opposite of $+9$ is $-9$, not $+9$ again. A tired brain sometimes adds when it should subtract; slowing down on the first move is worth it.
- **Freezing when the answer is negative.** If the equation says $x + 12 = 7$, then $x = -5$. That is a real, valid solution. Negative answers appear all the time and do not mean you made a mistake — check the original to confirm.
- **Confusing $ax = b$ with $x + a = b$.** A coefficient glued to $x$ (like $5x$) is multiplication, and it is undone by division. A number separated by a plus or minus sign is addition/subtraction, and it is undone by its opposite.
- **Skipping the check.** One back-substitution catches most of the errors the preceding bullets cause. It costs you ten seconds.

## Problems Involving One-Step Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="one_step_equations"></div>

## See Also

- [[Multi_Step_Equations]] — the next level up, when more than one move is needed
- [[Equations_With_Variables_On_Both_Sides]] — $x$ appears on the left and the right
- [[Solving_Equations_In_One_Variable]] — the broader setting for this topic
- [[Literal_Equations_And_Formulas]] — solving for a variable when the other side has letters too
- [[Variables_And_Algebraic_Expressions|Variables and Algebraic Expressions]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
