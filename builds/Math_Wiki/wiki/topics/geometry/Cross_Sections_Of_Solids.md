---
title: "Cross Sections of Solids"
type: topic
aliases: ["Cross Section", "Slicing Solids", "Plane Sections"]
tags: ["#branch-geometry", "#topic-solid-geometry", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Volume_Of_Pyramids_And_Cones"
  - "topics/pre_algebra/Surface_Area_And_Volume_Of_Spheres"
  - "topics/algebra/Ellipses"
  - "topics/algebra/Hyperbolas"
  - "topics/algebra/Parabolas"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
problem_type_ids: []
figures: ["geometry/cube_cross_sections.svg"]
summary: "Slice a solid with a plane and catch the flat region that appears in the cut — its shape depends on the angle."
---

> [[_overview|Home]] > [[Geometry|Geometry]] > Cross Sections of Solids

# Cross Sections of Solids

If you slice a loaf of bread with a clean, flat cut and look at the exposed surface, what you see is a flat region — a two-dimensional shape sitting inside the original three-dimensional object. That flat region is called a **cross section** of the solid. The same idea applies to any three-dimensional object: imagine a perfectly flat plane passing through it, and the cross section is the shape of the intersection. Remarkably, a single solid can produce many different cross-section shapes depending on how the slicing plane is oriented. A cube can reveal squares, rectangles, triangles, and even hexagons. A cone can produce circles, ellipses, parabolas, and hyperbolas. A cylinder can give circles, ellipses, or rectangles. Each shape corresponds to a specific kind of cut.

![[cube_cross_sections.svg|A cube showing square, rectangular, triangular, and hexagonal cross sections]]

This page surveys the most important families of cross sections: cubes, cylinders, and cones.

---

## Cube cross sections

A cube has six square faces and all right angles. At first you might guess the cross sections are always squares, but that is only what you get when the slicing plane is parallel to a face. Tilt the plane and new shapes appear.

- **Square** — slice parallel to any face. You get a copy of that face (or a smaller square if you slice close to a corner in a certain way).
- **Rectangle** — slice vertically through the cube parallel to two opposite edges but not parallel to any face. The cross section is a rectangle whose width is the cube's edge length and whose height depends on where the cut enters and exits.
- **Triangle** — slice through three faces meeting at a corner, cutting off that corner. The resulting cross section is a triangle, and if the cut is symmetric, it can even be equilateral.
- **Hexagon** — slice midway through the cube with a plane tilted so it hits all six faces. A symmetric cut of this kind produces a regular hexagon. This is the most surprising cross section — nothing about a cube looks six-sided until you find the right angle.

Other shapes are possible too. A tilted cut that misses some faces can produce a pentagon. Quadrilaterals other than rectangles and squares show up for off-center cuts. The rule of thumb: a plane cutting a convex solid with $f$ faces can produce cross-section polygons with at most $f$ sides, so a cube tops out at a hexagon.

---

## Cylinder cross sections

A cylinder has two circular bases and a curved side. Its cross sections come in exactly three flavors.

- **Circle** — slice perpendicular to the cylinder's axis (parallel to the bases). The cross section is a copy of the base circle, regardless of how high up the cut is.
- **Ellipse** — slice with a plane that is tilted but still passes through both sides of the curved surface without hitting the top or bottom base. The result is an ellipse, stretched in the direction of the tilt. The more you tilt, the more elongated the ellipse becomes.
- **Rectangle** — slice parallel to the cylinder's axis. You get a rectangle whose width is a chord across the circular base and whose height is the full height of the cylinder. When the slice goes through the center, the width equals the diameter, giving the largest possible rectangle.

An interesting limit case: a cut that just grazes the curved surface along a single line produces a degenerate "cross section" consisting only of that line. Most problems ignore this edge case and focus on the three main shapes.

---

## Cone cross sections: the four conic sections

This is the famous list. A **right circular cone** — the kind with a circular base and an apex directly above the center — gives rise to the four curves collectively known as the **conic sections**, all by slicing with a plane at different angles.

- **Circle** — slice perpendicular to the axis of the cone. You get a circle whose radius shrinks as you approach the apex.
- **Ellipse** — tilt the slicing plane slightly from horizontal. The cut still goes all the way through the cone's side, but the cross section is now an elongated oval — an ellipse.
- **Parabola** — tilt the plane until it becomes **parallel to one of the slanted side lines** of the cone. The cross section no longer closes up, because the slicing plane never catches the other side of the cone. The result is an open curve called a parabola.
- **Hyperbola** — tilt the plane further, so it is steep enough to slice through **both halves** of a double cone (the cone plus its mirror image reflected through the apex). Each half contributes one branch, and the result is a hyperbola with two separated pieces.

For more on each of these curves as algebraic objects, see [[Parabolas]], [[Ellipses]], and [[Hyperbolas]]. The key insight is that all four curves come from the same cone — only the angle of the slice changes.

---

## Example 1: a cube sliced to reveal a hexagon

> A cube has edges of length $6$ cm. A slicing plane passes through the midpoints of six edges in a symmetric pattern, producing a regular hexagonal cross section. What is the side length of the hexagon?

The hexagonal cross section of a cube connects six edge midpoints. Each side of the hexagon is the distance between two such midpoints on adjacent faces of the cube. For a cube with edge $s$, a careful calculation (using the distance formula in three dimensions) shows that each hexagon side has length

$$
\frac{s\sqrt{2}}{2}.
$$

Plugging in $s = 6$:

$$
\frac{6\sqrt{2}}{2} = 3\sqrt{2} \text{ cm} \approx 4.24 \text{ cm}.
$$

So the hexagon has six sides, each about $4.24$ cm long.

---

## Example 2: a cone sliced to reveal a parabola

> A right circular cone has a slant side that makes a $60^\circ$ angle with the vertical axis. A slicing plane passes through the cone parallel to one of those slant sides. Classify the resulting cross section.

The key fact is that a plane parallel to a slant side of a cone produces a **parabola** as its cross section. The specific angle of the slant side does not change which curve appears — as long as the plane is parallel to a generator line of the cone, you always get a parabola. Any steeper angle (so that the plane hits both halves of the double cone) would give a hyperbola instead, and any shallower angle would give an ellipse.

So the answer is: the cross section is a parabola. This happens to be the same curve you already know from algebra as the graph of a quadratic function $y = ax^2 + bx + c$. The link between "slice of a cone" and "graph of a quadratic" is one of the most famous connections in mathematics.

---

## Example 3: a cylinder sliced at an angle

> A right circular cylinder has radius $2$ in and height $10$ in. A slicing plane cuts the cylinder at a $45^\circ$ angle from the base, entering on one side of the curved surface and exiting on the other without touching the top or bottom circles. Classify the cross section.

Since the slicing plane is tilted but still cuts all the way across the curved side of the cylinder, the cross section must be an **ellipse**. (A perpendicular cut would give a circle, and a parallel-to-axis cut would give a rectangle. Neither applies here.) 

The ellipse's minor axis equals the diameter of the cylinder, because the cut is at its narrowest along the diameter of the base. That gives a minor axis of $2 r = 4$ in, so the minor **semi**-axis length is $b = 2$ in. The major axis is longer because the slicing plane is tilted, stretching the circle in the direction of the tilt. For a $45^\circ$ tilt, the major axis is $\sqrt{2}$ times the minor axis, giving $a = 2\sqrt{2}$ in.

So the cross section is an ellipse with semi-axes $a = 2\sqrt{2}$ in and $b = 2$ in.

---

## Common pitfalls

- **Assuming every cube cross section is a square.** Most cube cross sections are not squares. Even symmetric cuts can produce triangles, rectangles, pentagons, or hexagons depending on the tilt.
- **Forgetting that a parabola needs a plane parallel to a slant line.** A slice that is "just a little tilted" gives an ellipse, not a parabola. The parabola appears only at the exact critical angle where the plane is parallel to one side of the cone.
- **Treating a hyperbola as one curve.** A hyperbola has **two** branches. If the slicing plane only crosses one half of the cone, you get a single open curve (part of a hyperbola) but the full hyperbola requires a double cone — the original plus its reflection through the apex.
- **Confusing cross section with surface area.** A cross section is a flat two-dimensional region **inside** the solid, not on its outer skin. Surface area is about the outside; cross sections are about the inside.

---

## Prerequisites

- [[Volume_Of_Prisms_And_Cylinders]] — the cube and cylinder shapes you are slicing
- [[Classifying_Triangles_And_Quadrilaterals]] — needed to name the polygon cross sections
- [[Circumference_And_Area_Of_Circles]] — the circle cross section of a cylinder

---

## Problems Involving Cross Sections

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections are saved in this browser. Open your [[Vault]] later for hints, answers, or a printable worksheet.

<div class="problem-vault-widget" data-topic-slug="cross_sections_of_solids"></div>

---

## See Also

- [[Parabolas]] — one of the four conic sections
- [[Ellipses]] — another conic section
- [[Hyperbolas]] — the two-branch conic section
- [[Volume_Of_Prisms_And_Cylinders]] — solids whose cross sections you learn to classify
- [[Volume_Of_Pyramids_And_Cones]] — the tapered solids whose slices are the conics
- [[Surface_Area_And_Volume_Of_Spheres]] — whose cross sections are always circles
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
