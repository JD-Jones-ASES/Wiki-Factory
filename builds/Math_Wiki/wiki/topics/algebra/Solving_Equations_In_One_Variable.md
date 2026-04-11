---
title: "Solving Equations in One Variable"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Equations_With_Variables_On_Both_Sides"
  - "topics/algebra/Solving_Equations_By_Factoring"
  - "topics/algebra/Solving_Equations_By_Taking_Roots"
  - "topics/algebra/Absolute_Value_Equations"
  - "topics/algebra/Multi_Step_Equations"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Equations_With_Variables_On_Both_Sides"
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
problem_type_ids: []
figures: []
summary: "A survey of the main equation families — linear, absolute-value, quadratic, rational, and radical — showing how each one reduces to undoing operations to get x by itself."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Equations in One Variable

# Solving Equations in One Variable

When someone says "solve for $x$," they are asking a very specific question: for what value or values of $x$ does the two-sided statement on the page actually become true? Every equation you meet, no matter how ugly, is a kind of puzzle of that exact shape. The challenge is that different equation families — linear, absolute-value, quadratic, radical, rational — each hide $x$ in a different way, and the unwrapping procedure depends on how $x$ got wrapped up in the first place. This page is a map of the whole territory. It shows you which technique belongs to which equation family and gives you one example from each.

## The one idea underneath everything

Every procedure in this page is based on the same core move: **use inverse operations to get $x$ by itself, while keeping the equation balanced.** Each operation has a partner that undoes it. Addition undoes subtraction, multiplication undoes division, squaring undoes a square root, and so on. You apply the partner operation to both sides of the equation until the variable stands alone. Keeping the equation balanced means always doing the same move to both sides, so the equation continues to describe the same relationship throughout.

The complication is that once $x$ is inside a more exotic container — inside an absolute value, inside a square, inside a radical, inside a fraction's denominator — the inverse you need is no longer a simple addition or subtraction. Each family has its own specialized unwrapping technique.

## The linear family

Linear equations are the simplest. The variable $x$ appears only to the first power, with no exponents, square roots, or absolute values wrapping around it. General form:

$$
ax + b = c,
$$

or something that rearranges into that shape after expanding parentheses and combining like terms. The unwrapping procedure is the one you already know from [[Multi_Step_Equations]] and [[Equations_With_Variables_On_Both_Sides]]:

1. Expand parentheses.
2. Collect variable terms on one side and constants on the other.
3. Divide by the coefficient of $x$.

Three sub-cases deserve a mention because they surprise students. A **consistent** linear equation simplifies to something like $x = 5$ and has one solution. An **identity** simplifies to a true statement like $0 = 0$ or $5 = 5$ — every real number is a solution. A **contradiction** simplifies to a false statement like $0 = 7$ — no real number is a solution. Which of the three you get depends only on the equation; you recognize the case when all the variable terms vanish during simplification.

## The absolute-value family

An equation like $|x - 4| = 9$ is **not** linear, even though it looks simple. The absolute value bars create a piecewise structure: the inside expression could equal $9$ or could equal $-9$, and both cases produce the same distance from zero. So the technique for absolute-value equations is:

1. First get the absolute value by itself on one side of the equation, using ordinary linear moves.
2. Split into two cases: the inside equals the positive value, or the inside equals the negative value.
3. Solve each case as a linear equation.
4. If the right side is negative after step 1, the equation has **no solution** — no real number has a negative absolute value.

[[Absolute_Value_Equations]] has the long version with more examples.

## The quadratic family

When $x$ appears to the second power, the equation is quadratic. General form:

$$
ax^2 + bx + c = 0, \qquad a \ne 0.
$$

There are three standard techniques for solving quadratics, and you choose whichever one is easiest for a given equation:

- **Factoring.** If the left side factors into $(x - r_1)(x - r_2)$, the zero-product principle says each factor separately can be set to zero. See [[Solving_Quadratics_By_Factoring]] and [[Solving_Equations_By_Factoring]].
- **Square roots.** If the equation simplifies to $(\text{something})^2 = k$ with no middle $bx$ term, take a square root of each side and remember the $\pm$. See [[Solving_Quadratics_By_Square_Roots]] and [[Solving_Equations_By_Taking_Roots]].
- **Quadratic formula.** Works on every quadratic, even the ones that cannot be factored over the integers. See [[The_Quadratic_Formula]].

## The rational family

A **rational equation** has the variable in the denominator of a fraction. To solve one, multiply every term by the least common denominator (LCD) to clear the fractions, then solve the resulting polynomial equation using whichever technique matches its shape. Important: rational equations can generate **extraneous solutions** — answers that make a denominator zero in the original equation. Always check each candidate against the original before declaring a final answer.

## The radical family

A **radical equation** has $x$ under a square root (or another root). To solve one, first get the radical by itself on one side, then square both sides to remove it. The new equation is typically polynomial, and the earlier techniques take over. Just like with rational equations, squaring can introduce extraneous solutions that do not actually satisfy the original, so always verify every candidate back in the original equation.

## Worked examples

**Example 1 (linear).** Determine the value of $x$ that makes the equation $3x + 7 = 22$ true.

The variable is not inside any container — this is a plain multi-step linear equation. Peel the $+7$ away from the $3x$ by subtracting $7$ from each side:

$$
3x = 15.
$$

Now undo the multiplication by dividing each side by $3$:

$$
x = 5.
$$

Verification in the original: $3(5) + 7 = 15 + 7 = 22$. The equation holds, so $x = 5$ is the solution.

**Example 2 (absolute value).** Find all $x$ for which $|x - 4| = 9$.

The absolute value is already by itself, and $9$ is positive, so there will be two cases. The quantity inside, $x - 4$, is either $9$ or $-9$. Write both equations:

$$
x - 4 = 9 \qquad \text{or} \qquad x - 4 = -9.
$$

Solve each one by adding $4$ to both sides:

$$
x = 13 \qquad \text{or} \qquad x = -5.
$$

Both candidates check: $|13 - 4| = |9| = 9$, and $|{-5} - 4| = |{-9}| = 9$. The solution set is $x = 13$ or $x = -5$.

**Example 3 (radical).** Kai is solving the equation $\sqrt{x + 3} = 5$. What is the value of $x$?

The radical is already by itself on the left side, so square both sides to remove it:

$$
(\sqrt{x + 3})^2 = 5^2
$$

$$
x + 3 = 25.
$$

Now it is a one-step linear equation. Subtract $3$ from both sides:

$$
x = 22.
$$

Because squaring can produce extraneous solutions, verify the answer in the original: $\sqrt{22 + 3} = \sqrt{25} = 5$. The equation holds, so $x = 22$ is the solution.

Had the verification step produced anything other than $5$, the candidate would have had to be discarded as extraneous. Always, always check radical-equation candidates in the original equation, not in your own rewritten form.

## Common pitfalls

- **Using the wrong unwrapping technique for the family.** You cannot "move" an absolute value the way you move an addend. You cannot "divide away" a square the way you divide away a coefficient. Each container needs its own inverse move.
- **Forgetting the $\pm$ in absolute value and square root steps.** Every time you peel off an absolute value or a square, two cases appear. Writing only one of them costs you a solution.
- **Ignoring extraneous solutions.** Squaring, cross-multiplying, and clearing fractions can all introduce candidate values that are not actually solutions. Substitute every candidate back into the original equation and discard any that fail.
- **Declaring "no solution" when the equation is an identity.** If the variable cancels and the remaining statement is true (like $5 = 5$), the equation has infinitely many solutions — every real number works. If the remaining statement is false, then and only then is the solution set empty.
- **Losing negative signs when distributing.** Many rational and radical equations start with a step like $-2(x - 3) = 8$. The distributive property produces $-2x + 6 = 8$, not $-2x - 6 = 8$. This mistake is the leading cause of wrong answers on multi-step problems — see [[The_Distributive_Property_With_Variables]] for the full treatment.

## Problems Involving Solving Equations in One Variable

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_equations_in_one_variable"></div>

## See Also

- [[Multi_Step_Equations]]
- [[Equations_With_Variables_On_Both_Sides]]
- [[Solving_Equations_By_Factoring]]
- [[Solving_Equations_By_Taking_Roots]]
- [[Absolute_Value_Equations]]
- [[The_Quadratic_Formula]]
- [[Solving_Inequalities_In_One_Variable]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
