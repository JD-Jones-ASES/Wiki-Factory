---
title: "Piecewise Functions"
type: topic
aliases: []
tags: ["#branch-algebra-2", "#topic-functions", "#skill-procedural-calculation", "#skill-visualization", "#skill-multi-step", "#key-topic", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Notation"
  - "topics/algebra/Absolute_Value_Functions"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Inequalities_And_Their_Graphs"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Notation"
  - "topics/algebra/Inequalities_And_Their_Graphs"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: ["algebra/piecewise_step_graph.svg"]
summary: "A single function built by stitching together several sub-rules, each one active on its own slice of the domain."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Piecewise Functions

# Piecewise Functions

Most of the functions you meet in Algebra 2 — lines, parabolas, exponentials, absolute values — are each governed by a single formula that works everywhere on the real line. A **piecewise function** breaks that rule on purpose. Instead of one formula doing all the work, the function carries around a short list of rules, and which rule applies depends on where your input sits. You pick the right rule first, then evaluate.

Think of a cellphone plan that charges a flat fee for the first 2 GB of data, then a fixed price per gigabyte between 2 GB and 10 GB, and a different rate once you pass 10 GB. The total cost is a single function of the gigabytes you used, but three completely different formulas cover the three zones. Piecewise notation is the language that lets you pack all three into one tidy rule.

![[piecewise_step_graph.svg|A piecewise function with a constant piece, a linear piece, and a step drop]]

Once you can read the notation, the skill is cleanly procedural: match the input to the correct branch, run that branch's formula on it, and read off the output. The graphs, however, are where things get visually interesting — piecewise graphs can jump, corner, flatten, or split, and a single picture may contain several disconnected pieces.

---

## What it means

The general shape of a piecewise rule looks like this:

$$
f(x) = \begin{cases} \text{formula 1} & \text{when } x \text{ is in region 1}, \\ \text{formula 2} & \text{when } x \text{ is in region 2}, \\ \text{formula 3} & \text{when } x \text{ is in region 3}. \end{cases}
$$

Each row of the brace tells a short story. The left side of a row is the formula that does the computing; the right side is the condition — an inequality or interval — that decides whether the formula applies. The conditions must cover every input in the domain and must never overlap, so that every $x$ lands in exactly one branch.

You already know at least one piecewise function without realizing it. The absolute value rule

$$
|x| = \begin{cases} x & \text{when } x \geq 0, \\ -x & \text{when } x < 0, \end{cases}
$$

is piecewise: one branch for nonnegative inputs, another for negative ones. See [[Absolute_Value_Functions]] for the full treatment. That V-shaped graph is really two linear pieces glued together at the origin — the cleanest possible piecewise example.

---

## How it works: evaluating at a point

Evaluating $f(a)$ for a piecewise function always follows the same two-step routine.

1. **Check the conditions in order and find the one that $a$ satisfies.** Only one of them will be true; that is the branch you are on.
2. **Plug $a$ into that branch's formula and simplify.** You do not look at the other rows.

The whole game is making sure you match the input to the correct region. Students who rush here will sometimes plug a value into every branch and try to pick a "best answer" — that is not how the notation works. Each input belongs to exactly one branch, and the formula in any other branch has nothing to say about it.

### Handling boundary points

The edges between branches deserve extra care. When a rule says "when $x \leq 3$", the boundary value $x = 3$ belongs to that branch (because of the $\leq$). If instead it says "when $x < 3$", then $x = 3$ does **not** belong to that branch — you need to find the next row where the condition includes $3$. A valid piecewise definition makes sure every real number in the domain lands in exactly one branch, so one boundary is always closed (uses $\leq$ or $\geq$) and the other is open (uses $<$ or $>$). Watching the inequalities carefully is what stops boundary-point errors.

---

## Graphing a piecewise function

To draw the graph of a piecewise function, graph each branch only over its own region, and then glue the pieces together.

- **Sketch each branch's formula as if it applied everywhere**, lightly, so you can see the full line or curve.
- **Erase the parts outside that branch's region.** Only the portion of the graph over the assigned interval survives.
- **Mark the endpoints.** Use a **filled dot** at an endpoint where the branch's formula actually produces a value there (the condition uses $\leq$ or $\geq$), and use an **open dot** when it does not (the condition uses $<$ or $>$).

This is where the visually interesting behavior lives. A piecewise graph can have a **jump discontinuity** (the two branches meet at different heights at a boundary, and you see an empty gap between an open and a filled dot stacked on the same vertical line). It can have a **corner** where two branches meet at the same height but with different slopes — exactly like the tip of an absolute value V. Or the pieces may not meet at all, leaving a genuine break between segments. In every case, the open/filled dot at each boundary is the visual record of which branch "wins" at that input.

### Step functions

Some piecewise functions use **constant** branches — each formula is just a number, not a formula that depends on $x$. These are called **step functions**, because the graph looks like a staircase. Parking meters, shipping rates, and postage charges are the most familiar real-world examples. Each step is a flat horizontal segment at one height, and the graph hops from one step to the next at each boundary. Step functions are piecewise functions in their simplest possible form.

---

## Why it works

There is nothing magical going on here. A piecewise definition is a shortcut for saying "if the input looks like this, run formula A; otherwise, run formula B". Any time you wrote an `if`/`else` decision in a word problem, you were doing piecewise reasoning without the notation. The brace simply packs the list into a single typographic object so you can call the whole thing $f$, refer to its graph, and apply all the usual function-machinery (domain, range, composition from [[Function_Arithmetic_And_Composition]], and so on).

Piecewise functions also matter because real-world quantities genuinely behave this way. Tax brackets, overtime pay, tiered pricing, grade cutoffs, and any rule with a "threshold" baked into it are all pieced together from several regions with different formulas. Learning to read the brace is learning to translate between English rules and math.

---

## Worked examples

**Example 1.** Determine $f(-4)$, $f(0)$, $f(1)$, and $f(5)$ for the function

$$
f(x) = \begin{cases} x^2 + 1 & \text{when } x < 0, \\ 3 & \text{when } 0 \leq x \leq 2, \\ 2x - 1 & \text{when } x > 2. \end{cases}
$$

For each input, walk down the list and find the first row whose condition is true.

- For $x = -4$: the condition $x < 0$ is true, so use the top branch. $f(-4) = (-4)^2 + 1 = 16 + 1 = 17$.
- For $x = 0$: the top branch requires $x < 0$, which fails (zero is not less than zero). The middle branch requires $0 \leq x \leq 2$, which holds. So $f(0) = 3$.
- For $x = 1$: the middle branch still applies, and it is constant on its whole region, so $f(1) = 3$.
- For $x = 5$: the top two branches both fail. The bottom branch requires $x > 2$, which holds. So $f(5) = 2(5) - 1 = 9$.

The answers are $f(-4) = 17$, $f(0) = 3$, $f(1) = 3$, and $f(5) = 9$. Notice how the middle branch produced the same output for two very different inputs — that is what a constant branch does, and it is perfectly legal.

**Example 2.** Maya runs a small-batch nut-butter operation. Her supplier charges a flat \$18 for any order up to 5 pounds of almonds, \$3 per pound for any order from 5 pounds up to and including 20 pounds, and \$2.50 per pound once an order exceeds 20 pounds (with no fixed fee in any of these zones). Write the total cost $C(p)$ as a piecewise function of the pounds ordered, and compute the cost of $3$-pound, $12$-pound, and $25$-pound orders.

Translate each zone of the verbal description into a row of the brace.

$$
C(p) = \begin{cases} 18 & \text{when } 0 < p \leq 5, \\ 3p & \text{when } 5 < p \leq 20, \\ 2.50p & \text{when } p > 20. \end{cases}
$$

Evaluate at each requested weight.

- For $p = 3$: $0 < 3 \leq 5$, so the flat fee applies: $C(3) = \$18$.
- For $p = 12$: $5 < 12 \leq 20$, so $C(12) = 3(12) = \$36$.
- For $p = 25$: $p > 20$, so $C(25) = 2.50(25) = \$62.50$.

A sanity check at a boundary: at $p = 5$, the flat-fee branch is the one that applies (because the $\leq$ sits on the top branch), and $C(5) = \$18$. If Maya ordered just a hair more — say $p = 5.01$ — the middle branch kicks in and the cost jumps to about $\$15.03$. So ordering exactly $5$ pounds is temporarily more expensive than ordering $5.01$ pounds, a quirk of her supplier's pricing.

**Example 3.** Give the domain and range of

$$
g(x) = \begin{cases} -x - 1 & \text{when } -5 \leq x < -1, \\ x + 1 & \text{when } -1 \leq x \leq 3. \end{cases}
$$

**Domain.** The two branches together cover $-5 \leq x \leq 3$, with no overlap. The point $x = -1$ lives in the second branch. So the domain is $[-5, 3]$.

**Range.** Analyze each branch separately.

- The top branch is $y = -x - 1$ on $-5 \leq x < -1$. It is a line with slope $-1$. At $x = -5$, $y = -(-5) - 1 = 4$. As $x$ approaches $-1$ from the left, $y$ approaches $-(-1) - 1 = 0$ but does not quite reach it (because the condition is $x < -1$). So this branch produces outputs in the range $(0, 4]$.
- The bottom branch is $y = x + 1$ on $-1 \leq x \leq 3$. At $x = -1$, $y = 0$. At $x = 3$, $y = 4$. So this branch produces outputs in $[0, 4]$.

Taking the union, every output from $0$ up through $4$ is achievable. The point $y = 0$ is produced by the bottom branch (so it is covered even though the top branch misses it). The range is $[0, 4]$.

A quick structural observation: the two branches meet at $(−1, 0)$ — the top branch approaches that point from above-left while the bottom branch actually sits at it — so the graph has no gap there, only a corner.

---

## Common pitfalls

- Plugging an input into the wrong branch because you misread the inequality on its condition. Always verify that the chosen branch's condition is actually satisfied before you compute.
- Treating a strict inequality ($<$) and a non-strict one ($\leq$) as if they meant the same thing. They differ at exactly one point — the boundary — and that point can change which branch you use.
- Drawing a graph that is filled (or hollow) at both ends of a boundary. At any seam, exactly one of the two dots should be filled and the other should be open, unless the two formulas happen to agree at that boundary.
- Forgetting that the domain is the union of the condition regions. If a row's condition says $1 < x < 4$, the values $x = 1$ and $x = 4$ are not part of that row's piece — and they are only in the domain at all if some other row claims them.
- Assuming the graph has to be connected. A piecewise graph can have genuine gaps between its pieces, especially when two branches produce different outputs at a shared boundary.
- Using the constant branch's number as the input to some other branch. If one branch is just the rule $f(x) = 3$, then on its region the output is $3$ no matter what $x$ is — do not multiply that $3$ by $x$ or confuse it with an input.

---

## Problems Involving Piecewise Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="piecewise_functions"></div>

## See Also

- [[Absolute_Value_Functions]] — the most familiar piecewise function, built from two linear branches
- [[Function_Notation]] — the input-output grammar that piecewise rules extend
- [[Function_Basics]] — domain, range, and the one-output-per-input principle
- [[Linear_Functions]] — each branch of a typical piecewise graph is a line, so the slope and intercept tools transfer directly
- [[Inequalities_And_Their_Graphs]] — for reading the conditions that decide which branch applies
- [[Relations_And_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
