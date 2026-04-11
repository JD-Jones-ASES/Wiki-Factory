---
title: "Mean, Median, Mode, and Range"
type: topic
aliases: ["Measures of Center", "Average Median Mode"]
tags: ["#branch-pre-algebra", "#topic-statistics"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "9", section: "9.6"}
related:
  - "topics/pre_algebra/Data_Displays"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
  - "topics/pre_algebra/Dividing_Fractions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
  - "topics/pre_algebra/Dividing_Fractions"
problem_type_ids: []
figures: []
summary: "Four quick numbers that summarize a data set: average, middle, most common, and spread."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Mean, Median, Mode, and Range

# Mean, Median, Mode, and Range

A raw list of numbers — game scores, daily rainfall, quiz grades — can be overwhelming. **Summary statistics** squeeze that list down into a handful of numbers that answer quick questions: *What's typical? What's most common? How spread out are the values?* Four of these summaries do most of the work in pre-algebra: **mean**, **median**, **mode**, and **range**. Each one tells you something slightly different, and the trick is knowing which one to trust in which situation.

---

## The four summaries

| Statistic | What it tells you | How to compute it |
|-----------|------------------|--------------------|
| **Mean** $\bar{x}$ | The arithmetic average | Add all values, divide by the count |
| **Median** | The middle value of the sorted list | Sort, then take the center (or average the two center values if the count is even) |
| **Mode** | The value(s) that occur most often | Count how often each value appears; pick the winner(s) |
| **Range** | How far apart the extremes sit | Largest value minus smallest value |

The first three are called **measures of center** — they try to pin down a single "typical" value. The fourth, range, is a crude **measure of spread**: it tells you how wide the data stretches from smallest to largest.

In symbols, if your data set is $x_1, x_2, \ldots, x_n$, then the mean is

$$
\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}.
$$

---

## Key ideas

- **Sort before you look for the median.** The center of an *unsorted* list is almost never the median. This is the number-one slip students make.
- **Mode counts can vary.** Some data sets have zero modes (when every value is unique), exactly one mode, or even two or three (when multiple values tie for "most frequent"). A set with exactly two modes is called **bimodal**.
- **The mean is pulled toward extreme values; the median is not.** A single huge number can drag the mean way off while leaving the median untouched. That stability is why house prices, incomes, and test-score reports almost always quote the median.
- **Range is about width, not center.** Two data sets can have the same mean and median but wildly different ranges. Range is the first hint of how spread out the numbers are.

---

## Example 1: All four on a small data set

Compute the mean, median, mode, and range of the quiz scores

$$
7,\ 9,\ 6,\ 8,\ 9,\ 10,\ 9,\ 7.
$$

**Sort first.** Ordered, the scores read $6, 7, 7, 8, 9, 9, 9, 10$. Sorting takes two seconds and saves a lot of confusion.

**Mean.** Add everything and divide by $n = 8$:

$$
\bar{x} = \frac{6 + 7 + 7 + 8 + 9 + 9 + 9 + 10}{8} = \frac{65}{8} = 8.125.
$$

**Median.** There are $8$ values (an even count), so the median sits between positions $4$ and $5$. Those values are $8$ and $9$, so

$$
\text{median} = \frac{8 + 9}{2} = 8.5.
$$

**Mode.** Scan the sorted list: $9$ shows up three times, more than any other value. The mode is $9$.

**Range.** Largest minus smallest: $10 - 6 = 4$.

So this data set clusters around a center of about $8.1$ to $8.5$, most students scored a $9$, and the scores span a width of $4$ points.

---

## Example 2: Outliers pull the mean but spare the median

Seven friends compare how much money is in their wallets (in dollars):

$$
12,\ 14,\ 15,\ 16,\ 18,\ 20,\ 200.
$$

One friend just cashed a birthday check, and that $\$200$ is an **outlier** — a value sitting far from the rest of the pack. Watch what happens.

**Mean.**

$$
\bar{x} = \frac{12 + 14 + 15 + 16 + 18 + 20 + 200}{7} = \frac{295}{7} \approx 42.14.
$$

**Median.** With $7$ values sorted, the middle is the $4$th entry: $16$.

The mean says "typical wallet has about $\$42$," which is absurd — nobody except the outlier has anywhere near $\$42$. The median reports $\$16$, which matches what your eyes tell you from the raw list.

This is exactly why news stories about housing, salaries, and net worth almost always report the **median** rather than the mean. A handful of billionaires or mansions would otherwise drag the mean into fantasyland. The rule of thumb: if you suspect your data has outliers, trust the median for "typical."

---

## Example 3: Working backward to find a missing score

Jordan's first four test scores are $82, 88, 91, 77$. What does Jordan need to score on the fifth test to finish with an overall mean of exactly $85$?

Let the unknown fifth score be $x$. The mean of all five tests must satisfy

$$
\frac{82 + 88 + 91 + 77 + x}{5} = 85.
$$

Sum the known scores: $82 + 88 + 91 + 77 = 338$. The equation becomes

$$
\frac{338 + x}{5} = 85.
$$

Multiply both sides by $5$:

$$
338 + x = 425.
$$

Subtract $338$ from both sides:

$$
x = 87.
$$

**Check.** $(82 + 88 + 91 + 77 + 87)/5 = 425/5 = 85.$ Good. Jordan needs an $87$.

Any "what-grade-do-I-need-on-the-final?" problem is this same setup in disguise. Write the mean as a fraction, set it equal to the target, and solve for the missing value.

---

## Common pitfalls

- **Forgetting to sort before finding the median.** Grabbing the middle of an unsorted list gives the "middle item of the list" rather than the actual middle-sized value. Always order first.
- **Confusing mode with "mean-ish" values.** The mode is the value that appears *most often*, not the value nearest the average. On a data set like $1, 2, 2, 2, 100$ the mode is $2$, even though the mean is $21.4$.
- **Reporting the wrong number of values.** When you calculate the mean, $n$ must equal how many numbers you actually added, not how many appear in a tally chart or frequency table.
- **Treating range as a measure of center.** Range describes width, not typicality. A data set with range $50$ can be "narrow around $100$" or "narrow around $1{,}000{,}000$" — the range tells you nothing about where the values sit.
- **Letting an outlier hijack the mean without noticing.** If the mean and median disagree by a lot, stop and look at the data. An outlier is almost always the cause, and you usually want the median in that case.

---

## Prerequisites

Before tackling practice problems, you'll want to be comfortable with:

- [[Adding_And_Subtracting_Integers]] — for summing data sets that include negatives
- [[Dividing_Fractions]] — the mean is a division of a sum by a count, and that division often leaves a fraction or decimal

---

## Problems Involving Mean, Median, Mode, and Range

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="mean_median_mode_and_range"></div>

---

## See Also

- [[Data_Displays]]
- [[Data_Displays_And_Measures_Of_Spread]]
- [[Dividing_Fractions]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
