---
title: "Properties of Exponents"
type: topic
aliases: ["Exponent Rules", "Laws of Exponents"]
tags: ["#branch-algebra-1", "#topic-exponents-and-radicals", "#key-formula", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Zero_And_Negative_Exponents"
  - "topics/algebra/Multiplying_Polynomials"
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/algebra/Scientific_Notation"
  - "topics/algebra/Exponential_Functions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Exponents_And_Powers"
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "A short list of rules that let you simplify any expression built from multiplying, dividing, and stacking powers."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Properties of Exponents

# Properties of Exponents

Exponents are, at their heart, a compact way of writing repeated multiplication. The expression $b^5$ is shorthand for $b \cdot b \cdot b \cdot b \cdot b$ — five copies of $b$ multiplied together. That is the entire definition, and once you believe it, every rule on this page follows from basic counting. You will not be memorizing mysterious laws; you will be noticing patterns that come straight out of "how many copies of $b$ are we actually multiplying?"

The payoff is that once the rules feel natural, you can simplify long, intimidating expressions almost on sight. You will meet these rules again in [[Multiplying_Polynomials]], in [[Simplifying_Radical_Expressions]], in [[Scientific_Notation]], and in [[Exponential_Functions]]. They are the grammar of anything exponential. This page covers the five main rules for positive-integer exponents; [[Zero_And_Negative_Exponents]] handles the companion rules for $b^0$ and $b^{-n}$.

## What it means / The idea

Let $b$ be a nonzero real number and $m$, $n$ positive integers. The five core properties are:

**Product of powers** — multiplying two powers with the same base:
$$
b^m \cdot b^n = b^{m+n}.
$$

**Power of a power** — raising a power to another power:
$$
(b^m)^n = b^{mn}.
$$

**Quotient of powers** — dividing two powers with the same base:
$$
\frac{b^m}{b^n} = b^{m-n}, \qquad b \ne 0.
$$

**Power of a product** — raising a product to a power:
$$
(ab)^n = a^n b^n.
$$

**Power of a quotient** — raising a quotient to a power:
$$
\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}, \qquad b \ne 0.
$$

Those five identities cover almost every simplification you will do with exponents in Algebra 1. Notice that three of them involve **the same base** (product, power-of-a-power, and quotient), while the other two distribute a power across a product or a quotient.

## How it works / The procedure

There is no single multi-step algorithm for exponent problems; instead, you pattern-match. Scan the expression, ask yourself which rule applies to which piece, and apply them one at a time.

1. **Look at each group of powers.** Which bases match? Matching bases means product/quotient rules can collapse them. Mismatched bases stay separate.
2. **Work from the inside out.** Apply the power-of-a-power rule on any nested parentheses before doing anything else.
3. **Apply product or quotient rules.** For same-base products, add the exponents. For same-base quotients, subtract (top minus bottom).
4. **Distribute powers across products and quotients.** Whenever a parenthesized product or quotient is raised to a power, send the exponent to every factor inside.
5. **Check each step for common-base mistakes.** You cannot add exponents on $b^3 \cdot c^4$ — the bases differ, and the expression stays as $b^3 c^4$.
6. **Simplify any plain number parts at the end.** If the coefficients can be multiplied or divided, finish the arithmetic.

Two habits make this much easier: write down the rule name you are using as you work ("product rule," "power of a power"), and never combine exponents for **different** bases. That second habit prevents about half of the errors on this topic.

## Why it works

Every rule is really a counting argument, and the product rule is the clearest illustration. Write $b^3 \cdot b^4$ as $(b \cdot b \cdot b) \cdot (b \cdot b \cdot b \cdot b)$. Counting the copies of $b$ on the right gives seven, so $b^3 \cdot b^4 = b^7 = b^{3+4}$. Exponents add under multiplication because the copies simply stack.

The power-of-a-power rule comes from the same idea, one level up. $(b^3)^4$ means four copies of $b^3$ multiplied: $b^3 \cdot b^3 \cdot b^3 \cdot b^3$. Using the product rule repeatedly gives $b^{3+3+3+3} = b^{12} = b^{3 \cdot 4}$. Raising a power to a power multiplies the exponents.

Quotients work by canceling: $b^5 / b^2$ means $(b \cdot b \cdot b \cdot b \cdot b)/(b \cdot b)$, and two of the $b$s on top cancel with the two on the bottom, leaving $b^3 = b^{5-2}$. Every other rule on the page is this same idea dressed up differently — they are all just bookkeeping for "how many copies of the base are still around after the operation?"

## Worked examples

### Example 1

Simplify $3^4 \cdot 3^2$.

Both powers have the same base, $3$, so the **product of powers** rule applies. Add the exponents:

$$
3^4 \cdot 3^2 = 3^{4+2} = 3^6.
$$

If the problem wants a numerical answer, $3^6 = 729$. If it wants the form with the exponent, $3^6$ is fine. Either way, the point is that the exponents added because the bases matched and the operation was multiplication.

### Example 2

Simplify $(2^3)^5$.

Here you have a power raised to another power, which is the **power of a power** rule. Multiply the exponents:

$$
(2^3)^5 = 2^{3 \cdot 5} = 2^{15}.
$$

A common early mistake is to add instead of multiply here, writing $(2^3)^5 = 2^{3 + 5} = 2^8$. That is wrong. Adding is for the product rule, where the powers sit side by side. Multiplying is for the power-of-a-power rule, where one power is raised to another. The distinction between "side by side" and "stacked" is the whole difference.

### Example 3

Simplify $\dfrac{7^8}{7^3}$.

Both powers have the same base, $7$, so the **quotient of powers** rule applies. Subtract the bottom exponent from the top:

$$
\frac{7^8}{7^3} = 7^{8 - 3} = 7^5.
$$

The order of subtraction matters — it is always top minus bottom, never the other way around. If you accidentally do $7^{3 - 8} = 7^{-5}$, you have not ruined your life (the answer is the reciprocal, $1/7^5$, which is a perfectly real number), but it is not the same expression. For this topic, keep top minus bottom and you will not have to worry about negative exponents yet. Those get their own treatment in [[Zero_And_Negative_Exponents]].

## Common pitfalls

- **Multiplying the exponents when you should add them.** $b^m \cdot b^n = b^{m+n}$, **not** $b^{mn}$. Multiplying is what you do for $(b^m)^n$, which is a different shape. If two powers sit next to each other with a multiplication between them, add. If one power is raised to another, multiply.
- **Adding exponents on unlike bases.** $x^3 \cdot y^5$ does not become $xy^8$ or anything like it. The bases do not match, so the product rule does not apply. You write $x^3 y^5$ and leave it alone.
- **Distributing a power across addition.** $(a + b)^2$ is **not** $a^2 + b^2$. The power-of-a-product rule only works across multiplication, not addition. See [[Multiplying_Polynomials]] for what $(a + b)^2$ really equals. Do not let the shape of the power-of-a-product rule trick you into distributing where it does not belong.
- **Forgetting that the coefficient has its own exponent.** In $(3x^2)^4$, the $3$ gets raised to the fourth power too: $(3x^2)^4 = 3^4 \cdot x^{2 \cdot 4} = 81 x^8$. A common error is to write $3 x^8$, forgetting that the coefficient was inside the parentheses.
- **Subtracting in the wrong order.** In the quotient rule, it is the **top** exponent minus the bottom, not the other way around. $b^8 / b^3 = b^5$, not $b^{-5}$. Stick with top-minus-bottom.

## Problems Involving Properties of Exponents

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="properties_of_exponents"></div>

## See Also

- [[Zero_And_Negative_Exponents]] — the companion rules for $b^0$ and $b^{-n}$
- [[Multiplying_Polynomials]] — the first place these rules really earn their keep
- [[Simplifying_Radical_Expressions]] — exponents and radicals are two sides of the same coin
- [[Scientific_Notation]] — powers of $10$ in particular
- [[Exponential_Functions]] — the function-flavored view of repeated multiplication
- [[Exponents_And_Powers|Exponents and Powers]] — the pre-algebra introduction
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
