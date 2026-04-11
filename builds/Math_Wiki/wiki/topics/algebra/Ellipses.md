---
title: "Ellipses"
type: topic
aliases: ["Ellipse", "Ellipse Equation", "Oval"]
tags: ["#branch-algebra-2", "#topic-conic-sections", "#key-topic", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "9", section: "9.3"}
  - {book: "algtrig", chapter: "10", section: "10.2"}
related:
  - "topics/geometry/Circles"
  - "topics/algebra/Parabolas"
  - "topics/algebra/Hyperbolas"
  - "topics/algebra/Completing_The_Square"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/geometry/Circles"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Quadratic_Functions"
problem_type_ids: []
figures: []
summary: "An oval curve built from two foci: every point on the ellipse has the same total distance to the two focus points."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Ellipses

# Ellipses

Stand outside with a loop of string, two thumbtacks, and a pencil. Pin the thumbtacks to a piece of cardboard, drop the string loop around both pins, and pull the pencil tight against the loop. Now trace a curve, keeping the string taut the whole time. What you draw is an ellipse. The shape closes into a smooth oval, slightly stretched in the direction the pins are separated, and if you move the pins closer together the oval rounds out toward a circle.

That physical construction is the geometric definition in disguise. Each pin is a **focus**, and the length of the string is a fixed total distance. Moving the pencil around keeps that total constant — the distance from the pencil to one pin plus the distance from the pencil to the other pin never changes. So an ellipse is the curve traced by every point whose two distances to a pair of fixed focus points add up to the same value. Writing that total as $2a$ gives

$$
d_1 + d_2 = 2a,
$$

where $d_1$ and $d_2$ are the distances from a point on the ellipse to the two foci. The halfway point between the two foci — the midpoint of the segment they define — is the **center** of the ellipse.

---

## Standard form

Translate the string-and-pins construction into coordinates and you get a clean algebraic form. An ellipse with center $(h, k)$ and a horizontal major axis has equation

$$
\dfrac{(x - h)^2}{a^2} + \dfrac{(y - k)^2}{b^2} = 1, \qquad a > b > 0.
$$

Here $a$ is the **semi-major axis** (half the longer axis) and $b$ is the **semi-minor axis** (half the shorter one). Stepping $a$ units left and right from the center lands on the two **vertices**. Stepping $b$ units up and down lands on the two **co-vertices**. Together the four points form the corners of a rectangle (sometimes called a guide rectangle) that hugs the ellipse, and the curve itself is sketched inside the rectangle touching each side at one point.

If the longer axis runs vertically instead, the $a^2$ and $b^2$ swap positions:

$$
\dfrac{(x - h)^2}{b^2} + \dfrac{(y - k)^2}{a^2} = 1, \qquad a > b > 0.
$$

Either way, **the larger denominator always sits under the variable that runs along the major axis**. That is the quickest way to tell which direction an ellipse is stretched.

### Locating the foci

The foci are not at the same distance as the vertices — they sit closer to the center. The focal distance $c$ satisfies

$$
c^2 = a^2 - b^2,
$$

with $c < a$. For a horizontal-axis ellipse the foci are at $(h - c,\; k)$ and $(h + c,\; k)$. For a vertical-axis ellipse they are at $(h,\; k - c)$ and $(h,\; k + c)$ — always on the major axis, always inside the curve. When $a = b$, the formula gives $c = 0$, the two foci collapse into the center, and the ellipse becomes a [[Circles|circle]] of radius $r = a = b$. A circle is just the special case of an ellipse whose two pins have been placed on top of each other.

---

## Key ideas

- Every ellipse is controlled by two foci and a fixed total distance $2a$. The closer the foci sit to each other, the rounder the ellipse; the farther apart, the more stretched.
- The relation $c^2 = a^2 - b^2$ links the three lengths. $a$ is always the largest of the three — the semi-major axis is the longest half-measurement of the ellipse, and the foci sit inside the curve.
- A real planetary orbit is an ellipse with the sun at one focus (Kepler's first law). The eccentricity $e = c/a$, a number between $0$ and $1$, measures how stretched the orbit is: nearly zero means nearly circular, closer to one means highly elongated.
- The **whispering gallery** effect is a reflective property: a sound made at one focus of an elliptical room reflects off the walls and converges cleanly at the other focus, even across a very large room.

---

## Example 1: reading parts from standard form

> Determine the center, vertices, co-vertices, and foci of $\dfrac{(x + 1)^2}{9} + \dfrac{(y - 2)^2}{25} = 1$.

Compare to the standard form. The center is $(-1, 2)$. The denominators are $9$ and $25$; the larger one sits under the $y$-term, so the major axis is **vertical**. That means $a^2 = 25$ and $b^2 = 9$:

$$
a = 5, \qquad b = 3, \qquad c = \sqrt{25 - 9} = \sqrt{16} = 4.
$$

Step $5$ units up and down from the center $(-1, 2)$ for the vertices, $3$ units left and right for the co-vertices, and $4$ units up and down for the foci.

- **Vertices:** $(-1,\; 2 + 5) = (-1, 7)$ and $(-1,\; 2 - 5) = (-1, -3)$.
- **Co-vertices:** $(-1 - 3,\; 2) = (-4, 2)$ and $(-1 + 3,\; 2) = (2, 2)$.
- **Foci:** $(-1,\; 2 + 4) = (-1, 6)$ and $(-1,\; 2 - 4) = (-1, -2)$.

The ellipse is taller than it is wide, and the two foci sit on the long vertical axis, inside the curve.

---

## Example 2: building the equation from geometric data

> Give the standard form of the ellipse with center $(2, -1)$, horizontal major axis of length $10$, and minor axis of length $6$.

A horizontal major axis of length $10$ means the full distance across the ellipse in the $x$-direction is $10$, so the semi-major axis is $a = 5$. A minor axis of length $6$ gives $b = 3$. The center is $(h, k) = (2, -1)$, so

$$
\dfrac{(x - 2)^2}{25} + \dfrac{(y + 1)^2}{9} = 1.
$$

For a quick sanity check on the foci: $c^2 = 25 - 9 = 16$, so $c = 4$. The foci sit $4$ units left and right of the center, at $(-2, -1)$ and $(6, -1)$. Those are inside the horizontal stretch of the ellipse, as they should be.

---

## Example 3: completing the square

> Convert $4x^2 + 9y^2 - 16x + 54y + 61 = 0$ to standard form and name the center and vertices.

Group the $x$-terms and the $y$-terms, then factor out the squared-variable coefficients:

$$
4(x^2 - 4x) + 9(y^2 + 6y) = -61.
$$

Complete the square inside each group. Half of $-4$ is $-2$, squared is $4$; half of $6$ is $3$, squared is $9$. Anything added inside the $x$-parentheses gets multiplied by $4$ on its way out, and anything added inside the $y$-parentheses gets multiplied by $9$:

$$
4(x^2 - 4x + 4) + 9(y^2 + 6y + 9) = -61 + 16 + 81 = 36.
$$

Factor the trinomials and divide every term by $36$ to force the right-hand side to $1$:

$$
4(x - 2)^2 + 9(y + 3)^2 = 36,
$$

$$
\dfrac{(x - 2)^2}{9} + \dfrac{(y + 3)^2}{4} = 1.
$$

Now read the form. The center is $(2, -3)$, the larger denominator is $9$ under the $x$-term, so the major axis is horizontal with $a^2 = 9$ and $b^2 = 4$, giving $a = 3$ and $b = 2$. The vertices sit $3$ units left and right of the center, at $(-1, -3)$ and $(5, -3)$. The focal distance is $c = \sqrt{9 - 4} = \sqrt{5}$, so the foci are at $(2 - \sqrt{5},\; -3)$ and $(2 + \sqrt{5},\; -3)$.

---

## Common pitfalls

- **Swapping $a$ and $b$.** The convention is that $a$ is always the larger semi-axis, so $a^2$ is always the larger denominator. If you accidentally name the smaller one $a$, every computation of $c$ and every foci location will be wrong.
- **Using the wrong sign in $c^2 = a^2 - b^2$.** For an ellipse you subtract the smaller square from the larger. A [[Hyperbolas|hyperbola]] uses $c^2 = a^2 + b^2$ instead. Keep the two relations separate.
- **Forgetting to factor out the coefficients before completing the square.** When the general form has coefficients like $4x^2 + 9y^2$, you must factor the $4$ and the $9$ out of the $x$-group and $y$-group respectively before completing the square. Forgetting this is the most common scripted-problem error.
- **Placing foci off the major axis.** The foci always sit on the longer axis, inside the curve. They never land on the minor axis or outside the ellipse.

---

## Prerequisites

Before tackling practice problems, be solid on:

- [[Circles]] — the limiting case $a = b$ gives you a circle, and the algebra feels familiar
- [[Completing_The_Square]] — the bridge from general quadratic form to standard conic form
- [[Quadratic_Functions]] — comfort with squared terms and vertex-style rewriting

---

## Problems Involving Ellipses

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="ellipses"></div>

---

## See Also

- [[Circles]] — the limiting case where the two foci merge into one center
- [[Parabolas]] — one focus and one line, instead of two foci
- [[Hyperbolas]] — two foci with a difference-of-distances rule
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
