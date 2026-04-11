---
title: "Scatter Plots and Trend Lines"
type: topic
aliases: ["Line Of Best Fit", "Scatter Diagram", "Trend Line"]
tags: ["#branch-algebra-1", "#topic-linear", "#topic-statistics", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "4", section: "4.6"}
related:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/pre_algebra/Slope_As_Rate_Of_Change"
  - "topics/algebra/Slope"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Modeling_With_Linear_Functions"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/pre_algebra/Plotting_Points_And_The_Coordinate_Plane"
  - "topics/algebra/Slope"
  - "topics/algebra/Writing_Linear_Equations"
problem_type_ids: []
figures: ["algebra/scatter_trend_line.svg"]
summary: "Plot paired data, read the overall direction, sketch a line that captures the trend, and use it to predict."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Scatter Plots and Trend Lines

# Scatter Plots and Trend Lines

Real measurements almost never line up perfectly. When you collect data on two things at once — say, hours of sleep and next-morning alertness, or engine size and fuel economy — the points scatter. A **scatter plot** is nothing more than those paired measurements dropped onto the coordinate plane, one dot per observation. The dots rarely sit on a clean curve, but surprisingly often they cluster around a straight line. That line is the bridge between messy data and the algebra you already know.

![[scatter_trend_line.svg|Scatter plot with trend line]]

---

## Key ideas

A **scatter plot** is a graph of pairs $(x, y)$ in which $x$ is one measured quantity and $y$ is another, with each point representing a single observation. You do not connect the dots the way you would for the graph of an equation — the points are independent snapshots, not a function.

Once the dots are on the page, the first thing to look at is the **direction** of the cloud.

- **Positive correlation** — the cloud rises from lower-left to upper-right. As $x$ grows, $y$ tends to grow too.
- **Negative correlation** — the cloud falls from upper-left to lower-right. Larger $x$-values go with smaller $y$-values.
- **No correlation** — the dots look scattered randomly with no tilt. Knowing one variable tells you little about the other.

When the cloud has a clear direction, you can sketch a **trend line** — sometimes called a **line of best fit** — straight through the middle of it. The goal is not to hit every point — that is usually impossible — but to let the line run through the crowd so that roughly as many points sit above it as below it. Once drawn, the trend line is an ordinary linear equation $y = mx + b$, and you can read its slope and y-intercept using the tools from [[Slope]] and [[Writing_Linear_Equations]].

### What a trend line is good for

- **Describing the relationship.** The slope says how much $y$ changes for each unit of $x$, a real-world [[Slope|rate of change]] like "points per hour of study" or "gallons per mile".
- **Predicting.** Once you have the equation, you can plug in an $x$-value and estimate the matching $y$.
- **Comparing groups.** If two sets of data each get their own trend line, the slopes and intercepts give you a clean way to compare them.

### Interpolation vs. extrapolation

Predicting inside the range of your data is called **interpolation**, and it is usually reasonable — the trend line is supported by real observations on both sides. Predicting far outside the range is called **extrapolation**, and it is much riskier: the pattern that held for the observed data might bend, flatten, or break entirely at extreme values.

### Correlation is not causation

This is the single most important idea in the topic, and it stays with you for every science and statistics class that follows. A strong correlation between two variables only says that the numbers move together. It does **not** prove that changing one forces the other to change. There is usually a hidden third factor lurking behind the scenes.

Classic example: the number of beach drownings in a city each week is correlated with ice-cream sales in the same city. The two rise together and fall together, but buying an ice-cream cone does not cause anyone to drown. Both are caused by hot weather, which sends people both to the ice-cream counter and into the ocean. Before you claim that $x$ *causes* $y$, always ask whether some background variable might be driving both.

---

## Example 1: identifying the trend

> Seven students reported how many hours they practiced their instrument last week $(x)$ and their score out of $100$ on a weekly quiz $(y)$: $(1, 48)$, $(2, 55)$, $(3, 58)$, $(4, 66)$, $(5, 70)$, $(6, 78)$, $(7, 84)$. Describe the correlation.

Plot the seven points on a coordinate plane with hours on the horizontal axis and quiz scores on the vertical axis. The cloud moves steadily upward from left to right — more practice lines up with higher scores. The correlation is **positive**, and it looks strong because the points sit close to a straight-line pattern.

---

## Example 2: drawing a trend line and predicting

> Using the practice-and-score data from Example 1, draw a trend line, write its equation, and predict the score of a student who practices $9$ hours.

Eyeball a straight line through the middle of the cloud so about half the points fall above it and half below. Two convenient points the line passes near are $(1, 48)$ and $(7, 84)$. Use those to find the slope:

$$
m = \frac{84 - 48}{7 - 1} = \frac{36}{6} = 6.
$$

So each additional hour of practice seems to add about $6$ points to the quiz score. To find the y-intercept, start from $y = mx + b$ at one of the chosen points. Using $(1, 48)$:

$$
48 = 6(1) + b \implies b = 42.
$$

The equation of the trend line is

$$
y = 6x + 42.
$$

To predict the score for $9$ hours of practice, substitute $x = 9$:

$$
y = 6(9) + 42 = 54 + 42 = 96.
$$

The model predicts a score of about $96$ out of $100$. But notice that $x = 9$ sits beyond the largest observed value of $7$, so this is **extrapolation**, and a $96$ is not guaranteed. A prediction at, say, $x = 4.5$ would be much more trustworthy because it is inside the data range.

---

## Example 3: classifying three scatter plots

> Imagine three separate scatter plots. Plot A shows outdoor temperature $(x)$ versus hot-cocoa sales $(y)$ at a coffee cart: as it gets colder, sales shoot up. Plot B shows daily hours on social media $(x)$ versus hours of sleep $(y)$: heavier users sleep less. Plot C shows a student's shoe size $(x)$ versus their history test score $(y)$. For each plot, describe the correlation.

- **Plot A** shows a **negative** correlation: larger $x$ (warmer temperature) corresponds to smaller $y$ (fewer cocoas). The cloud slopes downward.
- **Plot B** also shows a **negative** correlation: more social-media time lines up with fewer hours of sleep.
- **Plot C** shows **no correlation**. Shoe size and history grade have nothing meaningful to do with each other, so the dots scatter without any tilt. (This is a good warning that finding two unrelated variables and expecting a trend line is not how data analysis works.)

And note the crucial caveat from Plot B: even though social media and sleep show a strong negative relationship, you cannot conclude from this data alone that scrolling *causes* the lost sleep. Busy students might both scroll more and have less time to sleep for the same underlying reason. Before jumping to cause and effect, you would need a carefully designed experiment — a topic you will meet in later statistics courses.

---

## Common pitfalls

- **Connecting the dots.** A scatter plot is not a line graph — leave the dots alone and sketch a single straight trend line through them.
- **Forcing a line through a cloud with no trend.** If the points do not tilt, there is no trend line to draw. "No correlation" is a valid answer.
- **Confusing correlation with causation.** Two variables that move together may both be driven by a third cause you are not measuring. Always ask why before you claim one causes the other.
- **Reckless extrapolation.** Predictions from a trend line are only trustworthy near the observed data. Pushing far beyond the range of $x$ can give nonsense answers, like test scores above $100$ or negative quantities.
- **Picking only the extreme points when fitting the line by eye.** Use points that lie near the middle of the cloud, not just the outliers.

---

## Prerequisites

Before you practice problems on this page, make sure you are solid on:

- [[Plotting_Points_And_The_Coordinate_Plane]] — you will be plotting data by the dozen.
- [[Slope]] — since the trend line's steepness *is* a slope.
- [[Writing_Linear_Equations]] — for turning two chosen points into $y = mx + b$.

Afterwards, [[Modeling_With_Linear_Functions]] and [[Linear_Functions]] take the same idea further, with more careful attention to units and the meaning of slope in context.

---

## Problems Involving Scatter Plots and Trend Lines

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="scatter_plots_and_trend_lines"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Slope]]
- [[Writing_Linear_Equations]]
- [[Linear_Functions]]
- [[Modeling_With_Linear_Functions]]
- [[Plotting_Points_And_The_Coordinate_Plane]]
- [[Slope]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
