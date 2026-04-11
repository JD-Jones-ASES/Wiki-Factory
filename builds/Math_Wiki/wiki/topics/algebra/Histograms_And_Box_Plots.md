---
title: "Histograms and Box Plots"
type: topic
aliases: ["Five Number Summary", "Interquartile Range", "Frequency Distribution", "Whisker Plot"]
tags: ["#branch-algebra-1", "#topic-statistics", "#skill-visualization", "#skill-procedural-calculation", "#key-topic", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_1", chapter: "10", section: "10.3"}
related:
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
  - "topics/pre_algebra/Data_Displays"
  - "topics/algebra/Scatter_Plots_And_Trend_Lines"
  - "topics/algebra/Correlation_And_Residuals"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
  - "topics/pre_algebra/Data_Displays"
problem_type_ids: []
figures: ["algebra/box_plot_five_number.svg"]
summary: "Bin-based frequency pictures, the five-number summary, the IQR ruler for spread, and the 1.5 IQR outlier rule."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Histograms and Box Plots

# Histograms and Box Plots

Two numeric data displays do most of the heavy lifting in high-school statistics: the **histogram**, which shows the shape of the entire distribution at once, and the **box plot**, which compresses the same data into five anchor numbers and compares groups at a glance. They are designed to answer different questions. A histogram tells you where the values pile up, whether the distribution leans to one side, and whether there are any unusual gaps. A box plot tells you the middle, the middle half, and whether any points sit suspiciously far from the crowd. Becoming fluent with both --- and with the **interquartile range** that drives the outlier rule --- is a milestone for reading real data the way testing questions expect you to.

---

## Histograms: shape from binned frequencies

A histogram turns a list of numbers into a picture by first sorting them into **bins** --- consecutive intervals of equal width on the number line --- and then drawing a bar over each bin whose height is the count (the **frequency**) of data values that fell inside. Because the bins tile the number line with no gaps, the bars touch. That touching is the visual tell that the horizontal axis is a continuous quantity, not a list of categories.

Choosing bin width is a judgment call. Too narrow and every bar is one tall and one short; too wide and a handful of fat bars hide all the interesting wiggle. For most classroom datasets, between $5$ and $12$ bins is about right.

Once the histogram is drawn, you read three things off its **shape**.

- **Symmetric.** The left and right sides are roughly mirror images. A symmetric distribution often has its mean and median close together.
- **Skewed right (positively skewed).** A long tail stretches to the right. Most values sit in the lower bins; a few unusually large values drag the tail out. Mean sits noticeably above median.
- **Skewed left (negatively skewed).** A long tail stretches to the left. Most values sit in the upper bins; a few unusually small ones create the tail. Mean sits noticeably below median.
- **Uniform.** Every bar is roughly the same height. No single bin stands out, which tells you values are evenly spread across the whole range.
- **Bimodal.** Two distinct peaks with a valley between them. Usually a signal that the data is really a mixture of two different underlying groups.

You can also read specific counts: the number of data values in any given bar is just the bar's height, and the number in a range of bins is the sum of their heights.

---

## The five-number summary

A **box plot** (also called a **box-and-whisker plot**) compresses a data set down to five numbers, drawn above a number line. Together these five values are called the **five-number summary**.

- **Minimum** --- smallest value in the data.
- **First quartile $Q_1$** --- the median of the lower half of the data, i.e., the value with $25\%$ of the data at or below it.
- **Median $Q_2$** --- the middle value of the full sorted data set.
- **Third quartile $Q_3$** --- the median of the upper half, i.e., the value with $75\%$ of the data at or below it.
- **Maximum** --- largest value in the data.

To draw the plot itself, put a number line below the page, stretch a **box** from $Q_1$ to $Q_3$, cut a vertical line inside the box at the median, then extend two **whiskers** from the box out to the minimum and the maximum. The box covers the middle $50\%$ of the data; the whiskers cover the rest.

![[box_plot_five_number.svg|Box plot labeled with the five-number summary]]

The numeric width of the box is the **interquartile range**, written $\text{IQR}$ and computed as

$$
\text{IQR} = Q_3 - Q_1.
$$

Since the IQR ignores the top and bottom quarters of the data entirely, a single extreme value cannot pull it around the way it pulls the range. That stability makes the IQR the preferred measure of spread whenever a data set might contain outliers.

---

## Quartiles step by step

To compute the five-number summary by hand, sort the data first, then find the median as usual. With the median in place, the **lower half** is everything below it and the **upper half** is everything above it. The standard convention for an odd total: leave the single middle value *out* of both halves. The standard convention for an even total: split the list exactly in two; both halves contain half of the data.

Apply the same "middle value" procedure to each half:

- $Q_1$ is the median of the lower half.
- $Q_3$ is the median of the upper half.

If a half has an even count of values, $Q_1$ or $Q_3$ is the average of the two middle values of that half, exactly the way you handle the median of an even list.

---

## The outlier rule

A value is flagged as an **outlier** whenever it sits more than $1.5 \times \text{IQR}$ beyond a quartile. The two cutoff lines are called the **fences**:

$$
\text{upper fence} = Q_3 + 1.5 \cdot \text{IQR},
$$

$$
\text{lower fence} = Q_1 - 1.5 \cdot \text{IQR}.
$$

Any value **strictly greater** than the upper fence or **strictly less** than the lower fence is an outlier by this rule. Everything else is inside the fences and treated as normal variation. The $1.5$-IQR rule is not the only way to define "outlier" in statistics, but it is the standard informal rule used on standardized tests.

When a data set has outliers, modern box plots usually draw the whiskers only out to the **most extreme non-outlier** on each side, then mark each outlier individually with a dot beyond the whisker. For this course, either convention is acceptable as long as you can identify outliers and explain your reasoning.

---

## Example 1: Building a five-number summary

> Compute the five-number summary and the IQR of the following dataset of weights (in grams) for $9$ apples picked from a single tree: $142, 168, 155, 149, 175, 162, 158, 135, 170$.

**Sort.** Put the values in order first:

$$
135,\ 142,\ 149,\ 155,\ 158,\ 162,\ 168,\ 170,\ 175.
$$

**Minimum and maximum.** The smallest value is $135$ g and the largest is $175$ g.

**Median.** With $n = 9$ values, the median sits in position $5$ of the sorted list. Counting in from the left: $135, 142, 149, 155, \mathbf{158}$. So $Q_2 = 158$ g.

**Lower half.** With an odd total, leave the median out. The lower half is $\{135, 142, 149, 155\}$ --- four values. $Q_1$ is the average of the two middle values of this half, which are $142$ and $149$:

$$
Q_1 = \frac{142 + 149}{2} = \frac{291}{2} = 145.5 \text{ g}.
$$

**Upper half.** The upper half is $\{162, 168, 170, 175\}$ --- also four values. $Q_3$ is the average of its two middle values, $168$ and $170$:

$$
Q_3 = \frac{168 + 170}{2} = \frac{338}{2} = 169 \text{ g}.
$$

**IQR.**

$$
\text{IQR} = Q_3 - Q_1 = 169 - 145.5 = 23.5 \text{ g}.
$$

**Summary.** Minimum $= 135$, $Q_1 = 145.5$, Median $= 158$, $Q_3 = 169$, Maximum $= 175$, with an IQR of $23.5$ g. The middle $50\%$ of the apples weighs between roughly $145.5$ g and $169$ g --- a span only about half as wide as the full range of $40$ g from lightest to heaviest.

---

## Example 2: Reading counts off a histogram

> A described histogram shows daily step counts for $45$ participants in a fitness challenge, grouped into bins of width $2{,}000$ steps. The bar heights, from left to right, are: $\text{[2000, 4000)} = 2$, $\text{[4000, 6000)} = 5$, $\text{[6000, 8000)} = 11$, $\text{[8000, 10000)} = 14$, $\text{[10000, 12000)} = 9$, $\text{[12000, 14000)} = 4$. Determine how many participants took at least $8{,}000$ steps. Also describe the shape of the distribution.

**Counting values in a range.** "At least $8{,}000$ steps" means bins $[8000, 10000)$ through $[12000, 14000)$. Read those bar heights and add them:

$$
14 + 9 + 4 = 27 \text{ participants}.
$$

So $27$ of the $45$ participants --- that's $60\%$ --- walked at least $8{,}000$ steps on the measured day. As a check, the six bar heights should sum to the total number of participants: $2 + 5 + 11 + 14 + 9 + 4 = 45$. That matches the $45$ on the roster.

**Shape.** Scan the bars left to right. The heights start small ($2, 5$), rise steadily ($11, 14$), then fall off ($9, 4$). The tallest bar, $14$, sits in the $[8000, 10000)$ bin. The distribution is roughly **symmetric**, with a light left tail (a few low-step participants) and a light right tail (a few high-step participants). The "typical" participant walked somewhere in the $8{,}000$-step neighborhood, which is exactly where the peak sits.

---

## Example 3: Using the $1.5 \times \text{IQR}$ rule on a specific value

> A data set of daily coffee-shop transactions has a first quartile $Q_1 = 118$ and a third quartile $Q_3 = 186$. Determine whether a day with $310$ transactions counts as an outlier under the $1.5 \times \text{IQR}$ rule. Determine whether a day with $38$ transactions does.

**Step 1 --- Compute the IQR.**

$$
\text{IQR} = Q_3 - Q_1 = 186 - 118 = 68.
$$

**Step 2 --- Compute $1.5 \times \text{IQR}$.**

$$
1.5 \times 68 = 102.
$$

**Step 3 --- Build the fences.** The upper and lower fences are this step away from the outer quartiles:

$$
\text{upper fence} = 186 + 102 = 288,
$$

$$
\text{lower fence} = 118 - 102 = 16.
$$

**Step 4 --- Check each value.**

- *Is $310$ an outlier?* Compare $310$ to the upper fence $288$. Since $310 > 288$, it sits past the fence, so **yes**, $310$ is flagged as an outlier on the high side.
- *Is $38$ an outlier?* Compare $38$ to the lower fence $16$. Since $38 > 16$, it sits inside the fence, so **no**, $38$ is not flagged. It may look low compared to the middle $50\%$, but it does not reach the $1.5 \times \text{IQR}$ threshold.

This is the exact reasoning tested on a standardized math question: the rule is mechanical once you have $Q_1$ and $Q_3$, but it does not apply by "gut feel." Always compute the fences before declaring anything an outlier.

---

## Common pitfalls

- **Forgetting to sort.** Quartiles come out of a sorted list. Pulling values from the original order gives nonsense numbers that aren't true quartiles at all.
- **Including or excluding the median incorrectly.** On an odd-count data set, drop the median out of both halves when computing $Q_1$ and $Q_3$. On an even-count data set, both halves keep all of their values.
- **Confusing range with IQR.** Range is max minus min and responds to every outlier. IQR is $Q_3 - Q_1$ and ignores the top and bottom $25\%$. They answer different questions.
- **Misreading a histogram as a bar graph.** Histogram bars must touch because the bins tile a continuous axis. Bar-graph bars have gaps because the axis lists separate categories. Treating one as the other distorts the shape.
- **Declaring an outlier without computing fences.** "Way more than the others" is not a formal test. Compute $1.5 \times \text{IQR}$ and compare to the fences before labeling a value.
- **Assuming skewness and "lopsidedness" are the same.** The direction of the skew is the direction of the *long tail*, not the side where most of the data sits. A right-skewed histogram has most of its bars on the left and a long low-frequency tail stretching to the right.
- **Mixing up which display answers which question.** To see the full shape of a distribution, use a histogram. To compare two or more groups on center and spread, use side-by-side box plots. Both are correct; neither is universal.

---

## Prerequisites

Before tackling practice problems, be comfortable with:

- [[Mean_Median_Mode_And_Range]] --- medians and quartiles are just "medians of halves"
- [[Data_Displays_And_Measures_Of_Spread]] --- the middle-school version of this topic, which covers IQR and the fence rule in less depth
- [[Data_Displays]] --- bar graphs, line graphs, and pie charts that histograms extend

---

## Problems Involving Histograms and Box Plots

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="histograms_and_box_plots"></div>

---

## See Also

- [[Mean_Median_Mode_And_Range]]
- [[Data_Displays_And_Measures_Of_Spread]]
- [[Data_Displays]]
- [[Scatter_Plots_And_Trend_Lines]]
- [[Correlation_And_Residuals]]
- [[Sampling_Methods_And_Bias]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
