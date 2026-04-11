---
title: "Arithmetic Sequences and Linear Patterns"
type: topic
aliases: ["Arithmetic Sequence", "Common Difference"]
tags: ["#branch-pre-algebra", "#topic-sequences-and-series", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "9", section: "9.3"}
related:
  - "topics/algebra/Sequences"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Slope"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "A sequence whose terms climb or fall by the same fixed amount every step — and a linear function in disguise."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Arithmetic Sequences and Linear Patterns

# Arithmetic Sequences and Linear Patterns

A **sequence** is nothing more than a list of numbers written down in a specific order. You already meet sequences all the time, even if you do not call them that: the odd numbers $1, 3, 5, 7, \ldots$, the positive multiples of four $4, 8, 12, 16, \ldots$, the powers of two $2, 4, 8, 16, \ldots$. Each number in a sequence is called a **term**, and mathematicians number them with subscripts so they can talk about any one specifically. The first term is $a_1$, the second is $a_2$, the tenth is $a_{10}$, and the general "$n$th term" is written $a_n$.

An **arithmetic sequence** is the simplest well-behaved sequence in the whole subject: each term sits the same fixed distance away from the one before it. That fixed distance is called the **common difference** and is written $d$. In a formula,

$$
d = a_{n+1} - a_n,
$$

and because $d$ must be the same no matter which two consecutive terms you pick, you can spot an arithmetic sequence by doing a quick difference check: subtract each term from the one right after it and see whether all the answers agree.

---

## The explicit formula

If the first term of an arithmetic sequence is $a_1$ and the common difference is $d$, then you can climb up to any later term by adding $d$ over and over. From $a_1$ to $a_2$ is one step of $d$; from $a_1$ to $a_3$ is two steps; from $a_1$ to $a_n$ is exactly $n - 1$ steps. That reasoning gives the single most important formula on this page:

$$
a_n = a_1 + (n - 1)d.
$$

This is called the **explicit formula** because it hands you any term you want without forcing you to walk through every earlier term. You do not need to know $a_{49}$ to compute $a_{50}$ — you plug $n = 50$ into the formula and out comes the answer in one line.

A handy way to remember the formula: the subscript $n$ tells you which term you want, and you always take **one fewer** jump of size $d$ than the term number. Miss that "minus one" and you are off by exactly one copy of $d$, which is the most common slip in this whole topic.

---

## Connection to linear functions

Here is the punchline that gives the page its title. Every arithmetic sequence is really a **linear function** hiding inside sequence notation. Watch what happens when you expand the explicit formula:

$$
a_n = a_1 + (n - 1)d = dn + (a_1 - d).
$$

Compare that with the familiar line $y = mx + b$. The role of the slope $m$ is played by $d$, and the role of the y-intercept $b$ is played by $a_1 - d$. If you were to plot the points $(1, a_1), (2, a_2), (3, a_3), \ldots$ on a coordinate plane, they would land perfectly on a straight line whose slope equals the common difference.

The only real difference between an arithmetic sequence and a [[Linear_Functions|linear function]] is the **input set**. A linear function takes any real number — fractions, decimals, negatives, all of it. A sequence is only allowed to receive the term numbers $1, 2, 3, 4, \ldots$ as inputs. So a sequence is a linear function whose domain has been trimmed down to the positive whole numbers. Because arithmetic sequences grow at a steady rate, their graphs are straight-line dot patterns — the picture you get when you sample a line at evenly spaced integer inputs.

---

## Example 1: identifying an arithmetic sequence

> For each list, decide whether it is arithmetic. If it is, state the common difference and write the next three terms.
>
> (a) $6, 10, 14, 18, 22, \ldots$
> (b) $1, 3, 9, 27, 81, \ldots$
> (c) $20, 13, 6, -1, -8, \ldots$

The test is the same every time: subtract each term from the next and see whether the answers match.

For (a): $10 - 6 = 4$, $14 - 10 = 4$, $18 - 14 = 4$, $22 - 18 = 4$. All the differences equal $4$, so this sequence **is arithmetic** with $d = 4$. The next three terms are $22 + 4 = 26$, $26 + 4 = 30$, and $30 + 4 = 34$.

For (b): $3 - 1 = 2$, $9 - 3 = 6$, $27 - 9 = 18$. The differences are growing, not staying put, so this sequence is **not arithmetic**. (It is actually a geometric sequence with common ratio $3$, a topic you will meet in [[Sequences]].)

For (c): $13 - 20 = -7$, $6 - 13 = -7$, $-1 - 6 = -7$, $-8 - (-1) = -7$. All four differences agree, so this sequence **is arithmetic** with $d = -7$. A negative $d$ simply means the terms are going down instead of up. The next three terms are $-8 - 7 = -15$, $-15 - 7 = -22$, and $-22 - 7 = -29$.

---

## Example 2: using the explicit formula

> An arithmetic sequence has $a_1 = 4$ and $d = 6$. Write an explicit formula for $a_n$ and use it to compute $a_{25}$.

Drop the values straight into $a_n = a_1 + (n - 1)d$:

$$
a_n = 4 + (n - 1)(6).
$$

You could stop here, but it is usually more useful to simplify until the formula looks like a linear rule. Distribute the $6$:

$$
a_n = 4 + 6n - 6 = 6n - 2.
$$

Now the connection to linear functions is staring right at you: slope $6$, "y-intercept" $-2$. To find the twenty-fifth term, plug in $n = 25$:

$$
a_{25} = 6(25) - 2 = 150 - 2 = 148.
$$

Sanity check: starting from $a_1 = 4$ and adding the common difference $24$ times should also give $4 + 24 \cdot 6 = 4 + 144 = 148$. Both paths agree, and the answer is $a_{25} = 148$.

---

## Example 3: working backward from two terms

> The first four terms of an arithmetic sequence are $30, 26, 22, 18, \ldots$. Build the explicit formula and determine the first term in the sequence that is negative.

Start with the quick diagnostic. The differences are $26 - 30 = -4$, $22 - 26 = -4$, and $18 - 22 = -4$. The sequence is arithmetic with $a_1 = 30$ and $d = -4$.

Now build the explicit formula:

$$
a_n = 30 + (n - 1)(-4) = 30 - 4n + 4 = 34 - 4n.
$$

To pin down the first negative term, you want the smallest whole-number value of $n$ for which $a_n$ drops below zero. Solve the inequality

$$
34 - 4n < 0
$$

by adding $4n$ to both sides and then dividing:

$$
34 < 4n \quad\Longrightarrow\quad n > 8.5.
$$

The smallest positive integer larger than $8.5$ is $n = 9$. Check: $a_9 = 34 - 4(9) = 34 - 36 = -2$, while $a_8 = 34 - 32 = 2$ is still positive. So the ninth term is where the sequence first dips below zero, and its value is $-2$.

Notice how fast this is compared to climbing term by term. That speed is exactly why the explicit formula is worth memorizing.

---

## Real-world sense: the savings-account picture

Arithmetic sequences describe any situation where the same amount is added (or taken away) at each step. Imagine a savings jar that already has \$200 in it, and every Friday you drop in another \$25. The balance after $n$ Fridays is

$$
B_n = 200 + 25n,
$$

which is the same shape as the explicit formula, just with different labels. Six months of deposits ($n = 26$) gives $B_{26} = 200 + 25(26) = 200 + 650 = 850$ dollars. Sitting in a theater where each row has two more seats than the one in front, or watching a sidewalk vendor add the same number of hats to her stack each hour — these are all arithmetic-sequence problems in disguise. Whenever a quantity grows or shrinks by the same amount each step, reach for $a_n = a_1 + (n - 1)d$.

---

## Common pitfalls

- **Off-by-one on the exponent of $d$.** The formula is $a_1 + (n - 1)d$, not $a_1 + nd$. The $-1$ is there because you only take $n - 1$ jumps to go from the first term to the $n$th.
- **Confusing "term number" with "term value."** In $a_{10} = 32$, the $10$ is the *position* (the tenth slot), while $32$ is the *value* that sits in that slot. They are two different things — the formula turns one into the other.
- **Skipping the constant-difference check.** Seeing two equal differences is not enough. Some non-arithmetic sequences fool you for the first gap or two, so always confirm with at least three successive differences before committing.
- **Losing the sign of $d$.** A sequence that decreases has a negative common difference. Compute $d$ as "next term minus current term," not the other way around, or you will end up with the wrong sign.

---

## Prerequisites

Before you jump into practice, make sure you are comfortable with:

- [[Order_Of_Operations]] — so the formula $a_1 + (n - 1)d$ is evaluated in the right order
- [[Multiplying_And_Dividing_Integers]] — so negative common differences do not trip you up
- [[Variables_And_Algebraic_Expressions]] — so the subscript notation $a_n$ feels like second nature

---

## Problems Involving Arithmetic Sequences and Linear Patterns

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="arithmetic_sequences_and_linear_patterns"></div>

---

## See Also

- [[Sequences]] — the fuller algebra-2 treatment with geometric sequences and sum formulas
- [[Linear_Functions]] — the continuous cousin of an arithmetic sequence
- [[Slope]] — the common difference plays the role of slope in the sequence-as-line picture
- [[Summation]] — writing and evaluating sums of sequences in sigma notation
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
