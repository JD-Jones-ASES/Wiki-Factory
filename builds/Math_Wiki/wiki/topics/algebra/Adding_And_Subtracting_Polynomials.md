---
title: "Adding and Subtracting Polynomials"
type: topic
aliases: ["Polynomial Addition", "Polynomial Subtraction", "Combining Polynomials"]
tags: ["#branch-algebra-1", "#topic-polynomials"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "6", section: "6.4"}
related:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Special_Products"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Greatest_Common_Factor"
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "Line up like terms, add their coefficients, and remember to flip every sign when you subtract."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Adding and Subtracting Polynomials

# Adding and Subtracting Polynomials

Adding and subtracting polynomials sounds intimidating, but it is really the same move you already use when you simplify something like $3x + 5x$. You hunt for matching pieces — terms that have identical variable parts — and you combine their coefficients. Everything else stays where it is. The only new wrinkle is keeping track of signs, especially when a subtraction sign sits in front of a whole set of parentheses.

$$
(3x^2 + 2x - 1) + (x^2 - 5x + 4) = 4x^2 - 3x + 3
$$

---

## What is a polynomial?

Before we start adding them, let's be precise about what a polynomial actually is.

A **monomial** is a single chunk built from numbers and variables joined only by multiplication, where every exponent is a whole number (so no square roots on variables, no variables in denominators). Good examples: $6$, $-4y$, $\tfrac{1}{2}a^3$, $7xy^2$. Bad examples: $\sqrt{x}$ (exponent is $\tfrac{1}{2}$, not a whole number) and $\dfrac{3}{z}$ (that is really $3z^{-1}$, and $-1$ is not a whole-number exponent).

A **polynomial** is either a single monomial or a sum of several monomials glued together with plus and minus signs. The pieces being summed are called the **terms** of the polynomial. So $4x^3 - 2x + 7$ is a polynomial with three terms: $4x^3$, $-2x$, and $7$. The number sitting in front of a variable part is the **coefficient** (the coefficient of $4x^3$ is $4$), and a term with no variable at all — like the $7$ — is called a **constant term**.

The **degree** of a monomial counts up the exponents on its variables. The term $5x^3$ has degree $3$; the term $-4x^2y$ has degree $2 + 1 = 3$; a lonely constant like $9$ has degree $0$. The **degree of a polynomial** is the largest degree that appears among its terms. So $4x^3 - 2x + 7$ is a degree-$3$ polynomial, which people also call a **cubic**.

Polynomials with a small number of terms get special names you will see again and again:

- one term — a **monomial** (like $5x^2$)
- two terms — a **binomial** (like $3x - 7$)
- three terms — a **trinomial** (like $x^2 + 4x + 4$)

Past three terms, people usually just say "polynomial." A polynomial sits in **standard form** once you've reordered its terms so the degrees walk downward — highest power first, lowest power last. For instance, $2x + x^3 - 5$ is tidier as $x^3 + 2x - 5$, and once it's in that order the leading coefficient and degree are easy to read off.

---

## Like terms are the only terms you can combine

Two terms are called **like terms** when they have exactly the same variable part — same letters raised to the same powers. The coefficients in front can differ; the variable parts must match. So $6x^2$ and $-11x^2$ are like terms, but $6x^2$ and $6x^3$ are not (the exponents disagree), and $6x^2$ and $6y^2$ are not (the letters disagree).

When you add or subtract polynomials, the only terms that collapse together are like terms. Unlike terms just sit there, unchanged, riding along into the final answer. Adding $3x^2 + 5x$ does not simplify any further because $3x^2$ and $5x$ have different degrees — nothing is alike about them.

To add like terms, keep the variable part and add the coefficients: $6x^2 + (-11x^2) = -5x^2$. That's it.

---

## Adding polynomials: drop the parentheses and combine

Adding two polynomials is a two-step recipe. First, erase the parentheses (when a plus sign sits in front, the parentheses are just decoration — they do not change any signs inside). Second, gather like terms and add their coefficients. Many students find it helps to physically underline or color-code matching terms before combining.

There are two layouts you can use. The **horizontal method** writes everything on one line; the **vertical method** stacks the polynomials on top of each other with like terms lined up in columns, the same way you line up place values to add ordinary numbers. Both give the same answer, so pick whichever feels cleaner for a given problem.

---

## Subtracting polynomials: distribute the minus sign first

Subtraction is where nearly every mistake happens. When a minus sign sits in front of a set of parentheses, that minus is really a hidden $-1$ that has to be handed to **every single term** inside. In other words, subtraction is just "add the opposite of the whole second polynomial":

$$
A - B = A + (-1)\cdot B
$$

So before you try to combine anything, rewrite the subtraction by flipping every sign inside the second set of parentheses. A plus becomes a minus; a minus becomes a plus. Only after that sign-flip do you start gathering like terms. Skipping this step — or flipping only the first term and forgetting the rest — is the single most common polynomial error in Algebra I.

---

## Example 1: Adding two trinomials

> Add $(2x^2 + 6x - 3) + (4x^2 - x + 8)$.

Both sets of parentheses have a plus in front, so we can drop them without any sign changes:

$$
2x^2 + 6x - 3 + 4x^2 - x + 8
$$

Now hunt for like terms. The $x^2$ terms are $2x^2$ and $4x^2$; the $x$ terms are $6x$ and $-x$; the constants are $-3$ and $8$. Combine each group separately:

$$
(2x^2 + 4x^2) + (6x - x) + (-3 + 8)
$$

$$
= 6x^2 + 5x + 5
$$

The answer is already in standard form, with degrees descending from left to right. Notice that the middle group $(6x - x)$ simplifies to $5x$, not $6x$ — the missing coefficient on $-x$ is really $-1$.

---

## Example 2: Subtracting where distributing the minus matters

> Simplify $(7y^2 - 4y + 2) - (3y^2 + 5y - 9)$.

This is a subtraction, so the first move is to hand the minus sign to every term inside the second polynomial. Each sign flips:

$$
7y^2 - 4y + 2 \;-\; 3y^2 \;-\; 5y \;+\; 9
$$

Pay attention to that last term. The original was $-9$, and subtracting $-9$ gives $+9$. That is the term most people drop. Now collect like terms:

$$
(7y^2 - 3y^2) + (-4y - 5y) + (2 + 9)
$$

$$
= 4y^2 - 9y + 11
$$

A good habit: write out the flipped-sign line on its own before you start combining. If you try to flip signs in your head and collect terms at the same time, one of the minus signs will get away from you.

---

## Example 3: Vertical stacking with a missing degree

> Add $(3a^3 + 2a - 5) + (a^3 + 4a^2 - a + 7)$ using the vertical method.

The first polynomial has no $a^2$ term at all. That's fine, but when we stack the two polynomials, we need to leave a blank column where the missing term would go — the same way you would line up $307 + 1{,}452$ by place value instead of jamming the digits together. Line up like terms in columns, highest degree on the left:

$$
\begin{array}{rrrrr}
  3a^3 &       & + 2a & - 5 \\
+ \; a^3 & + 4a^2 & - \; a & + 7 \\
\hline
  4a^3 & + 4a^2 & + \; a & + 2
\end{array}
$$

Column by column: $3a^3 + a^3 = 4a^3$. The second column only has $4a^2$ (nothing to combine it with), so it comes down unchanged. The $a$ column gives $2a + (-a) = a$. The constants give $-5 + 7 = 2$. The final answer is $4a^3 + 4a^2 + a + 2$.

One tidy consequence to notice: when you add or subtract polynomials, you always get another polynomial. You never produce a stray square root or a fraction with a variable in the bottom. Polynomials behave well together under these operations.

---

## Common pitfalls

- **Losing the minus sign on only some terms.** When you subtract a polynomial, every term of that second polynomial flips. Write the sign-flipped line as a separate step and double-check each term before combining.
- **Combining terms that only look similar.** $5x^2$ and $5x$ are not like terms — the exponents are different. The variable parts have to match exactly, letter for letter and exponent for exponent.
- **Forgetting the invisible coefficient of $1$.** In $y^3 - y + 4$, the middle term is $-1 \cdot y$, not zero. When you combine $5y + (-y)$, the result is $4y$, not $5y$.
- **Skipping the zero placeholder in vertical form.** If one polynomial is missing a degree the other has, leave that column empty (or write $+ 0x^2$) so the like terms stay aligned. Jamming the columns closed is how degrees get miscombined.

---

## Prerequisites

Before you tackle practice, make sure the following are comfortable:

- [[The_Distributive_Property]] — the idea behind handing a minus sign to every term
- [[Adding_And_Subtracting_Integers]] — so signed arithmetic on coefficients feels automatic
- [[Variables_And_Algebraic_Expressions]] — for the basic vocabulary of terms and coefficients

---

## Problems Involving Adding and Subtracting Polynomials

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="adding_and_subtracting_polynomials"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Multiplying_Polynomials]]
- [[Special_Products]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Greatest_Common_Factor]]
- [[The_Distributive_Property]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
