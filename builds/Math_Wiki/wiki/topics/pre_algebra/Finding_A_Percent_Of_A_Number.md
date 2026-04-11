---
title: "Finding a Percent of a Number"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Percent_Increase_And_Decrease"
  - "topics/pre_algebra/The_Percent_Equation"
  - "topics/pre_algebra/Understanding_Percents"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Understanding_Percents"
  - "topics/pre_algebra/Multiplying_Decimals"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
problem_type_ids: []
figures: []
summary: "Take a percent of any number by scaling: convert to a decimal and multiply."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Finding a Percent of a Number

# Finding a Percent of a Number

Tip jars, sales tax, homework grades, interest on a savings account — the world is packed with questions that start "what is _this much_ of _that much_?" Answering them in your head is one of the most useful everyday skills math teaches. The idea behind every one of those questions is the same: take a quantity, figure out how much of it you care about, and scale it by that fraction. Percent language just dresses up the scaling step so it is easier to talk about.

## What it means

The word **percent** comes from "per hundred," which is the whole secret. A percent is simply hundredths written in a different outfit. When someone says "$37\%$," they really mean "$37$ out of every $100$," which is the decimal $0.37$ and the fraction $\dfrac{37}{100}$ rolled into one. The three forms are interchangeable; you pick whichever is most convenient for the problem in front of you.

**Finding a percent of a number** is therefore just a scaled-down copy of that number. You want to know what portion of the whole you are keeping. In symbols:

$$
\text{percent of number} = \frac{\text{percent}}{100} \times \text{number}
$$

Equivalently, convert the percent to a decimal first and then multiply:

$$
p\% \text{ of } N \;=\; \frac{p}{100}\cdot N \;=\; (0.01 \cdot p) \cdot N
$$

That is the entire rule. No tricks, no secret formulas — just multiplication by a number between $0$ and $1$ (when the percent is between $0\%$ and $100\%$), or by a number larger than $1$ (when the percent is more than $100\%$, which is allowed and perfectly meaningful).

## How it works

Two clean steps handle every problem of this type:

1. **Turn the percent into a decimal.** Shift the decimal point two places to the left. $25\% \to 0.25$. $6\% \to 0.06$. $150\% \to 1.50$. A quick sanity check: the decimal should never come out negative, and for percents below $100\%$ it should always be smaller than $1$.
2. **Multiply that decimal by the number.** The product is the answer you wanted.

If the percent is a friendly fraction you already know, skip the decimal step and use the fraction directly. $25\%$ is the same as $\tfrac{1}{4}$, so one quarter of any number is as simple as dividing by $4$. $50\%$ means cut in half. $10\%$ means slide the decimal one place to the left. These shortcuts are the same rule in disguise; they just save paper when the arithmetic is clean.

## Why it works

Why does shifting a decimal point two places give the correct scale factor? Because $p\%$ literally means "$p$ out of $100$." Dividing $p$ by $100$ — which is all the decimal shift does — hands you the decimal fraction $\dfrac{p}{100}$. When you multiply that decimal fraction by a quantity, you are asking the quantity to shrink down to the same ratio. A $20\%$ slice of $\$50$ is geometrically the same thing as a $\tfrac{20}{100} = \tfrac{1}{5}$ slice of $\$50$, and one-fifth of $\$50$ is $\$10$.

The procedure works for percents of any size. A $150\%$ "slice" of a quantity is larger than the whole original, because the multiplier $1.5$ is greater than one. A $0.5\%$ slice is tiny, because the multiplier $0.005$ is much less than one. Both are legal, and both follow the same two-step rule.

## Worked examples

**Example 1.** The hiking club has $50$ members, and $20\%$ of them are new this year. How many new members joined?

Convert the percent to a decimal: $20\% = 0.20$. Multiply:

$$
0.20 \times 50 = 10
$$

Ten new members joined. A fraction-based check is easy here — $20\%$ is $\tfrac{1}{5}$, and $\tfrac{1}{5}$ of $50$ is $10$. Same answer.

**Example 2.** A jeweler is pricing a new ring at $\$175$, and her state charges $8\%$ sales tax. How much tax will a buyer pay?

Convert the percent: $8\% = 0.08$. Notice the leading zero — you shifted the decimal point two places to the left, and that required inserting a zero as a placeholder. Now multiply:

$$
0.08 \times 175
$$

Break the multiplication into two easier parts if you want to do it by hand. $0.08 \times 100 = 8$, and $0.08 \times 75 = 6$. Adding gives $8 + 6 = 14$. The sales tax is $\$14$. A shopper who forgets the tax at checkout is in for an unwelcome surprise.

**Example 3.** A city's $2025$ water-quality report notes that a particular reservoir holds $240{,}000$ gallons and lost $0.5\%$ of its volume to evaporation on one especially hot weekend. How many gallons evaporated?

The temptation is to read $0.5\%$ as "half" and be done in one second — but that would be $50\%$, which is a very different number. Half of a percent is much smaller. Convert carefully: $0.5\% = 0.005$. Then multiply:

$$
0.005 \times 240{,}000
$$

The easiest mental path is to strip the zeros and put them back. $5 \times 24 = 120$, and the total shift of zero places (three from $240{,}000$, balanced by three decimal places in $0.005$) lands the answer at $1{,}200$. So roughly $1{,}200$ gallons disappeared into the summer air. Tiny percent, big number, respectable loss. This kind of check — making sure small percents produce small answers and large percents produce large answers — is one of the best defenses against a misplaced decimal point.

## Common pitfalls

- **Forgetting to shift the decimal point.** Typing $25 \times 80$ into a calculator when you meant "$25\%$ of $80$" produces $2{,}000$ instead of $20$. The two-place shift is the step most often missed.
- **Getting the shift direction wrong.** Going from percent to decimal, you always move the decimal point left (the decimal gets smaller). Moving it right converts in the wrong direction and gives a huge number.
- **Confusing $0.5\%$ with $0.5$.** The percent $0.5\%$ is $0.005$, not $0.5$. That one is a factor of $100$ off, so any answer that follows will be off by a factor of $100$.
- **Treating "$150\%$" as illegal.** Percents over $100$ are perfectly ordinary — they just mean the answer is larger than the original quantity. A $150\%$ increase over a baseline of $40$ gives $60$, and that is not a paradox, it is a scale factor of $1.5$.

## Problems Involving Finding a Percent of a Number

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="finding_a_percent_of_a_number"></div>

## See Also

- [[Percent_Increase_And_Decrease]]
- [[The_Percent_Equation]]
- [[Understanding_Percents]]
- [[Fractions_Decimals_And_Percents]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
