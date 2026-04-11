---
title: "Triangle Angle Sum and Exterior Angles"
type: topic
aliases: ["Triangle Angle Sum", "Exterior Angle Theorem", "Triangle Interior Angles"]
tags: ["#branch-pre-algebra", "#topic-euclidean-geometry"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "7", section: "7.1"}
related:
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Similar_Triangles"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/algebra/One_Step_Equations"
problem_type_ids: []
figures: []
summary: "Every triangle's three interior angles sum to 180 degrees, and each exterior angle equals the sum of the two non-adjacent interior angles."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Triangle Angle Sum and Exterior Angles

# Triangle Angle Sum and Exterior Angles

There is one fact about triangles that shows up in nearly every geometry problem you will ever solve: no matter how you draw a triangle — tall and thin, wide and squat, a skinny right triangle or a fat obtuse one — its three interior angles always add up to the same number. That number is $180^\circ$, the same as the measure of a straight line. Once you internalize this, finding a missing angle in a triangle becomes as simple as subtraction.

A second, equally handy fact connects the interior angles of a triangle to the angles formed outside it when you extend one of its sides. This is called the **Exterior Angle Theorem**, and it gives you a slick shortcut for dozens of problems that would otherwise require two steps.

---

## Key ideas

**The Triangle Angle-Sum Theorem.** Label the three interior angles of a triangle as $\angle A$, $\angle B$, and $\angle C$. Then:

$$
m\angle A + m\angle B + m\angle C = 180^\circ
$$

This is true for *every* triangle drawn in a flat plane — no exceptions. A near-flat triangle with two angles close to $90^\circ$ still obeys the rule, and so does an obtuse triangle with one very large angle; the three numbers always balance out to $180^\circ$.

One quick way to see why this has to be true: tear the three corners off any paper triangle and try to fit them side by side. They always line up into a perfectly straight angle — which is exactly $180^\circ$. The rule is built into the geometry of flat space itself.

**Consequences of the $180^\circ$ rule.** A handful of smaller facts fall out of the theorem with no extra work:

- A triangle can have at most one right angle. Two right angles alone would already add to $180^\circ$, leaving nothing for the third.
- A triangle can have at most one obtuse angle. Two angles over $90^\circ$ would already exceed $180^\circ$.
- Every triangle has at least two acute angles.
- In an equilateral triangle, all three angles must be equal, and since they share $180^\circ$, each one is exactly $60^\circ$.
- In an isosceles triangle, the two base angles — the ones sitting opposite the equal sides — are equal to each other.

**Finding a missing angle.** The whole point of the theorem is that if you know any two interior angles of a triangle, you can compute the third by subtracting their sum from $180^\circ$:

$$
m\angle C = 180^\circ - m\angle A - m\angle B
$$

This is the single most used move in triangle problems.

**Exterior angles: a linear-pair picture.** Pick a vertex of a triangle — say vertex $C$ — and extend one of the sides that meet there past the vertex. The angle formed between the extension and the other side of the triangle is called an **exterior angle** at $C$. The interior angle $\angle C$ and this new angle sit on a straight line together, so they always add to $180^\circ$. In symbols, if the exterior angle is $\angle D$:

$$
m\angle C + m\angle D = 180^\circ
$$

Any pair of angles on a straight line like this is called a *linear pair*.

**The Exterior Angle Theorem.** Here is where the slick shortcut comes in. Because the three interior angles already add to $180^\circ$, and because the interior angle at $C$ plus the exterior angle at $C$ also adds to $180^\circ$, a little algebra connects the exterior angle directly to the *other two* interior angles:

$$
m\angle D = m\angle A + m\angle B
$$

In words: an exterior angle of a triangle is the sum of the two interior angles it is not touching. These two non-adjacent angles are usually called the **remote interior angles** of the exterior angle. This theorem is convenient because it lets you compute the exterior angle in one move, without detouring through the interior angle at the same vertex.

---

## Example 1: finding a missing interior angle

> A triangle has two known angles measuring $52^\circ$ and $81^\circ$. How many degrees is the third angle?

Apply the Angle-Sum Theorem. Call the unknown angle $x$. The three angles add to $180^\circ$:

$$
52^\circ + 81^\circ + x = 180^\circ
$$

Combine the two known angles:

$$
133^\circ + x = 180^\circ
$$

Subtract $133^\circ$ from both sides:

$$
x = 180^\circ - 133^\circ = 47^\circ
$$

So the third angle measures $47^\circ$. Because all three angles are less than $90^\circ$, this triangle is acute.

---

## Example 2: the angles of an isosceles triangle

> An isosceles triangle has a vertex angle of $30^\circ$. What is the measure of each base angle?

An isosceles triangle has two equal sides, and the two angles opposite those equal sides are called the **base angles**. They are always equal to each other. The *vertex angle* is the third angle — the one between the two equal sides.

Let each base angle measure $x$. The three interior angles sum to $180^\circ$, so:

$$
x + x + 30^\circ = 180^\circ
$$

$$
2x = 150^\circ
$$

$$
x = 75^\circ
$$

Each base angle is $75^\circ$. Notice that this answer obeys the basic consistency check: $75^\circ + 75^\circ + 30^\circ$ does indeed equal $180^\circ$. A good habit whenever you solve for an angle is to add all three back up and confirm they still reach $180^\circ$.

---

## Example 3: using the Exterior Angle Theorem

> In triangle $LMN$, side $MN$ is extended past $N$ to a point $P$. The two interior angles at the un-extended vertices are $m\angle L = 40^\circ$ and $m\angle M = 75^\circ$. Compute the measure of the exterior angle $\angle LNP$.

The exterior angle at $N$ is formed by the side $LN$ and the extension $NP$. Vertices $L$ and $M$ are both *non-adjacent* to that exterior angle — in other words, they are the remote interior angles. So the Exterior Angle Theorem applies directly:

$$
m\angle LNP = m\angle L + m\angle M = 40^\circ + 75^\circ = 115^\circ
$$

The exterior angle measures $115^\circ$. No detour needed.

You could also confirm this the long way round. First find the interior angle at $N$ using the Angle-Sum Theorem: $m\angle N = 180^\circ - 40^\circ - 75^\circ = 65^\circ$. Then use the fact that $\angle N$ and $\angle LNP$ form a linear pair: $m\angle LNP = 180^\circ - 65^\circ = 115^\circ$. Same answer, twice the work. That is why the Exterior Angle Theorem is worth memorizing.

---

## Common pitfalls

- **Pairing the exterior angle with the wrong interior angles.** The Exterior Angle Theorem links an exterior angle to the *two interior angles at the OTHER vertices* — never the interior angle at the same vertex. Accidentally including the adjacent interior angle will give a wrong answer.
- **Treating the rule as a calculator fact instead of a constraint.** $180^\circ$ is not just "what you plug in once." Every solution you propose must stay consistent with it: if you find that two angles of a triangle are $110^\circ$ and $85^\circ$, something has gone wrong because they already exceed $180^\circ$ before you even add the third.
- **Assuming isosceles when you haven't checked.** The trick "the two base angles are equal" only works once you know the triangle really is isosceles. Ordinary scalene triangles have three different angles.
- **Confusing exterior angles with reflex angles.** The exterior angle is the one formed with the extension of a side, not the full turn around the vertex. It is always less than $180^\circ$ for a normal triangle.

---

## Prerequisites

Before you tackle the practice problems, check that you are comfortable with:

- [[Classifying_Triangles_And_Quadrilaterals]] — so the words "isosceles," "scalene," "right," "obtuse" are already familiar
- [[One_Step_Equations]] — so you can quickly isolate the unknown angle after you substitute

---

## Problems Involving Triangle Angle Sum and Exterior Angles

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="triangle_angle_sum_and_exterior_angles"></div>

---

## See Also

- [[Classifying_Triangles_And_Quadrilaterals]]
- [[Similar_Triangles]]
- [[The_Pythagorean_Theorem]]
- [[Similar_Triangles]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
