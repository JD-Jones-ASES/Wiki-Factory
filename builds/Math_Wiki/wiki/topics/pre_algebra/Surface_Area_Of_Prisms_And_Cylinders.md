---
title: "Surface Area of Prisms and Cylinders"
type: topic
aliases: ["Prism Surface Area", "Cylinder Surface Area", "Net Method"]
tags: ["#branch-pre-algebra", "#topic-solid-geometry", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Volume_Of_Pyramids_And_Cones"
  - "topics/pre_algebra/Surface_Area_And_Volume_Of_Spheres"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Perimeter_And_Area_Of_Polygons"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Perimeter_And_Area_Of_Polygons"
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
problem_type_ids: []
figures: ["geometry/prism_cylinder_labeled.svg"]
summary: "Unfold the solid into a flat net, compute each piece, and add — that sum is the surface area."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Surface Area of Prisms and Cylinders

# Surface Area of Prisms and Cylinders

The easiest way to think about surface area is to imagine pulling a solid apart along its seams and flattening every face onto a table. The resulting flat pattern is called a **net**. Once the net is laid out, the total surface area is just the sum of the areas of the flat pieces — no three-dimensional thinking required. The only skill that actually matters is keeping track of which shapes appear, how many copies there are, and what their dimensions are.

![[prism_cylinder_labeled.svg|A rectangular prism and cylinder, each with their dimensions labeled]]

This "net approach" works for every prism and every cylinder. The hard step is visualizing the unfolded pattern; once you have the net, the arithmetic is ordinary area work.

---

## Rectangular prism: six rectangles in three matched pairs

Unfold a rectangular box and you get six flat rectangles. Crucially, those six rectangles come in three pairs of identical twins, one pair for each axis of the box. If the box has length $l$, width $w$, and height $h$:

- two top-and-bottom rectangles of area $lw$ each
- two front-and-back rectangles of area $lh$ each
- two left-and-right rectangles of area $wh$ each

Add everything up:

$$
SA = 2lw + 2lh + 2wh
$$

Factoring out the $2$ gives the more compact form

$$
SA = 2(lw + lh + wh).
$$

Either version gives the same answer. The factored form saves a multiplication but makes no other difference.

### What "prism" means here

If the base is not a rectangle — for example, a triangular prism — the rule still works, but the sides are no longer all rectangles. A triangular prism has two triangular bases (the front and back, each with area equal to whatever formula the triangle calls for) plus three rectangular side panels whose widths equal the sides of the triangle. Add all five pieces together and you have the prism's surface area.

---

## Cylinder: two circles plus one rolled-up rectangle

A cylinder looks curved, but its net is remarkably clean: two identical circles for the top and bottom, and a single **rectangle** for the curved side. The rectangle is the tricky piece, so look at it carefully. If you slice a cylinder vertically and unroll the side, you get a flat rectangle whose dimensions are:

- **height** = the cylinder's height $h$
- **width** = the circumference of the base circle = $2\pi r$

That rectangle's area is $(2\pi r)(h) = 2\pi r h$. The two flat circles each contribute $\pi r^2$. Adding all three pieces:

$$
SA = 2\pi r^2 + 2\pi r h
$$

Or, factoring:

$$
SA = 2\pi r (r + h).
$$

Both forms are correct. Use whichever is easier for the numbers you have.

---

## Example 1: a 3D-printed rectangular enclosure

> A rectangular 3D-printed enclosure measures $12$ cm long, $8$ cm wide, and $5$ cm tall. Compute its surface area.

Apply the formula directly:

$$
SA = 2(lw + lh + wh) = 2(12 \cdot 8 + 12 \cdot 5 + 8 \cdot 5).
$$

Inside the parentheses: $12 \cdot 8 = 96$, $12 \cdot 5 = 60$, and $8 \cdot 5 = 40$. Add: $96 + 60 + 40 = 196$. Now double:

$$
SA = 2 \cdot 196 = 392 \text{ cm}^2.
$$

Surface area uses square units because every face is a flat region.

---

## Example 2: a cylindrical spool core

> A cylindrical spool for a custom machining part has a radius of $2$ in and a height of $7$ in. Compute its surface area in terms of $\pi$.

The two circular ends contribute

$$
2 \pi r^2 = 2\pi (2)^2 = 8\pi \text{ in}^2.
$$

The unrolled side is a rectangle with height $7$ in and width $2 \pi r = 2\pi (2) = 4\pi$ in, so its area is

$$
2 \pi r h = 2\pi (2)(7) = 28\pi \text{ in}^2.
$$

Add the pieces:

$$
SA = 8\pi + 28\pi = 36\pi \text{ in}^2.
$$

Leaving the answer in terms of $\pi$ is exact. Approximating gives about $113.1 \text{ in}^2$.

---

## Example 3: backing out a missing height

> A rectangular prism has length $10$ cm, width $4$ cm, and a surface area of $172 \text{ cm}^2$. Determine its height.

Start from the formula and substitute what you know, leaving $h$ as the unknown:

$$
172 = 2(lw + lh + wh) = 2(10 \cdot 4 + 10h + 4h).
$$

Simplify inside:

$$
172 = 2(40 + 14h) = 80 + 28h.
$$

Subtract $80$ from both sides and divide by $28$:

$$
92 = 28h \quad\Longrightarrow\quad h = \frac{92}{28} = \frac{23}{7} \approx 3.29 \text{ cm}.
$$

Backward problems always reduce to a linear equation once you plug everything in. Expand the expression in full, then isolate the unknown the same way you would in [[Multi_Step_Equations]].

---

## Common pitfalls

- **Counting only four rectangles on a box.** A rectangular prism has **six** faces. Students sometimes forget the top and bottom because those are "not on the sides." Every box has three pairs.
- **Using circumference instead of area for the top of a cylinder.** The top of a cylinder is a flat disk with area $\pi r^2$, not a ring with length $2\pi r$. The circumference enters only as the **width** of the unrolled side.
- **Forgetting to multiply by $2$.** Every term in the box formula has a $2$ in front because every face has a twin. Leaving off one $2$ is an easy way to produce an answer that is exactly half of the correct one.
- **Using the wrong unit.** Surface area is in square units, not cubic. If your answer has a $^3$, you computed volume by mistake.

---

## Prerequisites

- [[Circumference_And_Area_Of_Circles]] — both the circle area and the circle circumference appear in the cylinder formula
- [[Perimeter_And_Area_Of_Polygons]] — needed for prism bases that are not rectangles
- [[Volume_Of_Prisms_And_Cylinders]] — the same shapes seen from a different angle

---

## Problems Involving Surface Area of Prisms and Cylinders

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your picks stay in this browser so you can build a set before opening the [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="surface_area_of_prisms_and_cylinders"></div>

---

## See Also

- [[Volume_Of_Prisms_And_Cylinders]] — what fills the inside, rather than covers the outside
- [[Volume_Of_Pyramids_And_Cones]] — tapered cousins
- [[Surface_Area_And_Volume_Of_Spheres]] — the round case with its own formulas
- [[Circumference_And_Area_Of_Circles]] — ingredients of the cylinder net
- [[Perimeter_And_Area_Of_Polygons]] — ingredients of non-rectangular prism bases
- [[Composite_Figures]] — mixing several prisms or cylinders
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
