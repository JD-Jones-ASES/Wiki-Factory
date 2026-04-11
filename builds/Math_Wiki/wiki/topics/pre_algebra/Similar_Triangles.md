---
title: "Similar Triangles"
type: topic
aliases: ["Similar Triangle", "AA Similarity", "Triangle Similarity"]
tags: ["#branch-pre-algebra", "#topic-similarity-and-congruence"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "7", section: "7.2"}
related:
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Proportions_In_Similar_Figures"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Applications_Of_The_Pythagorean_Theorem"
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Triangle_Angle_Sum_And_Exterior_Angles"
  - "topics/pre_algebra/Ratios_And_Proportions"
problem_type_ids: []
figures: []
summary: "Triangles with the same shape but possibly different sizes, caught by the AA rule and unlocked by proportional sides."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Similar Triangles

# Similar Triangles

Two triangles are **similar** when they share the same shape without necessarily sharing the same size. One may be a miniature of the other, or a scaled-up photocopy — as long as the two figures have the same proportions, mathematicians treat them as the same shape at different zoom levels. The symbol $\sim$ is used to record this relationship: writing $\triangle ABC \sim \triangle DEF$ says that the first triangle is similar to the second.

What makes the idea so powerful is that "same shape" can be captured in two equivalent ways: through angles and through sides. If you know one of those things, the other comes along for free.

---

## Key ideas

**The two things that must agree.** Suppose $\triangle ABC \sim \triangle DEF$. Then two conditions hold at once:

1. The matching (corresponding) angles are equal: $\angle A = \angle D$, $\angle B = \angle E$, $\angle C = \angle F$.
2. The matching sides are in the same ratio:

$$
\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}
$$

The common value of those ratios is called the **scale factor**. A scale factor of $2$ means the second triangle has sides twice as long as the first; a scale factor of $\tfrac{1}{3}$ means its sides are one-third as long.

**Corresponding parts have to be paired up carefully.** When you write $\triangle ABC \sim \triangle DEF$, the order of the letters matters. The first letter in each name labels the first pair of matching vertices ($A \leftrightarrow D$), the second labels the second pair ($B \leftrightarrow E$), and so on. Side $AB$ corresponds to side $DE$ — not to $EF$ — because those two sides run between the matched vertex pairs. Get the pairing wrong and every ratio you set up will be wrong.

**The Angle-Angle shortcut.** In general, checking similarity by hand would mean verifying three angles and three ratios — six things. But triangles are special: because their interior angles always add up to $180^\circ$, knowing two angles automatically fixes the third. That leads to the single most useful rule in this whole chapter, the **Angle-Angle criterion** — usually written **AA similarity**:

> If two angles of one triangle equal two angles of another triangle, the two triangles are similar.

You don't have to measure the third angle. You don't have to measure any sides. Two angle matches, and similarity is guaranteed.

**Why the sides still work out.** Once AA guarantees the same shape, the side ratios line up automatically. This is the engine behind *indirect measurement*: if you can't reach the top of a flagpole or the far side of a canyon, you can still figure out the distance by setting up a smaller, reachable triangle that shares two angles with the big one, then solving a proportion.

**The bridge to trigonometry.** Similar triangles are the hidden reason the sine, cosine, and tangent ratios even exist. Every right triangle with, say, a $30^\circ$ angle is similar to every other right triangle with a $30^\circ$ angle (they already share the right angle plus the $30^\circ$, so AA kicks in). That means the ratio `opposite / hypotenuse` is always the same for a $30^\circ$ right triangle, no matter how big you draw it. That single ratio is what we decide to call $\sin 30^\circ$. Without similar triangles, trig wouldn't make sense — you couldn't give a fixed number to an angle.

---

## Example 1: checking whether two triangles are similar

> In $\triangle ABC$, $m\angle A = 45^\circ$ and $m\angle B = 75^\circ$. In $\triangle XYZ$, $m\angle X = 60^\circ$ and $m\angle Z = 75^\circ$. Are the two triangles similar?

Both triangles have a $75^\circ$ angle, so one pair of angles already matches. For AA, we need a second pair. But the two known angles in each triangle aren't obviously partners yet — one triangle lists $45^\circ$ and $75^\circ$, the other lists $60^\circ$ and $75^\circ$. Let's fill in each missing angle using the Triangle Angle Sum.

For $\triangle ABC$:

$$
m\angle C = 180^\circ - 45^\circ - 75^\circ = 60^\circ
$$

For $\triangle XYZ$:

$$
m\angle Y = 180^\circ - 60^\circ - 75^\circ = 45^\circ
$$

Now put the full angle sets side by side: $\triangle ABC$ has angles $\{45^\circ, 60^\circ, 75^\circ\}$ and $\triangle XYZ$ has angles $\{45^\circ, 60^\circ, 75^\circ\}$. Every angle of one triangle matches an angle of the other. Two matches are already enough for AA, so **yes**, the triangles are similar. The correct correspondence pairs the equal angles: $A \leftrightarrow Y$, $B \leftrightarrow Z$, $C \leftrightarrow X$. We could write this as $\triangle ABC \sim \triangle YZX$. The order matters — listing the wrong pairing of letters would describe a relationship that isn't true.

---

## Example 2: solving for a missing side

> Triangle $PQR$ is similar to triangle $STU$, with $PQ = 6$, $QR = 9$, $ST = 8$. What is the length of $TU$?

Because the triangles are similar, the sides across corresponding vertices are in the same ratio. The way the similarity is written, $P \leftrightarrow S$ and $Q \leftrightarrow T$, so $PQ$ matches with $ST$. Likewise $Q \leftrightarrow T$ and $R \leftrightarrow U$, so $QR$ matches with $TU$. That gives the proportion:

$$
\frac{PQ}{ST} = \frac{QR}{TU}
$$

Plug in the three known values:

$$
\frac{6}{8} = \frac{9}{TU}
$$

Cross-multiply — the product of the top of the first fraction with the bottom of the second equals the product of the bottom of the first with the top of the second:

$$
6 \cdot TU = 8 \cdot 9
$$

$$
6 \cdot TU = 72
$$

$$
TU = 12
$$

So $TU = 12$ units. A useful sanity check: the scale factor from the first triangle to the second is $\tfrac{8}{6} = \tfrac{4}{3}$, and indeed $9 \cdot \tfrac{4}{3} = 12$. The numbers are consistent.

---

## Example 3: measuring what you cannot reach

> A cell-phone tower sits in the middle of an empty lot. You cannot walk up and measure its height, but you notice that it casts a $35$-foot shadow. At exactly the same moment, a $6$-foot sign standing next to it casts a $2.5$-foot shadow. How tall is the tower?

The sun is so far away that its rays are essentially parallel, so the light strikes the tower and the sign at the same angle above the horizon. Both the tower and the sign stand vertically, meeting the ground at a $90^\circ$ right angle. That gives each object its own right triangle: the object itself is one leg, the shadow is the other leg, and the slanted sun ray is the hypotenuse. Both triangles share a right angle, and they share the sun's angle above the ground — two matching angles, so AA similarity applies.

Let $h$ stand for the unknown height of the tower. Set up the proportion by matching the "height" sides to the "shadow" sides:

$$
\frac{h}{35} = \frac{6}{2.5}
$$

Cross-multiply:

$$
2.5 \cdot h = 35 \cdot 6
$$

$$
2.5 h = 210
$$

$$
h = \frac{210}{2.5} = 84
$$

So the tower stands about $84$ feet tall. Notice what you did and did not use: you never climbed the tower, never held a measuring tape up high, never did anything dangerous. Two easy measurements on the ground plus AA similarity was enough to give you the full answer. This trick — called *indirect measurement* — is exactly how ancient Greek astronomers estimated the sizes of the Earth, Moon, and Sun.

---

## Common pitfalls

- **Misreading the correspondence.** When you write $\triangle ABC \sim \triangle DEF$, the pairing $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$ is baked into the order of the letters. Pairing the wrong vertices scrambles every proportion you try to write.
- **Using "congruent" when you mean "similar."** Congruent triangles are identical in every respect — same angles *and* same side lengths. Similar triangles only need the same shape, not the same size. Every pair of congruent triangles is similar, but most similar triangles are not congruent.
- **Forgetting that AA is enough.** Some students check all three angles anyway, or even start measuring sides. Two matching angles seals the deal on their own, because the third angle is forced by $180^\circ$.
- **Flipping the proportion upside down.** In a similarity proportion the two triangles have to be treated consistently: all the numerators come from the same triangle, all the denominators from the other. Mixing them gives a wrong ratio. When in doubt, write each side as "triangle-one length over the matching triangle-two length."

---

## Prerequisites

Before you work through practice problems, make sure you are comfortable with:

- [[Classifying_Triangles_And_Quadrilaterals]] — so you can recognize and describe triangle parts confidently
- [[Triangle_Angle_Sum_And_Exterior_Angles]] — you'll need the $180^\circ$ rule constantly when applying AA
- [[Ratios_And_Proportions]] — setting up and solving a proportion is the core mechanic in every side-length problem

---

## Problems Involving Similar Triangles

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="similar_triangles"></div>

---

## See Also

- [[Triangle_Angle_Sum_And_Exterior_Angles]]
- [[Proportions_In_Similar_Figures]]
- [[The_Pythagorean_Theorem]]
- [[Applications_Of_The_Pythagorean_Theorem]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
