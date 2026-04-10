---
title: "Function Basics"
type: topic
aliases: ["FunctionBasics", "Functions Intro (Algebra 2)", "Function Machine"]
tags: ["#branch-algebra-2", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "2", section: "2.1"}
related:
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Function_Notation"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Function_Arithmetic_And_Composition"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Relations_And_Functions"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: []
summary: "The algebra-2 treatment of functions: inputs, outputs, domain from a formula, range from a graph, and the parent-function preview."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Function Basics

# Function Basics

You met the core idea on [[Relations_And_Functions]]: a function is the kind of relation where each input gets a single output. This page is where algebra 2 sharpens that picture into a working tool. The focus is no longer just on finite lists of ordered pairs — it is on functions defined by formulas, the rules that tell you how to compute the output for any legal input.

$$
f(x) = \text{a recipe for turning } x \text{ into an output}
$$

Once you see a function as a recipe, the three skills you need for the rest of the course fall naturally out of it: feed something in and see what comes out (evaluation), figure out which inputs the recipe can actually swallow (domain), and read heights off a completed picture (range).

---

## The machine picture

The most useful mental model of a function is a machine with a single chute. You drop a number $x$ in the top. The machine obeys its recipe — maybe it squares the input, maybe it takes a square root, maybe it does several steps in a row — and a single output drops out the bottom. The symbol $f(x)$, pronounced "f of x," is not a product. It means "the output that the machine named $f$ produces when the input is $x$."

A function written as $y = f(x)$ has two roles for its variables. The input $x$ is the **independent variable**: you choose it freely. The output $y$ is the **dependent variable**: its value follows, like a shadow, from whatever you decided to put into the machine.

### Explicit vs. implicit descriptions

When the output is written out in closed form — that is, $y$ is entirely on one side of the equation and the rule for building it lives on the other side, as in $y = 3x^2 - 1$ — we say the function is **explicit**. You can evaluate it immediately by substitution. A rule like $x^2 + y^2 = 25$ is **implicit**: $x$ and $y$ are tangled together, and it may or may not describe a function at all. (This particular one is a circle — a relation, but not a function.) Most of the functions you will meet in algebra 2 are explicit; we will handle implicit cases on a page-by-page basis when they come up.

### Piecewise rules

Sometimes the recipe changes depending on which region the input comes from. A **piecewise** function has one formula for small inputs, another for large ones, and maybe a third somewhere in the middle. When you evaluate a piecewise function, your first move is always to figure out which piece applies to the input you were handed.

---

## Finding the domain from a formula

The **domain** of a function is the set of inputs the recipe is allowed to accept. When the function is given by a formula, you hunt for the places the formula would break down, and then you exclude them. Two places are by far the most dangerous:

- **Division by zero.** If the formula has an $x$ sitting in a denominator, any input that makes the denominator hit zero is forbidden. You must exclude those $x$-values.
- **Square roots of negatives.** If the formula has a square root $\sqrt{\cdot}$, the stuff under the root (the radicand) cannot be negative. You must require it to be $\geq 0$.

(Cube roots are fine for any input; logs have their own rules; but for now the big two are enough.) When there is nothing to worry about — for example, $f(x) = 5x - 8$ is just a multiplication and a subtraction — the domain is all real numbers, written $(-\infty, \infty)$ or $\mathbb{R}$.

## Finding the range from a graph

The **range** is the set of outputs the machine actually produces. Reading a range straight from a formula is usually trickier than finding the domain, because you have to reason about what the formula does to every legal input. The cleanest way to see the range is from a graph: project the graph onto the $y$-axis and collect every vertical level the curve touches. Whatever interval of $y$-values you end up with is the range.

## Parent functions — a preview

As you move through algebra 2, a small gallery of standard shapes will keep reappearing: the line $f(x) = x$, the parabola $f(x) = x^2$, the absolute-value V of $f(x) = |x|$, the square-root curve $f(x) = \sqrt{x}$, the reciprocal curve $f(x) = 1/x$, and a few others. Each of these is the **parent** of a whole family — every wider, narrower, shifted, or flipped version lives on the same branch of that family tree. This page is not where we study them, but recognizing the names early will make every later page easier. Each family gets its own dedicated topic.

---

## Example 1: evaluating a function at several inputs

> Let $f(x) = 2x^2 - 5x + 3$. Compute $f$ at $x = 0$, $x = -1$, and $x = 4$.

Each evaluation is the same drill: copy the recipe, put the input in parentheses wherever $x$ used to be, then clean up the arithmetic.

$$
f(0) = 2(0)^2 - 5(0) + 3 = 0 - 0 + 3 = 3
$$

$$
f(-1) = 2(-1)^2 - 5(-1) + 3 = 2(1) + 5 + 3 = 10
$$

$$
f(4) = 2(4)^2 - 5(4) + 3 = 2(16) - 20 + 3 = 32 - 20 + 3 = 15
$$

The parentheses around $-1$ in the second line are not decoration. If you write $2 \cdot -1^2$ without them, you risk squaring $1$ first and then negating, which would give $-1$ instead of $+1$. Slow down when you substitute a negative number: it is the single most common arithmetic slip in function evaluation.

---

## Example 2: finding the domain

> For each rule, identify the set of valid inputs.
>
> (a) $f(x) = \dfrac{x + 2}{x - 5}$
>
> (b) $g(x) = \sqrt{3x + 12}$
>
> (c) $h(x) = x^3 + 7x - 1$

**(a)** The recipe has $x$ in a denominator. Whatever makes the denominator zero must be thrown out:

$$
x - 5 = 0 \ \Longrightarrow\ x = 5.
$$

So the input $x = 5$ is forbidden, but every other real number is fine. The domain is every real number except $5$:

$$
\text{Domain} = \{x \in \mathbb{R} : x \neq 5\} = (-\infty, 5) \cup (5, \infty).
$$

This is the case where most algebra 2 students lose points — they forget to look at the denominator, write "all reals," and drop the exclusion. Any time you see an $x$ downstairs, pause and ask what makes it zero.

**(b)** The recipe has a square root. The expression under the root must be at least zero:

$$
3x + 12 \geq 0 \ \Longrightarrow\ 3x \geq -12 \ \Longrightarrow\ x \geq -4.
$$

The domain is everything from $-4$ upward:

$$
\text{Domain} = [-4, \infty).
$$

The endpoint is included because $\sqrt{0} = 0$ is a perfectly good output.

**(c)** No denominators, no even roots, no logs. Nothing can go wrong, so the input can be anything real:

$$
\text{Domain} = (-\infty, \infty) = \mathbb{R}.
$$

---

## Example 3: reading a graph

> A function $f$ has been graphed. The curve enters from the left at the point $(-3, 5)$, slopes down through $(0, 1)$, reaches its lowest value of $-2$ at $x = 2$, then climbs back up and leaves the visible window at $(6, 5)$. (a) What is $f(0)$? (b) For what input $x$ does $f(x) = -2$? (c) Work out the domain and range from the picture.

**(a)** To get $f(0)$, slide your finger along the $x$-axis until you hit $x = 0$, then walk straight up or down to the curve. The curve passes through $(0, 1)$, so $f(0) = 1$.

**(b)** This is the reverse question: the description tells you the function hits its lowest height of $-2$ at exactly one spot, $x = 2$. So the unique input with output $-2$ is $x = 2$.

**(c)** The visible portion of the curve runs from $x = -3$ to $x = 6$, so every $x$-value in that closed interval appears:

$$
\text{Domain} = [-3, 6].
$$

The curve reaches a minimum height of $-2$ at the bottom and a maximum height of $5$ at the two endpoints. Every value between $-2$ and $5$ is achieved somewhere along the way, so:

$$
\text{Range} = [-2, 5].
$$

---

## Common pitfalls

- **Treating $f(a + 1)$ like $f(a) + f(1)$.** This is wrong for almost every function. To evaluate $f(a + 1)$, you substitute the entire expression $a + 1$ into the recipe wherever $x$ appears, then simplify.
- **Forgetting to exclude denominator zeros when stating the domain.** Always scan the formula for any fraction with $x$ downstairs, set the denominator equal to zero, and solve.
- **Skipping parentheses when substituting a negative.** $(-2)^2 = 4$, but $-2^2 = -4$. Wrapping the input in parentheses the moment you substitute saves you every time.
- **Confusing domain and range.** The domain is the set of legal **inputs** — the $x$-values the machine will accept. The range is the set of possible **outputs** — the $y$-values the machine actually produces. Mixing them up is the number-one vocabulary error in algebra 2.

---

## Prerequisites

Before you tackle the practice problems, make sure you are solid on:

- [[Relations_And_Functions]] — the algebra 1 introduction this page extends
- [[Variables_And_Algebraic_Expressions]] — so letters feel like placeholders for numbers
- [[Evaluating_Expressions]] — substitution is the engine behind every function evaluation
- [[Plotting_Points_And_The_Coordinate_Plane]] — so reading a graph is second nature

---

## Problems Involving Function Basics

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="function_basics"></div>

---

## See Also

- [[Relations_And_Functions]]
- [[Function_Notation]]
- [[Linear_Functions]]
- [[Function_Arithmetic_And_Composition]]
- [[Inverse_Functions]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
