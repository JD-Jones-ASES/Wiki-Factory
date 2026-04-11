---
title: "Data Displays and Measures of Spread"
type: topic
aliases: ["Box Plot", "Histogram", "Five-Number Summary", "IQR", "Outliers"]
tags: ["#branch-pre-algebra", "#topic-statistics"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "9", section: "9.5"}
related:
  - "topics/pre_algebra/Data_Displays"
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Data_Displays"
problem_type_ids: []
figures: ["pre_algebra/box_plot.svg"]
summary: "Histograms, box plots, quartiles, IQR, and the outlier rule: tools for numeric data spread."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Data Displays and Measures of Spread

# Data Displays and Measures of Spread

The first round of [[Data_Displays|data displays]] — bar graphs, pie charts, line graphs — handles categories and time. But what if your data is *already numeric*, and you want to see the whole shape of the distribution? That's where **histograms** and **box plots** step in. Both are designed for numeric data, and both put the emphasis on **spread** — how tightly or loosely the values cluster — instead of just reporting a single "average." Once you can read these two displays and can compute the **interquartile range** and the **outlier fences**, you've got the core toolkit for thinking about real data sets the way statisticians do.

---

## Histograms vs. bar graphs

A **histogram** looks like a bar graph at first glance, but there's a crucial difference: the bars represent **numeric intervals (bins)**, not categories. Bin boundaries are consecutive, so the bars touch — there's no gap between them, and that touching is the visual signal that the horizontal axis is a continuous number line instead of a set of labels.

- **Bar graph:** horizontal axis shows categories (colors, sports, states). Bars don't touch.
- **Histogram:** horizontal axis shows numeric bins (e.g., $60$–$69$, $70$–$79$, $80$–$89$). Bars touch.

The height of each bar in a histogram is the **frequency**: how many data points fell into that bin. A histogram is the right tool when you want to see where numeric values pile up and where they thin out.

**Quick example.** Twenty-eight students take a test. Their scores are grouped into four bins:

| Bin | Frequency |
|-----|-----------|
| 60–69 | 3 |
| 70–79 | 8 |
| 80–89 | 12 |
| 90–100 | 5 |

The tallest bar sits over the $80$–$89$ bin, so the class performed best there. Adding the bin heights gives $3 + 8 + 12 + 5 = 28$ total students, which matches the class size. Everyone who scored below $70$ is visible at a glance (just the first bar, $3$ students).

---

## The five-number summary

A **box plot** (sometimes called a box-and-whisker plot) is a compact picture of five key values pulled from a sorted data set:

- **Minimum** — the smallest value
- **First quartile $Q_1$** — the median of the lower half
- **Median $Q_2$** — the middle value of the whole list
- **Third quartile $Q_3$** — the median of the upper half
- **Maximum** — the largest value

These five numbers together are the **five-number summary**, and the difference between the outer quartiles gives the **interquartile range (IQR)**:

$$
\text{IQR} = Q_3 - Q_1.
$$

The IQR is the width of the middle $50\%$ of the data. It's a much better measure of spread than the range because a single extreme value can't hijack it — the quartiles ignore the top and bottom quarters of the list entirely.

A third measure of spread you'll occasionally see is the **mean absolute deviation (MAD)** — the average of the absolute distances between each value and the mean — but in middle school the heavy lifting is done by the IQR.

---

## Key ideas

- **Histograms are for numeric data in ranges.** If your horizontal axis is categories, you want a bar graph. If it's a number line chopped into intervals, you want a histogram.
- **The five-number summary orders itself.** Once you sort the data, the minimum is at one end, the maximum is at the other, and the median sits dead center. Quartiles are then just "medians of the halves."
- **IQR is the ruler for spread.** A small IQR means the middle $50\%$ is tightly packed. A large IQR means the middle $50\%$ is wide.
- **Box plots make side-by-side comparisons easy.** Stacking two or three box plots for related groups shows differences in center *and* in spread at the same time.
- **Outliers live beyond the fences.** A common informal rule: a value is flagged as an outlier when it sits more than $1.5 \times \text{IQR}$ past either quartile. Past $Q_3 + 1.5 \cdot \text{IQR}$ is high, past $Q_1 - 1.5 \cdot \text{IQR}$ is low.

---

## Example 1: Building a box plot from scratch

Here's a data set — number of minutes $11$ students spent on homework yesterday:

$$
10,\ 45,\ 22,\ 18,\ 30,\ 55,\ 12,\ 40,\ 25,\ 35,\ 20.
$$

**Step 1 — Sort.** Always begin by putting the values in increasing order:

$$
10,\ 12,\ 18,\ 20,\ 22,\ 25,\ 30,\ 35,\ 40,\ 45,\ 55.
$$

**Step 2 — Identify the minimum and maximum.** The smallest value is $10$, the largest is $55$.

**Step 3 — Find the median $Q_2$.** With $11$ values, the median sits at position $6$. Counting in: $10, 12, 18, 20, 22, \mathbf{25}$. So $Q_2 = 25$.

**Step 4 — Find $Q_1$.** The lower half (everything below the median) is $\{10, 12, 18, 20, 22\}$. That's five values; its median is the third one, $18$. So $Q_1 = 18$.

**Step 5 — Find $Q_3$.** The upper half is $\{30, 35, 40, 45, 55\}$. The median of those five values is $40$. So $Q_3 = 40$.

**Step 6 — Compute the IQR.**

$$
\text{IQR} = Q_3 - Q_1 = 40 - 18 = 22.
$$

**The five-number summary:** Minimum $= 10$, $Q_1 = 18$, Median $= 25$, $Q_3 = 40$, Maximum $= 55$.

**Step 7 — Draw the box plot.** Above a number line that spans $10$ to $55$:

```
     10      18     25           40         55
      |--+---[======|=============]----+-----|
      |      |      |             |          |
     min    Q1    median         Q3         max
     <-- whisker -->             <-- whisker -->
                    <--------- box ---------->
```

The **box** runs from $Q_1 = 18$ to $Q_3 = 40$. A line inside the box marks the median at $25$. Two **whiskers** stretch from the box out to the minimum at $10$ and the maximum at $55$. The middle $50\%$ of students fall between $18$ and $40$ minutes — a spread of $22$ minutes — while the overall range is $55 - 10 = 45$ minutes.

![[box_plot.svg|Box plot with five-number summary]]

---

## Example 2: Checking for outliers with the $1.5 \times \text{IQR}$ fences

Suppose a different data set has $Q_1 = 25$ and $Q_3 = 55$. Is the value $110$ an outlier?

**Step 1 — Compute the IQR.**

$$
\text{IQR} = 55 - 25 = 30.
$$

**Step 2 — Compute $1.5 \times \text{IQR}$.**

$$
1.5 \times 30 = 45.
$$

**Step 3 — Set the fences.** The **upper fence** sits $45$ above $Q_3$, and the **lower fence** sits $45$ below $Q_1$:

$$
\text{upper fence} = Q_3 + 45 = 55 + 45 = 100,
$$

$$
\text{lower fence} = Q_1 - 45 = 25 - 45 = -20.
$$

**Step 4 — Check the value.** Is $110$ beyond a fence? Yes: $110 > 100$, so $110$ is past the upper fence. That flags it as an outlier.

You can also check the other end. Is $-30$ an outlier? Yes, because $-30 < -20$. Is $0$ an outlier? No, because $-20 \leq 0 \leq 100$.

The fences give you an objective, reproducible way to decide whether a value is "just big" or "suspiciously big." It's not the only definition of "outlier" in statistics, but it's the standard informal rule taught in middle school.

---

## Example 3: Comparing two classes with box plots

Two math classes take the same test. Their five-number summaries look like this:

| | Min | $Q_1$ | Median | $Q_3$ | Max |
|---|---|---|---|---|---|
| **Class A** | 58 | 68 | 78 | 88 | 98 |
| **Class B** | 70 | 74 | 80 | 84 | 92 |

**Which class has a higher typical score?** Compare medians: Class B's median is $80$, Class A's is $78$. Class B edges out Class A on typical performance.

**Which class is more spread out?** Compute each IQR. Class A has $\text{IQR} = 88 - 68 = 20$, while Class B has $\text{IQR} = 84 - 74 = 10$. Class A's middle $50\%$ is twice as wide as Class B's. The overall ranges also show the same story: Class A spans $98 - 58 = 40$ points, Class B spans $92 - 70 = 22$ points.

**Interpretation.** Class B is more consistent — most students cluster tightly around $80$. Class A has both higher highs *and* lower lows; performance is much more variable. A teacher looking at these two plots would see that Class B needs less remediation overall but might also have fewer students who can take on a hard enrichment problem.

This side-by-side comparison is exactly what box plots were built for. Two numbers (one median, one IQR) per group let you compare center *and* spread in a single glance.

---

## Common pitfalls

- **Forgetting to sort before computing quartiles.** Quartiles come out of a sorted list. Using the original order gives nonsense.
- **Including the median when you split the list to find the quartiles.** With an odd number of data points, the median is a single middle value; leave it *out* when you form the lower and upper halves. With an even number, the median is the average of two middle values, and both halves keep all their values.
- **Mixing up range and IQR.** Range measures extreme-to-extreme width (max minus min). IQR measures the middle $50\%$. They answer different questions about spread.
- **Treating a histogram like a bar graph.** In a histogram the bars must touch because the bins are consecutive intervals. Leaving gaps implies you're looking at categories, which misrepresents numeric data.
- **Calling every extreme value an outlier.** The fence rule depends on the IQR — two data sets with the same extremes but different IQRs will disagree about whether a value is an outlier. Always compute the fences before labeling.
- **Letting the median alone tell the whole story.** Two groups can share a median but differ wildly in spread. Reporting IQR (or the full five-number summary) alongside the median gives a fairer picture.

---

## Prerequisites

- [[Mean_Median_Mode_And_Range]] — for the basic measures of center and the simple range
- [[Data_Displays]] — for bar graphs, line graphs, and pie charts, which histograms and box plots build on

---

## Problems Involving Data Displays and Measures of Spread

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="data_displays_and_measures_of_spread"></div>

---

## See Also

- [[Data_Displays]]
- [[Mean_Median_Mode_And_Range]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
