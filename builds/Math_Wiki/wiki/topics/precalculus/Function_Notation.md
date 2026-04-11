---
title: "Function Notation"
type: topic
aliases: ["Function Notation", "f of x", "f(x)"]
tags: ["#branch-pre-calculus", "#topic-functions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "1", section: "1.3"}
  - {book: "math_2", chapter: "9", section: "9.2"}
related:
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Function_Arithmetic_And_Composition"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Relations_And_Functions"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Evaluating_Expressions"
problem_type_ids: []
figures: []
summary: "The symbol f(x) is a naming system for function outputs — read it as 'f at x', never as multiplication."
---

> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Function Notation

# Function Notation

When a function shows up in a sentence, mathematicians reach for a very compact piece of shorthand. Instead of writing "the output of the rule named $f$ when its input is $x$," they simply write $f(x)$. It looks like multiplication but is not — the parentheses are doing a different job entirely. They mark the slot where the input goes.

$$
f(x) \;\longleftarrow\; \text{the output of } f \text{ when the input is } x
$$

Read aloud, $f(x)$ is spoken as **"f at x"** or **"the value of f at x."** Some people say "f of x," which is also fine, but that phrasing is the one students most often mishear as "f times x." It is not multiplication. The $f$ is a name; the parentheses hold whatever you plan to feed in.

---

## Key ideas

**The function name and the input name are independent.** The letter in front — $f$, $g$, $h$, $p$, $\varphi$ — is the name of the machine. The letter inside the parentheses is just a placeholder for a number. Writing $f(t) = 2t + 5$ describes the same function as $f(x) = 2x + 5$; the $t$ is simply reminding you that the input might represent time. You can change the placeholder to anything you like without changing the function at all.

**To evaluate, you substitute.** Whenever you see something inside the parentheses of a function, erase every copy of the placeholder in the rule and replace it with whatever was supplied. If the rule is $f(x) = x^2 - 2x + 4$ and someone asks for $f(3)$, rewrite the rule with $3$ wherever $x$ used to live: $f(3) = 3^2 - 2(3) + 4 = 9 - 6 + 4 = 7$. Keep the new input wrapped in parentheses during the substitution step — it protects negative signs and expressions.

**Function notation eats more than numbers.** The input slot is happy to swallow a variable, a negative, a sum, a product, or another entire expression. If $f(x) = x^2 + 1$, then $f(a)$ equals $a^2 + 1$, and $f(x + h)$ equals $(x + h)^2 + 1$. The procedure is always the same: drop whatever is inside the parentheses into every appearance of $x$ in the rule, then simplify.

**Multiple function names work in parallel.** A problem can use $f$, $g$, and $h$ side by side to describe three different rules. This lets you compare outputs, combine them, or describe cause-and-effect relationships. For instance, if $C(x)$ gives the cost of producing $x$ items and $p(x)$ gives the price per item, you can talk about both in the same sentence without confusion.

**Reversing the question.** Sometimes the task is not "given the input, find the output" but the opposite: "given the output, find the input." In symbols, that means solving $f(x) = 7$ for $x$ — set the rule equal to $7$ and solve the resulting equation with the usual algebra tools.

---

## Example 1: plugging in plain numbers

> Let $f(x) = 3x^2 - 5x + 1$. Work out $f$ at $x = 0$, $x = 2$, and $x = -1$.

Every evaluation is the same three-step routine: copy the rule, replace $x$ with the new input (in parentheses), then simplify.

For $f(0)$:

$$
f(0) = 3(0)^2 - 5(0) + 1 = 0 - 0 + 1 = 1
$$

For $f(2)$:

$$
f(2) = 3(2)^2 - 5(2) + 1 = 3(4) - 10 + 1 = 12 - 10 + 1 = 3
$$

For $f(-1)$ — pause carefully on the signs. The input $-1$ stays inside parentheses so that $(-1)^2$ correctly comes out as $+1$:

$$
f(-1) = 3(-1)^2 - 5(-1) + 1 = 3(1) + 5 + 1 = 9
$$

So $f(0) = 1$, $f(2) = 3$, $f(-1) = 9$. Notice how the protective parentheses around $-1$ stop the squaring from flipping into a sign mistake.

---

## Example 2: the input is an expression

> Let $g(t) = t^2 + 4t$. Find and simplify $g(a + 3)$.

This is where function notation really starts to earn its keep. The variable name inside the parentheses is just a symbol standing for the input, so we can hand it an entire expression. Replace every $t$ in the rule with $(a + 3)$ — keeping the new input in parentheses protects against sign errors and expansion errors:

$$
g(a + 3) = (a + 3)^2 + 4(a + 3)
$$

Expand the square and distribute:

$$
= a^2 + 6a + 9 + 4a + 12
$$

Combine like terms:

$$
= a^2 + 10a + 21
$$

So $g(a + 3) = a^2 + 10a + 21$. The same method works for any expression you can write. Ask for $g(2x)$ and you would replace $t$ with $(2x)$ to get $g(2x) = (2x)^2 + 4(2x) = 4x^2 + 8x$. The rule does not care what shape the input has; it just follows the recipe.

---

## Example 3: the difference quotient (a preview of calculus)

> Let $f(x) = x^2 - 3x$. Find and simplify the difference quotient $\dfrac{f(x + h) - f(x)}{h}$.

This strange-looking ratio is the most important expression in all of pre-calculus. It asks: how much does the output of $f$ change when the input moves from $x$ to a nearby point $x + h$, measured per unit of $h$? When $h$ is tiny, that ratio tells you how fast $f$ is changing near $x$ — which is exactly the question calculus is about to answer with the word **derivative**. For now, the goal is purely algebraic: compute the two pieces, subtract, and cancel the $h$ out of the denominator.

**Step 1. Compute $f(x + h)$.** Replace every $x$ in the rule with $(x + h)$:

$$
f(x + h) = (x + h)^2 - 3(x + h)
$$

Expand:

$$
= x^2 + 2xh + h^2 - 3x - 3h
$$

**Step 2. Subtract $f(x)$.** We have $f(x) = x^2 - 3x$, so the numerator of the difference quotient is:

$$
f(x + h) - f(x) = \bigl(x^2 + 2xh + h^2 - 3x - 3h\bigr) - \bigl(x^2 - 3x\bigr)
$$

Distribute the minus sign and cancel matching terms. The $x^2$ cancels an $-x^2$, and the $-3x$ cancels a $+3x$:

$$
= 2xh + h^2 - 3h
$$

**Step 3. Divide by $h$.** Factor an $h$ out of every term and cancel:

$$
\frac{f(x + h) - f(x)}{h} = \frac{2xh + h^2 - 3h}{h} = \frac{h(2x + h - 3)}{h} = 2x + h - 3
$$

So the simplified difference quotient is $2x + h - 3$. The magic is that the $h$ in the denominator — which would make the expression undefined at $h = 0$ — has cancelled. If you now imagine letting $h$ shrink to zero, the answer settles onto $2x - 3$. That is your first glimpse of the derivative of $x^2 - 3x$, and it is the whole reason function notation exists in the form it does.

---

## Common pitfalls

- **Reading $f(x)$ as a product.** The parentheses are a slot, not a multiplication symbol. $f(3)$ does not mean "$f$ times $3$." It means "evaluate the rule named $f$ using $3$ as the input." This is the single most common misreading in the course.
- **Dropping parentheses around a negative input.** When you substitute $-2$ into $f(x) = x^2 + 5x$, write $f(-2) = (-2)^2 + 5(-2)$, not $-2^2 + 5 \cdot -2$. Without the parentheses, $-2^2$ becomes $-(2^2) = -4$ instead of the correct $+4$.
- **Forgetting to replace every $x$.** The substitution rule is strict: if the placeholder appears three times in the formula, all three copies have to be swapped for the new input, not just one or two.
- **Confusing the function name with the variable name.** In $f(t) = 2t + 5$, the function is $f$, not $t$. Changing the placeholder to $x$ does not give you a new function. Changing the rule (say, to $2t^2 + 5$) does.

---

## Prerequisites

Before working through practice problems, you should be comfortable with:

- [[Relations_And_Functions]] — what a function is and why the vertical-line test matters
- [[Function_Basics]] — domain, range, and the input-output picture
- [[Evaluating_Expressions]] — plugging numbers into algebraic formulas and simplifying carefully

Function notation is essentially [[Evaluating_Expressions|evaluation]] dressed in new clothes — if that skill is solid, everything on this page falls into place.

---

## Problems Involving Function Notation

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="function_notation"></div>

---

## See Also

- [[Relations_And_Functions]]
- [[Function_Basics]]
- [[Linear_Functions]]
- [[Function_Arithmetic_And_Composition]]
- [[Inverse_Functions]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
