---
title: "Multiplying and Dividing Rational Expressions"
type: topic
aliases: ["Rational Expression Multiplication", "Rational Expression Division"]
tags: ["#branch-algebra-2", "#topic-rational-expressions", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "6", section: "6.3"}
related:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Adding_And_Subtracting_Rational_Expressions"
  - "topics/algebra/Solving_Rational_Equations"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Dividing_Fractions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Dividing_Fractions"
problem_type_ids: []
figures: []
summary: "Multiply two rational expressions by factoring everything first, then canceling what matches, then multiplying the survivors. Divide by flipping the second fraction and multiplying."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Multiplying and Dividing Rational Expressions

# Multiplying and Dividing Rational Expressions

Once you can [[Simplifying_Rational_Expressions|simplify one rational expression]], combining two of them through multiplication or division is just that same skill, applied with a little extra bookkeeping. The big idea is that polynomial fractions follow the same arithmetic rules as ordinary numeric fractions. If you can do

$$
\frac{2}{3} \cdot \frac{9}{4} = \frac{18}{12} = \frac{3}{2}
\qquad \text{and} \qquad
\frac{2}{3} \div \frac{4}{9} = \frac{2}{3} \cdot \frac{9}{4} = \frac{3}{2},
$$

then you already know the shape of every problem on this page. The only new wrinkle is that your numerators and denominators are polynomials instead of integers, so the shrinking step is a **factor-and-cancel** job rather than a "divide top and bottom by the greatest common factor" job.

---

## The rule for multiplication

Two rational expressions multiply by the straightforward rule that has always governed fractions:

$$
\frac{P}{Q} \cdot \frac{R}{S} = \frac{P \cdot R}{Q \cdot S}, \qquad Q \neq 0,\; S \neq 0.
$$

You could literally carry this out — multiply the two numerators, multiply the two denominators, then try to simplify whatever monster you land on — but that is almost always the wrong order of operations for a human. The smarter plan is:

1. Factor each numerator and each denominator completely.
2. Identify every common factor across the full product, top versus bottom, and divide them out.
3. Only after the canceling is done do you multiply the surviving factors together.

Factoring first makes the cancellation obvious and keeps the numbers you have to multiply small. Multiplying first turns a 3-term numerator into a 5-term monster that is much harder to factor, even though the final answer is exactly the same.

**A small but important note.** Once you cancel across a multiplication, the factor you crossed out does not belong to "the top" or "the bottom" anymore — cancellation is a cross-fraction move. A factor on the top of the *first* fraction can cancel with a factor on the bottom of the *second*, and vice versa. Think of the whole product as one giant numerator over one giant denominator while you look for matches.

---

## The rule for division

Division of rational expressions is handled with a single move: **turn the division into multiplication by flipping the second fraction upside down** (the divisor). In symbols,

$$
\frac{P}{Q} \div \frac{R}{S} = \frac{P}{Q} \cdot \frac{S}{R} = \frac{PS}{QR}, \qquad R \neq 0.
$$

After the flip, the problem is a multiplication problem, and you solve it with the three-step routine above: factor, cancel, multiply. Always flip the **second** fraction — the one you are dividing by. Flipping the first fraction is a classic error that will turn a perfectly good problem into garbage. And if you are ever asked to divide by a plain polynomial (say, by $x - 2$) rather than by a full fraction, rewrite that polynomial as $\dfrac{x - 2}{1}$ first, and then invert as usual.

### Restrictions for division are slightly trickier

For a multiplication problem, the forbidden $x$-values come from the two original denominators — any value that would make either $Q$ or $S$ equal to zero is excluded.

For a division problem, you have the same two denominators to worry about *plus* a new one: the original $R$ (the top of the second fraction), because when you flip, $R$ moves to the bottom. So a division problem has up to **three** sources of restrictions:

- values that kill $Q$ (the first denominator, which stays on the bottom),
- values that kill $S$ (the second denominator, now on top after the flip — but it was a real denominator before, so it still counts),
- values that kill $R$ (the second numerator, now a denominator after the flip).

You collect all of these restrictions from the *original* problem, before any cancellation. Cancellation can hide them, but they stay attached to the final answer.

---

## Example 1: a multiplication that needs factoring first

> Multiply $\dfrac{x^2 - 4}{x + 5} \cdot \dfrac{x + 5}{x + 2}$ and list all restrictions.

**Restrictions.** The original denominators are $(x + 5)$ and $(x + 2)$, so $x \neq -5$ and $x \neq -2$.

**Factor.** Only the first numerator needs work: $x^2 - 4$ is a difference of squares, so $(x - 2)(x + 2)$. Nothing else factors further.

$$
\frac{(x - 2)(x + 2)}{x + 5} \cdot \frac{x + 5}{x + 2}
$$

**Cancel across the whole product.** The $(x + 5)$ on the bottom of the left fraction matches the $(x + 5)$ on the top of the right fraction. The $(x + 2)$ on the top of the left fraction matches the $(x + 2)$ on the bottom of the right fraction. Both pairs divide out.

$$
= \frac{x - 2}{1} = x - 2, \qquad x \neq -5,\; x \neq -2.
$$

What is remarkable about the answer is that neither $-5$ nor $-2$ is visible in the simplified form — the polynomial $x - 2$ is a happy, defined number for every real $x$. But the restrictions came from the *original* expression, and they are still part of the answer. This is exactly why stating restrictions matters: the simplified form on its own is a different function from the original product.

---

## Example 2: division = flip and multiply

> Divide $\dfrac{x^2 + 3x}{x - 1} \div \dfrac{x^2 + 3x + 2}{x^2 - 1}$ and list all restrictions.

**Flip the divisor.** The second fraction — the one we are dividing by — turns upside down, and the division becomes multiplication:

$$
\frac{x^2 + 3x}{x - 1} \cdot \frac{x^2 - 1}{x^2 + 3x + 2}
$$

**Collect the restrictions from the original problem.** That means looking at (a) the first denominator $x - 1$, which tells you $x \neq 1$; (b) the second denominator $x^2 - 1 = (x - 1)(x + 1)$, which gives $x \neq 1$ and $x \neq -1$; and (c) the second numerator $x^2 + 3x + 2 = (x + 1)(x + 2)$, which, because it ends up in a denominator after the flip, forbids $x = -1$ and $x = -2$. Bundling: $x \neq 1$, $x \neq -1$, $x \neq -2$.

**Factor everything.**

$$
\frac{x(x + 3)}{x - 1} \cdot \frac{(x - 1)(x + 1)}{(x + 1)(x + 2)}
$$

**Cancel across the product.** The $(x - 1)$ on the bottom of the left matches the $(x - 1)$ on the top of the right, and the $(x + 1)$ on the top of the right matches the $(x + 1)$ on the bottom of the right:

$$
= \frac{x(x + 3)}{x + 2}, \qquad x \neq 1,\; x \neq -1,\; x \neq -2.
$$

Notice how two of those three restrictions — $x \neq 1$ and $x \neq -1$ — are invisible in the final form. They exist only because the *original* division problem forbade them. This is the central gotcha of division: the flip injects a new denominator, and its zeros become real forbidden values that survive the simplification.

---

## Example 3: dividing by a bare polynomial

> Simplify $\dfrac{x^2 + 2x - 8}{x + 1} \div (x - 2)$.

The divisor is a plain polynomial with no visible denominator. Rewrite it as a fraction over $1$ so the flip rule has something to work with:

$$
\frac{x^2 + 2x - 8}{x + 1} \div \frac{x - 2}{1}
$$

**Restrictions.** From the first denominator $x + 1$, you get $x \neq -1$. The divisor $x - 2$, once flipped, becomes a denominator, so $x \neq 2$.

**Flip and factor.**

$$
\frac{x^2 + 2x - 8}{x + 1} \cdot \frac{1}{x - 2} = \frac{(x + 4)(x - 2)}{(x + 1)(x - 2)}
$$

**Cancel.** The $(x - 2)$ factors on top and on bottom divide out:

$$
= \frac{x + 4}{x + 1}, \qquad x \neq -1,\; x \neq 2.
$$

This example deserves a careful look because the restriction $x \neq 2$ came entirely from the flip — nowhere in the *original* expression was there a denominator of $x - 2$. The act of dividing by $(x - 2)$ is what forbade $x = 2$, and the bookkeeping is the only thing that keeps the answer honest.

---

## Common pitfalls

- **Flipping the wrong fraction.** In a division problem, *always* invert the **second** fraction — the divisor — and leave the first one alone. Flipping the first instead is a classic wrong move that looks superficially right and then wrecks the whole problem.
- **Multiplying first, factoring later.** If you FOIL the numerators and denominators before you look for common factors, you will land on a polynomial fraction that is much harder to factor than the parts you started with. Always factor first, cancel, *then* multiply the survivors.
- **Losing division restrictions.** The second numerator $R$ becomes a denominator after the flip, so any value that makes $R = 0$ is forbidden in the original division problem. Skipping that source of restrictions is the single most common bookkeeping error in this section.
- **Canceling pieces of sums instead of factors.** The rule from the previous section still holds: you can only cancel full factors, not individual $x$'s or numbers that are being added or subtracted. $\dfrac{x + 3}{x + 5}$ is already in lowest terms.
- **Dropping the restrictions that cancel out of view.** In Examples 1 and 2 above, restrictions disappeared from the simplified form after the cancellations, but they were still real. The tail `, x != ...` at the end of your answer is not optional — it is the difference between writing an equivalent expression and writing a different function that happens to have a similar formula.

---

## Prerequisites

This topic stacks directly on top of three earlier ones, and it is effectively impossible to practice it without them:

- [[Simplifying_Rational_Expressions]] — the routine of "factor, cancel, restrict" is exactly what you need here, applied twice
- [[Factoring_Trinomials_Leading_Coefficient_1]] and [[Factoring_Trinomials_General]] — for cleaning up quadratic numerators and denominators
- [[Factoring_Special_Forms]] — so differences of squares are instant-recognition
- [[Multiplying_Fractions]] and [[Dividing_Fractions]] — the arithmetic version of everything on this page. If the numeric version feels unfamiliar, spend ten minutes there first; the polynomial version will suddenly feel much gentler.

---

## Problems Involving Multiplying and Dividing Rational Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="multiplying_and_dividing_rational_expressions"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Simplifying_Rational_Expressions]]
- [[Adding_And_Subtracting_Rational_Expressions]]
- [[Solving_Rational_Equations]]
- [[Multiplying_Fractions]]
- [[Dividing_Fractions]]
- [[Factoring_Completely]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
