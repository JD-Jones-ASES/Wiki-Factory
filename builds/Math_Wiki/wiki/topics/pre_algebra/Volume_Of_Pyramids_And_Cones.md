---
title: "Volume of Pyramids and Cones"
type: topic
aliases: ["Pyramid Volume", "Cone Volume"]
tags: ["#branch-pre-algebra", "#topic-solid-geometry", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Surface_Area_And_Volume_Of_Spheres"
  - "topics/pre_algebra/Surface_Area_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Composite_Figures"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Perimeter_And_Area_Of_Polygons"
problem_type_ids: []
figures: ["geometry/pyramid_cone_labeled.svg"]
summary: "Tapered solids hold exactly one-third of the prism or cylinder with the same base and height."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Volume of Pyramids and Cones

# Volume of Pyramids and Cones

A **pyramid** and a **cone** look almost like a prism and cylinder, except instead of running straight up, they taper to a single point called the **apex**. Because the upper slices shrink as you climb, a pyramid or cone holds a lot less material than the untapered solid would. The surprising part is exactly how much less: exactly one-third. A cone that shares its base circle and height with a cylinder carries one-third the cylinder's volume, no more and no less. The same ratio works for any pyramid paired with its corresponding prism.

![[pyramid_cone_labeled.svg|A square pyramid and a cone with base, height, and apex labeled]]

A pyramid has one polygonal base and triangular side faces that lean inward and meet at the apex. A cone has one circular base and a single curved side surface that sweeps up to its apex. In both cases, the **height** $h$ is measured straight up from the base to the apex, perpendicular to the base — not along a slanted edge.

---

## The one-third rule

For both solids, the volume formula is

$$
V = \tfrac{1}{3} B h
$$

where $B$ is the area of the base and $h$ is the perpendicular height. The letter $B$ means the same thing it did for prisms: compute the area of whichever polygon is sitting at the bottom.

For a cone, the base is a circle with area $\pi r^2$, so

$$
V = \tfrac{1}{3} \pi r^2 h.
$$

Compare these to the prism and cylinder formulas in [[Volume_Of_Prisms_And_Cylinders]]. The only difference is the factor of $\tfrac{1}{3}$ stuck out front.

---

## Why one-third?

The neatest way to see this is a physical experiment, and the cleanest way to picture it is with water. Take an empty cone and an empty cylinder that have the same circular base and the same height. Fill the cone with water, pour it into the cylinder, and watch. You will find that it takes exactly **three** cone-fulls to fill the cylinder to the top. That is not a coincidence of sizes — it works for any matched pair. The cylinder has three times the volume of the cone, or equivalently, the cone has one-third the volume of the cylinder.

The same thing happens with any matched prism-and-pyramid pair: three pyramid-fulls fill one prism. Calculus can prove this rigorously by adding up the shrinking horizontal slices from apex to base, but the water demo is enough to convince you that a single constant, $\tfrac{1}{3}$, does the bookkeeping for all tapered solids.

---

## Example 1: a square pyramid art installation

> A square-based pyramid for an art installation has a base with side length $12$ ft and a perpendicular height of $9$ ft. Determine its volume.

The base is a square, so

$$
B = s^2 = 12^2 = 144 \text{ ft}^2.
$$

Plug into the one-third rule:

$$
V = \tfrac{1}{3} B h = \tfrac{1}{3} (144)(9) = \tfrac{1}{3} (1296) = 432 \text{ ft}^3.
$$

A handy shortcut: if the numbers are friendly, multiply the base area by the height first, then divide by $3$ at the end.

---

## Example 2: a drone payload cone

> A drone carries a conical payload with a radius of $3$ cm and a height of $10$ cm. Compute its volume in terms of $\pi$.

The base is a circle, so $B = \pi r^2 = \pi (3)^2 = 9\pi \text{ cm}^2$. Using the cone formula,

$$
V = \tfrac{1}{3} \pi r^2 h = \tfrac{1}{3} (9\pi)(10) = \tfrac{90\pi}{3} = 30\pi \text{ cm}^3.
$$

Leaving the answer as $30\pi \text{ cm}^3$ keeps it exact. Converting to a decimal at the very end gives approximately $94.2 \text{ cm}^3$.

---

## Example 3: solving for a missing height

> A custom cake mold shaped like a square pyramid has a base with side length $8$ in and holds a volume of $128 \text{ in}^3$. What is the mold's perpendicular height?

Compute the base area first: $B = 8^2 = 64 \text{ in}^2$. Now plug the known pieces into the formula:

$$
128 = \tfrac{1}{3} (64) h.
$$

Multiply both sides by $3$ to clear the fraction:

$$
384 = 64 h.
$$

Divide by $64$:

$$
h = \frac{384}{64} = 6 \text{ in}.
$$

The order was: clear the fraction first (multiply by $3$), then peel away $B$ (divide). Missing-dimension problems are just linear equations in disguise.

---

## Common pitfalls

- **Forgetting the $\tfrac{1}{3}$ factor.** This is the single most common error on pyramid and cone problems. If your answer matches the corresponding prism or cylinder volume, you probably skipped the one-third.
- **Using slant height instead of perpendicular height.** The formula wants the straight-up height from the center of the base to the apex, not the tilted distance along a side edge. The slant is longer and will overestimate the volume.
- **Mixing up the triangle inside a pyramid face with the pyramid height.** The triangular faces of a pyramid have their own dimensions; those have nothing to do with the $h$ inside $V = \tfrac{1}{3} B h$. Keep them labeled separately.
- **Using diameter for $r$ in the cone formula.** As with cylinders, the formula needs the radius. Halve the diameter before squaring.

---

## Prerequisites

- [[Volume_Of_Prisms_And_Cylinders]] — the one-third rule always comes paired with the untapered version
- [[Circumference_And_Area_Of_Circles]] — for computing the base of a cone
- [[Perimeter_And_Area_Of_Polygons]] — for computing the base of a non-circular pyramid

---

## Problems Involving Volume of Pyramids and Cones

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your picks stay in this browser, and you can open your [[Vault]] later to view hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="volume_of_pyramids_and_cones"></div>

---

## See Also

- [[Volume_Of_Prisms_And_Cylinders]] — the three-to-one partner of every pyramid and cone
- [[Surface_Area_And_Volume_Of_Spheres]] — the round solid that completes the family
- [[Surface_Area_Of_Prisms_And_Cylinders]] — outer skin of the untapered shapes
- [[Circumference_And_Area_Of_Circles]] — the $\pi r^2$ formula used inside the cone volume
- [[Composite_Figures]] — mixing tapered and untapered parts
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
