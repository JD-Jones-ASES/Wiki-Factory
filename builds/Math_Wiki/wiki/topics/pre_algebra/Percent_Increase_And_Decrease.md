---
title: "Percent Increase and Decrease"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#word-problem-support", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Finding_A_Percent_Of_A_Number"
  - "topics/pre_algebra/The_Percent_Equation"
  - "topics/pre_algebra/Simple_And_Compound_Interest"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Finding_A_Percent_Of_A_Number"
  - "topics/pre_algebra/Understanding_Percents"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
problem_type_ids: []
figures: []
summary: "Measure how much a quantity changed, expressed as a percent of what it started at."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Percent Increase and Decrease

# Percent Increase and Decrease

Prices rise. Prices drop. Populations grow. Stock values swing. None of those changes mean much by themselves — a price jumping by $\$5$ is a yawn when the original price was $\$500$ and a disaster when the original price was $\$10$. What actually matters is the change relative to where you started. Percent change is the tool math gives you for expressing that comparison cleanly, and it is the same tool whether the quantity grew, shrank, or did both in sequence.

## What it means

A **percent change** is the amount a quantity changed, rescaled so you can compare it against the original quantity without carrying units. If a quantity grew, we call it a **percent increase**. If it shrank, we call it a **percent decrease**. The formula is the same for both directions, and the sign of the result tells you which one you are looking at:

$$
\text{percent change} \;=\; \frac{\text{new} - \text{old}}{\text{old}} \times 100\%
$$

Two ingredients go into the fraction: the raw change on top, and the original amount on the bottom. The top can be positive (an increase) or negative (a decrease). The bottom is always the starting quantity — the value from before the change, never the value after.

Once you have that percent in hand, it is easy to go the other way too. If the original quantity is $N$ and it increases by $r$ percent, the new quantity is

$$
N_{\text{new}} \;=\; N \cdot \left(1 + \frac{r}{100}\right)
$$

and if it decreases by $r$ percent:

$$
N_{\text{new}} \;=\; N \cdot \left(1 - \frac{r}{100}\right)
$$

The number inside the parentheses is called the **multiplier**. It is the scale factor that turns the old quantity directly into the new one in a single multiplication step. A $15\%$ markup has multiplier $1.15$. A $15\%$ discount has multiplier $0.85$.

## How it works

Computing percent change is a three-step routine:

1. **Identify the original and the new value.** Read the problem carefully. The original is whichever value you had first, not whichever one is bigger.
2. **Subtract to get the raw change.** Subtract old from new. If the new value is larger, the subtraction gives a positive number (an increase). If the new value is smaller, the subtraction gives a negative number (a decrease).
3. **Divide by the original and convert to a percent.** Divide the raw change by the original, then multiply by $100$ to dress the result in percent clothing.

Going from a percent back to a new value is the shorter trip: start with the original, build the multiplier, and multiply. If you see "after a $20\%$ increase," the multiplier is $1.20$ and you multiply the original by that. If you see "after a $30\%$ decrease," the multiplier is $0.70$ and you multiply. The multiplier always lives between $0$ and $1$ for decreases and is greater than $1$ for increases.

## Why it works

The whole point of dividing by the old value is to make the comparison fair. A $\$10$ gain is tiny on a $\$1000$ starting price (just $1\%$) but enormous on a $\$15$ starting price (about $67\%$). Dividing by the original rescales the raw change so both situations speak the same language — everyone is now quoted as "hundredths of the original." That is what allows people to compare the price movement of a candy bar to the price movement of a car without getting lost.

The multiplier shortcut works because percent change can always be written as an addition or a subtraction of percents. Keeping $100\%$ of the original and adding another $20\%$ gives $120\%$ of the original, which is the same as multiplying by $1.20$. Keeping $100\%$ and removing $30\%$ leaves $70\%$, which is the same as multiplying by $0.70$. The multiplier is just a compact way to do "keep the whole thing and adjust."

## Worked examples

**Example 1.** A jewelry maker sells a pair of silver earrings for $\$24$. Silver prices jumped over the winter, and she now sells the same earrings for $\$30$. By what percent did the price increase?

Pick out the old and the new. Old = $\$24$. New = $\$30$. Raw change:

$$
30 - 24 = 6
$$

Divide by the original and scale to a percent:

$$
\frac{6}{24} \times 100\% = 0.25 \times 100\% = 25\%
$$

The earrings are $25\%$ more expensive than before. Notice that dividing by $24$ (the old price) is what made the result a clean $25\%$. If you had mistakenly divided by $30$ (the new price), you would have gotten $20\%$ — close enough to look right, but still wrong. Always divide by the starting value.

**Example 2.** A pair of hiking boots was priced at $\$90$, and the store marked them down by $35\%$ for a holiday sale. What is the new sale price?

Two roads reach the same answer. The first is the "multiplier" road. A $35\%$ decrease means the sale price is $100\% - 35\% = 65\%$ of the original, and $65\%$ is the multiplier $0.65$:

$$
90 \times 0.65 = 58.50
$$

The sale price is $\$58.50$. The second road splits the problem in two — find $35\%$ of $90$ and subtract:

$$
0.35 \times 90 = 31.50
$$

Then $90 - 31.50 = 58.50$. Same answer either way. The multiplier road is faster when the percent is clean; the split-and-subtract road is easier to explain to yourself the first few times you meet the idea.

**Example 3.** A town had a population of $1{,}200$ five years ago. Today it has $1{,}536$ residents. What is the percent increase in population?

Old = $1{,}200$. New = $1{,}536$. Raw change:

$$
1{,}536 - 1{,}200 = 336
$$

Divide by the original:

$$
\frac{336}{1{,}200}
$$

That fraction needs a little work. $\tfrac{336}{1{,}200}$ simplifies by dividing numerator and denominator by $12$: $\tfrac{28}{100}$. That is already in per-hundred form, so

$$
\frac{28}{100} \times 100\% = 28\%
$$

The town grew by $28\%$ over the five-year period. A sanity check: $28\%$ of $1{,}200$ is about $336$, and adding that back to $1{,}200$ should give $1{,}536$. It does.

## Common pitfalls

- **Dividing by the wrong base.** The denominator in the percent-change formula is the original value, always. Students who divide by the new value end up with a number that is close to the right answer but systematically off.
- **Forgetting the $100\%$ step.** The fraction $\tfrac{\text{new} - \text{old}}{\text{old}}$ is a decimal, not a percent. Multiply by $100$ to finish the conversion.
- **Assuming a $20\%$ increase followed by a $20\%$ decrease returns the original.** It does not. A $20\%$ increase on $100$ gives $120$, and a $20\%$ decrease on $120$ gives $96$, not $100$. The two percents are applied to different bases, so they do not cancel.
- **Confusing percent change with percent of a whole.** "Tax of $8\%$" is a percent of a whole (the subtotal) and uses the methods on [[Finding_A_Percent_Of_A_Number]]. "The price went up $8\%$" is a percent change from one value to another and uses the formula above. Reading carefully and asking "change from what to what?" keeps the two ideas from getting mixed up.

## Problems Involving Percent Increase and Decrease

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="percent_increase_and_decrease"></div>

## See Also

- [[Finding_A_Percent_Of_A_Number]]
- [[The_Percent_Equation]]
- [[Simple_And_Compound_Interest]]
- [[Applications_Tax_Tip_Discount_And_Simple_Interest]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
