---
title: "The Dot Product"
type: topic
aliases: ["Dot Product", "Scalar Product"]
tags: ["#branch-pre-calculus", "#topic-vectors"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.1"}
related:
  - "topics/precalculus/Vectors"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Law_Of_Cosines"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Vectors"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
problem_type_ids: []
figures: []
summary: "One number that captures the angle between two vectors — the bridge from raw components to geometry."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > The Dot Product

# The Dot Product

You already know how to add [[Vectors|vectors]], subtract them, and scale them by a number. What is missing from that list is a way to *multiply* two vectors together. There is actually more than one kind of vector product, but the easiest one — and the one that unlocks almost every practical question about angles and perpendicularity — is the **dot product**.

Given two vectors $\vec{u} = \langle u_1, u_2 \rangle$ and $\vec{v} = \langle v_1, v_2 \rangle$, the dot product is defined by

$$
\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2
$$

Multiply matching components, then add. The answer is just a single number — no brackets, no arrow on top. A pair of vectors goes in; one plain real number comes out. That is the first thing to remember about the dot product: it squeezes two arrows down to one scalar.

---

## Two definitions, one operation

The strange and wonderful thing about the dot product is that the same number can be described in a completely different way. If $\theta$ is the angle between the two arrows, then you can also compute the dot product from the magnitudes and the cosine:

$$
\vec{u} \cdot \vec{v} = |\vec{u}| \, |\vec{v}| \cos\theta
$$

These two formulas — the **algebraic** version $u_1 v_1 + u_2 v_2$ and the **geometric** version $|\vec{u}| |\vec{v}| \cos\theta$ — always give the same answer, even though they look totally different. That double personality is the real point of the dot product. The first formula is how you *compute* the number when you have components. The second formula is how you *interpret* the number once you have it. Together they let you slide back and forth between raw arithmetic and real geometry.

Setting the two expressions equal and isolating the cosine gives the formula that everything else in this lesson is built on:

$$
\cos\theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| \, |\vec{v}|}
$$

Once you can turn two vectors into a dot product and two magnitudes, you can read off the angle between them with a single $\arccos$.

---

## What it is good for

Three applications show up constantly:

- **Finding the angle between two vectors.** Compute the dot product, divide by the product of the magnitudes, take an inverse cosine. Done.
- **Testing perpendicularity.** Suppose the angle is exactly $90°$. Then $\cos 90° = 0$, so the geometric formula collapses to $\vec{u} \cdot \vec{v} = 0$. This gives a clean test: two nonzero vectors meet at a right angle exactly when their dot product vanishes. No drawing, no protractor — just arithmetic on four numbers.
- **Projecting one vector onto another.** The dot product also measures how much of $\vec{u}$ points in the same direction as $\vec{v}$, which is the first step in resolving forces and decomposing motion.

---

## Example 1: An algebraic warm-up

> Compute $\vec{u} \cdot \vec{v}$ for $\vec{u} = \langle 3, 4 \rangle$ and $\vec{v} = \langle 2, -1 \rangle$.

Multiply matching slots and add:

$$
\vec{u} \cdot \vec{v} = (3)(2) + (4)(-1) = 6 - 4 = 2
$$

That is the entire calculation — one line. The answer is a plain number, not a vector. The fact that this scalar equals $2$ does not yet tell you much by itself; the meaning only emerges once you pair it with the magnitudes, which is what the next example does.

---

## Example 2: Finding the angle between two vectors

> Find the angle $\theta$ between $\vec{u} = \langle 1, 2 \rangle$ and $\vec{v} = \langle 4, 3 \rangle$.

Start with the dot product:

$$
\vec{u} \cdot \vec{v} = (1)(4) + (2)(3) = 4 + 6 = 10
$$

Next the two magnitudes:

$$
|\vec{u}| = \sqrt{1^2 + 2^2} = \sqrt{5} \qquad |\vec{v}| = \sqrt{4^2 + 3^2} = \sqrt{25} = 5
$$

Plug into the angle formula:

$$
\cos\theta = \frac{10}{\sqrt{5} \cdot 5} = \frac{10}{5\sqrt{5}} = \frac{2}{\sqrt{5}}
$$

Take the inverse cosine: $\theta = \arccos(2/\sqrt{5}) \approx \arccos(0.894) \approx 26.57°$. The two arrows point in roughly the same direction — less than a $30°$ spread — which fits a geometric sketch: both sit in Quadrant I, and $\vec{v}$ is only a little more horizontal than $\vec{u}$.

---

## Example 3: A perpendicularity test

> Are the vectors $\vec{u} = \langle 2, 3 \rangle$ and $\vec{v} = \langle 6, -4 \rangle$ perpendicular?

Skip the angle computation and go straight to the dot product:

$$
\vec{u} \cdot \vec{v} = (2)(6) + (3)(-4) = 12 - 12 = 0
$$

The dot product came out to exactly zero, and since both vectors are nonzero, that means the angle between them must be $90°$. So yes, $\vec{u}$ and $\vec{v}$ are perpendicular. Notice how the whole check was three multiplications and one subtraction — no square roots, no inverse trig. This test is one of the most efficient tools in all of vector algebra, and it is the reason the dot product is worth learning even before you meet the angle formula.

A quick sanity check: $\vec{v}$ can be obtained from $\vec{u}$ by swapping the components and negating one of them (and scaling), which is exactly the recipe for building a vector perpendicular to a given one. Every pair of vectors related that way will pass the dot product test.

---

## Common pitfalls

- **Treating the result as a vector.** The dot product answer is a single number, not a vector. Writing $\vec{u} \cdot \vec{v} = \langle 6, -4 \rangle$ is a sign that something went wrong — you were probably still in componentwise-multiplication mode instead of summing at the end.
- **Swapping cosine and sine.** The geometric formula uses $\cos\theta$, not $\sin\theta$. If you use sine by mistake, you get a different quantity called the magnitude of the cross product, which is a different tool entirely.
- **Dividing by the dot product instead of the magnitudes.** In $\cos\theta = \dfrac{\vec{u} \cdot \vec{v}}{|\vec{u}||\vec{v}|}$, the dot product sits on top, not the bottom. Keeping the structure straight matters; the fractions are easy to invert by accident.
- **Forgetting to take $\arccos$.** After computing $\dfrac{\vec{u} \cdot \vec{v}}{|\vec{u}||\vec{v}|}$, that ratio is the *cosine* of the angle, not the angle itself. You still have to hit the inverse cosine key to read out $\theta$ in degrees or radians.

---

## Prerequisites

- [[Vectors]] — component form, magnitude, and addition are assumed throughout this page.
- [[The_Unit_Circle]] — all the angle calculations eventually lean on exact cosine values like $\cos 0° = 1$, $\cos 60° = 1/2$, and $\cos 90° = 0$.
- [[Circular_Functions]] — you will evaluate cosine and arccosine on arbitrary inputs, including negative values when the angle is obtuse.

---

## Problems Involving The Dot Product

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="dot_product"></div>

---

## See Also

- [[Vectors]] — the foundation this page rests on
- [[Law_Of_Cosines]] — another place cosine shows up in geometry problems
- [[The_Unit_Circle]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
