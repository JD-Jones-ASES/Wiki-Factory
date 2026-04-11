---
title: "The Distributive Property with Variables"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-linear", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Solving_Two_Step_Equations"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
problem_type_ids: []
figures: []
summary: "Hand the outside factor to every term inside the parentheses, carrying signs along, whether the inside terms are numbers or variables."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > The Distributive Property with Variables

# The Distributive Property with Variables

You already know the distributive property from plain arithmetic: $a(b + c) = ab + ac$. When every letter in that formula is replaced by a number, the property just tells you two equivalent ways to do mental arithmetic. The real muscle appears when the letters inside the parentheses are themselves variables. Now the distributive property becomes a way to take a compact expression like $3(x + 4)$ and open it up into the equivalent expanded form $3x + 12$, which you can combine with other terms and eventually plug into an equation.

The rule is the same in both settings: hand the outside factor to every term inside the parentheses, sign and all, and write the results as a sum (or difference) of the new terms. Nothing is skipped, nothing is doubled up.

## The rule in symbols

For any numbers and expressions $a$, $b$, $c$:

$$
a(b + c) = ab + ac, \qquad a(b - c) = ab - ac.
$$

When $b$ or $c$ is an expression involving a letter, the product $ab$ or $ac$ becomes an algebraic term. For instance, if $b = x$, then $ab = a \cdot x = ax$, written with the number before the letter. If $b = 2x$, then $ab = a \cdot 2x = 2ax$. You simply multiply the coefficient by the outside factor and leave the variable along for the ride.

If there are more than two terms inside the parentheses, the same idea applies — every term gets touched. For example,

$$
5(x + 2y - 3) = 5x + 10y - 15.
$$

That is the basic move. The rest of this lesson is about handling the wrinkles that show up in real problems: negative outside factors, implicit $-1$ factors in front of parentheses, and mixing the distributed result with other terms already in the expression.

## How to do it

1. Look at the factor outside the parentheses. It may be a plain number, a negative number, a variable, or even an implicit $-1$ (when you see a lone minus in front of the parentheses).
2. Multiply that factor by each term inside, one at a time, keeping each term's sign glued to it.
3. Write the results out as a new expression, separated by the same signs that came out of your multiplications.
4. Combine any like terms that appear — either from inside the parentheses or from elsewhere in the expression.

Two things to watch very carefully. First, a lone minus sign in front of parentheses is really a coefficient of $-1$: $-(x - 5)$ means $(-1)(x - 5)$, which expands to $-x + 5$. Second, every term gets flipped, not just the first one. That is the slip that costs the most points on homework.

## Why it works

The distributive property is a statement about how multiplication interacts with addition, and it is true for every real number — which means it is also true for every value a variable might take on. If $x$ stands for $7$ today and $12$ tomorrow, the expressions $3(x + 4)$ and $3x + 12$ produce the same answer on both days: $3 \cdot 11 = 33$ on day one and $3 \cdot 16 = 48$ on day two. The two forms are not just equal on certain values of $x$; they are equal for every value of $x$. That is what makes it a safe move to rewrite one as the other.

Geometrically, you can still picture the area-of-a-split-rectangle argument from [[The_Distributive_Property]]. A rectangle of height $a$ and base $(b + c)$ has area $a(b + c)$. Split the base and the same rectangle is the union of two pieces with areas $ab$ and $ac$. Nothing about that argument relied on $b$ or $c$ being a specific number, so swapping in variables does not break anything.

## Worked examples

### Example 1: a single distribution

Give the expanded form of $4(x + 6)$.

The outside factor is $4$. Hand it to each term inside in turn:

$$
4(x + 6) = 4 \cdot x + 4 \cdot 6 = 4x + 24.
$$

That is the final simplified form. There is nothing more to combine because $4x$ and $24$ are not like terms — one has a variable, the other does not.

As a quick sanity check, pick any value of $x$ and see that both forms give the same answer. Try $x = 5$: the original is $4(5 + 6) = 4 \cdot 11 = 44$, and the expanded form is $4 \cdot 5 + 24 = 20 + 24 = 44$. They agree, as they should for every value of $x$.

### Example 2: the hidden $-1$ out front

Expand $-(2x - 7)$.

A minus sign sitting alone in front of parentheses is short for "times negative one." So $-(2x - 7)$ means $(-1)(2x - 7)$. Distribute $-1$ to each term inside, keeping the sign of each piece:

$$
(-1)(2x) + (-1)(-7) = -2x + 7.
$$

Notice that every term flipped sign. The $2x$ became $-2x$, and the $-7$ became $+7$. Students who write $-(2x - 7) = -2x - 7$ have done the distribution to the first term only and left the $-7$ untouched, which is the most common error in the entire lesson.

### Example 3: distribute, then combine

Expand and simplify $2(3x + 4) - 5$.

Two operations are happening: a distribution, and then a subtraction of a constant. Handle the distribution first, because that is the operation inside the parentheses shell:

$$
2(3x + 4) = 2 \cdot 3x + 2 \cdot 4 = 6x + 8.
$$

Now fold in the $-5$ that has been sitting at the end all along:

$$
6x + 8 - 5.
$$

The $8$ and $-5$ are like terms — both are plain numbers — so combine them:

$$
6x + 3.
$$

Check at $x = 1$: the original is $2(3 + 4) - 5 = 2 \cdot 7 - 5 = 14 - 5 = 9$, and the simplified form is $6 \cdot 1 + 3 = 9$. The two agree, confirming the expansion is right.

This is the pattern you will see over and over when simplifying algebraic expressions: distribute to clear parentheses, then combine whatever is left that matches.

## Common pitfalls

- **Forgetting to distribute to every term.** If the parentheses hold $x + 4$, both the $x$ and the $4$ must be multiplied by the outside factor. Missing the second term is the number-one error.
- **Forgetting to distribute a negative through every term.** A lone minus out front is a factor of $-1$. It flips the sign of every term inside, not just the first one.
- **Combining unlike terms.** After distributing, $4x$ and $24$ are not like terms and cannot be merged. Only terms with the same variable part (same letter, same exponent) are allowed to combine.
- **Dropping a coefficient during distribution.** Multiplying $3$ into $2x$ gives $6x$, not $3x$ or $2x$. Multiply the outside factor by the coefficient of each inside term and keep the variable along.
- **Losing the sign of a term that had no explicit plus in front.** The first term inside the parentheses is positive by default; the later terms carry whatever sign is written in front of them. Keep those signs anchored.

## Problems Involving The Distributive Property with Variables

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_distributive_property_with_variables"></div>

## See Also

- [[The_Distributive_Property]]
- [[Variables_And_Algebraic_Expressions]]
- [[Solving_Two_Step_Equations]]
- [[Evaluating_Expressions]]
- [[Multi_Step_Equations|Multi-Step Equations (Algebra 1)]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
