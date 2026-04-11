---
title: "Parallel and Perpendicular Lines"
type: topic
aliases: ["Slopes of Parallel Lines", "Slopes of Perpendicular Lines", "Negative Reciprocal Slopes"]
tags: ["#branch-algebra-1", "#topic-linear", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "4", section: "4.5"}
related:
  - "topics/algebra/Slope"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Linear_Functions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Slope"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/algebra/Writing_Linear_Equations"
problem_type_ids: []
figures: ["algebra/parallel_perpendicular_lines.svg"]
summary: "Parallel lines have equal slopes; perpendicular lines have slopes whose product is -1."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Parallel and Perpendicular Lines

# Parallel and Perpendicular Lines

Two lines in the plane can do three things: they can cross at some angle, cross at a right angle, or never meet at all. The ones that never meet are called **parallel**; the ones that cross at a right angle are called **perpendicular**. What is remarkable is that both of these geometric relationships show up cleanly in the **slopes** of the lines. You do not have to graph anything, measure angles, or draw careful figures — you just look at $m$.

![[parallel_perpendicular_lines.svg|Parallel and perpendicular lines in the coordinate plane]]

The two rules you need are short enough to memorize today:

$$
\text{Parallel:} \qquad m_1 = m_2
$$

$$
\text{Perpendicular:} \qquad m_1 \cdot m_2 = -1
$$

That is it. The rest of the page is about what those two rules let you compute.

---

## Key ideas

### Parallel means same slope

Parallel lines climb at exactly the same rate. If one line rises $3$ units for every step to the right, a parallel line also rises $3$ units for every step to the right. Because the rise is the same, the two lines stay an equal vertical distance apart forever and never meet. In symbols, if two non-vertical lines have slopes $m_1$ and $m_2$, they are parallel exactly when $m_1 = m_2$. (Vertical lines, which have undefined slope, are also parallel to each other, but you should handle that case visually rather than with the formula.)

The y-intercepts do **not** have to match. The parallel lines $y = 2x + 1$ and $y = 2x - 7$ have the same slope $2$ but sit at different heights on the y-axis. The slopes being equal is the whole condition; the intercepts are free.

### Perpendicular means negative reciprocal slopes

Perpendicular is a sharper condition. Two non-vertical lines meet at a right angle exactly when their slopes multiply to give $-1$:

$$
m_1 \cdot m_2 = -1
$$

Solve that equation for $m_2$ and you get the same statement in a more usable form:

$$
m_2 = -\dfrac{1}{m_1}
$$

In words, you get the slope of a perpendicular line by flipping the original slope upside down **and** changing its sign. Mathematicians call this the **negative reciprocal**. So if a line has slope $\dfrac{4}{5}$, a perpendicular line has slope $-\dfrac{5}{4}$. If a line has slope $-6$, a perpendicular line has slope $\dfrac{1}{6}$. A horizontal line (slope $0$) is perpendicular to a vertical line (slope undefined), and that is the one case the formula cannot describe — treat it as a special exception.

### Putting it to work

Once you know the slope relationships, two kinds of problems become routine:

1. **Writing a new equation.** Given a line and a point, write the equation of a parallel or perpendicular line through that point.
2. **Classifying two given lines.** Given two equations, decide whether the lines they describe are parallel, perpendicular, or neither.

Both problem types reduce to comparing slopes and then, if needed, running the point-slope procedure from [[Writing_Linear_Equations]].

---

## Example 1: Writing a parallel line

> Find an equation in slope-intercept form for the line that runs parallel to $y = \dfrac{1}{3}x + 6$ and passes through $(9, 4)$.

The given line has slope $\dfrac{1}{3}$. A parallel line must have the **same** slope, so the new line also has slope $\dfrac{1}{3}$. Now I know a slope and a point, which is exactly the setup for point-slope form:

$$
y - y_1 = m(x - x_1)
$$

Substitute $m = \dfrac{1}{3}$, $x_1 = 9$, $y_1 = 4$:

$$
y - 4 = \dfrac{1}{3}(x - 9)
$$

Distribute the $\dfrac{1}{3}$ on the right:

$$
y - 4 = \dfrac{1}{3}x - 3
$$

Add $4$ to both sides to isolate $y$:

$$
y = \dfrac{1}{3}x + 1
$$

The original line had intercept $6$, and the parallel line has intercept $1$ — they are parallel (same slope) but sit at different heights, which is exactly what the picture should look like.

---

## Example 2: Writing a perpendicular line

> A line runs perpendicular to $y = -2x + 5$ and goes through $(4, -1)$. Give its equation in slope-intercept form.

The given line has slope $-2$. The perpendicular line needs the negative reciprocal of $-2$. Flip $-2$ to $-\dfrac{1}{2}$, then change the sign:

$$
m_{\perp} = -\dfrac{1}{-2} = \dfrac{1}{2}
$$

Sanity check: $(-2) \cdot \dfrac{1}{2} = -1$, which is exactly the perpendicular condition. Good.

Now use point-slope with $m = \dfrac{1}{2}$ and the point $(4, -1)$:

$$
y - (-1) = \dfrac{1}{2}(x - 4)
$$

$$
y + 1 = \dfrac{1}{2}x - 2
$$

Subtract $1$ from both sides:

$$
y = \dfrac{1}{2}x - 3
$$

That is the equation of the perpendicular line through the given point.

---

## Example 3: Classify two given lines

> For each pair, decide whether the two lines are parallel, perpendicular, or neither.
>
> (a) $y = 5x - 2$ and $y = 5x + 9$
> (b) $y = \dfrac{3}{4}x + 1$ and $y = -\dfrac{4}{3}x - 6$
> (c) $y = -x + 4$ and $y = x + 4$

The strategy is the same every time: read off the slopes, then compare.

**(a)** Both slopes are $5$. Because $m_1 = m_2$, the lines are **parallel**. The intercepts $-2$ and $9$ are different, so they are distinct parallel lines (not the same line).

**(b)** The slopes are $\dfrac{3}{4}$ and $-\dfrac{4}{3}$. Check the product:

$$
\dfrac{3}{4} \cdot \left(-\dfrac{4}{3}\right) = -\dfrac{12}{12} = -1
$$

The product is $-1$, so the lines are **perpendicular**. Another way to see it: flipping $\dfrac{3}{4}$ gives $\dfrac{4}{3}$, and changing the sign gives $-\dfrac{4}{3}$ — that is the second slope exactly.

**(c)** The slopes are $-1$ and $1$. They are not equal, so the lines are not parallel. Check the perpendicular product: $(-1)(1) = -1$. The product is $-1$, so the lines are **perpendicular**. (This one is fun: $y = x$ and $y = -x$ meet at the origin and make a perfect X, exactly the right angle the rule predicts.)

---

## Common pitfalls

- **Forgetting to flip AND change the sign.** Perpendicular slopes need both steps. The perpendicular slope of $\dfrac{2}{7}$ is not $\dfrac{7}{2}$ (that is only the reciprocal) and not $-\dfrac{2}{7}$ (that is only the sign change). It is $-\dfrac{7}{2}$.
- **Thinking the intercepts have to match.** Parallel means equal slopes, nothing more. The y-intercepts are usually different — in fact, if the intercepts were also equal the lines would be identical, not just parallel.
- **Not converting to slope-intercept form first.** If a line is written as $3x + 2y = 10$, you cannot just stare at the numbers and read off the slope. Solve for $y$ first: $y = -\dfrac{3}{2}x + 5$, so the slope is $-\dfrac{3}{2}$.
- **Treating horizontal and vertical lines with the formula.** A horizontal line has slope $0$ and a vertical line has undefined slope. They are perpendicular to each other, but you cannot check that with the "product equals $-1$" rule (you cannot multiply by undefined). Recognize this case by sight.

---

## Prerequisites

Before you tackle practice problems, make sure you're comfortable with:

- [[Slope]] — computing and comparing slopes
- [[Slope_Intercept_Form]] — reading the slope out of an equation
- [[Writing_Linear_Equations]] — the point-slope machinery you'll reuse here

---

## Problems Involving Parallel and Perpendicular Lines

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="parallel_and_perpendicular_lines"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Slope]]
- [[Slope_Intercept_Form]]
- [[Writing_Linear_Equations]]
- [[Linear_Functions]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
