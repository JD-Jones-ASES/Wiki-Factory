---
title: "Mathematical Induction"
type: topic
aliases: ["Induction", "Proof by Induction", "Mathematical Induction", "Principle of Mathematical Induction"]
tags: ["#branch-pre-calculus", "#topic-sequences-and-series"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "9", section: "9.2"}
related:
  - "topics/precalculus/Binomial"
  - "topics/precalculus/Summation"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Summation"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "Prove a statement for every positive integer by verifying a base case and a step-up rule."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Mathematical Induction

# Mathematical Induction

Some statements in math are claims about *every* positive integer at once — every counting number from $1$ forward. An example: the sum of the first $n$ positive integers equals $n(n+1)/2$. This is one statement that, if true, holds for $n = 1$ and $n = 2$ and $n = 100$ and $n = 1{,}000{,}000$ — infinitely many claims all rolled into one. You cannot verify it by checking every case; there are too many. **Induction** is the tool built for exactly this situation.

The idea is elegant. Instead of checking every $n$ on its own, you do two small jobs:

1. **Base case.** Show the statement is true for the smallest value of $n$ you care about — usually $n = 1$.
2. **Inductive step.** Show that *if* the statement happens to be true for some value $n = k$, *then* it must also be true for the next value $n = k + 1$.

Once both jobs are finished, the statement is proved for every $n$ from the base case up. The base case lights up $n = 1$. The inductive step then uses $n = 1$ to light up $n = 2$; it uses $n = 2$ to light up $n = 3$; it uses $n = 3$ to light up $n = 4$; and so on forever. Two steps together, infinitely many cases proved.

---

## The domino picture

The classic way to picture induction is a long row of dominoes. You want to know whether every domino in the row will fall. Two things have to be true:

- The first domino actually gets knocked over. (Base case.)
- Every standing domino is close enough to the next one that whenever a domino falls, it tips the next one over. (Inductive step.)

If both of those hold, you don't have to check dominoes $5$, $17$, or $1{,}000{,}000$ by hand. The combination is enough. Induction is that argument formalized: a base case to start the chain and a rule that pushes the chain forward one link at a time.

---

## The recipe

To prove a statement $P(n)$ is true for every integer $n \geq 1$:

1. **State** $P(n)$ clearly. Usually this is an equation or an inequality you want to verify.
2. **Check $P(1)$** — the base case. Plug in $n = 1$ on both sides and show the statement holds.
3. **Assume $P(k)$** is true for some unspecified integer $k \geq 1$. This is the **inductive hypothesis** — you are not claiming it's true for a specific $k$, you are using it as a temporary given.
4. **Prove $P(k+1)$** follows from $P(k)$. This is the inductive step. Start from the left side of $P(k+1)$, rearrange until you can swap in what the inductive hypothesis tells you, then simplify to the right side of $P(k+1)$.
5. **Conclude.** By the principle of mathematical induction, $P(n)$ holds for every integer $n \geq 1$.

Every induction proof follows the same scaffolding. Once you have walked through one or two, the structure becomes automatic — the only real work is the algebra in step 4.

---

## Example 1: the sum of the first n positive integers

> Prove that $1 + 2 + 3 + \cdots + n = \dfrac{n(n+1)}{2}$ for every integer $n \geq 1$.

Let $P(n)$ be the equation we are trying to prove.

**Base case ($n = 1$).** The left side is just $1$. The right side is $\dfrac{1 \cdot 2}{2} = 1$. Both sides equal $1$, so $P(1)$ is confirmed.

**Inductive hypothesis.** Suppose $P(k)$ is true for some integer $k \geq 1$. In plain form, this means we are assuming

$$
1 + 2 + 3 + \cdots + k = \dfrac{k(k+1)}{2}.
$$

**Inductive step.** We need to show $P(k+1)$ is true — that is, we need to show

$$
1 + 2 + 3 + \cdots + k + (k+1) = \dfrac{(k+1)(k+2)}{2}.
$$

Start with the left side. The first $k$ terms are the sum that appears in $P(k)$, so by the inductive hypothesis we can replace them:

$$
\underbrace{1 + 2 + \cdots + k}_{\text{= }\dfrac{k(k+1)}{2}\text{ by hypothesis}} + (k+1) = \dfrac{k(k+1)}{2} + (k+1).
$$

Combine the two terms over a common denominator of $2$:

$$
= \dfrac{k(k+1)}{2} + \dfrac{2(k+1)}{2} = \dfrac{k(k+1) + 2(k+1)}{2}.
$$

Factor $(k+1)$ out of the numerator:

$$
= \dfrac{(k+1)(k+2)}{2}.
$$

That is exactly the right side of $P(k+1)$. So assuming $P(k)$ made $P(k+1)$ come out. The inductive step is finished.

**Conclusion.** The base case $P(1)$ is true, and $P(k)$ implies $P(k+1)$. By induction, $P(n)$ holds for every integer $n \geq 1$. $\blacksquare$

Done. One base case, one clean inductive step, and an infinite family of statements is proved in less than half a page.

---

## Example 2: an inequality with a later base case

> Prove that $3^n > 100 n$ for every integer $n \geq 6$.

Not every induction proof starts at $n = 1$. Some statements only become true once $n$ is large enough, and you simply shift the base case. Here, you can check that $3^n > 100n$ fails for $n = 1, 2, \ldots, 5$, but it starts working at $n = 6$.

**Base case ($n = 6$).** $3^6 = 729$ and $100 \cdot 6 = 600$. Since $729 > 600$, $P(6)$ is true.

**Inductive hypothesis.** Assume $3^k > 100 k$ for some $k \geq 6$.

**Inductive step.** We want to show $3^{k+1} > 100(k+1)$. Use the fact that $3^{k+1} = 3 \cdot 3^k$, then swap in the inductive hypothesis:

$$
3^{k+1} = 3 \cdot 3^k > 3 \cdot 100 k = 300 k.
$$

So $3^{k+1}$ is bigger than $300 k$. Is $300 k$ big enough to also exceed $100(k+1)$? Check: $300 k \geq 100(k+1)$ is the same as $300 k \geq 100 k + 100$, which simplifies to $200 k \geq 100$, i.e. $k \geq 1/2$. Since our $k$ is at least $6$, that is obviously true. Chaining the pieces:

$$
3^{k+1} > 300 k \geq 100(k+1),
$$

so $3^{k+1} > 100(k+1)$, which is $P(k+1)$.

**Conclusion.** Base case verified at $n = 6$, and $P(k)$ implies $P(k+1)$. By induction, $3^n > 100 n$ for all $n \geq 6$. $\blacksquare$

Same recipe, different kind of claim. When you are proving an inequality rather than an equation, the inductive step usually ends with a chain of inequalities strung together rather than an equation reached by factoring.

---

## Example 3: why the base case really matters

Imagine someone asks you to prove $n = n + 1$ for every positive integer by induction. (Obviously false, but play along.) The inductive step can be "done" in a trick sort of way: assume $k = k + 1$, then add $1$ to both sides to get $k + 1 = k + 2$, which is the statement at $n = k + 1$. Step $k \to k + 1$ looks fine in isolation.

But $P(1)$ says $1 = 2$, which is obviously false. The base case fails, so the whole induction collapses. You never got the first domino to fall, so nothing that comes after can be trusted. The moral: both halves of an induction proof are required. A working inductive step without a base case is an argument that proves nothing at all.

---

## Common pitfalls

- **Forgetting to do the base case.** The inductive step alone proves nothing — you need an actual starting point. Always verify $P(1)$ (or whatever the first integer is) with a clean plug-in.
- **Assuming what you are trying to prove.** The inductive hypothesis is $P(k)$, not $P(k+1)$. If you write "assume the formula works for $k+1$," you have assumed what you are trying to prove, and the argument is circular.
- **Confusing the hypothesis with the goal.** During the inductive step, $P(k)$ is a *given* you get to use for free, and $P(k+1)$ is what you need to *derive*. Keep the two roles straight.
- **Algebra slips in the inductive step.** Most broken proofs come from arithmetic errors, not conceptual ones. Double-check every factoring, every common denominator, and every distribution.
- **Starting at the wrong base case.** Some statements are only true from $n = 2$ or $n = 6$ onward. If the problem says "for $n \geq 6$," the base case is $n = 6$, not $n = 1$.

---

## Prerequisites

Induction plays well with:

- [[Summation]] — many induction exercises prove formulas for sums.
- [[Variables_And_Algebraic_Expressions]] — the inductive step lives or dies on your ability to manipulate algebraic expressions with a variable index.

Once you have induction in your pocket, try using it to prove the [[Binomial]] theorem, which is the standard follow-up application.

---

## Problems Involving Mathematical Induction

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="induction"></div>

---

## See Also

- [[Binomial]]
- [[Summation]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
