---
title: "Vectors"
type: topic
aliases: ["Vector", "2D Vectors", "Vectors in the Plane"]
tags: ["#branch-pre-calculus", "#topic-vectors"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.10"}
related:
  - "topics/precalculus/Dot_Product"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/The_Distance_Formula"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/The_Distance_Formula"
problem_type_ids: []
figures: ["precalculus/vector_addition.svg"]
summary: "A vector carries a length and a direction at the same time; its components are its horizontal and vertical shadows."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Vectors

# Vectors

A plain number like $60$ is great for tracking a quantity that only needs *how much*: sixty pounds, sixty dollars, sixty miles per hour on the highway. But there are plenty of real situations where *how much* is only half the story. A plane moving at $600$ mph heading due north ends up nowhere near a plane moving at $600$ mph heading due west. A rope pulling a sled at $50$ pounds of force does something different depending on whether you pull straight forward or straight up. These quantities carry two pieces of information at once: a **size** and a **direction**.

The mathematical object that packs both pieces into a single symbol is called a **vector**. On paper we draw it as an arrow: the length of the arrow stands for the size, and the way the arrow points stands for the direction. Whenever you see the notation $\vec{v}$, think "arrow."

## Component form

An arrow floating in space is a nice picture, but it is hard to do arithmetic with. To make vectors computable, we park them in the coordinate plane and describe each one by how far it runs horizontally and how far it runs vertically. These two numbers are called the **components** of the vector:

$$
\vec{v} = \langle v_1, v_2 \rangle
$$

The first number $v_1$ is the horizontal component (how far the arrow moves right, or left if negative). The second number $v_2$ is the vertical component (how far it moves up, or down if negative). The angle brackets $\langle \; \rangle$ are used instead of parentheses so you can tell a vector apart from a point at a glance.

If an arrow starts at the point $P(x_0, y_0)$ and ends at the point $Q(x_1, y_1)$, the component form is simply end minus start:

$$
\vec{v} = \langle x_1 - x_0, \; y_1 - y_0 \rangle
$$

Notice that this is the exact same subtraction the [[The_Distance_Formula|distance formula]] does behind the scenes — the difference is that here we keep the two numbers separate instead of squaring and adding them.

---

## The three core operations

Three operations turn vectors into a full algebra. All of them work componentwise, which is the real payoff of using coordinates in the first place.

**Addition.** To add two vectors, add the horizontals and add the verticals:

$$
\vec{u} + \vec{v} = \langle u_1 + v_1, \; u_2 + v_2 \rangle
$$

Geometrically this is **head to tail**: drop the tail of $\vec{v}$ on top of the head of $\vec{u}$, and the arrow from the very start to the very end is the sum. Subtraction works the same way: $\vec{u} - \vec{v} = \langle u_1 - v_1, u_2 - v_2 \rangle$.

![[vector_addition.svg|Vector addition by the head-to-tail rule]]

**Scalar multiplication.** To stretch or shrink a vector by a real number $c$, multiply both components by $c$:

$$
c\vec{v} = \langle c v_1, \; c v_2 \rangle
$$

If $c$ is positive the arrow keeps pointing the same direction but changes length. If $c$ is negative, the arrow reverses. If $|c| > 1$ the arrow grows; if $|c| < 1$ the arrow shrinks.

**Magnitude.** The length of the arrow is exactly what the [[The_Pythagorean_Theorem|Pythagorean theorem]] gives you when you treat the components as the two legs of a right triangle:

$$
|\vec{v}| = \sqrt{v_1^2 + v_2^2}
$$

Some books write $\|\vec{v}\|$ with double bars. Either notation means the same thing: a non-negative real number that measures size.

---

## Direction: the angle the arrow makes

Magnitude is only half of the description. The other half is the angle $\theta$ the arrow makes with the positive $x$-axis. Once you have the components, you recover the angle from

$$
\theta = \arctan\!\left(\frac{v_2}{v_1}\right)
$$

The big warning here is that $\arctan$ by itself always lands in the range $(-90°, 90°)$, so it cannot distinguish a vector in Quadrant II from one in Quadrant IV — both come back with a negative raw angle. After computing $\arctan$, sketch the vector, look at which quadrant it sits in, and adjust by adding $180°$ when needed. This is the same quadrant-checking habit you developed with [[The_Unit_Circle|the unit circle]], applied to vectors.

---

## Polar to rectangular: going the other way

Often a problem gives you the magnitude and the angle instead of the components — a force of $20$ newtons at $30°$ above the horizontal, or a boat moving at $12$ mph on a heading of $45°$. To recover the components, read them straight off a right triangle:

$$
\vec{v} = \langle r\cos\theta, \; r\sin\theta \rangle
$$

where $r = |\vec{v}|$ is the magnitude. The horizontal component is $r\cos\theta$, and the vertical component is $r\sin\theta$. This conversion is the bridge between physical descriptions ("$20$ newtons at $30°$") and the componentwise arithmetic that actually computes things.

---

## Example 1: Build the vector, then find its size and direction

> A vector runs from $P(1, 2)$ to $Q(5, 5)$. Write it in component form, find its magnitude, and find the angle it makes with the positive $x$-axis.

Subtract end from start to get the components:

$$
\vec{v} = \langle 5 - 1, \; 5 - 2 \rangle = \langle 4, 3 \rangle
$$

The magnitude is a classic $3$-$4$-$5$ right triangle:

$$
|\vec{v}| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5
$$

The angle is $\theta = \arctan(3/4) \approx 36.87°$. Both components are positive, so the arrow sits in Quadrant I and the raw $\arctan$ answer is already correct — no quadrant fix needed.

---

## Example 2: Adding and scaling

> Let $\vec{u} = \langle 2, -3 \rangle$ and $\vec{v} = \langle -1, 5 \rangle$. Compute $3\vec{u} + 2\vec{v}$.

First scale each vector, then add componentwise:

$$
3\vec{u} = \langle 6, -9 \rangle \qquad 2\vec{v} = \langle -2, 10 \rangle
$$

$$
3\vec{u} + 2\vec{v} = \langle 6 + (-2), \; -9 + 10 \rangle = \langle 4, 1 \rangle
$$

The arithmetic is plain integer work on each slot. That is the whole point of component form: once vectors live in coordinates, every operation collapses into ordinary algebra on two numbers at a time.

---

## Example 3: From magnitude and angle to components

> A force of $20$ newtons is applied at an angle of $60°$ above the horizontal. Write the force as a vector in component form.

Use the polar-to-rectangular formulas with $r = 20$ and $\theta = 60°$:

$$
\vec{F} = \langle 20\cos 60°, \; 20\sin 60° \rangle
$$

From the unit circle, $\cos 60° = \dfrac{1}{2}$ and $\sin 60° = \dfrac{\sqrt{3}}{2}$:

$$
\vec{F} = \langle 20 \cdot \tfrac{1}{2}, \; 20 \cdot \tfrac{\sqrt{3}}{2} \rangle = \langle 10, \; 10\sqrt{3} \rangle
$$

As a decimal that is about $\langle 10, 17.32 \rangle$ newtons. The horizontal "push" part of the force is $10$ newtons and the vertical "lift" part is about $17.32$ newtons. Splitting a force like this into horizontal and vertical pieces is the first move in almost every physics problem — once you have the components, you can add the force to any other force acting on the object using plain componentwise addition.

---

## Why vectors matter

Vectors appear in almost every field that uses applied math:

- **Velocity.** A moving object has a speed (size) and a direction of travel. Wind, currents, and headings are all vector sums.
- **Force.** A pushing, pulling, or gravitational force has a size and a direction. Two forces on the same object combine as a vector sum.
- **Displacement.** Moving from point $A$ to point $B$ is captured by the vector $\overrightarrow{AB}$, exactly the end-minus-start formula above.

Every one of those applications ends up looking like "break the physical thing into horizontal and vertical components, do componentwise arithmetic, then convert back." The notation is designed to make that loop as painless as possible.

---

## Common pitfalls

- **Using parentheses instead of angle brackets.** The point $(3, 4)$ and the vector $\langle 3, 4 \rangle$ are different objects — the point is a fixed location, the vector is an arrow. Keep the notation consistent so your work is readable.
- **Ignoring quadrant when computing direction.** $\arctan$ only covers half the circle. If the vector sits in Quadrant II or Quadrant III, add $180°$ to the raw calculator answer.
- **Forgetting to scale both components.** In $3\vec{v}$, the factor $3$ hits $v_1$ *and* $v_2$. Scaling only one slot is a very common slip.
- **Mixing up magnitude and components.** $|\vec{v}|$ is one non-negative number. The components $v_1, v_2$ are two signed numbers. They are not interchangeable — the magnitude is the answer to "how long?", not "where is it pointing?"
- **Subtracting in the wrong order for $\overrightarrow{PQ}$.** It is end minus start, not start minus end. Getting this backward flips every sign in the components and sends the arrow the wrong way.

---

## Prerequisites

- [[The_Pythagorean_Theorem]] — every magnitude calculation is a Pythagorean theorem application, so you should be fluent with $a^2 + b^2 = c^2$.
- [[The_Distance_Formula]] — the exact same subtraction-then-Pythagoras pattern, just packaged a little differently. If distances on a grid make sense, vectors will too.
- [[The_Unit_Circle]] — for converting between polar form (magnitude and angle) and rectangular form (components), you need fluent $\sin$ and $\cos$ values at the standard angles.
- [[Circular_Functions]] — you will evaluate sine, cosine, and arctan constantly, including at obtuse and negative angles.

---

## Problems Involving Vectors

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="vectors"></div>

---

## See Also

- [[Dot_Product]] — the key operation for measuring angles between vectors and testing perpendicularity
- [[The_Distance_Formula]] — the grid-distance cousin of vector magnitude
- [[The_Unit_Circle]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
