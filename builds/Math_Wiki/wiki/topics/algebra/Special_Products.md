---
title: "Special Products"
type: topic
aliases: ["Perfect Square Trinomial", "Difference of Squares Product", "Binomial Square"]
tags: ["#branch-algebra-1", "#topic-polynomials", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "6", section: "6.6"}
related:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Properties_Of_Exponents"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/algebra/Properties_Of_Exponents"
problem_type_ids: []
figures: []
summary: "Three binomial-multiplication patterns worth memorizing: the difference of squares and the two perfect square trinomials."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Special Products

# Special Products

Most binomial multiplications need the full FOIL routine. A small handful do not. If the two binomials share a special shape, the four FOIL products collapse into a shorter result that you can write in one step — no scratch work required. Learning to recognize these shapes saves time every day once you hit [[Factoring_Trinomials_General|factoring]], the [[The_Quadratic_Formula|quadratic formula]], and beyond.

There are three patterns to memorize:

$$
\begin{aligned}
(a + b)(a - b) &= a^2 - b^2 \\[4pt]
(a + b)^2 &= a^2 + 2ab + b^2 \\[4pt]
(a - b)^2 &= a^2 - 2ab + b^2
\end{aligned}
$$

The first is called the **difference of squares**. The second and third are the two **perfect square trinomials** — sometimes called a **binomial square**. Each pattern has a specific reason the middle work simplifies, and once you see why, the formulas stop looking arbitrary.

---

## Key ideas

### Where the difference of squares comes from

Suppose you multiply $(a + b)(a - b)$. Running FOIL by hand gives four products:

$$
(a + b)(a - b) = a \cdot a + a \cdot (-b) + b \cdot a + b \cdot (-b)
$$

$$
= a^2 - ab + ba - b^2
$$

Look at the two middle terms. $-ab$ and $+ba$ are opposites — multiplication is commutative, so $ba$ is the same quantity as $ab$, and the signs disagree. They add to zero and vanish. What remains is just the first square minus the last square:

$$
(a + b)(a - b) = a^2 - b^2
$$

That cancellation only happens because the two binomials are identical except for one sign. If you tried $(a + b)(a + c)$ the middle terms would be $ac + bc$, which do **not** cancel. The sum-and-difference shape is the whole reason the pattern works.

### Where the perfect square trinomials come from

Now try $(a + b)^2$. That means $(a + b)(a + b)$ — two copies of the same binomial. FOIL gives:

$$
(a + b)(a + b) = a^2 + ab + ba + b^2
$$

This time the middle terms have **the same sign**, so instead of cancelling they **add**:

$$
= a^2 + 2ab + b^2
$$

The middle term is twice the product of the two pieces of the original binomial. Running the same argument on $(a - b)^2 = (a - b)(a - b)$ gives $-ab - ba = -2ab$, so:

$$
(a - b)^2 = a^2 - 2ab + b^2
$$

The pattern is the same trinomial either way, except the sign of the middle term matches the sign inside the original binomial. The first and last terms are always positive — they are squares.

### What "$a$" and "$b$" really mean

In these formulas, $a$ and $b$ stand in for whatever two pieces make up your binomial. They don't have to be simple letters. In $(3x + 4)^2$, the role of $a$ is played by $3x$ and the role of $b$ is played by $4$. You square each one, multiply them together and double that, and drop the answer straight into the template. Matching the pieces to the roles is the only work; the rest is pure substitution.

---

## Example 1: a difference of squares

> Expand $(3x - 5)(3x + 5)$.

The two binomials match the difference-of-squares shape: same first term $3x$, same second term $5$, and the signs between them are opposite. Identify the pieces: $a = 3x$ and $b = 5$. Then drop straight into the pattern $a^2 - b^2$:

$$
(3x - 5)(3x + 5) = (3x)^2 - 5^2
$$

Square each piece — remember to square both the coefficient and the variable:

$$
= 9x^2 - 25
$$

And that's the answer. No middle term, because it cancelled. Notice how fast that was compared to running FOIL on four products.

---

## Example 2: squaring a binomial sum

> Expand $(2x + 7)^2$.

This is a perfect square, so the result will have three terms. Match the pieces: $a = 2x$ and $b = 7$. Then fill in $a^2 + 2ab + b^2$:

$$
(2x + 7)^2 = (2x)^2 + 2(2x)(7) + 7^2
$$

Work each piece. The square of $2x$ is $4x^2$. The middle is $2 \cdot 2x \cdot 7 = 28x$. The square of $7$ is $49$:

$$
= 4x^2 + 28x + 49
$$

The tempting wrong answer here is $4x^2 + 49$, which drops the middle term entirely. You can catch the mistake by testing a number: at $x = 1$, the real expression $(2 + 7)^2 = 81$, while the wrong trinomial would give $4 + 49 = 53$. The missing $28$ is exactly the middle term $28(1)$.

---

## Example 3: squaring a binomial difference

> Expand $(4y - 1)^2$.

Same template, but the middle term picks up a minus sign because the original binomial has a minus. With $a = 4y$ and $b = 1$:

$$
(4y - 1)^2 = (4y)^2 - 2(4y)(1) + 1^2
$$

Square, double, square again:

$$
= 16y^2 - 8y + 1
$$

The first and last terms are always positive even when the binomial is a difference — you are squaring them, and a square cannot be negative. Only the middle term tracks the sign inside the original binomial.

---

## Common pitfalls

- **Forgetting the middle term on a perfect square.** $(a + b)^2 \ne a^2 + b^2$. The middle term $2ab$ is the biggest payoff of knowing the formula and the easiest thing to drop. If your expansion of a squared binomial has only two terms, something is missing.
- **Squaring the coefficient but not the variable.** When $a = 3x$, the square is $(3x)^2 = 9x^2$, not $3x^2$. The exponent applies to the whole factor inside the parentheses.
- **Sign slips on the middle term.** For $(a - b)^2$ the middle is $-2ab$. For $(a + b)^2$ it is $+2ab$. For a difference of squares $(a + b)(a - b)$ there is no middle at all. Match the sign of the middle to the sign inside the binomial, and use no middle when the binomials are a sum-and-difference pair.
- **Forcing the pattern where it does not fit.** The difference of squares only works when you have sum-and-difference of the same two terms. $(x + 4)(x - 5)$ is not a special product — the second pieces don't match, so fall back on FOIL.

---

## Prerequisites

Before you practice special products, be comfortable with:

- [[Multiplying_Polynomials]] — so you can verify any special-product shortcut by FOIL and spot when the pattern does not apply
- [[The_Distributive_Property]] — FOIL is really two applications of the distributive property, and that is where the middle terms come from
- [[Properties_Of_Exponents]] — so $(3x)^2 = 9x^2$ is automatic and you don't drop the coefficient inside a square

---

## Problems Involving Special Products

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="special_products"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Multiplying_Polynomials]] — the general method these patterns shortcut
- [[Factoring_Special_Forms]] — same three patterns run in reverse, from a trinomial or difference back to factors
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Factoring_Trinomials_General]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
