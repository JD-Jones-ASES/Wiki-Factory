---
title: "Factoring Trinomials: Leading Coefficient 1"
type: topic
aliases: ["Factoring Monic Trinomials"]
tags: ["#branch-algebra-1", "#topic-polynomials", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Greatest_Common_Factor"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Adding_And_Subtracting_Polynomials"
  - "topics/algebra/Greatest_Common_Factor"
problem_type_ids: []
figures: []
summary: "Run FOIL in reverse: find two numbers that multiply to the constant and add to the middle coefficient."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Factoring Trinomials: Leading Coefficient 1

# Factoring Trinomials: Leading Coefficient 1

You already know from [[Multiplying_Polynomials]] that when you multiply two binomials $(x + p)(x + q)$ together, the FOIL pairings produce a trinomial. In fact, if you track what happens to $p$ and $q$ as FOIL unfolds, a pattern jumps out — the middle coefficient of the result is $p + q$, and the constant term is $pq$. This entire topic is about running that process **in reverse**. Starting from a trinomial of the form $x^2 + bx + c$, you ask yourself which two numbers $p$ and $q$ would have produced that middle and last term, and once you find them, you can write the factored form immediately.

Factoring matters because it unlocks a huge amount of downstream algebra. If you can factor $x^2 - 5x + 6$ into $(x - 2)(x - 3)$, you have just learned that the equation $x^2 - 5x + 6 = 0$ is only true when one of those two factors is zero, which means $x = 2$ or $x = 3$. That is the whole idea behind [[Solving_Quadratics_By_Factoring]]. Factoring also simplifies rational expressions, reveals the zeros of a polynomial function, and helps you spot perfect squares and differences of squares. So the modest-looking search-for-two-numbers routine on this page actually drives a lot of later chapters.

## What it means / The idea

A **trinomial** is a polynomial with three terms. The trinomials on this page all have the particular shape

$$
x^2 + bx + c
$$

where the coefficient in front of $x^2$ is exactly $1$. That leading $1$ is important; the moment it is anything other than $1$, the technique is similar in spirit but needs extra care, which is handled on [[Factoring_Trinomials_General]].

To factor $x^2 + bx + c$, look for two integers $p$ and $q$ satisfying

$$
p + q = b \qquad \text{and} \qquad pq = c.
$$

When two such integers exist, the factored form is

$$
x^2 + bx + c = (x + p)(x + q).
$$

If no integer pair works, the trinomial is either **prime** over the integers (it still factors, but only with irrational or complex numbers) or it needs a different technique. For this topic you can assume every trinomial you meet has integer factors; the pairs really are findable.

## How it works / The procedure

1. **State the search clearly.** You need a pair of integers, call them $p$ and $q$, with $p \cdot q = c$ and $p + q = b$. Those are the two conditions every candidate pair has to satisfy simultaneously.
2. **List factor pairs of $c$.** If $c$ is positive, both factors are the same sign (both positive or both negative). If $c$ is negative, the two factors have opposite signs — one positive, one negative.
3. **Find the pair whose sum is $b$.** Walk through the list and check each pair's sum. As soon as one matches $b$, you have found $p$ and $q$.
4. **Write the factored form.** $(x + p)(x + q)$, with whatever signs $p$ and $q$ brought with them.
5. **Check by multiplying back out.** Multiply the two binomials via FOIL and verify you recover the original trinomial. If the middle coefficient or the constant does not match, you picked the wrong pair — go back and try another.

The signs in step 2 deserve a closer look, because they are where most errors happen. There are really three cases:

- **$c > 0$ and $b > 0$:** both $p$ and $q$ are positive.
- **$c > 0$ and $b < 0$:** both $p$ and $q$ are negative.
- **$c < 0$:** one is positive, one is negative. The larger (in absolute value) will match the sign of $b$.

## Why it works

Multiply $(x + p)(x + q)$ out and watch what happens. FOIL gives $x^2 + qx + px + pq = x^2 + (p + q)x + pq$. So if the product of those two binomials is $x^2 + bx + c$, then whatever $p$ and $q$ are, they must satisfy $p + q = b$ and $pq = c$. That is precisely the condition we are hunting for. Factoring the leading-coefficient-$1$ case is the inverse operation of multiplying two leading-coefficient-$1$ binomials, and the relationship between the coefficients is exactly what the multiplication produces. Nothing is hidden.

## Worked examples

### Example 1

Express $x^2 + 7x + 12$ as a product of two binomials.

We need two integers with product $12$ and sum $7$. Because $c = 12$ is positive and $b = 7$ is positive, both integers should be positive. Walk the positive factor pairs of $12$:

| Pair | Sum |
|---|---|
| $1, 12$ | $13$ |
| $2, 6$ | $8$ |
| $3, 4$ | $7$ |

The pair $(3, 4)$ hits both conditions: $3 \cdot 4 = 12$ and $3 + 4 = 7$. So

$$
x^2 + 7x + 12 = (x + 3)(x + 4).
$$

Check by FOIL: $(x + 3)(x + 4) = x^2 + 4x + 3x + 12 = x^2 + 7x + 12$. Matches. 

### Example 2

Express $x^2 - 5x + 6$ as a product of two binomials.

We need two integers with product $6$ and sum $-5$. The constant $c = 6$ is still positive, but the middle coefficient $b = -5$ is negative. That means both integers should be **negative** — a positive times a positive cannot be negative, so the only way to get a positive product from a negative sum is for both factors to be negative. Walk the negative factor pairs of $6$:

| Pair | Sum |
|---|---|
| $-1, -6$ | $-7$ |
| $-2, -3$ | $-5$ |

The pair $(-2, -3)$ hits both conditions. So

$$
x^2 - 5x + 6 = (x - 2)(x - 3).
$$

Check: $(x - 2)(x - 3) = x^2 - 3x - 2x + 6 = x^2 - 5x + 6$. Matches.

### Example 3

Express $x^2 + 2x - 15$ as a product of two binomials.

Now we need two integers with product $-15$ and sum $2$. Because $c = -15$ is negative, one of the integers is positive and the other is negative. The middle coefficient is $b = 2$, which is positive, so the **positive** one should have the larger absolute value. Walk the factor pairs of $-15$ where the positive one dominates:

| Pair | Sum |
|---|---|
| $-1, 15$ | $14$ |
| $-3, 5$ | $2$ |
| $-5, 3$ | $-2$ (wrong sign) |
| $-15, 1$ | $-14$ (wrong sign) |

The pair $(-3, 5)$ works: $(-3)(5) = -15$ and $-3 + 5 = 2$. So

$$
x^2 + 2x - 15 = (x - 3)(x + 5).
$$

Check: $(x - 3)(x + 5) = x^2 + 5x - 3x - 15 = x^2 + 2x - 15$. Matches.

Notice the pattern across the three examples: the signs inside the binomials are dictated by the signs of $b$ and $c$, and getting them right is the single biggest habit to build on this topic.

## Common pitfalls

- **Mixing up the sum and the product.** You are looking for two numbers whose **product** is $c$ and whose **sum** is $b$, not the other way around. If you catch yourself looking for the pair that sums to $c$, slow down and reread the problem.
- **Wrong signs on the factors.** When $c$ is negative, exactly one of the two factors is negative, not both. When $c$ is positive and $b$ is negative, both factors are negative. Write down the sign rule before you start listing pairs.
- **Ignoring negative possibilities entirely.** Some students list only positive factor pairs of $c$, even when $c$ is negative or $b$ is negative. Every integer $c$ has both positive and negative factor pairs; allow both lists.
- **Forgetting to factor out a common monomial first.** If you see $2x^2 + 14x + 24$, pull out a $2$ before doing anything else: $2(x^2 + 7x + 12) = 2(x + 3)(x + 4)$. See [[Greatest_Common_Factor]] for the details.
- **Skipping the multiplication check.** FOIL-ing your factored form back out and comparing to the original is the single best insurance against a sign error or a bad pair. Do not skip it while you are learning the technique.

## Problems Involving Factoring Trinomials with Leading Coefficient 1

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="factoring_trinomials_leading_coefficient_1"></div>

## See Also

- [[Multiplying_Polynomials]] — the forward operation that this page inverts
- [[Factoring_Trinomials_General]] — the harder version, when the leading coefficient is not $1$
- [[Factoring_Special_Forms]] — perfect squares and differences of squares
- [[Greatest_Common_Factor]] — always pull out the GCF before factoring a trinomial
- [[Solving_Quadratics_By_Factoring]] — what factoring lets you do next
- [[Special_Products]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
