---
title: "The Midpoint Formula"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-analytic-geometry", "#key-formula", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/The_Distance_Formula"
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Dividing_Fractions"
problem_type_ids: []
figures: []
summary: "Average the coordinates: the midpoint of a segment is just the average of its two endpoints, axis by axis."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > The Midpoint Formula

# The Midpoint Formula

If you and a friend want to meet for lunch exactly halfway between your houses, you probably already know the trick: take the two addresses and find the spot in between. The **midpoint formula** is the coordinate-plane version of that idea. Given two points, it hands you the exact center point of the segment joining them. It is one of the friendlier formulas in all of geometry because it is really just "take the average of the two $x$-coordinates, take the average of the two $y$-coordinates, and put them together." If you can find an average, you can use the midpoint formula.

## What it means

Given two points $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ in the coordinate plane, the **midpoint** $M$ of the segment $\overline{P_1 P_2}$ is the point whose coordinates are the averages of the corresponding coordinates of the endpoints:

$$
M = \left( \frac{x_1 + x_2}{2},\ \frac{y_1 + y_2}{2} \right)
$$

So the $x$-coordinate of the midpoint is the average of the two $x$-coordinates, and the $y$-coordinate is the average of the two $y$-coordinates. That is the entire formula. Each axis is handled on its own — the two averages do not interact with each other.

In one dimension, on a plain number line, the idea is even simpler. The midpoint between two numbers $a$ and $b$ is just:

$$
M = \frac{a + b}{2}
$$

The formula for the plane is nothing more than the number-line formula applied once for each axis.

## How it works

To use the formula, label your two endpoints carefully so you do not mix up coordinates.

1. Pick one endpoint and call it $(x_1, y_1)$. Pick the other and call it $(x_2, y_2)$. It does not matter which is which — averages are symmetric.
2. Add the two $x$-coordinates and divide by $2$. That is the $x$-coordinate of the midpoint.
3. Add the two $y$-coordinates and divide by $2$. That is the $y$-coordinate of the midpoint.
4. Write the midpoint as an ordered pair.

The formula also works in reverse. If you know the midpoint and one endpoint, you can solve for the other endpoint by treating each coordinate equation separately. For example, if $M = (m_x, m_y)$ and one endpoint is $(x_1, y_1)$, then the missing endpoint $(x_2, y_2)$ satisfies:

$$
m_x = \frac{x_1 + x_2}{2}, \qquad m_y = \frac{y_1 + y_2}{2}
$$

Multiplying both sides of each equation by $2$ and moving the known coordinates to the right gives the unknown:

$$
x_2 = 2 m_x - x_1, \qquad y_2 = 2 m_y - y_1
$$

No new idea, just basic algebra applied to the midpoint definition.

## Why it works

The midpoint is the point halfway along the segment, which means its $x$-coordinate is halfway between the two $x$-coordinates and its $y$-coordinate is halfway between the two $y$-coordinates. "Halfway between two numbers" is exactly what an average computes — it splits the difference and lands right in the middle. Because the two axes of the coordinate plane are independent (horizontal position does not affect vertical position), you can average each axis on its own and the results combine to give the midpoint of the whole segment. The formula is just the number-line average, applied twice.

## Worked examples

**Example 1.** Determine the midpoint of the segment with endpoints $(2, 8)$ and $(10, 4)$.

Label the endpoints: $(x_1, y_1) = (2, 8)$ and $(x_2, y_2) = (10, 4)$. Apply the formula one coordinate at a time.

The $x$-coordinate of the midpoint:

$$
\frac{x_1 + x_2}{2} = \frac{2 + 10}{2} = \frac{12}{2} = 6.
$$

The $y$-coordinate of the midpoint:

$$
\frac{y_1 + y_2}{2} = \frac{8 + 4}{2} = \frac{12}{2} = 6.
$$

So the midpoint is $(6, 6)$. A quick plotting check: the segment runs from upper-left-ish to the right, and $(6, 6)$ is visibly between the two endpoints. Good.

**Example 2.** Find the midpoint of the segment with endpoints $(-3, 5)$ and $(7, -1)$.

Label: $(x_1, y_1) = (-3, 5)$ and $(x_2, y_2) = (7, -1)$.

The $x$-coordinate of the midpoint:

$$
\frac{-3 + 7}{2} = \frac{4}{2} = 2.
$$

The $y$-coordinate of the midpoint:

$$
\frac{5 + (-1)}{2} = \frac{4}{2} = 2.
$$

So the midpoint is $(2, 2)$. The important move here is keeping the signs on the negative coordinates. If you wrote $-3 + 7$ as $-10$ instead of $4$, you would have subtracted when you meant to add. The formula calls for addition, not for "distance between the two numbers."

**Example 3.** The midpoint of a segment is $(5, 3)$, and one endpoint is $(1, 1)$. Determine the other endpoint.

This is the reverse-direction problem. Call the unknown endpoint $(x_2, y_2)$, and use the rearranged formula. For the $x$-coordinate:

$$
x_2 = 2(5) - 1 = 10 - 1 = 9.
$$

For the $y$-coordinate:

$$
y_2 = 2(3) - 1 = 6 - 1 = 5.
$$

So the missing endpoint is $(9, 5)$. You can verify by running the original midpoint formula forward. Averaging $(1, 1)$ and $(9, 5)$:

$$
\left( \frac{1 + 9}{2},\ \frac{1 + 5}{2} \right) = \left( \frac{10}{2},\ \frac{6}{2} \right) = (5, 3).
$$

That matches the given midpoint, so the answer checks.

## Common pitfalls

- **Subtracting instead of adding.** The midpoint formula averages the coordinates — it does not take differences. Subtracting belongs to the distance formula, not the midpoint formula.
- **Mixing up $x$ and $y$.** Keep the coordinates in their own column. Add $x$s with $x$s and $y$s with $y$s. Writing $\tfrac{x_1 + y_2}{2}$ is a very common slip.
- **Dropping a negative sign.** When an endpoint has a negative coordinate, carry the sign into the sum: $-3 + 7 = 4$, not $10$. A small sign error here puts the midpoint on the wrong side of the plane.
- **Forgetting to divide by $2$.** Averaging is a two-step move: add, then divide. Skipping the division gives you twice the midpoint instead.

## Problems Involving The Midpoint Formula

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_midpoint_formula"></div>

## See Also

- [[Plotting_Points_And_The_Coordinate_Plane]]
- [[The_Distance_Formula]]
- [[Mean_Median_Mode_And_Range]]
- [[Integers_And_The_Number_Line]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
