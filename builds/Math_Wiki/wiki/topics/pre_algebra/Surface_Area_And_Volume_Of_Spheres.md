---
title: "Surface Area and Volume of Spheres"
type: topic
aliases: ["Sphere Volume", "Sphere Surface Area"]
tags: ["#branch-pre-algebra", "#topic-solid-geometry", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Volume_Of_Pyramids_And_Cones"
  - "topics/pre_algebra/Surface_Area_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Composite_Figures"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
  - "topics/pre_algebra/Exponents_And_Powers"
problem_type_ids: []
figures: ["geometry/sphere_labeled.svg"]
summary: "Two clean formulas for the perfectly round solid — one for the outer skin, one for the inside."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Surface Area and Volume of Spheres

# Surface Area and Volume of Spheres

Picture a perfectly round ball. Every single point on its outer skin is exactly the same distance from a hidden center, and that distance is what we call the **radius**. A sphere is the cleanest three-dimensional shape in the whole family — no corners, no edges, no flat faces, no preferred orientation. Because of that perfect symmetry, both its volume and its surface area depend on nothing more than the single number $r$.

![[sphere_labeled.svg|A sphere with its radius labeled]]

There are two formulas to memorize on this page and both are short.

---

## The two formulas

For a sphere of radius $r$:

$$
SA = 4 \pi r^2
$$

$$
V = \tfrac{4}{3} \pi r^3
$$

Surface area scales with $r^2$ (same as any area) and volume scales with $r^3$ (same as any volume). That is not a coincidence: doubling the radius quadruples the skin area and multiplies the inside by eight. Keep that scaling instinct handy — it catches a lot of arithmetic mistakes before they become wrong answers.

---

## Intuition

Why the specific numbers $4$ and $\tfrac{4}{3}$? Calculus provides a clean derivation, but you can build a decent picture without any of that machinery.

**Surface area.** Imagine wrapping a sphere with the area of a flat disk of the same radius. That disk has area $\pi r^2$. You would need exactly **four** such disks to cover the whole sphere. So the surface area is $4 \pi r^2$. This is not a folk story — it really does take exactly four great-circle disks' worth of area to wrap the sphere's outer surface.

**Volume.** The inside of a sphere of radius $r$ can be compared to a cylinder that exactly encloses it. Such a cylinder has radius $r$ and height $2r$, giving it a volume of $\pi r^2 (2r) = 2\pi r^3$. The sphere uses up two-thirds of the cylinder's space, which gives

$$
V_{\text{sphere}} = \tfrac{2}{3} (2\pi r^3) = \tfrac{4}{3}\pi r^3.
$$

Again, not a folk story — this is a real theorem (Archimedes figured it out over two thousand years ago). The two-thirds ratio was so important to him that his tomb was reportedly marked with a sphere inside a cylinder.

---

## Example 1: volume and surface area of a sphere inside a cube

> An art-installation sphere is constructed so that it fits exactly inside a cube whose edges are $10$ cm long. What are its surface area and volume, in terms of $\pi$?

When a sphere sits snugly inside a cube, the sphere's diameter equals the cube's side length. So the diameter is $10$ cm, making the radius

$$
r = \frac{10}{2} = 5 \text{ cm}.
$$

**Surface area:**

$$
SA = 4\pi r^2 = 4\pi (5)^2 = 4\pi (25) = 100\pi \text{ cm}^2.
$$

**Volume:**

$$
V = \tfrac{4}{3}\pi r^3 = \tfrac{4}{3}\pi (5)^3 = \tfrac{4}{3}\pi (125) = \tfrac{500}{3}\pi \text{ cm}^3.
$$

Approximating at the very end gives $SA \approx 314.16 \text{ cm}^2$ and $V \approx 523.60 \text{ cm}^3$. Notice how the inside-the-cube scenario simply fixed the radius as half the edge — nothing about the sphere formulas themselves changed.

---

## Example 2: a cube inside a sphere

> A drone payload capsule is a sphere of radius $6$ in. What is the edge length of the largest cube that fits snugly inside the sphere, and what is that cube's volume?

When a cube is inscribed inside a sphere, the cube's **space diagonal** (corner to opposite corner, passing through the interior) equals the sphere's diameter. The diameter is $2r = 12$ in, so the cube's space diagonal is $12$ in.

For a cube with edge length $s$, the space diagonal is $s\sqrt{3}$ (this comes from applying the Pythagorean theorem twice). Setting that equal to the diameter:

$$
s\sqrt{3} = 12 \quad\Longrightarrow\quad s = \frac{12}{\sqrt{3}} = 4\sqrt{3} \text{ in}.
$$

The cube's volume is $s^3$:

$$
V_{\text{cube}} = (4\sqrt{3})^3 = 64 \cdot 3\sqrt{3} = 192\sqrt{3} \text{ in}^3 \approx 332.55 \text{ in}^3.
$$

For comparison, the sphere itself has volume $\tfrac{4}{3}\pi (6)^3 = 288\pi \approx 904.78 \text{ in}^3$. The cube uses about $37\%$ of the sphere's available space.

---

## Example 3: solving backward for a radius

> A spherical 3D-printed bearing has a surface area of $36\pi \text{ mm}^2$. What is its radius, and what is its volume?

Start from the surface area formula and plug in:

$$
36\pi = 4\pi r^2.
$$

Divide both sides by $4\pi$:

$$
9 = r^2 \quad\Longrightarrow\quad r = 3 \text{ mm}.
$$

Now that the radius is known, substitute into the volume formula:

$$
V = \tfrac{4}{3}\pi r^3 = \tfrac{4}{3}\pi (3)^3 = \tfrac{4}{3}\pi (27) = 36\pi \text{ mm}^3.
$$

One nice quirk: for this particular radius, the numeric value of $SA$ (in square mm) equals the numeric value of $V$ (in cubic mm). That is not a universal rule, just an artifact of $r = 3$ making things cancel. Your answer is $r = 3 \text{ mm}$ and $V = 36\pi \text{ mm}^3$.

---

## Common pitfalls

- **Mixing up $r^2$ and $r^3$.** Surface area uses $r^2$, volume uses $r^3$. An easy memory: two-dimensional things get the square, three-dimensional things get the cube.
- **Forgetting to halve the diameter.** If the problem gives the diameter instead of the radius, divide by $2$ first, then square or cube. Squaring the diameter is a common slip that quadruples your final answer.
- **Cubing sloppily.** $r^3$ means $r \cdot r \cdot r$, not $3r$. For $r = 4$, that is $64$, not $12$.
- **Dropping the $\tfrac{4}{3}$.** In the volume formula, the $\tfrac{4}{3}$ factor is not optional. If your answer matches $\pi r^3$ without any fraction, you forgot it.

---

## Prerequisites

- [[Circumference_And_Area_Of_Circles]] — where the $\pi r^2$ inside the surface area formula comes from
- [[Volume_Of_Prisms_And_Cylinders]] — the $2\pi r^3$ cylinder the sphere fits inside
- [[Exponents_And_Powers]] — for handling $r^2$ and $r^3$ cleanly

---

## Problems Involving Surface Area and Volume of Spheres

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections are saved in this browser, and you can visit your [[Vault]] later to view hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="surface_area_and_volume_of_spheres"></div>

---

## See Also

- [[Volume_Of_Prisms_And_Cylinders]] — the cylinder that circumscribes the sphere
- [[Volume_Of_Pyramids_And_Cones]] — the other tapered solids
- [[Surface_Area_Of_Prisms_And_Cylinders]] — non-round outer-skin calculations
- [[Circumference_And_Area_Of_Circles]] — the two-dimensional companion
- [[Composite_Figures]] — for problems combining a sphere with other shapes
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
