---
title: "Adding and Subtracting Decimals"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "5", section: "5.5.2"}
related:
  - "topics/pre_algebra/Multiplying_Decimals"
  - "topics/pre_algebra/Dividing_Decimals"
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
  - "topics/pre_algebra/Converting_Between_Fractions_And_Decimals"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Decimal_Place_Value_And_Comparing_Decimals"
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
problem_type_ids: []
figures: []
summary: "Add and subtract decimals by lining up the decimal points."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Adding and Subtracting Decimals

# Adding and Subtracting Decimals

If you have ever counted change at a cash register, you have already added decimals. A receipt with items like $3.79, $1.54, and $0.89 is really a decimal addition problem, and the cashier's drawer is a subtraction problem waiting to happen. The friendly thing about money is that it pins every value to exactly two places after the point, so you rarely stop to think about what "lining things up" means. Once the problem leaves the world of dollars and cents, those alignment habits matter even more.

This page is about the mechanics of that alignment and the single rule that makes decimal addition and subtraction work every time.

---

## What it means

Adding or subtracting decimals is the same operation you already know for whole numbers, but now some of the digits sit to the right of a decimal point. The value of a digit depends entirely on its column: a $7$ in the tenths column is worth $0.7$, a $7$ in the hundredths column is worth $0.07$, and a $7$ in the thousandths column is worth $0.007$. To combine two numbers faithfully, you must add digits that represent the same size of piece — tenths with tenths, hundredths with hundredths, and so on.

Whole-number arithmetic hides this requirement because the ones column lines up automatically on the right edge. Decimals force you to be explicit.

---

## The rule

Follow these steps and you will not miss:

1. Stack the numbers vertically with the decimal points directly above one another.
2. If one number has fewer digits after the point than the other, attach trailing zeros so every number shows the same number of decimal places. (Attaching a trailing zero never changes a decimal's value — $0.3$ and $0.30$ are the same number.)
3. Bring the decimal point straight down into the answer row, in the same column.
4. Add or subtract column by column from right to left, carrying or regrouping exactly as you would for whole numbers.

The decimal point's position is the only new thing. Once you have lined it up, the arithmetic is ordinary.

---

## Why it works

Column arithmetic works because every column represents a specific place value, and addition is allowed to combine only quantities of the same kind. When you stack a $5$ in the tenths column above a $3$ in the tenths column, you are saying "five tenths plus three tenths." That lands in the tenths column as "eight tenths" without any conversion.

If you lined the numbers up by their right edges instead of by the decimal point, you might end up adding tenths to hundredths, which is nonsense in the same way that adding feet to inches directly would be. The decimal point is your place-value anchor; keeping it vertical keeps every column honest.

Attaching trailing zeros is just a reminder to yourself. Writing $2.7$ as $2.70$ does not add any value to the number, but it fills in an empty hundredths column with a clear "$0$ hundredths" so you can see what you are subtracting from. See [[Decimal_Place_Value_And_Comparing_Decimals]] for more on why this is safe.

---

## Worked examples

### Example 1: Adding two decimals (align the points)

Suppose you want to add $2.6$ and $14.38$.

**Step 1.** Stack the numbers with the decimal points aligned. The shorter number gets a trailing zero so both show two digits after the point:

$$
\begin{array}{r}
  \phantom{1}2.60 \\
  +\ 14.38 \\
  \hline
\end{array}
$$

**Step 2.** Add each column from right to left. Hundredths: $0 + 8 = 8$. Tenths: $6 + 3 = 9$. Ones: $2 + 4 = 6$. Tens: nothing plus $1$ gives $1$. Drop the decimal point straight down:

$$
\begin{array}{r}
  \phantom{1}2.60 \\
  +\ 14.38 \\
  \hline
  16.98
\end{array}
$$

The sum is $16.98$. A quick sanity check: $2.6$ is close to $3$ and $14.38$ is close to $14$, so the answer should be near $17$. It is.

### Example 2: Subtracting with borrowing across the decimal point

Now try $9.2 - 4.57$.

**Step 1.** Stack the numbers and attach a trailing zero so both have two decimal places:

$$
\begin{array}{r}
  \phantom{1}9.20 \\
  -\ 4.57 \\
  \hline
\end{array}
$$

**Step 2.** Work right to left. The hundredths column asks for $0 - 7$, which you cannot do without regrouping. Borrow one tenth from the tenths column: the $2$ tenths becomes $1$ tenth, and the $0$ hundredths becomes $10$ hundredths. Now subtract: $10 - 7 = 3$ in the hundredths column.

**Step 3.** The tenths column is now $1 - 5$, which again needs a borrow. Take one whole from the ones column: $9$ ones becomes $8$ ones, and the $1$ tenth becomes $11$ tenths. Subtract: $11 - 5 = 6$ in the tenths column.

**Step 4.** The ones column is now $8 - 4 = 4$. Bring the decimal point straight down:

$$
\begin{array}{r}
  \phantom{1}9.20 \\
  -\ 4.57 \\
  \hline
  4.63
\end{array}
$$

The difference is $4.63$. Estimate check: $9 - 5 = 4$, and the exact answer is a little over $4$. Good.

### Example 3: Adding several decimals of different lengths

Here is one that mixes short and long decimals: $5.3 + 0.74 + 12.006$.

Attach zeros so everything shows three decimal places, then add:

$$
\begin{array}{r}
  \phantom{1}5.300 \\
  \phantom{1}0.740 \\
  +\ 12.006 \\
  \hline
  18.046
\end{array}
$$

The total is $18.046$. Notice how the trailing zeros made the thousandths column safe to add even though two of the three numbers had nothing written there originally.

---

## Common mistakes

- **Lining up the last digits instead of the decimal points.** Right-edge alignment is a whole-number habit that silently destroys decimal arithmetic. Always align by the point.
- **Forgetting a trailing zero.** A problem like $1.2 - 0.35$ must be rewritten as $1.20 - 0.35$ before you start regrouping. Skipping the zero invites an off-by-one-place error.
- **Dropping the decimal point from the answer.** Once you have committed to a column layout, the answer's decimal point belongs in the same column as the input points. Draw it straight down before you read off the answer.
- **Treating a whole number as if it had no decimal point.** If the problem is $12 - 3.47$, rewrite $12$ as $12.00$ so the columns line up. The whole number has a decimal point; it is just invisible on the right of the ones place.

---

## Prerequisites

Before practicing problems from this page, make sure you are comfortable with:

- [[Decimal_Place_Value_And_Comparing_Decimals]] — reading a decimal by its column names
- [[Place_Value_Rounding_And_Estimation]] — rounding whole numbers and estimating sums so you can sanity-check your answers

If either of those is shaky, start there first and come back.

---

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="adding_and_subtracting_decimals"></div>

_More problem types are coming soon._

---

## See also

- [[Multiplying_Decimals]] — the rule changes in an interesting way for products
- [[Dividing_Decimals]] — a close cousin that also leans on place value
- [[Adding_And_Subtracting_Fractions]] — a parallel universe where the common "denominator" replaces the decimal point
- [[Fractions_Decimals_And_Percents]] — moving between the two notations
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]

---

## Sources in the 

- **Math I** — Chapter 5 (Decimals), Section 5.2: Adding and Subtracting Decimals
