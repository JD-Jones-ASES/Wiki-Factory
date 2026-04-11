---
title: "Multiplying Fractions"
type: topic
aliases: ["Fraction Multiplication", "Multiply Fractions"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "4", section: "4.1"}
related:
  - "topics/pre_algebra/Dividing_Fractions"
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
  - "topics/pre_algebra/Multiplying_Decimals"
  - "topics/pre_algebra/The_Distributive_Property"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Mixed_Numbers_And_Improper_Fractions"
problem_type_ids: []
figures: []
summary: "Multiply fractions by multiplying numerators and denominators, then simplify."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Multiplying Fractions

# Multiplying Fractions

Multiplying fractions is the friendliest of the four fraction operations. You do not need a common denominator, you do not need to line anything up, and you do not need to convert mixed numbers back and forth. You just multiply straight across: tops with tops, bottoms with bottoms. What can make the process feel slippery is not the arithmetic but the meaning — what does it even mean to take "two-thirds of one-half"? Once that picture clicks, the rule stops feeling like magic and starts feeling like counting.

## What it means

In everyday language the word **of** almost always signals multiplication. "Half of twelve" is $12 \times \tfrac{1}{2}$, which is $6$. The same thing happens with fractions of fractions. "Half of a third" is $\tfrac{1}{2} \times \tfrac{1}{3}$, and the answer is $\tfrac{1}{6}$.

Picture a rectangular chocolate bar. Slice it into three equal horizontal strips — each strip is one third of the bar. Now take one of those strips and cut it in half vertically. The little rectangle you are holding is half of one third, and if you finished slicing every other strip the same way you would see that the bar has been divided into $2 \times 3 = 6$ equal pieces. The piece in your hand is exactly $\tfrac{1}{6}$ of the whole.

That is the **area model** of fraction multiplication. When you multiply $\tfrac{a}{b}$ by $\tfrac{c}{d}$, you are asking: if I chop a unit square into $b$ strips across and $d$ strips down, what fraction does a grid of $a$ by $c$ little tiles cover? The answer has $a \cdot c$ shaded tiles out of a total of $b \cdot d$. There is the rule, already staring back at you.

## The rule

$$
\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}
$$

In words: the new numerator is the old numerators multiplied together, and the new denominator is the old denominators multiplied together. Simplify the answer at the end — or, better, cancel common factors before you multiply so the numbers stay small.

When one of the factors is a whole number, rewrite it first as that number over $1$. For example, $7$ becomes $\tfrac{7}{1}$. After that, the rule works exactly the same.

## Why it works

The denominator of a fraction tells you how many equal parts make one whole. If you slice a whole into $b$ pieces and then slice each of those pieces into $d$ more pieces, you end up with $b \cdot d$ tiny pieces covering the same whole — that is where $b \cdot d$ comes from in the denominator of the answer. The numerator counts how many of those tiny pieces you are keeping: $a$ rows of $c$ pieces each gives $a \cdot c$ total. So the answer is $\tfrac{a c}{b d}$, exactly what the rule says.

Another way to see it is through repeated addition. Multiplying $\tfrac{2}{5}$ by $4$ should mean "four copies of two-fifths", which is $\tfrac{2}{5} + \tfrac{2}{5} + \tfrac{2}{5} + \tfrac{2}{5} = \tfrac{8}{5}$. That matches the straight-across rule: $\tfrac{4}{1} \cdot \tfrac{2}{5} = \tfrac{8}{5}$.

## Worked examples

### Example 1: straight-across multiplication

Multiply and simplify: $\dfrac{3}{7} \cdot \dfrac{5}{8}$.

Multiply the numerators together, then the denominators together:

$$
\frac{3}{7} \cdot \frac{5}{8} = \frac{3 \cdot 5}{7 \cdot 8} = \frac{15}{56}
$$

Check whether the answer simplifies. The numerator $15$ factors as $3 \cdot 5$, and the denominator $56$ factors as $2^3 \cdot 7$. They share no common factors, so $\tfrac{15}{56}$ is already in lowest terms.

**Answer:** $\dfrac{15}{56}$.

### Example 2: cross-canceling before you multiply

Multiply and simplify: $\dfrac{9}{10} \cdot \dfrac{4}{15}$.

You could multiply first and simplify at the end, but the numbers will balloon. Instead, scan for common factors that sit **diagonally** across the two fractions. A factor in one numerator can cancel with a factor in the **other** denominator (never its own).

- $9$ in the first numerator and $15$ in the second denominator share a factor of $3$. Divide both by $3$: $9 \div 3 = 3$ and $15 \div 3 = 5$.
- $4$ in the second numerator and $10$ in the first denominator share a factor of $2$. Divide both by $2$: $4 \div 2 = 2$ and $10 \div 2 = 5$.

After cross-canceling, the problem becomes:

$$
\frac{3}{5} \cdot \frac{2}{5} = \frac{3 \cdot 2}{5 \cdot 5} = \frac{6}{25}
$$

**Answer:** $\dfrac{6}{25}$. Because you canceled first, no simplification is needed at the end.

### Example 3: a whole number times a fraction

A recipe calls for $\tfrac{2}{5}$ cup of oats per serving. How many cups do you need for $6$ servings?

Rewrite $6$ as a fraction over $1$, then multiply straight across:

$$
6 \cdot \frac{2}{5} = \frac{6}{1} \cdot \frac{2}{5} = \frac{6 \cdot 2}{1 \cdot 5} = \frac{12}{5}
$$

Convert the improper fraction to a mixed number: $\tfrac{12}{5} = 2\tfrac{2}{5}$.

**Answer:** $2\tfrac{2}{5}$ cups of oats.

## Common mistakes

- **Finding a common denominator.** That is only needed for adding and subtracting. To multiply, leave the denominators alone and just multiply them.
- **Canceling inside the same fraction first.** Cross-canceling goes between a numerator of one fraction and the denominator of the **other**. Canceling within one fraction is the same as simplifying it, which is fine but does not take the place of cross-canceling.
- **Putting a whole number in the denominator.** When you rewrite $5$ as a fraction, it becomes $\tfrac{5}{1}$, not $\tfrac{1}{5}$.
- **Forgetting to simplify.** Even if cross-canceling is not obvious, check the final answer for a greatest common factor bigger than $1$.

## Prerequisites

Before tackling problems here, make sure you are solid on:

- [[Equivalent_Fractions_And_Simplifying|Equivalent fractions and simplifying]] — you will use this constantly to reduce answers.
- [[Mixed_Numbers_And_Improper_Fractions|Mixed numbers and improper fractions]] — many word problems hand you a mixed number and expect an improper fraction back, or the reverse.

If either of those feels shaky, warm up there and come back.

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="multiplying_fractions"></div>

_More problem types are coming soon._

## See also

- [[Dividing_Fractions]] — the inverse operation, which reuses everything on this page.
- [[Adding_And_Subtracting_Fractions]] — when you need a common denominator instead.
- [[Multiplying_Decimals]] — the decimal cousin of this topic.
- [[The_Distributive_Property]] — multiplying a fraction across a sum of terms.
- [[Topics_Overview]]
- [[_overview|Home]]

## Sources in the 

- **Math I** — Chapter 4 (Multiplying and Dividing Fractions), Section 4.1: Multiplying Fractions
