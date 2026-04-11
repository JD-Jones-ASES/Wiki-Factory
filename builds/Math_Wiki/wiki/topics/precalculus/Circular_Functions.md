---
title: "Circular Functions"
type: topic
aliases: ["Unit Circle Definition of Trig", "Trig Functions on the Unit Circle"]
tags: ["#branch-pre-calculus", "#topic-unit-circle"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.3"}
related:
  - "topics/precalculus/Angles"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Identities"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Angles"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Similar_Triangles"
problem_type_ids: []
figures: ["precalculus/right_triangle_soh_cah_toa.svg"]
summary: "Sine and cosine of any angle, defined as the coordinates of a point on the unit circle — extending right-triangle trig to every real angle."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Circular Functions

# Circular Functions

Right-triangle trigonometry works beautifully for acute angles. A leg over the hypotenuse gives you sine, an adjacent leg over the hypotenuse gives you cosine, and those ratios are perfectly behaved between $0^{\circ}$ and $90^{\circ}$. But the moment you want the cosine of $150^{\circ}$, or $-30^{\circ}$, or $5\pi/4$, the triangle picture falls apart. There is no such thing as a right triangle with a $150^{\circ}$ interior angle. Something has to take the triangle's place.

The replacement is the **unit circle**. Think of any angle $\theta$, drawn in standard position (vertex at the origin, initial ray along the positive $x$-axis). Rotate the other ray by $\theta$ — counter-clockwise for positive angles, clockwise for negative ones — until you land on its terminal side. Now find the one point where that terminal side crosses the circle of radius $1$ centered at the origin. Call that intersection point $P = (x, y)$. Then the **circular function** definitions say:

$$
\cos\theta = x, \qquad \sin\theta = y.
$$

That is the whole idea. Cosine is the horizontal coordinate of the point on the unit circle. Sine is the vertical coordinate. Every question about trig at a general angle eventually reduces to locating a point on a circle.

---

## Why this generalizes right-triangle trig

For an acute angle drawn in standard position, the terminal side lands somewhere in the first quadrant. Drop a vertical segment from $P$ to the $x$-axis, and you have built a right triangle with hypotenuse $1$, horizontal leg $x$, and vertical leg $y$. The opposite-over-hypotenuse definition of sine gives $y/1 = y$, and the adjacent-over-hypotenuse definition of cosine gives $x/1 = x$. Same answer. The unit-circle rule agrees with the triangle rule wherever the triangle rule makes sense, then keeps working where it doesn't.

![[right_triangle_soh_cah_toa.svg|SOH-CAH-TOA on a 3-4-5 triangle]]

Once you are comfortable with acute angles, the rule extends to every other angle for free. An angle of $150^{\circ}$ puts the terminal side in the second quadrant, so $x$ is negative and $y$ is positive — meaning $\cos(150^{\circ}) < 0$ and $\sin(150^{\circ}) > 0$. An angle of $-30^{\circ}$ puts it just below the $x$-axis in the fourth quadrant, so $x > 0$ and $y < 0$. Nothing about the definition changes; only the location of $P$ on the circle changes.

---

## The other four functions

Once you have sine and cosine, the remaining four circular functions are built from them by division:

$$
\tan\theta = \dfrac{\sin\theta}{\cos\theta}, \qquad \cot\theta = \dfrac{\cos\theta}{\sin\theta},
$$

$$
\sec\theta = \dfrac{1}{\cos\theta}, \qquad \csc\theta = \dfrac{1}{\sin\theta}.
$$

Each of these quotient definitions carries a restriction: division by zero is forbidden. Tangent and secant are undefined wherever $\cos\theta = 0$, which happens at $\theta = \pi/2 + k\pi$ for any integer $k$. Cotangent and cosecant are undefined wherever $\sin\theta = 0$, which happens at $\theta = k\pi$. These gaps will later become the vertical asymptotes of the tangent, cotangent, secant, and cosecant graphs on the [[Graphs_Of_Trigonometric_Functions]] page.

---

## Key ideas

- **Definition in one line.** For $\theta$ in standard position, let $(x, y)$ be the point where its terminal side meets the unit circle. Then $\cos\theta = x$ and $\sin\theta = y$.
- **Quadrant signs.** The sign of cosine follows the sign of $x$; the sign of sine follows the sign of $y$. So $\cos$ is positive in quadrants I and IV, negative in II and III; $\sin$ is positive in quadrants I and II, negative in III and IV.
- **Values are bounded.** Because every point on the unit circle has $-1 \leq x \leq 1$ and $-1 \leq y \leq 1$, the outputs of sine and cosine never escape the interval $[-1, 1]$. This is why equations like $\sin\theta = 2$ have no solutions.
- **Pythagorean identity.** The point $(x, y)$ sits on the circle $x^2 + y^2 = 1$, so substituting gives $\sin^2\theta + \cos^2\theta = 1$. This single equation is the backbone of most trig simplification work later.
- **Periodicity.** Rotating by a full turn of $2\pi$ (or $360^{\circ}$) lands on the same point, so $\sin(\theta + 2\pi) = \sin\theta$ and $\cos(\theta + 2\pi) = \cos\theta$. Every circular function repeats.
- **Domains.** Sine and cosine accept every real number. Tangent and secant skip the $\cos\theta = 0$ angles; cotangent and cosecant skip the $\sin\theta = 0$ angles.

---

## Example 1: Reading off the six values at a quadrantal angle

> Compute all six circular functions of $\theta = \pi$.

An angle of $\pi$ radians is a half-turn counter-clockwise from the positive $x$-axis, landing the terminal side on the **negative** $x$-axis. The point where this ray meets the unit circle is $(-1, 0)$.

Straight from the definition: $\cos\pi = -1$ and $\sin\pi = 0$. Now build the other four:

$$
\tan\pi = \dfrac{\sin\pi}{\cos\pi} = \dfrac{0}{-1} = 0, \qquad \sec\pi = \dfrac{1}{\cos\pi} = -1.
$$

The remaining two involve division by $\sin\pi = 0$, so they are undefined:

$$
\cot\pi \text{ is undefined,} \qquad \csc\pi \text{ is undefined.}
$$

Being undefined is not the same as equaling zero. Say it out loud when it happens, so you don't silently write something false.

---

## Example 2: Recovering sine and cosine from a non-unit radius

> An angle $\theta$ in standard position has terminal side passing through the point $Q = (3, -4)$. Find $\cos\theta$ and $\sin\theta$.

The point $(3, -4)$ is not on the unit circle — its distance from the origin is $\sqrt{3^2 + (-4)^2} = \sqrt{25} = 5$. To use the circular-function definition, scale the point down to the unit circle by dividing both coordinates by that distance:

$$
P = \left(\dfrac{3}{5},\; \dfrac{-4}{5}\right).
$$

That scaled point is where the same terminal side meets the unit circle. So $\cos\theta = 3/5$ and $\sin\theta = -4/5$. Note the quadrant: $x > 0$ and $y < 0$ puts the terminal side in quadrant IV, and the signs of cosine and sine match that quadrant's pattern.

This trick generalizes. If the terminal side contains $(a, b)$ with $r = \sqrt{a^2 + b^2}$, then $\cos\theta = a/r$ and $\sin\theta = b/r$. When $r = 1$, it collapses back to the unit-circle rule.

---

## Example 3: Using the Pythagorean identity to finish a value

> Suppose $\theta$ is a quadrant II angle with $\sin\theta = 3/5$. Find $\cos\theta$.

Plug into $\sin^2\theta + \cos^2\theta = 1$:

$$
\left(\dfrac{3}{5}\right)^2 + \cos^2\theta = 1 \quad\Longrightarrow\quad \cos^2\theta = 1 - \dfrac{9}{25} = \dfrac{16}{25}.
$$

Taking the square root gives $\cos\theta = \pm 4/5$, and now the quadrant information pins down the sign. In quadrant II the $x$-coordinate is negative, so cosine is negative:

$$
\cos\theta = -\dfrac{4}{5}.
$$

Never skip the quadrant check. The Pythagorean identity alone only gives you the magnitude; the sign comes from where the terminal side lives.

---

## Common pitfalls

- **Treating the radius as $1$ when it isn't.** If a problem hands you a point like $(3, -4)$ on the terminal side, you must divide by $r = \sqrt{a^2 + b^2}$ before reading off cosine and sine.
- **Forgetting which coordinate is which.** Cosine is the horizontal coordinate and sine is the vertical one. The mnemonic "$\cos$ comes before $\sin$ alphabetically, and $x$ comes before $y$" is an easy way to keep them straight.
- **Calling an undefined value zero.** When the denominator in $\tan$, $\cot$, $\sec$, or $\csc$ hits zero, the function is undefined at that angle — not zero. Watch the specific angle you are evaluating.
- **Missing the sign flip across quadrants.** The Pythagorean identity only fixes the square of each value. The quadrant fixes the sign.

---

## Prerequisites

- [[Angles]] — standard position, radians, and coterminal angles, because the definition starts with "draw the angle in standard position"
- [[The_Pythagorean_Theorem]] — the unit circle equation $x^2 + y^2 = 1$ is just Pythagoras with hypotenuse $1$, and so is the identity $\sin^2\theta + \cos^2\theta = 1$
- [[Similar_Triangles]] — the trick of scaling any point on the terminal side down to the unit circle uses similar-triangle reasoning

---

## Problems Involving Circular Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="circular_functions"></div>

---

## See Also

- [[The_Unit_Circle]] — the exact values of sine and cosine at the special angles
- [[Graphs_Of_Trigonometric_Functions]] — what these functions look like plotted across the real line
- [[Identities]] — the reciprocal, quotient, and Pythagorean identities in full
- [[Inverse_Trigonometric_Functions]] — undoing sine, cosine, and tangent
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
</content>
</invoke>