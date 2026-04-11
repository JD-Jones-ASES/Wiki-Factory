---
title: "Completing the Square"
type: topic
aliases: ["Complete the Square"]
tags: ["#branch-algebra-2", "#topic-quadratics", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "3", section: "3.5"}
related:
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/algebra/Solving_Quadratics_By_Factoring"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/The_Discriminant"
  - "topics/algebra/Special_Products"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Graphing_Quadratic_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Special_Products"
  - "topics/algebra/Factoring_Special_Forms"
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: ["algebra/perfect_square_completion.svg"]
summary: "Rebuild any quadratic into (x - h)^2 = k by manufacturing a perfect square trinomial, then finish with a square root."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Completing the Square

# Completing the Square

You already know how to solve a quadratic of the form $(x - h)^2 = k$ — apply a square root to each side and read off the answers. See [[Solving_Quadratics_By_Square_Roots]] for the short version. The only catch is that most quadratic equations you meet in the wild do **not** arrive wearing that convenient shape. You will see things like $x^2 + 8x - 3 = 0$, where there is a lone $x$ stirring up the middle, no perfect square in sight.

**Completing the square** is the procedure for reshaping any quadratic equation into the $(x - h)^2 = k$ form so that the square root shortcut suddenly works. You do not wait for a perfect square to appear — you build one.

![[perfect_square_completion.svg|The geometric completion of a square]]

The key insight is that every expression of the form $x^2 + bx$ is just one carefully chosen constant away from being a perfect square trinomial.

---

## The perfect square trinomial pattern

From [[Special_Products]] and [[Factoring_Special_Forms]] you already know the pattern

$$
(x + p)^2 = x^2 + 2px + p^2.
$$

Read that identity from right to left. If the middle coefficient of a trinomial $x^2 + (\text{something})x + (\text{something else})$ is exactly $2p$, then the last term **must** be $p^2$ for the whole thing to factor as $(x + p)^2$.

So if the middle coefficient is $b$, then $b = 2p$, which means $p = b/2$. And the required last term is

$$
p^2 = \left(\frac{b}{2}\right)^2.
$$

That is the whole secret of completing the square: given any expression $x^2 + bx$, halve the middle coefficient, then square the result. The number you get is the unique constant that turns $x^2 + bx$ into a perfect square trinomial. In symbols,

$$
x^2 + bx + \left(\frac{b}{2}\right)^2 = \left(x + \frac{b}{2}\right)^2.
$$

**Why it works.** The right-hand expansion has middle term $2 \cdot x \cdot (b/2) = bx$, which matches what we started with. And the right-hand constant is $(b/2)^2$, which is exactly what we added. Nothing was fudged — we just used the perfect-square identity in reverse.

---

## The algorithm (monic case: leading coefficient is 1)

Here is the procedure for solving $x^2 + bx + c = 0$ when the coefficient in front of $x^2$ is $1$:

1. **Move the constant.** Slide $c$ to the right side so the quadratic piece sits alone: $x^2 + bx = -c$.
2. **Halve the middle coefficient, then square the result.** That number is $(b/2)^2$.
3. **Add it to both sides.** This is a critical step. The new constant belongs on both sides of the equation, not just the left — otherwise you change what the equation says.
4. **Factor the left side as a perfect square.** Because of the identity above, the left side automatically becomes $(x + b/2)^2$.
5. **Finish with a square root.** Apply the square root property and solve the remaining linear equation.

Steps 1–4 reshape the equation. Step 5 is just [[Solving_Quadratics_By_Square_Roots]] taking over at the finish line.

### A caution about the balance move

The number $(b/2)^2$ that you manufacture in step 2 **must** be added to both sides. If you only drop it on the left, you have secretly changed the equation — the two sides no longer represent the same truth, and the answers you get will be wrong. Think of the equals sign as a balance scale: anything you add to one pan has to land on the other pan too.

---

## Example 1: a clean monic case

> Find all real solutions to $x^2 + 6x - 7 = 0$.

**Move the constant.** Send $-7$ to the right side by adding $7$ to both sides:

$$
x^2 + 6x = 7.
$$

**Find $(b/2)^2$.** Here $b = 6$, so halve the middle coefficient to get $3$, and square the result to get $9$. That $9$ is what the left side needs to become a perfect square.

**Add $9$ to both sides.**

$$
x^2 + 6x + 9 = 7 + 9
$$

$$
x^2 + 6x + 9 = 16.
$$

**Factor the left side.** By the perfect square trinomial pattern,

$$
(x + 3)^2 = 16.
$$

**Apply the square root property.**

$$
x + 3 = \pm\sqrt{16} = \pm 4.
$$

Split into the two linear cases and solve:

$$
x + 3 = 4 \quad\text{or}\quad x + 3 = -4
$$

$$
x = 1 \quad\text{or}\quad x = -7.
$$

Both solutions check back into the original equation, so the answer is $x = 1$ or $x = -7$. (For this particular equation, factoring would also have worked — $x^2 + 6x - 7 = (x + 7)(x - 1)$ — but completing the square is the method that works even when factoring does not.)

---

## Example 2: a tidier monic case

> Find all real solutions to $x^2 - 10x + 21 = 0$.

Move the constant:

$$
x^2 - 10x = -21.
$$

Here $b = -10$, so $b/2 = -5$ and $(b/2)^2 = 25$. Add $25$ to both sides:

$$
x^2 - 10x + 25 = -21 + 25
$$

$$
(x - 5)^2 = 4.
$$

A key move: the sign inside the factored square matches the sign of $b/2$. Because $b/2 = -5$, the perfect square on the left is $(x - 5)^2$, not $(x + 5)^2$. Getting this sign wrong is one of the top errors on this topic.

Apply a square root to each side:

$$
x - 5 = \pm 2
$$

$$
x = 5 \pm 2.
$$

So $x = 7$ or $x = 3$. A quick substitution into the original equation confirms both.

---

## Example 3: when the leading coefficient is not 1

> Find all real solutions to $2x^2 + 8x - 10 = 0$.

The pattern $x^2 + bx + (b/2)^2 = (x + b/2)^2$ assumes the coefficient on $x^2$ is exactly $1$. Whenever the leading coefficient is not $1$, start by forcing the leading coefficient down to $1$ before anything else.

**Divide every term by $2$.**

$$
x^2 + 4x - 5 = 0.
$$

Now the equation is monic, and the rest proceeds exactly like Examples 1 and 2.

Move the constant:

$$
x^2 + 4x = 5.
$$

Halve the middle coefficient: $4/2 = 2$. Square it: $2^2 = 4$. Add to both sides:

$$
x^2 + 4x + 4 = 9
$$

$$
(x + 2)^2 = 9.
$$

Square-root both sides:

$$
x + 2 = \pm 3
$$

$$
x = -2 \pm 3.
$$

So $x = 1$ or $x = -5$.

The two takeaways from this example: (1) always strip the leading coefficient first when it is not $1$, either by dividing through or by factoring it out; (2) the $(b/2)^2$ recipe uses the new middle coefficient after the divide, not the old one.

---

## Why every quadratic formula comes from here

Completing the square is not just one solution method among many — it is the engine that produces [[The_Quadratic_Formula]]. If you run the exact same five steps on the general equation $ax^2 + bx + c = 0$ (with $a \ne 0$) instead of specific numbers, the procedure spits out

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$

So every time you use the quadratic formula, you are silently invoking a completed square that somebody did for you once and for all. Understanding this derivation is why Algebra 2 teachers insist on drilling the technique even after you know the formula — it keeps the formula from being magic.

It also explains the quantity $b^2 - 4ac$ inside the radical. That is the **discriminant**, and its sign controls whether you get two real solutions, one repeated real solution, or a pair of complex solutions. See [[The_Discriminant]] for the breakdown.

---

## Common pitfalls

- **Adding $(b/2)^2$ to only one side.** The balance must stay. Every time you add a number to the left to make a perfect square, you must add the same number to the right too, or the equation stops meaning the same thing.
- **Losing the sign when you factor.** After adding $(b/2)^2$, the left side factors as $(x + b/2)^2$. The sign of $b/2$ carries through — if $b$ is negative, the inside of the parenthesis should be $x - |b/2|$. Example: for $x^2 - 10x + 25$, the factor is $(x - 5)^2$, not $(x + 5)^2$.
- **Skipping the leading-coefficient fix.** When $a \ne 1$, the $(b/2)^2$ recipe does not apply as written. You must divide every term by $a$ first (or factor $a$ out), then complete the square on the resulting monic equation.
- **Forgetting the $\pm$ at the end.** The final step is a square root, which always produces two cases. If you only wrote one, you only found one of the two solutions. See [[Solving_Quadratics_By_Square_Roots]] for more on this particular trap.
- **Using the original $b$ after dividing by $a$.** If you divided every term by $3$ at the start, the new middle coefficient is $b/3$, not $b$. Always update your numbers before halving and squaring.

---

## Prerequisites

Completing the square is a procedure that stacks several skills on top of each other. Make sure these are all solid before you try a full practice set:

- [[Special_Products]] — so you instantly recognize $(x + p)^2$ expansions and their patterns
- [[Factoring_Special_Forms]] — so you can factor a perfect square trinomial without hesitation
- [[Solving_Quadratics_By_Square_Roots]] — because this is the final step of every completed-square problem
- [[Multi_Step_Equations]] — for the arithmetic on both sides after you manufacture the constant

---

## Problems Involving Completing the Square

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="completing_the_square"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Solving_Quadratics_By_Square_Roots]] — the shortcut that waits at the end of every completed-square problem
- [[Solving_Quadratics_By_Factoring]] — the faster method when a quadratic happens to factor cleanly
- [[The_Quadratic_Formula]] — what you get when you complete the square on $ax^2 + bx + c = 0$ in full generality
- [[The_Discriminant]] — the $b^2 - 4ac$ quantity that falls out of the derivation
- [[Special_Products]]
- [[Factoring_Special_Forms]]
- [[Graphing_Quadratic_Functions]] — completing the square is how you convert a quadratic into vertex form
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
