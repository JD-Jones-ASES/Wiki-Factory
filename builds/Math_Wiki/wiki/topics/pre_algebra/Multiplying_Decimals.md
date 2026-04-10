---
title: "Multiplying Decimals"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "5", section: "5.5.3"}
related:
  - "topics/pre_algebra/Dividing_Decimals"
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Decimal_Place_Value_And_Comparing_Decimals"
  - "topics/pre_algebra/Adding_And_Subtracting_Decimals"
problem_type_ids: []
figures: []
summary: "Multiply as if the factors were whole numbers, then place the decimal point by counting decimal places."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Multiplying Decimals

# Multiplying Decimals

Imagine you are buying $0.3$ pounds of cheese that costs $1.2$ dollars per pound. The answer should be a small number — less than half a pound of a one-dollar item can't cost much. If you reach for long division or a calculator, you will get $0.36$ dollars, or about thirty-six cents. What is interesting is that you can get that same answer without thinking about decimals at all for most of the work.

This is the secret of decimal multiplication: you are allowed to pretend the decimal points are not there while you multiply. You only have to put them back at the very end, and there is a simple counting rule for where they go. The whole operation is really two ideas glued together.

---

## What it means

When you multiply two decimals, you are multiplying two numbers that each happen to include fractional parts. Unlike addition and subtraction, there is no need to stack the decimal points in a column. Stacking by the point would actually get in your way. Instead, you handle the digits as whole numbers first, and then you figure out where the decimal point belongs in the product using place value.

The key observation is that every decimal is a whole number scaled down by a power of ten. Once you spot that, the method practically writes itself.

---

## The rule

Here is the complete procedure:

1. Temporarily ignore the decimal points. Multiply the two factors as if they were plain whole numbers.
2. Count how many digits sit to the right of the decimal point in the first factor. Call that $a$.
3. Count how many digits sit to the right of the decimal point in the second factor. Call that $b$.
4. Add: $a + b$. That sum is the number of decimal places the answer must have.
5. Starting from the right edge of your whole-number product, count $a + b$ places to the left and insert the decimal point there.

If the whole-number product does not have enough digits for the count, prepend zeros on the left until it does.

---

## Why it works

Any decimal can be rewritten as a whole number divided by a power of ten. For instance:

$$
1.2 = \frac{12}{10} \qquad 0.3 = \frac{3}{10} \qquad 0.045 = \frac{45}{1000}
$$

Now look at what happens when you multiply two decimals written in this form:

$$
1.2 \times 0.3 = \frac{12}{10} \times \frac{3}{10} = \frac{12 \times 3}{10 \times 10} = \frac{36}{100} = 0.36
$$

Two things jumped out of the algebra. First, the numerators were just the ordinary whole-number product $12 \times 3 = 36$ — the decimal points played no role there. Second, the denominators multiplied together too, producing $10 \times 10 = 100$. One place plus one place became two places in the denominator, and a denominator of $100$ means the answer has two decimal places.

This is exactly the counting rule. "Count the decimal places in the factors and add them" is a compact way of saying "the denominators are powers of ten, and powers of ten multiply by adding exponents." Every decimal multiplication is really a whole-number multiplication followed by a single division by a power of ten.

---

## Worked examples

### Example 1: A decimal times a decimal

Compute $1.2 \times 0.3$.

**Step 1.** Ignore the points and multiply as whole numbers: $12 \times 3 = 36$.

**Step 2.** Count decimal places. The factor $1.2$ has one digit after its point. The factor $0.3$ has one digit after its point. Total places: $1 + 1 = 2$.

**Step 3.** Place the decimal point two digits from the right of $36$. Since $36$ only has two digits, the point goes right in front of the $3$:

$$
1.2 \times 0.3 = 0.36
$$

Sanity check: about one-third of $1.2$ should give roughly $0.4$, and $0.36$ is in that neighborhood.

### Example 2: A whole number times a decimal

Compute $4 \times 2.75$.

**Step 1.** Ignore the point and multiply the digits: $4 \times 275 = 1100$.

**Step 2.** Count decimal places. The factor $4$ has zero digits after a point (it is a whole number). The factor $2.75$ has two digits after its point. Total: $0 + 2 = 2$.

**Step 3.** Starting from the right of $1100$, count two places left. The point lands between the two middle digits:

$$
4 \times 2.75 = 11.00 = 11
$$

The trailing zeros can be dropped because they do not change the value. A quick estimate confirms this: four times "a little under three" should be a little under twelve, and $11$ sits right where it belongs.

### Example 3: A product that needs padding with zeros

Compute $0.02 \times 0.4$.

**Step 1.** Whole-number product: $2 \times 4 = 8$.

**Step 2.** Count decimal places. The factor $0.02$ has two digits after its point. The factor $0.4$ has one. Total: $2 + 1 = 3$ decimal places in the answer.

**Step 3.** The whole-number product is just the single digit $8$. To place the decimal point three spots to the left of the right edge, you need to prepend zeros until there is room. Write $0.008$:

$$
0.02 \times 0.4 = 0.008
$$

The answer is eight thousandths. This matches intuition: multiplying two small-ish numbers often produces an even smaller one.

### Example 4: Multiplying by a power of ten

Compute $3.45 \times 100$.

Here the whole-number product is $345 \times 100 = 34500$. With two decimal places from $3.45$ and zero from $100$, the total is two decimal places, so count from the right: $345.00$, which is $345$.

There is a faster pattern worth noticing. Multiplying a decimal by $10$ shifts its point one place to the right; by $100$, two places to the right; by $1000$, three. Every zero in the power of ten corresponds to one hop rightward. This is the same rule in disguise — you are just tracking how the denominator $10^n$ cancels with the shifting point.

---

## Common mistakes

- **Trying to stack the decimal points in a column.** That is the rule for addition and subtraction. For multiplication, the point positions are irrelevant until the very end.
- **Counting decimal places in only one factor.** You must count digits after the point in **both** factors and add the two counts. Missing one is the single most common slip.
- **Forgetting to prepend zeros.** When the whole-number product is too short to hold the required count of decimal places, you need to pad on the left with zeros (see Example 3). Stopping at the existing digits gives an answer that is too big.
- **Cancelling a trailing zero too early.** Trailing zeros can be removed only after the decimal point is placed. If you drop them sooner, you lose track of the digit count.
- **Not sanity-checking the size.** Multiplying two numbers less than $1$ gives a number less than either of them. Multiplying a number greater than $1$ by a number less than $1$ shrinks it. If your answer has the wrong order of magnitude, you probably misplaced the point.

---

## Prerequisites

Before working through multiplication problems, make sure you are comfortable with:

- [[Decimal_Place_Value_And_Comparing_Decimals]] — knowing which column is tenths, hundredths, and thousandths
- [[Adding_And_Subtracting_Decimals]] — the warm-up that makes place-value reasoning automatic

If either of those feels shaky, swing by those pages first and come back.

---

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="multiplying_decimals"></div>

_More problem types are coming soon._

---

## See also

- [[Dividing_Decimals]] — the inverse operation, with its own decimal-placement trick
- [[Multiplying_Fractions]] — another way to reach the same answers, by turning the decimals into fractions first
- [[Place_Value_Rounding_And_Estimation]] — how to build a quick estimate to catch misplaced decimal points
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]

---

## Sources in the ingested textbooks

- **Math I** — Chapter 5 (Decimals), Section 5.3: Multiplying Decimals
