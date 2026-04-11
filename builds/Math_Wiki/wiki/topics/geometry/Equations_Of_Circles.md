---
title: "Equations of Circles"
type: topic
aliases: ["Circle Equation Standard Form", "Circle General Form"]
tags: ["#branch-geometry", "#topic-analytic-geometry", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Circles"
  - "topics/geometry/Inscribed_Angles_And_Arcs"
  - "topics/geometry/Chords_Secants_And_Tangents"
  - "topics/algebra/Completing_The_Square"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/The_Distance_Formula"
  - "topics/algebra/Completing_The_Square"
problem_type_ids: []
figures: ["geometry/circle_parts.svg"]
summary: "Two algebraic faces of a circle — the center-radius standard form and the expanded general form — and how to convert between them using completing the square."
---

> [[_overview|Home]] > [[Geometry|Geometry]] > Equations of Circles

# Equations of Circles

A circle on the coordinate plane is completely determined by two pieces of information: its center $(h, k)$ and its radius $r$. Give those two pieces and you can write an equation whose solutions are exactly the points sitting on the circle. This topic covers the two most common algebraic forms for a circle — the clean **standard form** that displays the center and radius directly, and the expanded **general form** where they are hidden — and shows how to move between them using [[Completing_The_Square]].

![[circle_parts.svg|The parts of a circle in the coordinate plane]]

The whole page is an application of the [[The_Distance_Formula|distance formula]], which itself comes from [[The_Pythagorean_Theorem|the Pythagorean theorem]]. Once you see the derivation, the equation stops feeling arbitrary.

---

## Standard form

The **standard form** of a circle with center $(h, k)$ and radius $r$ is

$$
(x - h)^2 + (y - k)^2 = r^2.
$$

Plug any point $(x, y)$ on the circle into the left side and you always get $r^2$. Plug any point off the circle and you get a different value. So the equation picks out exactly the points lying on the circle.

**Why this works.** Let $(x, y)$ be any point on a circle of center $(h, k)$ and radius $r$. The distance from the center to that point is, by the distance formula,

$$
\sqrt{(x - h)^2 + (y - k)^2}.
$$

This must equal $r$. Square both sides to clear the radical and you get the standard-form equation above. That is the whole derivation — the equation of a circle is the distance formula squared.

Reading the standard form back: the signs inside the parentheses are *subtracted* values, so $(x - 3)^2$ means $h = 3$, while $(x + 5)^2 = (x - (-5))^2$ means $h = -5$. The right-hand side is $r^2$, not $r$, so when $r^2 = 49$ the radius is $r = 7$.

---

## General form

If you expand a standard-form equation by squaring the two binomials and collecting constants, you get an equation that looks like

$$
x^2 + y^2 + Dx + Ey + F = 0.
$$

This is the **general form**, where $D$, $E$, and $F$ are constants that depend on the original center and radius but are not directly readable from the equation. Specifically,

$$
D = -2h, \quad E = -2k, \quad F = h^2 + k^2 - r^2.
$$

A general-form equation still describes a circle (as long as the numbers are consistent), but you cannot see the center or radius at a glance. To recover them, you need to convert back to standard form, and that conversion uses completing the square.

---

## Converting general form to standard form

The algorithm is straightforward:

1. Group the $x$ terms together and the $y$ terms together. Move the constant to the right side of the equation.
2. [[Completing_The_Square|Complete the square]] on the $x$ terms: halve the coefficient of $x$, square that, and add the result to both sides.
3. Do the same for the $y$ terms.
4. Factor the left side as the sum of two perfect squares: $(x - h)^2 + (y - k)^2$.
5. Read off the center $(h, k)$ and the radius $r = \sqrt{r^2}$ from the right side.

Once you internalize the steps, the whole conversion is usually under a minute on paper.

---

## Example 1: writing the equation from center and radius

> A circle has center $(4, -3)$ and radius $6$. Give its equation in standard form.

Substitute $h = 4$, $k = -3$, and $r = 6$ into the standard form:

$$
(x - 4)^2 + (y - (-3))^2 = 6^2.
$$

Simplify the double negative and square the radius:

$$
(x - 4)^2 + (y + 3)^2 = 36.
$$

That is the answer. Double-check by testing the point $(4, 3)$, which should lie on the circle because it is $6$ units directly above the center: $(4 - 4)^2 + (3 + 3)^2 = 0 + 36 = 36$. Consistent.

---

## Example 2: reading the center and radius from a standard-form equation

> What are the center and radius of the circle whose equation is $(x + 2)^2 + (y - 7)^2 = 81$?

Match the given equation term by term against $(x - h)^2 + (y - k)^2 = r^2$.

- $(x + 2)^2 = (x - (-2))^2$, so $h = -2$.
- $(y - 7)^2$, so $k = 7$.
- The right side is $81$, so $r^2 = 81$, giving $r = 9$.

Center: $(-2, 7)$. Radius: $9$.

---

## Example 3: converting general form to standard form

> Convert $x^2 + y^2 - 8x + 6y - 11 = 0$ into standard form, then give the center and the radius.

Group $x$ terms and $y$ terms; move the constant to the right side:

$$
(x^2 - 8x) + (y^2 + 6y) = 11.
$$

Complete the square on the $x$ terms. The coefficient of $x$ is $-8$, so halve it to get $-4$ and square it to get $16$. Add $16$ to both sides:

$$
(x^2 - 8x + 16) + (y^2 + 6y) = 11 + 16.
$$

Complete the square on the $y$ terms. The coefficient of $y$ is $6$, so halve it to get $3$ and square it to get $9$. Add $9$ to both sides:

$$
(x^2 - 8x + 16) + (y^2 + 6y + 9) = 11 + 16 + 9.
$$

Factor each group as a perfect square and simplify the right side:

$$
(x - 4)^2 + (y + 3)^2 = 36.
$$

Now read off the answer. Center: $(4, -3)$. Radius: $r = \sqrt{36} = 6$.

A common check: plug a convenient circle point back into the general form. For instance $(10, -3)$ should lie on this circle because it sits $6$ units to the right of the center. Substitute into $x^2 + y^2 - 8x + 6y - 11$: $100 + 9 - 80 - 18 - 11 = 0$. Good.

---

## Common pitfalls

- **Reading $r$ directly off the right side.** The right side of standard form is $r^2$, not $r$. When the right side is $49$, the radius is $7$, not $49$.
- **Getting the sign of the center wrong.** The standard form is $(x - h)^2$, so whatever number is being *subtracted* is the $h$ coordinate. $(x + 5)^2$ corresponds to $h = -5$ because $+5$ comes from $-(-5)$. Signs flip when you read them.
- **Forgetting to add the completed-square constants to both sides.** When you convert general form to standard form, the new constants $(b/2)^2$ have to go on both sides to keep the equation balanced. Dropping them only on the left silently changes the equation.
- **Assuming any $x^2 + y^2 + Dx + Ey + F = 0$ is a circle.** If the right-hand side after completing the square comes out negative, there is no real circle — just a solution set with no points in it. The numbers have to be consistent.

---

## Prerequisites

- [[Plotting_Points_And_The_Coordinate_Plane]] — comfort with the coordinate plane before writing equations on it
- [[The_Distance_Formula]] — the derivation of standard form is literally the distance formula squared
- [[Completing_The_Square]] — the single algebraic move needed to convert between general form and standard form

---

## Problems Involving Equations of Circles

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="equations_of_circles"></div>

---

## See Also

- [[Circles]]
- [[Inscribed_Angles_And_Arcs]]
- [[Chords_Secants_And_Tangents]]
- [[Completing_The_Square]] — the core algebraic technique behind general-to-standard conversion
- [[The_Distance_Formula]]
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
