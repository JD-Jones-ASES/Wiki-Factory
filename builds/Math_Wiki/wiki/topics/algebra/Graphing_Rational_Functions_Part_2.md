---
title: "Graphing Rational Functions: Part 2"
type: topic
aliases: ["Slant Asymptotes", "Rational Sign Analysis"]
tags: ["#branch-algebra-2", "#topic-rational-expressions", "#topic-functions", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "6", section: "6.5"}
related:
  - "topics/algebra/Graphing_Rational_Functions_Part_1"
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Introduction_To_Rational_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Graphing_Rational_Functions_Part_1"
  - "topics/algebra/Factoring_Trinomials_General"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
problem_type_ids: []
figures: []
summary: "Slant asymptotes, sign analysis, and a start-to-finish graphing recipe for rational functions."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Graphing Rational Functions: Part 2

# Graphing Rational Functions: Part 2

[[Graphing_Rational_Functions_Part_1|Part 1]] gave you the four basic features: vertical asymptotes, holes, horizontal asymptotes, and intercepts. That's enough to sketch many rational functions, but not all. When the top polynomial outgrows the bottom by exactly one degree, the graph develops a **slant asymptote** — a diagonal line it hugs far from zero instead of a horizontal one. And even once all the asymptotes are in place, you still need to know **which side of the x-axis** each branch of the graph lives on between its critical x-values. That's where a sign diagram earns its keep. Put it all together and you get a complete graphing recipe that handles every rational function in the algebra-2 curriculum.

---

## Slant asymptotes from polynomial long division

A slant asymptote (also known as an oblique asymptote) shows up when the numerator's degree is **exactly one more** than the denominator's:

$$
\deg p = \deg q + 1.
$$

To find the slant asymptote of $f(x) = p(x)/q(x)$, perform polynomial long division of $p$ by $q$. The result looks like

$$
p(x) = q(x) \cdot Q(x) + R(x),
$$

where $Q(x)$ is the quotient and $R(x)$ is the remainder (of lower degree than $q$). Divide both sides by $q(x)$:

$$
\dfrac{p(x)}{q(x)} = Q(x) + \dfrac{R(x)}{q(x)}.
$$

As $|x| \to \infty$, the fraction $R(x)/q(x)$ shrinks toward zero (because the remainder has a lower degree than the denominator), and what's left is $Q(x)$. If $\deg p - \deg q = 1$, then $Q(x)$ is a linear expression like $ax + b$, which is exactly a slant line. That line is the slant asymptote. If $\deg p - \deg q > 1$, the quotient is a higher-degree polynomial and the graph follows a curved "asymptote" — usually out of scope for algebra-2.

---

## Sign analysis between the critical x-values

Once you know the vertical asymptotes, the holes, and the x-intercepts, the x-axis is divided into intervals by those special values. Within each interval, the sign of $f(x)$ cannot change — a rational function only changes sign at a place where the numerator or the denominator equals zero. So once you know the sign on one point in each interval, you know it for the entire interval.

The quickest way is to pick a convenient test value in each interval and plug it into the factored form. You don't need the exact value; you only need to know whether the result comes out positive or negative. Draw a number line, mark the critical x-values, label each interval with a plus or minus sign, and now you know which side of the x-axis each branch of the graph will live on.

---

## The complete graphing recipe

Put everything from Part 1 and Part 2 into a standing procedure:

1. **Factor** the numerator and the denominator completely.
2. **Identify vertical asymptotes** — denominators zeros that don't cancel.
3. **Identify holes** — factors that cancel between top and bottom.
4. **Identify the horizontal or slant asymptote** from the degree comparison.
5. **Identify the x-intercepts** — numerator zeros that don't cancel.
6. **Identify the y-intercept** by evaluating $f(0)$.
7. **Do sign analysis** on the intervals between the critical x-values.
8. **Sketch**, piece by piece, using the asymptotes as guides and the sign diagram as a floor plan.

After a few hand-graphed examples, this routine becomes automatic.

---

## Example 1: a slant asymptote from long division

> Find the slant asymptote of $f(x) = \dfrac{x^2 + 3}{x - 1}$.

The numerator has degree $2$, the denominator has degree $1$, and $2 - 1 = 1$, so a slant asymptote exists. Carry out polynomial long division of $x^2 + 3$ by $x - 1$:

$$
\dfrac{x^2 + 3}{x - 1} = x + 1 + \dfrac{4}{x - 1}.
$$

(Quick sanity check: multiplying $(x + 1)(x - 1) = x^2 - 1$, and $(x^2 - 1) + 4 = x^2 + 3$. ✓)

As $|x| \to \infty$, the remainder piece $4/(x - 1)$ vanishes, and the graph hugs the line $y = x + 1$. That's the slant asymptote. The graph also has a vertical asymptote at $x = 1$ (where the denominator vanishes and the numerator $1 + 3 = 4$ doesn't), and the y-intercept is $f(0) = (0 + 3)/(0 - 1) = -3$.

Sketch: two branches separated by the vertical wall at $x = 1$, both leaning into the slant asymptote $y = x + 1$ far from the wall, with the left branch passing through $(0, -3)$ on its way out.

---

## Example 2: sign analysis on a factored rational

> Do a sign analysis for $f(x) = \dfrac{(x - 1)(x + 2)}{(x - 3)(x + 1)}$.

The critical x-values are the zeros of the top and bottom combined: $x = 1$, $x = -2$, $x = 3$, $x = -1$. Sorted: $-2, -1, 1, 3$. These four values divide the number line into five intervals:

$$
(-\infty, -2), \ (-2, -1), \ (-1, 1), \ (1, 3), \ (3, \infty).
$$

Pick a test value in each:

- $x = -3$ (far left): top = $(-3 - 1)(-3 + 2) = (-4)(-1) = 4$ (positive); bottom = $(-3 - 3)(-3 + 1) = (-6)(-2) = 12$ (positive). Ratio: **positive**.
- $x = -1.5$: top = $(-1.5 - 1)(-1.5 + 2) = (-2.5)(0.5) = -1.25$ (negative); bottom = $(-1.5 - 3)(-1.5 + 1) = (-4.5)(-0.5) = 2.25$ (positive). Ratio: **negative**.
- $x = 0$: top = $(-1)(2) = -2$ (negative); bottom = $(-3)(1) = -3$ (negative). Ratio: **positive**.
- $x = 2$: top = $(1)(4) = 4$ (positive); bottom = $(-1)(3) = -3$ (negative). Ratio: **negative**.
- $x = 4$ (far right): top = $(3)(6) = 18$ (positive); bottom = $(1)(5) = 5$ (positive). Ratio: **positive**.

Sign pattern: $+, -, +, -, +$ from left to right. The graph lives above the x-axis on the outer and middle intervals, and below it on $(-2, -1)$ and $(1, 3)$. Combined with the vertical asymptotes at $x = 3$ and $x = -1$, the sketch practically draws itself.

---

## Example 3: the complete graphing recipe

> Sketch $f(x) = \dfrac{x^2 - 4}{x^2 - x - 6}$.

**Step 1 — factor.** Top: $x^2 - 4 = (x - 2)(x + 2)$. Bottom: $x^2 - x - 6 = (x - 3)(x + 2)$. So

$$
f(x) = \dfrac{(x - 2)(x + 2)}{(x - 3)(x + 2)}.
$$

**Step 2 — vertical asymptotes.** The $(x + 2)$ factor cancels from top and bottom, so it produces a **hole** at $x = -2$, not an asymptote. The remaining denominator factor $(x - 3)$ gives a vertical asymptote at $x = 3$.

**Step 3 — the hole.** After cancellation, the simplified function is $(x - 2)/(x - 3)$. Evaluate at $x = -2$: $(-2 - 2)/(-2 - 3) = -4/-5 = 4/5$. The hole sits at $(-2, 4/5)$.

**Step 4 — horizontal asymptote.** Both top and bottom have degree $2$ in the original, with leading coefficients of $1$ and $1$. So the horizontal asymptote is $y = 1$.

**Step 5 — x-intercept.** Numerator factor $(x - 2)$ gives $x = 2$. The x-intercept is $(2, 0)$. (The cancelled $(x + 2)$ factor does **not** give an x-intercept — it gives the hole.)

**Step 6 — y-intercept.** $f(0) = (0 - 4)/(0 - 0 - 6) = -4/-6 = 2/3$. Point: $(0, 2/3)$.

**Step 7 — sign analysis** on the simplified form $(x - 2)/(x - 3)$. Critical values at $x = 2$ and $x = 3$ divide the line into $(-\infty, 2)$, $(2, 3)$, and $(3, \infty)$. Test $x = 0$: $(0 - 2)/(0 - 3) = -2/-3 > 0$. Test $x = 2.5$: $(0.5)/(-0.5) = -1 < 0$. Test $x = 4$: $(2)/(1) = 2 > 0$. Signs: $+, -, +$.

**Step 8 — sketch.** Draw the vertical asymptote at $x = 3$ and the horizontal asymptote at $y = 1$. Plot the x-intercept $(2, 0)$, the y-intercept $(0, 2/3)$, and the hole at $(-2, 4/5)$. Left branch: approaches $y = 1$ for very negative $x$, dips through the hole and the two intercepts, and plunges toward $-\infty$ as $x \to 3^-$. Right branch: starts high near $x \to 3^+$ and settles down toward $y = 1$ as $x \to \infty$. The sign diagram confirms the left branch sits above the axis except on $(2, 3)$, and the right branch is always above it.

---

## Common pitfalls

- **Skipping the factoring step.** Every feature of the graph depends on what cancels and what doesn't. Factoring is non-negotiable.
- **Confusing a hole with an asymptote.** The test is whether a factor truly cancels. If it does, it's a hole (graph is smooth except for a single missing point). If it doesn't, it's a wall.
- **Using the wrong degree comparison for the asymptote.** Equal degrees give a horizontal asymptote at the ratio of leading coefficients. Numerator degree one more gives a slant asymptote. Numerator degree two or more larger gives a curved end behavior.
- **Forgetting to plot the hole.** Even when the graph looks perfect otherwise, the original function is undefined at the hole x-value and has to be marked with an open circle.

---

## Prerequisites

- [[Graphing_Rational_Functions_Part_1]] — the basic features, which this page builds on
- [[Factoring_Trinomials_General]] — you'll factor both numerator and denominator
- [[Polynomial_Functions_And_Graphs]] — polynomial long division and end-behavior intuition

---

## Problems Involving Graphing Rational Functions (Part 2)

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphing_rational_functions_part_2"></div>

---

## See Also

- [[Graphing_Rational_Functions_Part_1]] — start here for the basic feature hunt
- [[Simplifying_Rational_Expressions]] — factoring and cancelling as a building block
- [[Polynomial_Functions_And_Graphs]] — end behavior and long division
- [[Introduction_To_Rational_Functions]] — the pre-calc overview
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
