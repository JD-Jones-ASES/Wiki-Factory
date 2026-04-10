---
title: "Dividing Decimals"
type: topic
aliases: ["Decimal Division", "Dividing With Decimals"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "5", section: "5.4"}
related:
  - "topics/pre_algebra/Adding_And_Subtracting_Decimals"
  - "topics/pre_algebra/Multiplying_Decimals"
  - "topics/pre_algebra/Dividing_Fractions"
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Decimal_Place_Value_And_Comparing_Decimals"
  - "topics/pre_algebra/Multiplying_Decimals"
problem_type_ids: []
figures: []
summary: "How to divide decimals by sliding the decimal point so the divisor becomes a whole number."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Dividing Decimals

# Dividing Decimals

Dividing decimals sounds scary until you notice it is just whole-number division in disguise. If you can do $72 \div 9$, you can do $7.2 \div 0.9$. The trick is to slide the decimal point in both numbers by the same amount so the divisor becomes a whole number. Once that shift is done, you divide exactly like you always have and drop the decimal point back into the answer in the right spot.

## What it means

Division asks: *how many copies of the divisor fit inside the dividend?* When one or both numbers have a decimal point, the question is still the same. For example, $1.5 \div 0.25$ is asking how many quarters (each worth $0.25$) fit into $1.5$. The answer is $6$, the same as it would be if you rewrote the problem as $150 \div 25$.

That rewriting is the whole game. You are not changing the answer — you are simply choosing a cleaner form of the same problem.

## The rule

For any decimal division $a \div b$, first count how many digits sit after the decimal point of $b$. Slide the point in $b$ that many places to the right — this turns $b$ into a whole number. Then slide the point in $a$ the **same** number of places to the right, padding with zeros on the end if $a$ runs out of digits. Now divide the two whole-looking numbers normally, and put the point in your answer directly above its new spot in $a$.

In symbols, if you are computing $a \div b$ where $b$ has $n$ digits after the decimal point, the equivalent whole-divisor problem is:

$$
a \div b \;=\; \frac{a \times 10^{n}}{b \times 10^{n}}
$$

For dividing by a power of ten, there is a shortcut: slide the decimal point in the dividend one place to the **left** for each zero in the power of ten.

$$
x \div 10 = \text{shift left 1}, \quad x \div 100 = \text{shift left 2}, \quad x \div 1000 = \text{shift left 3}
$$

## Why it works

Multiplying both the top and the bottom of a fraction by the same number never changes the value of the fraction. Division is a fraction: $a \div b = \tfrac{a}{b}$. When you multiply both $a$ and $b$ by $10$ (or $100$, or $1000$), the quotient is unchanged:

$$
\frac{a}{b} \;=\; \frac{a \times 10}{b \times 10}
$$

So shifting the decimal point in the divisor and dividend by the same number of places is just multiplying both by the same power of ten. You pick the power of ten that makes the divisor whole, because whole-number division is much easier.

## Worked examples

### Example 1: A clean one-shift problem

Compute $7.2 \div 0.9$.

**Step 1.** The divisor is $0.9$, which has one digit after the decimal point. Shift the decimal one place to the right in both numbers:

$$
7.2 \div 0.9 \;=\; 72 \div 9
$$

**Step 2.** Now it is simple whole-number division: $72 \div 9 = 8$.

**Step 3.** Since the rewritten problem had no decimal point to place, the answer is just $8$.

**Check.** Does $0.9 \times 8 = 7.2$? Yes. Done.

### Example 2: A two-shift problem with a decimal answer

Compute $3.15 \div 0.25$.

**Step 1.** The divisor $0.25$ has two digits after its point, so slide **both** numbers' decimals two positions rightward:

$$
3.15 \div 0.25 \;=\; 315 \div 25
$$

**Step 2.** Do the whole-number division. $25$ goes into $315$ how many times? $25 \times 12 = 300$, with $15$ left over. Since there is a remainder, keep dividing by annexing a zero: $150 \div 25 = 6$. So the full quotient is $12.6$.

**Step 3.** Write the result.

$$
3.15 \div 0.25 \;=\; 12.6
$$

**Check.** $0.25 \times 12.6 = 3.15$. Good.

### Example 3: Dividing by a power of ten

Compute $48.7 \div 100$.

$100$ has two zeros, so slide the decimal point in $48.7$ two places to the left:

$$
48.7 \div 100 \;=\; 0.487
$$

If you run out of digits while sliding left, pad with zeros — for instance, $5.2 \div 1000 = 0.0052$.

## Common mistakes

- **Shifting only one of the numbers.** If you move the decimal in the divisor but forget the dividend, you have changed the problem. Always shift both by the same count.
- **Forgetting to line up the decimal point in the quotient.** After you rewrite the problem, place the decimal point in the answer directly above its new spot in the dividend. A misplaced point turns $3.2$ into $32$ or $0.32$.
- **Sliding the wrong direction for powers of ten.** Dividing by $10$ makes a number *smaller*, so the decimal point moves **left**. Multiplying by $10$ makes it bigger — the point moves right. Mixing these up is the single most common slip.
- **Stopping too early.** If there is a remainder and the problem expects a decimal answer, annex zeros in the dividend and keep dividing until the remainder is zero or the pattern repeats.
- **Losing a zero when padding.** If the dividend is shorter than the divisor after shifting, write in any needed zeros rather than dropping digits.

## Prerequisites

Before you practice dividing decimals, make sure you have these down:

- [[Decimal_Place_Value_And_Comparing_Decimals]] — you need to read decimal positions fluently so you know where the point lands in your answer.
- [[Multiplying_Decimals]] — you will use multiplication to check every division, and the decimal-shift logic is closely related.

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="dividing_decimals"></div>

_More problem types are coming soon._

## See also

- [[Adding_And_Subtracting_Decimals]]
- [[Multiplying_Decimals]]
- [[Dividing_Fractions]]
- [[Place_Value_Rounding_And_Estimation]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]

## Sources in the ingested textbooks

- **Math I** — Chapter 5, Section 5.4: Dividing Decimals
