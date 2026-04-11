---
title: "Sinusoid"
type: topic
aliases: ["Sinusoidal Function", "Sinusoids", "Sinusoidal Model"]
tags: ["#branch-pre-calculus", "#topic-unit-circle", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.9"}
related:
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Identities"
  - "topics/precalculus/Transformations"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/precalculus/Transformations"
problem_type_ids: []
figures: []
summary: "Any stretched, shifted sine or cosine wave. Four parameters — amplitude, period, phase shift, midline — fully describe the shape."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Sinusoid

# Sinusoid

A **sinusoid** is any function you can build by stretching, shrinking, and shifting the basic sine graph (or, equivalently, the basic cosine graph — the two shapes differ only by a head start). The same wave shows up in tides rising and falling with the moon, in the daily swing of sunrise and sunset, in the voltage of alternating current, and in the pressure wave of a pure tone striking your eardrum. Once you understand the four knobs that tune a sinusoid, you can match that wave to almost any repeating real-world measurement.

$$
f(x) = A \sin\!\big(B(x - h)\big) + k.
$$

Four parameters, four knobs. Every decision about how the wave looks ends up inside one of those four letters, and every letter corresponds to a feature you can see on the graph.

---

## The four parameters

**Amplitude $A$: how tall the wave is.**
The amplitude measures how far the graph reaches above or below its central line. If the maximum value of $f(x)$ is $M$ and the minimum is $m$, then

$$
A = \dfrac{M - m}{2}.
$$

Think of it this way: the wave climbs $A$ units above the middle and drops $A$ units below. A sinusoid with $A = 3$ has peaks that sit three units above its central line and troughs three units below. Taking the absolute value matters — by convention $A > 0$, and if the formula hands you a negative number you fold it into a reflection instead.

**Midline $k$: the central line the wave swings around.**
This is the horizontal line $y = k$ that splits the wave evenly. Algebraically,

$$
k = \dfrac{M + m}{2}.
$$

Every peak is a distance $A$ above $y = k$, and every trough is a distance $A$ below. Moving $k$ up or down drags the entire graph vertically without changing its shape.

**Angular frequency $B$ and the period.**
The parameter $B$ controls how quickly the wave repeats. The **period** — the horizontal distance between two consecutive peaks — is given by

$$
\text{period} = \dfrac{2\pi}{|B|}.
$$

Large $|B|$ squeezes the graph into a rapid oscillation; small $|B|$ stretches it into a slow roll. For a basic $\sin x$ the value is $B = 1$ and the period is $2\pi$. For a graph that repeats every $24$ hours, you would set $B = \dfrac{2\pi}{24} = \dfrac{\pi}{12}$ so the formula matches the calendar.

**Phase shift $h$: where the wave starts.**
The horizontal shift $h$ slides the whole wave left or right. A positive $h$ delays the graph — you see the familiar shape of $A \sin(Bx) + k$ pushed $h$ units to the right. The crucial bookkeeping rule is that $h$ is whatever is being *subtracted* inside the parentheses. If the formula reads $f(x) = 3 \sin\!\big(2x - \pi\big) + 1$, first factor the $2$ out: $3 \sin\!\big(2(x - \pi/2)\big) + 1$. Now $h = \pi/2$, not $\pi$. Skipping the factoring step is the most common slip in this topic.

---

## Fitting a sinusoid to data

Real-world problems usually give you a few features of the wave — the peak, the trough, the time between repeats — and ask for a formula. The recipe is exactly the reverse of the formulas above.

1. Compute the midline: $k = (M + m)/2$.
2. Compute the amplitude: $A = (M - m)/2$.
3. Find the period, then set $B = 2\pi / \text{period}$.
4. Pick a horizontal shift $h$ so the first peak of your formula lands where the first peak of the data lands. If you are using a cosine form, $h$ is simply the $x$-coordinate of a peak. For a sine form, $h$ is the $x$-coordinate of a zero-crossing on the way up.

---

## Example 1: reading a formula

> Identify the amplitude, period, phase shift, and midline of $f(x) = 4 \sin\!\big(3(x - \pi/6)\big) - 2$.

Match term by term against $f(x) = A \sin(B(x - h)) + k$:

- $A = 4$, so the amplitude is $4$.
- $B = 3$, so the period is $\dfrac{2\pi}{3}$.
- $h = \pi/6$, so the graph is shifted $\pi/6$ units to the right.
- $k = -2$, so the midline is $y = -2$.

Sanity check the extremes: the graph climbs to $k + A = -2 + 4 = 2$ and drops to $k - A = -2 - 4 = -6$. So the wave oscillates between $-6$ and $2$, centered on $y = -2$.

---

## Example 2: modeling daylight hours

> A certain northern city has $16$ hours of daylight on the longest day of the year (around day $172$) and $8$ hours on the shortest day (around day $355$). Build a sinusoid $H(d)$ that models the number of daylight hours on day $d$ of the year.

Start from the features.

**Midline:** $k = (16 + 8)/2 = 12$ hours.
**Amplitude:** $A = (16 - 8)/2 = 4$ hours.
**Period:** one full year, so period $= 365$ and $B = \dfrac{2\pi}{365}$.
**Phase shift:** a cosine peaks at the start if there is no shift, so pick the cosine form and set $h = 172$ to place the peak on day $172$.

Putting it together:

$$
H(d) = 4 \cos\!\left(\dfrac{2\pi}{365}(d - 172)\right) + 12.
$$

Spot-check: $H(172) = 4 \cdot \cos(0) + 12 = 4 + 12 = 16$. Half a period later, at $d = 172 + 365/2 \approx 354.5$, the argument is $\pi$ and cosine is $-1$, so $H \approx 4 \cdot (-1) + 12 = 8$. Both extremes match the description.

---

## Example 3: sketching from the parameters

> Describe the key features of $g(x) = -2 \cos\!\big(\pi x\big) + 5$ without plotting.

Compare with $A \cos(B(x - h)) + k$ and read off values. Amplitude $|A| = 2$. The leading negative flips the cosine graph upside down — where the usual cosine peaks, this one troughs. The period is $2\pi / \pi = 2$, so the wave repeats every $2$ units of $x$. The midline is $y = 5$. Because the cosine is flipped, the graph starts at the trough $y = 5 - 2 = 3$ at $x = 0$, rises through $y = 5$ at $x = 1/2$, peaks at $y = 5 + 2 = 7$ at $x = 1$, and returns to the trough at $x = 2$. There is no phase shift: $h = 0$.

---

## Common pitfalls

- **Forgetting to factor before reading $h$.** If the formula is $\sin(2x - \pi)$ and not $\sin(2(x - \pi/2))$, the phase shift is $\pi/2$, not $\pi$. Always factor out $B$ before claiming $h$.
- **Confusing amplitude with the peak value.** The peak is $A + k$, not $A$. A sinusoid with amplitude $3$ and midline $10$ has a peak of $13$, not $3$.
- **Treating a negative amplitude as unusual.** A negative $A$ is just a reflection across the midline. Convention is to report $A$ as positive and absorb the sign into either a $\pi$ phase shift or a flip of the function.
- **Mixing the period formula up.** The period is $2\pi / |B|$, not $2\pi B$. An easy check: if $B = 1$ the period should come out to $2\pi$, which is the baseline for $\sin x$.

---

## Prerequisites

Before practicing, these should feel comfortable:

- [[The_Unit_Circle]] — the geometric source of the basic sine and cosine waves
- [[Circular_Functions]] — the definitions of $\sin x$ and $\cos x$ as circular coordinates
- [[Graphs_Of_Trigonometric_Functions]] — the baseline shapes you are stretching and shifting
- [[Transformations]] — how $Af(B(x - h)) + k$ moves any parent function

---

## Problems Involving Sinusoids

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="sinusoid"></div>

---

## See Also

- [[Graphs_Of_Trigonometric_Functions]] — the parent graphs every sinusoid is built from
- [[Circular_Functions]]
- [[The_Unit_Circle]]
- [[Identities]] — sometimes the fastest route to a sinusoid form is an identity rewrite
- [[Transformations]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
