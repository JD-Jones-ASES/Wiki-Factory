---
title: "Factoring Trinomials: General"
type: topic
aliases: ["AC Method", "Factoring by Grouping", "Factoring Trinomials a Not 1"]
tags: ["#branch-algebra-1", "#topic-polynomials", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "7", section: "7.3"}
related:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Multiplying_Polynomials"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Multiplying_Polynomials"
problem_type_ids: []
figures: []
summary: "Factor ax^2 + bx + c when a is not 1 by splitting the middle term using a product-and-sum search, then grouping."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Factoring Trinomials: General

# Factoring Trinomials: General

Once the leading coefficient on a quadratic is something other than $1$, the quick "find two numbers that multiply to $c$ and add to $b$" trick from [[Factoring_Trinomials_Leading_Coefficient_1]] stops working on its own. The numbers out front muddy the arithmetic, so you need a slightly more careful approach. The method on this page — the **ac method**, sometimes called factor-by-grouping — extends the same habit of thinking in product-and-sum pairs, but routes it through one extra step so any leading coefficient becomes workable.

A general trinomial has the shape:

$$
ax^2 + bx + c
$$

with $a \neq 0$ (and on this page, usually $a \neq 1$). The goal is to rewrite it as a product of two binomials.

---

## The ac method, step by step

Instead of searching for factors of the constant term, you search for factors of the **product** $a \cdot c$, and then use those numbers to split the middle term into two pieces that factor nicely by grouping.

1. Identify $a$, $b$, and $c$ from the trinomial.
2. Compute the product $ac$.
3. Hunt for two integers — call them $m$ and $n$ — whose **product is $ac$** and whose **sum is $b$**.
4. Replace the middle term $bx$ with $mx + nx$, turning the trinomial into a four-term polynomial.
5. Bracket the left pair of terms and the right pair of terms, then pull the greatest common factor out of each bracket separately.
6. If you did step 5 correctly, the two groups should reveal the same binomial factor. Pull that shared binomial out as a final GCF.

If no integer pair $m, n$ exists that hits both targets, the trinomial cannot be factored over the integers — it is **prime**.

### Pull the GCF first

Before any of that, glance at all three terms and ask: do they share a common factor? If yes, pull it out using [[Greatest_Common_Factor|greatest common factor]] techniques before you start hunting for $m$ and $n$. Shrinking the coefficients early makes the remaining search dramatically faster, and missing this shortcut is the single most common waste of time on general-trinomial problems.

### A brief alternative: trial factors

You can also guess and check. Write placeholders like $(?\,x + ?)(?\,x + ?)$, list the factor pairs of $a$ and the factor pairs of $c$, and test combinations until the outer plus inner products give you $bx$. This works, but with large $a$ and $c$ the search tree gets big in a hurry, which is exactly why the ac method exists — it turns guessing into arithmetic.

---

## Example 1: a straightforward ac walkthrough

> Rewrite $2x^2 + 11x + 12$ as a product of two binomials.

Identify $a = 2$, $b = 11$, $c = 12$, so $ac = 2 \cdot 12 = 24$.

Find two integers whose product is $24$ and whose sum is $11$. List factor pairs of $24$: $1 \cdot 24$, $2 \cdot 12$, $3 \cdot 8$, $4 \cdot 6$. The pair $3$ and $8$ works, because $3 \cdot 8 = 24$ and $3 + 8 = 11$.

Split the middle term $11x$ into $3x + 8x$:

$$
2x^2 + 3x + 8x + 12
$$

Bracket the left pair and the right pair, then pull a GCF out of each bracket:

$$
x(2x + 3) + 4(2x + 3)
$$

Both groups share the factor $(2x + 3)$. Pull it out:

$$
(2x + 3)(x + 4)
$$

Check by multiplying the binomials back out: $(2x + 3)(x + 4) = 2x^2 + 8x + 3x + 12 = 2x^2 + 11x + 12$. Match.

---

## Example 2: a negative constant term

> Split $3x^2 - 7x - 6$ into factors.

Here $a = 3$, $b = -7$, $c = -6$, so $ac = 3 \cdot (-6) = -18$. Because $ac$ is negative, the two numbers you want will have **opposite signs** — one positive, one negative. Because the sum $b = -7$ is negative, the larger piece (by absolute value) has to be the negative one.

Factor pairs of $18$ with mixed signs: $\{1, -18\}$, $\{-1, 18\}$, $\{2, -9\}$, $\{-2, 9\}$, $\{3, -6\}$, $\{-3, 6\}$. Check sums: $2 + (-9) = -7$. That's the winner.

Split $-7x$ into $2x - 9x$:

$$
3x^2 + 2x - 9x - 6
$$

Group and pull GCFs:

$$
x(3x + 2) - 3(3x + 2)
$$

Notice that the second group pulls out $-3$ so the surviving binomial matches $(3x + 2)$. Factoring that shared binomial out gives:

$$
(3x + 2)(x - 3)
$$

Quick multiply check: $(3x + 2)(x - 3) = 3x^2 - 9x + 2x - 6 = 3x^2 - 7x - 6$. Correct.

---

## Example 3: pull a GCF first, then factor

> Find the factored form of $4x^3 + 10x^2 - 6x$.

First scan: every term has a factor of $2$ and an $x$, so the GCF is $2x$. Pulling it out:

$$
4x^3 + 10x^2 - 6x = 2x\!\left(2x^2 + 5x - 3\right)
$$

Now apply the ac method to the trinomial inside the parentheses. With $a = 2$, $b = 5$, $c = -3$, compute $ac = 2 \cdot (-3) = -6$. Find integers multiplying to $-6$ and summing to $5$: the pair $6$ and $-1$ works, since $6 + (-1) = 5$.

Split the middle term:

$$
2x^2 + 6x - x - 3
$$

Group and pull GCFs:

$$
2x(x + 3) - 1(x + 3)
$$

Share the binomial out:

$$
(x + 3)(2x - 1)
$$

Put the $2x$ from the GCF back in front, and the fully factored answer is:

$$
4x^3 + 10x^2 - 6x = 2x(x + 3)(2x - 1)
$$

Any of those three factors — $2x$, $(x + 3)$, or $(2x - 1)$ — could be missed if you tried to factor the trinomial before pulling the GCF, which is why the first scan matters so much.

---

## Common pitfalls

- **Skipping the GCF scan.** If $4x^2 + 14x + 12$ looks intimidating, remember that every term shares a $2$. Pulling it out leaves $2(2x^2 + 7x + 6)$, which is much smaller to factor.
- **Wrong sign on one of $m, n$.** When $ac$ is positive and $b$ is positive, both numbers are positive. When $ac$ is positive and $b$ is negative, both are negative. When $ac$ is negative, the two numbers have opposite signs and the bigger absolute value takes the sign of $b$.
- **Losing the binomial match during grouping.** After pulling the GCF out of each group, the two remaining binomials must be **identical**. If they differ by a sign, try factoring $-1$ out of the second group instead.
- **Forgetting to check by multiplying.** Every factored answer should be double-checked by expanding with FOIL or distribution. If the middle term doesn't come out right, one of the two binomials is wrong.
- **Declaring a trinomial prime too early.** Before you give up, verify you've listed every factor pair of $ac$, including negative ones. A missed pair is not the same as "no pair exists."

---

## Prerequisites

Before grinding through practice problems, make sure you are solid on:

- [[Factoring_Trinomials_Leading_Coefficient_1]] — the product-and-sum search when $a = 1$, which is the core skill you are extending
- [[Greatest_Common_Factor]] — so the "pull out the GCF first" step is automatic
- [[Multiplying_Polynomials]] — so you can verify every factoring with a clean FOIL check

---

## Problems Involving Factoring Trinomials: General

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="factoring_trinomials_general"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Special_Forms]]
- [[Factoring_Completely]]
- [[Solving_Quadratics_By_Factoring]]
- [[Greatest_Common_Factor]]
- [[Multiplying_Polynomials]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
