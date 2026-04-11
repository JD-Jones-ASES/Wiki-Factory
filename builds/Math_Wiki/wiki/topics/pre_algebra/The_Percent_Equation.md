---
title: "The Percent Equation"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Understanding_Percents"
  - "topics/pre_algebra/Finding_A_Percent_Of_A_Number"
  - "topics/pre_algebra/Percent_Increase_And_Decrease"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Understanding_Percents"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
problem_type_ids: []
figures: []
summary: "Every percent problem is the same relationship — part equals percent times whole — solved for a different unknown."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > The Percent Equation

# The Percent Equation

Once you understand that a percent is just hundredths, almost every percent word problem collapses into a single equation with three moving parts: a **part**, a **whole**, and a **percent**. Two of those numbers are usually given and you have to find the third. That is what the percent equation is — a tidy piece of shorthand that turns messy word problems into a one-line algebra move. The secret is learning to spot which of the three pieces the problem is hiding, because the approach is the same either way.

## What it means

The percent equation expresses the relationship between the three quantities:

$$
\text{part} = \text{percent} \cdot \text{whole}
$$

Here the **percent** is written as a decimal (not a percent sign). The **whole** is the total amount you are taking a slice of. The **part** is the piece of that total the percent picks out. For example, "$15\%$ of $200$" translates to $0.15 \cdot 200 = 30$, so the part is $30$.

Three versions of the same equation cover the three kinds of question you will see, depending on which quantity is missing. Rearranging with basic algebra gives:

$$
\text{part} = \text{percent} \cdot \text{whole}
$$

$$
\text{percent} = \frac{\text{part}}{\text{whole}}
$$

$$
\text{whole} = \frac{\text{part}}{\text{percent}}
$$

All three forms are algebraic moves on the original equation — divide both sides to isolate the unknown. You do not need to memorize three separate rules; you just need to recognize which variable is missing.

## How it works

The real work in percent problems is **identifying** the three quantities in a sentence. Once you label them, the equation writes itself.

- The **percent** is almost always the number that wears the $\%$ sign or is described as a rate ("what percent," "$20$ percent off," "an $8\%$ increase").
- The **whole** is the total you start with — the original price, the full list, the principal, the class. Look for the phrase "of ___" right after the percent.
- The **part** is the outcome — the tax amount, the tip, the number of students who voted yes, the discount dollars. Look for the phrase "is ___" or "is what percent of ___."

A useful translation template comes from the English sentence itself. The word "is" means "equals" and the word "of" means "times." So a sentence like "$12$ is what percent of $60$?" becomes directly:

$$
12 = p \cdot 60
$$

Solve for $p$ by dividing both sides by $60$, and you get $p = 0.20 = 20\%$. This "is-equals, of-times" trick keeps you from mixing up which number is which.

Once the equation is set up, remember that percents need to be in **decimal form** before you multiply. $15\%$ is $0.15$ when you plug it in. At the end, if you solved for a percent, multiply by $100$ to report it with a percent sign.

## Why it works

The percent equation is a fancy way of saying "a percent is a fraction." Writing $p\%$ as $\tfrac{p}{100}$ turns the phrase "$p$ percent of the whole" into the multiplication $\tfrac{p}{100} \cdot \text{whole}$, and that product is exactly what the part must equal. Every one of the three forms above is the same relationship with basic algebra applied to isolate a different variable. You do not need a new rule for each type of question; you just need one equation and one division move.

You can think of the three forms as three spots on the same scale: the part, the whole, and the rate that connects them. If you know two, you can always find the third.

## Worked examples

**Example 1. Finding the part.** What is $15\%$ of $240$?

The percent is $15\%$, the whole is $240$, and the part is the unknown. Rewrite $15\%$ as a decimal, then multiply:

$$
\text{part} = 0.15 \cdot 240.
$$

Multiply it out:

$$
0.15 \cdot 240 = 36.
$$

So $15\%$ of $240$ is $36$. A quick gut check: $10\%$ of $240$ is $24$, and half of that is $12$, so $15\%$ should be $24 + 12 = 36$. The answer checks.

**Example 2. Finding the percent.** Maya's hiking club has $180$ members. $45$ of them signed up for the spring trip. What percent of the club is going?

The part is $45$, the whole is $180$, and the percent is what we are after. Use the second form:

$$
\text{percent} = \frac{45}{180}.
$$

Simplify the fraction. Both numerator and denominator share a factor of $45$:

$$
\frac{45}{180} = \frac{1}{4} = 0.25.
$$

Convert back to a percent by multiplying by $100$:

$$
0.25 \cdot 100 = 25\%.
$$

So $25\%$ of the club signed up for the trip. A sanity check: a quarter of $180$ is $45$, which matches what the problem said.

**Example 3. Finding the whole.** A jewelry maker sold $72$ bracelets at a craft fair and later learned that this was $30\%$ of her total inventory. How many bracelets did she bring to the fair?

Identify the three roles: the known part is $72$, the known percent is $30\% = 0.30$, and the missing piece is the whole. Use the third form:

$$
\text{whole} = \frac{72}{0.30}.
$$

Divide:

$$
\frac{72}{0.30} = 240.
$$

She brought $240$ bracelets to the fair. You can double-check by running the original equation forward: $0.30 \cdot 240 = 72$. The numbers agree.

## Common pitfalls

- **Misidentifying the whole.** The whole is the total you are comparing against, not necessarily the bigger number. In "$72$ is $30\%$ of what number?" the whole is the unknown, not the $72$.
- **Forgetting to convert the percent to a decimal.** Plugging $15$ into the equation instead of $0.15$ gives answers that are $100$ times too big. Always convert first.
- **Reversing part and percent.** If the question asks "what percent of $180$ is $45$?" the answer is $25\%$, not $4\%$ and not $400\%$. Set up the ratio $\tfrac{\text{part}}{\text{whole}}$, not the other way around.
- **Forgetting to multiply by $100$ at the end.** After dividing $\tfrac{\text{part}}{\text{whole}}$, the result is a decimal. It only becomes a percent once you multiply by $100$ and attach the $\%$ sign.

## Problems Involving The Percent Equation

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_percent_equation"></div>

## See Also

- [[Understanding_Percents]]
- [[Finding_A_Percent_Of_A_Number]]
- [[Percent_Increase_And_Decrease]]
- [[Proportions_And_Cross_Multiplication]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
