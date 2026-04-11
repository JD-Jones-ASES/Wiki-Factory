---
title: "Graphs of Trigonometric Functions"
type: topic
aliases: ["Trig Graphs", "Sine Wave", "Cosine Wave", "Tangent Graph"]
tags: ["#branch-pre-calculus", "#topic-unit-circle", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.8"}
related:
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Sinusoid"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
  - "topics/precalculus/Identities"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: ["precalculus/sine_cosine_graphs.svg"]
summary: "What sine, cosine, and tangent look like plotted across the real line: waves with period 2 pi, and a tangent graph broken by vertical asymptotes."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Graphs of Trigonometric Functions

# Graphs of Trigonometric Functions

Up to this point, trig has been a machine that turns one angle into one number. You feed in $\pi/3$ and it hands back $\sqrt{3}/2$. That is fine for answering isolated questions, but to see the full personality of sine, cosine, and tangent, you need to pin down thousands of those one-number answers at once and plot them. When you do, three very different curves emerge: the two smooth waves of $y = \sin x$ and $y = \cos x$, and the broken, asymptote-laced graph of $y = \tan x$.

The idea to hold onto is that each graph is a direct transcription of motion around the unit circle. As the angle $x$ sweeps counter-clockwise from $0$ to $2\pi$, the point $(\cos x, \sin x)$ walks once around the circle. The graph of sine is a record of its $y$-coordinate over time; the graph of cosine is a record of its $x$-coordinate; the graph of tangent is the ratio of the two. Every feature of every curve — where it crosses zero, where it reaches its maximum, where it blows up — is readable directly off the circle picture.

![[sine_cosine_graphs.svg|Graphs of sine and cosine]]

---

## The sine graph

Start the unit-circle point at $(1, 0)$ and let the angle grow. As the angle moves from $0$ to $\pi/2$, the $y$-coordinate climbs from $0$ up to $1$. From $\pi/2$ to $\pi$, the point swings into the second quadrant and $y$ drops back down to $0$. From $\pi$ to $3\pi/2$, the point passes through the third quadrant and $y$ goes negative, reaching $-1$ at the bottom. From $3\pi/2$ to $2\pi$, the point climbs through the fourth quadrant and $y$ returns to $0$.

Plot those $y$-values against the input angle, and you get one full cycle of the **sine wave**:

- Starts at $(0, 0)$
- Climbs to a peak of $(\pi/2,\; 1)$
- Falls through $(\pi,\; 0)$
- Reaches a trough at $(3\pi/2,\; -1)$
- Returns to $(2\pi,\; 0)$

Past $x = 2\pi$ the angle has come back to its starting direction, so the whole pattern repeats — and it repeats in the other direction for negative inputs too. The graph is a smooth wave oscillating forever between $y = -1$ and $y = 1$.

### Sine in numbers

- **Domain:** all real numbers, $(-\infty, \infty)$
- **Range:** $[-1, 1]$
- **Period:** $2\pi$ (one full cycle every $2\pi$ units of input)
- **Amplitude:** $1$ (half the distance from trough to peak)
- **Zeros:** $x = k\pi$ for every integer $k$
- **Symmetry:** the graph is odd — it has rotational symmetry about the origin, matching the identity $\sin(-x) = -\sin x$

---

## The cosine graph

Repeat the same thought experiment, but track the $x$-coordinate of the unit-circle point instead of the $y$-coordinate. At angle $0$ the point is at $(1, 0)$, so cosine starts at its maximum of $1$. From $0$ to $\pi/2$, $x$ slides down to $0$. From $\pi/2$ to $\pi$ it continues down to $-1$. From $\pi$ back to $2\pi$ it climbs back up through $0$ to $1$.

Plot those values and you get the **cosine wave**:

- Starts at $(0,\; 1)$ — the maximum
- Falls through $(\pi/2,\; 0)$
- Reaches a trough at $(\pi,\; -1)$
- Climbs through $(3\pi/2,\; 0)$
- Returns to $(2\pi,\; 1)$

Compare the two pictures and you will notice the cosine graph is identical to the sine graph, just shifted $\pi/2$ units to the left. That is a legitimate identity: $\cos x = \sin(x + \pi/2)$. The two waves are the same shape, traced out by the same motion, started at a different spot on the circle.

### Cosine in numbers

- **Domain:** all real numbers, $(-\infty, \infty)$
- **Range:** $[-1, 1]$
- **Period:** $2\pi$
- **Amplitude:** $1$
- **Zeros:** $x = \pi/2 + k\pi$ for every integer $k$
- **Symmetry:** the graph is even — mirror-symmetric across the $y$-axis, matching $\cos(-x) = \cos x$

---

## The tangent graph

Tangent is the ratio $\tan x = \sin x / \cos x$, and that division rule dictates the entire shape of its graph. Wherever cosine hits zero the denominator vanishes and tangent blows up: the graph has a vertical asymptote at every $x = \pi/2 + k\pi$. Between consecutive asymptotes, tangent runs a full ride from $-\infty$ to $+\infty$, passing through zero at each $x = k\pi$.

Take a single branch, the one centered on $x = 0$. At $x = -\pi/2$ the graph is asymptotic to $-\infty$. At $x = 0$ it crosses through the origin. At $x = \pi/2$ it races up to $+\infty$. That S-curve repeats on every interval $(\pi/2 + k\pi,\; 3\pi/2 + k\pi)$. Unlike sine and cosine, tangent has no maximum and no minimum — its range is all of $\mathbb{R}$.

Tangent also repeats twice as fast as sine and cosine. Its period is $\pi$, not $2\pi$. This falls out of the ratio definition: moving $x$ by $\pi$ flips the sign of both sine and cosine, and those two sign flips cancel in the quotient, leaving the tangent value unchanged.

### Tangent in numbers

- **Domain:** every real number except $x = \pi/2 + k\pi$
- **Range:** $(-\infty, \infty)$
- **Period:** $\pi$
- **Asymptotes:** vertical lines at $x = \pi/2 + k\pi$
- **Zeros:** $x = k\pi$
- **Symmetry:** odd, $\tan(-x) = -\tan x$

---

## Key ideas

- **Unit circle is the source.** Every feature of a trig graph — peaks, troughs, zeros, asymptotes — has a one-to-one origin story on the unit circle. If a graph looks confusing, draw the circle next to it and watch the point move.
- **Sine and cosine are the same curve, offset by $\pi/2$.** Learning both is really learning one wave and remembering which one starts high and which starts at zero.
- **Amplitude changes with a leading coefficient.** Writing $y = A \sin x$ multiplies every output by $A$, so the wave now oscillates between $-|A|$ and $|A|$ instead of $-1$ and $1$.
- **Period changes with a coefficient on $x$.** The function $y = \sin(Bx)$ repeats every $2\pi/B$ units, so larger $B$ squeezes the wave and smaller $B$ stretches it out.
- **Tangent is broken, not continuous.** There is no way to connect two consecutive branches without crossing an asymptote. Always draw the asymptotes first as dashed lines, then fill in the branches between them.

---

## Example 1: Sketching one cycle of $y = \cos x$

> Plot one full cycle of $y = \cos x$, using the five key points from the first period.

Start at the $y$-intercept. When $x = 0$, $\cos(0) = 1$, so the first key point is $(0, 1)$ — the maximum.

Move a quarter-period forward. A quarter of $2\pi$ is $\pi/2$, and $\cos(\pi/2) = 0$. Second point: $(\pi/2,\; 0)$.

Halfway through the cycle: $\cos(\pi) = -1$. Third point: $(\pi,\; -1)$ — the minimum.

Three quarters through: $\cos(3\pi/2) = 0$. Fourth point: $(3\pi/2,\; 0)$.

End of the cycle: $\cos(2\pi) = 1$. Fifth point: $(2\pi,\; 1)$.

Connect these five points with a smooth curve that dips below the $x$-axis between the second and fourth points, and you have one clean cycle. For a longer window, copy that cycle to the left and right as many times as you need — the wave is identical from period to period.

---

## Example 2: Reading amplitude and period from $y = 3\sin(2x)$

> What are the amplitude and period of $f(x) = 3\sin(2x)$, and what are its maximum and minimum values?

Compare to the parent form $y = A\sin(Bx)$. Here $A = 3$ and $B = 2$.

The amplitude is $|A| = 3$, so the wave oscillates between $-3$ and $3$. The maximum value is $3$ and the minimum is $-3$.

The period is $2\pi / B = 2\pi / 2 = \pi$. One full cycle of $f$ now fits in an interval of length $\pi$ instead of $2\pi$, so the graph is horizontally compressed by a factor of $2$.

The shape is still sinusoidal — the five key points within one period now sit at $x = 0$, $\pi/4$, $\pi/2$, $3\pi/4$, and $\pi$, with output values $0$, $3$, $0$, $-3$, and $0$. Same wave; new spacing and new height.

---

## Example 3: Finding an asymptote of $y = \tan x$

> Where is the first vertical asymptote of $y = \tan x$ to the right of $x = 0$?

Tangent is $\sin x / \cos x$. The graph has a vertical asymptote precisely where the denominator hits zero, so look for the smallest positive $x$ with $\cos x = 0$. On the unit circle, the $x$-coordinate is zero at $x = \pi/2$ and $x = 3\pi/2$ within the first full turn.

The smallest such value to the right of $0$ is $x = \pi/2$. At that input the tangent function is undefined and the graph has a vertical asymptote. Just to the left, $\tan x$ shoots up toward $+\infty$; just to the right, the next branch starts from $-\infty$ and climbs back up toward the next zero at $x = \pi$.

---

## Common pitfalls

- **Connecting tangent branches through an asymptote.** Each branch lives between two consecutive asymptotes. Never let your pencil cross one.
- **Confusing period with amplitude.** The period is a horizontal measurement (how far until the pattern repeats); the amplitude is a vertical measurement (how tall each peak is). Changing $A$ stretches vertically; changing $B$ stretches horizontally.
- **Misreading the starting point.** Sine starts at zero on the $y$-axis; cosine starts at its maximum. Swapping them is the most common sketching mistake.
- **Forgetting that tangent has period $\pi$, not $2\pi$.** Half a turn of the unit circle already returns the same tangent value, so the tangent graph repeats twice as fast as its sine or cosine siblings.

---

## Prerequisites

- [[Circular_Functions]] — the unit-circle definitions that these graphs are plotted from
- [[The_Unit_Circle]] — the exact key-point values you will use to sketch one clean cycle
- [[Function_Basics]] — domain, range, symmetry, and transformations translate directly from other function families

---

## Problems Involving Graphs of Trigonometric Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphs_of_trigonometric_functions"></div>

---

## See Also

- [[Circular_Functions]] — where the values being plotted come from
- [[Sinusoid]] — shifts, stretches, and full transformations of the sine and cosine curves
- [[Inverse_Trigonometric_Functions]] — the curves obtained by reflecting these graphs across $y = x$
- [[Identities]] — algebraic connections between sine, cosine, and tangent
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
</content>
