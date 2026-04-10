---
title: "Simple and Compound Interest"
type: topic
aliases: ["Interest", "Compound Interest"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#word-problem-support"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_2", chapter: "3", section: "3.4"}
related:
  - "topics/pre_algebra/Finding_A_Percent_Of_A_Number"
  - "topics/pre_algebra/Percent_Increase_And_Decrease"
  - "topics/pre_algebra/Applications_Tax_Tip_Discount_And_Simple_Interest"
  - "topics/pre_algebra/Understanding_Percents"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Finding_A_Percent_Of_A_Number"
problem_type_ids: []
figures: []
summary: "Two formulas for money growing over time — simple interest is a flat add-on each year, compound interest earns interest on its own interest."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Simple and Compound Interest

# Simple and Compound Interest

Interest is the price paid for the use of money. When you deposit money in a savings account, the bank pays you interest for letting them hold your dollars. When you borrow money, you pay interest to the lender for the same reason. There are two main ways to compute that price, and they differ in a subtle way that turns out to matter enormously over long spans of time.

**Simple interest** never changes its target: it always looks back at the original amount you started with and charges a fixed percentage of that same number every year. **Compound interest** is greedier — each year it adds the new interest into the pile and then charges interest on the bigger pile next time. Over a year or two the two methods give similar answers. Over a decade or a lifetime they drift dramatically apart, and compound interest wins every single time.

$$
\text{Simple: } \quad I = P r t \qquad A = P(1 + r t)
$$

$$
\text{Compound: } \quad A = P\!\left(1 + \tfrac{r}{n}\right)^{n t}
$$

---

## Key ideas

**The three inputs are always the same.** Every interest problem starts with three numbers: the amount of money at the beginning (called the principal), the annual rate of interest written as a decimal, and the length of time the money sits — usually measured in years. The standard letters are $P$ for principal, $r$ for the rate as a decimal, and $t$ for time in years. A $5\%$ rate becomes $r = 0.05$; a $3.25\%$ rate becomes $r = 0.0325$.

**Simple interest earns a fixed number of dollars each year.** With simple interest, you take a flat percentage of the original principal every year and add it on. If you start with $\$1{,}000$ at $5\%$ simple interest, you earn $\$50$ in year one, $\$50$ in year two, $\$50$ in year three, and so on forever — because the bank is always computing $5\%$ of $\$1{,}000$, not $5\%$ of whatever the balance currently happens to be. The interest earned after $t$ years is

$$
I = P r t,
$$

and the total amount in the account is the original principal plus that interest, which can be written compactly as $A = P(1 + rt)$.

**Compound interest turns each year's interest into next year's principal.** With compound interest, the bank credits the interest to the account periodically — once a year, once a quarter, once a month — and from then on, that newly-added interest earns interest too. The account grows a little faster each period because the base it is earning on keeps getting bigger. If the rate is $r$ per year and interest is compounded $n$ times per year for $t$ years, the formula for the final balance is

$$
A = P\!\left(1 + \tfrac{r}{n}\right)^{n t}.
$$

Read this carefully. The quantity $r/n$ is the rate per compounding period (annual rate divided by the number of periods in a year), and $n t$ is the total number of periods. You multiply the principal by $(1 + r/n)$ once for each period, which is exactly what repeated compounding does.

**The special case of annual compounding is the cleanest.** When the bank compounds once per year, $n = 1$ and the formula collapses to

$$
A = P(1 + r)^t.
$$

This is the version you meet first in most textbooks, and it is all you need when the problem says "compounded annually." The more general $n$-compounding formula handles quarterly, monthly, or daily credits.

**Over the long run, compound always beats simple for the same rate.** With simple interest, the extra dollars grow in a straight line — a fixed amount each year, forever. With compound interest, the extra dollars grow in a curve that bends upward because each year's earnings are working themselves. A graph of the two side by side shows the simple-interest line and the compound-interest curve crossing at year zero, moving along together for a couple of years, and then the compound curve pulling steadily ahead. The gap is small at first and then keeps widening.

---

## Example 1: plain simple interest

> You put $\$1{,}200$ in an account that pays $4\%$ simple interest per year. What is the balance after three years?

Write down the three inputs: $P = 1200$, $r = 0.04$, $t = 3$. The interest earned is

$$
I = P r t = 1200 \cdot 0.04 \cdot 3 = 144.
$$

So the account earns $\$144$ over three years. The balance is the starting principal plus that interest:

$$
A = P + I = 1200 + 144 = 1444.
$$

You end with $\$1{,}444$. Notice how clean the arithmetic is: the interest is exactly $\$48$ a year times three years. Simple interest is called "simple" for a reason.

---

## Example 2: compound interest, annual

> You put $\$1{,}200$ in an account that pays $4\%$ interest compounded annually. What is the balance after three years?

Same inputs: $P = 1200$, $r = 0.04$, $t = 3$. Since interest is credited once per year, $n = 1$ and the formula simplifies to

$$
A = P(1 + r)^t = 1200 (1.04)^3.
$$

Compute $(1.04)^3$ step by step:

$$
(1.04)^2 = 1.0816, \qquad (1.04)^3 = 1.0816 \cdot 1.04 \approx 1.124864.
$$

So

$$
A \approx 1200 \cdot 1.124864 \approx 1349.84.
$$

The final balance is about $\$1{,}349.84$. Compare this to Example 1: with simple interest the account grew to $\$1{,}344$; with compound interest it grew to $\$1{,}349.84$. The compound balance is about $\$5.84$ ahead — small after three years, but growing. Over thirty years the gap would be in the hundreds of dollars, and over a lifetime in the thousands.

Wait — let me recheck the simple total. $I = 1200 \cdot 0.04 \cdot 3 = 144$, so $A = 1344$. The compound version beats it by $1349.84 - 1344 = 5.84$. That extra five-dollars-and-change is the interest on the interest. Compound interest paid itself a little bit in year two, and a little more in year three.

---

## Example 3: compounded more often

> You put $\$2{,}000$ into an account that pays $6\%$ interest compounded monthly. What is the balance after five years?

This problem uses the full compound-interest formula because the compounding is not annual. The monthly rate is $r/n = 0.06/12 = 0.005$, and the total number of compounding periods is $n t = 12 \cdot 5 = 60$. Substituting:

$$
A = 2000 \left(1 + \tfrac{0.06}{12}\right)^{60} = 2000 (1.005)^{60}.
$$

Using a calculator, $(1.005)^{60} \approx 1.34885$, so

$$
A \approx 2000 \cdot 1.34885 \approx 2697.70.
$$

You would have about $\$2{,}697.70$ after five years. As a sanity check, simple interest at the same rate and time would have paid $I = 2000 \cdot 0.06 \cdot 5 = 600$, for a total of $\$2{,}600$. The monthly compounding added nearly $\$100$ on top of that — it really does matter how often interest is credited.

---

## Example 4: a loan application

> Maria borrows $\$800$ at $6\%$ simple interest for $2.5$ years. How much does she pay back in total?

Simple interest applies to loans just as much as to savings accounts. Plug in $P = 800$, $r = 0.06$, $t = 2.5$:

$$
I = 800 \cdot 0.06 \cdot 2.5 = 120.
$$

Maria owes $\$120$ in interest on top of the original $\$800$, for a total repayment of $\$800 + \$120 = \$920$. Notice that time can be a decimal when the period is not a whole number of years. Half a year is $t = 0.5$; nine months is $t = 0.75$.

---

## Simple vs. compound: a side-by-side comparison

To see the difference clearly, put $\$2{,}000$ into two accounts at $5\%$ for four years, one simple and one compounded annually.

**Simple interest:** $I = 2000 \cdot 0.05 \cdot 4 = 400$, so $A = 2400$ exactly. The account earns $\$100$ every year for four years — same amount, year after year.

**Compound interest:** $A = 2000(1.05)^4$. Work out $(1.05)^4$: $1.05^2 = 1.1025$, then $1.1025^2 = 1.21550625$. So $A \approx 2000 \cdot 1.21550625 \approx 2431.01$.

Compound interest has won by about $\$31$ over only four years. Year by year, the compound balance climbs $\$100 \to \$105 \to \$110.25 \to \$115.76 \to \$121.55$ — each year's gain is a little larger than the year before. That bending-upward pattern is what makes compound interest one of the most talked-about ideas in personal finance.

---

## Common pitfalls

- **Forgetting to convert the percent to a decimal.** A rate of $5\%$ becomes $r = 0.05$, not $r = 5$. Leaving the percent sign in will give an answer that is off by a factor of $100$.
- **Mixing up $n$ and $t$.** In the compound formula, $n$ counts compounding periods per year (monthly is $12$, quarterly is $4$), while $t$ is the total number of years. The exponent is the product $n t$, the total number of periods.
- **Using the wrong time units.** Rates are almost always quoted per year. If a problem gives time in months, convert — six months is $t = 0.5$ years, nine months is $t = 0.75$ years.
- **Applying simple interest when the problem says "compounded."** Any phrase like "compounded annually," "compounded quarterly," or "compounded daily" signals the compound formula. The word "simple" must appear for simple interest.

---

## Prerequisites

Before working through practice problems, it helps to be solid on:

- [[Fractions_Decimals_And_Percents]] — converting percentages to the decimal form the formulas expect
- [[Finding_A_Percent_Of_A_Number]] — the skill the simple interest formula is built on

---

## Problems Involving Simple and Compound Interest

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="simple_and_compound_interest"></div>

---

## See Also

- [[Finding_A_Percent_Of_A_Number]]
- [[Percent_Increase_And_Decrease]]
- [[Applications_Tax_Tip_Discount_And_Simple_Interest]]
- [[Understanding_Percents]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
