---
title: "Dividing Fractions"
type: topic
aliases: ["Fraction Division", "Divide Fractions"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "4", section: "4.3"}
related:
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Dividing_Decimals"
  - "topics/pre_algebra/Mixed_Numbers_And_Improper_Fractions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "Dividing fractions means multiplying by the reciprocal: keep, change, flip."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Dividing Fractions

# Dividing Fractions

Dividing a fraction by another fraction sounds like it should be harder than multiplying, but once you learn the single trick, it becomes the same calculation. The trick is to flip the second fraction upside down and multiply. That move is often taught with the memorable mnemonic **keep, change, flip** — and every student rediscovers, eventually, that this is not a new rule so much as a restatement of what division has always meant.

## What it means

Division asks the question, "how many of these fit inside that?" When you ask how many halves fit in three, the answer is $6$, because $3 \div \tfrac{1}{2} = 6$. There are two halves in every one, and three ones, so $3 \times 2 = 6$. Notice that answering the division question ended up looking like a multiplication by $2$, which is exactly the reciprocal of $\tfrac{1}{2}$.

That pattern holds for every division. Splitting a pizza into pieces of size $\tfrac{1}{4}$ gives four pieces per pizza, and two pizzas give $2 \cdot 4 = 8$ pieces. The operation $2 \div \tfrac{1}{4}$ is equivalent to the operation $2 \cdot 4$.

A **reciprocal** is what you get when you swap the numerator and denominator of a fraction. Some textbooks call this number the *multiplicative inverse* for a reason that will make sense in a minute. Swapping $\tfrac{3}{5}$ gives $\tfrac{5}{3}$. Swapping a whole number $n$ is the same as writing $\tfrac{1}{n}$, because $n$ is secretly $\tfrac{n}{1}$. Zero has no reciprocal — flipping $\tfrac{0}{1}$ would give $\tfrac{1}{0}$, which is undefined.

Why "multiplicative inverse"? Because a fraction times its reciprocal always equals $1$. For instance, $\tfrac{3}{5} \cdot \tfrac{5}{3} = \tfrac{15}{15} = 1$. Multiplying by a reciprocal is the fraction equivalent of undoing a multiplication.

## The rule

$$
\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}
$$

In words: to divide by a fraction, **multiply by its reciprocal**. The three steps of "keep, change, flip" make the process easy to remember: **keep** the first fraction as it is, **change** the division sign to a multiplication sign, and **flip** the second fraction to its reciprocal. From there, you are doing the same [[Multiplying_Fractions|multiplication]] you already know.

## Why it works

Imagine you ask, "what is $\tfrac{a}{b}$ divided by $\tfrac{c}{d}$?" That is the same as asking, "what number, when multiplied by $\tfrac{c}{d}$, gives $\tfrac{a}{b}$?" Call the answer $x$. Then $x \cdot \tfrac{c}{d} = \tfrac{a}{b}$. To solve for $x$, multiply both sides by $\tfrac{d}{c}$ (the reciprocal of $\tfrac{c}{d}$). On the left, $\tfrac{c}{d} \cdot \tfrac{d}{c} = 1$, so everything on the left collapses to $x$. On the right, $\tfrac{a}{b} \cdot \tfrac{d}{c}$ is what you are left holding. The answer is

$$
x = \frac{a}{b} \cdot \frac{d}{c}
$$

which is exactly the keep-change-flip rule.

A gentler version of the same story: dividing by $2$ is the same as multiplying by $\tfrac{1}{2}$. Dividing by $\tfrac{1}{2}$ is the same as multiplying by $2$. In both cases, dividing by something and multiplying by its reciprocal are two ways of asking the same question. Fraction division just applies the pattern to fractions that are not whole numbers.

## Worked examples

### Example 1: fraction divided by a fraction

Divide: $\dfrac{4}{9} \div \dfrac{5}{6}$.

Apply keep-change-flip. Keep the first fraction, change the sign to multiplication, and flip the second fraction:

$$
\frac{4}{9} \div \frac{5}{6} = \frac{4}{9} \cdot \frac{6}{5}
$$

Before multiplying, look for a cross-cancellation. The $6$ in the new numerator and the $9$ in the old denominator share a factor of $3$:

$$
\frac{4}{\cancelto{3}{9}} \cdot \frac{\cancelto{2}{6}}{5} = \frac{4 \cdot 2}{3 \cdot 5} = \frac{8}{15}
$$

**Answer:** $\dfrac{8}{15}$.

### Example 2: a whole number divided by a fraction

A baker has $2$ cups of flour. Each biscuit uses $\tfrac{1}{4}$ cup. How many biscuits can the baker make?

Set this up as a division: $2 \div \tfrac{1}{4}$. Rewrite the whole number as a fraction over $1$, then keep-change-flip:

$$
\frac{2}{1} \div \frac{1}{4} = \frac{2}{1} \cdot \frac{4}{1} = \frac{2 \cdot 4}{1 \cdot 1} = 8
$$

**Answer:** the baker can make $8$ biscuits.

This example is the clearest picture of why the rule works. "How many quarter cups fit in two cups?" There are $4$ quarter cups per whole cup, and $2$ whole cups, so $2 \cdot 4 = 8$ quarter cups total. Dividing by $\tfrac{1}{4}$ really is the same as multiplying by $4$.

### Example 3: a fraction divided by a whole number

Divide: $\dfrac{7}{12} \div 2$.

Notice which number gets flipped. You are dividing by $2$, so $2$ is the second number, and it is $2$ whose reciprocal you take. Rewrite $2$ as $\tfrac{2}{1}$, then keep-change-flip:

$$
\frac{7}{12} \div \frac{2}{1} = \frac{7}{12} \cdot \frac{1}{2} = \frac{7 \cdot 1}{12 \cdot 2} = \frac{7}{24}
$$

**Answer:** $\dfrac{7}{24}$. Cutting $\tfrac{7}{12}$ of something in half gives $\tfrac{7}{24}$ of that thing — half as much, as you would expect.

## Common mistakes

- **Flipping the wrong fraction.** Only the **second** fraction (the divisor) gets flipped. The first one stays put — that is why the mnemonic is keep, change, flip and not flip, change, flip.
- **Flipping both fractions.** That turns division into something entirely different. Do not touch the first fraction.
- **Forgetting to convert whole numbers.** When you divide $\tfrac{3}{4} \div 6$, you are dividing by $6$, whose reciprocal is $\tfrac{1}{6}$. Do not flip $\tfrac{3}{4}$.
- **Trying to use a common denominator.** A common denominator is for adding and subtracting. Dividing fractions does not need one at all.
- **Dividing by zero.** $\tfrac{a}{b} \div 0$ is undefined, because $0$ has no reciprocal.

## Prerequisites

You will get much more out of this page if you are already comfortable with:

- [[Multiplying_Fractions|Multiplying fractions]] — every fraction division becomes a multiplication after the flip, so that is the skill you are really practicing.
- [[Equivalent_Fractions_And_Simplifying|Equivalent fractions and simplifying]] — you will still need to reduce answers and cross-cancel to keep numbers manageable.

If those are rusty, go warm up and then come back.

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="dividing_fractions"></div>

_More problem types are coming soon._

## See also

- [[Multiplying_Fractions]] — the inverse operation; everything here depends on that rule.
- [[Adding_And_Subtracting_Fractions]] — the other side of fraction arithmetic, where you actually do need a common denominator.
- [[Dividing_Decimals]] — the decimal cousin of this topic.
- [[Mixed_Numbers_And_Improper_Fractions]] — convert mixed numbers into improper fractions before dividing.
- [[Topics_Overview]]
- [[_overview|Home]]

## Sources in the 

- **Math I** — Chapter 4 (Multiplying and Dividing Fractions), Section 4.3: Dividing Fractions
