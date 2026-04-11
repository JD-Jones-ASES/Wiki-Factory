---
title: "Graphs of Polar Equations"
type: topic
aliases: ["Polar Graphs", "Polar Curves", "Graphs of Polar Equations"]
tags: ["#branch-pre-calculus", "#topic-analytic-geometry", "#skill-visualization", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Introduction_To_Polar_Coordinates"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Polar_Form_Of_Complex_Numbers"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Introduction_To_Polar_Coordinates"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
problem_type_ids: []
figures: []
summary: "Once a point can be named by a radius and an angle, an equation of the form r = f(theta) carves out a curve whose shape — circle, cardioid, rose, limacon, spiral — depends entirely on how f responds as theta sweeps through a full turn."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Graphs of Polar Equations

# Graphs of Polar Equations

A rectangular graph answers the question, "as $x$ changes, what does $y$ do?" by plotting a vertical response against a horizontal input. The grid is flat, the axes are perpendicular, and every function traces out a curve that respects the left-right march of the domain.

Polar graphing asks a different question entirely: "as the angle $\theta$ sweeps counterclockwise from the polar axis, how far from the pole does the curve reach?" The input is no longer a left-right position — it is a direction. The output is no longer an up-down height — it is a distance. Because the input rotates, the curves that result from simple polar equations look nothing like the curves that come out of simple rectangular equations. A single expression as tame as $r = 1 + \cos\theta$ traces out a heart-shaped cardioid that has no clean rectangular formula at all.

$$
r = f(\theta) \qquad \text{means} \qquad (x, y) = \big(f(\theta)\cos\theta,\; f(\theta)\sin\theta\big).
$$

Every polar equation is silently a parameterization of the plane by $\theta$: you tell me an angle, and I compute a radius and therefore a point. Stringing the points together as $\theta$ runs through a full revolution gives the graph.

---

## The simplest cases: constant $r$ and constant $\theta$

Two polar equations are so basic they barely need a plotting step. The equation $r = a$ says "no matter what the angle is, the distance from the pole equals $a$." That is exactly the definition of a circle of radius $|a|$ centered at the pole. The angle $\theta$ never appears on the right side, so the graph is invariant under rotation — a feature of any polar equation whose right side is a constant.

The equation $\theta = \theta_0$ says "no matter what the radius is, the angle from the polar axis is always $\theta_0$." That traces out a straight line through the pole in the direction $\theta_0$ and its opposite direction $\theta_0 + \pi$. Both halves of the line count because polar conventions allow $r$ to be negative.

These two facts are the polar analogs of the rectangular $y = \text{constant}$ and $x = \text{constant}$ lines, except the roles are swapped: constant radius gives a circle, constant angle gives a line.

---

## Circles that are not centered at the pole

Something subtle happens when the equation looks like $r = 2a\cos\theta$ or $r = 2a\sin\theta$. These are also circles, but they are **not** centered at the pole. Multiplying both sides of $r = 2a\cos\theta$ by $r$ gives $r^2 = 2ar\cos\theta$, which translates to $x^2 + y^2 = 2ax$ by the standard conversions. Moving the $2ax$ over and completing the square lands on $(x - a)^2 + y^2 = a^2$, a circle of radius $|a|$ centered at $(a, 0)$. The graph passes through the pole at $\theta = \pi/2$ (where $\cos\theta = 0$) and reaches its farthest point at $\theta = 0$.

In the same way, $r = 2a\sin\theta$ is a circle of radius $|a|$ centered at $(0, a)$, passing through the pole at $\theta = 0$ and reaching its peak at $\theta = \pi/2$.

Recognizing these patterns saves you from plotting point-by-point: whenever you see $r$ equal to a number times a single cosine or sine of $\theta$ (nothing else added, nothing inside the function but $\theta$), you are looking at a circle through the pole.

---

## Cardioids and limacons

Add a constant to the cosine or sine term and the circle distorts into a family called **limacons**. The general form is

$$
r = a + b\cos\theta \qquad \text{or} \qquad r = a + b\sin\theta,
$$

with $a, b > 0$. The comparison of $a$ and $b$ determines the shape:

- If $a = b$, the limacon is a **cardioid** — a heart-shaped curve that passes through the pole with a cusp and has no inner loop. The equation $r = 1 + \cos\theta$ is the standard example.
- If $a > b$, the limacon is a **dimpled** shape without an inner loop, somewhere between a cardioid and a circle.
- If $a < b$, the limacon has an **inner loop** that appears when $r$ becomes negative for part of the $\theta$ range.

The role of cosine versus sine is just where the curve points. A cosine-based limacon has its axis of symmetry along the horizontal polar axis. A sine-based limacon has its axis along the vertical line $\theta = \pi/2$. If cosine is positive, the shape bulges to the right; if the sign of $b$ is negative (as in $r = 1 - \cos\theta$), the shape bulges to the left.

---

## Rose curves

The next family comes from plugging a multiple of $\theta$ into the cosine or sine. A **rose curve** has the form

$$
r = a\cos(n\theta) \qquad \text{or} \qquad r = a\sin(n\theta),
$$

with $n$ a positive integer. The graph looks like a flower with a predictable number of petals:

- If $n$ is **odd**, the curve has exactly $n$ petals.
- If $n$ is **even**, the curve has exactly $2n$ petals.

The rule feels strange at first. An odd $n$ causes the second half of the $\theta$ sweep to retrace the same points the first half already drew (because cosine and sine pick up a sign flip on a half-turn, and the negative radius lands you back on top of a petal you already plotted). An even $n$ does not retrace, so every petal traced in the first half of the sweep gets a fresh mate in the second half.

The magnitude $|a|$ sets the length of each petal: the tip of a petal sits at distance $|a|$ from the pole. Cosine versions point a petal along the polar axis; sine versions point a petal upward along $\theta = \pi/2$.

---

## Symmetry shortcuts

Before plotting dozens of points, check for symmetries. Each polar symmetry lets you plot half (or a quarter) of the curve and copy the rest.

- **Symmetry about the polar axis** (the horizontal axis): if replacing $\theta$ with $-\theta$ leaves the equation unchanged, the graph is symmetric across the polar axis. Cosine-based equations like $r = 1 + \cos\theta$ pass this test because $\cos(-\theta) = \cos\theta$.
- **Symmetry about the line $\theta = \pi/2$** (the vertical axis): if replacing $\theta$ with $\pi - \theta$ leaves the equation unchanged, the graph is symmetric across the vertical axis. Sine-based equations pass this test because $\sin(\pi - \theta) = \sin\theta$.
- **Symmetry about the pole** (a half-turn rotation): if replacing $r$ with $-r$ (or $\theta$ with $\theta + \pi$) leaves the equation unchanged, the graph is symmetric through the pole. Equations with only even powers of $r$ and of the trig function pass this test.

These are sufficient conditions, not necessary ones — a curve might have a symmetry that a naive test misses because of the many-descriptions issue polar coordinates inherit. Visual confirmation after plotting is the best safety net.

---

## Example 1: the circle $r = 2\cos\theta$

> Identify and sketch the curve $r = 2\cos\theta$.

This matches the $r = 2a\cos\theta$ pattern with $a = 1$, so the graph is a circle of radius $1$ centered at $(1, 0)$ in rectangular coordinates. To confirm, build a small table of $(\theta, r)$ values:

| $\theta$ | $\cos\theta$ | $r$ |
|---|---|---|
| $0$ | $1$ | $2$ |
| $\pi/4$ | $\sqrt{2}/2$ | $\sqrt{2} \approx 1.41$ |
| $\pi/2$ | $0$ | $0$ |
| $3\pi/4$ | $-\sqrt{2}/2$ | $-\sqrt{2}$ |
| $\pi$ | $-1$ | $-2$ |

From $\theta = 0$ the point sits at distance $2$ along the polar axis, giving rectangular $(2, 0)$. At $\theta = \pi/2$ the radius collapses to $0$, and the curve passes through the pole. Between those angles, the points trace the upper half of a circle. The values from $\theta = \pi/2$ to $\theta = \pi$ have negative $r$, which flips each point through the pole — and lands you exactly on the lower half of the same circle. So the full curve is already drawn by the time $\theta$ reaches $\pi$; the second half of the revolution simply retraces it. The graph is a single circle of radius $1$, tangent to the vertical axis at the pole and reaching rightward to $(2, 0)$.

---

## Example 2: the cardioid $r = 1 + \cos\theta$

> Describe the graph of $r = 1 + \cos\theta$ and locate its key features.

Because $a = b = 1$, this is a cardioid. Symmetry check: replace $\theta$ with $-\theta$. Cosine is even, so $1 + \cos(-\theta) = 1 + \cos\theta$, and the curve is symmetric across the polar axis. You only need to trace it from $\theta = 0$ to $\theta = \pi$ and mirror the result.

Build a table:

| $\theta$ | $\cos\theta$ | $r = 1 + \cos\theta$ |
|---|---|---|
| $0$ | $1$ | $2$ |
| $\pi/3$ | $1/2$ | $3/2$ |
| $\pi/2$ | $0$ | $1$ |
| $2\pi/3$ | $-1/2$ | $1/2$ |
| $\pi$ | $-1$ | $0$ |

The maximum radius, $r = 2$, happens at $\theta = 0$ and sits on the polar axis at rectangular $(2, 0)$. As $\theta$ swings counterclockwise to $\pi/2$, the radius shrinks to $1$, and the curve crosses the vertical axis at $(0, 1)$. By $\theta = \pi$ the radius has collapsed to $0$, so the curve passes through the pole and creates the distinctive cusp on the left side. Mirror the upper half across the polar axis to get the lower half, and the result is a heart-shaped cardioid pointing rightward, wider on the right, tapering to a cusp at the pole on the left. The widest point across the pole-to-cusp axis is $2$.

---

## Example 3: the four-petaled rose $r = 2\sin(2\theta)$

> Sketch $r = 2\sin(2\theta)$.

With $n = 2$ (even), the rose rule predicts $2n = 4$ petals. The maximum radius is $|a| = 2$, so each petal reaches distance $2$ from the pole. Because the equation uses sine, the petal tips are perpendicular to where cosine petals would sit — specifically, petals point along the directions where $\sin(2\theta) = \pm 1$.

Solve $2\theta = \pi/2$ for the first petal tip: $\theta = \pi/4$. So one petal points into the first quadrant along the direction $\theta = \pi/4$. The next tip comes from $2\theta = 3\pi/2$, giving $\theta = 3\pi/4$, a petal into the second quadrant. The remaining two petals show up at $\theta = 5\pi/4$ and $\theta = 7\pi/4$, one in each of the third and fourth quadrants. Each petal passes through the pole at the $\theta$-values where $\sin(2\theta) = 0$, namely $\theta = 0, \pi/2, \pi, 3\pi/2$, which split the plane into the four sectors that hold the petals.

The completed graph is a four-petaled rose with petals oriented at $45^{\circ}$ angles — one pointing into each open quadrant, reaching a maximum distance of $2$ at its tip.

---

## Common pitfalls

- **Treating $r$ as only positive.** Polar graphing allows negative radii, and most cardioid and rose curves actively use them. Skipping the $\theta$-values where $r < 0$ removes half the graph.
- **Miscounting petals.** The rose-petal rule has the opposite parity behavior most students expect: odd $n$ gives $n$ petals, even $n$ gives $2n$. Memorize this once, not each time.
- **Confusing cosine with sine in the orientation.** A cosine-based curve has its feature aligned with the polar axis. A sine-based curve has the same shape rotated by $\pi/2$. They are the same family, just rotated.
- **Failing to use symmetry.** Computing 16 points when four would have fit because the curve is symmetric wastes time and invites arithmetic slips. Always check symmetry before plotting.
- **Thinking the interval always has to be $[0, 2\pi]$.** Some polar curves close in less than a full revolution — $r = 2\cos\theta$, for example, retraces itself after $\theta = \pi$. Others, like the Archimedean spiral $r = \theta$, never close at all and grow without bound.

---

## Prerequisites

- [[Introduction_To_Polar_Coordinates]] — the $(r, \theta)$ naming system and the conversions to and from rectangular coordinates
- [[The_Unit_Circle]] — the exact values of cosine and sine at the special angles, which drive every point on a table-based plot
- [[Circular_Functions]] — sine and cosine as functions of a real input, needed to build and read $r = f(\theta)$

---

## Problems Involving Graphs Of Polar Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polar_graphs"></div>

---

## See Also

- [[Introduction_To_Polar_Coordinates]] — the coordinate system that sets the stage for polar equations
- [[Polar_Form_Of_Complex_Numbers]] — the same $(r, \theta)$ picture applied to complex numbers
- [[Circular_Functions]] — the sine and cosine that shape most polar curves
- [[Introduction_To_Conics]] — circles, ellipses, parabolas, and hyperbolas that reappear as simple polar equations
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
