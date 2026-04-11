---
title: "Units of Measurement and Conversion"
type: topic
aliases: ["Unit Conversion", "Dimensional Analysis", "Converting Units"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#skill-procedural-calculation", "#word-problem-support", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Unit_Rates"
  - "topics/pre_algebra/Ratios_Rates_And_Proportions"
  - "topics/pre_algebra/Scale_Drawings_And_Maps"
  - "topics/pre_algebra/Multiplying_Fractions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Unit_Rates"
  - "topics/pre_algebra/Ratios_Rates_And_Proportions"
problem_type_ids: []
figures: []
summary: "Change from one unit to another by multiplying by a carefully chosen fraction equal to one, then canceling matching unit names."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Units of Measurement and Conversion

# Units of Measurement and Conversion

Every measurement comes with two parts — a **number** and a **unit** — and neither half is optional. "Fifty" is not a useful answer on its own. Fifty what? Inches, dollars, minutes, miles, grams? The unit is what tells you what kind of thing you measured, and unit mismatches are the single most common way physical problems go wrong. Unit conversion is the reliable little trick that keeps those mismatches from happening: it lets you translate a measurement written in one unit into the same measurement written in another unit, without changing what you actually have.

The key insight is that a **conversion factor** — something like $12 \text{ inches} = 1 \text{ foot}$ — can be rewritten as a fraction that equals $1$. And since multiplying by $1$ never changes a value, you can multiply your original measurement by that fraction and the number on your label will change even though the thing you measured did not. The technique goes by the fancy name **dimensional analysis**, but in practice it is just the art of stacking fractions so that unwanted units cancel and wanted units survive.

## What it means / The idea

Here are the conversion facts you will use most often. Memorize a few and look the rest up as needed.

**US customary length:** $1 \text{ foot} = 12 \text{ inches}$, $1 \text{ yard} = 3 \text{ feet}$, $1 \text{ mile} = 5{,}280 \text{ feet}$.
**US customary weight:** $1 \text{ pound} = 16 \text{ ounces}$, $1 \text{ ton} = 2{,}000 \text{ pounds}$.
**US customary capacity:** $1 \text{ cup} = 8 \text{ fluid ounces}$, $1 \text{ pint} = 2 \text{ cups}$, $1 \text{ quart} = 2 \text{ pints}$, $1 \text{ gallon} = 4 \text{ quarts}$.
**Metric length:** $1 \text{ cm} = 10 \text{ mm}$, $1 \text{ m} = 100 \text{ cm}$, $1 \text{ km} = 1{,}000 \text{ m}$.
**Metric mass:** $1 \text{ g} = 1{,}000 \text{ mg}$, $1 \text{ kg} = 1{,}000 \text{ g}$.
**Metric capacity:** $1 \text{ L} = 1{,}000 \text{ mL}$.
**Time:** $1 \text{ min} = 60 \text{ s}$, $1 \text{ hr} = 60 \text{ min}$, $1 \text{ day} = 24 \text{ hr}$.
**US-to-metric (approximations):** $1 \text{ inch} \approx 2.54 \text{ cm}$, $1 \text{ mile} \approx 1.61 \text{ km}$, $1 \text{ pound} \approx 0.454 \text{ kg}$.

The central trick of unit conversion is this. Since any conversion fact like $12 \text{ in} = 1 \text{ ft}$ can be rewritten as a fraction equal to $1$, you get two conversion fractions to pick from:

$$
\frac{12 \text{ in}}{1 \text{ ft}} = 1 \qquad \text{or} \qquad \frac{1 \text{ ft}}{12 \text{ in}} = 1
$$

Both are equal to $1$, so multiplying by either one does nothing to the value of the measurement — only to its unit label. You pick the version that will cancel the unit you want to get rid of, because unit names cancel just like algebraic variables do.

## How it works / The procedure

1. **Write the starting measurement as a fraction over $1$.** A quantity like $7$ feet becomes $\dfrac{7 \text{ ft}}{1}$. This makes it look like every other fraction in the problem.
2. **Pick a conversion fraction.** Choose the version whose **top** has the unit you want to end up with and whose **bottom** has the unit you want to cancel. Getting this upside down is the single biggest source of errors — take your time.
3. **Multiply.** Stack the starting fraction against the conversion fraction just like you would multiply any two fractions. The unit you wanted to cancel should appear once on top and once on the bottom, letting you cross it off.
4. **Simplify numbers only.** After the units cancel, do the arithmetic: multiply the numerators, multiply the denominators, and divide. Every trace of the old unit should be gone, replaced by the new one.
5. **Repeat if needed.** For longer conversions (like seconds to hours), chain multiple conversion fractions back to back in a single expression, letting each one cancel a unit the previous one left behind.

## Why it works

Because every conversion fraction equals exactly $1$, multiplying by one of them does not change the physical amount — it only repackages it in a different unit label. If $12 \text{ in} = 1 \text{ ft}$, then $\tfrac{1 \text{ ft}}{12 \text{ in}} = \tfrac{12 \text{ in}}{12 \text{ in}} = 1$, so when you multiply $7 \text{ ft}$ by $\tfrac{12 \text{ in}}{1 \text{ ft}}$, the numerical value of the product does not describe a different physical length — it describes the same length, just recounted in smaller pieces. The unit names are doing the bookkeeping for you, which is why canceling them by name is not just a shortcut — it is the whole point of the method. If your final answer has the wrong units, your arithmetic is wrong, no matter how tidy it looks.

## Worked examples

### Example 1

Kai is cutting wire at the maker space and the design calls for a length of $7.5$ feet. The bench ruler, though, is marked only in inches. Express Kai's needed length in inches.

Start with $7.5$ feet over $1$ and multiply by the fraction $\dfrac{12 \text{ in}}{1 \text{ ft}}$ — feet on the bottom so they cancel, inches on top so they survive:

$$
\frac{7.5 \text{ ft}}{1} \cdot \frac{12 \text{ in}}{1 \text{ ft}} = \frac{7.5 \cdot 12 \text{ in}}{1} = 90 \text{ in}.
$$

The feet names match one on top and one on bottom, so they cross off, leaving only inches in the label. Kai needs $90$ inches of wire. A quick sanity check: $7.5$ feet is somewhere between $7$ feet ($84$ inches) and $8$ feet ($96$ inches), and $90$ sits right in between. Good sign.

### Example 2

At the farmer's market, Zoe is pricing coffee beans sold by weight. A bag weighs $2500$ grams, and the sign she needs to post uses kilograms. Determine the bag's weight in kilograms.

Here the move is from a small unit to a bigger one, so the answer should be a smaller number than $2500$. Multiply by $\dfrac{1 \text{ kg}}{1000 \text{ g}}$ — grams on the bottom cancel, kilograms on top survive:

$$
\frac{2500 \text{ g}}{1} \cdot \frac{1 \text{ kg}}{1000 \text{ g}} = \frac{2500 \text{ kg}}{1000} = 2.5 \text{ kg}.
$$

The bag weighs $2.5$ kilograms. The number shrank by a factor of $1000$, which is exactly how metric prefixes are set up to work. If you had accidentally flipped the fraction and multiplied by $\dfrac{1000 \text{ g}}{1 \text{ kg}}$, the grams would not have canceled and you would have been left with a weird mixed unit, which is your cue to flip the fraction and try again.

### Example 3

Emilia is planning a hiking club outing and needs to explain a trail distance to a friend who thinks in kilometers. The trail is $3$ miles long. Using the approximation $1 \text{ mile} \approx 1.61 \text{ km}$, express the trail distance in kilometers.

This conversion goes from US customary to metric, so you set it up the same way. Multiply by $\dfrac{1.61 \text{ km}}{1 \text{ mile}}$ so miles cancel and kilometers survive:

$$
\frac{3 \text{ mi}}{1} \cdot \frac{1.61 \text{ km}}{1 \text{ mi}} = \frac{3 \cdot 1.61 \text{ km}}{1} = 4.83 \text{ km}.
$$

The trail is about $4.83$ kilometers. A fast sanity check: $1$ mile is a bit more than $1.5$ km, so $3$ miles should be a bit more than $4.5$ km. $4.83$ is right in that neighborhood, so the answer passes the smell test. When a problem uses the word "approximately" or the symbol $\approx$, it is a signal that the conversion factor is rounded, so your answer is only as accurate as the factor you plugged in — do not pretend to have more precision than the source does.

## Common pitfalls

- **Flipping the conversion fraction.** The unit you want to cancel must be on the **opposite** side of the fraction bar from where it lives in the starting measurement. If your starting value has feet on top (as a numerator), the conversion fraction needs feet on the bottom. Double-check by writing the labels out and crossing off matching ones.
- **Forgetting the difference between "from" and "to."** Converting from a small unit to a big unit (inches to feet, grams to kilograms, seconds to hours) gives a smaller number. Converting the other way gives a bigger number. If the size of your answer goes the wrong direction, the fraction was upside down.
- **Dropping the unit label mid-problem.** If you write $2500 \cdot \tfrac{1}{1000}$ without the unit names attached, you lose the ability to check your work. Always keep the unit names glued to the numbers until the very end.
- **Mixing unit systems without converting first.** You cannot add $2$ feet to $30$ centimeters and get a clean answer. Pick one system, convert both measurements into it, then do the addition.
- **Using an exact conversion when only an approximate one applies.** $1 \text{ inch} = 2.54 \text{ cm}$ is exact by definition, but $1 \text{ mile} \approx 1.61 \text{ km}$ is rounded. For most pre-algebra problems, these rounded values are fine, but do not pretend the final answer is more precise than the factor allowed.

## Prerequisites

- [[Multiplying_Fractions]] — every conversion is a fraction-times-fraction operation with cancellation
- [[Unit_Rates]] — a conversion factor is itself a unit rate in disguise
- [[Ratios_Rates_And_Proportions]] — conversion factors come out of proportional reasoning

## Problems Involving Units of Measurement and Conversion

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="units_of_measurement_and_conversion"></div>

## See Also

- [[Unit_Rates]] — the "miles per hour" or "dollars per pound" form that underlies most conversion factors
- [[Ratios_Rates_And_Proportions]] — proportional reasoning is where dimensional analysis comes from
- [[Scale_Drawings_And_Maps]] — scale problems usually involve converting units mid-way
- [[Multiplying_Fractions]] — the arithmetic engine behind every conversion step
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
