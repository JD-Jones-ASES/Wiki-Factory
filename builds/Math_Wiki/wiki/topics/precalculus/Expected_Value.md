---
title: "Expected Value"
type: topic
aliases: ["Expected Value", "EV", "Weighted Average", "Mean of a Random Variable"]
tags: ["#branch-pre-calculus", "#topic-probability", "#skill-procedural-calculation", "#skill-multi-step", "#key-formula", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "algtrig", chapter: "11", section: "11.4"}
related:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/precalculus/Binomial_Probability"
  - "topics/precalculus/Permutations_And_Combinations"
  - "topics/precalculus/Conditional_Probability"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/pre_algebra/Probability_Of_Simple_And_Compound_Events"
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Mean_Median_Mode_And_Range"
problem_type_ids: []
figures: []
summary: "A single weighted sum that predicts the long-run average of a random process, used to evaluate games, grades, and any situation where each outcome carries its own payoff and its own probability."
---
> [[_overview|Home]] > [[Precalculus|Pre-Calculus & Trig]] > Expected Value

# Expected Value

Probability tells you how likely each outcome of a random process is. A payoff table tells you what each outcome is worth. **Expected value** glues those two ideas together and spits out a single number that summarizes the process — the average payoff you should anticipate per trial if you ran the process many times. It is the most useful one-number summary in probability and the single most important tool for deciding whether a game, an investment, or a gamble is worth playing.

The formula is short and almost suspiciously simple. If a random process has possible outcomes $x_1, x_2, \ldots, x_n$ with respective probabilities $p_1, p_2, \ldots, p_n$ (so that $p_1 + p_2 + \cdots + p_n = 1$), then the expected value is

$$
E[X] = x_1 p_1 + x_2 p_2 + \cdots + x_n p_n = \sum_{i=1}^{n} x_i \, p_i.
$$

In prose: multiply each outcome by its probability, then add the products. The result is a weighted average — each outcome "pulls" the mean toward itself with strength equal to its probability. The probabilities themselves act as the weights.

---

## Why the formula is an average

Imagine running the random process a huge number of times — say, ten thousand trials. Because probabilities are long-run frequencies, outcome $x_1$ should occur about $10{,}000 p_1$ times, outcome $x_2$ about $10{,}000 p_2$ times, and so on. The total payoff across all trials is approximately

$$
10{,}000 p_1 \cdot x_1 + 10{,}000 p_2 \cdot x_2 + \cdots + 10{,}000 p_n \cdot x_n.
$$

Divide that total by the number of trials to get the average payoff per trial:

$$
\dfrac{10{,}000 p_1 x_1 + \cdots + 10{,}000 p_n x_n}{10{,}000} = p_1 x_1 + p_2 x_2 + \cdots + p_n x_n.
$$

The $10{,}000$ cancels and the expression reduces to exactly $E[X]$. So the expected value is not a prediction of any single trial's outcome — it is the long-run average payoff per trial, and individual trials will usually differ from it, sometimes dramatically. The law of large numbers guarantees that as you run more and more trials, the running average settles toward $E[X]$.

---

## Fair games, losing games, winning games

If a game charges an entry fee and pays off different amounts based on the outcome of some random process, the **net payoff** on a single play is "winnings minus fee." The sign of the expected net payoff determines whether the game is **fair**, **favorable**, or **unfavorable**.

- $E[\text{net}] = 0$: a **fair** game. Over the long run, the player breaks even.
- $E[\text{net}] > 0$: a **favorable** game. The player comes out ahead on average. (These are vanishingly rare in practice — no business offers them to customers.)
- $E[\text{net}] < 0$: an **unfavorable** game. The player loses on average. (This is every casino game ever designed.)

You can write the fair-game condition two equivalent ways. Either compute the expected net payoff and ask whether it is zero, or compute the expected gross winnings and compare directly to the entry fee. When the expected gross winnings equal the entry fee, the expected net is zero and the game is fair. Both calculations give the same answer, and you can pick whichever feels cleaner for the problem in front of you.

---

## Expected value as a weighted average of grades

Expected value is often introduced through gambling scenarios, but the formula applies any time you have **numbers with weights**. A classic non-gambling example is grade calculation. Suppose a class has three components with the following weights: homework $25\%$, midterm $35\%$, final exam $40\%$. If your homework average is $92$, your midterm score is $78$, and your final exam score is $84$, your course grade is a **weighted average** with the percentages playing the role of probabilities:

$$
\text{course grade} = (0.25)(92) + (0.35)(78) + (0.40)(84).
$$

That expression has the same shape as $E[X] = \sum x_i p_i$. The three scores are the "outcomes," and the three weights (which sum to $1$) are the "probabilities." Grade calculations, GPA calculations, batting averages weighted by at-bats, portfolio returns weighted by allocation — they are all expected-value calculations wearing different hats.

---

## Example 1: a three-outcome spinner

> A spinner is divided into three unequal colored sectors. Landing on red has probability $1/2$ and wins $\$2$. Landing on blue has probability $1/3$ and wins $\$6$. Landing on green has probability $1/6$ and wins $\$12$. Determine the expected value of a single spin.

The probabilities already sum to $1/2 + 1/3 + 1/6 = 3/6 + 2/6 + 1/6 = 6/6 = 1$, so the outcome list is complete. Multiply each payoff by its probability and add:

$$
E[X] = \left(\dfrac{1}{2}\right)(2) + \left(\dfrac{1}{3}\right)(6) + \left(\dfrac{1}{6}\right)(12).
$$

Each product is a clean whole number:

$$
= 1 + 2 + 2 = 5.
$$

So a single spin is "worth" $\$5$ on average, in the long-run-frequency sense. If you spun $1000$ times, you should expect total winnings close to $\$5000$ — not because any one spin pays exactly $\$5$ (no individual spin pays that amount), but because the average across all spins converges to the expected value.

---

## Example 2: deciding whether a game is fair

> A carnival game charges $\$3$ to play. You draw a single card from a fresh standard deck. Drawing a face card (jack, queen, or king — twelve of them in a deck of $52$) wins $\$10$; drawing any other card wins nothing. Is the game fair, favorable, or unfavorable to the player?

Compute the expected gross winnings first. A face card appears with probability $12/52 = 3/13$ and pays $\$10$. Any other card appears with probability $40/52 = 10/13$ and pays $\$0$:

$$
E[\text{winnings}] = \left(\dfrac{3}{13}\right)(10) + \left(\dfrac{10}{13}\right)(0) = \dfrac{30}{13} \approx 2.31.
$$

The expected winnings of about $\$2.31$ fall short of the $\$3$ entry fee, so the expected net payoff is

$$
E[\text{net}] = 2.31 - 3.00 = -0.69.
$$

The game is **unfavorable**: every play loses about $\$0.69$ on average. Over $100$ plays, a typical player should expect to lose about $\$69$ — the carnival's profit per hundred customers. To make the game fair, the entry fee would have to drop to about $\$2.31$, or the prize would have to rise to $13$ dollars (since $(3/13)(13) = 3$ exactly).

---

## Example 3: a weighted course grade

> A semester course has three components: participation ($15\%$), two midterms ($25\%$ each), and a final ($35\%$). What is the course grade of a student who earns $95$ on participation, $72$ and $80$ on the two midterms, and $86$ on the final?

Treat each percentage as a probability-like weight and multiply by the corresponding score:

$$
\text{grade} = (0.15)(95) + (0.25)(72) + (0.25)(80) + (0.35)(86).
$$

Work the four products one at a time to keep the arithmetic clean:

$$
(0.15)(95) = 14.25, \qquad (0.25)(72) = 18.00, \qquad (0.25)(80) = 20.00, \qquad (0.35)(86) = 30.10.
$$

Sum the four products:

$$
\text{grade} = 14.25 + 18.00 + 20.00 + 30.10 = 82.35.
$$

The course grade is $82.35$. Cross-check the weights first: $0.15 + 0.25 + 0.25 + 0.35 = 1.00$. Good. If they had not summed to $1$, you would either be missing a component or have a typo in one of the weights, and no amount of correct multiplication downstream would rescue the answer.

Notice that a simple (unweighted) average of the four raw scores would give $(95 + 72 + 80 + 86)/4 = 333/4 = 83.25$, which differs from the weighted answer. The difference matters: because the final is worth more than participation, the comparatively low participation pull matters less and the final pulls harder. Weighted averages always differ from plain averages whenever the weights are uneven.

---

## Common pitfalls

- **Forgetting to check that probabilities sum to $1$.** If $\sum p_i \neq 1$, you either missed an outcome or miscounted the sample space. The expected-value formula assumes a complete outcome list.
- **Confusing gross winnings with net payoff.** A game with $\$3$ entry and $\$10$ jackpot is not "worth $\$10$ times the jackpot probability" to the player — the player also paid $\$3$ up front. Subtract the entry fee.
- **Treating the expected value as a prediction of a single trial.** No single spin of the spinner in Example 1 pays exactly $\$5$; the possible single-spin payoffs are $\$2$, $\$6$, or $\$12$. $E[X]$ is a long-run average, not a forecast for the next spin.
- **Using the arithmetic mean when the problem asks for a weighted mean.** When weights are uneven — different credit hours, different exam percentages, different trial sizes — an unweighted average gives the wrong answer.
- **Dropping a sign on a negative outcome.** Losses enter the formula as **negative** payoffs. A game with a $\$5$ loss outcome needs $x_i = -5$, not $5$, or the expected value will be overstated.

---

## Prerequisites

- [[Probability_Of_Simple_And_Compound_Events]] — the source of the $p_i$ values.
- [[Fractions_Decimals_And_Percents]] — for fluid conversion between the two forms that probabilities take in real problems.
- [[Mean_Median_Mode_And_Range]] — the plain-average concept that expected value generalizes.

---

## Problems Involving Expected Value

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="expected_value"></div>

---

## See Also

- [[Binomial_Probability]] — where expected value collapses to the simple shortcut $np$
- [[Permutations_And_Combinations]] — the counting arithmetic that feeds probabilities in many EV problems
- [[Conditional_Probability]] — probabilities that change when information arrives, and the expected values that track with them
- [[Mean_Median_Mode_And_Range]] — the pre-algebra idea that EV generalizes
- [[Precalculus|Pre-Calculus & Trig]]
- [[Topics_Overview]]
- [[_overview|Home]]
