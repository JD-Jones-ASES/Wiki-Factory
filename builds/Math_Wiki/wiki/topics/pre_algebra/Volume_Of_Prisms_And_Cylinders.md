---
title: "Volume of Prisms and Cylinders"
type: topic
aliases: ["Prism Volume", "Cylinder Volume"]
tags: ["#branch-pre-algebra", "#topic-solid-geometry", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Volume_Of_Pyramids_And_Cones"
  - "topics/pre_algebra/Surface_Area_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Surface_Area_And_Volume_Of_Spheres"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Composite_Figures"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Perimeter_And_Area_Of_Polygons"
  - "topics/pre_algebra/Evaluating_Expressions"
problem_type_ids: []
figures: ["geometry/prism_cylinder_labeled.svg"]
summary: "Stack copies of a flat base to get volume: multiply the base area by the height."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Volume of Prisms and Cylinders

# Volume of Prisms and Cylinders

Imagine taking a flat shape and stacking exact copies of it on top of itself until the pile reaches a certain height. That is what a **prism** and a **cylinder** are: one two-dimensional footprint, repeated vertically without any tapering or twisting. Because every horizontal slice of the solid looks identical to the base, the amount of space inside is just "how big the base is" multiplied by "how tall the stack is." That single observation powers every volume problem on this page.

![[prism_cylinder_labeled.svg|A rectangular prism and a cylinder with base and height labeled]]

A **prism** has two parallel congruent polygon faces (the bases) connected by flat rectangular sides. If you slice a prism parallel to its bases, every cross-section is the same polygon. A **cylinder** works the same way but the base is a circle, so you can think of a cylinder as a prism whose base has infinitely many sides.

---

## The master formula

For both shapes, volume comes from one rule:

$$
V = B h
$$

Here $B$ is the **area of the base** and $h$ is the **height** of the solid measured perpendicular to that base. The units on volume are always cubic, such as $\text{cm}^3$ or $\text{in}^3$, because area (square units) gets multiplied by length (linear units).

The variable $B$ is a placeholder, not a fixed formula. You compute $B$ the usual way for whatever polygon sits at the bottom. For a rectangular base, $B = lw$. For a triangular base, $B = \tfrac{1}{2} b h_{\triangle}$. Be careful with two different heights in the same problem: the triangle has its own internal height, separate from the prism's overall height.

For a circular base, the area formula is $B = \pi r^2$ (from [[Circumference_And_Area_Of_Circles]]). Substituting into $V = Bh$ gives the cylinder formula directly:

$$
V = \pi r^2 h
$$

So there is really only one volume idea here, not two. A cylinder is a prism whose base happens to be a circle.

---

## Why it works

Picture a rectangular prism that is $3$ cm long, $2$ cm wide, and $4$ cm tall. Fill it with unit cubes, each $1$ cm on a side. One layer at the bottom holds $3 \times 2 = 6$ cubes. Stack four identical layers and you have used $6 \times 4 = 24$ cubes total. That number is exactly $B \cdot h$, where $B = 6$ is the number of cubes per layer and $h = 4$ is how many layers tall you stacked. The same reasoning works for any base shape: count how much one layer holds, then multiply by the number of layers.

---

## Example 1: a cafeteria tray container

> A rectangular storage bin for cafeteria trays has a length of $48$ cm, a width of $30$ cm, and a height of $15$ cm. Determine its volume.

The base is a rectangle with area

$$
B = lw = 48 \cdot 30 = 1440 \text{ cm}^2.
$$

Multiply by the height:

$$
V = Bh = 1440 \cdot 15 = 21{,}600 \text{ cm}^3.
$$

Nothing fancy — just area of the base times height.

---

## Example 2: a cylindrical 3D-printer filament spool

> A plastic cylinder used as a filament spool core has a radius of $4$ cm and a height of $9$ cm. Compute its volume, leaving your answer in terms of $\pi$.

The base is a circle, so

$$
B = \pi r^2 = \pi (4)^2 = 16\pi \text{ cm}^2.
$$

Multiply by the height:

$$
V = Bh = 16\pi \cdot 9 = 144\pi \text{ cm}^3.
$$

Leaving $\pi$ in the answer keeps it exact. If you need a decimal, multiply by about $3.14159$ at the very end — never partway through.

---

## Example 3: working backward to a missing height

> A triangular prism has a base that is a right triangle with legs of length $6$ in and $8$ in. The prism holds a volume of $192 \text{ in}^3$. What is its height?

The base is a right triangle, so

$$
B = \tfrac{1}{2} (6)(8) = 24 \text{ in}^2.
$$

Plug into $V = Bh$ and solve for the unknown:

$$
192 = 24 \cdot h
$$

$$
h = \frac{192}{24} = 8 \text{ in}.
$$

Whenever a problem gives you the volume and asks for a missing dimension, rewrite $V = Bh$ as a simple equation and isolate the variable you want. You never need a new formula — you only need to rearrange this one.

---

## Common pitfalls

- **Confusing the triangle's height with the prism's height.** A triangular prism has two different "heights": one is inside the base triangle (used to compute $B$), the other is how tall the whole solid is. Label them with different letters if it helps.
- **Using diameter instead of radius in the cylinder formula.** $V = \pi r^2 h$ expects the radius. If the problem gives you a diameter of $10$, the radius is $5$ and $r^2 = 25$, not $100$.
- **Mixing units.** If the base area comes out in square inches and the height is given in feet, convert first. Volume cannot be trusted when the inputs disagree on units.
- **Forgetting to cube the unit.** The answer is in cubic units, not square units. Writing $\text{cm}^2$ on a volume answer is a giveaway that something got lost.

---

## Prerequisites

- [[Circumference_And_Area_Of_Circles]] — needed to compute $B$ for cylinders
- [[Perimeter_And_Area_Of_Polygons]] — needed to compute $B$ for non-circular prism bases
- [[Evaluating_Expressions]] — for substituting numbers into $V = Bh$ carefully

---

## Problems Involving Volume of Prisms and Cylinders

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your picks are remembered in this browser until you open the [[Vault]] to view hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="volume_of_prisms_and_cylinders"></div>

---

## See Also

- [[Volume_Of_Pyramids_And_Cones]] — the tapered cousins, each one-third of the corresponding prism or cylinder
- [[Surface_Area_Of_Prisms_And_Cylinders]] — the outer skin of the same shapes
- [[Surface_Area_And_Volume_Of_Spheres]] — the round solid with its own formula family
- [[Circumference_And_Area_Of_Circles]] — where $\pi r^2$ comes from
- [[Composite_Figures]] — combining these solids for more complex problems
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
