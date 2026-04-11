---
title: "More Exotic Functions"
type: topic
aliases: ["Piecewise Functions", "Step Functions"]
tags: ["#branch-algebra-2", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "8", section: "8.4"}
related:
  - "topics/algebra/Absolute_Value_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
  - "topics/algebra/Linear_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Quadratic_Functions"
problem_type_ids: []
figures: ["algebra/piecewise_function.svg"]
summary: "Piecewise, step, and floor functions — the rule changes partway through."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > More Exotic Functions

# More Exotic Functions

Every function you've met so far used a **single formula** that worked for every input. Plug an $x$ into $f(x) = x^2$ and you always square it; plug one into $f(x) = 1/x$ and you always divide. But the real world is full of situations where the rule changes partway through. A cell phone bill charges one rate for the first few gigabytes and a different rate after that. A parking garage charges one price for the first hour and a different price each hour after. A tax bracket applies one percentage until you cross a threshold, then a different percentage above it. Functions that capture those kinds of rules need more than one formula, and they are the subject of this page.

The two biggest families are **piecewise functions** (where the formula simply swaps over at a breakpoint) and **step functions** (a special kind of piecewise function that jumps in flat steps). We'll also see how old friends like $|x|$ secretly belong here too.

---

## Piecewise functions in one picture

A **piecewise-defined function** is one you specify by breaking its domain into non-overlapping chunks and giving a separate formula for each chunk. The notation uses a big left curly brace with one line per piece:

$$
f(x) = \begin{cases} \text{formula A} & \text{if } x \text{ is in region A} \\ \text{formula B} & \text{if } x \text{ is in region B} \\ \text{formula C} & \text{if } x \text{ is in region C} \end{cases}
$$

To evaluate $f$ at a given input, first figure out which region the input lands in, then apply the formula for that region. To graph the whole thing, draw each piece only over its own region and stop at the boundaries. Boundary points need either a filled dot (if the formula at that boundary applies) or an open dot (if the formula excludes the boundary).

Absolute value, which you've already met in [[Absolute_Value_Functions]], is quietly a piecewise function:

$$
|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}
$$

The V-shape is exactly what happens when you tape the right-hand piece of $y = x$ to the left-hand piece of $y = -x$ at the origin.

![[piecewise_function.svg|A three-piece piecewise function]]

---

## Step functions and the floor

A **step function** is a piecewise function whose pieces are all horizontal. Its graph looks like a staircase. The most famous one is the **greatest integer function**, written $\lfloor x \rfloor$ and sometimes called the **floor function**. For any real input $x$, it returns the largest integer that is less than or equal to $x$. So $\lfloor 2.7 \rfloor = 2$, $\lfloor 5 \rfloor = 5$, and $\lfloor -1.3 \rfloor = -2$ (not $-1$, because $-2 \leq -1.3 < -1$).

As an infinite piecewise function, the floor looks like

$$
\lfloor x \rfloor = \begin{cases} \vdots \\ -1 & \text{if } -1 \leq x < 0 \\ 0 & \text{if } 0 \leq x < 1 \\ 1 & \text{if } 1 \leq x < 2 \\ 2 & \text{if } 2 \leq x < 3 \\ \vdots \end{cases}
$$

Graphically that's a staircase: each tread is a horizontal segment of length $1$, with a filled dot on its left end and an open dot on its right end.

Step functions show up any time a real quantity is charged in discrete units — postage that rounds up to the nearest ounce, parking that rounds up to the nearest hour, data that rounds up to the nearest gigabyte, and so on.

---

## Example 1: evaluating a piecewise function

> Let
> $$
> f(x) = \begin{cases} x + 3 & \text{if } x < 0 \\ x^2 & \text{if } 0 \leq x \leq 2 \\ 4 & \text{if } x > 2 \end{cases}
> $$
> Find $f(-2)$, $f(0)$, $f(1)$, $f(2)$, and $f(5)$.

For each input, find its region first, then use that region's formula.

- $f(-2)$: $-2 < 0$, so use the first line. $f(-2) = -2 + 3 = 1$.
- $f(0)$: $0$ satisfies $0 \leq x \leq 2$, so use the middle line. $f(0) = 0^2 = 0$.
- $f(1)$: $1$ is in the middle interval too. $f(1) = 1^2 = 1$.
- $f(2)$: the middle line's condition is $0 \leq x \leq 2$, which includes $x = 2$. $f(2) = 2^2 = 4$.
- $f(5)$: $5 > 2$, so use the third line. $f(5) = 4$.

Notice that at $x = 0$ and $x = 2$, you have to look carefully at which piece "owns" the boundary. The middle line's interval $0 \leq x \leq 2$ includes both endpoints, so the linear piece ($x + 3$) does NOT evaluate at $x = 0$ — the middle piece wins. At $x = 2$ the flat piece says "$x > 2$" (strict), so the middle piece still wins. This careful bookkeeping is why you need open and filled dots on the graph.

---

## Example 2: graphing a three-piece function

> Sketch the function from Example 1.

The three pieces come together on the coordinate plane as three separate curve segments.

- **Piece 1** (linear, $x < 0$): the line $y = x + 3$ restricted to $x$-values to the left of the y-axis. At $x = 0$, the formula would give $y = 3$, but the inequality is strict ($x < 0$), so the segment ends just shy of the y-axis. Mark the point $(0, 3)$ with an **open dot** — the graph gets arbitrarily close to it but doesn't include it.
- **Piece 2** (parabolic, $0 \leq x \leq 2$): the parent parabola $y = x^2$ from $x = 0$ to $x = 2$. Both endpoints are included (the inequalities are non-strict), so mark $(0, 0)$ and $(2, 4)$ with **filled dots**.
- **Piece 3** (constant, $x > 2$): a horizontal line at height $y = 4$ extending to the right of $x = 2$. The left endpoint is excluded ($x > 2$ is strict), so mark $(2, 4)$ with an **open dot** — except there's already a filled dot there from piece 2, and the filled dot wins visually because the function IS defined at $x = 2$ (by the middle piece).

Notice that the three pieces don't necessarily meet. At $x = 0$, the linear piece is about to hit $y = 3$ but doesn't, and the parabolic piece starts fresh at $y = 0$. The graph **jumps** from $3$ down to $0$ at $x = 0$. That's perfectly legal for a piecewise function — the graph doesn't have to be continuous.

---

## Example 3: the floor function on a few inputs

> Evaluate $\lfloor x \rfloor$ at $x = 4.7$, $x = -2.3$, $x = 0$, $x = -0.1$, and $x = 7$.

The floor always rounds **down** to the greatest integer $\leq x$.

- $\lfloor 4.7 \rfloor = 4$. (4 is an integer, and $4 \leq 4.7 < 5$.)
- $\lfloor -2.3 \rfloor = -3$. This is the one that catches students. Rounding "down" on a negative number means going **more negative**, so we land at $-3$, not $-2$. Check: $-3 \leq -2.3 < -2$. ✓
- $\lfloor 0 \rfloor = 0$. (Any integer floors to itself.)
- $\lfloor -0.1 \rfloor = -1$. Again, "down" on a negative means lower, so $-1$, not $0$.
- $\lfloor 7 \rfloor = 7$.

On the graph, each of these values corresponds to a step. Between integers, the floor sits flat; at each integer, the step jumps up by $1$. A postage meter that charges $\$0.50$ per ounce (rounded up) could be modeled by an analogous **ceiling** function, which rounds up instead of down.

---

## Common pitfalls

- **Choosing the wrong piece at a boundary.** Always read the inequality symbols carefully. Strict ($<, >$) excludes the boundary; non-strict ($\leq, \geq$) includes it. Whichever piece uses the non-strict inequality owns the boundary.
- **Drawing the graph as one continuous curve.** Piecewise graphs are allowed (and often expected) to jump. If the two pieces disagree at the boundary, there's a gap and you need open/filled dots to mark it.
- **Rounding a negative number in the wrong direction for the floor.** The floor of $-1.4$ is $-2$, not $-1$. "Round down" on a negative means farther from zero.
- **Thinking absolute value is a single-formula function.** It behaves like one in calculations, but it's really a two-piece function. That's why its graph has a kink at the origin.

---

## Prerequisites

- [[Function_Basics]] — function notation and domains
- [[Linear_Functions]] — most piecewise pieces are linear
- [[Quadratic_Functions]] — second most common kind of piece

---

## Problems Involving More Exotic Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="more_exotic_functions"></div>

---

## See Also

- [[Absolute_Value_Functions]] — absolute value is secretly piecewise
- [[Function_Basics]] — the basic mechanics of functions
- [[Transformations_I_Shifts_And_Reflections]] — shifts and reflections apply to piecewise functions too
- [[Linear_Functions]] — common piece type
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
