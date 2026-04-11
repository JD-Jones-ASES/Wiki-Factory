---
title: "Nonlinear Systems"
type: topic
aliases: ["Nonlinear System of Equations", "Systems with Curves", "Curve Intersections"]
tags: ["#branch-pre-calculus", "#topic-systems", "#topic-conic-sections", "#skill-algebraic-manipulation", "#skill-multi-step", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra_1/Systems_Of_Linear_Equations"
  - "topics/algebra_1/Substitution_Method"
  - "topics/algebra_2/Quadratic_Equations"
  - "topics/algebra_2/Circles"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra_1/Systems_Of_Linear_Equations"
  - "topics/algebra_1/Substitution_Method"
  - "topics/algebra_2/Quadratic_Equations"
problem_type_ids: []
figures: []
summary: "When one or more equations in a system are not straight lines, the intersection can have zero, one, two, or more points, and the toolkit expands from elimination into substitution, squaring, and graphical reasoning about conics meeting lines and other curves."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Nonlinear Systems

# Nonlinear Systems

By the time you meet systems of equations in algebra, you have already learned how to handle two straight lines at once: graph them, substitute, eliminate, and out pops the single point (or the empty set, or the whole line) where they agree. The entire picture rests on the fact that two lines in the plane meet in at most one place.

That picture breaks open as soon as one of the equations bends. A parabola can cross a line at $0$, $1$, or $2$ points depending on where the line sits. A circle can miss a line entirely, touch it once as a tangent, or slice it cleanly into a chord and leave two intersection points behind. A pair of circles can meet in as many as $2$ points. These **nonlinear systems** — systems where at least one equation is something other than a straight line — are every bit as solvable as linear ones, but the number of solutions and the geometric picture take a little more care.

$$
\begin{cases} y = x^2 - 4 \\ y = 2x + 1 \end{cases} \qquad\Longrightarrow\qquad x^2 - 4 = 2x + 1.
$$

The algebraic strategy is still what it has always been: reduce two equations in two unknowns down to one equation in one unknown, solve that one, and then push each answer back through one of the original equations to recover the other coordinate. The twist is that the single-variable equation you end up with is no longer linear, so you are back in the world of factoring, the quadratic formula, or occasionally clever squaring tricks.

---

## Substitution is the workhorse

Most nonlinear systems you will meet are built with two equations where one of them is solved for (or easily solvable for) $y$ in terms of $x$. That makes substitution the natural first move: take the expression for $y$ from one equation and drop it into the $y$ slot of the other. The result is a single-variable equation in $x$, which you then solve using whatever tool fits.

A typical setup pairs a quadratic $y = ax^2 + bx + c$ with a line $y = mx + k$. Substituting the line's expression into the parabola's slot gives $mx + k = ax^2 + bx + c$, which rearranges to a quadratic $ax^2 + (b-m)x + (c-k) = 0$. The discriminant of that quadratic then counts the intersections directly:

- $b^2 - 4ac > 0$: two real $x$-values, so two intersection points
- $b^2 - 4ac = 0$: one repeated $x$-value, so one point (the line is tangent to the parabola)
- $b^2 - 4ac < 0$: no real $x$-values, so no intersection points

The same counting pattern works whenever you can reduce to a quadratic in one variable. The discriminant is doing the work of a visual check without having to graph anything.

---

## Elimination still helps when both curves are even in the same variable

Substitution is not the only game in town. If both equations contain the same squared term — say $x^2 + y^2 = 25$ (a circle) and $x^2 - y = 5$ (a parabola) — you can subtract one equation from the other to knock out the $x^2$ entirely and leave a simpler equation behind. That elimination move is particularly handy when both curves carry a matching $x^2$ or $y^2$ on opposite sides of an equation.

A common target is two circles. Given $x^2 + y^2 = 25$ and $(x-3)^2 + y^2 = 16$, expanding the second gives $x^2 - 6x + 9 + y^2 = 16$. Subtract this from the first, the $x^2 + y^2$ cancels, and what is left is a linear equation in $x$: $6x - 9 = 9$, so $x = 3$. Plugging $x = 3$ back into either original circle finishes the job and gives the $y$-values of the intersection points.

---

## Geometric reasoning about the solution count

Before you start cranking through algebra, it pays to picture what is happening. The number of solutions in a nonlinear system is a feature of the geometry, not a fluke of the numbers.

- **Line and parabola.** A parabola opening upward is a single U-shape. A line can miss it entirely (flying over the vertex), touch it once (tangent at the bottom or off to one side), or cut across it in two places. Zero, one, or two solutions.
- **Line and circle.** A line through the center of a circle always produces a chord, so two points. A line grazing the edge of the circle touches at exactly one tangent point. A line that misses the circle entirely gives no intersections. Zero, one, or two solutions.
- **Parabola and horizontal line.** A horizontal line $y = k$ meets a parabola $y = ax^2 + bx + c$ wherever the parabola reaches height $k$. For an upward-opening parabola with minimum at height $h$: if $k > h$ you get two intersections, if $k = h$ you get one at the vertex, and if $k < h$ you get none.
- **Circle and circle.** Two circles either miss, touch at one point (externally or internally tangent), cross in two places, or coincide entirely. Zero, one, two, or infinitely many solutions.

When your algebra says you have zero solutions and the picture says two, go back and check — one of the two is lying, and it is almost always the algebra.

---

## Example 1: parabola meets line

> Solve the system
> $\begin{cases} y = x^2 - 4 \\ y = 2x + 1 \end{cases}$

Substitute the expression for $y$ from the second equation into the first:

$$
2x + 1 = x^2 - 4.
$$

Move everything to one side:

$$
0 = x^2 - 2x - 5.
$$

This does not factor over the integers, so use the quadratic formula:

$$
x = \dfrac{2 \pm \sqrt{4 + 20}}{2} = \dfrac{2 \pm \sqrt{24}}{2} = 1 \pm \sqrt{6}.
$$

Recover each $y$ by plugging back into $y = 2x + 1$:

$$
y = 2(1 + \sqrt{6}) + 1 = 3 + 2\sqrt{6}, \qquad y = 2(1 - \sqrt{6}) + 1 = 3 - 2\sqrt{6}.
$$

Two intersection points: $(1 + \sqrt{6},\; 3 + 2\sqrt{6})$ and $(1 - \sqrt{6},\; 3 - 2\sqrt{6})$. The discriminant $24 > 0$ confirmed in advance that the line would cut the parabola in two places; the answer matches the picture.

---

## Example 2: circle meets line

> Kai is designing a logo in which a straight edge just touches the outside of a circular emblem. The circle is $x^2 + y^2 = 25$ and the straight edge lies on $y = x - 7$. Where do they meet, and is the line tangent, secant, or disjoint from the circle?

Substitute $y = x - 7$ into the circle equation:

$$
x^2 + (x - 7)^2 = 25.
$$

Expand and simplify:

$$
x^2 + x^2 - 14x + 49 = 25 \quad\Longrightarrow\quad 2x^2 - 14x + 24 = 0 \quad\Longrightarrow\quad x^2 - 7x + 12 = 0.
$$

Factor: $(x - 3)(x - 4) = 0$, so $x = 3$ or $x = 4$.

Recover $y$ from the line equation:

$$
y = 3 - 7 = -4, \qquad y = 4 - 7 = -3.
$$

The line meets the circle in two points, $(3, -4)$ and $(4, -3)$. Because there are two distinct intersection points, the line is a **secant** — it cuts the circle cleanly. It is not tangent (which would require exactly one point) and it is not disjoint (which would give none). Kai will need to move the line out a bit if the design calls for a true tangent.

---

## Example 3: parabola meets horizontal line

> Find every intersection of $y = x^2 - 6x + 5$ with the horizontal line $y = -4$, or explain that no intersection exists.

Set the two expressions for $y$ equal:

$$
x^2 - 6x + 5 = -4.
$$

Move everything to one side:

$$
x^2 - 6x + 9 = 0.
$$

This factors as $(x - 3)^2 = 0$, which has a single repeated root $x = 3$. Recovering $y$ gives $y = -4$ directly from the horizontal-line equation. There is exactly one intersection point: $(3, -4)$.

The geometry matches. The parabola $y = x^2 - 6x + 5$ can be rewritten by completing the square as $y = (x - 3)^2 - 4$, which shows its vertex sits at $(3, -4)$. The horizontal line $y = -4$ is level with the vertex, so it kisses the parabola at the single lowest point and goes nowhere else. This is the $b^2 - 4ac = 0$ case: one solution, a tangent intersection, a repeated root.

---

## Common pitfalls

- **Dropping a solution while squaring.** Some systems require squaring both sides to clear a radical. Squaring can introduce extraneous roots that do not satisfy the original equations — always plug the candidates back in at the end to check.
- **Stopping after finding $x$.** The system asks for ordered pairs, not just $x$-values. Each $x$ has to be paired with the corresponding $y$ from one of the original equations, and you need to verify the pair satisfies the other equation too.
- **Forgetting that circles have two $y$-values per $x$.** For a circle $x^2 + y^2 = r^2$, solving for $y$ gives $y = \pm\sqrt{r^2 - x^2}$. Using only the positive root loses half the circle and can miss intersection points on the bottom half.
- **Assuming there is always a solution.** A horizontal line below the vertex of an upward parabola has no intersection at all, and the quadratic that comes out will have a negative discriminant. Recognize the empty solution set for what it is — it is not an algebra mistake.
- **Mixing up which variable the discriminant is in.** When counting solutions by discriminant, you need the quadratic to be in one variable (either all $x$ or all $y$). If your equation still has both variables, substitution has not finished its job yet.

---

## Prerequisites

- [[Systems_Of_Linear_Equations]] — the baseline case, where both equations are straight lines and the toolkit (graphing, substitution, elimination) is introduced
- [[Solving_Systems_By_Substitution|Solving Systems by Substitution]] — the single technique that handles the vast majority of nonlinear systems
- [[The_Quadratic_Formula|The Quadratic Formula]] — the quadratic formula and the discriminant both show up every time a parabola meets a line

---

## Problems Involving Nonlinear Systems

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="nonlinear_systems"></div>

---

## See Also

- [[Systems_Of_Linear_Equations]] — the simpler case that nonlinear systems generalize
- [[The_Quadratic_Formula|The Quadratic Formula]] — the discriminant tool that counts intersection points in advance
- [[Circles]] — conic sections whose equations are the most common nonlinear partner in a system
- [[Parabolas]] — another workhorse of curve-meets-line problems
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
