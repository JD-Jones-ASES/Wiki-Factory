---
title: "Logarithmic Functions"
type: topic
aliases: ["Logarithmic Function", "Log Function"]
tags: ["#branch-algebra-2", "#topic-logarithms", "#topic-functions", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.6"}
related:
  - "topics/algebra/Logarithms"
  - "topics/algebra/Logarithmic_Equations"
  - "topics/algebra/Properties_Of_Logarithms"
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Inverse_Functions"
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Logarithms"
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Inverse_Functions"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: ["algebra/log_exp_inverses.svg"]
summary: "The function f(x) = log_b(x) is the mirror image of the exponential b^x across y = x — its full shape, domain, and behavior fall out of that single fact."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Logarithmic Functions

# Logarithmic Functions

A **logarithmic function** is the function-level partner of the logarithm you just met on the [[Logarithms]] page. Instead of computing one logarithm at a time, we treat the whole rule as a machine: feed it a positive input, and the machine hands back the exponent that turns the base into that input.

$$
f(x) = \log_{b}(x), \qquad b > 0, \quad b \neq 1.
$$

The entire personality of this function comes from one idea: it is the **inverse** of the exponential function $g(x) = b^x$. Everything that follows — the shape of the graph, the domain, the range, the asymptote — is a consequence of that inverse relationship. Once you see it, the function stops feeling strange and starts feeling inevitable.

## Why logs are the inverse of exponentials

Raising $b$ to a power is a machine: put in the exponent, read off the result. Undoing that machine means putting in the result and reading off the exponent. That is exactly what a logarithm does. In symbols, we wrote the "if and only if" rule as

$$
\log_{b}(x) = y \quad \text{if and only if} \quad b^y = x.
$$

That is the inverse relationship written out. The domain of the exponential becomes the range of the logarithm, and the range of the exponential becomes the domain of the logarithm. From [[Inverse_Functions]] we know this forces two consequences:

- The graphs of $y = b^x$ and $y = \log_{b}(x)$ are mirror images of each other across the line $y = x$.
- Every feature of the logarithm graph is a flipped version of a feature of the exponential graph.

The exponential function $b^x$ has domain "all real numbers" and range "positive reals only". Swap those, and the logarithm function has domain "positive reals only" and range "all real numbers". The exponential function has a horizontal asymptote at $y = 0$; swap the axes, and the logarithm has a vertical asymptote at $x = 0$. Nothing on this page needs to be memorized separately from the exponential — it is just the exponential's reflection.

![[log_exp_inverses.svg|The logarithm as the mirror of the exponential]]

---

## Key ideas

- **Domain: $(0, \infty)$.** Only strictly positive numbers can be fed in. The argument of every logarithm must clear zero. If a problem gives you $f(x) = \log_{b}(g(x))$, always solve $g(x) > 0$ first to pin down the inputs the function will actually accept.
- **Range: $(-\infty, \infty)$.** Every real number appears as an output somewhere, because every real exponent is legal on the exponential side.
- **Anchor points.** The graph always passes through $(1, 0)$ because $\log_{b}(1) = 0$ for every base. It always passes through $(b, 1)$ because $\log_{b}(b) = 1$. Those two points plus the asymptote are enough to sketch the function.
- **Vertical asymptote at $x = 0$.** As the input slides toward zero from the right, the outputs plunge toward $-\infty$ (when $b > 1$) or rocket toward $+\infty$ (when $0 < b < 1$). The $y$-axis is a wall the curve never touches.
- **Monotonicity.** When $b > 1$, the function strictly climbs from $-\infty$ to $\infty$ as $x$ slides from $0$ to $\infty$. When $0 < b < 1$, it strictly drops instead. Either way, the curve is one-to-one, so it has its own inverse — which is, of course, the exponential $b^x$.
- **Transformations.** Shifts and reflections work the usual way. Writing $f(x) = \log_{b}(x - h) + k$ shifts the parent graph right by $h$ and up by $k$. The asymptote shifts to $x = h$, and the new domain is $x > h$. A leading negative sign, $-\log_{b}(x)$, flips the curve upside down across the $x$-axis.

---

## Example 1: Building the graph of a log function from its exponential twin

> Sketch $f(x) = \log_{3}(x)$ by listing five clean points.

The fastest way to plot a logarithm by hand is to stop thinking about the logarithm and think about its exponential twin instead. Since $f(x) = \log_{3}(x)$ is the inverse of $g(x) = 3^x$, we can build a table of $(x, y)$ pairs for the exponential and then swap the two columns.

For the exponential $g(x) = 3^x$ at clean inputs:

- $g(-2) = \tfrac{1}{9}$
- $g(-1) = \tfrac{1}{3}$
- $g(0) = 1$
- $g(1) = 3$
- $g(2) = 9$

Swap each pair to get points on $f$:

$$
\left(\tfrac{1}{9}, -2\right), \quad \left(\tfrac{1}{3}, -1\right), \quad (1, 0), \quad (3, 1), \quad (9, 2).
$$

Plot those five points and connect them with a smoothly climbing curve. Near $x = 0$, the curve dives toward $-\infty$ and stays clear of the $y$-axis. For large $x$, the curve keeps climbing but much more slowly than any straight line — that gentle flattening is the signature of logarithmic growth.

---

## Example 2: Reading off the domain of a log function

> What is the domain of $f(x) = \ln(9 - x^2)$?

The argument of any logarithm must be strictly positive. The argument here is $9 - x^2$, so we require

$$
9 - x^2 > 0.
$$

Rearrange: $x^2 < 9$. Taking square roots, $|x| < 3$, which means $-3 < x < 3$. In interval notation the domain is $(-3, 3)$.

Notice how the natural restriction turns the domain into an *interval* rather than a ray — because the argument is a downward parabola in $x$, it is only positive for a bounded stretch of inputs. Whenever the argument inside a log is itself a polynomial or rational expression, the domain work is the real work.

---

## Example 3: Pulling features off a transformed log function

> Given $f(x) = \log_{5}(x - 2) - 1$, describe every key feature of its graph: which inputs it accepts, which outputs it produces, where the asymptote sits, and where the curve meets the axes.

Match the expression to the pattern $\log_{b}(x - h) + k$. Here $b = 5$, $h = 2$, and $k = -1$. That tells us the parent $\log_{5}$ graph has slid two units to the right and one unit down.

**Domain.** The argument must be positive: $x - 2 > 0$, so $x > 2$. In interval notation: $(2, \infty)$.

**Range.** Every logarithm function covers all real outputs, so the range stays at $(-\infty, \infty)$.

**Vertical asymptote.** The parent asymptote $x = 0$ moves along with the horizontal shift, landing at $x = 2$.

**$x$-intercept.** Set the output equal to zero and solve:

$$
\log_{5}(x - 2) - 1 = 0 \quad\Longrightarrow\quad \log_{5}(x - 2) = 1 \quad\Longrightarrow\quad x - 2 = 5^1 = 5.
$$

So $x = 7$, and the $x$-intercept is $(7, 0)$.

**$y$-intercept.** A $y$-intercept would require $x = 0$ to sit in the domain. It doesn't ($x = 0$ fails $x > 2$), so there is no $y$-intercept. Shifted logarithm graphs that start to the right of the $y$-axis simply never touch it.

---

## Common pitfalls

- **Forgetting to restrict the domain.** The first move on every logarithm problem is to set the argument strictly greater than zero and solve. Skipping that step is the leading cause of wrong answers and missed extraneous solutions later.
- **Confusing the vertical asymptote with a horizontal one.** Logarithms never flatten out into a horizontal asymptote. Their outputs grow without bound (slowly), so the only asymptote is vertical — the wall at $x = h$ where the argument would hit zero.
- **Drawing the curve like a square root.** Both shapes rise and flatten, but $\log_{b}(x)$ dives to $-\infty$ on the left edge of its domain, while $\sqrt{x}$ starts at a finite height. Check the behavior near $x = 0^+$ before committing to a sketch.
- **Treating the base as irrelevant.** Changing the base changes how fast the curve grows. $\log_{2}$ rises faster than $\log_{10}$, which rises faster than $\log_{100}$. All of them have the same shape, but the vertical stretch changes.

---

## Prerequisites

Before practicing, make sure you are comfortable with:

- [[Logarithms]] — the definition, common and natural logs, and swapping forms
- [[Exponential_Functions]] — logs are defined as the inverses of these, so their graphs borrow everything
- [[Inverse_Functions]] — the $y = x$ reflection is the master key for every property on this page
- [[Function_Basics]] — domain, range, and how to read transformations off an equation

---

## Problems Involving Logarithmic Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="logarithmic_functions"></div>

---

## See Also

- [[Logarithms]]
- [[Logarithmic_Equations]]
- [[Properties_Of_Logarithms]]
- [[Exponential_Functions]]
- [[Inverse_Functions]]
- [[Transformations_I_Shifts_And_Reflections]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
