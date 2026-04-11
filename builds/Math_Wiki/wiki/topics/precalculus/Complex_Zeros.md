---
title: "Complex Zeros of Polynomials"
type: topic
aliases: ["Complex Roots", "Complex Zeros", "Fundamental Theorem of Algebra", "Conjugate Root Theorem"]
tags: ["#branch-pre-calculus", "#topic-complex-numbers"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "3", section: "3.1"}
related:
  - "topics/algebra/The_Complex_Number_System"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/precalculus/Polar_Form_Of_Complex_Numbers"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/The_Complex_Number_System"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Polynomial_Long_Division"
problem_type_ids: []
figures: []
summary: "Every polynomial of degree n has exactly n roots once you allow complex numbers, and those roots pair up as conjugates when the coefficients are real."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Complex Zeros of Polynomials

# Complex Zeros of Polynomials

When you first learned to factor polynomials over the real numbers, a quiet frustration showed up: certain quadratics had no real roots, and higher-degree polynomials sometimes refused to factor all the way down. The expression $x^2 + 1$ has no real zero because no real number squares to $-1$. Once you allow the [[The_Complex_Number_System|complex number]] $i$, however, that obstruction disappears, and a much cleaner theory replaces the patchwork of special cases.

The single statement that rebuilds the whole picture is called the **Fundamental Theorem of Algebra**. Loosely put, every nonconstant polynomial with complex-number coefficients has at least one complex zero. You can read that as a promise: no matter how ugly the polynomial, it will factor at least once over the complex numbers. That single promise is powerful because you can apply it repeatedly.

## How many zeros does a polynomial have?

Once you can extract one complex zero, divide the linear factor out and apply the theorem again to the quotient. Each pass drops the degree by one. If the original polynomial had degree $n$, the process terminates after exactly $n$ passes, producing $n$ linear factors over the complex numbers. In other words, a polynomial of degree $n$ factors as

$$
p(x) = a(x - r_1)(x - r_2)\cdots(x - r_n),
$$

where each $r_k$ is a complex number and $a$ is the leading coefficient. Some of those roots may repeat — a double root like $(x - 3)^2$ counts twice — so the honest statement is that a degree-$n$ polynomial has exactly $n$ complex zeros, **counting multiplicity**. You never "lose" roots again; you only fail to see them without complex numbers.

---

## The conjugate pairs rule

There is a beautiful symmetry that applies whenever your polynomial has **real** coefficients (not just rational or integer — real). If $a + bi$ is a zero, then $a - bi$, its complex conjugate, is also a zero. Nonreal roots show up in matched pairs.

The reason is not mysterious. Taking a complex conjugate plays nicely with addition and multiplication: the conjugate of a sum is the sum of the conjugates, and the conjugate of a product is the product of the conjugates. So if you conjugate the entire equation $p(a + bi) = 0$, real coefficients stay put, and every instance of $a + bi$ flips to $a - bi$. The result is $p(a - bi) = \overline{0} = 0$, which says that $a - bi$ is also a zero. Same equation, conjugated.

This rule has one immediate consequence: a polynomial with real coefficients and **odd** degree must have at least one real zero. The nonreal zeros must pair up, so an odd-degree polynomial cannot have all of its zeros come in pairs — at least one root has to be its own conjugate, meaning it has zero imaginary part, meaning it is real.

---

## Finding complex zeros of a quadratic

For a quadratic $ax^2 + bx + c$ with real coefficients, complex roots appear precisely when the **discriminant** $b^2 - 4ac$ is negative. The [[The_Quadratic_Formula|quadratic formula]] still works; you just take a square root of a negative and write it in $i$ form.

---

## Example 1: a quadratic with complex roots

> Find all zeros of $x^2 - 4x + 13$.

Apply the quadratic formula with $a = 1$, $b = -4$, $c = 13$:

$$
x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(13)}}{2(1)} = \frac{4 \pm \sqrt{16 - 52}}{2} = \frac{4 \pm \sqrt{-36}}{2}.
$$

The discriminant is $-36$, so square-rooting gives $\sqrt{-36} = 6i$:

$$
x = \frac{4 \pm 6i}{2} = 2 \pm 3i.
$$

Both zeros: $x = 2 + 3i$ and $x = 2 - 3i$. They are complex conjugates of each other, exactly as the pair rule demanded — the coefficients of the polynomial are real, so the nonreal zeros had to come as a matched pair.

---

## Example 2: a cubic with one real and two complex zeros

> Find all zeros of $f(x) = x^3 - 5x^2 + 17x - 13$.

A cubic has three zeros counted with multiplicity. By the conjugate pairs rule, the number of nonreal zeros must be even — zero or two — which means a real-coefficient cubic always has **at least one** real zero.

Hunt for a rational zero first using the rational root theorem. The constant term is $-13$ and the leading coefficient is $1$, so any rational zero must be $\pm 1$ or $\pm 13$. Testing $x = 1$:

$$
f(1) = 1 - 5 + 17 - 13 = 0.
$$

That works, so $x = 1$ is a root and $(x - 1)$ is a factor. Divide by $(x - 1)$ using synthetic or long division. The quotient comes out to $x^2 - 4x + 13$, and you already know the zeros of that quadratic from Example 1: $x = 2 \pm 3i$.

The complete factorization over the complex numbers is

$$
f(x) = (x - 1)(x - (2 + 3i))(x - (2 - 3i)).
$$

Three zeros, one real and two nonreal conjugates. The cubic could never have produced three nonreal zeros alone, because that would mean three conjugates — and three is odd, which is impossible when complex zeros must pair up.

---

## Example 3: building a polynomial from zeros

> Find a polynomial with real coefficients and lowest possible degree whose zeros include $x = 2$ and $x = 1 - 4i$.

Because the coefficients must be real, the zero $1 - 4i$ forces its conjugate $1 + 4i$ to be a zero as well, even though it was not listed. So the polynomial must have at least three zeros: $2$, $1 - 4i$, and $1 + 4i$. The minimum degree is $3$.

Build the polynomial as a product of linear factors:

$$
p(x) = (x - 2)\bigl(x - (1 - 4i)\bigr)\bigl(x - (1 + 4i)\bigr).
$$

Multiply the conjugate pair first — this is where the imaginary parts cancel out and you get a real quadratic:

$$
\bigl(x - (1 - 4i)\bigr)\bigl(x - (1 + 4i)\bigr) = (x - 1)^2 - (4i)^2 = (x^2 - 2x + 1) - (-16) = x^2 - 2x + 17.
$$

Now multiply by $(x - 2)$:

$$
p(x) = (x - 2)(x^2 - 2x + 17) = x^3 - 4x^2 + 21x - 34.
$$

All coefficients are real, as required, and the polynomial has exactly the three zeros we demanded.

---

## Common pitfalls

- **Forgetting that the conjugate pairs rule requires real coefficients.** If the polynomial has complex coefficients in it already, conjugates do not have to pair up. The rule is a special property of real-coefficient polynomials.
- **Counting each repeated root only once.** A factor of $(x - 3)^2$ contributes $x = 3$ as a double root, and the total root count must include it twice for the "$n$ zeros" claim to hold up.
- **Trying to guess nonreal roots by the rational root theorem.** The rational root theorem only ever produces rational real roots. It is still the right first step, but once those are exhausted, the remaining roots must be found by factoring the reduced polynomial and using the quadratic formula.
- **Dropping the plus-or-minus on $\sqrt{-D}$.** When the discriminant is negative, the quadratic formula still has $\pm$. Both signs give genuine roots — the conjugate pair.

---

## Prerequisites

- [[The_Complex_Number_System]] — you must be comfortable adding, multiplying, and simplifying $a + bi$ expressions, and in particular with the fact that $(a + bi)(a - bi) = a^2 + b^2$.
- [[The_Quadratic_Formula]] — the direct route to complex roots of a quadratic when the discriminant is negative.
- [[Factoring_Completely]] — for reducing a higher-degree polynomial once a single root has been peeled off.

---

## Problems Involving Complex Zeros

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="complex_zeros"></div>

---

## See Also

- [[The_Complex_Number_System]] — the arithmetic machinery that complex roots rely on
- [[Polar_Form_Of_Complex_Numbers]] — a different picture of $a + bi$ that makes powers and roots much easier
- [[The_Quadratic_Formula]]
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
