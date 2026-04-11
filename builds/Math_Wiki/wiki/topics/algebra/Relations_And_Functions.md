---
title: "Relations and Functions"
type: topic
aliases: ["Relations", "Functions Introduction", "Is It A Function"]
tags: ["#branch-algebra-1", "#topic-functions", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "4", section: "4.2"}
  - {book: "math_2", chapter: "9", section: "9.1"}
related:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Notation"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Function_Arithmetic_And_Composition"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: []
summary: "A relation is any collection of ordered pairs; a function is the special kind where every input has exactly one output."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Relations and Functions

# Relations and Functions

Most of algebra is built on a single idea: start with an input, follow a rule, get back an output. The vocabulary on this page gives that idea a precise language. By the end you should be able to look at a list of coordinates, a table of values, a mapping arrow diagram, or a graph — and answer a single yes-or-no question: does this object actually behave like a function, or does it sneak one input past two different outputs?

$$
\text{input} \ \longrightarrow \ \text{rule} \ \longrightarrow \ \text{output}
$$

---

## What is a relation?

A **relation** is just a bag of ordered pairs $(x, y)$. Nothing more. You can describe that bag however you like — by listing the pairs out, by organizing them in a table, by drawing them on a coordinate plane, by drawing arrows from each first coordinate to its partner second coordinate, or by writing down an equation that every pair in the bag must satisfy. All of these presentations are describing the same kind of object: a set of $(x, y)$ pairs.

Every relation comes with two built-in sets. The **domain** is the collection of all first coordinates that actually show up in the relation — the inputs. The **range** is the collection of all second coordinates — the outputs. If a value shows up more than once, you only list it once in the domain or range: these are sets, not tallies.

---

## What is a function?

A **function** is the restricted kind of relation that gives each input a single, unambiguous output. In other words, scan the $x$-coordinates of all your ordered pairs. If any $x$-value appears twice with two different $y$-values, the relation is disqualified — it is not a function. If every $x$ either appears once, or appears several times always paired with the same $y$, you have a function.

A quick way to state the rule: for every input in the domain, you should be able to answer the question "what output does the function produce here?" with exactly one number. No ambiguity. Two possible outputs for the same input breaks the contract.

It is perfectly fine for two different inputs to share the same output. The relation $\{(1, 7), (2, 7), (3, 7)\}$ is a function — three different inputs, all three sent to the number $7$. The rule is only about whether a single input ever has competing outputs.

---

## Four ways to picture a relation

The same relation can wear several different costumes. A fluent algebra student learns to recognize it in all four and to slide between them.

1. **A set of ordered pairs.** The most literal form: a list like $\{(1, 3),\, (2, 5),\, (3, 7)\}$. To test whether it is a function, scan the first coordinates for repeats with different partners.
2. **A table of values.** The $x$-column stores the inputs and the $y$-column stores the outputs. Each row is one ordered pair. A repeated entry in the $x$-column with different $y$-entries kills the function property.
3. **A mapping diagram.** Draw the domain on the left, the range on the right, and pull an arrow from each input to its output. A function is any diagram where no input has two arrows leaving it.
4. **A graph.** Plot every ordered pair as a point in the coordinate plane. The function property translates into a visual check, which is where the vertical line test comes in.

---

## The vertical line test

If you are staring at a graph and want to know whether it describes a function, here is the only test you need.

> Sweep a vertical line across the graph from left to right. If that moving line ever touches the graph at two or more points at the same time, the graph cannot represent a function. If the line touches at most one point at every horizontal position, the graph does represent a function.

Why does this work? A vertical line is the set of points sharing a single $x$-value. If the graph hits that line in two places, that single $x$-value is paired with two different $y$-values — precisely the forbidden situation. A circle, for example, fails the test instantly: any vertical line through the interior stabs the circle at a top point and a bottom point, so the same $x$ lands at two different heights. A straight (non-vertical) line always passes the test, because every vertical line crosses it in exactly one place.

---

## Example 1: is this relation a function?

> Decide whether each of the following sets of ordered pairs is a function. For any that is not, say which input is the troublemaker.
>
> (a) $\{(-4, 2),\ (-1, 6),\ (3, 6),\ (5, -2)\}$
>
> (b) $\{(7, 1),\ (2, 9),\ (7, -3),\ (4, 0)\}$
>
> (c) $\{(0, 8),\ (1, 8),\ (2, 8),\ (3, 8)\}$

Scan the first coordinates in each bag.

**(a)** The inputs are $-4, -1, 3, 5$. Every one of them is different. Each input has exactly one output, so this relation **is** a function. Notice that the output $6$ shows up twice — but that does not matter. Repeats in the second coordinate are allowed.

**(b)** The inputs are $7, 2, 7, 4$. The value $7$ shows up twice, and the two pairs involving it are $(7, 1)$ and $(7, -3)$. One input, two different outputs. This relation is **not** a function; $x = 7$ is the troublemaker.

**(c)** The inputs $0, 1, 2, 3$ are all distinct. Every input points to the same output, $8$, but that is fine — the rule only forbids one input from having several outputs. This relation **is** a function. (In fact, it is a piece of the constant function $f(x) = 8$.)

---

## Example 2: applying the vertical line test

> Imagine the following graphs. For each one, decide whether it represents a function.
>
> (a) A straight line slanting upward from the lower left to the upper right.
>
> (b) A circle of radius $4$ centered at the origin.
>
> (c) A perfectly vertical line through $x = 2$.
>
> (d) A parabola opening upward with its lowest point at $(0, -1)$.

Slide a vertical line across each picture and count crossings.

**(a)** A non-vertical straight line is crossed by every vertical line in exactly one point. The graph **is** a function.

**(b)** A vertical line drawn through the inside of the circle pierces the top half and the bottom half — two crossings. The graph is **not** a function. For instance, both $(0, 4)$ and $(0, -4)$ sit on the circle, so the input $x = 0$ has two competing outputs.

**(c)** A vertical line is, in a sense, entirely made of stacked-up points sharing a single $x$-value. If your "graph" is literally the line $x = 2$, then a test line drawn at $x = 2$ overlaps it completely — infinitely many crossings. It is emphatically **not** a function. (This is why linear equations of the form $x = c$ are called vertical lines, not linear functions.)

**(d)** A parabola opening upward, like $y = x^2 - 1$, is crossed by each vertical line at exactly one point. It **is** a function, even though many horizontal lines hit it twice. The vertical line test is the only one that matters for function-ness.

---

## Example 3: reading domain and range off a finite relation

> Write down the domain and the range of the relation $\{(-2, 5),\ (1, 0),\ (3, 5),\ (4, -7)\}$, and then say whether the relation is a function.

Peel off all the first coordinates and all the second coordinates, listing each distinct value only once:

$$
\text{Domain} = \{-2,\ 1,\ 3,\ 4\}, \qquad \text{Range} = \{-7,\ 0,\ 5\}.
$$

Even though the output $5$ comes up twice in the list of pairs, you only write it once inside the range set. Now check for function-ness: the four inputs $-2, 1, 3, 4$ are all different, so every input has a single output partner. The relation **is** a function.

---

## Common pitfalls

- **Confusing "repeated output" with "repeated input."** Two ordered pairs sharing the same $y$-value is fine; two ordered pairs sharing the same $x$-value with different $y$-values is the fatal mistake. Always scan the first column, not the second.
- **Forgetting that vertical lines fail.** A perfectly vertical line has a single input paired with infinitely many outputs. It is never a function.
- **Misreading the vertical line test.** The test asks whether the moving line ever hits the graph more than once — at the same moment. A line that hits the graph once on the left and once on the right (at different $x$-values) is perfectly acceptable.
- **Listing repeated values in the domain or range.** These are sets, so each distinct value is listed once. Writing the range of $\{(1, 5), (2, 5)\}$ as $\{5, 5\}$ is wrong; it is just $\{5\}$.

---

## Prerequisites

Before you work practice problems on this page, make sure you are comfortable with:

- [[Variables_And_Algebraic_Expressions]] — so the $x$ and $y$ symbols feel natural
- [[Evaluating_Expressions]] — plugging a number in for a letter is the engine behind "find $f(3)$"
- [[Plotting_Points_And_The_Coordinate_Plane]] — reading ordered pairs off a graph is half the skill

---

## Problems Involving Relations and Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="relations_and_functions"></div>

---

## See Also

- [[Function_Basics]]
- [[Function_Notation]]
- [[Linear_Functions]]
- [[Plotting_Points_And_The_Coordinate_Plane]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
