---
title: "Real Zeros of Polynomials"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-polynomials", "#topic-functions", "#skill-multi-step", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Graphs_Of_Polynomials"
  - "topics/precalculus/Real_Zeros_Of_Polynomials_Advanced"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/precalculus/Complex_Zeros"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Factoring_Completely"
  - "topics/precalculus/Graphs_Of_Polynomials"
problem_type_ids: []
figures: []
summary: "When factoring fails outright, the Rational Zeros Theorem hands you a finite candidate list to test with synthetic division — reducing an infinite search for roots to a short arithmetic checklist."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Real Zeros of Polynomials

# Real Zeros of Polynomials

Finding the zeros of a quadratic is a one-step job: apply the quadratic formula and you are done. For cubics, quartics, and higher-degree polynomials there is no such convenient closed-form escape hatch — and even when a general formula does exist (as it does for cubics and quartics), it is too unwieldy to use in practice. Instead, precalculus teaches a two-step strategy that works for most textbook polynomials:

1. **Narrow the search.** Use the **Rational Zeros Theorem** to produce a short list of candidate rational numbers that *might* be zeros.
2. **Test the list.** Use **synthetic division** to check each candidate efficiently, and whenever a candidate is a zero, use the resulting quotient to break the polynomial into a smaller piece you can keep factoring.

If after you have tried every rational candidate the remaining quotient is a quadratic (or lower), finish the job with the quadratic formula. This combination reliably cracks any polynomial whose zeros are a mix of rational numbers and simple irrationals — which covers nearly every polynomial you will see in a precalculus textbook.

---

## Why the Rational Zeros Theorem works

Here is the theorem in a single sentence: if $p(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{1}x + a_{0}$ has **integer coefficients**, and a rational number $p/q$ (in lowest terms) is a zero of $p(x)$, then $p$ must divide the constant term $a_{0}$ and $q$ must divide the leading coefficient $a_{n}$.

The payoff is enormous. Without the theorem, any rational number in $\mathbb{Q}$ could in principle be a zero — an infinite search. With the theorem, only the finitely many fractions built from $\text{(factor of } a_{0}\text{)} / \text{(factor of } a_{n}\text{)}$ qualify, and that list is usually quite short. For a polynomial with $a_{0} = 6$ and $a_{n} = 2$, the factors of $6$ are $\{1, 2, 3, 6\}$ and the factors of $2$ are $\{1, 2\}$, giving the candidate list

$$
\pm 1,\; \pm 2,\; \pm 3,\; \pm 6,\; \pm \tfrac{1}{2},\; \pm \tfrac{3}{2}.
$$

Twelve candidates, no more, no less. If the polynomial has any rational zeros at all, they must come from this list. If none of the candidates check out, you know with certainty the polynomial has no rational zeros, and you move on to numerical or irrational techniques.

Two quick notes on the mechanics. First, include both the positive and the negative of each fraction — the theorem's fraction $p/q$ allows any sign. Second, eliminate duplicates: $2/2$ and $1/1$ are the same number, so only list $1$ once. A clean candidate list is sorted and deduplicated.

---

## Testing candidates with synthetic division

Once you have the candidate list, you need an efficient way to test each one. Plugging numbers into the polynomial directly works but is slow, especially for higher degrees. **Synthetic division** is the same test dressed up as a much faster arithmetic routine.

The idea: if $r$ is a zero of $p(x)$, then $(x - r)$ is a factor, so dividing $p(x)$ by $(x - r)$ gives a remainder of $0$. Synthetic division performs that division using only the coefficients of $p$ and the test value $r$, producing both the quotient and the remainder in one short table. When the remainder comes out $0$, you know $r$ is a zero, *and* the coefficients of the quotient are sitting right in front of you — ready to be used as a smaller polynomial to factor further.

A synthetic division tableau for dividing $p(x) = 2x^{3} - 5x^{2} + x + 2$ by $(x - r)$ looks like this:

$$
\begin{array}{c|cccc}
r & 2 & -5 & 1 & 2 \\
  &   & 2r & (\cdot) & (\cdot) \\
\hline
  & 2 & (\cdot) & (\cdot) & (\cdot)
\end{array}
$$

The rules are simple. Bring down the leading coefficient. Multiply by $r$, write the result under the next coefficient, and add. Repeat across the row. The last number in the bottom row is the remainder; the rest of the bottom row gives the coefficients of the quotient polynomial, which has degree one less than the dividend.

---

## The full workflow

Combining the two tools, the standard strategy for finding all real zeros of a polynomial is:

1. **List candidates** using the Rational Zeros Theorem.
2. **Synthetic-divide** by each candidate one at a time. The moment you hit a candidate with remainder $0$, stop and note that value as a confirmed zero.
3. **Factor the polynomial** as $(x - r) \cdot q(x)$, where $q(x)$ is the quotient from the successful synthetic division.
4. **Repeat** the whole process on $q(x)$, using its (usually shorter) candidate list.
5. **Stop** when $q(x)$ reduces to a quadratic (or linear, or constant). Finish with the quadratic formula or direct factoring.

Every successful division brings the degree down by one, so the process is guaranteed to terminate. Over three or four rounds a nightmare degree-$5$ polynomial collapses into a linear factor times a quadratic, and the quadratic formula takes it the rest of the way.

---

## Example 1: Listing candidate rational roots of $2x^{3} - 5x^{2} + x + 2 = 0$

> List every candidate rational root for $f(x) = 2x^{3} - 5x^{2} + x + 2$.

Apply the Rational Zeros Theorem with $a_{0} = 2$ and $a_{n} = 2$. The factors of the constant term $2$ are $\{1, 2\}$, and the factors of the leading coefficient $2$ are also $\{1, 2\}$.

The candidate set is all fractions $\pm \dfrac{\text{factor of } 2}{\text{factor of } 2}$:

$$
\pm \frac{1}{1},\; \pm \frac{2}{1},\; \pm \frac{1}{2},\; \pm \frac{2}{2}.
$$

After reducing and removing duplicates (note that $\pm 2/2 = \pm 1$, which is already in the list):

$$
\text{Candidates: } \; 1,\; -1,\; 2,\; -2,\; \tfrac{1}{2},\; -\tfrac{1}{2}.
$$

Six candidates total. Every rational zero of $f$, if any, must be one of these six numbers. The next step — finding out which of them actually are zeros — happens in Example 2.

---

## Example 2: Finding the actual rational roots

> Using the candidate list from Example 1, find every actual rational zero of $f(x) = 2x^{3} - 5x^{2} + x + 2$.

Test the candidates one at a time by synthetic division. Start with $r = 1$:

$$
\begin{array}{c|cccc}
1 & 2 & -5 & 1 & 2 \\
  &   & 2 & -3 & -2 \\
\hline
  & 2 & -3 & -2 & 0
\end{array}
$$

The final remainder is $0$, so $x = 1$ **is** a zero of $f$. And the quotient coefficients $2, -3, -2$ tell you that

$$
f(x) = (x - 1)(2x^{2} - 3x - 2).
$$

Check this by multiplying out mentally — the degrees match, and the leading term $2x^{3}$ and constant term $(-1)(-2) = 2$ both match $f$.

Now you only need to find the rational zeros of the remaining quadratic $q(x) = 2x^{2} - 3x - 2$. You could run the Rational Zeros Theorem again on $q(x)$, but factoring directly works faster here:

$$
2x^{2} - 3x - 2 = (2x + 1)(x - 2).
$$

Setting each factor to zero gives the remaining rational zeros $x = -\tfrac{1}{2}$ and $x = 2$. So the full set of rational zeros of $f$ is

$$
x = 1, \quad x = -\tfrac{1}{2}, \quad x = 2.
$$

All three showed up on the candidate list from Example 1 — which is the Rational Zeros Theorem working exactly as advertised.

---

## Example 3: Full factorization via division

> Use the zero $x = 1$ from Example 2 to fully factor $f(x) = 2x^{3} - 5x^{2} + x + 2$ into linear factors.

You already have the first factor from the synthetic division:

$$
f(x) = (x - 1) \cdot (2x^{2} - 3x - 2).
$$

The quadratic $2x^{2} - 3x - 2$ was factored in Example 2 as $(2x + 1)(x - 2)$. Substituting gives the complete factorization over the rationals:

$$
f(x) = (x - 1)(2x + 1)(x - 2).
$$

Every real zero of $f$ is visible on the right-hand side. The three zeros are $x = 1$ (from the first factor), $x = -\tfrac{1}{2}$ (from the second factor), and $x = 2$ (from the third). Because $f$ is degree $3$, it has at most three real zeros, so this factorization is complete — there is nothing left to find. If you were asked to sketch the graph of $f$, you would now know the $x$-intercepts exactly, the end behavior (odd degree, positive leading coefficient, so falls to the lower-left and rises to the upper-right), and the $y$-intercept ($f(0) = 2$). That is more than enough for a confident hand-sketch.

---

## Common pitfalls

- **Forgetting to list both signs.** A candidate like $3$ always travels with its partner $-3$. If you only list positive candidates, you miss half the zeros.
- **Skipping the duplicate cleanup.** If the constant term is $2$ and the leading coefficient is $2$, then $2/2 = 1$ and $1/1 = 1$ produce the same candidate. Write the candidate list once, check each value once.
- **Not lowering the degree after a hit.** When synthetic division turns up a zero, the real work is only half done — you still need to take the quotient and factor it further, because there may be additional zeros hidden inside.
- **Applying the theorem to non-integer coefficients.** The Rational Zeros Theorem requires the polynomial to have **integer** coefficients. If your polynomial has $\tfrac{1}{2}$ or $\sqrt{3}$ sitting among the coefficients, the theorem does not apply — clear the fractions first by multiplying through, or use a different tool.
- **Believing the candidate list must contain a zero.** The theorem only says that **if** a rational zero exists, it is on the list. A polynomial can have zero rational zeros (for example, all irrational or all complex), and in that case every candidate on the list will fail. The theorem is about narrowing the search, not guaranteeing success.

---

## Prerequisites

- [[Polynomial_Functions_And_Graphs]] — the algebra-2 baseline for polynomials, degree, zeros, and multiplicity
- [[Factoring_Completely]] — the follow-up step once you have peeled off a linear factor via synthetic division
- [[Graphs_Of_Polynomials]] — connects the zeros you find here to the shape of the graph

---

## Problems Involving Real Zeros of Polynomials

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="real_zeros_of_polynomials"></div>

---

## See Also

- [[Real_Zeros_Of_Polynomials_Advanced]] — the next step, adding sign-change rules and bounds to narrow the candidate list further
- [[Graphs_Of_Polynomials]] — where the zeros you find here become the $x$-intercepts of the graph
- [[Factoring_Completely]] — the broader toolkit for breaking polynomials apart
- [[Polynomial_Functions_And_Graphs]] — the algebra-2 foundation
- [[Complex_Zeros]] — what to do when the remaining quotient has no real zeros
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
