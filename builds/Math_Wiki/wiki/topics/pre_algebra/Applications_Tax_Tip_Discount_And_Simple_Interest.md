---
title: "Applications: Tax, Tip, Discount, and Simple Interest"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#word-problem-support", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Understanding_Percents"
  - "topics/pre_algebra/The_Percent_Equation"
  - "topics/pre_algebra/Percent_Increase_And_Decrease"
  - "topics/pre_algebra/Simple_And_Compound_Interest"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Understanding_Percents"
  - "topics/pre_algebra/The_Percent_Equation"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
problem_type_ids: []
figures: []
summary: "Four of the most common real-world percent problems — tax, tip, discount, and simple interest — all built from the same idea."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Applications: Tax, Tip, Discount, and Simple Interest

# Applications: Tax, Tip, Discount, and Simple Interest

Percent problems stop feeling like algebra homework and start feeling like real life the moment a bill shows up. Restaurants add a tip, stores subtract a discount, governments add a sales tax, and banks add interest on savings or subtract interest on loans. All four of these situations boil down to the same skill: compute a percentage of an amount, then either add it or subtract it from the original. Once you see that unified pattern, the four topics stop being four topics at all — they become one habit of thought applied four ways. This is where percent conversions earn their keep.

## What it means

Each of the four applications uses the same basic move: multiply an amount by a rate (expressed as a decimal) to find a percent-sized piece. What the piece means, and whether you add or subtract it, depends on the situation.

**Sales tax.** A tax is an amount added to a purchase by the government. It is a percent of the purchase price.

$$
\text{tax} = (\text{tax rate}) \cdot (\text{price})
$$

$$
\text{total} = \text{price} + \text{tax}
$$

**Tip.** A tip, or gratuity, is extra money given for a service — most commonly at a restaurant. It is a percent of the bill before tax.

$$
\text{tip} = (\text{tip rate}) \cdot (\text{bill})
$$

$$
\text{total} = \text{bill} + \text{tip}
$$

**Discount.** A discount is a reduction in price, usually advertised as a percent off.

$$
\text{discount} = (\text{discount rate}) \cdot (\text{original price})
$$

$$
\text{sale price} = \text{original price} - \text{discount}
$$

**Simple interest.** Interest is money a bank pays you (on savings) or charges you (on a loan). The simple-interest formula is:

$$
I = P \cdot r \cdot t
$$

where $I$ is the interest earned in dollars. $P$ stands for the **principal** — the starting deposit or loan amount. $r$ is the annual rate written as a decimal, not a percent ($5\% \to 0.05$). $t$ is the elapsed time measured in **years**. To find the total amount after the interest has been added, combine principal and interest:

$$
A = P + I = P(1 + r t)
$$

## How it works

Every problem in this group is a two-step process: compute the percent-sized piece, then combine it with the original amount — add for tax, tip, and interest; subtract for discount. The cleanest habit is to write the rate as a decimal before you plug it in. If the problem says $18\%$, you write $0.18$. If it says $4.5\%$, you write $0.045$. This protects you from the classic blunder of multiplying by $18$ instead of $0.18$, which would give you an answer $100$ times too big.

A handy shortcut works for tax and tip problems when you want only the final total, not the extra amount separately. Multiplying the original amount by $(1 + r)$ rolls both steps into one:

$$
\text{total with tax} = \text{price} \cdot (1 + \text{tax rate})
$$

Same idea for a discount, with subtraction:

$$
\text{sale price} = \text{original price} \cdot (1 - \text{discount rate})
$$

That one-step version is exactly the simple-interest total formula, $A = P(1 + rt)$, when $t = 1$ year.

## Why it works

Each application is a practical instance of the percent equation you already know. A tax _rate_ and a tip _rate_ and a discount _rate_ all do the same mathematical job — they pick out a percent-sized slice of a known whole. What differs is whether that slice is tacked onto the original amount, as with tax, tip, or interest, or subtracted from it, as with discount. Interest adds more nuance with the time variable $t$, but the central move is still percent-of-amount. Learning one pattern and remembering four small sign-and-direction details is much easier than memorizing four separate recipes.

## Worked examples

**Example 1. Restaurant bill with tip.** The school band stops at a diner after rehearsal. Their pre-tip total is $\$42.50$, and the director plans to add an $18\%$ gratuity. Determine the gratuity amount and the final cost the band will pay.

Convert the rate to a decimal: $18\% = 0.18$. Compute the tip as a percent of the bill:

$$
\text{tip} = 0.18 \cdot 42.50.
$$

Multiplying gives $7.65$. So the tip is $\$7.65$. Add it to the bill to get the total:

$$
\text{total} = 42.50 + 7.65 = 50.15.
$$

The final charge is $\$50.15$. You could also do this in one step using the shortcut: $42.50 \cdot 1.18 = 50.15$. Same answer.

**Example 2. Clearance sweater.** A sweater originally priced at $\$85$ is on sale for $25\%$ off. Determine the sale price.

Convert $25\%$ to the decimal $0.25$. Compute the discount:

$$
\text{discount} = 0.25 \cdot 85 = 21.25.
$$

Subtract from the original price to get the sale price:

$$
\text{sale price} = 85 - 21.25 = 63.75.
$$

The sale price is $\$63.75$. Using the one-step version, the sale price is $85 \cdot (1 - 0.25) = 85 \cdot 0.75 = 63.75$. Same number.

**Example 3. Savings account with simple interest.** A coffee shop deposits $\$2000$ into a savings account that pays $4\%$ simple interest per year. How much interest will the account earn in $3$ years, and what will the total balance be?

Here the principal is $P = 2000$, the annual rate is $r = 0.04$, and the time is $t = 3$ years. The interest is:

$$
I = P \cdot r \cdot t = 2000 \cdot 0.04 \cdot 3.
$$

Work left to right. $2000 \cdot 0.04 = 80$, and $80 \cdot 3 = 240$:

$$
I = 240.
$$

So the account earns $\$240$ in interest over three years. The total balance is the principal plus the interest:

$$
A = 2000 + 240 = 2240.
$$

After three years, the account holds $\$2240$. Notice that simple interest is the same amount each year — $\$80$ — because the interest is always calculated on the original principal, not on a growing balance.

## Common pitfalls

- **Leaving the percent as a whole number.** Writing $18$ instead of $0.18$ makes the answer $100$ times too big. Convert to decimal form before multiplying.
- **Adding the wrong thing to the wrong thing.** Discounts are subtracted; tax, tip, and interest are added. Reading the word problem carefully is the only protection.
- **Using the wrong time unit for simple interest.** The rate in $I = Prt$ is an **annual** rate, so time $t$ must be in years. Six months is $0.5$, not $6$.
- **Taxing the tip, or tipping on the tax.** Standard practice is to compute the tip on the pre-tax bill and the tax on the pre-tip price. Some problems bend this, but when in doubt, apply each rate to the original amount separately.

## Problems Involving These Applications

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="applications_tax_tip_discount_and_simple_interest"></div>

## See Also

- [[Understanding_Percents]]
- [[The_Percent_Equation]]
- [[Percent_Increase_And_Decrease]]
- [[Simple_And_Compound_Interest]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
