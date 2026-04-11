---
title: "Perimeter and Area of Polygons"
type: topic
aliases: ["Polygon Area", "Polygon Perimeter", "Area Of Polygons"]
tags: ["#branch-pre-algebra", "#topic-euclidean-geometry", "#key-formula", "#skill-formula-substitution", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Composite_Figures"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Polygon_Angle_Sums"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Variables_And_Expressions"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: ["pre_algebra/polygon_areas.svg"]
summary: "Perimeter walks the boundary; area measures the inside. Each polygon family has its own short formula."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Perimeter and Area of Polygons

# Perimeter and Area of Polygons

Picture building a fence around a backyard. You pace along every edge of the property and add up the distances — that total tells you how much fence to buy. That walk-around distance is called the **perimeter**. Now picture rolling sod across the same yard. The question becomes how much grass covers the inside, and that filled-in amount is called the **area**. Perimeter is a length, measured in feet or meters or centimeters. Area is a two-dimensional coverage, measured in square feet or square meters or square centimeters. Any time you hear one of the two words, picture whether you are walking the edge or filling the middle — it will save you from mixing the formulas up.

![[polygon_areas.svg|Triangle, rectangle, parallelogram, and trapezoid with their base and height labeled]]

Every polygon has its own shortcut for area, but they are all built from the same underlying idea: count how many unit squares fit inside. The formulas simply automate that count. Once you know the handful of shortcuts for triangles, rectangles, parallelograms, and trapezoids, almost every shape you meet in pre-algebra geometry becomes a calculation you can finish in a couple of lines.

## What it means / The idea

**Perimeter** is the total distance around the outside of a polygon. To compute it, you add the lengths of every side. No formula is really needed — just $P = s_1 + s_2 + s_3 + \cdots$ — but regular polygons (same-length sides) have quick versions like $P = 4s$ for a square or $P = 3s$ for an equilateral triangle.

**Area** is harder, because different polygon families sit differently against a grid of unit squares. The core area formulas for the families you meet first are

$$
A_{\text{triangle}} = \tfrac{1}{2} b h, \quad A_{\text{rectangle}} = \ell w, \quad A_{\text{parallelogram}} = b h, \quad A_{\text{trapezoid}} = \tfrac{1}{2}(b_1 + b_2) h
$$

In every formula, $b$ or $\ell$ is a **base** (a bottom side you pick) and $h$ is the **height**, which is the perpendicular distance between the base and the opposite side. The height is not a slanted side — it is measured straight up, at a right angle to the base. A parallelogram drawn leaning sideways still has a height that comes in vertically, and that is the length you plug in.

A **regular polygon** — one with all sides the same length and all angles equal — has its own area formula involving an **apothem** (the straight-line distance from the center to the middle of a side):

$$
A_{\text{regular}} = \tfrac{1}{2} a P
$$

where $a$ is the apothem and $P$ is the perimeter. You will meet this for regular hexagons and octagons in particular.

## How it works / The procedure

1. **Name the shape.** Is it a triangle, rectangle, parallelogram, trapezoid, or regular polygon? If you cannot match it to one of those, you probably have a [[Composite_Figures|composite figure]] that must be split into named pieces first.
2. **Pull out the measurements you need.** For perimeter, that means every side length. For area, it means the base and the perpendicular height (for triangles, parallelograms, trapezoids), or the length and width (for rectangles). Watch for slanted sides that are not the height.
3. **Pick the right formula and plug in.** Write the formula first, then substitute. Working symbolically for one line keeps the structure visible and catches a surprising number of errors.
4. **Simplify carefully with the order of operations.** Multiply before adding, handle the $\tfrac{1}{2}$ last, and keep the units attached to each number so you can check your final answer.
5. **Label units.** Area answers end in square units ($\text{cm}^2$, $\text{ft}^2$, $\text{m}^2$). Perimeter answers end in plain length units ($\text{cm}$, $\text{ft}$, $\text{m}$). A raw number without units is an incomplete answer.

## Why it works

Every polygon area formula is really a rule for counting unit squares. A rectangle with length $\ell$ and width $w$ fits into a grid as $\ell$ columns of $w$ squares, so the count is $\ell \cdot w$. A parallelogram can be sliced along a vertical cut and rearranged into a rectangle of the same base and height, so its count is also $b h$ — same area as its rectangle cousin. A triangle is literally half of a parallelogram that shares its base and height, because if you make a copy of the triangle, rotate it, and join it to the original, you get a parallelogram of area $b h$, and the original triangle was half of that, hence $\tfrac{1}{2} b h$. A trapezoid can be split into a rectangle and two triangles, or (even slicker) paired with a flipped copy of itself to form a parallelogram whose base is $(b_1 + b_2)$ and whose height is $h$, which is why its area is half of $(b_1 + b_2) h$. Every formula is the end of a short visual argument, which is why it is worth picturing the shape even while you are crunching numbers.

## Worked examples

### Example 1

Rohan is fencing a triangular vegetable patch at the community garden. The triangle has sides of $6$ meters, $8$ meters, and $10$ meters, with the $8$-meter side lying flat on the ground. The height measured straight up from that $8$-meter base to the opposite corner is $6$ meters. Determine the perimeter (how much fencing Rohan needs) and the area (how much ground the patch covers).

Perimeter is the easy part — just add the three side lengths:

$$
P = 6 + 8 + 10 = 24 \text{ m}.
$$

Rohan needs $24$ meters of fencing. For the area, use the triangle formula with $b = 8$ and $h = 6$:

$$
A = \tfrac{1}{2} b h = \tfrac{1}{2} \cdot 8 \cdot 6 = \tfrac{1}{2} \cdot 48 = 24 \text{ m}^2.
$$

The patch covers $24$ square meters. Notice the number $24$ shows up twice but means two completely different things — once as a length and once as a coverage — and the units are what keep them separate. This is a classic right triangle (its $6$-$8$-$10$ sides are a scaled Pythagorean triple), which is why the $6$-meter side doubles as the height here.

### Example 2

Zoe is staining a trapezoidal wooden sign for the food pantry. The top edge is $14$ inches long, the bottom edge is $22$ inches long, and the perpendicular distance between the two parallel edges is $9$ inches. Give the area of the face of the sign in square inches.

Label the pieces of the trapezoid formula. The two parallel sides are $b_1 = 14$ and $b_2 = 22$, and the height is $h = 9$. Plug in:

$$
A = \tfrac{1}{2}(b_1 + b_2) h = \tfrac{1}{2}(14 + 22) \cdot 9.
$$

Add inside the parentheses first:

$$
= \tfrac{1}{2} \cdot 36 \cdot 9.
$$

Multiply left to right:

$$
= 18 \cdot 9 = 162 \text{ in}^2.
$$

The face of Zoe's sign covers $162$ square inches. A nice check: the trapezoid sits between a $14 \times 9 = 126$-square-inch rectangle and a $22 \times 9 = 198$-square-inch rectangle, so you expect an area somewhere in between. It is — the trapezoid's area of $162$ is exactly the average of $126$ and $198$, which is what the formula is quietly computing.

### Example 3

Emilia is laying a parallelogram-shaped tile mosaic at the coffee shop. The tile has a base of $15$ cm along the floor and the opposite side is also $15$ cm. Its two slanted sides each measure $13$ cm, but the straight-up height from the base to the top side is only $12$ cm. Compute the area of one tile.

The temptation is to use the $13$-cm slanted side as the height, because it is the nearest-looking sloped length. Resist that. The parallelogram area formula needs the perpendicular height, which is $h = 12$ cm, not the slanted $13$. Plug into the formula with $b = 15$ and $h = 12$:

$$
A = b h = 15 \cdot 12 = 180 \text{ cm}^2.
$$

Each tile covers $180$ square centimeters. The $13$-cm slanted side would have given $15 \cdot 13 = 195$, an answer that is too big — if a parallelogram were tilted hard enough, its slanted side could be much longer than its straight height, and using the slant would overstate the area every time. Using the perpendicular height is what keeps the formula honest.

## Common pitfalls

- **Using a slanted side instead of the perpendicular height.** For a parallelogram, triangle, or trapezoid, the height is measured straight up from the base, perpendicular to it. The slanted side is longer and gives a wrong, too-big area.
- **Forgetting the $\tfrac{1}{2}$ on the triangle formula.** $A = b h$ is the parallelogram formula, and a triangle is only half of one. Skipping the half doubles the answer.
- **Confusing perimeter with area.** Perimeter is a one-dimensional length with plain units, while area is a two-dimensional coverage with square units. If your answer to an area question does not end in "square something," something is off.
- **Adding all four sides of a parallelogram into the area formula.** Perimeter uses every side; area uses only base and height. Keep the two questions separate in your head.
- **Mixing units mid-problem.** If one side is in meters and another is in centimeters, convert both to the same unit first. Otherwise the multiplication is meaningless.

## Prerequisites

- [[Classifying_Triangles_And_Quadrilaterals]] — you need to recognize which family a shape belongs to before you pick a formula
- [[Variables_And_Expressions]] — every formula uses variables as placeholders for the actual measurements
- [[Order_Of_Operations]] — plugging numbers into a formula is an expression you then evaluate correctly

## Problems Involving Perimeter and Area of Polygons

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="perimeter_and_area_of_polygons"></div>

## See Also

- [[Composite_Figures]] — how to handle shapes built from two or more of these pieces
- [[Circumference_And_Area_Of_Circles]] — the curved-edge counterpart to polygon area
- [[Classifying_Triangles_And_Quadrilaterals]] — the family tree of shapes that these formulas apply to
- [[Polygon_Angle_Sums]] — angle-side relationships that often show up alongside perimeter and area
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
