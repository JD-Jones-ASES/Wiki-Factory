---
title: "Binomial Probability"
type: topic
aliases: ["Binomial Distribution", "Binomial PMF", "Binomial Random Variable", "n Choose k Probability"]
tags: ["#branch-pre-calculus", "#topic-probability", "#skill-formula-substitution", "#skill-multi-step", "#key-formula", "#test-sat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "11", section: "11.5"}
related:
  - "topics/precalculus/Permutations_And_Combinations"
  - "topics/precalculus/Binomial"
  - "topics/precalculus/Expected_Value"
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Permutations_And_Combinations"
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/precalculus/Binomial"
problem_type_ids: []
figures: ["precalculus/binomial_pmf_bar_chart.svg"]
summary: "The probability model for counting successes in a fixed number of independent yes/no trials, built from one formula and two summary numbers — mean np and variance np(1-p)."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Binomial Probability

# Binomial Probability

Lots of random processes amount to running the same yes/no experiment many times in a row. Flip a coin $20$ times and count the heads. Fire a free throw $10$ times and count the makes. Answer $5$ multiple-choice questions by pure guessing and count the correct ones. In every such scenario you have a fixed number of **trials**, each trial has exactly two outcomes (conventionally called "success" and "failure"), and the probability of success stays constant from trial to trial. Those three conditions — fixed $n$, two outcomes per trial, constant $p$, independent trials — are the defining fingerprint of a **binomial** random variable.

A binomial random variable $X$ counts the total number of successes across all $n$ trials. Its possible values are $0, 1, 2, \ldots, n$, and for any specific count $k$, the probability is given by a short formula:

$$
P(X = k) = \binom{n}{k} \, p^{k} \, (1-p)^{n-k}.
$$

Three pieces multiplied together: a combination count $\binom{n}{k}$, a success probability $p^k$, and a failure probability $(1-p)^{n-k}$. Get those three pieces right and you can answer any "what is the probability of exactly $k$ successes in $n$ trials" question.

![[binomial_pmf_bar_chart.svg|Bar chart of a binomial probability mass function]]

---

## Unpacking the formula

The formula looks dense at first glance, but each of its three factors has a plain-English meaning.

**The power $p^k$.** Any single sequence of $n$ trials that produces exactly $k$ successes has some specific pattern — SSFSF... for example. Because the trials are independent, the probability of that exact sequence is the product of the individual trial probabilities. The $k$ successful trials contribute $p$ each (total $p^k$), and the $n - k$ failing trials contribute $1-p$ each (total $(1-p)^{n-k}$). So each specific sequence with $k$ successes has probability

$$
p^k (1-p)^{n-k}.
$$

**The count $\binom{n}{k}$.** Lots of different sequences produce the same total of $k$ successes. SSFSF and FSSFS both have $k = 3$ successes, and they are distinct sequences even though they give the same count. How many distinct sequences are there? The number of ways to choose which of the $n$ trials are the successful ones — exactly $\binom{n}{k}$, the same combination symbol that appears in [[Binomial|the Binomial Theorem]] and in the [[Permutations_And_Combinations|combination formula]].

**Multiplying the two together** gives the total probability of seeing $k$ successes in any order: probability of one specific sequence ($p^k (1-p)^{n-k}$), multiplied by the number of such sequences ($\binom{n}{k}$). That product is $P(X = k)$.

The bar chart above shows the distribution for a specific case of $n$ and $p$ — each bar's height is $P(X = k)$ for one value of $k$. Varying $p$ slides the peak of the distribution around; large $p$ pushes the peak to the right (many successes are likely), small $p$ pushes the peak to the left (few successes are likely). Varying $n$ stretches the distribution over more values. Every bar chart of a binomial distribution has the same overall shape: a single peak, skewed toward whichever side $p$ leans, with the bars shrinking as you move out to the edges.

---

## Mean and variance

Two summary numbers describe a binomial distribution compactly, without needing to work out every bar height.

The **mean** (expected value) is

$$
\mu = E[X] = np.
$$

The intuition is immediate: each of $n$ trials has a per-trial expected contribution of $p$ successes, and the linearity of expectation adds those up. Flipping a fair coin $n = 20$ times ($p = 0.5$) gives $\mu = 20(0.5) = 10$ heads on average. Rolling a six-sided die $n = 60$ times and counting sixes ($p = 1/6$) gives $\mu = 60 \cdot (1/6) = 10$ sixes on average.

The **variance** is

$$
\sigma^2 = np(1-p),
$$

and the standard deviation is the square root of that: $\sigma = \sqrt{np(1-p)}$. The variance vanishes when $p = 0$ or $p = 1$ (in those edge cases $X$ is not random at all), and it is maximized at $p = 0.5$ (when the outcome of each trial is most unpredictable).

These two shortcut formulas are much faster than unpacking the full distribution. If all you need is the average count of successes, the formula $\mu = np$ lets you skip the distribution entirely.

---

## Using the complement for "at least" questions

A common question type asks for $P(X \geq k)$ — the probability of getting at least $k$ successes — rather than an exact count. Computing the complement is almost always easier than computing a long sum.

The key identity is

$$
P(X \geq k) = 1 - P(X \leq k - 1) = 1 - \sum_{j=0}^{k-1} \binom{n}{j} p^j (1-p)^{n-j}.
$$

When $k$ is close to $0$ (say, "at least one success"), the complement is compact: $P(X \geq 1) = 1 - P(X = 0)$, just a single subtraction. When $k$ is large, you might compute $P(X \geq k)$ directly by summing the upper tail instead. Either way, the complement trick reframes a long-tail question as a short-tail question.

---

## Example 1: exact count on a multiple-choice quiz

> A quiz has $5$ multiple-choice questions, each with $4$ answer choices. A student guesses randomly on every question. What is the probability of getting exactly $3$ correct?

Each question is an independent trial with success probability $p = 1/4$ (the student picks the correct option by luck) and failure probability $1 - p = 3/4$. With $n = 5$ questions and target $k = 3$, plug into the formula:

$$
P(X = 3) = \binom{5}{3} \left(\dfrac{1}{4}\right)^3 \left(\dfrac{3}{4}\right)^2.
$$

Work out each piece separately. The combination $\binom{5}{3} = 10$ (row $5$ of Pascal's triangle, third entry in from either edge). The success factor $(1/4)^3 = 1/64$. The failure factor $(3/4)^2 = 9/16$. Multiply the three pieces together:

$$
P(X = 3) = 10 \cdot \dfrac{1}{64} \cdot \dfrac{9}{16} = \dfrac{90}{1024} = \dfrac{45}{512} \approx 0.088.
$$

So the probability of exactly $3$ correct answers is about $8.8\%$. Not nothing, but not likely either — guessing rarely nets you a majority.

---

## Example 2: at-least-one via the complement

> A field archer has a $0.30$ probability of hitting the bullseye on any single shot. Determine the probability that at least one of her next $8$ shots hits the bullseye.

"At least one" is the prototypical complement problem. The event "at least one hit" has as its complement the event "zero hits." If $X$ is the number of hits in $8$ shots, then $X$ is binomial with $n = 8$, $p = 0.30$, and

$$
P(X \geq 1) = 1 - P(X = 0) = 1 - \binom{8}{0}(0.30)^0 (0.70)^8.
$$

The combination at the front is $\binom{8}{0} = 1$. The $(0.30)^0$ factor is $1$ (anything to the zeroth power equals $1$). So the formula simplifies all the way down to

$$
P(X \geq 1) = 1 - (0.70)^8.
$$

Compute $(0.70)^8$ by squaring a few times. $(0.70)^2 = 0.49$. $(0.70)^4 = (0.49)^2 = 0.2401$. $(0.70)^8 = (0.2401)^2 \approx 0.0576$. Subtract from $1$:

$$
P(X \geq 1) \approx 1 - 0.0576 = 0.9424.
$$

So there is roughly a $94\%$ chance of at least one bullseye in $8$ shots. Trying to compute this directly as $P(X = 1) + P(X = 2) + \cdots + P(X = 8)$ would require eight separate formula applications; the complement route needed one.

---

## Example 3: the $np$ shortcut for the mean

> A factory produces circuit boards with a $5\%$ defect rate. In a random sample of $200$ boards, how many defective boards are expected on average?

The sample is $n = 200$ independent Bernoulli trials, each with success probability $p = 0.05$ (where "success" means "the board is defective" — a slightly ironic usage of the word). The number of defects $X$ is binomial with those parameters, and the question asks for the expected value.

Use the shortcut formula $\mu = np$ directly without touching the full distribution:

$$
\mu = np = 200 \cdot 0.05 = 10.
$$

On average, the sample contains $10$ defective boards. The matching standard deviation is

$$
\sigma = \sqrt{np(1-p)} = \sqrt{200 \cdot 0.05 \cdot 0.95} = \sqrt{9.5} \approx 3.08.
$$

So a typical sample of $200$ boards has roughly $10 \pm 3$ defects — occasionally as few as $4$ or as many as $16$, but $10$ is the long-run average. Computing this with the full formula $P(X = k)$ for every $k$ from $0$ to $200$ and adding $k \cdot P(X = k)$ is possible, but pointless when the $np$ shortcut gives the answer in one multiplication.

---

## Common pitfalls

- **Using the formula when trials are not independent.** Drawing cards **without** replacement breaks independence — the probability of a success on trial $2$ depends on what happened on trial $1$. Binomial is the wrong model there; a hypergeometric distribution is the right one. Drawing **with** replacement keeps trials independent and keeps you inside binomial territory.
- **Forgetting the combination factor.** A very common error is writing $P(X = k) = p^k (1-p)^{n-k}$, which is the probability of one **specific** sequence — not the full probability of getting $k$ successes across all possible sequences. You must multiply by $\binom{n}{k}$.
- **Mixing up $p$ and $1 - p$ in the exponents.** The success probability $p$ is raised to the number of successes $k$. The failure probability $1-p$ is raised to the number of failures $n - k$. If the two exponents get switched, the formula still produces a number, but the wrong one.
- **Reading "at least $k$" as $P(X = k)$.** "At least" always implies a sum or complement, not a single formula plug-in.
- **Treating $np$ as a probability.** The mean $np$ is a count of successes, not a probability. For $n = 200$ and $p = 0.05$ you get $np = 10$ — ten expected successes, not a $10\%$ probability of anything.

---

## Prerequisites

- [[Permutations_And_Combinations]] — the $\binom{n}{k}$ factor in every binomial calculation.
- [[Probability_Of_Simple_And_Compound_Events]] — the independence principle that underlies "multiply the probabilities of independent events."
- [[Binomial|The Binomial Theorem]] — the identity $\sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = 1$ is exactly the binomial theorem applied to $(p + (1-p))^n = 1^n = 1$, which is why the probabilities of all possible counts add to one.

---

## Problems Involving Binomial Probability

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="binomial_probability"></div>

---

## See Also

- [[Permutations_And_Combinations]] — the counting engine
- [[Binomial|The Binomial Theorem]] — the algebraic identity that makes the probabilities sum to one
- [[Expected_Value]] — where $np$ appears as a specialization of $\sum x_i p_i$
- [[Normal_Distribution]] — the shape the binomial bar chart approaches as $n$ grows large
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
