---
title: "Slope-Intercept Form"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-linear", "#key-formula", "#representation-symbolic", "#representation-graphical", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Graphing_Linear_Equations_From_Tables"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Arithmetic_Sequences_And_Linear_Patterns"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Graphing_Linear_Equations_From_Tables"
  - "topics/pre_algebra/Evaluating_Expressions"
problem_type_ids: []
figures: []
summary: "y = mx + b packages the two most useful facts about a line into a single equation."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Slope-Intercept Form

# Slope-Intercept Form

A straight line on the coordinate plane has infinitely many points on it, but you never actually need that many to describe it. You only need two pieces of information: how steeply the line tilts, and one anchor point to pin it in place. Slope-intercept form is the industry-standard way to package both pieces into a single equation. Once you can read that equation, you can sketch the graph, predict where it hits each axis, and compare two lines at a glance. It is the workhorse of every graphing question in pre-algebra and algebra 1.

## What it means

The **slope-intercept form** of a linear equation is

$$
y = mx + b
$$

Each letter plays a specific role.

- $y$ and $x$ are the coordinates of any point on the line. If you pick a value for $x$, the equation tells you exactly one matching value for $y$, and $(x, y)$ is on the line.
- $m$ is the **slope** of the line — the measure of how tilted it is. A positive $m$ means the line climbs as you move to the right; a negative $m$ means it descends; a zero $m$ means it is perfectly flat; and a very large $m$ means it is almost vertical. In number terms, slope is the amount $y$ increases for every one-unit increase in $x$, which is commonly phrased "rise over run":

$$
m \;=\; \frac{\text{rise}}{\text{run}} \;=\; \frac{\Delta y}{\Delta x}
$$

- $b$ is the **$y$-intercept**, which is where the line crosses the vertical axis. Plug $x = 0$ into the formula and you immediately get $y = m(0) + b = b$, so the point $(0, b)$ is always on the line. That point is the anchor.

Together, $m$ and $b$ fully determine the line. Two lines with the same $m$ but different $b$'s are parallel; two lines with the same $b$ but different $m$'s cross at the $y$-axis but lean in different directions; and two lines with the same $m$ and $b$ are actually the same line.

## How it works

The form is most useful in three different directions, and each one corresponds to a common problem type:

- **Building an equation from a graph or description.** If you already know the slope and the $y$-intercept, slot them into the template. "A line with slope $\tfrac{2}{3}$ and $y$-intercept $-5$" becomes $y = \tfrac{2}{3}x - 5$. No computation required.
- **Reading the slope and intercept from an equation.** If the equation is already in the form $y = mx + b$, the values are just the coefficients you see. For $y = -4x + 7$, the slope is $-4$ and the intercept is $7$. If the equation is not yet in that form — say $2x + 3y = 12$ — rearrange until $y$ is alone on one side. Subtract $2x$ from both sides to get $3y = -2x + 12$, then divide everything by $3$ to get $y = -\tfrac{2}{3}x + 4$. Now the slope is $-\tfrac{2}{3}$ and the intercept is $4$.
- **Graphing the line.** Plot $(0, b)$ first — that is your anchor point on the $y$-axis. From there, use the slope as a movement rule. Interpret $m$ as rise over run; if $m = \tfrac{2}{3}$, move up $2$ and right $3$ to find a second point. Draw the line through the two points.

## Why it works

Why does a single pair of numbers — one for slope, one for intercept — capture a whole infinite line? The answer is that a line is the simplest possible relationship between $x$ and $y$: as $x$ changes by a fixed step, $y$ changes by a proportional fixed step, and there is no curvature anywhere along the way. The slope captures that proportion. Once the proportion is set, the only remaining freedom is where the line sits vertically, and that is what the intercept fixes. There is literally nothing more to specify.

The specific form $y = mx + b$ also makes it effortless to compute $y$ for any $x$ you care about — just plug in. That is why it is the form your graphing calculator, spreadsheet, and programming language all expect. Other forms of a linear equation (standard form, point-slope form) carry the same information in different clothing, but slope-intercept form is the one that is easiest to read out loud.

## Worked examples

### Example 1

Write the slope-intercept form of a line with slope $3$ and $y$-intercept $-4$.

This one is a straight substitution. The template is $y = mx + b$. With $m = 3$ and $b = -4$:

$$
y = 3x + (-4)
$$

Clean up the sign so the equation reads the usual way:

$$
y = 3x - 4
$$

The line climbs three units of $y$ for every one unit of $x$, and it crosses the $y$-axis at $-4$.

### Example 2

Put the equation $4x + 2y = 10$ into slope-intercept form, and state the slope and the $y$-intercept.

The equation is in what is called standard form, but you want the $y$ alone. Start by subtracting $4x$ from both sides so only the $y$-term stays on the left:

$$
2y = -4x + 10
$$

Next, divide every term on both sides by $2$ so the coefficient of $y$ becomes $1$:

$$
y = -2x + 5
$$

The equation is now in slope-intercept form. Read off the values: $m = -2$ and $b = 5$. The slope is $-2$, meaning the line drops two units of $y$ for every one unit of $x$ you move to the right, and the line crosses the $y$-axis at the point $(0, 5)$.

### Example 3

Graph the line $y = \tfrac{1}{2}x + 3$ on the coordinate plane, using only the slope and intercept to locate points.

Start at the $y$-intercept. $b = 3$, so the anchor point is $(0, 3)$. Mark it clearly on the $y$-axis.

Next, use the slope to find a second point. $m = \tfrac{1}{2}$, which reads as "rise $1$, run $2$." From the anchor, move right $2$ units and up $1$ unit. You land at $(2, 4)$. Mark that.

Two points are enough to draw a line, but a third makes the drawing more reliable. Repeat the slope move from $(2, 4)$: right $2$, up $1$, arriving at $(4, 5)$. Mark that too. The three points $(0, 3)$, $(2, 4)$, and $(4, 5)$ should fall in a perfectly straight line. Draw a ruler through all three and extend the line across the graph. You can also check backward — from the anchor, move left $2$ and down $1$ to reach $(-2, 2)$, another valid point on the same line.

## Common pitfalls

- **Mixing up the $x$-intercept and the $y$-intercept.** In slope-intercept form, $b$ is the $y$-intercept — the spot where the line meets the $y$-axis. The $x$-intercept is a different point, found by setting $y = 0$ and solving for $x$. They coincide only if the line passes through the origin.
- **Flipping rise and run in the slope.** The vertical change belongs in the numerator and the horizontal change in the denominator — never swap them. Writing $m = \tfrac{3}{2}$ when you meant $\tfrac{2}{3}$ is one of the most common slips.
- **Forgetting to divide every term when isolating $y$.** When the coefficient of $y$ in an equation is not $1$, you have to divide both the $x$-term and the constant by that coefficient. Dividing only the $y$-term leaves a garbled equation that no longer describes the original line.
- **Taking the sign of $b$ at face value in equations written with a minus.** The equation $y = 2x - 7$ is the same as $y = 2x + (-7)$, which means $b = -7$, not $7$. The $y$-intercept is the point $(0, -7)$.

## Problems Involving Slope-Intercept Form

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="slope_intercept_form"></div>

## See Also

- [[Graphing_Linear_Equations_From_Tables]]
- [[Plotting_Points_And_The_Coordinate_Plane]]
- [[Arithmetic_Sequences_And_Linear_Patterns]]
- [[Slope|Slope (Algebra 1)]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
