---
title: "Properties of Addition and Multiplication"
type: topic
aliases: ["Field Properties", "Arithmetic Properties"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-topic", "#skill-algebraic-manipulation", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/The_Distributive_Property"
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Variables_And_Expressions"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
problem_type_ids: []
figures: []
summary: "The five core rules (commutative, associative, distributive, identity, inverse) that let you rearrange and regroup arithmetic legally."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Properties of Addition and Multiplication

# Properties of Addition and Multiplication

When you rearrange $3 + 5$ into $5 + 3$, or swap $(2 + 4) + 1$ for $2 + (4 + 1)$, you are using rules so familiar that they feel invisible. But every one of those moves is backed by a named property of arithmetic — a rule that guarantees you are allowed to make the swap and still get the same answer. This page pulls five of those rules out of the background and gives them names, symbols, and examples. Together, they are the license plates for every legal move you will make in algebra.

These properties matter because algebra is essentially the art of rewriting an expression in a more useful form without changing its value. Every time you collect like terms, reorder factors, or pull out a common factor, you are invoking one of the five rules below. Knowing their names is helpful, but knowing what each one actually lets you do is more helpful — and that is what the rest of this page will try to make stick.

## What it means / The idea

There are five core properties. Each comes with a short sentence describing the idea, a clean algebraic form, and a concrete number example so the abstract version has something to lean on.

**1. Commutative property — the order does not matter.** For any numbers $a$ and $b$:

$$
a + b = b + a \qquad \text{and} \qquad a \cdot b = b \cdot a
$$

In numbers: $4 + 7 = 7 + 4 = 11$, and $3 \cdot 5 = 5 \cdot 3 = 15$. A warning: subtraction and division are **not** commutative. $7 - 4$ is not the same as $4 - 7$, and $8 \div 2$ is not the same as $2 \div 8$.

**2. Associative property — the grouping does not matter.** For any numbers $a$, $b$, and $c$:

$$
(a + b) + c = a + (b + c) \qquad \text{and} \qquad (a \cdot b) \cdot c = a \cdot (b \cdot c)
$$

In numbers: $(2 + 5) + 8 = 2 + (5 + 8) = 15$, and $(3 \cdot 4) \cdot 2 = 3 \cdot (4 \cdot 2) = 24$. Again, subtraction and division are **not** associative: $(10 - 5) - 2 = 3$ but $10 - (5 - 2) = 7$, which is a different number.

**3. Distributive property — multiplication spreads across a sum.** For any numbers $a$, $b$, and $c$:

$$
a (b + c) = a b + a c
$$

In numbers: $3 (4 + 6) = 3 \cdot 10 = 30$ on one side, and $3 \cdot 4 + 3 \cdot 6 = 12 + 18 = 30$ on the other. See [[The_Distributive_Property]] for a deeper dive.

**4. Identity property — the number that does nothing.** Adding $0$ to any number leaves it alone, and multiplying any number by $1$ leaves it alone:

$$
a + 0 = a \qquad \text{and} \qquad a \cdot 1 = a
$$

In numbers: $9 + 0 = 9$ and $9 \cdot 1 = 9$. The $0$ is the "do-nothing" partner for addition, and the $1$ is the "do-nothing" partner for multiplication.

**5. Inverse property — the number that undoes a number.** Every number has an **opposite** ($-a$) that cancels it under addition, and every nonzero number has a **reciprocal** ($\tfrac{1}{a}$) that cancels it under multiplication:

$$
a + (-a) = 0 \qquad \text{and} \qquad a \cdot \frac{1}{a} = 1 \qquad (a \ne 0)
$$

In numbers: $7 + (-7) = 0$ and $7 \cdot \tfrac{1}{7} = 1$. These inverses are exactly the moves that later get used to solve equations — you add the opposite to cancel a constant, or multiply by the reciprocal to cancel a coefficient.

## How it works / The procedure

When you are simplifying or rewriting an expression, the properties give you specific permissions. A good habit is to ask, before each move: *which property am I using right now?*

1. **Reorder freely when you are adding or multiplying.** If the expression is a long chain of additions, or a long chain of multiplications, the commutative property lets you shuffle the pieces into any order that makes the arithmetic easier.
2. **Regroup to pair friendly numbers together.** The associative property lets you redraw the invisible parentheses so that two numbers you would rather add first (or multiply first) end up next to each other.
3. **Break a product across a sum, or collect a common factor back out.** The distributive property is what lets you go from $3(x + 4)$ to $3 x + 12$, and from $5 x + 5 y$ back to $5(x + y)$.
4. **Add or multiply by do-nothing partners when it helps.** The identity property is quiet, but it is behind tricks like writing $x$ as $1 \cdot x$ or inserting a $+0$ when you are rearranging.
5. **Cancel terms using inverses.** Adding the opposite of a term wipes it out. Multiplying by the reciprocal of a factor wipes it out. This is the backbone of all equation-solving later on.

## Why it works

These properties are not random facts about numbers — they are the essential truths that make arithmetic behave predictably. Think about why the commutative property for addition feels obvious: if you have three apples and then grab two more, you end up with five apples, and if you had started with two and grabbed three more, you still end up with five. The order you picked them up in cannot change how many you have, because the end count only depends on the total. Multiplication commutes for similar reasons — a grid of $3 \times 5$ dots and a grid of $5 \times 3$ dots are the same collection of dots, just with your head tilted.

Associativity is the same idea one level up. Regrouping how you bundle the additions does not change the final count, because each individual $+1$ is being done once either way. The distributive property has a picture too (see the rectangle diagram on [[The_Distributive_Property]]), and it follows from the same "multiplication is repeated addition" logic. The identity and inverse properties just identify the specific numbers that act as neutral elements and as cancellers. Together these five rules define what people mean when they say ordinary arithmetic is "well-behaved," and they are exactly the rules that algebra is allowed to quietly assume without re-proving them.

## Worked examples

### Example 1

Priya is adding up the scores on her community garden signup sheet: $17 + 24 + 3$. She notices that $17 + 3 = 20$ is friendly, but $17 + 24$ is not. The commutative property lets her reorder the three numbers, and the associative property lets her regroup them:

$$
17 + 24 + 3 = 17 + 3 + 24 = (17 + 3) + 24 = 20 + 24 = 44
$$

The commutative property turned $24 + 3$ into $3 + 24$, and the associative property let her quietly put the parentheses around the first two numbers in the new order. Both moves preserve the value, so the total is still $44$. The arithmetic was easier because the friendly pair $17 + 3$ collapsed to a round $20$.

### Example 2

Rohan is finishing the bill for a pop-up book fair at his school newspaper: $4 \cdot 7 \cdot 25$. The big insight is that $4 \cdot 25 = 100$, which is much easier to work with than $4 \cdot 7 = 28$. Reorder and regroup:

$$
4 \cdot 7 \cdot 25 = 7 \cdot 4 \cdot 25 = 7 \cdot (4 \cdot 25) = 7 \cdot 100 = 700
$$

The commutative property swapped $7$ and $4$, and the associative property let Rohan bracket the $4 \cdot 25$ together so it could collapse first. Without the rules, he might have stubbornly done $4 \cdot 7 = 28$ and then $28 \cdot 25$, which is correct but slower. Total is $\$700$.

### Example 3

Zoe is simplifying a short expression from her photography class budget: $5 (x + 3) - 5 x$. The distributive property opens up the parenthesis so the $x$-terms can talk to each other, and the inverse property is what finishes the job.

Hand the $5$ to each term inside the parenthesis (distributive property):

$$
5 (x + 3) - 5 x = 5 x + 15 - 5 x
$$

Now use the commutative property to put the two $x$-terms next to each other, then use the inverse property: $5 x$ and $-5 x$ are additive opposites, so they cancel to $0$:

$$
5 x + 15 - 5 x = 5 x + (-5 x) + 15 = 0 + 15
$$

And finally the identity property collapses $0 + 15$ to just $15$:

$$
0 + 15 = 15
$$

So $5(x + 3) - 5 x = 15$, a constant — which makes sense, because the $5 x$ from the distribution and the $-5 x$ from outside the parenthesis were built to cancel each other out, leaving only the $5 \cdot 3$ piece behind.

## Common pitfalls

- **Thinking subtraction is commutative.** It is not. $7 - 4 = 3$ and $4 - 7 = -3$, which are different numbers. Same warning for division: $8 \div 2 = 4$ while $2 \div 8 = 0.25$. The commutative and associative properties only apply to addition and multiplication.
- **Confusing commutative (order) with associative (grouping).** Commutative is about swapping positions: $a + b = b + a$. Associative is about moving the parentheses: $(a + b) + c = a + (b + c)$. Both feel related because both let you be flexible, but the first changes order and the second changes grouping.
- **Mixing up the additive and multiplicative identities.** The do-nothing partner for addition is $0$, and the do-nothing partner for multiplication is $1$. Students sometimes write $a + 1 = a$ or $a \cdot 0 = a$, which are both wrong. $a + 0 = a$ and $a \cdot 1 = a$ are the correct identity statements.
- **Trying to find a reciprocal of zero.** Every nonzero number has a reciprocal, but $0$ does not. $\tfrac{1}{0}$ is undefined, because there is no number that multiplies with $0$ to give $1$. The inverse property for multiplication has to exclude $0$ from its promise.

## Prerequisites

- [[Variables_And_Expressions]] — the properties are stated with variables, so you need to be at home with letter names
- [[Adding_And_Subtracting_Integers]] — the examples all involve adding and subtracting, often with negatives
- [[Multiplying_And_Dividing_Integers]] — ditto for the multiplicative side

## Problems Involving Properties of Addition and Multiplication

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="properties_of_addition_and_multiplication"></div>

## See Also

- [[The_Distributive_Property]] — the detailed treatment of property number three
- [[Order_Of_Operations]] — the convention that tells you which property to use first
- [[Integers_And_The_Number_Line]] — where opposites live and why they cancel
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
