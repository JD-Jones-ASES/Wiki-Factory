---
title: "Angles"
type: topic
aliases: ["Degrees and Radians", "Angle Measure", "Coterminal Angles", "Standard Position"]
tags: ["#branch-pre-calculus", "#topic-unit-circle"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.1"}
related:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/pre_algebra/Similar_Triangles"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
problem_type_ids: []
figures: []
summary: "Angles as rotations: degree versus radian measure, the conversion pi-over-180, standard position, and coterminal angles."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Angles

# Angles

In elementary geometry an angle is usually introduced as a static shape — "two rays sharing a common endpoint." That picture is fine as far as it goes, but trigonometry takes a different and more powerful view. In trig, an angle is a **rotation**: you start with a ray pointing one direction, then spin it about its endpoint until it points somewhere else. The amount of the spin is what the angle actually measures.

Thinking of angles as rotations immediately unlocks things the static picture cannot. You can spin in two directions — the counterclockwise spin is called **positive** and the clockwise one **negative**. You can also spin more than once all the way around, giving angles larger than a full revolution. All of that becomes important the instant you want to describe circular motion, periodic waves, or the behavior of the sine and cosine functions.

---

## Key ideas

**Two ways to measure a rotation.** A full trip around a circle can be labeled in two different units:

- In **degrees**, one complete revolution is split into $360$ equal parts. Each part is called a degree and written with a small circle: $360^\circ$. A quarter turn is $90^\circ$, a half turn is $180^\circ$, a three-quarter turn is $270^\circ$.
- In **radians**, one complete revolution is assigned the value $2\pi$. The symbol $\pi$ is roughly $3.14159\ldots$, the famous irrational number that shows up in every circle calculation. A quarter turn is $\pi/2$ radians, a half turn is $\pi$ radians, a three-quarter turn is $3\pi/2$ radians.

Degrees are the unit you grew up with. Radians are the unit that every higher math course — calculus, physics, engineering — eventually switches to, for a reason that will become clear only once you see why the derivative of $\sin x$ comes out cleanly as $\cos x$: that simple fact is only true when $x$ is a radian measurement. For now, think of degrees and radians as two different rulers for the same quantity, like inches and centimeters.

**The master conversion.** Because a half revolution equals both $180^\circ$ and $\pi$ radians, we get the fundamental identity:

$$
180^\circ = \pi \text{ rad}
$$

Divide by $180^\circ$ on both sides and you get the ratio $\dfrac{\pi}{180^\circ}$, a unit conversion that turns degrees into radians:

$$
d^\circ \cdot \frac{\pi}{180^\circ} = r \text{ rad}
$$

Flip the ratio upside down to go the other way:

$$
r \text{ rad} \cdot \frac{180^\circ}{\pi} = d^\circ
$$

A useful mental shortcut: "multiply by $\pi/180$ to push degrees into radians; multiply by $180/\pi$ to pull radians back out into degrees."

**Standard position.** When we draw an angle on the coordinate plane, we almost always pin it down in a particular way called **standard position**:

- The vertex of the angle sits at the origin $(0, 0)$.
- The **initial side** — the ray that the rotation starts from — lies along the positive $x$-axis.
- The **terminal side** — the ray that the rotation ends on — swings out to wherever the rotation carries it.

A positive angle rotates counterclockwise from the initial side; a negative angle rotates clockwise. Once an angle is in standard position, you can classify it by which quadrant its terminal side lands in (Quadrant I, II, III, or IV), or say it is a **quadrantal** angle if its terminal side lies exactly on one of the axes.

**Coterminal angles.** Here is a feature of the rotational picture that has no analogue in the static picture: several different angles can *look the same on paper*. An angle of $30^\circ$ and an angle of $390^\circ$ and an angle of $-330^\circ$ all have their terminal sides in the same place — the first one spins a small counterclockwise nudge, the second adds a full revolution on top, and the third spins backwards the "long way around." Angles that share a terminal side are called **coterminal**.

Two angles are coterminal precisely when they differ by an integer number of full revolutions:

- In degrees: add or subtract multiples of $360^\circ$.
- In radians: add or subtract multiples of $2\pi$.

So $\theta$ and $\theta + 360^\circ$ are coterminal, $\theta$ and $\theta - 720^\circ$ are coterminal, and so on forever in both directions.

---

## Example 1: converting from degrees to radians

> Express $45^\circ$ in radian measure.

Multiply by the conversion factor $\dfrac{\pi}{180^\circ}$. Writing the degrees as a fraction makes the cancellation visible:

$$
45^\circ \cdot \frac{\pi}{180^\circ} = \frac{45\pi}{180} \text{ rad}
$$

The degree symbols cancel. Simplify the fraction by noticing that $45$ and $180$ share a common factor of $45$:

$$
\frac{45\pi}{180} = \frac{\pi}{4}
$$

So $45^\circ = \dfrac{\pi}{4}$ radians. For comparison, $30^\circ$ comes out as $\pi/6$, $60^\circ$ comes out as $\pi/3$, and $90^\circ$ comes out as $\pi/2$. These four values — together with $\pi$ for $180^\circ$ and $2\pi$ for a full turn — are the ones you will see most often in a pre-calculus course, and the ones worth committing to memory.

---

## Example 2: converting from radians to degrees

> Convert $\dfrac{5\pi}{6}$ radians into degrees.

Now go the other direction. Multiply by $\dfrac{180^\circ}{\pi}$:

$$
\frac{5\pi}{6} \cdot \frac{180^\circ}{\pi} = \frac{5 \cdot 180^\circ}{6}
$$

The $\pi$ cancels. Simplify the fraction:

$$
\frac{5 \cdot 180^\circ}{6} = \frac{900^\circ}{6} = 150^\circ
$$

So $\dfrac{5\pi}{6}$ radians equals $150^\circ$. If you picture this in standard position, the terminal side lands in Quadrant II, thirty degrees shy of the negative $x$-axis.

---

## Example 3: finding coterminal angles

> Find one positive and one negative angle, both coterminal with $\theta = 110^\circ$.

To build a coterminal angle in degrees, just add or subtract a whole number of full revolutions — that is, multiples of $360^\circ$. You have infinitely many choices.

For a positive coterminal angle, add $360^\circ$ once:

$$
110^\circ + 360^\circ = 470^\circ
$$

That rotation spins through a complete circle and then keeps going an additional $110^\circ$, so it lands on the same terminal side as the original.

For a negative coterminal angle, subtract $360^\circ$ once:

$$
110^\circ - 360^\circ = -250^\circ
$$

A $-250^\circ$ rotation goes backward (clockwise) by $250^\circ$, which is $110^\circ$ past the negative $y$-axis in the clockwise direction — exactly the same resting position as a small counterclockwise $110^\circ$ spin. Picture them in your head: same final arrow, two very different journeys to get there.

If the problem had been stated in radians, the exact same process works — you just add or subtract $2\pi$ instead of $360^\circ$. An angle of $\pi/3$ is coterminal with $\pi/3 + 2\pi = 7\pi/3$ and with $\pi/3 - 2\pi = -5\pi/3$.

---

## Common pitfalls

- **Forgetting which direction the conversion factor runs.** Degrees to radians uses $\pi/180$; radians to degrees uses $180/\pi$. One quick way to remember: when your answer should be bigger (because a degree is a smaller unit than a radian), multiply by the larger factor.
- **Leaving a calculator in the wrong mode.** Calculators have a "degree mode" and a "radian mode," and the answers they produce are completely different. If your sine of a small angle comes out close to the angle itself, you're in radian mode. If it doesn't, you're in degree mode. Always check before you trust a number.
- **Mistaking coterminal for equal.** Coterminal angles share a terminal side, but they are not literally the same number. $30^\circ$ and $390^\circ$ are coterminal, not equal. The distinction matters once you start solving trig equations and counting solutions.
- **Dropping the $\pi$ when writing radian answers.** Radians without $\pi$ are real numbers too — angles like $2$ radians or $-0.5$ radians are perfectly meaningful — so don't automatically tack a $\pi$ on the end. Only include it when the algebra actually produces one.

---

## Prerequisites

Before you work through the practice set, make sure you are comfortable with:

- [[Plotting_Points_And_The_Coordinate_Plane]] — since standard position lives on the coordinate grid
- [[Triangle_Angle_Sum_And_Exterior_Angles]] — for the basic $180^\circ$ arithmetic that keeps coming back
- [[Circumference_And_Area_Of_Circles]] — where $\pi$ first shows up, and the reason a full revolution measures $2\pi$ radians

---

## Problems Involving Angles

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="angles"></div>

---

## See Also

- [[The_Unit_Circle]]
- [[Circular_Functions]]
- [[Graphs_Of_Trigonometric_Functions]]
- [[Similar_Triangles]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
