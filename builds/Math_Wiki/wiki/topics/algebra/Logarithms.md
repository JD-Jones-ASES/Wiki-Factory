---
title: "Logarithms"
type: topic
aliases: ["Logarithm", "Log", "Common Logarithm", "Natural Logarithm"]
tags: ["#branch-algebra-2", "#topic-logarithms", "#topic-functions", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "7", section: "7.3"}
related:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Exponential_Equations"
  - "topics/algebra/Logarithmic_Functions"
  - "topics/algebra/Logarithmic_Equations"
  - "topics/algebra/Properties_Of_Logarithms"
  - "topics/algebra/Inverse_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Exponential_Functions"
  - "topics/algebra/Inverse_Functions"
  - "topics/algebra/Function_Basics"
problem_type_ids: []
figures: []
summary: "The logarithm log_b(x) is the exponent you must put on b to get x; it is the inverse operation of raising b to a power."
---
> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Logarithms

# Logarithms

Exponents answer the question "if I start with a base and raise it to a power, what do I get?" Logarithms answer the opposite question: "I already have the number — what power should I have used?" If you know that $2^3 = 8$, then asking for the logarithm base $2$ of $8$ is simply asking how many factors of $2$ got multiplied together to land on $8$. The answer is $3$, and we write it as $\log_{2}(8) = 3$.

That is the entire idea. A logarithm is just an exponent with a different job title. It is the exponent you *would have needed* on a given base to produce a given result. Every logarithm statement is secretly an exponential statement wearing different clothes, and learning to swap between the two forms is the single most important skill on this page.

## The definition (the "if and only if" rule)

Here is the formal rule that ties the two worlds together. For a base $b$ with $b > 0$ and $b \neq 1$, and for any positive number $x$:

$$
\log_{b}(x) = y \quad \text{if and only if} \quad b^y = x.
$$

Read $\log_{b}(x)$ out loud as "log base $b$ of $x$". The little $b$ riding under the word "log" is the base. Whatever sits inside the parentheses is called the **argument** of the logarithm. The output of the logarithm is always the exponent the base would need.

The phrase "if and only if" matters. It says the two statements are equivalent — not similar, not related, *equivalent*. Every logarithm equation has an exponential twin that says the same thing, and every exponential equation has a logarithm twin. Building fluency means reading either form and instantly producing the other.

Why the restrictions on $b$? Base $1$ is useless because $1$ raised to any power is still $1$; you could never get anywhere except back to $1$. Bases that are zero or negative break the rules of exponents in messy ways. And the argument $x$ must be positive because a positive base raised to any real exponent always produces a positive number — you simply cannot land on zero or a negative by raising a positive base to a real power.

---

## Key ideas

- **A logarithm is an exponent.** When you compute $\log_{b}(x)$, you are reporting the power you would put on $b$ to produce $x$. That single sentence unlocks every problem.
- **Two special bases get their own shorthand.** The **common logarithm** uses base $10$ and is written $\log(x)$ with no base printed. The **natural logarithm** uses $e \approx 2.71828$ and is written $\ln(x)$. If you see $\log(x)$ bare, assume base $10$; if you see $\ln(x)$, assume base $e$.
- **Logs and exponentials cancel.** Because they undo each other, $\log_{b}(b^x) = x$ and $b^{\log_{b}(x)} = x$. Either chaining collapses straight back to the input.
- **The anchor values.** For every legal base, $\log_{b}(1) = 0$ (because any base to the zero power is $1$) and $\log_{b}(b) = 1$ (because any base to the first power is itself). Memorize these — they catch most beginner mistakes.
- **Change-of-base formula.** Most calculators only have $\log$ and $\ln$ buttons. To compute $\log_{b}(x)$ for any other base, rewrite it as $\dfrac{\ln(x)}{\ln(b)}$ or $\dfrac{\log(x)}{\log(b)}$. Both quotients produce the same answer.

---

## Example 1: Swapping between logarithmic and exponential form

> Rewrite each statement in the other form: (a) $\log_{4}(64) = 3$, (b) $5^{-2} = \tfrac{1}{25}$, (c) $\ln(1) = 0$.

Each swap uses the same recipe. The base stays the same, the exponent and the result trade places, and one form is built from the word "log" while the other is built from a power.

**(a)** The logarithmic statement $\log_{4}(64) = 3$ says "the exponent that turns $4$ into $64$ is $3$." In exponential form that becomes $4^3 = 64$.

**(b)** The exponential statement $5^{-2} = \tfrac{1}{25}$ says "a base of $5$ with exponent $-2$ produces $\tfrac{1}{25}$." In logarithmic form that becomes $\log_{5}\!\left(\tfrac{1}{25}\right) = -2$. Negative logs happen exactly when the argument is a fraction less than one — nothing unusual going on.

**(c)** The natural log statement $\ln(1) = 0$ uses base $e$ implicitly. Writing the exponent on the base gives $e^0 = 1$, which is the "log of $1$ is zero" rule we just mentioned.

---

## Example 2: Computing a common or natural logarithm by hand

> What is the value of $\log(10{,}000)$, and what is the value of $\ln(e^7)$?

**First question.** The common logarithm uses base $10$, so we want the exponent $y$ with $10^y = 10{,}000$. Rewrite $10{,}000$ as a power of $10$: it is $10 \cdot 10 \cdot 10 \cdot 10 = 10^4$. Therefore

$$
\log(10{,}000) = 4.
$$

**Second question.** The natural logarithm uses base $e$, so we want the exponent $y$ with $e^y = e^7$. That is immediate — the exponent is $7$. Therefore

$$
\ln(e^7) = 7.
$$

This kind of recognition is faster than any calculator. Whenever the argument is already an obvious power of the base, the logarithm just hands you back the exponent.

---

## Example 3: Using change of base

> Find the value of $\log_{6}(200)$ to four decimal places.

Most calculators do not have a button for base $6$ logarithms, so we reach for the change-of-base formula:

$$
\log_{b}(x) = \dfrac{\ln(x)}{\ln(b)}.
$$

Plug in $b = 6$ and $x = 200$:

$$
\log_{6}(200) = \dfrac{\ln(200)}{\ln(6)} \approx \dfrac{5.2983}{1.7918} \approx 2.9569.
$$

A quick sanity check: $6^2 = 36$ and $6^3 = 216$, so the answer should sit between $2$ and $3$, and much closer to $3$. Our number $2.9569$ fits that picture. Using $\log$ instead of $\ln$ produces the same final value — the top and bottom of the quotient both shift to base $10$, so the ratio is unchanged.

---

## Common pitfalls

- **Treating $\log_{b}(x)$ as a number times $x$.** The symbol $\log$ is a function name, not a variable or a multiplier. $\log_{2}(x)$ means "the log base two function applied to $x$", not "log times two times $x$".
- **Forgetting the base.** If a problem writes $\log$ with no subscript it means base $10$; if it writes $\ln$ it means base $e$. Those are not optional — they change the numeric answer.
- **Taking a logarithm of zero or a negative number.** It is undefined. If an expression or equation produces $\log_{b}(0)$ or $\log_{b}(-3)$, something went wrong or the input must be rejected.
- **Assuming $\log(a + b) = \log(a) + \log(b)$.** This is false. The product rule says $\log(ab) = \log(a) + \log(b)$ — it is multiplication that splits into addition, not addition that splits into itself. See [[Properties_Of_Logarithms]].

---

## Prerequisites

Make sure these feel solid before you practice:

- [[Exponential_Functions]] — logs only make sense as inverses of exponentials; the base $b$ is the same beast in both worlds
- [[Inverse_Functions]] — the "if and only if" definition is exactly the inverse relationship from that page
- [[Function_Basics]] — function notation, domain, range, and the idea that one input gives one output

---

## Problems Involving Logarithms

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="logarithms"></div>

---

## See Also

- [[Logarithmic_Functions]]
- [[Logarithmic_Equations]]
- [[Properties_Of_Logarithms]]
- [[Exponential_Functions]]
- [[Exponential_Equations]]
- [[Inverse_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
