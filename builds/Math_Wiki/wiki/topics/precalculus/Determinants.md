---
title: "Determinants"
type: topic
aliases: ["Determinant", "2x2 Determinant", "3x3 Determinant", "Cofactor Expansion"]
tags: ["#branch-pre-calculus", "#topic-matrices", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "11", section: "11.2"}
related:
  - "topics/precalculus/Matrix_Arithmetic"
  - "topics/precalculus/Augmented_Matrices"
  - "topics/precalculus/Matrix_Methods"
  - "topics/precalculus/Vectors"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Matrix_Arithmetic"
problem_type_ids: []
figures: []
summary: "A single number attached to every square matrix that detects invertibility and measures signed area or volume."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Determinants

# Determinants

Every square matrix (one with the same number of rows as columns) carries a single number called its **determinant**. The determinant is written $\det(A)$ or, equivalently, with vertical bars around the grid: $|A|$. That one number is surprisingly informative. It tells you whether the matrix is invertible, it comes out of geometry as the signed area or volume of a parallelogram or parallelepiped, it is the conversion factor that says how the matrix stretches area, and it turns up in every shortcut for solving square systems of linear equations.

The reason to care is simple: once you know $\det(A)$ you can often answer big questions about $A$ without doing a single row operation. In particular, the determinant is zero exactly when $A$ is **singular** — meaning $A$ has no inverse, the columns are linearly dependent, and the matrix squashes space flat instead of just rotating and stretching it.

---

## The $2 \times 2$ determinant

For a $2 \times 2$ matrix, there is a one-line rule. Let

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

Then

$$
\det(A) = ad - bc
$$

Multiply the top-left and bottom-right corners (the **main diagonal**), then subtract the product of the top-right and bottom-left (the **anti-diagonal**). That is the whole formula, and it is worth memorizing — you will reach for it constantly.

A quick numerical check: if

$$
A = \begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}
$$

then $\det(A) = 3(4) - 2(1) = 12 - 2 = 10$. Because the result is nonzero, this matrix is invertible, so a system of two linear equations with $A$ as its coefficient matrix will have exactly one solution. On the other hand,

$$
B = \begin{pmatrix} 2 & 6 \\ 1 & 3 \end{pmatrix}
$$

gives $\det(B) = 2(3) - 6(1) = 0$. The second row is half the first, which is why the determinant collapses — geometrically, the two column vectors point along the same line, so the "parallelogram" they span has zero area.

---

## The $3 \times 3$ determinant by cofactor expansion

There is no single-line formula that stays short for $3 \times 3$. Instead, you use **cofactor expansion**, also known as expansion along a row. Pick any row or column (usually the top row, because it is easy to read), walk across it, and for each entry build a little piece that combines three things: the entry itself, a sign, and a **minor** (the determinant of the $2 \times 2$ matrix you get by deleting the row and column of that entry).

Sign pattern for a $3 \times 3$ matrix:

$$
\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}
$$

For the top row of

$$
A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}
$$

the expansion is

$$
\det(A) = a_{11} \det\!\begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix} - a_{12} \det\!\begin{pmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{pmatrix} + a_{13} \det\!\begin{pmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}
$$

Each of the little $2 \times 2$ determinants is another $ad - bc$ computation, so a $3 \times 3$ determinant boils down to three $2 \times 2$ determinants plus some signs. The same technique scales up: a $4 \times 4$ determinant can be expanded into four $3 \times 3$ determinants, and so on, but the work explodes quickly and most people switch to row reduction or software past $3 \times 3$.

**Shortcut:** pick a row or column with zeros. Any entry that is zero kills its whole cofactor term, because the product is zero. A row with two zeros collapses a $3 \times 3$ determinant to a single $2 \times 2$ calculation.

---

## What the determinant is measuring

For a $2 \times 2$ matrix, $|\det(A)|$ is the area of the parallelogram whose sides are the two column vectors of $A$. If the columns lie on the same line, the parallelogram has zero area, and the determinant is zero. For a $3 \times 3$ matrix, $|\det(A)|$ is the volume of the parallelepiped (a skewed box) whose edges are the three column vectors. If those three vectors all lie in a single plane, the box is flat and has zero volume, so the determinant is again zero.

The sign of the determinant tracks orientation: positive means the columns are arranged in the "standard" sense (like the $x$- and $y$-axes), negative means the arrangement has been flipped. For our purposes the most important takeaway is the absolute value — the magnitude of the determinant is how much a linear transformation scales area or volume when you apply it.

---

## Example 1: A $2 \times 2$ determinant

> Compute $\det\!\begin{pmatrix} 5 & -2 \\ 3 & 4 \end{pmatrix}$ and decide whether the matrix is invertible.

Main-diagonal product minus anti-diagonal product:

$$
\det\!\begin{pmatrix} 5 & -2 \\ 3 & 4 \end{pmatrix} = 5(4) - (-2)(3) = 20 + 6 = 26
$$

Because $26 \neq 0$, this matrix is **invertible** (nonsingular). Any $2 \times 2$ system of equations with this coefficient matrix has exactly one solution.

---

## Example 2: A $3 \times 3$ determinant via cofactor expansion

> Compute

$$
\det\!\begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & -2 \end{pmatrix}
$$

Expand along the top row using the $+\, -\, +$ sign pattern. Deleting row 1 and column 1 gives the first $2 \times 2$ minor; deleting row 1 and column 2 gives the second; deleting row 1 and column 3 gives the third.

$$
\det(A) = 2 \det\!\begin{pmatrix} 4 & 5 \\ 0 & -2 \end{pmatrix} - (-1) \det\!\begin{pmatrix} 0 & 5 \\ 1 & -2 \end{pmatrix} + 3 \det\!\begin{pmatrix} 0 & 4 \\ 1 & 0 \end{pmatrix}
$$

Evaluate each $2 \times 2$ determinant:

$$
\det\!\begin{pmatrix} 4 & 5 \\ 0 & -2 \end{pmatrix} = 4(-2) - 5(0) = -8
$$

$$
\det\!\begin{pmatrix} 0 & 5 \\ 1 & -2 \end{pmatrix} = 0(-2) - 5(1) = -5
$$

$$
\det\!\begin{pmatrix} 0 & 4 \\ 1 & 0 \end{pmatrix} = 0(0) - 4(1) = -4
$$

Plug back in, being very careful with the signs:

$$
\det(A) = 2(-8) - (-1)(-5) + 3(-4) = -16 - 5 - 12 = -33
$$

The determinant is $-33$. It is nonzero, so this matrix is invertible. Its absolute value, $33$, is the volume of the parallelepiped spanned by the three columns of $A$.

---

## Example 3: A singular matrix

> Compute $\det\!\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 5 \end{pmatrix}$.

Expand along the top row:

$$
\det(A) = 1 \det\!\begin{pmatrix} 4 & 6 \\ 1 & 5 \end{pmatrix} - 2 \det\!\begin{pmatrix} 2 & 6 \\ 0 & 5 \end{pmatrix} + 3 \det\!\begin{pmatrix} 2 & 4 \\ 0 & 1 \end{pmatrix}
$$

The three small determinants are $4(5) - 6(1) = 14$, $2(5) - 6(0) = 10$, and $2(1) - 4(0) = 2$. Substituting:

$$
\det(A) = 1(14) - 2(10) + 3(2) = 14 - 20 + 6 = 0
$$

The determinant is $0$, so this matrix is **singular** — no inverse, no unique solution for the corresponding system. Looking at the first two rows, row 2 is exactly twice row 1, which is why the answer collapses to zero. Whenever a row (or column) is a scalar multiple of another, the determinant is forced to be zero.

---

## What a nonzero vs. zero determinant tells you

- **$\det(A) \neq 0$** — the matrix is invertible, the columns are linearly independent, and the system $A\vec{x} = \vec{b}$ has exactly one solution for every right-hand side $\vec{b}$.
- **$\det(A) = 0$** — the matrix is singular, the columns are linearly dependent (one is a combination of the others), and the system $A\vec{x} = \vec{b}$ either has no solutions or infinitely many, depending on $\vec{b}$.

This simple test is why determinants come up so often in linear-system analysis. A quick $ad - bc$ calculation can often save you from trying to invert a matrix that has no inverse in the first place.

---

## Common pitfalls

- **Flipping the sign in the $2 \times 2$ rule.** The pattern is main diagonal *minus* anti-diagonal: $ad - bc$, never $ad + bc$. Swapping the sign gives the determinant of a different matrix.
- **Dropping the alternating signs in cofactor expansion.** Every other term carries a minus. Writing the sign pattern above your matrix before you start is a cheap insurance policy.
- **Mixing up the minor and the cofactor.** The **minor** is just the smaller determinant, with no sign. The **cofactor** is the minor with the $+$ or $-$ already attached. Cofactor expansion uses the signed cofactors, so keep track of which one you are computing.
- **Trying to take the determinant of a non-square matrix.** Determinants are only defined for square matrices. A $2 \times 3$ or $3 \times 2$ has no determinant — full stop.
- **Assuming a nonzero determinant means big numbers.** A determinant of $\tfrac{1}{1000}$ is still nonzero, so the matrix is still invertible. Zero is the only magic value; tiny is fine.

---

## Prerequisites

- [[Matrix_Arithmetic]] — you need to be comfortable writing matrices, identifying entries by row and column, and recognizing square matrices before you can compute determinants.
- [[Augmented_Matrices]] — helpful for seeing why "singular" equals "bad system," even though the determinant approach does not use row operations directly.

---

## Problems Involving Determinants

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="determinants"></div>

---

## See Also

- [[Matrix_Arithmetic]] — the operations determinants sit on top of
- [[Matrix_Methods]] — solving systems with matrices, including Cramer's rule which is built from determinants
- [[Augmented_Matrices]] — an alternative approach to square systems using row reduction
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
