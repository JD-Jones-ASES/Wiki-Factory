---
title: "Triangle Congruence Criteria"
type: topic
aliases: ["SSS SAS ASA AAS HL", "Congruent Triangles"]
tags: ["#branch-geometry", "#topic-similarity-and-congruence", "#key-topic", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Special_Right_Triangles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
problem_type_ids: []
figures: ["geometry/triangle_congruence_criteria.svg"]
summary: "The five short lists of matching parts — SSS, SAS, ASA, AAS, HL — that force two triangles to be identical copies of each other."
---
> [[_overview|Home]] > [[Geometry|Geometry]] > Triangle Congruence Criteria

# Triangle Congruence Criteria

Two triangles are **congruent** when you can slide, flip, or rotate one of them until it lies exactly on top of the other. Every corresponding side matches length for length, and every corresponding angle matches degree for degree. The catch: a triangle has six measurements in total (three sides plus three angles), and you almost never want to check all six. The good news is that you don't have to. Three well-chosen pieces of information are enough to force the other three — and "well-chosen" has exactly five acceptable shapes, which go by the initials SSS, SAS, ASA, AAS, and HL.

![[triangle_congruence_criteria.svg|The five shortcuts that force two triangles to match]]

Think of the five criteria as shortcuts for proving two triangles are the same without having to measure every piece. Each one is a recipe: if your two triangles share a list of parts that fits one of these patterns, you are entitled to say they are congruent.

---

## The five legal shortcuts

**SSS — Side-Side-Side.** If all three sides of one triangle have the same lengths as all three sides of another, the triangles are congruent. Intuition: three given side lengths can be assembled into only one triangle shape, no matter how you try to wiggle the vertices.

**SAS — Side-Angle-Side.** Two sides and the angle trapped *between them* are enough, as long as the angle is the one formed where those two sides meet. The angle has to be the "included" angle, not a random one on the side.

**ASA — Angle-Side-Angle.** Two angles plus the side *between them*. Because the triangle's three angles must add to $180°$ (see [[Triangle_Angle_Sum_And_Exterior_Angles]]), knowing two of them pins down the third automatically, so the missing angles cause no ambiguity.

**AAS — Angle-Angle-Side.** Two angles plus any side that is *not* between them. AAS works because, once you know two angles, the third angle is forced, and any one side length locks in the scale.

**HL — Hypotenuse-Leg (right triangles only).** For right triangles specifically: if the hypotenuses match and any one leg matches, the two triangles are congruent. This is the only SSA-shaped shortcut that is legal, and it works only because the right angle eliminates the usual ambiguity.

Each criterion is a promise of the form *give me these three matching measurements in the right configuration, and I'll hand you every other measurement for free.*

---

## Why two patterns are NOT congruence criteria

**AAA — Angle-Angle-Angle.** Three matching angles are *not* enough. Two triangles can have the same three angles but different overall sizes — a tiny triangle and an enormous triangle with matching $30°$, $60°$, $90°$ corners would be similar but not congruent. AAA guarantees [[Similar_Triangles|similarity]], not congruence.

**SSA — Side-Side-Angle.** Two sides plus a non-included angle is ambiguous in general. Depending on whether the non-included angle lies opposite the longer or shorter of the two sides, you can sometimes build two different triangles with the same three measurements. This is the notorious "ambiguous case" and is the reason HL has to be stated carefully as a right-triangle-only exception, not a general rule.

So the valid list is exactly: SSS, SAS, ASA, AAS, HL. Memorize those five and no others.

---

## Example 1: picking the criterion from given markings

> Triangle $\triangle PQR$ has $PQ = 12$, $QR = 9$, and the measure of the angle at $Q$ is $48°$. Triangle $\triangle XYZ$ has $XY = 12$, $YZ = 9$, and the measure of the angle at $Y$ is $48°$. Are the triangles congruent, and if so by which criterion?

Line up the matching parts: $PQ$ matches $XY$ (both $12$), $QR$ matches $YZ$ (both $9$), and the angle at $Q$ matches the angle at $Y$ (both $48°$).

The angle at $Q$ sits at the shared vertex of sides $PQ$ and $QR$ — it is the angle included between the two matching sides. Similarly the angle at $Y$ is between $XY$ and $YZ$ on the other triangle. Two sides plus the included angle is the **SAS** pattern.

Conclusion: $\triangle PQR \cong \triangle XYZ$ by SAS.

---

## Example 2: deciding whether the given parts force congruence

> Two triangles share the measurements $40°$, $60°$, and $80°$ but have side lengths $3$, $4$, and $5$ in one triangle and $6$, $8$, and $10$ in the other. Are they congruent?

The two triangles share all three angles. That is AAA information, which guarantees the triangles have the same shape but does not guarantee the same size. Indeed the side lengths in the second triangle are double those in the first, so the second triangle is twice as large. The triangles are similar (see [[Similar_Triangles]]) but **not** congruent.

---

## Example 3: the HL shortcut on a right triangle pair

> Two right triangles each have a hypotenuse of length $13$. One of the legs of the first triangle measures $5$, and one of the legs of the second triangle also measures $5$. Are the triangles congruent?

Both triangles are right triangles (guaranteed in the setup). Both share a hypotenuse of length $13$, and both share a leg of length $5$. That is the exact form of the **HL** criterion: hypotenuse plus leg on a right-triangle pair.

You can sanity-check with the [[The_Pythagorean_Theorem|Pythagorean theorem]]: the other leg of each triangle must satisfy $\text{leg}^2 + 5^2 = 13^2$, giving $\text{leg}^2 = 169 - 25 = 144$, so $\text{leg} = 12$. Both triangles end up with sides $5$, $12$, $13$, and really are congruent.

Conclusion: congruent by **HL**.

---

## Common pitfalls

- **Using AAA to claim congruence.** Three matching angles only proves [[Similar_Triangles|similarity]]. Always look for at least one matching side length before declaring congruence.
- **Using SSA in general.** Two sides plus a non-included angle can produce two different triangles. HL is the *one* exception, and it requires a right angle that you already know is there.
- **Mislabeling the "included" angle in SAS.** The angle in SAS has to be the one formed exactly where the two matching sides meet. If the given angle is somewhere else on the triangle, you have SSA, not SAS, and no legal shortcut applies.
- **Mixing up ASA and AAS.** In ASA, the given side is the one sandwiched *between* the two given angles. In AAS, the given side is *not* between the two angles. Both are valid criteria; just don't write one when you mean the other.

---

## Prerequisites

- [[Triangle_Angle_Sum_And_Exterior_Angles]] — makes ASA and AAS work because the third angle is determined
- [[Similar_Triangles]] — the AAA shortcut that explains why AAA is not a congruence criterion
- [[Classifying_Triangles_And_Quadrilaterals]] — vocabulary for recognizing right triangles, which HL relies on

---

## Problems Involving Triangle Congruence Criteria

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="triangle_congruence_criteria"></div>

---

## See Also

- [[Special_Right_Triangles]] — a special case where the HL criterion is extra useful
- [[Classifying_Triangles_And_Quadrilaterals]]
- [[Similar_Triangles]]
- [[Triangle_Angle_Sum_And_Exterior_Angles]]
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
