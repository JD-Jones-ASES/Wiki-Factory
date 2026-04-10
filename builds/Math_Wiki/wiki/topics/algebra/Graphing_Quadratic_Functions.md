---
title: "Graphing Quadratic Functions"
type: topic
aliases: ["Parabola Graph", "Quadratic Graph"]
tags: ["#branch-algebra-1", "#topic-quadratics", "#skill-visualization", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "8", section: "8.5"}
related:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/The_Discriminant"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Parabolas"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Quadratic_Functions"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
problem_type_ids: []
figures: ["algebra/parabola_vertex_axis_of_symmetry.svg"]
summary: "Sketch the parabola y = ax² + bx + c by finding the vertex with x = -b/(2a), plotting the y-intercept and its symmetric partner, and using the sign and size of a to set direction and width."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Graphing Quadratic Functions

# Graphing Quadratic Functions

Every quadratic function $y = ax^2 + bx + c$ draws the same family of curves: a smooth, symmetric U-shape called a **parabola**. Change the coefficients and you stretch, flip, or slide the U around the plane, but the shape itself never breaks. That is a huge pedagogical win — once you can sketch one parabola, you can sketch all of them, because you are really just finding the same handful of key points every time.

The trick is knowing which points to plot. You do **not** need a big table of thirty $(x, y)$ pairs. Five carefully chosen points — sometimes just three — are enough for a clean sketch, because the symmetry of the parabola lets each point you plot work double-duty.

![[parabola_vertex_axis_of_symmetry.svg|A parabola with vertex, axis of symmetry, and intercepts labeled]]

---

## Key features in one place

Before we touch an example, let us pin down the vocabulary you will use on every problem.

**Direction of opening** — controlled by the sign of $a$.
- If $a > 0$, the parabola opens **upward** like a valley. The vertex sits at the bottom of the curve, which makes it the function's minimum value.
- If $a < 0$, the parabola opens **downward** like a hill. The vertex sits at the top of the curve, which makes it the function's maximum value.

**Width** — controlled by the size of $|a|$.
- If $|a| > 1$, the parabola is **narrower** than the parent $y = x^2$. Larger $|a|$ means a tighter squeeze.
- If $0 < |a| < 1$, the parabola is **wider** than the parent.
- When $|a| = 1$, the width matches the parent $y = x^2$ exactly, though the curve may still be flipped or shifted.

**The vertex** — the single turning point of the curve. Its $x$-coordinate is

$$
x_v = -\dfrac{b}{2a},
$$

and you get its $y$-coordinate by plugging that number back into the function:

$$
y_v = f(x_v) = a x_v^2 + b x_v + c.
$$

**Axis of symmetry** — a vertical mirror line running through the vertex, with equation $x = x_v = -\dfrac{b}{2a}$. Every point on the parabola has a partner point on the other side of this line at the same height.

**$y$-intercept** — always the constant term. Set $x = 0$ and you get $y = c$, so the parabola crosses the $y$-axis at $(0, c)$. This is essentially free — no work required.

**$x$-intercepts (roots)** — the places where $y = 0$, found by solving $ax^2 + bx + c = 0$. You can use [[Solving_Quadratics_By_Factoring|factoring]], [[The_Quadratic_Formula|the quadratic formula]], or [[Solving_Quadratics_By_Square_Roots|taking square roots]] depending on the form. [[The_Discriminant|The discriminant]] $b^2 - 4ac$ tells you up front how many $x$-intercepts the graph will actually show — two, one, or none.

---

## The three-point workflow

Here is the fastest way to turn a formula into a sketch:

1. Compute $x_v = -\dfrac{b}{2a}$. This is the axis of symmetry and the vertex's $x$-coordinate.
2. Plug $x_v$ into the function to get $y_v$. Plot the vertex $(x_v, y_v)$.
3. Mark the $y$-intercept $(0, c)$. Its mirror image across the axis of symmetry lives at $(2x_v, c)$. Plot both — you now have three points, spaced symmetrically.
4. If you want more accuracy, solve $ax^2 + bx + c = 0$ for the $x$-intercepts and plot them too.
5. Connect the dots with a smooth U (up or down, depending on the sign of $a$).

Three points plus the direction of opening is enough to draw a passable parabola. Five points makes it nearly perfect.

---

## Example 1: a plain upward parabola

> Sketch the parabola $y = x^2 - 4x + 3$. Identify the vertex, the line of symmetry, the direction of opening, the $y$-intercept, and the $x$-intercepts.

Read off the coefficients: $a = 1$, $b = -4$, $c = 3$.

**Direction of opening.** Since $a = 1 > 0$, the U opens **upward** and the vertex is a minimum.

**Vertex.** Compute the $x$-coordinate:

$$
x_v = -\dfrac{b}{2a} = -\dfrac{-4}{2(1)} = \dfrac{4}{2} = 2.
$$

Now plug $x = 2$ into the original expression to find $y_v$:

$$
y_v = (2)^2 - 4(2) + 3 = 4 - 8 + 3 = -1.
$$

So the vertex is $(2, -1)$, and the symmetry line is $x = 2$.

**$y$-intercept.** The constant $c = 3$, so the curve crosses the $y$-axis at $(0, 3)$. No work there.

**Symmetric partner of the $y$-intercept.** The axis of symmetry is $x = 2$, and the $y$-intercept sits at $x = 0$, which is $2$ units to the left. Reflect across the axis to find its twin $2$ units to the right, at $x = 4$:

$$
y(4) = (4)^2 - 4(4) + 3 = 16 - 16 + 3 = 3.
$$

The mirror point is $(4, 3)$, just as symmetry promised.

**$x$-intercepts.** Set $y = 0$ and solve:

$$
x^2 - 4x + 3 = 0 \implies (x - 1)(x - 3) = 0,
$$

so $x = 1$ or $x = 3$. The parabola crosses the $x$-axis at $(1, 0)$ and $(3, 0)$. (A quick sanity check: these two points are symmetric about $x = 2$, which they should be.)

**Sketch.** You now have five points — $(0, 3)$, $(1, 0)$, $(2, -1)$, $(3, 0)$, $(4, 3)$ — arranged symmetrically around the vertex. Connect them with a smooth upward U and you are done.

---

## Example 2: a downward parabola

> Describe the parabola $y = -x^2 + 6x - 5$ and sketch its graph.

Now $a = -1$, $b = 6$, $c = -5$.

**Direction of opening.** Because $a = -1 < 0$, this parabola opens **downward** — the vertex will sit at the top of the curve instead of the bottom.

**Vertex.** Use the same formula:

$$
x_v = -\dfrac{b}{2a} = -\dfrac{6}{2(-1)} = -\dfrac{6}{-2} = 3.
$$

Substitute $x = 3$ into the function:

$$
y_v = -(3)^2 + 6(3) - 5 = -9 + 18 - 5 = 4.
$$

The vertex is $(3, 4)$ and the symmetry line is $x = 3$. Because the parabola opens downward, $y = 4$ is the **maximum value** of this function — no point on the curve rises higher.

**$y$-intercept.** $y(0) = -5$, so the curve passes through $(0, -5)$. Its mirror image across $x = 3$ is at $x = 6$, and $y(6) = -36 + 36 - 5 = -5$, which confirms the partner point $(6, -5)$.

**$x$-intercepts.** Solve $-x^2 + 6x - 5 = 0$. Multiply both sides by $-1$ to clean up the leading coefficient: $x^2 - 6x + 5 = 0$, which factors as $(x - 1)(x - 5) = 0$. So $x = 1$ or $x = 5$, and the parabola crosses the $x$-axis at $(1, 0)$ and $(5, 0)$.

**Sketch.** Plot the five points and connect them with a downward U. Notice how flipping the sign of $a$ flipped the whole curve upside down — the vertex moved from the bottom of the picture to the top, and the parabola now falls away on either side instead of rising.

---

## Example 3: a narrower parabola

> Find the key features of $y = 2x^2 - 8x + 3$ and sketch the curve.

Here $a = 2$, $b = -8$, $c = 3$.

**Direction and width.** $a = 2 > 0$, so the parabola opens upward. More importantly, $|a| = 2 > 1$, which means the curve is **narrower** than the parent $y = x^2$ — it climbs faster and forms a tighter U.

**Vertex.**

$$
x_v = -\dfrac{-8}{2(2)} = \dfrac{8}{4} = 2.
$$

$$
y_v = 2(2)^2 - 8(2) + 3 = 8 - 16 + 3 = -5.
$$

Vertex: $(2, -5)$. Symmetry line: $x = 2$.

**$y$-intercept.** $y(0) = 3$, giving $(0, 3)$. Its symmetric partner across $x = 2$ is at $x = 4$, where $y(4) = 32 - 32 + 3 = 3$, so $(4, 3)$.

**$x$-intercepts.** Checking $\Delta = b^2 - 4ac = 64 - 24 = 40$ first tells us the parabola *does* cross the $x$-axis (since $\Delta > 0$), but because $40$ is not a perfect square the roots will be irrational — so [[Solving_Quadratics_By_Factoring|factoring]] is out and we reach for [[The_Quadratic_Formula|the quadratic formula]]:

$$
x = \dfrac{8 \pm \sqrt{40}}{4} = \dfrac{8 \pm 2\sqrt{10}}{4} = 2 \pm \dfrac{\sqrt{10}}{2}.
$$

Numerically that comes out to $x \approx 0.42$ and $x \approx 3.58$, so the $x$-intercepts are roughly $(0.42, 0)$ and $(3.58, 0)$. They are symmetric about $x = 2$, as required.

**Sketch.** The curve dips down to $(2, -5)$ and climbs back up steeply on both sides. Compared to Example 1, this parabola is clearly narrower — at $x = 0$ and $x = 4$, the height is already $+3$, whereas the Example 1 parabola only reached $y = 3$ way out at $x = 0$ and $x = 4$ because $|a|$ was smaller there. Bigger $|a|$ means a steeper climb out of the vertex.

---

## Common pitfalls

- **Dropping a minus sign in $-\tfrac{b}{2a}$.** Remember that the formula has a negative sign *outside* the fraction. If $b$ is already negative, the two minuses cancel and you get a positive $x_v$. Writing it as $x_v = -\dfrac{b}{2a}$ and computing carefully, step by step, prevents the slip.
- **Forgetting to plug $x_v$ back in to find $y_v$.** Many students stop after computing $x_v$ and treat that as the vertex. The vertex is a point $(x_v, y_v)$ — two coordinates — not a single number.
- **Drawing the U the wrong way up.** Always check the sign of $a$ *before* you sketch. If $a > 0$ the arms of the parabola point up; if $a < 0$ they point down. A quick glance at the leading coefficient saves an embarrassing redraw.
- **Assuming every parabola has $x$-intercepts.** When [[The_Discriminant|the discriminant]] is negative, the curve never crosses the $x$-axis. Leave those out of your sketch rather than inventing imaginary crossings.
- **Using only the vertex.** One point plus a shape is not a sketch. Always add at least the $y$-intercept and its symmetric partner so you know how wide the arms of the curve are.

---

## Prerequisites

Before you tackle practice problems here, make sure you are comfortable with:

- [[Quadratic_Functions]] — recognizing the standard form $y = ax^2 + bx + c$ and reading off its coefficients.
- [[Plotting_Points_And_The_Coordinate_Plane|Plotting points]] — nothing we do here works if the coordinate plane still feels unfamiliar.
- [[Solving_Quadratics_By_Factoring]] — the fastest route to $x$-intercepts when the trinomial is factorable.
- [[The_Quadratic_Formula]] — the backup route when factoring fails.
- [[The_Discriminant]] — to predict in advance how many $x$-intercepts the parabola will actually show.

---

## Problems Involving Graphing Quadratic Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphing_quadratic_functions"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Quadratic_Functions]]
- [[The_Quadratic_Formula]]
- [[The_Discriminant]]
- [[Solving_Quadratics_By_Factoring]]
- [[Completing_The_Square]]
- [[Parabolas]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
