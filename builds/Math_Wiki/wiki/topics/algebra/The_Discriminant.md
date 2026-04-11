---
title: "The Discriminant"
type: topic
aliases: ["Discriminant", "b squared minus 4ac"]
tags: ["#branch-algebra-1", "#topic-quadratics", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "8", section: "8.4"}
related:
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Graphing_Quadratic_Functions"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Completing_The_Square"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
problem_type_ids: []
figures: ["algebra/discriminant_three_cases.svg"]
summary: "The number b² - 4ac hidden under the radical in the quadratic formula tells you — without solving — how many real roots a quadratic has."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > The Discriminant

# The Discriminant

Every time you punch a quadratic equation into [[The_Quadratic_Formula|the quadratic formula]], one little expression does all the heavy lifting before you even think about the $\pm$ sign. That expression is the piece $b^2 - 4ac$ that lives under the square root. Mathematicians have a name for it — the **discriminant** — and a handy shortcut symbol, the Greek capital delta:

$$
\Delta = b^2 - 4ac
$$

Why care about just this chunk of the formula? Because its sign alone tells you the whole story about the solutions of $ax^2 + bx + c = 0$, **before** you bother simplifying radicals or reducing fractions. One number. Three possible outcomes. That is the magic of the discriminant.

![[discriminant_three_cases.svg|Three discriminant cases and their parabolas]]

---

## The three cases

When you stare at the quadratic formula

$$
x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a},
$$

the thing that can wreck your day is the stuff inside the square root. If it is positive, the square root is a real number and the $\pm$ produces two different answers. If it is exactly zero, the $\pm$ adds and subtracts zero — you get the same answer twice. If it is negative, no real number squares to give you a negative, so you are stuck (in algebra 1, at least — you will revisit this in [[The_Complex_Number_System|complex numbers]] later).

That behavior boils down to three rules worth memorizing:

- **$\Delta > 0$** — the quadratic has **two distinct real solutions**. If $\Delta$ happens to be a perfect square like $1, 4, 9, 16, 25, \dots$, those solutions are rational and the quadratic factors cleanly over the integers. If $\Delta$ is positive but not a perfect square, the solutions are irrational (they keep a square root in them).
- **$\Delta = 0$** — the quadratic has **exactly one real solution**, sometimes called a *repeated root* or *double root* because the two branches of the $\pm$ collapse into the same number.
- **$\Delta < 0$** — the quadratic has **no real solutions**. There is no real number $x$ that satisfies the equation at all.

### How this shows up on the graph

The rule becomes much more memorable once you picture the parabola $y = ax^2 + bx + c$ and ask where it meets the $x$-axis. Real solutions of the equation and $x$-intercepts of the graph are the same thing, so the three cases translate straight into three pictures:

- When $\Delta > 0$, the parabola **crosses the $x$-axis at two separate points** — a clean two-intercept picture.
- When $\Delta = 0$, the parabola **just barely touches the $x$-axis** at a single point, and that point is the vertex. The curve kisses the axis and bounces back without crossing.
- When $\Delta < 0$, the parabola **never touches the $x$-axis** at all. It either floats entirely above the axis (if $a > 0$) or sits entirely below it (if $a < 0$).

So with a single arithmetic check, you can predict the shape of a graph you have not even drawn. That is why experienced problem solvers compute $\Delta$ first, and only reach for a solution method once they know what they are hunting for. The [[Graphing_Quadratic_Functions|graph of a quadratic function]] page shows the picture side in detail.

---

## Example 1: a positive discriminant

> Without solving, decide how many real solutions $x^2 - 5x + 6 = 0$ has, and describe what the parabola $y = x^2 - 5x + 6$ looks like near the $x$-axis.

Read the coefficients off the standard form: $a = 1$, $b = -5$, $c = 6$. Plug into $\Delta = b^2 - 4ac$:

$$
\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1.
$$

The discriminant is $1$, which is positive **and** a perfect square. Two conclusions follow instantly:

1. The equation has **two distinct real solutions**, and both are rational — so the quadratic factors cleanly. (In fact, $x^2 - 5x + 6 = (x - 2)(x - 3)$, so the roots are $2$ and $3$.)
2. The parabola $y = x^2 - 5x + 6$ **crosses the $x$-axis twice**, at $x = 2$ and $x = 3$.

Notice how much information the single number $\Delta = 1$ gave you before you even thought about factoring.

---

## Example 2: a zero discriminant

> How many real solutions does $x^2 - 4x + 4 = 0$ have, and what does that mean for the graph of $y = x^2 - 4x + 4$?

Here $a = 1$, $b = -4$, $c = 4$. The discriminant is

$$
\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0.
$$

Since $\Delta = 0$ exactly, there is **one repeated real solution**. That single root must be the $x$-coordinate of the vertex, because the vertex is the *only* place a parabola with $\Delta = 0$ ever meets the horizontal axis. The parabola $y = x^2 - 4x + 4$ **touches the $x$-axis at one point and nowhere else** — it grazes the axis at the vertex and rises on both sides.

You can double-check this by factoring: $x^2 - 4x + 4 = (x - 2)^2$, so the only solution is $x = 2$. A perfect square trinomial always has a zero discriminant — that is really the same fact wearing two different disguises.

---

## Example 3: a negative discriminant

> Does $x^2 + x + 3 = 0$ have any real solutions? Where is the parabola $y = x^2 + x + 3$ relative to the $x$-axis?

Coefficients: $a = 1$, $b = 1$, $c = 3$. Compute:

$$
\Delta = (1)^2 - 4(1)(3) = 1 - 12 = -11.
$$

The discriminant is $-11$, a negative number. That means the quadratic formula would ask you for $\sqrt{-11}$, which is not a real number. So the equation $x^2 + x + 3 = 0$ has **no real solutions at all**.

On the graph, this says the parabola $y = x^2 + x + 3$ **never crosses or touches the $x$-axis**. Since $a = 1 > 0$ it opens upward, so the whole curve floats above the axis. Plug in a couple of test values if you want to see it: $y(0) = 3$, $y(-1) = 3$, $y(1) = 5$ — always positive, exactly as the discriminant predicted.

---

## Why it is worth computing first

Before you settle on a solution method, the discriminant tells you which tool to grab from the toolbox:

- $\Delta$ is a **perfect square** $\Rightarrow$ the quadratic factors over the integers, so [[Solving_Quadratics_By_Factoring|factoring]] is probably fastest.
- $\Delta$ is **positive but not a perfect square** $\Rightarrow$ the answers will involve irrational numbers, so skip factoring and go directly to [[The_Quadratic_Formula|the quadratic formula]] or [[Completing_The_Square|completing the square]].
- $\Delta = 0$ $\Rightarrow$ the trinomial is a perfect square. Factor it as $(\text{something})^2 = 0$ and read off the single repeated root.
- $\Delta < 0$ $\Rightarrow$ stop. There are no real answers; the equation has no real roots, and the parabola has no real $x$-intercepts. (If the course has introduced complex numbers, you can continue; otherwise the answer is simply "no real solution".)

This check takes only a few seconds, and it saves you from hunting for factors that do not exist or from solving an equation that has no answer.

---

## Common pitfalls

- **Sign slips with $b$.** The formula uses $b^2$, which is always non-negative, but forgetting to square a negative $b$ properly — for instance computing $(-5)^2$ as $-25$ instead of $25$ — wipes out the calculation. Square first, negate never.
- **Arithmetic with $-4ac$.** When $c$ is negative, $-4ac$ comes out positive, and it is easy to make the sign wrong. Write both factors including their signs, then simplify.
- **Saying "no solution" when you should say "no real solution".** Below algebra 1 it is common to just say "no solution" when $\Delta < 0$. Once complex numbers enter the picture, the quadratic still has roots — they are imaginary. Be precise: a negative discriminant means no **real** solution.
- **Treating $\Delta = 0$ as "no solution".** A zero discriminant gives you *one* real answer, not zero. The parabola touches the $x$-axis at the vertex, and that single point is a real root.

---

## Prerequisites

Before you lean on the discriminant, make sure the surrounding machinery is solid:

- [[The_Quadratic_Formula]] — the discriminant is literally the piece under its square root, and the connection makes the three cases obvious.
- [[Solving_Quadratics_By_Factoring]] — so you recognize when a perfect-square discriminant means the trinomial factors over the integers.
- [[Graphing_Quadratic_Functions]] — to picture the three graphical outcomes instead of memorizing them as rules.

---

## Problems Involving The Discriminant

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_discriminant"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[The_Quadratic_Formula]]
- [[Graphing_Quadratic_Functions]]
- [[Solving_Quadratics_By_Factoring]]
- [[Completing_The_Square]]
- [[Quadratic_Functions]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
