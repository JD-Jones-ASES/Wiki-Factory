---
title: "Greatest Common Factor"
type: topic
aliases: ["GCF", "GCF of Monomials", "Common Factor"]
tags: ["#branch-algebra-1", "#topic-polynomials"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "7", section: "7.1"}
related:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Factoring_Completely"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/algebra/Multiplying_Polynomials"
problem_type_ids: []
figures: []
summary: "Find the largest common factor of a set of terms, then pull it out of a polynomial — the first step of every factoring problem."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Greatest Common Factor

# Greatest Common Factor

Factoring is the [[The_Distributive_Property|distributive property]] run backwards. Instead of taking $3(2x + 5)$ and multiplying it out to $6x + 15$, you start at $6x + 15$ and work backwards to $3(2x + 5)$. The piece you pull to the outside is the **greatest common factor** of the terms — the largest quantity that divides evenly into every term of the polynomial.

Pulling the GCF out is the first move in almost every factoring problem you will ever do. Trinomial factoring, the [[Factoring_Special_Forms|difference of squares]], grouping — each of those techniques works best (and sometimes only works at all) once the GCF is gone. Students who skip this step end up fighting needlessly ugly numbers for the rest of a problem; students who make it a habit clean up half the mess for free.

$$
\text{GCF}(A, B, C) \cdot \Bigl(\text{remaining polynomial}\Bigr) = A + B + C
$$

---

## Key ideas

### Finding the GCF of monomials

A monomial is made of two kinds of parts: a numerical coefficient (a whole number) and one or more variable powers. The GCF is built in those two parts independently and then multiplied together.

**Numerical piece.** Take the ordinary GCF of the numbers you already know from pre-algebra. If the coefficients are $12$ and $18$, the largest integer dividing both is $6$. If the coefficients are $20$, $50$, and $15$, the largest integer dividing all three is $5$.

**Variable piece.** Look at each variable separately. A variable can only appear in the GCF if it appears in **every** term, and its exponent in the GCF is the **smallest** exponent it carries across the terms. If $x$ shows up as $x^3$, $x^5$, and $x^2$, the GCF gets $x^2$ — the smallest count, because that is the most $x$'s you can safely pull out of each term at once. If a variable is missing from even one term, it can't go in the GCF at all.

**Combine.** Multiply the numerical GCF by each variable piece. That product is the monomial GCF.

### Factoring the GCF out of a polynomial

Once you know the GCF, the rest is three mechanical steps:

1. Write the GCF outside a set of parentheses.
2. Divide every term of the polynomial by the GCF and write the quotients inside the parentheses.
3. Multiply back as a check — the expanded form must match the original exactly.

That third step catches almost every error people make with GCF factoring, so get into the habit of doing it. Distributing the GCF back through is usually faster than the factoring itself.

### The GCF can be more than a monomial

A common factor doesn't have to be a single number or variable — it can be an entire parenthesized group. If the same binomial shows up in two places, treat the whole binomial as one piece and pull it out exactly the same way. This is the secret behind **factoring by grouping**, and it shows up constantly once you start working with four-term polynomials. Example 3 below walks through a case.

---

## Example 1: finding the GCF of three monomials

> Find the GCF of $24x^4 y^2$, $36 x^2 y^5$, and $60 x^3 y^3$.

Work the numerical piece first. The coefficients are $24$, $36$, and $60$. Running through the divisors, the largest integer that divides all three is $12$. (Check: $24 = 12 \cdot 2$, $36 = 12 \cdot 3$, $60 = 12 \cdot 5$.)

Now the variables. For $x$, the exponents are $4$, $2$, and $3$. The smallest is $2$, so the GCF contribution is $x^2$. For $y$, the exponents are $2$, $5$, and $3$. The smallest is $2$, so the GCF contribution is $y^2$.

Multiplying the three pieces together:

$$
\text{GCF} = 12 x^2 y^2
$$

You can double-check by dividing each original term by this GCF and seeing whether the quotients are still clean monomials: $24 x^4 y^2 / 12 x^2 y^2 = 2x^2$, $36 x^2 y^5 / 12 x^2 y^2 = 3 y^3$, and $60 x^3 y^3 / 12 x^2 y^2 = 5 x y$. Three clean monomials, so the GCF is correct.

---

## Example 2: factoring a GCF out of a trinomial

> Factor $20 x^4 - 45 x^3 + 15 x^2$.

**Step 1 — Find the GCF of the three terms.** The coefficient GCF of $20$, $45$, and $15$ is $5$. Every term has at least $x^2$, and the smallest power of $x$ present is $x^2$. So the GCF is $5 x^2$.

**Step 2 — Divide each term by $5 x^2$.** Line them up:

$$
\dfrac{20 x^4}{5 x^2} = 4 x^2, \qquad
\dfrac{-45 x^3}{5 x^2} = -9 x, \qquad
\dfrac{15 x^2}{5 x^2} = 3
$$

**Step 3 — Write the factored form.** The GCF goes outside and the three quotients go inside the parentheses:

$$
20 x^4 - 45 x^3 + 15 x^2 = 5 x^2 \bigl( 4 x^2 - 9 x + 3 \bigr)
$$

**Check by distributing.** $5 x^2 \cdot 4 x^2 = 20 x^4$, $5 x^2 \cdot (-9x) = -45 x^3$, and $5 x^2 \cdot 3 = 15 x^2$. Match — the factoring is correct.

The trinomial inside the parentheses still doesn't factor nicely, but that's fine. Pulling out the GCF cleaned up the coefficients dramatically and is often as much as a problem wants from you.

---

## Example 3: the GCF is a binomial

> Factor $3(x - 5) - 2x(x - 5)$.

Both terms in this expression contain the same binomial factor $(x - 5)$. That binomial is the common piece you can pull out, even though it has two letters and a minus sign inside it. Treat $(x - 5)$ as though it were a single object — call it $B$ for a moment if that helps — and look at what sits next to it in each term: a $+3$ in the first term and a $-2x$ in the second term.

Pulling the shared $(x - 5)$ outside:

$$
3(x - 5) - 2x(x - 5) = (x - 5) \bigl( 3 - 2x \bigr)
$$

Check by multiplying back: $(x - 5)(3) - (x - 5)(2x) = 3(x - 5) - 2x(x - 5)$. Correct.

This is what the GCF really means in its broadest form — "any factor common to every term," not just numbers and single letters. Once you see a binomial show up in more than one place, you can always pull it out, and doing so is what lets [[Factoring_Completely|factoring by grouping]] untangle four-term polynomials later in the chapter.

---

## Common pitfalls

- **Taking the biggest coefficient but forgetting the variables.** The GCF of $12 x^3 y^2 - 18 x^2 y$ is $6 x^2 y$, not just $6$. If you stop at the coefficient, you leave factors of $x$ and $y$ on the table and the inner polynomial is not as simple as it should be.
- **Using the largest exponent instead of the smallest.** For variables, the exponent in the GCF is the **smallest** power that appears, not the largest. Pulling out more than every term actually has leaves one or more terms with a negative exponent, which isn't a factoring error you can hide.
- **Forgetting to divide every term.** When you pull the GCF out, every term in the polynomial changes. If you only divide two out of three, the factored form won't multiply back to the original. Always write the three (or four) quotients out side by side before building the parentheses.
- **Skipping the check.** Multiplying the GCF back into the parentheses is almost free and catches nearly every arithmetic mistake. The source books are blunt about this: if the expansion doesn't match the original polynomial, something is wrong, so redo the step.
- **Dropping the last $1$.** When the GCF divides a term exactly into itself — for example, $5x$ divided by $5x$ — the quotient is $1$, not $0$. Don't erase the term; write the $1$ inside the parentheses so the count of terms stays right.

---

## Prerequisites

Before you practice GCF factoring, make sure you are comfortable with:

- [[Properties_Of_Exponents]] — so you can confidently divide $x^4$ by $x^2$ and read off $x^2$ as the answer
- [[The_Distributive_Property]] — GCF factoring is distribution run in reverse, and the check step is literal distribution
- [[Multiplying_Polynomials]] — so expanding the factored form back into the original is quick and reliable

---

## Problems Involving Greatest Common Factor

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="greatest_common_factor"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Multiplying_Polynomials]] — the forward operation that GCF factoring reverses
- [[Factoring_Trinomials_Leading_Coefficient_1]] — the next step after GCF, handling $x^2 + bx + c$
- [[Factoring_Trinomials_General]] — factoring with a non-$1$ leading coefficient, where pulling the GCF first is often essential
- [[Factoring_Special_Forms]] — the three memorized patterns from [[Special_Products]] run in reverse
- [[Factoring_Completely]] — combining GCF with trinomial and special-form techniques
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
