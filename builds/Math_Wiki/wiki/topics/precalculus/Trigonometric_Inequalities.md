---
title: "Trigonometric Inequalities"
type: topic
aliases: ["Trig Inequalities", "Solving Trig Inequalities"]
tags: ["#branch-pre-calculus", "#topic-trig-equations", "#skill-multi-step", "#skill-visualization", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Trigonometric_Equations"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/precalculus/Circular_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Trigonometric_Equations"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
problem_type_ids: []
figures: []
summary: "Once you can find the angles where a trig function equals a target value, the next step is to find the whole interval where the function sits above or below that value, using the unit circle and the wave graph together as visual tools."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Trigonometric Inequalities

# Trigonometric Inequalities

The companion to every [[Trigonometric_Equations|trig equation]] is a **trig inequality** — a question that asks not "where does this function equal a target value?" but "where is this function above (or below) the target?" Think of it as going from a single snapshot to an entire interval.

$$
\sin x = \dfrac{1}{2} \quad \text{vs.} \quad \sin x > \dfrac{1}{2}.
$$

The equation picks out a handful of isolated angles; the inequality picks out an entire range of angles. Both kinds of question have the same first step — find the boundary angles where equality holds — but the inequality asks for a little more: you have to decide which side of those boundaries puts the function on the correct side of the target.

The best way to see what is happening is with two tools at once. The **unit circle** gives you the boundary angles directly, and the **graph of the function** (a cosine or sine wave) shows at a glance which parts of the interval sit above or below the target line. Either tool alone can solve the problem, but using them together is the fastest route and the one least likely to drop a piece of the answer.

---

## The standard solution procedure

Three steps handle the vast majority of trig inequalities on a bounded interval like $[0, 2\pi)$:

1. **Solve the corresponding equation** to find the boundary angles. For $\sin x > \dfrac{1}{2}$, the boundaries are the angles where $\sin x = \dfrac{1}{2}$, namely $x = \pi/6$ and $x = 5\pi/6$.
2. **Partition the given interval at the boundaries.** The boundaries split $[0, 2\pi)$ into sub-intervals. For the sine example, the sub-intervals are $[0, \pi/6)$, $(\pi/6, 5\pi/6)$, and $(5\pi/6, 2\pi)$.
3. **Test a point from each sub-interval.** Plug a convenient angle from each piece into the trig function and check whether the inequality holds. Any sub-interval where it holds is part of the answer; any sub-interval where it fails is not.

The wave graph is a shortcut for step three. Instead of testing numerical values, you can sketch the trig function on the interval, draw a horizontal line at the target value, and read off the pieces where the curve sits on the correct side of the line. Those pieces are your answer.

---

## When the inequality is strict vs. non-strict

A strict inequality like $\sin x > 1/2$ excludes the boundary points, so the answer uses open intervals. A non-strict inequality like $\sin x \ge 1/2$ includes them, so the answer uses closed intervals.

$$
\sin x > \dfrac{1}{2} \;\Longrightarrow\; x \in \left(\dfrac{\pi}{6},\; \dfrac{5\pi}{6}\right),
$$

$$
\sin x \ge \dfrac{1}{2} \;\Longrightarrow\; x \in \left[\dfrac{\pi}{6},\; \dfrac{5\pi}{6}\right].
$$

The distinction is small on paper but important to get right — a problem that grades on interval notation will dock points for using the wrong bracket.

---

## The cyclic nature means the answer can wrap around

A trig inequality on $[0, 2\pi)$ sometimes has a solution that crosses the point $x = 0$, meaning it consists of two disjoint pieces — one starting near the left end of the interval, one ending near the right end. For example, $\cos x > 0$ on $[0, 2\pi)$ has the solution $[0, \pi/2) \cup (3\pi/2, 2\pi)$, because the cosine wave dips below zero in the middle of the interval and rises back up at the end.

When you solve a trig inequality over the full real line (no bounded interval), the answer is automatically periodic. Each piece of the bounded-interval solution becomes a family of intervals spaced by the period ($2\pi$ for sine and cosine, $\pi$ for tangent). The cleanest way to write such a family is with a periodic-tail notation:

$$
\sin x > \dfrac{1}{2} \;\Longrightarrow\; \dfrac{\pi}{6} + 2k\pi < x < \dfrac{5\pi}{6} + 2k\pi, \; k \in \mathbb{Z}.
$$

That says: one solution interval lives between $\pi/6$ and $5\pi/6$, and the whole pattern repeats every $2\pi$ units along the real line.

---

## Example 1: $\sin x > \dfrac{1}{2}$ on $[0, 2\pi)$

> Solve $\sin x > \dfrac{1}{2}$ on $[0, 2\pi)$.

**Step 1 — find the boundaries.** Solve $\sin x = \dfrac{1}{2}$. The unit circle gives $x = \pi/6$ (Quadrant I reference angle) and $x = \pi - \pi/6 = 5\pi/6$ (Quadrant II). Both sit inside $[0, 2\pi)$.

**Step 2 — partition the interval.** The boundaries split $[0, 2\pi)$ into three sub-intervals:

$$
[0, \pi/6), \quad (\pi/6, 5\pi/6), \quad (5\pi/6, 2\pi).
$$

**Step 3 — test a representative angle from each piece.** Pick $x = 0$ from the first, $x = \pi/2$ from the second, and $x = \pi$ from the third:

- $\sin(0) = 0$. Is $0 > 1/2$? No.
- $\sin(\pi/2) = 1$. Is $1 > 1/2$? Yes.
- $\sin(\pi) = 0$. Is $0 > 1/2$? No.

Only the middle sub-interval satisfies the inequality. Because the inequality is strict, the endpoints are excluded:

$$
\boxed{x \in \left(\dfrac{\pi}{6},\; \dfrac{5\pi}{6}\right)}.
$$

Visually: draw the sine wave on $[0, 2\pi)$, sketch the horizontal line $y = 1/2$, and notice the wave sits above that line only in the hump between $\pi/6$ and $5\pi/6$. Same answer, reached with a picture instead of three test points.

---

## Example 2: $\cos x \le 0$ on $[0, 2\pi)$

> Solve $\cos x \le 0$ on $[0, 2\pi)$.

**Step 1 — find the boundaries.** Solve $\cos x = 0$. Cosine equals zero at the quadrantal angles $x = \pi/2$ and $x = 3\pi/2$, both inside the interval.

**Step 2 — partition.** The interval $[0, 2\pi)$ splits into three pieces:

$$
[0, \pi/2), \quad (\pi/2, 3\pi/2), \quad (3\pi/2, 2\pi).
$$

**Step 3 — test a point from each piece.** Pick $x = 0$, $x = \pi$, $x = 7\pi/4$:

- $\cos(0) = 1$. Is $1 \le 0$? No.
- $\cos(\pi) = -1$. Is $-1 \le 0$? Yes.
- $\cos(7\pi/4) = \sqrt{2}/2$. Is $\sqrt{2}/2 \le 0$? No.

The middle piece is the only one that works. The inequality is non-strict, so the boundary angles where $\cos x = 0$ are included:

$$
\boxed{x \in \left[\dfrac{\pi}{2},\; \dfrac{3\pi}{2}\right]}.
$$

A quick sanity check: cosine is the $x$-coordinate on the unit circle, and $x$-coordinate is non-positive exactly in Quadrants II and III, which together span the angles from $\pi/2$ to $3\pi/2$ inclusive. Same answer, read directly off the unit circle.

---

## Example 3: $\tan x \ge 1$ on $[0, \pi/2)$

> Solve $\tan x \ge 1$ on $[0, \pi/2)$.

**Step 1 — find the boundary.** Solve $\tan x = 1$. In the first quadrant this gives the single angle $x = \pi/4$.

**Step 2 — partition.** The interval $[0, \pi/2)$ splits at the boundary into $[0, \pi/4)$ and $[\pi/4, \pi/2)$. Notice the right endpoint of the full interval $\pi/2$ is *not* included, because tangent has a vertical asymptote there — tangent is undefined at $\pi/2$ and heads to infinity as $x$ approaches it from below.

**Step 3 — test a point from each piece.** Pick $x = 0$ and $x = \pi/3$:

- $\tan(0) = 0$. Is $0 \ge 1$? No.
- $\tan(\pi/3) = \sqrt{3} \approx 1.73$. Is $1.73 \ge 1$? Yes.

Only the second piece satisfies the inequality. Since the inequality is non-strict, $\pi/4$ is included, but $\pi/2$ must stay excluded because tangent is undefined there.

$$
\boxed{x \in \left[\dfrac{\pi}{4},\; \dfrac{\pi}{2}\right)}.
$$

This example shows a small feature that equations rarely surface: the **domain** of the trig function matters. For tangent, the boundary of a bounded interval might coincide with a vertical asymptote, and the inequality can never be satisfied at such a point because the function has no value there. Always check the domain before finalizing your answer, and exclude any asymptote from the solution.

---

## Common pitfalls

- **Dropping the boundary test.** Forgetting to solve the corresponding equation means you have nothing to partition the interval with. Every trig inequality starts with a trig equation.
- **Flipping the inequality sign by accident.** When you multiply or divide both sides by a negative number, the sign flips — same as with algebraic inequalities. Ignoring this produces an answer that is exactly wrong.
- **Confusing open and closed intervals.** A strict inequality uses parentheses; a non-strict inequality uses brackets on the boundary points. Mixing these up is a small error that costs real points.
- **Losing the domain of the function.** For tangent, cotangent, secant, and cosecant, the function is undefined at certain angles. Those angles can never be part of a solution set, regardless of what the inequality wants.
- **Solving only within $[0, 2\pi)$ when the question asks for all real solutions.** On the full real line, the answer is periodic. Each interval piece repeats every period, and the full solution needs that periodic tail.
- **Testing the boundary angles themselves instead of interior points.** A boundary is the tipping point where the sign flips — picking it as the test point gives an ambiguous answer and tells you nothing. Always pick a value strictly inside the sub-interval.

---

## Prerequisites

- [[Trigonometric_Equations]] — the technique for finding boundary angles, without which the inequality is unsolvable
- [[The_Unit_Circle]] — the source of exact values and the natural place to picture sign changes of sine, cosine, and tangent
- [[Graphs_Of_Trigonometric_Functions]] — the wave pictures that let you read the answer visually, a huge accelerator once they become second nature

---

## Problems Involving Trigonometric Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="trigonometric_inequalities"></div>

---

## See Also

- [[Trigonometric_Equations]] — the equation version of the same problem, always solved first
- [[The_Unit_Circle]] — the tool that delivers boundary angles with no extra machinery
- [[Graphs_Of_Trigonometric_Functions]] — wave pictures that make the intervals visible
- [[Inverse_Trigonometric_Functions]] — needed to find non-standard boundary angles
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
