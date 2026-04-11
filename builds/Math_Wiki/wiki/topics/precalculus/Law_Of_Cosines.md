---
title: "The Law of Cosines"
type: topic
aliases: ["Law of Cosines", "SAS Triangle Solving", "SSS Triangle Solving"]
tags: ["#branch-pre-calculus", "#topic-laws-of-sines-and-cosines", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.3"}
related:
  - "topics/precalculus/Law_Of_Sines"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
problem_type_ids: []
figures: []
summary: "A Pythagorean-style relation that works for any triangle, letting you solve SSS and SAS cases in one step."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > The Law of Cosines

# The Law of Cosines

The [[Law_Of_Sines|Law of Sines]] is elegant, but it has one blind spot: it needs at least one angle-side opposite pair before it can get started. If a problem hands you three sides and no angles, or two sides and the angle sitting between them, the Law of Sines cannot set up its first equation. That is exactly the gap the **Law of Cosines** fills.

For any triangle, if you label the sides $a$, $b$, $c$ and the angles opposite those sides $A$, $B$, $C$ respectively, the Law of Cosines says:

$$
c^2 = a^2 + b^2 - 2ab\cos C
$$

Triangles have three sides, so the relationship shows up in three interchangeable flavors — one centered on each angle. Pick whichever version matches the side you want to find:

$$
a^2 = b^2 + c^2 - 2bc\cos A \qquad b^2 = a^2 + c^2 - 2ac\cos B \qquad c^2 = a^2 + b^2 - 2ab\cos C
$$

---

## The secret: it is Pythagoras in disguise

Look carefully at $c^2 = a^2 + b^2 - 2ab\cos C$ and imagine sliding the angle $C$ toward $90°$. What is $\cos 90°$? It is exactly $0$, so the final term collapses completely and the formula shrinks to

$$
c^2 = a^2 + b^2
$$

which is the [[The_Pythagorean_Theorem|Pythagorean theorem]] on the nose. The Law of Cosines is what the Pythagorean theorem looks like when you stop insisting on a right angle. Whenever $C$ is smaller than $90°$, the cosine is positive and the correction $-2ab\cos C$ makes $c$ a little shorter than Pythagoras would predict; whenever $C$ is larger than $90°$, the cosine is negative and $c$ gets longer. The formula is a single rule that smoothly handles acute, right, and obtuse triangles at the same time.

This is why you do not really have to memorize a new formula here. You already know Pythagoras; the Law of Cosines is the upgraded version that keeps track of the angle when it is not a clean $90°$.

---

## When to reach for it

There are exactly two triangle setups where the Law of Cosines is your starting move:

- **SAS — two sides and the angle between them.** You know, say, $a$, $b$, and $C$. Plug those three pieces into $c^2 = a^2 + b^2 - 2ab\cos C$ and solve directly for the missing side $c$.
- **SSS — all three sides, no angles.** Rearrange the formula to put the cosine on its own side: $\cos C = \dfrac{a^2 + b^2 - c^2}{2ab}$. Take an inverse cosine and you have an angle.

For the other classic setups — one side plus two angles (AAS or ASA), or the tricky two-sides-with-a-non-included-angle (SSA) — the Law of Sines is usually faster. A common workflow is to use the Law of Cosines once to crack the triangle open, then switch to the Law of Sines to mop up the remaining angles, which is almost always less arithmetic.

---

## Example 1: SAS — find the missing side

> Find the missing angles and sides of triangle $ABC$, given $a = 8$, $b = 5$, and $C = 60°$.

You know the two sides that meet at angle $C$, so the formula centered on $C$ is the right one:

$$
c^2 = a^2 + b^2 - 2ab\cos C
$$

Plug in the numbers:

$$
c^2 = 8^2 + 5^2 - 2(8)(5)\cos 60°
$$

Because $\cos 60° = \dfrac{1}{2}$, the final product simplifies cleanly:

$$
c^2 = 64 + 25 - 80 \cdot \tfrac{1}{2} = 89 - 40 = 49
$$

So $c = 7$. Now that you know every side, switching to the [[Law_Of_Sines|Law of Sines]] is the cleanest way to find $A$ and $B$: $\dfrac{\sin A}{8} = \dfrac{\sin 60°}{7}$ gives $\sin A = \dfrac{8 \sin 60°}{7} \approx 0.990$, so $A \approx 81.8°$. Then $B = 180° - 60° - 81.8° \approx 38.2°$.

---

## Example 2: SSS — find an angle from three sides

> Find the angle $C$ in a triangle with $a = 9$, $b = 12$, and $c = 15$.

Three sides, no angles, so solve the Law of Cosines for $\cos C$:

$$
\cos C = \frac{a^2 + b^2 - c^2}{2ab} = \frac{81 + 144 - 225}{2(9)(12)} = \frac{0}{216} = 0
$$

Since the cosine of $C$ works out to exactly $0$, the angle is $C = 90°$. That is not an accident: $9$, $12$, $15$ is a scaled-up $3$-$4$-$5$ Pythagorean triple, and the Law of Cosines recognizes the right angle immediately by zeroing out the cosine term.

---

## Example 3: A real-world distance

> Two hiking trails start at the same trailhead. One heads $3.2$ km in one direction and the other heads $4.5$ km in a direction making a $110°$ angle with the first. How far apart are the trail ends?

This is an SAS setup in disguise. Let the two known sides be $a = 3.2$ and $b = 4.5$, with included angle $C = 110°$, and let $c$ be the unknown distance between the endpoints:

$$
c^2 = 3.2^2 + 4.5^2 - 2(3.2)(4.5)\cos 110°
$$

Compute each piece: $3.2^2 = 10.24$, $4.5^2 = 20.25$, and $\cos 110° \approx -0.342$. The last term is $-2(3.2)(4.5)(-0.342) \approx 9.85$:

$$
c^2 \approx 10.24 + 20.25 + 9.85 = 40.34
$$

Then $c \approx \sqrt{40.34} \approx 6.35$ km. Notice that the cosine came out negative because the angle is obtuse, which flipped the sign of the correction term and made $c$ bigger than either of the two trail legs — exactly what you would expect when the trails bend away from each other.

---

## Common pitfalls

- **Mismatched angle and side.** The angle in the formula must be the one *opposite* the side you are solving for, or (for SAS) the one *between* the two sides you know. Lining up the wrong pair is the most common first-try mistake — sketch the triangle and label everything before you plug in.
- **Calculator mode.** If the problem uses degrees, your calculator must be in degree mode. Running $\cos 60°$ in radian mode gives the cosine of roughly $60$ radians and returns garbage.
- **Forgetting the $2ab$ factor.** It is easy to write $c^2 = a^2 + b^2 - \cos C$ or to drop the $2$. The coefficient is $-2ab$, multiplied by the cosine — keep all three pieces.
- **SSS with an impossible triangle.** If you compute $\cos C$ and get a value outside $[-1, 1]$, the three side lengths you were given cannot form a triangle at all. That is the Law of Cosines telling you the problem is inconsistent, not an arithmetic error to hunt down.

---

## Prerequisites

- [[The_Pythagorean_Theorem]] — the whole picture is just Pythagoras with a cosine correction, so you should be fluent with $a^2 + b^2 = c^2$ before coming here.
- [[The_Unit_Circle]] — you need to know the standard cosine values $\cos 30°$, $\cos 45°$, $\cos 60°$, $\cos 90°$, $\cos 120°$, and so on without hesitating.
- [[Circular_Functions]] — comfort with evaluating $\cos \theta$ for angles in any quadrant, including obtuse angles where the cosine goes negative.

---

## Problems Involving The Law of Cosines

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="law_of_cosines"></div>

---

## See Also

- [[Law_Of_Sines]] — the partner rule, better for AAS and ASA cases
- [[The_Pythagorean_Theorem]] — the $C = 90°$ special case
- [[The_Unit_Circle]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
