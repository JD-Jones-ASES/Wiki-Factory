---
title: "Polynomial Basics"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-polynomials", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs:
  - {book: "algebra_1", chapter: "6", section: "6.1"}
related:
  - "topics/algebra/Adding_And_Subtracting_Polynomials"
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/pre_algebra/Evaluating_Expressions"
problem_type_ids: []
figures: []
summary: "The vocabulary of polynomials: terms, coefficients, degree, leading coefficient, and the standard form that organizes it all."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Polynomial Basics

# Polynomial Basics

Before you can add, subtract, multiply, or factor polynomials, you have to be able to **talk** about them. That is the whole job of this page: name the parts, measure them, and write the whole thing in a standard shape so anybody reading it knows what they are looking at. It is the algebra equivalent of labelling the pieces before you build anything. Once the vocabulary is in place, every later polynomial topic — [[Adding_And_Subtracting_Polynomials|combining like terms]], [[Multiplying_Polynomials|multiplying out]], even [[Factoring_Completely|factoring completely]] — becomes a conversation about those same parts.

A **polynomial** in one variable is a sum of **terms**, where every term is a constant (a number) multiplied by a non-negative whole-number power of the variable. Nothing fancier is allowed. If you see a square root sitting over an $x$, or an $x$ in the denominator of a fraction, or a variable up in an exponent, you are no longer looking at a polynomial.

$$
a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0
$$

Every letter in that template has a name, and those names are the whole point of this topic.

---

## Key ideas

### Terms, coefficients, and the constant term

A **term** is one of the chunks separated by $+$ or $-$ signs. In the polynomial $5x^3 - 2x^2 + 7x - 4$, the four terms are $5x^3$, $-2x^2$, $7x$, and $-4$. Notice that the sign belongs to the term to its right — the second term is **negative** $2x^2$, not $2x^2$. When you separate terms, always pull the sign along with the number.

The numerical factor in front of a variable is the **coefficient** of that term. In $5x^3$, the coefficient is $5$. In $-2x^2$, the coefficient is $-2$. When a term is just a letter, like $x$, the coefficient is $1$ hiding in silence — $x$ means $1x$. When a term is just a number, like $-4$, there is no variable attached at all, and we call it the **constant term**. A constant term is still a term; it is the one term whose value never depends on $x$.

### Degree of a term, degree of a polynomial

The **degree** of a single term is the exponent on the variable in that term. So $5x^3$ has degree $3$, $-2x^2$ has degree $2$, and $7x$ has degree $1$ because $x$ is the same as $x^1$. The constant term $-4$ has degree $0$, because $-4 = -4 \cdot x^0$ and $x^0 = 1$. That last bit catches people — a plain number is not "degree nothing," it is degree zero. It still gets counted.

The **degree of the whole polynomial** is the largest degree among all of its terms, not the degree of the term you happen to write first. So in $5x^3 - 2x^2 + 7x - 4$, the degree is $3$, because $3$ is the biggest exponent that appears anywhere. If you were to write the same polynomial scrambled up as $7x - 4 + 5x^3 - 2x^2$, the degree would still be $3$. Order of writing does not change the underlying polynomial.

### Leading term, leading coefficient

Once you know the degree, the **leading term** is the term that has that degree — the top-degree piece. In $5x^3 - 2x^2 + 7x - 4$, the leading term is $5x^3$. The **leading coefficient** is the number in front of the leading term, which here is $5$. The leading coefficient matters a lot later on: it controls the end behavior of [[Polynomial_Functions_And_Graphs|polynomial graphs]], and a good factoring strategy often starts by checking whether the leading coefficient is $1$ or something larger.

### Monomials, binomials, trinomials

Polynomials get classified by **how many terms** they have, and the names you hear most often cover the small cases:

- A **monomial** has one term. Examples: $6$, $-3x$, $4x^2$, $\tfrac{1}{2}x^7$.
- A **binomial** has two terms. Examples: $x + 5$, $3x^2 - 8$, $4x^5 + 2x^2$.
- A **trinomial** has three terms. Examples: $x^2 + 7x + 12$, $2a^2 - 5a + 1$.

Past three terms, people usually just say "a polynomial with four terms" instead of inventing a new name. And remember: the classification is by term count, not by degree. The trinomial $x^2 + 7x + 12$ has three terms but degree $2$, while the binomial $4x^5 + 2$ has two terms but degree $5$.

### Standard form

A polynomial is in **standard form** (or **descending order**) when its terms are arranged so the degrees go from highest to lowest as you read left to right. The polynomial $5x^3 - 2x^2 + 7x - 4$ is already in standard form. The same polynomial written as $-4 + 7x - 2x^2 + 5x^3$ contains exactly the same information but is not in standard form. Putting a polynomial in standard form is almost always the first thing you do, because it makes the leading term obvious and the degree is instant.

---

## Example 1: Identify the degree and leading coefficient

> Determine the degree and the leading coefficient of $3x^4 - 5x^2 + 7$. Classify it by the number of terms.

Start by counting terms: there are three chunks separated by $+$ and $-$, namely $3x^4$, $-5x^2$, and $7$. Three terms means this is a **trinomial**.

Now measure the degree of each term. The first term $3x^4$ has degree $4$. The second term $-5x^2$ has degree $2$. The third term $7$ is a constant, so it has degree $0$. The biggest of those is $4$, so the **degree of the polynomial is $4$**.

The leading term is the term with that top degree, which is $3x^4$. The number in front of it is $3$, so the **leading coefficient is $3$**.

A thing worth noticing: the polynomial is missing $x^3$ and $x^1$ terms, and it still has degree $4$. Missing a term in the middle does not lower the degree — it just means the coefficients on those middle powers are zero. You could write this polynomial as $3x^4 + 0x^3 - 5x^2 + 0x + 7$ if you wanted to make that explicit, and it comes up often in [[Polynomial_Division|polynomial division]], where those zeros become important placeholders.

---

## Example 2: Classify a binomial

> Give the classification and degree of $4x^2 - 9$.

Count the terms first: $4x^2$ and $-9$. Two terms makes this a **binomial**.

Find the degree of each term. The first term $4x^2$ has degree $2$ because of the exponent on $x$. The constant $-9$ has degree $0$. The larger of these is $2$, so the **degree of the polynomial is $2$**. The leading term is $4x^2$ and the leading coefficient is $4$.

This particular binomial has a name you will meet again soon. Because the first term is a perfect square ($4x^2 = (2x)^2$) and the second term is $-9 = -(3)^2$, the whole thing is a **difference of squares**: $4x^2 - 9 = (2x+3)(2x-3)$. You will not need to factor it for this topic, but recognizing that the vocabulary lines up — binomial, degree 2, two perfect squares with a minus sign between — is exactly the kind of pattern-spotting that [[Factoring_Special_Forms|factoring special forms]] builds on.

---

## Example 3: Put a polynomial in standard form

> Write $7 + 2x - 5x^3$ in standard form, then state its degree and leading coefficient.

The terms are $7$, $2x$, and $-5x^3$. Their degrees are $0$, $1$, and $3$ respectively. Standard form wants the biggest degree first, so I should reorder them as degree $3$, then degree $1$, then degree $0$. Carry each sign along with its term when you move it:

$$
7 + 2x - 5x^3 = -5x^3 + 2x + 7
$$

Now the degrees go $3, 1, 0$ from left to right — that is descending order. The **degree is $3$** and the **leading coefficient is $-5$**. Notice that the leading coefficient is allowed to be negative; "leading" means "comes first in standard form," not "positive."

A common slip at this step is to forget that the polynomial has no $x^2$ term and write something like $-5x^3 + 0x^2 + 2x + 7$ to show that. That is not wrong — it is the same polynomial — but it is usually cleaner to leave the zero-coefficient term out entirely unless you are setting up for [[Polynomial_Division|long or synthetic division]], where placeholders actually matter.

---

## Common pitfalls

- **Forgetting that a constant has degree zero.** The number $-4$ is not "ungraded" — it is degree $0$, because $-4 = -4x^0$. This matters when you compare it to the other terms to find the polynomial's overall degree, and it matters in [[Polynomial_Functions_And_Graphs|polynomial function graphs]] where the constant term controls the $y$-intercept.
- **Reading the degree off the first-written term.** If a polynomial is not in standard form, the first term you see might not have the biggest exponent. Always scan every term and take the largest exponent as the degree, regardless of where it appears. Better yet: rewrite in standard form first and the leading term is obvious.
- **Dropping the sign when a term moves.** When you reorder $7 + 2x - 5x^3$ into $-5x^3 + 2x + 7$, the minus sign stays glued to the $5x^3$. A term's sign is part of the term, not a separate piece of punctuation.
- **Confusing "coefficient" with "constant."** The coefficient of $3x^2$ is $3$; the constant term of $3x^2 + 5$ is $5$. Those are two different words for two different roles. Every term has a coefficient (the number in front), but only the degree-zero term is called the constant term.
- **Calling something a polynomial when it isn't.** Expressions like $\dfrac{4}{x}$, $\sqrt{x} + 1$, and $2^x$ are not polynomials because the exponents on the variable are not non-negative whole numbers. A polynomial's variable exponents must be $0, 1, 2, 3, \ldots$ and nothing else.

---

## Prerequisites

Before you settle into this topic, make sure these feel routine:

- [[Variables_And_Algebraic_Expressions]] — the basic idea of a variable and a term
- [[Properties_Of_Exponents]] — so that the powers $x^2$, $x^3$, $x^4$ are not a mystery
- [[Evaluating_Expressions]] — for plugging numbers into a polynomial once you know its parts

---

## Problems Involving Polynomial Basics

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polynomial_basics"></div>

---

## See Also

- [[Adding_And_Subtracting_Polynomials]]
- [[Multiplying_Polynomials]]
- [[Polynomial_Functions_And_Graphs]]
- [[Properties_Of_Exponents]]
- [[Variables_And_Algebraic_Expressions]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
