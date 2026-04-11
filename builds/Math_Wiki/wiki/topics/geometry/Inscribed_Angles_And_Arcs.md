---
title: "Inscribed Angles and Arcs"
type: topic
aliases: ["Inscribed Angle Theorem", "Central Angle Theorem"]
tags: ["#branch-geometry", "#topic-euclidean-geometry", "#key-topic", "#test-sat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Circles"
  - "topics/geometry/Chords_Secants_And_Tangents"
  - "topics/geometry/Equations_Of_Circles"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Points_Lines_Angles_And_Angle_Relationships"
problem_type_ids: []
figures: ["geometry/inscribed_angle_theorem.svg"]
summary: "Central angles equal the arcs they cut off, inscribed angles are half as big, and arcs translate directly into lengths and sector areas."
---
> [[_overview|Home]] > [[Geometry|Geometry]] > Inscribed Angles and Arcs

# Inscribed Angles and Arcs

An **arc** is a curved slice of a circle's boundary. Every arc has two natural measurements: how long it is (a length, measured in centimeters or feet), and how wide it is (a *measure*, given in degrees as a portion of the full $360°$ of the circle). And every arc has angles that point at it — angles whose sides lie along the circle's radii or along chords. This page connects all four quantities: arc measure, arc length, central angle, and inscribed angle.

![[inscribed_angle_theorem.svg|An inscribed angle equals half its central angle]]

The single most useful fact here is that an angle with its vertex *on* the circle is exactly half an angle with its vertex *at the center*, provided both angles point at the same arc. Everything else on this page is either a direct consequence or a use case.

---

## Central angles and arc measure

A **central angle** is an angle whose vertex is at the center of the circle and whose two sides are radii of the circle. The central angle's measure (in degrees) is defined to equal the measure of the arc it cuts off between its two sides. If a central angle measures $72°$, the arc between its two radii also measures $72°$, and the complementary arc (the long way around) measures $360° - 72° = 288°$. Central angle and arc measure are the same number, by construction.

This lets you convert freely: whenever a problem tells you about a central angle, you know the arc it points at, and vice versa.

---

## Inscribed angles

An **inscribed angle** is an angle whose vertex sits *on the circle itself*, with its two sides being chords of the circle. The arc "intercepted" by the inscribed angle is the arc that lies between the two chords, on the opposite side of the chords from the vertex. The headline rule:

$$
\text{inscribed angle} = \frac{1}{2} \cdot \text{intercepted arc}.
$$

So if the intercepted arc measures $80°$, the inscribed angle measures $40°$. If the central angle subtended by the same arc measures $80°$, then the inscribed angle is half of that — also $40°$.

Two useful corollaries fall out immediately:

- **All inscribed angles that share the same intercepted arc are equal.** Drop a bunch of different vertices on the circle and connect each one to both endpoints of the same arc. Every angle you build this way has the same measure.
- **An angle inscribed in a semicircle is a right angle.** A semicircle is half the circle, so its arc measure is $180°$. Half of $180°$ is $90°$, meaning any triangle that has one side equal to a diameter of the circle must have a $90°$ angle at the third vertex. This is sometimes called Thales' theorem, and it gives a very clean way to spot hidden right triangles inside circle problems.

---

## Arc length as a fraction of circumference

Arc *measure* tells you the share of the circle an arc takes up (out of $360°$). Arc *length* is the actual curved-line distance. Since circumference is $2\pi r$ and a full circle is $360°$, an arc of measure $\theta$ has length

$$
\text{arc length} = \frac{\theta}{360°} \cdot 2\pi r.
$$

It is literally the fraction of the circle the arc covers, times the full circumference. Same reasoning for **sector area** — a "pizza slice" bounded by two radii and the arc between them:

$$
\text{sector area} = \frac{\theta}{360°} \cdot \pi r^2.
$$

These two formulas are the workhorses of any problem that asks about part of a circle.

---

## Example 1: inscribed angle from a central angle

> A central angle of circle $\bigodot O$ measures $110°$ and cuts off an arc from point $A$ to point $B$. Point $C$ lies on the opposite side of the circle from this arc, and you draw chords $\overline{CA}$ and $\overline{CB}$. What is the measure of the inscribed angle at $C$?

The central angle equals the arc measure, so $\overset{\frown}{AB} = 110°$. The inscribed angle at $C$ intercepts this same arc, so its measure is half:

$$
m\angle C = \frac{1}{2} \cdot 110° = 55°.
$$

The inscribed angle at $C$ measures $55°$.

---

## Example 2: right triangle hidden in a semicircle

> On circle $\bigodot O$ with diameter $\overline{PQ}$, a third point $R$ lies on the circle. If $PR = 8$ and the diameter $PQ = 10$, determine the length of $QR$.

Since $\overline{PQ}$ is a diameter, the inscribed angle at $R$ (namely $\angle PRQ$) intercepts a semicircle and therefore measures $90°$. Triangle $\triangle PRQ$ is a right triangle with the right angle at $R$, hypotenuse $PQ = 10$, and one leg $PR = 8$.

Apply [[The_Pythagorean_Theorem]]:

$$
PR^2 + QR^2 = PQ^2 \implies 8^2 + QR^2 = 10^2.
$$

$$
64 + QR^2 = 100 \implies QR^2 = 36 \implies QR = 6.
$$

So $QR$ has length $6$.

---

## Example 3: arc length and sector area

> A circular skate park has a curved ramp section that takes up a central angle of $45°$ on a circle of radius $12$ meters. Give the arc length of the curved edge and the area of the sector (the wedge bounded by the two radii and the arc).

Plug into the arc-length formula:

$$
\text{arc length} = \frac{45°}{360°} \cdot 2\pi (12) = \frac{1}{8} \cdot 24\pi = 3\pi \text{ meters}.
$$

And the sector-area formula:

$$
\text{sector area} = \frac{45°}{360°} \cdot \pi (12)^2 = \frac{1}{8} \cdot 144\pi = 18\pi \text{ square meters}.
$$

So the curved edge is $3\pi$ meters (about $9.42$ m) and the sector covers $18\pi$ square meters (about $56.55$ m$^2$).

---

## Common pitfalls

- **Forgetting the $\tfrac{1}{2}$ factor on inscribed angles.** It is tempting to treat the inscribed angle as equal to the arc — that is the rule for *central* angles only. Inscribed angles are always half.
- **Using arc length when the problem wants arc measure.** Arc measure is given in degrees and ranges $0$ to $360°$; arc length is a physical distance and depends on the radius. They are different quantities tied together by the arc-length formula.
- **Confusing "intercepted arc" with the other arc.** Every chord splits a circle into two arcs — a minor and a major. The intercepted arc is the one *inside* the inscribed angle's two sides, not the one behind the vertex.
- **Mixing up sector with segment.** A "sector" is the pie-wedge bounded by two radii and an arc. A "segment" is the flatter region bounded by a chord and an arc. These have different area formulas.

---

## Prerequisites

- [[Circumference_And_Area_Of_Circles]] — you need $C = 2\pi r$ and $A = \pi r^2$ before arc length and sector area make sense
- [[Triangle_Angle_Sum_And_Exterior_Angles]] — pops up constantly once the semicircle-right-angle trick is in play
- [[Points_Lines_Angles_And_Angle_Relationships]] — general angle vocabulary used throughout

---

## Problems Involving Inscribed Angles and Arcs

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="inscribed_angles_and_arcs"></div>

---

## See Also

- [[Chords_Secants_And_Tangents]] — the other family of circle-line interaction facts
- [[Equations_Of_Circles]] — analytic version of this content once you put the circle on a coordinate plane
- [[Circles]]
- [[Circumference_And_Area_Of_Circles]]
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
