---
title: "Scale Drawings and Maps"
type: topic
aliases: ["Scale Drawings", "Map Scale", "Scale Factor Problems"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-translation", "#word-problem-support", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Ratios_Rates_And_Proportions"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
  - "topics/pre_algebra/Unit_Rates"
  - "topics/pre_algebra/Similar_Triangles"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Ratios_Rates_And_Proportions"
  - "topics/pre_algebra/Proportions_And_Cross_Multiplication"
  - "topics/pre_algebra/Unit_Rates"
problem_type_ids: []
figures: ["pre_algebra/map_scale.svg"]
summary: "Turn drawing distances into real distances (or back) by using the scale as a ratio you can solve with a proportion."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Scale Drawings and Maps

# Scale Drawings and Maps

A map of your state fits on a single sheet of paper, but the actual state is hundreds of miles across. An architect's blueprint of a house is small enough to carry in a folder, but the house itself will fill a lot. A plastic model car sits on a desk, but the real car is longer than you are tall. Something has to shrink when a real object is drawn on paper or built as a toy, and the number that governs the shrinking (or the stretching) is called the **scale**. Once you know the scale, you can bounce back and forth between drawing measurements and real-world measurements with nothing more than a single proportion.

![[map_scale.svg|A simple road map with a scale bar showing 1 inch = 50 miles and two marked towns]]

Scale problems are everywhere in daily life: driving directions, model kits, architectural plans, dollhouses, shadow-based height problems, photocopies enlarged or reduced by a given percent. They are also a favorite of every standardized test, because they pack ratio reasoning, unit conversion, and a tiny bit of algebra into a single problem. Learning the technique well pays dividends far past pre-algebra.

## What it means / The idea

A **scale** compares a length in a drawing, map, or model to the matching real-world length. It is written as a ratio using a colon or the word "represents." Examples:

- Road map: $1 \text{ inch} : 50 \text{ miles}$ — one inch of map is fifty miles on the ground.
- Blueprint: $\tfrac{1}{4} \text{ inch} : 1 \text{ foot}$ — a quarter inch of blueprint is one foot of building.
- Model car: $1 : 24$ — one unit on the model is twenty-four units on the real car (whatever the unit is, as long as it matches on both sides).

The heart of every scale problem is the idea that the ratio between any drawing length and the matching real length is the same across the whole drawing. If one inch stands for fifty miles, then half an inch stands for twenty-five miles, three inches stand for one hundred fifty miles, and $x$ inches stand for $50x$ miles. That steady ratio is exactly what a **proportion** captures:

$$
\frac{\text{drawing distance}}{\text{real distance}} = \frac{\text{drawing distance}}{\text{real distance}}
$$

Two matching ratios set equal to each other. One side is the known scale from the map key. The other side is the pair from the specific problem, where one of the two numbers is the unknown you are solving for.

## How it works / The procedure

1. **Read the scale carefully.** Note which unit is on the drawing side and which unit is on the real side. A scale of "$1 \text{ cm} : 50 \text{ km}$" has centimeters on the drawing and kilometers on the ground, and you must keep those units straight.
2. **Write the scale as a ratio.** Put drawing length on top and real length on the bottom, or pick the opposite convention — whichever you pick, you must stick with it.
3. **Set up a proportion.** On one side put the known scale. On the other side put the specific lengths from the problem, with a variable for whichever length you do not know. Make sure the drawing-length entries are in the same corner on both sides, and same for real lengths.
4. **Cross-multiply and solve.** The proportion becomes a one-step equation that gives you the unknown length.
5. **Check the units and the size.** If the unknown is a real-world distance, does the answer look plausibly big? If it is a drawing distance, does it look plausibly small? Scale problems are easy to mess up by a factor of ten or a hundred, so a quick reasonableness check saves grief.

The same five steps cover enlargements (model-to-real) and reductions (real-to-model) in either direction.

## Why it works

Scale drawings work because they are **similar** to the original — every length is scaled by the same constant factor. If the real building's kitchen wall is five times as long as its bathroom wall, the blueprint's kitchen wall is five times as long as its bathroom wall, too. The same constant of proportionality sits underneath every length pair, which is exactly what a proportion expresses. Cross-multiplication is just the algebraic way of using that constant to escape: once you set the two ratios equal, the product of the outer pair equals the product of the inner pair, and the unknown drops out in one step.

You can also think of it as multiplying by a **scale factor**. A scale of $1 : 100$ means the real object is $100$ times as large as the model, so to go from model to real you multiply by $100$, and to go from real to model you divide by $100$. The proportion setup is doing that arithmetic for you, but it is also flexible enough to handle scales that use different units on the two sides (like inches to miles), where a raw "multiply by a number" trick gets confusing.

## Worked examples

### Example 1

Mateo is using a road map at the tutoring center for a geography project. The scale bar on the map reads $1 \text{ inch} = 50 \text{ miles}$. He measures the distance between two towns on the map and gets $3.5$ inches. Determine the real distance between the towns in miles.

Set up the proportion with drawing distance on top and real distance on the bottom. The known ratio is $1$ inch to $50$ miles. The unknown real distance, call it $d$, matches up with a $3.5$-inch drawing distance:

$$
\frac{1 \text{ in}}{50 \text{ mi}} = \frac{3.5 \text{ in}}{d}.
$$

Cross-multiply:

$$
1 \cdot d = 50 \cdot 3.5.
$$

Compute the right side: $50 \cdot 3.5 = 175$. So $d = 175$ miles. The two towns are $175$ miles apart on the actual road. Quick reasonableness check: a $3.5$-inch gap at $50$ miles per inch should be roughly $3 \cdot 50 = 150$ miles at a glance, and the exact answer of $175$ miles is in that neighborhood. Good sign.

### Example 2

Priya is building a scale model of the science fair stage at home. The architect's scale for the model is $\tfrac{1}{2} \text{ inch} = 1 \text{ foot}$. The real stage is $24$ feet long. Compute how long Priya should make the model stage in inches.

This time the unknown is the drawing length. Let $x$ be the model stage length in inches. The known ratio is $\tfrac{1}{2}$ inch per $1$ foot, and the problem pairs $x$ inches with $24$ feet:

$$
\frac{\tfrac{1}{2} \text{ in}}{1 \text{ ft}} = \frac{x \text{ in}}{24 \text{ ft}}.
$$

Cross-multiply:

$$
\tfrac{1}{2} \cdot 24 = 1 \cdot x.
$$

Simplify the left side: $\tfrac{1}{2} \cdot 24 = 12$. So $x = 12$ inches. The model stage should be $12$ inches long. Reasonableness check: at half an inch per foot, $24$ feet should give roughly half of $24$, which is $12$. Matches.

### Example 3

Leilani is reviewing a $1 : 48$ scale model airplane at the maker space. The real wingspan of the airplane is $19.2$ meters, and she wants to know the wingspan of the model in centimeters. In a $1 : 48$ scale, the units on both sides are the same, so every $1$ unit on the model stands for $48$ of the same unit on the real plane. Determine the model's wingspan in centimeters.

First, convert the real wingspan into centimeters so the units match the answer she wants: $19.2 \text{ m} = 1920 \text{ cm}$. Now set up the proportion with model on top and real on bottom:

$$
\frac{1 \text{ cm}}{48 \text{ cm}} = \frac{x \text{ cm}}{1920 \text{ cm}}.
$$

Cross-multiply:

$$
1 \cdot 1920 = 48 \cdot x,
$$

which is $1920 = 48x$. Divide both sides by $48$:

$$
x = \frac{1920}{48} = 40 \text{ cm}.
$$

The model wingspan is $40$ centimeters. A shortcut: with a $1 : 48$ scale you can just divide the real measurement by $48$, which is $1920 / 48 = 40$. The proportion setup is doing that same arithmetic but is safer when the scale involves different units like inches and miles.

## Common pitfalls

- **Putting drawing and real lengths in different corners of the two ratios.** If the drawing distance is on top in the known ratio, it must be on top in the unknown ratio too. Mismatching the corners guarantees a wrong answer — often flipped upside down from the correct one.
- **Ignoring unit conversion.** A scale like $1 \text{ cm} : 50 \text{ km}$ does not let you mix meters into the problem without converting first. Get both sides into the units the scale uses before plugging in, or convert at the end.
- **Multiplying when you should divide.** Going from model to real, you multiply by the scale factor; going from real to model, you divide. A proportion setup handles either direction automatically, which is why it is the safer tool.
- **Forgetting to reduce a scale.** A scale given as $2 : 100$ is the same as $1 : 50$. The simpler version is easier to work with and less likely to cause arithmetic slips.
- **Reading the scale backwards.** Some keys list real-to-drawing ($50 \text{ mi per in}$), others list drawing-to-real ($1 \text{ in per 50 mi}$). Read the key slowly and note which is which before setting anything up.

## Prerequisites

- [[Ratios_Rates_And_Proportions]] — a scale is a ratio and every scale problem is a proportion
- [[Proportions_And_Cross_Multiplication]] — the solving step at the center of every scale problem
- [[Unit_Rates]] — for converting between different unit systems (miles to feet, cm to km, inches to feet)

## Problems Involving Scale Drawings and Maps

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="scale_drawings_and_maps"></div>

## See Also

- [[Ratios_Rates_And_Proportions]] — the underlying ratio-reasoning toolkit
- [[Proportions_And_Cross_Multiplication]] — how the algebra step actually works
- [[Unit_Rates]] — the "miles per inch" framing is a unit rate
- [[Similar_Triangles]] — similar figures follow the same scale-factor logic
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
