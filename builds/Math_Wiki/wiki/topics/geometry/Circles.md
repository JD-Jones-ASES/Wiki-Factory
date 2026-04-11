---
title: "Circles"
type: topic
aliases: ["Circle", "Circle Equation", "Analytic Circles"]
tags: ["#branch-geometry", "#topic-analytic-geometry", "#key-topic", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs: []
related: ["topics/Coordinate_Plane", "formulas/Pythagorean_Theorem"]
status: draft
confidence: high
branch: geometry
prerequisites: ["topics/Coordinate_Plane", "formulas/Pythagorean_Theorem"]
problem_type_ids:
  - "circles_equation_from_center_radius"
  - "circles_center_radius_from_equation"
  - "circles_area_from_radius"
  - "circles_circumference_from_radius"
  - "circles_area_from_diameter"
figures: ["geometry/circle_parts.svg"]
summary: "The set of points equidistant from a center; its equation, area, and circumference."
---
> [[_overview|Home]] > [[Geometry|Geometry]] > Circles

# Circles

A **circle** is the set of all points in a plane that are the same distance from a single fixed point. That fixed point is called the **center**, and the constant distance is the **radius**.

You already know circles. What algebra adds is a recipe for describing any circle with one equation. Once you have the equation, you can answer every question about the circle with nothing more than careful substitution.

![[circle_parts.svg|Parts of a circle]]

---

## The standard form

The most useful way to write a circle's equation is the **standard form**:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

where $(h, k)$ is the center and $r$ is the radius. Plug any point $(x, y)$ on the circle into the left side and you get $r^2$. Points off the circle give a different value.

### Why this works

Pick any point $(x, y)$ on a circle centered at $(h, k)$ with radius $r$. The distance from the center to that point is, by the distance formula:

$$
\sqrt{(x - h)^2 + (y - k)^2}
$$

This distance equals $r$ for every point on the circle. Squaring both sides to get rid of the square root gives the standard form. So the circle's equation is just the distance formula (which itself comes from the [[Pythagorean_Theorem]]) with both sides squared.

---

## Area and circumference

Every circle has two famous measurements:

- **Area:** $A = \pi r^2$
- **Circumference:** $C = 2 \pi r$

The number $\pi$ (pi) is about $3.14159$, but it is irrational — it has no exact decimal form. For most problems you should leave $\pi$ in your answer rather than approximating. Writing $25\pi$ is exact; writing $78.54$ is a rounded estimate.

### Diameter vs. radius

The **diameter** $d$ of a circle is twice the radius: $d = 2r$, so $r = d / 2$. Problems sometimes give you the diameter instead of the radius — always convert to the radius first before applying formulas.

---

## Example: from center and radius to equation

> Find the equation of the circle with center $(3, -2)$ and radius $5$.

Start from the standard form:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

Substitute $h = 3$, $k = -2$, $r = 5$:

$$
(x - 3)^2 + (y - (-2))^2 = 5^2
$$

Simplify the double negative and square the radius:

$$
(x - 3)^2 + (y + 2)^2 = 25
$$

That's the answer.

---

## Example: from equation to center and radius

> Find the center and radius of the circle $(x + 4)^2 + (y - 1)^2 = 36$.

Compare to the standard form and match term by term. Watch the signs carefully — $(x - h)^2$ means $h$ is whatever is being subtracted. So $(x + 4)^2 = (x - (-4))^2$ means $h = -4$. And $(y - 1)^2$ means $k = 1$.

The right side is $r^2 = 36$, so $r = 6$.

**Center:** $(-4, 1)$. **Radius:** $6$.

---

## Prerequisites

Before you practice circle problems, make sure you're comfortable with:

- [[The_Coordinate_Plane|The coordinate plane]] — plotting points and reading coordinates
- [[Pythagorean_Theorem|The Pythagorean theorem]] — where the distance formula (and therefore the circle equation) comes from

If either of those is shaky, start there and come back.

---

## Problems Involving Circles

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections stay in this browser. When you're ready, open your [[Vault]] to see them all, view hints and answers, and print a worksheet.

<div class="problem-vault-widget" data-topic-slug="circles"></div>

---

## See Also

- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[Formulas_Overview]]
- [[Vault|Your Practice Vault]]
- [[_overview|Home]]
