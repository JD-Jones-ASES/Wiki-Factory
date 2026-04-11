---
title: "Sequences"
type: topic
aliases: ["Arithmetic Progression", "Geometric Progression", "Infinite Geometric Series"]
tags: ["#branch-algebra-2", "#topic-sequences-and-series", "#key-topic", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "4", section: "4.5"}
  - {book: "algtrig", chapter: "9", section: "9.3"}
related:
  - "topics/pre_algebra/Arithmetic_Sequences_And_Linear_Patterns"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Exponential_Functions"
  - "topics/precalculus/Summation"
  - "topics/algebra/Function_Basics"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Properties_Of_Exponents"
problem_type_ids: []
figures: []
summary: "Arithmetic and geometric sequences, their explicit formulas, finite sums, and the convergence of an infinite geometric series."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Sequences

# Sequences

A **sequence** is a list of numbers written in a definite order. The first entry is called $a_1$, the second $a_2$, and the entry in the $n$th slot is written $a_n$. You are really looking at a function whose input is a natural number and whose output is the number that lives in that slot — in other words, $a : \mathbb{N} \to \mathbb{R}$ with $a(n) = a_n$. This "function with an integer input" framing is the whole reason sequences fit naturally alongside the other function families you have been studying.

Two families of sequences matter so much that they dominate the rest of the chapter. In one family, you get from one term to the next by **adding** a fixed number. In the other, you get from one term to the next by **multiplying** by a fixed number. Those two families are the arithmetic sequences and the geometric sequences, and they will feel familiar quickly: the first behaves like a [[Linear_Functions|linear function]], and the second behaves like an [[Exponential_Functions|exponential function]], only with their domains cut down to the positive integers.

---

## Arithmetic sequences

An **arithmetic sequence** is a list in which every pair of neighbors differs by the same number. That fixed gap is called the **common difference** and is denoted $d$:

$$
d = a_{n+1} - a_n \qquad \text{for every } n \geq 1.
$$

Because climbing from the first term to the $n$th term takes exactly $n - 1$ jumps of size $d$, you can reach any term you like in a single line of algebra. The result is the **$n$th-term formula for an arithmetic sequence**:

$$
a_n = a_1 + (n - 1)d.
$$

If you expand and collect, this can be rewritten as $a_n = dn + (a_1 - d)$. Those are exactly the ingredients of a line with slope $d$ and intercept $a_1 - d$. Plotting the points $(n, a_n)$ on a grid produces a perfectly straight dotted pattern — the same picture as [[Linear_Functions|$f(x) = mx + b$]], only sampled at the integers.

### Summing the first $n$ terms

One of the most useful facts about an arithmetic sequence is that you can sum any finite stretch of it with a single formula. Pair up the terms: the first with the last, the second with the second-to-last, and so on. Each pair has the same total, $a_1 + a_n$. If there are $n$ terms in all, you end up with $n/2$ such pairs, and the grand total is

$$
S_n = \dfrac{n(a_1 + a_n)}{2}.
$$

A useful alternate form comes from substituting $a_n = a_1 + (n - 1)d$ into the box above:

$$
S_n = \dfrac{n}{2}\left(2a_1 + (n - 1)d\right).
$$

Use whichever form is more convenient. If you already know $a_n$, the first version is faster; if you only have $a_1$ and $d$, the second version saves a step.

---

## Geometric sequences

A **geometric sequence** is a list where you move from one term to the next by multiplying by a fixed nonzero number. That multiplier is called the **common ratio** and is denoted $r$:

$$
r = \dfrac{a_{n+1}}{a_n} \qquad \text{for every } n \geq 1.
$$

Going from $a_1$ to $a_n$ now takes $n - 1$ multiplications by $r$, which gives the **$n$th-term formula for a geometric sequence**:

$$
a_n = a_1 \cdot r^{\,n-1}.
$$

The connection to the exponential family is just as clean as the arithmetic–linear link. If you let $x = n$, the formula reads $a(x) = a_1 \cdot r^{\,x-1}$, which is an exponential function of $x$ — a [[Exponential_Functions|$b^x$-style machine]] viewed only at integer inputs. If $r > 1$, the terms climb faster and faster; if $0 < r < 1$, the terms shrink toward zero; and if $r < 0$, the terms alternate between positive and negative while their sizes behave like a decay or growth pattern depending on $|r|$.

### Summing the first $n$ terms

A finite geometric sum has a neat closed form too, although the derivation is different. If you call the total $S_n$ and then multiply both sides by $r$, most of the terms cancel in the subtraction $S_n - rS_n$. The result is

$$
S_n = \dfrac{a_1(1 - r^n)}{1 - r} \qquad (r \neq 1).
$$

When $r = 1$ every term equals $a_1$, so $S_n = n a_1$ by direct counting. The $r \neq 1$ restriction in the box is there because the denominator $1 - r$ would otherwise be zero.

### Infinite geometric series

Here is where geometric sequences do something arithmetic sequences never can: if the common ratio is small enough in size, you can add up **infinitely many** terms and still get a finite answer. The phrase to memorize is **"the ratio must be strictly between $-1$ and $1$."** In symbols,

$$
|r| < 1 \quad\Longrightarrow\quad S_\infty = \dfrac{a_1}{1 - r}.
$$

The quickest way to see why this works is to stare at the finite-sum formula and imagine $n$ growing larger and larger. If $|r| < 1$, then $r^n$ is shrinking toward zero, so the numerator $a_1(1 - r^n)$ approaches $a_1$, and the sum approaches $a_1 / (1 - r)$. If $|r| \geq 1$, the terms of the sequence do not shrink at all (they either stay the same size or grow), the partial sums run off to infinity, and the infinite series is simply **not defined** — mathematicians say the series **diverges**. This convergence cutoff is the single most important fact about infinite geometric series, and it is tested constantly.

---

## Recursive versus explicit formulas

Every sequence can be described in at least two different ways. A **recursive** rule tells you how to get the next term from the previous one, together with a starting value. For an arithmetic sequence the recursion is $a_1 = \text{(given)}$ and $a_{n+1} = a_n + d$. For a geometric sequence it is $a_1 = \text{(given)}$ and $a_{n+1} = r \cdot a_n$. Recursive rules are intuitive — they describe what the sequence is "doing" step by step — but they are slow to use when you want a term far down the list, because you have to crawl through every term in between.

An **explicit** formula, by contrast, hands you any term you ask for in a single substitution. Both $a_n = a_1 + (n - 1)d$ and $a_n = a_1 r^{n-1}$ are explicit formulas. In practice you will use the recursive description to understand what the sequence looks like and the explicit formula to compute large-index terms without burning time.

---

## Example 1: arithmetic versus geometric versus neither

> Decide whether each of the following is arithmetic, geometric, or neither. If it is arithmetic, state $d$; if it is geometric, state $r$; if it is neither, say so.
>
> (a) $8, 14, 20, 26, 32, \ldots$
> (b) $3, 12, 48, 192, 768, \ldots$
> (c) $1, 4, 9, 16, 25, \ldots$
> (d) $81, -27, 9, -3, 1, \ldots$

Always run the two tests in order: first check whether the differences are constant, then check whether the ratios are constant.

For (a): differences are $6, 6, 6, 6$ — all equal. This is **arithmetic** with $d = 6$.

For (b): differences are $9, 36, 144, \ldots$ — not constant, so this is not arithmetic. Ratios: $12/3 = 4$, $48/12 = 4$, $192/48 = 4$, $768/192 = 4$. All equal, so this is **geometric** with $r = 4$.

For (c): differences are $3, 5, 7, 9$ — growing, so not arithmetic. Ratios: $4/1 = 4$, $9/4 = 2.25$, $16/9 \approx 1.78$ — not constant either, so not geometric. These are the perfect squares, so the sequence is **neither** arithmetic nor geometric. (The differences *themselves* form an arithmetic sequence, which is a fun observation, but that does not turn the original list into either of the two main types.)

For (d): differences are $-108, 36, -12, 4$ — not constant. Ratios: $-27/81 = -\tfrac{1}{3}$, $9/(-27) = -\tfrac{1}{3}$, $-3/9 = -\tfrac{1}{3}$, $1/(-3) = -\tfrac{1}{3}$. All equal, so this is **geometric** with $r = -\tfrac{1}{3}$. The negative ratio is what causes the signs to alternate.

---

## Example 2: finding a formula from two terms

> An arithmetic sequence has $a_4 = 19$ and $a_{10} = 49$. Determine the common difference, the first term, the explicit formula for $a_n$, and the sum of the first $20$ terms.

The trick to "given two terms" problems is to realize that going from one term to another takes a known number of jumps. Moving from the fourth term to the tenth term is $10 - 4 = 6$ jumps of size $d$, so:

$$
a_{10} - a_4 = 6d \quad\Longrightarrow\quad 49 - 19 = 6d \quad\Longrightarrow\quad d = 5.
$$

Now back-solve for $a_1$ using the explicit formula with the fourth term:

$$
19 = a_1 + (4 - 1)(5) = a_1 + 15 \quad\Longrightarrow\quad a_1 = 4.
$$

Write the formula:

$$
a_n = 4 + (n - 1)(5) = 5n - 1.
$$

Quick spot checks: $a_4 = 5(4) - 1 = 19$ and $a_{10} = 5(10) - 1 = 49$. Both match the given values. For the sum of the first twenty terms, first compute $a_{20} = 5(20) - 1 = 99$, then apply the arithmetic-sum formula:

$$
S_{20} = \dfrac{20 \cdot (a_1 + a_{20})}{2} = \dfrac{20 \cdot (4 + 99)}{2} = \dfrac{20 \cdot 103}{2} = 1030.
$$

The first twenty terms add to $1030$.

---

## Example 3: a finite geometric sum and an infinite one

> Consider the geometric sequence with $a_1 = 8$ and $r = \tfrac{1}{2}$. Compute the sum of the first $10$ terms, then decide whether the infinite series converges. If it does, find the total.

First, write down the explicit formula just to make sure you are working with the right sequence: $a_n = 8 \cdot (\tfrac{1}{2})^{n-1}$. The first few terms are $8, 4, 2, 1, \tfrac{1}{2}, \ldots$ — the terms are shrinking because $|r| < 1$.

For the finite sum of the first $10$ terms, plug into the geometric sum formula:

$$
S_{10} = \dfrac{8 \cdot \left(1 - (\tfrac{1}{2})^{10}\right)}{1 - \tfrac{1}{2}}.
$$

Compute $(\tfrac{1}{2})^{10} = \tfrac{1}{1024}$, so the numerator becomes $8 \cdot \tfrac{1023}{1024} = \tfrac{8184}{1024}$, and dividing by $1 - \tfrac{1}{2} = \tfrac{1}{2}$ multiplies by $2$:

$$
S_{10} = 2 \cdot \dfrac{8184}{1024} = \dfrac{16368}{1024} = \dfrac{1023}{64} \approx 15.98.
$$

For the infinite series, check the convergence condition: $|r| = \tfrac{1}{2}$ is strictly less than $1$, so the series converges. Use $S_\infty = a_1 / (1 - r)$:

$$
S_\infty = \dfrac{8}{1 - \tfrac{1}{2}} = \dfrac{8}{\tfrac{1}{2}} = 16.
$$

Notice that $S_{10} \approx 15.98$ is already extremely close to the infinite total of $16$ — the terms are shrinking so fast that after only ten terms you are within a hundredth of the limit. That behavior is typical: once $|r|$ is small, the partial sums sneak up on $S_\infty$ surprisingly quickly.

If instead the ratio had been $r = 2$, the infinite series $8 + 16 + 32 + 64 + \cdots$ would **diverge** because $|r| = 2 \geq 1$. The terms keep growing, the partial sums run off to infinity, and there is no finite total to speak of.

---

## A note on compound interest

Geometric sequences turn up immediately in any "multiply by the same factor each step" situation. If you deposit \$1{,}000 in an account paying $6\%$ annual interest, compounded once a year, then after one year the balance is $1{,}000 \cdot 1.06$, after two years it is $1{,}000 \cdot (1.06)^2$, and after $n$ years it is

$$
a_n = 1000 \cdot (1.06)^{\,n-1}
$$

if you number the starting balance as the first term. The common ratio is the multiplier $1.06$, and the sequence grows exponentially — a direct application of [[Exponential_Functions]] through the lens of a geometric sequence. Similar reasoning drives population growth, radioactive decay, drug dosage tracking, and countless other real-world models.

---

## Common pitfalls

- **Mistaking "close to constant" for constant.** The sequence $2, 4, 7, 11, 16, \ldots$ has differences $2, 3, 4, 5$ — not constant, so it is not arithmetic, even though the gaps *look* regular. Always confirm that every difference (or ratio) is exactly the same before committing.
- **Forgetting the $-1$ in the exponent.** The formula is $a_n = a_1 r^{\,n-1}$, not $a_1 r^n$. Slipping the exponent by one is the number-one error in geometric-sequence problems.
- **Ignoring the convergence condition for an infinite series.** $S_\infty = a_1 / (1 - r)$ is only valid when $|r| < 1$. Applying it blindly to a divergent series (say, $r = 2$) will give you a finite number that has no meaning.
- **Mixing up $n$ (the term number) with $a_n$ (the term value).** $a_{20}$ is the twentieth term, not the term whose value equals $20$. If a problem asks "which term equals $-50$?", you set $a_n = -50$ and solve for $n$, not the other way around.
- **Assuming every sequence is one of the two main types.** Many perfectly natural sequences — the Fibonacci numbers, the perfect squares, the factorials — are neither arithmetic nor geometric. Do not force an $a_n = a_1 + (n - 1)d$ or $a_n = a_1 r^{n-1}$ fit where none exists.

---

## Prerequisites

Before you tackle practice problems, make sure you are comfortable with:

- [[Function_Basics]] — sequences are functions whose domain is the positive integers
- [[Linear_Functions]] — arithmetic sequences are linear functions sampled at integer inputs
- [[Exponential_Functions]] — geometric sequences are exponential functions sampled at integer inputs
- [[Properties_Of_Exponents]] — so that working with $r^{n-1}$ is second nature

---

## Problems Involving Sequences

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="sequences"></div>

---

## See Also

- [[Arithmetic_Sequences_And_Linear_Patterns]] — the pre-algebra introduction with fewer moving parts
- [[Summation]] — sigma notation and the algebraic rules for manipulating sums
- [[Linear_Functions]] — the continuous parent of an arithmetic sequence
- [[Exponential_Functions]] — the continuous parent of a geometric sequence
- [[Function_Basics]] — domain, range, and function notation
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
