---
title: "The Unit Circle"
type: topic
aliases: ["Special Angles", "Unit Circle Values"]
tags: ["#branch-pre-calculus", "#topic-unit-circle", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.5"}
related:
  - "topics/precalculus/Angles"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Identities"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Angles"
  - "topics/precalculus/Circular_Functions"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
problem_type_ids: []
figures: ["precalculus/unit_circle.svg"]
summary: "The exact values of sine and cosine at the special angles, derived from 30-60-90 and 45-45-90 reference triangles and memorized via one diagram."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > The Unit Circle

# The Unit Circle

Once you know that $\cos\theta$ and $\sin\theta$ are just the coordinates of a point on a circle of radius $1$, a natural question follows: at which angles can you actually compute those coordinates by hand? Your calculator gives a decimal for every angle, but a decimal approximation is not the same as an exact value. For a handful of special angles — the ones built out of $\pi/6$, $\pi/4$, and $\pi/3$ — you can pin down sine and cosine to exact radical expressions using nothing more than the two most famous right triangles.

The **unit circle** you will memorize is a single diagram with those exact values marked at 16 key points. It is the single most useful picture in trigonometry, and it repays every minute you spend with it. Before you memorize the picture, you should see where the numbers come from.

$$
\text{At each special angle } \theta,\;\; (\cos\theta,\; \sin\theta) \text{ is an exact coordinate on } x^2 + y^2 = 1.
$$

![[unit_circle.svg|The unit circle with 16 special angles]]

---

## Building the values from reference triangles

### The 45-45-90 triangle gives $\theta = \pi/4$

An isosceles right triangle has two $45^{\circ}$ angles and one $90^{\circ}$ angle. If each leg has length $1$, the Pythagorean theorem gives a hypotenuse of $\sqrt{1^2 + 1^2} = \sqrt{2}$. The two legs are equal, so the opposite and adjacent sides measure the same. For a $45^{\circ}$ angle in this triangle:

$$
\cos(45^{\circ}) = \dfrac{\text{adjacent}}{\text{hypotenuse}} = \dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2}, \qquad \sin(45^{\circ}) = \dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2}.
$$

In radians $45^{\circ} = \pi/4$, and so $(\cos(\pi/4),\;\sin(\pi/4)) = (\sqrt{2}/2,\; \sqrt{2}/2)$. That point sits exactly halfway around the first quadrant on the unit circle.

### The 30-60-90 triangle gives $\theta = \pi/6$ and $\theta = \pi/3$

Start with an equilateral triangle of side length $2$ and drop an altitude from one vertex. That altitude cuts the base in half (giving a segment of length $1$) and creates two congruent right triangles with angles $30^{\circ}$, $60^{\circ}$, and $90^{\circ}$. The short leg has length $1$, the hypotenuse has length $2$, and by the Pythagorean theorem the long leg has length $\sqrt{2^2 - 1^2} = \sqrt{3}$.

Looking at the $30^{\circ}$ angle in this triangle, the side opposite it is the short leg (length $1$) and the side adjacent is the long leg (length $\sqrt{3}$). So:

$$
\cos(30^{\circ}) = \dfrac{\sqrt{3}}{2}, \qquad \sin(30^{\circ}) = \dfrac{1}{2}.
$$

For the $60^{\circ}$ angle the roles swap — the side opposite is the long leg, the side adjacent is the short leg — so:

$$
\cos(60^{\circ}) = \dfrac{1}{2}, \qquad \sin(60^{\circ}) = \dfrac{\sqrt{3}}{2}.
$$

In radians $30^{\circ} = \pi/6$ and $60^{\circ} = \pi/3$. The points $(\sqrt{3}/2,\; 1/2)$ and $(1/2,\; \sqrt{3}/2)$ are the unit-circle coordinates at those two angles. Notice how the values of sine and cosine swap — $\sin(\pi/6) = 1/2$ and $\cos(\pi/3) = 1/2$. This is no coincidence: $\pi/6$ and $\pi/3$ are complementary, and complementary angles always swap their sine and cosine values.

### The quadrantal angles

At the four angles where the terminal side lands on an axis, the point on the unit circle is obvious from the picture: $(1, 0)$ at $\theta = 0$, $(0, 1)$ at $\theta = \pi/2$, $(-1, 0)$ at $\theta = \pi$, and $(0, -1)$ at $\theta = 3\pi/2$. These are the "free" values you should be able to recite without thinking.

---

## The full first quadrant

Putting the special angles together, the first quadrant of the unit circle contains five points in order from the positive $x$-axis to the positive $y$-axis:

| $\theta$ | $(\cos\theta, \sin\theta)$ |
|---|---|
| $0$ | $(1,\; 0)$ |
| $\pi/6$ | $(\sqrt{3}/2,\; 1/2)$ |
| $\pi/4$ | $(\sqrt{2}/2,\; \sqrt{2}/2)$ |
| $\pi/3$ | $(1/2,\; \sqrt{3}/2)$ |
| $\pi/2$ | $(0,\; 1)$ |

Watch the cosine column walk from $1$ down to $0$ and the sine column walk from $0$ up to $1$. That monotone march is a useful sanity check — if your memorized value ever disagrees with that pattern, something went wrong.

---

## Reflecting into the other three quadrants

The second, third, and fourth quadrants do not require new values. Every special angle outside quadrant I is a reflection of one of the five first-quadrant angles, and the magnitudes of sine and cosine stay the same under reflection — only the signs change.

The angle between the terminal side and the $x$-axis is called the **reference angle**. For any non-quadrantal angle $\theta$, the reference angle $\theta'$ is acute, and the absolute values of $\cos\theta$ and $\sin\theta$ match the first-quadrant values at $\theta'$. The quadrant of $\theta$ then supplies the correct signs.

A quick way to keep the signs straight: cosine is the $x$-coordinate, so cosine is positive wherever $x > 0$ (quadrants I and IV) and negative wherever $x < 0$ (quadrants II and III). Sine is the $y$-coordinate, so sine is positive wherever $y > 0$ (quadrants I and II) and negative wherever $y < 0$ (quadrants III and IV). A common mnemonic arranges the four quadrants by which of sine, cosine, and tangent are positive: all three in the first quadrant, sine only in the second, tangent only in the third, cosine only in the fourth — a rotation around the plane you can memorize in about a minute.

---

## Key ideas

- **Five first-quadrant values.** Memorize the table above. Every other special-angle value comes from reflecting these five.
- **Reference angle + sign chart.** For any special angle, the reference angle gives the magnitude of sine and cosine; the quadrant gives the sign.
- **Complementary-angle swap.** Angles $\theta$ and $\pi/2 - \theta$ swap sine and cosine: $\sin(\pi/6) = 1/2 = \cos(\pi/3)$, and $\sin(\pi/3) = \sqrt{3}/2 = \cos(\pi/6)$.
- **The unit circle fits the Pythagorean identity.** Every point you list must satisfy $x^2 + y^2 = 1$. Checking this is a fast way to verify your memory: $\left(\sqrt{3}/2\right)^2 + \left(1/2\right)^2 = 3/4 + 1/4 = 1$.
- **Radian measure lives everywhere here.** The special angles appear as fractions of $\pi$, not as degree values, because nearly all of calculus and beyond uses radians.

---

## Example 1: Reading off sine and cosine of $5\pi/6$

> Find $\cos(5\pi/6)$ and $\sin(5\pi/6)$.

Locate the angle. In radians, $5\pi/6$ is a little more than halfway around the second quadrant — specifically, it is $\pi$ minus $\pi/6$. That means its reference angle is $\pi/6$, and its terminal side lands in the second quadrant.

The first-quadrant values at $\pi/6$ are $\cos(\pi/6) = \sqrt{3}/2$ and $\sin(\pi/6) = 1/2$. Now apply the quadrant II sign rule: cosine is negative (because $x < 0$) and sine is positive (because $y > 0$). So:

$$
\cos\!\left(\dfrac{5\pi}{6}\right) = -\dfrac{\sqrt{3}}{2}, \qquad \sin\!\left(\dfrac{5\pi}{6}\right) = \dfrac{1}{2}.
$$

No new work, just a sign flip on the cosine.

---

## Example 2: Handling a negative angle with $-\pi/3$

> Find $\cos(-\pi/3)$ and $\sin(-\pi/3)$.

A negative angle rotates clockwise from the positive $x$-axis. Rotating $\pi/3$ clockwise lands the terminal side in the fourth quadrant, with reference angle $\pi/3$.

The first-quadrant values at $\pi/3$ are $\cos(\pi/3) = 1/2$ and $\sin(\pi/3) = \sqrt{3}/2$. In quadrant IV, cosine stays positive and sine flips to negative:

$$
\cos\!\left(-\dfrac{\pi}{3}\right) = \dfrac{1}{2}, \qquad \sin\!\left(-\dfrac{\pi}{3}\right) = -\dfrac{\sqrt{3}}{2}.
$$

This example also illustrates two symmetries worth noticing: cosine is even ($\cos(-\theta) = \cos\theta$) and sine is odd ($\sin(-\theta) = -\sin\theta$). You can see both facts land correctly here.

---

## Example 3: Finding every angle where $\cos\theta = 1/2$

> List every angle $\theta$ in $[0, 2\pi)$ with $\cos\theta = 1/2$.

Cosine equals $1/2$ at a first-quadrant angle whose reference angle you already know: $\pi/3$. Because cosine is the $x$-coordinate, a positive value of $1/2$ means $x > 0$, which happens in quadrants I and IV.

The quadrant I angle with reference angle $\pi/3$ is simply $\theta = \pi/3$ itself. The quadrant IV angle with the same reference angle is $\theta = 2\pi - \pi/3 = 5\pi/3$. So on $[0, 2\pi)$ the solutions are:

$$
\theta = \dfrac{\pi}{3} \quad \text{or} \quad \theta = \dfrac{5\pi}{3}.
$$

Any equation of the form $\cos\theta = k$ or $\sin\theta = k$ where $k$ is one of the standard values can be solved the same way: find the reference angle from the first quadrant, then use the sign of $k$ to pick the correct two quadrants, and write down the angle in each.

---

## Common pitfalls

- **Mixing up $\sin(\pi/6)$ and $\sin(\pi/3)$.** The small-numerator angle $\pi/6$ is near the $x$-axis, so its sine (the $y$-coordinate) is small: $1/2$. The larger-numerator angle $\pi/3$ is near the $y$-axis, so its sine is large: $\sqrt{3}/2$. If in doubt, visualize the triangle and ask which coordinate you're reading.
- **Writing $\sqrt{2}/2$ as $1/2$ or $1/\sqrt{2}$ inconsistently.** These are the same number, but most textbooks prefer the rationalized form $\sqrt{2}/2$. Pick one form and stick with it.
- **Confusing the reference angle with the angle itself.** The reference angle is always acute and always measured from the $x$-axis. For $\theta = 5\pi/6$, the reference angle is $\pi/6$, not $5\pi/6$.
- **Forgetting to apply the quadrant sign.** Taking the first-quadrant value and dropping it into a second-, third-, or fourth-quadrant slot unchanged is the number-one source of errors. Always do the sign check last.

---

## Prerequisites

- [[Circular_Functions]] — the definition of sine and cosine as unit-circle coordinates, which this page specializes to the exact values at special angles
- [[Angles]] — radian measure and standard position
- [[The_Pythagorean_Theorem]] — the engine behind both the 45-45-90 and 30-60-90 triangle calculations

---

## Problems Involving The Unit Circle

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_unit_circle"></div>

---

## See Also

- [[Circular_Functions]] — the general definition that these values fit into
- [[Identities]] — the Pythagorean identity, which every unit-circle point satisfies
- [[Graphs_Of_Trigonometric_Functions]] — where these values become sample points on a wave
- [[Inverse_Trigonometric_Functions]] — using unit-circle values to evaluate arcsin, arccos, arctan
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
</content>
