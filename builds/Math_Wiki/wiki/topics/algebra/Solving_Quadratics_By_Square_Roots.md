---
title: "Solving Quadratics by Square Roots"
type: topic
aliases: ["Square Root Method", "Square Root Property"]
tags: ["#branch-algebra-1", "#topic-quadratics", "#key-technique"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "8", section: "8.2"}
related:
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/The_Discriminant"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/algebra/Properties_Of_Exponents"
problem_type_ids: []
figures: []
summary: "When a quadratic already wears a perfect-square coat, undo the square and collect both roots."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Quadratics by Square Roots

# Solving Quadratics by Square Roots

Not every quadratic equation needs heavy machinery. When the variable part is already trapped inside a single perfect square — something like $x^2$, or $(x - 4)^2$, or $(2x + 1)^2$ — you can solve the equation in just a few lines by undoing that square directly. No factoring. No quadratic formula. Just a clean "isolate, then unsquare" move.

The situations where this trick works all share the same shape:

$$
(\text{something})^2 = k.
$$

Your goal is to peel off the square and leave a linear equation underneath. That peeling step is the **square root property**.

---

## The square root property

If $k \ge 0$, then the equation $x^2 = k$ has two solutions:

$$
x = \sqrt{k} \quad \text{or} \quad x = -\sqrt{k}.
$$

We usually write both cases in one breath using the plus-or-minus symbol:

$$
x = \pm\sqrt{k}.
$$

The reason there are two answers is simple: both a positive number and its negative partner square to the same value. For example, $5^2 = 25$ and $(-5)^2 = 25$, so the equation $x^2 = 25$ has to count both $5$ and $-5$ as valid solutions.

If the right side is negative — say $x^2 = -9$ — then no real number squares to it. (Squaring a real number always lands on zero or something positive.) In Algebra 1 we simply say the equation has **no real solution** and stop there. Algebra 2 will introduce imaginary numbers that fix this, but that is a problem for later.

---

## When to use this method

Reach for the square root property the moment you spot any of these patterns:

- $x^2 = k$ — the bare form.
- $ax^2 + c = 0$ — a quadratic with no middle term. Move $c$, divide by $a$, and you are back to the bare form.
- $(x - h)^2 = k$ — a shifted square. The whole parenthesis plays the role of $x$.
- $(ax + b)^2 = k$ — the same trick, but the inside is a linear expression.

In every case, the recipe is identical:

1. Isolate the square on one side of the equation.
2. Apply a square root to each side, keeping both positive and negative possibilities by writing $\pm$.
3. Solve whatever linear equation is left.

The most important word in that recipe is **both**. Dropping the negative root is the single most common mistake on this topic. Train yourself to write $\pm$ the instant you unsquare, before you do anything else.

---

## Example 1: the bare form

> Find all real solutions to $x^2 = 49$.

The square is already isolated, so apply the square root property immediately:

$$
x = \pm\sqrt{49} = \pm 7.
$$

The two solutions are $x = 7$ and $x = -7$. Check both: $7^2 = 49$ and $(-7)^2 = 49$. Each one works, so each one belongs in the final answer.

A student who writes only $x = 7$ has found half the answer and will lose half the credit. The $\pm$ is not decoration — it is the second root.

### Two shapes inside the same example

You will also see equations where $k$ is a positive number but not a perfect square. For instance, $x^2 = 12$ gives

$$
x = \pm\sqrt{12} = \pm 2\sqrt{3}
$$

after pulling the factor of $4$ out from under the radical. The answer is irrational, but there are still exactly two of them.

Finally, if you ever meet $x^2 = -16$, stop. There is no real number whose square is $-16$, so the equation has no real solution in Algebra 1.

---

## Example 2: a shifted square

> Find all real solutions to $(x - 3)^2 = 16$.

This time the square wraps a whole binomial, but the method does not change. Treat $(x - 3)$ as one unit and unsquare:

$$
x - 3 = \pm\sqrt{16} = \pm 4.
$$

Now you have two linear equations hiding inside one compact line. Write them out and solve each:

$$
x - 3 = 4 \quad\text{or}\quad x - 3 = -4
$$

$$
x = 7 \quad\text{or}\quad x = -1.
$$

**Check.** Substitute $x = 7$: $(7 - 3)^2 = 4^2 = 16$ — good. Substitute $x = -1$: $(-1 - 3)^2 = (-4)^2 = 16$ — also good. Both roots survive the check because both signs were kept alive in the very first step.

---

## Example 3: rearrange first, then unsquare

> Find all real solutions to $2x^2 - 18 = 0$.

The square is not isolated yet, so your first job is to get $x^2$ alone on one side. Move the constant:

$$
2x^2 = 18.
$$

Divide both sides by $2$:

$$
x^2 = 9.
$$

Now the equation is in bare form and the square root property finishes the job:

$$
x = \pm\sqrt{9} = \pm 3.
$$

The two solutions are $x = 3$ and $x = -3$. The "no middle term" signature — no lone $x$, only $x^2$ and a constant — is a reliable flag that square roots are the fastest path. Factoring would also work, but isolating and unsquaring is usually two lines shorter.

---

## Common pitfalls

- **Forgetting the $\pm$.** The number one error. An unsquare operation always yields two roots whenever $k > 0$. If you wrote only the positive one, you lost half the answer before you even started simplifying.
- **Applying the square root before isolating the square.** The property only works once the squared expression sits by itself on one side. If there is still a stray constant or coefficient hanging around, the unsquare will mangle the arithmetic. Clean up first.
- **Simplifying inside the parentheses instead of unsquaring.** When you see $(x - 3)^2 = 16$, do not expand the left side into $x^2 - 6x + 9$. The whole point of this method is to preserve the square and peel it off in one move.
- **Declaring "no solution" when $k$ is positive but not a perfect square.** Irrational roots like $\pm 2\sqrt{5}$ are still real solutions. No real solution only happens when $k$ is strictly negative.

---

## Prerequisites

Before you start the practice problems, make sure these are comfortable:

- [[Multi_Step_Equations]] — solving $x - 3 = \pm 4$ at the end of every example is just a multi-step equation wearing a hat
- [[Square_Roots_And_Cube_Roots]] — knowing when a square root simplifies (like $\sqrt{12} = 2\sqrt{3}$) keeps answers tidy
- [[Properties_Of_Exponents]] — a clean grip on squaring and unsquaring prevents sign slips

---

## Problems Involving Solving Quadratics by Square Roots

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_quadratics_by_square_roots"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Solving_Quadratics_By_Factoring]] — the other fast method when the quadratic is not a bare square
- [[Completing_The_Square]] — how to force any quadratic into $(x - h)^2 = k$ form
- [[The_Quadratic_Formula]] — the universal fallback that handles every quadratic
- [[The_Discriminant]] — quick diagnostic for how many real roots a quadratic has
- [[Square_Roots_And_Cube_Roots]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
