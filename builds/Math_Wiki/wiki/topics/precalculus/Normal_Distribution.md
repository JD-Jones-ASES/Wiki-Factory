---
title: "Normal Distribution"
type: topic
aliases: ["Bell Curve", "Gaussian Distribution", "Empirical Rule", "68-95-99.7 Rule", "Z-Score"]
tags: ["#branch-pre-calculus", "#topic-statistics", "#skill-estimation", "#skill-formula-substitution", "#key-topic", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "11", section: "11.3"}
related:
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
  - "topics/precalculus/Margin_Of_Error_And_Confidence_Intervals"
  - "topics/precalculus/Binomial_Probability"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
  - "topics/pre_algebra/Data_Displays_And_Measures_Of_Spread"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
problem_type_ids: []
figures: ["precalculus/normal_curve_empirical_rule.svg"]
summary: "The bell-shaped probability model — what its mean and standard deviation control, how the 68-95-99.7 rule lets you estimate percentages by hand, and how z-scores translate a raw value into standard units."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Normal Distribution

# Normal Distribution

Huge quantities of real-world data follow a characteristic shape when you plot a histogram: a single central peak, a roughly symmetric profile, and fading tails that drop off to either side. Heights of adult women, scores on a standardized reading test, the diameters of ball bearings off a factory line, the sum of two dozen dice rolls — all of these produce nearly identical silhouettes. That shared silhouette is the **normal distribution**, and learning to read it is one of the most practical skills in all of statistics.

A normal distribution is controlled by just two numbers: the **mean** $\mu$, which fixes where the peak sits on the number line, and the **standard deviation** $\sigma$, which fixes how wide the bell is. Change $\mu$ and the whole curve slides left or right without changing shape. Change $\sigma$ and the curve stretches out (large $\sigma$ — a wide, short bell) or squeezes in (small $\sigma$ — a tall, narrow spike). Every other feature of the curve — its total area, its symmetry, the ratios between percentages in different regions — stays locked.

![[normal_curve_empirical_rule.svg|Normal curve with 68-95-99.7 empirical rule bands]]

$$
\text{A normal distribution is fully specified by its mean } \mu \text{ and standard deviation } \sigma.
$$

---

## The 68-95-99.7 rule

Because every normal curve has the same shape, fixed percentages of the data always live in fixed bands around the mean — measured in standard deviations, not in raw units. The rule is so useful that it has a name: the **empirical rule**, sometimes called the **68-95-99.7 rule**.

- Roughly $68\%$ of the data sits within one standard deviation of the mean — between $\mu - \sigma$ and $\mu + \sigma$.
- Roughly $95\%$ sits within two standard deviations — between $\mu - 2\sigma$ and $\mu + 2\sigma$.
- Roughly $99.7\%$ sits within three standard deviations — between $\mu - 3\sigma$ and $\mu + 3\sigma$.

These three percentages are the only numbers you need to memorize for most hand-calculation questions on the topic. Everything else is arithmetic.

Two corollaries are worth writing down explicitly because they crop up over and over:

- Because the curve is symmetric, each of the three central bands splits evenly around the mean. The first band leaves $34\%$ of the data on each side of the mean (half of $68\%$). The second band leaves $47.5\%$ on each side (half of $95\%$). The third leaves $49.85\%$ on each side.
- Outside the three-sigma band, only about $0.3\%$ of the data remains — roughly $0.15\%$ in each tail.

A useful decomposition of the curve into six slices follows directly. Starting from the far left and moving right:

| Region | Percent of data |
|---|---|
| Below $\mu - 2\sigma$ | $2.5\%$ |
| Between $\mu - 2\sigma$ and $\mu - \sigma$ | $13.5\%$ |
| Between $\mu - \sigma$ and $\mu$ | $34\%$ |
| Between $\mu$ and $\mu + \sigma$ | $34\%$ |
| Between $\mu + \sigma$ and $\mu + 2\sigma$ | $13.5\%$ |
| Above $\mu + 2\sigma$ | $2.5\%$ |

Those six numbers sum to exactly $100\%$, and the symmetry is immediately visible in the table — the percentages run $2.5, 13.5, 34, 34, 13.5, 2.5$, which reads the same forward and backward. If you can reproduce that decomposition from memory, you can answer a huge fraction of empirical-rule questions without ever touching a calculator.

---

## Z-scores: translating raw values into standard units

To use the empirical rule on a specific data value, the first step is to measure that value **in units of $\sigma$** rather than in its original units. The conversion is called a **z-score**, and the formula is

$$
z = \dfrac{x - \mu}{\sigma}.
$$

A z-score of $0$ means the raw value $x$ sits right at the mean. A z-score of $+1$ means $x$ sits exactly one standard deviation above the mean. A z-score of $-2.5$ means $x$ sits two and a half standard deviations below the mean. The sign tells you the side of the mean; the magnitude tells you how many standard deviations away you are.

Z-scores have two enormous advantages. First, they strip units from the problem — a z-score is dimensionless, so you can legitimately compare a reading test result to a math test result to a shoe-size measurement, provided each comes from its own normal distribution. Second, they plug directly into the empirical rule: the rule is written in terms of multiples of $\sigma$, and a z-score is literally a count of $\sigma$s.

A quick mental sanity check whenever you compute a z-score: if $x > \mu$, the z-score must be positive; if $x < \mu$, the z-score must be negative. If your answer disagrees with that, you flipped a subtraction.

---

## Example 1: the central $68\%$ band

> A manufacturer's ball bearings have diameters that are normally distributed with mean $\mu = 100$ millimeters and standard deviation $\sigma = 15$ millimeters. What percent of bearings have diameters between $70$ and $130$ millimeters?

Translate the endpoints into standard units. The lower endpoint is $70 = 100 - 2(15) = \mu - 2\sigma$, and the upper endpoint is $130 = 100 + 2(15) = \mu + 2\sigma$. So the question is asking for the percent of the distribution within two standard deviations of the mean.

That is exactly the middle band in the empirical rule. Roughly $95\%$ of bearings have diameters between $70$ and $130$ millimeters. The remaining $5\%$ — split into $2.5\%$ below $70$ mm and $2.5\%$ above $130$ mm — sit in the two tails.

No calculator, no z-table, just a quick recognition that "two standard deviations either side" maps to the $95\%$ band.

---

## Example 2: computing a z-score

> For the same distribution ($\mu = 100$ mm, $\sigma = 15$ mm), compute the z-score of a bearing whose diameter measures $x = 130$ mm.

Plug directly into the formula:

$$
z = \dfrac{x - \mu}{\sigma} = \dfrac{130 - 100}{15} = \dfrac{30}{15} = 2.
$$

A z-score of $z = 2$ means the bearing is two standard deviations above the mean. That agrees with what you already saw in Example 1: the value $130$ mm sits at the upper edge of the $95\%$ middle band.

Using the formula in reverse is just as useful. If somebody asked "what raw diameter corresponds to $z = -1$?", the answer would be $x = \mu + z\sigma = 100 + (-1)(15) = 85$ mm — one standard deviation below the mean. That algebraic rearrangement $x = \mu + z\sigma$ is worth memorizing alongside the z-score formula itself.

---

## Example 3: a one-sided tail using the empirical rule

> A state achievement test has normally distributed scores with mean $\mu = 500$ and standard deviation $\sigma = 100$. Estimate the percent of test-takers who score above $600$.

Begin with a z-score check: $z = (600 - 500) / 100 = 1$. The cutoff sits exactly one standard deviation above the mean. Now use the six-slice decomposition from the empirical rule, focusing on the portion of the curve above $\mu + \sigma$.

The middle $68\%$ band runs from $\mu - \sigma$ to $\mu + \sigma$. That leaves $100\% - 68\% = 32\%$ in the two tails combined. By symmetry, each tail holds exactly half of that total: $32\% / 2 = 16\%$ in the upper tail above $\mu + \sigma$, and $16\%$ in the lower tail below $\mu - \sigma$.

So about $16\%$ of test-takers score above $600$. As a quick cross-check using the finer decomposition: the slice between $\mu + \sigma$ and $\mu + 2\sigma$ holds $13.5\%$, and the slice above $\mu + 2\sigma$ holds $2.5\%$. Adding those gives $13.5\% + 2.5\% = 16\%$, matching the first calculation.

---

## Common pitfalls

- **Dropping a factor of two on the tails.** The empirical rule gives percentages for the **central** bands. If the question asks about a one-sided tail, you have to split the leftover symmetrically. Don't say "$5\%$ of data lies above $\mu + 2\sigma$" — that $5\%$ is the total in both tails; only $2.5\%$ sits above.
- **Treating a z-score as a probability.** A z-score is a coordinate on a number line, not a percent. Converting $z$ to a percent requires the empirical rule (for whole-number z-scores) or a z-table (for arbitrary values).
- **Forgetting the sign of the z-score.** Below-the-mean values have negative z-scores. Writing $z = 2$ for a value below the mean flips your interpretation entirely.
- **Using the empirical rule for non-normal data.** The 68-95-99.7 rule is specific to normal distributions. Strongly skewed or multi-modal data does not obey it, and applying the rule anyway gives garbage answers.
- **Mixing up the mean and the median.** The normal distribution is symmetric, so its mean, median, and mode coincide at the peak. That is a rare property — for skewed distributions the three move apart, and you cannot substitute one for another.

---

## Prerequisites

- [[Mean_Median_Mode_And_Range]] — the centering concepts that $\mu$ and the symmetry of the curve rely on.
- [[Data_Displays_And_Measures_Of_Spread]] — so that standard deviation already feels like a familiar measure of width.
- [[Fractions_Decimals_And_Percents]] — because every empirical-rule question ends with a quick conversion between decimal probabilities and percentages.

---

## Problems Involving Normal Distribution

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="normal_distribution"></div>

---

## See Also

- [[Margin_Of_Error_And_Confidence_Intervals]] — where the normal curve reappears as a sampling distribution
- [[Binomial_Probability]] — whose bar chart looks more and more like a bell curve as $n$ grows
- [[Data_Displays_And_Measures_Of_Spread]] — the pre-algebra starting point on spread
- [[Mean_Median_Mode_And_Range]] — the three centering measures that all coincide for a normal curve
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
