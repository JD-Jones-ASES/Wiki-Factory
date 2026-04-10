---
title: "Inequalities and Their Graphs"
type: topic
aliases: ["Inequality Graphs", "Graphing Inequalities on a Number Line"]
tags: ["#branch-algebra-1", "#topic-inequalities"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "3", section: "3.1"}
related:
  - "topics/pre_algebra/Writing_And_Graphing_Inequalities"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/algebra/Systems_Of_Linear_Inequalities"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Rational_Numbers_On_The_Number_Line"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "Comparing expressions with <, >, \u2264, \u2265 and picturing the infinite set of solutions on a number line."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Inequalities and Their Graphs

# Inequalities and Their Graphs

An **inequality** is what you write when two expressions are not required to be equal — one of them may be smaller, or larger, or equal at most. Where an equation like $x = 5$ picks out exactly one number, an inequality like $x > 5$ picks out a whole stretch of the number line at once. Learning to read, write, and draw that stretch is the first step of the inequality chapter.

The four symbols you will use look like this:

$$
<\ \text{(less than)},\qquad >\ \text{(greater than)}
$$

$$
\leq\ \text{(less than or equal to)},\qquad \geq\ \text{(greater than or equal to)}
$$

---

## Reading an inequality

Every inequality is a sentence. Read it left to right and say the symbol out loud. The statement $x < 7$ says "$x$ is a number smaller than $7$" — so $6$, $0$, and $-14$ all count, but $7$ itself does not. The statement $y \geq -2$ says "$y$ is at least $-2$" — the value $-2$ is allowed, and so is any number to its right.

Any number that makes the sentence true is called a **solution**. The full collection of solutions is the **solution set**. Unlike the solution of a simple equation, which is usually a single value, the solution set of an inequality is usually infinite. That is why a picture — a number-line graph — is the natural way to display it.

## Strict vs. inclusive: open and closed circles

Graphs of inequalities have a tiny but very important convention that separates strict comparisons from inclusive ones:

- A **strict** inequality ($<$ or $>$) uses an **open circle** at the endpoint. The endpoint is *not* a solution, so we leave the circle hollow to show "not included."
- An **inclusive** inequality ($\leq$ or $\geq$) uses a **closed circle** at the endpoint. The endpoint *is* a solution, so we fill the circle in.

After drawing the circle, shade the portion of the number line that contains every other solution — right for "greater," left for "less." The shaded ray runs off toward infinity, and an arrow on the end of the line reminds you the solutions never stop.

The circle decision is the single most common place students lose points on this topic. Whenever you draw a graph, ask yourself: "Could the endpoint itself be the answer?" If yes, fill the circle. If no, leave it hollow.

---

## Example 1: graphing a strict inequality

> Graph $x > -1$ on a number line.

The symbol is a plain "greater than," with no equal-to bar underneath, so $-1$ itself is **not** a solution. Place an **open** circle at $-1$. Because we want numbers bigger than $-1$, shade the portion of the line that runs from $-1$ toward the right, and add an arrow on the far end.

$$
\underset{-4\ -3\ -2\ -1\ \ \ 0\ \ \ 1\ \ \ 2\ \ \ 3\ \ \ 4}{\longleftarrow\!\circ\!\rule[0.5ex]{3cm}{0.5pt}\!\longrightarrow}
$$

Every number to the right of that hollow dot — say $0$, $1.5$, $42$ — makes the sentence $x > -1$ true. Every number to the left of the dot, and the dot itself, does not.

---

## Example 2: graphing an inclusive inequality

> Graph $x \leq 3$ on a number line.

This time the inequality is "less than *or equal to*," so $3$ itself counts as a solution. Draw a **closed** (filled-in) circle at $3$, and shade everything to the **left** of it toward negative infinity.

You can sanity-check quickly by plugging in a sample value. Try $x = 3$: the sentence reads $3 \leq 3$, which is true because equality is allowed. Try $x = 0$: $0 \leq 3$ is also true. Try $x = 8$: $8 \leq 3$ is false, which is correct — $8$ sits in the unshaded region.

---

## Example 3: writing an inequality from a graph

> A number line shows a filled circle at $6$ and shading that extends to the right, with an arrow heading toward positive infinity. Which inequality does this graph represent?

Read the two visual clues in order:

1. The circle at $6$ is **closed**, so $6$ is included. The symbol will carry the bar — either $\leq$ or $\geq$.
2. The shading runs to the **right**, toward bigger numbers. So the variable is at least $6$ — the symbol is $\geq$.

Putting those together gives $x \geq 6$. As a quick check, both $6$ and $9$ should make the sentence true ($6 \geq 6$ is true because of the equals case; $9 \geq 6$ is true outright), and both sit inside the shaded region. A value outside the shading, like $2$, gives $2 \geq 6$, which is false. The graph and the inequality agree.

---

## Checking whether a value is a solution

A common question is: "Is $x = 4$ a solution of $2x - 1 \geq 7$?" Substitute and simplify the left side: $2(4) - 1 = 7$. The sentence becomes $7 \geq 7$, and because the $\geq$ symbol allows equality, this is true. So yes, $4$ is a solution.

Try $x = 3$ in the same inequality: $2(3) - 1 = 5$, which gives $5 \geq 7$ — false. So $3$ is not a solution. The set of all valid values is therefore "everything from $4$ onward," which you would graph with a closed circle at $4$ and shading to the right.

---

## Common pitfalls

- **Choosing the wrong circle.** If the inequality has a bar under it ($\leq$ or $\geq$), the endpoint belongs to the solution set and the circle is filled. A plain $<$ or $>$ uses a hollow circle. Whenever the graph is wrong, check this first.
- **Shading the wrong direction.** "Greater than" always shades toward the larger numbers (the right), and "less than" shades toward the smaller numbers (the left). Be careful with negatives: $x > -5$ still shades *right*, even though $-5$ is negative.
- **Confusing an inequality with an equation.** $x = 7$ picks out a single point. $x \geq 7$ picks out $7$ together with every number above it. Keep in mind that inequalities almost always describe a whole range of answers, not a single value.
- **Flipping the sentence.** The expression "$5 < x$" is the same as "$x > 5$." Reading it as "$x < 5$" is a common slip. When you see the variable on the right, rewrite the sentence so the variable comes first and then pick the symbol.

---

## Prerequisites

Before tackling practice on this topic, make sure you are comfortable with:

- [[Integers_And_The_Number_Line]] — positive and negative numbers, and how they are ordered left to right
- [[Rational_Numbers_On_The_Number_Line]] — placing fractions and decimals between the whole number tick marks
- [[Variables_And_Algebraic_Expressions]] — so that $2x - 1$ and similar expressions feel routine

If any of those is shaky, start there, then come back.

---

## Problems Involving Inequalities and Their Graphs

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="inequalities_and_their_graphs"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Writing_And_Graphing_Inequalities]]
- [[Solving_Multi_Step_Inequalities]]
- [[Compound_Inequalities]]
- [[Absolute_Value_Inequalities]]
- [[Systems_Of_Linear_Inequalities]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
