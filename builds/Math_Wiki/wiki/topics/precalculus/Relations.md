---
title: "Relations"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-analytic-geometry", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Introduction_To_Functions"
  - "topics/precalculus/Graphs_Of_Functions"
  - "topics/precalculus/Cartesian_Plane"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/Variables_And_Expressions"
  - "topics/algebra/Relations_And_Functions"
problem_type_ids: []
figures: []
summary: "Any pairing of x-values with y-values, whether or not it obeys the one-output-per-input rule that turns a relation into a function."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Relations

# Relations

A **relation** is the most permissive kind of pairing you can put between two sets of numbers. Whenever you have a collection of coordinate pairs $(x, y)$ — no matter how they were chosen, no matter whether any rule generated them — you already have a relation. The word just names the collection. Because the definition is so loose, every function is a relation, but plenty of relations are not functions. Understanding which relations make the cut, and which do not, is one of the first things a precalculus course asks of you.

You can picture a relation as a list of points, a region of the plane, or the solution set of an equation. Whatever form you use, the underlying object is always the same: a bundle of coordinate pairs. The question "is this a function?" is the question "does any $x$-value show up with two different $y$-values?" If the answer is no, the relation is a function; if the answer is yes, it is not. That single check is the gateway from the broad category of relations to the narrower category of functions, and it is the main reason the word *relation* exists at all.

## The formal definition

At its most compact, a relation is any collection of coordinate pairs $(x, y)$ grouped together for some reason. Written as a set:

$$
R \;=\; \{\,(x, y) \,:\, x \text{ and } y \text{ satisfy some condition}\,\}.
$$

The "condition" can be absolutely anything. It might be a specific equation, like $y = x^2$. It might be an inequality, like $y \ge x$. It might be a tabular list of pairs with no algebraic description at all, like $\{(1, 4),\, (2, 7),\, (5, -3)\}$. It might be a shape drawn freehand on the Cartesian plane. Whatever captures the pairing is fair game.

Two more vocabulary words come attached to every relation. The **domain** is the set of all $x$-values that appear as the first coordinate of at least one pair in the relation. The **range** is the set of all $y$-values that appear as the second coordinate of at least one pair. If the relation is $\{(1, 4),\, (2, 7),\, (5, -3)\}$, the domain is $\{1, 2, 5\}$ and the range is $\{4, 7, -3\}$. If the relation is the circle $x^2 + y^2 = 25$, the domain is $[-5, 5]$ and the range is $[-5, 5]$.

## Every function is a relation (but not vice versa)

A function is just a relation with one extra requirement: no $x$-value is allowed to appear as the first coordinate of two different pairs. Said differently, the single-output rule you met in [[Introduction_To_Functions|introduction to functions]] is the membership test for the subcategory "functions" inside the bigger category "relations." Functions are the well-behaved relations — the ones in which knowing $x$ tells you $y$ uniquely. Non-function relations are the wilder ones, in which knowing $x$ might leave $y$ ambiguous.

Here is a picture of the hierarchy:

$$
\text{all coordinate pairs} \;\supset\; \text{relations} \;\supset\; \text{functions}.
$$

The middle set, "relations," is where this page lives. Any pairing at all. The outer set, "every coordinate pair you could imagine," is not especially interesting — without some structure, there is nothing to say. The inner set, "functions," is the special case with the single-output rule.

Why spend any time on relations that are not functions, if functions get all the good tools? Two reasons. First, some important shapes — circles, ellipses, full sideways parabolas — are relations that are not functions, and refusing to talk about them because they fail the vertical line test would be needlessly limiting. Second, the broader category of relations includes things like inequalities that carve out *regions* of the plane, and those regions are indispensable for linear programming, systems of inequalities, and many applied problems.

## Three ways a relation can show up

**As a list of pairs.** A small relation can be written out explicitly: $R = \{(1, 2),\, (3, 4),\, (5, 6)\}$. The domain is $\{1, 3, 5\}$ and the range is $\{2, 4, 6\}$. To test whether the relation is a function, check whether any first coordinate is repeated with a different second coordinate. In this case all three first coordinates are different, so $R$ is a function.

**As an equation.** A relation can be the solution set of a two-variable equation: $x^2 + y^2 = 25$ defines the relation consisting of all points on the circle of radius $5$ centered at the origin. To test whether the relation is a function, either (a) solve for $y$ and check whether you get a single expression or two, or (b) look at the graph and apply the vertical line test. For the circle, solving gives $y = \pm\sqrt{25 - x^2}$ — two values — so it is not a function.

**As an inequality or a region.** A relation can also be a whole region of the plane. The inequality $y \ge x$ defines the relation consisting of every point on or above the line $y = x$: a half-plane. Describing this relation as "a collection of coordinate pairs" is honest — it just happens to be an infinite collection forming a shaded half of the plane. A half-plane is emphatically not a function, since for every $x$-value there are infinitely many $y$-values with $(x, y)$ in the relation.

## Reading the domain and range

The domain and range of a relation come directly from the coordinates of the pairs. You do not need any fancy tools.

- For a **list of pairs**: collect all first coordinates into the domain and all second coordinates into the range, removing duplicates.
- For an **equation**: determine which $x$-values produce at least one real $y$-value (domain), and which $y$-values show up as a second coordinate somewhere (range). For a circle $x^2 + y^2 = r^2$, both domain and range are $[-r, r]$.
- For a **region or inequality**: project the region straight down onto the $x$-axis and read off the domain; project straight left onto the $y$-axis and read off the range. A half-plane like $y \ge x$ has domain $(-\infty, \infty)$ and range $(-\infty, \infty)$ — every $x$-value appears, and every $y$-value appears.

## Worked examples

**Example 1.** Identify which of the following sets of coordinate pairs describe a function of $x$, and give the domain and range of each.

$A = \{(-2, 3),\, (0, 3),\, (2, 3),\, (4, 3)\}$, $B = \{(1, -1),\, (1, 1),\, (4, 2),\, (9, 3)\}$, $C = \{(-3, 9),\, (-2, 4),\, (0, 0),\, (2, 4),\, (3, 9)\}$.

For $A$, the first coordinates are $-2, 0, 2, 4$ — all distinct. So $A$ is a **function**. The second coordinate is always $3$, but that is no obstacle: a function can absolutely send many inputs to the same output. The domain is $\{-2, 0, 2, 4\}$ and the range is $\{3\}$.

For $B$, the first coordinates are $1, 1, 4, 9$ — the value $1$ appears twice, once paired with $-1$ and once paired with $1$. That is two different outputs for the same input, which breaks the single-output rule. So $B$ is **not** a function. Its domain is $\{1, 4, 9\}$ and its range is $\{-1, 1, 2, 3\}$. (By the way, $B$ is the graph of the square-root relation $y^2 = x$ at four sample points — exactly the non-function you would get if you kept both the positive and negative square roots.)

For $C$, the first coordinates are $-3, -2, 0, 2, 3$ — all distinct. So $C$ is a **function**. Notice that the second coordinates repeat: both $-3$ and $3$ pair with $9$, and both $-2$ and $2$ pair with $4$. That is allowed. What is forbidden is a repeated first coordinate, not a repeated second. The domain is $\{-3, -2, 0, 2, 3\}$ and the range is $\{0, 4, 9\}$.

**Example 2.** Describe the relation defined by the inequality $y \ge x$, state its domain and range, and decide whether it is a function.

The relation is the set $\{(x, y) : y \ge x\}$ — every coordinate pair whose second coordinate is greater than or equal to its first. Geometrically this is a **half-plane**. Draw the line $y = x$ (a diagonal through the origin with slope $1$); every point on the line itself satisfies $y = x$, which counts as $\ge$, so the boundary is included. Every point above the line satisfies $y > x$, also in the relation. Every point below the line fails, so it is excluded.

The domain is $(-\infty, \infty)$: for any real number $x$, you can always find a $y$ with $y \ge x$ (for instance, $y = x$ itself works). The range is $(-\infty, \infty)$ as well: for any real number $y$, you can always find an $x$ with $y \ge x$ (for instance, $x = y$, or $x = y - 1$). Both the horizontal and vertical shadows of the shaded region cover the entire real line.

Is this relation a function of $x$? Take $x = 0$. Then every $y$ with $y \ge 0$ is paired with the input $0$, so the relation contains the pairs $(0, 0)$, $(0, 1)$, $(0, 2)$, and infinitely many more. That is an enormous number of outputs for the single input $x = 0$, so the single-output rule fails violently. The relation is **not** a function. It is a perfectly respectable half-plane, and it is the kind of object that appears whenever you graph a two-variable inequality, but it is not a function.

**Example 3.** Determine whether the equation $x = y^2$ defines $y$ as a function of $x$. Give the domain of the relation, the range of the relation, and a description of the curve it draws.

First, solve for $y$: $y^2 = x$, so $y = \pm\sqrt{x}$. This tells you two things at once. For $x > 0$, there are two $y$-values — one positive and one negative — both satisfying the equation. For $x = 0$, there is one $y$-value, namely $y = 0$. For $x < 0$, there is no real $y$-value at all, because $y^2$ cannot be negative.

Because most inputs produce two outputs, the equation does **not** define $y$ as a function of $x$. The relation fails the vertical line test: at, say, $x = 9$, the pairs $(9, 3)$ and $(9, -3)$ are both in the relation.

The domain of the relation is $\{x : x \ge 0\} = [0, \infty)$. The range is all real numbers: every value $y$ is paired with the input $x = y^2$, which is always a legitimate non-negative number. The range is $(-\infty, \infty)$.

The curve is a sideways parabola opening to the right, with its vertex at the origin. The upper branch is the graph of $y = \sqrt{x}$ (a function on its own), the lower branch is the graph of $y = -\sqrt{x}$ (another function), and together they form the full relation. This is a typical way to rescue a non-function: slice it into pieces, each of which *is* a function, and study those pieces separately.

## Common pitfalls

- **Thinking a relation must be expressible by an equation.** A relation is just a collection of coordinate pairs. A random list of five points is a relation. A scribble on a coordinate plane is a relation. Equations and formulas are one way to describe a relation, not a requirement.
- **Mixing up the rules for repeated coordinates.** A function forbids repeated *first* coordinates (same $x$, two $y$'s). It allows repeated *second* coordinates (different $x$'s, same $y$). The rule is asymmetric, and swapping the two leads to wrong answers on every "is this a function?" problem.
- **Forgetting that the domain of an equation is determined by the real numbers.** Even if an equation like $y^2 = x$ is perfectly algebraic, the domain of the relation it defines in real numbers is restricted by the requirement that all pairs be real. For $y^2 = x$, the domain is $[0, \infty)$, not $(-\infty, \infty)$.
- **Equating "not a function" with "bad."** A circle is not a function, but it is a great shape. A half-plane is not a function, but it is the solution set of an inequality you will graph constantly. "Not a function" means you cannot write the relation in the form $y = f(x)$; it does not mean the relation is useless.

## Problems Involving Relations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="relations"></div>

## See Also

- [[Introduction_To_Functions]] — the special case of relations that obey the single-output rule
- [[Graphs_Of_Functions]] — what changes when the relation you are graphing happens to be a function
- [[Cartesian_Plane|The Cartesian Plane]] — the coordinate grid on which every relation lives
- [[Graphs_Of_Equations]] — a major source of relations given by two-variable equations
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
