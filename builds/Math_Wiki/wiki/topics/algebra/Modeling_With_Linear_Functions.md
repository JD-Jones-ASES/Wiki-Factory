---
title: "Modeling with Linear Functions"
type: topic
aliases: ["Linear Models", "Linear Modeling"]
tags: ["#branch-algebra-2", "#topic-functions", "#topic-linear", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "2", section: "2.4"}
related:
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Slope"
  - "topics/algebra/Slope_Intercept_Form"
  - "topics/algebra/Writing_Linear_Equations"
  - "topics/algebra/Systems_Of_Linear_Equations"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Linear_Functions"
  - "topics/algebra/Slope"
  - "topics/algebra/Slope_Intercept_Form"
problem_type_ids: []
figures: []
summary: "Turning a real-world, constant-rate scenario into a linear function and using it to predict."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Modeling with Linear Functions

# Modeling with Linear Functions

The world is full of situations where one quantity grows or shrinks at a steady rate from some starting point: a pay stub that goes up by a fixed amount per hour worked, a gas tank that drains by a fixed number of gallons per mile, a monthly bill built from a flat fee plus a per-use charge. Whenever you can describe a situation with the phrase "a fixed starting value, plus a constant rate times something," you are looking at a linear model — and the tool you use to capture it is a [[Linear_Functions|linear function]].

A linear model is nothing more than this familiar form, given a job to do:

$$
f(x) = mx + b
$$

What makes modeling different from evaluating is that now the letters stand for things you can touch. The number $m$ is a **rate of change** in real-world units — dollars per mile, degrees per hour, gallons per minute. The number $b$ is an **initial value** — a starting amount, a flat fee, a base measurement — whatever quantity you have before the rate has had time to act.

---

## A four-step recipe

Modeling problems are long, but the approach is short. Every time you build a linear model, do the same four things:

1. **Name the variables.** Decide which quantity you will feed into the model (the independent variable) and which one you want it to predict (the dependent variable). Give them letters.
2. **Find the rate of change.** This is the slope $m$. Look for the phrase "per" in the problem — "dollars per text," "meters per second," "miles per gallon." The number in front of "per" is almost always your slope, with the right sign.
3. **Find the starting value.** This is the y-intercept $b$. Look for words like "flat fee," "initial," "base," "sea level," or "when $x = 0$." It is the amount already in place before anything happens.
4. **Write the function and use it.** Combine $m$ and $b$ into $f(x) = mx + b$, then answer whatever the problem asks by plugging in or solving.

Once the function is written, every follow-up question — "how much does it cost for 20 miles?", "when does the tank run dry?", "when does plan A beat plan B?" — is just arithmetic.

---

## Example 1: a gym membership

> A neighborhood gym charges a one-time joining fee of $\$30$ plus a monthly rate of $\$15$. Write a linear function $C(t)$ that gives the total amount a member has paid after $t$ months. Use it to find the cost after one year, and to find how long it takes before a member has paid $\$150$.

**Identify the variables.** Let $t$ be the number of months (independent), and let $C(t)$ be the total dollars paid so far (dependent).

**Identify the slope.** The monthly rate is $\$15$ per month. Every time $t$ grows by one, $C$ grows by $15$. So $m = 15$, and the units are dollars per month.

**Identify the y-intercept.** Before any months have passed, the member has already paid the joining fee of $\$30$. That is the amount when $t = 0$, so $b = 30$, and the units are dollars.

**Write the model.**

$$
C(t) = 15t + 30
$$

In this model, the slope $m = 15$ means "the cost increases by $\$15$ for each additional month of membership." The y-intercept $b = 30$ means "the member has already paid $\$30$ at the moment they sign up, before any monthly fees." Naming both meanings out loud is the whole point — this is where your algebra meets the world.

**Cost after one year.** One year is $t = 12$, so

$$
C(12) = 15(12) + 30 = 180 + 30 = \$210.
$$

**When does the total reach $\$150$?** Set $C(t) = 150$ and solve:

$$
15t + 30 = 150 \quad\Longrightarrow\quad 15t = 120 \quad\Longrightarrow\quad t = 8 \text{ months}.
$$

---

## Example 2: a road trip

> At noon, a car is $60$ miles north of its starting city, driving north on a highway at a steady speed. One hour later, at 1:00 PM, the car is $125$ miles north. Write a linear function $D(t)$ that gives the car's distance from the starting city (in miles) as a function of hours after noon. What is the car's speed, and where will it be at 4:00 PM?

**Name the variables.** Let $t$ be the number of hours after noon, and let $D(t)$ be the distance from the starting city in miles.

**Find the slope.** Between noon and 1:00 PM, the distance grew from $60$ miles to $125$ miles — an increase of $65$ miles in one hour. The slope is

$$
m = \frac{125 - 60}{1 - 0} = 65 \text{ miles per hour}.
$$

In this model, the slope $m = 65$ is literally the car's **speed**: every additional hour adds $65$ miles to the distance. Slope and speed are the same idea wearing different clothes.

**Find the y-intercept.** At $t = 0$ (noon), the car was already $60$ miles away from the starting city. That is the initial value, so $b = 60$. Meaning: $b = 60$ is the distance from the starting city at the moment the clock starts, not the distance from the car itself. Without it, the model would claim the car was sitting at the starting city at noon — which is wrong.

**Write the model.**

$$
D(t) = 65t + 60
$$

**Where is the car at 4:00 PM?** Four o'clock is four hours after noon, so $t = 4$:

$$
D(4) = 65(4) + 60 = 260 + 60 = 320 \text{ miles north of the starting city}.
$$

---

## Example 3: draining a tank

> A rainwater collection tank holds $2{,}400$ gallons when it is full. A valve at the bottom drains the tank at a steady rate of $30$ gallons per minute. Write a linear function $V(t)$ that gives the volume of water in the tank $t$ minutes after the valve is opened, then interpret the slope and intercept, and find how long it takes for the tank to run empty.

**Name the variables.** Let $t$ be the number of minutes after the valve opens, and let $V(t)$ be the gallons of water remaining in the tank.

**Find the slope.** The tank is losing $30$ gallons every minute. Because the volume is going down, the rate of change is negative: $m = -30$, in units of gallons per minute.

**Find the y-intercept.** At $t = 0$, the tank is full: $2{,}400$ gallons. So $b = 2400$, measured in gallons.

**Write the model.**

$$
V(t) = -30t + 2400
$$

**Interpret the numbers in context.** The slope $m = -30$ means "the tank loses $30$ gallons every minute the valve is open" — the negative sign is what makes it shrinking rather than growing. The y-intercept $b = 2400$ means "at the instant the valve opens, the tank already contains $2{,}400$ gallons of water." Both pieces are required; neither is the full story by itself.

**When does the tank empty?** Set $V(t) = 0$ and solve:

$$
-30t + 2400 = 0 \quad\Longrightarrow\quad 30t = 2400 \quad\Longrightarrow\quad t = 80 \text{ minutes}.
$$

So the tank drains completely after $80$ minutes — roughly an hour and twenty minutes.

---

## A note on sign

The sign of the slope always carries meaning, and you should always check it against the story. A shrinking quantity — water draining, fuel burning, a balance going down — has a **negative** slope. A growing quantity — a bill increasing, a bank account earning a fixed amount, a position moving forward — has a **positive** slope. If your answer has the wrong sign, the model will still compute numbers, but they will describe the wrong world.

---

## A note on units

Always attach units to both $m$ and $b$. In the gym example, the slope is not just $15$; it is $15$ dollars per month. In the road trip, the slope is not just $65$; it is $65$ miles per hour. Unit-free numbers are the fastest way to get the wrong answer: the same digits could mean gallons, miles, or dollars, and only the units tell you which. Writing them down every time also gives you a free check — if your "cost" came out in "hours," you multiplied the wrong two things.

---

## Common pitfalls

- **Confusing the slope with a single output.** The slope is a rate — something "per" something else. It is not the cost of one month, or the distance at 1:00 PM, unless those happen to coincide numerically.
- **Forgetting the initial value.** Leaving off $b$ is the most common modeling mistake. If the problem mentions a flat fee, a joining cost, a starting distance, or a full tank, that number belongs in the y-intercept, not the slope.
- **Using the wrong sign.** Anything "shrinking," "draining," "losing," or "decreasing" contributes a negative slope. Check the sign by asking, "does the output grow when $t$ grows?" If no, $m$ is negative.
- **Skipping the interpretation step.** A model is not finished until you can say, in English, what $m$ means and what $b$ means in the language of the problem. If you cannot say it, you probably built the model from the wrong numbers.

---

## Prerequisites

Before you work practice problems, make sure you are comfortable with:

- [[Linear_Functions]] — the object you are building
- [[Slope]] — so you can recognize a rate of change in the wild
- [[Slope_Intercept_Form]] — the form $y = mx + b$, the scaffolding of every linear model

---

## Problems Involving Modeling with Linear Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="modeling_with_linear_functions"></div>

_Practice generators for this topic are coming in the Cluster 2 generator wave of this session._

---

## See Also

- [[Linear_Functions]]
- [[Slope]]
- [[Slope_Intercept_Form]]
- [[Writing_Linear_Equations]]
- [[Systems_Of_Linear_Equations]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
