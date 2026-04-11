---
title: "Slope"
type: topic
aliases: ["Slope of a Line"]
tags: ["#branch-algebra-1", "#topic-linear", "#key-topic", "#key-formula", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Parallel_And_Perpendicular_Lines"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Modeling_With_Linear_Functions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Ratios_And_Equivalent_Ratios"
problem_type_ids: []
figures: []
summary: "A single number that measures how steeply and in which direction a line climbs through the coordinate plane."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Slope

# Slope

Imagine you are hiking up a trail marked on graph paper. Some stretches of trail feel like a brutal climb, where a small step forward gains you a lot of elevation. Other stretches feel like a gentle ramp, where you walk a long way before you gain any height. And sometimes you hit a flat section where the elevation does not change at all. **Slope** is the single number mathematicians use to describe exactly how steep (and in what direction) a straight line is climbing through the coordinate plane. It tells you, per unit of horizontal travel, how much the line gains or loses in height.

Slope turns out to be one of the most productive numbers you will compute in Algebra 1. Once you know a line's slope and any one point the line passes through, you can write its whole equation. Lines with equal slopes are parallel. Lines whose slopes multiply to give $-1$ meet at right angles (see [[Parallel_And_Perpendicular_Lines]]). Even in word problems with nothing to do with graphs, slope is the secret name for the phrase **rate of change** — dollars per hour, miles per gallon, degrees per minute, steps per second. It is a remarkably versatile quantity.

## What it means / The idea

Start with any two points on a non-vertical line, call them $(x_1, y_1)$ and $(x_2, y_2)$. As you move from the first point to the second, the $y$-coordinate changes by some amount (the vertical change, or **rise**) and the $x$-coordinate changes by some amount (the horizontal change, or **run**). The slope is the ratio of those two changes:

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

Some books also write this as $m = \Delta y / \Delta x$, where $\Delta$ (delta) is shorthand for "change in." Both versions say the same thing: slope is vertical change divided by horizontal change.

Four kinds of lines give four flavors of slope, and learning to tell them apart by eye is a big payoff:

- **Positive slope ($m > 0$):** the line climbs left to right, like a ramp going up as you read. Bigger $m$ means steeper climb.
- **Negative slope ($m < 0$):** the line falls left to right. The $-$ sign is not cosmetic — it records the direction of travel.
- **Zero slope ($m = 0$):** the line is horizontal. The rise is zero no matter how far you walk, so the ratio is $0$.
- **Undefined slope:** the line is vertical. The run is zero, and division by zero is undefined, so slope does not exist for vertical lines. We do not say "the slope is infinity"; we say it is **undefined**.

## How it works / The procedure

Given two points and asked for a slope:

1. **Label the points.** Call one of them $(x_1, y_1)$ and the other $(x_2, y_2)$. It does not matter which you call which, as long as you are consistent.
2. **Compute the rise.** Take $y_2 - y_1$. Mind the signs — a negative coordinate minus a positive coordinate stays negative.
3. **Compute the run.** Take $x_2 - x_1$ using the **same** point order you picked for the rise.
4. **Divide rise by run.** Simplify the fraction if possible. If the denominator is zero, the line is vertical and the slope is undefined.
5. **Interpret the sign.** A positive answer means climbing; a negative answer means falling; $0$ means level.

Given a graph and asked for a slope, pick any two lattice points the line clearly crosses, then apply the same formula — or just count the vertical squares and horizontal squares between the two points and divide.

## Why it works

The formula is really a statement about **ratios** of change. Because the line is straight, the ratio of vertical change to horizontal change is the same no matter which two points on it you pick. Double the run, and the rise doubles too. Halve the run, and the rise halves. The ratio is preserved, which is exactly what a slope captures. A curve would give you different ratios for different point pairs, which is why curves do not have a single slope and straight lines do. And it is why the consistency in step 1 matters: if you flip your point order halfway through (calling one point $(x_1, y_1)$ for the rise but $(x_2, y_2)$ for the run), you get a sign error and the ratio will come out wrong.

## Worked examples

### Example 1

Leilani is tracking her walking pace on a pedometer app that plots time in minutes on the $x$-axis and steps taken on the $y$-axis. Two recorded points on her walk are $(2, 240)$ and $(7, 840)$. Compute the slope of the line through these points.

Pick the first as $(x_1, y_1) = (2, 240)$ and the second as $(x_2, y_2) = (7, 840)$. Rise is $840 - 240 = 600$. Run is $7 - 2 = 5$. Slope is

$$
m = \frac{600}{5} = 120.
$$

Leilani's line has slope $120$, which in this context means she is taking $120$ steps per minute. That is the **rate of change** interpretation working alongside the geometric one.

### Example 2

Give the slope of the line that passes through $(3, 8)$ and $(-1, -4)$.

Take the first as $(x_1, y_1) = (3, 8)$ and the second as $(x_2, y_2) = (-1, -4)$. Rise is $-4 - 8 = -12$. Run is $-1 - 3 = -4$. Slope is

$$
m = \frac{-12}{-4} = 3.
$$

The two negatives cancel, leaving $m = 3$. The line climbs $3$ units vertically for every $1$ unit horizontally. Notice I could have swapped which point I called first — if I had used $(-1, -4)$ as $(x_1, y_1)$ and $(3, 8)$ as $(x_2, y_2)$, rise would have been $8 - (-4) = 12$ and run would have been $3 - (-1) = 4$, so $m = 12/4 = 3$. Same answer, which is the guarantee I was promising — the labeling does not change the result as long as it stays consistent.

### Example 3

A horizontal line passes through the points $(-5, 6)$ and $(10, 6)$. Determine its slope.

Apply the formula with $(x_1, y_1) = (-5, 6)$ and $(x_2, y_2) = (10, 6)$. Rise is $6 - 6 = 0$. Run is $10 - (-5) = 15$. Slope is

$$
m = \frac{0}{15} = 0.
$$

A horizontal line has slope $0$. You can see this without computing: both points have the same $y$-coordinate, so there is no vertical change between them, and zero divided by anything (other than zero) is zero. If instead the two points had shared the same $x$-coordinate — say $(4, 1)$ and $(4, 9)$ — the run would have been zero, and the slope would have been **undefined**, the hallmark of a vertical line.

## Common pitfalls

- **Putting horizontal change in the numerator.** The formula is $(y_2 - y_1)/(x_2 - x_1)$ — vertical change on top, horizontal change on the bottom. Swapping them flips the answer upside down. A slope of $2$ becomes a slope of $\tfrac{1}{2}$, which is a different line.
- **Inconsistent point order.** If you use $(x_2, y_2)$ first in the numerator, you must also use it first in the denominator. Mixing orders introduces a sign error that usually shows up as the wrong-sign slope.
- **Dropping a negative sign.** When a coordinate is negative, subtracting it flips the sign. For example, $5 - (-3) = 5 + 3 = 8$, not $5 - 3 = 2$. Write the minuses carefully and let the arithmetic follow.
- **Calling a vertical line's slope zero.** Vertical lines have **undefined** slope, not zero slope. A slope of zero describes a horizontal line. These are opposite situations even though both feel "not slanting like a normal line."
- **Forgetting to simplify the fraction.** A slope written as $\tfrac{6}{4}$ is not wrong, but it is not in lowest terms, and on a standardized test the answer key will usually expect $\tfrac{3}{2}$.

## Problems Involving Slope

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="slope"></div>

## See Also

- [[Parallel_And_Perpendicular_Lines]] — how slope relationships tell you when lines never meet or meet at a right angle
- [[Writing_Linear_Equations]] — once you know the slope and a point, you can write the line's equation
- [[Linear_Functions]] — the function-flavored view of the same objects
- [[Modeling_With_Linear_Functions]] — slope as rate of change in real situations
- [[Plotting_Points_And_The_Coordinate_Plane|Plotting Points and the Coordinate Plane]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
