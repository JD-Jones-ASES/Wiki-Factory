---
title: "Graphs of Rational Functions"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-rational-expressions", "#topic-functions", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Graphing_Rational_Functions_Part_1"
  - "topics/algebra/Graphing_Rational_Functions_Part_2"
  - "topics/precalculus/Graphs_Of_Polynomials"
  - "topics/precalculus/Graphs_Of_Functions"
  - "topics/algebra/Factoring_Completely"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Graphing_Rational_Functions_Part_1"
  - "topics/algebra/Factoring_Completely"
  - "topics/precalculus/Graphs_Of_Polynomials"
problem_type_ids: []
figures: []
summary: "Where the denominator and numerator compete: zeros of the denominator carve out forbidden x-values, and the race between the two degrees determines the far-right and far-left behavior."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Graphs of Rational Functions

# Graphs of Rational Functions

A **rational function** is built by dividing one polynomial by another:

$$
r(x) = \frac{N(x)}{D(x)},
$$

where $N(x)$ and $D(x)$ are both polynomials and $D(x)$ is not the zero polynomial. The name comes from the fact that "rational number" means "ratio of integers," and a rational function is just the same idea with polynomials instead of integers.

Unlike polynomials, rational functions can fail to be defined at certain $x$-values, can shoot off to $\pm\infty$ partway through the graph, and can settle down to a finite horizontal line far out to the sides. All of that unusual behavior comes from one source: wherever $D(x) = 0$, division breaks. The goal of this page is to read four features directly from a rational formula — domain, vertical asymptotes, holes, and end behavior — fast enough to produce a clean sketch.

---

## Domain: what's off-limits

A rational function is defined everywhere its denominator is nonzero. To find the **domain**, solve $D(x) = 0$ and then exclude those solutions from the real line:

$$
\text{domain of } r \;=\; \{x \in \mathbb{R} : D(x) \neq 0\}.
$$

For example, if $D(x) = x^{2} - 4 = (x - 2)(x + 2)$, the domain is all real numbers except $x = 2$ and $x = -2$. Those two forbidden $x$-values will become either vertical asymptotes or holes, depending on whether the same values also zero out the numerator.

---

## Vertical asymptotes and holes: two flavors of "D(x) = 0"

Suppose $x = c$ makes the denominator zero. Two possibilities arise depending on what the numerator does at the same spot.

**Case 1: the numerator does not vanish at $c$.** Then $r(x) = N(x)/D(x)$ tries to divide a nonzero number by a tiny number near $x = c$, producing huge outputs with unbounded magnitude. The graph has a **vertical asymptote** at $x = c$: a vertical line the curve approaches but never touches. On one side of $c$ the curve races to $+\infty$, and on the other side it races to $-\infty$ or $+\infty$ depending on sign information you can extract by checking the sign of $r$ just to the left and just to the right of $c$.

**Case 2: the numerator also vanishes at $c$.** Then both top and bottom are zero, and the value of $r(c)$ is formally $0/0$ — indeterminate. When this happens, try factoring both $N$ and $D$ and canceling the shared factor $(x - c)$. If after cancellation the denominator of the simplified expression is still zero at $x = c$, you still have a vertical asymptote. If after cancellation the simplified expression is fine at $x = c$, the original function has a **hole** at that point: the graph behaves exactly like the simplified version everywhere except $x = c$, where the point is missing entirely.

The practical rule is: factor numerator and denominator, cancel whatever you can, and then re-check which forbidden values survive. Survivors become vertical asymptotes. Forbidden values that get canceled out become holes.

---

## Horizontal and slant asymptotes: the degree race

Far to the left and right, the behavior of $r(x) = N(x)/D(x)$ is controlled by which polynomial grows faster. Let $n$ be the degree of $N$ and $d$ be the degree of $D$:

- **$n < d$ (denominator wins).** The denominator grows faster, so the ratio shrinks to zero. The graph has a **horizontal asymptote at $y = 0$**: both arms flatten toward the $x$-axis.
- **$n = d$ (tie).** The leading terms of $N$ and $D$ are both of the same degree, so their ratio approaches the ratio of leading coefficients. If the leading coefficients are $a$ and $b$, the graph has a **horizontal asymptote at $y = a/b$**.
- **$n > d$ (numerator wins).** The numerator grows faster, so the ratio grows without bound. The graph has **no horizontal asymptote**. If $n$ is exactly one more than $d$, polynomial long division of $N$ by $D$ produces a linear quotient plus a proper remainder, and the line $y = (\text{linear quotient})$ is a **slant asymptote** (also called an oblique asymptote). Both arms of $r$ approach that slanted line as $|x| \to \infty$.

This is really a statement about the limits at infinity: dividing out the fastest-growing term in the numerator by the fastest-growing term in the denominator gives the end behavior in one step.

---

## The full sketching routine

Putting it all together, a clean sketch of a rational function comes from five quick checks:

1. **Factor** both numerator and denominator completely.
2. **Cancel** any shared factors. Record any canceled factor $(x - c)$ as a hole.
3. **Vertical asymptotes** at each $x$-value where the simplified denominator is zero.
4. **Horizontal or slant asymptote** from the degree comparison of the simplified numerator and denominator.
5. **$x$-intercepts** at the zeros of the simplified numerator; **$y$-intercept** at $r(0)$ (if $0$ is in the domain).

Plot the asymptotes as dashed lines, mark the intercepts and holes, then connect everything with a smooth curve that obeys the asymptote behavior on each side. The dashed asymptotes act as invisible rails the curve never crosses near the ends (and rarely, but not never, crosses in the middle).

---

## Example 1: Vertical and horizontal asymptotes of $f(x) = \dfrac{2x + 3}{x - 1}$

> Find all vertical and horizontal asymptotes of $f(x) = \dfrac{2x + 3}{x - 1}$.

**Factor and cancel.** Both $2x + 3$ and $x - 1$ are already first-degree and share no common factors, so there is nothing to cancel. No holes will appear.

**Vertical asymptote.** Set the denominator equal to zero: $x - 1 = 0$, so $x = 1$. The numerator at $x = 1$ is $2(1) + 3 = 5 \neq 0$, confirming a genuine vertical asymptote (not a hole). The line $x = 1$ is the vertical asymptote.

**Horizontal asymptote.** Compare degrees: the numerator has degree $1$, the denominator has degree $1$, so they tie. The horizontal asymptote is the ratio of leading coefficients, $\tfrac{2}{1} = 2$. The line $y = 2$ is the horizontal asymptote.

As $x \to \pm\infty$, the graph flattens toward $y = 2$. As $x$ approaches $1$ from the right, the denominator is a tiny positive number and the numerator is close to $5$, so $f(x) \to +\infty$. As $x$ approaches $1$ from the left, the denominator is a tiny negative number, so $f(x) \to -\infty$. That gives the classic two-branch shape of a shifted reciprocal function.

---

## Example 2: A hole in $g(x) = \dfrac{x^{2} - 4}{x - 2}$

> Identify and describe the hole in $g(x) = \dfrac{x^{2} - 4}{x - 2}$.

**Factor and cancel.** The numerator factors as a difference of squares: $x^{2} - 4 = (x - 2)(x + 2)$. So

$$
g(x) = \frac{(x - 2)(x + 2)}{x - 2}.
$$

The factor $(x - 2)$ appears in both top and bottom and can be canceled, leaving the simplified form

$$
g(x) = x + 2 \quad \text{for } x \neq 2.
$$

The restriction $x \neq 2$ is critical. The original function is still undefined at $x = 2$, even though the simplified form $x + 2$ has no problem there.

**What the graph looks like.** The simplified form $x + 2$ is just a line with slope $1$ and $y$-intercept $2$. So the graph of $g$ is exactly that line, with **one point removed** at $x = 2$. At $x = 2$ the line would pass through $(2, 4)$, so the hole sits at the point $(2, 4)$. On paper you draw the line $y = x + 2$ and then place an open circle at $(2, 4)$ to indicate the missing point.

There is no vertical asymptote here — the denominator zero at $x = 2$ was canceled, so the graph does not blow up there. There is also no horizontal asymptote, because once you simplify, the function is a degree-$1$ polynomial, which grows without bound in both directions.

---

## Example 3: End behavior of $h(x) = \dfrac{x^{2} + 1}{x - 3}$

> Describe the end behavior of $h(x) = \dfrac{x^{2} + 1}{x - 3}$. Include any horizontal or slant asymptote.

**Factor and cancel.** The numerator $x^{2} + 1$ does not factor over the reals, and the denominator $x - 3$ shares no common factors with it. Nothing cancels.

**Degree comparison.** The numerator has degree $2$; the denominator has degree $1$. Since $n = 2 > 1 = d$, there is **no horizontal asymptote**. But because $n$ is exactly one more than $d$, a **slant asymptote** exists and can be computed by long-dividing $N$ by $D$.

Polynomial long division of $x^{2} + 1$ by $x - 3$ proceeds as follows. First, $x^{2} \div x = x$. Multiply $x$ by $(x - 3)$ to get $x^{2} - 3x$. Subtract:

$$
(x^{2} + 0x + 1) - (x^{2} - 3x) = 3x + 1.
$$

Next, $3x \div x = 3$. Multiply $3$ by $(x - 3)$ to get $3x - 9$. Subtract:

$$
(3x + 1) - (3x - 9) = 10.
$$

So the division gives

$$
h(x) = x + 3 + \frac{10}{x - 3}.
$$

As $x \to \pm\infty$, the remainder term $\tfrac{10}{x - 3}$ shrinks to zero, leaving $h(x) \approx x + 3$. The **slant asymptote** is the line $y = x + 3$. Far to the right, the graph runs parallel to (and just above) that line; far to the left, it runs parallel to (and just below) it. In between, a vertical asymptote sits at $x = 3$, where $h$ blows up.

---

## Common pitfalls

- **Canceling without noting the hole.** When you cancel a factor like $(x - 2)$ from top and bottom, the function still has that value excluded from its domain. The simplified expression looks fine at $x = 2$, but the original does not — the point stays missing, and you must mark a hole.
- **Declaring a horizontal asymptote when the degrees do not tie or the bottom does not win.** If the numerator has higher degree, there is no horizontal asymptote at all. The graph heads to infinity on both sides. Students often write $y = 0$ as a default, which is wrong in this case.
- **Thinking the graph cannot cross a horizontal asymptote.** Vertical asymptotes are walls — the graph never crosses them. Horizontal asymptotes are only guides for behavior at the ends. In the interior of the graph, a rational function is perfectly free to cross its horizontal asymptote, and often does exactly once.
- **Forgetting to factor before analyzing.** Without factoring, you cannot tell a hole from a vertical asymptote, and you cannot spot shared factors. Factoring is the first move, always.
- **Mixing up leading coefficients with the full leading terms.** The horizontal asymptote in the tie case is the ratio of leading *coefficients*, not the ratio of full leading terms (which would be $1$). For $\tfrac{3x^{2} + 1}{5x^{2} - 2}$, the horizontal asymptote is $y = 3/5$, not $y = 3/(5x^{2})$ or anything involving $x$.

---

## Prerequisites

- [[Graphing_Rational_Functions_Part_1]] — the algebra-2 entry point, where holes and vertical asymptotes are first introduced
- [[Factoring_Completely]] — you cannot find holes or read leading terms without factoring top and bottom first
- [[Graphs_Of_Polynomials]] — because a rational function's end behavior reduces to a polynomial end-behavior question after long division

---

## Problems Involving Graphs of Rational Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphs_of_rational_functions"></div>

---

## See Also

- [[Graphing_Rational_Functions_Part_1]] — introductory algebra-2 coverage
- [[Graphing_Rational_Functions_Part_2]] — advanced algebra-2 coverage, including slant asymptotes
- [[Graphs_Of_Polynomials]] — the polynomial case, whose rules govern the end-behavior comparison
- [[Factoring_Completely]] — the preprocessing step for any rational function problem
- [[Graphs_Of_Functions]] — the general function-graphing toolbox
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
