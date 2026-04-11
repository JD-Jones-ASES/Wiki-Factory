---
title: "Graphs of Polynomials"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-polynomials", "#topic-functions", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Power_Functions"
  - "topics/algebra/Factoring_Completely"
  - "topics/precalculus/Real_Zeros_Of_Polynomials"
  - "topics/precalculus/Graphs_Of_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Power_Functions"
problem_type_ids: []
figures: []
summary: "Three features control every polynomial sketch: where the arms run, how the curve meets each zero, and how many times it can change direction."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Graphs of Polynomials

# Graphs of Polynomials

Once you move past parabolas into cubics, quartics, and higher-degree curves, the brute-force approach of plotting a dozen points and connecting the dots stops being practical. A good sketch of $y = x^{5} - 4x^{3} + x$ really only needs three pieces of information: where the two arms of the curve end up, what happens at each $x$-intercept, and a rough upper bound on how many wiggles you should draw in the middle. In precalculus the goal is to extract all three pieces directly from the formula, without ever touching a calculator.

The first two of those pieces — end behavior and multiplicity — were introduced in [[Polynomial_Functions_And_Graphs]] during algebra 2. This page sharpens them and adds the third ingredient: the **turning point** ceiling. Between them, these three rules give you a reliable sketch for any polynomial written in factored form, and a solid outline for any polynomial written in standard form.

---

## Setting the stage

Call a function **polynomial** when you can write it as a finite sum of non-negative integer powers of $x$, each tagged with a real coefficient:

$$
p(x) = a_{n} x^{n} + a_{n-1} x^{n-1} + \cdots + a_{1} x + a_{0}, \quad a_{n} \neq 0.
$$

The exponent $n$ is the **degree**, and $a_{n}$ is the **leading coefficient**. Every polynomial is continuous (no breaks, no holes, no vertical drops) and smooth (no sharp corners), so its graph is always one unbroken curve that flows gracefully from left to right. Those two guarantees are what make a sketch possible from so little raw data.

---

## Rule 1: End behavior from the leading term

Far out on the left and far out on the right, the leading term $a_{n}x^{n}$ dwarfs every other piece of the polynomial. Try plugging $x = 50$ into $q(x) = -3x^{4} + x^{2} + 2$: the $-3x^{4}$ contribution is $-18{,}750{,}000$, while $x^{2} + 2 = 2502$. The smaller terms barely nudge the answer. That is why far-left and far-right behavior reduces to a single-term question, and that question has exactly four answers determined by the parity of $n$ and the sign of $a_{n}$:

| Degree $n$ | Sign of $a_{n}$ | $x \to -\infty$ | $x \to +\infty$ |
|---|---|---|---|
| even | $+$ | $y \to +\infty$ | $y \to +\infty$ |
| even | $-$ | $y \to -\infty$ | $y \to -\infty$ |
| odd | $+$ | $y \to -\infty$ | $y \to +\infty$ |
| odd | $-$ | $y \to +\infty$ | $y \to -\infty$ |

Even-degree polynomials are "matching arms" — both arms point the same way. Odd-degree polynomials are "opposite arms" — the two sides always disagree. The sign of the leading coefficient then decides *which* way.

---

## Rule 2: Multiplicity at each zero

Factor the polynomial completely (over the real numbers). Each linear factor $(x - c)$ raised to some power $k$ contributes a zero at $x = c$ with **multiplicity** $k$. The multiplicity controls how the graph meets the $x$-axis there:

- **Odd multiplicity ($1, 3, 5, \ldots$):** the graph **crosses** the $x$-axis at $c$. It enters from one side and leaves on the other. Multiplicity $1$ is a plain, straight-through crossing; multiplicity $3$ flattens horizontally right at $c$ before continuing through; multiplicity $5$ flattens even more.
- **Even multiplicity ($2, 4, 6, \ldots$):** the graph **touches** the $x$-axis at $c$ but bounces back without crossing. It behaves like a mini parabola (for multiplicity $2$) or a mini quartic (for multiplicity $4$) riding on the axis.

This is the single most useful fact for hand-sketching a polynomial: it tells you the sign pattern of $p(x)$ on every interval between zeros without plugging in a single test value. If you know the sign just to the right of the largest zero (from end behavior), you can walk backward across each zero and flip or hold the sign according to whether the multiplicity is odd or even.

---

## Rule 3: Turning points bounded by $n - 1$

A **turning point** is a spot where the graph stops rising and starts falling, or stops falling and starts rising — a local peak or valley. If $p$ has degree $n$, then $p$ has **at most** $n - 1$ turning points. A cubic has at most $2$; a quartic has at most $3$; a quintic has at most $4$. The ceiling is sharp: some polynomials hit it exactly, and others come in under it.

Two notes on this rule. First, "at most" means the actual count can be lower — $y = x^{3}$ has zero turning points, not two. Second, you usually cannot pin down the exact number without calculus, but the upper bound is already enough to catch sketches that are trying to wiggle too much. If you have drawn four turning points on a degree-$4$ polynomial, you know you need to erase one.

---

## Putting the three rules together

The sketching routine for a polynomial in factored form is short:

1. Multiply the leading terms from each factor to recover the degree and leading coefficient. Read off the two end-behavior arrows.
2. List every zero with its multiplicity. Mark each with a "crosses" or "touches" tag.
3. Plug in $x = 0$ for the $y$-intercept.
4. Draw the two arms, pass the curve through each crossing zero, have it bounce at each touching zero, and connect everything with a smooth curve. Your number of humps should not exceed $n - 1$.

---

## Example 1: Sketching $f(x) = (x - 1)(x + 2)(x - 3)$

> Sketch $f(x) = (x - 1)(x + 2)(x - 3)$ by hand. Label end behavior, zeros with multiplicities, and the $y$-intercept.

The leading term comes from multiplying $x \cdot x \cdot x = x^{3}$, so the degree is $3$ and the leading coefficient is $+1$. Odd degree plus positive leading coefficient means the left arm falls to $-\infty$ and the right arm rises to $+\infty$.

The zeros sit at $x = -2$, $x = 1$, and $x = 3$, each from a factor to the first power. Every multiplicity is $1$, so the graph crosses straight through at all three zeros — no bounces.

The $y$-intercept is

$$
f(0) = (0 - 1)(0 + 2)(0 - 3) = (-1)(2)(-3) = 6.
$$

Now draw. The curve comes up from the lower-left, crosses the $x$-axis at $x = -2$, climbs to a local peak, passes through $(0, 6)$, starts dropping, crosses the axis again at $x = 1$, falls to a local valley, turns around, and crosses a third time at $x = 3$ on its way up to $+\infty$. A cubic has at most $2$ turning points, and this sketch uses exactly two (one peak between $x = -2$ and $x = 1$, one valley between $x = 1$ and $x = 3$). That matches the ceiling, which is typical when all three real zeros are distinct.

---

## Example 2: End behavior of $g(x) = -3x^{4} + x^{2} + 2$

> Describe the end behavior of $g(x) = -3x^{4} + x^{2} + 2$ without graphing.

Only the leading term matters at the ends, so ignore the $x^{2}$ and the $+2$ and focus on $-3x^{4}$. The degree $4$ is even, so the two arms of $g$ must head in the **same** direction. The leading coefficient $-3$ is negative, so that shared direction is **downward**:

$$
\text{as } x \to -\infty, \; g(x) \to -\infty; \quad \text{as } x \to +\infty, \; g(x) \to -\infty.
$$

Both arms point into the lower half of the plane. The rest of the graph (zeros, turning points, $y$-intercept $g(0) = 2$) lives somewhere in a bounded middle region, but you already know the overall shape sweeps from the lower-left up through a bounded zone and back down to the lower-right. That is the "upside-down bowl with wiggles" shape typical of even-degree polynomials with negative leading coefficients.

---

## Example 3: Maximum turning points of a degree-$5$ polynomial

> A polynomial $p(x)$ has degree $5$. What is the largest possible number of turning points on its graph, and what does that imply about its $x$-intercepts?

Rule $3$ caps the turning-point count at $n - 1 = 5 - 1 = 4$. So $p$ can have at most **four** turning points: up to four places where the curve changes from rising to falling or vice versa.

If $p$ actually reaches that maximum of four turning points, the graph swings up and down four separate times. Between each pair of turning points the function flips sign at least once, so the curve can potentially cross the $x$-axis in up to five distinct spots — which matches the other well-known cap, that a degree-$n$ polynomial has at most $n$ real zeros counted with multiplicity. A degree-$5$ polynomial cannot have six or more real zeros, cannot have five or more turning points, and cannot have matching-arms end behavior (degree $5$ is odd, so the arms always disagree).

Note that "at most" is the operative phrase for both caps. A degree-$5$ polynomial can also have zero turning points (as with $y = x^{5}$), one turning point, two, three, or four. Likewise it can have anywhere from one real zero (the minimum for any odd degree, since the graph must cross the $x$-axis at least once on its trip from $-\infty$ to $+\infty$) up to five.

---

## Common pitfalls

- **Treating degree and leading coefficient as the same thing.** They are two separate pieces of information. The degree decides matching-arms versus opposite-arms; the sign of the leading coefficient decides which way. Forgetting either half gives a wrong end-behavior answer half the time.
- **Confusing "touching" with "not a zero."** A bounce point is still a zero — the polynomial still evaluates to $0$ there. It just does not cross the axis. On an $x$-intercept list you should include every bounce zero right alongside every crossing zero.
- **Drawing too many humps.** A degree-$3$ polynomial cannot have three turning points, a degree-$4$ cannot have four, and so on. Count your humps against $n - 1$ before you commit to a sketch.
- **Reading multiplicity from standard form.** You cannot tell multiplicity from $p(x) = x^{4} - 5x^{2} + 4$ directly — you have to factor first (here it becomes $(x-1)(x+1)(x-2)(x+2)$, so every zero is simple). Multiplicity only shows up in the factored form.
- **Ignoring the $y$-intercept.** Plugging in $x = 0$ costs nothing and pins down a single point the curve must pass through. It is an excellent sanity check after you sketch everything else.

---

## Prerequisites

- [[Polynomial_Functions_And_Graphs]] — the algebra-2 introduction to the same three rules, with more elementary examples
- [[Factoring_Completely]] — because multiplicity can only be read from a fully factored polynomial
- [[Power_Functions]] — the single-term reference curves $y = x^{n}$ whose shape the leading term mimics at the ends

---

## Problems Involving Graphs of Polynomials

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphs_of_polynomials"></div>

---

## See Also

- [[Polynomial_Functions_And_Graphs]] — the algebra-2 version of this lesson, with the foundational framing
- [[Real_Zeros_Of_Polynomials]] — finding the $x$-intercepts when the polynomial is not already factored
- [[Power_Functions]] — the monomial building blocks behind every polynomial's end behavior
- [[Factoring_Completely]] — how to get from standard form into the factored form needed for multiplicity
- [[Graphs_Of_Functions]] — the general toolbox of function-graphing moves
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
