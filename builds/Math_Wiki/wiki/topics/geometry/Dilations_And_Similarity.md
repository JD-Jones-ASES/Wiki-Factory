---
title: "Dilations and Similarity"
type: topic
aliases: ["Dilation", "Similar Figures", "Scale Factor"]
tags: ["#branch-geometry", "#topic-similarity-and-congruence", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/geometry/Rigid_Transformations"
  - "topics/geometry/Coordinate_Geometry_Proofs"
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/Proportions_In_Similar_Figures"
  - "topics/pre_algebra/Scale_Drawings_And_Maps"
status: draft
confidence: high
branch: geometry
prerequisites:
  - "topics/pre_algebra/Similar_Triangles"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
problem_type_ids: []
figures: ["geometry/dilation.svg"]
summary: "Scaling a figure from a center by a factor k changes lengths by k, areas by k squared, and volumes by k cubed."
---
> [[_overview|Home]] > [[Geometry|Geometry]] > Dilations and Similarity

# Dilations and Similarity

A **dilation** is the fourth transformation most geometry courses cover, alongside the three rigid moves from [[Rigid_Transformations]]. Unlike a translation, rotation, or reflection, a dilation is allowed to change size. You pick a fixed point called the **center** of the dilation and a number $k$ called the **scale factor**, and every point in the plane gets pushed either outward (if $|k| > 1$) or pulled inward (if $0 < |k| < 1$) along the line connecting it to the center. Distances scale, but angles do not — the overall shape stays recognizable even as it grows or shrinks.

![[dilation.svg|A triangle dilated from the origin with scale factor 2]]

Figures related by a dilation are called **similar**. Two figures are similar when they have the same shape but possibly different sizes, which technically means their corresponding angles match and their corresponding sides are in a consistent ratio.

---

## The coordinate rule for a dilation at the origin

When the center of the dilation is the origin, the coordinate rule is about as simple as it gets:

$$
(x, y) \to (kx, ky)
$$

Multiply both coordinates by the scale factor, and you are done. A scale factor of $k = 2$ doubles every coordinate, which sends every point to twice the distance from the origin along the same ray. A scale factor of $k = \tfrac{1}{2}$ halves every coordinate, bringing everything half as far from the origin.

If the center of dilation is some other point $(a, b)$, the rule is slightly more work: translate so that $(a, b)$ lands at the origin, dilate using the rule above, then translate back. The center itself always maps to itself, regardless of $k$.

---

## Scale factors: lengths, areas, and volumes

Here is the fact that does the most heavy lifting on similarity problems:

- **Lengths** scale by $k$. A segment that was $7$ units long becomes $7k$ units long.
- **Areas** scale by $k^2$. A region with area $12$ square units becomes $12 k^2$ square units.
- **Volumes** scale by $k^3$. A solid with volume $30$ cubic units becomes $30 k^3$ cubic units.

The exponents match the dimensions: length is one-dimensional, area is two-dimensional, volume is three-dimensional. A doubled figure ($k = 2$) is twice as long, four times as large in area, and eight times as large in volume. Similarly, if one similar figure has sides in the ratio $3:5$ to another, its areas are in the ratio $9:25$ and its volumes are in the ratio $27:125$.

This is why doubling a box's dimensions doesn't just double the amount of paint needed to cover it — it quadruples the paint. And why a tiny scale model weighs a stunningly small fraction of what the real object weighs.

---

## What makes two figures similar

Two figures are **similar** (written $\triangle ABC \sim \triangle DEF$ for triangles, or $\sim$ for other shapes) when you can map one onto the other using a sequence of rigid transformations followed by a dilation. Equivalently, two polygons are similar whenever both of the following hold:

- All pairs of corresponding angles are equal.
- All pairs of corresponding sides are in the same ratio, called the **scale factor**.

For triangles, either condition is enough on its own (equal angles force equal ratios and vice versa), which is why triangle similarity has its famous shortcuts like angle-angle (AA). Those shortcuts are covered in more detail on [[Similar_Triangles]]. For other polygons you typically need both conditions.

---

## Example 1: dilating a triangle from the origin

> Triangle $ABC$ has vertices $A(1, 2)$, $B(4, 2)$, and $C(3, 5)$. Apply a dilation centered at the origin with scale factor $k = 3$. What are the coordinates of the image triangle, and how do its side lengths compare to the original?

Apply $(x, y) \to (3x, 3y)$ to each vertex.

- $A(1, 2) \to A'(3, 6)$
- $B(4, 2) \to B'(12, 6)$
- $C(3, 5) \to C'(9, 15)$

Check one side length: the original $AB$ is horizontal with length $4 - 1 = 3$. The image $A'B'$ is also horizontal with length $12 - 3 = 9$. So $A'B' = 3 \cdot AB$, matching the scale factor. The same $3\times$ ratio holds for the other two sides. The image triangle is similar to the original, with every length tripled. If the original triangle had area $A_0$, the image has area $9 A_0$, since area scales by $k^2 = 9$.

---

## Example 2: using similarity to compute a missing length

> A scale model of an art installation is similar to the real installation, with a scale factor of $\tfrac{1}{20}$. A certain steel beam on the real installation is $16$ ft long. What is the length of the corresponding beam on the scale model?

Every length on the scale model is $\tfrac{1}{20}$ of the corresponding length on the real installation. So the model beam has length

$$
16 \cdot \tfrac{1}{20} = \tfrac{16}{20} = \tfrac{4}{5} \text{ ft}.
$$

That is $0.8$ ft, or about $9.6$ inches. The scale factor applies uniformly to every length in the figure, never to areas or volumes directly — for those you would need to use $k^2$ or $k^3$ instead.

---

## Example 3: area ratios from a side ratio

> Two similar custom cake molds have base edges in the ratio $2:5$. The smaller cake mold has a base area of $48 \text{ cm}^2$. What is the base area of the larger cake mold?

Because the side ratio is $2 : 5$, the scale factor from the smaller to the larger is $k = \tfrac{5}{2}$. Areas scale by $k^2$, so the larger area is

$$
48 \cdot k^2 = 48 \cdot \left(\tfrac{5}{2}\right)^2 = 48 \cdot \tfrac{25}{4} = 12 \cdot 25 = 300 \text{ cm}^2.
$$

For this problem the volume ratio would be $\left(\tfrac{5}{2}\right)^3 = \tfrac{125}{8}$, so if the smaller mold holds $64 \text{ cm}^3$, the larger one would hold $64 \cdot \tfrac{125}{8} = 1000 \text{ cm}^3$ — a useful double-check technique on similarity questions.

---

## Common pitfalls

- **Using $k$ where you should use $k^2$ or $k^3$.** Lengths scale by $k$, areas by $k^2$, volumes by $k^3$. Mixing these up is the single most common error on similarity problems.
- **Forgetting that the center of dilation is a fixed point.** The center maps to itself under any dilation. If you dilate a triangle from one of its own vertices, that vertex stays put and the other two slide outward.
- **Confusing "scale factor" with "ratio."** If the ratio is $3 : 5$, the scale factor depends on which direction you are going: from the $3$-figure to the $5$-figure is $k = \tfrac{5}{3}$; from the $5$-figure to the $3$-figure is $k = \tfrac{3}{5}$. Always know which direction is which.
- **Assuming corresponding angles are different after a dilation.** They are not. Dilations preserve all angles exactly — only lengths change.

---

## Prerequisites

- [[Similar_Triangles]] — the most common case of similarity and a natural warm-up
- [[Plotting_Points_And_The_Coordinate_Plane]] — for applying coordinate dilation rules
- [[Proportions_And_Cross_Multiplication]] — for turning side ratios into missing-length equations

---

## Problems Involving Dilations and Similarity

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your choices are saved in this browser until you open your [[Vault]] to view hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="dilations_and_similarity"></div>

---

## See Also

- [[Rigid_Transformations]] — the size-preserving partners of the dilation
- [[Similar_Triangles]] — the most common arena for similarity arguments
- [[Similar_Triangles]] — side-ratio setups
- [[Scale_Drawings_And_Maps]] — similarity in real-world contexts
- [[Coordinate_Geometry_Proofs]] — uses scale factors inside proofs
- [[Geometry|Geometry]]
- [[Topics_Overview]]
- [[_overview|Home]]
