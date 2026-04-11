---
title: "Exponential Functions"
type: topic
aliases: ["Exponential Function", "Exponential Growth and Decay"]
tags: ["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-functions", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.2"}
related:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Inverse_Functions"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Exponential_Equations"
  - "topics/algebra/Growth_Decay_And_Applications"
  - "topics/algebra/Power_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Zero_And_Negative_Exponents"
problem_type_ids: []
figures: ["algebra/exponential_growth_decay.svg"]
summary: "The function f(x) = a b^x, where the variable lives in the exponent and the base sets the growth factor."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Exponential Functions

# Exponential Functions

An **exponential function** is one where the variable is not sitting at the base of a power but perched up in the exponent. That single structural change is what separates this family from everything you have met before. In a [[Power_Functions|power function]] like $f(x) = x^3$, the variable is the base and the exponent is fixed; here, the base is fixed and the variable is the exponent. The result is a curve that either climbs faster and faster or fades away more and more slowly, with nothing like the straight lines or neat parabolas you are used to.

The general form that algebra courses work with is

$$
f(x) = a \cdot b^x
$$

where the **base** $b$ is a positive number with $b \neq 1$, and $a$ is the **initial value** — the output when $x = 0$, because $b^0 = 1$ forces $f(0) = a$. The number $b$ is often called the **growth factor** (or decay factor). If you leave $a$ out, the simplest exponential is $f(x) = b^x$, which every book treats as the baseline shape of the family.

---

## Why the base matters

The base decides the whole character of the graph. Two things can happen:

- **Growth** ($b > 1$). Each step to the right multiplies the output by another copy of $b$, so the function rises, and rises faster and faster. The curve takes off in a direction that no polynomial can keep up with for long.
- **Decay** ($0 < b < 1$). Each step to the right multiplies the output by a fraction, so the function shrinks — slowly at first and then seemingly to nothing, but it never quite reaches zero. Values like $b = \tfrac{1}{2}$ or $b = 0.9$ are classic decay bases.

The forbidden values are $b \le 0$ (which breaks the function on many inputs) and $b = 1$ (which gives the flat line $y = 1$, not an exponential at all). With those out of the way, every legitimate exponential function has the same basic behavior, just flipped or stretched by its particular choice of base.

![[exponential_growth_decay.svg|Exponential growth and decay]]

---

## Properties shared by every exponential

No matter which legal base you pick, the graph of $f(x) = b^x$ shares a small set of features. Knowing them makes sketching and sanity-checking fast:

- **Domain.** Any real number can sit in the exponent — positive, negative, zero, whole, fractional, or irrational. The domain is all real numbers.
- **Range.** The output is always strictly positive. A positive base raised to any real power cannot give you zero or a negative number, so the range is $(0, \infty)$. If $a < 0$, the whole graph flips below the $x$-axis and the range becomes $(-\infty, 0)$.
- **A shared $y$-intercept.** Because $b^0 = 1$, every basic exponential $f(x) = b^x$ passes through the point $(0, 1)$, regardless of what the base is. Scaling by $a$ moves that intercept to $(0, a)$.
- **A horizontal asymptote at $y = 0$.** On one side of the graph the curve gets closer and closer to the $x$-axis without ever touching it. For a growth function, the asymptote is on the left; for a decay function, it is on the right. If the graph is shifted vertically by adding a constant $k$, the asymptote moves up or down with it to $y = k$.
- **Monotonic and one-to-one.** An exponential is always either strictly increasing (growth) or strictly decreasing (decay). It never turns around. That makes it one-to-one, and it is what allows the inverse to exist — that inverse is the [[Logarithmic_Functions|logarithmic function]].

---

## The natural base $e$

Among all the possible growth bases, one special number shows up so often in science, finance, and calculus that it gets its own letter: $e$. The **natural base** is an irrational number whose decimal expansion begins $e \approx 2.71828$, and the function $f(x) = e^x$ is called the **natural exponential function**.

What makes $e$ natural? It is the base that makes the exponential "self-calibrating" in a way that becomes precise in calculus, and it arises naturally from the compound-interest idea: if you push the compounding frequency higher and higher, ordinary compound interest approaches a continuous model that uses $e$. For now, treat $e$ as a constant your calculator already knows, somewhere between $2$ and $3$, that behaves like any other exponential base in the family.

---

## Example 1: evaluating an exponential function

> Let $f(x) = 4 \cdot 2^x$. Find $f(0)$, $f(3)$, and $f(-2)$, and say where each point sits relative to the $y$-intercept.

Substitute each input and simplify the power carefully. For $f(0)$:

$$
f(0) = 4 \cdot 2^0 = 4 \cdot 1 = 4.
$$

That confirms the initial-value rule: $f(0)$ is exactly $a = 4$. The point $(0, 4)$ is on the graph, and it is the $y$-intercept.

For $f(3)$:

$$
f(3) = 4 \cdot 2^3 = 4 \cdot 8 = 32.
$$

Three steps to the right has multiplied the starting value by $2$ three times. That is the promise of an exponential: each unit step scales the output by the same factor.

For $f(-2)$, a negative exponent asks for a reciprocal:

$$
f(-2) = 4 \cdot 2^{-2} = 4 \cdot \dfrac{1}{4} = 1.
$$

Two steps to the left has divided the initial value by $2$ twice. Decay behavior appears on the left side of a growth function, and growth behavior appears on the left side of a decay function. The direction depends on which side of the $y$-axis you are on.

---

## Example 2: reading growth vs. decay from the base

> For each function, state whether it represents growth or decay, identify the initial value, and give the $y$-intercept.
>
> (a) $f(x) = 5 \cdot 3^x$
> (b) $g(x) = 7 \cdot (0.8)^x$
> (c) $h(x) = 2 \cdot \left(\dfrac{1}{4}\right)^x$

For (a), the base is $3 > 1$, so $f$ is a growth function. The initial value is $a = 5$, so $f(0) = 5$, and the $y$-intercept is $(0, 5)$.

For (b), the base is $0.8$, which sits strictly between $0$ and $1$, so $g$ is a decay function. The initial value is $a = 7$, and the $y$-intercept is $(0, 7)$. Even though the curve is decaying, the starting value is still $7$ — decay describes what happens as $x$ increases, not where you begin.

For (c), the base is $\tfrac{1}{4}$, which is also between $0$ and $1$, so $h$ is decay. The initial value is $a = 2$, and the $y$-intercept is $(0, 2)$. A classic way to check: plug $x = 1$ and confirm that $h(1) = 2 \cdot \tfrac{1}{4} = \tfrac{1}{2}$, smaller than $h(0) = 2$. Smaller on the next step is exactly what decay looks like.

---

## Example 3: transformations of a basic exponential

> Describe how the graph of $g(x) = 2^{x+1} - 3$ is obtained from the graph of $f(x) = 2^x$, and state the new horizontal asymptote and range.

Read the transformations in the order they affect $x$ first, then the output. The $x + 1$ inside the exponent means "replace $x$ with $x + 1$," which shifts the graph **one unit to the left**. The $-3$ at the end lowers every output by $3$, which shifts the graph **down three units**.

The parent curve $f(x) = 2^x$ has a horizontal asymptote at $y = 0$. Moving the graph down by $3$ drags the asymptote along with it, so the new asymptote is $y = -3$.

The range of $f(x) = 2^x$ is $(0, \infty)$. After the vertical shift, every output is $3$ smaller, so the new range is $(-3, \infty)$. The domain does not change — every real number is still a valid input, as with every exponential.

As a spot check, the new $y$-intercept: $g(0) = 2^{0+1} - 3 = 2 - 3 = -1$. The point $(0, -1)$ is on the shifted graph, and $-1$ is indeed greater than $-3$, so the graph sits above its asymptote as expected.

---

## A note on compound interest

One place the exponential family shows up immediately is in money. If you put a **principal** of $P$ dollars into an account that pays annual interest rate $r$ (written as a decimal), and the interest is added back into the account $n$ times per year, the amount after $t$ years is

$$
A = P\left(1 + \dfrac{r}{n}\right)^{nt}.
$$

This is the **compound interest formula**, and the $(\ldots)^{nt}$ on the right is precisely an exponential function whose base is $1 + \tfrac{r}{n}$ and whose exponent is $nt$. As you let $n$ grow without bound — meaning the interest is compounded ever more frequently — this formula approaches the continuous version $A = P e^{rt}$ that uses the natural base. Both cases, and many more, are taken up in [[Growth_Decay_And_Applications]].

---

## Common pitfalls

- **Confusing the base with the exponent.** In $f(x) = 2^x$ the variable is the exponent, so the graph is exponential. In $g(x) = x^2$ the variable is the base, so the graph is a parabola. Different families, very different shapes.
- **Forgetting that the output is always positive.** No matter how negative $x$ gets, a positive base raised to that power is still positive. The graph of $f(x) = b^x$ never crosses or touches the $x$-axis.
- **Dropping the negative exponent.** A step to the left of zero gives a reciprocal, not a negative output: $2^{-3} = \tfrac{1}{8}$, not $-8$. A common mistake is to write the latter.
- **Ignoring the asymptote after a shift.** When you add a constant to an exponential, the horizontal asymptote moves with the graph. A function like $f(x) = 3 \cdot 2^x + 5$ has asymptote $y = 5$, not $y = 0$.

---

## Prerequisites

Before you tackle practice problems, make sure you are comfortable with:

- [[Function_Basics]] — how to read function notation and describe domain, range, and intercepts
- [[Properties_Of_Exponents]] — the rules for multiplying, dividing, and stacking powers
- [[Zero_And_Negative_Exponents]] — so a step to the left of the $y$-axis is not a mystery

---

## Problems Involving Exponential Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="exponential_functions"></div>

---

## See Also

- [[Exponential_Equations]]
- [[Logarithmic_Functions]]
- [[Growth_Decay_And_Applications]]
- [[Inverse_Functions]]
- [[Power_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
