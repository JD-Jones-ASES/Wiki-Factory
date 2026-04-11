---
title: "Inverse Trigonometric Functions"
type: topic
aliases: ["Arcsine", "Arccosine", "Arctangent", "Arc Trig", "Inverse Trig"]
tags: ["#branch-pre-calculus", "#topic-unit-circle", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.2"}
related:
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/precalculus/Trigonometric_Equations"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/algebra/Inverse_Functions"
problem_type_ids: []
figures: []
summary: "Arcsin, arccos, and arctan undo sine, cosine, and tangent — but only after restricting the domain of each trig function to a stretch where it's one-to-one."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Inverse Trigonometric Functions

# Inverse Trigonometric Functions

Inverse functions are always about undoing. If a function takes in an input and produces an output, its inverse takes in an output and hands you back the input that produced it. So far so good — except trig functions run into an immediate obstacle. Sine, cosine, and tangent are not one-to-one. Infinitely many different angles produce the same sine value. The equation $\sin\theta = 1/2$ has solutions at $\theta = \pi/6$, $\theta = 5\pi/6$, $\theta = 13\pi/6$, and countless more. If you ask "what angle has sine equal to $1/2$?", the honest answer is "which of the infinitely many do you want?"

That failure of one-to-one-ness would normally mean no inverse function exists at all. But there is a standard rescue: cut the input domain of the original function down to a stretch where it **is** one-to-one, and define the inverse on that restricted piece. The result is not a true inverse of the whole trig function — it is a partial inverse that agrees with the trig function on a specific, carefully chosen interval. The outputs of these partial inverses are called **principal values**.

$$
\arcsin x,\; \arccos x,\; \arctan x \;\text{ all return angles, not ratios.}
$$

Burn that sentence into your brain. A common beginner error is to look at $\arccos(1/2)$ and think "oh, that's a number like $0.5$". It is not — it is an angle, and the angle is $\pi/3$ radians.

---

## Why domain restriction is the whole idea

Picture the sine graph from the [[Graphs_Of_Trigonometric_Functions]] page. It is a wave that moves up to $1$, back down through zero, down to $-1$, back up, and keeps repeating. A horizontal line drawn anywhere between $y = -1$ and $y = 1$ crosses that wave infinitely many times. By the horizontal line test, sine has no inverse on its full domain.

The fix: find a piece of the sine curve where the wave climbs monotonically from $-1$ to $1$ without repeating. The standard choice is the interval $[-\pi/2,\; \pi/2]$, which starts at the trough $(-\pi/2,\; -1)$, climbs through the origin, and ends at the peak $(\pi/2,\; 1)$. On this stretch, every output value between $-1$ and $1$ is hit exactly once, so the restricted function **does** have an inverse. That inverse is $\arcsin$.

The analogous choice for cosine is the interval $[0,\; \pi]$, where the cosine graph drops monotonically from $\cos(0) = 1$ to $\cos(\pi) = -1$. And for tangent, where the graph has vertical asymptotes, the chosen interval is the open stretch $(-\pi/2,\; \pi/2)$ — the branch of tangent that passes through the origin and climbs from $-\infty$ to $+\infty$ between the two asymptotes.

Each of these intervals is called the **principal value range** of the corresponding inverse trig function. Whenever you compute $\arcsin x$, $\arccos x$, or $\arctan x$, the answer must lie in the principal value range — any other correct angle is not the one the inverse function hands back.

---

## The three main inverse trig functions

| Function | Domain | Range (principal values) |
|---|---|---|
| $\arcsin x$ | $[-1,\; 1]$ | $[-\pi/2,\; \pi/2]$ |
| $\arccos x$ | $[-1,\; 1]$ | $[0,\; \pi]$ |
| $\arctan x$ | $(-\infty,\; \infty)$ | $(-\pi/2,\; \pi/2)$ |

A few facts fall out of this table:

- **Domain of arcsin and arccos is $[-1, 1]$.** You cannot take the arcsin of $2$. Since sine never outputs a value outside $[-1, 1]$, no angle has sine equal to $2$, and the expression $\arcsin(2)$ is undefined.
- **Domain of arctan is all of $\mathbb{R}$.** Tangent covers every real number as an output, so arctan accepts every real number as an input.
- **Arcsin outputs are in the fourth and first quadrants** ($-\pi/2$ to $\pi/2$). Never the second or third.
- **Arccos outputs are in the first and second quadrants** ($0$ to $\pi$). Never the third or fourth.
- **Arctan outputs are in the fourth and first quadrants**, and the endpoints are excluded because the tangent has asymptotes there.

Alternative notation you will see: $\sin^{-1} x$ means $\arcsin x$, $\cos^{-1} x$ means $\arccos x$, and $\tan^{-1} x$ means $\arctan x$. Be careful — the superscript $-1$ here is **not** an exponent. The expression $\sin^{-1}(1/2)$ is $\pi/6$, not $1/\sin(1/2)$.

---

## Key ideas

- **The output is always an angle.** Whenever you see $\arcsin$, $\arccos$, or $\arctan$ in a problem, the result has to be an angle measure — in radians throughout pre-calculus and calculus.
- **Only the principal value.** Out of infinitely many angles that satisfy $\sin\theta = k$, only the one in $[-\pi/2,\; \pi/2]$ is the value of $\arcsin(k)$.
- **Inputs live in the correct domain.** You cannot take arcsin or arccos of a number with absolute value greater than $1$. Arctan is more forgiving and accepts anything.
- **Composition rules are one-sided.** Feeding a number in and out works cleanly only on the restricted interval. For example, $\sin(\arcsin x) = x$ for every $x$ in $[-1, 1]$, but $\arcsin(\sin x) = x$ only if $x$ is already in $[-\pi/2,\; \pi/2]$.
- **Graphs mirror the restricted originals.** The graph of $y = \arcsin x$ is the reflection of the sine curve's restricted piece across the line $y = x$. Same trick for arccos and arctan.

---

## Example 1: Computing $\arcsin(1/2)$ and resisting the trap

> Find the exact value of $\arcsin(1/2)$.

You are looking for the angle whose sine is $1/2$ **and** which lies in the principal value range $[-\pi/2,\; \pi/2]$.

The equation $\sin\theta = 1/2$ has two solutions inside $[0, 2\pi)$: $\theta = \pi/6$ and $\theta = 5\pi/6$. But $5\pi/6$ is not in $[-\pi/2,\; \pi/2]$, so it is disqualified. Only $\pi/6$ survives.

$$
\arcsin\!\left(\dfrac{1}{2}\right) = \dfrac{\pi}{6}.
$$

The answer is a single angle, not the whole family of angles with sine $1/2$. Don't list more than one — the inverse function, by definition, can only hand you one value.

---

## Example 2: Computing $\arccos(-\sqrt{2}/2)$

> Find the exact value of $\arccos(-\sqrt{2}/2)$.

Now you want the angle whose cosine is $-\sqrt{2}/2$ **and** which lies in $[0,\; \pi]$.

The reference angle with cosine value $\sqrt{2}/2$ is $\pi/4$. Since the target value is negative, the angle must live in a quadrant where cosine is negative — that is, quadrant II or quadrant III. The arccos range $[0, \pi]$ only includes angles from quadrant I and quadrant II, so the only quadrant II angle with reference angle $\pi/4$ is:

$$
\arccos\!\left(-\dfrac{\sqrt{2}}{2}\right) = \pi - \dfrac{\pi}{4} = \dfrac{3\pi}{4}.
$$

That angle sits comfortably inside $[0, \pi]$, and its cosine really is $-\sqrt{2}/2$. Done.

---

## Example 3: Computing $\arctan(\sqrt{3})$ and watching the range

> Find the exact value of $\arctan(\sqrt{3})$.

You want the angle whose tangent is $\sqrt{3}$, and it must live strictly inside $(-\pi/2,\; \pi/2)$.

Think back to the special-angle values. From the unit circle, $\sin(\pi/3) = \sqrt{3}/2$ and $\cos(\pi/3) = 1/2$, so $\tan(\pi/3) = (\sqrt{3}/2) / (1/2) = \sqrt{3}$. That angle is in the first quadrant, which is safely inside the arctan principal value range. No correction needed.

$$
\arctan(\sqrt{3}) = \dfrac{\pi}{3}.
$$

Notice that arctan is doing the work of two translations at once: it undoes the tangent, and it picks the single angle inside its range that gives the requested ratio. Any angle coterminal with $\pi/3$ — say $\pi/3 + \pi = 4\pi/3$ — also has tangent $\sqrt{3}$, but it falls outside $(-\pi/2,\; \pi/2)$ and is not what arctan returns.

---

## Common pitfalls

- **Treating the answer as a ratio instead of an angle.** If a problem says "compute $\arccos(-1/2)$" and your answer looks like a number between $0$ and $1$, stop. The output must be an angle measure — here it is $2\pi/3$ radians.
- **Listing every matching angle.** Inverse trig functions are single-valued. $\arcsin(1/2) = \pi/6$ and only $\pi/6$, never the pair $\pi/6$ and $5\pi/6$. Save the multi-angle answer for trig **equations**, not for inverse **function** evaluations.
- **Ignoring the principal range.** When the raw-matching angle lives outside the principal range, subtract or reflect it into the correct range instead of writing it down unchanged.
- **Confusing $\sin^{-1} x$ with $(\sin x)^{-1} = 1/\sin x$.** The $-1$ superscript in $\sin^{-1}$ is a notational convention for the inverse function, not an exponent. The reciprocal of $\sin x$ is $\csc x$, which is a completely different animal.
- **Feeding arcsin or arccos a number outside $[-1, 1]$.** If you see $\arcsin(2)$ in your work, something earlier in the problem went wrong — the expression has no value.

---

## Prerequisites

- [[Circular_Functions]] — you cannot invert a function whose own definition you haven't seen yet
- [[The_Unit_Circle]] — every example on this page uses exact special-angle values
- [[Inverse_Functions]] — the general framework of domain restriction and the $y = x$ reflection carries directly over

---

## Problems Involving Inverse Trigonometric Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="inverse_trigonometric_functions"></div>

---

## See Also

- [[Circular_Functions]] — the functions being inverted
- [[The_Unit_Circle]] — where the exact values come from
- [[Graphs_Of_Trigonometric_Functions]] — the restricted pieces that define the inverses
- [[Trigonometric_Equations]] — when you want every solution, not just the principal one
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
</content>
