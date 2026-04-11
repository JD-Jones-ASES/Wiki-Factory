---
title: "Polygon Angle Sums"
type: topic
aliases: ["Interior Angle Sum", "Exterior Angle Sum", "Regular Polygon Angles"]
tags: ["#branch-geometry", "#topic-euclidean-geometry", "#key-formula"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Points_Lines_Angles_And_Angle_Relationships"
  - "topics/geometry/Triangle_Congruence_Criteria"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Points_Lines_Angles_And_Angle_Relationships"
problem_type_ids: []
figures: ["geometry/regular_polygon_interior_angle.svg"]
summary: "How the interior and exterior angles of any polygon add up, derived by triangulating the shape, with handy shortcuts for regular polygons."
---

> [[_overview|Home]] > [[Geometry|Geometry]] > Polygon Angle Sums

# Polygon Angle Sums

Every triangle's interior angles add to $180°$. Every quadrilateral's interior angles add to $360°$. Every pentagon's interior angles add to $540°$. There's a pattern here: as you add a side to a polygon, the interior-angle total jumps by another $180°$. This page gives you the clean formulas for that pattern, shows why the formulas work, and does the same thing for exterior angles.

![[regular_polygon_interior_angle.svg|A regular polygon triangulated into triangles from one vertex]]

Once you have these formulas, any question about the angles of a polygon — regular or irregular, four sides or forty — collapses to a single multiplication and a single division.

---

## The interior angle sum formula

For any convex polygon with $n$ sides,

$$
\text{sum of interior angles} = (n - 2) \cdot 180°.
$$

Plug in the small cases as sanity checks. For a triangle ($n = 3$), you get $(3 - 2) \cdot 180° = 180°$, matching [[Triangle_Angle_Sum_And_Exterior_Angles]]. For a quadrilateral ($n = 4$), you get $(4 - 2) \cdot 180° = 360°$. A pentagon ($n = 5$) gives $540°$, and a hexagon ($n = 6$) gives $720°$. Each additional side adds $180°$ to the total.

---

## How to derive it (triangulation)

Pick any single vertex of your polygon and draw straight lines from that vertex to every other vertex. This chops the polygon into a bunch of triangles. Count them: an $n$-sided polygon splits into exactly $n - 2$ triangles this way, because each triangle uses two neighboring vertices plus your chosen vertex, and you run out after $n - 2$ steps.

Every triangle contributes $180°$ to the polygon's total interior-angle sum, because every piece of every polygon interior angle ends up inside one of the triangles. So the total is

$$
(n - 2) \cdot 180°.
$$

No trickery — the triangle is the building block, and you are adding up how many of them fit inside.

---

## The exterior angle sum

At each vertex of a convex polygon, extend one of the two sides past the vertex. The angle between the extended side and the other side is called an **exterior angle**. Add up one exterior angle per vertex (one at each corner, same direction of travel) and you get an invariant that surprises students the first time they see it:

$$
\text{sum of exterior angles} = 360°
$$

**for every convex polygon**, regardless of how many sides it has. A triangle's three exterior angles total $360°$; a hundred-sided polygon's hundred exterior angles also total $360°$. The intuition: walk around the outside of the polygon once, turning through each exterior angle as you go. By the time you return to your starting vertex, you have made exactly one full rotation, and one full rotation is $360°$.

---

## Regular polygon shortcuts

A **regular polygon** has all sides equal *and* all angles equal. Regular polygons are especially easy because every interior angle takes the same value, and every exterior angle takes the same value, so you can just divide.

For a regular $n$-gon:

$$
\text{each interior angle} = \frac{(n - 2) \cdot 180°}{n}
$$

$$
\text{each exterior angle} = \frac{360°}{n}.
$$

Notice that for a regular polygon, each interior angle plus its neighboring exterior angle must sum to $180°$, because those two angles together form a straight line along one of the sides. That gives an extra sanity check on any regular-polygon calculation.

---

## Example 1: interior angle of a regular hexagon

> A regular hexagon — a shape with six equal sides and six equal angles, like the honeycomb cell — has what measure for each interior angle?

Use the regular-polygon formula with $n = 6$:

$$
\text{each interior angle} = \frac{(6 - 2) \cdot 180°}{6} = \frac{4 \cdot 180°}{6} = \frac{720°}{6} = 120°.
$$

Each interior angle of a regular hexagon measures $120°$. Cross-check with the exterior-angle shortcut: each exterior angle is $360° / 6 = 60°$, and $120° + 60° = 180°$. Consistent.

---

## Example 2: finding the missing interior angle in an irregular pentagon

> A pentagon has four known interior angles of $80°$, $115°$, $97°$, and $128°$. What is the measure of the fifth interior angle?

The interior angles of a pentagon total $(5 - 2) \cdot 180° = 540°$. Subtract the four known angles:

$$
540° - 80° - 115° - 97° - 128° = 540° - 420° = 120°.
$$

The fifth angle measures $120°$.

---

## Example 3: working backwards from an interior angle

> A regular polygon has an interior angle of $150°$ at every vertex. How many sides does the polygon have?

Set up the formula for a regular polygon's interior angle and solve for $n$:

$$
\frac{(n - 2) \cdot 180°}{n} = 150°.
$$

Multiply both sides by $n$:

$$
(n - 2) \cdot 180° = 150° \cdot n.
$$

Expand the left side:

$$
180° \cdot n - 360° = 150° \cdot n.
$$

Subtract $150° \cdot n$ from both sides:

$$
30° \cdot n - 360° = 0.
$$

Add $360°$ to both sides and divide by $30°$:

$$
30° \cdot n = 360° \implies n = 12.
$$

The polygon has $12$ sides. That's a regular dodecagon. Cross-check: each exterior angle is $360° / 12 = 30°$, and $150° + 30° = 180°$. Consistent.

---

## Common pitfalls

- **Subtracting only $1$ instead of $2$ from $n$.** The formula uses $(n - 2)$, not $(n - 1)$. The easy way to remember this is to check against the triangle: a triangle has $n = 3$, and $(3 - 2) \cdot 180° = 180°$, exactly what you want.
- **Using the interior-sum formula per vertex.** The expression $(n - 2) \cdot 180°$ is the *total* for the whole polygon, not the measure of a single angle. You only get the per-vertex value if you divide by $n$, and only then if the polygon is regular.
- **Expecting the exterior sum to depend on $n$.** It does not. The sum of exterior angles is $360°$ for every convex polygon. This is counterintuitive but reliable.
- **Applying these formulas to concave (non-convex) polygons.** If one of the polygon's interior angles is greater than $180°$ (a "dent"), the shape is concave and the clean exterior-sum story breaks down. These formulas assume a convex polygon.

---

## Prerequisites

- [[Triangle_Angle_Sum_And_Exterior_Angles]] — the $180°$ fact that the entire derivation rests on
- [[Classifying_Triangles_And_Quadrilaterals]] — lets you recognize when a quadrilateral is also a special case where the angle sum gives extra information
- [[Points_Lines_Angles_And_Angle_Relationships]] — vocabulary for interior vs. exterior angles

---

## Problems Involving Polygon Angle Sums

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polygon_angle_sums"></div>

---

## See Also

- [[Triangle_Angle_Sum_And_Exterior_Angles]] — the base case
- [[Classifying_Triangles_And_Quadrilaterals]] — where quadrilaterals' $360°$ total comes from
- [[Triangle_Congruence_Criteria]]
- [[Points_Lines_Angles_And_Angle_Relationships]]
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
