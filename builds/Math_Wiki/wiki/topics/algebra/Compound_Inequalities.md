---
title: "Compound Inequalities"
type: topic
aliases: ["And Inequality", "Or Inequality", "Between Inequality"]
tags: ["#branch-algebra-1", "#topic-inequalities"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "3", section: "3.3"}
related:
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/algebra/Systems_Of_Linear_Inequalities"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
problem_type_ids: []
figures: []
summary: "Two inequalities joined by AND (both must hold) or OR (at least one must hold), solved together and graphed on a number line."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Compound Inequalities

# Compound Inequalities

Sometimes one inequality isn't enough to describe a situation. A thermostat might need the temperature to be at least $65^\circ$ **and** at most $72^\circ$. A safety rule might say a ride is off-limits for anyone under $48$ inches **or** over $76$ inches tall. Each of these describes a set of numbers with two conditions at once, which is exactly what a **compound inequality** is built for.

A compound inequality is made by gluing two ordinary inequalities together with the word **and** or the word **or**. Which word you use completely changes the shape of the answer.

---

## AND vs OR: the whole story

An **"and" compound inequality** (also called a *conjunction*) is satisfied only when **both** inequalities are true for the same value of $x$. Picture it as the overlap between two sets of numbers — the intersection.

An **"or" compound inequality** (a *disjunction*) is satisfied when **at least one** of the two inequalities is true. That is the union of two sets — if $x$ lives in either one, it counts.

A handy way to keep them straight: **AND shrinks, OR grows.** Adding an "and" usually narrows the answer (both rules must apply), while adding an "or" usually widens it (either rule is enough).

### The "between" shortcut

An "and" inequality like $x > -2$ and $x \leq 5$ can be written in a single compact line:

$$
-2 < x \leq 5
$$

Read that left-to-right as "negative two is less than $x$, which is less than or equal to five," or out loud as "$x$ is between $-2$ and $5$, not including $-2$ but including $5$." This compact form only makes sense for "and" inequalities — you **cannot** stack an "or" that way, because its solution has a gap in the middle.

### Graphing on a number line

- **AND** gives a single bounded segment between two points. Closed dots ($\bullet$) mark endpoints included by $\leq$ or $\geq$; open dots ($\circ$) mark endpoints excluded by $<$ or $>$.
- **OR** gives two rays pointing away from each other with empty space in between.

If the two conditions of an "and" don't overlap at all, there's **no solution** — no number can satisfy both at once.

---

## Example 1: solving an AND compound inequality

> Solve $-5 < 3x + 1 \leq 10$. Graph the solution and write it as a compound inequality.

The shortcut form means both $-5 < 3x + 1$ **and** $3x + 1 \leq 10$. You can solve them at the same time by treating the inequality as a three-part sandwich — whatever you do to the middle, do it to **both** outer pieces.

Subtract $1$ from all three parts:

$$
-5 - 1 < 3x + 1 - 1 \leq 10 - 1
$$

$$
-6 < 3x \leq 9
$$

Divide every part by $3$. Since $3$ is positive, no inequality signs flip:

$$
-2 < x \leq 3
$$

So the solution is every number strictly greater than $-2$ and less than or equal to $3$. On a number line, draw an open circle at $-2$, a closed circle at $3$, and shade the segment between them.

---

## Example 2: solving an OR compound inequality

> Solve $2x - 3 < -7$ or $4x + 1 \geq 13$. Graph the solution.

For an "or" inequality you can't use the three-part shortcut — the two conditions don't overlap around a single center, so solve each inequality on its own.

**First piece:**

$$
2x - 3 < -7
$$

$$
2x < -4
$$

$$
x < -2
$$

**Second piece:**

$$
4x + 1 \geq 13
$$

$$
4x \geq 12
$$

$$
x \geq 3
$$

Because the connector is "or," any value that satisfies **either** piece is in the solution. The final answer is:

$$
x < -2 \;\text{ or }\; x \geq 3
$$

Graph it as two rays shooting outward: an open circle at $-2$ with shading running left, plus a closed circle at $3$ with shading running right. The middle stretch between $-2$ and $3$ is **not** shaded because no number in there makes either piece true.

---

## Example 3: an AND inequality with no solution

> Solve $x > 6$ and $x < 1$.

Read this literally: you are looking for numbers that are larger than $6$ **and** smaller than $1$ at the same time. Nothing works. There is no number that lives to the right of $6$ while also sitting to the left of $1$ — the two regions don't touch.

The answer is **no solution**, sometimes written as the empty set $\varnothing$. On a number line, nothing gets shaded.

This is the flip side of the earlier warning: if an "and" forces two disjoint conditions, the intersection is empty. Check the overlap first, and you'll catch these cases before grinding through any arithmetic.

---

## Common pitfalls

- **Confusing AND with OR.** Always reread the connector before you graph. "And" produces a single piece (or nothing); "or" produces two rays (or sometimes the whole line).
- **Using the three-part shortcut on an OR.** Writing "$x < -2 < 3 \leq x$" is meaningless. Only "and" can collapse into the compact form.
- **Forgetting to flip the sign.** When you divide or multiply every part of the sandwich by a negative number, every inequality reverses direction — both in the middle and at the outer edges.
- **Dropping a part of the sandwich.** In a three-part inequality, every step has to touch all three pieces. If you subtract from the middle only, you've changed the problem.
- **Mistaking "no overlap" for a real answer.** If an "and" produces two disjoint conditions, the answer is "no solution," not just one of the pieces.
- **Open vs closed dots.** A strict inequality ($<$ or $>$) uses an open dot; $\leq$ or $\geq$ uses a closed dot. The dot style has to match the sign exactly.

---

## Prerequisites

Before you practice compound inequalities, make sure you are comfortable with:

- [[Inequalities_And_Their_Graphs]] — the basic vocabulary, symbols, and number-line pictures for one-variable inequalities
- [[Solving_Multi_Step_Inequalities]] — so you know the rules for isolating $x$, especially the sign-flip when dividing by a negative
- [[Integers_And_The_Number_Line]] — so "between," "left of," and "right of" line up automatically in your head

---

## Problems Involving Compound Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="compound_inequalities"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Inequalities_And_Their_Graphs]]
- [[Solving_Multi_Step_Inequalities]]
- [[Absolute_Value_Inequalities]]
- [[Systems_Of_Linear_Inequalities]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
