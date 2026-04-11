---
title: "Solving Systems by Elimination"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-systems", "#key-technique", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Systems_Of_Linear_Equations"
  - "topics/algebra/Solving_Systems_By_Substitution"
  - "topics/algebra/Solving_Systems_By_Graphing"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Multi_Step_Equations"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Systems_Of_Linear_Equations"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Writing_Linear_Equations"
problem_type_ids: []
figures: []
summary: "Line up a pair of linear equations, scale them so one variable has opposite coefficients, and add the equations to make that variable disappear."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Systems by Elimination

# Solving Systems by Elimination

The **elimination method** (sometimes called the addition method) is one of the three standard ways to solve a system of linear equations, and it is the fastest method when both equations are already in standard form $ax + by = c$. The strategy is short enough to summarize in a sentence: scale the two equations so that one variable has opposite coefficients, then add the equations together so that variable disappears. Whatever is left is a single equation in a single variable, and you can finish it off with the usual linear-equation machinery.

Pair this page with [[Solving_Systems_By_Substitution]] and [[Solving_Systems_By_Graphing]] for the full picture of how systems are solved. Each method has cases where it is the fastest, and elimination wins when both equations are in standard form with friendly coefficients.

## The core idea

Here is the insight. If $a = b$ and $c = d$ are both true, then $a + c = b + d$ is also true. In plain English: if you add equals to equals, the results are still equal. So you can always take a pair of equations and add them together to produce a new, perfectly valid equation.

Usually "adding equations" would just make things more complicated. But if you can first arrange for one variable to have opposite coefficients in the two equations — say, $+5y$ in the first and $-5y$ in the second — then when you add them, the $y$ terms cancel and you are left with a single equation that contains only $x$. One variable has been eliminated, and the problem has reduced to a linear equation you already know how to solve.

The trick is usually **engineering** those opposite coefficients. Rarely do they appear for free. Most of the time you have to multiply one or both equations by carefully chosen constants first. Once the setup is right, the addition step does all the work.

## The procedure

Here is the method in full.

1. **Put both equations in standard form.** Both should look like $ax + by = c$ with the variable terms aligned. If one equation is in a different form, rearrange it.
2. **Pick the variable to eliminate.** Look at the coefficients. If one variable already has opposite coefficients in the two equations, you are ready to add. If one variable has equal coefficients, subtract one equation from the other (or multiply one equation by $-1$ and then add). If nothing lines up, multiply one or both equations by chosen constants to create opposite coefficients on the chosen variable.
3. **Add the equations.** The target variable cancels, and you are left with a single equation in the other variable. Solve it.
4. **Back-substitute.** Plug the value you just found into either original equation to get the second variable.
5. **Verify.** Check the ordered pair in both originals.

## Picking the multiplier

Engineering the opposite coefficients is the only creative step in elimination, and it is worth thinking about carefully. Suppose the two equations have $y$-coefficients $3$ and $-2$. You want those to become opposites. The least common multiple of $3$ and $2$ is $6$, so aim for $+6y$ and $-6y$. Multiply the first equation by $2$ (to turn $3y$ into $6y$) and the second equation by $3$ (to turn $-2y$ into $-6y$). Now the $y$-terms are opposites and will cancel when you add.

Another example: coefficients $4$ and $6$ on the same variable. The least common multiple is $12$. Multiply the first equation by $3$ and the second by $-2$ (or the first by $-3$ and the second by $2$) to get $+12$ and $-12$. Either choice works; both produce opposite coefficients.

If one coefficient is already a multiple of the other, you only need to scale one equation. Coefficients $2$ and $6$? Multiply the first by $-3$ and the $2$ becomes $-6$, opposite to the second equation's $6$. No need to scale the second equation at all.

## When a single multiplier is not enough

Sometimes the coefficients on **both** variables are ugly, and you will need to scale both equations even to eliminate one variable. This is fine — it just means more arithmetic up front. The payoff is that the resulting single-variable equation is still clean and easy to solve. Do not be put off by having to multiply both equations; it is the right move when no simple rescaling of one equation alone will create opposite coefficients.

## Worked examples

### Example 1: no multiplication needed

Find the ordered pair $(x, y)$ that satisfies

$$
\begin{cases} 2x + 3y = 12 \\ 2x - y = 4 \end{cases}
$$

Both equations are in standard form. Notice that the $x$-coefficients are already identical — both are $2$. That means subtracting the second equation from the first will cancel the $x$-terms:

$$
(2x + 3y) - (2x - y) = 12 - 4.
$$

Expand carefully, paying attention to the signs from the second equation:

$$
2x + 3y - 2x + y = 8
$$

$$
4y = 8.
$$

The $2x$ terms cancel as planned. Divide each side by $4$: $y = 2$. Back-substitute into the simpler original equation, $2x - y = 4$, which becomes $2x - 2 = 4$. Peel off the $-2$ by adding $2$ to each side: $2x = 6$. Divide each side by $2$: $x = 3$. The solution is $(3, 2)$.

Verification: $2(3) + 3(2) = 6 + 6 = 12$ (check), and $2(3) - 2 = 4$ (check). Both equations hold, confirming $(3, 2)$.

### Example 2: one multiplier

Determine the ordered pair $(x, y)$ satisfying

$$
\begin{cases} 3x + 2y = 5 \\ x + 4y = 11 \end{cases}
$$

The coefficients do not line up as opposites, so scaling is needed. One path: multiply the second equation by $-3$ to turn its $x$-coefficient into $-3$, which is the opposite of the first equation's $3$.

Multiply every term in the second equation by $-3$:

$$
-3 \cdot (x + 4y) = -3 \cdot 11
$$

$$
-3x - 12y = -33.
$$

Add this to the first equation term by term:

$$
(3x + 2y) + (-3x - 12y) = 5 + (-33)
$$

$$
-10y = -28.
$$

Divide each side by $-10$: $y = \tfrac{28}{10} = \tfrac{14}{5}$. That is already cleaner as a fraction, so keep it that way. Back-substitute into the simpler original, $x + 4y = 11$:

$$
x + 4 \cdot \tfrac{14}{5} = 11
$$

$$
x + \tfrac{56}{5} = 11
$$

$$
x = 11 - \tfrac{56}{5} = \tfrac{55}{5} - \tfrac{56}{5} = -\tfrac{1}{5}.
$$

The solution is $\left(-\tfrac{1}{5}, \tfrac{14}{5}\right)$. Verification in the first original: $3 \cdot (-\tfrac{1}{5}) + 2 \cdot \tfrac{14}{5} = -\tfrac{3}{5} + \tfrac{28}{5} = \tfrac{25}{5} = 5$ (check). Verification in the second: $-\tfrac{1}{5} + 4 \cdot \tfrac{14}{5} = -\tfrac{1}{5} + \tfrac{56}{5} = \tfrac{55}{5} = 11$ (check).

### Example 3: both equations need multipliers

Maya encounters the system

$$
\begin{cases} 4x + 3y = 18 \\ 3x - 2y = 5 \end{cases}
$$

The coefficients on $y$ are $3$ and $-2$. The least common multiple of $3$ and $2$ is $6$, so target opposites of $+6$ and $-6$ on the $y$-terms. Multiply the first equation by $2$ (turning $3y$ into $6y$) and the second equation by $3$ (turning $-2y$ into $-6y$).

First equation $\times 2$:

$$
2 \cdot (4x + 3y) = 2 \cdot 18
$$

$$
8x + 6y = 36.
$$

Second equation $\times 3$:

$$
3 \cdot (3x - 2y) = 3 \cdot 5
$$

$$
9x - 6y = 15.
$$

Now the $y$-coefficients are $+6$ and $-6$, perfect opposites. Add the scaled equations:

$$
(8x + 6y) + (9x - 6y) = 36 + 15
$$

$$
17x = 51.
$$

Divide each side by $17$: $x = 3$. Back-substitute into the first original, $4x + 3y = 18$:

$$
4(3) + 3y = 18
$$

$$
12 + 3y = 18.
$$

Peel off the $12$ by subtracting from each side: $3y = 6$. Divide each side by $3$: $y = 2$. The solution is $(3, 2)$.

Verification: $4(3) + 3(2) = 12 + 6 = 18$ (check), and $3(3) - 2(2) = 9 - 4 = 5$ (check). The answer holds.

## Common pitfalls

- **Dropping a sign when adding.** The subtraction step $(2x + 3y) - (2x - y)$ becomes $0 + 4y$, not $0 + 2y$. The minus sign distributes across the entire parenthesized expression, so $-(-y) = +y$. This is the number-one cause of wrong answers in elimination, so write out the expansion explicitly before combining.
- **Multiplying only one side of an equation.** When you scale an equation by a constant, every term gets multiplied — left side and right side. Multiplying only the left side destroys the equation.
- **Picking a multiplier that doesn't quite work.** If your scaled equations have coefficients $+6y$ and $-4y$ on the same variable, those are not opposites and adding will not cancel. Double-check that the sum (not difference) of the two target coefficients is zero.
- **Solving only the first variable.** After the addition step, you have one variable pinned down, but a solution of a system is an **ordered pair**. Back-substitute to find the second variable. Do not stop at one.
- **Misreading a no-solution or infinite-solution system.** If elimination produces a statement like $0 = 7$, the system has no solution — the equations are inconsistent. If it produces $0 = 0$, the system has infinitely many solutions — the two equations describe the same line. Do not try to force an ordered pair out of these cases.

## Problems Involving Solving Systems by Elimination

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_systems_by_elimination"></div>

## See Also

- [[Systems_Of_Linear_Equations]]
- [[Solving_Systems_By_Substitution]]
- [[Solving_Systems_By_Graphing]]
- [[Writing_Linear_Equations]]
- [[Multi_Step_Equations]]
- [[Systems_Of_Linear_Inequalities]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
