---
title: "Chords, Secants, and Tangents"
type: topic
aliases: ["Power of a Point", "Chord-Chord Product"]
tags: ["#branch-geometry", "#topic-euclidean-geometry", "#key-technique"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Circles"
  - "topics/geometry/Inscribed_Angles_And_Arcs"
  - "topics/geometry/Equations_Of_Circles"
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Circumference_And_Area_Of_Circles"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Similar_Triangles"
problem_type_ids: []
figures: ["geometry/chord_secant_tangent.svg"]
summary: "Three ways a line can meet a circle — chord, secant, tangent — each with a power-of-a-point product rule that turns crossings into simple equations."
---

> [[_overview|Home]] > [[Geometry|Geometry]] > Chords, Secants, and Tangents

# Chords, Secants, and Tangents

A straight line can interact with a circle in three ways. It can stay completely outside the circle and never touch it. It can cut clean through the circle at two points. Or it can just kiss the circle at a single point without crossing. The three *named* cases are:

- **Chord** — a line segment whose endpoints both lie on the circle.
- **Secant** — a full line (or ray) that crosses the circle at exactly two points. A chord is the piece of a secant that sits inside the circle.
- **Tangent** — a line (or line segment) that touches the circle at exactly one point, called the point of tangency.

![[chord_secant_tangent.svg|Chord, secant, and tangent with the power-of-a-point products]]

Each of these arrangements gives you a product rule that relates lengths of segments through a common point — the family of relationships known as **power of a point**. Once you set them up, most circle-intersection problems collapse into algebra you already know.

---

## Power of a point, chord-chord version

Take two chords of a circle that cross each other inside the circle, at a point $P$. Let one chord split into segments of length $a$ and $b$ at $P$, and the other chord split into segments of length $c$ and $d$ at $P$. Then

$$
a \cdot b = c \cdot d.
$$

No matter which two chords you pick, as long as they cross at $P$, the product of the two pieces of each chord is the same. This is the chord-chord power-of-a-point rule.

---

## Power of a point, secant-secant and secant-tangent versions

Now suppose the crossing point $P$ sits *outside* the circle. Draw two secant lines from $P$ that each meet the circle at two points. Let the first secant hit the circle at distances $a$ (near) and $b$ (far) from $P$, and the second secant hit the circle at distances $c$ (near) and $d$ (far). Then

$$
a \cdot b = c \cdot d.
$$

Each product uses the *near* distance times the *whole* distance (so $a \cdot b$ with $a$ near and $b$ far, which is secant length times the external-piece length). If you replace one of the secants with a tangent from $P$ meeting the circle at a point $T$, and write $t$ for the length $PT$, the tangent counts as both its own "near" and "far" piece, so the rule becomes

$$
t^2 = a \cdot b.
$$

This is the secant-tangent version. You can stack it with another tangent to get tangent-tangent: two tangents drawn from the same external point to the same circle have equal length, so if one is $t_1$ and the other is $t_2$, then

$$
t_1 = t_2.
$$

Putting all three together: anywhere you have a common point that two circle-crossing lines pass through, a product rule is waiting.

---

## Two more essential facts

- **Equal chords sit equidistant from the center, and the perpendicular bisector of any chord passes through the center.** If you ever need to find a circle's center from just a piece of the circle, drop perpendicular bisectors through two chords and watch them meet at the center.
- **A tangent meets the radius drawn to the point of tangency at a right angle.** Any time you draw a radius to the spot where a tangent touches the circle, the tangent is perpendicular to that radius. Combined with [[The_Pythagorean_Theorem]], this turns a lot of tangent problems into right-triangle problems.

---

## Example 1: chord-chord product

> Two chords of a circle cross at an interior point $P$. The first chord is split by $P$ into pieces of lengths $6$ and $10$. The second chord is split by $P$ into pieces of lengths $5$ and $x$. Determine $x$.

Apply the chord-chord rule at $P$:

$$
6 \cdot 10 = 5 \cdot x.
$$

$$
60 = 5x \implies x = 12.
$$

So the missing piece has length $12$.

---

## Example 2: tangent perpendicular to radius

> A skate park has a circular bowl of radius $8$ feet. A kid stands at a point $P$ outside the bowl and places a straight edge from $P$ that is tangent to the edge of the bowl at a single point $T$. The distance from $P$ to the center of the bowl is $17$ feet. What is the length of the tangent segment $PT$?

The tangent at $T$ is perpendicular to the radius $\overline{OT}$, so triangle $\triangle OTP$ is a right triangle with the right angle at $T$. The hypotenuse is $OP = 17$, one leg is $OT = 8$ (the radius), and the other leg is $PT$ (what we want).

By [[The_Pythagorean_Theorem]]:

$$
OT^2 + PT^2 = OP^2 \implies 8^2 + PT^2 = 17^2.
$$

$$
64 + PT^2 = 289 \implies PT^2 = 225 \implies PT = 15.
$$

So the tangent segment measures $15$ feet.

---

## Example 3: secant-tangent from an external point

> A point $P$ outside a circle sends out two straight paths. One is a tangent that touches the circle at $T$, with $PT = 12$. The other is a secant through $P$ that enters the circle at $A$ and exits at $B$, with the near piece $PA = 9$. Determine the far distance $PB$.

Use the secant-tangent rule:

$$
PT^2 = PA \cdot PB.
$$

$$
12^2 = 9 \cdot PB \implies 144 = 9 \cdot PB \implies PB = 16.
$$

The full distance from $P$ through the circle to the far intersection point is $16$.

---

## Common pitfalls

- **Using the wrong distances in the secant rule.** The rule is always $(\text{near}) \cdot (\text{whole}) = (\text{near}) \cdot (\text{whole})$, meaning each product uses the distance from $P$ to the near intersection times the distance from $P$ to the far intersection. Do not multiply the two internal pieces — that's the chord-chord version, and it only applies when $P$ is inside the circle.
- **Forgetting to square the tangent length.** In the secant-tangent rule the tangent length appears as $t^2$, not $t$. That is because the tangent is both its own "near" distance and its own "far" distance, so it gets multiplied by itself.
- **Assuming a tangent is perpendicular to any chord.** It is only perpendicular to the *radius* drawn to the point of tangency, and that radius has to end at the tangent's touching point. Perpendicular-tangent arguments require you to draw in the radius first.
- **Mixing up chords and secants.** A chord is a segment that ends on the circle. A secant is a full line (or ray) that keeps going past the circle. For the power-of-a-point rule, the distinction matters because it determines where $P$ lives (inside vs. outside the circle).

---

## Prerequisites

- [[Circumference_And_Area_Of_Circles]] — general comfort with the basic parts of a circle
- [[The_Pythagorean_Theorem]] — every tangent-plus-radius problem uses it
- [[Similar_Triangles]] — the underlying reason the chord-chord and secant-secant products are equal (the two triangles formed by connecting the intersection points are similar)

---

## Problems Involving Chords, Secants, and Tangents

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="chords_secants_and_tangents"></div>

---

## See Also

- [[Inscribed_Angles_And_Arcs]] — the angle-based half of circle geometry
- [[Circles]]
- [[Equations_Of_Circles]] — the analytic version once the circle sits on the coordinate plane
- [[Similar_Triangles]]
- [[The_Pythagorean_Theorem]]
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
