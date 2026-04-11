---
title: "Exponential Equations"
type: topic
aliases: ["ExpEquations", "Solving Exponential Equations"]
tags: ["#branch-algebra-2", "#topic-exponents-and-radicals", "#topic-logarithms", "#key-technique"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.4"}
  - {book: "algtrig", chapter: "6", section: "6.1"}
related:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Logarithms"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Logarithmic_Equations"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Properties_Of_Logarithms"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Logarithms"
problem_type_ids: []
figures: []
summary: "Two techniques for solving equations with the variable in the exponent: rewrite with a common base, or apply a logarithm."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Exponential Equations

# Exponential Equations

An **exponential equation** is an equation in which the unknown is stuck up in the exponent rather than sitting on the baseline. Instead of $x^2 = 16$ — where you extract the variable by taking a square root — you face something like $2^x = 16$ or $5^x = 80$, and you have to find an approach that reaches into the exponent itself. There are two standard techniques, and the decision tree for picking between them is short: if both sides can be written with the same base, use the first method; otherwise, use the second.

$$
\text{Method 1: common base} \qquad \text{Method 2: apply a logarithm}
$$

Every exponential equation you will meet in a high-school algebra class surrenders to one of these two moves (sometimes to a clean combination of both).

---

## Method 1: the common-base approach

The [[Exponential_Functions|exponential function]] $f(x) = b^x$ (with $b > 0$ and $b \neq 1$) is one-to-one, which means different inputs always give different outputs. Flipping that statement around gives a very useful rule:

$$
b^{\,f(x)} = b^{\,g(x)} \quad \Longrightarrow \quad f(x) = g(x).
$$

In words: if two powers with the **same** base are equal, then the exponents have to be equal. That single fact turns the exponential problem into an ordinary equation about the exponents, which you already know how to solve.

The strategy, then, is to rewrite both sides of the original equation as powers of the same base — usually the smallest prime that both numbers share. Once both sides wear the same base, you can erase the base and set the exponents equal to each other. The trick is recognizing the hidden powers: $4 = 2^2$, $8 = 2^3$, $16 = 2^4$, $27 = 3^3$, $125 = 5^3$, and so on. Fluency with [[Properties_Of_Exponents]] is what turns this move from a guessing game into a recipe.

---

## Method 2: the logarithm approach

Sometimes no common base is available — for example, $3^x = 17$. There is no clean way to write $17$ as a power of $3$, so the first technique has nowhere to go. The fix is to reach for a tool that can pull a variable out of an exponent: the logarithm.

The key idea is that a logarithm is the inverse of an exponential function (see [[Logarithms]] and [[Inverse_Functions]]), so logging both sides of an equation is a legal operation — it preserves equality and drops the exponent into a place you can get at. Using the **Power Rule** $\ln(b^x) = x \ln b$, the equation $b^x = c$ becomes $x \ln b = \ln c$, which is linear in $x$:

$$
b^x = c \quad \Longrightarrow \quad x = \dfrac{\ln c}{\ln b}.
$$

You may use the natural log $\ln$ or the common log $\log_{10}$ — the final numerical answer is the same. The steps are always: isolate the exponential, apply a logarithm to each side, bring the exponent out front with the Power Rule, and solve what is left. When the unknown only shows up once, what is left is a single linear equation.

---

## Example 1: two same-base problems

> Find all real solutions to each equation.
>
> (a) $2^{3x} = 2^{x+4}$
> (b) $9^x = 27$

For (a), both sides are already powers of $2$. Because $b^{f(x)} = b^{g(x)}$ forces the exponents to match, erase the base and write

$$
3x = x + 4.
$$

That is a short linear equation. Subtract $x$ from both sides: $2x = 4$, so $x = 2$. The exponents match when $x = 2$, and a quick substitution into the original equation confirms that $2^{6} = 2^{6}$.

For (b), neither side is a power of the other at first glance — but both $9$ and $27$ are powers of $3$. Use $9 = 3^2$ and $27 = 3^3$ to rewrite the equation as

$$
(3^2)^x = 3^3 \quad \Longrightarrow \quad 3^{2x} = 3^3.
$$

The bases are equal, so the exponents must be equal: $2x = 3$, giving $x = \tfrac{3}{2}$.

A common slip here is trying to set $9 = 27$, or writing $9^x = 27$ as $(9/27)^x$ or some other invented manipulation. The legal move is always **rewrite with a common base first**, then remove the base, then solve.

---

## Example 2: a same-base problem with two rewrites

> Determine $x$ such that $4^{x-1} = 8^{x+2}$.

Neither side is a power of the other, but both $4$ and $8$ are powers of $2$. Rewrite each side using the smallest shared base:

$$
(2^2)^{x-1} = (2^3)^{x+2}.
$$

Now apply the power-of-a-power rule from [[Properties_Of_Exponents]] to collapse the nested exponents. Multiply the outer and inner exponents on each side:

$$
2^{\,2(x-1)} = 2^{\,3(x+2)} \quad \Longrightarrow \quad 2^{\,2x-2} = 2^{\,3x+6}.
$$

Same base, so erase it and set the exponents equal:

$$
2x - 2 = 3x + 6.
$$

Subtract $2x$ from both sides and subtract $6$: $-8 = x$. So $x = -8$. Negative solutions are normal for exponential equations — nothing breaks.

---

## Example 3: no common base, so logarithms

> What value of $x$ makes $5^x = 80$ true? Round to four decimal places.

There is no neat way to write $80$ as a power of $5$ (the surrounding values are $5^2 = 25$ and $5^3 = 125$, so the answer is somewhere between $2$ and $3$, but not clean). Common base is a dead end. Apply a logarithm to each side — natural log is as good as any:

$$
\ln(5^x) = \ln 80.
$$

Now use the Power Rule to bring the $x$ out of the exponent and onto the outside:

$$
x \ln 5 = \ln 80.
$$

Divide both sides by $\ln 5$:

$$
x = \dfrac{\ln 80}{\ln 5}.
$$

That is the exact answer. For a decimal, punch it into a calculator: $\ln 80 \approx 4.3820$ and $\ln 5 \approx 1.6094$, so

$$
x \approx \dfrac{4.3820}{1.6094} \approx 2.7228.
$$

A sanity check: $5^{2.7228}$ should be near $80$ — and it is. The solution sits between $2$ and $3$, exactly where the powers of $5$ tell you it should.

---

## Example 4: isolate the exponential first, then log

> What is $x$ if $3 e^{2x} - 1 = 74$?

The exponential $e^{2x}$ is tangled up with a multiplier and a constant, so before any logarithm can help you, get the exponential alone on one side. Add $1$ to both sides, then divide by $3$:

$$
3 e^{2x} = 75 \quad \Longrightarrow \quad e^{2x} = 25.
$$

Now the exponential is isolated. Apply the natural log to both sides — the natural log is a perfect partner for $e$, because $\ln(e^{\text{anything}}) = $ that anything:

$$
\ln(e^{2x}) = \ln 25 \quad \Longrightarrow \quad 2x = \ln 25.
$$

Divide by $2$ to finish:

$$
x = \dfrac{\ln 25}{2} \approx \dfrac{3.2189}{2} \approx 1.6094.
$$

(You can also simplify $\ln 25 = 2 \ln 5$ and cancel the $2$, giving the clean exact answer $x = \ln 5$.)

The takeaway is the order of operations in reverse: first unwind whatever is outside the exponential, and only then bring in a log.

---

## A worked application: doubling time

> An investment grows according to $A(t) = 1000 \cdot 2^{t/5}$ dollars after $t$ years. After how many years does the investment reach $\$7{,}000$?

Set the model equal to the target balance and solve for $t$:

$$
1000 \cdot 2^{t/5} = 7000.
$$

Isolate the exponential by dividing both sides by $1000$:

$$
2^{t/5} = 7.
$$

There is no clean power of $2$ that equals $7$, so reach for a logarithm. Applying $\ln$ to each side and then using the Power Rule:

$$
\dfrac{t}{5} \ln 2 = \ln 7 \quad \Longrightarrow \quad t = \dfrac{5 \ln 7}{\ln 2}.
$$

Running the numbers: $\ln 7 \approx 1.9459$ and $\ln 2 \approx 0.6931$, so

$$
t \approx \dfrac{5 \cdot 1.9459}{0.6931} \approx 14.04 \text{ years}.
$$

Interpreted in context, the account reaches $\$7{,}000$ a little over fourteen years after it begins. Notice how modeling problems like this always end with **number plus unit** — a raw $14.04$ is not the answer; $14.04$ **years** is.

---

## Common pitfalls

- **Writing "$\log$ both sides" but forgetting the Power Rule.** Applying a log is only useful if you follow it up by pulling the exponent out front. Stopping at $\log(5^x) = \log 80$ is not solving anything.
- **Trying the same-base method when no shared base exists.** If neither side is a power of the other, stop forcing it — switch to logarithms. Common base works for equations like $3^x = 81$; it does not work for $3^x = 50$.
- **Dropping the base but keeping the constants.** In $2^{3x} = 2^{x+4}$, only the exponents survive the removal of the base. You do not keep an extra $2$ somewhere. The equation becomes $3x = x + 4$, nothing more.
- **Rounding partway through.** If an exact answer like $\dfrac{\ln 80}{\ln 5}$ is asked for, leave it in that form. If a decimal is asked for, compute the logs at full precision before dividing — rounding each piece first introduces error that shows up in the last digit.
- **Losing a solution in a "disguised quadratic."** An equation like $e^{2x} - 5 e^x + 6 = 0$ can be turned into a quadratic in $u = e^x$; it will usually give two values of $u$, and therefore two answers for $x$ (unless one of the $u$-values is non-positive, which you then reject because $e^x$ is always positive).

---

## Which method should I use?

A short checklist when you face a new problem:

1. **Is the unknown alone on one side already?** If not, isolate the exponential expression first.
2. **Can both sides be written as powers of the same base?** If yes, do so and set the exponents equal. Done.
3. **If no common base is handy,** apply a logarithm to each side, use the Power Rule, and solve the resulting linear equation for the variable.

Common-base answers are usually clean rational numbers; logarithm answers are usually messy decimals (or exact ratios of logs). Either form is acceptable as long as you know which one the problem wants.

---

## Prerequisites

Before you work practice problems, make sure you are comfortable with:

- [[Exponential_Functions]] — the objects these equations are built on
- [[Properties_Of_Exponents]] — so rewrites like $9^x = (3^2)^x = 3^{2x}$ feel automatic
- [[Logarithms]] — the tool that drops a variable out of an exponent

---

## Problems Involving Exponential Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="exponential_equations"></div>

---

## See Also

- [[Exponential_Functions]]
- [[Logarithms]]
- [[Logarithmic_Equations]]
- [[Properties_Of_Logarithms]]
- [[Growth_Decay_And_Applications]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
