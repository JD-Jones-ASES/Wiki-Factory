---
title: "Multiplying and Dividing Integers"
type: topic
aliases: ["Integer Multiplication", "Integer Division", "Sign Rules"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "2", section: "2.4"}
related:
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Order_Of_Operations_With_Integers"
  - "topics/pre_algebra/Multiplying_Fractions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
problem_type_ids: []
figures: []
summary: "Sign rules for integer products and quotients, and why two negatives combine to make a positive."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Multiplying and Dividing Integers

# Multiplying and Dividing Integers

Once you can add and subtract integers, the natural next question is what happens when you multiply them. Multiplication with positive numbers is familiar territory — $3 \times 4$ is just $4 + 4 + 4$. The surprise is that once a negative sign gets involved, you have to learn which direction the result flips. Fortunately there are only a handful of cases, and once you see why they behave the way they do, you never have to memorize them again.

## What it means

Multiplying two integers means combining their magnitudes and then figuring out whether the answer is positive or negative. The **magnitude** is the absolute value — what the numbers look like with the signs peeled off. That part is easy: $4 \times 5 = 20$ no matter what signs are sitting in front of the $4$ and the $5$. The whole game is the sign.

Dividing works the same way. Whenever you divide one integer by another (and the second one is not zero), the result might not be an integer at all — you could land on a fraction — but the sign of whatever you end up with follows the exact same rules as multiplication. Any quotient problem is really a multiplication problem turned sideways: $\tfrac{-12}{4}$ is asking "what number times $4$ gives $-12$?"

**Zero is special.** Multiplying any integer by zero gives zero, period: $0 \cdot n = 0$ for every integer $n$. Dividing zero by a nonzero integer also gives zero: $0 \div n = 0$. But **dividing by zero is undefined.** It is not a legal move and has no answer at all. Keep that last one in the back of your mind — it will come up again every time you work with fractions, rational expressions, or functions.

## The rule

There are only four sign combinations, and they pair up neatly.

$$
(+)\cdot(+) = +, \qquad (-)\cdot(-) = +
$$

$$
(+)\cdot(-) = -, \qquad (-)\cdot(+) = -
$$

Division obeys the identical table. To state it in words rather than symbols:

- **Same signs give a positive.** Two positives multiplied together are positive, and two negatives multiplied together are also positive.
- **Different signs give a negative.** A positive times a negative is negative, and a negative times a positive is also negative.
- Compute the product or quotient of the absolute values first, then attach the sign at the end.

For a **chain** of more than two factors, you can use a shortcut. Count how many negative factors appear. If the count is **even**, the whole product is positive. If the count is **odd**, the whole product is negative. You do not have to work left to right if you do not want to — just tally the minus signs.

## Why it works

The "negative times negative gives positive" rule is the one students get asked about the most, and it does not have to be magic. Think of multiplying by $-1$ as the instruction "flip to the opposite." One flip turns $5$ into $-5$. A second flip turns $-5$ back into $5$. Two flips cancel. So multiplying by $-1$ twice is the same as doing nothing, which means $(-1)\cdot(-1) = 1$. Any "negative times negative" is just a rescaled version of that: $(-3)\cdot(-4) = 3 \cdot 4 \cdot (-1) \cdot (-1) = 12 \cdot 1 = 12$.

Here is another way to see it. Subtracting a negative is the same as adding a positive — that is the rule you met in [[Adding_And_Subtracting_Integers]]. Multiplying by a negative number is repeated subtraction. Four copies of a negative number removed is the same as four copies of its opposite added. So removing four copies of $-3$ gives $+12$.

A third way, if you prefer pattern recognition: watch the sequence $(-3)\cdot 3,\ (-3)\cdot 2,\ (-3)\cdot 1,\ (-3)\cdot 0,\ (-3)\cdot(-1),\ \dots$ The products are $-9, -6, -3, 0, ?$ Each step increases the product by $3$. The next term in the pattern has to be $3$, which forces $(-3)\cdot(-1) = 3$. Any consistent extension of the multiplication rules to negatives requires this.

Division inherits the sign rule because division is the inverse of multiplication. Asking "what is $(-12) \div (-4)$?" is the same as asking "what number, times $-4$, gives $-12$?" The answer is $3$, a positive number. Any way you arrive at the sign rules for multiplication, the division rules follow for free.

## Worked examples

### Example 1: A single product

Compute $(-6)(-7)$.

Pull the signs off. The magnitudes are $6$ and $7$, so the absolute value of the answer is $6 \cdot 7 = 42$.

Now the sign. Both factors are negative — same signs — so the product is positive. Attach the sign:

$$
(-6)(-7) = 42.
$$

Answer: $42$.

### Example 2: A chain of signs

Compute $(-2)(3)(-4)$.

First do the arithmetic on the magnitudes: $2 \cdot 3 \cdot 4 = 24$. That is the size of the answer, ignoring signs.

Now count the negative factors. The factors are $-2$, $3$, and $-4$. Two of them are negative ($-2$ and $-4$); one is positive ($3$). Two is an even count, so the chain has an even number of flips, which means the overall sign is positive.

$$
(-2)(3)(-4) = +24 = 24.
$$

You can double-check by multiplying left to right. $(-2)(3) = -6$ (different signs, negative). Then $(-6)(-4) = 24$ (same signs, positive). Either path gives the same answer.

Answer: $24$.

## Common mistakes

- **Forgetting to flip when signs differ.** Computing $7 \cdot (-2)$ as $14$ instead of $-14$. The magnitudes are right, but the sign was dropped. Always handle the sign and the magnitude as separate decisions.
- **Thinking $(-)(-) = -$.** A stubborn misconception. Two negatives make a positive in multiplication and division every time. If you get this wrong, check the pattern argument above until it feels inevitable.
- **Miscounting signs in a chain.** When there are four or five factors, it is easy to lose track. Circle each negative sign, count the circles, and the answer's sign is positive for an even count or negative for an odd count.
- **Trying to divide by zero.** Any time a denominator hits zero, stop. There is no numerical answer. Watch for hidden zeros — a variable expression might look harmless until the value that would make the bottom zero shows up.
- **Confusing $-3^2$ with $(-3)^2$.** Without parentheses, exponents bind tighter than the minus sign, so $-3^2 = -(3^2) = -9$. With parentheses, $(-3)^2 = (-3)(-3) = 9$. This one bites almost every student at least once.

## Prerequisites

Before practicing these problems, make sure you are comfortable with:

- [[Integers_And_The_Number_Line]] — you need to recognize integers, their signs, and their absolute values.
- [[Adding_And_Subtracting_Integers]] — the intuition for sign changes under subtraction carries straight over into why multiplication behaves the way it does.

If either topic is fuzzy, work through it first and then come back.

## Problems Involving This Topic

Pick a problem type, choose a difficulty, choose how many you want, and click **Add to Vault**. Your selections stay in this browser. When you are ready, open your [[Vault]] to see them all, view hints and answers, and print a worksheet.

<div class="problem-vault-widget" data-topic-slug="multiplying_and_dividing_integers"></div>

_More problem types are coming soon._

## See also

- [[Integers_And_The_Number_Line]]
- [[Adding_And_Subtracting_Integers]]
- [[Order_Of_Operations_With_Integers]]
- [[Multiplying_Fractions]]
- [[Algebra_Overview]]
- [[Topics_Overview]]
- [[Vault|Your Practice Vault]]
- [[_overview|Home]]

## Sources in the ingested textbooks

- **Math I**, Chapter 2, Section 2.4 — integer multiplication and division sign rules.
