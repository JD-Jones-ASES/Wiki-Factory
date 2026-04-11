---
title: "Data Displays"
type: topic
aliases: ["Graphs and Charts", "Statistical Displays"]
tags: ["#branch-pre-algebra", "#topic-statistics"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "9", section: "9.5"}
related:
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Finding_A_Percent_Of_A_Number"
  - "topics/pre_algebra/Adding_And_Subtracting_Integers"
problem_type_ids: []
figures: ["pre_algebra/histogram_example.svg"]
summary: "Bars, lines, slices, dots, and stems: pick the visual that matches the question you are asking."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Data Displays

# Data Displays

A table of numbers rarely tells you what a picture of those same numbers does at a glance. **Data displays** — bar graphs, line graphs, pie charts, pictographs, stem-and-leaf plots — turn lists into shapes your brain can read in a second. The trick is matching the display to the *kind* of data you have and the *question* you want to answer. The same numbers can look dramatically different depending on which graph you pick, and a poor choice can hide the very pattern you're trying to show.

---

## The main displays and when to pick each

| Display | Best for | What the axes mean |
|---------|----------|--------------------|
| **Bar graph** | Comparing separate categories | Horizontal axis lists categories; vertical axis shows amount |
| **Line graph** | Showing how a quantity changes over time | Horizontal axis = time; vertical = measured quantity |
| **Pie chart (circle graph)** | Showing parts of a single whole | Each wedge is a category's share of $100\%$ |
| **Pictograph** | Informal counts using small icons | Each icon stands for a fixed number of items |
| **Stem-and-leaf plot** | Numeric data where you want the actual values preserved | Leading digits = stems, final digits = leaves |

The decision tree is roughly: **categories?** bar graph. **Over time?** line graph. **Parts of a whole?** pie chart. **Small dataset where every value matters?** stem-and-leaf. **Informal, for a flyer or a poster?** pictograph. When your data is *numeric and continuous*, reach instead for a **histogram** (see [[Data_Displays_And_Measures_Of_Spread]]):

![[histogram_example.svg|A histogram of test scores]]

---

## Key ideas

- **Bar graphs compare discrete categories.** The bars do not touch — that gap is a signal that each bar represents a separate label (sport, color, flavor), not a range of numbers. Bar length shows amount.
- **Line graphs are for change over time.** Dots are plotted at each time point and connected in order. A rising line means growth, a falling line means decline, and a flat stretch means no change.
- **Pie charts must account for $100\%$ of the data.** Every slice together must cover the whole circle. If the categories overlap or skip part of the data, a pie chart is the wrong tool.
- **Pictographs need a key.** If one icon equals $5$ books, half an icon means $2.5$ books. Without that key, a pictograph is just decoration.
- **Stem-and-leaf plots keep the exact numbers.** Most graphs hide the raw values behind bars or dots. A stem-and-leaf plot shows the literal data while still revealing the shape of the distribution.
- **A misleading axis can lie to you.** If the vertical axis of a bar graph starts at, say, $95$ instead of $0$, tiny differences between bars look like huge gaps. Always check where the axis starts.

---

## Example 1: Reading a bar graph

A middle school surveys $40$ students about their favorite lunch item, and the results are drawn as a bar graph:

| Item | Count |
|------|-------|
| Pizza | 14 |
| Tacos | 10 |
| Salad | 6 |
| Sandwich | 8 |
| Other | 2 |

**How many students chose tacos?** Look at the top of the tacos bar — it lines up with the $10$ mark on the vertical axis. So $10$ students picked tacos.

**What fraction picked salad?** That's $6$ students out of $40$ total:

$$
\frac{6}{40} = \frac{3}{20} = 0.15 = 15\%.
$$

**Which item is least popular?** The shortest bar belongs to "Other" at $2$ students.

Bar graphs make these comparisons instant because your eye can scan across the tops of the bars instead of re-reading numbers in a table.

---

## Example 2: A pie chart for a monthly budget

A household has a monthly budget of $\$3{,}600$, split into these five categories:

| Category | Share |
|----------|-------|
| Housing | 40% |
| Food | 20% |
| Transportation | 15% |
| Utilities | 10% |
| Everything else | 15% |

A pie chart is perfect here because each category is a slice of a single whole ($100\%$ of the monthly budget). To find the dollar amount spent on transportation, compute the percentage of $\$3{,}600$:

$$
15\% \times \$3{,}600 = 0.15 \times 3{,}600 = \$540.
$$

The same idea works for any slice. Housing eats $0.40 \times 3{,}600 = \$1{,}440$, and food takes $0.20 \times 3{,}600 = \$720$. A quick sanity check: the five slices should add back to $\$3{,}600$, and they do: $1{,}440 + 720 + 540 + 360 + 540 = 3{,}600$.

When you see a pie chart, remember the rule: the *whole circle* is the total, and each slice is a percentage of that total. To pull an actual count or amount out of the chart, multiply the percentage by the total.

---

## Example 3: A stem-and-leaf plot of test scores

Here are the scores that $15$ students earned on a $100$-point history test:

$$
62,\ 71,\ 85,\ 88,\ 74,\ 92,\ 67,\ 78,\ 83,\ 91,\ 76,\ 85,\ 73,\ 88,\ 95.
$$

Eyeballing that list, it's hard to spot the shape. A **stem-and-leaf plot** splits each score into a **stem** (the tens digit) and a **leaf** (the ones digit), then lists them side by side:

```
Stem | Leaves
-----|-------
  6  | 2 7
  7  | 1 3 4 6 8
  8  | 3 5 5 8 8
  9  | 1 2 5
```

Read the $7$ row as $71, 73, 74, 76, 78$. The stem "$7$" combined with each leaf gives an exact two-digit value — no information is lost.

A few things jump out of this picture that the raw list hid:

- The $70$s and $80$s are the fullest rows — most students scored in those ranges.
- There's a small cluster in the $60$s (two students struggled) and a small cluster in the $90$s (three students aced it).
- Scores like $85$ and $88$ appear twice, which you can see because the same leaf shows up more than once in the row.

Stem-and-leaf plots are the champions of *information density*: for small-to-medium data sets, they pack the raw values, the order, the shape of the distribution, and repeated values into about four lines of text. They're also easy to draw by hand — no ruler needed.

---

## Common pitfalls

- **Picking a pie chart for data that doesn't add to a whole.** If your categories overlap or omit parts of the data, the circle is a lie. Use a bar graph instead.
- **Connecting points on a bar graph.** Bar graphs compare discrete categories — drawing a line from "pizza" to "tacos" would pretend the categories are on a numeric scale. They aren't.
- **Using a line graph for things that aren't over time.** A line graph implies order and change along the horizontal axis. Favorite colors or states visited are categories, not a timeline, so use a bar graph.
- **Skipping the pictograph key.** A row of five apple icons could mean five apples, fifty apples, or five hundred apples depending on the key. Always read the key first.
- **Trusting a bar graph whose axis doesn't start at zero.** A bar that looks twice as tall as another one might actually represent only a $5\%$ difference. Check the starting value of the vertical axis before you draw conclusions.

---

## Prerequisites

- [[Finding_A_Percent_Of_A_Number]] — for pulling dollar amounts and counts out of pie charts
- [[Adding_And_Subtracting_Integers]] — for checking totals and reading axes with negative values

---

## Problems Involving Data Displays

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="data_displays"></div>

---

## See Also

- [[Mean_Median_Mode_And_Range]]
- [[Data_Displays_And_Measures_Of_Spread]]
- [[Finding_A_Percent_Of_A_Number]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
