---
title: "Summation"
type: topic
aliases: ["Sigma Notation", "Summation Notation", "Series"]
tags: ["#branch-pre-calculus", "#topic-sequences-and-series", "#key-formula"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "9", section: "9.4"}
related:
  - "topics/algebra/Sequences"
  - "topics/pre_algebra/Arithmetic_Sequences_And_Linear_Patterns"
  - "topics/algebra/Exponential_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Sequences"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Properties_Of_Exponents"
problem_type_ids: []
figures: []
summary: "Sigma notation — a compact way to write a long sum, together with the linearity rules and closed-form identities that make those sums tractable."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Summation

# Summation

Once you start working with [[Sequences]], you will often need to add up a long stretch of terms at once. Writing out $1 + 3 + 5 + 7 + \cdots + 199$ on paper is fine for a few terms, but it becomes absurd when there are fifty or a hundred entries, and it is a disaster when the list has a pattern that you want to manipulate symbolically. Mathematicians solve this problem with a single piece of shorthand called **sigma notation**, named after the capital Greek letter $\Sigma$ that sits at the heart of the symbol.

The expression

$$
\sum_{k=1}^{n} a_k
$$

is read "the sum of $a_k$ as $k$ runs from $1$ to $n$." It is a packaging device: it asks you to start with $k = 1$, plug that value into the expression $a_k$, then plug in $k = 2$, then $k = 3$, and so on all the way up to $k = n$, and finally add every one of those results together. In other words,

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + a_3 + \cdots + a_n.
$$

Each piece of the symbol has a name worth knowing:

- The letter $k$ is called the **index of summation**. It is just a placeholder — you could replace it with any other letter not already in use, such as $i$, $j$, or $n$.
- The number below the sigma (here $1$) is the **lower limit of summation**. It tells you the smallest value the index takes.
- The number above the sigma (here $n$) is the **upper limit of summation**. It tells you the largest value the index takes.
- The expression to the right of the sigma (here $a_k$) is the **summand**. It is the recipe that gets evaluated at each value of the index.

Those four ingredients together tell you exactly which sum you are being asked to compute, with zero ambiguity. Lower limits do not have to start at $1$, either — you will see sums that begin at $k = 0$, $k = 3$, or any other sensible starting point.

---

## Expanding a sum written in sigma notation

When you first meet sigma notation, the easiest move is to **write it out**. Replace the index with each value in turn, and stitch the pieces together with plus signs. For instance,

$$
\sum_{k=1}^{4} (2k + 3)
$$

becomes

$$
(2 \cdot 1 + 3) + (2 \cdot 2 + 3) + (2 \cdot 3 + 3) + (2 \cdot 4 + 3) = 5 + 7 + 9 + 11 = 32.
$$

That is literally all there is to expansion. Sigma notation is just a handwriting shortcut; underneath it you always have an ordinary sum.

---

## Writing an ordinary sum in sigma notation

Going the other direction — taking a long sum and compressing it into sigma notation — is slightly trickier because you have to spot the pattern first. The workflow is:

1. Identify the **summand**: find a formula whose $k$th value matches the $k$th term of the sum.
2. Identify the **lower limit**: pick the index value that produces the first term.
3. Identify the **upper limit**: pick the index value that produces the last term.
4. Bundle everything together inside a $\Sigma$.

For example, the sum $1 + 3 + 5 + 7 + \cdots + 99$ is the sum of the first $50$ odd positive integers. The $k$th odd number is $2k - 1$, so that is the summand. You want $k$ to run from $1$ (which gives $2(1) - 1 = 1$) up to $50$ (which gives $2(50) - 1 = 99$). Therefore,

$$
1 + 3 + 5 + \cdots + 99 = \sum_{k=1}^{50} (2k - 1).
$$

A small warning: if a summand already uses the letter $n$ somewhere else (say, in the upper limit), you must pick a different letter for the index. Using the same symbol for two different things is the fastest way to confuse yourself — and the answer key.

---

## Linearity: the two rules that make summation bearable

Sigma notation would not be nearly as useful if you always had to unpack it term by term. The reason you can do real algebra inside a sum is a pair of rules called the **linearity properties of summation**. They say that a $\Sigma$ behaves a lot like a derivative or an integral: it distributes across addition and pulls constants through.

**Rule 1 (sum rule).** If both sums are defined, then

$$
\sum_{k=m}^{p} (a_k + b_k) = \sum_{k=m}^{p} a_k + \sum_{k=m}^{p} b_k,
$$

and the same identity holds with a minus sign. You are allowed to split a long sum into two shorter ones whenever the summand is a sum or difference.

**Rule 2 (constant multiple rule).** If $c$ is a fixed real number, then

$$
\sum_{k=m}^{p} c \cdot a_k = c \sum_{k=m}^{p} a_k.
$$

A constant factor that sits inside every term can be pulled out in front of the $\Sigma$. The index $k$ is the only thing that is allowed to change as you march through the sum, so anything without a $k$ is just a tag-along factor.

Together, these two rules are exactly the properties of a **linear operator**. You will meet this word in a calculus or linear-algebra course, but the idea is perfectly visible right here: sigma notation is friendly to addition and scalar multiplication, period.

---

## Standard closed-form sums

For a few especially useful summands, the sum has a short closed-form expression that you can use without ever expanding the pieces. These three identities are the most common:

$$
\sum_{k=1}^{n} c = cn \qquad\text{(sum of the constant } c \text{, taken } n \text{ times)}
$$

$$
\sum_{k=1}^{n} k = \dfrac{n(n+1)}{2}
$$

$$
\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}
$$

The first is just repeated addition: if every term is $c$ and there are $n$ of them, the total is $cn$. The second is the famous "triangular-number" formula, which you may have seen attributed to a young Gauss — pair the first term with the last, the second with the second-to-last, and each pair sums to $n + 1$. The third is harder to prove from scratch (mathematical induction is the cleanest route), but once you have it, it reduces sums of squares to a one-line calculation. Combined with the linearity rules, these three identities let you evaluate an enormous range of sums without ever writing out every term.

---

## Example 1: expanding a sum in sigma notation

> Expand and evaluate $\displaystyle\sum_{k=1}^{5} \dfrac{(-1)^{k+1}}{k}$.

The $(-1)^{k+1}$ in the numerator is the standard trick for producing alternating signs: when $k$ is odd, $k + 1$ is even and $(-1)^{k+1} = +1$; when $k$ is even, $(-1)^{k+1} = -1$. So the signs will go $+, -, +, -, +$ for $k = 1, 2, 3, 4, 5$. Plug in each value:

$$
\sum_{k=1}^{5} \dfrac{(-1)^{k+1}}{k} = \dfrac{1}{1} - \dfrac{1}{2} + \dfrac{1}{3} - \dfrac{1}{4} + \dfrac{1}{5}.
$$

Combine the fractions over a common denominator of $60$:

$$
= \dfrac{60}{60} - \dfrac{30}{60} + \dfrac{20}{60} - \dfrac{15}{60} + \dfrac{12}{60} = \dfrac{60 - 30 + 20 - 15 + 12}{60} = \dfrac{47}{60}.
$$

So the partial sum is $47/60 \approx 0.783$. (If you continue this sum to infinity, you get a famous value — the natural logarithm of $2$. That identity shows up in a later calculus course.)

---

## Example 2: writing a sum in sigma notation

> Rewrite the sum $4 + 7 + 10 + 13 + 16 + \cdots + 97$ using sigma notation.

This is a sum of the terms of an arithmetic sequence — first term $4$, common difference $3$. The $k$th term is

$$
a_k = 4 + (k - 1)(3) = 3k + 1.
$$

Spot-check that formula: $a_1 = 4$, $a_2 = 7$, $a_3 = 10$. All match. To find the upper limit of summation, determine which value of $k$ makes $a_k = 97$:

$$
3k + 1 = 97 \quad\Longrightarrow\quad 3k = 96 \quad\Longrightarrow\quad k = 32.
$$

So the sum runs from $k = 1$ to $k = 32$:

$$
4 + 7 + 10 + \cdots + 97 = \sum_{k=1}^{32} (3k + 1).
$$

That is already the compact answer. If the problem also asks for the total, now is the moment to use linearity together with the closed-form identities:

$$
\sum_{k=1}^{32} (3k + 1) = 3\sum_{k=1}^{32} k + \sum_{k=1}^{32} 1 = 3 \cdot \dfrac{32 \cdot 33}{2} + 32 = 3 \cdot 528 + 32 = 1584 + 32 = 1616.
$$

Both rules came out to play: the sum of $3k + 1$ was split using Rule 1, the constant $3$ was pulled out using Rule 2, and then the two standard identities $\sum k = n(n+1)/2$ and $\sum c = cn$ finished the job.

---

## Example 3: linearity with a sum of squares

> Compute $\displaystyle\sum_{k=1}^{10} (k^2 - 4k + 3)$ using the linearity rules and the closed-form identities.

First split the sum into three pieces using Rule 1:

$$
\sum_{k=1}^{10} (k^2 - 4k + 3) = \sum_{k=1}^{10} k^2 - \sum_{k=1}^{10} 4k + \sum_{k=1}^{10} 3.
$$

Then pull out the constants using Rule 2:

$$
= \sum_{k=1}^{10} k^2 - 4\sum_{k=1}^{10} k + \sum_{k=1}^{10} 3.
$$

Now apply the three closed-form identities with $n = 10$:

$$
\sum_{k=1}^{10} k^2 = \dfrac{10 \cdot 11 \cdot 21}{6} = \dfrac{2310}{6} = 385,
$$

$$
\sum_{k=1}^{10} k = \dfrac{10 \cdot 11}{2} = 55,
$$

$$
\sum_{k=1}^{10} 3 = 3 \cdot 10 = 30.
$$

Assemble the pieces:

$$
385 - 4(55) + 30 = 385 - 220 + 30 = 195.
$$

Without the linearity rules, you would have been stuck evaluating a polynomial ten times and then adding ten signed numbers by hand. With them, the entire computation collapses to three quick formulas.

---

## Bridge to infinite series

Everything on this page is about **finite** sums — sums with a definite stopping point. Pre-calculus and calculus both go on to study **infinite** sums, where the upper limit of the $\Sigma$ is replaced by $\infty$. Some of those infinite sums converge to a finite total (the most famous is the infinite geometric series $\sum_{k=1}^{\infty} a r^{k-1} = a/(1 - r)$ whenever $|r| < 1$, which you first meet in [[Sequences]]), and some diverge. Deciding which is which is the whole subject of "convergence tests" in calculus. For now, lock in the notation, the linearity rules, and the three standard identities — together they handle essentially every finite-sum problem you will face in a high-school or early-college course.

---

## Common pitfalls

- **Reindexing without fixing the formula.** If you shift the lower limit from $k = 1$ to $k = 0$, every appearance of $k$ in the summand needs to be replaced by $k + 1$ (or the other way around). Shifting only the limits and leaving the summand alone silently changes the sum.
- **Pulling a term that depends on $k$ outside the $\Sigma$.** Rule 2 only applies to **constants** with respect to the index. You cannot yank $k^2$ or a $(-1)^k$ outside of a sum; those depend on the index and have to stay inside.
- **Off-by-one in the upper limit.** A sum from $k = 1$ to $k = n$ has exactly $n$ terms, but a sum from $k = 0$ to $k = n$ has $n + 1$ terms. Always count the terms once before applying a closed-form identity.
- **Ignoring the difference between index and upper limit.** Using the same letter for both — writing $\sum_{n=1}^n a_n$ — leaves you with a nonsense expression. Pick a fresh letter for the index whenever the upper limit already uses $n$.
- **Assuming every sum has a closed form.** The three identities $\sum c$, $\sum k$, $\sum k^2$ cover the "polynomial-in-$k$" cases. Sums like $\sum \sqrt{k}$ or $\sum 1/k$ do not simplify nicely at the pre-calculus level and have to be estimated or left in sigma form.

---

## Prerequisites

Before you tackle practice problems, make sure you are comfortable with:

- [[Sequences]] — the underlying objects whose terms you are adding up
- [[Function_Basics]] — so that the substitution step feels routine
- [[Properties_Of_Exponents]] — useful whenever the summand involves powers

---

## Problems Involving Summation

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="summation"></div>

---

## See Also

- [[Sequences]] — arithmetic, geometric, and infinite geometric series
- [[Arithmetic_Sequences_And_Linear_Patterns]] — the pre-algebra starting point
- [[Exponential_Functions]] — the continuous cousin of a geometric sequence
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
