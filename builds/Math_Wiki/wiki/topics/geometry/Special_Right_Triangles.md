---
title: "Special Right Triangles"
type: topic
aliases: ["30-60-90 Triangle", "45-45-90 Triangle"]
tags: ["#branch-geometry", "#topic-right-triangles", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Triangle_Congruence_Criteria"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Applications_Of_The_Pythagorean_Theorem"
  - "topics/pre_algebra/Similar_Triangles"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
problem_type_ids: []
figures: ["geometry/special_right_triangles.svg"]
summary: "Two right triangles with such clean side ratios — 1:1:√2 and 1:√3:2 — that you can skip the Pythagorean theorem entirely."
---
> [[_overview|Home]] > [[Geometry|Geometry]] > Special Right Triangles

# Special Right Triangles

Most right triangles force you to reach for [[The_Pythagorean_Theorem]] every time you want a missing side. But two particular right triangles — the **45-45-90** and the **30-60-90** — come up so often that their side ratios have been worked out once and for all. Memorize those ratios and you can read off the missing side of either triangle with no arithmetic more serious than a multiplication by $\sqrt{2}$ or $\sqrt{3}$.

The two triangles show up naturally. The 45-45-90 is half of a square cut along its diagonal. The 30-60-90 is half of an equilateral triangle cut down the middle. Because of their clean origins, both have exact, irrational side ratios instead of messy decimals.

![[special_right_triangles.svg|The two special right triangles and their side ratios]]

---

## The 45-45-90 triangle

This triangle has one right angle and two $45°$ angles, which makes the two legs equal in length (they sit opposite equal angles, and [[Classifying_Triangles_And_Quadrilaterals|isosceles]] triangles have equal sides opposite their equal angles). If each leg has length $1$, the Pythagorean theorem gives the hypotenuse:

$$
1^2 + 1^2 = c^2 \implies c^2 = 2 \implies c = \sqrt{2}.
$$

So the side ratio is

$$
\text{leg} : \text{leg} : \text{hypotenuse} = 1 : 1 : \sqrt{2}.
$$

Scale this up or down and the ratio holds. If each leg has length $x$, the hypotenuse has length $x\sqrt{2}$. If the hypotenuse has length $h$, each leg has length $h / \sqrt{2}$, which you usually rewrite as $h \sqrt{2} / 2$.

---

## The 30-60-90 triangle

This triangle has angles $30°$, $60°$, and $90°$. To derive its ratios, drop a perpendicular from one vertex of an equilateral triangle with side length $2$ down to the opposite side. The perpendicular cuts the base in half, so you get two right triangles, each with a short leg of length $1$ (half the base), a hypotenuse of length $2$ (the original side), and angles of $30°$ and $60°$ at the other two corners. The Pythagorean theorem gives the long leg:

$$
1^2 + b^2 = 2^2 \implies b^2 = 3 \implies b = \sqrt{3}.
$$

So the side ratio is

$$
\text{short leg} : \text{long leg} : \text{hypotenuse} = 1 : \sqrt{3} : 2.
$$

The short leg sits opposite the $30°$ angle, the long leg sits opposite the $60°$ angle, and the hypotenuse sits opposite the $90°$ angle. If the short leg has length $x$, the long leg has length $x\sqrt{3}$ and the hypotenuse has length $2x$.

---

## Why these triangles matter

The 45-45-90 falls out of any square, the 30-60-90 falls out of any equilateral triangle, and both appear inside the two most symmetric shapes in elementary geometry. So whenever a problem features a square cut along its diagonal, or an equilateral triangle cut in half, or any angle measured in multiples of $30°$ or $45°$, chances are a special right triangle is hiding inside waiting to speed up the arithmetic. These ratios also anchor your first exposure to trigonometry, because $\sin$ and $\cos$ of $30°$, $45°$, and $60°$ come straight from them.

---

## Example 1: 45-45-90 from a leg

> A skate park ramp is a right triangle with both legs of length $6$ feet and a $45°$ angle at each base corner. How long is the slanted edge (the hypotenuse)?

This is a 45-45-90 triangle with leg $6$. Apply the ratio $\text{leg} : \text{hypotenuse} = 1 : \sqrt{2}$:

$$
\text{hypotenuse} = 6 \cdot \sqrt{2} = 6\sqrt{2} \text{ feet}.
$$

If you want a decimal approximation, $6\sqrt{2} \approx 8.49$ feet. The exact form $6\sqrt{2}$ is preferred unless the problem asks for a decimal.

---

## Example 2: 30-60-90 from the short leg

> A climbing wall has a triangular support panel with angles $30°$, $60°$, and $90°$. The shortest side (opposite the $30°$ corner) measures $5$ meters. Give the lengths of the other two sides.

Short leg is $5$. Using the ratio $1 : \sqrt{3} : 2$:

$$
\text{long leg} = 5\sqrt{3} \text{ m} \qquad \text{hypotenuse} = 5 \cdot 2 = 10 \text{ m}.
$$

Sanity-check with the Pythagorean theorem: $5^2 + (5\sqrt{3})^2 = 25 + 75 = 100 = 10^2$. Consistent.

---

## Example 3: 30-60-90 from the hypotenuse

> A solar panel mount is a 30-60-90 right triangle whose hypotenuse measures $14$ cm. Determine the lengths of the two legs.

Hypotenuse is $14$ and corresponds to the $2$ in the $1 : \sqrt{3} : 2$ ratio. To find the scale, set $2x = 14$, so $x = 7$. Then:

$$
\text{short leg} = x = 7 \text{ cm} \qquad \text{long leg} = x\sqrt{3} = 7\sqrt{3} \text{ cm}.
$$

A quick check: $7^2 + (7\sqrt{3})^2 = 49 + 147 = 196 = 14^2$. Good.

---

## Common pitfalls

- **Putting the side opposite the wrong angle.** In a 30-60-90 triangle, the short leg is opposite the $30°$ corner, the long leg is opposite the $60°$ corner, and the hypotenuse is opposite the $90°$ corner. Mismatch those and every ratio flips.
- **Forgetting that the hypotenuse is twice the short leg, not twice the long leg.** The ratio is $1 : \sqrt{3} : 2$. The $2$ pairs with the $1$, not with the $\sqrt{3}$.
- **Mixing up $\sqrt{2}$ and $\sqrt{3}$.** The $45°$ triangle gets $\sqrt{2}$. The $30°$/$60°$ triangle gets $\sqrt{3}$. Associating the square ($4$ right angles, leads to $\sqrt{2}$) and the equilateral triangle ($3$ equal sides, leads to $\sqrt{3}$) with their respective shortcut helps this stick.
- **Treating $1/\sqrt{2}$ and $\sqrt{2}/2$ as if they were different answers.** They are the same number; most textbooks rationalize the denominator and write $\sqrt{2}/2$.

---

## Prerequisites

- [[The_Pythagorean_Theorem]] — where both special-triangle ratios come from, and a sanity check for every answer
- [[Similar_Triangles]] — why all 30-60-90 triangles (and all 45-45-90 triangles) share a single ratio regardless of size
- [[Classifying_Triangles_And_Quadrilaterals]] — you need to be able to recognize isosceles and equilateral triangles to see where these shortcuts live

---

## Problems Involving Special Right Triangles

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="special_right_triangles"></div>

---

## See Also

- [[Triangle_Congruence_Criteria]] — the HL criterion is especially at home among right triangles
- [[Applications_Of_The_Pythagorean_Theorem]] — when the triangle is not special, the full theorem takes over
- [[Similar_Triangles]]
- [[The_Pythagorean_Theorem]]
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
