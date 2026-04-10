---
title: "Properties of Logarithms"
type: topic
aliases: ["Log Properties", "Log Rules", "Logarithm Identities"]
tags: ["#branch-pre-calculus", "#topic-logarithms", "#topic-functions", "#key-topic", "#key-formula"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algtrig", chapter: "6", section: "6.5"}
related:
  - "topics/algebra/Logarithms"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Logarithmic_Equations"
  - "topics/algebra/Exponential_Equations"
  - "topics/precalculus/Introduction_To_Exponentials_And_Logarithms"
  - "topics/precalculus/Applications_Of_Exponentials_And_Logarithms"
status: draft
confidence: high
branch: pre-calculus
prerequisites:
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Logarithms"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: []
summary: "Three identities turn log arithmetic into exponent arithmetic, and a change-of-base formula lets any calculator compute any log."
---

> [[_overview|Home]] > [[Precalculus_Overview|Pre-Calculus]] > Properties of Logarithms

# Properties of Logarithms

A logarithm is just an exponent wearing different clothes, so anything you know about exponents has a translation into a statement about logs. That single idea gives rise to three identities that, taken together, turn logarithmic expressions into something you can actually manipulate with algebra.

$$
\log_b(xy) = \log_b(x) + \log_b(y)
$$

$$
\log_b\!\left(\tfrac{x}{y}\right) = \log_b(x) - \log_b(y)
$$

$$
\log_b(x^n) = n \cdot \log_b(x)
$$

Before calculators existed, these three rules are what made logarithms worth the trouble: they turned hard multiplications into easy additions, and hard powers into easy multiplications. Today they are indispensable for solving any equation where the unknown lives in an exponent, and they set up half of what calculus will do to exponentials and logs later on.

Throughout this page, $b > 0$ and $b \ne 1$, and every input to a log is assumed positive.

---

## Key ideas

**Each log rule is the shadow of an exponent rule.** The three identities are not new facts — they are exactly what the familiar exponent rules look like on the other side of the mirror. The product rule for logs corresponds to $b^{u+w} = b^u \cdot b^w$, the quotient rule corresponds to $b^{u-w} = b^u / b^w$, and the power rule corresponds to $(b^u)^n = b^{un}$. Once you see each pair side by side, the log rules stop being a list to memorize and start feeling inevitable.

**A log of a product is a sum of logs.** Suppose $x = b^u$ and $y = b^w$. Then $xy = b^u \cdot b^w = b^{u+w}$, which means $\log_b(xy) = u + w$. But $u = \log_b(x)$ and $w = \log_b(y)$, so substituting back gives

$$
\log_b(xy) = \log_b(x) + \log_b(y).
$$

That is a full derivation — the proof is nothing more than tracking names. Multiplication of inputs turns into addition of outputs.

**A log of a quotient is a difference of logs.** Using the same substitution, $x/y = b^u / b^w = b^{u-w}$, so $\log_b(x/y) = u - w = \log_b(x) - \log_b(y)$. Division of inputs turns into subtraction.

**A log of a power pulls the exponent out in front.** Write $x = b^u$ again. Then $x^n = (b^u)^n = b^{un}$, and so $\log_b(x^n) = un = n \cdot \log_b(x)$. Any exponent hiding inside a log can be yanked out and hung in front as a multiplier. This is the identity that makes logs such a powerful tool for isolating unknowns trapped in exponents.

**These identities go both directions.** You can use them to **expand** a single log into a sum of simpler logs, or to **contract** a sum of logs back into a single log. Both moves are useful, and fluency with each is the main skill of this section.

**Watch what the rules do NOT say.** There is no rule for $\log_b(x + y)$ — the log of a sum does not simplify the way the log of a product does. Likewise, $\log_b(x) \cdot \log_b(y)$ does not collapse, and $\log_b(x) / \log_b(y)$ does not equal $\log_b(x/y)$. These are the three tempting-but-false moves that trip up every student.

---

## Change of base

Your calculator almost certainly has two log buttons: $\log$ (base $10$) and $\ln$ (base $e$). It almost certainly does not have a button for base $5$ or base $7$. The **change-of-base formula** fixes that.

$$
\log_b(x) = \frac{\log_a(x)}{\log_a(b)}
$$

for any legal base $a$. In practice, you pick $a = 10$ or $a = e$ because those are the bases your calculator knows:

$$
\log_b(x) = \frac{\log(x)}{\log(b)} = \frac{\ln(x)}{\ln(b)}.
$$

### Where the formula comes from

Let $y = \log_b(x)$. By the definition of a log, that is equivalent to $b^y = x$. Take $\log_a$ of both sides:

$$
\log_a(b^y) = \log_a(x).
$$

The power rule (which you just proved) pulls the $y$ out front on the left: $y \cdot \log_a(b) = \log_a(x)$. Dividing both sides by $\log_a(b)$ gives exactly the change-of-base formula. Like the three main identities, the proof is just "translate to exponential form, apply an exponent rule, translate back."

---

## Example 1: expanding a single log

> Expand $\log_2\!\left(\dfrac{8 x^3}{y}\right)$ as a sum and difference of simpler logs. Assume all quantities are positive.

Attack the fraction first with the quotient rule:

$$
\log_2\!\left(\frac{8 x^3}{y}\right) = \log_2(8 x^3) - \log_2(y).
$$

The first term is a product, so apply the product rule:

$$
= \log_2(8) + \log_2(x^3) - \log_2(y).
$$

Now peel the exponent off the middle term with the power rule:

$$
= \log_2(8) + 3 \log_2(x) - \log_2(y).
$$

Finally, notice that $\log_2(8)$ is a recognizable number — $2^3 = 8$, so $\log_2(8) = 3$. That gives a fully simplified answer:

$$
= 3 + 3 \log_2(x) - \log_2(y).
$$

The order of operations is always the same: strip off the outer quotient first, then the products, then the powers. Evaluate any logs of numerical powers of the base at the end.

---

## Example 2: contracting a sum of logs

> Write $2 \ln(x) + \ln(x + 1) - \tfrac{1}{2}\ln(y)$ as a single logarithm.

This is the expansion process run in reverse. Start by using the power rule to tuck each coefficient back inside its log as an exponent:

$$
2 \ln(x) + \ln(x + 1) - \tfrac{1}{2}\ln(y) = \ln(x^2) + \ln(x + 1) - \ln(y^{1/2}).
$$

Now the first two terms are a sum of logs, which the product rule combines into a log of a product:

$$
= \ln(x^2 (x + 1)) - \ln(y^{1/2}).
$$

A difference of logs is a log of a quotient:

$$
= \ln\!\left(\frac{x^2(x + 1)}{\sqrt{y}}\right).
$$

Replacing $y^{1/2}$ with $\sqrt{y}$ in the final answer is a matter of taste, but the root form is usually cleaner to read. Contracting an expression to a single log is the move you make whenever you want to apply the one-to-one property "$\log_b(A) = \log_b(B)$ implies $A = B$" in an equation.

---

## Example 3: change of base in action

> Use a calculator to estimate $\log_5(200)$, rounded to four decimal places.

Your calculator has no "log base 5" key, so rewrite using the common-log version of the change-of-base formula:

$$
\log_5(200) = \frac{\log(200)}{\log(5)}.
$$

Punching these into a calculator: $\log(200) \approx 2.30103$ and $\log(5) \approx 0.69897$. Dividing,

$$
\log_5(200) \approx \frac{2.30103}{0.69897} \approx 3.2920.
$$

A quick sanity check: $5^3 = 125$ and $5^{3.5} \approx 279$, so the answer must land between $3$ and $3.5$. Our estimate of $3.2920$ fits comfortably inside that window. The natural-log version would give the same number: $\ln(200)/\ln(5) \approx 5.2983 / 1.6094 \approx 3.2920$.

---

## Common pitfalls

- **The log of a sum is not the sum of logs.** $\log_b(x + y)$ is its own beast and cannot be broken apart. The rule only works for products and quotients.
- **The power rule needs the exponent to be on the argument, not on the whole log.** $\log_b(x^n) = n \log_b(x)$, but $(\log_b(x))^n$ does not simplify.
- **Coefficients out front belong inside as exponents.** When contracting, a term like $3 \log_b(x)$ becomes $\log_b(x^3)$, not $\log_b(3x)$. The coefficient becomes a power, not a factor of the input.
- **Hidden domain restrictions can create extraneous solutions.** When you contract or expand logs in the middle of solving an equation, the resulting expression may have a different domain than the original. Always check final answers against the original equation.
- **The change-of-base formula is a division, not a subtraction.** $\log_b(x) = \log(x) / \log(b)$, not $\log(x) - \log(b)$.

---

## Prerequisites

Before working through practice problems, you should be solid on:

- [[Properties_Of_Exponents]] — the three log rules are just exponent rules in disguise
- [[Logarithms]] — the definition $\log_b(x) = y \iff b^y = x$ and basic evaluation
- [[Function_Basics]] — so domain restrictions on logs feel natural

---

## Problems Involving Properties of Logarithms

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="properties_of_logarithms"></div>

---

## See Also

- [[Introduction_To_Exponentials_And_Logarithms]]
- [[Applications_Of_Exponentials_And_Logarithms]]
- [[Logarithms]]
- [[Logarithmic_Equations]]
- [[Exponential_Equations]]
- [[Precalculus_Overview|Pre-Calculus]]
- [[Topics_Overview]]
- [[_overview|Home]]
