---
title: "Inverse Functions"
type: topic
aliases: ["Inverse Function", "InverseFunctions", "f inverse"]
tags: ["#branch-algebra-2", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.1"}
  - {book: "algtrig", chapter: "5", section: "5.3"}
related:
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Arithmetic_And_Composition"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Square_Root_Functions"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Exponential_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Arithmetic_And_Composition"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "The inverse function f^(-1) undoes f; it exists exactly when f is one-to-one, and its graph is f reflected across y = x."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Inverse Functions

# Inverse Functions

Every function is a machine: feed it an input, read off an output. The **inverse** of a function is the machine that runs the tape backwards. If the original sent $3$ to $11$, the inverse sends $11$ back to $3$. If it sent $-2$ to $4$, the inverse sends $4$ back to $-2$. The two machines undo each other, so stringing them together gives you back exactly what you started with.

We write the inverse of $f$ as $f^{-1}$, read "f-inverse". That little $-1$ is a label, not a power. It does **not** mean $\dfrac{1}{f(x)}$ and it does not mean a reciprocal of any kind — it is just the traditional symbol for "the function that undoes $f$". A common beginner mistake is to see $f^{-1}(5)$ and compute $\dfrac{1}{f(5)}$. Wrong notation, wrong number, wrong habit.

Formally, two functions $f$ and $g$ are inverses of each other when both compositions collapse to the identity:

$$
f^{-1}(f(x)) = x \quad \text{and} \quad f(f^{-1}(x)) = x.
$$

The first equation says: run the tape forward, then run it back, and you land where you started. The second says the same thing the other way around. Either check alone is not enough — you need both compositions to behave — but once both do, $f$ and $f^{-1}$ are genuinely inverses.

---

## Key ideas

- **Swap the roles of input and output.** Inverses trade domains for ranges. If $f$ takes in a temperature in Celsius and returns a temperature in Fahrenheit, then $f^{-1}$ takes in Fahrenheit and returns Celsius. Everywhere the original function mapped $a \to b$, the inverse maps $b \to a$.
- **Algebraic recipe.** To compute the inverse of a rule written as an equation: (1) write the rule as $y = f(x)$, (2) exchange every $x$ with every $y$, (3) re-solve the new equation for $y$, and (4) rename that $y$ as $f^{-1}(x)$. That procedure literally encodes "what input produces a given output?".
- **Not every function has an inverse.** If two different inputs ever share the same output, the reversal breaks down — the output has no unique input to return to. A function whose inverse exists is called **one-to-one**: distinct inputs always give distinct outputs. Symbolically, $f(a) = f(b)$ forces $a = b$.
- **The horizontal line test.** A function's graph is one-to-one exactly when no horizontal line ever touches the graph in more than one place. Vertical lines (from the vertical line test) check that you have a function at all; horizontal lines check whether that function is reversible.
- **Graphs reflect across $y = x$.** Plot $f$ and $f^{-1}$ on the same axes and the two curves are mirror images across the $45^\circ$ line. If $(a, b)$ is a point on $f$, then $(b, a)$ is the corresponding point on $f^{-1}$. This visual check is the quickest way to spot a mistake in an algebraic inverse.
- **Domain and range swap.** The domain of $f^{-1}$ equals the range of $f$, and the range of $f^{-1}$ equals the domain of $f$. Whenever you state an inverse, you may also need to restate the set of inputs it will accept.

---

## Restricting the domain to force invertibility

Some of the most useful functions — $f(x) = x^2$, $f(x) = |x|$, and all of the trigonometric functions — are **not** one-to-one over their natural domain. They fail the horizontal line test somewhere. For $f(x) = x^2$, the horizontal line $y = 9$ hits the parabola at both $x = 3$ and $x = -3$, so there is no single "input that produces $9$" to hand back.

The trick is surgical: chop off part of the domain so that what remains is one-to-one. If we restrict $f(x) = x^2$ to $x \geq 0$, the left branch of the parabola is gone, the horizontal line test succeeds, and the inverse is well defined: $f^{-1}(x) = \sqrt{x}$ on $[0, \infty)$. That is exactly the relationship from [[Square_Root_Functions]]. This restriction idea is how algebra-2 gets square roots from squaring, how calculus gets arcsine from sine, and how [[Logarithmic_Functions|logarithms]] come out of [[Exponential_Functions|exponentials]] — each inverse is born by carving the original function down until it becomes one-to-one.

---

## Example 1: inverting a linear function

> Let $f(x) = 3x - 5$. What is $f^{-1}(x)$, and does the composition check confirm the answer?

Start by writing the rule as an equation in $x$ and $y$:

$$
y = 3x - 5.
$$

Swap the names of the variables. Every $x$ becomes a $y$ and every $y$ becomes an $x$:

$$
x = 3y - 5.
$$

Now rearrange to isolate $y$. Add $5$ to both sides:

$$
x + 5 = 3y.
$$

Divide by $3$:

$$
y = \dfrac{x + 5}{3}.
$$

So the candidate inverse is $f^{-1}(x) = \dfrac{x + 5}{3}$. To be sure, run both compositions. Forward then back:

$$
f^{-1}(f(x)) = \dfrac{(3x - 5) + 5}{3} = \dfrac{3x}{3} = x.
$$

Back then forward:

$$
f(f^{-1}(x)) = 3 \cdot \dfrac{x + 5}{3} - 5 = (x + 5) - 5 = x.
$$

Both compositions collapse to $x$, so the two functions are genuine inverses. A linear function is always one-to-one when its slope is nonzero, so there is no domain restriction to worry about here.

---

## Example 2: inverting a quadratic — the domain-restriction move

> Sketch why $f(x) = x^2$ has no inverse over the whole real line, then find the inverse of the restricted function $f(x) = x^2$ with domain $x \geq 0$.

Over all real numbers, $f(x) = x^2$ sends both $4$ and $-4$ to $16$. A horizontal line at $y = 16$ pierces the parabola twice. That is the graphical version of the failure: there is no single rule that can send $16$ back home, because home could be either $4$ or $-4$.

Now restrict the domain. We only accept inputs $x \geq 0$. That kills the left branch of the parabola, leaves the right branch alone, and the remaining curve is strictly increasing — no horizontal line can ever cross it twice. The restricted function is one-to-one, so it has an inverse.

Find the rule the usual way. Start from $y = x^2$, swap variables:

$$
x = y^2.
$$

Solve for $y$. Taking the square root gives two candidates, $y = \sqrt{x}$ and $y = -\sqrt{x}$. Which one is correct? The outputs of the inverse must come from the domain of the original, and that domain is $y \geq 0$. So we keep the nonnegative root:

$$
f^{-1}(x) = \sqrt{x}, \qquad x \geq 0.
$$

If instead we had restricted the original to $x \leq 0$ — keeping the left branch of the parabola — the inverse would be $f^{-1}(x) = -\sqrt{x}$. Both choices are legitimate; what matters is that you pick one branch and stay on it.

---

## Example 3: applying the horizontal line test

> Which of the following functions are invertible on their full natural domain? (a) $f(x) = 2x + 7$, (b) $g(x) = x^2 - 4$, (c) $h(x) = x^3$, (d) $k(x) = |x - 2|$.

Imagine sliding a horizontal ruler up and down each graph and counting how many times it meets the curve.

**(a)** The line $y = 2x + 7$ is a straight, non-horizontal line. Any horizontal ruler crosses it exactly once. One-to-one, so $f^{-1}$ exists.

**(b)** The parabola $g(x) = x^2 - 4$ opens upward with vertex $(0, -4)$. Any horizontal ruler above $y = -4$ meets the parabola at two points (one on each side of the axis of symmetry). Not one-to-one. No inverse without first restricting the domain to, say, $x \geq 0$.

**(c)** The curve $h(x) = x^3$ is strictly increasing — it never flattens out and never turns around. Every horizontal ruler crosses it exactly once. One-to-one, so $h^{-1}$ exists. In fact $h^{-1}(x) = \sqrt[3]{x}$, and no domain restriction is needed because cubing preserves sign.

**(d)** The V-shaped graph of $k(x) = |x - 2|$ has its corner at $(2, 0)$. Any horizontal ruler above $y = 0$ hits both branches of the V, so $k$ fails the test. See [[Absolute_Value_Functions]] for the full anatomy of the V-shape and the domain restriction that makes it invertible.

---

## Common pitfalls

- **Reading $f^{-1}$ as a reciprocal.** The notation looks like a power, but it is not. $f^{-1}(x)$ is "the function that undoes $f$", while $\dfrac{1}{f(x)}$ is genuine division. They are almost never equal.
- **Checking only one composition.** Both $f(f^{-1}(x)) = x$ and $f^{-1}(f(x)) = x$ must hold. Verifying only one direction can hide an error, especially when the domains are restricted.
- **Forgetting the domain of the inverse.** Whenever you restrict the domain of the original to force invertibility (as with $x^2$), the inverse inherits a matching range restriction. State it explicitly or you will get wrong answers later.
- **Trying to invert a many-to-one function as if it were reversible.** If you forget to run the horizontal line test first, you can produce an algebraic rule that looks like an inverse but is not actually a function. The clue is usually a $\pm$ appearing in your work.
- **Mis-reading signs when swapping variables.** Going from $y = 3x - 5$ to $x = 3y - 5$ trips students up because it feels like a relabeling. Slow down: every $x$ must be replaced by $y$, and every $y$ must be replaced by $x$.

---

## Prerequisites

Make sure these are comfortable before you practice:

- [[Relations_And_Functions]] — what a function is, and why "one input, one output" is the whole story
- [[Function_Basics]] — notation, domain, range, and reading graphs
- [[Function_Arithmetic_And_Composition]] — composition $f(g(x))$ is the tool we use to verify inverses
- [[Multi_Step_Equations]] — you will need to solve for $y$ after swapping variables

---

## Problems Involving Inverse Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="inverse_functions"></div>

---

## See Also

- [[Function_Arithmetic_And_Composition]]
- [[Square_Root_Functions]]
- [[Quadratic_Functions]]
- [[Logarithmic_Functions]]
- [[Exponential_Functions]]
- [[Relations_And_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
