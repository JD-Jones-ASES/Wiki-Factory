---
title: "Polar Form of Complex Numbers"
type: topic
aliases: ["Trigonometric Form of Complex Numbers", "Modulus and Argument", "De Moivre's Theorem"]
tags: ["#branch-pre-calculus", "#topic-complex-numbers", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "8", section: "8.6"}
related:
  - "topics/algebra/The_Complex_Number_System"
  - "topics/precalculus/Complex_Zeros"
  - "topics/precalculus/Introduction_To_Polar_Coordinates"
  - "topics/precalculus/The_Unit_Circle"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/The_Complex_Number_System"
  - "topics/precalculus/The_Unit_Circle"
  - "topics/precalculus/Introduction_To_Polar_Coordinates"
problem_type_ids: []
figures: []
summary: "A second way of naming a complex number that turns products and powers into angle addition and exponent arithmetic."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Polar Form of Complex Numbers

# Polar Form of Complex Numbers

The form $z = a + bi$ is convenient for adding and subtracting, but it is surprisingly clumsy for multiplying, dividing, and taking powers. Each multiplication forces you to distribute four products and then go clean up $i^2 = -1$. Taking something like $(1 + i)^{10}$ by repeated distribution is a chore and an invitation to sign errors.

There is a second way of naming a complex number that turns all of that work into trigonometry. It is called the **polar form**, and once you see it, powers and roots of complex numbers become almost mechanical.

## The polar picture

Plot $z = a + bi$ as the point $(a, b)$ on the [[Introduction_To_Polar_Coordinates|complex plane]]. That point sits at some distance from the origin and at some angle from the positive real axis. Call the distance $r$ and call the angle $\theta$. Then a right-triangle reading of the point gives

$$
a = r\cos\theta, \qquad b = r\sin\theta.
$$

Substituting these into $z = a + bi$ collects the pieces into a single trigonometric expression:

$$
z = r(\cos\theta + i\sin\theta).
$$

That is the **polar form** of the complex number $z$. The number $r = |z| = \sqrt{a^2 + b^2}$ is called the **modulus** — it is the same "length" you already met in the [[The_Complex_Number_System|complex number system]]. The angle $\theta$ is called the **argument** of $z$, sometimes written $\arg(z)$, and it is determined from

$$
\tan\theta = \frac{b}{a},
$$

adjusted for which quadrant the point $(a, b)$ actually lives in. The argument is not unique — you can always add $2\pi$ and land on the same point — but most problems take the value with $0 \le \theta < 2\pi$ or $-\pi < \theta \le \pi$.

Going the other direction is just as fast: if you know $r$ and $\theta$, the rectangular form falls out by computing $a = r\cos\theta$ and $b = r\sin\theta$.

---

## Why polar form is worth the effort

Polar form is worth learning because complex multiplication collapses into two tiny operations: multiply the moduli, and add the arguments. In symbols, if $z_1 = r_1(\cos\theta_1 + i\sin\theta_1)$ and $z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$, then

$$
z_1 z_2 = r_1 r_2 \bigl(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\bigr).
$$

Lengths multiply and angles add. Division is the same idea in reverse:

$$
\frac{z_1}{z_2} = \frac{r_1}{r_2}\bigl(\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)\bigr).
$$

The geometry is transparent: multiplying by a complex number scales and rotates.

Applying the product rule $n$ times to the same number gives the formula known as **De Moivre's theorem**:

$$
\bigl(r(\cos\theta + i\sin\theta)\bigr)^n = r^n\bigl(\cos(n\theta) + i\sin(n\theta)\bigr).
$$

Raise the modulus to the $n$th power, multiply the angle by $n$, done. A problem that would take dozens of distributive steps in rectangular form is one line in polar form. The same move, run in reverse, produces $n$th roots of complex numbers by dividing the angle and the modulus appropriately, which is how you find all the cube roots or fifth roots of a given complex number.

---

## Example 1: converting rectangular to polar

> Write $z = -1 + i\sqrt{3}$ in polar form.

The modulus is a Pythagorean calculation:

$$
r = |z| = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = \sqrt{4} = 2.
$$

The argument satisfies $\tan\theta = \dfrac{\sqrt{3}}{-1} = -\sqrt{3}$. A calculator will return $\theta = -\dfrac{\pi}{3}$, which is in Quadrant IV — but the actual point $(-1, \sqrt{3})$ is in Quadrant II. Add $\pi$ to move into the correct quadrant:

$$
\theta = -\frac{\pi}{3} + \pi = \frac{2\pi}{3}.
$$

So the polar form is

$$
z = 2\!\left(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}\right).
$$

A quick sanity check: $2\cos(2\pi/3) = 2 \cdot (-1/2) = -1$ and $2\sin(2\pi/3) = 2 \cdot (\sqrt{3}/2) = \sqrt{3}$, matching the original $a = -1$ and $b = \sqrt{3}$.

---

## Example 2: multiplying in polar form

> Compute $(1 + i)(\sqrt{3} + i)$ using polar form.

First convert each factor. For $z_1 = 1 + i$: the modulus is $\sqrt{1^2 + 1^2} = \sqrt{2}$ and the argument is $\tan^{-1}(1/1) = \pi/4$, and the point $(1, 1)$ is in Quadrant I, so $\theta_1 = \pi/4$.

For $z_2 = \sqrt{3} + i$: the modulus is $\sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{4} = 2$ and the argument is $\tan^{-1}(1/\sqrt{3}) = \pi/6$, with the point in Quadrant I, so $\theta_2 = \pi/6$.

Multiply the moduli and add the arguments:

$$
z_1 z_2 = (\sqrt{2})(2)\!\left(\cos\!\left(\frac{\pi}{4} + \frac{\pi}{6}\right) + i\sin\!\left(\frac{\pi}{4} + \frac{\pi}{6}\right)\right) = 2\sqrt{2}\!\left(\cos\frac{5\pi}{12} + i\sin\frac{5\pi}{12}\right).
$$

Compare with the rectangular route — distributing $(1 + i)(\sqrt{3} + i)$ gives a four-term product that you then have to collect and simplify. Both routes end at the same complex number, but the polar route showed the geometric meaning: a scaling by $2\sqrt{2}$ and a rotation by $5\pi/12$.

---

## Example 3: raising to a power with De Moivre

> Compute $(1 + i)^{10}$.

Rectangular form would demand ten multiplications. Polar form handles it in two lines. Convert once: $1 + i$ has modulus $\sqrt{2}$ and argument $\pi/4$, so

$$
1 + i = \sqrt{2}\!\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right).
$$

Apply De Moivre with $n = 10$:

$$
(1 + i)^{10} = (\sqrt{2})^{10}\!\left(\cos\frac{10\pi}{4} + i\sin\frac{10\pi}{4}\right) = 32\!\left(\cos\frac{5\pi}{2} + i\sin\frac{5\pi}{2}\right).
$$

Simplify $5\pi/2$ by subtracting $2\pi$ to land in a standard angle: $5\pi/2 - 2\pi = \pi/2$. So

$$
(1 + i)^{10} = 32(\cos(\pi/2) + i\sin(\pi/2)) = 32(0 + i) = 32 i.
$$

A three-line computation that would have taken a page by hand.

---

## Common pitfalls

- **Picking the wrong quadrant for the argument.** The $\tan^{-1}$ key on a calculator only hands back angles in $(-\pi/2, \pi/2)$. Plot the point first and correct by $\pi$ when the actual $(a, b)$ is in Quadrant II or III.
- **Forgetting to scale the modulus when using De Moivre.** The formula raises $r$ to the $n$th power *and* multiplies the angle by $n$. Missing either half of the rule gives an answer with the wrong size or the wrong direction.
- **Confusing the polar angle with a degree/radian mismatch.** Pick one unit and stick with it. Radians tend to play more cleanly with the standard-angle values $\pi/6, \pi/4, \pi/3, \pi/2, \ldots$ from the [[The_Unit_Circle|unit circle]].
- **Treating polar form as the "final answer."** Many problems ask for the result back in $a + bi$ form, so plan on one last conversion step $a = r\cos\theta$, $b = r\sin\theta$ once you have finished the polar arithmetic.

---

## Prerequisites

- [[The_Complex_Number_System]] — you must know what $a + bi$ means, what a modulus is, and how rectangular multiplication works before you trade it in for something faster.
- [[The_Unit_Circle]] — the polar form is trigonometry wearing a different hat, so the standard sine and cosine values must be second nature.
- [[Introduction_To_Polar_Coordinates]] — the $(r, \theta)$ coordinate picture is exactly the geometry polar form is built on.

---

## Problems Involving Polar Form Of Complex Numbers

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polar_form_of_complex_numbers"></div>

---

## See Also

- [[The_Complex_Number_System]] — the rectangular side of the story
- [[Complex_Zeros]] — once you have roots of a polynomial, polar form is the cleanest way to describe them geometrically
- [[Introduction_To_Polar_Coordinates]] — where the $(r, \theta)$ picture first appeared
- [[The_Unit_Circle]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
