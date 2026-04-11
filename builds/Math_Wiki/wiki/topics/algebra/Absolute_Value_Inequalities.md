---
title: "Absolute Value Inequalities"
type: topic
aliases: ["Absolute-Value Inequality", "|x| < k Inequality", "|x| > k Inequality"]
tags: ["#branch-algebra-1", "#topic-inequalities", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "3", section: "3.5"}
related:
  - "topics/algebra/Absolute_Value_Equations"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Absolute_Value_Equations"
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
problem_type_ids: []
figures: []
summary: "|expr| < k is an AND compound inequality between -k and k; |expr| > k is an OR compound inequality outside -k and k."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Absolute Value Inequalities

# Absolute Value Inequalities

Absolute value measures **distance from zero** on a number line. So $|x|$ is how far $x$ sits from the origin, ignoring whether it is to the left or the right. That one idea is the whole key to absolute value inequalities — every problem in this lesson is really a statement about distance.

Suppose you are told that $|x| < 4$. In plain English: the distance from $x$ to zero is less than $4$. That means $x$ has to live strictly inside a band of width $8$ centered at the origin — anywhere from $-4$ up to $4$, but not at the endpoints. You just converted an absolute value inequality into a compound inequality:

$$
|x| < 4 \quad\longleftrightarrow\quad -4 < x < 4
$$

Now flip it. If $|x| > 4$, then $x$ is **more** than $4$ units from zero, so $x$ has to be far out to the left or far out to the right. There is no way for a single value to satisfy both halves, so this one is an "or":

$$
|x| > 4 \quad\longleftrightarrow\quad x < -4 \;\text{ or }\; x > 4
$$

That is the entire rulebook. "Less than" means between; "greater than" means outside.

---

## The two rules

For any expression and any positive constant $k$:

- **Less than (AND / between):**
$$
|\text{expr}| < k \iff -k < \text{expr} < k
$$
  The same rule works with $\leq$ — just carry the equality through on both sides.

- **Greater than (OR / outside):**
$$
|\text{expr}| > k \iff \text{expr} < -k \;\text{ or }\; \text{expr} > k
$$
  And again, $\geq$ works the same way.

In both cases, the first move is almost always to **isolate the absolute value on one side** of the inequality before doing anything else. Only after $|\text{expr}|$ stands alone do you drop the bars and write the compound inequality.

### Edge cases: when $k$ is zero or negative

Because $|\text{expr}|$ can never be negative, weird things happen when the right side is zero or below.

- $|\text{expr}| < -1$: the left side is always $\geq 0$, so it can never be less than a negative number. **No solution.**
- $|\text{expr}| \leq 0$: the only way absolute value lands at or below zero is if it equals zero exactly. Solve $\text{expr} = 0$ and you're done.
- $|\text{expr}| > -3$: absolute value is always $\geq 0$, which is always greater than $-3$. **All real numbers** work.
- $|\text{expr}| \geq 0$: absolute value is always $\geq 0$, so again **all real numbers** are solutions.

Check these edge cases before you try to crank through the compound inequality — they tell you the answer immediately.

---

## Example 1: a "less than" inequality (AND)

> Solve $|2x + 1| \leq 9$ and write the solution as a compound inequality.

The absolute value is already isolated on the left and the right side is positive, so rewrite as an "and" between $-9$ and $9$:

$$
-9 \leq 2x + 1 \leq 9
$$

Subtract $1$ from every part:

$$
-10 \leq 2x \leq 8
$$

Divide every part by $2$ (positive, so no signs flip):

$$
-5 \leq x \leq 4
$$

Every value of $x$ between $-5$ and $4$, endpoints included, makes the original inequality true. On a number line, draw closed dots at $-5$ and $4$ and shade the segment between them.

---

## Example 2: a "greater than" inequality requiring isolation (OR)

> Solve $3|x - 2| - 4 > 8$.

Two terms are sitting outside the absolute value bars, so isolate $|x - 2|$ first.

Add $4$ to both sides:

$$
3|x - 2| > 12
$$

Divide by $3$:

$$
|x - 2| > 4
$$

Now the form matches the "greater than" rule. Split into an "or":

$$
x - 2 < -4 \;\text{ or }\; x - 2 > 4
$$

Solve each half by adding $2$:

$$
x < -2 \;\text{ or }\; x > 6
$$

On a number line, put open circles at $-2$ and $6$ and shade the ray going left from $-2$ plus the ray going right from $6$. The middle band between $-2$ and $6$ is not part of the solution.

A common mistake here is to skip isolation and try $3(x - 2) - 4 > 8$. That answer would be wrong, because $|x - 2|$ is not the same as $x - 2$. Always peel the bars last, after everything else has been moved away.

---

## Example 3: edge cases with no solution or all real numbers

> Solve (a) $|x + 5| < -1$  and  (b) $|2x - 7| > -3$.

**(a)** The expression $|x + 5|$ represents a distance, and distances are never negative. There is no value of $x$ that can make $|x + 5|$ less than $-1$. The answer is **no solution** (the empty set $\varnothing$).

Don't bother setting up $-(-1) < x + 5 < -1$ — the shortcut rule explicitly requires the right-hand constant to be positive, and this one isn't. The problem dies on the first line.

**(b)** Flip the same trick: $|2x - 7|$ is always $\geq 0$, and $0$ is already larger than $-3$. Every real number satisfies this inequality, so the answer is **all real numbers** (often written $(-\infty, \infty)$ in interval notation).

Again, do not attempt the "or" split. It would produce two pieces that fail to describe the real situation, which is that *every* $x$ works.

---

## Common pitfalls

- **Skipping the isolation step.** You must get the absolute value alone — coefficient of $1$, nothing added or subtracted outside the bars — before you translate to a compound inequality.
- **Using AND when the sign is $>$ (or OR when the sign is $<$).** "Less than" equals "between two walls," so it's always an **and**. "Greater than" equals "past the walls on either side," so it's always an **or**. Mismatch these and the answer is guaranteed wrong.
- **Writing an "or" in compact three-part form.** The shortcut $-k < x < k$ only works for "and" inequalities. Something like "$x < -4 < 4 < x$" has no meaning.
- **Treating $|x| > \text{negative}$ as no solution.** It is the opposite — absolute value is always at least zero, which beats any negative number, so the answer is **all real numbers**.
- **Treating $|x| < \text{negative}$ as all real numbers.** Here the answer is **no solution**, because no distance can possibly be less than a negative amount.
- **Flipping signs only on one side.** When you multiply or divide by a negative, the inequality flips on **both** pieces of the compound form. Watch it.

---

## Prerequisites

Before you practice absolute value inequalities, make sure you are comfortable with:

- [[Absolute_Value_Equations]] — so the "two cases" idea feels familiar before you stretch it to inequalities
- [[Compound_Inequalities]] — because every absolute value inequality turns into an "and" or "or" compound inequality
- [[Solving_Multi_Step_Inequalities]] — for the sign-flip rule and the clean habits of isolating a variable

---

## Problems Involving Absolute Value Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="absolute_value_inequalities"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Absolute_Value_Equations]]
- [[Compound_Inequalities]]
- [[Inequalities_And_Their_Graphs]]
- [[Solving_Multi_Step_Inequalities]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
