---
title: "Trigonometric Equations"
type: topic
aliases: ["Trig Equations", "Solving Trigonometric Equations"]
tags: ["#branch-pre-calculus", "#topic-trig-equations", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.6"}
related:
  - "topics/precalculus/Identities"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Identities"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
problem_type_ids: []
figures: []
summary: "Find the angles that make a trig equation true; a single angle always expands into an infinite periodic family."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Trigonometric Equations

# Trigonometric Equations

A **trigonometric equation** is any equation whose unknown sits inside one or more trig functions. Unlike the [[Identities]] of the previous section, which are true for every angle, a trig equation is a genuine question: for which angles does the statement hold?

The answer almost always comes in two pieces. First you locate the angles in one full revolution of the unit circle that satisfy the equation — there are usually one or two of them. Then you tack on the periodic tail: sine and cosine repeat every $2\pi$, tangent repeats every $\pi$, so every solution you find spawns a whole family.

$$
\sin x = \dfrac{1}{2} \quad\Longrightarrow\quad x = \dfrac{\pi}{6} + 2k\pi \;\text{ or }\; x = \dfrac{5\pi}{6} + 2k\pi, \quad k \in \mathbb{Z}.
$$

The integer $k$ is the bookkeeping for "how many full rotations ahead or behind". Skipping that tail is the most common way students lose points on these problems.

---

## The basic move: start at the unit circle

For simple equations like $\cos x = \dfrac{\sqrt{3}}{2}$ or $\tan x = 1$, the strategy is to ask the unit circle directly. Where does the $x$-coordinate equal $\dfrac{\sqrt{3}}{2}$? Two places: at $x = \dfrac{\pi}{6}$ and at $x = -\dfrac{\pi}{6}$ (or equivalently $x = \dfrac{11\pi}{6}$). Then you add the period: every solution can be written as $x = \pm \dfrac{\pi}{6} + 2k\pi$.

A clean way to organize the work is:

1. Isolate the trig function so you have something like $\sin x = c$, $\cos x = c$, or $\tan x = c$ with a plain number on the right.
2. Find one reference angle whose sine, cosine, or tangent equals $|c|$.
3. Use the sign of $c$ and the rules about quadrants to place that reference angle in the right two (or one, for tangent) spots on the unit circle.
4. Add the period — $2\pi k$ for sine and cosine, $\pi k$ for tangent — to generate the full solution set.
5. If the problem asks for solutions on a restricted interval such as $[0, 2\pi)$, walk through the periodic family and list only the values that land inside the window.

---

## Equations that use an identity first

Many trig equations are not simple enough to attack directly. They mix sine and cosine, or they involve $\sin^{2}x$, or they have a double-angle term. The fix is to rewrite the equation using an identity until only one trig function of one angle remains. Then the basic move above does the rest.

Common rewrites:

- **Pythagorean swap.** If you see $\sin^{2}x$ and you already have a $\cos x$ in the equation, replace $\sin^{2}x$ with $1 - \cos^{2}x$. Now everything is in one function.
- **Double-angle break-up.** A $\sin(2x)$ can become $2\sin x\cos x$, which often factors nicely with whatever else is present.
- **Quadratic in disguise.** An expression such as $2\sin^{2}x - \sin x - 1 = 0$ looks like a trig equation but is a quadratic in the substitution $u = \sin x$. Factor it as $(2u + 1)(u - 1) = 0$, solve for $u$, then solve $\sin x = u$ for each value separately.

The thinking here is the same as in [[Logarithmic_Equations]] from the algebra side — use the rules of your function family to collapse the messy version down to a simple version, then let the simple version hand you the answer.

---

## Example 1: a straight unit-circle lookup

> Find every value of $x$ in $[0, 2\pi)$ with $2\cos x - 1 = 0$.

Isolate $\cos x$:

$$
2\cos x = 1 \quad\Longrightarrow\quad \cos x = \dfrac{1}{2}.
$$

Ask the unit circle where the $x$-coordinate equals $\dfrac{1}{2}$. Two places: $x = \dfrac{\pi}{3}$ in Quadrant I and $x = \dfrac{5\pi}{3}$ in Quadrant IV. Both lie inside the interval $[0, 2\pi)$.

**Solutions on $[0, 2\pi)$:** $x = \dfrac{\pi}{3}$ and $x = \dfrac{5\pi}{3}$.

If the question asked for *all* solutions, tack on the period: $x = \dfrac{\pi}{3} + 2k\pi$ or $x = \dfrac{5\pi}{3} + 2k\pi$ for any integer $k$.

---

## Example 2: factoring a quadratic in sine

> Determine every $x$ in $[0, 2\pi)$ that satisfies $2\sin^{2}x - \sin x - 1 = 0$.

Substitute $u = \sin x$ to make the structure visible:

$$
2u^{2} - u - 1 = 0.
$$

Factor: $(2u + 1)(u - 1) = 0$, so $u = -\dfrac{1}{2}$ or $u = 1$.

Translate back. For $\sin x = -\dfrac{1}{2}$, the unit circle gives $x = \dfrac{7\pi}{6}$ and $x = \dfrac{11\pi}{6}$ (both in Quadrants III and IV, where sine is negative). For $\sin x = 1$, the only answer in one full turn is $x = \dfrac{\pi}{2}$.

**Solutions on $[0, 2\pi)$:** $x = \dfrac{\pi}{2}$, $\dfrac{7\pi}{6}$, $\dfrac{11\pi}{6}$.

---

## Example 3: using a Pythagorean rewrite

> Find all angles $x$ in $[0, 2\pi)$ that satisfy $\cos^{2}x = \sin x + 1$.

There are two different trig functions in the equation, and the squared term is the problem. Use the Pythagorean identity to rewrite $\cos^{2}x = 1 - \sin^{2}x$:

$$
1 - \sin^{2}x = \sin x + 1.
$$

Move everything to one side:

$$
-\sin^{2}x - \sin x = 0 \quad\Longrightarrow\quad \sin^{2}x + \sin x = 0 \quad\Longrightarrow\quad \sin x(\sin x + 1) = 0.
$$

So either $\sin x = 0$ or $\sin x = -1$.

On $[0, 2\pi)$, $\sin x = 0$ gives $x = 0$ and $x = \pi$. The equation $\sin x = -1$ gives the unique solution $x = \dfrac{3\pi}{2}$.

**Solutions on $[0, 2\pi)$:** $x = 0$, $\pi$, $\dfrac{3\pi}{2}$.

---

## Common pitfalls

- **Losing the periodic tail.** On an interval problem like $[0, 2\pi)$ you list the finite set. On an "all real solutions" problem you must tack on $+ 2k\pi$ (or $+ k\pi$ for tangent) and say $k$ is any integer. Reading the question carefully is part of the problem.
- **Dividing by a trig function without thinking.** If you see $\sin x \cos x = \sin x$ and instinctively divide both sides by $\sin x$, you silently throw away every solution where $\sin x = 0$. Move everything to one side and factor instead.
- **Trusting your calculator's inverse blindly.** The $\arcsin$, $\arccos$, and $\arctan$ keys return only one angle each. The other quadrant's solution has to come from you, using symmetry or the unit circle.
- **Mixing up periods.** Sine and cosine repeat every $2\pi$, tangent every $\pi$. An equation like $\tan(2x) = 1$ has extra work because the argument is $2x$ — each family of solutions has to be divided by $2$, and the period collapses accordingly.

---

## Prerequisites

Before you practice, these should be solid:

- [[The_Unit_Circle]] — to read off reference angles and their locations
- [[Circular_Functions]] — the definitions of sine, cosine, and tangent
- [[Identities]] — the rewriting tools you will need on anything past the simplest problems
- [[Inverse_Trigonometric_Functions]] — for single-angle lookups your unit circle does not include

---

## Problems Involving Trigonometric Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="trigonometric_equations"></div>

---

## See Also

- [[Identities]] — the rewriting rules that turn ugly equations into solvable ones
- [[Inverse_Trigonometric_Functions]] — needed for lookups off the standard unit circle
- [[Graphs_Of_Trigonometric_Functions]] — every solution is an $x$-intercept of a shifted trig graph
- [[Trigonometric_Inequalities]] — the next step, once equations feel easy
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
