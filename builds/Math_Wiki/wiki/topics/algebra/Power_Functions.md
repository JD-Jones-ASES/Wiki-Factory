---
title: "Power Functions"
type: topic
aliases: ["Power Function", "Monomial Function"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-exponents-and-radicals"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "4", section: "4.2"}
related:
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Square_Root_Functions"
  - "topics/algebra/Cube_Root_And_Other_Radical_Functions"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: ["algebra/parent_function_gallery.svg"]
summary: "A menagerie of shapes controlled by one exponent: $f(x) = k x^n$ with $n$ positive, negative, or fractional."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Power Functions

# Power Functions

A **power function** is a simple-looking rule with a surprising amount of shape inside it:

$$
f(x) = k\,x^{n},
$$

where $k$ and $n$ are real constants and $n$ is the **exponent** (or degree). That is the whole definition — one constant out front, one variable raised to a fixed power. What makes this family interesting is that even though every member is written the same way, the picture you get on a coordinate plane changes dramatically as you slide $n$ around. A single tweak to that exponent can turn a straight line into a bowl, a bowl into an S-curve, an S-curve into a pair of branches hugging the axes. If you can recognize which shape to expect from the exponent alone, you can sketch a power function with almost no calculation.

You have already met several members of this family under other names. A line $y = kx$ is a power function with $n = 1$. A parabola $y = kx^{2}$ is a power function with $n = 2$. A square root graph $y = \sqrt{x}$ is a power function with $n = \tfrac{1}{2}$. What this page does is line all of them up side by side and explain how the exponent controls the shape.

![[parent_function_gallery.svg|A gallery of common parent functions]]

---

## The menagerie of shapes

Different values of $n$ produce genuinely different pictures. Here is a quick tour of the shapes you should be able to recognize at a glance:

| Exponent $n$ | Example | Typical shape |
|---|---|---|
| $n = 1$ | $y = x$ | Straight line through the origin (see [[Linear_Functions]]) |
| $n = 2$ | $y = x^{2}$ | Upward parabola, symmetric about the $y$-axis (see [[Quadratic_Functions]]) |
| $n = 3$ | $y = x^{3}$ | S-curve through the origin, climbs from lower-left to upper-right |
| $n = 4, 6, 8, \dots$ | $y = x^{4}$ | Flatter-bottomed bowl; the higher $n$ is, the flatter the middle and the steeper the sides |
| $n = 5, 7, 9, \dots$ | $y = x^{5}$ | Steeper S-curve; middle section hugs the $x$-axis longer, then shoots up |
| $n = -1$ | $y = \tfrac{1}{x}$ | Two hyperbola branches; vertical asymptote at $x = 0$, horizontal asymptote at $y = 0$ |
| $n = -2$ | $y = \tfrac{1}{x^{2}}$ | Two branches both opening upward; vertical asymptote at $x = 0$ |
| $n = \tfrac{1}{2}$ | $y = \sqrt{x}$ | Gentle curve starting at the origin, only defined for $x \geq 0$ (see [[Square_Root_Functions]]) |
| $n = \tfrac{1}{3}$ | $y = \sqrt[3]{x}$ | S-curve through the origin defined for every real input (see [[Cube_Root_And_Other_Radical_Functions]]) |

Every row of that table is a power function. Once you know which row you are in, the broad shape is already decided.

---

## How the exponent controls the shape

There are three questions you can ask about $n$ that jointly pin down the graph of $y = x^{n}$.

**Is $n$ positive or negative?** A positive exponent means the function grows as $|x|$ grows — larger inputs produce larger outputs in magnitude. A negative exponent flips that: now large inputs give small outputs, and tiny inputs (near zero) blow up. Negative exponents are where asymptotes come from, since $x = 0$ is not allowed when $n < 0$.

**Is $n$ even or odd?** When $n$ is a positive integer, the parity of $n$ controls the symmetry. An even exponent makes the function **even**, meaning $f(-x) = f(x)$: the graph is a mirror image across the $y$-axis, like $y = x^{2}$ or $y = x^{4}$. An odd exponent makes it **odd**, meaning $f(-x) = -f(x)$: rotating the graph $180^{\circ}$ around the origin lands it back on itself, like $y = x^{3}$ or $y = x^{5}$. Even powers produce U- or bowl-shapes; odd powers produce S-shapes.

**Is $n$ an integer or a fraction?** Integer exponents give the familiar lines, parabolas, cubics, and quartics. Fractional exponents behave like radicals — for instance, $x^{1/2} = \sqrt{x}$ and $x^{1/3} = \sqrt[3]{x}$. Between those, $x^{3/2} = (\sqrt{x})^{3}$ grows faster than $\sqrt{x}$ but slower than $x^{2}$, filling in the continuum between shapes.

A helpful visual anchor: every positive-exponent curve $y = x^{n}$ passes through $(0, 0)$ and $(1, 1)$. When $n$ is even, it also passes through $(-1, 1)$; when $n$ is odd, it passes through $(-1, -1)$. If you plant those two or three points and remember the parity rule, you can sketch any positive-integer power function without a table of values.

---

## End behavior: where the arms of the graph go

The **end behavior** of a function describes what happens to $y$ as $x$ heads off toward $+\infty$ or $-\infty$. For positive-integer power functions, the pattern is short and memorable:

- Even $n$: as $x \to +\infty$, $y \to +\infty$; as $x \to -\infty$, $y \to +\infty$. Both arms point up.
- Odd $n$: as $x \to +\infty$, $y \to +\infty$; as $x \to -\infty$, $y \to -\infty$. One arm up, one arm down.

For negative exponents, the story flips. The graph of $y = 1/x$ has two branches that approach the $x$-axis as $|x|$ grows — the ends flatten toward zero rather than flying off. And as $x$ approaches zero, the output races toward $\pm\infty$, producing a vertical asymptote. The graph of $y = 1/x^{2}$ behaves similarly near zero, but because squaring wipes out the sign, both branches stay above the $x$-axis.

---

## Example 1: comparing $y = x^{2}$, $y = x^{3}$, and $y = x^{4}$

Imagine overlaying these three graphs on the same pair of axes. All three pass through the origin. All three pass through $(1, 1)$. But they pull apart in two places.

On the **left half** (inputs where $x < 0$), $y = x^{2}$ and $y = x^{4}$ are above the axis because even powers of a negative number are positive; they look like bowls. On the same side, $y = x^{3}$ dives beneath the axis because an odd power keeps the negative sign.

In the **middle** (say for $0 < x < 1$), the higher exponents actually give smaller outputs. A number like $0.5$ cubed is $0.125$, and the same number raised to the fourth is $0.0625$. So $y = x^{4}$ is the flattest curve near zero and $y = x^{2}$ is the steepest.

In the **far right** (say for $x > 2$), the ordering reverses. Now $y = x^{4}$ rockets past $y = x^{3}$, which rockets past $y = x^{2}$. At $x = 3$ you get outputs of $9$, $27$, and $81$.

So the three curves start stacked together near $(0, 0)$, briefly put $y = x^{4}$ lowest and $y = x^{2}$ highest when $x$ is between $0$ and $1$, and then swap order entirely as $x$ gets large. The takeaway: a higher exponent produces a flatter middle but a steeper tail.

---

## Example 2: the reciprocal function $y = 1/x$

Set $n = -1$ and the picture changes completely. Rewrite the rule as

$$
y = \frac{1}{x}.
$$

Plugging in $x = 0$ is impossible (division by zero), so the domain excludes zero. What does the graph look like?

- For **large positive $x$**, the output is small and positive. At $x = 10$, $y = 0.1$. At $x = 100$, $y = 0.01$. The curve hugs the $x$-axis from above.
- For **small positive $x$** (close to zero), the output is huge. At $x = 0.1$, $y = 10$. At $x = 0.01$, $y = 100$. The curve shoots up toward the $y$-axis without ever touching it.
- For **negative $x$**, the same logic applies with signs flipped: the output is negative, and the branch lives in the third quadrant, mirroring the first-quadrant branch by a $180^{\circ}$ rotation about the origin.

You end up with two disconnected branches: one in the upper-right, one in the lower-left. The $y$-axis is a **vertical asymptote** and the $x$-axis is a **horizontal asymptote** — the curve sneaks arbitrarily close to each without ever meeting them. This is the simplest example of asymptotic behavior in algebra, and it is what you get whenever a power function has a negative exponent.

---

## Example 3: evaluating $y = x^{3/2}$ at a few points

A fractional exponent like $n = \tfrac{3}{2}$ is harder to picture, so build a small table of values. The rule $y = x^{3/2}$ means "take the square root of $x$, then cube it" — or equivalently, "cube $x$, then take the square root." Both orders give the same result when $x \geq 0$.

Because the square root of a negative is not real, the domain is $x \geq 0$. Plug in a few values:

| $x$ | $\sqrt{x}$ | $x^{3/2} = (\sqrt{x})^{3}$ |
|---|---|---|
| $0$ | $0$ | $0$ |
| $1$ | $1$ | $1$ |
| $4$ | $2$ | $8$ |
| $9$ | $3$ | $27$ |

Plot those four points and draw a smooth curve through them. Notice how the graph starts at the origin, climbs more slowly than $y = x^{2}$ for small inputs (at $x = 4$, you get $8$ instead of $16$), but still grows faster than $y = x$ (at $x = 4$, you get $8$ instead of $4$). A fractional exponent between $1$ and $2$ produces a shape that sits between the line and the parabola, exactly as you would expect from blending them.

---

## Common pitfalls

- **Confusing $x^{n}$ with $nx$.** The function $x^{3}$ is $x \cdot x \cdot x$; the function $3x$ is a line. They match only at $x = 0$ and at $x = \sqrt{3}$ — everywhere else their values diverge sharply.
- **Forgetting the domain restriction on negative exponents.** Any power function with $n < 0$ excludes $x = 0$ from its domain, because division by zero is undefined. That missing point creates a vertical asymptote, not just an isolated hole.
- **Treating $(-x)^{n}$ the same for even and odd $n$.** For even $n$, $(-x)^{n} = x^{n}$ (the sign disappears). For odd $n$, $(-x)^{n} = -x^{n}$ (the sign survives). This is the algebra behind the symmetry rules.
- **Expecting fractional-exponent graphs to be defined for every input.** An exponent like $\tfrac{1}{2}$ or $\tfrac{3}{4}$ requires a non-negative input because of the underlying square root. Only odd-denominator fractional exponents (like $\tfrac{1}{3}$) accept negative inputs.

---

## Prerequisites

Before tackling practice problems on this topic, make sure you are comfortable with:

- [[Properties_Of_Exponents]] — so the algebra of $x^{n}$ (including negative and fractional exponents) feels familiar
- [[Function_Basics]] — for the language of inputs, outputs, domains, and ranges
- [[Plotting_Points_And_The_Coordinate_Plane]] — so you can turn a table of values into a curve

If any of those feel shaky, start there and come back.

---

## Problems Involving Power Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="power_functions"></div>

---

## See Also

- [[Linear_Functions]] — the $n = 1$ case
- [[Quadratic_Functions]] — the $n = 2$ case
- [[Square_Root_Functions]] — the $n = \tfrac{1}{2}$ case
- [[Cube_Root_And_Other_Radical_Functions]] — the $n = \tfrac{1}{3}$ case
- [[Polynomial_Functions_And_Graphs]] — sums of positive-integer power functions
- [[Transformations_I_Shifts_And_Reflections]] — how to shift and flip any power curve
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
