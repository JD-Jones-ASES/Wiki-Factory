---
title: "Parabolas"
type: topic
aliases: ["Parabola (Conic)", "Conic Parabola", "Parabola Focus Directrix"]
tags: ["#branch-algebra-2", "#topic-conic-sections", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "9", section: "9.2"}
  - {book: "algtrig", chapter: "10", section: "10.5"}
related:
  - "topics/geometry/Circles"
  - "topics/algebra/Ellipses"
  - "topics/algebra/Hyperbolas"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Completing_The_Square"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Completing_The_Square"
  - "topics/geometry/Circles"
problem_type_ids: []
figures: ["algebra/conic_sections_gallery.svg"]
summary: "The conic view of a parabola: every point on the curve is the same distance from a fixed focus and a fixed directrix."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Parabolas

# Parabolas

You have already met parabolas once, back in [[Quadratic_Functions|quadratic functions]], where $y = ax^2 + bx + c$ produced a graceful U-shape that opened either up or down. That was the **function** view of a parabola. This page takes the **conic** view instead: a parabola is a shape defined not by a formula but by a simple distance rule involving one point and one line.

Pin a point $F$ (called the **focus**) to the plane. Draw a line $D$ (called the **directrix**) somewhere that does not pass through $F$. Now imagine collecting every point whose distance to $F$ is exactly the same as its perpendicular distance to $D$. The curve those points trace out is a parabola. The **vertex** is the one point of the parabola that sits halfway between the focus and the directrix, and the **axis of symmetry** is the line through both the vertex and the focus — the parabola is a mirror image of itself across that line.

The conic definition gives the shape a physical meaning that $y = ax^2 + bx + c$ hides. That meaning is where the reflective property comes from, and the reflective property is why the world is full of parabolas.

![[conic_sections_gallery.svg|The four conic sections]]

---

## Standard form for the conic view

Instead of writing $y = ax^2 + bx + c$, conic geometry prefers a form that makes the focus distance visible. Let $p$ be the signed distance from the vertex to the focus (and also from the vertex to the directrix, in the opposite direction). A parabola with vertex $(h, k)$ and a vertical axis of symmetry has the equation

$$
(x - h)^2 = 4p(y - k).
$$

Reading off the geometry:

- **Vertex:** $(h, k)$.
- **Focus:** $(h,\; k + p)$.
- **Directrix:** the horizontal line $y = k - p$.
- **Direction of opening:** up if $p > 0$; down if $p < 0$.

Swap the roles of $x$ and $y$ and you get a parabola with a **horizontal** axis of symmetry, vertex $(h, k)$, and equation

$$
(y - k)^2 = 4p(x - h).
$$

For this one the focus is at $(h + p,\; k)$, the directrix is the vertical line $x = h - p$, and the parabola opens right when $p > 0$, left when $p < 0$. A horizontal parabola is **not** a function of $x$ — its graph fails the vertical line test because any $x$ past the vertex gives two $y$ values, one on each branch.

### Connecting to vertex form

The vertex form $y = a(x - h)^2 + k$ that you learned in Cluster 3 is the same shape, just rearranged. Move the constant over and divide, and you get

$$
(x - h)^2 = \dfrac{1}{a}(y - k),
$$

so the conic's $4p$ matches the function's $\dfrac{1}{a}$. That is, $p = \dfrac{1}{4a}$. The vertex $(h, k)$ is identical in both pictures. If you already know how to sketch a quadratic from vertex form, you can find the focus and directrix of any parabola by computing $\dfrac{1}{4a}$ and stepping that distance up or down from the vertex.

---

## Key ideas

- The parabola is controlled by **one point and one line**, not by two foci like the ellipse and hyperbola. That is what makes it the simplest conic.
- The value $|p|$ is the distance from vertex to focus and from vertex to directrix. Small $|p|$ makes a narrow, pinched parabola; large $|p|$ opens the curve out wide.
- The **reflective property**: any ray coming in parallel to the axis of symmetry bounces off the parabola and passes through the focus. That is why satellite dishes, flashlight reflectors, and telescope mirrors are shaped this way — they collect or emit parallel beams through one focal point.
- To sketch quickly: plot the vertex, mark the focus $|p|$ units inside the curve, draw the directrix $|p|$ units outside on the other side, then bend a smooth curve through the vertex opening away from the directrix.

---

## Example 1: reading focus and directrix from vertex form

> Determine the vertex, focus, and directrix of the parabola $y = \dfrac{1}{8}(x - 3)^2 - 2$.

Match against $y = a(x - h)^2 + k$: the coefficient is $a = \dfrac{1}{8}$, the vertex is $(h, k) = (3, -2)$, and the parabola opens upward because $a > 0$. Convert $a$ to the conic $p$ using $p = \dfrac{1}{4a}$:

$$
p = \dfrac{1}{4 \cdot \frac{1}{8}} = \dfrac{1}{\frac{1}{2}} = 2.
$$

So the focus sits $2$ units above the vertex, and the directrix sits $2$ units below.

- **Vertex:** $(3, -2)$.
- **Focus:** $(3,\; -2 + 2) = (3, 0)$.
- **Directrix:** $y = -2 - 2 = -4$.

Every point on the curve is the same distance from $(3, 0)$ as from the horizontal line $y = -4$. That is the whole definition, turned into numbers.

---

## Example 2: building the equation from a focus and a directrix

> Write an equation for the parabola whose focus is $(0, 1)$ and whose directrix is the line $y = -5$.

The vertex lies halfway between the focus and the directrix, on the axis of symmetry (which is vertical here, because the directrix is horizontal). The midpoint of $(0, 1)$ and the point $(0, -5)$ directly below the focus is

$$
\left(0,\; \dfrac{1 + (-5)}{2}\right) = (0, -2),
$$

so the vertex is $(0, -2)$. The focus sits $1 - (-2) = 3$ units above the vertex, so $p = 3$ (positive, so the parabola opens upward). Plug $h = 0$, $k = -2$, $p = 3$ into the conic form:

$$
(x - 0)^2 = 4(3)(y - (-2)),
$$

which simplifies to

$$
x^2 = 12(y + 2).
$$

Check: the directrix should be at $y = k - p = -2 - 3 = -5$. That matches the given line, so the work is consistent.

---

## Example 3: completing the square to locate the focus

> Rewrite $x = y^2 - 4y + 7$ in the standard horizontal form, then give the vertex, focus, and directrix.

The squared variable is $y$, so this is a **horizontal** parabola. Group the $y$-terms and complete the square:

$$
x = (y^2 - 4y) + 7.
$$

Half of $-4$ is $-2$, and $(-2)^2 = 4$. Add and subtract $4$ inside the $y$-expression:

$$
x = (y^2 - 4y + 4) + 7 - 4 = (y - 2)^2 + 3.
$$

Rearrange into the conic shape $(y - k)^2 = 4p(x - h)$:

$$
(y - 2)^2 = x - 3 = 1 \cdot (x - 3),
$$

so $4p = 1$, which gives $p = \dfrac{1}{4}$. The vertex sits at $(3, 2)$ and, since $p$ is positive, the curve opens rightward.

- **Vertex:** $(3, 2)$.
- **Focus:** $(3 + \tfrac{1}{4},\; 2) = \left(\tfrac{13}{4},\, 2\right)$.
- **Directrix:** the vertical line $x = 3 - \tfrac{1}{4} = \tfrac{11}{4}$.

The parabola bends to the right around its vertex, and the focus sits a quarter-unit inside the curve.

---

## Common pitfalls

- **Mixing up the function view and the conic view.** The function vertex form $y = a(x - h)^2 + k$ and the conic form $(x - h)^2 = 4p(y - k)$ describe the same curve, but the coefficient out front plays different roles. Use $p = \dfrac{1}{4a}$ to translate between them.
- **Putting the focus on the wrong side of the vertex.** The focus always sits **inside** the curve — above the vertex if the parabola opens up, to the right of the vertex if it opens right. The directrix sits on the opposite side.
- **Forgetting that $x = (y - k)^2$ forms are not functions.** A horizontal parabola has two $y$-values for most $x$-values. You cannot treat it the same way as a vertical quadratic.
- **Sign errors on $p$.** A negative $p$ means the parabola opens down or to the left, and it also flips which side the directrix is on. Track the sign with the same care you would use in completing the square.

---

## Prerequisites

Before practicing problems on the conic form, be comfortable with:

- [[Quadratic_Functions]] — the function-view version of the same shape, and the language of vertex and axis of symmetry
- [[Completing_The_Square]] — the algebra for moving between general form and vertex form
- [[Circles]] — the first conic you studied, and a warm-up for the distance-based definitions

---

## Problems Involving Parabolas

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="parabolas"></div>

---

## See Also

- [[Quadratic_Functions]] — the function perspective on the same curve
- [[Ellipses]] — the next conic, built from two foci instead of one
- [[Hyperbolas]] — two foci with a difference-of-distances rule
- [[Circles]] — the simplest conic, the warm-up for this family
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
