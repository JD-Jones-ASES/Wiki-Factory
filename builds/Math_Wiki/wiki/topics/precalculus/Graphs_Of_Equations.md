---
title: "Graphs of Equations"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-analytic-geometry", "#key-topic", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Cartesian_Plane"
  - "topics/precalculus/Graphs_Of_Functions"
  - "topics/precalculus/Relations"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/The_Coordinate_Plane"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Quadratic_Functions"
problem_type_ids: []
figures: []
summary: "How a two-variable equation becomes a picture: every solution pair is a point on the curve, and every point on the curve satisfies the equation."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Graphs of Equations

# Graphs of Equations

An equation in two variables is a rule. It says something like "$y$ is twice $x$ plus one," or "the squared distances to the axes add up to twenty-five." On its own, a rule is abstract — it has no shape. What turns it into a picture is an agreement to interpret each variable as a coordinate and to mark, on the Cartesian plane, every coordinate pair that obeys the rule. The collection of those pairs is the **graph** of the equation, and the graph is what makes the equation feel like a thing you can see.

This bridge from algebra to picture is the central move of analytic geometry. It is the reason drawing curves by hand is a precalculus skill, the reason a calculator can render a function in a fraction of a second, and the reason an equation you have never seen before can become a familiar shape as soon as you plot a handful of its points. This page collects the tools you need for that bridge: how to read an equation's graph, how to find its intercepts, how to test it for symmetry, and how to recognize a small menagerie of standard shapes on sight.

## What the graph actually is

The graph of an equation in $x$ and $y$ is the collection of every coordinate pair $(x, y)$ that turns the equation into a true statement when you substitute. If the equation is $y = 2x - 2$, then the pair $(0, -2)$ is on the graph because $2 \cdot 0 - 2 = -2$ makes the equation true. The pair $(3, 4)$ is also on the graph because $2 \cdot 3 - 2 = 4$ checks out. The pair $(1, 5)$ is **not** on the graph because $2 \cdot 1 - 2 = 0 \ne 5$.

In symbolic form:

$$
\text{graph of } y = f(x, y) \;=\; \{\,(x, y) \in \mathbb{R}^2 \,:\, \text{the equation is true at } (x, y)\,\}.
$$

This means that checking whether a point lies on a curve is a one-step process: substitute the coordinates, see if the equation balances. You should never need to look at a picture to decide — the equation is the final word.

## The small menagerie of standard shapes

Three kinds of equations come up so often in precalculus that you should recognize them on sight.

**Lines.** Any equation of the form $Ax + By = C$, with $A$, $B$, $C$ constant and $A$ and $B$ not both zero, graphs as a straight line. The familiar slope-intercept form $y = mx + b$ is the same thing in disguise — rearrange the general form and you get it. You studied these thoroughly as [[Linear_Functions]] and [[Writing_Linear_Equations|wrote linear equations]] in algebra.

**Circles.** The equation

$$
(x - h)^2 + (y - k)^2 = r^2
$$

graphs as a circle centered at $(h, k)$ with radius $r$. The center is read right off the parentheses, and the radius is the square root of the right-hand side. A circle centered at the origin with radius $5$ simplifies to $x^2 + y^2 = 25$. Circles are not graphs of functions (they fail the vertical line test), but they are perfectly respectable graphs of equations.

**Parabolas.** The equation $y = ax^2 + bx + c$ graphs as a parabola that opens up (if $a > 0$) or down (if $a < 0$). You studied these as [[Quadratic_Functions]] and [[Graphing_Quadratic_Functions|graphed them]] in algebra. A parabola can also open sideways, with an equation of the form $x = ay^2 + by + c$ — the roles of $x$ and $y$ swap, so the curve is a function of $y$ instead of a function of $x$.

Beyond these three, the precalculus menagerie also includes ellipses and hyperbolas (the [[Introduction_To_Conics|conic sections]] chapter), cube-root curves, square-root curves, exponentials, logarithms, and trigonometric waves. Each has a shape that becomes automatic after you sketch it a handful of times.

## Intercepts, symmetry, and the shortcut toolkit

Plotting a curve from scratch is a huge amount of work if you do it one dot at a time. The trick is to find the **special points** where the curve does something that takes only one computation — intercepts and points of symmetry — and use them as anchors. Once the anchors are down, filling in the rest of the curve is mostly a matter of sketching smoothly.

**$x$-intercepts.** These are the points where the graph crosses the $x$-axis — that is, where $y = 0$. Set $y = 0$ in the equation and solve for $x$. Each solution gives you an anchor point on the $x$-axis.

**$y$-intercepts.** These are the points where the graph crosses the $y$-axis — that is, where $x = 0$. Set $x = 0$ in the equation and solve for $y$.

**Symmetry tests.** A graph is symmetric about the $y$-axis if replacing $x$ with $-x$ leaves the equation unchanged. It is symmetric about the $x$-axis if replacing $y$ with $-y$ leaves the equation unchanged. And it is symmetric about the origin if replacing both $x$ with $-x$ and $y$ with $-y$ leaves the equation unchanged. Symmetry is not just decorative — it literally halves or quarters the plotting work.

**Testing whether a point is on the graph.** Substitute and check. This is the one-step test described above, and it comes up constantly when a problem hands you a candidate point and asks whether it sits on the curve.

## Worked examples

**Example 1.** Sketch the graph of $y = x^2 - 4$ by finding its intercepts, testing its symmetry, and plotting a short table of values.

**Intercepts.** Set $y = 0$: $x^2 - 4 = 0$, so $x^2 = 4$, giving $x = \pm 2$. The $x$-intercepts are $(-2, 0)$ and $(2, 0)$. Set $x = 0$: $y = -4$, so the $y$-intercept is $(0, -4)$.

**Symmetry.** Replace $x$ with $-x$: the equation becomes $y = (-x)^2 - 4 = x^2 - 4$, which is identical to the original. So the graph is symmetric about the $y$-axis. Replace $y$ with $-y$: the equation becomes $-y = x^2 - 4$, which is different from the original (the signs don't match), so the graph is **not** symmetric about the $x$-axis.

**Table.** Using the symmetry, you only need to plot values for $x \ge 0$ and mirror them:

| $x$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $y$ | $-4$ | $-3$ | $0$ | $5$ |

Plotting $(0, -4)$, $(1, -3)$, $(2, 0)$, $(3, 5)$ and their $y$-axis mirrors $(-1, -3)$, $(-2, 0)$, $(-3, 5)$ gives seven points. Connecting them smoothly produces an upward-opening parabola with its lowest point at $(0, -4)$. The vertex sits at the $y$-intercept here because the equation has no linear term in $x$ — whenever a quadratic has the form $y = ax^2 + c$, its vertex sits on the $y$-axis at $(0, c)$.

**Example 2.** Sketch the graph of $x^2 + y^2 = 25$ and identify its center, radius, and intercepts.

Compare the equation to the standard circle form $(x - h)^2 + (y - k)^2 = r^2$. Here $h = 0$, $k = 0$, and $r^2 = 25$, so $r = 5$. The graph is a **circle of radius 5 centered at the origin**.

**Intercepts.** Set $y = 0$: $x^2 = 25$, giving $x = \pm 5$. The $x$-intercepts are $(-5, 0)$ and $(5, 0)$. Set $x = 0$: $y^2 = 25$, giving $y = \pm 5$. The $y$-intercepts are $(0, -5)$ and $(0, 5)$.

**Symmetry.** Replace $x$ with $-x$: $(-x)^2 + y^2 = 25$ is identical to the original, so the graph is symmetric about the $y$-axis. Replace $y$ with $-y$: same story, symmetric about the $x$-axis. Replace both: symmetric about the origin. A circle centered at the origin has all three symmetries at once.

To sketch the circle by hand, draw the four intercepts first — those are anchor points at the top, bottom, left, and right — then connect them with a smooth round curve. A compass (or a drawn approximation of one) makes the rounding precise.

Worth noting: this circle is not the graph of a single function $y = f(x)$, because most vertical lines cross it in two places. Solving for $y$ gives $y = \pm\sqrt{25 - x^2}$, which is really two functions stacked on top of each other — the upper semicircle and the lower semicircle.

**Example 3.** Determine whether the points $(3, 4)$ and $(2, -1)$ lie on the graph of $y = 2x - 2$, and if either does not, find the point on the line directly above or below it.

Substitute the first candidate into the equation. The right-hand side at $x = 3$ is $2 \cdot 3 - 2 = 4$, matching the $y$-coordinate of $(3, 4)$. So **$(3, 4)$ is on the graph**.

Substitute the second candidate. The right-hand side at $x = 2$ is $2 \cdot 2 - 2 = 2$, while the $y$-coordinate of $(2, -1)$ is $-1$. These do not match, so **$(2, -1)$ is not on the graph**. The point on the line with the same $x$-coordinate is $(2, 2)$ — exactly $3$ units above $(2, -1)$.

You can phrase this as a general rule: a point $(a, b)$ lies on the graph of $y = f(x)$ if and only if $b = f(a)$, and the vertical distance from $(a, b)$ to the graph is $|b - f(a)|$. Here that distance is $|-1 - 2| = 3$, confirming the "3 units above" observation.

## Common pitfalls

- **Confusing "graph of an equation" with "graph of a function."** A circle is a graph of the equation $x^2 + y^2 = 25$, but it is not the graph of any single function $y = f(x)$. Every function graph is an equation graph, but not vice versa. You will see this distinction sharpened on [[Graphs_Of_Functions|graphs of functions]].
- **Forgetting to check both $x$-intercept solutions.** When you set $y = 0$ and solve, you often get two or more values of $x$. Each one is a separate intercept point — don't abandon the second after writing down the first.
- **Misapplying the symmetry tests.** Symmetry about the $x$-axis uses $y \to -y$; symmetry about the $y$-axis uses $x \to -x$. Mixing up which axis goes with which substitution is the single most common mistake on symmetry questions.
- **Ignoring the domain of the equation.** Sometimes an equation is only true for certain $x$-values — for instance, $y = \sqrt{x}$ only makes sense when $x \ge 0$, so the graph has no points to the left of the $y$-axis. Before you plot, check whether any values of $x$ make the equation undefined.

## Problems Involving Graphs Of Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphs_of_equations"></div>

## See Also

- [[Cartesian_Plane|The Cartesian Plane]] — the coordinate surface these curves live on
- [[Graphs_Of_Functions]] — the special case where the graph represents a function, with additional reading tools
- [[Relations]] — the broader idea of any collection of coordinate pairs on the plane
- [[Introduction_To_Conics]] — the rich family of quadratic two-variable equations (ellipses, hyperbolas, and more)
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
