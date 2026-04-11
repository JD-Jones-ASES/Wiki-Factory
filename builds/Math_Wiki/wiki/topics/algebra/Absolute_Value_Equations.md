---
title: "Absolute Value Equations"
type: topic
aliases: ["Equations with Absolute Value"]
tags: ["#branch-algebra-2", "#topic-linear", "#key-technique", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/algebra/Absolute_Value_Functions"
  - "topics/pre_algebra/Absolute_Value_And_Opposites"
  - "topics/algebra/Multi_Step_Equations"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/pre_algebra/Absolute_Value_And_Opposites"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/One_Step_Equations"
problem_type_ids: []
figures: []
summary: "Strip the bars, split into two linear cases, and solve each one — that is the whole playbook."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Absolute Value Equations

# Absolute Value Equations

The absolute value bars around an expression are really asking a very particular question: **how far from zero is this number sitting on the number line?** Distance does not care about direction — the number $5$ is five units from zero, and so is $-5$. That little fact, that two different numbers can sit the same distance from zero, is why absolute value equations almost always produce **two** solutions instead of one. Whenever an equation contains a bar expression set equal to a positive number, the thing inside the bars is allowed to be either that positive value or its opposite, and both possibilities usually give valid answers.

The playbook for solving them is short: isolate the absolute value expression, split the equation into two linear cases, solve each case, and check. The word "split" is the big idea. You are turning a single, nonlinear equation into a pair of linear equations you already know how to solve. Everything else on this page is support for that one move.

## What it means / The idea

An **absolute value equation** is any equation that has a variable sitting inside absolute value bars. The bread-and-butter shape is

$$
|ax + b| = k
$$

where $a$, $b$, and $k$ are real numbers. The equation says "the distance from zero of the expression $ax + b$ equals $k$." Three things can happen depending on the right-hand side:

- **If $k > 0$**, there are two numbers at distance $k$ from zero (namely $k$ and $-k$), so the equation splits into two cases:
  $$
  ax + b = k \qquad \text{or} \qquad ax + b = -k
  $$
  Each case is a linear equation you finish by the [[One_Step_Equations|one-step]] or [[Multi_Step_Equations|multi-step]] moves you already know.
- **If $k = 0$**, the only number at distance $0$ from zero is $0$ itself, so the equation becomes a single linear case:
  $$
  ax + b = 0
  $$
  This is the one scenario where an absolute value equation has exactly one solution instead of two.
- **If $k < 0$**, there is no number whose distance from zero is negative, so the equation has **no solution**. Distance is never negative, and an equation like $|x - 4| = -5$ is simply a false statement no matter what $x$ is.

So before you split cases, glance at the right side. A positive number means two cases; zero means one case; a negative number means stop immediately and report no solution.

## How it works / The procedure

1. **Isolate the absolute value expression.** Get the bars alone on one side of the equation, with everything else on the other side. If the equation begins as $3|x + 2| - 5 = 7$, add $5$ and divide by $3$ first, so the bars stand alone.
2. **Inspect the right-hand side.** If it is negative, stop — no solution. If it is zero, there is one linear equation to solve. If it is positive, there are two.
3. **Write the two cases** (when positive). Drop the bars, and create one equation where the inside equals $k$ and another where the inside equals $-k$.
4. **Solve each linear equation separately** using regular multi-step techniques.
5. **Check each answer in the original equation.** Usually both check. Sometimes, especially when you had to do a lot of algebra before isolating the bars, one answer comes out to be extraneous, and this step will catch it.

## Why it works

The definition of $|y|$ is "the distance from $y$ to zero," which is the same as saying $|y| = y$ when $y \ge 0$ and $|y| = -y$ when $y < 0$. So when you encounter $|\text{stuff}| = k$, you are really saying that "stuff" is one of the two numbers $\{k, -k\}$, because those are the only numbers at distance $k$ from zero. Splitting into cases is just making both of those possibilities explicit and asking which values of $x$ land in each case. There is no hidden trick — the bars literally mean "one of these two things is happening."

## Worked examples

### Example 1

Determine all values of $x$ satisfying $|x - 5| = 3$.

The bars are already alone on the left side, and the right side is $3$, which is positive, so there are two linear cases:

$$
x - 5 = 3 \qquad \text{or} \qquad x - 5 = -3
$$

Add $5$ to both sides of each equation separately:

$$
x = 8 \qquad \text{or} \qquad x = 2.
$$

Check each in the original. For $x = 8$: $|8 - 5| = |3| = 3$. For $x = 2$: $|2 - 5| = |-3| = 3$. Both check, so the solutions are $x = 2$ and $x = 8$. Notice that these two answers sit equally far from $5$ on the number line — that makes sense, because the equation literally said "$x$ is $3$ units away from $5$."

### Example 2

Give all values of $x$ satisfying $|2x + 1| = 9$.

The bars are alone, and $9$ is positive, so split into two cases:

$$
2x + 1 = 9 \qquad \text{or} \qquad 2x + 1 = -9.
$$

Solve the first: subtract $1$ from both sides to get $2x = 8$, then divide by $2$ to get $x = 4$.

Solve the second: subtract $1$ from both sides to get $2x = -10$, then divide by $2$ to get $x = -5$.

Check. For $x = 4$: $|2(4) + 1| = |9| = 9$. For $x = -5$: $|2(-5) + 1| = |-9| = 9$. Both check. The solutions are $x = 4$ and $x = -5$.

### Example 3

Find all $x$ such that $|x + 4| = 0$.

The bars are alone, and the right side is $0$. That is the special case: the only number whose distance from zero is zero is zero itself, so you do **not** write two cases. You write one:

$$
x + 4 = 0.
$$

Subtract $4$ from both sides to get $x = -4$. Check: $|-4 + 4| = |0| = 0$. The single solution is $x = -4$.

It is worth pausing on this example because it is often the one that trips people up. The temptation is to write $x + 4 = 0$ and $x + 4 = -0$ as two separate cases, which of course give the same answer. That is harmless but wasteful. Better to recognize the $k = 0$ case when you see it and move straight to one linear equation. Compare this to the equation $|x + 4| = -2$, which would have no solution at all, because no number has negative distance from zero. And compare both to Example 1, where the right side is a positive $3$ and there are two genuinely different linear cases to handle.

## Common pitfalls

- **Forgetting the negative case.** The most common error on this topic is writing only $ax + b = k$ and moving on. If $k > 0$, you also need $ax + b = -k$, and that second case produces a second solution. Missing it halves your answer set.
- **Splitting the cases before isolating the bars.** If the equation is $|2x - 1| + 3 = 10$, you must subtract $3$ first to get $|2x - 1| = 7$, and then split. Splitting before isolating gives you two wrong linear equations.
- **Reporting a solution when the right side is negative.** An equation like $|x + 6| = -4$ has no solutions, full stop. Do not split it into $x + 6 = -4$ and $x + 6 = 4$ — both of those "solutions" fail when you check them in the original, because the absolute value of anything is not $-4$.
- **Treating $|x| = 0$ as two solutions.** $x = 0$ is the only answer. Writing $x = 0$ or $x = -0$ is redundant (they are the same number) and should be collapsed to a single case.
- **Skipping the check.** Checking matters especially when the equation required several moves to isolate the bars. A sign that flipped or a term that got dropped can produce an answer that looks right algebraically but fails when you plug it back into the original.

## Problems Involving Absolute Value Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="absolute_value_equations"></div>

## See Also

- [[Absolute_Value_Inequalities]] — the next topic over, where the bars equal a range instead of a point
- [[Absolute_Value_Functions]] — the function-flavored view of the same expression
- [[Multi_Step_Equations]] — the machinery you use after splitting into cases
- [[Absolute_Value_And_Opposites|Absolute Value and Opposites]] — the pre-algebra definition this page builds on
- [[One_Step_Equations]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
