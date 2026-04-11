---
title: "Polynomial Division"
type: topic
aliases: []
tags: ["#branch-algebra-2", "#topic-polynomials", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "5", section: "5.3"}
related:
  - "topics/algebra/Polynomial_Basics"
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Polynomial_Basics"
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/pre_algebra/The_Distributive_Property"
problem_type_ids: []
figures: []
summary: "Long division and synthetic division turn polynomials into quotients and remainders, the same way numerical long division breaks up integers."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Polynomial Division

# Polynomial Division

Polynomial division is the polynomial version of the long division you already know how to do with whole numbers. The goal is the same: take a big expression, split it across a smaller one, and figure out what the big one equals as a quotient plus a leftover piece. When you divide $17$ by $5$ you get $3$ with a remainder of $2$, which you can record as $17 = 5 \cdot 3 + 2$. When you divide the polynomial $P(x)$ by the polynomial $D(x)$ you get a **quotient** $Q(x)$ and a **remainder** $R(x)$, which you record the same way:

$$
P(x) = D(x) \cdot Q(x) + R(x)
$$

The remainder $R(x)$ has smaller degree than the divisor $D(x)$, just like the numerical remainder $2$ is smaller than the divisor $5$. If the remainder turns out to be $0$, the division came out clean, and the divisor is a **factor** of the dividend. Otherwise there is a leftover piece that you carry along as a fraction.

This page shows two tools for doing the work by hand: **polynomial long division**, which handles any divisor, and **synthetic division**, which is a shortcut that works only when the divisor has the form $(x - c)$ for some number $c$.

---

## Key ideas

### Setup: write everything in standard form

Before you divide, put both the dividend and the divisor in [[Polynomial_Basics|standard form]] with the highest-degree terms first. Then check whether any powers are missing from the dividend. If the dividend skips a power — say, it has an $x^3$ term and an $x^1$ term but no $x^2$ term — you must insert a placeholder with coefficient zero, i.e. $0x^2$, in the gap. Without that placeholder the columns stop lining up and you will lose track of what is being subtracted from what. This is the single most common place the procedure breaks down, and inserting the zero term before you start the division fixes it before it starts.

### Long division: mimic the integer algorithm

Polynomial long division looks exactly like the long division you did in grade school, only with letters. The steps repeat until you cannot go any further:

1. **Divide** the leading term of the current dividend by the leading term of the divisor. That quotient goes on top.
2. **Multiply** the divisor by that new quotient term.
3. **Subtract** that product from the current dividend. Be careful here: distribute the subtraction sign across every term of what you are subtracting.
4. **Bring down** the next term from the original dividend.
5. **Repeat** until the current dividend has a smaller degree than the divisor. What is left is the remainder.

You stop when the thing sitting in front of you has a smaller degree than the divisor — just like you stop long-dividing $17$ by $5$ when the leftover $2$ is smaller than $5$.

### Synthetic division: the fast lane for $(x - c)$

When the divisor is a linear binomial of the form $(x - c)$, you can skip most of the writing and work only with the coefficients. **Synthetic division** does exactly that. The procedure:

1. Write $c$ in a box on the left. (If the divisor is $x - 2$, then $c = 2$. If the divisor is $x + 3$, rewrite it as $x - (-3)$ and use $c = -3$. The sign flips.)
2. Write the coefficients of the dividend in a row to the right of the box, in standard-form order, with **zero placeholders for any missing powers**.
3. Bring the first coefficient straight down.
4. Multiply that number by $c$ and write the product under the next coefficient. Add the column.
5. Repeat step 4 for every remaining column.
6. The last number in the bottom row is the remainder. The earlier numbers are the coefficients of the quotient, whose degree is one less than the dividend.

Synthetic division is faster but narrower: it only helps when the divisor is linear with leading coefficient $1$. For anything else, fall back to long division.

### Why you would ever want to do this

There are three big reasons polynomial division keeps showing up:

1. **Factoring higher-degree polynomials.** If you already know one root of $P(x)$, say $x = 2$, then $(x - 2)$ divides $P(x)$ cleanly, and dividing lets you peel off that factor so you can work on the smaller quotient that remains.
2. **Simplifying rational expressions.** In later courses, turning $\dfrac{P(x)}{D(x)}$ into "quotient plus remainder over divisor" is the setup for integration, partial fractions, and [[Polynomial_Functions_And_Graphs|graphing rational functions]].
3. **The Remainder Theorem.** Dividing $P(x)$ by $(x - c)$ and reading off the remainder is the same as plugging $c$ into $P(x)$. That is a surprisingly fast way to evaluate polynomials, and it is also why synthetic division is such a good tool for root-checking.

---

## Example 1: Clean long division

> Compute the quotient $(x^2 + 5x + 6) \div (x + 2)$.

Both polynomials are already in standard form, and no powers are missing from the dividend, so no placeholders are needed. Set up long division with the dividend $x^2 + 5x + 6$ underneath and the divisor $x + 2$ outside.

**Step 1.** Divide the leading term $x^2$ of the dividend by the leading term $x$ of the divisor: $x^2 \div x = x$. Write $x$ on top.

**Step 2.** Multiply the divisor by that new term: $x \cdot (x + 2) = x^2 + 2x$.

**Step 3.** Subtract $x^2 + 2x$ from $x^2 + 5x$. Distribute the minus sign: $(x^2 + 5x) - (x^2 + 2x) = 3x$.

**Step 4.** Bring down the next term of the dividend, which is $+6$. The new working dividend is $3x + 6$.

**Step 5.** Divide the leading term $3x$ by the leading term $x$ of the divisor: $3x \div x = 3$. Write $+3$ on top next to the $x$. Multiply: $3 \cdot (x + 2) = 3x + 6$. Subtract: $(3x + 6) - (3x + 6) = 0$.

The remainder is $0$ and the quotient on top is $x + 3$, so

$$
\frac{x^2 + 5x + 6}{x + 2} = x + 3
$$

A clean zero remainder tells you $(x + 2)$ is a **factor** of $x^2 + 5x + 6$. In fact, $x^2 + 5x + 6 = (x + 2)(x + 3)$, which you can check by multiplying the factors back out.

---

## Example 2: Long division with a remainder

> Determine the quotient and remainder when $2x^3 - 3x^2 + 4x - 5$ is divided by $x - 1$.

The dividend is $2x^3 - 3x^2 + 4x - 5$, which has all four powers present — no zero placeholders needed. Set up long division with $x - 1$ outside.

Divide the leading term: $2x^3 \div x = 2x^2$. Write $2x^2$ on top. Multiply the divisor: $2x^2 \cdot (x - 1) = 2x^3 - 2x^2$. Subtract: $(2x^3 - 3x^2) - (2x^3 - 2x^2) = -x^2$.

Bring down $+4x$. The working dividend is $-x^2 + 4x$.

Divide: $-x^2 \div x = -x$. Write $-x$ on top. Multiply: $-x \cdot (x - 1) = -x^2 + x$. Subtract: $(-x^2 + 4x) - (-x^2 + x) = 3x$.

Bring down $-5$. The working dividend is $3x - 5$.

Divide: $3x \div x = 3$. Write $+3$ on top. Multiply: $3 \cdot (x - 1) = 3x - 3$. Subtract: $(3x - 5) - (3x - 3) = -2$.

The degree of $-2$ is $0$, which is less than the degree $1$ of the divisor, so the procedure stops. The quotient is $2x^2 - x + 3$ and the remainder is $-2$, which you record as

$$
\frac{2x^3 - 3x^2 + 4x - 5}{x - 1} = 2x^2 - x + 3 + \frac{-2}{x - 1}
$$

or equivalently $2x^3 - 3x^2 + 4x - 5 = (x - 1)(2x^2 - x + 3) + (-2)$. A non-zero remainder tells you $(x - 1)$ is **not** a factor. By the Remainder Theorem, this also means $P(1) = -2$, which you can check directly: $2(1)^3 - 3(1)^2 + 4(1) - 5 = 2 - 3 + 4 - 5 = -2$. Matches.

---

## Example 3: Synthetic division

> Use synthetic division to compute $(x^3 - 2x^2 + 3x - 6) \div (x - 2)$.

The divisor is $(x - 2)$, so $c = 2$. The dividend $x^3 - 2x^2 + 3x - 6$ has all four powers represented (coefficients $1, -2, 3, -6$), so no zero placeholders are needed.

Write $c$ in a box on the left and the coefficients to the right:

$$
\begin{array}{c|cccc}
2 & 1 & -2 & 3 & -6 \\
  &   &    &   &    \\
\hline
  &   &    &   &
\end{array}
$$

**Bring down** the first coefficient: $1$.

**Multiply** $1 \cdot 2 = 2$ and write it in the second column. **Add**: $-2 + 2 = 0$.

**Multiply** $0 \cdot 2 = 0$ and write it in the third column. **Add**: $3 + 0 = 3$.

**Multiply** $3 \cdot 2 = 6$ and write it in the fourth column. **Add**: $-6 + 6 = 0$.

The bottom row reads $1 \; 0 \; 3 \; 0$. The last entry, $0$, is the remainder. The earlier entries $1, 0, 3$ are the coefficients of the quotient, whose degree is one less than the dividend's degree of $3$, so the quotient has degree $2$:

$$
\frac{x^3 - 2x^2 + 3x - 6}{x - 2} = x^2 + 0x + 3 = x^2 + 3
$$

The remainder is $0$, so $(x - 2)$ is a factor and $x^3 - 2x^2 + 3x - 6 = (x - 2)(x^2 + 3)$. You can check by multiplying back: $(x - 2)(x^2 + 3) = x^3 + 3x - 2x^2 - 6 = x^3 - 2x^2 + 3x - 6$. Confirmed.

---

## Common pitfalls

- **Forgetting to insert zero placeholders.** If the dividend is $x^3 + 5x - 4$ (no $x^2$ term), you must rewrite it as $x^3 + 0x^2 + 5x - 4$ before dividing. Skipping the placeholder throws every column out of alignment and the whole calculation falls apart. This is the number one source of wrong answers on this topic.
- **Getting the sign of $c$ wrong in synthetic division.** When dividing by $(x + 3)$, remember that $(x + 3) = (x - (-3))$, so $c = -3$, not $+3$. Synthetic division always uses the number that makes the divisor equal to zero, not the number you see written.
- **Distributing subtraction carelessly.** In long division, every subtract step subtracts a whole polynomial. That minus sign has to reach every term. Forgetting to flip the sign on the second or third term inside the parentheses is a classic source of errors.
- **Stopping too early.** Keep dividing as long as the current working polynomial has degree at least as big as the divisor. The procedure ends when what is left has a smaller degree than the divisor — that is your remainder.
- **Using synthetic division on the wrong kind of divisor.** Synthetic division only works when the divisor is of the form $(x - c)$ — linear, leading coefficient $1$, one variable. If the divisor is $(2x - 3)$ or $(x^2 + 1)$ or anything else, reach for long division instead.

---

## Prerequisites

Polynomial division reuses several earlier skills, so have these solid first:

- [[Polynomial_Basics]] — the vocabulary (degree, leading term, standard form) you need before dividing
- [[Multiplying_Polynomials]] — the subtract step requires you to multiply the divisor by each new quotient term
- [[The_Distributive_Property]] — the subtract step also requires careful sign distribution

---

## Problems Involving Polynomial Division

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polynomial_division"></div>

---

## See Also

- [[Polynomial_Basics]]
- [[Multiplying_Polynomials]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Solving_Quadratics_By_Factoring]]
- [[Polynomial_Functions_And_Graphs]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
