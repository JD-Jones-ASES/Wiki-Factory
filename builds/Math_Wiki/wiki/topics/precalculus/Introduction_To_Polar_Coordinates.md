---
title: "Introduction to Polar Coordinates"
type: topic
aliases: ["Polar Coordinates", "Polar Coordinate System", "Pole and Polar Axis"]
tags: ["#branch-pre-calculus", "#topic-unit-circle", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.2"}
related:
  - "topics/precalculus/Polar_Form_Of_Complex_Numbers"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Vectors"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
problem_type_ids: []
figures: ["precalculus/polar_coordinates.svg"]
summary: "A second way of locating points in the plane using a distance from the origin and an angle, with simple conversion formulas to and from rectangular coordinates."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Introduction to Polar Coordinates

# Introduction to Polar Coordinates

The rectangular coordinate system describes a point in the plane by walking a certain distance right and then a certain distance up — two perpendicular measurements. This works, and you have been using it for years, but it is not the only reasonable way to say where a point is. For many problems — circular motion, radar plots, spirals, anything involving rotation about a central point — it is much more natural to describe a point by **how far** it sits from a fixed center and **in what direction**.

That is the idea behind **polar coordinates**. You fix a point called the **pole** (it plays the role of the origin) and a ray from the pole called the **polar axis** (it plays the role of the positive $x$-axis). Every other point in the plane is then named by two numbers: its distance from the pole and the angle its ray makes with the polar axis.

## The notation

A point in polar coordinates is written as the pair

$$
(r, \theta)
$$

where $r$ is the signed distance from the pole and $\theta$ is the angle, measured counterclockwise from the polar axis. Notice immediately that this is the same letter naming you already met in the [[Polar_Form_Of_Complex_Numbers|polar form of complex numbers]] — the geometry is identical, only the object being located is different.

One subtlety sets polar coordinates apart from rectangular ones: a single point in the plane has **infinitely many** different polar descriptions. You can always add a full turn of $2\pi$ to $\theta$ and land on the same point, so $(3, \pi/4)$, $(3, \pi/4 + 2\pi)$, and $(3, \pi/4 - 2\pi)$ all describe the same location. Going further, a negative radius is allowed by convention: $(-r, \theta)$ means "walk a distance $r$ in the direction opposite to $\theta$," which is the same as $(r, \theta + \pi)$. So the point $(3, \pi/4)$ is also $(-3, 5\pi/4)$. This multiplicity feels odd the first time you see it, but it is the price you pay for having a coordinate system built around angles, which are themselves periodic.

![[polar_coordinates.svg|The polar coordinate system]]

---

## Converting between rectangular and polar

Set the pole on top of the origin and the polar axis on top of the positive $x$-axis. Then a point with rectangular coordinates $(x, y)$ and polar coordinates $(r, \theta)$ is locked together by the right triangle whose hypotenuse is $r$. Reading the legs of the triangle gives

$$
x = r\cos\theta, \qquad y = r\sin\theta.
$$

These are the **polar-to-rectangular** conversion formulas. If you know $r$ and $\theta$, compute $x$ and $y$ directly.

The other direction — **rectangular to polar** — uses Pythagoras and the inverse tangent:

$$
r = \sqrt{x^2 + y^2}, \qquad \tan\theta = \frac{y}{x}.
$$

The first formula simply reads off the hypotenuse of the right triangle. The second requires the usual quadrant warning: $\tan^{-1}(y/x)$ from a calculator always returns an angle in $(-\pi/2, \pi/2)$, which cannot distinguish Quadrant II from Quadrant IV or Quadrant III from Quadrant I. After computing $\tan^{-1}(y/x)$, look at the signs of $x$ and $y$, decide which quadrant the point actually lives in, and add $\pi$ if the calculator landed you on the wrong half of the plane.

---

## Example 1: polar to rectangular

> Convert the polar point $(4, 2\pi/3)$ to rectangular coordinates.

Apply $x = r\cos\theta$ and $y = r\sin\theta$ with $r = 4$ and $\theta = 2\pi/3$. From the [[The_Unit_Circle|unit circle]] the standard values are $\cos(2\pi/3) = -1/2$ and $\sin(2\pi/3) = \sqrt{3}/2$. So

$$
x = 4 \cdot \left(-\frac{1}{2}\right) = -2, \qquad y = 4 \cdot \frac{\sqrt{3}}{2} = 2\sqrt{3}.
$$

The point in rectangular coordinates is $(-2, 2\sqrt{3})$. A quick sanity check: the point should sit in Quadrant II because $2\pi/3$ is between $\pi/2$ and $\pi$, and $(-2, 2\sqrt{3})$ has $x < 0$ and $y > 0$, which is Quadrant II. Good.

---

## Example 2: rectangular to polar

> Convert the rectangular point $(-3, -3)$ to polar coordinates with $r > 0$ and $0 \le \theta < 2\pi$.

Compute the modulus first:

$$
r = \sqrt{(-3)^2 + (-3)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}.
$$

For the angle, $\tan\theta = \dfrac{-3}{-3} = 1$, so a calculator returns $\tan^{-1}(1) = \pi/4$. But the point $(-3, -3)$ is in Quadrant III (both coordinates negative), while $\pi/4$ is in Quadrant I. Add $\pi$ to move the angle halfway around the plane:

$$
\theta = \pi/4 + \pi = 5\pi/4.
$$

So the polar form of the point is $(3\sqrt{2}, 5\pi/4)$. Check by converting back: $x = 3\sqrt{2}\cos(5\pi/4) = 3\sqrt{2} \cdot (-\sqrt{2}/2) = -3$, and $y = 3\sqrt{2}\sin(5\pi/4) = 3\sqrt{2} \cdot (-\sqrt{2}/2) = -3$. Matches.

---

## Example 3: multiple descriptions of the same point

> Give three different polar representations of the point whose rectangular form is $(0, 5)$.

The point $(0, 5)$ sits straight up the $y$-axis at distance $5$ from the origin. The most obvious polar form is $r = 5$ and $\theta = \pi/2$ (a quarter turn counterclockwise from the polar axis), giving $(5, \pi/2)$.

Add $2\pi$ to the angle to get a second description: $(5, \pi/2 + 2\pi) = (5, 5\pi/2)$. Same point.

Use a negative radius to get a third description. The rule $(-r, \theta)$ equals $(r, \theta + \pi)$, so the point $(5, \pi/2)$ is the same as $(-5, \pi/2 - \pi) = (-5, -\pi/2)$. All three pairs — $(5, \pi/2)$, $(5, 5\pi/2)$, $(-5, -\pi/2)$ — land on the same point in the plane, illustrating the many-names-one-point feature of polar coordinates.

---

## Why polar coordinates are worth learning

Beyond being a second way to name points, polar coordinates are the natural home for quantities that rotate. A graph of $r$ as a function of $\theta$ produces curves — circles, cardioids, roses, spirals — that take gruesome equations in rectangular form but collapse to a single line in polar form. A circle centered at the origin with radius $5$ is simply $r = 5$, compared with $x^2 + y^2 = 25$ in rectangular form. A spiral that turns tighter as it grows is $r = \theta$. These simple polar equations unlock a different class of curves altogether, which you will graph in [[Polar_Graphs|polar graphs]] and use again in [[Polar_Form_Of_Complex_Numbers|polar form of complex numbers]].

---

## Common pitfalls

- **Forgetting the quadrant correction.** Running $\tan^{-1}(y/x)$ on a calculator never returns an angle in Quadrant II or Quadrant III. Always sketch the point before committing to an angle.
- **Writing the answer in the wrong order.** Polar pairs are $(r, \theta)$: radius first, angle second. Swapping them produces a different point entirely.
- **Mixing degrees and radians mid-problem.** The standard sine and cosine values in radians — like $\cos(\pi/3) = 1/2$ — are not the same symbols as the degree values $\cos(60°) = 1/2$. Pick one unit and stay with it throughout.
- **Assuming polar coordinates are unique.** Because angles are periodic, there are infinitely many pairs $(r, \theta)$ that name the same point. A problem that asks for "the" polar form is really asking for a particular standard representative, usually $r > 0$ and $0 \le \theta < 2\pi$.

---

## Prerequisites

- [[The_Pythagorean_Theorem]] — the formula $r = \sqrt{x^2 + y^2}$ is a Pythagorean reading of the right triangle whose legs are the rectangular coordinates.
- [[The_Unit_Circle]] — the conversion formulas are built on $\cos\theta$ and $\sin\theta$, so you must be fluent with the standard-angle values.
- [[Circular_Functions]] — for working with sine, cosine, and inverse tangent at angles beyond the first quadrant.

---

## Problems Involving Introduction To Polar Coordinates

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="introduction_to_polar_coordinates"></div>

---

## See Also

- [[Polar_Form_Of_Complex_Numbers]] — the same $(r, \theta)$ picture applied to complex numbers rather than points
- [[Polar_Graphs]] — curves given by $r$ as a function of $\theta$
- [[Vectors]] — another application of magnitude-and-angle descriptions
- [[The_Unit_Circle]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
