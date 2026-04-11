---
title: "Applications of Exponentials and Logarithms"
type: topic
aliases: ["Exponential Applications", "Exp/Log Models", "Continuous Growth and Decay"]
tags: ["#branch-pre-calculus", "#topic-logarithms", "#topic-functions", "#word-problem-support", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "6", section: "6.2"}
related:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Exponential_Equations"
  - "topics/algebra/Growth_Decay_And_Applications"
  - "topics/algebra/Logarithmic_Equations"
  - "topics/precalculus/Introduction_To_Exponentials_And_Logarithms"
  - "topics/precalculus/Properties_Of_Logarithms"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Logarithms"
  - "topics/precalculus/Properties_Of_Logarithms"
problem_type_ids: []
figures: []
summary: "Pre-calc-level real-world models: continuous compounding, growth and decay, Newton's law of cooling, and the log scales used for earthquakes, sound, and acidity."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Applications of Exponentials and Logarithms

# Applications of Exponentials and Logarithms

The entire point of spending weeks on exponential and logarithmic mechanics is that they describe a breathtaking chunk of reality. Money compounding in an account, bacteria doubling in a petri dish, uranium slowly disappearing inside a rock, a cup of coffee cooling on a countertop, an earthquake rattling a building — all of them follow the same mathematical family. Change base, change sign on the exponent, adjust one constant, and the shape of the curve is the same.

This page shifts from the algebraic rules of [[Introduction_To_Exponentials_And_Logarithms]] and [[Properties_Of_Logarithms]] to what you actually do with them. Every example ends with the same manoeuvre: the unknown is trapped inside an exponent, and a logarithm is the tool that pries it out.

---

## Key ideas

**The natural base $e$ shows up because of compounding taken to the limit.** If an investment pays interest $n$ times per year, the balance after $t$ years is $P(1 + r/n)^{nt}$. Let $n$ grow without bound (interest credited every second, every microsecond, every instant) and the limit settles onto a single clean formula. That limit defines $e$, and it produces the model for **continuous compound interest**:

$$
A = P e^{rt}.
$$

Here $P$ is the starting principal, $r$ is the annual rate written as a decimal, $t$ is time in years, and $A$ is the ending balance. It is the most elegant version of the compounding story.

**A single growth-rate constant describes any exponentially growing quantity.** If a population, a culture of cells, or a savings balance grows continuously at some per-unit-time rate $k > 0$, the size at time $t$ is

$$
N(t) = N_0 \, e^{kt}.
$$

The constant $N_0 = N(0)$ is the size at the starting time, and $k$ is the continuous growth rate. The larger $k$ is, the steeper the climb.

**Decay is the same formula with a flipped sign.** For a quantity that loses a fixed fraction of itself per unit of time — a radioactive isotope, a drug being cleared from the bloodstream, a cooling object — use

$$
N(t) = N_0 \, e^{-kt}
$$

with $k > 0$. Writing the minus sign explicitly is a helpful convention: the "$k$" itself is always positive, and whether the curve rises or falls is controlled by the sign on the exponent.

**Newton's law of cooling gives the temperature of an object drifting toward its environment.** If an object at temperature $T_0$ is placed in surroundings held at a constant temperature $T_{\text{env}}$, the temperature $t$ minutes later is

$$
T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) \, e^{-kt}.
$$

The leftover temperature difference $T_0 - T_{\text{env}}$ decays exponentially toward zero, so the object's temperature approaches $T_{\text{env}}$ without ever quite getting there. The same formula works whether you are cooling a roast in a cold kitchen or warming an ice cube in a warm room.

**Logarithmic scales compress huge ranges into manageable numbers.** When a physical quantity spans many orders of magnitude — earthquake energy, sound intensity, hydrogen ion concentration — a linear scale is useless. The fix is to take a log. Three famous examples:

- **Richter magnitude** for earthquakes: $M = \log(I/I_0)$, where $I$ is the recorded intensity and $I_0$ is a reference intensity. A magnitude $6$ quake releases ten times more wave amplitude than a magnitude $5$.
- **pH** for acidity: $\mathrm{pH} = -\log[\mathrm{H}^+]$, where $[\mathrm{H}^+]$ is the hydrogen-ion concentration in moles per litre. A drop of one pH unit means ten times more hydrogen ions.
- **Decibels** for sound: $L = 10 \log(I/I_0)$, where $I$ is the sound intensity and $I_0$ is the threshold of hearing. A $10$-decibel increase means ten times more intensity.

Every log scale uses the same trick: take the ratio to a reference, then squish it with a log.

---

## Example 1: continuous compounding, solving for time

> You deposit $\$5{,}000$ in an account that earns $4\%$ interest compounded continuously. How long does it take for the balance to double? Use $\ln(2) \approx 0.6931$.

Let $A$ be the balance at time $t$. The continuous-compounding model gives

$$
A = 5000 \, e^{0.04 t}.
$$

Doubling means $A = 10{,}000$, so

$$
10000 = 5000 \, e^{0.04 t} \;\;\Longrightarrow\;\; 2 = e^{0.04 t}.
$$

The unknown $t$ is stuck in the exponent. Take the natural log of both sides and use $\ln(e^x) = x$:

$$
\ln(2) = 0.04 \, t \;\;\Longrightarrow\;\; t = \frac{\ln(2)}{0.04} \approx \frac{0.6931}{0.04} \approx 17.33 \text{ years.}
$$

So the balance doubles in roughly $17$ years and $4$ months. Notice that the starting principal $5000$ dropped out of the problem entirely: any continuously compounded account at $4\%$ doubles in the same time, no matter how much you put in. That quantity is called the doubling time, and every growth rate has one.

---

## Example 2: radioactive decay and half-life

> Carbon-$14$ decays continuously with $k \approx 0.0001213$ per year. A bone fragment in an archaeological site contains $38\%$ of the carbon-$14$ it would have had when the animal was alive. Estimate the age of the bone.

The decay model is

$$
N(t) = N_0 \, e^{-0.0001213 \, t}.
$$

"38% of the original" means $N(t) / N_0 = 0.38$, so

$$
0.38 = e^{-0.0001213 \, t}.
$$

Take $\ln$ of both sides to free the exponent:

$$
\ln(0.38) = -0.0001213 \, t.
$$

Now $\ln(0.38) \approx -0.9676$, which gives

$$
t = \frac{-0.9676}{-0.0001213} \approx 7977 \text{ years.}
$$

The sign cancellation is worth pausing over: $\ln$ of a number between $0$ and $1$ is negative, and the $-k$ on the right is also negative, so the time comes out positive as it must. The bone is about $8{,}000$ years old.

---

## Example 3: Newton's law of cooling, finding $k$

> A cup of coffee brewed at $180^\circ$F is left on a countertop in a room held at $70^\circ$F. After five minutes the coffee has cooled to $150^\circ$F. How much longer until it reaches a safe drinking temperature of $115^\circ$F?

The temperature follows

$$
T(t) = 70 + (180 - 70) \, e^{-kt} = 70 + 110 \, e^{-kt}.
$$

The single unknown constant is $k$. Use the five-minute data point: $T(5) = 150$.

$$
150 = 70 + 110 \, e^{-5k} \;\;\Longrightarrow\;\; 80 = 110 \, e^{-5k} \;\;\Longrightarrow\;\; e^{-5k} = \frac{80}{110} = \frac{8}{11}.
$$

Take $\ln$ of both sides, then divide by $-5$:

$$
-5k = \ln(8/11) \;\;\Longrightarrow\;\; k = -\tfrac{1}{5}\ln(8/11) \approx \tfrac{1}{5}(0.3185) \approx 0.0637.
$$

Now plug this $k$ back into the model and ask: for what $t$ does $T(t) = 115$?

$$
115 = 70 + 110 \, e^{-0.0637 t} \;\;\Longrightarrow\;\; 45 = 110 \, e^{-0.0637 t} \;\;\Longrightarrow\;\; e^{-0.0637 t} = \frac{45}{110} \approx 0.4091.
$$

One more log:

$$
-0.0637 \, t = \ln(0.4091) \approx -0.8938 \;\;\Longrightarrow\;\; t \approx \frac{0.8938}{0.0637} \approx 14.03 \text{ minutes.}
$$

So the coffee hits $115^\circ$F about $14$ minutes after you poured it. The first five minutes were already up, so you need to wait another $9$ minutes or so. Every variation of this cooling problem has the same shape: use one data point to find $k$, then use the model to answer a future-time question.

---

## Example 4: a log scale, from sound to intensity

> One rock concert registers $110$ decibels at a fan's seat; a jet engine at the same distance is $130$ decibels. How many times more intense is the jet engine?

Both sounds obey $L = 10 \log(I / I_0)$ with the same reference $I_0$. Call the concert intensity $I_1$ and the jet intensity $I_2$. Then

$$
110 = 10 \log(I_1 / I_0) \quad\text{and}\quad 130 = 10 \log(I_2 / I_0).
$$

Subtract the first from the second:

$$
20 = 10 \log(I_2 / I_0) - 10 \log(I_1 / I_0) = 10 \bigl[\log(I_2/I_0) - \log(I_1/I_0)\bigr].
$$

The quotient rule for logs contracts the bracket into a single log of a ratio:

$$
20 = 10 \log\!\left(\frac{I_2/I_0}{I_1/I_0}\right) = 10 \log\!\left(\frac{I_2}{I_1}\right).
$$

Divide by $10$ and convert back from log form to exponential form:

$$
\log\!\left(\frac{I_2}{I_1}\right) = 2 \;\;\Longrightarrow\;\; \frac{I_2}{I_1} = 10^2 = 100.
$$

The jet engine is $100$ times more intense than the concert. A $20$-decibel jump always means an intensity ratio of $100$; a $30$-decibel jump means a ratio of $1000$. The linear feel of decibels hides an enormous dynamic range inside a tidy log.

---

## Common pitfalls

- **Mistaking "growth rate" for "per-year percent increase."** The $k$ in the continuous-growth model $N_0 e^{kt}$ is not the same as a stated annual percentage. A continuously compounded $5\%$ rate grows faster per year than a flat $5\%$ added once, because the interest keeps on itself.
- **Dropping the minus sign in a decay problem.** If you write $N_0 e^{kt}$ with a positive $k$ when you meant decay, the model predicts growth and every downstream answer is wrong. Make the sign explicit: $N_0 e^{-kt}$ with $k > 0$.
- **Taking the wrong log for the problem.** For continuous models built on $e$, use $\ln$. For base-$10$ log scales (pH, decibels, Richter), use $\log$. Mixing them up gives a silent numerical error.
- **Forgetting that $T - T_{\text{env}}$, not $T$, is what decays.** Newton's law of cooling drives the temperature **difference** to zero, not the temperature itself. The environment shows up twice in the formula for a reason.
- **Treating a log scale like a linear scale.** The difference between a magnitude $5$ and a magnitude $7$ earthquake is not "twice as strong" — it is a factor of $10^2 = 100$ in amplitude, and roughly $1000$ in released energy.

---

## Prerequisites

Before tackling application problems, you should be comfortable with:

- [[Exponential_Functions]] — the $b^x$ family and how its graph behaves
- [[Logarithms]] — the definition of a log and basic evaluation
- [[Properties_Of_Logarithms]] — especially the power rule, which is what lets you solve for a variable in the exponent

---

## Problems Involving Applications of Exponentials and Logarithms

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="applications_of_exponentials_and_logarithms"></div>

---

## See Also

- [[Introduction_To_Exponentials_And_Logarithms]]
- [[Properties_Of_Logarithms]]
- [[Growth_Decay_And_Applications]]
- [[Exponential_Equations]]
- [[Logarithmic_Equations]]
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
