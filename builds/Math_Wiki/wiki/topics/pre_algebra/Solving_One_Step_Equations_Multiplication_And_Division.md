---
title: "Solving One-Step Equations (Multiplication and Division)"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-linear", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Solving_One_Step_Equations_Addition_And_Subtraction"
  - "topics/pre_algebra/Solving_Two_Step_Equations"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Solving_One_Step_Equations_Addition_And_Subtraction"
problem_type_ids: []
figures: []
summary: "Undo multiplication with division and division with multiplication, applying the inverse operation to both sides."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Solving One-Step Equations (Multiplication and Division)

# Solving One-Step Equations (Multiplication and Division)

Once you are comfortable with equations where something is added to or subtracted from the variable, the next family to meet is the one where the variable is being **multiplied** or **divided** by a number. Equations like $3x = 15$ and $\dfrac{x}{4} = 7$ are exactly one step away from an answer, but the step has to be the right one. Adding or subtracting will not touch a coefficient that is stuck to the variable by multiplication — you need to undo multiplication with its inverse.

Multiplication and division are the second inverse pair in arithmetic. Where addition and subtraction cancel each other, multiplication and division do the same. That single fact is the key to this whole lesson.

## The idea

In an equation of the form $ax = c$, the number $a$ is multiplying the variable. It is clinging to $x$ through multiplication, and the only way to peel it off without disturbing anything else is to divide by $a$. Divide both sides by $a$, and the $a$ on the left cancels with itself, leaving $x$ alone.

In an equation of the form $\dfrac{x}{b} = c$, the variable is being divided by $b$. To peel the $b$ off, do the inverse: apply a factor of $b$ to each side of the equation. The division on the left cancels, and the right side gets multiplied by $b$ as well.

In symbols:

$$
ax = c \quad \Longrightarrow \quad x = \frac{c}{a}, \qquad \frac{x}{b} = c \quad \Longrightarrow \quad x = bc.
$$

Two things to notice about the symbolic rule:

- The rule demands that you apply the inverse to **both** sides. Dividing only the left side of $3x = 15$ by $3$ gives the nonsense $x = 15$. The equals sign only stays valid if you treat the sides identically.
- The rule needs $a$ (or $b$) to be nonzero. Division by zero is not allowed, which is the one case where this method refuses to work. You will almost never see an equation where the coefficient is genuinely zero — if it is, the equation is a statement like $0 \cdot x = 5$, which has no solution.

## How to do it

1. Look at the variable and ask: "what number is doing what to it?"
2. If a number is multiplying the variable, divide both sides by that number.
3. If the variable is being divided by a number, apply that number as a factor to each side.
4. Simplify, and write the result as $x = \text{something}$.
5. Substitute your answer back into the original equation to check that it works.

Negative coefficients are handled identically — the division still works, but you must include the sign. Dividing by $-2$ in an equation like $-2x = 18$ gives $x = -9$, not $x = 9$. Keep the sign glued to the number at all times.

## Why it works

Like the previous lesson, this method rests on the balance view of an equation. If two things are equal, you may multiply both of them by the same number and they remain equal; you may divide both of them by the same nonzero number and they remain equal. These are the **multiplication** and **division** properties of equality. They grant you permission to make the change you need.

Picking the inverse operation works for a simple reason: every number (except zero) has a reciprocal, and a number times its reciprocal is $1$. Dividing by $3$ is the same as multiplying by $\tfrac{1}{3}$, and $3 \cdot \tfrac{1}{3} = 1$. Once the coefficient on $x$ shrinks to $1$, it effectively disappears, and what is left is a clean statement of the value of $x$.

## Worked examples

### Example 1: undoing multiplication

Determine the value of $x$ that makes $7x = 42$ true.

The variable has a coefficient of $7$, meaning it is being multiplied by $7$. The inverse operation is division, so divide each side of the equation by $7$:

$$
\frac{7x}{7} = \frac{42}{7}
$$

On the left, $\tfrac{7}{7} = 1$, so $\tfrac{7x}{7} = 1 \cdot x = x$. On the right, $42 \div 7 = 6$:

$$
x = 6
$$

Check by substitution: $7 \cdot 6 = 42$. The original equation is satisfied.

### Example 2: undoing division

Give the value of $x$ for which $\dfrac{x}{5} = 6$.

Here the variable is being divided by $5$, so the inverse move is to multiply by $5$. Apply the factor $5$ to each side:

$$
5 \cdot \frac{x}{5} = 5 \cdot 6
$$

On the left, the $5$ on the outside cancels the $5$ on the bottom, leaving $x$. On the right, $5 \cdot 6 = 30$:

$$
x = 30
$$

Check: $\tfrac{30}{5} = 6$. The value of the left side matches the value on the right, so the answer is correct. A plausibility check first would have told you $x$ must be five times as large as $6$, which $30$ is.

### Example 3: a negative coefficient

Find all $x$ for which $-2x = 18$.

The coefficient is $-2$, not just $2$. That means the variable is being multiplied by $-2$. The inverse is division by $-2$ — not by $2$. Divide each side by $-2$, keeping the sign:

$$
\frac{-2x}{-2} = \frac{18}{-2}
$$

On the left, $\tfrac{-2}{-2} = 1$, so what remains is $x$. On the right, $18 \div (-2) = -9$:

$$
x = -9
$$

Check: $-2 \cdot (-9) = 18$. Product of two negatives is positive, and $2 \cdot 9 = 18$, so the value comes out exactly $18$. The answer is verified.

The sign trap in problems like this catches a lot of students. If you divide by $2$ instead of $-2$, the left side does not simplify cleanly — you are left with $-x = 9$, one more step away from a real answer. Going straight for $-2$ lands you at the solution in a single clean division.

## Common pitfalls

- **Dividing (or multiplying) only one side.** The equals sign only stays true if both sides are changed identically. If you divide the left by $3$, you must divide the right by $3$.
- **Using the wrong operation.** If the variable is being multiplied, do not multiply — that only piles more coefficient on. Use the inverse: divide.
- **Dropping a negative sign.** When the coefficient is negative, divide by the negative. The sign must travel with the number from start to finish.
- **Confusing $\dfrac{x}{b}$ with $bx$.** $\dfrac{x}{4} = 7$ is a division equation; $4x = 7$ is a multiplication equation. They call for opposite moves: the first wants a multiply, the second wants a divide.
- **Forgetting to check.** Substituting your answer back into the original equation takes a few seconds and catches almost every sign slip.

## Problems Involving Solving One-Step Equations (Multiplication and Division)

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_one_step_equations_multiplication_and_division"></div>

## See Also

- [[Solving_One_Step_Equations_Addition_And_Subtraction]]
- [[Solving_Two_Step_Equations]]
- [[Multiplying_And_Dividing_Integers]]
- [[Variables_And_Algebraic_Expressions]]
- [[One_Step_Equations|One-Step Equations (Algebra 1)]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
