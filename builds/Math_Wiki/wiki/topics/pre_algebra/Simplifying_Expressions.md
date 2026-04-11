---
title: "Simplifying Expressions"
type: topic
aliases: ["Combining Like Terms"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/Translating_Words_To_Algebraic_Expressions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Variables_And_Expressions"
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "Rewriting an algebraic expression into its shortest equivalent form by combining like terms and opening parentheses."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Simplifying Expressions

# Simplifying Expressions

An algebraic expression is a chain of variables, numbers, and operations — things like $3x + 2y - x + 4y + 5 - 3$ or $2(a + 4) - 3a$. Often the chain is longer than it needs to be, because the same variable shows up in more than one place, or because a pair of parentheses is masking something that could be opened up and rolled into the rest. To **simplify** an expression is to rewrite it as the shortest equivalent form — the one with the fewest possible pieces — without changing what the expression equals for any choice of the variables. Simplification is the cleanup step that makes every later move in algebra easier.

The full cleanup toolkit has two main moves. The first is **combining like terms**, which lets you collapse matching variable pieces into a single term. The second is applying the **distributive property** (see [[The_Distributive_Property]]) to open up any parentheses so the inside terms can merge with the outside ones. Both moves rely on the same underlying rule: you are never allowed to change what the expression evaluates to, only how it is written.

## What it means / The idea

A **term** is a single chunk of an expression joined to its neighbors by $+$ or $-$ signs. In $3x + 2y - x + 4y + 5 - 3$, the terms are $3x$, $+2y$, $-x$, $+4y$, $+5$, and $-3$. Each term has a **coefficient** (the number part, which may be a silent $1$ or $-1$) and a **variable part** (the letters with their exponents, or no variable at all if it is a plain number).

Two terms are **like terms** when their variable parts match exactly — same letters, same exponents. The coefficients can be anything. For example, $3x$ and $-x$ are like terms (both have just $x$). $5 x^2$ and $2 x^2$ are like terms (both have $x^2$). But $3x$ and $3 x^2$ are **not** like terms, because $x$ and $x^2$ are different variable parts. Plain numbers like $5$ and $-3$ are also like terms with each other, because they both have no variable part.

The headline rule is simple:

$$
a x^n + b x^n = (a + b) x^n
$$

To combine like terms, you add or subtract their coefficients and keep the shared variable part untouched. Unlike terms just stay where they are — there is no way to merge $3x$ and $2y$ into a single piece, and trying to is one of the classic pre-algebra mistakes.

## How it works / The procedure

1. **Open parentheses.** If any parentheses have a factor multiplying them from outside, apply the distributive property to hand the outside factor to each inside term. Watch the signs carefully, especially when the outside factor is negative.
2. **Group like terms.** Scan the expression and gather terms that share the same variable part. Matching variable exponents is the whole game. Some people underline each group in a different color or rearrange the terms so that matching ones sit next to each other.
3. **Combine each group.** Add (or subtract) the coefficients of each group, leaving the variable part alone. An $x$-group becomes a single $x$-term, a $y$-group becomes a single $y$-term, and the plain numbers combine into a single constant.
4. **Write the final expression.** Typically, list the terms in a standard order — variable terms first (often alphabetical or highest-exponent first) and the plain number last. Drop any terms whose coefficient collapsed to $0$.

## Why it works

Combining like terms is really just the distributive property in reverse. Think about $3x + 2x$. Both terms share the variable factor $x$, so you can factor that $x$ out: $3x + 2x = (3 + 2) x = 5 x$. The coefficients added because the distributive property told them to. The same logic holds for any matching variable part: $4 y^2 + 7 y^2 = (4 + 7) y^2 = 11 y^2$. And unlike terms refuse to combine for exactly the opposite reason — there is no common variable factor to pull out, so nothing can merge.

This is also why two different variables stay apart. $3x + 2y$ has no common factor (well, a common factor of $1$, which is useless), so there is no way to pull anything out and write it as a single term. Trying to write $3x + 2y = 5 xy$ or $5$ would change what the expression equals for almost every pair of values of $x$ and $y$, and that is a rewrite the rules forbid.

## Worked examples

### Example 1

Maya is copying an expression off the whiteboard in her tutoring center notebook and wants to simplify $3x + 2y - x + 4y + 5 - 3$. There are no parentheses to worry about, so skip straight to grouping the like terms. The $x$-group is $3x$ and $-x$, the $y$-group is $+2y$ and $+4y$, and the constant group is $+5$ and $-3$.

Combine each group by adding the coefficients, remembering that a lone $x$ really means $+1 x$:

$$
(3 - 1) x = 2 x \qquad (2 + 4) y = 6 y \qquad 5 - 3 = 2
$$

Put the pieces back together, writing the variable terms first:

$$
3 x + 2 y - x + 4 y + 5 - 3 = 2 x + 6 y + 2
$$

The cleaned-up expression has three pieces instead of six, and is equal to the original for every choice of $x$ and $y$.

### Example 2

Leilani is tidying up a line from her hiking club's budget sheet: $2 (a + 4) - 3 a$. There is a parenthesis with an outside factor, so step one is the distributive property. Hand the $2$ to each term inside:

$$
2 (a + 4) - 3 a = 2 \cdot a + 2 \cdot 4 - 3 a = 2 a + 8 - 3 a
$$

Now the parenthesis is gone and the expression is a flat chain of three terms. Group the like pieces: the $a$-group is $2 a$ and $-3 a$, and the constant group is just $+8$ on its own. Combine the $a$-group:

$$
(2 - 3) a = -1 a = -a
$$

The final simplified form, written with the variable term first and the constant second, is:

$$
-a + 8 \qquad \text{or equivalently} \qquad 8 - a
$$

Either form is correct. Many teachers prefer the version with the variable term first, but the two expressions mean exactly the same thing.

### Example 3

Kai is cleaning up a polynomial on the maker-space chalkboard: $3 x^2 + 5 x^2 + 4 x - x + 7 - 2$. The thing to notice here is that $x^2$ and $x$ are **not** like terms, because their exponents are different. So the $x^2$ terms must be kept separate from the $x$ terms.

Group like terms by matching variable part. The $x^2$-group is $3 x^2$ and $5 x^2$. The $x$-group is $+4 x$ and $-x$. The constant group is $+7$ and $-2$. Combine each:

$$
(3 + 5) x^2 = 8 x^2 \qquad (4 - 1) x = 3 x \qquad 7 - 2 = 5
$$

Put them back together, this time listing the highest-exponent term first, which is the standard way to write a polynomial:

$$
3 x^2 + 5 x^2 + 4 x - x + 7 - 2 = 8 x^2 + 3 x + 5
$$

A tidy three-term answer replaces the original six-term mess.

## Common pitfalls

- **Combining unlike terms by mistake.** $3 x + 2 y$ does not become $5 xy$ or $5$ or anything else. Without a matching variable part, the two terms have nothing to combine. The merge rule is strict: only terms with identical variable parts can be collapsed.
- **Treating $x$ and $x^2$ as like terms.** The exponent matters. $3 x + 5 x^2$ has two different variable parts, so the expression stays as is. It cannot collapse to $8 x^3$ or $8 x^2$ or anything else — the exponents have to match exactly.
- **Dropping the sign of a term when you move it.** A term carries its sign with it. When you rearrange $3 x + 2 y - x$ into $3 x - x + 2 y$, the $-x$ stays negative. Students often lose that minus during the shuffle, which turns into a $+ x$ and breaks the answer.
- **Forgetting to distribute a negative outside factor to every inside term.** In $-2 (x + 5)$, both pieces inside must flip: the result is $-2 x - 10$, not $-2 x + 10$. A negative factor is one of the easiest places to miss a sign.

## Prerequisites

- [[Variables_And_Expressions]] — you need to understand what terms and coefficients are before you can simplify
- [[The_Distributive_Property]] — opening parentheses is usually step one of a simplification
- [[Order_Of_Operations]] — you have to know which operation acts first when you check your work

## Problems Involving Simplifying Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="simplifying_expressions"></div>

## See Also

- [[The_Distributive_Property_With_Variables]] — the full distributive move when letters are inside the parentheses
- [[Evaluating_Expressions]] — plugging numbers in once the expression is simplified
- [[Translating_Words_To_Algebraic_Expressions]] — turning a sentence into an expression that will later need simplifying
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
