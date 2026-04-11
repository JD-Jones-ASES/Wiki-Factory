---
title: "Function Arithmetic and Composition"
type: topic
aliases: ["Function Composition", "Function Arithmetic", "Composite Functions", "Combining Functions"]
tags: ["#branch-algebra-2", "#topic-functions", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "4", section: "4.4"}
  - {book: "algtrig", chapter: "5", section: "5.2"}
  - {book: "algtrig", chapter: "1", section: "1.2"}
related:
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Notation"
  - "topics/algebra/Inverse_Functions"
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Linear_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Function_Basics"
  - "topics/precalculus/Function_Notation"
  - "topics/algebra/Evaluating_Expressions"
  - "topics/algebra/Multiplying_Polynomials"
problem_type_ids: []
figures: []
summary: "Adding, subtracting, multiplying, dividing, and chaining functions — plus why order matters when you chain."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Function Arithmetic and Composition

# Function Arithmetic and Composition

Once you have more than one function on the table, two natural questions arise. The first is arithmetic: can I add two functions, or multiply them, the way I would combine two expressions? The second is chaining: what happens if I pipe the output of one function straight into another? Both ideas are essential, and both have their own notation.

$$
(f + g)(x) = f(x) + g(x) \qquad (f \circ g)(x) = f(g(x))
$$

The left-hand rule says "do the two functions separately, then combine their outputs." The right-hand rule is different in spirit — it says "run the input through $g$ first, and then feed whatever came out into $f$." These are two very different operations, and a huge part of this lesson is keeping them straight.

---

## Part 1: arithmetic on functions

Given any two functions $f$ and $g$ whose domains share some values, you can form four new functions by combining their outputs pointwise:

$$
\begin{aligned}
(f + g)(x) &= f(x) + g(x) \\
(f - g)(x) &= f(x) - g(x) \\
(f \cdot g)(x) &= f(x) \cdot g(x) \\
\left(\tfrac{f}{g}\right)(x) &= \dfrac{f(x)}{g(x)}
\end{aligned}
$$

The idea is mechanical — whatever you can do to two numbers, you can do to two function outputs. A subtle point hides inside all four definitions: the new function is only legal at inputs where both $f(x)$ and $g(x)$ are defined. That means the domain of $f + g$, $f - g$, and $f \cdot g$ is the overlap of the two individual domains. For the quotient $f/g$, you also have to throw out every $x$ where $g(x) = 0$, because a fraction with a zero denominator is undefined.

**Domain intersection in plain English.** If $f$ requires $x \geq 0$ and $g$ requires $x \neq 3$, then every combination of the two requires both conditions at once: $x \geq 0$ *and* $x \neq 3$. Take the more restrictive of the two at every step.

---

## Part 2: composition

Composition is the other way to combine functions, and it is the star of this topic. The symbol for composition is a little open circle:

$$
(f \circ g)(x) = f(g(x))
$$

Read the left side as **"f composed with g, evaluated at x."** The recipe on the right tells you what to do: first run $x$ through $g$, record the output, then run *that* number through $f$. The little circle is a kind of arrow pointing in the direction of the data flow. If you think of each function as a black box, $f \circ g$ is the result of wiring the output port of $g$ directly into the input port of $f$.

**Domain of a composition.** For $(f \circ g)(x)$ to make sense, two things must happen. First, $x$ has to be a legal input for $g$. Second, whatever $g$ spits out has to be a legal input for $f$. So the domain of the composition is the set of $x$ values where both stages succeed — and that can be smaller than either domain alone. For example, if $g$ produces negatives but $f$ only accepts non-negatives, the combined machine will only work on inputs where $g(x) \geq 0$.

**Order of operations, literally.** Inside $(f \circ g)(x)$, the function closest to the $x$ is the one that acts first. Work from the inside out: $g$ first, then $f$. Students often reverse this, reading left-to-right and applying $f$ before $g$, which is wrong.

---

## Part 3: the headline rule — composition is not commutative

Here is the single most important takeaway on this page:

$$
(f \circ g)(x) \neq (g \circ f)(x) \quad \text{in general.}
$$

Swapping the order of composition typically gives you an entirely different function. This is very different from ordinary arithmetic, where $3 + 5 = 5 + 3$ and $3 \cdot 5 = 5 \cdot 3$. Addition and multiplication of functions *are* commutative — if you pick a point $x$ and compute $(f + g)(x)$ versus $(g + f)(x)$, the two numbers match because ordinary addition is commutative. But composition? Not even close. If you doubt it, example 3 below will show you a concrete case where $(f \circ g)(2)$ and $(g \circ f)(2)$ come out to two very different numbers.

Why does the order matter so much? Because composition is not combining two outputs — it is routing the data through a specific pipeline. "Double it, then add one" is a genuinely different procedure from "add one, then double it," and the two pipelines produce different final values at almost every starting point.

---

## Example 1: adding, multiplying, and evaluating

> Let $f(x) = 2x - 1$ and $g(x) = x^2 + 3$. Build $(f + g)(x)$ and $(f \cdot g)(x)$ as simplified expressions, then evaluate $(f + g)(4)$.

**Sum.** By the rule, $(f + g)(x) = f(x) + g(x)$. Write both formulas and add:

$$
(f + g)(x) = (2x - 1) + (x^2 + 3) = x^2 + 2x + 2
$$

Both $f$ and $g$ are polynomials, so each has domain all real numbers; the sum has domain all real numbers too.

**Product.** Multiply the two expressions using the distributive property:

$$
(f \cdot g)(x) = (2x - 1)(x^2 + 3) = 2x^3 + 6x - x^2 - 3 = 2x^3 - x^2 + 6x - 3
$$

Notice that adding two functions produced another polynomial of the same degree as the bigger of the two, while multiplying produced a polynomial of higher degree. Function arithmetic often changes the character of what you started with.

**Evaluation.** For $(f + g)(4)$, you have two equivalent roads. You can use the simplified formula: $(f + g)(4) = 4^2 + 2(4) + 2 = 16 + 8 + 2 = 26$. Or you can evaluate each piece and add: $f(4) = 2(4) - 1 = 7$, $g(4) = 4^2 + 3 = 19$, and $7 + 19 = 26$. Both paths give the same answer, which is a useful sanity check.

---

## Example 2: a composition as a formula

> Let $f(x) = x^2 + 1$ and $g(x) = 2x - 3$. Find a simplified formula for $(f \circ g)(x)$, then evaluate it at $x = 4$.

Work from the inside out. Start by writing what the composition means:

$$
(f \circ g)(x) = f(g(x)) = f(2x - 3)
$$

The placeholder in $f$'s rule is $x$; replace every copy of that placeholder with the entire expression $2x - 3$:

$$
f(2x - 3) = (2x - 3)^2 + 1
$$

Expand the square. Careful — $(2x - 3)^2$ is $(2x - 3)(2x - 3)$, not $4x^2 + 9$:

$$
= 4x^2 - 12x + 9 + 1 = 4x^2 - 12x + 10
$$

So $(f \circ g)(x) = 4x^2 - 12x + 10$. To evaluate at $x = 4$, plug in: $4(4)^2 - 12(4) + 10 = 64 - 48 + 10 = 26$.

As a double-check, step through the composition one piece at a time. First $g(4) = 2(4) - 3 = 5$. Then $f(5) = 5^2 + 1 = 26$. Matches.

---

## Example 3: non-commutativity with real numbers

> Let $f(x) = 3x + 2$ and $g(x) = x^2$. Compute $(f \circ g)(2)$ and $(g \circ f)(2)$ and compare.

**First composition: $(f \circ g)(2)$.** Start from the inside. The function $g$ acts first, so $g(2) = 2^2 = 4$. Now feed that $4$ into $f$:

$$
(f \circ g)(2) = f(g(2)) = f(4) = 3(4) + 2 = 14
$$

**Second composition: $(g \circ f)(2)$.** This time $f$ acts first. Start by finding $f(2) = 3(2) + 2 = 8$. Now feed $8$ into $g$:

$$
(g \circ f)(2) = g(f(2)) = g(8) = 8^2 = 64
$$

**The verdict.** $(f \circ g)(2) = 14$ and $(g \circ f)(2) = 64$. These are not equal. Not even close. Swapping the order of composition turned $14$ into $64$ at the same input — a concrete, undeniable demonstration that composition depends on order. If you were to compute the two full formulas, you would find $(f \circ g)(x) = 3x^2 + 2$ and $(g \circ f)(x) = (3x + 2)^2 = 9x^2 + 12x + 4$, and those are genuinely different functions, not just two names for the same thing.

The moral: whenever you see $(f \circ g)$, check which function is on the right side of the circle. That one runs first. Mixing up the order is the single most common mistake in every problem on this topic, so slow down and draw a little arrow reminding yourself of the direction if it helps.

---

## Common pitfalls

- **Reading composition left-to-right.** In $(f \circ g)(x)$, the function on the right — $g$ — acts first. The circle is read inside-out, not left-to-right. Many students flip the order and get the wrong answer.
- **Confusing $(f \cdot g)(x)$ with $(f \circ g)(x)$.** Multiplication of functions uses a dot or no symbol and combines outputs at the same input: $f(x) \cdot g(x)$. Composition uses the little circle and pipes one output into the next function: $f(g(x))$. These produce very different formulas.
- **Losing the domain restrictions.** When you simplify a composition, the answer can look cleaner than the original and suggest a larger domain than is really legal. Always look at the unsimplified composite before declaring a domain — if $g$ excludes $x = 3$, then $(f \circ g)$ also excludes $x = 3$ even if the simplified formula hides that restriction.
- **Forgetting to exclude zeros of the denominator in a quotient.** For $(f/g)(x)$, every $x$ where $g(x) = 0$ must be removed from the domain, on top of the usual domain intersection.
- **Assuming composition is commutative.** It is not. $(f \circ g)$ and $(g \circ f)$ are almost always two different functions. Treat them as separate objects.

---

## Prerequisites

Before practicing these problems, be sure you are comfortable with:

- [[Function_Basics]] — domain, range, and the input-output picture
- [[Function_Notation]] — reading and evaluating $f(x)$ correctly
- [[Evaluating_Expressions]] — substituting one expression into another and simplifying
- [[Multiplying_Polynomials]] — expanding squares, distributing, collecting like terms

Composition, in particular, is essentially the skill of substituting an expression in place of $x$. If that move feels fluent, composition is just the same skill with new symbols around it.

---

## Problems Involving Function Arithmetic and Composition

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="function_arithmetic_and_composition"></div>

---

## See Also

- [[Function_Basics]]
- [[Function_Notation]]
- [[Linear_Functions]]
- [[Inverse_Functions]]
- [[Relations_And_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
