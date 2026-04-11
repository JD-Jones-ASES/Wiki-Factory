---
title: "Variables and Expressions"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-numbers-and-operations", "#skill-translation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs:
  - {book: "algebra_1", chapter: "1", section: "1.1"}
related:
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Translating_Words_To_Algebraic_Expressions"
  - "topics/algebra/One_Step_Equations"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Evaluating_Expressions"
problem_type_ids: []
figures: []
summary: "A variable is a letter standing in for a number; an expression is a recipe you can evaluate once the number is known."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Variables and Expressions

# Variables and Expressions

Algebra starts with one big idea: a letter can stand in for a number you do not yet know. Once you allow that, you can write down a **recipe** like $3x + 5$ that describes what to do with any number somebody hands you, without committing to a specific one. That recipe is called an **algebraic expression**, and the letter is called a **variable**. Everything else in this course is built on these two ideas.

This topic is the official starting point. It sets up the vocabulary — variable, term, coefficient, constant — and the two things you will do with expressions constantly: **evaluate** them when you know the number that the variable stands for, and **write** them when you are translating a sentence or a situation into symbols. Both skills should feel automatic by the time you finish this page, because every later topic — from [[One_Step_Equations|solving equations]] to [[Linear_Functions|graphing functions]] — assumes you can already do them.

---

## Key ideas

### Variables, constants, and terms

A **variable** is a letter or symbol that stands in for a number. Common choices are $x$, $y$, $n$, $t$, and $a$, but any letter is fair game. The choice of letter has no mathematical meaning; it is just a label. What matters is the role the letter plays in the expression.

A **constant** is a number whose value is fixed and does not change. The numbers $3$, $-7$, $\tfrac{1}{2}$, and $\pi$ are all constants. Constants always mean exactly what they say; $3$ is $3$ no matter what $x$ turns out to be.

An **algebraic expression** is a recipe built from variables and constants glued together using the usual arithmetic moves — plus, minus, times, divide, powers, and occasionally roots. Examples: $3x + 5$, $2a^2 - 7b$, $\dfrac{n + 4}{3}$, $x^2 - 4x + 7$. Expressions can be simple or long, but they are always a **recipe**, not a question. An expression is not the same as an **equation**, which adds an equals sign and asserts that two expressions are equal. Compare $3x + 5$ (an expression — just a recipe) with $3x + 5 = 20$ (an equation — a claim about which value of $x$ makes the two sides equal). An expression is something you evaluate; an equation is something you solve.

Inside an expression, the chunks separated by $+$ or $-$ signs are called **terms**. In $4x - 9 + 2x$, the three terms are $4x$, $-9$, and $2x$. The sign belongs to the term to its right — the second term is **negative** $9$, not $9$. Always carry the sign with the term.

### Coefficients

The numerical factor in front of a variable in a term is the **coefficient** of that term. In $4x$ the coefficient is $4$. In $-7y$ the coefficient is $-7$. In $2x$ the coefficient is $2$.

Two subtleties get people stuck. First, a variable with no visible number in front has an invisible coefficient of $1$: $x$ is really $1x$ and $-y$ is really $-1y$. Second, a term that is just a number (like the $-9$ in $4x - 9$) has no variable attached and is called a **constant term** instead. It does not have a "coefficient" in the usual sense — it is just a constant.

### Evaluating an expression

To **evaluate** an expression at a particular value of the variable, substitute that value in for every appearance of the variable, then simplify using [[Order_Of_Operations|PEMDAS]]. The substitution step is mechanical: wherever you see $x$, replace it with the number, in parentheses if the number is negative. Then carry out the arithmetic exactly in the PEMDAS order — parentheses, then exponents, then multiplication and division left to right, then addition and subtraction left to right.

The two things that slip are (a) skipping the order of operations and doing additions before exponents or multiplications, and (b) dropping the parentheses around a negative substitute, which is where most of the sign errors on this topic live. Always wrap a negative number in parentheses before you drop it into the expression.

### Translating words into expressions

The other direction — turning a sentence into an algebraic expression — is the skill that makes word problems solvable. A small vocabulary covers most cases:

- "Sum of," "added to," "increased by," "plus" → $+$
- "Difference of," "subtracted from," "decreased by," "less than," "minus" → $-$
- "Product of," "times," "of" (in percent problems) → $\cdot$
- "Quotient of," "divided by," "per" → $\div$ or a fraction

Two phrases deserve careful attention. "$7$ less than a number" means "the number minus $7$," which becomes $n - 7$, **not** $7 - n$. The order of the words reverses the order of the subtraction. Similarly, "the quotient of $a$ and $b$" is $a \div b$, with the first-named quantity on top.

When the sentence includes a compound description, you often need parentheses to keep the multiplication from running into the wrong piece. "$3$ times the sum of $x$ and $4$" is $3(x + 4)$, not $3x + 4$. The parentheses capture the fact that the sum has to happen before the multiplication.

---

## Example 1: Evaluate at a specific value

> Compute the value of the expression $3x^2 - 4$ when $x = 5$.

Substitute $5$ for every $x$ in the expression. There is only one $x$, and it is inside the squared term:

$$
3(5)^2 - 4
$$

Now apply PEMDAS. The exponent goes first: $5^2 = 25$.

$$
= 3(25) - 4
$$

Next is multiplication: $3 \cdot 25 = 75$.

$$
= 75 - 4
$$

Finally the subtraction:

$$
= 71
$$

The expression evaluates to $71$ when $x = 5$. One thing worth noticing: the exponent applies only to the $x$, not to the $3$. The expression $3x^2$ means $3 \cdot x \cdot x$, not $(3x)^2$. If you accidentally squared the $3$ along with the $x$, you would have computed $(3 \cdot 5)^2 = 225$, which is a very different answer.

---

## Example 2: Translate a sentence into an expression

> Rohan is writing an expression for his tutoring center's worksheet. Express the phrase "$7$ less than twice a number" as an algebraic expression using $n$ for the unknown number.

Read the phrase in chunks. "Twice a number" means multiplying the number by $2$, which gives $2n$. "$7$ less than" means subtracting $7$ from whatever came before it.

The tricky part is the word order. "$7$ less than $2n$" means "$2n$ minus $7$," not "$7$ minus $2n$." The phrase "$A$ less than $B$" subtracts $A$ from $B$, which is backwards from the order the words appeared. So the answer is

$$
2n - 7
$$

A good way to double-check: plug in a specific number and see whether the expression matches what the sentence describes. If the number is $10$, then twice it is $20$, and $7$ less than $20$ is $13$. Now evaluate the expression at $n = 10$: $2(10) - 7 = 20 - 7 = 13$. Matches. If you had written $7 - 2n$ by mistake, you would have gotten $7 - 20 = -13$, which is clearly not what "$7$ less than $20$" means.

---

## Example 3: Identify terms and coefficients

> Zoe is organizing a community-garden budget expression. Write down the terms and the coefficient of each variable term in $4x - 9 + 2x$.

Start by separating the expression into its **terms**, which are the chunks separated by $+$ or $-$ signs. Pulling the signs along with the numbers that follow them, the three terms are

$$
4x, \quad -9, \quad 2x
$$

Now label each one. The first term $4x$ has variable $x$ and coefficient $4$. The second term $-9$ has no variable at all — it is a **constant term**, and it does not have a coefficient in the usual sense (only variable terms have coefficients). The third term $2x$ has variable $x$ and coefficient $2$.

The two variable terms $4x$ and $2x$ are "like terms" because they both involve the same variable to the same power (both are $x$ to the first power). Like terms can be combined by adding their coefficients: $4x + 2x = 6x$. So the expression $4x - 9 + 2x$ simplifies to

$$
6x - 9
$$

which has only two terms: $6x$ and $-9$. That is a key simplification move you will use constantly in [[Adding_And_Subtracting_Polynomials|combining polynomials]] and in [[One_Step_Equations|solving equations]].

---

## Common pitfalls

- **Applying the wrong order of operations.** If you evaluate $3 + 4 \cdot 5$ as $35$, you are doing the addition before the multiplication, which PEMDAS forbids. The right answer is $23$, because $4 \cdot 5$ resolves to $20$ first, and then $3 + 20 = 23$.
- **Forgetting parentheses around a negative substitute.** When you evaluate $-x^2$ at $x = -3$, the expression becomes $-(-3)^2 = -(9) = -9$, not $9$. The $-$ sitting outside the $(-3)^2$ is not part of the square, and the parentheses on the $(-3)$ are what make it clear that the entire negative number is being squared.
- **Reversing a "less than" subtraction.** The phrase "$7$ less than $x$" is $x - 7$, not $7 - x$. The word "than" swaps the order of the numbers relative to the order the words appear.
- **Treating an expression like an equation.** An expression like $3x + 5$ has no equals sign — it is not asking you to find $x$, it is just a recipe. If the problem says "evaluate," you need a specific value of $x$ to plug in, and if none is given, you cannot produce a single number. If the problem says "solve," there had better be an equals sign somewhere.
- **Losing the coefficient on $-y$ or $y$.** The coefficient of $y$ is $+1$ and the coefficient of $-y$ is $-1$. The "$1$" is invisible but real. Ignoring it costs you a sign later.

---

## Prerequisites

Before you settle into this topic, make sure these feel automatic:

- [[Order_Of_Operations]] — because evaluating an expression is just PEMDAS applied to the substituted form
- [[Integers_And_The_Number_Line]] — so that negative substitutes and negative coefficients do not trip you up
- [[Evaluating_Expressions]] — the pre-algebra version of the same evaluation skill

---

## Problems Involving Variables and Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="variables_and_expressions"></div>

---

## See Also

- [[Variables_And_Algebraic_Expressions]]
- [[Evaluating_Expressions]]
- [[Order_Of_Operations]]
- [[Translating_Words_To_Algebraic_Expressions]]
- [[One_Step_Equations]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
