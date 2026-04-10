---
title: "Introduction to Exponentials and Logarithms"
type: topic
aliases: ["Exponentials and Logarithms", "Exp and Log Introduction"]
tags: ["#branch-pre-calculus", "#topic-logarithms", "#topic-functions", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "6", section: "6.3"}
related:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Logarithms"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Growth_Decay_And_Applications"
  - "topics/precalculus/Properties_Of_Logarithms"
  - "topics/precalculus/Applications_Of_Exponentials_And_Logarithms"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Inverse_Functions"
  - "topics/algebra/Properties_Of_Exponents"
problem_type_ids: []
figures: []
summary: "A high-level tour of the exponential and logarithmic families, their inverse relationship, and the two bases that matter most: 10 and e."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Introduction to Exponentials and Logarithms

# Introduction to Exponentials and Logarithms

Exponential and logarithmic functions come packaged as a pair. One grows by repeated multiplication; the other answers the question "after how many multiplications?" They are the two sides of the same mathematical coin, and together they show up in every corner of science — from populations and money to radioactive particles and the loudness of a rock concert.

This page takes the bird's-eye view. The mechanics of solving equations, graphing transformations, and simplifying expressions live on the specialist pages [[Exponential_Functions]], [[Logarithms]], [[Logarithmic_Functions]], [[Exponential_Equations]], and [[Logarithmic_Equations]]. Here the goal is simply to understand what these functions are and how they fit together.

$$
f(x) = b^x \qquad\longleftrightarrow\qquad f^{-1}(x) = \log_b(x)
$$

---

## Key ideas

**An exponential function keeps the base fixed and lets the exponent vary.** If you pick a positive base $b$ (with $b \ne 1$) and write $f(x) = b^x$, the input $x$ lives in the exponent while the base stays put. This is very different from a power function like $x^3$, where the base is the variable and the exponent is fixed. Swapping those two roles changes the whole shape of the graph.

**The value of the base controls the shape.** When $b > 1$, the function grows — slowly at first, then explosively. When $0 < b < 1$, the function decays — dropping toward the $x$-axis without ever touching it. In both cases the output is always positive, the graph always passes through $(0, 1)$ (because $b^0 = 1$ for any base), and the $x$-axis acts as a horizontal asymptote.

**A logarithm is the exponent in disguise.** Given a base $b > 0$, $b \ne 1$, the **base-$b$ logarithm** $\log_b(x)$ is defined as the power you must raise $b$ to in order to land at $x$. In symbols,

$$
\log_b(x) = y \quad \text{means exactly} \quad b^y = x.
$$

Every true statement about exponents has an equivalent statement about logs. "$2^5 = 32$" and "$\log_2(32) = 5$" say exactly the same thing in two different languages.

**The log is the inverse of the exponential.** Because $b^x$ is a one-to-one function, it has an inverse, and that inverse is precisely $\log_b(x)$. The two functions undo each other, which gives the pair of cancellation laws you will use constantly in later work:

$$
\log_b(b^x) = x \qquad\text{and}\qquad b^{\log_b(x)} = x.
$$

The first equation holds for every real $x$; the second holds whenever $x > 0$, since you cannot take the log of a non-positive number.

**The graph of the log is the graph of the exponential reflected over $y = x$.** That is the visual meaning of "inverse" — swap every point $(a, b)$ for $(b, a)$. So while $b^x$ has domain "all real numbers" and range "positive numbers only," the logarithm $\log_b(x)$ has domain "positive numbers only" and range "all real numbers." The horizontal asymptote of the exponential becomes the vertical asymptote of the log.

---

## Two bases that get their own nicknames

Any positive base (other than $1$) is legal, but two choices dominate the subject:

**The common base, $b = 10$.** Because we count in tens, the base-$10$ logarithm was the workhorse of pre-calculator numerical work — it powered log tables, slide rules, and navigational almanacs for centuries. The notation $\log(x)$, with no subscript, is a silent agreement that the base is $10$.

**The natural base, $b = e$.** The letter $e$ stands for a specific irrational number whose decimal expansion starts $2.71828\ldots$ and never repeats. Its importance will not be obvious until you meet continuous growth and calculus, but it turns out to be the one base that makes the slope of an exponential equal to its own height at every point — a miracle that ripples through physics, finance, and probability. The base-$e$ logarithm gets its own notation too: $\ln(x)$, read "natural log of $x$."

So there are three equivalent sentences to keep straight:

- $\log_b(x)$ means "base-$b$ log of $x$," for any positive $b \ne 1$.
- $\log(x)$ means $\log_{10}(x)$ — base $10$ assumed.
- $\ln(x)$ means $\log_e(x)$ — base $e$ assumed.

---

## A first look at the graphs

Sketch $y = 2^x$ by plugging in a few points: $(-2, 1/4)$, $(-1, 1/2)$, $(0, 1)$, $(1, 2)$, $(2, 4)$, $(3, 8)$. The points rocket upward to the right and glide down toward the $x$-axis on the left. The graph never dips below the axis, because any positive number raised to any power is still positive.

Now sketch its inverse, $y = \log_2(x)$, by simply swapping coordinates: $(1/4, -2)$, $(1/2, -1)$, $(1, 0)$, $(2, 1)$, $(4, 2)$, $(8, 3)$. The points climb slowly to the right, drop toward negative infinity as $x$ approaches zero from the positive side, and live only in the right half of the plane. Fold the paper along the line $y = x$ and the two curves land on top of each other — a physical demonstration of the inverse relationship.

---

## Example 1: translating between exponential and log form

> Rewrite each statement in the other form.
> (a) $3^4 = 81$. (b) $\log_5(125) = 3$. (c) $e^0 = 1$.

The recipe is always the same. In the exponential equation $b^y = x$, the base stays the base, the exponent $y$ becomes the output of the log, and $x$ becomes the input: $\log_b(x) = y$.

(a) $3^4 = 81$ becomes $\log_3(81) = 4$. The base is $3$, the exponent is $4$, the result is $81$.

(b) $\log_5(125) = 3$ becomes $5^3 = 125$. Read it as "the power of $5$ that gives $125$ is $3$," and then read that as "five to the three equals one twenty-five."

(c) $e^0 = 1$ becomes $\ln(1) = 0$. Every log of $1$ is zero, because every nonzero base raised to the zero power equals $1$.

---

## Example 2: evaluating simple logs without a calculator

> Find the exact value of $\log_2(32)$, $\log_{1/3}(9)$, and $\ln(e^5)$.

For the first one, ask: what power of $2$ gives $32$? Since $2^5 = 32$, the answer is $\log_2(32) = 5$.

For the second, the base is a fraction. Ask: what power of $1/3$ gives $9$? Remember that $(1/3)^{-1} = 3$, and squaring gives $(1/3)^{-2} = 9$. So $\log_{1/3}(9) = -2$. Negative answers are common when the base is less than $1$.

For the third, use the cancellation law directly. Since $\ln$ means $\log_e$, and $\log_e(e^x) = x$ for every real $x$, we get $\ln(e^5) = 5$ instantly — no calculator required.

---

## Example 3: a domain check

> Find the domain of $h(x) = \log(x - 3) + \ln(7 - x)$.

The input to any logarithm must be positive. Both logs on the right must be happy at the same time, so write both conditions and intersect them.

The first log needs $x - 3 > 0$, which means $x > 3$. The second log needs $7 - x > 0$, which means $x < 7$. Putting both conditions together, $3 < x < 7$, or in interval notation, $(3, 7)$. Outside that window at least one of the two logs is undefined, so $h$ has nothing to say.

Domain checks are the main way log notation stays connected to the idea that "logs of non-positive numbers do not exist." Every time you use one, remind yourself that the input has to be strictly greater than zero.

---

## Common pitfalls

- **$\log(x)$ is not the same as $\log(x)^2$ or $\log(x^2)$ — pay attention to where the square lives.** $\log(x^2)$ means "log of $x$ squared"; $(\log(x))^2$ means "square the log." They almost always give different numbers.
- **There is no log of a negative number, and no log of zero.** If your work produces $\log(-4)$ or $\log(0)$, retrace your steps — you probably introduced an extraneous solution somewhere.
- **$\ln$ and $\log$ are not interchangeable.** A calculator button labelled $\log$ is base $10$; the one labelled $\ln$ is base $e$. Using the wrong one silently changes the answer.
- **Exponential functions are not power functions.** $2^x$ and $x^2$ look similar in notation but behave completely differently: one blasts upward forever, the other is a parabola symmetric about the $y$-axis.

---

## Prerequisites

Before diving into practice problems, you should be comfortable with:

- [[Function_Basics]] — domain, range, inputs and outputs
- [[Inverse_Functions]] — the idea of undoing a function by reflecting it across $y = x$
- [[Properties_Of_Exponents]] — the algebra of exponents, including negatives and fractions

For deeper mechanics, visit the dedicated algebra pages: [[Exponential_Functions]], [[Logarithms]], and [[Logarithmic_Functions]].

---

## Problems Involving Introduction to Exponentials and Logarithms

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="introduction_to_exponentials_and_logarithms"></div>

---

## See Also

- [[Exponential_Functions]]
- [[Logarithms]]
- [[Logarithmic_Functions]]
- [[Properties_Of_Logarithms]]
- [[Applications_Of_Exponentials_And_Logarithms]]
- [[Growth_Decay_And_Applications]]
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
