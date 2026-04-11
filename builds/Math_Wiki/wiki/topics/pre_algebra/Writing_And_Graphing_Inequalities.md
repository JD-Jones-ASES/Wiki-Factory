---
title: "Writing and Graphing Inequalities"
type: topic
aliases: ["Inequality Symbols", "Number Line Inequalities"]
tags: ["#branch-pre-algebra", "#topic-inequalities", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "5", section: "5.1"}
related:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Solving_One_Step_And_Two_Step_Inequalities"
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Solving_Multi_Step_Inequalities"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: ["algebra/inequality_number_line.svg"]
summary: "Turn everyday phrases like 'at least' and 'no more than' into inequality symbols and picture the answers on a number line."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Writing and Graphing Inequalities

# Writing and Graphing Inequalities

An **equation** pins a variable down to a single number: $x = 7$ says there is exactly one right answer. An **inequality** is looser. It describes a whole range of values that make a sentence true — everything bigger than some number, everything at or below some cutoff, everything between two points. Real life is full of these: a speed limit, a minimum age, a budget, a score you need to pass. Inequalities are how algebra talks about those situations.

![[inequality_number_line.svg|Four inequalities graphed on number lines]]

The four symbols you need are:

$$
\begin{aligned}
&x < 7 && \text{"$x$ is less than $7$"} \\
&x > 7 && \text{"$x$ is greater than $7$"} \\
&x \leq 7 && \text{"$x$ is less than or equal to $7$"} \\
&x \geq 7 && \text{"$x$ is greater than or equal to $7$"}
\end{aligned}
$$

The two with the little line underneath ($\leq$ and $\geq$) include the boundary value. The two without the line ($<$ and $>$) are called **strict** — they leave the boundary out.

---

## Translating English into symbols

Most inequality problems begin with a sentence in ordinary English, and the trick is hearing which direction the symbol should point and whether the boundary itself is allowed. A short cheat sheet of phrases shows up over and over:

| What the sentence says | Which symbol |
|---|---|
| is fewer than, is less than | $<$ |
| is more than, is greater than | $>$ |
| is at most, is no more than, cannot exceed | $\leq$ |
| is at least, is no less than, must be | $\geq$ |

A good habit: underline the comparison words in the sentence before writing any math. If the phrase is "at most $50$," the boundary of $50$ is still allowed, so you want $\leq$. If the phrase is "more than $50$," the number $50$ itself is not a legal answer, so you need strict $>$.

One mental model that helps: the inequality symbol always points at the smaller value. In $x < 9$, the narrow end points at $x$, saying $x$ is the smaller of the two.

---

## Graphing on a number line

Every inequality in one variable has a picture, and the picture lives on a number line. There are only two things to decide:

1. **Does the boundary value count?** If yes, mark it with a filled-in (closed) circle. If no, use an empty (open) circle.
2. **Which direction are the legal answers?** Shade the ray toward larger numbers for "greater than" and toward smaller numbers for "less than."

A filled circle says "this point is part of the answer." An open circle says "get arbitrarily close to this point, but don't actually land on it." The shading then carries the solution off toward infinity in the correct direction.

One warning that catches a lot of beginners: the direction of the shading has nothing to do with which way the symbol "points" when you write it. Read the symbol's meaning ("greater than" or "less than $x$") and then shade the side of the number line that matches.

---

## Example 1: turning English into an inequality

> Write each sentence as an inequality. Let $n$ stand for the unknown number.
> (a) A number is at least $25$.
> (b) The cost is no more than $\$12$.
> (c) The score is greater than $80$.
> (d) The age is less than $18$.

Read each phrase and match it to a symbol.

(a) "At least $25$" means the number can be $25$ itself or anything higher, so use $\geq$:

$$
n \geq 25
$$

(b) "No more than $\$12$" caps the cost at $12$, including exactly $12$, so use $\leq$:

$$
n \leq 12
$$

(c) "Greater than $80$" leaves $80$ out of the answer — strict $>$:

$$
n > 80
$$

(d) "Less than $18$" also excludes the boundary — strict $<$:

$$
n < 18
$$

Notice how "at least" and "no more than" both use the line-underneath symbols, while "greater than" and "less than" do not. The difference is whether the boundary value itself counts.

---

## Example 2: graphing an inequality on a number line

> Graph $x \geq -1$ on a number line.

The symbol is $\geq$, so the boundary $-1$ **is** part of the solution. That means a closed circle at $-1$. "Greater than or equal to" means shade toward larger values, which is to the right:

```
    closed circle at -1, heavy shading to the right
<---|----|----|----●====|====|====|====|---->
   -4   -3   -2   -1    0    1    2    3
```

Every point on the shaded ray — including $-1$ exactly — is a valid answer. Pick any value from that region, substitute it back into $x \geq -1$, and the inequality is satisfied.

---

## Example 3: strict inequality and reading a graph

> Graph $x < 2$ on a number line, then describe in English which numbers are solutions.

Since the symbol is strict ($<$), the value $2$ itself does **not** count. Draw an open circle at $2$ and shade the entire ray heading left, toward the smaller numbers:

```
    open circle at 2, heavy shading to the left
<====|====|====|====|====○----|----|----|---->
    -3   -2   -1    0    1    2    3    4
```

In words: $x$ is any real number strictly smaller than $2$. So $1.99$ is in; $0$, $-5$, and $-100$ are all in; but $2$ is not, and neither is $2.0001$. The open circle is the visual way of saying "close but no cigar."

You can also go the other direction. Given a number line with a closed circle at $4$ and shading that runs to the left, the matching inequality is $x \leq 4$: the solid circle signals $\leq$ (not strict) and the leftward shading signals "less than or equal."

---

## Common pitfalls

- **Mistaking "at most" for "less than."** "At most $50$" means the answer can be exactly $50$, so the symbol must be $\leq$. Only phrases like "fewer than" or "less than" cut the boundary off with strict $<$.
- **Using the wrong circle.** Open circle for strict ($<$ or $>$), closed circle for inclusive ($\leq$ or $\geq$). If you cannot remember which is which, think: a line under the symbol means the endpoint is included, and "included" means the circle is filled in.
- **Shading the wrong direction.** Do not rely on which way the symbol "looks." Translate the symbol into words — "$x$ is greater than..." — and then shade toward the larger numbers.
- **Forgetting the variable has a real-world floor.** A speed $s$ on a highway satisfies $s \leq 65$, but also $s \geq 0$, because speeds are not negative. In word problems, watch for hidden constraints that the algebra alone does not show.

---

## Prerequisites

Before tackling practice problems, make sure you are solid on:

- [[Integers_And_The_Number_Line]] — reading positions, directions, and the meaning of "greater than" on a number line
- [[Variables_And_Algebraic_Expressions]] — comfortable using a letter to stand for an unknown number
- [[Order_Of_Operations]] — so that when an expression sits next to an inequality symbol, you know what it evaluates to

---

## Problems Involving Writing and Graphing Inequalities

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="writing_and_graphing_inequalities"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Solving_One_Step_And_Two_Step_Inequalities]]
- [[Inequalities_And_Their_Graphs]]
- [[Solving_Multi_Step_Inequalities]]
- [[Integers_And_The_Number_Line]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
