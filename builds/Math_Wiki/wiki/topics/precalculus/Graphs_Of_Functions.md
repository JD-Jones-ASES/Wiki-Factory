---
title: "Graphs of Functions"
type: topic
aliases: []
tags: ["#branch-pre-calculus", "#topic-functions", "#key-topic", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/precalculus/Introduction_To_Functions"
  - "topics/precalculus/Graphs_Of_Equations"
  - "topics/precalculus/Function_Notation"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/precalculus/Introduction_To_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: []
summary: "What a function's curve can tell you at a glance — domain, range, zeros, extrema, and whether the graph is rising or falling."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Graphs of Functions

# Graphs of Functions

Once you are comfortable with the idea that a function $f$ associates each input with a single output, the next natural question is: what does the whole function *look like* when you draw it? The answer is a curve — the set of every pair $(x, f(x))$ plotted on the Cartesian plane. Unlike the dots and tables you used to organize a handful of values, a graph shows you all of them at once, and if you know how to read it, the picture tells you almost everything about the function's behavior in a single glance.

Reading graphs fluently is one of the highest-leverage skills in precalculus. Every function class that comes after — exponentials, logarithms, sinusoids, rational functions, conic-adjacent curves — is introduced through its graph, and problems on standardized tests frequently hand you a graph with no equation and ask you to extract information from it. This page focuses on the specific reading skills: finding a function's domain and range from its picture, spotting the zeros and the extrema, identifying where it is increasing or decreasing, and deciding whether a mystery curve even *is* a function in the first place.

## The graph of $f$ is a specific kind of curve

If $f$ is a function with some domain, its graph is the set of points

$$
\{\,(x, f(x)) \,:\, x \text{ is in the domain of } f\,\}.
$$

This is a special case of the graph of an equation: the equation is $y = f(x)$, and the curve is the picture of all its solutions. The thing that makes the graph of a function distinctive is the single-output rule. Because each $x$-input produces exactly one $y$-output, the curve can never stack two heights at the same $x$. That impossibility is the content of a visual test that every student learns.

## The vertical line test

Here is the test, stated as a check you can perform with a pencil and a ruler. Pick a vertical line anywhere in the plane. Count how many times the graph meets that line. If the answer is ever $2$ or more, the curve is not the graph of a function. If every possible vertical line meets the curve in at most one point, it is.

Why does this work? A vertical line is the set of all points with some fixed $x$-value. If the curve meets the line in two places, those two places are two different $y$-values with the same $x$-value — meaning the input $x$ has been assigned two different outputs. That breaks the single-output rule, so the curve can't be a function.

This test is the fastest way to spot a non-function: the top half of a circle is fine, the whole circle is not; $y = x^2$ is fine, $x = y^2$ is not; any curve that ever "folds back" on itself violates the test somewhere. You will meet this same distinction on [[Relations|relations]], where it is the sharp line between "relation" and "function."

## Reading the domain and range from a picture

The **domain** of a function is the set of $x$-values where the function is defined — the collection of legal inputs. On a graph, the domain shows up as the horizontal spread of the curve: collapse the entire curve straight down onto the $x$-axis, and the shadow it casts *is* the domain. If the curve runs from $x = -3$ to $x = 5$ and never disappears, the domain is $[-3, 5]$. If the curve has a gap in the middle, the domain has a gap. If the curve extends forever to the right, the domain is unbounded on the right.

The **range** is the analogous collapse onto the $y$-axis: it is the set of heights the curve actually reaches. Tilt the curve's shadow onto the $y$-axis and the shaded segment is the range. A parabola opening upward with its vertex at $(0, -4)$ has a range of $[-4, \infty)$, because $y = -4$ is the lowest height the curve achieves and no height is left unreached above that.

A common habit is to check "which way does the curve extend?" and "does it ever turn around?" before committing to a domain and range. An upward parabola runs in both horizontal directions forever, so its domain is $(-\infty, \infty)$; it turns around at its vertex, so its range is bounded below but not above.

## Zeros, intercepts, and extrema

Four features of a function-graph get called out so often that they deserve their own names.

**Zeros.** A **zero** of the function $f$ is any $x$-value for which $f(x) = 0$. On the graph, zeros are exactly the $x$-intercepts — the places the curve meets the $x$-axis. The zeros of $f(x) = x^2 - 4$ are $x = -2$ and $x = 2$; the graph of $f$ meets the $x$-axis at the points $(-2, 0)$ and $(2, 0)$.

**$y$-intercept.** The graph of a function has at most one $y$-intercept (because the function has at most one output at $x = 0$). Its height is simply $f(0)$, if $0$ is in the domain. If $0$ is not in the domain — like for $f(x) = 1/x$ — the graph has no $y$-intercept at all.

**Local extrema.** A **local maximum** is a point on the graph that is higher than everything immediately around it — a peak. A **local minimum** is a point lower than everything immediately around it — a valley. A cubic like $f(x) = x^3 - 3x$ has a local maximum at $x = -1$ and a local minimum at $x = 1$. Local extrema are always written as coordinate pairs, because you need both the $x$-value (where the peak or valley happens) and the $y$-value (how high or low the curve actually gets).

**Global extrema.** When a curve has an overall highest or lowest point across its entire domain, that point is called a global (or absolute) maximum or minimum. The vertex of an upward-opening parabola is a global minimum; an odd-degree polynomial never has any global extremum because it runs to $\pm\infty$ on both ends.

## Increasing and decreasing behavior

As you sweep $x$ from left to right, the graph might be climbing or falling at each moment. An interval of $x$-values where the curve climbs as $x$ increases is called an **increasing interval**; an interval where the curve falls is a **decreasing interval**. The formal versions are:

- $f$ is **increasing** on an interval $I$ when, for any two inputs $a < b$ inside $I$, the outputs satisfy $f(a) < f(b)$.
- $f$ is **decreasing** on an interval $I$ when, for any two inputs $a < b$ inside $I$, the outputs satisfy $f(a) > f(b)$.

"Increasing on an interval" is stronger than "going up between two particular points." It has to work for *every* pair inside the interval. The cubic $f(x) = x^3 - 3x$ is increasing on $(-\infty, -1)$, decreasing on $(-1, 1)$, and increasing again on $(1, \infty)$. The turnaround points — where the behavior switches — are the local extrema.

## Worked examples

**Example 1.** The graph of a function $f$ is a smooth curve that starts at the point $(-4, -3)$, rises to a high point at $(0, 5)$, falls to a low point at $(3, -2)$, and then rises again to end at the point $(6, 4)$. Give the domain, range, zeros, and intervals of increase and decrease.

The curve begins at $x = -4$ and ends at $x = 6$, so collapsing horizontally gives the domain $[-4, 6]$. The lowest height reached anywhere on the curve is $-3$ at the left endpoint, and the highest height is $5$ at $(0, 5)$. The range is therefore $[-3, 5]$.

The zeros are the $x$-values where the curve crosses the $x$-axis. Because the curve runs from $(-4, -3)$ up to $(0, 5)$, it must cross $y = 0$ somewhere between $x = -4$ and $x = 0$; call that zero $x_1$. Between $(0, 5)$ and $(3, -2)$ the curve must cross $y = 0$ again; call that zero $x_2$. Between $(3, -2)$ and $(6, 4)$ it crosses $y = 0$ a third time at some zero $x_3$. Without an exact equation you cannot pin down $x_1, x_2, x_3$ numerically, but the graph shows you there are exactly three of them.

For the intervals of increase and decrease, look at where the curve is climbing and where it is falling:

- Increasing on $[-4, 0]$ (climbing from $(-4, -3)$ up to $(0, 5)$)
- Decreasing on $[0, 3]$ (falling from $(0, 5)$ to $(3, -2)$)
- Increasing on $[3, 6]$ (climbing from $(3, -2)$ back up to $(6, 4)$)

The local maximum is at $(0, 5)$ and the local minimum is at $(3, -2)$. The point $(0, 5)$ is also the global maximum (no height anywhere else reaches $5$). The global minimum is $(-4, -3)$, reached at the left endpoint of the domain.

**Example 2.** Determine whether the curve defined by $x = y^2 - 1$ is the graph of a function of $x$. If it is not, explain what the vertical line test reveals.

Solve the equation for $y$ to see the two-valued output: $y^2 = x + 1$, so $y = \pm\sqrt{x + 1}$. For any $x > -1$, there are two different $y$-values that both satisfy the equation — $\sqrt{x+1}$ and $-\sqrt{x+1}$. That is exactly the situation the vertical line test is designed to catch.

Concretely, pick $x = 3$. Substituting gives $3 = y^2 - 1$, so $y^2 = 4$, so $y = 2$ or $y = -2$. Both $(3, 2)$ and $(3, -2)$ lie on the curve, so a vertical line through $x = 3$ meets the curve in two places. The curve fails the vertical line test.

So the equation $x = y^2 - 1$ is **not** the graph of a function of $x$. It is a perfectly legitimate graph of an equation — it traces out a sideways parabola opening to the right with its vertex at $(-1, 0)$ — but the curve is not a function in the $y = f(x)$ sense. You *can* split it into two functions, $y = \sqrt{x+1}$ (the top half) and $y = -\sqrt{x+1}$ (the bottom half), each of which is a valid function on its own.

**Example 3.** A function $h$ has domain $[-5, 5]$ and its graph is a semicircle forming the upper half of a circle of radius $5$ centered at the origin. Give the range, the $x$-intercepts, the $y$-intercept, and the interval on which $h$ is increasing.

The upper semicircle satisfies $x^2 + y^2 = 25$ with $y \ge 0$, which is $h(x) = \sqrt{25 - x^2}$. The domain is $[-5, 5]$ as given, because the radicand is non-negative exactly when $x^2 \le 25$.

The **range** is the set of heights the semicircle actually reaches. The lowest height is $0$, hit at the two endpoints $x = \pm 5$. The highest height is $5$, hit at the top of the semicircle above $x = 0$. So the range is $[0, 5]$.

The **$x$-intercepts** are the zeros of $h$: the places where the curve meets the $x$-axis. These are the points where $\sqrt{25 - x^2} = 0$, which gives $25 - x^2 = 0$, so $x = \pm 5$. The $x$-intercepts are $(-5, 0)$ and $(5, 0)$.

The **$y$-intercept** is $h(0) = \sqrt{25 - 0} = 5$, so the graph meets the $y$-axis at $(0, 5)$.

As for where the function is increasing, trace the semicircle from left to right. From $x = -5$ up to $x = 0$, the curve is climbing from height $0$ to height $5$ — that is an increasing interval. From $x = 0$ to $x = 5$, the curve is falling from height $5$ back to height $0$ — that is a decreasing interval. So $h$ is increasing on $[-5, 0]$ and decreasing on $[0, 5]$. The single turnaround point is the global maximum at $(0, 5)$.

## Common pitfalls

- **Reading the $y$-value as the domain or the $x$-value as the range.** Domain is on the $x$-axis, range is on the $y$-axis. Always double-check which axis you are collapsing onto.
- **Forgetting that zeros are $x$-intercepts, not $y$-intercepts.** A zero of $f$ satisfies $f(x) = 0$, which is a height of zero — so the point is on the $x$-axis. "Zero" and "$x$-intercept" mean the same thing for a function graph.
- **Confusing local and global extrema.** A local maximum only needs to beat its immediate neighbors. A global maximum has to beat the *entire* rest of the curve. The vertex of a parabola is both, but a wiggly cubic can have local extrema that are nowhere near the global extremes.
- **Declaring a curve a non-function before checking the whole picture.** The vertical line test has to fail for the curve to be ruled out — one vertical line that hits the curve twice is enough, but you need to actually find one. Some curves that look like they might fail actually pass (for example, the graph of $y = |x|$ has a corner at the origin but is still a function).

## Problems Involving Graphs Of Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphs_of_functions"></div>

## See Also

- [[Introduction_To_Functions]] — the definition of a function, before graphs enter the picture
- [[Graphs_Of_Equations]] — the broader category of which function graphs are a special case
- [[Function_Notation]] — reading and writing $f(x)$, which is the algebraic counterpart of plotting a point
- [[Relations]] — the umbrella category that includes curves failing the vertical line test
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
