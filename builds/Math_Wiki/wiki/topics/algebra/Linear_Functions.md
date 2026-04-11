---
title: "Linear Functions"
type: topic
aliases: ["LinearFunctions", "Linear Function"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-linear"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "2", section: "2.3"}
  - {book: "algtrig", chapter: "2", section: "2.3"}
related:
  - "topics/algebra/Slope"
  - "topics/algebra/Slope_Intercept_Form"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Modeling_With_Linear_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Parallel_And_Perpendicular_Lines"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Slope"
  - "topics/algebra/Slope_Intercept_Form"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: []
summary: "A function of the form f(x) = mx + b: one input goes in, a straight-line output comes out."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Linear Functions

# Linear Functions

A **function** is a machine. You feed it one input, and it hands you back exactly one output. Every input has a partner; no input is ever sent to two different places. A **linear function** is the simplest interesting machine of all — the output is always the input times some number, with a fixed amount added on top.

In symbols, a linear function looks like this:

$$
f(x) = mx + b
$$

The letter $m$ is the **slope** and $b$ is the **y-intercept**, exactly the same two numbers you already know from [[Slope_Intercept_Form|slope-intercept form]]. The difference is a new name — $f(x)$ instead of $y$ — and a new way of talking about it.

---

## Function notation: what "f of x" means

The expression $f(x)$ is pronounced **"f of x"**, and it is the single most useful piece of notation in the whole course. It does not mean "f times x." It means "the output that the function named $f$ produces when its input is $x$."

Think of $f$ as the name of the machine. Whatever you put inside the parentheses is the input; whatever sits on the other side of the equals sign is the recipe for building the output. So if someone writes

$$
f(x) = 3x - 4,
$$

they are telling you: "to evaluate this machine, multiply your input by three and then subtract four." The letter $x$ is just a stand-in for whatever number you want to feed in. You could put $5$ in its place, or $-2$, or even a whole expression like $a + 1$. In every case the recipe is the same.

A linear function requires $m \neq 0$. If $m$ is zero, the output never changes no matter what input you give it — that is called a **constant function**, and its graph is a horizontal line at height $b$.

### Domain and range

For every linear function with $m \neq 0$, you can feed in any real number at all and the machine will happily give you a real number back. That means the **domain** (the set of legal inputs) is all real numbers, written $(-\infty, \infty)$. The **range** (the set of possible outputs) is also all real numbers, because as $x$ sweeps across the whole number line, $mx + b$ does the same. The only exception is a constant function, whose range is the single value $\{b\}$.

---

## Independent and dependent variables

When you write $f(x) = mx + b$, the letter $x$ is called the **independent variable** because you are free to pick whatever value of $x$ you want. The output $f(x)$ is called the **dependent variable** because its value depends on the choice you made for $x$. On a graph, the independent variable lives on the horizontal axis and the dependent variable lives on the vertical axis. You pick a spot on the x-axis, and the function tells you how high to go.

---

## Reading a graph

The graph of $f(x) = mx + b$ is a straight line. The y-intercept $b$ is the single number $f(0)$ — the height of the line where it crosses the y-axis. The slope $m$ tells you how much the output climbs every time the input takes one step to the right. A positive slope tilts uphill; a negative slope tilts downhill; a slope of zero lies perfectly flat.

If someone hands you a graph of a linear function and asks, "what is $f(2)$?", you do not need the equation at all. You just slide your finger to $x = 2$, walk straight up (or down) until you hit the line, and read the height — that is $f(2)$.

---

## Example 1: evaluating a linear function

> Let $f(x) = -2x + 7$. Find $f(3)$, $f(0)$, and $f(-4)$.

Every evaluation follows the same pattern — copy the rule, replace every $x$ with the input, then simplify.

$$
f(3) = -2(3) + 7 = -6 + 7 = 1
$$

$$
f(0) = -2(0) + 7 = 0 + 7 = 7
$$

$$
f(-4) = -2(-4) + 7 = 8 + 7 = 15
$$

Notice that $f(0) = 7$. That is the y-intercept $b$, showing up exactly where it should: the number you get when the input is zero. Notice also that the signs in $f(-4)$ are worth a pause — the negative input combined with the negative slope gives a positive product. Slow down on signed arithmetic; this is where most small errors creep in.

---

## Example 2: writing a linear function from a slope and a point

> Write, in function notation, the linear function whose slope is $\tfrac{1}{2}$ and whose graph passes through the point $(4, 5)$.

The goal is to find the values of $m$ and $b$. We already know $m = \tfrac{1}{2}$, so we need the y-intercept.

Start from the general form and plug in the known slope:

$$
f(x) = \tfrac{1}{2}x + b
$$

The point $(4, 5)$ tells us that when the input is $4$, the output must be $5$. In function language, $f(4) = 5$. Substitute and solve for $b$:

$$
5 = \tfrac{1}{2}(4) + b
$$

$$
5 = 2 + b
$$

$$
b = 3
$$

So the function is:

$$
f(x) = \tfrac{1}{2}x + 3
$$

As a sanity check, plug in $x = 4$: $f(4) = \tfrac{1}{2}(4) + 3 = 2 + 3 = 5$. The point lands on the line, so the answer is correct.

---

## Example 3: reading values from a graph

> A linear function $g$ is graphed on a standard coordinate grid. The line passes through $(0, -1)$ and climbs through $(1, 2)$, $(2, 5)$, and $(3, 8)$. Describe the function in words, give $g(5)$, and find the input that produces an output of $-4$.

First, look at the y-intercept. The line crosses the y-axis at $(0, -1)$, so $b = -1$. Now walk from any point to the next: from $(0, -1)$ to $(1, 2)$, the output jumps up by $3$ when the input grows by $1$. That is the slope: $m = 3$. So

$$
g(x) = 3x - 1.
$$

In words: the function takes any input, triples it, and then takes one away.

For $g(5)$, evaluate: $g(5) = 3(5) - 1 = 15 - 1 = 14$.

For the other question — "what input produces an output of $-4$?" — set the rule equal to $-4$ and solve:

$$
3x - 1 = -4 \quad\Longrightarrow\quad 3x = -3 \quad\Longrightarrow\quad x = -1.
$$

So $g(-1) = -4$. Reading values off a graph and reading them off the equation are two views of the same object.

---

## A note on function arithmetic

Linear functions play nicely with one another. If $f(x) = 2x + 1$ and $g(x) = x - 3$, you can add them, subtract them, or multiply them the way you would combine any two expressions. Adding gives $(f + g)(x) = f(x) + g(x) = (2x + 1) + (x - 3) = 3x - 2$ — still a linear function. Multiplying, though, breaks the pattern: $(f \cdot g)(x) = (2x + 1)(x - 3) = 2x^2 - 5x - 3$, which is no longer linear. You will meet this idea in depth on [[Function_Arithmetic_And_Composition]].

---

## Common pitfalls

- **Reading $f(x)$ as multiplication.** The parentheses in $f(x)$ are notation, not a product. $f(3)$ means "feed three into the machine named $f$," not "$f$ times three."
- **Forgetting signs when substituting a negative input.** When you replace $x$ with $-4$ in $-2x + 7$, the negatives combine to give $+8$, not $-8$. Put the input in parentheses while you substitute.
- **Mixing up $m$ and $b$.** Every linear function has exactly these two numbers. The slope $m$ controls the tilt; the y-intercept $b$ controls the height where the line crosses the y-axis. Writing them in the wrong order — or using the point's $y$-value as the intercept instead of solving for $b$ — is the most common slip in example-2-style problems.
- **Assuming every function is linear.** If the rule involves $x^2$, $\sqrt{x}$, $1/x$, or similar, it is not linear and the straight-line intuition breaks. A linear function uses only a multiplication and an addition on the input — nothing else.

---

## Prerequisites

Before working practice problems, make sure you are comfortable with:

- [[Slope]] — the number $m$ that measures steepness
- [[Slope_Intercept_Form]] — the equation $y = mx + b$, which is the same object written with $y$ instead of $f(x)$
- [[Plotting_Points_And_The_Coordinate_Plane]] — so you can read and sketch graphs
- [[Function_Basics]] — the general idea of a function, which this page specializes

---

## Problems Involving Linear Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="linear_functions"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Slope]]
- [[Slope_Intercept_Form]]
- [[Writing_Linear_Equations]]
- [[Modeling_With_Linear_Functions]]
- [[Parallel_And_Perpendicular_Lines]]
- [[Function_Basics]]
- [[Function_Arithmetic_And_Composition]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
