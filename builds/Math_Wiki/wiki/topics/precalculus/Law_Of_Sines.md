---
title: "The Law of Sines"
type: topic
aliases: ["Law of Sines", "LawOfSines", "Sine Rule"]
tags: ["#branch-pre-calculus", "#topic-laws-of-sines-and-cosines", "#key-topic", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.4"}
related:
  - "topics/precalculus/Law_Of_Cosines"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Angles"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Angles"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
problem_type_ids: []
figures: []
summary: "A proportion between sides and their opposite angles that solves any triangle — even the non-right ones — as long as you respect the ambiguous case."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > The Law of Sines

# The Law of Sines

Right-triangle trigonometry (SOH-CAH-TOA) handles the special case where one of the angles is exactly $90^{\circ}$. Most real triangles are not that cooperative. To solve an **oblique triangle** — any triangle that is not a right triangle — you need something stronger. The law of sines is the first of the two such tools. It says that in any triangle, the ratio of the sine of an angle to its opposite side is the same for all three angle-side pairs.

Let the angles be labeled $A$, $B$, $C$ and let $a$, $b$, $c$ be the sides opposite those angles (lower-case matches the opposite upper-case). Then:

$$
\dfrac{\sin A}{a} = \dfrac{\sin B}{b} = \dfrac{\sin C}{c}.
$$

Equivalently, flip the fractions:

$$
\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C}.
$$

Both versions say the same thing. Pick whichever puts your unknown on top when you solve, so the last step is a multiplication instead of a division.

---

## When to reach for the law of sines

The law of sines solves a triangle when you know **any angle together with its opposite side**, plus one more piece of information. There are two standard scenarios:

- **AAS or ASA** — you know two angles and any side. The third angle comes from the fact that the three angles add to $180^{\circ}$. Then the law of sines gives you the other two sides one at a time. This case always produces exactly one triangle.
- **SSA** — you know two sides and an angle opposite one of them. This case is trouble. Depending on the numbers, there may be zero triangles, exactly one triangle, or two different triangles that both fit the data. This is the **ambiguous case**, and it is the single hardest thing in this topic.

If instead you are given three sides (SSS) or two sides with the angle *between* them (SAS), the law of sines cannot start the job — no angle is paired with its opposite side. In those cases reach for [[Law_Of_Cosines]] first, then finish with the law of sines if you like.

---

## The ambiguous case: what SSA hides

Suppose you know an angle $A$, the side $a$ opposite it, and one of the other sides $b$. The question is whether a triangle with those measurements exists at all, and if so, how many. The cleanest way to think about it is this: imagine placing angle $A$ at one vertex and drawing side $b$ along one of its rays. Now swing side $a$ from the end of $b$ toward the other ray of $A$. Does it reach?

Let $h = b \sin A$ — that is the perpendicular distance from the free end of $b$ to the other ray. Three outcomes are possible:

- If $a < h$, side $a$ is too short to reach the opposite ray, and **no triangle exists**.
- If $a = h$, side $a$ just barely reaches. You get exactly **one triangle**, and it is a right triangle.
- If $h < a < b$, side $a$ can reach the opposite ray in *two* different places — one tilted toward $A$, one away. You get **two different triangles**, both valid.
- If $a \geq b$, side $a$ is long enough that swinging it meets the other ray in only one useful place. You get **one triangle**.

Applying the law of sines to an SSA problem and then forgetting this classification is how almost everyone loses points on their first oblique-triangle quiz.

---

## Example 1: ASA, the clean case

> In a triangle, $A = 40^{\circ}$, $B = 75^{\circ}$, and the side $c$ opposite $C$ measures $12$. Find the remaining angle and the other two sides.

First find the missing angle from the triangle-angle sum: $C = 180^{\circ} - 40^{\circ} - 75^{\circ} = 65^{\circ}$.

Now use the law of sines, lining up the known pair $(C, c) = (65^{\circ}, 12)$ with each unknown in turn. For side $a$ opposite $A$:

$$
\dfrac{a}{\sin A} = \dfrac{c}{\sin C} \quad\Longrightarrow\quad a = \dfrac{12 \sin 40^{\circ}}{\sin 65^{\circ}} \approx \dfrac{12 \cdot 0.6428}{0.9063} \approx 8.51.
$$

For side $b$ opposite $B$:

$$
b = \dfrac{12 \sin 75^{\circ}}{\sin 65^{\circ}} \approx \dfrac{12 \cdot 0.9659}{0.9063} \approx 12.79.
$$

Sanity check: the largest side should be opposite the largest angle, and it is — $B = 75^{\circ}$ is the largest angle and $b \approx 12.79$ is the longest side.

---

## Example 2: SSA with exactly one triangle (no ambiguity)

> A triangle has $A = 35^{\circ}$, $a = 20$, and $b = 15$. Find $B$.

Because $a > b$, the longer side sits opposite the larger angle — there is no ambiguity, only one triangle fits. Apply the law of sines:

$$
\dfrac{\sin B}{15} = \dfrac{\sin 35^{\circ}}{20} \quad\Longrightarrow\quad \sin B = \dfrac{15 \sin 35^{\circ}}{20} \approx 0.4302.
$$

Take the inverse sine: $B \approx 25.47^{\circ}$. The alternative $180^{\circ} - 25.47^{\circ} = 154.53^{\circ}$ would make the triangle's angles exceed $180^{\circ}$, so that second value is rejected.

---

## Example 3: SSA with zero, one, or two triangles

> For each set of data, decide how many triangles (if any) are possible: (i) $A = 42^{\circ}$, $a = 3$, $b = 10$; (ii) $A = 30^{\circ}$, $a = 5$, $b = 10$; (iii) $A = 30^{\circ}$, $a = 6$, $b = 10$.

Compute $h = b \sin A$ in each case and compare with $a$.

**(i)** $h = 10 \sin 42^{\circ} \approx 6.69$. Here $a = 3 < h$, so side $a$ cannot reach — **no triangle exists**.

**(ii)** $h = 10 \sin 30^{\circ} = 5$. Here $a = 5 = h$, so side $a$ just touches. **Exactly one triangle**, and it is right-angled at the foot of the perpendicular.

**(iii)** $h = 10 \sin 30^{\circ} = 5$. Here $5 < a = 6 < b = 10$, so side $a$ can reach in two different places. **Two triangles** both satisfy the given data. Applying the law of sines gives $\sin B = \dfrac{10 \sin 30^{\circ}}{6} \approx 0.833$, whose two candidate angles are $B_1 \approx 56.44^{\circ}$ and $B_2 = 180^{\circ} - 56.44^{\circ} \approx 123.56^{\circ}$. Both lead to valid triangles (each with a different $C$ and $c$).

---

## Common pitfalls

- **Forgetting the ambiguous case entirely.** If the problem is SSA, always compute $h = b \sin A$ and classify before trusting a single answer from $\arcsin$. The calculator only ever returns the acute candidate.
- **Losing the second solution.** When $\sin B$ comes out to a value like $0.833$, the two candidates are $\arcsin(0.833)$ and $180^{\circ} - \arcsin(0.833)$. Check *both* to see which ones produce valid triangles (the angle sum must stay under $180^{\circ}$).
- **Mismatched pairs.** The law of sines couples each angle with its *opposite* side. Lining up $A$ with $b$, or using the wrong $c$ for $C$, silently turns the proportion into nonsense.
- **Using the law of sines when you should be using the law of cosines.** If you have SSS or SAS, the law of sines has no complete pair to start with. Use [[Law_Of_Cosines]] to find a first angle or side, then switch.

---

## Prerequisites

Before practicing, these should feel comfortable:

- [[Angles]] — degree and radian measures, angle sum of a triangle
- [[Circular_Functions]] — the sine function as a ratio built from the unit circle
- [[Inverse_Trigonometric_Functions]] — $\arcsin$ is how you reverse-engineer an angle from its sine
- [[The_Unit_Circle]] — the sign of sine in each quadrant, which drives the ambiguous-case classification

---

## Problems Involving the Law of Sines

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="law_of_sines"></div>

---

## See Also

- [[Law_Of_Cosines]] — the partner rule that handles SSS and SAS triangles
- [[Inverse_Trigonometric_Functions]] — needed to recover angles from a sine value
- [[Circular_Functions]]
- [[Angles]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
