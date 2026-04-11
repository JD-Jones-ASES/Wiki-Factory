---
title: "Algebraic Functions"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-functions", "#key-topic", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Introduction_To_Functions"
  - "topics/precalculus/Graphs_Of_Functions"
  - "topics/precalculus/Introduction_To_Rational_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Operations_With_Radicals"
  - "topics/algebra/Simplifying_Rational_Expressions"
problem_type_ids: []
figures: []
summary: "Functions you can write using only the arithmetic operations and radicals — the natural playground before you meet exponentials, logs, and trig."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Algebraic Functions

# Algebraic Functions

When you spent time with [[Polynomial_Functions_And_Graphs|polynomials]], [[Simplifying_Rational_Expressions|rational expressions]], and [[Operations_With_Radicals|radicals]] in algebra, every function you wrote down shared a common ingredient list: you combined the variable $x$ with constants using plus, minus, times, divide, powers, and roots. Nothing else. No $2^x$, no $\log x$, no $\sin x$. Everything you built stayed inside a single family — the **algebraic functions** — and precalculus is where that family gets a formal name and a clear boundary.

Giving this family a name matters because the rest of precalculus is mostly about the *other* side of that boundary. Exponentials, logarithms, and the six trig functions are all **transcendental** — they cannot be written using only those arithmetic ingredients, no matter how cleverly you rearrange them. The split between algebraic and transcendental is the big structural divide of the whole course, and recognizing which side a function lives on tells you what tools will be available.

## What an algebraic function looks like

A function $f$ is **algebraic** when you can build the output $f(x)$ starting from the variable $x$ and real-number constants using a finite sequence of the following moves:

- addition and subtraction,
- multiplication and division,
- raising to a rational-number power (including integer powers and radicals).

Nothing is required to be polynomial or simple — a tower of nested fractions and square roots is still algebraic, as long as every step on the way is one of those three moves. A compact way to write the definition is:

$$
f(x) \text{ is algebraic} \iff f(x) \text{ can be built from } x \text{ using } +,\, -,\, \cdot,\, \div,\, \text{and rational-exponent powers.}
$$

Because rational-exponent powers include roots, any radical expression qualifies. The cube root function $x^{1/3}$, the square-root function $\sqrt{x-4}$, and the five-root function $\sqrt[5]{2x+7}$ are all algebraic.

## Why the definition is drawn where it is

The boundary between algebraic and transcendental is not arbitrary. Every algebraic function $y = f(x)$ has a hidden property: it secretly satisfies a polynomial equation in two variables. For example, $y = \sqrt{x}$ secretly satisfies $y^2 - x = 0$, and $y = \dfrac{1}{x+3}$ secretly satisfies $(x+3)y - 1 = 0$. You can hunt the polynomial equation down by clearing radicals and fractions. Transcendental functions like $y = 2^x$ have no such polynomial equation lurking behind them, no matter how hard you search.

That hidden-polynomial property is not something you will be tested on, but it is worth knowing because it explains why the division is natural rather than a bookkeeping convenience. Algebraic functions come with a guarantee: whatever identities they obey can eventually be reduced to polynomial identities. Transcendental functions obey identities of an entirely different kind (like $\sin^2\theta + \cos^2\theta = 1$), which you will meet later in [[Identities|trigonometric identities]] and in [[Properties_Of_Logarithms|logarithm properties]].

## The three big subfamilies

Most algebraic functions you meet in precalculus fall into three overlapping groups, each of which gets its own chapter later.

**Polynomials.** Expressions of the form $a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$. Their domain is all real numbers because plugging any real number into a polynomial never triggers a division by zero or a negative inside a square root. You studied these as [[Polynomial_Functions_And_Graphs|polynomial functions]] in algebra.

**Rational functions.** Any quotient $\dfrac{p(x)}{q(x)}$ of two polynomials. Their domain excludes the roots of the denominator $q(x)$, and they get their own chapter as [[Introduction_To_Rational_Functions|rational functions]].

**Radical (root) functions.** Anything containing $\sqrt{\phantom{x}}$, $\sqrt[3]{\phantom{x}}$, $\sqrt[4]{\phantom{x}}$, or in general $x^{p/q}$ with a rational exponent. When the root is **even** (square, fourth, sixth), the radicand has to be non-negative, which puts a real restriction on the domain. When the root is **odd**, there is no sign restriction and the domain stays all of $\mathbb{R}$.

Many functions live in more than one of these groups at once. The function $h(x) = \dfrac{\sqrt{x+2}}{x^2 - 1}$ is simultaneously rational (it has a polynomial in the denominator) and radical (it has a square root in the numerator) — and also just "algebraic," the umbrella term that covers them both.

## Finding the domain of an algebraic function

Because algebraic functions are built from those three operations only, there are exactly two things that can trip up a domain: **division by zero** and **even roots of negative numbers**. To find the domain of any algebraic function, you hunt for every place one of those things could happen and exclude it.

The recipe is:

1. Identify every denominator in the expression. Set each one equal to zero and solve. Exclude those $x$-values.
2. Identify every even-index radical ($\sqrt{\phantom{x}}$, $\sqrt[4]{\phantom{x}}$, $\sqrt[6]{\phantom{x}}$, and so on). Set the radicand $\ge 0$ and solve. Keep only $x$-values satisfying that.
3. Intersect. The domain is the set of real numbers that clears *all* these conditions simultaneously.

If there are no denominators and no even roots — just a polynomial — the domain is all real numbers and you are done after step 0.

## Worked examples

**Example 1.** Determine whether $f(x) = \dfrac{x^3 - 2}{x^2 + 1}$ is an algebraic function, and give its domain.

Every ingredient in $f(x)$ is polynomial (numerator $x^3 - 2$, denominator $x^2 + 1$), and the only operation between them is division. That is a rational function, which is a subfamily of algebraic functions, so yes — $f$ is algebraic.

For the domain, check the denominator: $x^2 + 1 = 0$ forces $x^2 = -1$, which has no real solutions. So the denominator is never zero for any real $x$. There are no even radicals at all. Both hazards are clear, so the domain is all real numbers:

$$
\text{domain}(f) = (-\infty,\, \infty).
$$

This is a nice illustration that "rational function" does not automatically mean "missing points" — you have to actually check the denominator. When it has no real roots, the domain is as big as a polynomial's.

**Example 2.** Determine whether $g(x) = 3^x$ is an algebraic function.

The output is $3$ raised to the variable power $x$. The definition of algebraic allows rational-exponent powers like $x^{2/3}$, but notice carefully which slot the variable sits in: in $x^{2/3}$, the variable is the *base* and the rational number is the *exponent*. In $3^x$, the variable is the *exponent* and the number is the *base*. That is a fundamentally different move, and it is exactly the move that escapes the algebraic family.

No finite sequence of additions, subtractions, multiplications, divisions, and rational-exponent powers on $x$ will ever produce $3^x$. So $g(x) = 3^x$ is **not** an algebraic function — it is transcendental. You will meet it again as an [[Exponential_Functions|exponential function]], and the whole point of its chapter is that it needs brand-new tools (logarithms, exponent rules unique to variable exponents) that the algebraic toolkit cannot supply.

A good mental shortcut: if the variable shows up in an exponent slot, the function is transcendental. If the variable only shows up as a base (possibly raised to rational powers), the function is algebraic.

**Example 3.** Construct an algebraic function whose domain is exactly $[4, \infty)$.

The phrase "domain is exactly $[4, \infty)$" is code for "the function is defined when $x \ge 4$ and undefined when $x < 4$." To force that cutoff, use an even radical with a radicand that is zero at $x = 4$ and negative below it — the simplest choice is a square root.

Try $h(x) = \sqrt{x - 4}$. To check the domain, set the radicand $\ge 0$:

$$
x - 4 \ge 0 \iff x \ge 4.
$$

The domain is exactly $[4, \infty)$, as required. The function is algebraic (square roots are included), and you can verify that plugging in $x = 4$ gives $h(4) = \sqrt{0} = 0$, while plugging in $x = 3$ gives $\sqrt{-1}$, which is not a real number — undefined, as expected.

You could have reached the same domain with many other algebraic expressions — $h(x) = (x-4)^{1/2}$ is the same function in different clothing, and $h(x) = \dfrac{1}{\sqrt{x-4} \cdot 0 + 1} + \sqrt{x - 4}$ is the same function with extra decoration. The minimal expression $\sqrt{x-4}$ is the cleanest.

## Common pitfalls

- **Confusing base-exponent with exponent-base.** $x^{2/3}$ is algebraic; $(2/3)^x$ is not. The position of the variable is what matters.
- **Forgetting that odd roots have all real inputs.** $\sqrt[3]{x - 5}$ is defined for every real $x$, including negative $x - 5$, because cube-rooting a negative number is perfectly fine. Only *even* roots need the radicand-positive check.
- **Missing a hidden denominator when rationalizing domains.** In $\dfrac{1}{\sqrt{x-4}}$, the square root requires $x - 4 \ge 0$, **and** the denominator being nonzero forces $x - 4 > 0$ (strict inequality). The stricter condition wins: the domain is $(4, \infty)$, not $[4, \infty)$.
- **Assuming "has a fraction" means "rational function."** A rational function is a quotient of two *polynomials*. A function like $\dfrac{\sqrt{x}}{x - 1}$ has a fraction but is not rational in the technical sense — it is still algebraic, just a radical function with a denominator.

## Problems Involving Algebraic Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="algebraic_functions"></div>

## See Also

- [[Introduction_To_Functions]] — the broader framing: what any function is, before you narrow to the algebraic ones
- [[Introduction_To_Rational_Functions]] — the most important algebraic subfamily built from quotients of polynomials
- [[Graphs_Of_Functions]] — what these functions look like once you plot them
- [[Exponential_Functions|Exponential Functions]] — the most famous example of what algebraic functions are *not*
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
