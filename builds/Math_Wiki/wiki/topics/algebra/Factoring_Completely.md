---
title: "Factoring Completely"
type: topic
aliases: ["Complete Factoring", "Factoring Strategy", "Unified Factoring"]
tags: ["#branch-algebra-1", "#topic-polynomials", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "7", section: "7.5"}
related:
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
problem_type_ids: []
figures: []
summary: "The unified factoring flow: pull the GCF, count the remaining terms, pick the matching pattern, and keep going until nothing splits."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Factoring Completely

# Factoring Completely

By the time you reach this topic, you have already met every factoring move the course has to offer — pulling out a greatest common factor, splitting a trinomial into a product of two binomials, spotting a difference of squares, and handling a four-term expression by grouping. What you have not yet practiced is **choosing which move to use and in what order**. That is what "factoring completely" means: keep peeling off factors until every piece left over is prime, i.e. cannot be broken down any further using the methods in this course.

Think of it as a decision flow rather than a single trick. Every polynomial you meet will send you down the same chute, and at each junction you ask a single question about what is in front of you.

---

## Strategy: the decision flow

A polynomial is factored *completely* once none of the factors left over can be split any further. Here is the routine you apply every single time, in this order:

1. **Greatest common factor first.** Look at every term and pull out the largest monomial (including any common variable powers) that divides all of them. If the leading coefficient is negative, it is usually cleaner to factor a negative out with the GCF so the inside polynomial starts with a positive coefficient.
2. **Count the terms that remain inside the parentheses.** That count chooses your next move:
   - **Two terms.** Check for a **difference of squares**, $a^2 - b^2 = (a + b)(a - b)$. A sum of squares like $a^2 + b^2$ does **not** factor over the real numbers and stays prime.
   - **Three terms.** Factor as a **trinomial**. If the leading coefficient is $1$, find two integers whose product is the constant term and whose sum is the middle coefficient. If the leading coefficient is not $1$, use the methods of [[Factoring_Trinomials_General|factoring trinomials with a leading coefficient other than 1]]. Before you start, peek at the discriminant of the trinomial visually — if it looks like $a^2 \pm 2ab + b^2$, it is a perfect-square trinomial, which is just a faster route.
   - **Four or more terms.** Try **factor by grouping**: pair the terms, factor a common piece out of each pair, then pull the shared binomial out to the outside.
3. **Can any factor still be factored?** After step 2 you should have a product of two or more factors. Look at each one. A binomial might still be a difference of squares. A trinomial might still split. Keep going until nothing on the page can be broken down again.
4. **Check your work.** Multiply the final factors back together. If you get the original polynomial, you are done. If you get something else, retrace your steps.

The single most common failure on this topic is stopping too early — treating a partial factoring as a final answer. The fix is routine: after every step, look again.

---

## Example 1: GCF, then a difference of squares

> Break $2x^3 - 8x$ into its complete factored form.

Start at step 1 and scan for a common factor. Both terms share a $2$ and a single $x$, so the GCF is $2x$.

$$
2x^3 - 8x = 2x(x^2 - 4)
$$

Move to step 2 and count the terms inside the parentheses. There are two: $x^2$ and $-4$. That is a classic **difference of squares**, with $a = x$ and $b = 2$:

$$
x^2 - 4 = (x + 2)(x - 2)
$$

Glue the result back onto the $2x$ from step 1:

$$
2x^3 - 8x = 2x(x + 2)(x - 2)
$$

Run step 3 and check each factor. The $2x$ is a monomial (prime), and each binomial has a first-degree $x$ minus or plus a constant — there is no further splitting. Done.

**Check.** $2x(x + 2)(x - 2) = 2x(x^2 - 4) = 2x^3 - 8x$. Matches the original.

---

## Example 2: GCF, then a trinomial

> Write $3x^2 - 21x + 30$ as a product of prime factors.

Step 1: every term is divisible by $3$, so pull a $3$ out front.

$$
3x^2 - 21x + 30 = 3(x^2 - 7x + 10)
$$

Step 2: three terms remain, and the leading coefficient is $1$, so look for two integers whose product is $10$ (the constant) and whose sum is $-7$ (the middle coefficient). The pair $-5$ and $-2$ works: $(-5)(-2) = 10$ and $-5 + (-2) = -7$.

$$
x^2 - 7x + 10 = (x - 5)(x - 2)
$$

Reassemble with the GCF:

$$
3x^2 - 21x + 30 = 3(x - 5)(x - 2)
$$

Step 3: the $3$ is prime, and each binomial is as simple as it gets. Nothing else factors.

**Check.** $3(x - 5)(x - 2) = 3(x^2 - 7x + 10) = 3x^2 - 21x + 30$.

---

## Example 3: four terms → grouping

> Put $x^3 + 2x^2 - 3x - 6$ into fully factored form.

Step 1: the four terms share no common monomial besides $1$, so there is no GCF to peel off this time. (Always look anyway — even when there isn't one, the check costs you nothing.)

Step 2: four terms sends you to grouping. Pair the first two and the last two:

$$
x^3 + 2x^2 - 3x - 6 = (x^3 + 2x^2) + (-3x - 6)
$$

Pull a common factor from each pair. The first pair shares $x^2$; the second pair shares $-3$:

$$
= x^2(x + 2) - 3(x + 2)
$$

Notice that $(x + 2)$ now appears in both pieces. Factor it out like a single variable:

$$
= (x + 2)(x^2 - 3)
$$

Step 3: look again. The factor $x + 2$ is a simple linear binomial and stays prime. The factor $x^2 - 3$ is a difference, but $3$ is not a perfect square, so it does not split using the difference-of-squares pattern with integers. In Algebra I it counts as prime. (Later courses show that it splits using irrational numbers: $x^2 - 3 = (x + \sqrt{3})(x - \sqrt{3})$. That is beyond this unit.)

$$
x^3 + 2x^2 - 3x - 6 = (x + 2)(x^2 - 3)
$$

**Check.** Multiply out: $(x + 2)(x^2 - 3) = x^3 - 3x + 2x^2 - 6 = x^3 + 2x^2 - 3x - 6$. That matches the starting polynomial.

---

## Common pitfalls

- **Skipping the GCF step.** Forcing yourself to find a GCF first — even when the answer is $1$ — keeps the inside polynomial smaller and the trinomial hunt much easier. Many problems that look impossible at first become trivial once the GCF is out.
- **Stopping at partial factoring.** Writing $4x^2 - 16 = 4(x^2 - 4)$ is a real accomplishment, but it is not the final answer. The inside factor is still a difference of squares, so the fully factored form is $4(x + 2)(x - 2)$. After every step, ask: *can I factor anything further?*
- **Trying to factor a sum of squares.** $x^2 + 9$ cannot be split over the real numbers. If you ever catch yourself writing $x^2 + 9 = (x + 3)(x - 3)$, stop — that product is $x^2 - 9$, which changes the sign on the constant. A sum of squares is prime in this course.
- **Losing a sign when grouping.** Pairing and factoring four-term expressions is where sign errors love to hide. Check that the two pulled-out factors leave behind the *same* binomial; if they disagree by a sign, you likely need to pull a negative out of one of the pairs.

---

## Prerequisites

Every step of the decision flow reuses a technique from an earlier topic. Make sure these are solid first:

- [[Greatest_Common_Factor]] — step 1 of the flow
- [[Factoring_Trinomials_Leading_Coefficient_1]] — the most common path for three-term polynomials
- [[Factoring_Trinomials_General]] — when the leading coefficient is not $1$
- [[Factoring_Special_Forms]] — difference of squares and perfect-square trinomials

Once all four of those feel routine, this topic is mostly about recognising which to reach for.

---

## Problems Involving Factoring Completely

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="factoring_completely"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Greatest_Common_Factor]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Trinomials_General]]
- [[Factoring_Special_Forms]]
- [[Solving_Quadratics_By_Factoring]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
