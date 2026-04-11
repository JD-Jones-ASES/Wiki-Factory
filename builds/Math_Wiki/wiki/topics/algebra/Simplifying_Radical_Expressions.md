---
title: "Simplifying Radical Expressions"
type: topic
aliases: ["Simplifying Radicals", "Simplest Radical Form", "Rationalizing Denominators"]
tags: ["#branch-algebra-1", "#topic-exponents-and-radicals"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "9", section: "9.4"}
related:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Rational_Exponents"
  - "topics/algebra/Operations_With_Radicals"
  - "topics/algebra/Powers_And_Roots"
  - "topics/algebra/Properties_Of_Exponents"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Divisibility_Factors_And_Prime_Factorization"
  - "topics/algebra/Properties_Of_Exponents"
problem_type_ids: []
figures: []
summary: "Rewrite radicals in their tidiest form: no perfect squares trapped inside, no fractions under the radical, and no radicals stuck in the denominator."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Simplifying Radical Expressions

# Simplifying Radical Expressions

A **radical expression** is any expression that carries a radical sign — most commonly a square root. The stuff sitting under the radical is called the **radicand**. So in $\sqrt{18}$ the radicand is $18$, and in $\sqrt{3x + 7}$ the radicand is $3x + 7$.

Two different-looking radical expressions can actually name the same number. For example, $\sqrt{72}$ and $6\sqrt{2}$ are equal — but the second one is cleaner, smaller, and easier to compare with other radicals. Teachers and textbooks agree on a tidy standard called **simplest radical form**, and every simplification technique in this lesson is aimed at putting an expression into that form.

A square-root expression is in simplest radical form whenever all three of these conditions hold:

- No factor of the radicand is itself a perfect square (other than $1$).
- The radicand contains no fractions.
- No radical appears below a fraction bar.

The last rule — no radicals in the denominator — has its own name: you must **clear the radical from the bottom**, a move traditionally called rationalizing. Before we get to that, we need two workhorse rules for moving numbers in and out of a radical.

---

## The product and quotient rules

Square roots distribute across multiplication and division (but **not** across addition or subtraction — that's a famous trap). For any non-negative $a$ and $b$:

$$
\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}
$$

And for non-negative $a$ and **positive** $b$:

$$
\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}}
$$

These two rules do almost all the work. The first lets you break a radicand into pieces and pull a perfect-square chunk out of the radical. The second lets you separate a fraction into two independent radicals you can simplify on their own.

---

## Key ideas

- A radical is "simplified" when there's nothing left to factor out, nothing under a fraction bar, and nothing stranded in a denominator.
- Strategy for square roots: factor the radicand into a **largest perfect-square factor** times whatever is left, then pull the square root of the perfect square outside the radical.
- The product rule $\sqrt{ab} = \sqrt{a}\sqrt{b}$ is what actually lets you "pull things out." The quotient rule handles radicands that are fractions.
- To clear a simple radical from a denominator, multiply the top and bottom by that radical. The square of a square root is just the number, so the bottom becomes rational.
- Radicals do *not* split over sums. $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$. Always factor, never add terms inside the radical and distribute.

---

## Worked Example 1: Rewrite $\sqrt{72}$ in simplest radical form

> Reduce $\sqrt{72}$ to simplest radical form.

Start by looking for the **largest perfect square** that divides $72$. Work through your memorized squares from the top down: is $72$ divisible by $36$? Yes, because $72 = 36 \cdot 2$. That's the one we want — it's the biggest perfect square hiding inside the radicand.

Now apply the product rule and split the radical into two pieces:

$$
\sqrt{72} = \sqrt{36 \cdot 2} = \sqrt{36} \cdot \sqrt{2}
$$

The first factor is a perfect square, so take its root:

$$
= 6\sqrt{2}
$$

That's the answer. The $2$ under the radical can't be reduced any further because $2$ has no perfect-square factors (besides the trivial $1$), so $6\sqrt{2}$ is in simplest radical form.

**Why finding the largest perfect square matters.** You could also have written $72 = 4 \cdot 18$ and then $\sqrt{72} = \sqrt{4} \cdot \sqrt{18} = 2\sqrt{18}$. That answer isn't yet in simplest form — the $18$ still hides a factor of $9$. You'd need a second round of simplification: $\sqrt{18} = \sqrt{9 \cdot 2} = 3\sqrt{2}$, so $2\sqrt{18} = 2 \cdot 3\sqrt{2} = 6\sqrt{2}$. Same answer, extra work. Spotting the biggest square up front saves a pass.

---

## Worked Example 2: A radicand that is a fraction

> Rewrite $\sqrt{\dfrac{18}{25}}$ in simplest radical form.

This expression violates the second rule — the radicand is a fraction. Use the quotient rule to split it into two separate radicals:

$$
\sqrt{\dfrac{18}{25}} = \dfrac{\sqrt{18}}{\sqrt{25}}
$$

The denominator is friendly right away, because $25$ is a perfect square: $\sqrt{25} = 5$.

$$
= \dfrac{\sqrt{18}}{5}
$$

The numerator still needs work. Factor $18$ as $9 \cdot 2$ to pull out a perfect square:

$$
\sqrt{18} = \sqrt{9 \cdot 2} = 3\sqrt{2}
$$

Slot that back in:

$$
= \dfrac{3\sqrt{2}}{5}
$$

Now check the three rules. The radicand inside the numerator is $2$, which has no perfect-square factors — good. There's no fraction inside the radical anymore — good. There's no radical in the denominator — good. Done.

---

## Worked Example 3: Clearing a radical from the denominator

> Rewrite $\dfrac{1}{\sqrt{3}}$ so that no radical appears below the bar.

The expression itself is perfectly legal, but by convention we don't leave a lone radical sitting in a denominator. The trick is simple: multiply the fraction by a carefully chosen form of $1$.

Multiply the top and bottom by $\sqrt{3}$. Because $\dfrac{\sqrt{3}}{\sqrt{3}}$ equals $1$, this doesn't change the value of the fraction — only its appearance.

$$
\dfrac{1}{\sqrt{3}} \cdot \dfrac{\sqrt{3}}{\sqrt{3}} = \dfrac{\sqrt{3}}{\sqrt{3} \cdot \sqrt{3}}
$$

The denominator becomes $\sqrt{3} \cdot \sqrt{3} = \sqrt{9} = 3$. (That's exactly why the trick works: multiplying a square root by itself cancels the radical.)

$$
= \dfrac{\sqrt{3}}{3}
$$

No radical remains in the denominator, and the numerator is already in simplest form. Done.

### Bonus: a conjugate rationalization

What if the denominator is something like $\dfrac{1}{\sqrt{2} + 1}$? Multiplying top and bottom by $\sqrt{2}$ won't work, because $(\sqrt{2} + 1)\sqrt{2} = 2 + \sqrt{2}$ — still a radical. Instead, multiply by the **conjugate** $\sqrt{2} - 1$. That turns the denominator into a difference of squares:

$$
\dfrac{1}{\sqrt{2} + 1} \cdot \dfrac{\sqrt{2} - 1}{\sqrt{2} - 1} = \dfrac{\sqrt{2} - 1}{(\sqrt{2})^2 - 1^2} = \dfrac{\sqrt{2} - 1}{2 - 1} = \sqrt{2} - 1
$$

Both radicals in the denominator vanish in one move. This conjugate technique gets its full treatment in [[Operations_With_Radicals]].

---

## Common pitfalls

- **Splitting a radical across a sum.** $\sqrt{a + b}$ is not $\sqrt{a} + \sqrt{b}$. The numeric test is brutal: $\sqrt{9 + 16} = \sqrt{25} = 5$, but $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$. Radicals only split over products, never sums.
- **Stopping before the radicand is fully reduced.** After your first simplification, look at what's left under the radical. If it still has a perfect-square factor (say, $18 = 9 \cdot 2$), keep going.
- **Forgetting to square the factor in the conjugate step.** When you multiply by the conjugate, the bottom becomes $a^2 - b^2 c$ — you square both pieces, not just one.
- **Leaving a radical in the denominator.** An answer like $\dfrac{5}{\sqrt{2}}$ is technically correct but not in simplest form. Multiply top and bottom by $\sqrt{2}$ to finish.

---

## Prerequisites

Before you tackle simplification problems, be solid on these:

- [[Square_Roots_And_Cube_Roots]] — you need the square roots of small perfect squares on automatic recall, because that's the move that actually pulls numbers out of radicals.
- [[Divisibility_Factors_And_Prime_Factorization]] — the fastest way to find the largest perfect-square factor of a large radicand is to factor it into primes and pair them up.
- [[Properties_Of_Exponents]] — the product rule for radicals is really the exponent rule $\left(ab\right)^{1/2} = a^{1/2} b^{1/2}$ in a different costume. Knowing exponents makes the radical rules obvious instead of mysterious.

---

## Problems Involving Simplifying Radical Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="simplifying_radical_expressions"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Square_Roots_And_Cube_Roots]]
- [[Rational_Exponents]]
- [[Operations_With_Radicals]]
- [[Powers_And_Roots]]
- [[Properties_Of_Exponents]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
