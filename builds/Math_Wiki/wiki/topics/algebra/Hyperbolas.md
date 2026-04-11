---
title: "Hyperbolas"
type: topic
aliases: ["Hyperbola", "Hyperbola Equation", "Hyperbola Asymptotes"]
tags: ["#branch-algebra-2", "#topic-conic-sections", "#key-topic"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "9", section: "9.4"}
  - {book: "algtrig", chapter: "10", section: "10.3"}
related:
  - "topics/geometry/Circles"
  - "topics/algebra/Parabolas"
  - "topics/algebra/Ellipses"
  - "topics/algebra/Completing_The_Square"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Ellipses"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: []
summary: "Two open branches defined by a fixed difference between distances to two foci; sketched with a reference rectangle and two asymptotes."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Hyperbolas

# Hyperbolas

A hyperbola looks nothing like the other conics. It is not a closed oval like an ellipse or a single cupped curve like a parabola. It is **two separate branches**, facing away from each other, each shaped like a bent arm opening outward. The branches never meet, and as they travel outward they hug a pair of straight lines called **asymptotes** without ever quite touching them. Sketching one cleanly is mostly a matter of drawing the right helper shapes first and then laying the branches in.

The distance rule is a cousin of the one that defines an ellipse, with one small but important change. An ellipse uses the **sum** of the two focal distances; a hyperbola uses the **absolute difference**. Fix two points $F_1$ and $F_2$ (the **foci**) and a positive distance $2a$. The set of points $(x, y)$ where

$$
\bigl|d_1 - d_2\bigr| = 2a
$$

traces out both branches at once: one branch for the points closer to $F_1$, the other for the points closer to $F_2$. The midpoint of the segment connecting the foci is the **center**. In practice this definition is what makes hyperbolas show up in hyperbolic navigation and sound-ranging: if two listeners hear the same signal, the time difference between them pins the source to one branch of a hyperbola whose foci are the two listener positions.

---

## Standard form

Centered at $(h, k)$ with a **horizontal transverse axis** — the axis through both vertices running left-to-right — a hyperbola has equation

$$
\dfrac{(x - h)^2}{a^2} - \dfrac{(y - k)^2}{b^2} = 1.
$$

Note the minus sign between the two terms. That single change, compared to the ellipse, swaps the shape from closed oval to two-branch split. The number $a > 0$ is the distance from the center to either **vertex** (the tip of each branch), and $b > 0$ is the half-height of the reference rectangle you use for sketching. The branches open left and right, and the two vertices sit at $(h - a,\; k)$ and $(h + a,\; k)$.

For a **vertical transverse axis**, the roles of $x$ and $y$ swap:

$$
\dfrac{(y - k)^2}{a^2} - \dfrac{(x - h)^2}{b^2} = 1.
$$

Now the branches open up and down, and the vertices sit at $(h,\; k - a)$ and $(h,\; k + a)$. An easy mnemonic: the variable whose term is **positive** (not subtracted) tells you which direction the branches open. If the $x$-term is positive, the branches face left and right; if the $y$-term is positive, the branches face up and down.

### The focal relation: PLUS, not minus

For a hyperbola the focal distance $c$ satisfies

$$
c^2 = a^2 + b^2.
$$

Compare this to the ellipse's $c^2 = a^2 - b^2$. The sign flip is the single most important thing to remember when you move between the two conics. On a hyperbola, $c > a$, which puts the two **foci outside** the vertices — farther from the center than the branches — while on an ellipse $c < a$ and the foci sit inside.

For a horizontal hyperbola the foci are at $(h - c,\; k)$ and $(h + c,\; k)$. For a vertical hyperbola they are at $(h,\; k - c)$ and $(h,\; k + c)$.

### Asymptotes and the reference rectangle

The cleanest way to sketch a hyperbola by hand is to draw its **reference rectangle** first. Starting at the center $(h, k)$, walk $a$ units along the transverse axis direction and $b$ units along the perpendicular direction. Mark those four points as corners of a rectangle. For a horizontal hyperbola the rectangle is $2a$ wide and $2b$ tall; for a vertical hyperbola it is $2b$ wide and $2a$ tall.

Now extend the two diagonals of the rectangle out in both directions. Those diagonal lines are the **asymptotes** — the straight lines the hyperbola approaches but never crosses. For a horizontal hyperbola centered at $(h, k)$, the asymptotes are

$$
y - k = \pm\dfrac{b}{a}(x - h),
$$

and for a vertical hyperbola they are

$$
y - k = \pm\dfrac{a}{b}(x - h).
$$

Once the asymptotes are drawn and the vertices are marked, sketch each branch starting at a vertex, curving outward, and bending toward the nearest asymptote as it runs off to infinity.

---

## Key ideas

- The defining rule is the **difference** of the two focal distances, not the sum. The hyperbola has two branches, and each branch sits closer to one focus than the other.
- The sign pattern is the quickest classifier. In the general equation $Ax^2 + Cy^2 + Dx + Ey + F = 0$, opposite signs on $A$ and $C$ mean a hyperbola; same signs mean a circle or an ellipse; only one squared term means a parabola.
- **Always draw the reference rectangle first** when sketching. The rectangle is what lets you place the asymptotes accurately, and the asymptotes are what tell you how steeply the branches open.
- The foci sit **outside** the curve, not inside. The eccentricity $e = c/a$ is greater than $1$ for every hyperbola, whereas ellipses have $e < 1$.

---

## Example 1: reading parts from standard form

> Determine the center, vertices, foci, and asymptotes of $\dfrac{(x - 2)^2}{9} - \dfrac{(y + 1)^2}{16} = 1$.

The $x$-term is positive and the $y$-term is subtracted, so this is a horizontal hyperbola with center $(2, -1)$. From the denominators, $a^2 = 9$ and $b^2 = 16$:

$$
a = 3, \qquad b = 4, \qquad c = \sqrt{9 + 16} = \sqrt{25} = 5.
$$

Walk $a = 3$ units left and right of the center for the vertices and $c = 5$ units left and right for the foci.

- **Vertices:** $(2 - 3,\; -1) = (-1, -1)$ and $(2 + 3,\; -1) = (5, -1)$.
- **Foci:** $(2 - 5,\; -1) = (-3, -1)$ and $(2 + 5,\; -1) = (7, -1)$.
- **Asymptotes:** $y + 1 = \pm\dfrac{4}{3}(x - 2)$.

To sketch it: draw the $6 \times 8$ reference rectangle centered at $(2, -1)$, extend the diagonals outward to get the asymptote lines, then curve two branches through the vertices opening left and right.

---

## Example 2: building the equation from geometric data

> Write an equation for the hyperbola with foci $(0, -7)$ and $(0, 7)$ and vertices $(0, -3)$ and $(0, 3)$.

The foci and vertices both lie on the $y$-axis, so the transverse axis is **vertical** and the center is the midpoint of the foci, which is the origin $(0, 0)$. The vertices are $3$ units above and below the center, so $a = 3$ and $a^2 = 9$. The foci are $7$ units above and below, so $c = 7$ and $c^2 = 49$. Use the hyperbola relation:

$$
b^2 = c^2 - a^2 = 49 - 9 = 40.
$$

Plug into the vertical-transverse form:

$$
\dfrac{y^2}{9} - \dfrac{x^2}{40} = 1.
$$

Check the asymptotes: they are $y = \pm\dfrac{a}{b}x = \pm\dfrac{3}{\sqrt{40}}x$, which run fairly shallowly because $b$ is much larger than $a$. That matches the geometric picture — vertices close to the center, foci much farther out, and asymptotes spreading wide.

---

## Example 3: completing the square

> Convert $16x^2 - 9y^2 + 64x + 18y + 199 = 0$ to standard form, and give the center, vertices, and foci.

Group the $x$-terms and the $y$-terms, then factor out the squared-variable coefficients. Watch the sign: $-9y^2$ factors out a $-9$, which flips the sign inside the $y$-parentheses.

$$
16(x^2 + 4x) - 9(y^2 - 2y) = -199.
$$

Complete the square inside each group. Half of $4$ is $2$ (squared: $4$); half of $-2$ is $-1$ (squared: $1$). Anything added inside the $x$-parentheses gets multiplied by $16$ on its way out, and anything added inside the $y$-parentheses gets multiplied by $-9$:

$$
16(x^2 + 4x + 4) - 9(y^2 - 2y + 1) = -199 + 64 - 9 = -144.
$$

Factor and divide every term by $-144$. Dividing by a negative flips the signs and swaps which term is positive, which is how you know this is a **vertical** hyperbola:

$$
16(x + 2)^2 - 9(y - 1)^2 = -144,
$$

$$
\dfrac{(y - 1)^2}{16} - \dfrac{(x + 2)^2}{9} = 1.
$$

Now read the form. The center is $(-2, 1)$, the positive term is the $y$-term so the transverse axis is vertical, and $a^2 = 16$ and $b^2 = 9$, giving $a = 4$ and $b = 3$. The focal distance is $c = \sqrt{16 + 9} = \sqrt{25} = 5$.

- **Vertices:** $(-2,\; 1 - 4) = (-2, -3)$ and $(-2,\; 1 + 4) = (-2, 5)$.
- **Foci:** $(-2,\; 1 - 5) = (-2, -4)$ and $(-2,\; 1 + 5) = (-2, 6)$.
- **Asymptotes:** $y - 1 = \pm\dfrac{4}{3}(x + 2)$.

---

## Common pitfalls

- **Using the ellipse sign for $c$.** A hyperbola satisfies $c^2 = a^2 + b^2$ — both terms add. If you accidentally use $c^2 = a^2 - b^2$ (the ellipse version), you may get a negative number under the square root and think the problem is broken. Memorize the PLUS for hyperbolas.
- **Confusing which term is $a^2$.** In a hyperbola, $a^2$ is always the denominator of the **positive** (not subtracted) term, regardless of which number is larger. That is a break from the ellipse convention, where $a^2$ is always the larger denominator. For hyperbolas, size does not choose $a$ — the sign does.
- **Forgetting the reference rectangle.** A lot of hyperbola sketches look wrong because the asymptotes are drawn in first, before the rectangle. The rectangle is what gives you the exact slopes $\pm b/a$; skipping it leads to mushy, tilted asymptotes.
- **Mixing up horizontal vs vertical asymptote slopes.** For a horizontal hyperbola the slopes are $\pm b/a$. For a vertical one they are $\pm a/b$. Draw the rectangle and read the diagonals; do not try to memorize which variable goes on top.

---

## Prerequisites

Before tackling practice problems, be comfortable with:

- [[Ellipses]] — the sum-of-distances cousin, with $c^2 = a^2 - b^2$. Knowing this relation inside out is what lets you catch the sign flip.
- [[Completing_The_Square]] — the same algebra you used for circles and ellipses, with extra care about factoring negatives out of the $y$-group.
- [[Linear_Functions]] — for comfort with the slope-intercept and point-slope form of the asymptote equations.

---

## Problems Involving Hyperbolas

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="hyperbolas"></div>

---

## See Also

- [[Ellipses]] — same two-foci idea, but with a sum-of-distances rule instead of a difference
- [[Parabolas]] — one focus and one directrix, the simplest conic
- [[Circles]] — the simplest closed conic and a warm-up for the algebra
- [[Completing_The_Square]] — the standard move for converting general form to standard form
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
