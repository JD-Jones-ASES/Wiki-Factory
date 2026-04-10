---
title: "Quadratic Functions"
type: topic
aliases: ["QuadraticFunctions", "Quadratic Functions and Vertex Form"]
tags: ["#branch-algebra-2", "#topic-quadratics", "#topic-functions", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "3", section: "3.6"}
  - {book: "algtrig", chapter: "2", section: "2.4"}
related:
  - "topics/algebra/Graphing_Quadratic_Functions"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Applications_Of_Quadratic_Functions"
  - "topics/algebra/The_Discriminant"
  - "topics/algebra/Linear_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Graphing_Quadratic_Functions"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: []
summary: "Two ways to write the same parabola: standard form shows the y-intercept, vertex form shows the turning point."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Quadratic Functions

# Quadratic Functions

A **quadratic function** is the next family you meet after the linear ones, and it behaves very differently. Where a linear function climbs or falls at a steady rate, a quadratic curves — it speeds up, slows down, stops, and turns around. The graph is a **parabola**, a smooth U-shape that either opens up like a bowl or opens down like an arch. Every quadratic has a single highest or lowest point called the **vertex**, and that point does most of the interesting work.

There are two common ways to write the same quadratic function, and each reveals something different about it. Both matter. You will move between them constantly, so it pays to be comfortable with each.

The **standard form** (sometimes called general form) is

$$
f(x) = ax^2 + bx + c, \qquad a \neq 0.
$$

and the **vertex form** is

$$
f(x) = a(x - h)^2 + k.
$$

They describe the same shape. The only difference is which information is visible at a glance.

---

## What each form tells you

**Standard form** $f(x) = ax^2 + bx + c$ is the form most textbook problems hand you. Its advantages:

- The constant $c$ is the **$y$-intercept**, because $f(0) = c$. Plug in zero, read off the answer.
- The leading coefficient $a$ tells you which way the parabola opens. If $a > 0$, the curve opens upward and the vertex is the lowest point (a **minimum**). If $a < 0$, the curve opens downward and the vertex is the highest point (a **maximum**).
- The absolute size of $a$ controls how narrow or wide the parabola is. Large $|a|$ pinches it tight; small $|a|$ spreads it out. A coefficient of $1$ gives the baseline shape of $y = x^2$.
- The downside: the vertex is hidden. You cannot see it from the coefficients without a bit of computation.

**Vertex form** $f(x) = a(x - h)^2 + k$ wears its secret on the outside. Its advantages:

- The vertex sits right there: $(h, k)$. No work required.
- The axis of symmetry — the vertical line the parabola mirrors across — is simply $x = h$.
- The value $k$ is the **maximum or minimum value** of the function (maximum if $a < 0$, minimum if $a > 0$).
- Watch the sign carefully. For something like $g(x) = 2(x - 7)^2 + 4$, the turning point sits at $(7, 4)$, and the $7$ is positive even though the form shows subtraction. The minus is built into the pattern $(x - h)$, not a sign you strip off.

Both forms hold the same information. Picking which one to use is a matter of which question you are asking.

---

## From standard form to vertex form: completing the square

The bridge between the two forms is [[Completing_The_Square]]. Start with $ax^2 + bx + c$, and you want to end with $a(x - h)^2 + k$. The recipe:

1. Factor out $a$ from the first two terms only, leaving the constant alone.
2. Inside the parentheses, take half of the coefficient of $x$, square it, and add and subtract that number inside the parentheses.
3. Group the perfect square trinomial, factor it, and collect the remaining constants outside.

The extra step when $a \neq 1$ is that adding a number inside the parentheses is really adding $a$ times that number to the whole expression, so you must track the bookkeeping carefully.

### The vertex shortcut

If you just want the vertex without rewriting the whole function, there is a shortcut from standard form alone. For $f(x) = ax^2 + bx + c$, the vertex is

$$
\left( -\dfrac{b}{2a},\; f\!\left(-\dfrac{b}{2a}\right) \right).
$$

Compute the $x$-coordinate with the formula, then plug that value back into the original function to get the $y$-coordinate. This is faster than completing the square when all you need is the location of the turning point.

---

## Domain, range, and evaluation

Every quadratic function, no matter how its coefficients look, accepts any real number as an input. The domain is always all of $\mathbb{R}$ — there is nothing you can feed a quadratic that breaks it.

The range, on the other hand, depends on the direction of opening and on the vertex. If the parabola opens upward (with vertex $(h, k)$), the output can be anything from $k$ up to infinity: the range is $[k, \infty)$. If it opens downward, the output is capped above by $k$: the range is $(-\infty, k]$. The vertex's $y$-coordinate is literally the edge of the range.

Evaluating a quadratic at a specific input is the same as any other function: substitute the number for every $x$ and simplify carefully. Watch signs on the squared term — if you plug in $-2$ into $f(x) = 2x^2 - 3x + 1$, the first term is $2(-2)^2 = 2 \cdot 4 = 8$, not $-8$.

---

## Example 1: evaluating a quadratic at several inputs

> Let $f(x) = 2x^2 - 3x + 1$. Find $f(0)$, $f(1)$, and $f(-2)$.

For $f(0)$, substitute $0$ for every $x$:

$$
f(0) = 2(0)^2 - 3(0) + 1 = 0 - 0 + 1 = 1.
$$

So the parabola crosses the $y$-axis at $(0, 1)$ — which is exactly the $y$-intercept you can read off the constant $c = 1$ in standard form.

For $f(1)$:

$$
f(1) = 2(1)^2 - 3(1) + 1 = 2 - 3 + 1 = 0.
$$

Since $f(1) = 0$, the point $(1, 0)$ is on the parabola and $x = 1$ is a zero of the function.

For $f(-2)$, go slowly on the signs:

$$
f(-2) = 2(-2)^2 - 3(-2) + 1 = 2(4) - (-6) + 1 = 8 + 6 + 1 = 15.
$$

So $f(-2) = 15$. Notice how the squared term kills the negative sign — this is the difference between a quadratic and a linear function, and it is why parabolas symmetric.

---

## Example 2: reading the vertex from vertex form

> Identify the vertex of $f(x) = -3(x - 4)^2 + 5$ and state the maximum or minimum value of the function.

Compare term by term with $f(x) = a(x - h)^2 + k$. The match-up is $a = -3$, $h = 4$, $k = 5$. So the vertex is $(4, 5)$, directly off the form.

Since $a = -3 < 0$, the parabola opens downward. That means the vertex is the **highest** point on the graph — the function reaches a maximum at $x = 4$, and the maximum value is $y = 5$. The range is $(-\infty, 5]$.

If someone asks "where does this function hit its largest output?" the answer is $x = 4$. If they ask "what is the largest output?" the answer is $5$. These two questions ask for different coordinates of the same point; keep them straight.

---

## Example 3: converting from standard to vertex form

> Write $f(x) = x^2 - 8x + 13$ in vertex form and state the vertex.

The leading coefficient is already $1$, so no factoring step is needed. Focus on the $x^2 - 8x$ part and complete the square.

Half of $-8$ is $-4$, and $(-4)^2 = 16$. Add and subtract $16$ inside the expression:

$$
f(x) = (x^2 - 8x + 16) - 16 + 13.
$$

Group the perfect square trinomial and collapse the constants:

$$
f(x) = (x - 4)^2 - 3.
$$

That is vertex form. Reading it off, the vertex is $(4, -3)$. Since $a = 1 > 0$, the parabola opens upward, so the vertex is a minimum and the minimum value is $-3$. The range is $[-3, \infty)$.

**Double-check with the vertex formula.** Using the shortcut $x = -\dfrac{b}{2a}$ on the original $f(x) = x^2 - 8x + 13$ gives $x = -\dfrac{-8}{2(1)} = 4$, and $f(4) = 16 - 32 + 13 = -3$. Same vertex. The two methods agree.

---

## Common pitfalls

- **Sign errors on the vertex.** In vertex form $f(x) = a(x - h)^2 + k$, the vertex is $(h, k)$, and $h$ is whatever is being subtracted. If you see $(x + 2)^2$, rewrite it as $(x - (-2))^2$ first; the vertex's $x$-coordinate is $-2$, not $+2$.
- **Treating vertex form like standard form.** Plugging $x = 0$ into vertex form gives you the $y$-intercept, but that is not $k$. You have to actually compute $a \cdot h^2 + k$.
- **Losing $a$ during completing the square.** When the leading coefficient is not $1$, you factor $a$ out of the first two terms. Anything you add inside those parentheses gets multiplied by $a$ on its way out — forgetting this step is the most common slip.
- **Confusing the vertex with a zero.** The vertex is the turning point. A zero is where the function crosses the $x$-axis. Some parabolas have no zeros at all (when the vertex sits entirely above or below the $x$-axis), but every parabola has exactly one vertex.

---

## Prerequisites

Before tackling practice problems on this topic, be comfortable with:

- [[Graphing_Quadratic_Functions]] — the visual picture of parabolas
- [[Completing_The_Square]] — the algebraic bridge between standard and vertex form
- [[The_Quadratic_Formula]] — for locating zeros when factoring fails
- [[Linear_Functions]] — the function-notation habits transfer directly

---

## Problems Involving Quadratic Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="quadratic_functions"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Graphing_Quadratic_Functions]]
- [[Completing_The_Square]]
- [[The_Quadratic_Formula]]
- [[The_Discriminant]]
- [[Applications_Of_Quadratic_Functions]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
