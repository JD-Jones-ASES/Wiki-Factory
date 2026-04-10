---
title: "Adding and Subtracting Fractions"
type: topic
aliases: ["Fraction Addition", "Fraction Subtraction", "Adding Fractions", "Subtracting Fractions"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "math_1", chapter: "3", section: "3.5"}
related:
  - "topics/pre_algebra/Multiplying_Fractions"
  - "topics/pre_algebra/Dividing_Fractions"
  - "topics/pre_algebra/Mixed_Numbers_And_Improper_Fractions"
  - "topics/pre_algebra/Adding_And_Subtracting_Decimals"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Comparing_And_Ordering_Fractions"
  - "topics/pre_algebra/Greatest_Common_Factor_And_Least_Common_Multiple"
problem_type_ids: []
figures: []
summary: "Combining fractions by matching denominators, then adding or subtracting only the numerators."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Adding and Subtracting Fractions

# Adding and Subtracting Fractions

Fractions are just counts of pieces. If you know how big each piece is, you can combine two collections by counting total pieces and keeping that piece size. That single idea drives every addition or subtraction of fractions you will ever do. The trick, when denominators disagree, is to first rebuild each fraction so that both sides are chopped into the same-sized pieces.

## What it means

Think of $\frac{3}{8}$ as three eighth-slices of a pizza, and $\frac{2}{8}$ as two more eighth-slices from another pizza of the same size. Sliding them onto one plate gives you five eighth-slices, written $\frac{5}{8}$. Nothing about the slice size changed, so the denominator stayed at $8$. Only the count of pieces (the numerator) changed.

Now suppose one pizza is cut into halves and the other into thirds. You can't just smush $\frac{1}{2}$ and $\frac{1}{3}$ together the way you did before, because the pieces aren't the same size. You have to re-slice each pizza until both use the same cut. Sixths work: a half becomes $\frac{3}{6}$ and a third becomes $\frac{2}{6}$. Once the pieces match, you're back to the easy case.

So the whole task of adding or subtracting fractions boils down to one question: **do my fractions already share a denominator?** If yes, combine the numerators and move on. If not, force them to share one first.

## The rule

When two fractions have the **same** denominator, add or subtract their numerators and keep the denominator unchanged:

$$
\frac{a}{c} + \frac{b}{c} = \frac{a+b}{c}
$$

$$
\frac{a}{c} - \frac{b}{c} = \frac{a-b}{c}
$$

(Both formulas assume $c \neq 0$.)

When two fractions have **different** denominators, follow four steps:

1. Compute the least common denominator $\operatorname{lcd}$, which is the least common multiple of the denominators.
2. Rewrite each fraction as an equivalent one whose denominator is the $\operatorname{lcd}$.
3. Combine the numerators, keeping the $\operatorname{lcd}$ as the new denominator.
4. Simplify the result if a common factor exists.

## Why it works

Rewriting $\frac{1}{2}$ as $\frac{3}{6}$ is not a change in value — it is the same number shown with finer pieces. Once both fractions use the finer pieces, you are back to the "same size pieces" case, and counting pieces is how addition works. The denominator tells you how big each piece is; the numerator tells you how many pieces you have. You can only combine counts when the pieces match.

## Worked examples

### Example 1: like denominators
Compute $\dfrac{5}{12} + \dfrac{1}{12}$.

**Solution.** Both fractions use twelfths, so the pieces already match. Add the numerators and leave the denominator alone.

$$
\frac{5}{12} + \frac{1}{12} = \frac{5 + 1}{12} = \frac{6}{12}
$$

The result $\frac{6}{12}$ reduces — both $6$ and $12$ share the factor $6$.

$$
\frac{6}{12} = \frac{6 \div 6}{12 \div 6} = \frac{1}{2}
$$

So the final answer is $\dfrac{1}{2}$.

### Example 2: unlike denominators, with subtraction
Compute $\dfrac{3}{4} - \dfrac{2}{5}$.

**Solution.** The denominators are $4$ and $5$. They share no common factor, so the least common denominator is their product, $20$.

Rebuild each fraction over $20$:

$$
\frac{3}{4} = \frac{3 \cdot 5}{4 \cdot 5} = \frac{15}{20}
$$

$$
\frac{2}{5} = \frac{2 \cdot 4}{5 \cdot 4} = \frac{8}{20}
$$

Now subtract the numerators:

$$
\frac{15}{20} - \frac{8}{20} = \frac{15 - 8}{20} = \frac{7}{20}
$$

Since $7$ is prime and does not divide $20$, the answer $\dfrac{7}{20}$ is already in simplest form.

### Example 3: unlike denominators, larger numbers
Compute $\dfrac{7}{10} + \dfrac{1}{6}$.

**Solution.** For the denominators $10$ and $6$, list a few multiples: $10, 20, 30, \dots$ and $6, 12, 18, 24, 30, \dots$. The smallest shared one is $30$, so the least common denominator is $30$.

$$
\frac{7}{10} = \frac{7 \cdot 3}{10 \cdot 3} = \frac{21}{30}
$$

$$
\frac{1}{6} = \frac{1 \cdot 5}{6 \cdot 5} = \frac{5}{30}
$$

Add:

$$
\frac{21}{30} + \frac{5}{30} = \frac{26}{30}
$$

Both $26$ and $30$ are divisible by $2$, so simplify once more:

$$
\frac{26}{30} = \frac{13}{15}
$$

The final answer is $\dfrac{13}{15}$.

## Common mistakes

- Adding across the top **and** the bottom. Writing $\frac{1}{2} + \frac{1}{3} = \frac{2}{5}$ is wrong because the pieces were never the same size. Match the denominators first, then combine only the numerators.
- Forgetting to simplify at the end. An answer like $\frac{8}{12}$ is technically correct but not in lowest terms; it should be reduced to $\frac{2}{3}$.
- Multiplying only the bottom of a fraction when rebuilding it. To rewrite $\frac{3}{4}$ over a denominator of $20$, you must scale both the top and the bottom by the same factor.
- Leaving an improper result when the context asks for a mixed number. If a problem about recipes or measurements yields $\frac{9}{4}$, it usually reads more clearly as $2\tfrac{1}{4}$.
- Confusing the least common denominator with the greatest common factor. The $\operatorname{lcd}$ is built to merge fractions; the GCF is used to reduce a single fraction.

## Prerequisites

- [[Equivalent_Fractions_And_Simplifying]]
- [[Comparing_And_Ordering_Fractions]]
- [[Greatest_Common_Factor_And_Least_Common_Multiple]]

If any of these feel shaky, strengthen them first — the steps in this lesson assume you can rebuild a fraction with a new denominator and reduce a result confidently.

## Problems Involving This Topic

<div class="problem-vault-widget" data-topic-slug="adding_and_subtracting_fractions"></div>

_More problem types are coming soon._

## See also

- [[Multiplying_Fractions]]
- [[Dividing_Fractions]]
- [[Mixed_Numbers_And_Improper_Fractions]]
- [[Adding_And_Subtracting_Decimals]]
- [[Algebra_Overview|Algebra]]
- [[_overview|Home]]

## Sources in the ingested textbooks

- **Math I** — Chapter 3, Section 3.5: Adding and Subtracting Fractions
