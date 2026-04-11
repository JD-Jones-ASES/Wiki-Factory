---
title: "The Complex Number System"
type: topic
aliases: ["Complex Numbers", "Imaginary Numbers", "Arithmetic of Complex Numbers"]
tags: ["#branch-algebra-2", "#topic-complex-numbers", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "3", section: "3.1"}
related:
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/precalculus/Complex_Zeros"
  - "topics/precalculus/Polar_Form_Of_Complex_Numbers"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
problem_type_ids: []
figures: ["precalculus/complex_plane.svg"]
summary: "A second kind of number built by declaring that the square of i equals -1, with an arithmetic that extends the real numbers cleanly."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > The Complex Number System

# The Complex Number System

For everything you have done so far, the equation $x^2 = -1$ has been a dead end. No real number, positive or negative, can square to a negative result, so problems that demanded it were simply labeled "no real solution" and set aside. Mathematicians eventually decided to stop setting those problems aside. Instead of refusing, they invented a new symbol, called it $i$, and declared by fiat that

$$
i^2 = -1.
$$

That single declaration — one symbol, one rule — opens up an entire second dimension of numbers and makes every polynomial equation solvable. The symbol $i$ is called the **imaginary unit**, even though there is nothing less real about it than any other number you have ever used. The name is a historical accident from a time when the idea seemed strange.

## What a complex number looks like

Once you have $i$, you can build brand new numbers by gluing a real piece to an $i$-piece. Any expression of the form

$$
z = a + bi
$$

where $a$ and $b$ are ordinary real numbers is called a **complex number**. The piece $a$ is its **real part**, and the piece $bi$ is its **imaginary part**. Ordinary real numbers are still included — just set $b = 0$ and you get back something like $7 + 0i$, which is simply $7$. So real numbers sit inside the complex numbers as the special case with no $i$ at all.

Writing a pure imaginary number like $\sqrt{-25}$ in the standard $a + bi$ form takes one quick step. Since $-25 = 25 \cdot (-1)$, pull a $5$ out of the square root and replace the remaining $\sqrt{-1}$ with $i$: the answer is $5i$.

![[complex_plane.svg|Four complex numbers plotted on the complex plane]]

---

## Adding and subtracting

Addition and subtraction of complex numbers follow the same rule as combining like terms: the real parts combine with the real parts, and the imaginary parts combine with the imaginary parts.

$$
(a + bi) + (c + di) = (a + c) + (b + d)i
$$

Nothing special — treat $i$ the way you treat a variable. Subtraction is the same story with the signs of the second number flipped.

---

## Multiplying

Multiplication is where $i^2 = -1$ earns its keep. You start by distributing the way you would multiply any two binomials, and then you replace every $i^2$ you find with $-1$. As a worked pattern:

$$
(a + bi)(c + di) = ac + adi + bci + bd\,i^2 = (ac - bd) + (ad + bc)i.
$$

The $-bd$ in the real part is exactly where $i^2 = -1$ does its work.

A useful side observation is the **powers of $i$**. Using $i^2 = -1$, you get $i^3 = i^2 \cdot i = -i$, and then $i^4 = i^2 \cdot i^2 = (-1)(-1) = 1$. From there the pattern repeats every four steps: $i, -1, -i, 1, i, -1, -i, 1, \ldots$. To simplify a high power like $i^{23}$, divide $23$ by $4$ and keep the remainder: $23 = 4 \cdot 5 + 3$, so $i^{23} = i^3 = -i$.

---

## The conjugate and division

Given a complex number $z = a + bi$, its **complex conjugate** is obtained by flipping the sign of the imaginary part:

$$
\overline{z} = a - bi.
$$

Conjugates are extraordinarily useful because multiplying a complex number by its conjugate always gives a real, non-negative result:

$$
(a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2 i^2 = a^2 + b^2.
$$

All the imaginary parts cancel. This is the key trick for **dividing** one complex number by another: you are not really allowed to leave $i$ stuck in a denominator, just as you are not allowed to leave $\sqrt{2}$ stuck in a denominator. To clear the $i$ out of the bottom, multiply the top and bottom by the conjugate of the denominator. The denominator becomes a real number and the division collapses into ordinary arithmetic.

---

## The modulus

The **modulus** (or absolute value) of a complex number measures its size:

$$
|a + bi| = \sqrt{a^2 + b^2}.
$$

If you plot $a + bi$ as the point $(a, b)$ on the plane, this is just the straight-line distance from that point back to the origin — the Pythagorean theorem in disguise. The plane used for this picture is called the **complex plane**: the horizontal axis holds the real parts and the vertical axis holds the imaginary parts. Every complex number becomes a point, and every arithmetic operation corresponds to a geometric move on that plane.

---

## Example 1: adding, subtracting, and multiplying

> Simplify $(4 + 5i) + (-1 + 3i)$, then $(4 + 5i) - (-1 + 3i)$, then $(2 + 3i)(1 - 4i)$.

Real parts with real parts, imaginary with imaginary for the sum:

$$
(4 + 5i) + (-1 + 3i) = (4 - 1) + (5 + 3)i = 3 + 8i.
$$

Subtraction flips the signs of the second number first, so $(4 + 5i) - (-1 + 3i) = (4 + 1) + (5 - 3)i = 5 + 2i$.

For the product, distribute all four pairs and then replace $i^2$ with $-1$:

$$
(2 + 3i)(1 - 4i) = 2 - 8i + 3i - 12 i^2 = 2 - 5i - 12(-1) = 14 - 5i.
$$

---

## Example 2: dividing using the conjugate

> Write $\dfrac{3 + 2i}{1 - i}$ in the form $a + bi$.

The denominator is $1 - i$, so its conjugate is $1 + i$. Multiply both the top and bottom by that conjugate:

$$
\frac{3 + 2i}{1 - i} \cdot \frac{1 + i}{1 + i} = \frac{(3 + 2i)(1 + i)}{(1 - i)(1 + i)}.
$$

Expand the top: $(3 + 2i)(1 + i) = 3 + 3i + 2i + 2i^2 = 3 + 5i - 2 = 1 + 5i$. Expand the bottom using the difference-of-squares pattern: $(1 - i)(1 + i) = 1^2 - i^2 = 1 - (-1) = 2$.

$$
\frac{3 + 2i}{1 - i} = \frac{1 + 5i}{2} = \frac{1}{2} + \frac{5}{2} i.
$$

Both components are now real fractions, and the $i$ is safely out of the basement.

---

## Example 3: modulus

> Find the modulus of $z = -6 + 8i$.

Plug into the formula:

$$
|z| = \sqrt{(-6)^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10.
$$

Geometrically, the point $(-6, 8)$ in the complex plane sits exactly $10$ units from the origin. Notice also that the conjugate $\overline{z} = -6 - 8i$ has the same modulus, since $(-8)^2 = 8^2$. Conjugates always land at the same distance from the origin — they are mirror images across the real axis.

---

## Common pitfalls

- **Never apply $\sqrt{a}\sqrt{b} = \sqrt{ab}$ when both radicands are negative.** That rule works only when at least one is non-negative. Writing $\sqrt{-4}\sqrt{-9} = \sqrt{36} = 6$ is wrong. The correct computation is $(2i)(3i) = 6 i^2 = -6$. Always convert to $i$ form before multiplying roots of negatives.
- **Forgetting to replace $i^2$ with $-1$.** Every multiplication problem produces an $i^2$ term; if you leave it, you have only finished half the job.
- **Dropping the conjugate step in division.** Leaving $i$ in a denominator is considered unsimplified — finish the problem by multiplying the top and bottom by the conjugate.
- **Mixing up modulus and real part.** The modulus $|a + bi|$ is the Pythagorean $\sqrt{a^2 + b^2}$, never just the real part $a$.

---

## Prerequisites

- [[Solving_Quadratics_By_Square_Roots]] — the move $x^2 = -1 \Rightarrow x = \pm i$ is the bridge that makes $i$ necessary in the first place.
- [[The_Quadratic_Formula]] — once the discriminant is negative, the whole answer lives in the complex numbers, so comfort with $b^2 - 4ac$ first is essential.
- [[Multiplying_And_Dividing_Integers]] — fluency with signs makes every complex multiplication cleaner, since sign tracking is where most mistakes happen.

---

## Problems Involving The Complex Number System

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_complex_number_system"></div>

---

## See Also

- [[Complex_Zeros]] — where complex numbers fall out of polynomial equations naturally, in conjugate pairs
- [[Polar_Form_Of_Complex_Numbers]] — a second way to write $a + bi$ that turns multiplication into angle-addition
- [[The_Quadratic_Formula]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
