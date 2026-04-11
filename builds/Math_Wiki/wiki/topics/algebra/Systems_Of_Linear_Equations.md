---
title: "Systems of Linear Equations"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-systems", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Solving_Systems_By_Graphing"
  - "topics/algebra/Solving_Systems_By_Substitution"
  - "topics/algebra/Solving_Systems_By_Elimination"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Writing_Linear_Equations"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "A system of linear equations is two (or more) line equations that must be satisfied at the same time; the solution is the point (or points) where all the lines meet."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Systems of Linear Equations

# Systems of Linear Equations

A single linear equation in two variables, like $y = 2x + 1$, has infinitely many solutions — every point on the line that the equation draws is a solution. That is not very useful if you want to pin down a specific $(x, y)$. But pair the equation with a second requirement, like $y = -x + 7$, and suddenly the question has a sharper shape: which point satisfies **both** line equations at the same time? That paired setup is called a **system of linear equations**, and it is one of the most common structures in all of algebra.

Systems show up everywhere. If you are mixing two chemicals and need the total volume and total cost to hit specific targets, you have a system. If two runners leave from different points at different speeds and you want to know when and where they meet, you have a system. Even small word problems about ages or coin values often reduce to a system of two equations in two unknowns. On standardized tests, systems are among the most frequently tested algebra topics.

## What a system is

Informally, a **system** is two or more equations you have to satisfy simultaneously. For this page we focus on the most common case: two linear equations in two variables, typically $x$ and $y$. Written together they usually look like this:

$$
\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}
$$

The big curly brace means "both of these equations at once." A **solution** of the system is an ordered pair $(x, y)$ that, when plugged into both equations, produces a true statement in each one. Because every linear equation in two variables draws a line in the plane, a solution of the system is visually the same as a point where both lines pass through. In short, a solution is where the lines meet.

## How many solutions can there be?

Two lines in a plane can do exactly three things, and each possibility corresponds to a type of system:

- **They cross at exactly one point.** The system has **one unique solution**. This is the most common case. The lines have different slopes, so they must cross somewhere, and that crossing point is the ordered pair that solves both equations.
- **They are parallel and never meet.** The system has **no solution**. The two equations describe lines with the same slope but different y-intercepts, so they climb in the same direction but at different heights. They never share a point.
- **They are the same line drawn twice.** The system has **infinitely many solutions** — every point on the line satisfies both equations, so there is no "unique" answer. This happens when one equation is just a rescaling or rearrangement of the other.

Recognizing which of these three cases you are in often saves work. If two lines have the same slope and the same intercept, there is no solving to do; the answer is "infinitely many solutions." If they have the same slope and different intercepts, there is also no solving to do; the answer is "no solution." The interesting work happens in the one-unique-solution case.

## Three methods for solving

There are three standard techniques for finding the solution of a two-variable system. Each has its own page with full details; this section gives you a quick tour so you know which tool to reach for when.

### Graphing

Sketch both lines on a coordinate plane and read off the intersection point. This method is the most visual and the easiest to understand, but it is also the least accurate — if the lines cross at a non-integer point, graphing gives you an estimate at best. It is best used when you want to *see* the geometry or when the problem gives you clean integer intersections. See [[Solving_Systems_By_Graphing]] for the full treatment.

### Substitution

Solve one of the equations for one of the variables, then plug that expression into the other equation. You end up with a single equation in a single variable, which you can solve the usual way. Substitution is fastest when one equation already has a variable alone (like $y = 3x + 2$) or when one coefficient is $1$ or $-1$, because isolating the variable costs almost nothing. See [[Solving_Systems_By_Substitution]].

### Elimination

Add (or subtract) the two equations so that one variable cancels, leaving you with a single equation in the remaining variable. If no cancellation happens naturally, multiply one or both equations by a constant first to create opposite coefficients on the same variable. Elimination is fastest when both equations are already in standard form $ax + by = c$ and when the coefficients are small integers. See [[Solving_Systems_By_Elimination]].

## Which method to pick

All three methods always produce the same answer when the system has a unique solution — they are different doors into the same room. A decent rule of thumb:

- If one equation already has a variable isolated, use **substitution**.
- If both equations are in standard form with opposite or easily matched coefficients, use **elimination**.
- If you want a visual check or the numbers are small, use **graphing**.

When a system has no solution, all three methods produce an unmistakable symptom: the variables cancel out and the remaining statement is false. When a system has infinitely many solutions, the variables cancel and the remaining statement is true. Recognizing the symptom $0 = 7$ (false — no solution) or $0 = 0$ (true — infinite solutions) lets you finish a special-case problem quickly without second-guessing yourself.

## Worked examples

**Example 1 (substitution).** Solve the system

$$
\begin{cases} y = 2x + 1 \\ 3x + y = 16 \end{cases}
$$

The first equation already has $y$ by itself, so substitution is the obvious choice. Plug the expression $2x + 1$ into the second equation wherever $y$ appears:

$$
3x + (2x + 1) = 16.
$$

This is now a single equation in a single variable. Simplify the left:

$$
5x + 1 = 16.
$$

Peel off the $+1$ by subtracting $1$ from each side: $5x = 15$. Divide each side by $5$: $x = 3$. Now back-substitute $x = 3$ into the first equation to get $y$: $y = 2(3) + 1 = 7$. The solution of the system is $(3, 7)$.

Verification in both originals: first equation, $7 = 2(3) + 1 = 7$ (check). Second equation, $3(3) + 7 = 9 + 7 = 16$ (check). The point $(3, 7)$ satisfies both equations, confirming the solution.

**Example 2 (elimination).** Find the ordered pair $(x, y)$ that satisfies

$$
\begin{cases} 2x + 3y = 12 \\ 2x - y = 4 \end{cases}
$$

Both equations already have a $2x$ term, and the coefficients on $x$ are identical. That means subtracting the second equation from the first will wipe the $x$-terms out — perfect for elimination. Write the subtraction carefully:

$$
(2x + 3y) - (2x - y) = 12 - 4
$$

$$
2x + 3y - 2x + y = 8
$$

$$
4y = 8.
$$

Divide each side by $4$ to get $y = 2$. Back-substitute into either original equation to find $x$; the second is simpler: $2x - 2 = 4$, so $2x = 6$ and $x = 3$. The solution is $(3, 2)$.

Verification: $2(3) + 3(2) = 6 + 6 = 12$ (check), and $2(3) - 2 = 4$ (check). Both equations hold, so $(3, 2)$ is correct.

**Example 3 (no solution case).** Emilia encounters the system

$$
\begin{cases} 4x - 2y = 8 \\ 2x - y = 5 \end{cases}
$$

Before solving, notice the slopes. If the first equation were divided through by $2$, it would read $2x - y = 4$, which has exactly the same $2x - y$ combination on the left as the second equation, but a different right-hand side ($4$ versus $5$). That is the signature of parallel lines: same slope, different intercepts.

Try the elimination method anyway to see what happens. Multiply the second equation by $-2$ so its left side becomes the negative of the first equation's left side:

$$
-2 \cdot (2x - y) = -2 \cdot 5
$$

$$
-4x + 2y = -10.
$$

Add this to the first equation:

$$
(4x - 2y) + (-4x + 2y) = 8 + (-10)
$$

$$
0 = -2.
$$

The variables have vanished and the remaining statement is $0 = -2$, which is false. That is the signal: **there is no real number pair $(x, y)$ that satisfies both equations**. The system has no solution, and geometrically the two lines are parallel. On a graph you would see them climbing at the same slope but never touching.

Had the final statement instead been $0 = 0$ (true), it would have meant the two equations describe the same line and the system has infinitely many solutions. The pattern to memorize: after elimination collapses away the variables, a true statement like $0 = 0$ means infinite solutions, and a false statement like $0 = -2$ means no solution.

## Common pitfalls

- **Forgetting that one method's answer must also work in the other equation.** Both originals must hold for the ordered pair to count as a solution. If you only verify against the equation you most recently used, you might miss an arithmetic error from earlier.
- **Misreading the cancellation signs.** In elimination, $(2x + 3y) - (2x - y)$ is $4y$, not $2y$ — the subtraction distributes over the entire parenthesized expression, so $-(-y) = +y$. Dropping this sign is the single most common cause of wrong answers.
- **Choosing the wrong method.** All three techniques give the right answer, but some are much faster than others for a given system. If one equation has a variable already isolated, substitution will beat elimination. If both are in standard form with easy coefficients, elimination will beat substitution.
- **Confusing "no solution" with "$(0, 0)$ is the solution."** When the variables cancel to $0 = 7$, the system has **no solution** — not $(0, 0)$. Similarly, when the variables cancel to $0 = 0$, the system has **infinitely many solutions**, not zero.
- **Not back-substituting to find the second variable.** After finding one coordinate of the solution, plug it into one of the original equations (usually the simpler one) to get the other coordinate. Do not stop at one variable — a solution is an ordered pair, not a number.

## Problems Involving Systems of Linear Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="systems_of_linear_equations"></div>

## See Also

- [[Solving_Systems_By_Graphing]]
- [[Solving_Systems_By_Substitution]]
- [[Solving_Systems_By_Elimination]]
- [[Linear_Functions]]
- [[Writing_Linear_Equations]]
- [[Systems_Of_Linear_Inequalities]]
- [[Parallel_And_Perpendicular_Lines]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
