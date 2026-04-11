---
title: "The Binomial Theorem"
type: topic
aliases: ["Binomial", "Binomial Theorem", "Binomial Coefficients", "Pascal's Triangle"]
tags: ["#branch-pre-calculus", "#topic-sequences-and-series"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "9", section: "9.1"}
related:
  - "topics/precalculus/Summation"
  - "topics/precalculus/Induction"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/precalculus/Summation"
problem_type_ids: []
figures: ["precalculus/pascals_triangle.svg"]
summary: "A one-line formula for expanding any power of a sum, plus Pascal's triangle as a bookkeeping device."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > The Binomial Theorem

# The Binomial Theorem

A **binomial** is a two-term expression like $a + b$ or $x - 3$. Raising a binomial to a small power is something you can muscle through with FOIL and the distributive property, but the work balloons quickly. $(a+b)^2$ is manageable, $(a+b)^3$ is tedious, $(a+b)^8$ is something no human wants to touch by hand. The **binomial theorem** gives you a single formula that writes out the entire expansion — every term, in order, with the right coefficient — for any whole-number power:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} \, a^{n-k} \, b^{k}.
$$

Each term is three pieces multiplied together: a **coefficient** $\binom{n}{k}$, a power of $a$, and a power of $b$. As $k$ runs from $0$ to $n$, the exponent on $a$ slides down from $n$ to $0$ while the exponent on $b$ climbs from $0$ to $n$. The two exponents always add to $n$ — that is your quick sanity check every time you write a term.

---

## Factorials and binomial coefficients

The coefficients in the formula are built from **factorials**. For any whole number $n$, the factorial $n!$ is the product of every positive integer up to and including $n$:

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 3 \cdot 2 \cdot 1,
$$

with the conventions $0! = 1$ and $1! = 1$. So $4! = 24$, $5! = 120$, and $7! = 5040$ — factorials grow fast.

A **binomial coefficient** $\binom{n}{k}$ is a specific ratio of factorials:

$$
\binom{n}{k} = \dfrac{n!}{k! \, (n-k)!}.
$$

In words, it counts the number of ways to pick $k$ things from a group of $n$, where the order of your pick does not matter. Read the symbol aloud as "$n$ choose $k$," which is where the counting interpretation comes from: how many committees of $k$ can you form out of $n$ people? That is exactly $\binom{n}{k}$.

A couple of quick facts that you can verify straight from the formula:

- $\binom{n}{0} = 1$ and $\binom{n}{n} = 1$ for every $n$.
- $\binom{n}{1} = n$ and $\binom{n}{n-1} = n$.
- **Symmetry:** $\binom{n}{k} = \binom{n}{n-k}$. Choosing $k$ winners is the same problem as choosing $n-k$ losers.

---

## Pascal's triangle

There is a famous visual bookkeeper for the binomial coefficients called **Pascal's triangle**. Each row lists the coefficients $\binom{n}{0}, \binom{n}{1}, \binom{n}{2}, \ldots, \binom{n}{n}$ for one value of $n$. The outer edges are all $1$, and every interior entry is the sum of the two numbers directly above it to the left and right. Here are the first six rows (rows $0$ through $5$):

```
n = 0:             1
n = 1:           1   1
n = 2:         1   2   1
n = 3:       1   3   3   1
n = 4:     1   4   6   4   1
n = 5:   1   5  10  10   5   1
```

Read row $5$ left to right: $1, 5, 10, 10, 5, 1$. Those are the coefficients you need for $(a+b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5$. No computation, no formula — just a copy from the triangle. That is the whole point.

![[pascals_triangle.svg|Pascal's Triangle rows 0-6]]

**Where does each entry come from?** The addition rule

$$
\binom{n}{k-1} + \binom{n}{k} = \binom{n+1}{k}
$$

is what makes the triangle work. It says: to get a number in the next row, add the two numbers in the current row that sit just above it. Let's use it to build row $5$ from row $4$, without factorials:

- Left edge: $1$ (always).
- Next: $1 + 4 = 5$.
- Next: $4 + 6 = 10$.
- Next: $6 + 4 = 10$.
- Next: $4 + 1 = 5$.
- Right edge: $1$ (always).

The row comes out to $1, 5, 10, 10, 5, 1$, which matches what is already in the triangle above. Every row can be built from the one before it by pure addition — no factorials required once you get rolling.

---

## Example 1: expanding a small power

> Use the binomial theorem to expand $(x - 2)^4$.

Match the formula to the expression: $a = x$, $b = -2$, and $n = 4$. Row $4$ of Pascal's triangle is $1, 4, 6, 4, 1$. That gives us the five coefficients straight away. Now write each term, sliding $x$'s exponent down from $4$ to $0$ and $(-2)$'s exponent up from $0$ to $4$:

$$
(x-2)^4 = 1 \cdot x^4 + 4 \cdot x^3 \cdot (-2) + 6 \cdot x^2 \cdot (-2)^2 + 4 \cdot x \cdot (-2)^3 + 1 \cdot (-2)^4.
$$

Evaluate the powers of $-2$ carefully — signs alternate because $-2$ raised to odd powers stays negative:

$$
= x^4 - 8x^3 + 24x^2 - 32x + 16.
$$

Quick sanity check: the exponents on $x$ add down to $0$ from $4$ one step at a time; the constant term at the end is $(-2)^4 = 16$, which is correct; and the linear term picks up four copies of $(-2)^3 = -8$, giving $-32x$. All consistent.

---

## Example 2: finding one specific term

> In the expansion of $(2x + y)^5$, what is the term that contains $x^3$?

You could expand the whole thing, but the formula lets you zoom in on exactly one term. Call the index of that term $k$. The general term is

$$
\binom{5}{k} (2x)^{5-k} y^{k}.
$$

We want the power of $x$ to be $3$, so we need $5 - k = 3$, which gives $k = 2$. Plug that in:

$$
\binom{5}{2} (2x)^3 y^2 = 10 \cdot 8x^3 \cdot y^2 = 80 \, x^3 y^2.
$$

(That $\binom{5}{2} = 10$ comes from row $5$ of Pascal's triangle, the $k = 2$ entry.) No other term in the expansion is needed — you landed directly on the coefficient that is $80$.

This ability to pull any term out of a large expansion is where the formula really earns its keep. It would be painful to expand $(2x+y)^{15}$ completely just to find the $x^3 y^{12}$ term — but with $k = 12$ and one formula plug-in, the answer falls out in a single line.

---

## Example 3: a numerical shortcut

> Compute $(1.01)^4$ to three decimal places without a calculator.

Write $1.01 = 1 + 0.01$ and use the theorem with $a = 1$, $b = 0.01$, $n = 4$. Row $4$ coefficients again are $1, 4, 6, 4, 1$:

$$
(1 + 0.01)^4 = 1 + 4(0.01) + 6(0.01)^2 + 4(0.01)^3 + (0.01)^4.
$$

Work each piece: $4(0.01) = 0.04$; $6(0.0001) = 0.0006$; the remaining two terms are $0.000004$ and $0.00000001$, both invisible at three decimal places. Add:

$$
(1.01)^4 \approx 1 + 0.04 + 0.0006 \approx 1.040604 \approx 1.041.
$$

Financial formulas, physics approximations, and anything else involving small perturbations leans on exactly this kind of expansion. When $b$ is tiny, the terms drop off so fast that you need only the first few.

---

## Common pitfalls

- **Dropping a sign on a negative second term.** If $b = -2$, every term where $b$ is raised to an odd power picks up a minus sign. Track the sign on $b$, not just its magnitude.
- **Exponents that do not add to $n$.** Every term of $(a+b)^n$ has exponents summing to $n$. If you write a term where the exponents add to the wrong number, it is not a term of that expansion. Fast check: add the two exponents — does the total equal $n$?
- **Misreading Pascal's triangle.** Row $n$ has $n + 1$ entries, not $n$. The very top row (just a lonely $1$) is row $0$, so "row $4$" is the row reading $1, 4, 6, 4, 1$.
- **Ignoring the power on the inner expression.** In $(2x + y)^5$, the $a$ in the formula is $2x$, not $x$. When you raise $2x$ to a power, you raise both the $2$ and the $x$. Forgetting the $2$'s power is the single most common mistake on this topic.
- **Forgetting that $0! = 1$.** A computation with $\binom{n}{0}$ or $\binom{n}{n}$ uses $0!$ in the denominator; treating $0!$ as $0$ would divide by zero and blow up the formula.

---

## Prerequisites

You will have a much easier time if you are solid on:

- [[The_Distributive_Property]] — so you know what an expansion looks like when you do it by hand.
- [[Summation]] — the theorem is written with $\Sigma$ notation, and being comfortable reading a sigma sum is half the battle.

Pair this with [[Induction]] to see where the theorem comes from — the standard textbook proof of the binomial theorem is a proof by induction.

---

## Problems Involving The Binomial Theorem

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="binomial"></div>

---

## See Also

- [[Summation]]
- [[Induction]]
- [[Probability_Of_Simple_And_Compound_Events]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
