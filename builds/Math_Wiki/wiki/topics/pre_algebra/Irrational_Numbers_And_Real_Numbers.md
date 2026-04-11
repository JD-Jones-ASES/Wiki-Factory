---
title: "Irrational Numbers and Real Numbers"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Decimal_Place_Value_And_Comparing_Decimals"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "Every point on the number line is a real number; the irrational ones are the points you cannot pin down as a fraction."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Irrational Numbers and Real Numbers

# Irrational Numbers and Real Numbers

Up to now, almost every number you have worked with has fit into a simple mold: it could be written as a fraction of two whole numbers. Halves, thirds, decimals that eventually stop, decimals that eventually repeat — they are all secretly fractions in a costume. But there are other numbers, hiding between the fractions, that refuse to be written as any fraction at all. The square root of two is the most famous one. Pi is another. These are **irrational numbers**, and joining them together with the fractions you already know gives the full set of **real numbers** — every point on the number line, with no gaps.

## What it means

A **rational number** is one you can express as a ratio — a fraction $p/q$ whose top and bottom are integers and whose bottom is nonzero:

$$
\text{rational} = \frac{p}{q}, \quad p, q \in \mathbb{Z}, \quad q \neq 0.
$$

That definition is broader than it first looks. It catches all the whole numbers (write $7$ as $\tfrac{7}{1}$), all the negatives (write $-3$ as $\tfrac{-3}{1}$), all the ordinary fractions ($\tfrac{2}{5}$), and all the decimals that either end or eventually repeat ($0.25 = \tfrac{1}{4}$, $0.\overline{3} = \tfrac{1}{3}$). All of those are rational.

An **irrational number**, by contrast, sits on the real number line but stubbornly resists being expressed as any fraction $p/q$ of integers. Its decimal expansion marches on forever without ever settling into a repeating block. The classic examples are:

$$
\sqrt{2} = 1.41421356\ldots
$$

$$
\pi = 3.14159265\ldots
$$

Neither of those decimal expansions ever stops, and neither ever falls into a repeating pattern, no matter how far out you calculate.

The **real numbers** are the rationals and irrationals combined — the complete collection you can mark off on a number line:

$$
\mathbb{R} = \{\text{rationals}\} \cup \{\text{irrationals}\}
$$

Pick any dot along the line: it pairs up with one real number. Pick any real number: it lands on one dot along the line. There are no gaps, no missing spots, and no leftovers.

## How it works

To decide whether a given number is rational or irrational, try to write it as a ratio of two integers. If you can, it is rational. If you cannot, you need a different argument, because an irrational number has to be recognized by what it cannot do, not by what it can.

Here are the usual shortcuts:

- **Any integer** is rational. Put it over $1$.
- **Any fraction of integers** is rational by definition.
- **Any terminating decimal** is rational. $0.875$ is $\tfrac{875}{1000} = \tfrac{7}{8}$.
- **Any repeating decimal** is rational. $0.\overline{6}$ is $\tfrac{2}{3}$.
- **Square roots of perfect squares** are rational. $\sqrt{9} = 3$, $\sqrt{49} = 7$.
- **Square roots of non-perfect squares** are irrational. $\sqrt{2}$, $\sqrt{3}$, $\sqrt{7}$, $\sqrt{10}$ — all irrational.
- **$\pi$** is irrational. So is the ratio of the circumference of a circle to its diameter, which is where $\pi$ comes from.

When a problem asks "which set does this number belong to?" your job is to move down the ladder: is it a natural number? An integer? A rational? An irrational? The real numbers contain them all.

Estimating where an irrational number sits on the number line is its own small skill. For a square root like $\sqrt{10}$, find the nearest perfect squares above and below. $9 < 10 < 16$, so $\sqrt{9} < \sqrt{10} < \sqrt{16}$, which gives $3 < \sqrt{10} < 4$. That tells you $\sqrt{10}$ lands somewhere between $3$ and $4$, closer to the $3$ side because $10$ is closer to $9$ than to $16$.

## Why it works

The reason the real numbers are useful — and the reason irrationals had to be invented at all — is that there are lengths you can build with straight edges and right angles that cannot be written as any fraction of integers. The diagonal of a unit square is exactly $\sqrt{2}$, and no ratio of whole numbers ever lands on that value. The ancient Greeks discovered this and it genuinely upset them. Their world view was that every length should be expressible as a ratio, and $\sqrt{2}$ proved them wrong.

Adding the irrationals to the rationals is what makes the number line **complete** — meaning every point on it corresponds to some number, not just the ones you can reach with fractions. That completeness is why the number line feels like a smooth, continuous line rather than a dusty scattering of rational points.

## Worked examples

**Example 1.** Classify each of these numbers as rational or irrational: $\tfrac{3}{4}$, $0.\overline{3}$, $\sqrt{7}$, $\pi$.

Start with $\tfrac{3}{4}$. It is already a fraction of two integers, so it is rational.

Next, $0.\overline{3}$. The bar means "these digits repeat forever": $0.3333\ldots$. Repeating decimals are rational, and in this case the fraction equivalent is $\tfrac{1}{3}$.

Next, $\sqrt{7}$. Is $7$ a perfect square? No — the perfect squares near it are $4$ and $9$, neither equal to $7$. So $\sqrt{7}$ is irrational. Its decimal expansion $2.6457\ldots$ goes on forever without repeating.

Finally, $\pi$. This is the classic irrational. Its decimal expansion $3.14159265\ldots$ never ends and never repeats.

Final classification: $\tfrac{3}{4}$ and $0.\overline{3}$ are rational; $\sqrt{7}$ and $\pi$ are irrational. All four are real numbers — they all sit somewhere on the number line.

**Example 2.** Locate $\sqrt{2}$ between two consecutive integers on the number line, and estimate to the nearest tenth.

First, find the perfect squares around $2$. The perfect squares nearest to $2$ are $1$ and $4$, so:

$$
\sqrt{1} < \sqrt{2} < \sqrt{4}
$$

$$
1 < \sqrt{2} < 2.
$$

So $\sqrt{2}$ is between $1$ and $2$. To refine, test a few one-decimal guesses. $1.4^2 = 1.96$, which is just under $2$. $1.5^2 = 2.25$, which is just over $2$. So $\sqrt{2}$ is between $1.4$ and $1.5$, and closer to $1.4$ since $1.96$ is closer to $2$ than $2.25$ is. To the nearest tenth, $\sqrt{2} \approx 1.4$.

**Example 3.** Determine whether $\sqrt{9}$ and $\sqrt{10}$ are rational or irrational, and explain why they land in different categories.

For $\sqrt{9}$: $9$ is a perfect square because $3 \cdot 3 = 9$. So $\sqrt{9} = 3$, a whole number. Write it as $\tfrac{3}{1}$ and you have a ratio of two integers, making it rational.

For $\sqrt{10}$: Is $10$ a perfect square? The perfect squares around $10$ are $9$ and $16$, neither equal to $10$. So $\sqrt{10}$ is not a whole number, and in fact it cannot be written as any fraction of integers. That makes $\sqrt{10}$ irrational. Its decimal expansion $3.16227\ldots$ runs on without repeating.

The lesson here is important: not every square root is irrational. Only square roots of non-perfect-square integers are. When the radicand happens to be a perfect square, the root is a clean integer — very much rational.

## Common pitfalls

- **Assuming all square roots are irrational.** $\sqrt{16}$, $\sqrt{25}$, $\sqrt{100}$ are all whole numbers, and therefore rational. Only non-perfect-square roots are irrational.
- **Thinking repeating decimals are irrational.** Repeating decimals are rational — they have fraction equivalents. Only decimals that go on forever **and** never settle into a repeating pattern are irrational.
- **Claiming $\pi = \tfrac{22}{7}$.** The fraction $\tfrac{22}{7}$ is a close approximation, but it is not equal to $\pi$. If $\pi$ equaled any fraction of integers, it would be rational — and it is not.
- **Forgetting zero is rational.** Zero can be written as $\tfrac{0}{1}$ (or $\tfrac{0}{q}$ for any nonzero $q$), so it belongs squarely in the rational numbers.

## Problems Involving Irrational and Real Numbers

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="irrational_numbers_and_real_numbers"></div>

## See Also

- [[Square_Roots_And_Cube_Roots]]
- [[Integers_And_The_Number_Line]]
- [[Decimal_Place_Value_And_Comparing_Decimals]]
- [[Equivalent_Fractions_And_Simplifying]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
