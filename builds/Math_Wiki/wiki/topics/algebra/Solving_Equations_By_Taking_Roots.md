---
title: "Solving Equations by Taking Roots"
type: topic
aliases: []
tags: ["#branch-algebra-2", "#topic-quadratics", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/algebra/Solving_Equations_By_Factoring"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Solving_Equations_In_One_Variable"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Solving_Quadratics_By_Square_Roots"
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
problem_type_ids: []
figures: []
summary: "When a squared expression sits alone on one side of the equation, take a square root — and remember the plus-or-minus."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Solving Equations by Taking Roots

# Solving Equations by Taking Roots

Most quadratic equations you meet have a middle $bx$ term, and the techniques for handling those are [[Solving_Quadratics_By_Factoring|factoring]], [[Completing_The_Square|completing the square]], or [[The_Quadratic_Formula|the quadratic formula]]. But a surprising number of quadratics arrive with no middle term at all — equations like $x^2 = 49$, or $(x - 3)^2 = 16$, or $3x^2 - 48 = 0$. For these, the fastest way forward is to do the most literal thing possible: apply a square root to each side of the equation. This page walks through that technique, which is called the **square root property** or "taking roots," and shows you when it is the right tool for the job.

## The square root property

Here is the principle. Suppose an equation has the form

$$
X^2 = k,
$$

where $X$ is some expression containing the variable and $k$ is a number. The square root property says:

- If $k > 0$, there are two real solutions: $X = \sqrt{k}$ or $X = -\sqrt{k}$, usually written $X = \pm \sqrt{k}$.
- If $k = 0$, there is exactly one solution: $X = 0$.
- If $k < 0$, there are no real solutions, because no real number squared is negative. (Complex solutions do exist — $X = \pm i\sqrt{|k|}$ — but that is an Algebra 2 extension; most test items stay in the real numbers.)

The crucial detail is the $\pm$. When you take a square root, you are asking "what number squared gives $k$?" and the answer is always a pair, one positive and one negative. Both numbers square to the same $k$, so both are legitimate solutions. Dropping the negative root is the single most common mistake on this topic, and the one that shows up most often on the SAT and ACT.

## The procedure

The square root method is a good fit exactly when the equation can be massaged into the shape $X^2 = k$ with no leftover $x$ terms. Here is the procedure:

1. **Isolate the square.** Use the usual linear moves (add, subtract, multiply, divide) to get the squared expression by itself on one side of the equation. Everything else, including constants, moves to the other side.
2. **Apply the square root property.** Write $X = \pm \sqrt{k}$. Do not forget the $\pm$.
3. **Solve the resulting linear equation.** Whatever is inside the square is now a plain linear expression — break it into the two cases (one for the positive root, one for the negative root) and solve each one.
4. **Verify in the original equation.** Because squaring can sometimes hide sign errors, it is worth plugging each answer back in.

The first step is the one that distinguishes this technique from its cousins. If you cannot get the equation to look like $X^2 = k$ without having an $x$ term left on the wrong side, this method will not work and you should reach for factoring or the quadratic formula instead.

## When this method is the right tool

Use square roots when the equation, after simplification, has no middle $bx$ term — that is, when the only variable content is a single squared expression. Three telltale shapes:

- $x^2 = k$ — the simplest case. The square is already isolated.
- $(x + p)^2 = k$ — a binomial squared. Treat $(x + p)$ as the single variable $X$ and take a root.
- $ax^2 + c = 0$ — a quadratic with no linear term. Isolate $x^2$ first, then take a root.

Any quadratic after [[Completing_The_Square]] always has this shape — in fact, that is the entire point of completing the square. And equations of the form $(x + p)^2 = k$ show up constantly in geometry and vertex-form problems.

## Worked examples

### Example 1

Find all real values of $x$ for which $x^2 = 81$.

The square is already alone on the left side, and $81 > 0$, so the square root property applies directly. Apply a square root to each side and include the plus-or-minus:

$$
x = \pm \sqrt{81} = \pm 9.
$$

That gives two solutions: $x = 9$ or $x = -9$. A fast verification: $9^2 = 81$ (check), and $(-9)^2 = 81$ (check). Both squares land on $81$, which is why both values are roots of the equation.

If you had written only $x = 9$, you would have handed in half the answer. The equation $x^2 = 81$ has two real solutions, and the $\pm$ keeps both of them visible throughout your work.

### Example 2

Determine all values of $x$ for which $(x + 2)^2 = 25$.

The squared expression $(x + 2)^2$ is already isolated on the left. Think of $x + 2$ as a single quantity $X$. The equation says $X^2 = 25$, so apply the square root property:

$$
x + 2 = \pm \sqrt{25} = \pm 5.
$$

Now split into the two linear cases:

$$
x + 2 = 5 \qquad \text{or} \qquad x + 2 = -5.
$$

Solve each one by subtracting $2$ from each side:

$$
x = 3 \qquad \text{or} \qquad x = -7.
$$

Verification in the original: $(3 + 2)^2 = 5^2 = 25$ (check), and $(-7 + 2)^2 = (-5)^2 = 25$ (check). The two solutions are $x = 3$ and $x = -7$.

### Example 3

Rohan is solving the equation $3x^2 - 48 = 0$. What are all real values of $x$?

The squared term is not yet alone. First rearrange so the $x^2$ is isolated. Add $48$ to each side:

$$
3x^2 = 48.
$$

Now divide each side by $3$:

$$
x^2 = 16.
$$

With the square isolated, apply the square root property:

$$
x = \pm \sqrt{16} = \pm 4.
$$

So there are two solutions: $x = 4$ and $x = -4$. Verification in the original equation: $3(4)^2 - 48 = 48 - 48 = 0$ (check), and $3(-4)^2 - 48 = 48 - 48 = 0$ (check). Both check out.

Notice that this equation could also have been factored as $3(x^2 - 16) = 3(x - 4)(x + 4) = 0$ and solved by [[Solving_Equations_By_Factoring]]. Both approaches give the same answer. Square roots tend to be faster when the middle term is missing; factoring is faster when the coefficients are small integers and the trinomial splits cleanly. Pick whichever path gets you to the answer with the least arithmetic.

## Common pitfalls

- **Dropping the negative root.** This is the top mistake on every form of this topic. Every time you take a square root to solve an equation, two solutions appear — one positive and one negative. Writing $x = \sqrt{k}$ instead of $x = \pm \sqrt{k}$ silently loses half the answer. If there is exactly one root ($k = 0$), say so explicitly.
- **Taking the root before isolating the square.** From $3x^2 - 48 = 0$, you cannot just rewrite the left side. Clean off the $-48$ and the $3$ first, so that the left side reads $x^2$ alone. Otherwise the square root property is not applicable.
- **Taking a square root of a negative.** If the right side comes out negative after isolation, the equation has **no real solutions**. Write "no real solutions" and stop — do not try to take a square root of a negative number in real-number work.
- **Squaring a sum term-by-term.** When you have $(x + 2)^2$, the square root property gives $x + 2 = \pm 5$, not $x^2 + 4 = \pm 5$. And when you expand $(x + 2)^2$, it is $x^2 + 4x + 4$, not $x^2 + 4$. Both of these are pattern errors, and both cost points on tests.
- **Forgetting the two cases.** After taking a root, write out the two linear equations separately: one for the positive case and one for the negative. Solving them together in your head is where sign errors creep in.

## Problems Involving Solving Equations by Taking Roots

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_equations_by_taking_roots"></div>

## See Also

- [[Solving_Quadratics_By_Square_Roots]]
- [[Solving_Equations_By_Factoring]]
- [[Completing_The_Square]]
- [[The_Quadratic_Formula]]
- [[Solving_Equations_In_One_Variable]]
- [[Parabolas]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
