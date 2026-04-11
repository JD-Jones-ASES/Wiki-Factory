---
title: "Correlation and Residuals"
type: topic
aliases: ["Correlation Coefficient", "Residual Plot", "Linear Fit Quality", "Goodness Of Fit"]
tags: ["#branch-algebra-2", "#topic-statistics", "#topic-linear", "#skill-visualization", "#skill-procedural-calculation", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algebra_2", chapter: "11", section: "11.2"}
related:
  - "topics/algebra/Scatter_Plots_And_Trend_Lines"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Modeling_With_Linear_Functions"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Slope"
  - "topics/algebra/Histograms_And_Box_Plots"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Scatter_Plots_And_Trend_Lines"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Slope"
problem_type_ids: []
figures: ["algebra/residual_plot_pattern.svg"]
summary: "The correlation coefficient r, how to compute and interpret a residual, and how to read a residual plot to decide whether a linear model fits."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Correlation and Residuals

# Correlation and Residuals

Once you have drawn a trend line through a scatter plot (see [[Scatter_Plots_And_Trend_Lines]]), two natural questions hover in the background. First: *how well* does the line actually capture the pattern in the data --- is this a tight fit or a loose one? Second: *is a line even the right shape* to use, or is the data bent into some other curve that a straight line will miss? The correlation coefficient answers the first question with a single number between $-1$ and $1$. **Residuals**, together with the **residual plot**, answer the second by showing the errors the line is still making and asking whether those errors look random or systematic.

---

## The correlation coefficient

For a set of paired data $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$, the **correlation coefficient**, written $r$, is a single number that reports two things at once.

- **Sign.** Positive $r$ indicates a scatter plot that trends upward (larger $x$ goes with larger $y$). Negative $r$ indicates a scatter plot that trends downward (larger $x$ goes with smaller $y$).
- **Strength.** The absolute value $|r|$, on a scale from $0$ to $1$, says how tightly the points cluster around the trend line. Values near $1$ (or $-1$) mean the points sit nearly on a straight line. Values near $0$ mean the points are a formless cloud with no linear pattern at all.

A few informal benchmarks most algebra textbooks agree on:

| $|r|$ range | Strength of linear relationship |
|--------------|----------------------------------|
| $0.00$ to $0.30$ | Weak or no linear relationship |
| $0.30$ to $0.70$ | Moderate linear relationship |
| $0.70$ to $1.00$ | Strong linear relationship |

So $r = 0.92$ describes a strong positive relationship; $r = -0.85$ describes a strong negative one; $r = 0.14$ describes essentially no linear relationship, no matter what the points may look like casually.

Two cautions that matter on every standardized test question about $r$:

1. **$r$ only detects *linear* patterns.** A scatter plot that bends into a clean U-shape can have $r$ very close to zero even though the two variables are perfectly related --- the bending just isn't a straight line, and $r$ can't see it. Always look at the scatter plot, not just the number.
2. **$r$ is not a percent.** An $r$ of $0.6$ does not mean the line explains "$60\%$ of the relationship." The standard "percent of variation explained" quantity is $r^2$, not $r$ itself.

### Compared to $r^2$

The square of the correlation, $r^2$, is called the **coefficient of determination**. In a linear regression, $r^2$ reports the fraction of the variability in $y$ that the regression line accounts for. A linear fit with $r^2 = 0.81$ explains about $81\%$ of the variation in the $y$-values, leaving $19\%$ attributable to other factors or noise. Algebra 2 questions usually stay at the level of $r$ itself, but you will meet $r^2$ again in [[Linear_Regression]] and in any later statistics course.

---

## Residuals: the error of a single prediction

Once you have a trend line --- or a regression line computed by a calculator --- every data point $(x_i, y_i)$ has a **predicted value** $\hat{y}_i$ that comes from plugging $x_i$ into the line's equation. The **residual** at that point is the vertical gap between where the point actually landed and where the line said it would land:

$$
\text{residual}_i = y_i - \hat{y}_i.
$$

The sign matters. A **positive residual** means the actual data point is *above* the trend line --- the line undershot. A **negative residual** means the actual point is *below* the line --- the line overshot. A residual of zero means the point landed exactly on the line.

For a single data point, the residual is just one number. For a whole data set, you can build a list of residuals, one per observation, and plot them.

---

## The residual plot

A **residual plot** is a scatter plot in its own right: the horizontal axis shows the explanatory variable $x$ (or, equivalently, the predicted value $\hat{y}$), and the vertical axis shows the residual $y - \hat{y}$. Every original data point gives one dot on the residual plot. A horizontal reference line at $0$ marks where the trend line lives.

The residual plot is the deciding tool for a very specific question: *is a linear model appropriate for this data?*

Describe two cases.

### Random cloud around zero: linear model is appropriate

If the residual plot looks like a shapeless cloud hovering around the $0$ line --- with no trend, no curve, no fan-out --- then the linear model has squeezed all the pattern out of the data. What remains is random noise, which is exactly what residuals should look like when the line is doing its job. In this case, a linear model is an appropriate choice.

![[residual_plot_pattern.svg|Residual plot showing a clear pattern, not random scatter]]

### Visible pattern (curve or fan): linear model is not appropriate

If the residual plot shows a visible pattern --- a U-shape, an upside-down U, a steady tilt, or a fan that widens as $x$ grows --- then the linear model missed something systematic. A curve in the residual plot means the underlying relationship is curved, not straight, and a linear fit is leaving real structure in the errors. A fan that widens with $x$ means the spread of $y$ is growing with $x$ (statisticians call this *non-constant variance*), and a simple linear model will overstate its confidence for the large-$x$ part of the data. Either way, a linear model is not the right tool. A better fit would be a quadratic, exponential, or other non-linear model --- topics that show up in [[Quadratic_Functions]], [[Linear_Regression]], and later precalculus courses.

The workflow is worth memorizing. First fit a line. Then look at the residual plot. If the plot is a random cloud, keep the line. If the plot has a clear pattern, the line is wrong and you need a different family of curves.

---

## Key ideas

- **Correlation $r$ summarizes a linear relationship in one number.** It reports both the direction (via its sign) and the tightness (via its absolute value). Outside the linear setting, $r$ is not trustworthy.
- **Correlation is not causation.** Two variables can move together without one causing the other. This was hammered in [[Scatter_Plots_And_Trend_Lines]] and is just as true here: a strong $r$ does not prove a causal link.
- **A residual is a *signed* vertical distance.** Actual minus predicted. Above the line is positive; below the line is negative. Getting the sign backward is the most common slip on this topic.
- **The residual plot tests the shape of the fit, not its quality.** A random cloud says the linear shape is right (even if $r$ is not especially strong). A patterned residual plot says the linear shape is wrong (even if $r$ looks high at first glance).
- **Look at pictures, not just numbers.** A dataset can have a misleadingly nice $r$ and still be a terrible fit for a line; the only way to catch this is by looking at the scatter plot and the residual plot.

---

## Example 1: Classifying a scatter pattern

> Imagine four described scatter plots. Plot W shows "hours of weekly tutoring" versus "end-of-semester grade" for $40$ students, with a cloud that climbs steadily from lower left to upper right and sits tightly around an imaginary line. Plot X shows "outdoor temperature" versus "gas company heating bill" across a winter, with a cloud that falls sharply from upper left to lower right, also tight. Plot Y shows "student height" versus "number of text messages sent per day" for $30$ students, with points scattered in every direction. Plot Z shows "number of free kicks taken" versus "goals scored" for a small soccer team, with a cloud that tilts mildly upward but is spread out. Classify each by strength and direction.

Describe what the correlation coefficient would roughly look like in each case.

- **Plot W.** A tight cloud that rises steadily has a **strong positive** correlation. The $r$-value would sit somewhere around $0.85$ to $0.95$. Each additional hour of tutoring lines up with a fairly predictable grade increase.
- **Plot X.** A tight cloud that falls from upper left to lower right has a **strong negative** correlation, with $r$ near $-0.85$ or so. As the temperature rises, the heating bill falls in a consistent, predictable way.
- **Plot Y.** A formless cloud with no obvious tilt has **no meaningful linear relationship**. The correlation coefficient would sit near $0$, perhaps between $-0.2$ and $0.2$. Knowing a student's height tells you nothing about their texting volume.
- **Plot Z.** A spread-out cloud that rises only mildly has a **weak positive** correlation. An $r$ around $0.35$ to $0.50$ is about right. More free kicks trend toward slightly more goals, but the point-to-point noise is large.

Notice how sign and strength are two separate pieces. Plots W and X are both "strong," just in opposite directions. Plot Z is the same direction as W but noticeably looser.

---

## Example 2: Computing a single residual

> A regression line fitted to a town's data on average daily temperature $x$ (in degrees Fahrenheit) and bottled-water sales $y$ (in cases) is $\hat{y} = 2.4 x - 78$. On one particular day the temperature was $92$ degrees and the actual sales were $168$ cases. Compute the residual for that day and interpret what the sign means.

**Predicted value.** Plug $x = 92$ into the regression equation:

$$
\hat{y} = 2.4(92) - 78 = 220.8 - 78 = 142.8 \text{ cases}.
$$

**Residual.** Subtract the prediction from the actual:

$$
\text{residual} = y - \hat{y} = 168 - 142.8 = 25.2 \text{ cases}.
$$

**Interpretation.** The residual is **positive**, which says the actual sales on this day sat *above* the regression line's prediction. In concrete terms, the regression model predicted about $143$ cases for a $92$-degree day, but the town actually sold about $168$ cases --- the model undershot by $25.2$ cases. A single positive residual like this does not mean the model is wrong; some points will always sit above the line while others sit below it. The model would only be in trouble if many residuals in the same part of the data all pointed the same direction, which would show up on the residual plot as a visible pattern instead of random scatter.

---

## Example 3: Reading a residual plot

> A linear regression is fit to the relationship between a car's age $x$ (in years) and its resale price $y$ (in dollars). The residual plot shows points that are tightly clustered above the zero line for cars less than $4$ years old, dip well below the zero line for cars between $5$ and $9$ years old, then climb back above the zero line for cars older than $10$ years. Determine whether a linear model is appropriate for this data, and describe what a better approach would look like.

Describe the pattern first. The residuals are *not* scattered randomly around zero. Instead they trace a curve: up, then down, then up again, in a shape that looks like a wide U or a shallow wave when you follow the dots across the plot. The residuals are systematically positive on the ends and systematically negative in the middle.

**Is a linear model appropriate?** **No.** A scatter that is genuinely linear should produce a residual plot with no discernible pattern --- just random dots hovering around zero. The wave-like pattern here is a signal that the underlying relationship between car age and resale price is curved, not straight. The line is predicting too low for young cars, too high for middle-aged cars, and too low again for old cars.

**Describe a better approach.** A curved model is needed. Car depreciation classically follows an **exponential decay** pattern: prices drop quickly in the first few years, then level off. Fitting an exponential model $y = a \cdot b^x$ (where $0 < b < 1$) to the data would likely produce a residual plot that looks much more like a random cloud, which is what a good fit is supposed to do. Alternatively, a quadratic or other non-linear curve might capture the bend. What you should *not* do is accept the linear fit just because it gave a nonzero $r$ --- the residual plot is telling you the line is missing the real shape of the data.

---

## Common pitfalls

- **Confusing $r$ with a percent.** An $r$ of $0.6$ is *not* "$60\%$ correlation." The "percent of variation explained" quantity is $r^2 = 0.36$, or $36\%$. Whenever a question asks for a percent, check whether they want $r$ or $r^2$.
- **Trusting $r$ on a curved data set.** The correlation coefficient only detects *linear* patterns. A clean parabola can have $r$ near zero while the two variables are perfectly related. Always look at the scatter plot before committing to a linear model.
- **Getting the residual sign backward.** The formula is *actual minus predicted*, in that order. Swapping them flips every sign in the data set and reverses any interpretation you try to give.
- **Mixing up a good fit with a tight one.** A tight cloud gives a high $|r|$, but a curved tight cloud still fails the linear-model test. Conversely, a loose but unpatterned cloud can be an appropriate setting for a linear model even if $r$ is not especially high.
- **Reading a residual plot as a scatter plot.** The residual plot is not the original data. It is the *errors* of the line, and the thing you are checking for is whether those errors look random. The moment you see a curve, a tilt, or a fan, the linear fit is suspect.
- **Treating correlation as causation.** Even a rock-solid $r = 0.98$ does not prove that $x$ causes $y$. A lurking third variable is always a possibility. This is repeated from [[Scatter_Plots_And_Trend_Lines]] because it is tested on almost every standardized exam.

---

## Prerequisites

Before practicing with this page, be comfortable with:

- [[Scatter_Plots_And_Trend_Lines]] --- the scatter plots you will be reading come from this earlier topic
- [[Writing_Linear_Equations]] --- so you can set up the equation of a regression line and plug in values
- [[Slope]] --- the slope of the regression line gives the unit of change used in prediction

Afterwards, [[Linear_Regression]] formalizes the process of finding the best-fit line by calculator, and [[Modeling_With_Linear_Functions]] shows how the regression equation gets interpreted in the language of the original problem.

---

## Problems Involving Correlation and Residuals

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="correlation_and_residuals"></div>

---

## See Also

- [[Scatter_Plots_And_Trend_Lines]]
- [[Writing_Linear_Equations]]
- [[Linear_Functions]]
- [[Modeling_With_Linear_Functions]]
- [[Slope]]
- [[Linear_Regression]]
- [[Histograms_And_Box_Plots]]
- [[Sampling_Methods_And_Bias]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
