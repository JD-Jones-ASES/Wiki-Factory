---
title: "Introduction to Functions"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-functions", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Function_Notation"
  - "topics/precalculus/Graphs_Of_Functions"
  - "topics/precalculus/Relations"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Variables_And_Expressions"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "The input-output machine picture of a function, the notation $f(x)$, and the visual test that tells a function apart from a general relation."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Introduction to Functions

# Introduction to Functions

The single most powerful idea in all of precalculus is the notion of a **function**. Everything that follows — exponentials, logarithms, trigonometry, rational curves, the beginnings of calculus — is really a conversation about specific families of functions. Before you can appreciate the distinctions between those families, you need a clean mental picture of what a function is, what it is not, and how to talk about one precisely.

Happily, the core idea is concrete enough that you can carry a simple cartoon of it in your head. A function is a **machine**. You drop an input number into the hopper on top, something inside churns, and a single output number drops out at the bottom. The machine is allowed to be complicated — it might square the input, add seven, take the reciprocal, and then multiply by three — but the one rule it must obey is this: the same input always produces the same output, and there is only ever one output. Drop a $5$ in; the machine gives you back whatever answer it gives, every time, and it does not give you two different answers at once.

That one rule is the whole definition, tightened up a bit. Everything else on this page is language for talking about the machine efficiently.

## The formal statement

Stated precisely, a **function** $f$ from a set $A$ to a set $B$ is a rule that assigns, to each element $x$ of $A$, one and only one element of $B$. The set $A$ is called the **domain**, which you can think of as the collection of legal inputs. The set of outputs you actually hit when you run every element of the domain through the rule is called the **range**. Written symbolically:

$$
f : A \to B, \qquad \text{every } x \in A \text{ is sent to exactly one } f(x) \in B.
$$

In precalculus, $A$ and $B$ are almost always subsets of the real numbers, so you can picture them as number lines rather than abstract sets. What matters is the "exactly one" clause. It is the line between a function and the broader category of [[Relations|relations]], which allow the same input to send you to multiple outputs.

## Function notation

The machine cartoon has a standard piece of notation: $f(x)$. This is the output you get when you feed the input $x$ into the function $f$. It is not "$f$ times $x$" — the parentheses mean "apply the rule" and have nothing to do with multiplication. Reading $f(x)$ aloud, mathematicians say "$f$ of $x$."

If the rule of $f$ is "square the input and subtract seven," you write that as

$$
f(x) = x^2 - 7.
$$

To evaluate $f$ at a specific input, substitute the input for $x$ everywhere on the right side. For example, $f(3)$ means "apply the rule with $x = 3$," which gives $f(3) = 3^2 - 7 = 2$. The output $2$ is paired with the input $3$, and you can describe that pairing as the coordinate pair $(3, 2)$ — the same pair you would plot on a coordinate grid.

The letter $f$ is conventional but not required. You will see $g$, $h$, $p$, $q$, $r$, $T$, and many others, especially when a problem has several functions in play at once and you need a way to tell them apart. See [[Function_Notation]] for more on this.

## The vertical line test

Once you start graphing equations on the [[Cartesian_Plane|coordinate plane]], a simple visual test tells you whether the resulting curve is the graph of a function of $x$. Pick any vertical line. Count how many times the curve meets that line. If the answer is ever $2$ or more, the curve is **not** a function of $x$; if every vertical line meets the curve in at most one point, it is.

The reason is the single-output rule again. A vertical line is the set of points where $x$ is fixed at some value. If the curve meets the line in two places, those two places are two different heights above the same input $x$ — two different outputs paired with one input. That is exactly what a function is not allowed to do.

Concrete examples: the parabola $y = x^2$ passes the test (every vertical line hits it once or not at all). The circle $x^2 + y^2 = 25$ fails the test (most vertical lines hit it twice). The sideways parabola $x = y^2$ fails (every vertical line for $x > 0$ hits it twice). The absolute-value curve $y = |x|$ passes (it has a corner at the origin but no vertical line meets it twice). These visual distinctions will return when you study [[Graphs_Of_Functions|graphs of functions]] in more depth.

## Three common ways to describe a function

In practice, a function can show up in any of three forms, and part of becoming fluent is moving easily between them.

**By formula.** A rule given as an equation, like $f(x) = 2x - 7$ or $g(x) = \sqrt{x + 4}$. This is the most compact form and the one you will see most often. To evaluate at a specific input, substitute.

**By table.** A two-column list: inputs in one column, outputs in the other. A table makes individual values explicit at the cost of hiding the general pattern. A table describes a function as long as no input appears twice with different outputs.

**By graph.** A curve in the Cartesian plane whose points are the pairs $(x, f(x))$. A graph shows every value at once and is the best format for seeing the shape of a function's behavior — rising, falling, approaching a ceiling, oscillating.

Every precalculus course makes you translate between these three forms constantly. Given a formula, you build a table of values and plot its graph. Given a graph, you read off a table of key points. Given a table (say, a list of experimental data), you try to guess a formula that fits.

## Worked examples

### Example 1

Determine whether the equation $y = x^2$ defines $y$ as a function of $x$, and compute the output at $x = -3$.

For $y = x^2$ to define $y$ as a function of $x$, every legal input $x$ must produce exactly one output $y$. Pick any real number $x$ and compute $x^2$. You get a single, unambiguous real number — squaring never produces two different answers. So yes, $y = x^2$ does define $y$ as a function of $x$. Writing it with function notation, you can name the function $f$ and say $f(x) = x^2$.

At $x = -3$, substitute:

$$
f(-3) = (-3)^2 = 9.
$$

The output is $9$. The coordinate pair $(-3, 9)$ lies on the graph of $f$.

A useful contrast: the equation $y^2 = x$ does **not** define $y$ as a function of $x$. At $x = 9$, both $y = 3$ and $y = -3$ satisfy the equation, so the same input produces two outputs, which breaks the single-output rule. The graph of $y^2 = x$ is a sideways parabola that fails the vertical line test, and you cannot write it in the form $y = f(x)$ without splitting it into two pieces.

### Example 2

Given $f(x) = 2x - 7$, compute $f(3)$, $f(-2)$, and $f(a + 1)$.

Each of these is a substitution into the rule "$2x - 7$."

$$
f(3) = 2 \cdot 3 - 7 = 6 - 7 = -1.
$$

$$
f(-2) = 2 \cdot (-2) - 7 = -4 - 7 = -11.
$$

The third one is slightly different. Instead of a specific number, you are handed an algebraic expression $a + 1$ and asked to evaluate the function there. Substitute $a + 1$ in place of $x$ everywhere on the right side:

$$
f(a + 1) = 2(a + 1) - 7 = 2a + 2 - 7 = 2a - 5.
$$

The output is the simplified algebraic expression $2a - 5$. This kind of symbolic evaluation comes up constantly — when you compose functions, when you shift graphs, when you compute the difference quotient that opens calculus. The move is always the same: wherever you see $x$ in the rule, stick the new expression in, parentheses and all, then simplify.

### Example 3

Determine whether the set of coordinate pairs $\{(1, 2),\, (2, 3),\, (1, 4),\, (5, 6)\}$ describes a function of $x$.

A function from $x$ to $y$ demands that each $x$-value appear at most once in the input column. Scan the first coordinates: $1, 2, 1, 5$. The value $1$ shows up twice — once paired with $2$, once paired with $4$. That is two different outputs for the same input $x = 1$, exactly the single-output rule being broken.

So the set does **not** describe a function of $x$. It does describe a relation, and if you plotted all four points and drew a vertical line through $x = 1$, it would hit two of them — a visible vertical line test failure.

A small change would rescue the example. Replace the third pair with $(3, 4)$, and the set becomes $\{(1, 2),\, (2, 3),\, (3, 4),\, (5, 6)\}$. Now the first coordinates $1, 2, 3, 5$ are all distinct, and each input has exactly one output. That set **is** a function. Notice that the outputs are still allowed to repeat if they want — what the rule forbids is a repeated input with different outputs, not a repeated output with different inputs.

## Common pitfalls

- **Reading $f(x)$ as multiplication.** $f(x)$ is "the value of $f$ at $x$," not "$f$ times $x$." This feels obvious until you run into an expression like $f(a + b)$ and get tempted to distribute $f$ like a coefficient. Don't — $f$ is a function, not a factor.
- **Letting an input collide with two different outputs.** A relation can contain $(1, 2)$ and $(1, 4)$ at the same time. A function cannot. The single-output rule is the only property that distinguishes these two categories.
- **Forgetting the domain restriction.** $f(x) = 1/x$ is a perfectly valid function, but its domain excludes $x = 0$ because $1/0$ is undefined. Always check whether your substitution produces an undefined value.
- **Mixing up "output $y$" with "the letter $y$."** The function rule might use any letter for the input or the output. $r = t^3$ is the same kind of statement as $y = x^3$; the letters are just labels.

## Problems Involving Introduction To Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="introduction_to_functions"></div>

## See Also

- [[Function_Notation]] — more on reading, writing, and evaluating $f(x)$ fluently
- [[Graphs_Of_Functions]] — how the machine-picture becomes a curve, and what the curve reveals
- [[Relations]] — the broader category of which functions are a special case
- [[Algebraic_Functions]] — the big sub-family you meet first in precalculus
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
