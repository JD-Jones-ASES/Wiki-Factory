---
title: "Absolute Value Functions"
type: topic
aliases: ["Absolute Value Function", "AbsoluteValueFunctions", "V-Shape Function"]
tags: ["#branch-algebra-2", "#topic-functions", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "4", section: "4.1"}
  - {book: "algtrig", chapter: "2", section: "2.1"}
related:
  - "topics/algebra/Absolute_Value_Equations"
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/pre_algebra/Absolute_Value_And_Opposites"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
  - "topics/algebra/Transformations_Ii_Stretches_Compressions_And_Combined"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/pre_algebra/Absolute_Value_And_Opposites"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: []
summary: "f(x) = |x| is a V-shape with vertex at the origin; the form a|x - h| + k slides, stretches, and flips it."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Absolute Value Functions

# Absolute Value Functions

The **absolute value function** is the cleanest example of a graph that is not a line, not a parabola, and not a curve — it is made of two straight pieces glued together. Its parent form is

$$
f(x) = |x|,
$$

and its graph is a perfect **V** with the point of the V at the origin. One branch heads up and to the right; the other branch heads up and to the left; the two meet at $(0, 0)$ without any curvature whatsoever.

Why is the shape a V? Because the rule $|x|$ itself does two different things on two different sides of zero. If you feed it a nonnegative input, it returns the input unchanged. If you feed it a negative input, it returns the input with the sign flipped so the result comes out positive. The rule is therefore **piecewise**:

$$
|x| = \begin{cases} x & \text{when } x \geq 0, \\ -x & \text{when } x < 0. \end{cases}
$$

Look carefully. On the right half of the coordinate plane the rule is literally $y = x$ — the line through the origin with slope $1$. On the left half the rule is $y = -x$ — the line through the origin with slope $-1$. Each half of the V is just a line, and they happen to meet at the origin because both halves evaluate to $0$ there. The V-shape is not a decorative quirk; it is the visible seam where the two formulas switch.

The **domain** of $f(x) = |x|$ is every real number — you can feed it anything. The **range** is $y \geq 0$, since absolute value never produces a negative output. The graph lives entirely on or above the $x$-axis.

---

## Key ideas

- **The vertex is the corner of the V.** Every absolute value graph has one sharp point where the two lines meet. For the parent $f(x) = |x|$, that corner sits at the origin. When the function is transformed, the corner moves.
- **Both branches are straight.** Absolute value graphs do not curve. Each branch is a line, which means the slope is constant on each side of the vertex and the two slopes are opposites of each other (one positive, one negative).
- **Axis of symmetry through the vertex.** A vertical line drawn through the corner cuts the V into mirror halves. For $f(x) = |x|$, that line is $x = 0$; for a shifted V, the axis moves with the vertex.
- **Opens up or opens down.** The parent points upward like a mountain valley. Multiplying the absolute value by a negative number tips the whole V upside down so it opens downward instead, like a mountain peak.
- **Output is never negative (for the parent).** The output of $|x|$ on its own is always $\geq 0$. You can only push the graph below the $x$-axis by multiplying by a negative number or by subtracting a positive constant.

---

## The transformed form: $a|x - h| + k$

Once you know the V-shape of the parent, you can build any absolute value graph with three dials:

$$
f(x) = a \, |x - h| + k.
$$

Each letter controls exactly one thing.

- **$h$ shifts the corner left or right.** The vertex moves from the origin to $x = h$. Watch the sign: the expression is $x - h$, so a graph of $|x - 4|$ has its corner at $x = 4$, while $|x + 3| = |x - (-3)|$ has its corner at $x = -3$. The sign of $h$ is the opposite of what the expression literally shows. (This is the same sign trick as [[Parabolas|parabolas]] and [[Square_Root_Functions|square root functions]].)
- **$k$ shifts the corner up or down.** Adding $k$ on the outside lifts the whole V by $k$ units; a negative $k$ drops it. The corner ends up at the height $k$ above (or below) the $x$-axis.
- **$a$ stretches and flips.** The absolute value of $a$ controls steepness: if $|a| > 1$, the V is narrower and climbs faster; if $|a| < 1$, the V is wider and climbs more gradually. The sign of $a$ controls orientation: a positive $a$ opens upward and a negative $a$ flips the V upside down.

Putting it all together: the vertex of $a|x - h| + k$ is always the point $(h, k)$. The axis of symmetry is the vertical line $x = h$. If $a > 0$, the range is $y \geq k$ (the corner is the lowest point). If $a < 0$, the range is $y \leq k$ (the corner is the highest point). The domain is always every real number.

---

## Example 1: graphing the parent function

> Sketch $f(x) = |x|$ by tabulating a handful of inputs. What are its vertex, axis of symmetry, domain, and range?

Build a short table of inputs that straddle the origin so you can see both halves of the V.

| $x$   | $|x|$ | Rule used |
|-------|-------|-----------|
| $-3$  | $3$   | $-x$ branch: $-(-3) = 3$ |
| $-2$  | $2$   | $-x$ branch |
| $-1$  | $1$   | $-x$ branch |
| $0$   | $0$   | either branch gives $0$ |
| $1$   | $1$   | $x$ branch |
| $2$   | $2$   | $x$ branch |
| $3$   | $3$   | $x$ branch |

Plot the seven points and connect them. You will see that the left three points lie on the line $y = -x$ (slope $-1$) and the right three points lie on the line $y = x$ (slope $+1$), with the two halves meeting at $(0, 0)$. That sharp meeting point is the **vertex**.

- **Vertex:** $(0, 0)$.
- **Axis of symmetry:** $x = 0$ (the $y$-axis). Reflecting any point on the right branch across this line lands on the matching point of the left branch.
- **Domain:** all real numbers, $(-\infty, \infty)$. You can plug in anything.
- **Range:** $[0, \infty)$. The output bottoms out at $0$ and grows forever as $x$ moves away from the origin in either direction.

---

## Example 2: reading the vertex and direction from a formula

> For $g(x) = -2|x - 3| + 4$, identify the vertex, the direction the V opens, the axis of symmetry, and the range. Describe how the graph differs from the parent.

Match the given formula to the general form $a|x - h| + k$ term by term. Here $a = -2$, $h = 3$, and $k = 4$.

**Vertex.** The corner always sits at $(h, k)$, so it is at $(3, 4)$. Notice that the expression inside the bars is $x - 3$, and $h$ comes out as $+3$, not $-3$ — the sign is the opposite of what the literal expression shows.

**Direction.** Since $a = -2$ is negative, the whole V is flipped upside down. The parent opens upward; this one opens downward. The vertex is therefore the **highest** point of the graph, not the lowest.

**Axis of symmetry.** A vertical line through the vertex: $x = 3$.

**Range.** Because the V opens downward from its peak at height $4$, every output is at or below $4$. In interval notation the range is $(-\infty, 4]$.

**How it differs from the parent.** Relative to $|x|$, the graph has been shifted right $3$ units (by $h = 3$), shifted up $4$ units (by $k = 4$), reflected across the horizontal line $y = 4$ (because $a$ is negative), and made twice as steep (because $|a| = 2$). The branches now have slopes $-2$ on the right and $+2$ on the left, the negatives of what they would be for the parent.

As a quick sanity check, evaluate one point. Plug in $x = 4$:

$$
g(4) = -2|4 - 3| + 4 = -2(1) + 4 = 2.
$$

So $(4, 2)$ is on the graph — one unit to the right of the vertex, and two units down, exactly matching the slope of $-2$ along that branch.

---

## Example 3: sketching a transformed V from scratch

> Graph $h(x) = |x + 2| - 3$ by plotting the vertex first and then one more point on each branch.

Rewrite $|x + 2|$ as $|x - (-2)|$ so the form matches $a|x - h| + k$ cleanly. The parameters are $a = 1$, $h = -2$, $k = -3$.

**Step 1: plot the vertex.** The corner goes at $(h, k) = (-2, -3)$. Mark that point on your axes.

**Step 2: use the slopes.** Because $a = 1$, the right branch rises with slope $+1$ and the left branch rises with slope $-1$ — exactly the parent slopes, unshifted. From the vertex, step one unit to the right and one unit up to get the point $(-1, -2)$. Step one unit to the left and one unit up from the vertex to get $(-3, -2)$.

**Step 3: extend the branches.** Keep walking the same slope pattern. Two units right and two units up from the vertex gives $(0, -1)$. Three units right and three up gives $(1, 0)$, which is the **x-intercept** on the right side of the graph. Symmetrically, three units left and three up gives $(-5, 0)$, the other x-intercept.

Connect the vertex to your plotted points with straight segments and extend past them — you should see a clean V sitting $3$ units below and $2$ units left of where the parent V would sit, with its corner at $(-2, -3)$ and both branches eventually crossing the $x$-axis.

- **Vertex:** $(-2, -3)$.
- **Axis of symmetry:** $x = -2$.
- **Domain:** all real numbers.
- **Range:** $y \geq -3$ (the V opens upward from its vertex at height $-3$).

---

## Common pitfalls

- **Flipping the sign of $h$.** The form is $|x - h|$, so $|x + 5|$ has $h = -5$ and the vertex slides **left**, not right. Writing the expression as $|x - (-5)|$ before reading off $h$ kills this mistake.
- **Treating $|x| = -x$ as a contradiction.** When $x$ is already negative, $-x$ is positive (the opposite of a negative is positive). The rule is not saying absolute values come out negative — it is saying you flip the sign of a negative input to make the result positive.
- **Drawing a curve instead of straight lines.** Absolute value graphs never curve. Each branch is perfectly straight, and the transition happens abruptly at the vertex. If your sketch looks rounded near the bottom of the V, fix it.
- **Confusing the function with the equation.** The equation $|x - 1| = 3$ is solved in [[Absolute_Value_Equations]] and produces a pair of solutions ($x = 4$ and $x = -2$). This page is about the whole graph — the set of all points $(x, |x - 1|)$ — not about intersecting it with a specific horizontal line.

---

## Prerequisites

Make sure these are comfortable before you practice:

- [[Relations_And_Functions]] — to be sure what a function's graph means
- [[Function_Basics]] — notation, domain, range, reading a rule as a table
- [[Absolute_Value_And_Opposites]] — the number-line meaning of $|x|$ as distance from zero
- [[Linear_Functions]] — each branch of a V is a line, so slope-reading skills carry over

---

## Problems Involving Absolute Value Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="absolute_value_functions"></div>

---

## See Also

- [[Absolute_Value_Equations]]
- [[Absolute_Value_Inequalities]]
- [[Transformations_I_Shifts_And_Reflections]]
- [[Transformations_Ii_Stretches_Compressions_And_Combined]]
- [[Quadratic_Functions]]
- [[Linear_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
