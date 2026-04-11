---
title: "Cube Root and Other Radical Functions"
type: topic
aliases: ["Cube Root Function", "Nth Root Functions", "Higher Radical Functions"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-exponents-and-radicals"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "8", section: "8.3"}
related:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/algebra/Square_Root_Functions"
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/algebra/Operations_With_Radicals"
  - "topics/algebra/Power_Functions"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/algebra/Square_Root_Functions"
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: ["algebra/cube_root_function.svg"]
summary: "The cube root function f(x) = ∛x accepts every real input, including negatives — and the parity of the index decides the shape of every nth-root relative."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Cube Root and Other Radical Functions

# Cube Root and Other Radical Functions

The **cube root function** is the rule

$$
f(x) = \sqrt[3]{x},
$$

which returns the unique real number whose cube equals $x$. So $\sqrt[3]{8} = 2$ because $2^3 = 8$, and $\sqrt[3]{27} = 3$ because $3^3 = 27$. The cube root is a close cousin of the square root you met in [[Square_Root_Functions]], but it behaves very differently in one crucial way — and that difference is the whole point of this lesson.

More generally, for any positive integer $n$, the **nth root function** $f(x) = \sqrt[n]{x}$ is the inverse of raising to the $n$th power. The shape of its graph, and even the set of inputs it accepts, is decided by whether $n$ is even or odd.

![[cube_root_function.svg|The parent cube root function f(x) = ∛x]]

---

## The key contrast: odd index vs even index

Here is the single fact that separates cube roots from square roots: **a cube root is happy to eat negative numbers**.

Why? Because cubing a negative number gives a negative result. Watch: $(-2)^3 = -2 \cdot -2 \cdot -2 = -8$, so a negative answer came out of cubing a negative input. Running that backwards, $\sqrt[3]{-8} = -2$ — there is a genuine real number whose cube is $-8$. No imaginary numbers required.

Contrast that with a square root. Squaring any real number (positive or negative or zero) produces a result that is zero or positive, so $\sqrt{-8}$ has no real answer. The parity of the exponent makes all the difference.

The same split carries over to every $n$th root:

| Feature | Odd index ($n = 3, 5, 7, \dots$) | Even index ($n = 2, 4, 6, \dots$) |
|---|---|---|
| Domain | all real numbers, $(-\infty, \infty)$ | nonneg reals, $[0, \infty)$ |
| Range | all real numbers, $(-\infty, \infty)$ | nonneg reals, $[0, \infty)$ |
| Symmetry of graph | rotational symmetry about the origin | no such symmetry |
| Accepts negatives? | yes | no (not in the reals) |

So a fifth root or a seventh root acts basically like the cube root — curves through the origin and reaches into both the positive and the negative sides of the plane. A fourth root or a sixth root acts basically like the square root — a one-sided curve trapped in the first quadrant.

---

## The shape of $f(x) = \sqrt[3]{x}$

Unlike the square root curve, which starts at the origin and grows only in one direction, the cube root curve extends infinitely in both directions. It passes through these memorable points:

$$
(-8, -2), \quad (-1, -1), \quad (0, 0), \quad (1, 1), \quad (8, 2).
$$

Plot those five and the shape jumps out: a curve that rises steeply near the origin, levels off as inputs grow in either direction, and has a rotational symmetry about the origin (if you spin the graph a half turn around $(0, 0)$, you get the same picture back). Informally, the shape looks like a gently stretched "S" turned on its side.

The origin is called an **inflection point** because the curve's bend switches direction there: to the left of the origin the graph is concave up, and to the right it is concave down. Every transformation of the cube root function keeps this single anchoring feature — the inflection point is the thing that moves when you shift the graph around.

The general transformation form is

$$
f(x) = a\sqrt[3]{x - h} + k,
$$

and the three knobs do the same jobs they did for the square root: $h$ slides the inflection point right or left, $k$ lifts or drops it, and $a$ stretches, squashes, or flips the curve vertically. The one important difference is that there is nothing to restrict — the domain stays all real numbers no matter how you transform.

---

## Example 1: cube root accepts negatives

> Compute $f$ at several inputs for $f(x) = \sqrt[3]{x}$, including negative ones: $x = 8$, $x = -8$, $x = 27$, $x = -1$, $x = 0$.

Work each one as "what number cubed gives this?":

$$
f(8) = \sqrt[3]{8} = 2 \quad \text{since } 2^3 = 8.
$$

$$
f(-8) = \sqrt[3]{-8} = -2 \quad \text{since } (-2)^3 = -8.
$$

$$
f(27) = \sqrt[3]{27} = 3 \quad \text{since } 3^3 = 27.
$$

$$
f(-1) = \sqrt[3]{-1} = -1 \quad \text{since } (-1)^3 = -1.
$$

$$
f(0) = \sqrt[3]{0} = 0 \quad \text{since } 0^3 = 0.
$$

Notice how $f(8) = 2$ and $f(-8) = -2$. The outputs are opposites, just as the inputs are opposites — that is the rotational symmetry showing up in the numbers. Try the same five inputs with the square root function and you will get stuck immediately: $\sqrt{-8}$ and $\sqrt{-1}$ have no real answers at all, because no real number squared ever gives a negative.

---

## Example 2: even-index restriction

> Identify the domain and range of $g(x) = \sqrt[4]{x}$, the fourth root function. Then try to compute $g(-16)$.

The index $n = 4$ is **even**, so this behaves like the square root. You need $x \geq 0$ for the expression to land in the reals, because raising any real number to the fourth power gives a nonnegative result.

- **Domain:** $[0, \infty)$
- **Range:** $[0, \infty)$

Now the attempted evaluation: $g(-16) = \sqrt[4]{-16}$. You are asking for a real number whose fourth power equals $-16$. Squaring a real number is nonneg, and squaring again is still nonneg, so the fourth power of any real is at least $0$. No real number fits. Inside the real numbers, $g(-16)$ is undefined.

For contrast, run the cube root on the same input: $\sqrt[3]{-16}$ is a perfectly good real number (it happens to be about $-2.52$), because cubing can produce negatives.

The rule is short and worth memorizing: **even-index roots reject negatives, odd-index roots embrace them.**

---

## Example 3: transforming the cube root

> Let $h(x) = \sqrt[3]{x - 1} + 2$. Compute $h$ at a few inputs and describe the transformation from the parent cube root graph.

Identify the pieces from $a\sqrt[3]{x - h} + k$: here $a = 1$, $h = 1$, $k = 2$. The inflection point of the parent graph sat at $(0, 0)$; in the transformed graph it moves to $(h, k) = (1, 2)$.

In words: shift right $1$ unit, then up $2$ units. The shape of the curve is unchanged (no stretch, no flip), just relocated.

Evaluate at three inputs that make the radicand a perfect cube, so the arithmetic stays clean.

At $x = 1$ (the inflection point itself):

$$
h(1) = \sqrt[3]{1 - 1} + 2 = \sqrt[3]{0} + 2 = 0 + 2 = 2.
$$

At $x = 9$ (radicand becomes $8$, a perfect cube):

$$
h(9) = \sqrt[3]{9 - 1} + 2 = \sqrt[3]{8} + 2 = 2 + 2 = 4.
$$

At $x = -7$ (radicand becomes $-8$, a negative perfect cube):

$$
h(-7) = \sqrt[3]{-7 - 1} + 2 = \sqrt[3]{-8} + 2 = -2 + 2 = 0.
$$

So the three points $(1, 2)$, $(9, 4)$, and $(-7, 0)$ all sit on the graph. Plotting them confirms the curve still sweeps from lower-left to upper-right through the new inflection point at $(1, 2)$, just the way the parent swept through $(0, 0)$.

Notice the crucial feature: the input $x = -7$ is negative, and the function still produces a valid real output. Every real input is allowed, which is the hallmark of an odd-index radical.

---

## Common pitfalls

- **Assuming all radicals restrict the domain.** Only the even-index ones do. For cube roots, fifth roots, and any odd-index radical, every real number is a legal input — no need to set up an inequality.
- **Writing $\sqrt[3]{-8}$ as "undefined."** This is a leftover habit from square roots. For odd-index radicals, a negative input produces a perfectly ordinary negative output. Check it by cubing your answer.
- **Confusing $-\sqrt[3]{x}$ with $\sqrt[3]{-x}$.** These two expressions happen to give the same value here — the cube root function is what mathematicians call **odd**, meaning $f(-x) = -f(x)$ — but that coincidence does not carry over to even roots, where $\sqrt{-x}$ is usually not even defined.
- **Forgetting the inflection point instead of a starting point.** A cube root graph does not start anywhere — it extends in both directions. The anchor to move around is the inflection point at $(h, k)$, not an endpoint.

---

## Prerequisites

Before you practice, be comfortable with:

- [[Square_Roots_And_Cube_Roots]] — plain arithmetic of cube roots, including for negatives
- [[Square_Root_Functions]] — the parent template for reading transformation parameters off an equation
- [[Simplifying_Radical_Expressions]] — so higher-index radicals don't look alien
- [[Function_Basics]] — domain, range, and $f(x)$ notation

---

## Problems Involving Cube Root and Other Radical Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="cube_root_and_other_radical_functions"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Square_Root_Functions]]
- [[Simplifying_Radical_Expressions]]
- [[Operations_With_Radicals]]
- [[Power_Functions]]
- [[Inverse_Functions]]
- [[Function_Basics]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
