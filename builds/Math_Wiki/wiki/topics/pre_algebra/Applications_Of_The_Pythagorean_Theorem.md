---
title: "Applications of the Pythagorean Theorem"
type: topic
aliases: ["Pythagorean Applications", "Pythagorean Word Problems"]
tags: ["#branch-pre-algebra", "#topic-euclidean-geometry"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "7", section: "7.5"}
related:
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: []
summary: "Using a squared plus b squared equals c squared to solve ladder problems, diagonals, grid distances, and other right-triangle situations."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Applications of the Pythagorean Theorem

# Applications of the Pythagorean Theorem

By itself, the equation $a^2 + b^2 = c^2$ is a very short piece of algebra — three variables, two squares, one sum. What makes it worth studying is the astonishing number of real-world situations it silently governs. Any time a right angle sits hidden in a problem — a wall meeting the floor, a ladder meeting the ground, a TV screen's width meeting its height, a hiker turning ninety degrees — Pythagoras is the tool that unlocks the missing distance.

This page is about spotting those right angles in the wild and turning them into arithmetic. If the theorem itself feels shaky, bounce back to [[The_Pythagorean_Theorem]] first and come back here once you're comfortable with the formula.

---

## Key ideas

**Step one is always the same: find the right angle.** Every Pythagorean application begins with the same question: *where is the right angle in this situation?* Sometimes a problem tells you outright ("a ladder leans against a vertical wall"). Sometimes you have to spot it yourself, as in a rectangular screen where the corners are automatically right angles. Once you have located the right angle, the two sides that form it are the **legs** ($a$ and $b$), and the side opposite — always the longest — is the **hypotenuse** ($c$).

**Solving for the hypotenuse versus solving for a leg.** The same equation handles both jobs, but the algebra looks slightly different:

- To find the hypotenuse from two legs, compute $c^2 = a^2 + b^2$, then take a square root.
- To find a missing leg from the hypotenuse and one leg, rearrange the equation to $a^2 = c^2 - b^2$, then take a square root.

The only thing that changes is which variable you are isolating. The structure of the equation is the same in both cases.

**Exact versus decimal answers.** When the square root works out to a whole number — $9$, $13$, $25$ — give the exact answer. When it does not, you have a choice: leave it in simplified radical form, such as $\sqrt{50} = 5\sqrt{2}$, or round to a sensible decimal like $7.1$. The problem's context usually tells you which to choose. "How far, in feet, to the nearest tenth?" is asking for a decimal. "Give the exact length" is asking for the radical.

**Distances on a coordinate grid.** Pythagoras is also how you measure the straight-line distance between two points in the coordinate plane. Draw a horizontal leg and a vertical leg forming a right angle between the two points, read off the lengths as the differences of the coordinates, and apply the theorem. That special case is important enough that it gets its own name — the **distance formula** — which you will meet shortly. For now, recognize it as just the Pythagorean Theorem wearing a new outfit.

**The converse is useful too.** A triangle with sides $a$, $b$, $c$ (the largest being $c$) is a right triangle *if and only if* $a^2 + b^2 = c^2$. Carpenters, masons, and anyone else who cares whether a corner is truly square uses this in reverse: if they measure three distances — along one wall, along a second wall, and diagonally across the two — and those numbers form a Pythagorean triple like $(3, 4, 5)$ or $(6, 8, 10)$, the corner is certified square.

---

## Example 1: the ladder problem

> A $17$-foot ladder leans against a vertical wall. The foot of the ladder rests $8$ feet from the base of the wall. How high up the wall does the top of the ladder reach? Round to the nearest tenth of a foot.

First find the right angle. The wall is vertical and the ground is horizontal, so the wall meets the ground at $90^\circ$. The ladder slants from a point up on the wall down to a point out on the ground; the two portions along the wall and along the ground are legs, and the ladder itself is the hypotenuse.

Collect the labels. The leg along the ground is $b = 8$ feet. The ladder — the hypotenuse — is $c = 17$ feet. The unknown is the height on the wall, call it $a$.

Apply the theorem:

$$
a^2 + b^2 = c^2
$$

$$
a^2 + 8^2 = 17^2
$$

$$
a^2 + 64 = 289
$$

Subtract $64$ from each side:

$$
a^2 = 225
$$

Take the positive square root (distances are never negative):

$$
a = \sqrt{225} = 15
$$

The ladder reaches exactly $15$ feet up the wall. This happens to be an exact whole number because $(8, 15, 17)$ is a well-known Pythagorean triple — one of the small-integer side triples that satisfy the theorem perfectly.

---

## Example 2: sizing a TV by its diagonal

> A wide-screen TV is advertised as $55$ inches — the diagonal of the screen. The screen has a $16 : 9$ aspect ratio, so if we write the width as $16k$ and the height as $9k$, how wide and how tall is the actual screen? Round to the nearest tenth of an inch.

Televisions are always sized by the diagonal, which means the advertised number is the hypotenuse of the right triangle formed by the width, the height, and the corner-to-corner line. Set up the Pythagorean equation with the unknown scale factor $k$:

$$
(16k)^2 + (9k)^2 = 55^2
$$

Square each piece:

$$
256 k^2 + 81 k^2 = 3025
$$

Combine like terms:

$$
337 k^2 = 3025
$$

Divide both sides by $337$:

$$
k^2 \approx 8.977
$$

Take a square root:

$$
k \approx 2.996
$$

Now plug back into the width and height:

$$
\text{width} = 16 k \approx 16 \cdot 2.996 \approx 47.9 \text{ inches}
$$

$$
\text{height} = 9 k \approx 9 \cdot 2.996 \approx 27.0 \text{ inches}
$$

So a "$55$-inch" TV is actually about $47.9$ inches wide and $27.0$ inches tall. The diagonal is always larger than either side by itself — worth remembering when you are deciding whether a screen fits on a piece of furniture.

---

## Example 3: distance between two grid points

> Compute the straight-line distance between the points $(2, 1)$ and $(11, 13)$ in the coordinate plane. Give an exact answer.

Draw (even mentally) a horizontal line from $(2, 1)$ to $(11, 1)$ and then a vertical line from $(11, 1)$ up to $(11, 13)$. Those two segments meet at the point $(11, 1)$ in a perfect right angle — the corner of a box. The straight line from $(2, 1)$ to $(11, 13)$ is the hypotenuse of the right triangle whose legs you just drew.

The horizontal leg runs from $x = 2$ to $x = 11$, so its length is $11 - 2 = 9$. The vertical leg runs from $y = 1$ to $y = 13$, so its length is $13 - 1 = 12$. Call the distance between the points $d$:

$$
d^2 = 9^2 + 12^2 = 81 + 144 = 225
$$

$$
d = \sqrt{225} = 15
$$

So the distance between the two points is exactly $15$ units. Another classic Pythagorean triple, $(9, 12, 15)$, which is just $(3, 4, 5)$ multiplied by $3$.

When the numbers don't cooperate so nicely, you still apply the same procedure — the only difference is that your final square root lands on something like $\sqrt{73}$ instead of a clean integer. You will see this exact pattern used over and over once you meet the official distance formula in coordinate geometry.

---

## Common pitfalls

- **Mixing up which side is the hypotenuse.** The hypotenuse sits across from the right-angle corner, and it beats both legs in length. If a problem hands you the hypotenuse and one leg, do *not* plug them into the theorem as though they were both legs. Rearrange first: $\text{leg}^2 = \text{hyp}^2 - \text{other leg}^2$.
- **Forgetting to square, or forgetting to square-root.** The formula has both operations in it. Compute the squares first, add or subtract, and only at the very end take the square root.
- **Negative roots sneaking in.** Taking a square root technically gives you both a positive and a negative value, but a length cannot be negative in a physical problem. Always keep only the positive root here.
- **Using the theorem on a triangle that isn't a right triangle.** Pythagoras applies *only* to right triangles. If the problem does not contain a right angle, the equation is not valid — you will need a different tool (like the Law of Cosines, further along).

---

## Prerequisites

Before you start practicing, it helps to be steady on:

- [[The_Pythagorean_Theorem]] — where the formula $a^2 + b^2 = c^2$ comes from in the first place
- [[Square_Roots_And_Cube_Roots]] — so you can evaluate and simplify the roots that come out at the end
- [[Plotting_Points_And_The_Coordinate_Plane]] — so the grid-distance version of the problem feels natural

---

## Problems Involving Applications of the Pythagorean Theorem

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="applications_of_the_pythagorean_theorem"></div>

---

## See Also

- [[The_Pythagorean_Theorem]]
- [[Similar_Triangles]]
- [[Triangle_Angle_Sum_And_Exterior_Angles]]
- [[Square_Roots_And_Cube_Roots]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
