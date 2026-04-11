---
title: "Augmented Matrices"
type: topic
aliases: ["Augmented Matrix", "Row Operations", "Row-Echelon Form", "Gaussian Elimination"]
tags: ["#branch-pre-calculus", "#topic-matrices", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "11", section: "11.1"}
related:
  - "topics/precalculus/Matrix_Arithmetic"
  - "topics/precalculus/Matrix_Methods"
  - "topics/precalculus/Determinants"
  - "topics/algebra/Solving_Systems_By_Elimination"
  - "topics/algebra/Solving_Systems_By_Substitution"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Solving_Systems_By_Substitution"
  - "topics/algebra/Solving_Systems_By_Elimination"
problem_type_ids: []
figures: []
summary: "Turn a linear system into a matrix, then drive it toward row-echelon form with three legal moves."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Augmented Matrices

# Augmented Matrices

When you solve a linear system on paper with [[Solving_Systems_By_Elimination|elimination]], a lot of the work is bookkeeping — copying the same variable names over and over again, keeping the equals signs aligned, tracking which equation just had a multiple of another added to it. The variables are not really doing anything; they just hold the numerical coefficients in place.

An **augmented matrix** is the idea of dropping the variables entirely and working only with the numbers. You keep the coefficients on the left, the constants from the right-hand side of the equations on the right, and a single vertical bar to remind you which side is which. Once the system is in matrix form, you manipulate rows directly instead of writing out whole equations. Every bit of information you need is still there, but there is a lot less to write.

---

## From a system to a matrix

Given the linear system

$$
\begin{cases} 2x + 3y = 7 \\ x - y = 1 \end{cases}
$$

line the coefficients up in a grid in the same order as the variables appear, and park the right-hand constants after a vertical bar:

$$
\left[\begin{array}{cc|c} 2 & 3 & 7 \\ 1 & -1 & 1 \end{array}\right]
$$

Each row of the matrix is one equation. Each column on the left corresponds to one variable — column 1 for $x$, column 2 for $y$. The bar is just a visual reminder of where the equation's equals sign would sit if the variables were still written out. If a variable is missing from an equation, write a $0$ in that slot so every row has the same width.

A larger system with three equations in three unknowns produces a $3 \times 4$ augmented matrix (three rows for the equations, four columns for $x$, $y$, $z$, and the constants). The pattern scales the same way for bigger systems.

---

## The three legal moves on rows

To solve a system, we manipulate equations — multiply an equation by a constant, add one equation to another, swap the order in which we write them. Each of those moves leaves the solution set untouched because it produces an **equivalent system**. Translating those moves to the matrix world, you get three **row operations** — and they are the only moves that keep the solution set unchanged:

- **Swap** — interchange two rows. Useful when you want a friendlier number in a leading position.
- **Scale** — multiply every entry of a single row by a nonzero constant. A zero multiplier is not allowed, because it would erase information.
- **Replace** — add a multiple of one row to another, overwriting the second row with the result. This is the matrix version of the elimination step, and it is where most of the real work happens.

When you apply a row operation, you apply it to every entry in the row, including the constant column to the right of the bar. Short notation helps you track the moves: $R_1 \leftrightarrow R_2$ for a swap, $3R_2$ for scaling, $R_2 + 4R_1$ for the replacement move where row 2 becomes itself plus four times row 1.

---

## Targets: row-echelon and reduced row-echelon form

The point of doing row operations is to simplify the matrix into a clean pattern that makes reading off the solution easy. Two standard target patterns.

A matrix is in **row-echelon form** when each nonzero row starts with a $1$ (called a **leading one**), and every leading one sits strictly to the right of the one in the row above. Any all-zero rows are pushed to the bottom. This triangular look is what you aim for during **Gaussian elimination** — once you hit it, the last equation gives one variable directly, and you chase the rest upward with **back-substitution**.

A matrix is in **reduced row-echelon form (RREF)** when it is already in row-echelon form *and* each leading $1$ is the only nonzero entry in its column — every slot above and below a leading one has been cleared. The process that drives a matrix all the way to RREF is called **Gauss-Jordan elimination**. When a matrix is in RREF, the solution is sitting right there, no back-substitution needed.

---

## A complete Gaussian elimination, start to finish

> Solve the system $\begin{cases} 2x + 3y = 7 \\ x - y = 1 \end{cases}$ using row operations.

Start with the augmented matrix:

$$
\left[\begin{array}{cc|c} 2 & 3 & 7 \\ 1 & -1 & 1 \end{array}\right]
$$

**Step 1: Get a leading $1$ in the top-left.** The top row starts with a $2$, not a $1$. Swapping rows is easier than scaling, and row 2 already begins with a $1$, so swap:

$$
R_1 \leftrightarrow R_2: \quad \left[\begin{array}{cc|c} 1 & -1 & 1 \\ 2 & 3 & 7 \end{array}\right]
$$

**Step 2: Zero out the slot below the leading $1$.** Row 2 still begins with a $2$. Replace $R_2$ with $R_2 - 2R_1$ so that the $2$ becomes a $0$:

$$
R_2 - 2R_1: \quad \left[\begin{array}{cc|c} 1 & -1 & 1 \\ 0 & 5 & 5 \end{array}\right]
$$

Quick check on row 2: $2 - 2(1) = 0$, $3 - 2(-1) = 5$, $7 - 2(1) = 5$. The new row $(0, 5 \mid 5)$ says $5y = 5$, which is already enough information to finish.

**Step 3: Turn the second leading entry into a $1$.** Scale row 2 by $1/5$:

$$
\tfrac{1}{5} R_2: \quad \left[\begin{array}{cc|c} 1 & -1 & 1 \\ 0 & 1 & 1 \end{array}\right]
$$

The matrix is now in row-echelon form. Reading row 2, $y = 1$. Back-substituting into row 1, $x - y = 1$ becomes $x - 1 = 1$, so $x = 2$.

**Step 4 (optional): Push to RREF.** To read $x$ directly without back-substitution, clear the $-1$ above the leading $1$ in column $2$. Replace $R_1$ with $R_1 + R_2$:

$$
R_1 + R_2: \quad \left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 1 \end{array}\right]
$$

The matrix is now in **reduced** row-echelon form, and the answer is literally staring at you: row 1 says $x = 2$, row 2 says $y = 1$. The solution to the original system is $(x, y) = (2, 1)$. You can (and should) plug it back into the original two equations to verify: $2(2) + 3(1) = 7$ and $2 - 1 = 1$. Both check.

---

## Example 2: A $3 \times 3$ system, stopping at row-echelon form

> Turn $\begin{cases} x + 2y - z = 3 \\ 2x - y + z = 1 \\ -x + y + 2z = 6 \end{cases}$ into row-echelon form and solve.

The augmented matrix is

$$
\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 2 & -1 & 1 & 1 \\ -1 & 1 & 2 & 6 \end{array}\right]
$$

Zero out column 1 below the top-left $1$ with two replacement moves: $R_2 - 2R_1$ and $R_3 + R_1$:

$$
\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & -5 & 3 & -5 \\ 0 & 3 & 1 & 9 \end{array}\right]
$$

Scale row 2 by $-1/5$ to make the next leading entry a $1$:

$$
\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & -3/5 & 1 \\ 0 & 3 & 1 & 9 \end{array}\right]
$$

Clear column 2 below that leading $1$ with $R_3 - 3R_2$:

$$
\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & -3/5 & 1 \\ 0 & 0 & 14/5 & 6 \end{array}\right]
$$

Scale row 3 by $5/14$ to finish the staircase:

$$
\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & -3/5 & 1 \\ 0 & 0 & 1 & 15/7 \end{array}\right]
$$

Row-echelon form achieved. Read row 3: $z = 15/7$. Back-substitute into row 2: $y - \tfrac{3}{5} \cdot \tfrac{15}{7} = 1$, which gives $y - \tfrac{9}{7} = 1$, so $y = \tfrac{16}{7}$. Back-substitute into row 1: $x + 2 \cdot \tfrac{16}{7} - \tfrac{15}{7} = 3$, so $x + \tfrac{17}{7} = 3$ and $x = \tfrac{4}{7}$. Full solution: $(x, y, z) = \left(\tfrac{4}{7}, \tfrac{16}{7}, \tfrac{15}{7}\right)$.

---

## Example 3: Spotting no solution from the matrix

> What does the system $\begin{cases} x + y = 2 \\ 2x + 2y = 7 \end{cases}$ look like in row-echelon form?

Augmented matrix:

$$
\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & 2 & 7 \end{array}\right]
$$

Apply $R_2 - 2R_1$:

$$
\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & 0 & 3 \end{array}\right]
$$

Row 2 now translates back to $0x + 0y = 3$, which says $0 = 3$ — a flat contradiction. Whenever you see a row of the form $[0 \; 0 \; \cdots \; 0 \mid c]$ with a nonzero constant $c$, the system has **no solution**. Geometrically the two original equations were parallel lines, and you just confirmed it algebraically.

---

## Common pitfalls

- **Forgetting to update the constant column.** The vertical bar is a visual guide, not a wall. When you scale or replace a row, the number on the right of the bar moves with every entry on the left.
- **Scaling by zero.** Multiplying a row by $0$ erases information and breaks the equivalence with the original system. The scale factor must be nonzero.
- **Mixing up the direction of a replacement.** $R_2 \to R_2 - 2R_1$ overwrites *row 2* using *row 1* as a tool. Row 1 stays put. Swapping the roles will change the wrong row.
- **Declaring a system inconsistent too early.** A row like $[0 \; 0 \; 0 \mid 0]$ is fine — it just means one of the original equations was redundant. Only a row with a nonzero constant on the right of zeros on the left indicates no solution.

---

## Prerequisites

- [[Solving_Systems_By_Substitution]] — the underlying idea of replacing one equation by a combination of equations carries over directly.
- [[Solving_Systems_By_Elimination]] — the "add a multiple of one equation to another" move is literally what the replacement row operation does.

---

## Problems Involving Augmented Matrices

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="augmented_matrices"></div>

---

## See Also

- [[Matrix_Arithmetic]] — the grid objects you are pushing around with row operations
- [[Matrix_Methods]] — several full strategies that use augmented matrices to solve systems
- [[Determinants]] — a different angle on square systems that avoids row reduction
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
