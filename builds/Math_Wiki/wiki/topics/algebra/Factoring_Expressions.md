---
title: "Factoring Expressions"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-polynomials", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs:
  - {book: "algebra_1", chapter: "7", section: "7.1"}
related:
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/pre_algebra/The_Distributive_Property"
problem_type_ids: []
figures: []
summary: "A guided tour of the factoring toolkit: start with the GCF, count the remaining terms, and reach for the pattern that matches what is left."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Factoring Expressions

# Factoring Expressions

Factoring is [[Multiplying_Polynomials|multiplying]] run in reverse. When you multiply, you take factors and smash them together to get a single polynomial; when you factor, you take a single polynomial apart into a product of smaller pieces. Both directions use the same tools and the same vocabulary. What makes factoring harder is that there is usually more than one sensible move available at any moment, so you have to learn to **look** at an expression and decide what to try first.

The goal of this page is to give you that sense of sequence: a short list of moves, in the order you should try them, so that factoring stops feeling like guesswork. Once you have the sequence, each individual move — pulling a GCF, recognizing a difference of squares, splitting a trinomial — is a routine you already know.

---

## Key ideas

### The one rule: GCF first, always

Before you do anything else, look for a **greatest common factor** shared by every term of the expression. If one exists, factor it out using the distributive property and set it aside to the left of a set of parentheses. Only then should you look at what is inside those parentheses.

There are two reasons this rule is non-negotiable. First, pulling the GCF makes the remaining polynomial smaller and its numbers friendlier, which makes every later step easier. Second, forgetting to pull the GCF is the number-one cause of incomplete factoring. A polynomial like $6x^2 - 24$ is easy to rush through as $(6x + 12)(x - 2)$, which is wrong; the right way is to pull the $6$ first to get $6(x^2 - 4)$, then recognize $x^2 - 4$ as a difference of squares and finish at $6(x + 2)(x - 2)$. Always GCF first, even when you think you can skip it.

A minor refinement: if the leading coefficient of the polynomial is **negative**, it is usually cleaner to pull a negative out with the GCF so the inside polynomial starts with a positive leading coefficient. For example, $-2x^2 + 10x - 12$ factors more easily as $-2(x^2 - 5x + 6) = -2(x - 2)(x - 3)$ than it does if you try to keep the leading $-2x^2$ as is.

### After the GCF, count the terms

Once the GCF is out of the way, look at what is inside the parentheses and **count the terms**. The number of terms chooses your next move:

- **Two terms** → look for a special form. The big one is the **difference of squares**, $a^2 - b^2 = (a + b)(a - b)$. A **sum of squares** $a^2 + b^2$ does not factor over the real numbers in this course; it stays as is.
- **Three terms** → factor as a **trinomial**. If the leading coefficient is $1$, use [[Factoring_Trinomials_Leading_Coefficient_1|the product-sum method]]: find two integers whose product is the constant term and whose sum is the middle coefficient. If the leading coefficient is larger, use the AC method from [[Factoring_Trinomials_General]].
- **Four or more terms** → try **grouping**. Pair up the terms, pull a common factor out of each pair, and look for a shared binomial you can factor out next.

After you apply the matching move, **look again**. If any of the factors you just produced can still be factored, do so. This is where "factoring completely" comes from — you keep going until nothing splits any further. The full decision flow is laid out on the [[Factoring_Completely]] page.

### The patterns in one place

It is worth memorizing three patterns, because they appear constantly:

$$
a^2 - b^2 = (a + b)(a - b)
$$

$$
a^2 + 2ab + b^2 = (a + b)^2
$$

$$
a^2 - 2ab + b^2 = (a - b)^2
$$

You will see these come up again in [[Factoring_Special_Forms]]. For now, just notice that each has a distinctive shape: a difference of two perfect squares, or a trinomial whose first and last terms are perfect squares with a middle term equal to twice their "parts" multiplied together.

---

## Example 1: GCF only

> Factor $6x^2 - 15x$.

Both terms have a common numerical factor: $\gcd(6, 15) = 3$. Both terms also have at least one $x$, so $x$ is common too. The GCF is therefore $3x$.

Pull the $3x$ out in front and record what each term turns into once the $3x$ is removed:

$$
6x^2 - 15x = 3x(2x - 5)
$$

Now look inside the parentheses. The expression $2x - 5$ has two terms. Is it a difference of squares? No: $2x$ is not a perfect square ($\sqrt{2x}$ is not a nice expression) and $5$ is not a perfect square. So $2x - 5$ is **prime** — it does not factor any further over the integers — and the fully factored form is

$$
6x^2 - 15x = 3x(2x - 5)
$$

Check the answer by multiplying back out: $3x \cdot 2x + 3x \cdot (-5) = 6x^2 - 15x$. That matches, so the factoring is correct.

---

## Example 2: Difference of squares

> Factor $x^2 - 16$.

The first question is always: is there a GCF? Scan the two terms. The numerical GCF is $\gcd(1, 16) = 1$ (so nothing to pull out that way), and there is no $x$ in the constant term (so nothing variable to pull either). The GCF is just $1$, which is the same as saying there is no nontrivial GCF. That is fine — move on.

Now count terms. There are two, so look for a special form. Each term is a perfect square: $x^2 = (x)^2$ and $16 = (4)^2$. And the sign between them is minus. That is the **difference of squares** pattern with $a = x$ and $b = 4$:

$$
x^2 - 16 = (x + 4)(x - 4)
$$

Look again at the factors. Each is a binomial with a first-degree $x$ and a constant; there is no further factoring possible. Done.

Check: $(x + 4)(x - 4) = x^2 - 4x + 4x - 16 = x^2 - 16$. Matches.

One thing to notice: it is tempting to try the difference of squares on anything with a minus sign, but both terms have to be perfect squares for the pattern to apply. An expression like $x^2 - 7$ has only one perfect square, so it is **not** a difference of squares over the integers and stays prime in this course.

---

## Example 3: GCF, then a trinomial

> Factor $2x^2 + 8x + 6$ completely.

Step 1: GCF first. Scan the three coefficients: $2$, $8$, $6$. Their GCD is $2$. None of the terms share an $x$, so the GCF is just $2$.

$$
2x^2 + 8x + 6 = 2(x^2 + 4x + 3)
$$

Already the inside polynomial looks much friendlier — the leading coefficient is now $1$, which is the easy case.

Step 2: count the terms inside. There are three, so the next move is factoring the trinomial. Because the leading coefficient is $1$, use the product-sum method: find two integers whose product is the constant term $3$ and whose sum is the middle coefficient $4$. The pair $1$ and $3$ works: $1 \cdot 3 = 3$ and $1 + 3 = 4$.

$$
x^2 + 4x + 3 = (x + 1)(x + 3)
$$

Reassemble the factors with the GCF from step 1:

$$
2x^2 + 8x + 6 = 2(x + 1)(x + 3)
$$

Step 3: look again at each factor. The $2$ is a prime constant, and each of the binomials has degree $1$ with integer coefficients — none of them can be factored further. The final answer is $2(x + 1)(x + 3)$.

Check by multiplying back: $(x + 1)(x + 3) = x^2 + 4x + 3$, then $2(x^2 + 4x + 3) = 2x^2 + 8x + 6$. That matches the original, so the factoring is correct.

This example shows why the GCF step is so valuable. If you had tried to factor $2x^2 + 8x + 6$ directly as a trinomial with leading coefficient $2$, you would have needed the harder [[Factoring_Trinomials_General|AC method]]. Pulling the $2$ first converted the problem into the easy leading-coefficient-$1$ case.

---

## Common pitfalls

- **Skipping the GCF.** It is always tempting to jump straight to a trinomial or difference-of-squares step, but if there is a GCF hiding, you will end up with a messier problem and probably an incomplete answer. Make "GCF first" a reflex, even when the answer ends up being $1$.
- **Trying to factor a sum of squares.** Expressions like $x^2 + 9$ cannot be split into two binomials with real integer coefficients. If you ever catch yourself writing $x^2 + 9 = (x + 3)(x - 3)$, stop — that product is $x^2 - 9$, which has the wrong sign on the constant.
- **Stopping at a partial factoring.** Writing $6x^2 - 24 = 6(x^2 - 4)$ is good progress, but the job is not done. The $x^2 - 4$ inside is still a difference of squares. The final answer is $6(x + 2)(x - 2)$. After every step, look at each factor and ask whether it can be broken down further. The full flow is on [[Factoring_Completely]].
- **Losing a sign during grouping.** When you factor a common piece out of a pair like $-3x - 6$, pull a $-3$ out rather than $+3$, because then both pairs will share the same binomial. A sign mismatch between pairs is a signal that you pulled the wrong sign out of one of them.
- **Writing the factors but forgetting to check.** Multiplying your factors back out takes thirty seconds and catches almost every mistake. Make it part of the routine.

---

## Prerequisites

Factoring is a collection of moves, each of which has its own prep:

- [[Multiplying_Polynomials]] — because factoring is multiplication in reverse, you need to be fluent at the forward direction to recognize the patterns
- [[Greatest_Common_Factor]] — the first step of every factoring problem
- [[The_Distributive_Property]] — the underlying machinery of pulling a GCF out or multiplying factors back in to check

---

## Problems Involving Factoring Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="factoring_expressions"></div>

---

## See Also

- [[Greatest_Common_Factor]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Special_Forms]]
- [[Factoring_Completely]]
- [[Solving_Quadratics_By_Factoring]]
- [[Multiplying_Polynomials]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
