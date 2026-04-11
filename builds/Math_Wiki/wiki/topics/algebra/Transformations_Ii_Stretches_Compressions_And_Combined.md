---
title: "Transformations II: Stretches, Compressions, and Combined"
type: topic
aliases: ["Stretches and Compressions", "Combined Transformations"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-transformations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "8", section: "8.2"}
related:
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Absolute_Value_Functions"
  - "topics/algebra/Square_Root_Functions"
  - "topics/algebra/Function_Basics"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Quadratic_Functions"
problem_type_ids: []
figures: []
summary: "Stretching, squeezing, and putting all four transformation moves together in one formula."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Transformations II: Stretches, Compressions, and Combined

# Transformations II: Stretches, Compressions, and Combined

[[Transformations_I_Shifts_And_Reflections|Part I]] introduced four ways to move a parent graph without reshaping it: slide horizontally, slide vertically, reflect across the x-axis, reflect across the y-axis. Those moves preserved the exact shape of the curve — they just repositioned it or mirrored it. This page adds two more moves that actually change the proportions: **vertical stretches and compressions**, which make the graph taller or shorter, and **horizontal stretches and compressions**, which make the graph skinnier or wider. Then we put everything together into one master formula.

---

## Vertical stretches and compressions

Multiplying the whole function by a constant $a$ produces

$$
g(x) = a \cdot f(x).
$$

Every output of the parent gets scaled by $a$. If $f(3) = 5$, then $g(3) = 5a$.

There are three cases to keep straight:

- **$|a| > 1$**: every output grows in magnitude, so the graph gets **taller**. This is a vertical **stretch** by a factor of $|a|$. A point that was two units above the x-axis ends up $2|a|$ units above.
- **$0 < |a| < 1$**: every output shrinks, so the graph gets **shorter**. This is a vertical **compression** by the factor $|a|$.
- **$a < 0$**: the vertical stretch or compression is combined with a reflection across the x-axis, because the sign of every output flips.

So $g(x) = 3x^2$ is the parabola $x^2$ pulled upward to three times its usual height at every $x$. And $g(x) = -\tfrac{1}{2}x^2$ is the same parabola squished to half its height and then flipped upside down.

---

## Horizontal stretches and compressions (backwards again)

Multiplying the **input** by a constant $b$ produces

$$
g(x) = f(bx).
$$

This looks similar to the vertical case, but its effect on the graph runs in the opposite direction — yes, horizontal transformations are backwards yet again, and for the same reason the horizontal shifts were. You're asking the parent what it does at a scaled input.

- **$|b| > 1$**: the graph gets **narrower**, squeezed toward the y-axis, compressed by a factor of $1/|b|$. A point that used to sit at $x = 6$ is now found at $x = 6/b$.
- **$0 < |b| < 1$**: the graph gets **wider**, stretched away from the y-axis, by a factor of $1/|b|$.
- **$b < 0$**: on top of the stretch or compression, the graph is reflected across the y-axis.

A parabola $y = (2x)^2 = 4x^2$ is narrower than the parent $x^2$ — it grows faster for the same input. A parabola $y = (x/2)^2 = x^2 / 4$ is wider, growing more slowly.

Note that $(2x)^2$ and $4x^2$ happen to agree for the quadratic parent, so you could mistakenly call this a vertical stretch by 4 or a horizontal compression by 1/2 — both descriptions land on the same graph. For most functions the two moves produce genuinely different pictures, so learn to tell them apart.

---

## The combined form

All four moves together become one template:

$$
g(x) = a \cdot f\bigl(b(x - h)\bigr) + k
$$

The four constants each play a specific role:

- $h$: horizontal shift (positive $h$ moves right)
- $k$: vertical shift (positive $k$ moves up)
- $a$: vertical stretch or compression (with reflection if $a < 0$)
- $b$: horizontal stretch or compression (with reflection if $b < 0$)

The order that matters when applying these by hand is: horizontal moves first (dealing with $b$ and $h$ on the inside), then vertical moves (dealing with $a$ and $k$ on the outside). In other words, do everything attached to the $x$ before you do anything attached to the output.

---

## Example 1: pure vertical scaling of a parabola

> Compare $g(x) = 2x^2$ and $h(x) = \dfrac{1}{3} x^2$ to the parent $f(x) = x^2$.

For $g(x) = 2x^2$, the outside constant is $a = 2$. Every output doubles. The point $(1, 1)$ on the parent becomes $(1, 2)$ on $g$; the point $(2, 4)$ becomes $(2, 8)$. The new parabola is twice as tall everywhere, which makes it look **narrower** compared to the parent — it climbs faster.

For $h(x) = \tfrac{1}{3}x^2$, the outside constant is $a = \tfrac{1}{3}$, between 0 and 1. Every output shrinks to a third. The point $(3, 9)$ on the parent becomes $(3, 3)$ on $h$. The new parabola is only one-third as tall, so it looks **wider** — it climbs much more slowly.

Both graphs still pass through the origin (because $2 \cdot 0 = 0$ and $\tfrac{1}{3} \cdot 0 = 0$), and both still open upward.

---

## Example 2: horizontal scaling with the counterintuitive direction

> Compare $g(x) = (2x)^2$ and $h(x) = (x/2)^2$ to the parent $f(x) = x^2$.

For $g(x) = (2x)^2$, the inside constant is $b = 2$. Horizontal transformations run backwards, so multiplying the input by $2$ **compresses** the graph horizontally by a factor of $1/2$. A point that used to live at $x = 4$ now needs an input of only $x = 2$ to reach the same height. The parabola gets pulled in toward the y-axis, looking narrower.

For $h(x) = (x/2)^2$, the inside constant is $b = 1/2$, less than one. Multiplying by a small number horizontally **stretches** the graph outward by a factor of $2$. The point that used to be at $x = 2$ on the parent has migrated to $x = 4$. The parabola gets pushed away from the y-axis and looks wider.

If you compute the two formulas: $(2x)^2 = 4x^2$ and $(x/2)^2 = x^2/4$. For the quadratic family, the two descriptions overlap — a horizontal compression by $1/2$ is numerically the same as a vertical stretch by $4$. That coincidence is special to the parabola. For a function like $\sqrt{x}$, the two moves produce visibly different graphs.

---

## Example 3: all four moves applied to the parabola

> Describe the graph of $g(x) = -2(x - 3)^2 + 5$ in terms of transformations applied to $f(x) = x^2$.

Match against the combined form $g(x) = a \cdot f(b(x - h)) + k$. Here $a = -2$, $b = 1$, $h = 3$, and $k = 5$.

Apply the moves one at a time, inside first:

1. **Horizontal shift**: $h = 3$ slides the graph three units to the **right**. The parent's vertex $(0, 0)$ moves to $(3, 0)$.
2. **Horizontal stretch/compression**: $b = 1$, so nothing happens horizontally beyond the shift.
3. **Vertical stretch and reflection**: $a = -2$ scales every output by $2$ and flips the sign. The graph is now twice as tall and opens downward instead of upward.
4. **Vertical shift**: $k = 5$ lifts the whole picture five units up. The vertex, which was at $(3, 0)$ after the shift, ends up at $(3, 5)$.

Final result: a parabola opening **downward** with its peak (now a maximum) at $(3, 5)$, twice as steep as the parent. Symbolically that matches $g(x) = -2(x - 3)^2 + 5$, which is already in vertex form, confirming the vertex is at $(3, 5)$.

---

## Common pitfalls

- **Confusing horizontal and vertical stretches.** The outside constant $a$ changes heights; the inside constant $b$ changes widths (and runs backwards). Mixing them up inverts the picture.
- **Forgetting the reflection when $a$ or $b$ is negative.** $a = -2$ is both a stretch by $2$ **and** a flip across the x-axis; don't apply only one half of it.
- **Applying the shift before the stretch and getting the wrong endpoint.** The combined form is $a \cdot f(b(x - h)) + k$. If you expand $b(x - h)$ by distributing $b$ first, you can accidentally double-count either move. Keep $(x - h)$ inside its own parentheses until you've identified $h$.
- **Thinking $(2x)^2 = 4x^2$ is a general rule.** For the parabola, a horizontal compression numerically coincides with a vertical stretch. For most other parent functions, the two are distinct — don't carry the coincidence over.

---

## Prerequisites

- [[Transformations_I_Shifts_And_Reflections]] — the shifts and reflections that this page builds on
- [[Function_Basics]] — function notation and evaluation
- [[Quadratic_Functions]] — the test-bench parent for most transformation examples

---

## Problems Involving Transformations II

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="transformations_ii_stretches_compressions_and_combined"></div>

---

## See Also

- [[Transformations_I_Shifts_And_Reflections]] — the first half of the transformation toolkit
- [[Quadratic_Functions]] — vertex form is the combined-transformation form for parabolas
- [[Absolute_Value_Functions]] — stretched V-shapes
- [[Square_Root_Functions]] — horizontal stretches look very different from vertical ones here
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
