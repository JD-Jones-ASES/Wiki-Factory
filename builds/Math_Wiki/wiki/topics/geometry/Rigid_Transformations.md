---
title: "Rigid Transformations"
type: topic
aliases: ["Isometries", "Translations Rotations Reflections"]
tags: ["#branch-geometry", "#topic-transformations", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Dilations_And_Similarity"
  - "topics/geometry/Coordinate_Geometry_Proofs"
  - "topics/geometry/Circles"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Points_Lines_Angles_And_Angle_Relationships"
problem_type_ids: []
figures: ["geometry/rigid_transformations.svg"]
summary: "Three moves that slide, spin, or flip a figure without changing any of its lengths or angles."
---
> [[_overview|Home]] > [[Geometry|Geometry]] > Rigid Transformations

# Rigid Transformations

Imagine picking up a paper triangle and sliding it across a table, rotating it in place, or flipping it over onto its back. Nothing about the triangle itself has changed — the side lengths are the same, the angles are the same, the shape is the same — but its position or orientation on the table is different. Moves of that kind are called **rigid transformations**, and there are exactly three of them: **translations** (sliding), **rotations** (spinning about a point), and **reflections** (flipping across a line). Every rigid transformation keeps distances and angles exactly as they were before the move.

![[rigid_transformations.svg|A triangle translated, rotated, and reflected]]

In this page we write each move as a coordinate rule that tells you where a point $(x, y)$ lands after the transformation. That gives you a way to transform any figure — just apply the rule to each of its vertices and connect them in the same order.

---

## Translations: sliding without turning

A **translation** slides every point of a figure by the same displacement. No turning, no flipping, no resizing. If you shift every point $a$ units right and $b$ units up, the coordinate rule is

$$
(x, y) \to (x + a, y + b).
$$

Negative values shift left or down. For example, $(x, y) \to (x - 3, y + 4)$ moves every point three units left and four units up. Apply the rule to each vertex of a polygon, connect the new vertices in the same order, and you have a perfect copy of the original in a new location. Nothing bends or stretches.

---

## Rotations about the origin

A **rotation** spins a figure about a fixed point called the **center**. The most common center in coordinate geometry is the origin $(0, 0)$, and the most common angles are the multiples of $90^\circ$. Going counterclockwise (CCW), the rules are:

- $90^\circ$ CCW about the origin: $(x, y) \to (-y, x)$
- $180^\circ$ about the origin: $(x, y) \to (-x, -y)$
- $270^\circ$ CCW (or $90^\circ$ clockwise) about the origin: $(x, y) \to (y, -x)$

A quick sanity check for the $90^\circ$ CCW rule: the point $(3, 0)$ is on the positive $x$-axis. After a quarter turn counterclockwise, it should land on the positive $y$-axis at $(0, 3)$. Plugging into $(x, y) \to (-y, x)$ gives $(-0, 3) = (0, 3)$. Good — the rule matches intuition.

A $180^\circ$ rotation about the origin is the same as reflecting across the $x$-axis and then across the $y$-axis (or vice versa). That duality comes in handy when you want to avoid the rotation rule altogether.

---

## Reflections across lines

A **reflection** flips a figure across a **line of reflection**. Every point in the figure moves straight across that line to a mirror-image position the same distance away on the other side. The coordinate rules for the most common reflection lines are:

- Reflection over the $x$-axis: $(x, y) \to (x, -y)$
- Reflection over the $y$-axis: $(x, y) \to (-x, y)$
- Reflection over the line $y = x$: $(x, y) \to (y, x)$
- Reflection over the line $y = -x$: $(x, y) \to (-y, -x)$

Each of these negates or swaps coordinates depending on which line you reflect across. Notice the pattern: reflecting across a horizontal axis (the $x$-axis) changes only the vertical coordinate, while reflecting across a vertical axis (the $y$-axis) changes only the horizontal coordinate. Reflection swaps points across a line, just as holding a figure up to a mirror swaps left and right without changing distances to the mirror.

---

## Why "rigid"?

The word **rigid** is doing real work. These three transformations are the complete list of moves that preserve both **distance** (two points that were $5$ units apart stay $5$ units apart) and **angle** (the corners of a shape keep the same measures). Any move with both properties is called an **isometry**, and rigid transformations are exactly the isometries of the plane.

Because distances and angles are preserved, the image after a rigid transformation is always **congruent** to the original: same size, same shape, possibly a different location or orientation. Dilations (covered in [[Dilations_And_Similarity]]) are **not** rigid — they preserve angles but stretch distances, so they produce similar figures rather than congruent ones.

---

## Example 1: translating a triangle

> Triangle $ABC$ has vertices $A(1, 2)$, $B(4, 3)$, and $C(2, 5)$. Apply the translation $(x, y) \to (x + 3, y - 4)$. What are the coordinates of the image triangle $A'B'C'$?

Apply the rule to each vertex.

- $A(1, 2) \to A'(1 + 3, 2 - 4) = A'(4, -2)$
- $B(4, 3) \to B'(4 + 3, 3 - 4) = B'(7, -1)$
- $C(2, 5) \to C'(2 + 3, 5 - 4) = C'(5, 1)$

The image triangle has vertices $A'(4, -2)$, $B'(7, -1)$, $C'(5, 1)$. A quick check: each pair of image side lengths should match the pre-image side lengths. For example, the original $AB$ has length $\sqrt{(4-1)^2 + (3-2)^2} = \sqrt{10}$, and $A'B'$ has length $\sqrt{(7-4)^2 + (-1-(-2))^2} = \sqrt{10}$. Same distance, as rigidity promises.

---

## Example 2: rotating a point $90^\circ$ counterclockwise

> Take the point $P(5, -2)$ and rotate it $90^\circ$ counterclockwise about the origin. What are the coordinates of the image $P'$?

Apply the rule $(x, y) \to (-y, x)$:

$$
P(5, -2) \to P'\bigl(-(-2), \ 5\bigr) = P'(2, 5).
$$

Quick visual check: $P$ was in Quadrant IV (positive $x$, negative $y$). A quarter turn counterclockwise should land it in Quadrant I (both coordinates positive), and $(2, 5)$ is in Quadrant I. Rotations never change how far a point is from the center, and $P$ and $P'$ both have distance $\sqrt{25 + 4} = \sqrt{29}$ from the origin.

---

## Example 3: reflecting a figure over the $y$-axis

> A rectangle has vertices $P(2, 1)$, $Q(6, 1)$, $R(6, 4)$, and $S(2, 4)$. Determine the coordinates of its reflection across the $y$-axis.

The rule is $(x, y) \to (-x, y)$. Apply it vertex by vertex:

- $P(2, 1) \to P'(-2, 1)$
- $Q(6, 1) \to Q'(-6, 1)$
- $R(6, 4) \to R'(-6, 4)$
- $S(2, 4) \to S'(-2, 4)$

The image rectangle has vertices $P'(-2, 1)$, $Q'(-6, 1)$, $R'(-6, 4)$, $S'(-2, 4)$. It has the same dimensions — $4$ units wide, $3$ units tall — just on the other side of the $y$-axis.

One subtle point: the vertices in the image are listed here in the same order $P', Q', R', S'$ as the original. But reading them as you go around the shape, the orientation has reversed (a reflection swaps clockwise and counterclockwise). This orientation flip is the fingerprint of a reflection and is what distinguishes it from a translation or rotation.

---

## Common pitfalls

- **Swapping the $90^\circ$ and $270^\circ$ rules.** $90^\circ$ CCW is $(x, y) \to (-y, x)$, and $270^\circ$ CCW is $(x, y) \to (y, -x)$. Mixing them up produces a figure rotated the wrong way. A quick sanity check on a single easy point (like $(1, 0)$) catches the error.
- **Forgetting the minus sign on $y$-axis reflections.** Reflection across the $y$-axis negates the $x$, not the $y$. Students often write $(x, y) \to (x, -y)$, which is actually reflection across the $x$-axis.
- **Confusing center of rotation.** All the rotation rules on this page are for rotation **about the origin**. If the problem asks you to rotate about a different point, you must first translate that point to the origin, rotate, then translate back.
- **Reading the transformation in the wrong direction.** If the problem gives you the image and asks for the preimage, you apply the **inverse** of the rule, not the original. For a translation, that means subtracting the displacement instead of adding it.

---

## Prerequisites

- [[Plotting_Points_And_The_Coordinate_Plane]] — you must be comfortable locating $(x, y)$ quickly
- [[The_Pythagorean_Theorem]] — used to verify that distances are preserved
- [[Points_Lines_Angles_And_Angle_Relationships]] — needed to talk about angles between lines

---

## Problems Involving Rigid Transformations

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your picks are saved in this browser. Open your [[Vault]] when you are ready for hints, answers, or a printable worksheet.

<div class="problem-vault-widget" data-topic-slug="rigid_transformations"></div>

---

## See Also

- [[Dilations_And_Similarity]] — the scaling transformation that is **not** rigid
- [[Coordinate_Geometry_Proofs]] — combines transformations with distance and slope arguments
- [[Transformations_I_Shifts_And_Reflections]] — the function-graph version of the same ideas
- [[Transformations_Ii_Stretches_Compressions_And_Combined]] — scaling and combined transformations
- [[Circles]] — rotation is how circles are defined
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
