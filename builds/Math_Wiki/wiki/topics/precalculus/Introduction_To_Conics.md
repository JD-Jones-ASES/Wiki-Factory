---
title: "Introduction to Conic Sections"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-conic-sections", "#topic-analytic-geometry", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Parabolas"
  - "topics/algebra/Ellipses"
  - "topics/algebra/Hyperbolas"
  - "topics/algebra/The_Distance_Formula"
  - "topics/precalculus/Graphs_Of_Equations"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/The_Distance_Formula"
  - "topics/algebra/Graphs_Of_Equations"
  - "topics/algebra/Quadratic_Functions"
problem_type_ids: []
figures: []
summary: "Four curves, one source: slicing a double cone with a plane produces circles, ellipses, parabolas, and hyperbolas, and each one has a signature equation you can learn to recognize on sight."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Introduction to Conic Sections

# Introduction to Conic Sections

Take two cones, place them point-to-point so they form an hourglass shape, and slice that hourglass with a flat plane. The outline the plane carves on the cone's surface is called a **conic section**, or just a **conic**. The ancient Greek mathematician Apollonius wrote an eight-volume treatise classifying every curve you can get this way, and the answer is surprisingly clean: depending on the angle of the slicing plane, you get one of exactly four shapes.

- A **circle** — the plane cuts horizontally through one of the cones, perpendicular to its axis.
- An **ellipse** — the plane tilts a little but still cuts through only one cone.
- A **parabola** — the plane tilts far enough that it runs parallel to the slanted side of the cone.
- A **hyperbola** — the plane tilts past that parallel point and ends up cutting through both cones at once, producing two disconnected branches.

These four curves show up again and again in physics, engineering, and design. The orbit of a planet around the sun is an ellipse. The trajectory of a thrown object (ignoring air resistance) is a parabola. The cross-section of a satellite dish is also a parabola, which is why it can focus incoming signals onto a single point. A whispering gallery's two sweet-spot seats sit at the two foci of an ellipse. The Greek geometric construction is the same in every case, but the families of equations you use to describe them look different enough that precalculus teaches each one separately.

This page is the map. It names the four conics, gives the signature equation each one produces in the coordinate plane, and links out to the focused pages that cover each curve in detail. Once you can recognize the equation type from a single glance, you know which toolkit to reach for.

---

## The defining property each conic has

The geometric "slice a cone" description is beautiful but awkward to compute with. The coordinate-plane versions rely on distance-based definitions instead:

- A **circle** is the set of points equidistant from a single center point $(h, k)$. The common distance is the radius $r$.
- An **ellipse** is the set of points for which the **sum** of distances to two fixed points (called the **foci**) is a fixed constant. Picture pinning two thumbtacks to a board, looping a string around them, and tracing with a pencil held taut — the curve you draw is an ellipse.
- A **parabola** is the set of points equidistant from a single point (the **focus**) and a single line (the **directrix**). Every point on the curve is the same distance from the focus as it is from the directrix.
- A **hyperbola** is the set of points for which the **difference** of distances to two fixed foci is a fixed constant (in absolute value). The two-sign resolution gives the curve its two separate branches.

In each case the underlying idea is a statement about distances. And distances in the plane come from the [[The_Distance_Formula|distance formula]], which means every conic equation ultimately reduces to an algebraic relation you can derive by applying the distance formula to the defining condition.

---

## The four signature equations

When you carry out the distance-based derivations and simplify, each conic reduces to an equation with a characteristic form. In the standard-form versions below, the center or vertex is at the origin; you shift them to other locations by replacing $x$ with $x - h$ and $y$ with $y - k$.

**Circle.** Radius $r$, center at origin:

$$
x^{2} + y^{2} = r^{2}
$$

Shifted to center $(h, k)$:

$$
(x - h)^{2} + (y - k)^{2} = r^{2}
$$

The defining feature is that $x^{2}$ and $y^{2}$ appear with the **same** coefficient and the **same** sign (both positive).

**Ellipse.** Semi-axes $a$ and $b$, center at origin:

$$
\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1
$$

The defining feature is that $x^{2}$ and $y^{2}$ both appear with positive coefficients, but the coefficients are **different**. When they happen to match, the ellipse becomes a circle, so a circle is just a special case of an ellipse. When $a > b$ the ellipse is wider than it is tall; when $b > a$ it is taller than it is wide.

**Parabola.** Vertex at origin, opening upward:

$$
y = \frac{1}{4p} x^{2} \qquad \text{or equivalently} \qquad x^{2} = 4py
$$

Here $p$ is the distance from the vertex to the focus, and the directrix is the horizontal line $y = -p$. A sideways parabola opening rightward has the analogous form $y^{2} = 4px$. The defining feature is that **one** of the two variables is squared and the other appears to the first power.

**Hyperbola.** Center at origin, opening left/right:

$$
\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1
$$

The defining feature is a **minus sign** between the two squared terms. An up/down-opening hyperbola has the form $\tfrac{y^{2}}{a^{2}} - \tfrac{x^{2}}{b^{2}} = 1$ — same equation with the roles of $x$ and $y$ swapped.

---

## A pattern for spotting the type

When you see a second-degree equation in $x$ and $y$ like $Ax^{2} + Cy^{2} + Dx + Ey + F = 0$, you can usually identify the conic type in a few seconds:

- If $x^{2}$ and $y^{2}$ are both present with the **same** coefficient, it is a **circle** (or a single point, or nothing at all, depending on the constants).
- If $x^{2}$ and $y^{2}$ are both present with **different positive** coefficients, it is an **ellipse**.
- If $x^{2}$ and $y^{2}$ appear with **opposite** signs (one plus, one minus), it is a **hyperbola**.
- If only **one** of $x^{2}$ or $y^{2}$ appears and the other variable shows up only to the first power, it is a **parabola**.

From there, completing the square on $x$ and on $y$ transforms the equation into the standard form above, which directly reveals center, vertices, foci, and the other geometric landmarks.

---

## Example 1: Classifying $(x - 2)^{2} + (y + 1)^{2} = 9$

> Identify the conic described by $(x - 2)^{2} + (y + 1)^{2} = 9$. Find its center and radius.

The equation has $(x - \ldots)^{2}$ and $(y - \ldots)^{2}$ both added together, with the same coefficient (both implicitly $1$), and the right side is a positive number. That pattern is a **circle**.

Comparing with $(x - h)^{2} + (y - k)^{2} = r^{2}$, read off $h = 2$, $k = -1$ (remember: the sign inside the parentheses flips when you pull out the center), and $r^{2} = 9$, so $r = 3$. The circle has center $(2, -1)$ and radius $3$, living in the coordinate plane as a ring three units out from the center in every direction.

---

## Example 2: Classifying $4x^{2} + 9y^{2} = 36$

> Identify the conic described by $4x^{2} + 9y^{2} = 36$. Put it into standard form.

Both $x^{2}$ and $y^{2}$ are present with positive coefficients, but the coefficients are different ($4$ and $9$). That rules out a circle and points at an **ellipse**.

To get standard form, divide every term by $36$ so that the right side becomes $1$:

$$
\frac{4x^{2}}{36} + \frac{9y^{2}}{36} = 1 \quad\Longrightarrow\quad \frac{x^{2}}{9} + \frac{y^{2}}{4} = 1.
$$

Now it matches $\tfrac{x^{2}}{a^{2}} + \tfrac{y^{2}}{b^{2}} = 1$ with $a^{2} = 9$ and $b^{2} = 4$, so $a = 3$ and $b = 2$. The ellipse is centered at the origin, reaches $3$ units out along the $x$-axis (its major axis), and $2$ units out along the $y$-axis (its minor axis). Because the bigger semi-axis is horizontal, the ellipse is wider than it is tall.

---

## Example 3: Classifying $y = x^{2} - 4$

> Identify the conic described by $y = x^{2} - 4$. Find its vertex and the direction it opens.

Only one of the two variables appears squared. The variable $x$ is squared while $y$ appears to the first power. That pattern is a **parabola** — specifically, a parabola that opens along the $y$-direction (up or down).

To read off the vertex, rewrite the equation as $y - (-4) = (x - 0)^{2}$. This matches the form $y - k = (x - h)^{2}$ with vertex $(h, k) = (0, -4)$. The coefficient on $(x - 0)^{2}$ is $+1$, which is positive, so the parabola opens **upward**. Its vertex sits at $(0, -4)$, which is the low point of the curve, and the two branches rise symmetrically from there.

This is the same parabola you see in early algebra when graphing $y = x^{2}$ and shifting it down $4$ units. The conic-sections framework just relabels it as one of the four basic curve types and connects it to the focus/directrix definition: the focus sits $1/4$ unit above the vertex at $(0, -3.75)$, and the directrix is the horizontal line $y = -4.25$. Every point on the parabola is the same distance from the focus as from that line.

---

## Common pitfalls

- **Reading the sign wrong inside the parentheses.** In $(x - h)^{2}$, the vertex-$x$ is $+h$, not $-h$. If you see $(x + 2)^{2}$, the center is at $x = -2$, not $x = 2$. The minus sign is built into the standard form.
- **Mixing up $a^{2}$ and $a$.** The denominators in the ellipse and hyperbola equations are the **squares** of the semi-axes. If you read $\tfrac{x^{2}}{9}$ and record the semi-axis as $9$ instead of $\sqrt{9} = 3$, every subsequent distance will be wildly wrong.
- **Treating a parabola as a quadratic function with no conic interpretation.** A parabola *is* a conic section — it arises from slicing a cone at a particular tilt — and it has a focus and directrix just like the other three conics. The function-graphing machinery of algebra 2 (vertex form, axis of symmetry, and so on) and the conic-section machinery are two views of the same curve.
- **Assuming a circle is not an ellipse.** A circle is the special case of an ellipse where the two foci merge into a single center point. Treating circles and ellipses as one unified family is often the cleaner theoretical framing, even if textbooks present them as two separate sections.
- **Confusing ellipse and hyperbola because of a similar-looking equation.** The single sign between the two squared terms is everything. A plus makes it an ellipse; a minus makes it a hyperbola. Circle the sign first, then classify.

---

## Prerequisites

- [[The_Distance_Formula]] — every conic's defining property is a statement about distances, so you must be fluent with $\sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}$
- [[Graphs_Of_Equations]] — the general relation-between-$x$-and-$y$ framework, which is how conics are usually written
- [[Quadratic_Functions]] — the parabola is also the basic quadratic, so the $y = ax^{2} + bx + c$ background carries over directly

---

## Problems Involving Introduction to Conic Sections

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="introduction_to_conics"></div>

---

## See Also

- [[Parabolas]] — the full treatment of the parabola, including focus, directrix, and reflective property
- [[Ellipses]] — the full treatment of the ellipse, including foci, axes, and eccentricity
- [[Hyperbolas]] — the full treatment of the hyperbola, including asymptotes and two-branch behavior
- [[The_Distance_Formula]] — the tool behind every conic derivation
- [[Graphs_Of_Equations]] — the setting in which conics are drawn
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
