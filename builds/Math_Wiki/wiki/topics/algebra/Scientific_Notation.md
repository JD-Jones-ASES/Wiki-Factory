---
title: "Scientific Notation"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-exponents-and-radicals", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs:
  - {book: "algebra_1", chapter: "8", section: "8.4"}
related:
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Zero_And_Negative_Exponents"
  - "topics/pre_algebra/Exponents_And_Powers"
  - "topics/algebra/Polynomial_Basics"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Properties_Of_Exponents"
  - "topics/algebra/Zero_And_Negative_Exponents"
  - "topics/pre_algebra/Exponents_And_Powers"
problem_type_ids: []
figures: []
summary: "Write every number as one digit-plus-decimal between 1 and 10 times a power of 10, then arithmetic on huge and tiny quantities becomes routine exponent work."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Scientific Notation

# Scientific Notation

Astronomers measure distances in trillions of kilometers. Biologists measure cell sizes in millionths of a meter. Writing numbers that big or that small in full standard form is miserable — just counting the zeros is hard, and multiplying two of them together by hand is worse. **Scientific notation** fixes both problems by cracking every number into two clean pieces: a small decimal between $1$ and $10$ that carries the significant digits, and a power of $10$ that carries the size.

A value counts as scientific notation once you have rewritten it in the shape

$$
a \times 10^{n}
$$

The number $a$ has to satisfy $1 \le a < 10$, and $n$ has to be an integer (positive, negative, or zero). The factor $a$ goes by the name **coefficient** — some books say "mantissa" — and it always has the look of a single non-zero leading digit followed by a decimal part, such as $3.45$, $7.02$, or $1.000$. The exponent $n$ is a whole number — positive for numbers larger than $1$, negative for numbers smaller than $1$, and zero for numbers between $1$ and $10$. Once every number is in this form, the arithmetic of huge and tiny quantities collapses into exponent arithmetic, which is much kinder to your eyes and your pencil.

---

## Key ideas

### Why $1 \le a < 10$

The requirement that the coefficient $a$ falls in $[1, 10)$ — that is, at least $1$ and strictly less than $10$ — is what makes the scientific-notation form **unique**. Without that constraint, the same number could be written infinitely many different ways. For instance, the number $45{,}000$ could be written as

$$
45000 = 4.5 \times 10^{4} = 45 \times 10^{3} = 0.45 \times 10^{5}
$$

All three expressions equal $45{,}000$, but only the first one has a coefficient between $1$ and $10$. That is the only one counted as "in scientific notation." The other two are legal expressions, but not standard form.

The upshot: after any arithmetic you do in scientific notation, you should glance at your coefficient and make sure it is still in $[1, 10)$. If it drifted out — say, a multiplication gave you $42 \times 10^{3}$ — you need to **renormalize** by shifting the decimal point and adjusting the exponent to compensate. In that example, $42 \times 10^{3} = 4.2 \times 10^{1} \times 10^{3} = 4.2 \times 10^{4}$. The coefficient is now in range, and the exponent absorbed the change.

### Converting standard form → scientific notation

Take any number in standard form and move the decimal point until exactly one nonzero digit sits to the left of the decimal. Count how many places you moved, and the direction. That count (with the right sign) is your exponent.

- If the number is $\ge 10$, you move the decimal to the **left**, and the exponent is **positive** (equal to the number of places moved).
- If the number is between $0$ and $1$, you move the decimal to the **right**, and the exponent is **negative** (equal to minus the number of places moved).
- If the number is between $1$ and $10$, you do not move the decimal at all, and the exponent is $0$.

A useful way to remember the signs: a positive exponent means "make the number bigger" when you multiply by $10^{n}$, so you use a positive exponent when the original was already bigger than the coefficient. A negative exponent means "make the number smaller," so you use it when the original was tiny.

### Converting scientific notation → standard form

Reverse the process. Starting from $a \times 10^{n}$, move the decimal point in $a$ by $|n|$ places. Move it to the right if $n > 0$ (growing the number) and to the left if $n < 0$ (shrinking it). Fill in zeros as needed when the decimal runs out of digits.

### Arithmetic in scientific notation

Multiplication and division in scientific notation are a breeze because you can handle the coefficients and the exponents separately. For a product:

$$
(a \times 10^{m}) \cdot (b \times 10^{n}) = (ab) \times 10^{m + n}
$$

Multiply the coefficients, add the exponents. Then check whether the product $ab$ is still in $[1, 10)$ — if not, renormalize. For a quotient:

$$
\frac{a \times 10^{m}}{b \times 10^{n}} = \frac{a}{b} \times 10^{m - n}
$$

Divide the coefficients, subtract the exponents. Again, renormalize the result if the coefficient has drifted outside $[1, 10)$.

Addition and subtraction are trickier — you can only combine terms when the exponents match, which usually means rewriting one of the numbers to share the other's exponent before you add. That is a little beyond the scope of this introduction, and the three examples below focus on the conversion and multiplication cases.

---

## Example 1: Convert standard form to scientific notation

> Write $3{,}450{,}000$ in scientific notation.

Start by locating where the decimal point sits in $3{,}450{,}000$. A whole number has an implicit decimal point at the end, so the number is really $3{,}450{,}000.$ with the decimal on the far right.

Move the decimal to the left until only one nonzero digit is in front of it. Counting the places:

$$
3{,}\underbrace{4}_{1}\underbrace{5}_{2}\underbrace{0}_{3}\underbrace{0}_{4}\underbrace{0}_{5}\underbrace{0.}_{6}
$$

The decimal moves $6$ places to the left, stopping between the $3$ and the $4$. The coefficient is therefore $3.45$ (the trailing zeros drop away because they are not significant for the coefficient), and because the original number was larger than $10$, the exponent is positive $6$:

$$
3{,}450{,}000 = 3.45 \times 10^{6}
$$

Sanity check: $3.45 \times 10^{6} = 3.45 \times 1{,}000{,}000 = 3{,}450{,}000$. Matches the original, so the conversion is correct. Notice that the coefficient $3.45$ lives comfortably inside $[1, 10)$, which is exactly where a scientific-notation coefficient needs to be.

---

## Example 2: Convert scientific notation to standard form

> Write $5.8 \times 10^{-4}$ in standard form.

The exponent is negative, so the original number is smaller than $1$, and you will move the decimal to the **left**. Starting from $5.8$, move the decimal $4$ places to the left, filling in zeros for the spots you pass through that have no digit:

$$
5.8 \to 0.58 \to 0.058 \to 0.0058 \to 0.00058
$$

After four left-steps, the number reads $0.00058$. That is the standard form of $5.8 \times 10^{-4}$.

$$
5.8 \times 10^{-4} = 0.00058
$$

A common bookkeeping trick: after the conversion, count the zeros between the decimal point and the first nonzero digit. There should be three zeros here (the $0$ immediately after the decimal, then two more), and the first nonzero digit is $5$. That matches what the exponent $-4$ predicts: for a negative exponent $-n$, there are $n - 1$ zeros between the decimal point and the first nonzero digit. Here $n = 4$, so $n - 1 = 3$ zeros, and the count agrees.

---

## Example 3: Multiply in scientific notation

> Compute $(3 \times 10^{5})(4 \times 10^{2})$, giving the answer in scientific notation.

Handle the coefficients and the exponents separately. Multiply the coefficients: $3 \cdot 4 = 12$. Add the exponents: $5 + 2 = 7$. Combine:

$$
(3 \times 10^{5})(4 \times 10^{2}) = 12 \times 10^{7}
$$

Stop and check whether the coefficient $12$ is still in $[1, 10)$. It is **not** — $12$ is above $10$, so this is not in standard scientific-notation form yet. Renormalize by rewriting $12$ as $1.2 \times 10^{1}$:

$$
12 \times 10^{7} = (1.2 \times 10^{1}) \times 10^{7} = 1.2 \times 10^{8}
$$

The exponent absorbed the extra factor of $10$ from the coefficient, which is now safely inside $[1, 10)$. The final answer in proper scientific notation is

$$
(3 \times 10^{5})(4 \times 10^{2}) = 1.2 \times 10^{8}
$$

Quick sanity check in standard form: $3 \times 10^{5} = 300{,}000$, $4 \times 10^{2} = 400$, and $300{,}000 \cdot 400 = 120{,}000{,}000$. And $1.2 \times 10^{8} = 120{,}000{,}000$. Matches.

The renormalization step — looking back at the coefficient and adjusting if it drifted out of range — is the single thing that separates careful scientific-notation work from sloppy work. Build the habit now: every product or quotient ends with a range check.

---

## Common pitfalls

- **Leaving the coefficient outside $[1, 10)$.** After a multiplication, division, or any renormalization, always check that $1 \le a < 10$. A result like $12 \times 10^{7}$ is an intermediate answer, not a final one — it still needs renormalizing to $1.2 \times 10^{8}$. This is the number-one place students lose points on this topic.
- **Counting decimal places in the wrong direction.** Moving the decimal to the left corresponds to a positive exponent; moving it to the right corresponds to a negative one. It feels backwards at first. The mental check: a positive $10^{n}$ factor makes the number bigger, so it compensates for the fact that you made the coefficient smaller (by moving the decimal left), and the two effects have to cancel out.
- **Confusing the "count of decimal moves" with the "count of zeros."** In $3{,}450{,}000 = 3.45 \times 10^{6}$, the exponent $6$ is the number of decimal places moved, not the number of zeros in the original number. The original has only three trailing zeros, but the decimal moved six places because there were nonzero digits in between.
- **Forgetting that exponents add under multiplication (not multiply).** When you multiply $(3 \times 10^{5})(4 \times 10^{2})$, the exponents combine by **addition**: $5 + 2 = 7$, not $5 \cdot 2 = 10$. The multiplication rule for same-base exponents is $10^{m} \cdot 10^{n} = 10^{m+n}$, and the addition carries over into scientific notation.
- **Missing the coefficient of $1$ on a clean power of ten.** A number like $10^{6}$ is technically not in scientific notation until you write it as $1 \times 10^{6}$. The coefficient has to be shown, even when it is $1$.

---

## Prerequisites

Scientific notation is really just the exponent rules applied to base-$10$ numbers, so make sure these feel routine first:

- [[Properties_Of_Exponents]] — especially the product rule $10^m \cdot 10^n = 10^{m+n}$ and the quotient rule $10^m / 10^n = 10^{m-n}$
- [[Zero_And_Negative_Exponents]] — so that a negative exponent like $10^{-4}$ has a clear meaning
- [[Exponents_And_Powers]] — the pre-algebra groundwork for what $10^n$ even means

---

## Problems Involving Scientific Notation

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="scientific_notation"></div>

---

## See Also

- [[Properties_Of_Exponents]]
- [[Zero_And_Negative_Exponents]]
- [[Exponents_And_Powers]]
- [[Polynomial_Basics]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
