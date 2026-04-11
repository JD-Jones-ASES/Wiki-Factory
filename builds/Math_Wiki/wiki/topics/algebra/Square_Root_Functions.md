---
title: "Square Root Functions"
type: topic
aliases: ["Square Root Function", "Radical Function"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-exponents-and-radicals"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "4", section: "4.3"}
related:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/algebra/Operations_With_Radicals"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Cube_Root_And_Other_Radical_Functions"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/algebra/Simplifying_Radical_Expressions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: ["algebra/square_root_function.svg"]
summary: "The function f(x) = √x: a one-sided curve whose shape, starting point, and reach are controlled by three transformation numbers."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Square Root Functions

# Square Root Functions

The **square root function** is the rule that takes a number and hands you back its nonnegative square root. In symbols,

$$
f(x) = \sqrt{x}.
$$

Feed in $9$ and the machine returns $3$. Feed in $25$ and it returns $5$. Feed in $0$ and it returns $0$. The square root function is the reverse of squaring, but only for inputs that are already nonnegative — you will see why in a moment.

Because square roots sit at the heart of the [[The_Pythagorean_Theorem|Pythagorean theorem]], [[The_Quadratic_Formula|the quadratic formula]], and most distance calculations, the shape of this particular function is worth memorizing. It is not a line. It is not a parabola. It is its own creature, and once you meet it, you will recognize it everywhere.

![[square_root_function.svg|The parent square root function f(x) = √x]]

---

## Why the domain is restricted

Before anything else, ask: which inputs does this machine actually accept? The answer is the whole point of this page.

If you try to compute $\sqrt{-4}$, you are asking, "what number, multiplied by itself, equals $-4$?" No real number works. A positive times a positive is positive, a negative times a negative is also positive, and zero times itself is zero — no real number squared gives a negative result. The answer lives in the complex numbers (with an imaginary unit $i$), but at algebra-2 level we stay inside the real numbers. So $\sqrt{-4}$ is simply not defined here.

That one fact decides the entire domain and range of $f(x) = \sqrt{x}$:

- **Domain:** every $x$ that makes the stuff under the radical nonnegative. For the bare parent function, that is $x \geq 0$, or in interval notation, $[0, \infty)$.
- **Range:** by convention the square root symbol returns the nonnegative root, so $f(x) \geq 0$ for every legal input. The range is also $[0, \infty)$.

The graph therefore lives entirely in the first quadrant and along the nonnegative $x$-axis. It launches from the origin $(0, 0)$, climbs quickly at first, and then gradually flattens as the inputs grow. It never curls downward and it never crosses the $x$-axis a second time.

---

## Transformations: shifting, stretching, flipping

The real versatility of this topic comes from sliding and scaling the parent curve. The general form is

$$
f(x) = a\sqrt{x - h} + k,
$$

where each of the three numbers does one specific job.

- **$h$ (horizontal shift).** Subtracting $h$ inside the radical slides the whole graph right by $h$ units. A positive $h$ moves the starting point right; a negative $h$ moves it left. The new starting $x$-value is wherever the radicand is zero, so solve $x - h = 0$ to find it.
- **$k$ (vertical shift).** Adding $k$ outside the radical lifts the graph up by $k$ units. A negative $k$ drops it down.
- **$a$ (stretch and reflection).** Multiplying the whole radical by $a$ stretches the graph vertically if $|a| > 1$ and squashes it if $|a| < 1$. A negative $a$ flips the curve upside down — it now starts at the same point but heads down instead of up.

The starting point of the transformed graph — sometimes called the endpoint or anchor — is always $(h, k)$. Knowing that single fact unlocks almost every transformation problem. Once you plot that anchor, pick a couple of clean inputs (like $x = h + 1$, $x = h + 4$, $x = h + 9$, where the radicand becomes a perfect square) and the rest of the curve falls into place.

The **domain** of $a\sqrt{x - h} + k$ is $x \geq h$. The **range** depends on the sign of $a$: if $a > 0$, outputs run from $k$ upward ($y \geq k$); if $a < 0$, outputs run from $k$ downward ($y \leq k$).

---

## Example 1: reading a square-root function from its form

> Identify the domain, range, and starting point of $f(x) = \sqrt{x - 4} + 1$.

Match the form $a\sqrt{x - h} + k$ term by term. Here $a = 1$, $h = 4$, $k = 1$.

**Starting point:** $(h, k) = (4, 1)$. That is where the radicand equals zero and the graph launches.

**Domain:** the radicand $x - 4$ must be nonnegative, so $x - 4 \geq 0$, giving $x \geq 4$. In interval notation: $[4, \infty)$.

**Range:** since $a = 1$ is positive, outputs climb from the starting height $1$ upward. So $f(x) \geq 1$, or $[1, \infty)$.

As a sanity check, try a clean input: $f(13) = \sqrt{13 - 4} + 1 = \sqrt{9} + 1 = 3 + 1 = 4$. The point $(13, 4)$ sits on the graph, well above the starting point $(4, 1)$ — exactly the behavior we expected.

---

## Example 2: building a table and plotting

> Let $g(x) = 2\sqrt{x}$. Compute $g$ at the perfect squares $0, 1, 4, 9, 16$ and describe how the graph compares to the parent $y = \sqrt{x}$.

Plug the perfect squares in one at a time.

$$
g(0) = 2\sqrt{0} = 0
$$

$$
g(1) = 2\sqrt{1} = 2
$$

$$
g(4) = 2\sqrt{4} = 2 \cdot 2 = 4
$$

$$
g(9) = 2\sqrt{9} = 2 \cdot 3 = 6
$$

$$
g(16) = 2\sqrt{16} = 2 \cdot 4 = 8
$$

So the five plotted points are $(0, 0), (1, 2), (4, 4), (9, 6), (16, 8)$.

Compare these outputs to the parent $y = \sqrt{x}$, which would give $0, 1, 2, 3, 4$ at the same inputs. Every output from $g$ is exactly twice as tall. That is the vertical stretch by a factor of $a = 2$ in action — the curve starts at the same place (the origin) but climbs twice as fast.

The domain is unchanged: $x \geq 0$. The range is also $[0, \infty)$, since doubling a nonnegative number is still nonnegative.

---

## Example 3: a reflection

> Describe how $h(x) = -\sqrt{x + 3}$ transforms the parent graph. Give the starting point, domain, and range.

Read off the form: $a = -1$, $h = -3$, $k = 0$. The starting point is $(h, k) = (-3, 0)$.

The radicand $x + 3$ must be nonnegative, so $x \geq -3$. The domain is $[-3, \infty)$.

Because $a = -1$ is negative, the entire curve flips below the $x$-axis. Instead of launching up and to the right from $(-3, 0)$, it launches down and to the right. Outputs are never positive — they run from $0$ downward — so the range is $(-\infty, 0]$.

Check with one point: $h(-3 + 1) = h(-2) = -\sqrt{-2 + 3} = -\sqrt{1} = -1$. The point $(-2, -1)$ lies on the graph, just below and to the right of the starting anchor. That matches the flipped-down orientation.

---

## Inverse relationship to squaring

The square root function and the squaring function are mirror images of each other — but only on a restricted piece. Remember that squaring sends both $3$ and $-3$ to $9$, so it is not a one-to-one function on the full real line. To make squaring reversible, you have to chop off the left half and keep only inputs with $x \geq 0$.

Once you do, the pair $f(x) = x^2$ (with domain restricted to $[0, \infty)$) and $g(x) = \sqrt{x}$ are true inverses of each other. Composing them in either order gives back the original input:

$$
\sqrt{x^2} = x \quad (\text{when } x \geq 0), \qquad (\sqrt{x})^2 = x \quad (\text{when } x \geq 0).
$$

Graphically, the two curves reflect across the line $y = x$. The square root curve is exactly the right-hand branch of a sideways parabola. This observation is the gateway to [[Inverse_Functions|inverse functions]] as a general topic.

---

## Common pitfalls

- **Missing the domain restriction.** The number one mistake is treating $\sqrt{x - 4}$ like an ordinary polynomial and plugging in any input. Always start by asking which $x$ values make the radicand nonnegative.
- **Forgetting the sign of $h$.** The form is $\sqrt{x - h}$, so the equation $\sqrt{x + 3}$ has $h = -3$, not $h = +3$. The starting point shifts left, not right.
- **Thinking $\sqrt{x}$ can be negative.** By convention the radical symbol stands for the nonnegative root. If a problem wants both roots (like when solving $x^2 = 25$), it has to write $\pm\sqrt{25}$ explicitly.
- **Confusing a vertical stretch with a horizontal one.** Multiplying on the outside — $2\sqrt{x}$ — doubles every output height. Multiplying inside — $\sqrt{2x}$ — compresses the curve horizontally instead. They produce different graphs.

---

## Prerequisites

Before practicing, make sure you are comfortable with:

- [[Square_Roots_And_Cube_Roots]] — knowing what $\sqrt{x}$ even means for a plain number
- [[Simplifying_Radical_Expressions]] — so radicals inside the function don't trip you up
- [[Function_Basics]] — notation like $f(x)$, domain, range, and graphs
- [[Linear_Functions]] — the template for reading transformations off an equation

---

## Problems Involving Square Root Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="square_root_functions"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Cube_Root_And_Other_Radical_Functions]]
- [[Simplifying_Radical_Expressions]]
- [[Operations_With_Radicals]]
- [[Quadratic_Functions]]
- [[Inverse_Functions]]
- [[Function_Basics]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
