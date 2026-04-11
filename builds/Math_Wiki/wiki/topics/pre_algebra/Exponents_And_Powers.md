---
title: "Exponents and Powers"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-exponents-and-radicals", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Rational_Exponents"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "Shorthand for repeated multiplication, with special care for zero, one, and negative bases."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Exponents and Powers

# Exponents and Powers

Writing $7 \cdot 7 \cdot 7 \cdot 7 \cdot 7 \cdot 7$ gets tiring fast, and for good reason — repeated multiplication by the same number shows up in science, money, and measurement constantly. **Exponents** are the mathematical shorthand for that repetition. They turn a long string of the same factor into a compact two-character expression, and they bring with them a new layer in the order of operations. Learning the notation now pays off forever: exponents power (pun intended) everything from scientific notation to compound interest to computer algorithms.

## What it means

An expression of the form $b^n$ is called a **power**. The number $b$ is the **base** — it is the factor being multiplied — and $n$ is the **exponent**, also called the **power**. The exponent tells you how many copies of the base to multiply together.

$$
b^n = \underbrace{b \cdot b \cdot b \cdots b}_{n \text{ factors}}
$$

A few concrete examples:

$$
2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 32
$$

$$
10^3 = 10 \cdot 10 \cdot 10 = 1000
$$

$$
4^2 = 4 \cdot 4 = 16
$$

We read $b^n$ out loud as "$b$ to the $n$th power" or simply "$b$ to the $n$." Two exponents have special nicknames: $b^2$ is read as "$b$ squared" because it gives the area of a square with side length $b$, and $b^3$ is read as "$b$ cubed" because it gives the volume of a cube with side length $b$.

## How it works

Three special cases deserve their own attention because they trip up almost everyone the first time around.

**Exponent of one.** Any base raised to the power of one is just the base itself.

$$
b^1 = b
$$

That makes sense — one copy of $b$ multiplied together is just $b$.

**Exponent of zero.** Any **nonzero** base raised to the power of zero equals one.

$$
b^0 = 1 \quad (\text{for } b \neq 0)
$$

This looks strange — "multiply zero copies of something and get $1$?" — but it fits the pattern. Dividing by the base steps the exponent down by one each time: $2^3 = 8$, $2^2 = 4$, $2^1 = 2$, $2^0 = 1$. Each step divides by $2$, so the next one has to be $1$ to keep the pattern consistent. (The case $0^0$ is handled separately and we do not tackle it here.)

**Negative bases and parentheses matter.** The expressions $(-3)^2$ and $-3^2$ look nearly identical but give different answers. In $(-3)^2$, the parentheses say "the base is $-3$," so we square negative three:

$$
(-3)^2 = (-3) \cdot (-3) = 9.
$$

In $-3^2$, with no parentheses, the exponent binds tighter than the minus sign. The base is just $3$, and the minus sits out front like a negative one that multiplies the result:

$$
-3^2 = -(3 \cdot 3) = -9.
$$

So $(-3)^2 = 9$ and $-3^2 = -9$. This is the number-one sign mistake in pre-algebra, and the only cure is to read the parentheses carefully. When an exponent meets a minus, parentheses are what decide which one wins.

## Why it works

Exponents were invented to compress repeated multiplication the same way multiplication itself compresses repeated addition. Just as $5 \cdot 4$ is shorthand for $4 + 4 + 4 + 4 + 4$, $5^4$ is shorthand for $5 \cdot 5 \cdot 5 \cdot 5$. The compression matters because repeated multiplication grows explosively: $2^{10}$ is already $1024$, and $2^{20}$ is over a million. Writing those out as chains of $\cdot$s would be ridiculous. Notation is doing real work here.

The rule $b^0 = 1$ is not a random convention. It is the only value that keeps the pattern of "divide by the base when you decrease the exponent by one" consistent all the way down. Breaking the pattern at zero would wreck later rules for multiplying and dividing powers.

## Worked examples

### Example 1

Evaluate $2^5$, $3^4$, and $10^3$.

For $2^5$, multiply five copies of $2$:

$$
2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2.
$$

Build it up step by step: $2 \cdot 2 = 4$, then $4 \cdot 2 = 8$, then $8 \cdot 2 = 16$, then $16 \cdot 2 = 32$. So $2^5 = 32$.

For $3^4$, multiply four copies of $3$:

$$
3^4 = 3 \cdot 3 \cdot 3 \cdot 3 = 9 \cdot 9 = 81.
$$

For $10^3$, multiply three copies of $10$:

$$
10^3 = 10 \cdot 10 \cdot 10 = 1000.
$$

Powers of $10$ have a tidy pattern: $10^n$ is a $1$ followed by $n$ zeros. That fact is the basis for scientific notation.

### Example 2

Determine $(-2)^3$ and $(-2)^4$. Is the answer positive or negative each time?

For $(-2)^3$, multiply three copies of $-2$:

$$
(-2)^3 = (-2) \cdot (-2) \cdot (-2).
$$

The first two factors give $(-2) \cdot (-2) = 4$. Multiplying by the third $-2$ flips the sign: $4 \cdot (-2) = -8$.

$$
(-2)^3 = -8.
$$

For $(-2)^4$, multiply four copies of $-2$:

$$
(-2)^4 = (-2) \cdot (-2) \cdot (-2) \cdot (-2).
$$

The first two give $4$, the next two give another $4$, and $4 \cdot 4 = 16$:

$$
(-2)^4 = 16.
$$

Pattern: a negative base raised to an **odd** exponent gives a negative result (an odd number of sign flips), and a negative base raised to an **even** exponent gives a positive result (an even number of sign flips).

### Example 3

Compute the difference between $(-5)^2$ and $-5^2$.

These look identical but are not. For $(-5)^2$, the parentheses lock $-5$ in as the base:

$$
(-5)^2 = (-5) \cdot (-5) = 25.
$$

For $-5^2$, with no parentheses, the exponent attaches only to $5$, and the minus is applied last:

$$
-5^2 = -(5 \cdot 5) = -25.
$$

So $(-5)^2 = 25$ and $-5^2 = -25$. Their difference is:

$$
(-5)^2 - (-5^2) = 25 - (-25) = 50.
$$

The two expressions disagree by $50$, all because of a pair of parentheses.

## Common pitfalls

- **Multiplying base times exponent.** $3^4$ is not $3 \cdot 4 = 12$. It is $3 \cdot 3 \cdot 3 \cdot 3 = 81$. An exponent counts factors, not a product.
- **Ignoring parentheses around a negative base.** $(-2)^4 = 16$ but $-2^4 = -16$. The parentheses tell you what the base is.
- **Saying $b^0 = 0$.** Zero copies multiplied together is defined as $1$, not $0$. The only catch is that $0^0$ is left undefined.
- **Reading $b^1$ as $b$ times $1$.** $b^1$ is just $b$. The exponent of one says "one copy." Do not turn it into a needless multiplication.

## Problems Involving Exponents and Powers

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="exponents_and_powers"></div>

## See Also

- [[Order_Of_Operations]]
- [[Square_Roots_And_Cube_Roots]]
- [[Multiplying_And_Dividing_Integers]]
- [[Rational_Exponents]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
