---
title: "Variables and Algebraic Expressions"
type: topic
aliases: ["Algebraic Expressions", "Variables"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "8", section: "8.8.1"}
related:
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Simplifying_Expressions"
  - "topics/pre_algebra/Translating_Words_To_Algebraic_Expressions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "A variable is a letter standing in for a number; an expression combines numbers, variables, and operations with no equals sign."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Variables and Algebraic Expressions

# Variables and Algebraic Expressions

Algebra starts the moment you let a letter hold a number's place. The letter is called a **variable**. Sometimes the number is genuinely unknown (you're trying to solve for it). Sometimes the number changes (tomorrow's hours worked, next month's gas price). Either way, using a symbol lets you describe a whole family of situations with a single compact phrase.

A string built from numbers, variables, and arithmetic operations — but with no equals sign — is called an **algebraic expression**. Think of an expression as a recipe: plug in a value for each variable and you get a number back out. Until you plug anything in, the expression just sits there, waiting.

---

## The four pieces of an expression

To read and write expressions fluently you need a short vocabulary.

- **Variable.** A letter that stands for a number. The classics are $x$, $y$, and $n$, but any symbol is fair game. The letter is not the value — it only holds a spot where a value can live.
- **Term.** A single chunk of an expression separated from the others by $+$ or $-$ signs. A term may be a plain number, a variable on its own, a number times a variable, or a product of several variables. The expression $4x + 9$ has two terms: $4x$ and $9$.
- **Coefficient.** The number that multiplies the variable part of a term. In $4x$ the coefficient is $4$; in the term $y$ the coefficient is an invisible $1$ (we almost never write $1y$, but that is what it is).
- **Constant term.** A term with no variable at all. In $4x + 9$, the constant term is $9$ — no matter what $x$ turns out to be, that $9$ never moves.

A useful rule: when you multiply a number by a variable you write the number first. Write $7k$, not $k7$. The value is identical, but the first form is what the rest of math assumes.

---

## Expression vs. equation

It's easy to confuse these two at first, so keep the contrast sharp.

- An **expression** has **no equals sign**. It's a phrase. You can evaluate it, simplify it, or factor it, but you cannot *solve* it because there is nothing to solve.
- An **equation** contains an equals sign. It claims that two expressions have the same value and invites you to find out which value (or values) of the variable make that claim true.

So $3n + 2$ is an expression. $3n + 2 = 14$ is an equation. The second one has a solution ($n = 4$); the first one is waiting for you to choose a value.

---

## Example 1: identifying the parts

> In the expression $6a + 11 - 2b$, name the terms, the coefficients, and the constant term.

Start by walking along the expression, stopping at every $+$ or $-$ sign. Each chunk you collect is a term:

- First term: $6a$. The coefficient is $6$ and the variable is $a$.
- Second term: $+11$. There is no variable here, so $11$ is the constant term.
- Third term: $-2b$. The sign stays with the term, so the coefficient is $-2$ and the variable is $b$.

**Terms:** $6a$, $11$, $-2b$. **Coefficients of the variable terms:** $6$ and $-2$. **Constant term:** $11$.

Notice how the minus sign in front of $2b$ attaches to the coefficient. A sign always rides along with the number it modifies — losing track of that is the most common early-algebra slip.

---

## Example 2: writing an expression from words

> Write an algebraic expression for "five more than twice a number."

Break the phrase into pieces and translate each one.

1. "A number" — pick a letter, say $n$.
2. "Twice a number" — that's the number doubled, so $2n$.
3. "Five more than" — you add $5$ to whatever came before.

Stack the pieces in order:

$$
2n + 5
$$

That's the whole expression. As a sanity check, try $n = 3$: twice $3$ is $6$, and five more than $6$ is $11$. Plugging $n = 3$ into $2n + 5$ gives $6 + 5 = 11$. The two descriptions agree, which is what a good translation should do.

For more practice turning English into symbols, see [[Translating_Words_To_Algebraic_Expressions]].

---

## Example 3 (optional): a real-context expression

> A concert ticket costs $\$15$. A fan also pays a flat $\$3$ processing fee on each order, no matter how many tickets are purchased. Write an expression for the total charge when the fan orders $n$ tickets.

Think about the total as two pieces: the price of the tickets plus the fee that gets tacked on once.

- Price of the tickets: each ticket is $\$15$, and there are $n$ of them, so that portion costs $15n$ dollars.
- Processing fee: $3$ dollars, charged once per order.

Adding gives the total:

$$
15n + 3
$$

Here the coefficient $15$ is the price per ticket, and the constant term $3$ is the fixed fee. Plug in $n = 4$ to test: $15 \cdot 4 + 3 = 63$, and indeed four tickets at $\$15$ plus a $\$3$ fee costs $\$63$.

Once you have an expression like this, you can use it for any value of $n$. That single step — moving from one specific calculation to a general rule — is the reason algebra exists. Plugging actual numbers into an expression is its own skill; see [[Evaluating_Expressions]] for a full walkthrough.

---

## How this topic connects

Expressions are the raw material for almost everything that follows in algebra.

- You will rewrite and clean them up in [[Simplifying_Expressions]] by combining like terms.
- You will open up grouped sub-expressions using [[The_Distributive_Property]].
- You will plug concrete numbers into them in [[Evaluating_Expressions]] to get a value.
- You will turn sentences into expressions and back again in [[Translating_Words_To_Algebraic_Expressions]].

Before you dive into those, make sure your arithmetic foundation is solid: [[Integers_And_The_Number_Line]] keeps signs from biting you, and [[Order_Of_Operations]] guarantees that everyone who evaluates your expression gets the same answer.

---

## Problems Involving Variables and Expressions

Choose a problem type, pick a difficulty, and click **Add to Vault**. Your selections stick around in this browser, so you can build up an entire worksheet before you open your [[Vault]] to see hints, answers, or a printable page.

<div class="problem-vault-widget" data-topic-slug="variables_and_algebraic_expressions"></div>

---

## See Also

- [[Evaluating_Expressions]]
- [[The_Distributive_Property]]
- [[Simplifying_Expressions]]
- [[Translating_Words_To_Algebraic_Expressions]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
