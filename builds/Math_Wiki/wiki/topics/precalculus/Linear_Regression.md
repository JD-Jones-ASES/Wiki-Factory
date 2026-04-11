---
title: "Linear Regression"
type: topic
aliases: ["Least Squares Line", "Best-Fit Line", "Regression Line"]
tags: ["#branch-pre-calculus", "#topic-statistics", "#topic-linear", "#key-topic", "#test-sat", "#test-act", "#test-psat"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Scatter_Plots_And_Trend_Lines"
  - "topics/algebra/Slope"
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Writing_Linear_Equations"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Slope"
  - "topics/pre_algebra/Slope_Intercept_Form"
  - "topics/algebra/Scatter_Plots_And_Trend_Lines"
problem_type_ids: []
figures: []
summary: "The least-squares regression line drops a straight line through a scatter plot so that the total squared vertical error is as small as possible, giving slope, intercept, and a correlation coefficient you can read in context."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Linear Regression

# Linear Regression

Look at any real dataset and you will see something the textbook examples rarely show: the points do not line up perfectly. A scatter of coffee-shop revenue against temperature, or final exam scores against hours studied, or plant height against days of sunlight — every one of them produces a cloud of dots that *nearly* follows a straight trend but never exactly. The job of linear regression is to put the best possible straight line through that cloud and then use the line as a summary of what the data is telling you.

The word "best" has to be pinned down, because there are many lines you could draw through a scatter plot. The standard answer is the **least-squares line**: the unique line $y = mx + b$ that makes the total of the squared vertical gaps between the points and the line as small as it can possibly be. Those vertical gaps are called **residuals**, and squaring them before summing serves two purposes. First, it keeps positive errors above the line from cancelling negative errors below the line. Second, it punishes a big miss more than several small ones, which is usually what you want when you care about reliable predictions.

$$
\hat y = m x + b, \qquad \text{residual}_i = y_i - \hat y_i = y_i - (m x_i + b).
$$

The hat on $\hat y$ is a notation that statisticians use to mean "predicted by the line" as opposed to $y_i$, which is the actual observed value. The residual is the signed vertical distance from the dot to the line, and the regression engine tunes $m$ and $b$ so that $\sum (y_i - \hat y_i)^2$ is the smallest it can be.

---

## Reading slope and intercept in context

The algebra of the line is nothing new — you are back in [[Slope_Intercept_Form|slope-intercept form]]. What is new is that $m$ and $b$ now carry units and have to be interpreted against the problem you started with.

- **The slope $m$** measures how much $y$ is expected to change when $x$ increases by one unit. If $x$ is hours studied and $y$ is test score, a slope of $4.5$ means each extra hour of studying is associated with about $4.5$ more points on the test. Notice the careful phrase "is associated with" — regression describes a pattern; it does not prove that studying causes the score to rise.
- **The intercept $b$** is the predicted value of $y$ when $x = 0$. Sometimes that prediction is meaningful (predicted revenue when zero customers walked in: zero dollars, ideally). Sometimes it is nonsense (predicted weight of a person of height $0$ inches). Always ask whether the intercept is inside the range of the data before you attach any real-world meaning to it.
- **The line itself** is a prediction tool on the interval where the data lives. Plugging an $x$-value from inside the data range into $\hat y = m x + b$ is called **interpolation** and is generally safe. Plugging in an $x$-value far outside the range is called **extrapolation** and is genuinely risky — the linear trend that holds inside the data may not hold beyond it.

---

## The correlation coefficient $r$

A regression line comes with a companion number called the **correlation coefficient**, traditionally written $r$. It ranges from $-1$ to $1$ and captures two things at once:

- **The sign of $r$** tells you the direction. A positive $r$ means the line slopes up — as $x$ grows, $y$ grows. A negative $r$ means the line slopes down — as $x$ grows, $y$ shrinks.
- **The magnitude of $|r|$** tells you how tightly the points hug the line. $|r|$ near $1$ means the cloud is close to a perfect straight line (strong linear relationship). $|r|$ near $0$ means the points scatter all over the place, with little or no linear pattern at all.

A few rough bands you can use when describing a scatter:

| $|r|$ | Description of the fit |
|---|---|
| $0.9$ - $1.0$ | very strong linear pattern |
| $0.7$ - $0.9$ | strong |
| $0.4$ - $0.7$ | moderate |
| $0.0$ - $0.4$ | weak or none |

The value $r = 0$ does not mean "no relationship" — it means "no *linear* relationship". A scatter that traces out a clean parabola has $r$ very close to $0$ because the upward half cancels the downward half, even though the relationship between the variables is perfectly deterministic. Always look at the scatter before you trust $r$ to summarize it.

---

## Computing the least-squares line from a small dataset

For a by-hand calculation the standard formulas are

$$
m = \dfrac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2}, \qquad b = \bar y - m \bar x,
$$

where $\bar x$ and $\bar y$ are the sample means. The intercept formula guarantees that the regression line passes through the point $(\bar x, \bar y)$ — the centroid of the data cloud. That single fact is a useful sanity check: if you compute a line and it does not pass through the mean point, something went wrong in your arithmetic.

For anything beyond five or six data points you will use a calculator, spreadsheet, or statistics package instead of computing the sums by hand. On a TI-style graphing calculator the workflow is `STAT -> Edit` to enter the data, then `STAT -> CALC -> LinReg(ax+b)` to produce the slope, intercept, and $r$. Practicing with tiny datasets first, though, is the cleanest way to see why the formulas work.

---

## Example 1: fitting a line to a five-point dataset

> Maya tracks how many minutes she spends practicing piano each day and the number of pieces she can play cleanly by the end of the week. Five weeks of data:

| week | practice minutes per day ($x$) | pieces mastered ($y$) |
|---|---|---|
| 1 | $10$ | $2$ |
| 2 | $20$ | $3$ |
| 3 | $30$ | $5$ |
| 4 | $40$ | $6$ |
| 5 | $50$ | $8$ |

> Compute the least-squares line and interpret the slope.

Start by finding the two means. The $x$ values $10, 20, 30, 40, 50$ have mean $\bar x = 30$. The $y$ values $2, 3, 5, 6, 8$ sum to $24$, so $\bar y = 4.8$.

Now compute the deviations $x_i - \bar x$ and $y_i - \bar y$:

| $x_i$ | $y_i$ | $x_i - \bar x$ | $y_i - \bar y$ | $(x_i - \bar x)(y_i - \bar y)$ | $(x_i - \bar x)^2$ |
|---|---|---|---|---|---|
| $10$ | $2$ | $-20$ | $-2.8$ | $56$ | $400$ |
| $20$ | $3$ | $-10$ | $-1.8$ | $18$ | $100$ |
| $30$ | $5$ | $0$ | $0.2$ | $0$ | $0$ |
| $40$ | $6$ | $10$ | $1.2$ | $12$ | $100$ |
| $50$ | $8$ | $20$ | $3.2$ | $64$ | $400$ |

The totals are $\sum (x_i - \bar x)(y_i - \bar y) = 150$ and $\sum (x_i - \bar x)^2 = 1000$. So:

$$
m = \dfrac{150}{1000} = 0.15, \qquad b = 4.8 - (0.15)(30) = 4.8 - 4.5 = 0.3.
$$

The regression line is

$$
\hat y = 0.15 x + 0.3.
$$

The slope of $0.15$ says that each additional minute of daily practice is associated with about $0.15$ more pieces mastered by week's end. Equivalently, every extra $10$ minutes per day is associated with about $1.5$ more pieces. The intercept of $0.3$ is the model's prediction at zero practice — close to zero, which passes a sanity check, though predicting piano mastery from no practice at all is outside the data range and should not be taken seriously.

---

## Example 2: predicting a value from the regression line

> Using Maya's line $\hat y = 0.15 x + 0.3$, estimate how many pieces she would master in a week of practicing $35$ minutes per day.

Substitute $x = 35$:

$$
\hat y = 0.15(35) + 0.3 = 5.25 + 0.3 = 5.55.
$$

The model predicts about $5.55$ pieces — in practice, somewhere between $5$ and $6$. Because $x = 35$ falls comfortably inside the observed range of $10$ to $50$ minutes, this is an interpolation and is reasonable to trust as a rough estimate. If the question had asked about $x = 180$ minutes, the prediction of $\hat y = 0.15(180) + 0.3 = 27.3$ pieces would be extrapolation far beyond the data and would not deserve the same confidence — nothing in the dataset rules out a ceiling effect somewhere after an hour of daily practice.

---

## Example 3: reading a correlation coefficient from a described scatter

> Four scatter plots are described below. For each, estimate $r$ to the nearest tenth and describe the relationship in words.
>
> - **Plot A:** points form a nearly perfect straight line with positive slope; the biggest gap of any point from the line is tiny.
> - **Plot B:** points trend downward overall; the trend is clear, but there is noticeable spread around the line.
> - **Plot C:** points are scattered across the plane with no visible tilt in either direction.
> - **Plot D:** points follow a downward trend so tightly that the scatter looks almost like a single line.

Plot A has a positive slope (so $r > 0$) and very little scatter about the line (so $|r|$ is near the high end). A reasonable estimate is $r \approx 0.95$, a very strong positive linear relationship.

Plot B slopes downward ($r < 0$) with moderate spread. An estimate around $r \approx -0.6$ fits — a moderate-to-strong negative linear relationship.

Plot C has no visible tilt, so $r$ is near $0$. An estimate of $r \approx 0.1$ is appropriate, describing essentially no linear relationship.

Plot D slopes down ($r < 0$) and hugs the line tightly. Something like $r \approx -0.98$ captures a very strong negative linear relationship.

Notice the pattern: the sign comes from the direction of the slope, and the magnitude comes from how tightly the points hug the line. Those two judgments, taken together, are the correlation coefficient in words.

---

## Common pitfalls

- **Confusing correlation with causation.** A high $|r|$ tells you two variables move together; it does not tell you that one causes the other. Ice cream sales and drowning deaths are highly correlated in summer — because both are driven by hot weather, not because ice cream drives drowning.
- **Extrapolating off the edge of the data.** The line only summarizes the pattern inside the observed $x$ range. Running it out to $x = 100$ when your data only goes from $10$ to $50$ produces a prediction the data cannot actually support.
- **Reporting $r$ without looking at the plot.** A dataset with a clear nonlinear pattern can produce an $r$ near zero even when the variables are tightly related. $r$ measures only the *linear* part of the relationship.
- **Forgetting that the line passes through $(\bar x, \bar y)$.** If your computed regression line does not hit the centroid, a $\bar x$ or $\bar y$ arithmetic error is likely. Checking that $\bar y = m \bar x + b$ is a fast sanity check.
- **Using the intercept for prediction when $x = 0$ is outside the data range.** The intercept is what the line says, not what the phenomenon says. Interpret it cautiously.

---

## Prerequisites

- [[Slope_Intercept_Form]] — the algebraic form $y = mx + b$ that the regression line takes
- [[Slope]] — slope as a rate of change, which regression gives a real-world reading of
- [[Scatter_Plots_And_Trend_Lines|Scatter Plots and Trend Lines]] — the setting in which the line lives, a cloud of paired $(x, y)$ data

---

## Problems Involving Linear Regression

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="linear_regression"></div>

---

## See Also

- [[Scatter_Plots_And_Trend_Lines|Scatter Plots and Trend Lines]] — the graphical setting that regression summarizes with a single line
- [[Modeling_With_Linear_Functions|Modeling with Linear Functions]] — a deeper look at how slope and intercept get their meaning in context
- [[Slope_Intercept_Form]] — the algebra of a line, reinterpreted in data-fitting language
- [[Relations_And_Functions|Relations and Functions]] — linear models as one family of functions among many
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
