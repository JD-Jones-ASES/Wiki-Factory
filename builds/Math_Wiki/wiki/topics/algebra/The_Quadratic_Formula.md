---
title: "The Quadratic Formula"
type: topic
aliases: ["Quadratic Formula"]
tags: ["#branch-algebra-2", "#topic-quadratics", "#key-formula", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/algebra/The_Discriminant"
  - "topics/algebra/Graphing_Quadratic_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/Operations_With_Radicals"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "A single plug-and-chug recipe that spits out the solutions of any quadratic equation, even when factoring fails."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > The Quadratic Formula

# The Quadratic Formula

Factoring a quadratic is lovely when it works. But a great many quadratic equations — most of the ones you meet in physics, engineering, and real word problems — refuse to factor into nice integer pieces. For those, you need a tool that does not care whether the numbers are clean: a recipe you can point at any quadratic and crank out the answer. That recipe is **the quadratic formula**, and it is the single most useful formula in Algebra 2.

The formula takes any equation of the form $ax^2 + bx + c = 0$, with $a$ not zero, and hands you both solutions directly. No factoring, no guessing, no trial and error. It works when the answers are integers, it works when they are fractions, it works when they involve radicals, and it even tells you when no real solution exists. It is the universal finisher for quadratics — the "if all else fails" move that actually never fails.

## What it means / The idea

Given a quadratic equation rewritten so that one side is zero,

$$
ax^2 + bx + c = 0, \qquad a \ne 0,
$$

the two solutions for $x$ are

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$

The three coefficients you plug in — $a$, $b$, and $c$ — come from the equation in that order. The quantity $b^2 - 4ac$ under the radical is important enough to have its own name, the **discriminant**, and its sign tells you how many real solutions the equation has before you compute anything else. See [[The_Discriminant]] for the full story.

The formula comes from running the [[Completing_The_Square]] procedure on a generic $ax^2 + bx + c = 0$ instead of on a specific equation with numbers. When you complete the square symbolically, work through the algebra, and finish with a square root, exactly the formula above pops out. That is why every time you use it, you are really using completing the square in disguise — somebody did the symbolic work once, and you get to plug in numbers.

## How it works / The procedure

1. **Put the equation in standard form.** Move every term to one side so that zero sits on the other. The equation should read $ax^2 + bx + c = 0$ with one tidy quadratic on the left.
2. **Identify $a$, $b$, and $c$.** Read them off carefully. The coefficient of $x^2$ is $a$, the coefficient of $x$ is $b$, and the constant is $c$. Keep the signs attached.
3. **Plug into the formula.** Substitute the three numbers into $\dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.
4. **Simplify the inside of the radical first.** Compute $b^2$, then $4ac$, then the difference. This is the discriminant — stop for a moment and look at its sign.
5. **Take the square root.** If the discriminant is positive, you get a real number. If it is a perfect square, the root is an integer; otherwise it is irrational and you leave it as a radical.
6. **Finish the arithmetic.** The $\pm$ gives you two separate computations: one with $+\sqrt{\cdot}$ and one with $-\sqrt{\cdot}$. Each produces one solution, so you end with two values of $x$ (or one repeated value, or no real values).

A useful habit: always write the formula once with the correct $a$, $b$, $c$ already substituted, before you simplify. Most errors on this topic come from sloppy substitution, not sloppy arithmetic.

## Why it works

Running [[Completing_The_Square]] on $ax^2 + bx + c = 0$ in full generality reshapes it into

$$
\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}.
$$

Apply a square root to each side, simplify the radical on the right, and solve for $x$. The algebra is tidy; the result is the formula. So the quadratic formula is not magic sitting on its own — it is the completed-square identity after you finish the steps.

## Worked examples

### Example 1

Find all real solutions to $2x^2 + 5x - 3 = 0$.

The equation is already in standard form. Read off $a = 2$, $b = 5$, $c = -3$. Write the formula with these values:

$$
x = \frac{-5 \pm \sqrt{5^2 - 4(2)(-3)}}{2(2)}.
$$

Simplify inside the radical: $5^2 = 25$, and $4(2)(-3) = -24$. The discriminant is $25 - (-24) = 49$, a perfect square, which is a nice sign that this quadratic could have factored.

$$
x = \frac{-5 \pm \sqrt{49}}{4} = \frac{-5 \pm 7}{4}.
$$

Now split the $\pm$ into two cases:

$$
x = \frac{-5 + 7}{4} = \frac{2}{4} = \frac{1}{2} \qquad \text{or} \qquad x = \frac{-5 - 7}{4} = \frac{-12}{4} = -3.
$$

So $x = \tfrac{1}{2}$ or $x = -3$. As a double-check, this quadratic does factor: $2x^2 + 5x - 3 = (2x - 1)(x + 3)$, and those same roots pop out of the factored form.

### Example 2

Find all real solutions to $x^2 - 6x + 9 = 0$.

Here $a = 1$, $b = -6$, $c = 9$. Plug in:

$$
x = \frac{-(-6) \pm \sqrt{(-6)^2 - 4(1)(9)}}{2(1)} = \frac{6 \pm \sqrt{36 - 36}}{2} = \frac{6 \pm 0}{2}.
$$

The discriminant is zero, so the $\pm$ collapses — both branches give the same thing:

$$
x = \frac{6}{2} = 3.
$$

There is exactly one real solution, $x = 3$, and it is sometimes called a "repeated root" or a "double root." Whenever the discriminant comes out to zero, you get one solution instead of two. Geometrically, this corresponds to a parabola that touches the $x$-axis at a single point without crossing it.

Notice carefully what happened to the sign on $b$. The coefficient was $-6$, and the formula begins with $-b$, so we computed $-(-6) = +6$. A very frequent mistake is to forget the outer negative and write $-6$ instead of $+6$. Watch the signs.

### Example 3

Find all real solutions to $x^2 + x + 1 = 0$.

Now $a = 1$, $b = 1$, $c = 1$. Plug in:

$$
x = \frac{-1 \pm \sqrt{1^2 - 4(1)(1)}}{2(1)} = \frac{-1 \pm \sqrt{1 - 4}}{2} = \frac{-1 \pm \sqrt{-3}}{2}.
$$

The discriminant is $-3$, which is negative. Over the real numbers, a negative cannot have a square root, so the equation has **no real solutions**. If this were an Algebra 2 chapter on complex numbers, you would continue by writing $\sqrt{-3} = i\sqrt{3}$ and reporting the two complex solutions $x = \tfrac{-1 \pm i\sqrt{3}}{2}$. See [[The_Complex_Number_System]] for that continuation. But as far as the real line is concerned, this parabola never crosses it.

These three examples illustrate the three possible behaviors of the formula: two distinct real solutions (Example 1), one repeated real solution (Example 2), and no real solutions (Example 3). The discriminant picks which of the three you are in before you ever touch the square root.

## Common pitfalls

- **Sign error on $-b$.** The formula begins with $-b$, not $b$. If the coefficient of $x$ is $-7$, then $-b = -(-7) = +7$. Skipping the outer minus sign is the top-one error on this topic.
- **Dropping a sign under the radical.** The discriminant is $b^2 - 4ac$. If $c$ is negative, then $-4ac$ becomes a **positive** contribution — for example, $-4(2)(-3) = +24$. Tracking the signs carefully inside the radical is worth slowing down for.
- **Forgetting the equation must be in standard form first.** The formula only works on $ax^2 + bx + c = 0$. If the equation is $x^2 + 3x = 10$, you have to move the $10$ to the left first to get $x^2 + 3x - 10 = 0$ and then read off $c = -10$.
- **Writing $-b \pm \sqrt{\ldots}$ over $2$ instead of $2a$.** The denominator is $2a$, not $2$. If $a = 3$, the denominator is $6$. Putting in the wrong denominator rescales both roots and gives a wrong answer.
- **Stopping after finding only one root.** The $\pm$ gives you two separate computations; both answers are solutions. If you only wrote the $+$ branch and moved on, you only found half the truth.
- **Reporting a real solution when the discriminant is negative.** A negative discriminant means no real $x$ value makes the equation zero. Do not invent a number; report no real solution (or, in contexts that allow complex numbers, proceed using $i$).

## Problems Involving The Quadratic Formula

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_quadratic_formula"></div>

## See Also

- [[Completing_The_Square]] — the technique the formula is distilled from
- [[Solving_Quadratics_By_Factoring]] — the faster method when the quadratic factors cleanly
- [[Solving_Quadratics_By_Square_Roots]] — when the middle coefficient is already gone
- [[The_Discriminant]] — the sign inside the radical that previews how many solutions you get
- [[Graphing_Quadratic_Functions]]
- [[The_Complex_Number_System]] — what happens when the discriminant is negative
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
