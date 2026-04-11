---
title: "Graphing Linear Equations from Tables"
type: topic
aliases: ["Graphing Lines From A Table", "Table Method For Graphing Lines"]
tags: ["#branch-pre-algebra", "#topic-linear", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "8", section: "8.4"}
related:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/pre_algebra/Slope_As_Rate_Of_Change"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/algebra/Slope"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Linear_Functions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
problem_type_ids: []
figures: []
summary: "Pick x-values, compute y-values from the rule, plot the pairs, and draw the line that joins them."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Graphing Linear Equations from Tables

# Graphing Linear Equations from Tables

An equation like $y = 2x + 1$ is really a recipe with two slots. You feed in a number for $x$, the rule tells you what $y$ has to be, and the resulting pair $(x, y)$ is one dot on the coordinate plane. Do that a handful of times, draw a straight edge through the dots, and you have the graph of the equation.

This **table method** is the most dependable way to graph any linear equation before you have memorized shortcuts. It also makes it obvious *why* a line is a line in the first place: the rule forces each step in $y$ to match every step in $x$ in exactly the same way.

---

## Key ideas

A **linear equation in two variables** is any equation you can rearrange into the form

$$
y = mx + b,
$$

where $m$ and $b$ are just numbers. The graph of such an equation is always a perfectly straight line — never curved, never broken.

The number $b$ is called the **y-intercept**, and it is the point where the line meets the vertical axis. Whatever equation you have, plugging in $x = 0$ kills the $mx$ term and leaves $y = b$, so the line always passes through $(0, b)$.

### The four-step recipe

1. Pick several values for $x$. The friendliest choices are small, balanced integers such as $-2, -1, 0, 1, 2$. Including $0$ gives you the y-intercept automatically, and the negatives keep the picture symmetric.
2. For each $x$, evaluate the right side of the equation to get $y$.
3. Record each result as an ordered pair $(x, y)$.
4. Plot the pairs on the [[Plotting_Points_And_The_Coordinate_Plane|coordinate plane]] and connect them with a straight edge. Extend the line in both directions with arrows to show it continues forever.

### Recognizing linearity from a table

If an equation is genuinely linear, the table will have a **constant rate of change**: every time $x$ increases by the same step, $y$ will increase (or decrease) by the same step too. If the gap in $y$ keeps growing or shrinking, the relationship is not linear and the graph will bend. This observation is the seed of the idea of [[Slope|slope as a rate of change]].

### Horizontal and vertical lines

Two special cases show up often:

- An equation of the form $y = c$, where $c$ is a fixed number, graphs as a **horizontal line** that crosses the y-axis at $(0, c)$. Every point on it has the same y-coordinate.
- An equation of the form $x = c$ graphs as a **vertical line** through $(c, 0)$. Every point on it has the same x-coordinate. (Vertical lines are the one case where the $y = mx + b$ form breaks down.)

---

## Example 1: building a table for $y = 3x - 2$

> Graph the equation $y = 3x - 2$ using a table with $x = -2, -1, 0, 1, 2$.

Compute $y$ one row at a time. For $x = -2$: $y = 3(-2) - 2 = -6 - 2 = -8$. For $x = -1$: $y = 3(-1) - 2 = -5$. Continue down:

| $x$ | $y = 3x - 2$ |
|----:|-------------:|
| $-2$ | $-8$ |
| $-1$ | $-5$ |
| $0$  | $-2$ |
| $1$  | $1$  |
| $2$  | $4$  |

The pairs to plot are $(-2, -8)$, $(-1, -5)$, $(0, -2)$, $(1, 1)$, and $(2, 4)$. Mark each on graph paper, then draw the straight line that passes through all five. The line meets the y-axis at $(0, -2)$ — that is the y-intercept, and it matches the $-2$ sitting at the end of the equation.

Notice that each row of the table jumps from one $y$-value to the next by exactly $3$. That matches the coefficient in front of $x$, which is how we know the rule is linear before we even plot anything.

---

## Example 2: a table that includes negatives

> Graph $y = -x + 4$ using a table with $x = -1, 0, 1, 2, 3$.

The coefficient of $x$ is $-1$, so each increase of $1$ in $x$ should drop $y$ by exactly $1$. Work out each row carefully, since the sign flips are easy to miss.

| $x$ | $y = -x + 4$ |
|----:|-------------:|
| $-1$ | $5$ |
| $0$  | $4$ |
| $1$  | $3$ |
| $2$  | $2$ |
| $3$  | $1$ |

Plot $(-1, 5)$, $(0, 4)$, $(1, 3)$, $(2, 2)$, and $(3, 1)$, then draw the line through them. It slopes downward from left to right, and it crosses the y-axis at $(0, 4)$, just as the equation predicts. The constant gap of $-1$ between consecutive $y$-values confirms you are looking at a straight line.

---

## Example 3: is the relationship linear?

> A table lists the values $(1, 5)$, $(2, 8)$, $(3, 13)$, and $(4, 20)$. Does it come from a linear equation?

Compare the jumps in $y$ as $x$ walks up by $1$: from $5$ to $8$ is $+3$, from $8$ to $13$ is $+5$, and from $13$ to $20$ is $+7$. Since the differences keep growing, the rate of change is not constant, so the relationship is not linear. Plotting the points would produce a curve that gets steeper as you move to the right.

For comparison, the table $(1, 5), (2, 8), (3, 11), (4, 14)$ *is* linear: every step adds exactly $3$. The matching equation is $y = 3x + 2$, because the rule must start at $(0, 2)$ to hit $(1, 5)$ while stepping by $3$. This is a quick way to spot a line without graphing.

---

## Common pitfalls

- **Forgetting the order of operations.** In a rule like $y = 3x - 2$, multiply $3 \cdot x$ *first*, then subtract $2$. If you subtract before multiplying, every row will be wrong by the same amount.
- **Sign slips with negative $x$-values.** Negative inputs multiplied by negative coefficients turn positive — write the full substitution every row until the arithmetic is automatic.
- **Drawing the line through only two points.** Two points do determine a line, but if you compute a third or fourth point and it misses your line, one of the rows is wrong. A five-row table catches those mistakes before you draw.
- **Choosing awkward x-values.** Decimals and huge integers make the arithmetic harder than it needs to be. Stick to small integers unless the problem forces otherwise.

---

## Prerequisites

Before you practice problems on this page, it helps to be comfortable with:

- [[Plotting_Points_And_The_Coordinate_Plane]] — for placing $(x, y)$ pairs on the grid.
- [[Evaluating_Expressions]] — for turning each $x$ into the matching $y$ without arithmetic mistakes.
- [[Integers_And_The_Number_Line]] — so negative coordinates do not throw you off.

When you are ready, [[Slope_Intercept_Form]] shows how to read the slope and intercept directly from $y = mx + b$ so you can sketch the graph without even building a table.

---

## Problems Involving Graphing Linear Equations from Tables

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphing_linear_equations_from_tables"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Plotting_Points_And_The_Coordinate_Plane]]
- [[Slope_Intercept_Form]]
- [[Slope]]
- [[Evaluating_Expressions]]
- [[Writing_Linear_Equations]]
- [[Linear_Functions]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
