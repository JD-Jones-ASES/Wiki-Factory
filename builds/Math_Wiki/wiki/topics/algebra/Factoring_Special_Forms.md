---
title: "Factoring Special Forms"
type: topic
aliases: ["Difference of Squares", "Perfect Square Trinomial", "Special Factoring Patterns"]
tags: ["#branch-algebra-1", "#topic-polynomials", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "7", section: "7.4"}
related:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Special_Products"
  - "topics/algebra/Multiplying_Polynomials"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Special_Products"
  - "topics/algebra/Multiplying_Polynomials"
problem_type_ids: []
figures: []
summary: "Recognize and reverse two patterns: the difference of two squares and the perfect square trinomial."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Factoring Special Forms

# Factoring Special Forms

Two factoring patterns show up so often that students who memorize them save hours of grinding. They are the reversed versions of the famous [[Special_Products|special products]] you already met when multiplying binomials: the difference of squares, and the perfect square trinomial. Once you learn to **spot** them on sight, you can skip the ac method entirely and jump straight to the answer.

The trick is not just knowing the patterns — it is knowing when to apply them and when a polynomial only looks special but really isn't. Example 3 on this page is about exactly that test.

---

## Pattern 1: Difference of squares

For any two expressions $a$ and $b$:

$$
a^2 - b^2 = (a + b)(a - b)
$$

**How to recognize it:** the polynomial has exactly two terms, it is a subtraction, and **each term is a perfect square**. Perfect squares among the numbers you meet in Algebra 1 are $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$, and so on. Any variable raised to an even power is a perfect square, too: $x^2$, $x^4 = (x^2)^2$, $9y^2 = (3y)^2$, and $25n^6 = (5n^3)^2$.

**Watch out for the sign.** The pattern is a *difference* — the two terms must be connected by a minus sign. A **sum of squares** like $x^2 + 9$ does **not** factor over the real numbers. If you try to write $x^2 + 9 = (x + 3)(x - 3)$ you have accidentally created $x^2 - 9$ instead, and the expression $x^2 + 9$ stays prime.

## Pattern 2: Perfect square trinomial

There are two mirror-image versions of this pattern, one for each sign of the middle term:

$$
a^2 + 2ab + b^2 = (a + b)^2
$$

$$
a^2 - 2ab + b^2 = (a - b)^2
$$

**How to recognize it:** the polynomial has three terms, and:

1. The **first term** is a perfect square. Call its square root $a$.
2. The **last term** is a perfect square. Call its square root $b$.
3. The **middle term** has an absolute value equal to $2 \cdot a \cdot b$ — twice the product of the two square roots you just identified.

If all three conditions are met, the trinomial collapses into either $(a + b)^2$ or $(a - b)^2$ depending on the sign of the middle term. If condition 3 fails even when the first and last are perfect squares, you **do not have** a perfect square trinomial and you must factor it the normal way with the ac method from [[Factoring_Trinomials_General]].

---

## Example 1: a difference of squares

> Find the factored form of $4x^2 - 25$.

First, scan the shape: two terms, separated by minus. Second, check each term against the perfect-square test.

- $4x^2 = (2x)^2$, so the first term is a perfect square with $a = 2x$.
- $25 = 5^2$, so the last term is a perfect square with $b = 5$.

Slot those into the difference-of-squares pattern:

$$
4x^2 - 25 = (2x + 5)(2x - 5)
$$

Verify by multiplying the binomials: $(2x + 5)(2x - 5) = 4x^2 - 10x + 10x - 25 = 4x^2 - 25$. The cross terms cancel, which is always how a correct difference-of-squares factoring checks out.

---

## Example 2: a perfect square trinomial

> Rewrite $x^2 + 10x + 25$ as a squared binomial.

Three terms, so a perfect square trinomial is a candidate. Run the three-step test:

1. First term: $x^2 = (x)^2$. Perfect square with $a = x$. Good.
2. Last term: $25 = 5^2$. Perfect square with $b = 5$. Good.
3. Middle term check: $2ab = 2 \cdot x \cdot 5 = 10x$. That is exactly what the trinomial has. Good.

Because the middle term is **positive**, use the $(a + b)^2$ version of the pattern:

$$
x^2 + 10x + 25 = (x + 5)^2
$$

Check: $(x + 5)^2 = (x + 5)(x + 5) = x^2 + 5x + 5x + 25 = x^2 + 10x + 25$. Correct.

A quick mirror example to seal in the idea: $x^2 - 14x + 49$ has $a = x$, $b = 7$, and middle term $-14x = -2 \cdot x \cdot 7$, so it factors as $(x - 7)^2$. Same pattern, negative sign version.

---

## Example 3: looks special, but isn't — the critical test

> Try to factor $x^2 + 6x + 8$ as a perfect square trinomial.

At a glance this looks promising — three terms, the first term is $x^2$. Run the test anyway.

1. First term: $x^2 = (x)^2$. Perfect square with $a = x$. Good.
2. Last term: $8$. Is $8$ a perfect square? No — $\sqrt{8}$ is not an integer. The test already fails.

Even if you ignored step 2, step 3 would have flagged the problem: if you pretended $b = \sqrt{8}$, the required middle term would be $2 \cdot x \cdot \sqrt{8} = 2\sqrt{8}\,x$, which is nowhere near $6x$. Either way, **this is not a perfect square trinomial.** It is just an ordinary leading-coefficient-1 trinomial, so you factor it with the regular method from [[Factoring_Trinomials_Leading_Coefficient_1]]:

Search for two numbers whose product is $8$ and whose sum is $6$. The pair $2$ and $4$ works. So:

$$
x^2 + 6x + 8 = (x + 2)(x + 4)
$$

The takeaway: **always run the three checks before trusting the pattern.** Spotting "$x^2 + \text{stuff} + \text{stuff}$" is not enough. Running through the conditions takes ten seconds and prevents writing an answer like $(x + \sqrt{8})^2$, which is wrong and unhelpful.

---

## Common pitfalls

- **Treating a sum of squares as factorable.** Over the real numbers, $a^2 + b^2$ is prime. Do not write $x^2 + 16 = (x + 4)(x - 4)$ — that product is $x^2 - 16$, not $x^2 + 16$.
- **Forgetting to check the middle term.** Seeing $x^2$ and a perfect square on the ends is a hint, not a certificate. Confirm that the middle term equals $2ab$ before claiming a perfect square trinomial.
- **Sign on the wrong spot.** A **difference** of squares gives a product with one plus and one minus: $(a + b)(a - b)$. A **perfect square trinomial** with a minus in the middle gives a single squared factor $(a - b)^2$. Different patterns, different layouts.
- **Ignoring the GCF.** Before testing special forms, check whether all terms share a common factor. The polynomial $2x^2 - 50$ is not literally a difference of squares as written, but pulling out $2$ gives $2(x^2 - 25) = 2(x + 5)(x - 5)$.
- **Confusing $a$ and $b$ for the numbers vs. the square roots.** In the patterns, $a$ and $b$ are the **square roots** of the first and last terms, not the terms themselves. If the first term is $9x^2$, then $a = 3x$, not $9x^2$.

---

## Prerequisites

Before you practice the special-form patterns, make sure you are comfortable with:

- [[Factoring_Trinomials_Leading_Coefficient_1]] — the plain trinomial-factoring method you fall back on when the pattern doesn't apply
- [[Special_Products]] — the multiplication side of the same patterns, so you understand why they reverse the way they do
- [[Multiplying_Polynomials]] — so every factoring you write can be verified in under a minute

---

## Problems Involving Factoring Special Forms

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="factoring_special_forms"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Trinomials_General]]
- [[Factoring_Completely]]
- [[Solving_Quadratics_By_Factoring]]
- [[Special_Products]]
- [[Multiplying_Polynomials]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
