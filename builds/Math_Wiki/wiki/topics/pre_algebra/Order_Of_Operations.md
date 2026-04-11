---
title: "Order of Operations"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Evaluating_Expressions"
  - "topics/pre_algebra/Exponents_And_Powers"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Exponents_And_Powers"
problem_type_ids: []
figures: []
summary: "PEMDAS: a shared convention for evaluating expressions so everyone gets the same answer."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Order of Operations

# Order of Operations

Try handing the expression $2 + 3 \times 4$ to five different people and asking for the answer. Without a shared convention, you might get $20$ (from someone who added first, then multiplied) or $14$ (from someone who multiplied first, then added). Math cannot live with that kind of ambiguity — a single written expression must always point at a single number. The fix is a set of rules everyone agrees to follow, and that set of rules is what we call the **order of operations**.

## What it means

An **expression** is a string of numbers glued together by operation symbols: plus signs, minus signs, multiplication, division, exponents, and grouping tools such as parentheses and fraction bars. To **evaluate** an expression is to collapse it down to a single value. The order of operations is simply the global agreement about which symbols get to act first.

The rule in full is usually written as the acronym **PEMDAS**:

$$
\textbf{P} \to \textbf{E} \to \textbf{MD} \to \textbf{AS}
$$

Each letter is a rung on the ladder, and you climb from the top rung down:

- **P — Parentheses and other grouping symbols.** Anything enclosed in parentheses, brackets, braces, the top or bottom of a fraction bar, or under a radical sign is treated as a protected bubble. You simplify everything inside that bubble before it is allowed to interact with whatever is outside. When groups are nested inside other groups, you work from the innermost bubble outward.
- **E — Exponents.** Once the groups are resolved, take care of any powers (and, if you have seen them, roots).
- **M and D — Multiplication and Division.** These two share a rung. They are equally powerful, and when both appear in the same expression you handle them strictly left to right, in the order they are written.
- **A and S — Addition and Subtraction.** Like multiplication and division, these two share a rung. Work them left to right as well.

The two shared rungs are where most mistakes happen, so the rest of this page circles back to them a couple of times.

## How it works

Walking the ladder top to bottom, an expression gets rewritten one layer at a time, and the number of symbols shrinks on every pass. You never skip a rung. You never rearrange a rung. And when you finish the top rung, you drop to the next rung and do whatever it holds from left to right.

A cleaner way to picture it is the four-stage filter below. Every expression flows through the same four filters in order:

$$
\text{Groups} \longrightarrow \text{Exponents} \longrightarrow \text{Mult/Div (L to R)} \longrightarrow \text{Add/Sub (L to R)}
$$

The "left to right" tag on the bottom two stages is not optional wording. It is the part of the rule that keeps $12 \div 4 \times 3$ from turning into a coin flip. Multiplication and division have the same priority, so the symbols that appear earlier in the expression get handled first. Written out: $12 \div 4 \times 3 = 3 \times 3 = 9$. If you had silently multiplied first and then divided, you would have gotten $12 \div 12 = 1$, which is wrong. The left-to-right tiebreaker matters.

## Why it works

There is nothing magical about the PEMDAS ordering — it is a human convention, not a physical law. But it is not arbitrary either. The ordering reflects how the operations are built out of each other. Exponents are repeated multiplication, multiplication is repeated addition, and grouping symbols override everything because their whole job is to mark a phrase that must be read as one object. Putting the more powerful operations earlier in the evaluation preserves the natural layering: you are essentially unpacking the expression from the most compact shorthand down to the simplest one-step-at-a-time addition.

The convention is also mandatory in the sense that nothing else works. Any community sharing written mathematics has to pick some order and stick with it, because without one, every expression would need parentheses around every single step. PEMDAS is what the whole world settled on, and every calculator, programming language, and textbook honors it.

## Worked examples

### Example 1

Compute the value of $2 + 3 \times 4^2 - 6$.

Climb the PEMDAS ladder one step at a time. There are no parentheses, so skip straight to exponents:

$$
4^2 = 16
$$

Rewrite the expression with that substitution:

$$
2 + 3 \times 16 - 6
$$

Next rung is multiplication and division. Only multiplication appears here, and it handles the $3 \times 16$:

$$
2 + 48 - 6
$$

Last rung is addition and subtraction, done strictly left to right. First $2 + 48 = 50$, then $50 - 6 = 44$. The expression evaluates to $44$.

### Example 2

Simplify $\dfrac{20 - 2(3 + 1)^2}{2 \cdot 3 - 2}$.

The fraction bar is a grouping symbol in disguise: it forces you to finish the top and bottom separately before dividing. Start on the numerator. The innermost group is $(3 + 1) = 4$, which gives:

$$
20 - 2(4)^2
$$

The exponent is next — $4^2 = 16$ — leaving $20 - 2 \cdot 16$. Multiplication beats subtraction on the ladder, so $2 \cdot 16 = 32$ comes first, and then $20 - 32 = -12$. The numerator collapses to $-12$.

Now the denominator. Multiplication happens before subtraction, so $2 \cdot 3 = 6$ first, and then $6 - 2 = 4$. The denominator collapses to $4$.

With the top and bottom each reduced to a single number, the fraction bar finally acts as a division sign:

$$
\frac{-12}{4} = -3
$$

The whole expression equals $-3$.

### Example 3

Maya is packing lunches for a field trip. She buys $5$ sandwiches at $\$4$ each, $3$ juice boxes at $\$2$ each, and a single box of cookies for $\$7$ that the group will share. She wants a single expression that represents her total cost and its final value. Build and evaluate

$$
5 \times 4 + 3 \times 2 + 7
$$

Parentheses are absent and exponents are absent, so the top two rungs of the ladder are free. Drop to multiplication and division, working left to right. Two multiplications show up back to back. The left one is $5 \times 4 = 20$, and the next one is $3 \times 2 = 6$. After that pass, the expression is:

$$
20 + 6 + 7
$$

Add from left to right: $20 + 6 = 26$, then $26 + 7 = 33$. Maya's total is $\$33$. Notice that the expression is written with no parentheses at all — the PEMDAS rule is what kept the multiplications from tangling with the addition. If Maya had instead written $(5 + 3) \times 4 + 7$ by mistake, PEMDAS would have delivered $39$, an answer that has nothing to do with her groceries.

## Common pitfalls

- **Treating multiplication and division as separate rungs.** They share one rung, and the tiebreaker is left to right. Likewise, addition and subtraction share a rung. $10 - 4 + 1$ is $7$, not $5$, because the subtraction comes first.
- **Exponents eating only part of a base.** When a negative number is squared, the parentheses matter: $(-3)^2 = 9$, but $-3^2 = -(3^2) = -9$. The minus sign outside parentheses is really a multiply-by-$-1$, and that multiplication happens after the exponent.
- **Distributing into parentheses when you should finish inside first.** In a pure numerical problem, simplify the parentheses themselves — do not invoke the distributive property unless the inside has a variable in it.
- **Skipping the fraction bar's grouping power.** A horizontal fraction bar quietly says "parentheses on top, parentheses on bottom." Finish each piece separately before you divide.

## Problems Involving Order of Operations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="order_of_operations"></div>

## See Also

- [[The_Distributive_Property]]
- [[Evaluating_Expressions]]
- [[Exponents_And_Powers]]
- [[Integers_And_The_Number_Line]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
