---
title: "Matrix Arithmetic"
type: topic
aliases: ["Matrices", "Matrix Operations", "Matrix Addition", "Matrix Multiplication"]
tags: ["#branch-pre-calculus", "#topic-matrices"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "11", section: "11.4"}
related:
  - "topics/precalculus/Augmented_Matrices"
  - "topics/precalculus/Determinants"
  - "topics/precalculus/Matrix_Methods"
  - "topics/precalculus/Vectors"
  - "topics/algebra/Solving_Systems_By_Substitution"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Solving_Systems_By_Substitution"
  - "topics/algebra/Solving_Systems_By_Elimination"
problem_type_ids: []
figures: []
summary: "How to add, scale, and multiply grids of numbers — the three operations that make matrices computable."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Matrix Arithmetic

# Matrix Arithmetic

A **matrix** is a grid of numbers arranged in rows and columns. You box the grid with square brackets and say its size by counting "rows by columns." A matrix with $m$ rows and $n$ columns is called an $m \times n$ matrix, and the number sitting in row $i$, column $j$ is written $a_{ij}$. For example,

$$
A = \begin{pmatrix} 2 & -1 & 0 \\ 3 & 4 & 5 \end{pmatrix}
$$

is a $2 \times 3$ matrix (two rows, three columns) with $a_{11} = 2$, $a_{12} = -1$, $a_{23} = 5$, and so on.

That definition sounds abstract, but matrices show up everywhere once you start looking. A table of test scores, the coefficients of a system of linear equations, the pixel values of a black-and-white image, a rotation rule for a video game — all of them are matrices in disguise. The payoff of treating the grid as a single object is that you can define arithmetic on it, and once you have arithmetic, you get a whole algebra for free.

Two matrices are called **equal** exactly when they are the same size *and* their entries match position by position. This is stricter than "same numbers" — a $2 \times 3$ matrix can never equal a $3 \times 2$ matrix, even if they contain the same values, because the shape is part of the identity.

---

## Addition and subtraction: same shape, componentwise

To add two matrices, add the entries that sit in the same position. The catch is that both matrices must have exactly the same shape — you cannot add a $2 \times 2$ to a $2 \times 3$ because some slots would have nothing to pair with.

$$
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & -1 \\ 0 & 6 \end{pmatrix} = \begin{pmatrix} 1+5 & 2+(-1) \\ 3+0 & 4+6 \end{pmatrix} = \begin{pmatrix} 6 & 1 \\ 3 & 10 \end{pmatrix}
$$

Subtraction works the exact same way: subtract entry by entry. Because addition is componentwise, it inherits the familiar rules from real-number arithmetic — it is commutative ($A + B = B + A$) and associative — and there is a **zero matrix** $0$ full of zeros that acts as the additive identity: $A + 0 = A$.

---

## Scalar multiplication: stretch every entry

When you multiply a matrix by a plain real number (called a **scalar**), you hit every entry with that number:

$$
3 \cdot \begin{pmatrix} 2 & -1 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 6 & -3 \\ 0 & 15 \end{pmatrix}
$$

Scalar multiplication behaves like ordinary multiplication — it distributes over matrix addition, $k(A + B) = kA + kB$, and it composes through scaling, $(kr)A = k(rA)$.

---

## Matrix multiplication: rows hit columns

The third operation, the matrix product $AB$, is the one with real personality. It is defined through row-column **dot products**, and the first thing to check is that the shapes are compatible: you can form $AB$ only when the number of columns of $A$ equals the number of rows of $B$. If $A$ is $m \times n$ and $B$ is $n \times p$, then the product $AB$ has shape $m \times p$. The inner $n$ cancels out; the outer dimensions survive.

The entry in row $i$, column $j$ of the product $AB$ is built by taking row $i$ of $A$, lining it up against column $j$ of $B$, multiplying matching entries, and adding everything up:

$$
(AB)_{ij} = a_{i1} b_{1j} + a_{i2} b_{2j} + \cdots + a_{in} b_{nj}
$$

That is the whole method — match, multiply, add. Every other trick you will ever see with matrix multiplication is just a repeated application of this row-meets-column pattern.

### A $2 \times 2$ walk-through

Let

$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \qquad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
$$

Both are $2 \times 2$, so the product $AB$ is defined and it will also be $2 \times 2$. Build the answer one entry at a time.

- **Row 1, column 1** — row 1 of $A$ is $(1, 2)$, column 1 of $B$ is $(5, 7)$. Dot them: $1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19$.
- **Row 1, column 2** — row 1 of $A$ is $(1, 2)$, column 2 of $B$ is $(6, 8)$. Dot them: $1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22$.
- **Row 2, column 1** — row 2 of $A$ is $(3, 4)$, column 1 of $B$ is $(5, 7)$. Dot them: $3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43$.
- **Row 2, column 2** — row 2 of $A$ is $(3, 4)$, column 2 of $B$ is $(6, 8)$. Dot them: $3 \cdot 6 + 4 \cdot 8 = 24 + 32 = 56$.

Package the four numbers back into a grid:

$$
AB = \begin{pmatrix} 19 & 22 \\ 43 & 56 \end{pmatrix}
$$

---

## Order matters — $AB$ and $BA$ are not the same

Regular real-number multiplication does not care about order: $5 \cdot 3$ and $3 \cdot 5$ give $15$ either way. Matrix multiplication does not have that luxury. In fact, swapping the order can even change whether the product is defined in the first place. Try reversing the example above:

$$
BA = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix}
$$

Very different answer. So when you read a product, pay attention to which matrix is on the left and which is on the right — they play different roles. Because of this quirk, you will hear mathematicians say $A$ "left-multiplies" $B$ or $B$ "right-multiplies" $A$.

---

## The identity matrix

Among square matrices there is a special one called the **identity matrix** $I_n$ — a square grid with $1$s on the main diagonal and $0$s everywhere else. The $2 \times 2$ and $3 \times 3$ identities look like this:

$$
I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \qquad I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

The identity plays the same role that the number $1$ plays in ordinary multiplication: for any matrix $A$ of a compatible shape,

$$
AI = IA = A
$$

Nothing changes. This is the only situation in which order genuinely does not matter, and the identity becomes the anchor for the notion of a matrix **inverse** you will meet in [[Matrix_Methods|matrix methods]].

---

## Example 1: Combining operations

> Compute $2A - B$ for $A = \begin{pmatrix} 3 & -1 \\ 0 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & 2 \\ -3 & 1 \end{pmatrix}$.

Scale first, then subtract entry by entry. Multiply every slot of $A$ by $2$:

$$
2A = \begin{pmatrix} 6 & -2 \\ 0 & 8 \end{pmatrix}
$$

Now subtract $B$ from $2A$ componentwise:

$$
2A - B = \begin{pmatrix} 6 - 5 & -2 - 2 \\ 0 - (-3) & 8 - 1 \end{pmatrix} = \begin{pmatrix} 1 & -4 \\ 3 & 7 \end{pmatrix}
$$

The whole calculation is plain integer arithmetic on eight separate slots. That is the point of splitting things into components in the first place.

---

## Example 2: Shape check, then multiply

> Compute $AB$ for $A = \begin{pmatrix} 1 & 3 \\ -2 & 0 \\ 4 & -1 \end{pmatrix}$ and $B = \begin{pmatrix} 2 & 5 \\ -1 & 3 \end{pmatrix}$.

**Shape check.** $A$ is $3 \times 2$ and $B$ is $2 \times 2$. The inside numbers match ($2 = 2$), so the product is defined, and the answer has the outside shape $3 \times 2$.

Build each entry with a row-column dot product. Label rows of $A$ as $R_1, R_2, R_3$ and columns of $B$ as $C_1, C_2$.

$$
R_1 \cdot C_1 = 1(2) + 3(-1) = -1 \qquad R_1 \cdot C_2 = 1(5) + 3(3) = 14
$$

$$
R_2 \cdot C_1 = -2(2) + 0(-1) = -4 \qquad R_2 \cdot C_2 = -2(5) + 0(3) = -10
$$

$$
R_3 \cdot C_1 = 4(2) + (-1)(-1) = 9 \qquad R_3 \cdot C_2 = 4(5) + (-1)(3) = 17
$$

Stack the six numbers:

$$
AB = \begin{pmatrix} -1 & 14 \\ -4 & -10 \\ 9 & 17 \end{pmatrix}
$$

Note that $BA$ cannot even be formed here: $B$ has $2$ columns but $A$ has $3$ rows, and $2 \neq 3$.

---

## Example 3: The identity in action

> For $C = \begin{pmatrix} 2 & 7 \\ -3 & 5 \end{pmatrix}$, verify $CI_2 = C$.

Carry out the multiplication with $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$:

$$
CI_2 = \begin{pmatrix} 2(1) + 7(0) & 2(0) + 7(1) \\ -3(1) + 5(0) & -3(0) + 5(1) \end{pmatrix} = \begin{pmatrix} 2 & 7 \\ -3 & 5 \end{pmatrix} = C
$$

Exactly what the identity promises. Each row of $C$ is preserved because the $1$s pick out one entry and the $0$s zero out the rest.

---

## Common pitfalls

- **Adding incompatible sizes.** You can only add matrices that have the exact same number of rows and columns. A $2 \times 3$ plus a $3 \times 2$ is not defined — do not try to line them up diagonally or anything clever.
- **Forgetting the shape rule for products.** Before you start computing $AB$, check that columns of $A$ match rows of $B$. If they do not, the product is simply undefined.
- **Assuming $AB = BA$.** Commutativity fails for matrices. If an exam asks for $BA$, do not hand in $AB$ and expect partial credit — they can be entirely different grids.
- **Scaling only one row or column.** In $kA$, every single entry gets multiplied by $k$. Missing a row is the matrix equivalent of forgetting to distribute.
- **Mixing up row and column in the dot product.** The entry $(AB)_{ij}$ comes from row $i$ of the *left* matrix against column $j$ of the *right* matrix. Swap those and every number in your product comes out wrong.

---

## Prerequisites

- [[Solving_Systems_By_Substitution]] and [[Solving_Systems_By_Elimination]] — matrices are the machinery behind both methods. Seeing how variables turn into matrix slots is much easier once the pencil-and-paper versions feel routine.
- [[Vectors]] — the row-column dot product at the heart of matrix multiplication is the same dot product you use with vectors. If you are comfortable adding componentwise and dotting two lists of numbers, matrix multiplication will click faster.

---

## Problems Involving Matrix Arithmetic

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="matrix_arithmetic"></div>

---

## See Also

- [[Augmented_Matrices]] — how to turn a linear system into a matrix you can row-reduce
- [[Determinants]] — the single number a square matrix carries with it
- [[Matrix_Methods]] — using matrix operations to actually solve systems
- [[Vectors]] — the column-vector view of matrix multiplication
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
