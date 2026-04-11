---
title: "Solving Inequalities in One Variable"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-inequalities", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Solving_Multi_Step_Inequalities"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Equations_In_One_Variable"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/pre_algebra/Writing_And_Graphing_Inequalities"
  - "topics/pre_algebra/Solving_One_Step_And_Two_Step_Inequalities"
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
problem_type_ids: []
figures: []
summary: "Inequalities are solved with the same moves as equations, with one catch: multiplying or dividing by a negative reverses the direction of the inequality symbol."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Inequalities in One Variable

# Solving Inequalities in One Variable

An **inequality** is a statement that one expression is less than, greater than, less than or equal to, or greater than or equal to another. Instead of asking "for what value of $x$ are the two sides equal?" an inequality asks "for what values of $x$ is the left side smaller (or bigger, or no larger) than the right side?" The answer is almost never a single number — it is an entire range of numbers, usually described as an interval or sketched on a number line.

Solving an inequality is mostly the same as solving an equation. You apply inverse operations to both sides to get the variable by itself. There is exactly one new rule you have to remember, and it only kicks in once in a while: **if you multiply or divide both sides of an inequality by a negative number, the direction of the inequality symbol reverses.** A $<$ flips to a $>$, and vice versa. That single extra rule is responsible for almost every mistake students make on this topic.

## The four inequality symbols

Inequalities come in four flavors, and it helps to keep the punctuation straight:

- $<$ — strictly smaller than
- $>$ — strictly larger than
- $\le$ — at most (smaller, or exactly equal)
- $\ge$ — at least (larger, or exactly equal)

The "or equal to" symbols include the boundary point; the strict symbols do not. On a number line, the boundary is drawn as a closed dot for $\le$ or $\ge$, and as an open dot for $<$ or $>$. For intervals, the boundary is written with a square bracket (like $[3, \infty)$) when it is included, and a parenthesis (like $(3, \infty)$) when it is not.

## The procedure

Here is the full method for any linear inequality in one variable:

1. **Expand anything in parentheses** using the distributive property.
2. **Collect variable terms on one side and constants on the other**, using addition or subtraction. These moves **never** change the direction of the inequality symbol.
3. **Divide (or multiply) by the coefficient of the variable.** If that coefficient is **negative**, flip the inequality symbol. If it is positive, leave the symbol alone.
4. **Write the solution set.** Depending on the preferred notation, write it as an inequality ($x > 5$), as an interval ($[5, \infty)$), or as a drawing on a number line.
5. **Sanity-check with a test value.** Pick any number in your claimed solution set and substitute it into the original inequality. If the inequality holds true, your answer is likely correct; if it fails, go back and find the error.

Step 3 is the one special rule. It is worth saying out loud: **adding and subtracting never flips the symbol, but multiplying or dividing by a negative always does.** If you are unsure whether a move was a negative multiplication, pause and reason through it before writing the next line.

## Why the flip rule is real

Here is a way to convince yourself the flip rule is not arbitrary. Start with an obviously true inequality, say $2 < 5$. Now multiply both sides by $-1$:

$$
-2 \; ? \; -5.
$$

Which one is bigger? Picture the number line: $-5$ sits to the left of $-2$, which means $-2$ is the bigger of the two. So the correct symbol is $-2 > -5$, not $-2 < -5$. Notice what just happened: multiplying both sides by a negative forced the inequality symbol to flip — the ordering between the two values got **reversed**.

This phenomenon repeats for every inequality. Scaling or splitting each side by a negative factor mirrors every real value across the zero point of the number line, and mirroring swaps "left" and "right" — exactly why the symbol has to flip. Shifting both sides by the same amount, which is what addition and subtraction do, just slides every value by the same step and leaves the ordering intact, so no flip is needed there.

## Worked examples

**Example 1.** Find all real values of $x$ for which $2x - 5 > 7$.

The variable is only on the left, and there are no parentheses to expand. Start by pushing the $-5$ away from the variable. Add $5$ to each side:

$$
2x - 5 + 5 > 7 + 5
$$

$$
2x > 12.
$$

Now divide each side by $2$. Because $2$ is positive, the inequality symbol stays the same:

$$
x > 6.
$$

The solution set is every real number greater than $6$. In interval notation, that is $(6, \infty)$. Quick test: try $x = 10$. The original becomes $2(10) - 5 = 15$, and $15 > 7$ is true, so $x = 10$ is correctly in the solution set. Try $x = 5$: $2(5) - 5 = 5$, and $5 > 7$ is false — $x = 5$ is correctly not in the solution set.

**Example 2.** Give all values of $x$ that satisfy $3 - 4x \le 11$.

The variable lives inside a $-4x$ term on the left. Push the $3$ away from the variable by subtracting $3$ from each side. Subtraction does not flip the symbol:

$$
3 - 4x - 3 \le 11 - 3
$$

$$
-4x \le 8.
$$

Now divide each side by $-4$. This is the flip rule's moment — because $-4$ is **negative**, the symbol $\le$ reverses to $\ge$:

$$
x \ge -2.
$$

The solution set is every real number greater than or equal to $-2$, or $[-2, \infty)$ in interval notation. Test with $x = 0$: the original becomes $3 - 4(0) = 3$, and $3 \le 11$ is true. Test with $x = -5$: $3 - 4(-5) = 3 + 20 = 23$, and $23 \le 11$ is false. The sign flipped correctly.

**Example 3.** Zoe is working on the inequality $5(x + 2) < 3x + 10$. Determine every $x$ that satisfies it.

Start by expanding the parentheses on the left using the distributive property:

$$
5x + 10 < 3x + 10.
$$

Now collect variable terms on the left by subtracting $3x$ from each side. Subtraction does not flip the symbol:

$$
5x + 10 - 3x < 3x + 10 - 3x
$$

$$
2x + 10 < 10.
$$

Push the $10$ away from the variable by subtracting it from each side:

$$
2x < 0.
$$

Divide each side by $2$. Because $2$ is positive, no flip:

$$
x < 0.
$$

The solution set is every real number strictly less than $0$, or $(-\infty, 0)$ in interval notation. Test with $x = -3$: the original is $5(-3 + 2) = 5(-1) = -5$ on the left and $3(-3) + 10 = -9 + 10 = 1$ on the right. The inequality says $-5 < 1$, which is true. Test with $x = 4$: $5(6) = 30$ on the left and $3(4) + 10 = 22$ on the right. The inequality says $30 < 22$, which is false. Both tests match the solution set exactly.

## Common pitfalls

- **Forgetting to flip the symbol after dividing by a negative.** This is the signature mistake on inequalities and the reason $-4x \le 8$ becomes $x \ge -2$, not $x \le -2$. Every time you divide (or multiply) by a negative, pause and flip.
- **Flipping the symbol after adding or subtracting.** The flip rule only applies to multiplication and division by a negative. Adding or subtracting a negative number — for example, subtracting $7$ from both sides — does not change the direction of the symbol. "Subtracting a negative" is still subtraction, not multiplication.
- **Writing the solution as a number.** The solution to an equation is usually one number, but the solution to an inequality is usually an entire interval. Writing "$x = 6$" when the answer is "$x > 6$" is a common mix-up, especially after doing a lot of equation work.
- **Mishandling strict versus non-strict.** If the original says $\le$, the boundary point is part of the solution; if the original says $<$, it is not. Watch for this distinction when you reach your final answer.
- **Testing a boundary point.** When you want to sanity-check your solution set, use a test value from the **interior** of the set, not the boundary. A boundary point satisfies $\le$ but not $<$, and the distinction is easy to get wrong if you pick the endpoint.

## Problems Involving Solving Inequalities in One Variable

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_inequalities_in_one_variable"></div>

## See Also

- [[Solving_Multi_Step_Inequalities]]
- [[Compound_Inequalities]]
- [[Absolute_Value_Inequalities]]
- [[Inequalities_And_Their_Graphs]]
- [[Solving_Equations_In_One_Variable]]
- [[Systems_Of_Linear_Inequalities]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
