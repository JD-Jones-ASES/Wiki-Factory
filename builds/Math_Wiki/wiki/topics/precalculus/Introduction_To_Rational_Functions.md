---
title: "Introduction to Rational Functions"
type: topic
aliases: ["Rational Functions Intro"]
tags: ["#branch-pre-calculus", "#topic-rational-expressions", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "4", section: "4.1"}
related:
  - "topics/algebra/Graphing_Rational_Functions_Part_1"
  - "topics/algebra/Graphing_Rational_Functions_Part_2"
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Power_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Linear_Functions"
problem_type_ids: []
figures: []
summary: "A gentle welcome to rational functions via the reciprocal parent and its shifted cousins."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Introduction to Rational Functions

# Introduction to Rational Functions

A **rational function** is the ratio of two polynomial functions:

$$
f(x) = \dfrac{p(x)}{q(x)}
$$

where $p$ and $q$ are polynomials and $q$ is not the zero polynomial. That's it — any ordinary function you can write as a polynomial divided by another polynomial belongs to this family. The word "rational" here is borrowed from the word "ratio", not from anything about "reasonable" — a rational function is just a fraction whose top and bottom are both polynomials.

Pre-calculus treats rational functions as a first-class topic because their graphs behave in ways earlier families didn't. They can have **gaps** in their domain (the denominator might be zero somewhere), **walls** they can't cross (vertical asymptotes), and **horizons** they creep toward but never touch (horizontal asymptotes). This page is the gentle introduction: the parent function, its shape, and a preview of the tools you'll use to graph its descendants. The full graphing machinery lives on the algebra-2 pages [[Graphing_Rational_Functions_Part_1]] and [[Graphing_Rational_Functions_Part_2]].

---

## Domain: the first thing to think about

Because a fraction is undefined when its bottom is zero, the **domain** of a rational function is always "every real number **except** the zeros of the denominator." Writing out the domain is the first thing you do when you meet a new rational function. For instance, if

$$
f(x) = \dfrac{x + 5}{x - 4},
$$

then the denominator is zero at $x = 4$, and nothing else is wrong. The domain is $\{x \in \mathbb{R} : x \neq 4\}$, or equivalently $(-\infty, 4) \cup (4, \infty)$ in interval notation. Every rational function comes with this disclaimer: the graph has one or more x-values that are forbidden.

---

## The parent: $f(x) = 1/x$

The simplest rational function — the one that every other rational function is "a transformation of, in spirit" — is the **reciprocal**:

$$
f(x) = \dfrac{1}{x}.
$$

Its domain is everything except zero: $\{x : x \neq 0\}$. The graph has two branches, one in the first quadrant where $x$ and $y$ are both positive, and one in the third quadrant where both are negative. Neither branch touches either axis: the x-axis ($y = 0$) and the y-axis ($x = 0$) are both **asymptotes** — lines that the graph approaches arbitrarily closely without ever meeting.

Here's why the shape is what it is. For small positive $x$, like $x = 0.01$, the reciprocal $1/x$ is $100$ — very large. For very large positive $x$, like $x = 100$, the reciprocal is $0.01$ — very small. So as $x$ moves from small to large on the positive side, $y$ moves from large to small. On the negative side the same trade-off happens with opposite signs. The two branches are mirror images of each other through the origin, and the whole graph has 180° rotational symmetry about $(0, 0)$.

---

## Shifting and scaling the reciprocal

Every "near-reciprocal" rational function is some shift or stretch of $1/x$. If you take

$$
f(x) = \dfrac{k}{x - h} + c
$$

then the reciprocal parent has been slid horizontally by $h$, scaled vertically by $k$, and lifted vertically by $c$. The vertical asymptote of the parent was $x = 0$; for the shifted version, it's $x = h$. The horizontal asymptote of the parent was $y = 0$; for the shifted version, it's $y = c$. If $k > 0$, the branches stay in the "northeast / southwest" configuration relative to the new asymptote intersection. If $k < 0$, they flip to "northwest / southeast."

That's all you need to hand-sketch a simple rational function at the pre-calc intro level. The more complicated rational functions — the ones with polynomials of higher degree on top or bottom — need the full graphing recipe from [[Graphing_Rational_Functions_Part_2]].

---

## Example 1: finding the domain

> Write the domain of $f(x) = \dfrac{x + 3}{x - 4}$ in interval notation.

Set the denominator equal to zero and solve: $x - 4 = 0 \Rightarrow x = 4$. This is the one value that's excluded. Everything else is fair game.

The domain is therefore

$$
(-\infty, 4) \cup (4, \infty).
$$

In set-builder notation, that's $\{x \in \mathbb{R} : x \neq 4\}$. On the real number line, the domain is every point except a single dot at $x = 4$, which is where the graph will have a vertical asymptote.

---

## Example 2: describing the parent function's shape

> Describe the key features of the graph of $f(x) = \dfrac{1}{x}$.

First, the domain: everything except $x = 0$. The denominator is $x$, and it's zero only at $x = 0$.

Second, the asymptotes. The y-axis ($x = 0$) is a vertical asymptote because the function explodes as $x$ approaches $0$ from either side. The x-axis ($y = 0$) is a horizontal asymptote because $1/x$ approaches $0$ as $|x|$ grows without bound.

Third, the branches. For $x > 0$ the output $1/x$ is positive and decreases from very large values (near $x = 0^+$) toward $0$ (as $x \to \infty$). That puts the right branch entirely in quadrant I. For $x < 0$ the output is negative; the left branch lives entirely in quadrant III.

Fourth, the symmetry. The reciprocal is an **odd function**: $f(-x) = -f(x)$. That means its graph is unchanged by a half-turn rotation about the origin, which is exactly what you see when you compare the two branches.

Finally, the reciprocal never crosses either axis, because the x-axis is a horizontal asymptote and the y-axis is a vertical asymptote. Both axes are boundaries, not visited destinations.

---

## Example 3: shifting the reciprocal

> Describe the graph of $f(x) = \dfrac{1}{x - 2} + 3$ as a transformation of the parent $1/x$.

Match against the shift form $\dfrac{k}{x - h} + c$: here $k = 1$, $h = 2$, $c = 3$. So the parent reciprocal has been slid two units to the **right** and three units **up**.

Both asymptotes move with the graph. The vertical asymptote of the parent was $x = 0$; it is now $x = 2$. The horizontal asymptote of the parent was $y = 0$; it is now $y = 3$. The "center" where the two asymptotes cross — the place the graph rotates around — has moved from $(0, 0)$ to $(2, 3)$.

The branches stay in the "northeast/southwest" layout relative to the new center (because $k > 0$): one branch lies up and to the right of $(2, 3)$, the other down and to the left. The shape of each branch is the same as before; only the location has moved.

The domain is now $\{x : x \neq 2\}$, and the range is $\{y : y \neq 3\}$ — both "one forbidden value" sets, which is characteristic of the shifted reciprocal family.

---

## Common pitfalls

- **Forgetting to state the domain.** Every rational function excludes at least one x-value. Forgetting to write it down is the number-one way to lose points on a pre-calc homework.
- **Trying to "plug in" the asymptote x-value.** You can't evaluate $1/x$ at $x = 0$; the function is undefined there. No amount of limit chicanery in a basic pre-calc course will change that.
- **Drawing the two branches connected.** The branches of $1/x$ live in different quadrants and never meet. There's no ink allowed on or through the vertical asymptote.
- **Thinking the horizontal asymptote is always $y = 0$.** It's only $y = 0$ for the plain parent. For $1/(x - 2) + 3$, the horizontal asymptote is $y = 3$ — it moved with the function.

---

## Prerequisites

- [[Function_Basics]] — domains, ranges, and function notation
- [[Simplifying_Rational_Expressions]] — how rational expressions factor and cancel
- [[Linear_Functions]] — familiarity with simple shifts applied to basic parent functions

---

## Problems Involving Rational Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="introduction_to_rational_functions"></div>

---

## See Also

- [[Graphing_Rational_Functions_Part_1]] — the fuller algebra-2 graphing recipe, part 1
- [[Graphing_Rational_Functions_Part_2]] — slant asymptotes and sign diagrams
- [[Simplifying_Rational_Expressions]] — algebraic prep for the graphing work
- [[Power_Functions]] — the reciprocal is the $n = -1$ case of the power family
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
