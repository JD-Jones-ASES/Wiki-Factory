---
title: "Transformations I: Shifts and Reflections"
type: topic
aliases: ["Shifts and Reflections", "Function Shifts"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-transformations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "8", section: "8.1"}
related:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Absolute_Value_Functions"
  - "topics/algebra/Square_Root_Functions"
  - "topics/algebra/Transformations_Ii_Stretches_Compressions_And_Combined"
  - "topics/algebra/Function_Basics"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Absolute_Value_Functions"
problem_type_ids: []
figures: ["algebra/transformation_shifts.svg"]
summary: "Turning a parent function into a new one by sliding it around and flipping it."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Transformations I: Shifts and Reflections

# Transformations I: Shifts and Reflections

Every function family — parabolas, V-shapes, square roots, reciprocals — has one plain version that sits at the origin with no stretching and no moving. That plain version is called the **parent function**. Everything else in the family is that parent picked up, slid around, and maybe flipped over. Once you get comfortable with the four basic moves — shift horizontally, shift vertically, reflect across the x-axis, reflect across the y-axis — you can describe an enormous zoo of functions without ever plotting a single table of values.

This page is only about the sliding and flipping. Stretching and squishing will come next, in [[Transformations_Ii_Stretches_Compressions_And_Combined]].

![[transformation_shifts.svg|Three shifts of the parent parabola]]

---

## The four moves in symbols

Start with some parent function $f(x)$. The transformed function looks like one of these:

$$
g(x) = f(x - h) + k
$$

$$
g(x) = -f(x)
$$

$$
g(x) = f(-x)
$$

The first form handles both shifts at once: $h$ slides the graph horizontally and $k$ slides it vertically. The second form reflects the graph across the x-axis. The third reflects it across the y-axis.

---

## Vertical shifts are the intuitive ones

The $k$ in $f(x) + k$ simply adds the same number to every output. If the parent sends $3$ to $9$, the transformed function sends $3$ to $9 + k$. Every point on the graph moves up by $k$ units (or down, if $k$ is negative). That is exactly what "shift up by $k$" ought to mean.

So $g(x) = x^2 + 4$ is the parabola $y = x^2$ bodily lifted four units off its old home. The new vertex is at $(0, 4)$ instead of $(0, 0)$. Nothing else changes — same width, same direction, same symmetry.

---

## Horizontal shifts look backwards and there's a reason

Here is where students first get tripped up. The graph of

$$
g(x) = f(x - 3)
$$

is the parent graph slid **three units to the right**, not to the left, even though the formula has a minus sign. Every textbook says this and every student silently suspects there's been a typo.

The cleanest way to see why is to ask: **where does the new graph have the value the old graph had at zero?** The old graph had $f(0)$ at $x = 0$. The new graph $g(x) = f(x - 3)$ has $g(3) = f(3 - 3) = f(0)$. So the thing that used to live at $x = 0$ now lives at $x = 3$. The whole picture slid to the right.

Same rule in reverse: $g(x) = f(x + 2)$ slides the graph two units to the **left**. Inside the parentheses, the sign always opposes the direction your gut expects.

---

## Reflections are simpler

Stick a minus sign in front of the whole function — $-f(x)$ — and every output gets negated. Points that were above the x-axis end up below it, and vice versa. That's a reflection across the x-axis, and the graph looks like the original flipped upside down.

Stick a minus sign inside, on the input — $f(-x)$ — and you're asking the parent what it does with the opposite input. A point that was three units to the right of the y-axis now ends up at the same height three units to the **left**. That's a reflection across the y-axis, flipping the graph left-to-right.

One way to keep the two straight: **outside minus flips vertically, inside minus flips horizontally**. Or remember that the minus sign acts on the coordinate closest to it.

---

## Example 1: shifting a parabola

> Starting from the parent $f(x) = x^2$, describe the graph of $g(x) = (x - 4)^2 + 3$.

Match against the general form $f(x - h) + k$. The $x - 4$ inside tells you $h = 4$, so the graph slides **four units to the right**. The $+ 3$ on the outside tells you $k = 3$, so it also slides **three units up**.

The parent's vertex was at $(0, 0)$. The transformed vertex is at

$$
(0 + 4, \ 0 + 3) = (4, 3).
$$

Everything else about the parabola stays identical: it still opens upward, still has the same width, still has an axis of symmetry — just through $x = 4$ now instead of $x = 0$.

---

## Example 2: reflecting the absolute-value parent

> Compare the graphs of $g(x) = -|x|$ and $h(x) = |-x|$ to the parent $f(x) = |x|$.

For $g(x) = -|x|$, the minus is **outside**. Every output of the parent gets flipped in sign. The parent's V opens upward from $(0, 0)$; the reflection opens **downward** from $(0, 0)$ and looks like an upside-down V.

For $h(x) = |-x|$, the minus is **inside**. The parent has the property that $|{-x}| = |x|$ already, which means this "reflection" actually leaves the graph unchanged. The absolute-value parent is symmetric about the y-axis, so flipping it across the y-axis gives you the same picture back. Not every reflection matters; sometimes the function was already symmetric.

If we had done the same move to $f(x) = \sqrt{x}$, we would have gotten a genuinely different graph: $\sqrt{-x}$ is defined only for $x \leq 0$ and produces the left-hand mirror image of the usual square-root curve.

---

## Example 3: combining a shift with a reflection

> Describe the graph of $g(x) = -|x + 2| - 1$ as a series of moves applied to the parent $f(x) = |x|$.

Read the formula from the inside out.

1. $|x + 2|$ — the inside says $x + 2$, which is $x - (-2)$, so $h = -2$. That slides the V **two units to the left**. New vertex: $(-2, 0)$.
2. $-|x + 2|$ — the outside minus flips the whole picture upside down across the x-axis. The V now opens downward from $(-2, 0)$.
3. $-|x + 2| - 1$ — finally, subtract $1$ from every output. The entire graph drops **one unit**. New vertex: $(-2, -1)$.

The final picture is a downward-opening V with its peak at $(-2, -1)$, its two arms sloping away at the same steepness as the parent.

---

## Common pitfalls

- **Reading the horizontal shift in the wrong direction.** $f(x - 5)$ moves the graph right by $5$, not left. When you see a minus sign inside, the shift goes toward the positive side of the axis.
- **Mixing up the two kinds of minus sign.** Outside the function: $-f(x)$ reflects vertically. Inside the function: $f(-x)$ reflects horizontally. They produce different pictures (unless the parent is symmetric).
- **Forgetting to move the key landmarks.** If the parent had a vertex, x-intercept, or asymptote, the transformed graph has the same landmark shifted the same way. When you shift by $(h, k)$, every labeled point moves by $(h, k)$.
- **Trying to shift before reflecting, or vice versa, without a plan.** Apply one move at a time, updating your mental picture after each step. Rushing the order is how students lose the sign on an intercept.

---

## Prerequisites

- [[Function_Basics]] — you need to be comfortable with function notation before transformations make sense
- [[Quadratic_Functions]] — the parabola is the most common parent you'll be transforming
- [[Absolute_Value_Functions]] — the V is the second most common; its sharp vertex makes the transformations easy to see

---

## Problems Involving Transformations I

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="transformations_i_shifts_and_reflections"></div>

---

## See Also

- [[Transformations_Ii_Stretches_Compressions_And_Combined]] — the other half of the transformation story
- [[Quadratic_Functions]] — vertex form is transformation-in-action for the parabola family
- [[Absolute_Value_Functions]] — easy shifts and reflections to visualize
- [[Square_Root_Functions]] — shifts to the square-root parent
- [[Cube_Root_And_Other_Radical_Functions]] — odd-root transformations
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
