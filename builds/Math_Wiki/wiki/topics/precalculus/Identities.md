---
title: "Identities"
type: topic
aliases: ["Trig Identities", "Trigonometric Identities"]
tags: ["#branch-pre-calculus", "#topic-trig-identities", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "7", section: "7.4"}
related:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Graphs_Of_Trigonometric_Functions"
  - "topics/precalculus/Trigonometric_Equations"
  - "topics/precalculus/Inverse_Trigonometric_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Circular_Functions"
  - "topics/precalculus/Angles"
problem_type_ids: []
figures: []
summary: "Equations between trig functions that hold for every angle: the Pythagorean, even/odd, sum/difference, and double-angle families."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Identities

# Identities

An **identity** is an equation whose two sides agree no matter which angle you feed into it. That is a stronger promise than a regular equation. When you solve $2x - 1 = 7$, you are hunting for the one value of $x$ that makes the statement true. When you write a trig identity, the equal sign is a fact about the functions themselves — pick whatever $\theta$ you like and both sides will compute to the same number.

That promise has a practical payoff. Identities are the rewriting rules of trigonometry. They let you rename one expression as another, simpler one, or as one you already know how to handle. Proving an identity, rewriting an integral, solving a trig equation, collapsing a long expression down to a single number — all of it leans on the short list of identities on this page.

$$
\sin^{2}\theta + \cos^{2}\theta = 1
$$

Memorize that one line cold. Nearly every identity that follows can be traced back to it.

---

## Where the Pythagorean identity comes from

Picture a point on the **unit circle** — the circle of radius $1$ centered at the origin. Any such point satisfies the equation

$$
x^{2} + y^{2} = 1.
$$

Now connect that point to the definitions you already know from [[Circular_Functions]]. If an angle $\theta$ is drawn in standard position and its terminal ray meets the unit circle at a point, then by construction the $x$-coordinate of that point is $\cos\theta$ and the $y$-coordinate is $\sin\theta$. Substitute those names into the circle equation:

$$
(\cos\theta)^{2} + (\sin\theta)^{2} = 1,
$$

which we write more compactly as $\cos^{2}\theta + \sin^{2}\theta = 1$. There is nothing mystical about this identity — it is the equation of the unit circle wearing different labels. Every other identity in this topic is either a close cousin of this fact, a consequence of it, or follows from a symmetry of the circle picture.

### Two derived Pythagorean relatives

Divide both sides of $\sin^{2}\theta + \cos^{2}\theta = 1$ by $\cos^{2}\theta$, and every term turns into something familiar:

$$
\dfrac{\sin^{2}\theta}{\cos^{2}\theta} + 1 = \dfrac{1}{\cos^{2}\theta} \quad\Longrightarrow\quad \tan^{2}\theta + 1 = \sec^{2}\theta.
$$

Divide instead by $\sin^{2}\theta$ and you get $1 + \cot^{2}\theta = \csc^{2}\theta$. These two are not new ideas — they are the Pythagorean identity rewritten for when the natural variable is tangent or cotangent instead of sine and cosine.

---

## Even/odd identities

Reflecting a unit-circle point across the $x$-axis flips the $y$-coordinate and leaves the $x$-coordinate alone. In function language, swapping $\theta$ for $-\theta$ means:

- $\cos(-\theta) = \cos\theta$ — cosine is **even**.
- $\sin(-\theta) = -\sin\theta$ — sine is **odd**.
- $\tan(-\theta) = -\tan\theta$ — tangent is odd too, because it is sine over cosine.

These rules let you push a negative sign into or out of a trig function whenever it is convenient. They also explain why the graphs of cosine and sine have the symmetries they do.

---

## Sum and difference identities

There are recipes for the trig value of a *sum* of two angles in terms of the trig values of the angles separately:

$$
\cos(\alpha \pm \beta) = \cos\alpha \cos\beta \mp \sin\alpha \sin\beta
$$

$$
\sin(\alpha \pm \beta) = \sin\alpha \cos\beta \pm \cos\alpha \sin\beta
$$

Read the symbols as "top with top, bottom with bottom" — the cosine version uses the *opposite* sign on the right-hand side, the sine version uses the *same* sign. Getting those sign conventions crossed is the number-one mistake in this section, so copy both carefully before you try an example.

The most common use of these formulas is to evaluate a trig function at an angle your unit circle does not include directly, by writing that angle as a sum or difference of angles you *do* know.

---

## Double-angle identities

Set $\alpha = \beta = \theta$ in the sum identities and the formulas collapse to the **double-angle** versions:

$$
\sin(2\theta) = 2 \sin\theta \cos\theta
$$

$$
\cos(2\theta) = \cos^{2}\theta - \sin^{2}\theta.
$$

The cosine double-angle formula has two alternate forms you should recognize, both obtained by swapping $\sin^{2}\theta$ for $1 - \cos^{2}\theta$ (or the other way around) using the Pythagorean identity:

$$
\cos(2\theta) = 2\cos^{2}\theta - 1 = 1 - 2\sin^{2}\theta.
$$

All three versions are correct. Which one you reach for depends on what else is in the problem — if the rest of the expression is full of cosines, use the $2\cos^{2}\theta - 1$ form; if it is full of sines, use $1 - 2\sin^{2}\theta$.

---

## Example 1: a classic Pythagorean swap

> Show that $\dfrac{1 - \cos^{2}\theta}{\sin\theta} = \sin\theta$ wherever both sides are defined.

Rewrite the numerator using the Pythagorean identity. Because $\sin^{2}\theta + \cos^{2}\theta = 1$, we have $1 - \cos^{2}\theta = \sin^{2}\theta$. Substituting:

$$
\dfrac{1 - \cos^{2}\theta}{\sin\theta} = \dfrac{\sin^{2}\theta}{\sin\theta} = \sin\theta.
$$

The left side simplifies to the right side, so the identity holds.

---

## Example 2: evaluating cosine of a non-standard angle

> Use a sum identity to find the exact value of $\cos(75^{\circ})$.

The trick is to notice that $75^{\circ} = 45^{\circ} + 30^{\circ}$, and both of those are angles you already know. Apply the sum formula for cosine:

$$
\cos(75^{\circ}) = \cos(45^{\circ})\cos(30^{\circ}) - \sin(45^{\circ})\sin(30^{\circ}).
$$

Plug in the known values $\cos(45^{\circ}) = \sin(45^{\circ}) = \dfrac{\sqrt{2}}{2}$, $\cos(30^{\circ}) = \dfrac{\sqrt{3}}{2}$, and $\sin(30^{\circ}) = \dfrac{1}{2}$:

$$
\cos(75^{\circ}) = \dfrac{\sqrt{2}}{2} \cdot \dfrac{\sqrt{3}}{2} - \dfrac{\sqrt{2}}{2} \cdot \dfrac{1}{2} = \dfrac{\sqrt{6}}{4} - \dfrac{\sqrt{2}}{4} = \dfrac{\sqrt{6} - \sqrt{2}}{4}.
$$

That is an exact answer — decimal approximations would lose information.

---

## Example 3: a double-angle calculation

> Suppose $\sin\theta = \dfrac{3}{5}$ with $\theta$ in the first quadrant. Find $\sin(2\theta)$ and $\cos(2\theta)$.

First, locate $\cos\theta$. Since $\theta$ is in Quadrant I, cosine is positive. Use $\sin^{2}\theta + \cos^{2}\theta = 1$:

$$
\cos^{2}\theta = 1 - \left(\dfrac{3}{5}\right)^{2} = 1 - \dfrac{9}{25} = \dfrac{16}{25} \quad\Longrightarrow\quad \cos\theta = \dfrac{4}{5}.
$$

Now apply the double-angle formulas:

$$
\sin(2\theta) = 2 \sin\theta \cos\theta = 2 \cdot \dfrac{3}{5} \cdot \dfrac{4}{5} = \dfrac{24}{25}.
$$

$$
\cos(2\theta) = \cos^{2}\theta - \sin^{2}\theta = \dfrac{16}{25} - \dfrac{9}{25} = \dfrac{7}{25}.
$$

Notice how the single piece of information $\sin\theta = \dfrac{3}{5}$, together with the quadrant, determined everything else through the identity chain.

---

## Common pitfalls

- **Squared notation confusion.** The symbol $\sin^{2}\theta$ means $(\sin\theta)^{2}$, not $\sin(\theta^{2})$. This convention is universal in trigonometry, but the first time you see it you will probably misread it.
- **Sign slips on the cosine sum identity.** Cosine's sum formula uses the *opposite* sign: $\cos(A + B)$ takes a minus sign on the right, while $\cos(A - B)$ takes a plus. It is the opposite of what intuition suggests, so write the formula down before you use it.
- **Picking the wrong cosine double-angle form.** All three forms — $\cos^{2}\theta - \sin^{2}\theta$, $2\cos^{2}\theta - 1$, and $1 - 2\sin^{2}\theta$ — give the same answer, but one form may produce a dead end while another simplifies in a single step. Match the form to whatever the rest of the expression contains.
- **Treating an identity as an equation to solve.** An identity is a promise, not a question. When you prove an identity you show that two expressions are equal for every angle. That is a different goal from solving $\sin x = 1/2$, where you are asked to find particular angles. Confusing the two shows up constantly on quizzes.

---

## Prerequisites

Before practicing, these should feel routine:

- [[The_Unit_Circle]] — the source of every Pythagorean identity
- [[Circular_Functions]] — how $\sin\theta$, $\cos\theta$, and $\tan\theta$ are defined from a unit-circle point
- [[Angles]] — radian and degree measure, reference angles, the language of rotations

---

## Problems Involving Identities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="identities"></div>

---

## See Also

- [[Trigonometric_Equations]] — identities are the rewriting rules that shrink trig equations into solvable form
- [[Graphs_Of_Trigonometric_Functions]] — visual symmetries match the even/odd identities exactly
- [[The_Unit_Circle]]
- [[Circular_Functions]]
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
