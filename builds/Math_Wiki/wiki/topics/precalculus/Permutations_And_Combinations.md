---
title: "Permutations and Combinations"
type: topic
aliases: ["Permutations", "Combinations", "Counting Principles", "nPr and nCr"]
tags: ["#branch-pre-calculus", "#topic-probability", "#skill-formula-substitution", "#skill-procedural-calculation", "#key-formula", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "9", section: "9.5"}
related:
  - "topics/precalculus/Binomial"
  - "topics/precalculus/Binomial_Probability"
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/precalculus/Conditional_Probability"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/precalculus/Binomial"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: []
summary: "Two counting formulas — P(n,r) when order matters and C(n,r) when it does not — together with factorials and a quick diagnostic for picking the right one."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Permutations and Combinations

# Permutations and Combinations

Counting problems sound like they should be trivial. After all, counting is the first thing anyone learns about numbers. The trouble is that the lists get long fast. How many different ways can you line up seven runners on a starting grid? How many different five-card hands can come out of a standard deck? How many different three-scoop ice-cream cups can you order from a shop that carries eleven flavors? In every case the answer is a big number, and writing out every possibility by hand is nobody's idea of a good time.

Two short formulas handle almost all of these questions. One of them — the **permutation** formula — applies when the order of the chosen items matters. The other — the **combination** formula — applies when the order of the chosen items is irrelevant. Picking which one to use is the whole game. Once you have the right formula, the rest is arithmetic on factorials.

$$
P(n, r) = \dfrac{n!}{(n-r)!} \qquad\qquad C(n, r) = \dfrac{n!}{r!\,(n-r)!}
$$

---

## Factorials, the raw ingredient

Both formulas are built on **factorials**. For a whole number $n$, the symbol $n!$ stands for the running product

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 3 \cdot 2 \cdot 1,
$$

with the special convention $0! = 1$. So $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$, $5! = 120$, and $6! = 720$. Factorials explode in size: $10!$ is already over three million, and $15!$ is more than a trillion.

The reason factorials appear in counting formulas is straightforward. Say you want to arrange five distinct books on a shelf. You have $5$ choices for which book goes leftmost. After you place that one, $4$ books remain, so you have $4$ choices for the next slot, then $3$, then $2$, then $1$. Multiply: $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 5! = 120$. That is not a coincidence — any time you line up $n$ distinct objects, the number of orderings is exactly $n!$.

A small but crucial arithmetic habit: when you see a quotient of factorials, cancel before you multiply. Writing $8! / 5!$ and then computing $8! = 40320$ and $5! = 120$ on a calculator wastes effort; the expression collapses directly to $8 \cdot 7 \cdot 6 = 336$ once you cross out the shared tail $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$.

---

## Permutations: when order matters

A **permutation** is a listing of $r$ items pulled from a pool of $n$ distinct items, where rearranging the list produces a genuinely different answer. The number of such listings is

$$
P(n, r) = \dfrac{n!}{(n-r)!}.
$$

A clean way to see where this comes from: you have $n$ choices for the first slot, $n-1$ for the second, $n-2$ for the third, and so on down to $n - r + 1$ for the $r$th slot. The product of those $r$ descending factors is exactly $n \cdot (n-1) \cdots (n - r + 1)$, which is what you get when you cancel $(n-r)!$ out of $n!$.

The notation varies by textbook. You will see $P(n, r)$, $_nP_r$, and the calculator key ${nPr}$ — all three mean the same thing. On a graphing calculator, the function lives under the probability menu; punch in $n$, pick $nPr$, then punch in $r$.

---

## Combinations: when order doesn't matter

A **combination** is a selection of $r$ items from a pool of $n$ distinct items, where two selections are considered the same if they contain the same items in any order. The count is

$$
C(n, r) = \binom{n}{r} = \dfrac{n!}{r!\,(n-r)!}.
$$

The combination formula is the permutation formula divided by an extra $r!$, and that extra factor is doing real work. Whenever you count arrangements with $P(n, r)$, you have counted each underlying set of $r$ items $r!$ times — once for every possible rearrangement of those items. Dividing by $r!$ collapses each group of rearrangements into a single count.

The notation $\binom{n}{r}$ is read "$n$ choose $r$" and is the same symbol that appears in the [[Binomial|Binomial Theorem]]. That connection is not an accident: the coefficient of $x^{n-r} y^r$ in the expansion of $(x + y)^n$ is exactly the number of ways to choose which $r$ of the $n$ factors contribute a $y$ — a pure combination count.

---

## How to tell them apart

The single most common error on a test is confusing the two formulas. Here is a short diagnostic: read the problem and ask yourself whether swapping two of the chosen items produces a new outcome.

- A starting **lineup** for a relay race, with positions labeled first-leg through fourth-leg, is ordered. Swapping the first two runners changes who runs first. Use $P$.
- A **committee** of four people chosen from a group of twenty is unordered. Swapping two committee members leaves the same committee. Use $C$.
- A **password** made of four distinct letters is ordered. Use $P$.
- A **pizza** topped with three out of ten available toppings is unordered. Use $C$.
- A set of three **gold, silver, and bronze medals** awarded to three finalists is ordered (the medals are distinct). Use $P$.
- A **team** of three finalists advancing to the next round is unordered (they all advance together). Use $C$.

A useful rule of thumb: if the word **arrangement**, **lineup**, **sequence**, **order**, or **rank** appears in the problem, permutations are probably correct. If the word **committee**, **team**, **group**, **selection**, or **subset** appears, combinations are probably correct. When in doubt, imagine physically swapping two of the chosen items. If the answer changes, order matters.

---

## Example 1: arranging books on a shelf

> How many ways can Priya arrange $4$ different novels, chosen from her shelf of $7$ distinct novels, in a row on a display ledge?

Order matters here — a row labeled "leftmost, second, third, rightmost" counts two lineups as different whenever the books appear in different positions. So this is a permutation question with $n = 7$ and $r = 4$:

$$
P(7, 4) = \dfrac{7!}{(7 - 4)!} = \dfrac{7!}{3!} = 7 \cdot 6 \cdot 5 \cdot 4 = 840.
$$

Notice how the factorial tail $3!$ in the denominator cancels the tail of $7!$, leaving just the four descending factors from $7$ down to $4$. No calculator needed. Priya has $840$ different displays.

---

## Example 2: choosing a team

> How many ways can a coach choose a $3$-person starting squad from a roster of $8$ players, if all three positions are treated as interchangeable?

The three picked players all have the same role, so swapping two of them produces the same squad. Order does not matter — this is a combination problem with $n = 8$ and $r = 3$:

$$
C(8, 3) = \dfrac{8!}{3!\,(8-3)!} = \dfrac{8!}{3!\,5!} = \dfrac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = \dfrac{336}{6} = 56.
$$

There are $56$ different squads. If the problem had instead said "pick a point guard, a shooting guard, and a center" — three distinct positions — the calculation would have shifted to a permutation, because assigning the same three people to different roles would have counted as a different outcome. $P(8, 3) = 336$, exactly $6 = 3!$ times larger, because every unordered squad of three can be assigned to positions in $3! = 6$ ways.

---

## Example 3: a mixed warm-up

> Compute each of the following by hand: $5!$, $P(6, 2)$, and $C(6, 2)$.

These three values are sitting next to each other so that you can feel the pattern. Start with the factorial:

$$
5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120.
$$

For $P(6, 2)$, use the descending-factor shortcut — two factors starting from $6$:

$$
P(6, 2) = \dfrac{6!}{4!} = 6 \cdot 5 = 30.
$$

For $C(6, 2)$, divide the permutation count by $2! = 2$ because there are $2! = 2$ orderings of any two chosen items:

$$
C(6, 2) = \dfrac{P(6, 2)}{2!} = \dfrac{30}{2} = 15.
$$

Notice how the three answers stack up. The factorial $5! = 120$ counts every arrangement of five distinct items. The permutation $P(6, 2) = 30$ counts ordered pairs from a pool of six. The combination $C(6, 2) = 15$ counts unordered pairs from the same pool — exactly half of $30$, because each unordered pair has $2! = 2$ orderings. Keep that doubling-and-halving relationship in mind and you will never mix up the two formulas again.

---

## Common pitfalls

- **Using $P$ when order does not matter.** The single biggest error on this topic. A committee is unordered; a lineup is ordered. Imagine swapping two chosen items — if the answer stays the same, use $C$.
- **Forgetting that items must be distinct.** Both $P(n, r)$ and $C(n, r)$ assume the $n$ items are all different from each other. Problems with repeated letters (like counting arrangements of the letters in "MISSISSIPPI") need a different, slightly more elaborate formula.
- **Computing the full $n!$ when you only need a partial product.** Never punch $10!$ into a calculator to find $P(10, 3)$. Cancel the factorial tail first: $P(10, 3) = 10 \cdot 9 \cdot 8 = 720$.
- **Misreading $0!$.** By convention $0! = 1$, not $0$. This convention keeps $C(n, 0) = 1$ (there is exactly one way to choose nothing) and makes the combination formula work at the boundary.
- **Confusing $\binom{n}{r}$ with a fraction.** The symbol $\binom{n}{r}$ stacked vertically is NOT the fraction $n/r$. It is a single number computed from the formula above.

---

## Prerequisites

- [[Probability_Of_Simple_And_Compound_Events]] — the counting intuition that feeds into every probability question built on $P$ and $C$.
- [[Binomial|The Binomial Theorem]] — where the combination symbol $\binom{n}{r}$ shows up as a coefficient and reinforces the "choose $r$ items from $n$" interpretation.
- [[Function_Basics]] — so that substituting numbers into a multi-variable formula feels automatic.

---

## Problems Involving Permutations and Combinations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="permutations_and_combinations"></div>

---

## See Also

- [[Binomial|The Binomial Theorem]] — the same $\binom{n}{r}$ in a different costume
- [[Binomial_Probability]] — what happens when you attach probabilities to combination counts
- [[Probability_Of_Simple_And_Compound_Events]] — the pre-algebra foundation
- [[Conditional_Probability]] — the next step once sample-space counts stop being uniform
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
