---
title: "Solving Quadratics by Factoring"
type: topic
aliases: ["Zero Product Property", "Solving Quadratic Equations by Factoring"]
tags: ["#branch-algebra-1", "#topic-quadratics", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "8", section: "8.1"}
related:
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Quadratic_Functions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "Move everything to one side so the other side is zero, factor, and read the roots off each factor — the first method for solving quadratics."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Quadratics by Factoring

# Solving Quadratics by Factoring

A **quadratic equation** is any equation you can rearrange into the shape

$$
ax^2 + bx + c = 0,
$$

where $a$, $b$, and $c$ are numbers and $a \ne 0$. The highest power of the variable is exactly $2$, and that is the form we call *standard form*. Linear equations had at most one solution; quadratics can have two, one (a repeated root), or none at all among the real numbers. The first solving technique you learn — the one this topic is built around — is short enough to summarize in a single sentence: **make one side zero, factor the other side, then read off the values of $x$ that make each factor vanish.**

That trick leans on a single, clean fact about real numbers.

---

## The zero-product idea

Here is the fact that makes the whole method work. It might look obvious, but notice what the word "zero" is doing:

$$
\text{If } a \cdot b = 0, \text{ then } a = 0 \text{ or } b = 0 \text{ (or both).}
$$

Real numbers have no sneaky way of multiplying to zero by accident. The only way to get a product of zero is for at least one of the factors to already be zero. This is sometimes written as an "or" statement because you do not need *both* factors to be zero — just one is enough.

**This fact is only true when the other side is zero.** If you have a product like $(x - 2)(x + 1) = 4$, you cannot split it into $x - 2 = 4$ and $x + 1 = 4$. That would be completely invalid, because there are infinitely many pairs of numbers whose product is $4$ — say $2 \cdot 2$, or $8 \cdot \tfrac{1}{2}$, or $(-1) \cdot (-4)$ — and only the case where the product equals *zero* forces one of the factors to take a specific value. This is the one insight students lose the most points for on tests, so burn it in now: **before you split the factors, one side must be zero.**

### Strategy

Every problem on this topic follows the same four steps:

1. **Get zero on one side.** If the equation is not already in standard form, move every term to the left side so the right side reads $0$.
2. **Factor the left side completely.** Pull a GCF if there is one, then factor the remaining polynomial using the tools from [[Factoring_Completely]].
3. **Set each factor equal to zero.** The zero-product idea splits the single quadratic equation into two or more simpler equations — usually linear.
4. **Solve each small equation and collect the roots.** Each tiny equation gives one candidate value for $x$. Together they form the **solution set** of the original quadratic.

Optional but recommended: substitute each answer back into the *original* equation to confirm it makes both sides balance.

---

## Example 1: a standard-form trinomial

> Find all real solutions to $x^2 - 5x + 6 = 0$.

Step 1 is already done — the right side is zero. Jump to step 2 and factor the left. Two numbers that multiply to $6$ and add to $-5$: the pair $-2$ and $-3$ does it. So

$$
x^2 - 5x + 6 = (x - 2)(x - 3),
$$

which means the equation becomes

$$
(x - 2)(x - 3) = 0.
$$

Now step 3. By the zero-product idea, the product on the left is zero only when one of the two factors is zero. That gives two small linear equations:

$$
x - 2 = 0 \quad \text{or} \quad x - 3 = 0.
$$

Solve each one independently: $x = 2$ or $x = 3$.

**Check.** For $x = 2$: $(2)^2 - 5(2) + 6 = 4 - 10 + 6 = 0$. For $x = 3$: $(3)^2 - 5(3) + 6 = 9 - 15 + 6 = 0$. Both hit zero on the nose.

**Solution:** $x = 2$ or $x = 3$.

---

## Example 2: rearrange first

> Find all real solutions to $x^2 + 4x = 12$.

The right side is $12$, not $0$, so this is one of those classic trap cases. Do **not** try to factor yet. Move the $12$ to the left first by subtracting it from both sides:

$$
x^2 + 4x - 12 = 0.
$$

Now you are in standard form. Factor the trinomial: look for two integers whose product is $-12$ and whose sum is $4$. The pair $6$ and $-2$ fits: $6 \cdot (-2) = -12$ and $6 + (-2) = 4$. So

$$
(x + 6)(x - 2) = 0.
$$

Split using the zero-product idea:

$$
x + 6 = 0 \quad \text{or} \quad x - 2 = 0,
$$

giving $x = -6$ or $x = 2$.

**Check.** For $x = -6$: $(-6)^2 + 4(-6) = 36 - 24 = 12$. For $x = 2$: $(2)^2 + 4(2) = 4 + 8 = 12$. Both work against the original equation.

**Solution:** $x = -6$ or $x = 2$.

If you had tried to split the factors *before* moving the $12$ over, you would have been staring at something like $(x)(x + 4) = 12$, which is a dead end — there is no rule that lets you set $x = 12$ or $x + 4 = 12$. Always, *always* get zero on one side first.

---

## Example 3: a GCF case, and why $x = 0$ counts

> Find all real solutions to $2x^2 - 8x = 0$.

Step 1: the right side is already zero. Step 2: the left side has no constant term, but both pieces share a common monomial $2x$. Pull it out:

$$
2x(x - 4) = 0.
$$

Step 3 splits this into two equations: $2x = 0$ or $x - 4 = 0$. The first gives $x = 0$, the second gives $x = 4$.

**Solution:** $x = 0$ or $x = 4$.

Notice that $x = 0$ is a perfectly legitimate answer — $0$ is a number like any other. Students sometimes discard it out of habit because it "looks empty," but substituting it back in gives $2(0)^2 - 8(0) = 0 - 0 = 0$, which matches the right side. It earns a spot in the solution set.

There is also a tempting shortcut that must be avoided. Some students look at $2x^2 - 8x = 0$ and think: "Let me just divide both sides by $x$ to make things simpler." That move produces $2x - 8 = 0$, which gives $x = 4$ and drops the $x = 0$ answer entirely. **Never cancel a variable off both sides of an equation** — that variable might secretly be zero, and you will silently lose half your roots. Factor instead, every time.

---

## Common pitfalls

- **Setting factors equal to the right-hand side when it is not zero.** From $(x - 5)(x + 1) = 7$, writing $x - 5 = 7$ is the single biggest mistake on this topic. The zero-product idea only licenses the split when the right side is literally $0$. Subtract the $7$ first so the equation reads $(x - 5)(x + 1) - 7 = 0$, expand and re-factor, *then* split.
- **Forgetting to collect every term on one side.** If the equation starts as $x^2 = 9 - 2x$, you need to pull both the $9$ and the $-2x$ to the left before factoring: $x^2 + 2x - 9 = 0$. Skipping this step leaves you with garbage on the right that cannot be factored cleanly.
- **Dividing both sides by a variable expression.** As in Example 3, dividing by $x$ silently assumes $x \ne 0$ and throws away any root at zero. Factor the common piece out instead.
- **Thinking every quadratic factors over the integers.** A lot of quadratics simply do not split nicely — their roots are irrational or complex, and you will need either [[Solving_Quadratics_By_Square_Roots|square roots]], [[Completing_The_Square|completing the square]], or [[The_Quadratic_Formula|the quadratic formula]] to get them. This method is only your first tool, not your only one.

---

## Prerequisites

- [[Factoring_Completely]] — because step 2 is "factor completely" and the decision flow there is exactly what you need
- [[Factoring_Trinomials_Leading_Coefficient_1]] — the most common path for step 2
- [[Multi_Step_Equations]] — for the small linear equations that step 4 produces after the factors split apart

---

## Problems Involving Solving Quadratics by Factoring

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_quadratics_by_factoring"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Factoring_Completely]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Trinomials_General]]
- [[Greatest_Common_Factor]]
- [[Solving_Quadratics_By_Square_Roots]]
- [[Completing_The_Square]]
- [[The_Quadratic_Formula]]
- [[Quadratic_Functions]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
