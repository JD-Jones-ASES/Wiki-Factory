---
title: "Square Roots and Cube Roots"
type: topic
aliases: ["Square Root", "Cube Root", "Principal Square Root", "Radical"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "1", section: "1.1.4"}
related:
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/The_Pythagorean_Theorem"
  - "topics/pre_algebra/Rational_Exponents"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Exponents_And_Powers"
problem_type_ids: []
figures: []
summary: "Square roots, cube roots, and how to evaluate and estimate them."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Square Roots and Cube Roots

# Square Roots and Cube Roots

A **square root** asks a backwards question. Instead of "what do I get when I square $7$?" you ask, "what number, squared, gives me $49$?" The answer is $7$, and the symbol for this operation is $\sqrt{\phantom{x}}$, called a **radical sign**.

Cube roots work the same way for cubes. Instead of computing $4^3 = 64$, you start with $64$ and ask which number, cubed, produces it. Roots undo powers, the way subtraction undoes addition and division undoes multiplication.

---

## What a square root is

Formally, a square root of a non-negative number $n$ is any number $b$ satisfying $b^2 = n$. The number sitting under the radical sign is called the **radicand**.

Notice a subtlety: every positive number actually has two numbers that square to it. For $25$, both $5$ and $-5$ work, because

$$
5^2 = 25 \quad \text{and} \quad (-5)^2 = 25.
$$

To avoid ambiguity whenever you see the symbol $\sqrt{25}$, mathematicians use a convention: the radical always means the **principal square root**, which is the non-negative one. So $\sqrt{25} = 5$, even though $-5$ is also technically a square root of $25$.

A few things fall out of this convention:

- $\sqrt{0} = 0$. Zero squared is zero, and there's nothing negative about it.
- The expression $\sqrt{-4}$ does not name a real number. No real number, positive or negative, squares to a negative result — squaring always produces something non-negative.
- Writing $-\sqrt{25}$ means "the negative of the principal square root," which is $-5$. The minus sign is outside the radical.

### Perfect squares worth memorizing

A **perfect square** is a whole number that is the square of a whole number. Memorizing the small ones makes evaluating square roots almost instant:

$$
1,\ 4,\ 9,\ 16,\ 25,\ 36,\ 49,\ 64,\ 81,\ 100,\ 121,\ 144.
$$

If you see $\sqrt{81}$, you want to recognize that $9 \cdot 9 = 81$ without thinking. That recognition is the whole skill.

---

## What a cube root is

A **cube root** of a number $n$ is a number $b$ satisfying $b^3 = n$. The notation puts a small $3$ in the crook of the radical:

$$
\sqrt[3]{n}.
$$

Cube roots behave differently from square roots in one important way: they are defined for negative numbers too. The reason is that cubing a negative number still produces a negative number. For example,

$$
(-3)^3 = -3 \cdot -3 \cdot -3 = -27,
$$

so $\sqrt[3]{-27} = -3$. There's no ambiguity to dodge and no convention to pick — every real number has exactly one real cube root.

### Perfect cubes worth memorizing

$$
1,\ 8,\ 27,\ 64,\ 125,\ 216.
$$

And their negatives: $-1, -8, -27, -64, -125, -216$ are also perfect cubes, via $(-1)^3 = -1$, $(-2)^3 = -8$, and so on.

---

## Worked Example 1: Evaluating a square root

> Compute $\sqrt{81}$.

Ask the backward question: which non-negative number, multiplied by itself, gives $81$? Scan your list of perfect squares. You should recognize that $9 \cdot 9 = 81$, so

$$
\sqrt{81} = 9.
$$

A quick sanity check: $9^2 = 81$. The answer checks out. And because the radical denotes the principal (non-negative) root, we don't write $\pm 9$ here — just $9$.

---

## Worked Example 2: Evaluating a cube root of a negative number

> Compute $\sqrt[3]{-64}$.

Ask: which real number, cubed, gives $-64$? Because you're cubing, a negative input is allowed. Try $-4$:

$$
(-4)^3 = (-4) \cdot (-4) \cdot (-4) = 16 \cdot (-4) = -64.
$$

So

$$
\sqrt[3]{-64} = -4.
$$

Notice what would have gone wrong if this were a square root instead. The expression $\sqrt{-64}$ has no real-number answer, because you can't square any real number and land on $-64$. Cube roots save you from that problem.

---

## Worked Example 3: Estimating a square root that isn't a perfect square

> Between which two consecutive whole numbers does $\sqrt{50}$ fall?

Not every radicand is a perfect square. Most aren't. When the radicand is not a perfect square, the square root is an **irrational** number — it has a decimal expansion that never ends and never repeats. (The formal definition of irrational comes later; for now, just note that $\sqrt{50}$ can't be written as a neat fraction or terminating decimal.)

Even though the exact value is messy, you can pin it between the two nearest perfect squares. Ask yourself: what perfect square is just below $50$? That's $49$. What perfect square is just above $50$? That's $64$.

$$
49 < 50 < 64
$$

Take square roots of all three numbers in the chain. Because squaring preserves order for non-negative numbers, so does taking the principal square root:

$$
\sqrt{49} < \sqrt{50} < \sqrt{64}
$$

$$
7 < \sqrt{50} < 8.
$$

So $\sqrt{50}$ lies strictly between $7$ and $8$. In fact, because $50$ is much closer to $49$ than to $64$, the actual value is just slightly above $7$ (it's about $7.07$). This "sandwich" technique is the standard way to estimate square roots of non-perfect squares without a calculator.

---

## A common pitfall: the radical is not distributive over addition

It is tempting — and wrong — to say $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$. Try it with $a = 9$ and $b = 16$:

$$
\sqrt{9 + 16} = \sqrt{25} = 5,
$$

but

$$
\sqrt{9} + \sqrt{16} = 3 + 4 = 7.
$$

Five and seven are not the same. The radical does *not* distribute over a sum. It does, however, distribute over a product (for non-negative values): $\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}$. Learning which operations radicals play nicely with is most of what "simplifying radicals" is about.

---

## Prerequisites

Before you practice square and cube roots, make sure you're comfortable with:

- [[Integers_And_The_Number_Line|Integers and the number line]] — because cube roots can be negative, you'll need to multiply signed numbers without hesitation.
- [[Exponents_And_Powers|Exponents and powers]] — square roots undo squares and cube roots undo cubes, so you need to know what those operations mean first.

If either of those is shaky, start there and come back.

---

## Related topics

- [[Multiplying_And_Dividing_Integers|Multiplying and dividing integers]] — the sign rules explain why odd powers preserve negatives while even powers don't.
- [[The_Pythagorean_Theorem|The Pythagorean theorem]] — one of the most common places you'll actually need square roots, when solving for a missing side of a right triangle.
- [[Rational_Exponents|Rational exponents]] — radicals rewritten as powers with fractional exponents, which is the grown-up way to handle them in algebra.

---

## Problems Involving This Topic

Pick a problem type, choose a difficulty, choose how many problems you want, and click **Add to Vault**. Your selections stay in this browser. When you're ready, open your [[Vault]] to see them all, view hints and answers, and print a worksheet.

<div class="problem-vault-widget" data-topic-slug="square_roots_and_cube_roots"></div>

---

## See Also

- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[Vault|Your Practice Vault]]
- [[_overview|Home]]
