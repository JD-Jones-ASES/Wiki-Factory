---
title: "The Cartesian Plane"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-analytic-geometry", "#key-topic", "#test-sat", "#test-act", "#test-psat", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Graphs_Of_Equations"
  - "topics/precalculus/Graphs_Of_Functions"
  - "topics/precalculus/Introduction_To_Polar_Coordinates"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/The_Coordinate_Plane"
  - "topics/pre_algebra/The_Distance_Formula"
problem_type_ids: []
figures: []
summary: "A precalculus-level review of the two-axis coordinate grid, with a sharper focus on reading curves instead of just plotting isolated points."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > The Cartesian Plane

# The Cartesian Plane

You learned to plot points on a grid years ago — two perpendicular axes, a dot at $(3, -2)$, done. What changes in precalculus is that plotting individual points is no longer the main event. From here forward you will use the plane to draw **curves**: the full graph of an equation, the shape of a function, the path of a parametric motion. The grid becomes less of a worksheet and more of a reading surface, and that shift in how you use the plane is worth a deliberate pause.

This page does three things. It reviews the vocabulary of the two-dimensional grid so every later page can lean on the same terms. It sharpens your ability to **read** a curve for its key features — intercepts, symmetry, high points and low points — rather than just plot dots on it. And it draws a clean line between the coordinate plane you will use everywhere and the alternative [[Introduction_To_Polar_Coordinates|polar coordinate system]] you will meet later.

## Vocabulary of the grid

Two perpendicular number lines cross at a single point called the **origin**. The horizontal line is the $x$-axis and the vertical line is the $y$-axis. The two axes together carve the plane into four regions called **quadrants**, numbered counterclockwise starting from the upper right:

- Quadrant I: $x > 0$ and $y > 0$
- Quadrant II: $x < 0$ and $y > 0$
- Quadrant III: $x < 0$ and $y < 0$
- Quadrant IV: $x > 0$ and $y < 0$

Every location in the plane is named by a pair $(x, y)$ where the first coordinate tells you how far to move horizontally from the origin and the second coordinate tells you how far to move vertically. The pair $(x, y)$ is *ordered*, meaning the slot each number sits in matters: $(3, -2)$ and $(-2, 3)$ are different locations entirely.

The distance between any two points $(x_1, y_1)$ and $(x_2, y_2)$ comes from the [[The_Distance_Formula|distance formula]]:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.
$$

This is just the Pythagorean theorem applied to the right triangle whose legs are the horizontal and vertical gaps between the two points.

## From points to curves

An equation in two variables — something like $y = x^2 - 4$ or $x^2 + y^2 = 25$ — picks out a subset of the plane: the collection of every $(x, y)$ that makes the equation true. That subset, plotted on the coordinate grid, is the **graph** of the equation, and getting good at reading graphs is the main skill this chapter demands. The phrase "reading a graph" covers several specific habits.

**Intercepts.** The $x$-**intercepts** of a graph are the points where the curve touches the $x$-axis — that is, where $y = 0$. Setting $y = 0$ in the equation and solving for $x$ gives these points. The $y$-**intercept** is the point where the curve meets the $y$-axis, found by setting $x = 0$ and solving for $y$. A polynomial graph has at most one $y$-intercept (because a function can have only one output at $x = 0$), but it can have many $x$-intercepts.

**Symmetry.** A graph is **symmetric about the $y$-axis** if, whenever $(a, b)$ is on the curve, so is $(-a, b)$. It is **symmetric about the $x$-axis** if $(a, -b)$ is also on the curve whenever $(a, b)$ is. And it is **symmetric about the origin** if $(-a, -b)$ is also on the curve whenever $(a, b)$ is. Symmetry lets you cut your work in half: if you know the graph in one quadrant and you know its symmetry, you can reflect to fill in the rest for free.

**Extrema.** The highest point on a graph is its maximum; the lowest point is its minimum. These are written as coordinate pairs, not just single numbers — "the maximum is at $(2, 9)$" means the curve reaches a height of $y = 9$ at $x = 2$.

**Increasing and decreasing behavior.** As you sweep $x$ from left to right, the height $y$ of the curve might go up or might go down. An interval where the curve rises as $x$ increases is where the graph is "increasing"; an interval where the curve falls is where it is "decreasing." You will meet these ideas in more detail on [[Graphs_Of_Functions|graphs of functions]], where there is a formal definition and a standard way to record the intervals.

## The coordinate plane is a choice

One easy-to-miss point: the grid you are using is *one* coordinate system, not *the* coordinate system. The Cartesian plane measures location with two perpendicular distances. [[Introduction_To_Polar_Coordinates|Polar coordinates]] measure location with a distance and an angle. Both name every point in the plane, but they do so with different kinds of information, and some shapes are dramatically easier to describe in one system than the other. A circle of radius $5$ centered at the origin is the clunky $x^2 + y^2 = 25$ in Cartesian form but just $r = 5$ in polar form. A straight vertical line is $x = 3$ in Cartesian form but $r\cos\theta = 3$ in polar form. Part of the skill of precalculus is noticing which coordinate system a problem wants.

## Worked examples

### Example 1

The graph of $y = -(x - 2)^2 + 9$ is a parabola. Identify the vertex, the $y$-intercept, the $x$-intercepts, and any symmetry of the graph.

The expression is already in vertex form $y = a(x - h)^2 + k$ with $a = -1$, $h = 2$, $k = 9$. That makes the **vertex** the point $(2, 9)$. Because $a < 0$, the parabola opens downward, so the vertex is a maximum. The curve climbs toward that peak from the left, reaches $y = 9$ at $x = 2$, then falls symmetrically on the other side.

For the $y$-**intercept**, plug in $x = 0$: $y = -(0 - 2)^2 + 9 = -4 + 9 = 5$. The $y$-intercept is $(0, 5)$.

For the $x$-**intercepts**, plug in $y = 0$ and solve:

$$
0 = -(x - 2)^2 + 9 \;\Longrightarrow\; (x - 2)^2 = 9 \;\Longrightarrow\; x - 2 = \pm 3,
$$

so $x = 5$ or $x = -1$. The $x$-intercepts are $(-1, 0)$ and $(5, 0)$.

For the **symmetry**, every parabola $y = a(x - h)^2 + k$ is symmetric about the vertical line $x = h$. Here that line is $x = 2$. The curve is not symmetric about either axis or about the origin (the axis of symmetry is shifted sideways), but it *is* symmetric about the line $x = 2$, and you can see this by noting that the two $x$-intercepts $-1$ and $5$ sit equally far from $x = 2$ — both at distance $3$.

### Example 2

The function $f(x) = x^3 - 3x$ has the following table of values for $-2 \le x \le 2$:

| $x$ | $-2$ | $-1.5$ | $-1$ | $0$ | $1$ | $1.5$ | $2$ |
|---|---|---|---|---|---|---|---|
| $y$ | $-2$ | $1.125$ | $2$ | $0$ | $-2$ | $-1.125$ | $2$ |

Plot these seven points and describe the shape.

Placing the dots in order, you get a curve that starts low at $(-2, -2)$, rises to a local peak near $(-1, 2)$, falls through the origin to a local valley near $(1, -2)$, and rises again to $(2, 2)$. The shape is an S-curve that passes through the origin. Two features jump out after you plot the points:

- The curve is symmetric about the origin. Every point $(a, b)$ on the graph pairs with $(-a, -b)$ also on the graph. You can see this directly in the table: $(1, -2)$ matches $(-1, 2)$, and $(1.5, -1.125)$ matches $(-1.5, 1.125)$.
- There is a local maximum around $x = -1$ and a local minimum around $x = 1$, each at height roughly $|y| = 2$.

This is the right shape for a cubic with a negative turning region. Once you have the shape, a quick sanity check: the three $x$-intercepts of $x^3 - 3x = x(x^2 - 3)$ are $x = 0$ and $x = \pm\sqrt{3} \approx \pm 1.73$, which is consistent with the curve crossing zero between your plotted dots.

### Example 3

The point $P(-4, 7)$ is reflected across the $y$-axis, then reflected across the $x$-axis. Give the coordinates of the final image, and give the distance from $P$ to its final image.

Reflecting across the $y$-axis flips the sign of the $x$-coordinate and leaves the $y$-coordinate alone:

$$
(-4, 7) \longmapsto (4, 7).
$$

Reflecting the new point $(4, 7)$ across the $x$-axis flips the sign of the $y$-coordinate and leaves $x$ alone:

$$
(4, 7) \longmapsto (4, -7).
$$

The final image is $Q = (4, -7)$. The two reflections together are exactly a reflection through the origin, which turns any $(a, b)$ into $(-a, -b)$ — a quick way to check your answer.

The distance from $P = (-4, 7)$ to $Q = (4, -7)$ comes from the distance formula:

$$
PQ = \sqrt{(4 - (-4))^2 + (-7 - 7)^2} = \sqrt{8^2 + (-14)^2} = \sqrt{64 + 196} = \sqrt{260} = 2\sqrt{65}.
$$

That is approximately $16.12$ units. Notice that because $Q$ is the reflection of $P$ through the origin, the midpoint of $PQ$ is exactly the origin $(0, 0)$ — another sanity check.

## Common pitfalls

- **Swapping the order of coordinates.** $(3, -2)$ and $(-2, 3)$ are different points and they sit in different quadrants. The horizontal coordinate is always first.
- **Reading the $y$-intercept off the table at the wrong row.** The $y$-intercept happens at $x = 0$, not at $y = 0$ or at the leftmost row of a table. Always check the $x$-value.
- **Confusing symmetry types.** Symmetry about the $y$-axis, about the $x$-axis, and about the origin are three different conditions. A parabola opening upward (like $y = x^2$) has $y$-axis symmetry, but not origin symmetry. A cubic like $y = x^3$ has origin symmetry, but not $y$-axis symmetry. The only graph symmetric about all three is trivial cases like the origin alone.
- **Saying "highest point" when you mean "highest $y$-value."** The maximum of a graph is a **point** (a coordinate pair), not just a number. "The maximum is $9$" is ambiguous; "the maximum is at $(2, 9)$" is unambiguous.

## Problems Involving The Cartesian Plane

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="cartesian_plane"></div>

## See Also

- [[Graphs_Of_Equations]] — how a two-variable equation carves out a curve on this plane
- [[Graphs_Of_Functions]] — when the curve also happens to represent a function, additional reading skills come into play
- [[Introduction_To_Polar_Coordinates]] — the alternative coordinate system where rotation-based shapes become simple
- [[The_Distance_Formula|The Distance Formula]] — the engine behind measuring gaps in the Cartesian plane
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
