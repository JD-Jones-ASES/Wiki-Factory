---
title: "Systems of Linear Inequalities"
type: topic
aliases: ["System of Inequalities", "Graphing Systems of Inequalities", "Feasible Region"]
tags: ["#branch-algebra-1", "#topic-systems", "#topic-inequalities"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "5", section: "5.5"}
related:
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Solving_Systems_By_Graphing"
  - "topics/algebra/Solving_Systems_By_Substitution"
  - "topics/algebra/Solving_Systems_By_Elimination"
  - "topics/pre_algebra/Slope_Intercept_Form"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: []
summary: "Graph each inequality as a half-plane and take the overlap — the solution is the intersection region."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Systems of Linear Inequalities

# Systems of Linear Inequalities

A single linear inequality like $y < 2x + 1$ is not satisfied by just one point — it is satisfied by a whole *region*, half the coordinate plane cut off by a boundary line. A **system of linear inequalities** puts two or more of those half-plane constraints together at the same time, and asks you to find the ordered pairs that make *every* inequality true at once. Graphically, each inequality paints a half-plane; the solution is wherever all the paint overlaps.

In plain language: solving a system of inequalities means finding the region where every rule is obeyed simultaneously.

---

## What a solution looks like

A **solution** of a system of linear inequalities is any ordered pair $(x, y)$ that turns every inequality in the system into a true statement. The collection of all such ordered pairs is called the **solution region** (sometimes called the **feasible region** in word problems). It is the intersection — the common overlap — of the half-planes carved out by the individual inequalities.

Unlike a system of *equations*, where the answer is usually a single point, a system of *inequalities* has infinitely many solutions. Any point inside the overlapping region is a solution, and any point outside is not.

---

## How to graph one inequality

Before you can graph a system, you need to graph each inequality on its own. The recipe:

1. **Rewrite the inequality in slope-intercept form** if it isn't already, so you can see the boundary line $y = mx + b$ clearly.
2. **Graph the boundary line.** The style of the line depends on the inequality symbol:
   - Use a **solid line** for $\leq$ or $\geq$, because points on the boundary itself *are* solutions.
   - Use a **dashed line** for $<$ or $>$, because points exactly on the boundary are *not* solutions.
3. **Pick a test point** that is not on the line. The origin $(0, 0)$ is usually the fastest choice, unless the line runs through it.
4. **Plug the test point into the original inequality.** If it produces a true statement, shade the side of the line that contains the test point. If it produces a false statement, shade the other side.

The shaded half-plane (together with the line itself, if it is solid) is the graph of that one inequality.

---

## How to graph a system

To graph a whole system, graph each inequality on the *same* set of axes using the steps above. The region where all the shadings overlap is the solution region. If it helps, use a lighter tint or a different shading direction for each inequality so the overlap stands out.

A couple of edge cases to watch:

- If the shaded regions overlap on a line segment but not in an area, the "solution region" collapses onto the line.
- If the shadings never overlap at all — for example, two parallel boundary lines shaded in opposite directions — the system has **no solution**.

---

## Example 1: a first system with two strict inequalities

> Graph the solution region of the system
> $$
> \begin{cases}
> y > x - 2 \\
> y < -x + 4
> \end{cases}
> $$

**Step 1: graph the first boundary.** The boundary line for $y > x - 2$ is $y = x - 2$. It has slope $1$ and $y$-intercept $-2$. Draw it as a **dashed line** because the symbol is strict ($>$). Test $(0, 0)$: is $0 > 0 - 2 = -2$? Yes, $0 > -2$ is true, so shade the side of the line that contains the origin — the region *above* the dashed line.

**Step 2: graph the second boundary.** The boundary for $y < -x + 4$ is $y = -x + 4$. It has slope $-1$ and $y$-intercept $4$. Draw it as a **dashed line** as well ($<$ is strict). Test $(0, 0)$: is $0 < -0 + 4 = 4$? Yes, so shade the side containing the origin — the region *below* this second dashed line.

**Step 3: take the overlap.** The solution region is the set of points that sit above the first dashed line *and* below the second dashed line at the same time. That overlap is a wedge-shaped region opening to the right, with vertex where the two lines cross. Setting $x - 2 = -x + 4$ gives $2x = 6$, so $x = 3$ and $y = 1$. The two boundary lines meet at $(3, 1)$, but since both are dashed that corner point is **not** part of the solution.

Any interior point, such as $(1, 1)$, is a solution: check $1 > 1 - 2 = -1$ (true) and $1 < -1 + 4 = 3$ (true).

---

## Example 2: mixing strict and non-strict symbols

> Graph the solution region of the system
> $$
> \begin{cases}
> y \geq \tfrac{1}{2}x + 1 \\
> y < -2x + 6
> \end{cases}
> $$

**First inequality.** The boundary is $y = \tfrac{1}{2}x + 1$, a line with slope $\tfrac{1}{2}$ and $y$-intercept $1$. The symbol $\geq$ is non-strict, so draw a **solid line**. Test $(0, 0)$: is $0 \geq \tfrac{1}{2}(0) + 1 = 1$? No, $0 \geq 1$ is false. So shade the side *away* from the origin — the region above the solid line.

**Second inequality.** The boundary is $y = -2x + 6$, with slope $-2$ and $y$-intercept $6$. The symbol $<$ is strict, so use a **dashed line**. Test $(0, 0)$: is $0 < -2(0) + 6 = 6$? Yes, so shade the side containing the origin — below the dashed line.

**Overlap.** The solution region is the wedge that is simultaneously above the solid line and below the dashed line. Points on the solid boundary that also lie below the dashed boundary *are* solutions; points on the dashed line itself are *not*.

Quick test with $(1, 3)$: check $3 \geq \tfrac{1}{2}(1) + 1 = 1.5$ (true) and $3 < -2(1) + 6 = 4$ (true). So $(1, 3)$ is a solution.

This example shows why the line styles matter. A solid boundary is part of the answer set; a dashed boundary is a wall, not a door.

---

## Example 3: a feasible-region word problem

> A student has at most $\$20$ to spend on notebooks and pens. Notebooks cost $\$4$ each and pens cost $\$1$ each. The student wants to buy **at least** $3$ items total. If $x$ is the number of notebooks and $y$ is the number of pens, write a system of inequalities that describes the student's choices and describe the feasible region.

**Write the inequalities.** Translate each constraint into symbols.

- "At most $\$20$ to spend" gives $4x + y \leq 20$.
- "At least $3$ items total" gives $x + y \geq 3$.
- You cannot buy a negative number of anything, so also $x \geq 0$ and $y \geq 0$.

That gives the system
$$
\begin{cases}
4x + y \leq 20 \\
x + y \geq 3 \\
x \geq 0 \\
y \geq 0
\end{cases}
$$

**Graph each boundary.** Every inequality here uses $\leq$ or $\geq$, so every boundary line is **solid**. The non-negativity conditions $x \geq 0$ and $y \geq 0$ trap the picture inside the first quadrant (plus the two positive axes).

- $4x + y = 20$ passes through $(5, 0)$ and $(0, 20)$. Test $(0, 0)$: $4(0) + 0 = 0 \leq 20$, true, so shade below this line.
- $x + y = 3$ passes through $(3, 0)$ and $(0, 3)$. Test $(0, 0)$: $0 + 0 = 0 \geq 3$, false, so shade *above* this line.

**The feasible region.** The overlap is a four-sided region in the first quadrant, bounded below-left by the line $x + y = 3$ and above-right by $4x + y = 20$, and trapped between the axes. Any integer point inside the region — for example $(2, 4)$, meaning $2$ notebooks and $4$ pens — is a combination the student can actually afford while still buying at least $3$ things. Quick check: $4(2) + 4 = 12 \leq 20$ and $2 + 4 = 6 \geq 3$, both true.

That feasible region is the whole point. In a real problem you would then optimize something (cheapest cost, most pages, etc.) over the region — which is the gateway to linear programming later on.

---

## Testing a point

Any time you want to know whether a specific ordered pair is a solution, you can skip the graph and check algebraically: substitute the coordinates into every inequality in the system. The point is a solution only if **every single** inequality comes out true. One false check is enough to rule it out.

For example, is $(5, 0)$ a solution of the notebooks-and-pens system above? Check each condition: $4(5) + 0 = 20 \leq 20$ (true, since it is exactly $20$), $5 + 0 = 5 \geq 3$ (true), $5 \geq 0$ (true), $0 \geq 0$ (true). All four hold, so yes — the student could buy $5$ notebooks and $0$ pens.

---

## Common pitfalls

- **Shading before testing.** Do not guess which side of the boundary to shade. Pick a test point, plug it in, and *let the truth value decide*.
- **Using the wrong line style.** A solid line is for $\leq$ or $\geq$; a dashed line is for $<$ or $>$. Mixing these up changes whether the boundary itself is part of the solution.
- **Forgetting to flip when you multiply by a negative.** If you rearrange an inequality into slope-intercept form and multiply or divide both sides by a negative number, the inequality symbol flips. This trips people up more than any other single step.
- **Shading the individual regions but forgetting the overlap.** The solution is *only* where all the shadings coincide, not every place that any one inequality colors in.
- **Assuming a system always has a solution.** Two inequalities whose shaded half-planes never meet define a system with **no solution** — a perfectly legitimate answer. An example is $y > 2x + 3$ together with $y < 2x - 1$, whose boundary lines are parallel.

---

## Prerequisites

Before practicing systems, make sure you are comfortable with:

- [[Inequalities_And_Their_Graphs]] — graphing a single inequality as a half-plane is the building block of everything on this page.
- [[Slope_Intercept_Form]] — you will be converting lines to $y = mx + b$ constantly so you can eyeball the boundaries.
- [[Plotting_Points_And_The_Coordinate_Plane]] — every graph here lives in the $xy$-plane, so fluent plotting is non-negotiable.

---

## Problems Involving Systems of Linear Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="systems_of_linear_inequalities"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Inequalities_And_Their_Graphs]]
- [[Solving_Multi_Step_Inequalities]]
- [[Compound_Inequalities]]
- [[Solving_Systems_By_Graphing]]
- [[Solving_Systems_By_Substitution]]
- [[Solving_Systems_By_Elimination]]
- [[Slope_Intercept_Form]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
