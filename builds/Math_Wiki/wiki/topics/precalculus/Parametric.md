---
title: "Parametric Equations"
type: topic
aliases: ["Parametric Curves", "Parameterized Curves", "Parametric Equations"]
tags: ["#branch-pre-calculus", "#topic-functions", "#topic-analytic-geometry", "#skill-visualization", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Functions_And_Relations"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Vectors"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Functions_And_Relations"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
problem_type_ids: []
figures: []
summary: "Describe a curve in the plane by giving the horizontal and vertical position as separate functions of a third variable, usually interpreted as time, so the curve comes with both a shape and a direction of travel built in."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Parametric Equations

# Parametric Equations

Every rectangular equation of the form $y = f(x)$ has a built-in constraint: for each $x$, there is at most one $y$. That restriction is what makes $y = f(x)$ a function in the strict sense. It is also what rules out an enormous class of interesting curves. A circle fails the vertical line test. A horizontal parabola fails it. Any path that crosses itself or loops back fails it. Rectangular function notation runs out of room almost as soon as you leave the simplest curves behind.

**Parametric equations** fix this by stepping outside the $y$-is-a-function-of-$x$ box. Instead of tying $y$ directly to $x$, they introduce a third variable — usually called $t$ and often thought of as time — and write both $x$ and $y$ as separate functions of $t$:

$$
x = f(t), \qquad y = g(t).
$$

At each value of $t$, you get an ordered pair $(f(t), g(t))$, which plots as a point in the plane. As $t$ runs across its domain, those points trace out a curve. Because $x$ and $y$ are independent outputs, nothing forces the curve to pass the vertical line test — a parametric curve can loop, cross itself, or double back without breaking any rule.

The $t$ does more than just sidestep the function restriction. It also builds **orientation** into the curve. At $t = 0$ you are at a particular starting point; as $t$ increases you move through the curve in a particular direction; if you were to watch the graph drawn in real time, you would see a path with a definite sense of travel. That direction is additional information the rectangular form usually discards.

---

## The parameter has physical meaning

In nearly every application, $t$ carries a real-world interpretation. In projectile motion, $t$ is time measured in seconds, and the equations

$$
x(t) = x_0 + v_x t, \qquad y(t) = y_0 + v_y t - \tfrac{1}{2}g t^2
$$

describe the horizontal and vertical position of a thrown object at the same instant. Eliminating $t$ would give a single rectangular equation for the trajectory — a parabola — but would lose the timestamp that tells you exactly when the ball reaches its peak or when it hits the ground. Parametric form keeps both pieces of information at once.

In the description of circular or elliptical motion, $t$ can play the role of an angle. For the unit circle, the parametric form

$$
x(t) = \cos t, \qquad y(t) = \sin t
$$

traces the circle counterclockwise starting from $(1, 0)$ at $t = 0$, reaching $(0, 1)$ at $t = \pi/2$, and returning to the start at $t = 2\pi$. Every point of the unit circle is covered once, and the direction of travel is baked into the equations.

---

## Parameterizing a line through two points

One of the cleanest parametric setups is a straight line. Given two points $P_0 = (x_0, y_0)$ and $P_1 = (x_1, y_1)$, the line through them can be parameterized by linear interpolation:

$$
x(t) = x_0 + (x_1 - x_0) t, \qquad y(t) = y_0 + (y_1 - y_0) t.
$$

At $t = 0$ you sit at $P_0$; at $t = 1$ you sit at $P_1$; for $t$ between $0$ and $1$ you sit somewhere along the segment; for $t$ outside that interval you are on the line but beyond one of the two anchor points. The direction vector $(x_1 - x_0, y_1 - y_0)$ makes the orientation visible: every unit of $t$ moves you by that vector's worth of displacement.

This is the same idea you meet again in [[Vectors|vector]] form: a point is a vector, a direction is another vector, and the line is the set of all points you can reach by adding a scalar multiple of the direction vector to the starting point.

---

## Eliminating the parameter

Sometimes you want to know the pure shape of a curve — the set of points traced out — without caring about the timing. The operation that removes $t$ from the picture and leaves behind a single rectangular equation is called **eliminating the parameter**. The standard recipe is:

1. Solve one of the two parametric equations for $t$ in terms of the variable it involves ($x$ or $y$).
2. Substitute that expression into the other equation so that $t$ disappears.
3. Simplify the result to whatever rectangular form feels clean.

Eliminating the parameter is useful when a question asks, "What does this curve look like in terms of $x$ and $y$?" and does not care about the direction of travel or the rate of motion. But be aware: the rectangular equation you end up with may describe *more* points than the original parametric curve did. For example, $x = t^2$ and $y = t$ gives a rightward parabola when you eliminate the parameter — but only the part where $y$ matches the sign of the square root branch covered by the actual $t$ values. Always check whether your parametric domain covers the whole rectangular curve or just a piece.

Certain parametric curves resist clean elimination. A cycloid, the path of a point on a rolling wheel, has the parameterization $x = t - \sin t$, $y = 1 - \cos t$. There is no elementary rectangular equation for it — the parametric form is the only form.

---

## Trigonometric parameterizations are the natural home of circles and ellipses

The unit circle case generalizes cleanly. A circle of radius $R$ centered at $(h, k)$ can be parameterized by

$$
x(t) = h + R\cos t, \qquad y(t) = k + R\sin t,
$$

with $t \in [0, 2\pi]$ covering the circle exactly once. An ellipse with semi-axes $a$ and $b$ centered at $(h, k)$ becomes

$$
x(t) = h + a\cos t, \qquad y(t) = k + b\sin t.
$$

Eliminating the parameter in either case uses the Pythagorean identity $\cos^2 t + \sin^2 t = 1$. For the circle, $\left(\dfrac{x - h}{R}\right)^2 + \left(\dfrac{y - k}{R}\right)^2 = 1$, which rearranges to $(x - h)^2 + (y - k)^2 = R^2$. Same shape, new form.

These trigonometric parameterizations are by far the most common ones on test problems and in applications, because so many physical systems — planets, wheels, pendulums, alternating current — have circular or elliptical structure underneath.

---

## Example 1: parameterizing a line through two points

> Write a parametric description of the line through $(1, -2)$ and $(5, 6)$ such that $t = 0$ lands at the first point and $t = 1$ lands at the second.

The direction from $(1, -2)$ to $(5, 6)$ has components $5 - 1 = 4$ and $6 - (-2) = 8$. Using the linear interpolation formula:

$$
x(t) = 1 + 4t, \qquad y(t) = -2 + 8t.
$$

Check $t = 0$: $x(0) = 1$ and $y(0) = -2$, matching the first point. Check $t = 1$: $x(1) = 1 + 4 = 5$ and $y(1) = -2 + 8 = 6$, matching the second. The parameter value $t = 1/2$ lands at $(3, 2)$, the midpoint of the segment — exactly where you expect.

A quick rectangular check: the slope should be $\dfrac{6 - (-2)}{5 - 1} = \dfrac{8}{4} = 2$. From the parametric form, a unit increase in $t$ adds $4$ to $x$ and $8$ to $y$, giving the same slope of $\dfrac{8}{4} = 2$. Parametric and rectangular forms agree on the slope of the line, as they must.

---

## Example 2: converting $x = t^2, y = 2t$ to rectangular form

> Eliminate the parameter from $x = t^2$, $y = 2t$ and describe the resulting curve.

Solve the second equation for $t$: $t = y/2$. Substitute into the first:

$$
x = \left(\dfrac{y}{2}\right)^2 = \dfrac{y^2}{4},
$$

which rearranges to $y^2 = 4x$. This is a parabola opening to the right with vertex at the origin.

Because $y = 2t$ can take any real value (every $y$ is $2$ times some real $t$), the parametric curve covers the entire rightward parabola — not just a piece. The direction of travel on the curve is encoded in the sign of $t$: as $t$ increases from $-\infty$ to $0$, the curve sweeps through the lower branch of the parabola from far lower right toward the vertex; as $t$ continues from $0$ to $+\infty$, the curve sweeps up the upper branch to far upper right. Eliminating the parameter gives the shape $y^2 = 4x$ but hides the detail about which direction the curve is being traced.

---

## Example 3: the unit circle as $(\cos t, \sin t)$

> Use the parameterization $x(t) = \cos t$, $y(t) = \sin t$ to plot the unit circle over $t \in [0, 2\pi]$. Check a few points and confirm the direction of travel.

Evaluate at four anchor values:

| $t$ | $\cos t$ | $\sin t$ | point |
|---|---|---|---|
| $0$ | $1$ | $0$ | $(1, 0)$ |
| $\pi/2$ | $0$ | $1$ | $(0, 1)$ |
| $\pi$ | $-1$ | $0$ | $(-1, 0)$ |
| $3\pi/2$ | $0$ | $-1$ | $(0, -1)$ |

The curve starts on the positive $x$-axis at $(1, 0)$, moves to the top of the circle at $(0, 1)$, continues to the negative $x$-axis at $(-1, 0)$, descends to the bottom at $(0, -1)$, and returns to the start at $(1, 0)$ when $t = 2\pi$. The direction of travel is **counterclockwise** — the default convention for trigonometric parameterizations.

To confirm this is really the unit circle, eliminate the parameter by squaring both equations and adding:

$$
x^2 + y^2 = \cos^2 t + \sin^2 t = 1.
$$

The Pythagorean identity delivers the rectangular equation $x^2 + y^2 = 1$ immediately. Notice that the rectangular form tells you the shape is a unit circle but not which way it is being traced; that information only survives in the parametric form.

If you wanted the same shape traced **clockwise**, you could use $(\cos t, -\sin t)$ or equivalently $(\cos(-t), \sin(-t))$. Both produce the same circle but run the animation in reverse.

---

## Common pitfalls

- **Eliminating the parameter and losing part of the curve.** The rectangular equation you recover may describe more points than the parametric curve actually hits. Always check whether the parameter domain covers the whole rectangular curve.
- **Forgetting the direction of travel.** The parametric form carries orientation information that the rectangular form throws away. If a question asks about direction, the answer has to come from the parametric form.
- **Confusing the parameter with one of the coordinates.** The input $t$ is a third variable that is usually invisible on the final graph — you never see a $t$-axis in a 2D parametric plot. The graph lives in the $xy$-plane and is a projection of the motion.
- **Mixing up the starting point of a line parameterization.** The form $x(t) = x_0 + (x_1 - x_0)t$ has $t = 0$ at $(x_0, y_0)$, not at the origin. Dropping the $x_0$ and $y_0$ terms shifts the whole line to pass through the origin instead of through your starting point.
- **Assuming one parameterization is the only one.** The same curve can be traced by infinitely many different parameterizations, each with a different speed or direction. Saying "the parametric form" of a curve is usually sloppy — there is no unique one.

---

## Prerequisites

- [[Relations_And_Functions|Relations and Functions]] — the idea that a curve in the plane does not have to be the graph of a single-valued function
- [[The_Unit_Circle]] — the exact values of cosine and sine that drive the most common trigonometric parameterizations
- [[Circular_Functions]] — sine and cosine as continuous functions, needed to evaluate $x(t)$ and $y(t)$ at arbitrary $t$

---

## Problems Involving Parametric Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="parametric"></div>

---

## See Also

- [[Vectors]] — the same parameterize-with-a-direction idea applied in vector form
- [[Relations_And_Functions|Relations and Functions]] — how parametric curves sit in the wider landscape of plane curves
- [[The_Unit_Circle]] — the source of the trigonometric parameterizations of circles and ellipses
- [[Polar_Graphs]] — another way to describe curves using an angle, closely related to parametric form
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
