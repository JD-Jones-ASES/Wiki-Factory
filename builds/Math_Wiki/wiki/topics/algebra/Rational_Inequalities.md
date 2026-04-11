---
title: "Rational Inequalities"
type: topic
aliases: ["Sign Chart Method for Rational Inequalities"]
tags: ["#branch-algebra-2", "#topic-rational-expressions", "#topic-inequalities", "#skill-algebraic-manipulation", "#skill-multi-step", "#key-technique", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Polynomial_Inequalities"
  - "topics/algebra/Rational_Equations_And_Applications"
  - "topics/algebra/Graphs_Of_Rational_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Solving_Inequalities_In_One_Variable"
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Solving_Rational_Equations"
problem_type_ids: []
figures: []
summary: "Rearrange so the comparison is against zero, then sign-chart the numerator and denominator together — without ever multiplying both sides by the denominator."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Rational Inequalities

# Rational Inequalities

A **rational inequality** is an inequality whose expression is a quotient of polynomials — a fraction with an $x$ in the denominator — compared against zero (or something that can be rearranged to look that way). A typical one looks like $\dfrac{x+2}{x-3} \le 0$, or maybe $\dfrac{x^2 - 1}{x + 4} > 0$. These problems have the same spirit as [[Polynomial_Inequalities]]: find every $x$ for which the expression has the right sign, sketch a sign chart, and read off the answer as a union of intervals. But rational inequalities carry one critical complication that polynomial inequalities do not: the denominator can be zero. Values of $x$ that make the denominator zero are **never** part of the solution, because the expression is undefined there. They still go on the sign chart, though — just as locations where something interesting happens — because the sign of the whole expression can flip across them.

There is one more trap that needs a warning up front, before the procedure. The temptation to "clear the denominator" by multiplying both sides by $x - 3$ (or whatever the denominator is) feels natural and is completely wrong. Multiplying both sides of an inequality by an expression with an unknown sign is risky — when that expression is negative, it reverses the comparison, and you cannot tell in advance whether $x - 3$ is positive or negative without already solving the problem. So rational inequalities are never cleared by multiplying across. The correct move is to rearrange the inequality so one side is zero, combine into a single fraction, and then run the sign chart.

## What it means

A rational inequality takes one of the four standard comparison forms:

$$
\frac{P(x)}{Q(x)} > 0, \qquad \frac{P(x)}{Q(x)} < 0, \qquad \frac{P(x)}{Q(x)} \ge 0, \qquad \frac{P(x)}{Q(x)} \le 0.
$$

The sign of the fraction depends on the signs of $P(x)$ and $Q(x)$. A positive over a positive is positive. A negative over a negative is positive. A positive over a negative (or negative over positive) is negative. Zero in the numerator gives the fraction a value of zero. And zero in the denominator makes the fraction undefined — those inputs are excluded from the domain entirely, and the expression has no value there at all.

This means the **critical points** of a rational inequality come from two sources, and they play different roles:

- **Zeros of the numerator.** At these points the expression equals zero. They are included in the solution for $\ge$ or $\le$ problems (closed bracket), and excluded for $>$ or $<$ problems (open parenthesis).
- **Zeros of the denominator.** At these points the expression is undefined. They are **always** excluded — no matter what comparison symbol appears — and are always drawn with an open parenthesis. The expression cannot have any sign there because it does not exist.

A small example makes this concrete. Consider $\dfrac{x + 2}{x - 3} \le 0$. The numerator is zero at $x = -2$, and the denominator is zero at $x = 3$. Testing signs shows the expression is negative on the interval between them. The answer is:

$$
\frac{x + 2}{x - 3} \le 0 \quad\Longleftrightarrow\quad x \in [-2, 3)
$$

The left endpoint $-2$ gets a square bracket because the numerator is zero there (and the inequality is non-strict). The right endpoint $3$ gets a parenthesis because the denominator is zero there — the expression is undefined, so $3$ is off-limits no matter what the comparison symbol says.

## How it works

The method is a careful cousin of the polynomial version:

1. **Rearrange so one side is zero.** If the problem is $\dfrac{2x}{x - 1} \ge 1$, subtract $1$ from both sides: $\dfrac{2x}{x - 1} - 1 \ge 0$. Do **not** multiply both sides by the denominator. The rearrangement is always safe; the multiplication is not.
2. **Combine into a single fraction.** Use a common denominator to merge the two pieces of the left side into one. In the example above, $\dfrac{2x}{x - 1} - 1 = \dfrac{2x - (x - 1)}{x - 1} = \dfrac{x + 1}{x - 1}$. Now the inequality reads $\dfrac{x + 1}{x - 1} \ge 0$.
3. **Factor the numerator and denominator completely.** Treat them as separate polynomials. Every factoring tool from [[Factoring_Completely]] still applies.
4. **Find every critical point.** List the zeros of the numerator and the zeros of the denominator. Mark them as "included-candidate" or "excluded-always" so you do not lose track when you write the final answer.
5. **Build a sign chart.** Plot every critical point on a number line. In each interval between critical points, pick a test value and substitute into the factored form of the fraction. Record the sign of the result above that interval.
6. **Read off the solution.** Keep the intervals whose sign matches the comparison. For $\ge$ or $\le$, include the numerator zeros (closed bracket). For $>$ or $<$, exclude them (open parenthesis). The denominator zeros are always excluded, always open parenthesis. Write the answer in interval notation.

## Why it works

The same continuity argument that backs polynomial inequalities is still doing the heavy lifting. Between two consecutive critical points, neither the numerator nor the denominator can change sign — they are continuous polynomials with no zeros in that stretch — so their ratio also has a constant sign across the whole interval. Testing one point per interval pins the sign down. What is new is that the denominator can be zero, and at those points the ratio is not merely positive or negative — it is undefined. The denominator zeros still belong on the sign chart as "barriers" where the sign can change, but they are not candidates for membership in the solution set. The procedural rule that a denominator zero always gets an open parenthesis is really a restatement of "you cannot divide by zero." No algebra trick will rescue that point; it is permanently out of play.

## Worked examples

### Example 1

Express the solution set of $\dfrac{x + 2}{x - 3} \le 0$ in interval notation.

One side is already zero. The fraction is already factored — numerator $x + 2$ and denominator $x - 3$. Critical points are the zero of the numerator, $x = -2$, and the zero of the denominator, $x = 3$. The $-2$ is an "included-candidate" because the inequality is $\le$; the $3$ is "excluded-always" because the denominator is zero there.

The number line breaks into three intervals: $(-\infty, -2)$, $(-2, 3)$, and $(3, \infty)$. Test a value in each:

- At $x = -3$: $\dfrac{-3 + 2}{-3 - 3} = \dfrac{-1}{-6} = \dfrac{1}{6} > 0$. Mark $(-\infty, -2)$ as $+$.
- At $x = 0$: $\dfrac{0 + 2}{0 - 3} = \dfrac{2}{-3} < 0$. Mark $(-2, 3)$ as $-$.
- At $x = 4$: $\dfrac{4 + 2}{4 - 3} = \dfrac{6}{1} = 6 > 0$. Mark $(3, \infty)$ as $+$.

The inequality wants $\le 0$, so keep the negative intervals and include the numerator zero (because $\le$ is non-strict) but exclude the denominator zero (always). The solution is $-2 \le x < 3$, or in interval notation $[-2, 3)$. Notice the bracket on $-2$ and the parenthesis on $3$ — that asymmetry is the whole story.

### Example 2

Give every real $x$ satisfying $\dfrac{x - 4}{x + 1} > 0$.

One side is already zero. The fraction is already factored. Critical points: numerator zero at $x = 4$, denominator zero at $x = -1$. Both are "excluded-always" for different reasons — $4$ because the inequality is strict $>$ (which excludes the numerator zero), and $-1$ because the denominator is zero (which is always excluded).

Intervals: $(-\infty, -1)$, $(-1, 4)$, $(4, \infty)$. Test each:

- At $x = -2$: $\dfrac{-2 - 4}{-2 + 1} = \dfrac{-6}{-1} = 6 > 0$. Mark $(-\infty, -1)$ as $+$.
- At $x = 0$: $\dfrac{0 - 4}{0 + 1} = \dfrac{-4}{1} = -4 < 0$. Mark $(-1, 4)$ as $-$.
- At $x = 5$: $\dfrac{5 - 4}{5 + 1} = \dfrac{1}{6} > 0$. Mark $(4, \infty)$ as $+$.

The inequality wants $> 0$, so keep the positive intervals. Both critical points are excluded. The solution is $x < -1$ or $x > 4$, or in interval notation $(-\infty, -1) \cup (4, \infty)$.

### Example 3

Determine the solution set of $\dfrac{2x}{x - 1} \ge 1$.

This one is not yet in "fraction compared to zero" form. Subtract $1$ from both sides **without** multiplying anything across:

$$
\frac{2x}{x - 1} - 1 \ge 0
$$

Combine into a single fraction using $x - 1$ as the common denominator. Rewrite the $1$ as $\dfrac{x - 1}{x - 1}$:

$$
\frac{2x}{x - 1} - \frac{x - 1}{x - 1} = \frac{2x - (x - 1)}{x - 1} = \frac{x + 1}{x - 1}
$$

So the inequality becomes:

$$
\frac{x + 1}{x - 1} \ge 0
$$

Critical points: numerator zero at $x = -1$ (included-candidate, because $\ge$ is non-strict) and denominator zero at $x = 1$ (always excluded). Intervals: $(-\infty, -1)$, $(-1, 1)$, $(1, \infty)$. Test each:

- At $x = -2$: $\dfrac{-2 + 1}{-2 - 1} = \dfrac{-1}{-3} = \dfrac{1}{3} > 0$. Mark $(-\infty, -1)$ as $+$.
- At $x = 0$: $\dfrac{0 + 1}{0 - 1} = \dfrac{1}{-1} = -1 < 0$. Mark $(-1, 1)$ as $-$.
- At $x = 2$: $\dfrac{2 + 1}{2 - 1} = \dfrac{3}{1} = 3 > 0$. Mark $(1, \infty)$ as $+$.

Keep the positive intervals, include $-1$ (numerator zero, non-strict), exclude $1$ (denominator zero). The solution is $x \le -1$ or $x > 1$, or in interval notation $(-\infty, -1] \cup (1, \infty)$. Note again the asymmetry: a square bracket on $-1$, a parenthesis on $1$.

## Common pitfalls

- **Multiplying both sides by the denominator.** This is the single biggest mistake and the reason this topic gets its own page. When the denominator has an unknown sign, multiplying across may or may not reverse the comparison, and you cannot know which until you have already solved the problem. Always rearrange and combine into a single fraction instead — never clear the denominator.
- **Forgetting that the denominator zeros are off-limits.** Even when the original inequality is $\ge$ or $\le$, any $x$ that makes the denominator zero is excluded from the solution. These points always get open parentheses in the final interval notation, because the expression is undefined there.
- **Treating the numerator zero and the denominator zero the same way.** Numerator zeros are sometimes included (for non-strict inequalities) and sometimes excluded (for strict ones). Denominator zeros are always excluded. Keep these roles labeled on the sign chart so they do not get confused at the end.
- **Not getting a common denominator before factoring.** If the rearrangement leaves you with $\dfrac{2x}{x - 1} - 1 \ge 0$, you cannot sign-chart that directly — it is not yet in "single fraction vs zero" form. Combine it into one fraction first.
- **Testing a critical point.** A critical point makes the expression zero or undefined, neither of which tells you anything about the surrounding interval. Always test a value strictly inside an interval.
- **Dropping an interval from the answer.** When the solution involves two or more disconnected intervals, write all of them with a union symbol $\cup$. Forgetting the second piece is a common under-time-pressure error.

## Problems Involving Rational Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="rational_inequalities"></div>

## See Also

- [[Solving_Inequalities_In_One_Variable]]
- [[Simplifying_Rational_Expressions]]
- [[Solving_Rational_Equations]]
- [[Polynomial_Inequalities]]
- [[Rational_Equations_And_Applications]]
- [[Graphs_Of_Rational_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
