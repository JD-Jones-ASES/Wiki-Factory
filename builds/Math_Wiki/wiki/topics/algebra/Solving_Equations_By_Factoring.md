---
title: "Solving Equations by Factoring"
type: topic
aliases: []
tags: ["#branch-algebra-2", "#topic-quadratics", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Solving_Equations_By_Taking_Roots"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/The_Quadratic_Formula"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "Rewrite a quadratic (or higher) equation so one side is zero, factor the other side, and pick off the roots one factor at a time."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Solving Equations by Factoring

# Solving Equations by Factoring

Factoring gives you a remarkable shortcut. If you can rewrite a quadratic equation as the product of simpler pieces equal to zero, you do not need the quadratic formula, and you do not need to complete the square — you can read the solutions straight off the factored form. The method rests on a single clean fact about multiplication: **the only way for a product to equal zero is for at least one of the factors to equal zero.** Once the equation has the right shape, solving it is almost effortless.

This page pairs with [[Solving_Quadratics_By_Factoring]], which focuses on the Algebra 1 version of the technique. Here the scope is slightly wider — we will also touch on cases where the factored form has three factors, and we will spend more time on the backward question: given the roots, can you rebuild the equation?

## The zero-product principle

Call it the **zero-product principle**: for any two real numbers $a$ and $b$, if $a \cdot b = 0$, then $a = 0$ or $b = 0$ (or both). Multiplication by any nonzero number is a "safe" operation — it cannot accidentally produce zero. So if the product is $0$, at least one of the factors was already $0$. The same principle works for products of three or more factors: if $a \cdot b \cdot c = 0$, then at least one of $a$, $b$, $c$ is zero.

This is why the zero on the right side of the equation is non-negotiable. Watch what goes wrong if you ignore it. From the equation

$$
(x - 2)(x + 5) = 4,
$$

it is tempting to write $x - 2 = 4$ and $x + 5 = 4$. But the principle does **not** apply — there are infinitely many ways for two real numbers to multiply to $4$, and you have no reason to believe one of the two factors is $4$. The principle only works when the product in question equals $0$, because $0$ is the one target that forces a factor to match it. Before splitting the factors, get the right side to be exactly $0$.

## The procedure

Every problem on this page follows the same four-step recipe:

1. **Get zero on one side.** Move every term to the left side so the right side reads $0$. If the equation is already in standard form $ax^2 + bx + c = 0$, skip this step.
2. **Factor the non-zero side completely.** Start with a greatest common factor, then factor the remaining polynomial using whichever technique fits its shape: [[Factoring_Trinomials_Leading_Coefficient_1]], [[Factoring_Trinomials_General]], or a difference-of-squares pattern.
3. **Split using the zero-product principle.** Each factor becomes its own small equation, typically linear.
4. **Solve each small equation.** The resulting values of $x$ together form the solution set.

A verification pass is always a good idea, especially when the problem involves negative numbers or fractions. Plug each answer back into the original equation and confirm both sides match.

## The backward view

You can also run the technique backward: pick the roots first, then rebuild the equation. If you want the quadratic whose roots are $x = 4$ and $x = -3$, start with the factored form $(x - 4)(x + 3) = 0$ and multiply it out:

$$
(x - 4)(x + 3) = x^2 - x - 12.
$$

So the equation $x^2 - x - 12 = 0$ has exactly the roots $4$ and $-3$. Running the process this way is how homework problems and SAT items are constructed — and it also gives you a good sanity check: after you solve a quadratic, you can always multiply your factors back out and confirm the result matches the original equation.

## Worked examples

**Example 1.** Find all real values of $x$ for which $x^2 - 5x + 6 = 0$.

The equation is already in standard form with zero on the right, so jump to factoring. Look for two numbers whose product is $6$ and whose sum is $-5$. The pair $-2$ and $-3$ does it, because $(-2)(-3) = 6$ and $(-2) + (-3) = -5$. So

$$
x^2 - 5x + 6 = (x - 2)(x - 3) = 0.
$$

By the zero-product principle, either $x - 2 = 0$ or $x - 3 = 0$. Solving each gives $x = 2$ or $x = 3$.

Verification: $2^2 - 5(2) + 6 = 4 - 10 + 6 = 0$ (check), and $3^2 - 5(3) + 6 = 9 - 15 + 6 = 0$ (check). The solution set is $x = 2$ or $x = 3$.

**Example 2.** Give all real values of $x$ for which $2x^2 + 7x - 4 = 0$.

The leading coefficient is $2$, not $1$, so this calls for the general trinomial procedure from [[Factoring_Trinomials_General]]. Compute the product $a \cdot c = 2 \cdot (-4) = -8$. Now search for a pair of integers multiplying to $-8$ and adding to $7$. The pair $8$ and $-1$ satisfies both conditions: $8 \cdot (-1) = -8$ and $8 + (-1) = 7$.

Split the middle term and factor by grouping:

$$
2x^2 + 8x - x - 4 = 0
$$

$$
2x(x + 4) - 1(x + 4) = 0
$$

$$
(2x - 1)(x + 4) = 0.
$$

Apply the zero-product principle: either $2x - 1 = 0$ or $x + 4 = 0$. The first gives $2x = 1$, so $x = \tfrac{1}{2}$. The second gives $x = -4$.

Verification: for $x = \tfrac{1}{2}$, the left side of the original is $2(\tfrac{1}{4}) + 7(\tfrac{1}{2}) - 4 = \tfrac{1}{2} + \tfrac{7}{2} - 4 = 4 - 4 = 0$ (check). For $x = -4$, it is $2(16) + 7(-4) - 4 = 32 - 28 - 4 = 0$ (check). The solutions are $x = \tfrac{1}{2}$ and $x = -4$.

**Example 3.** Priya is trying to find every value of $x$ that satisfies

$$
x^2 - 9 = 0.
$$

The equation is already in standard form. The left side has no middle $x$ term, but it is still factorable — it is a **difference of squares**, because $x^2$ is a perfect square and $9 = 3^2$ is a perfect square. The difference-of-squares pattern says

$$
A^2 - B^2 = (A - B)(A + B),
$$

so with $A = x$ and $B = 3$ you get

$$
x^2 - 9 = (x - 3)(x + 3) = 0.
$$

Apply the zero-product principle: $x - 3 = 0$ or $x + 3 = 0$, giving $x = 3$ or $x = -3$. A quick check: $3^2 - 9 = 0$ and $(-3)^2 - 9 = 9 - 9 = 0$, so both are correct.

This equation could also have been solved by [[Solving_Equations_By_Taking_Roots]] — rearrange to $x^2 = 9$, take a square root, remember the $\pm$, and arrive at $x = \pm 3$. Both paths give the same answer. In general, any equation that factors as a difference of squares can also be handled by taking roots; pick whichever technique feels more natural.

## Common pitfalls

- **Splitting factors before the right side is zero.** This is the top mistake on every test. From $(x - 3)(x + 2) = 6$, you cannot write $x - 3 = 6$ or $x + 2 = 6$. Move the $6$ to the left first, re-expand or re-factor, then split.
- **Cancelling a variable from both sides.** Faced with $3x^2 = 12x$, the tempting move is to divide by $x$ and get $3x = 12$, which gives $x = 4$. But $x = 0$ is also a legitimate solution of the original equation, and you just lost it. Instead, move everything to one side, factor out the common $3x$, and use the zero-product principle: $3x(x - 4) = 0$ gives $x = 0$ or $x = 4$.
- **Not factoring completely.** If the trinomial has a GCF, pull it out first. $2x^2 - 10x + 12 = 0$ should become $2(x^2 - 5x + 6) = 0$ before you try to factor the trinomial. Skipping the GCF step makes the remaining numbers harder to work with.
- **Thinking every quadratic factors over the integers.** Plenty of quadratics have irrational or complex roots, and those will never factor cleanly. If the integer factor search turns up nothing, reach for [[The_Quadratic_Formula]] instead of forcing a factor pair that does not exist.
- **Forgetting that zero is a valid root.** If one of your factors is just $x$ (as in the $3x(x - 4) = 0$ case above), that factor gives $x = 0$. Students sometimes skip this root because it "looks empty," but it satisfies the original equation and belongs in the solution set.

## Problems Involving Solving Equations by Factoring

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_equations_by_factoring"></div>

## See Also

- [[Solving_Quadratics_By_Factoring]]
- [[Solving_Equations_By_Taking_Roots]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Trinomials_General]]
- [[Factoring_Completely]]
- [[The_Quadratic_Formula]]
- [[Completing_The_Square]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
