---
title: "Evaluating Expressions"
type: topic
aliases: ["Evaluate an Expression", "Substitution"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "8", section: "8.2"}
related:
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Simplifying_Expressions"
  - "topics/pre_algebra/Translating_Words_To_Algebraic_Expressions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "Substitute numbers for variables, then simplify using order of operations."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Evaluating Expressions

# Evaluating Expressions

An algebraic expression like $2x + 5$ is a recipe waiting for an ingredient. Once you are told what $x$ is, the recipe produces a single number. The process of plugging in that ingredient and cooking the number down is called **evaluating** the expression.

This is the everyday workhorse of algebra. Every time you use a formula — area of a rectangle, miles per hour, a phone-bill calculation — you are evaluating an expression. The steps are small, but one careless sign can turn the right answer into the wrong one, so the habits you build here will pay off for years.

---

## What it means

To **evaluate** an expression, you replace each variable with its given value and then simplify the arithmetic that remains. The variable is a placeholder; evaluation is the act of filling the placeholder in and collapsing the expression down to a single number.

A few vocabulary reminders from [[Variables_And_Algebraic_Expressions]]:

- A **variable** is a letter that stands for a number.
- An **expression** is a combination of numbers, variables, and operations with no equals sign.
- A **formula** is just an expression (or an equation) named for the quantity it computes, like $A = \ell w$ for the area of a rectangle.

Evaluating works the same way whether the expression is tiny ($2x$) or long ($3a^2 - 2b + 7$).

---

## The rule

Three steps, in this order, every time:

1. **Write the expression down** exactly as it appears.
2. **Substitute** the given value for each variable. Wrap each substituted value in parentheses. Always.
3. **Simplify** what remains using the [[Order_Of_Operations|order of operations]] (PEMDAS).

The parentheses in step 2 are not decoration. They keep negative signs and exponents from colliding, and they keep implied multiplication (like $3x$ meaning $3 \cdot x$) visible after the variable disappears.

---

## Why it works

A variable is a name for a number we have not committed to yet. When we pick a value, the expression is no longer abstract — it is a specific calculation. Order of operations is what guarantees that every person who evaluates the same expression with the same input lands on the same output. Without that shared convention, $2 + 3 \cdot 4$ could mean either $20$ or $14$, and formulas would be useless.

Parentheses during substitution are a safety rail. If $x = -3$ and the expression contains $x^2$, writing $-3^2$ gives $-9$ because the exponent binds tighter than the negative sign. Writing $(-3)^2$ gives the correct $9$, because now the parentheses tell the exponent to apply to the whole signed number. One little habit — always use parentheses when substituting — eliminates a class of bugs that otherwise haunts students for years.

---

## Worked examples

### Example 1: A simple linear expression

> Evaluate $2x + 5$ when $x = 4$.

Start by writing the expression, then substitute $(4)$ for $x$:

$$
2x + 5 = 2(4) + 5
$$

Multiply first, then add:

$$
2(4) + 5 = 8 + 5 = 13
$$

So when $x = 4$, the expression is worth $13$.

### Example 2: A negative value with an exponent

> Evaluate $3a^2 - 2b$ when $a = -2$ and $b = 5$.

Substitute both values. Notice the parentheses around $-2$ — this is the critical move:

$$
3a^2 - 2b = 3(-2)^2 - 2(5)
$$

Work through the order of operations. Exponents come before multiplication, so deal with $(-2)^2$ first:

$$
3(-2)^2 - 2(5) = 3(4) - 2(5)
$$

Now the two multiplications:

$$
3(4) - 2(5) = 12 - 10
$$

Finally the subtraction:

$$
12 - 10 = 2
$$

The value of the expression at $a = -2$, $b = 5$ is $2$.

What would have gone wrong without the parentheses? If you wrote $3 \cdot -2^2$, the exponent would grab only the $2$, giving $-4$, and the whole answer would come out wrong. The parentheses kept the negative sign tied to the base being squared.

### Example 3: A fraction bar groups the numerator

> Evaluate $\dfrac{a + b}{2}$ when $a = 7$ and $b = 11$.

Substitute, remembering that the fraction bar behaves like a pair of grouping symbols around the numerator:

$$
\frac{a + b}{2} = \frac{(7) + (11)}{2}
$$

Simplify the numerator first, then divide:

$$
\frac{7 + 11}{2} = \frac{18}{2} = 9
$$

Notice that you had to add before you divided, even though division normally comes first — the bar forces the addition to happen inside its implicit parentheses. This is the same expression that computes the average of two numbers, so the answer, $9$, is the midpoint of $7$ and $11$.

---

## Common mistakes

- **Dropping parentheses around a negative value.** $-4^2$ is $-16$, but $(-4)^2$ is $16$. If you substitute a negative number without parentheses, exponents bite you.
- **Ignoring implied multiplication.** The expression $3x$ means $3 \cdot x$. After substitution you must write $3(5)$, not $35$. Forgetting this turns $3x$ at $x = 5$ into the number thirty-five instead of fifteen.
- **Doing operations out of order.** The order of operations is not optional. Multiplication before addition, exponents before multiplication, grouping symbols before everything else.
- **Swapping variables.** In $3a^2 - 2b$, the $a$ and $b$ are not interchangeable. Replacing $a$ with $b$'s value (or vice versa) is easy to do in a hurry and hard to catch later.
- **Forgetting the fraction bar groups.** The bar acts like a parenthesis around the whole top and the whole bottom. Work each side out completely before you divide.

---

## Prerequisites

Before you practice evaluation problems, make sure you are solid on:

- [[Variables_And_Algebraic_Expressions]] — what a variable is and what an expression looks like.
- [[Order_Of_Operations]] — PEMDAS, because step 3 of the rule above leans on it entirely.

If either of those feels unsteady, start there and come back.

---

## Problems Involving This Topic

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections stay in this browser. When you are ready, open your [[Vault]] to see them all, view hints and answers, and print a worksheet.

<div class="problem-vault-widget" data-topic-slug="evaluating_expressions"></div>

_More problem types are coming soon._

## See also

- [[Variables_And_Algebraic_Expressions]]
- [[Order_Of_Operations]]
- [[The_Distributive_Property]]
- [[Simplifying_Expressions]]
- [[Translating_Words_To_Algebraic_Expressions]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]

## Sources in the 

- **Math I** — Chapter 8, Section 8.2: Evaluating Expressions
