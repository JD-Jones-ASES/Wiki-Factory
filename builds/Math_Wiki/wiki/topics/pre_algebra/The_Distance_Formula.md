---
title: "The Distance Formula"
type: topic
aliases: ["Distance Between Two Points", "Distance on a Coordinate Plane"]
tags: ["#branch-pre-algebra", "#topic-analytic-geometry", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "8", section: "8.2"}
related:
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/geometry/Circles"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: ["algebra/distance_formula_derivation.svg"]
summary: "The length of the segment connecting two points is just the Pythagorean theorem applied to a grid."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > The Distance Formula

# The Distance Formula

Suppose you plot two points on graph paper — say, $(1, 2)$ and $(4, 6)$ — and you want to know how far apart they are. You could try to measure with a ruler, but that is approximate at best, and useless if the numbers involve coordinates you cannot conveniently draw. What you really want is a formula: an exact rule that takes any two coordinate pairs and hands back the length of the straight segment between them.

There is such a formula, and it looks more complicated than it really is:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

The amazing thing is that this is not a new idea. It is the [[Pythagorean_Theorem|Pythagorean theorem]] wearing a slightly different costume. Every distance-formula problem is secretly a right-triangle problem in disguise, and once you see the triangle hiding inside, the formula is something you can derive on the spot rather than memorize.

![[distance_formula_derivation.svg|Deriving the distance formula from the Pythagorean theorem]]

---

## Why it works: a right triangle on the grid

Pick two points: call them $P(x_1, y_1)$ and $Q(x_2, y_2)$. Draw the segment from $P$ to $Q$ — that is the distance you are after. Now drop a horizontal line from one point and a vertical line from the other until they meet at a corner. You have just built a right triangle, with the segment $PQ$ as its hypotenuse.

How long are the two legs?

- The **horizontal leg** runs from $x_1$ to $x_2$, so its length is $|x_2 - x_1|$.
- The **vertical leg** runs from $y_1$ to $y_2$, so its length is $|y_2 - y_1|$.

Call those leg lengths $a$ and $b$, and call the hypotenuse $d$. The Pythagorean theorem says $a^2 + b^2 = d^2$, which translates into coordinates as

$$
(x_2 - x_1)^2 + (y_2 - y_1)^2 = d^2
$$

Take the positive square root of both sides — distance is never negative — and you land exactly on the distance formula. Since squaring wipes out any minus signs, you also do not have to worry about the absolute-value bars on the legs; the $(x_2 - x_1)^2$ is the same whether you started with a positive or a negative difference.

A side note: it does not matter which point you label first. If you swap $(x_1, y_1)$ and $(x_2, y_2)$, the sign of each difference flips, but squaring fixes it. The formula gives the same distance either way.

---

## Example 1: a classic 3-4-5 triangle

> Compute the distance between $(1, 2)$ and $(4, 6)$.

The horizontal leg has length $4 - 1 = 3$ and the vertical leg has length $6 - 2 = 4$. Plug into the formula:

$$
d = \sqrt{(4 - 1)^2 + (6 - 2)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

So the points sit exactly $5$ units apart. The triangle tucked inside this problem is the most famous right triangle in mathematics: the $3$-$4$-$5$. Whenever the leg differences come out to $3$ and $4$, expect a hypotenuse of $5$, and similarly for other Pythagorean triples like $5$-$12$-$13$ and $8$-$15$-$17$.

---

## Example 2: negative coordinates

> How far apart are the points $(-2, 5)$ and $(3, -7)$?

The negative numbers look intimidating, but the formula does not care — squaring makes every difference positive. Compute each leg:

$$
x_2 - x_1 = 3 - (-2) = 5 \qquad y_2 - y_1 = -7 - 5 = -12
$$

Subtracting a negative flips to addition, so the horizontal leg is $5$. The vertical difference is $-12$, but $(-12)^2 = 144$, so the sign vanishes as soon as you square. Now finish:

$$
d = \sqrt{5^2 + (-12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13
$$

Another Pythagorean triple, this one the $5$-$12$-$13$. The takeaway: the hardest part of negative-coordinate problems is the bookkeeping around the minus signs. Write each difference out carefully, square every leg before adding, and the sign issues dissolve.

---

## Example 3: testing for a right triangle

> Three points sit on the grid: $A(0, 0)$, $B(6, 0)$, and $C(6, 8)$. Do they form a right triangle?

For three points to be the vertices of a right triangle, the three side lengths have to satisfy $a^2 + b^2 = c^2$ — the converse of the Pythagorean theorem. So you compute all three distances and then check.

Side $AB$: $d = \sqrt{(6 - 0)^2 + (0 - 0)^2} = \sqrt{36} = 6$.

Side $BC$: $d = \sqrt{(6 - 6)^2 + (8 - 0)^2} = \sqrt{64} = 8$.

Side $AC$: $d = \sqrt{(6 - 0)^2 + (8 - 0)^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.

Now check: is $6^2 + 8^2 = 10^2$? That is $36 + 64 = 100$, which is true. The three points form a right triangle, with the right angle at $B$. If the arithmetic had not worked out, the triangle would be some other shape (acute or obtuse), and the answer would be no. This same trick — "compute all three sides with the distance formula, then check the Pythagorean relation" — is how you test any triple of points on a grid.

Applications do not stop there. Sum the three distances and you get the **perimeter** of the triangle. Apply the same idea to the sides of a quadrilateral and you can check whether it is a square, rhombus, or parallelogram just from coordinates. On a real map with grid coordinates, the distance formula tells you the straight-line distance between any two labeled locations.

---

## Common pitfalls

- **Forgetting to square each difference.** A very common slip is writing $\sqrt{(x_2 - x_1) + (y_2 - y_1)}$ instead of squaring the two differences first. Always square the legs, then add, then take the square root.
- **Subtraction sign errors with negatives.** When a coordinate is negative, the subtraction becomes addition: $3 - (-2) = 5$, not $1$. Write out each difference step by step.
- **Stopping at $d^2$ instead of $d$.** The formula gives $d^2$ after the squared-and-added step; you still need to take the square root for the actual distance.
- **Leaving an unsimplified radical.** If the arithmetic lands on $\sqrt{50}$, push it one step further to $5\sqrt{2}$. If it lands on $\sqrt{34}$, though, you are done — $34$ has no perfect-square factors.

---

## Prerequisites

Before practicing, make sure you are comfortable with:

- [[The_Pythagorean_Theorem]] — the distance formula is literally Pythagoras in coordinate clothing, and you cannot derive or really understand it without that starting point
- [[Plotting_Points_And_The_Coordinate_Plane]] — you need to be able to read and sketch points $(x, y)$ without hesitation
- [[Simplifying_Radical_Expressions]] — most answers come out as square roots, and the final form usually has the radical reduced

---

## Problems Involving The Distance Formula

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_distance_formula"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[The_Pythagorean_Theorem]]
- [[Plotting_Points_And_The_Coordinate_Plane]]
- [[Simplifying_Radical_Expressions]]
- [[Circles]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
