---
title: "Growth, Decay, and Applications"
type: topic
aliases: ["Exponential Growth and Decay", "Exponential Applications", "Exponential Models"]
tags: ["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-functions", "#word-problem-support", "#representation-verbal", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.7"}
related:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Exponential_Equations"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Logarithmic_Equations"
  - "topics/algebra/Simple_And_Compound_Interest"
  - "topics/algebra/Applications_Of_Exponentials_And_Logarithms"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Exponential_Equations"
  - "topics/algebra/Logarithms"
problem_type_ids: []
figures: ["algebra/compound_growth_comparison.svg"]
summary: "Real-world exponential models: population growth, radioactive decay, half-life, compound interest, and depreciation."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Growth, Decay, and Applications

# Growth, Decay, and Applications

Exponential functions are not just abstract curves on a grid — they are the mathematical shape that countless real-world situations take. Whenever a quantity grows or shrinks in proportion to how much of it is already present, you are looking at exponential behavior. Populations of bacteria double in roughly constant time. Radioactive atoms halve on a fixed schedule. Bank balances swell with interest that earns its own interest. Used cars lose a steady percentage of their value every year. Each of these stories turns into a recipe built from the same ingredients: a starting amount, a rate that describes how fast things change, and a time variable.

The job for this topic is translation. A word problem gives you a story; you must decide which formula models the situation, identify the parameters, substitute carefully, and interpret the final number in the language of the original story. The algebra is nothing new — you already know how to solve [[Exponential_Equations|exponential equations]] — but the first step is recognizing the right template.

---

## The five classic templates

Most problems in this section fit one of five patterns. Keep this short list in mind and half the translation work is done before you start.

**1. Population growth (per-period).**

$$
P(t) = P_0 (1 + r)^t
$$

Here $P_0$ is the starting population, $r$ is the growth rate per period (as a decimal, e.g. $0.03$ for $3\%$), and $t$ is the number of periods. The factor $1 + r$ is the multiplier applied each period.

**2. Exponential decay / depreciation.**

$$
V(t) = V_0 (1 - r)^t
$$

Same idea as growth, but now the per-period factor is less than $1$ because $r$ is being subtracted. This is the model for a car losing value, a population in decline, or any quantity that shrinks by a fixed percentage each period.

**3. Half-life decay.**

$$
A(t) = A_0 \left(\dfrac{1}{2}\right)^{t/T}
$$

When a radioactive material — or anything with a known halving interval — has half-life $T$, the model uses base $\tfrac{1}{2}$ and a **scaled** time variable $t/T$. The exponent counts how many half-lives have passed, and each whole-number exponent corresponds to another halving of the amount.

**4. Compound interest (discrete compounding).**

$$
A = P \left(1 + \dfrac{r}{n}\right)^{nt}
$$

Here $P$ is the principal (the starting deposit), $r$ is the annual rate as a decimal, $n$ is the number of compounding periods per year, and $t$ is the number of years. The per-period rate is $r/n$, and the total number of compoundings is $nt$. See [[Simple_And_Compound_Interest]] for a deeper look at the different compounding schedules.

**5. Continuous growth/decay (natural exponential).**

$$
A(t) = A_0 e^{kt}
$$

The continuous form uses the natural base $e$. When $k > 0$ the model describes growth; when $k < 0$ it describes decay. This shape appears in physics, biology, and chemistry as the default model for anything changing at a rate proportional to itself. Continuous compound interest uses the same formula with $k = r$: $A = P e^{rt}$.

Every story problem in this section eventually lives inside one of those five forms. Your first move on any new problem is deciding which of them fits.

![[compound_growth_comparison.svg|Comparing simple, annual, monthly, and continuous compounding]]

---

## A four-step approach to application problems

The algebra is the easy part. The hard part is the translation. For every word problem you meet, walk through the same four steps:

1. **Choose the right formula.** Does the problem say "doubles"? "Halves"? "Annual rate"? "Continuously"? "Per month"? Those words are hints that point to one specific template from the list above.
2. **Name the parameters.** Pull each number in the problem out and label it: initial value, rate, time, period length. Write down the units for every one.
3. **Substitute and solve.** Plug the parameters into the formula. If the unknown is the output (how much is left? how much is there after $t$ years?), compute it directly. If the unknown is the time (how long until... ?), you will be solving an [[Exponential_Equations|exponential equation]] — typically with a logarithm.
4. **Interpret the answer in context.** A bare number is not the answer. "After $20$ years, the population is approximately $396{,}000$ people" is the answer. Always restate the result in the language of the original story, with the right units attached.

---

## Example 1: population growth

> A small city had a population of $250{,}000$ people in the year 2010. If the population grows at a steady $2.3\%$ per year, estimate the population in the year 2030.

**Pick the formula.** "Grows at a steady rate per year" is the signal for the per-period growth model $P(t) = P_0 (1 + r)^t$.

**Identify the parameters.**

- Starting population: $P_0 = 250{,}000$ (units: people)
- Annual rate: $r = 0.023$ (units: per year)
- Time elapsed: $t = 2030 - 2010 = 20$ (units: years)

**Substitute and compute.** The per-year multiplier is $1 + 0.023 = 1.023$, so

$$
P(20) = 250{,}000 \cdot (1.023)^{20}.
$$

A calculator gives $(1.023)^{20} \approx 1.5794$, so

$$
P(20) \approx 250{,}000 \cdot 1.5794 \approx 394{,}850.
$$

**Interpret.** The model predicts that in 2030 the city's population will be roughly $395{,}000$ people — almost $60\%$ larger than its 2010 size. Always check the plausibility of the number: a $2.3\%$ annual rate over $20$ years should produce a noticeable but not extreme increase, and a jump from $250{,}000$ to around $395{,}000$ fits that expectation.

---

## Example 2: radioactive half-life

> Carbon-14 has a half-life of approximately $5{,}730$ years. Suppose a piece of ancient wood is found to contain $30\%$ of the carbon-14 it would have had while the tree was alive. Roughly how old is the wood?

**Pick the formula.** A half-life is given, so use the half-life decay model $A(t) = A_0 \left(\tfrac{1}{2}\right)^{t/T}$.

**Identify the parameters.**

- Initial amount: $A_0$ is the amount the wood had when the tree was alive. The problem doesn't give a number, but that is fine — it will cancel.
- Current amount: $A(t) = 0.30 A_0$ (thirty percent of the original).
- Half-life: $T = 5730$ years.
- Unknown: the time $t$, in years.

**Substitute and solve.** Plug into the formula:

$$
0.30 A_0 = A_0 \left(\dfrac{1}{2}\right)^{t/5730}.
$$

Divide both sides by $A_0$ (both sides of the equation had the initial amount hanging off them, and it falls out cleanly):

$$
0.30 = \left(\dfrac{1}{2}\right)^{t/5730}.
$$

There is no shared base here, so apply the natural log to each side and use the Power Rule from [[Properties_Of_Logarithms]]:

$$
\ln(0.30) = \dfrac{t}{5730} \cdot \ln\left(\dfrac{1}{2}\right).
$$

Solve for $t$:

$$
t = \dfrac{5730 \cdot \ln(0.30)}{\ln(1/2)}.
$$

Plug in: $\ln(0.30) \approx -1.2040$ and $\ln(1/2) \approx -0.6931$, so

$$
t \approx \dfrac{5730 \cdot (-1.2040)}{-0.6931} \approx 9{,}950 \text{ years}.
$$

**Interpret.** The wood is approximately $9{,}950$ years old. A sanity check: two half-lives would bring the sample to $25\%$ of the original, and two half-lives is $11{,}460$ years; the wood has a bit more than $25\%$ remaining ($30\%$), so it should be a bit **less** old than $11{,}460$ years. Our answer of about $9{,}950$ years fits.

---

## Example 3: compound interest

> A parent deposits $\$5{,}000$ into an account that pays $6\%$ annual interest, compounded monthly. How much is in the account after $10$ years?

**Pick the formula.** The problem says "compounded monthly," a dead giveaway for the discrete compound interest formula $A = P \left(1 + \tfrac{r}{n}\right)^{nt}$.

**Identify the parameters.**

- Principal: $P = 5000$ (units: dollars)
- Annual rate: $r = 0.06$ (units: per year)
- Compoundings per year: $n = 12$ (monthly, so twelve times per year)
- Time: $t = 10$ (units: years)

**Substitute and compute.** The per-period rate is $\dfrac{0.06}{12} = 0.005$, and the total number of compoundings is $12 \cdot 10 = 120$. So

$$
A = 5000 \cdot (1.005)^{120}.
$$

A calculator gives $(1.005)^{120} \approx 1.8194$, so

$$
A \approx 5000 \cdot 1.8194 \approx \$9{,}096.98.
$$

**Interpret.** After ten years, the account holds roughly $\$9{,}097$ — almost double the original deposit. A useful mental check: at a $6\%$ rate, the rule-of-thumb doubling time is about $12$ years ($72 / 6$), so you'd expect the balance to be a little short of doubled after $10$ years. The answer lines up.

---

## Example 4: continuous compounding and doubling time

> An investment account earns $5\%$ interest compounded continuously. How many years does it take for the balance to double, regardless of how much was originally deposited?

**Pick the formula.** "Compounded continuously" sends you to the natural exponential model $A(t) = A_0 e^{rt}$.

**Identify the parameters.**

- Initial amount: $A_0$ (whatever the starting deposit is; we will see it cancel).
- Rate: $r = 0.05$ (units: per year).
- Target: $A(T) = 2 A_0$, meaning the balance has doubled.

**Set up the equation.** The condition "balance has doubled" is

$$
2 A_0 = A_0 \cdot e^{0.05 T}.
$$

**Solve for $T$.** Divide both sides by $A_0$ (the starting amount cancels — the doubling time doesn't depend on how much you start with, a clean and maybe surprising fact):

$$
2 = e^{0.05 T}.
$$

Apply the natural log to each side:

$$
\ln 2 = 0.05 T \quad \Longrightarrow \quad T = \dfrac{\ln 2}{0.05}.
$$

Compute: $\ln 2 \approx 0.6931$, so

$$
T \approx \dfrac{0.6931}{0.05} \approx 13.86 \text{ years}.
$$

**Interpret.** At a continuously compounded rate of $5\%$, any amount in the account doubles in about $13.86$ years. The initial deposit is irrelevant; only the rate matters. This is a handy fact to have when you compare accounts — a higher rate shortens the doubling time, a lower rate stretches it, and the relationship is the same regardless of the principal.

---

## Example 5: depreciation

> A new car is purchased for $\$28{,}000$. It loses $15\%$ of its value each year. What is the car worth after $6$ years?

**Pick the formula.** A fixed percentage loss per year is the depreciation model $V(t) = V_0 (1 - r)^t$.

**Identify the parameters.**

- Initial value: $V_0 = 28{,}000$ (units: dollars)
- Annual loss rate: $r = 0.15$
- Time: $t = 6$ (units: years)

**Substitute and compute.** The per-year multiplier is $1 - 0.15 = 0.85$, so

$$
V(6) = 28{,}000 \cdot (0.85)^6.
$$

A calculator gives $(0.85)^6 \approx 0.3771$, so

$$
V(6) \approx 28{,}000 \cdot 0.3771 \approx \$10{,}560.
$$

**Interpret.** After six years of $15\%$-per-year depreciation, the car is worth approximately $\$10{,}560$ — a little over a third of its sticker price. Notice that this is not the same as losing $15 \cdot 6 = 90\%$ of the value in six years. Each year's loss is taken from the new, smaller value, so depreciation slows down in absolute terms even though the percentage stays constant.

---

## Common pitfalls

- **Writing the rate as a percent instead of a decimal.** A $3\%$ rate is $r = 0.03$, not $r = 3$. Using $3$ directly turns the model into runaway nonsense.
- **Skipping the "initial" step in a half-life problem.** Students sometimes plug in the remaining amount as the starting amount. The formula wants the original quantity in the $A_0$ slot; the current amount goes on the left side of the equation.
- **Forgetting to match units between rate and time.** If the rate is per month, the time must be in months. If the rate is annual and the time is in months, convert before substituting.
- **Leaving the answer without context.** "$9{,}950$" is not an answer; "$9{,}950$ years" is. Make a habit of writing the unit every time.
- **Confusing discrete and continuous compounding.** A $5\%$ annual rate compounded continuously does not give exactly the same result as $5\%$ compounded monthly or yearly. When in doubt, use the formula the problem specifies — the word "continuously" is the distinguishing signal.
- **Applying per-period decay to a problem with a half-life.** If the problem gives a half-life, use the half-life formula. If it gives a per-year loss rate, use the depreciation formula. The two shapes look similar but use different numbers.

---

## Prerequisites

Before you practice problems in this topic, make sure you are comfortable with:

- [[Exponential_Functions]] — the family of curves behind every one of these models
- [[Exponential_Equations]] — the techniques for solving when the unknown is in the exponent
- [[Logarithms]] — so that $\ln$ and $\log$ are familiar tools, not obstacles

---

## Problems Involving Growth, Decay, and Applications

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="growth_decay_and_applications"></div>

---

## See Also

- [[Exponential_Functions]]
- [[Exponential_Equations]]
- [[Logarithmic_Functions]]
- [[Simple_And_Compound_Interest]]
- [[Applications_Of_Exponentials_And_Logarithms]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
