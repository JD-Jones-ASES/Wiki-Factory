---
title: "Decimal Place Value and Comparing Decimals"
type: topic
aliases: ["Decimal Place Value", "Comparing Decimals", "Reading Decimals"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "5", section: "5.1"}
related:
  - "topics/pre_algebra/Adding_And_Subtracting_Decimals"
  - "topics/pre_algebra/Multiplying_Decimals"
  - "topics/pre_algebra/Dividing_Decimals"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
  - "topics/pre_algebra/Integers_And_The_Number_Line"
problem_type_ids: []
figures: []
summary: "Naming the places after the decimal point and using them to compare decimals digit by digit."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Decimal Place Value and Comparing Decimals

# Decimal Place Value and Comparing Decimals

A decimal point is a small dot that does a big job: it tells you where whole numbers end and fractional parts begin. Every digit to the right of the point stands for a piece smaller than one, and the pieces shrink by a factor of ten each step you take to the right. Once you can read the places out loud, comparing two decimals becomes a quick left-to-right scan of their digits.

## What it means

To the **left** of the decimal point, place values climb: ones, tens, hundreds, thousands. To the **right** of the decimal point, place values shrink in the same rhythm: tenths, hundredths, thousandths, ten-thousandths. The first place after the point is one-tenth ($\tfrac{1}{10}$) of one, the next is one-hundredth ($\tfrac{1}{100}$), and so on.

Here is a small place-value table for the number $62.4835$:

| Place | Tens | Ones | . | Tenths | Hundredths | Thousandths | Ten-thousandths |
|---|---|---|---|---|---|---|---|
| Digit | 6 | 2 | . | 4 | 8 | 3 | 5 |

Read it out loud as "sixty-two and four thousand eight hundred thirty-five ten-thousandths". The word *and* marks the location of the decimal point.

You can also write a decimal in three common forms:

- **Standard form:** $62.4835$
- **Expanded form:** $60 + 2 + 0.4 + 0.08 + 0.003 + 0.0005$
- **Word form:** sixty-two and four thousand eight hundred thirty-five ten-thousandths

## The rule

To compare two decimals, line up their decimal points and pad with trailing zeros so both numbers have the same number of digits after the point. Then scan digit by digit from **left to right**. The first place where the digits differ decides which decimal is larger.

$$
\text{Compare } 0.5 \text{ and } 0.45 \;\Longrightarrow\; \text{rewrite as } 0.50 \text{ and } 0.45
$$

For the ordering direction:

$$
0.50 > 0.45 \quad \text{because at the tenths place, } 5 > 4
$$

Adding trailing zeros never changes a decimal's value:

$$
0.5 \;=\; 0.50 \;=\; 0.500
$$

For decimals that may be negative, use the same digit-by-digit idea but remember: on the [[Integers_And_The_Number_Line|number line]], *more negative* means *smaller*. So $-0.7$ is less than $-0.3$, not greater.

## Why it works

Each place after the decimal is worth ten times less than the place to its left. That means the **leftmost** place of disagreement carries more weight than every place after it combined. If two decimals match in the tenths but differ in the hundredths, the difference is at most $0.09$. But a difference of even $1$ in the tenths is worth $0.1$, which is already bigger. So once you find the first place where the digits differ, you never need to look further — that place decides the winner.

Padding with trailing zeros just puts the two numbers on the same footing so the comparison is fair. It is the decimal version of saying "line up the columns before you compare".

## Worked examples

### Example 1: The $0.5$ vs. $0.45$ trap

Which is larger, $0.5$ or $0.45$? A common gut reaction is "$45$ is bigger than $5$, so $0.45$ must be bigger". That reasoning ignores place value — those digits live in different columns.

**Step 1.** Line up the decimal points and pad so both numbers show two places:

$$
0.50 \quad \text{vs.} \quad 0.45
$$

**Step 2.** Scan from the left. Both numbers start with $0$ in the ones place. Move to the tenths: $5$ vs. $4$. Since $5 > 4$, stop right there.

**Step 3.** Conclude:

$$
0.5 \;>\; 0.45
$$

**Intuition check.** Think of money. $0.5$ dollars is $50$ cents; $0.45$ dollars is $45$ cents. Fifty cents is clearly more.

### Example 2: Ordering three decimals, including a negative

Put $-0.3$, $0.25$, and $0.2$ in order from least to greatest.

**Step 1.** Any negative number is less than any positive number, so $-0.3$ is already the smallest. Set it aside.

**Step 2.** Compare the two positives, $0.25$ and $0.2$. Pad $0.2$ to $0.20$ so both have two decimal places:

$$
0.25 \quad \text{vs.} \quad 0.20
$$

At the tenths place both show $2$. Move to the hundredths: $5$ vs. $0$. Since $5 > 0$, we have $0.25 > 0.2$.

**Step 3.** Put everything together in order from least to greatest:

$$
-0.3 \;<\; 0.2 \;<\; 0.25
$$

### Example 3: Naming a decimal place

In the number $14.0706$, which digit is in the thousandths place?

Count positions to the right of the decimal point: first place is tenths ($0$), second is hundredths ($7$), third is thousandths ($0$), fourth is ten-thousandths ($6$). So the thousandths digit is $\mathbf{0}$. The zero matters — it is holding the thousandths place open so the following $6$ lands correctly in ten-thousandths.

## Common mistakes

- **Judging by length.** Students often assume a longer decimal is larger, so they declare $0.123 > 0.5$. Not true — more digits does not mean a bigger value.
- **Ignoring trailing zeros vs. leading zeros.** A **trailing** zero at the end of a decimal does not change its value: $0.40 = 0.4$. A **leading** zero between the decimal point and the first nonzero digit absolutely does: $0.04$ is very different from $0.4$.
- **Forgetting the word "and".** In word form, "and" marks the decimal point — not an addition. "Three and five tenths" is $3.5$, not $3 + 5$.
- **Reading negative decimals backwards.** $-0.8$ is less than $-0.2$, even though $8 > 2$. Negatives flip the usual size ordering.
- **Padding on the wrong side.** You can add zeros to the right of the last decimal digit without changing value, but you cannot sprinkle zeros anywhere you want — placing one in the middle changes the number completely.

## Prerequisites

Before this topic, you should already be comfortable with:

- [[Place_Value_Rounding_And_Estimation]] — the whole-number side of place value is the foundation decimals build on.
- [[Integers_And_The_Number_Line]] — negative decimals rely on knowing how negatives behave on a number line.

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="decimal_place_value_and_comparing_decimals"></div>

_More problem types are coming soon._

## See also

- [[Adding_And_Subtracting_Decimals]]
- [[Multiplying_Decimals]]
- [[Dividing_Decimals]]
- [[Fractions_Decimals_And_Percents]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]

## Sources in the 

- **Math I** — Chapter 5, Section 5.1: Decimal Place Value and Comparing Decimals
