---
title: "Logarithmic Equations"
type: topic
aliases: ["Log Equations", "LogEquations"]
tags: ["#branch-algebra-2", "#topic-logarithms"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.5"}
  - {book: "algtrig", chapter: "6", section: "6.4"}
related:
  - "topics/algebra/Logarithms"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Properties_Of_Logarithms"
  - "topics/algebra/Exponential_Equations"
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Logarithms"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Properties_Of_Logarithms"
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/The_Quadratic_Formula"
problem_type_ids: []
figures: []
summary: "To solve an equation with logs, collapse the log terms, convert to exponential form, and always reject solutions that make any argument nonpositive."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Logarithmic Equations

# Logarithmic Equations

A **logarithmic equation** is any equation whose unknown lives inside (or alongside) one or more logarithms. The job is to unearth the unknown. Because a logarithm is just an exponent, the main trick is to rewrite the statement as an exponential equation — that single rewrite is what "solves" most log problems, and everything else is preparation for it.

$$
\log_{b}(M) = c \quad\Longleftrightarrow\quad M = b^{c}.
$$

Read this rewrite rule as the action of unlocking the log. If you can get your equation into the left-hand form, you can immediately rewrite it as the right-hand form and continue with ordinary algebra. Getting there usually means shrinking several log terms into one, or isolating a lone log on one side of the equation.

## The master strategy

Here is the routine you will use on almost every problem in this topic.

1. **Clear out anything that is not a log.** Move constant terms and coefficients off to one side so the log expressions stand alone or are easier to combine.
2. **Collapse multiple logs into a single log.** Use the product rule $\log(A) + \log(B) = \log(AB)$, the quotient rule $\log(A) - \log(B) = \log(A/B)$, and the power rule $p \cdot \log(A) = \log(A^p)$ from [[Properties_Of_Logarithms]]. After this step you should have one log on each side of the equation, or one log equal to a number.
3. **Unlock the log.** Swap to exponential form. If both sides are the same base log, say $\log_{b}(M) = \log_{b}(N)$, then one-to-one behavior lets you conclude $M = N$ directly.
4. **Solve the leftover equation.** It is usually linear or quadratic.
5. **Verify every candidate.** Plug each candidate back into the *original* equation, and toss out any that force an argument of a log to be zero or negative.

That last step is not optional. It is the single most important habit on this page, so it gets its own section.

## Why you must verify: the extraneous-solution trap

Logarithms have one unbreakable rule — their argument must be strictly positive. When you apply the product rule or take both sides as "the argument of the same log", you sometimes invent a relationship that is perfectly legal for a polynomial but silently illegal for the original log equation. The algebra hands you a number; the number turns out to violate the domain restriction; the number is not actually a solution.

This is what we mean by an **extraneous solution**: a candidate that survives every algebra step but fails when plugged back into the original equation because it sends a log into forbidden territory. Verifying catches these impostors. You will see this play out in Example 3.

---

## Key ideas

- **The rewrite rule is the engine.** Once the equation looks like $\log_{b}(M) = c$ or $\log_{b}(M) = \log_{b}(N)$, you are one line from a plain algebra problem.
- **Combine logs before you convert.** Two or three separate log terms on one side cannot be unlocked directly. Use the product, quotient, and power rules to squeeze them into a single log first.
- **Logs on both sides with the same base mean the insides are equal.** If the base matches, you may drop the log wrappers and set arguments equal — no exponential rewrite needed.
- **Every candidate must be tested in the original equation.** Not in an intermediate line, not in a simplified version — the original. An extraneous root is the silent way to lose points.
- **Watch for equations that look quadratic in $\log(x)$.** An expression like $(\ln x)^2 - 3\ln x + 2 = 0$ is just a quadratic in disguise, solvable by letting $u = \ln x$.

---

## Example 1: An isolated log equal to a number

> Solve $\log_{3}(2x - 1) = 4$.

There is only one log on one side, and a plain number on the other, so we can convert to exponential form right away. Using the rewrite rule $\log_{b}(M) = c \iff M = b^c$ with $b = 3$, $M = 2x - 1$, and $c = 4$:

$$
2x - 1 = 3^4.
$$

Compute the right side: $3^4 = 81$. Now isolate $x$:

$$
2x - 1 = 81 \quad\Longrightarrow\quad 2x = 82 \quad\Longrightarrow\quad x = 41.
$$

Before celebrating, verify the candidate in the original equation. Plug $x = 41$ in: the argument becomes $2(41) - 1 = 81$, which is positive — good, the log is defined. And $\log_{3}(81) = 4$ because $3^4 = 81$. The candidate checks out.

**Solution:** $x = 41$.

---

## Example 2: Combining logs, then converting

> Solve $\log_{6}(x + 4) + \log_{6}(3 - x) = 1$.

Two separate log terms on the left, one number on the right. Before we can unlock anything, we have to collapse the left-hand side. The product rule turns a sum of logs (same base) into a log of a product:

$$
\log_{6}\!\left[(x + 4)(3 - x)\right] = 1.
$$

Now the left side is a single log and we can use the rewrite rule. With base $6$, argument $(x + 4)(3 - x)$, and exponent $1$:

$$
(x + 4)(3 - x) = 6^1 = 6.
$$

Expand the left side: $3x - x^2 + 12 - 4x = -x^2 - x + 12$. Set that equal to $6$ and move everything to one side:

$$
-x^2 - x + 12 = 6 \quad\Longrightarrow\quad -x^2 - x + 6 = 0 \quad\Longrightarrow\quad x^2 + x - 6 = 0.
$$

Factor: $(x + 3)(x - 2) = 0$, giving candidates $x = -3$ and $x = 2$.

Check each candidate in the original equation. For $x = -3$: the first argument is $-3 + 4 = 1 > 0$, and the second is $3 - (-3) = 6 > 0$. Both arguments are positive, so $x = -3$ is legal. For $x = 2$: the first argument is $2 + 4 = 6 > 0$, and the second is $3 - 2 = 1 > 0$. Also legal. Both candidates survive.

**Solution:** $x = -3$ or $x = 2$.

---

## Example 3: The extraneous-solution trap

> Solve $\log_{2}(x) + \log_{2}(x - 6) = 4$.

Two log terms on the left with the same base — the product rule applies:

$$
\log_{2}\!\left[x(x - 6)\right] = 4.
$$

Unlock the log by converting to exponential form with base $2$:

$$
x(x - 6) = 2^4 = 16.
$$

Expand and rearrange into standard quadratic form:

$$
x^2 - 6x = 16 \quad\Longrightarrow\quad x^2 - 6x - 16 = 0.
$$

Factor: $(x - 8)(x + 2) = 0$, giving the candidates $x = 8$ and $x = -2$. The algebra is tidy, and it is tempting to report both numbers as the answer. This is where the trap springs.

**Verify $x = 8$.** Arguments in the original equation: $\log_{2}(8)$ asks for a positive input, and $8 > 0$ is fine. The second log, $\log_{2}(8 - 6) = \log_{2}(2)$, also has a positive argument. Both are legal, and the equation becomes $\log_{2}(8) + \log_{2}(2) = 3 + 1 = 4$, which matches. So $x = 8$ is genuine.

**Verify $x = -2$.** Arguments in the original equation: $\log_{2}(-2)$. This is immediately undefined — we are not allowed to take the log of a negative number. There is no point checking the second log; this candidate is out. The reason it appeared at all is that the product rule step let us multiply two negative numbers (from the two arguments) together to get a positive number, which then *looked* legal inside a single log. The original problem never had that freedom, so the candidate was manufactured by our own algebra.

**Solution:** $x = 8$ only. The number $x = -2$ is an extraneous root introduced by combining the logs — exactly the kind of impostor the verification step is designed to catch.

---

## Common pitfalls

- **Skipping the verification step.** Every logarithmic equation can produce an extraneous solution the moment you combine log terms. If you do not plug candidates back into the original, you will eventually report a wrong answer.
- **Dropping the base when combining logs of different bases.** The product, quotient, and power rules only work when the bases match. If an equation mixes $\log_{2}$ with $\log_{4}$, first use change of base to rewrite one in terms of the other, then combine.
- **Forgetting that constants can ride into a log via the power rule.** A term like $2 \log x$ can become $\log(x^2)$, which is often what you need to collapse everything to a single log. Skipping this move is why some equations feel "stuck".
- **Treating $\log_{b}(M) = \log_{b}(N)$ as needing the exponential rewrite.** It does not. Because the log function is one-to-one, equal logs (same base) force equal arguments: $M = N$. Save the exponential rewrite for when one side is a plain number.

---

## Prerequisites

Before practicing, make sure these are comfortable:

- [[Logarithms]] — the definition of $\log_{b}(x)$ and the "if and only if" rewrite rule
- [[Logarithmic_Functions]] — the domain restriction is *why* extraneous solutions exist
- [[Properties_Of_Logarithms]] — product, quotient, and power rules for collapsing logs
- [[Exponential_Functions]] — the exponential side of every log equation
- [[The_Quadratic_Formula]] — many solved equations reduce to a quadratic you still have to factor or solve

---

## Problems Involving Logarithmic Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="logarithmic_equations"></div>

---

## See Also

- [[Logarithms]]
- [[Logarithmic_Functions]]
- [[Properties_Of_Logarithms]]
- [[Exponential_Equations]]
- [[Exponential_Functions]]
- [[Inverse_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
