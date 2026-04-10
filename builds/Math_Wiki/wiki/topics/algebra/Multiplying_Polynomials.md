---
title: "Multiplying Polynomials"
type: topic
aliases: ["Polynomial Multiplication", "FOIL", "Expanding Polynomials"]
tags: ["#branch-algebra-1", "#topic-polynomials"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "6", section: "6.5"}
  - {book: "algebra_2", chapter: "5", section: "5.2"}
related:
  - "topics/algebra/Adding_And_Subtracting_Polynomials"
  - "topics/algebra/Special_Products"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/pre_algebra/The_Distributive_Property"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: ["algebra/area_model_multiplication.svg"]
summary: "Every term of the first polynomial meets every term of the second — it's all just distribution, repeated."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Multiplying Polynomials

# Multiplying Polynomials

Multiplying polynomials is the place where [[The_Distributive_Property|the distributive property]] earns its keep. There is really only one rule on this whole page: every term of the first polynomial has to meet every term of the second, and the products get added together. Whether the factors are a monomial and a trinomial, two binomials, or something bigger, you are always just doing the same thing — reaching across the parentheses, again and again.

![[area_model_multiplication.svg|An area model for (x+3)(x+5)]]

$$
(a + b)(c + d) = ac + ad + bc + bd
$$

The tricks you will hear named — "FOIL," the box method, vertical multiplication — are all just bookkeeping systems that make sure you do not miss a pairing. They are not new rules.

---

## Monomial times polynomial: one distribution

The simplest version is a single term multiplying a longer polynomial. Here the distributive property applies directly: hand the outside factor to every term inside, then simplify each product using your [[Properties_Of_Exponents|exponent rules]]. Recall that when you multiply powers with the same base, you add their exponents — so $x^3 \cdot x^4 = x^7$, not $x^{12}$.

In symbols:

$$
a(b_1 + b_2 + \cdots + b_n) = ab_1 + ab_2 + \cdots + ab_n
$$

This is the atom of the whole section. Every harder case below reduces to stacking several of these on top of each other.

---

## Binomial times binomial: every pair meets

When both factors have two terms each, distribution forces every term in one factor to meet every term in the other. You can see why by distributing the whole first binomial across the second:

$$
(a + b)(c + d) = a(c + d) + b(c + d) = ac + ad + bc + bd
$$

You started with $2$ terms in one factor and $2$ in the other, and you ended up with $2 \cdot 2 = 4$ partial products. That product count is a pattern — an $m$-term polynomial times an $n$-term polynomial produces $mn$ partial products before you collect like terms.

### FOIL is a memory aid, not a new rule

You may have heard of **FOIL**, which stands for **First, Outer, Inner, Last**. It is a mnemonic for the four pairings you get when two binomials multiply:

- **F**irst: the first term in each binomial
- **O**uter: the outer pair
- **I**nner: the inner pair
- **L**ast: the last term in each binomial

FOIL works, but it is a crutch — sometimes called a "training wheel" — that only covers the binomial-times-binomial case. The moment either factor grows to three terms, FOIL stops covering the full set of pairings and you have to go back to real distribution. So it is much better to think of FOIL as a bookkeeping label for four products you were going to do anyway, not as a separate rule to memorize.

---

## Bigger products: area model and vertical method

When at least one factor has more than two terms, it pays to be systematic. Two organizers work well.

The **area model** (sometimes called the box method) draws a grid whose rows come from the terms of one factor and whose columns come from the terms of the other. You fill each cell with the product of its row and column labels, then sum every cell and gather like terms. A $2 \times 3$ grid for a binomial times a trinomial naturally gives you six partial products — exactly the number distribution predicts.

The **vertical method** stacks the polynomials the way you stack numbers for long multiplication. You multiply the top polynomial by each term of the bottom polynomial in turn, keeping like terms lined up in columns, and then sum the columns at the end. This method is especially friendly when the answer has many terms because the columnar layout makes it hard to lose track of degrees.

Both methods produce the same answer, and both are just distribution, organized.

---

## Example 1: Monomial times trinomial

> Multiply $4x^2(3x^3 - 2x + 5)$.

Hand the outside factor to each inside term in turn. Keep the signs attached to the terms they came from:

$$
4x^2(3x^3 - 2x + 5) = (4x^2)(3x^3) + (4x^2)(-2x) + (4x^2)(5)
$$

Now simplify each product. For each, multiply the coefficients and add the exponents on any matching bases:

$$
= 12x^{5} - 8x^{3} + 20x^{2}
$$

The answer has three terms because the starting polynomial had three; the monomial out front cannot create or destroy terms, it can only scale them. Notice the degree of the result ($5$) is the sum of the degrees of the factors ($2 + 3$). That rule of thumb — "degrees add under multiplication" — is a useful sanity check on any polynomial product.

---

## Example 2: Binomial times binomial via FOIL

> Multiply $(2x + 5)(3x - 4)$.

Walk the four FOIL pairings in order. First, outer, inner, last:

- **First:** $(2x)(3x) = 6x^2$
- **Outer:** $(2x)(-4) = -8x$
- **Inner:** $(5)(3x) = 15x$
- **Last:** $(5)(-4) = -20$

Stack the four partial products and combine the ones that are alike. Here $-8x$ and $15x$ are like terms:

$$
(2x + 5)(3x - 4) = 6x^2 - 8x + 15x - 20
$$

$$
= 6x^2 + 7x - 20
$$

A binomial times a binomial almost always collapses to a trinomial after like-term collection, because the outer and inner products usually share a degree. If they don't — if the exponents on the two variable parts happen to differ — you get a four-term answer instead. Both outcomes are fine; the rule is still "every pair must meet."

---

## Example 3: Binomial times trinomial by distribution

> Multiply $(x + 3)(2x^2 - x + 4)$.

Two terms times three terms means $2 \cdot 3 = 6$ partial products coming up. Distribute each term of the binomial across the whole trinomial:

$$
(x + 3)(2x^2 - x + 4) = x(2x^2 - x + 4) + 3(2x^2 - x + 4)
$$

Distribute inside each piece separately:

$$
= 2x^3 - x^2 + 4x + 6x^2 - 3x + 12
$$

Now collect like terms. The $x^2$ terms are $-x^2$ and $6x^2$; the $x$ terms are $4x$ and $-3x$; the rest stand alone:

$$
= 2x^3 + 5x^2 + x + 12
$$

If you'd rather use the vertical method for the same product, the layout looks like this:

$$
\begin{array}{rrrr}
 &  2x^2 & - \; x & + 4 \\
\times &     &     & (x + 3) \\
\hline
 &  6x^2 & - \; 3x & + 12 \\
 2x^3 & - \; x^2 & + 4x &   \\
\hline
 2x^3 & + 5x^2 & + \; x & + 12
\end{array}
$$

The top row is the trinomial times $+3$; the next row is the trinomial times $+x$, shifted left one column to keep like degrees in columns; the last line sums the columns. Either method gives $2x^3 + 5x^2 + x + 12$.

---

## A peek at special products

You will bump into three patterns so often that they deserve their own page, [[Special_Products]]:

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

$$
(a - b)^2 = a^2 - 2ab + b^2
$$

$$
(a + b)(a - b) = a^2 - b^2
$$

Every one of these is just distribution — you can derive them yourself by FOIL-ing out the left side. But they show up so often in later chapters (especially in [[Factoring_Special_Forms|factoring]] and in [[Completing_The_Square]]) that memorizing the shapes saves a lot of time.

A very common trap to watch for: $(a + b)^2$ is **not** $a^2 + b^2$. That middle term $2ab$ has to be there. Try it with actual numbers if you ever forget — $(3 + 4)^2 = 49$, not $9 + 16 = 25$. The squared sum is larger because the cross-product is missing from the wrong answer.

---

## Common pitfalls

- **Thinking FOIL is a special rule.** It is shorthand for the four products you get when two binomials multiply, and it only handles that case. If either factor has three or more terms, reach for the area model or the vertical method so you don't miss a pairing.
- **Forgetting to carry the sign.** When you distribute $-3x$ into $(2x - 4)$, the second product is $(-3x)(-4) = +12x$, not $-12x$. Keep the sign glued to the term it belongs to, and let negative-times-negative handle itself.
- **Multiplying coefficients but forgetting to add exponents.** In $(4x^3)(2x^5)$, the answer is $8x^8$, not $8x^{15}$. When bases match, exponents add.
- **Squaring a sum the wrong way.** $(x + 5)^2$ is $x^2 + 10x + 25$, not $x^2 + 25$. Write it as $(x + 5)(x + 5)$ and multiply it out — the middle term comes from the outer plus inner pairs and always has a coefficient of twice the product.

---

## Prerequisites

Before you start practicing, make sure you are solid on:

- [[The_Distributive_Property]] — every example on this page is really just repeated distribution
- [[Properties_Of_Exponents]] — to multiply powers of the same base cleanly
- [[Variables_And_Algebraic_Expressions]] — for the basic vocabulary of terms and coefficients

---

## Problems Involving Multiplying Polynomials

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="multiplying_polynomials"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Adding_And_Subtracting_Polynomials]]
- [[Special_Products]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Trinomials_General]]
- [[Properties_Of_Exponents]]
- [[The_Distributive_Property]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
