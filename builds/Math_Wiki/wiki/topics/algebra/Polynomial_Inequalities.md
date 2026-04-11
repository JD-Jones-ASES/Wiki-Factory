---
title: "Polynomial Inequalities"
type: topic
aliases: ["Sign Chart Method for Polynomial Inequalities"]
tags: ["#branch-algebra-2", "#topic-inequalities", "#skill-algebraic-manipulation", "#skill-multi-step", "#key-technique", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Rational_Inequalities"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Solving_Inequalities_In_One_Variable"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Polynomial_Basics"
problem_type_ids: []
figures: ["algebra/polynomial_sign_chart.svg"]
summary: "To solve a polynomial inequality, move everything to one side, factor, mark the critical points on a number line, and read off which intervals have the right sign."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Polynomial Inequalities

# Polynomial Inequalities

A **polynomial inequality** asks you to find every value of $x$ that makes a polynomial expression larger than, smaller than, or equal to zero — not just the specific values where the polynomial equals zero. For example, the question "for which $x$ is $x^2 - 5x + 6 \ge 0$?" is asking not just for the roots of $x^2 - 5x + 6$, but for the entire set of inputs where the graph of $y = x^2 - 5x + 6$ lives on or above the $x$-axis. The answer is almost never a single number. It is usually a collection of intervals on the number line, and those intervals are the whole point of the technique you are about to learn.

![[polynomial_sign_chart.svg|A sign chart for (x-2)(x-3) ≥ 0 showing positive regions x ≤ 2 and x ≥ 3]]

The key insight — the one that makes the whole method click — is that a polynomial can only change sign at one of its zeros. Between two consecutive zeros, the polynomial is stuck on one side of the $x$-axis: it is either positive everywhere on that stretch, or negative everywhere. So once you know the zeros, you only have to test a single point from each interval to learn the sign of the entire interval. That is the **sign chart method**, and it is the standard tool for these problems.

## What it means

A polynomial inequality is built from a polynomial $P(x)$ and one of the four comparison symbols $<$, $\le$, $>$, or $\ge$. The goal is to describe the set of all real numbers $x$ for which the comparison is true. The method does not care whether the polynomial is a quadratic, a cubic, or a quartic — the procedure is the same, as long as the polynomial can be factored into linear pieces (or the irreducible factors are understood).

For a quadratic example, the inequality $x^2 - 5x + 6 \ge 0$ factors as $(x - 2)(x - 3) \ge 0$. Because the two linear pieces produce sign changes only at $x = 2$ and $x = 3$, the real number line splits into three intervals — the piece below $2$, the piece between $2$ and $3$, and the piece above $3$ — and the product has a constant sign on each piece. Reading the signs off gives:

$$
x^2 - 5x + 6 \ge 0 \quad\Longleftrightarrow\quad (x - 2)(x - 3) \ge 0 \quad\Longleftrightarrow\quad x \le 2 \text{ or } x \ge 3
$$

That final answer, written in interval notation, is $(-\infty, 2] \cup [3, \infty)$. The two brackets are square because the inequality is non-strict, which means the boundary points where the polynomial equals zero are included in the solution set.

## How it works

Here is the standard five-step procedure. Learn it once and every polynomial inequality becomes a checklist:

1. **Move everything to one side.** Rewrite the inequality so the comparison is against $0$. If the problem is $x^2 + 2x > 3$, subtract $3$ from both sides to get $x^2 + 2x - 3 > 0$. Do not skip this step. The sign chart method reads signs relative to zero, so the other side has to be zero.
2. **Factor the polynomial completely.** Use every factoring tool you know — common factor, difference of squares, factor-by-grouping, trinomial factoring. The finer you factor, the cleaner the sign chart will be.
3. **Find the critical points.** These are the zeros of the polynomial — the $x$-values that make at least one factor equal to zero. List them in increasing order.
4. **Build a sign chart.** Draw a number line, plot the critical points, and in each interval between critical points pick any easy test value and substitute it into the factored form. You only need the sign of the result, not its exact value. Write $+$ or $-$ above the interval based on what each factor contributes. Repeat for every interval.
5. **Read off the solution.** Select the intervals whose sign matches the comparison. For a $> 0$ or $\ge 0$ problem, keep the positive intervals; for a $< 0$ or $\le 0$ problem, keep the negative ones. If the inequality is non-strict ($\le$ or $\ge$), also include the critical points themselves, because the polynomial equals zero there. If it is strict ($<$ or $>$), the critical points are excluded. Express the solution in interval notation.

## Why it works

Two facts from Algebra 1 keep the method honest. First, a continuous function (and every polynomial is continuous) cannot change sign without passing through zero — there is no "jumping" from positive to negative without crossing the $x$-axis. Second, the zeros of a polynomial are exactly the roots of its factors, so factoring reveals every candidate location where a sign change might happen. Between two consecutive zeros the polynomial stays on one side of the $x$-axis, so a single test value is enough to pin down the sign of the whole interval. And because the polynomial has only finitely many zeros, the real number line really does split into finitely many intervals with clean, constant signs. This is why the sign chart works — the tested signs on each piece are guaranteed to be correct for every point in that piece.

## Worked examples

### Example 1

Express the solution set of $x^2 - 5x + 6 \ge 0$ in interval notation.

The comparison is already against zero, so step one is free. Factor the quadratic: $x^2 - 5x + 6 = (x - 2)(x - 3)$. The critical points are $x = 2$ and $x = 3$. The number line breaks into three intervals: $(-\infty, 2)$, $(2, 3)$, and $(3, \infty)$.

Test a value from each interval in the factored form $(x - 2)(x - 3)$:

- At $x = 0$: $(0 - 2)(0 - 3) = (-2)(-3) = 6 > 0$. Mark the interval $(-\infty, 2)$ as $+$.
- At $x = 2.5$: $(2.5 - 2)(2.5 - 3) = (0.5)(-0.5) = -0.25 < 0$. Mark the interval $(2, 3)$ as $-$.
- At $x = 4$: $(4 - 2)(4 - 3) = (2)(1) = 2 > 0$. Mark the interval $(3, \infty)$ as $+$.

The inequality wants $\ge 0$, so keep the positive intervals **and** include the boundary points where the expression equals zero. The solution is $x \le 2$ or $x \ge 3$, which in interval notation is $(-\infty, 2] \cup [3, \infty)$.

### Example 2

Identify every real $x$ satisfying $(x - 1)(x + 2)(x - 3) < 0$.

The polynomial is already factored, and the comparison is already against zero. The critical points are $x = -2$, $x = 1$, and $x = 3$ (listed in increasing order). The number line breaks into four intervals: $(-\infty, -2)$, $(-2, 1)$, $(1, 3)$, and $(3, \infty)$.

Pick a friendly test value from each:

- At $x = -3$: $(-3 - 1)(-3 + 2)(-3 - 3) = (-4)(-1)(-6) = -24 < 0$. Mark $(-\infty, -2)$ as $-$.
- At $x = 0$: $(0 - 1)(0 + 2)(0 - 3) = (-1)(2)(-3) = 6 > 0$. Mark $(-2, 1)$ as $+$.
- At $x = 2$: $(2 - 1)(2 + 2)(2 - 3) = (1)(4)(-1) = -4 < 0$. Mark $(1, 3)$ as $-$.
- At $x = 4$: $(4 - 1)(4 + 2)(4 - 3) = (3)(6)(1) = 18 > 0$. Mark $(3, \infty)$ as $+$.

The inequality wants $< 0$, so keep only the negative intervals. The comparison is strict, so the critical points are **not** included. The solution is $x < -2$ or $1 < x < 3$, or in interval notation $(-\infty, -2) \cup (1, 3)$. Notice the sign pattern $- + - +$: with three distinct linear factors, the sign alternates as $x$ crosses each critical point. That alternation is a nice shortcut check — as long as none of the factors are repeated, the signs should alternate.

### Example 3

Determine the solution set of $2x^2 + x > 3$.

The comparison is not against zero yet, so move everything to one side. Subtract $3$ from both sides:

$$
2x^2 + x - 3 > 0
$$

Factor the quadratic. A quick trial with the factors of $-3 \cdot 2 = -6$ that add to $1$ gives $(2x + 3)(x - 1)$. Check: $(2x + 3)(x - 1) = 2x^2 - 2x + 3x - 3 = 2x^2 + x - 3$. Good.

The critical points come from $2x + 3 = 0$ (so $x = -\tfrac{3}{2}$) and $x - 1 = 0$ (so $x = 1$). The number line breaks into three intervals: $(-\infty, -\tfrac{3}{2})$, $(-\tfrac{3}{2}, 1)$, and $(1, \infty)$.

Test each interval in $(2x + 3)(x - 1)$:

- At $x = -2$: $(2(-2) + 3)((-2) - 1) = (-1)(-3) = 3 > 0$. Mark $(-\infty, -\tfrac{3}{2})$ as $+$.
- At $x = 0$: $(2(0) + 3)((0) - 1) = (3)(-1) = -3 < 0$. Mark $(-\tfrac{3}{2}, 1)$ as $-$.
- At $x = 2$: $(2(2) + 3)((2) - 1) = (7)(1) = 7 > 0$. Mark $(1, \infty)$ as $+$.

The inequality wants $> 0$, strictly. Keep the positive intervals, exclude the critical points. The solution is $x < -\tfrac{3}{2}$ or $x > 1$, or in interval notation $(-\infty, -\tfrac{3}{2}) \cup (1, \infty)$.

## Common pitfalls

- **Leaving something on the "wrong side."** If you try to sign-chart $x^2 + 2x$ against $3$ directly, the whole method falls apart, because sign charts read signs relative to zero only. Always rearrange to "polynomial $\diamond$ zero" before factoring.
- **Skipping a factor.** If you only partially factor (say, pull out an $x$ but leave a trinomial), you may miss a critical point and get the wrong sign pattern. Factor as completely as possible before building the chart.
- **Using brackets and parentheses inconsistently.** For non-strict inequalities ($\le$ or $\ge$), the critical points are part of the solution because the polynomial is zero there, and they should be written with square brackets. For strict inequalities ($<$ or $>$), the critical points are excluded and should be written with parentheses. Infinity is always paired with a parenthesis.
- **Testing the critical point itself.** A critical point makes the factored product equal to zero, which is neither positive nor negative, so it gives no useful information about the surrounding interval. Always test a value strictly inside an interval, never the boundary.
- **Assuming signs always alternate.** For polynomials with only distinct linear factors, the signs do alternate from interval to interval. But a repeated factor like $(x - 2)^2$ produces a sign that does **not** change as $x$ crosses $2$, because the factor is positive on both sides. Watch for multiplicity before relying on the alternation pattern.
- **Reversing the sign of the answer.** After you build a correct sign chart, make sure you pick the intervals whose sign matches the original comparison. If the problem says $< 0$, you want the negative intervals. It is easy to get the right chart and then pick the wrong intervals from it under time pressure.

## Problems Involving Polynomial Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polynomial_inequalities"></div>

## See Also

- [[Solving_Inequalities_In_One_Variable]]
- [[Factoring_Completely]]
- [[Polynomial_Basics]]
- [[Rational_Inequalities]]
- [[Compound_Inequalities]]
- [[Solving_Quadratics_By_Factoring]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
