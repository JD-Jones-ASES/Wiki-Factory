---
title: "Classifying Triangles and Quadrilaterals"
type: topic
aliases: ["Triangle Classification", "Quadrilateral Hierarchy"]
tags: ["#branch-pre-algebra", "#topic-euclidean-geometry", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Points_Lines_Angles_And_Angle_Relationships"
  - "topics/geometry/Polygon_Angle_Sums"
  - "topics/geometry/Triangle_Congruence_Criteria"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Points_Lines_Angles_And_Angle_Relationships"
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
problem_type_ids: []
figures: ["geometry/quadrilateral_hierarchy.svg"]
summary: "Sorting triangles by their sides and angles, and tracing the family tree of quadrilaterals from general parallelograms to squares."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Classifying Triangles and Quadrilaterals

# Classifying Triangles and Quadrilaterals

Most geometry problems start with a picture of a shape and one question: *what kind is it?* If you can name the shape precisely, half the work is already done, because every named shape comes with a bundle of properties you can immediately use. A triangle labeled "right" hands you a free $90°$ angle. A quadrilateral labeled "rhombus" hands you four equal sides and perpendicular diagonals. Naming unlocks.

This topic is the vocabulary page for triangles and four-sided shapes. Once the names are in your head, you can walk into [[Triangle_Angle_Sum_And_Exterior_Angles]], [[Polygon_Angle_Sums]], and [[Triangle_Congruence_Criteria]] without stopping to translate.

![[quadrilateral_hierarchy.svg|The family tree connecting quadrilaterals]]

---

## Triangles: two independent labels

Every triangle gets *two* labels, one for its sides and one for its angles, and the two labels are independent. A triangle is, say, an "isosceles right triangle" — that is one side-label and one angle-label stacked together.

**By side lengths:**

- **Equilateral** — all three sides have the same length. Because all sides match, all three angles also measure $60°$.
- **Isosceles** — at least two sides match. The angles opposite those two equal sides are also equal. (Equilateral triangles are technically isosceles too, since "at least two" is satisfied.)
- **Scalene** — no two sides match. All three angles are different as well.

**By interior angles:**

- **Acute** — every interior angle is strictly less than $90°$.
- **Right** — one interior angle is exactly $90°$, marked with a tiny square at the vertex.
- **Obtuse** — one interior angle is strictly greater than $90°$.

A triangle can have at most one right or obtuse angle, because [[Triangle_Angle_Sum_And_Exterior_Angles|the three angles always add to 180°]], and two angles of $90°$ or more would already blow past that total.

---

## Quadrilaterals: a family tree

A **quadrilateral** is any closed shape with exactly four straight sides. What makes this topic rich is that the most important quadrilaterals form a *hierarchy*: a square is a kind of rectangle, which is a kind of parallelogram, which is a kind of quadrilateral. Each step down the tree adds one more restriction while keeping all the properties from above.

- **Parallelogram** — both pairs of opposite sides are parallel. A consequence: opposite sides also come out equal in length, opposite angles come out equal, and the diagonals cut each other in half.
- **Rectangle** — a parallelogram where all four angles are right angles. You still get all the parallelogram properties, plus the diagonals end up equal in length.
- **Rhombus** — a parallelogram with four equal-length sides. Parallelogram properties hold, and the diagonals are perpendicular and bisect the angles they meet.
- **Square** — a shape that is both a rectangle and a rhombus at the same time. Four equal sides, four right angles, diagonals both equal and perpendicular. A square inherits everything.
- **Trapezoid** — exactly one pair of parallel sides. This is *not* a parallelogram, because only one pair is parallel, not two. An **isosceles trapezoid** is the special case where the two non-parallel sides are equal in length, which forces the base angles to match too.
- **Kite** — two pairs of consecutive sides are equal (think of a paper kite with a short pair on top and a long pair on bottom). The diagonals are perpendicular, and one of them bisects the other.

The angles of any quadrilateral add to $360°$, whatever the shape. See [[Polygon_Angle_Sums]] for why.

---

## How to use the hierarchy

The hierarchy tells you which properties you are *allowed* to use. If a problem tells you a shape is a rhombus, you immediately know it is also a parallelogram, so you may use every parallelogram fact too. If a shape is merely a parallelogram, you may *not* assume its sides are equal — that would be adding a rhombus property the problem never granted. Walk up the family tree, never down.

---

## Example 1: naming a triangle from its angles

> A triangle has interior angles of $35°$, $55°$, and $90°$. What labels apply?

First, check that the angles are valid: $35 + 55 + 90 = 180$, good.

The angle of $90°$ makes this a **right triangle**. None of the other two is also $90°$ (and none exceeds $90°$), so there is no second angle-label to apply.

For the side label, we use the fact that equal angles sit opposite equal sides. The two non-right angles are $35°$ and $55°$ — they differ, so the sides opposite them differ, and the triangle has no two equal sides. That makes it **scalene**.

Full answer: a **scalene right triangle**.

---

## Example 2: climbing the quadrilateral tree

> A four-sided shape has both pairs of opposite sides parallel, diagonals that are equal in length, and four interior angles that are all the same measure. Give its most specific name.

Start at the top: both pairs of opposite sides are parallel, so this is at least a **parallelogram**. That gives us opposite sides equal and opposite angles equal already.

Next, four equal interior angles in a quadrilateral must each be $360° \div 4 = 90°$, because the four angles sum to $360°$. Adding "all four angles are right angles" to a parallelogram promotes it to a **rectangle**.

The diagonals being equal in length also fits, but a rectangle already has equal diagonals automatically, so this fact does not push us further. We have no information about whether all four sides are equal, so we cannot promote all the way to a square.

Most specific name: **rectangle**.

---

## Example 3: isosceles versus equilateral

> Jordan sketches a triangle in which two of the sides measure $8$ cm and the third side measures $8$ cm as well. All three angles are equal. What is the most specific classification?

Two sides equal makes the triangle at least **isosceles**. But the third side also measures $8$ cm, so *all three* sides are equal. That promotes the triangle to **equilateral**.

What about the angle label? The three angles are equal and must sum to $180°$, so each one measures $180° \div 3 = 60°$. Every angle is less than $90°$, so the triangle is also **acute**.

Full answer: an **equilateral acute triangle** — though "equilateral" alone is usually enough, because the acute label is automatic for any equilateral triangle.

---

## Common pitfalls

- **Forgetting that squares are rectangles.** Every square satisfies the rectangle definition (four right angles, opposite sides parallel), so "square" and "rectangle" are not exclusive. On a shape-sorting quiz, mark squares as rectangles *and* rhombuses too.
- **Treating a trapezoid as a parallelogram.** A trapezoid has only one pair of parallel sides, not two, so none of the parallelogram shortcuts apply.
- **Applying rhombus properties to a generic parallelogram.** A plain parallelogram is not guaranteed to have equal sides or perpendicular diagonals. Only promote to rhombus when the problem actually says so.
- **Assuming equilateral from two equal sides.** Two equal sides mean isosceles, nothing more. You need a third equal side (or enough angle information to force one) before you are allowed to call it equilateral.

---

## Prerequisites

- [[Points_Lines_Angles_And_Angle_Relationships]] — you need the vocabulary of angles and parallel lines before triangles make sense
- [[Triangle_Angle_Sum_And_Exterior_Angles]] — the $180°$ fact drives most triangle-classification problems
- [[The_Pythagorean_Theorem]] — the hallmark property of right triangles, once you know how to spot them

---

## Problems Involving Classifying Triangles and Quadrilaterals

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="classifying_triangles_and_quadrilaterals"></div>

---

## See Also

- [[Triangle_Angle_Sum_And_Exterior_Angles]] — where the $180°$ rule earns its keep
- [[Polygon_Angle_Sums]] — generalizes the interior-angle idea to any number of sides
- [[Triangle_Congruence_Criteria]] — how knowing a triangle's type feeds into proving two are the same
- [[Similar_Triangles]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
