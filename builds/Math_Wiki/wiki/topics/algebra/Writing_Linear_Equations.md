---
title: "Writing Linear Equations"
type: topic
aliases: ["Writing Equations of Lines", "Finding the Equation of a Line"]
tags: ["#branch-algebra-1", "#topic-linear"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "4", section: "4.4"}
related:
  - "topics/algebra/Slope"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/algebra/Parallel_And_Perpendicular_Lines"
  - "topics/algebra/Linear_Functions"
  - "topics/pre_algebra/Graphing_Linear_Equations_From_Tables"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Slope"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "Given slope and intercept, slope and a point, or two points — write the equation of the line."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Writing Linear Equations

# Writing Linear Equations

Most line problems in algebra go in one of two directions. Either you are handed an equation and asked to draw or describe the line, or you are handed some facts about a line and asked to produce the equation. This page is about the second direction. Once you can turn a scrap of information — a slope, a point, two points — into a clean equation, you can go on to graph, intersect, and compare lines without friction.

The whole game comes down to choosing the right form and plugging numbers in carefully. You already know the two forms you need:

$$
y = mx + b \qquad \text{(slope-intercept form)}
$$

$$
y - y_1 = m(x - x_1) \qquad \text{(point-slope form)}
$$

The first is the final answer most problems want. The second is a scaffold: a convenient place to drop any point and any slope so you can simplify your way to the first.

---

## Key ideas

### Slope-intercept form

Slope-intercept form says everything about a line in two numbers. The letter $m$ is the slope — how steep the line climbs for every step to the right. The letter $b$ is the y-intercept — where the line crosses the vertical axis. If a problem hands you those two numbers directly, writing the equation is nearly instant.

### Point-slope form

Point-slope form is built for a different situation: you know the slope, and you know one point $(x_1, y_1)$ that sits on the line, but you do not yet know where the line meets the y-axis. Start from this form, simplify, and the missing y-intercept will appear on its own.

### Standard form

There is also a third form worth recognizing:

$$
Ax + By = C \qquad \text{(standard form)}
$$

where $A$, $B$, and $C$ are usually integers. Standard form is convenient for certain problems (like finding both intercepts quickly or lining up equations in a system), but it is almost never the natural starting place. Most of the time you will write the line in slope-intercept form first and convert at the end if standard form is requested.

### Three situations, three moves

There are really only three situations you have to be fluent in:

1. **Slope and y-intercept given.** Drop $m$ and $b$ straight into $y = mx + b$. Done.
2. **Slope and one point given.** Put $m$ and the point into point-slope form, then distribute and solve for $y$ to land in slope-intercept form.
3. **Two points given.** First compute the slope from the two points; then proceed as in situation 2.

Every textbook "write the equation" problem is one of those three.

---

## Example 1: Slope and y-intercept

> A line has slope $\dfrac{2}{5}$ and crosses the y-axis at $-7$. Find its equation in slope-intercept form.

This is the easiest case. Start from slope-intercept form:

$$
y = mx + b
$$

Substitute $m = \dfrac{2}{5}$ and $b = -7$:

$$
y = \dfrac{2}{5} x + (-7)
$$

Tidy the $+(-7)$ into a simple subtraction:

$$
y = \dfrac{2}{5} x - 7
$$

That is the final answer. Notice that because both pieces were handed to you, there was nothing to solve — just careful substitution.

---

## Example 2: Slope and a point (point-slope method)

> A line has slope $-4$ and goes through the point $(2, 9)$. Express its equation in slope-intercept form.

You have a slope but no y-intercept, so point-slope is the right scaffold. Begin with:

$$
y - y_1 = m(x - x_1)
$$

Substitute $m = -4$, $x_1 = 2$, $y_1 = 9$:

$$
y - 9 = -4(x - 2)
$$

Distribute the $-4$ on the right:

$$
y - 9 = -4x + 8
$$

Add $9$ to both sides so $y$ is alone:

$$
y = -4x + 17
$$

Done. The y-intercept $17$ was hiding in the algebra the whole time — point-slope let us pull it out. You can double-check by plugging the point $(2, 9)$ back in: $-4(2) + 17 = -8 + 17 = 9$. It matches, so the equation is right.

---

## Example 3: Two points

> A line passes through the two points $(-1, 8)$ and $(3, -4)$. Find its equation in slope-intercept form.

Two points give you enough information to pin down the line, but you are missing the slope, so build it first. The slope formula is just the change in $y$ over the change in $x$:

$$
m = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{-4 - 8}{3 - (-1)} = \dfrac{-12}{4} = -3
$$

Now the problem has collapsed into Example 2: slope $-3$, and a point (either one works — pick the one with smaller numbers). Using $(-1, 8)$:

$$
y - 8 = -3(x - (-1))
$$

$$
y - 8 = -3(x + 1)
$$

Distribute the $-3$:

$$
y - 8 = -3x - 3
$$

Add $8$ to both sides:

$$
y = -3x + 5
$$

Check by testing the other point, $(3, -4)$: $-3(3) + 5 = -9 + 5 = -4$. The second point lands on the line, so the equation is correct.

---

## Example 4 (optional): Converting to standard form

> Rewrite $y = \dfrac{2}{3}x - 4$ in standard form $Ax + By = C$ with integer coefficients.

Multiply everything by $3$ to clear the fraction:

$$
3y = 2x - 12
$$

Move the $x$ term to the left so the $x$ and $y$ terms share a side:

$$
-2x + 3y = -12
$$

Most textbooks prefer a positive leading coefficient on $x$. Multiply both sides by $-1$:

$$
2x - 3y = 12
$$

Same line, different dress.

---

## Common pitfalls

- **Mixing up the point coordinates in point-slope.** In $y - y_1 = m(x - x_1)$, the $y$-coordinate goes with $y$ and the $x$-coordinate goes with $x$. Swapping them is the single most common error on this topic.
- **Forgetting to distribute the slope.** After you substitute into point-slope, the slope has to be handed to **both** terms in the parentheses. Students often write $y - 8 = -3x + 1$ when the correct distribution is $y - 8 = -3x - 3$.
- **Leaving the equation stuck in point-slope form.** Unless the problem explicitly asks for point-slope, your final answer should usually be simplified to $y = mx + b$.
- **Skipping the slope step when given two points.** If you forget to compute the slope first, you have no $m$ to put in point-slope, and you are stuck. Two-point problems are always two steps: slope, then point-slope.

---

## Prerequisites

Before you practice writing equations, you should be solid on:

- [[Slope]] — computing slope from two points and from a graph
- [[Slope_Intercept_Form]] — reading $m$ and $b$ directly off an equation
- [[Multi_Step_Equations]] — the distribution and solving you'll do to simplify point-slope

If any of those feel shaky, start there and come back.

---

## Problems Involving Writing Linear Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="writing_linear_equations"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Slope]]
- [[Slope_Intercept_Form]]
- [[Parallel_And_Perpendicular_Lines]]
- [[Linear_Functions]]
- [[Graphing_Linear_Equations_From_Tables]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
