---
title: "Operations with Radicals"
type: topic
aliases: ["Radical Arithmetic", "Adding Radicals", "Multiplying Radicals", "Dividing Radicals"]
tags: ["#branch-algebra-1", "#topic-exponents-and-radicals", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "9", section: "9.5"}
related:
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/algebra/Rational_Exponents"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/algebra/Simplifying_Radical_Expressions"
problem_type_ids: []
figures: []
summary: "Add, subtract, multiply, and divide square roots — and learn why simplifying first is the whole trick."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Operations with Radicals

# Operations with Radicals

Once you know how to simplify a single square root, the natural next question is what happens when two of them show up together. Can you add $\sqrt{2}$ and $\sqrt{3}$? Can you multiply $\sqrt{6}$ by $\sqrt{10}$? Can you divide something by $\sqrt{3}$ and still call the result "nice"? The answers depend on which operation you are doing — each of the four has its own small rule — and almost every one of them rewards the same habit: **simplify each radical first, then worry about the operation.**

The core of this topic is best summarized in one display:

$$
\sqrt{a}\cdot\sqrt{b} = \sqrt{ab} \qquad \text{and} \qquad \dfrac{\sqrt{a}}{\sqrt{b}} = \sqrt{\dfrac{a}{b}}
$$

Those two product and quotient rules do all the heavy lifting for multiplication and division. Addition and subtraction have their own, slightly fussier rule, which is where most students first stumble.

---

## Key ideas

**Addition and subtraction: only "like" radicals combine.** Two radical terms are "like" when they share the same index (both square roots, or both cube roots, etc.) and the same number inside the root. Think of $\sqrt{7}$ the way you think of $x$: $3\sqrt{7} + 5\sqrt{7} = 8\sqrt{7}$, just as $3x + 5x = 8x$. But $\sqrt{2} + \sqrt{5}$ is as simplified as it gets — you cannot squish two different radicals together any more than you can squish $x + y$ into a single term.

**The hidden twin trap.** Two radicals that look completely different on the page can secretly be like terms once you simplify them. That is the insight you must carry into every problem. Before you declare "these cannot be combined," reduce each radicand using the product rule for square roots. More often than you would expect, two ugly radicals collapse into multiples of the same simplified root.

**Multiplication: combine under one radical, then tidy up.** The product rule $\sqrt{a}\cdot\sqrt{b} = \sqrt{ab}$ lets you slam two square roots together into a single one. After multiplying, you usually still need to pull out any perfect-square factors hiding inside. When a radical multiplies a sum like $\sqrt{3}(\sqrt{6} + 4\sqrt{2})$, apply the distributive property first, then simplify each piece.

**Division: the quotient rule plus rationalization.** The quotient rule $\dfrac{\sqrt{a}}{\sqrt{b}} = \sqrt{\dfrac{a}{b}}$ lets you tuck two square roots under one bar. But a final answer with a radical sitting in the denominator is traditionally not considered simplified, so the last move is usually to **rationalize the denominator** — multiply the top and bottom by whatever radical factor clears the root from below.

---

## Example 1: like radicals hidden inside simplification

> Combine $\sqrt{12} + \sqrt{27}$ into a single radical term.

At first glance, $\sqrt{12}$ and $\sqrt{27}$ look nothing alike, and your instinct might be to say "these are already as simple as they get." Resist that instinct. Pull out the perfect squares from each radicand:

$$
\sqrt{12} = \sqrt{4 \cdot 3} = 2\sqrt{3}
$$

$$
\sqrt{27} = \sqrt{9 \cdot 3} = 3\sqrt{3}
$$

Now the two terms are clearly like radicals — both are multiples of $\sqrt{3}$. Combine the coefficients:

$$
2\sqrt{3} + 3\sqrt{3} = (2 + 3)\sqrt{3} = 5\sqrt{3}
$$

The whole trick was seeing that $12$ and $27$ both hid a factor of $3$. Without the simplification step, you would never have spotted the match.

---

## Example 2: multiplying and cleaning up

> Find the product $(\sqrt{6})(\sqrt{10})$ in simplified radical form.

Apply the product rule — merge the two radicals into one:

$$
\sqrt{6}\cdot\sqrt{10} = \sqrt{6 \cdot 10} = \sqrt{60}
$$

You are not done. The radicand $60$ still has a perfect-square factor lurking inside: $60 = 4 \cdot 15$. Split it and pull the $4$ out:

$$
\sqrt{60} = \sqrt{4 \cdot 15} = 2\sqrt{15}
$$

Since $15 = 3 \cdot 5$ has no perfect-square factors, $2\sqrt{15}$ is the final simplified form. The moral: "multiply the radicals" is only step one. Step two is always "now simplify the result."

---

## Example 3: division with rationalization

> Rewrite $\dfrac{6}{\sqrt{3}}$ so that there is no radical in the denominator.

The denominator contains $\sqrt{3}$, which you want to turn into a whole number. Multiply the top and the bottom by $\sqrt{3}$ (this is the same as multiplying by $1$, so the value of the expression does not change):

$$
\dfrac{6}{\sqrt{3}} \cdot \dfrac{\sqrt{3}}{\sqrt{3}} = \dfrac{6\sqrt{3}}{\sqrt{3}\cdot\sqrt{3}} = \dfrac{6\sqrt{3}}{3}
$$

The bottom collapses because $\sqrt{3}\cdot\sqrt{3} = 3$ — squaring a square root always erases the radical. Now reduce the coefficient:

$$
\dfrac{6\sqrt{3}}{3} = 2\sqrt{3}
$$

For binomial denominators like $\dfrac{4}{1 + \sqrt{5}}$, the same idea works but you multiply top and bottom by the **conjugate** — in this case $1 - \sqrt{5}$. The product $(1 + \sqrt{5})(1 - \sqrt{5}) = 1 - 5 = -4$ is radical-free, thanks to the difference-of-squares pattern.

---

## Common pitfalls

- **Adding unrelated radicals.** $\sqrt{2} + \sqrt{3}$ is not $\sqrt{5}$, and it is not any other single radical. Different radicands cannot merge across a plus sign.
- **Forgetting to simplify after multiplying.** $\sqrt{8}\cdot\sqrt{6} = \sqrt{48}$ is technically correct but not simplified — $48 = 16 \cdot 3$, so the answer should be $4\sqrt{3}$.
- **Leaving a radical in the denominator.** An expression like $\dfrac{5}{\sqrt{2}}$ is not considered final form; rationalize it to $\dfrac{5\sqrt{2}}{2}$.
- **Skipping simplification before adding.** If you do not reduce each radical first, you will miss the fact that $\sqrt{8} + \sqrt{18}$ is really $2\sqrt{2} + 3\sqrt{2} = 5\sqrt{2}$ — a classic hidden-twin pattern.

---

## Prerequisites

Before practicing, make sure you are solid on these building blocks:

- [[Square_Roots_And_Cube_Roots]] — you need to be fluent with individual square roots before juggling several of them at once
- [[Simplifying_Radical_Expressions]] — the "pull out perfect squares" move is baked into almost every operation on this page

---

## Problems Involving Operations with Radicals

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="operations_with_radicals"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Simplifying_Radical_Expressions]]
- [[Square_Roots_And_Cube_Roots]]
- [[The_Pythagorean_Theorem]]
- [[Rational_Exponents]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
