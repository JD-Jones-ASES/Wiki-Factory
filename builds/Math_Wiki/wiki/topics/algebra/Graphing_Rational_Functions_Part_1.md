---
title: "Graphing Rational Functions: Part 1"
type: topic
aliases: ["Rational Function Graphs"]
tags: ["#branch-algebra-2", "#topic-rational-expressions", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "6", section: "6.4"}
related:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Graphing_Rational_Functions_Part_2"
  - "topics/algebra/Polynomial_Functions_And_Graphs"
  - "topics/algebra/Function_Basics"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: ["algebra/rational_asymptotes.svg"]
summary: "Finding asymptotes, holes, and intercepts so a rational function can be sketched sensibly."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Graphing Rational Functions: Part 1

# Graphing Rational Functions: Part 1

A **rational function** is a quotient of two polynomials:

$$
f(x) = \dfrac{p(x)}{q(x)}.
$$

Graphs of rational functions look nothing like the smooth continuous curves you've been drawing up to now. They can have gaps, vertical walls they never cross, and horizontal lines they creep toward without ever touching. This page is the first half of the graphing toolkit: how to find the four key features — **vertical asymptotes**, **holes**, **horizontal asymptotes**, and **intercepts** — that let you sketch a rational function without plotting a hundred points. Part 2 covers the deeper analysis with slant asymptotes and sign diagrams.

![[rational_asymptotes.svg|A rational function with vertical and horizontal asymptotes]]

---

## Where can a rational function explode?

A fraction is undefined whenever its bottom equals zero. That is the central fact that shapes every rational graph. So the first question to ask about $f(x) = p(x) / q(x)$ is: **which x-values make $q(x) = 0$?** Those x-values are the candidates for trouble. But not every zero of $q$ is the same kind of trouble — some of them are asymptotes, and some of them are holes. The distinction depends on whether the same x-value is also a zero of $p$.

**Vertical asymptote** at $x = c$: $q(c) = 0$ and $p(c) \neq 0$. The bottom tries to shrink to zero while the top stays nonzero, so $f(x)$ shoots to $\pm\infty$ near $c$. The graph has a vertical wall at $x = c$ that it never touches.

**Hole** at $x = c$: $q(c) = 0$ and $p(c) = 0$ too. The factor $(x - c)$ appears in both the top and the bottom and cancels when you simplify. The simplified version is a perfectly well-behaved function at $c$, but the original was still undefined there. So you draw the simplified graph and then erase a single point — the hole.

---

## Horizontal asymptotes from the degrees

A **horizontal asymptote** is a horizontal line that the graph approaches as $x$ gets very large in either direction. Which line, if any, comes down to a three-case rule based on comparing the degrees of the top and bottom polynomials.

Let $n$ be the degree of $p$ and $m$ be the degree of $q$.

- If $n < m$, the denominator grows faster than the numerator as $|x| \to \infty$. The fraction shrinks to zero. Horizontal asymptote: $y = 0$.
- If $n = m$, the degrees are tied and the ratio is dominated by the leading coefficients. Horizontal asymptote: $y = (\text{leading coef of } p) / (\text{leading coef of } q)$.
- If $n > m$, the numerator grows faster, so the fraction blows up in magnitude and no horizontal asymptote exists. (There may be a slant asymptote instead — that's for Part 2.)

The x-intercepts and y-intercept come in the usual way. A rational function crosses the x-axis wherever the **numerator** is zero (and the denominator isn't), and crosses the y-axis at $f(0)$ whenever that value is defined.

---

## Example 1: a basic asymptote hunt

> Describe the graph of $f(x) = \dfrac{x + 2}{x - 3}$. Find all asymptotes, intercepts, and holes.

**Vertical asymptote.** Set the denominator equal to zero: $x - 3 = 0 \Rightarrow x = 3$. Check the numerator at $x = 3$: $3 + 2 = 5 \neq 0$. Since the bottom is zero and the top isn't, this is a true vertical asymptote. The graph has a wall at $x = 3$.

**Horizontal asymptote.** Degree of the top is $1$, degree of the bottom is $1$, so the degrees are tied. The leading coefficient on top is $1$ and on the bottom is also $1$, so the horizontal asymptote is $y = 1 / 1 = 1$.

**Holes.** For a hole, we'd need the same x-value to make both top and bottom zero. Top is zero at $x = -2$; bottom is zero at $x = 3$. Different values, so no holes — just the asymptote.

**x-intercept.** Set the numerator to zero: $x + 2 = 0 \Rightarrow x = -2$. The graph crosses the x-axis at $(-2, 0)$.

**y-intercept.** $f(0) = (0 + 2)/(0 - 3) = -2/3$. The graph crosses the y-axis at $(0, -2/3)$.

With those four facts, sketching the curve becomes guided drawing: two branches, one on each side of the vertical wall at $x = 3$, both approaching $y = 1$ far from the wall, with the left branch passing through the two intercepts on its way out to the horizontal asymptote.

---

## Example 2: a hole hiding inside a rational function

> Describe the graph of $f(x) = \dfrac{x^2 - 4}{x - 2}$.

Factor the numerator: $x^2 - 4 = (x - 2)(x + 2)$. So

$$
f(x) = \dfrac{(x - 2)(x + 2)}{x - 2}.
$$

The factor $(x - 2)$ cancels **everywhere except at $x = 2$**, where the original expression is undefined. The simplified function is $f(x) = x + 2$, which is a straight line with slope $1$ and y-intercept $2$. But because the original expression couldn't be evaluated at $x = 2$, the graph of the original $f$ is that same line with a **hole** punched at the point $(2, 4)$ (since $2 + 2 = 4$).

So the final picture is the line $y = x + 2$, drawn normally, with an open circle at $(2, 4)$ to mark the hole. There's no asymptote at all — the problem children of rational functions can vanish when the cancellation works out just right.

---

## Example 3: horizontal asymptote from matching degrees

> Find the horizontal asymptote of $f(x) = \dfrac{3x^2 + x - 4}{5x^2 - 7}$.

The degree of the top is $2$, and the degree of the bottom is $2$. They match, so the horizontal asymptote is determined by the leading coefficients: $y = 3/5$.

You can see why with a quick "dominant term" argument. For very large $|x|$, the $x$ and constants become insignificant next to $x^2$. So $f(x)$ behaves approximately like $3x^2 / 5x^2 = 3/5$ when $x$ is very far from zero.

That means both ends of the graph will flatten out toward $y = 0.6$ — approaching but never quite reaching that horizontal line. The graph may wiggle above or below the asymptote in between, but its long-term destiny is that horizontal line.

---

## Common pitfalls

- **Declaring a vertical asymptote before checking for cancellation.** Always factor the numerator and denominator first. If a factor cancels, you get a hole, not an asymptote.
- **Assuming the graph never crosses the horizontal asymptote.** It can't cross near the edges of the picture, but it's allowed to cross in the middle. Horizontal asymptotes describe end behavior, not global behavior.
- **Forgetting to test the numerator at the candidate x-value.** Zero in the denominator is only half the story — you also need the numerator to be nonzero for a true asymptote.
- **Reading off the wrong leading coefficients when degrees match.** Use only the highest-degree coefficient from each polynomial. Lower-degree terms become irrelevant at infinity.

---

## Prerequisites

- [[Simplifying_Rational_Expressions]] — the factor-and-cancel moves are exactly what you need to find holes
- [[Factoring_Trinomials_Leading_Coefficient_1]] — so you can factor both the numerator and the denominator quickly
- [[Function_Basics]] — domain, range, and function notation

---

## Problems Involving Graphing Rational Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="graphing_rational_functions_part_1"></div>

---

## See Also

- [[Graphing_Rational_Functions_Part_2]] — slant asymptotes and full sign analysis
- [[Simplifying_Rational_Expressions]] — prerequisite for every rational graph
- [[Introduction_To_Rational_Functions]] — the pre-calculus overview of the whole topic
- [[Polynomial_Functions_And_Graphs]] — the polynomial-only cousin
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
