---
title: "Composite Figures"
type: topic
aliases: ["Compound Shapes", "Composite Shapes"]
tags: ["#branch-pre-algebra", "#topic-euclidean-geometry", "#skill-visualization", "#skill-multi-step", "#word-problem-support", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Perimeter_And_Area_Of_Polygons"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Volume_Of_Prisms_And_Cylinders"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Perimeter_And_Area_Of_Polygons"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
problem_type_ids: []
figures: ["pre_algebra/composite_figure.svg"]
summary: "Break an irregular shape into pieces you already know, measure each piece, then add or subtract to find the total."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Composite Figures

# Composite Figures

Real-world shapes almost never show up as a pure rectangle or a pure triangle. A garden bed might be shaped like a rectangle with a half-circle of herbs curving off one end. A concrete patio might be an L, as if someone took a bite out of one corner of a square. A stained-glass window might be a rectangle with a triangle sitting on top of it like a pointed hat. These are all **composite figures** — shapes built by joining or carving out simpler ones — and the trick to measuring them is to stop seeing them as "that weird shape" and start seeing them as a collection of shapes you already know how to handle.

![[composite_figure.svg|An L-shaped composite figure showing the decomposition into two rectangles]]

Once you get comfortable splitting a composite figure into its building blocks, you can compute its perimeter or area using only the formulas you have been practicing since sixth grade. The new skill is not another formula — it is the **seeing**. Where should the cut go? Which simpler shapes hide inside? Which edges actually belong to the outline, and which ones were imaginary lines you drew to help yourself think? This topic is where the geometry you know gets strung together into multi-step work.

## What it means / The idea

A composite figure is any 2D shape that can be **decomposed** into a handful of standard pieces: rectangles, triangles, parallelograms, trapezoids, semicircles, quarter-circles, and so on. There are two flavors of composition, and you should recognize both:

- **Additive composition.** Two or more shapes are glued together edge to edge. A rectangle with a semicircle on one end. A rectangle with a triangle on top. An L-shape, which is two rectangles sharing an edge. For area, you add the pieces. For perimeter, you trace only the outside and skip any edge that got buried in the join.
- **Subtractive composition.** A smaller shape is cut out of a bigger one. A rectangular plaque with a circular hole drilled in the middle. A square piece of cardboard with a triangle snipped off a corner. For area, you subtract the missing piece from the whole. For perimeter, you follow whatever edge the real boundary now traces.

The idea in one sentence:

$$
A_{\text{total}} = A_{\text{piece 1}} + A_{\text{piece 2}} + \cdots \quad \text{(add)} \qquad \text{or} \qquad A_{\text{total}} = A_{\text{big}} - A_{\text{cutout}} \quad \text{(subtract)}
$$

Whichever flavor you are looking at, the plan is the same: name the pieces, compute each one separately, then combine.

## How it works / The procedure

1. **Sketch and slice.** Redraw the figure on scratch paper and draw dotted lines where you want to split it. Every piece should be a shape whose area formula you already know — rectangle, triangle, parallelogram, trapezoid, circle, semicircle, or quarter-circle. If a piece still looks weird, cut it again.
2. **Label every side length you need.** Some side lengths will be given directly. Others you will have to figure out by subtracting. If one long side of an L-shape is $12$ and the short side that runs partway along the top is $5$, the leftover piece of the top must be $12 - 5 = 7$. Writing those derived lengths on the sketch prevents half the errors in composite problems.
3. **Compute each piece.** Apply the right formula — $A = \ell w$ for rectangles, $A = \tfrac{1}{2} b h$ for triangles, $A = \pi r^2$ for circles (or half of that for a semicircle) — and write each result down before moving on.
4. **Combine.** Add the pieces for a glued shape; subtract the cutout from the whole for a carved shape. Double-check the units, and if the problem asks for area, your answer should end in square units.
5. **Perimeter is different — trace the outline.** For perimeter, do not add up every side of every piece. Walk the boundary of the real composite figure with your finger and add only the edges you actually travel. An edge that was buried inside the join between two pieces does **not** count.

## Why it works

Area is additive. If you partition a flat region into non-overlapping pieces, the area of the whole equals the sum of the areas of the pieces — no more, no less. That is why the add-the-pieces strategy works for glued shapes, and why the subtract-the-hole strategy works for carved shapes (the region you care about is literally the big region minus the hole's region). Perimeter is different because it measures only the **boundary**, and the boundary is a single continuous curve around the outside. When two shapes get joined along a shared edge, that shared edge disappears into the interior, so it is not part of the boundary anymore. Forgetting that distinction — treating perimeter the same way you treat area — is the single most common way composite-figure problems go wrong.

## Worked examples

### Example 1

Maya is designing a flower bed for the community garden that is shaped like a rectangle with a semicircle of roses attached to one short end. The rectangle is $8$ feet long and $4$ feet wide, and the semicircle's flat edge lies exactly along the $4$-foot end of the rectangle, so its diameter is $4$ feet. Determine the total area of the flower bed, in square feet.

Split the figure into its two named pieces. The rectangle has area

$$
A_{\text{rect}} = \ell w = 8 \cdot 4 = 32 \text{ ft}^2.
$$

The semicircle has diameter $4$ feet, so its radius is $r = 2$ feet. A full circle of radius $2$ has area $\pi r^2 = 4\pi$; a semicircle is half of that, giving

$$
A_{\text{semi}} = \tfrac{1}{2}\pi r^2 = \tfrac{1}{2} \cdot \pi \cdot 4 = 2\pi \text{ ft}^2.
$$

Add the two pieces because the semicircle is glued on:

$$
A_{\text{total}} = 32 + 2\pi \approx 32 + 6.28 = 38.28 \text{ ft}^2.
$$

Maya's flower bed covers about $38.3$ square feet.

### Example 2

At the maker space, Kai is cutting a sheet of acrylic into an L-shaped countertop overlay. The full piece starts as a $12$-inch by $10$-inch rectangle, and a $5$-inch by $4$-inch rectangular corner is removed from the upper right to make room for a support post. Compute the area of the L-shaped piece.

This is a subtractive composite figure. The big rectangle has area

$$
A_{\text{big}} = 12 \cdot 10 = 120 \text{ in}^2.
$$

The removed corner has area

$$
A_{\text{cut}} = 5 \cdot 4 = 20 \text{ in}^2.
$$

Subtract the cutout from the whole:

$$
A_{\text{L}} = 120 - 20 = 100 \text{ in}^2.
$$

Kai's L-shape covers $100$ square inches. A sanity check: you can also reach this answer by slicing the L into two rectangles along a vertical dotted line, getting a $12 \times 6$ bottom strip and a $7 \times 4$ top strip, with areas $72$ and $28$, which add to $100$. Two approaches, same answer — that is a good sign the decomposition was clean.

### Example 3

Priya is painting a trim board for the school newspaper's pop-up book display. The board is shaped like a rectangle that is $14$ inches long and $6$ inches tall, with an identical isoceles triangle attached on top of the rectangle. The triangle's base matches the rectangle's $14$-inch top edge, and the triangle's height is $5$ inches. What is the total area Priya has to paint, and what is the perimeter of the outside of the trim board, given that the two slanted sides of the triangle measure $\sqrt{74}$ inches each?

Start with the area, which is the easier question. The rectangle is

$$
A_{\text{rect}} = 14 \cdot 6 = 84 \text{ in}^2,
$$

and the triangle is

$$
A_{\text{tri}} = \tfrac{1}{2} b h = \tfrac{1}{2} \cdot 14 \cdot 5 = 35 \text{ in}^2.
$$

Add because the triangle is glued on top:

$$
A_{\text{total}} = 84 + 35 = 119 \text{ in}^2.
$$

Now the perimeter. Walk the boundary starting at the bottom-left corner: across the bottom ($14$), up the right side ($6$), up the right slanted edge of the triangle ($\sqrt{74}$), down the left slanted edge of the triangle ($\sqrt{74}$), and down the left side ($6$). The $14$-inch top of the rectangle never shows up in the walk — it is the shared edge where the rectangle meets the triangle, buried inside the figure. So the perimeter is

$$
P = 14 + 6 + \sqrt{74} + \sqrt{74} + 6 = 26 + 2\sqrt{74} \approx 26 + 17.2 = 43.2 \text{ in}.
$$

The total area is $119$ square inches and the perimeter is about $43.2$ inches.

## Common pitfalls

- **Counting the buried edge in a perimeter.** When two pieces are joined along a shared edge, that edge is inside the composite figure and must not be added to the perimeter. Students who add up every side of every piece end up with a number that is too big.
- **Forgetting to subtract for a cutout.** On a subtractive figure, adding all the named pieces gives you the area of the whole rectangle, not the area of the shape with the hole. Make sure you are subtracting the cut piece.
- **Using the wrong radius for a half-circle.** A semicircle whose flat edge is the side of a rectangle has a diameter equal to that side — not a radius. Divide the side length by $2$ before plugging into $\pi r^2$.
- **Mixing units.** If one length is in feet and another in inches, convert to one unit before you do any arithmetic. An answer of "$8 \text{ ft} \cdot 6 \text{ in}$" is not a number.
- **Not labeling derived lengths on the sketch.** In an L-shape, only some side lengths are given; the rest you compute by subtraction. Write those computed lengths directly on the sketch or you will lose track partway through.

## Prerequisites

- [[Perimeter_And_Area_Of_Polygons]] — you need rectangle, triangle, parallelogram, and trapezoid formulas as reflexes
- [[Circumference_And_Area_Of_Circles]] — for the circular or semicircular pieces that show up constantly
- [[Classifying_Triangles_And_Quadrilaterals]] — so you can tell at a glance which formula each sub-piece needs

## Problems Involving Composite Figures

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="composite_figures"></div>

## See Also

- [[Perimeter_And_Area_Of_Polygons]] — the polygon area formulas every decomposition rests on
- [[Circumference_And_Area_Of_Circles]] — for semicircle and quarter-circle pieces
- [[Classifying_Triangles_And_Quadrilaterals]] — for naming the sub-shapes you cut out
- [[Volume_Of_Prisms_And_Cylinders]] — the 3D cousin, where composite solids work the same way
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
