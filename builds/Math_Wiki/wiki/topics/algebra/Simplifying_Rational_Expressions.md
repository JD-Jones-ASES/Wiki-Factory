---
title: "Simplifying Rational Expressions"
type: topic
aliases: ["Rational Expressions", "Reducing Rational Expressions", "Lowest Terms"]
tags: ["#branch-algebra-1", "#topic-rational-expressions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "9", section: "9.1"}
  - {book: "algebra_2", chapter: "6", section: "6.1"}
related:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Multiplying_And_Dividing_Rational_Expressions"
  - "topics/algebra/Adding_And_Subtracting_Rational_Expressions"
  - "topics/algebra/Solving_Rational_Equations"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "Factor the top, factor the bottom, cancel what matches — then keep track of every x the original denominator hated."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Simplifying Rational Expressions

# Simplifying Rational Expressions

A **rational expression** is just a fraction where the top and the bottom are polynomials. Things like $\dfrac{3}{x + 1}$, $\dfrac{x^2 - 4}{x^2 + 5x + 6}$, and $\dfrac{2a}{a^2 - 9}$ all qualify. The word "rational" is a nod to **ratio** — these expressions are ratios of polynomials, in the same way that ordinary fractions are ratios of integers.

Everything you already know about shrinking $\dfrac{12}{18}$ down to $\dfrac{2}{3}$ carries over to this new world. The plan for reducing a rational expression is the same plan:

$$
\text{factor the top} \;\Rightarrow\; \text{factor the bottom} \;\Rightarrow\; \text{strike out matching factors}
$$

The twist — and the reason this topic gets its own whole section — is that polynomials can equal zero. And when a denominator equals zero, the whole expression explodes into something undefined. Before you ever touch the cancellation step, you have to make a list of every variable value that would break the original bottom. Those forbidden values are called **restrictions** (some books also say *excluded values* or *domain restrictions*), and they stay attached to your answer like a disclaimer that survives the cleanup.

---

## The fundamental property

The rule that licenses all the cancellation work is short enough to memorize:

$$
\frac{P \cdot R}{Q \cdot R} = \frac{P}{Q}
$$

where $P$, $Q$, and $R$ are polynomials and $Q, R$ are nonzero. Read out loud: if a polynomial factor shows up in both the numerator and the denominator, you may divide it out of both. The key word is **factor**. Not a term, not a piece of a binomial — a *factor*, something being multiplied into the whole.

The three-step routine for reducing a rational expression to lowest terms:

1. Factor the numerator completely.
2. Factor the denominator completely.
3. Find all common factors and divide them away. State the restrictions from the *original* denominator.

That third step is where most of the student error lives, and it's really two chores glued together. One chore is the algebraic cancellation. The other chore is bookkeeping for the restrictions so that they do not vanish when the expression does.

---

## Restrictions: the thing that is easy to forget

Suppose you take the expression $\dfrac{x^2 - 4}{x - 2}$. Factor the top: $(x - 2)(x + 2)$. The $(x - 2)$ matches the bottom, so after canceling you're left with $x + 2$.

Here is the subtle point. The simplified expression $x + 2$ is perfectly happy at $x = 2$; plug in and you get $4$. But the *original* expression at $x = 2$ is $\dfrac{0}{0}$, which is undefined. The two expressions agree everywhere except at that one excluded point. If you draw their graphs, the original has a single missing point — a small open circle called a **hole** — at $(2, 4)$, while the simplified line runs right through.

Because of that discrepancy, the cancellation step erases information. Canceling is an equality *only when the restrictions are written down as part of the answer*. That's why the completed form looks like

$$
\frac{x^2 - 4}{x - 2} = x + 2, \qquad x \neq 2.
$$

The tail `, x != 2` is not decoration. It is the difference between a true statement and a false one.

To collect all the restrictions, set the **original** denominator equal to zero and solve. Every solution is forbidden. If the denominator factors as a product, set each factor to zero — you may get several restrictions at once. You'll keep all of them, even the ones that cancel.

---

## Example 1: a difference of squares on top

> Reduce $\dfrac{x^2 - 9}{x^2 + 6x + 9}$ as far as possible and list the restrictions.

**First, find the restrictions.** Set the original denominator to zero: $x^2 + 6x + 9 = (x + 3)^2 = 0$, so $x = -3$. That is the only forbidden value, and it stays with the answer.

**Now factor both pieces.** The numerator is a [[Factoring_Special_Forms|difference of squares]]: $x^2 - 9 = (x - 3)(x + 3)$. The denominator is a perfect-square trinomial: $x^2 + 6x + 9 = (x + 3)(x + 3)$. Rewrite:

$$
\frac{x^2 - 9}{x^2 + 6x + 9} = \frac{(x - 3)(x + 3)}{(x + 3)(x + 3)}
$$

**Cancel the shared factor.** One $(x + 3)$ lives on top and one lives on the bottom, so divide them out:

$$
= \frac{x - 3}{x + 3}, \qquad x \neq -3.
$$

That's the final form. Notice the lonely $(x + 3)$ left in the denominator — the restriction $x \neq -3$ was already visible there, so in this particular example you don't learn anything new by writing it. But in Example 2, canceling hides a restriction, and then the disclaimer is the only thing keeping the answer honest.

---

## Example 2: the cancellation hides a restriction

> Reduce $\dfrac{6x^2 + 12x}{3x^2 + 12x + 12}$ and state the restrictions.

**Restrictions first.** The denominator $3x^2 + 12x + 12 = 3(x + 2)^2$ is zero exactly when $x = -2$. Write it down now, before you do anything else: $x \neq -2$.

**Factor the numerator.** Pull out the [[Greatest_Common_Factor|GCF]]: $6x^2 + 12x = 6x(x + 2)$. The denominator you already factored as $3(x + 2)^2$. So:

$$
\frac{6x^2 + 12x}{3x^2 + 12x + 12} = \frac{6x(x + 2)}{3(x + 2)^2}
$$

**Cancel.** One copy of $(x + 2)$ divides out, and the numerical $6$ on top shares a factor of $3$ with the denominator. What remains:

$$
= \frac{2x}{x + 2}, \qquad x \neq -2.
$$

In the simplified form $\dfrac{2x}{x + 2}$, you might think the only forbidden value is $x = -2$ — and in this particular problem you would be right, because the restriction that got exposed is the same one that was there all along. But in general, a factor can cancel off the bottom entirely, and then the restriction it carried is invisible in the simplified form. The disclaimer is the only way to recover it.

---

## Example 3: factors that are opposites in disguise

> Reduce $\dfrac{3 - x}{x^2 - 9}$.

**Restrictions.** $x^2 - 9 = (x - 3)(x + 3)$, which is zero at $x = 3$ and $x = -3$. Both are excluded.

**Spot the trap.** Look at the top $(3 - x)$ and the bottom factor $(x - 3)$. They aren't the same — they are **opposites**. The move here is to factor a $-1$ out of the numerator so the common factor becomes visible:

$$
3 - x = -(x - 3).
$$

That small rewrite turns a mismatch into a match. Substitute and cancel:

$$
\frac{3 - x}{(x - 3)(x + 3)} = \frac{-(x - 3)}{(x - 3)(x + 3)} = \frac{-1}{x + 3}, \qquad x \neq 3,\; x \neq -3.
$$

The minus sign from the flip stays in the answer. That is one of the most common missed marks in this topic — students see the cancellation and forget that the sign is along for the ride.

A quick way to recognize opposite factors: if two expressions differ only in that their sign pattern is reversed, pulling a $-1$ out of one will turn them into the same thing. Think $(a - b)$ and $(b - a)$, or $(5 - y)$ and $(y - 5)$.

---

## Common pitfalls

- **Canceling *terms* instead of *factors*.** This is the single most common mistake in the whole topic. In $\dfrac{x + 5}{x + 7}$, the $x$ on top and the $x$ on bottom are terms in a sum — they are *not* factors of the whole numerator or denominator, so you cannot cross them out. The fraction is already in lowest terms. Test the shape with numbers if you aren't sure: $\dfrac{1 + 5}{1 + 7} = \dfrac{6}{8} = \dfrac{3}{4}$, which is not $\dfrac{5}{7}$, so the cancellation was fiction.
- **Forgetting to list restrictions from the original denominator.** The simplified expression often has a smaller denominator than the one you started with, so values that were forbidden can slip out of view. Always build the restriction list from the *original* denominator, before any cancellation, and carry it through to the final answer.
- **Missing the hidden minus sign with opposite factors.** When you turn $(3 - x)$ into $-(x - 3)$, the $-1$ stays in the answer. A leftover minus sign is often the only thing separating the right answer from the wrong one.
- **Incomplete factoring.** If you only pull out a GCF and stop, you will miss cancellations that the full factoring would have caught. Factor as far as you can — every difference of squares, every trinomial, every shared monomial — before looking for common factors. The [[Factoring_Completely|"factor completely"]] habit from the previous chapter is the prerequisite skill for this one.
- **Changing restrictions mid-problem.** Don't update the restriction list after you simplify; the list comes from the *original* expression and never changes once written.

---

## Prerequisites

You need to be strong at factoring before this topic makes sense, because every problem starts with a double factoring job:

- [[Factoring_Trinomials_Leading_Coefficient_1]] — for denominators like $x^2 - x - 6$
- [[Factoring_Trinomials_General]] — for denominators with a leading coefficient other than 1
- [[Greatest_Common_Factor]] — to pull out shared monomials before trinomial factoring
- [[Factoring_Special_Forms]] — so you recognize differences of squares and perfect-square trinomials on sight
- [[Equivalent_Fractions_And_Simplifying]] — the numeric version of the same reduction you're now doing with polynomials

If any of these feels shaky, start there. Practicing rational expression simplification without clean factoring is an exercise in frustration.

---

## Problems Involving Simplifying Rational Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="simplifying_rational_expressions"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Multiplying_And_Dividing_Rational_Expressions]]
- [[Adding_And_Subtracting_Rational_Expressions]]
- [[Solving_Rational_Equations]]
- [[Factoring_Completely]]
- [[Equivalent_Fractions_And_Simplifying]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
