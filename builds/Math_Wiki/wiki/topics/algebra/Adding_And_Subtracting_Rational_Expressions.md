---
title: "Adding and Subtracting Rational Expressions"
type: topic
aliases: ["Combining Rational Expressions", "Rational Expression Addition and Subtraction"]
tags: ["#branch-algebra-2", "#topic-rational-expressions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "6", section: "6.2"}
related:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Multiplying_And_Dividing_Rational_Expressions"
  - "topics/algebra/Solving_Rational_Equations"
  - "topics/algebra/Rational_Equations_And_Applications"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
problem_type_ids: []
figures: []
summary: "Match the denominators, combine the numerators, then simplify — algebra's version of adding numeric fractions, with polynomials on the bottom."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Adding and Subtracting Rational Expressions

# Adding and Subtracting Rational Expressions

Adding rational expressions is the same dance you already know from ordinary fractions — you can't merge the tops until the bottoms match. What changes is that the "bottom" is now a polynomial, so lining it up requires factoring instead of arithmetic. Once every fraction sits over the same denominator, the rest is bookkeeping.

The bottom you're aiming for is the **least common denominator**, or LCD: the smallest polynomial that every original denominator divides into cleanly. Find it, rebuild both fractions to sit on top of it, combine the numerators, and simplify.

$$
\dfrac{P}{Q} + \dfrac{R}{Q} = \dfrac{P + R}{Q}, \qquad \dfrac{P}{Q} - \dfrac{R}{Q} = \dfrac{P - R}{Q}, \quad Q \neq 0
$$

---

## Key ideas

### When the denominators already match

If both fractions share the same denominator, you do nothing to the bottom — just add or subtract the numerators and keep going. Factor the result afterward to see whether anything cancels.

### When the denominators are different

Here is the full recipe:

1. **Factor every denominator completely.**
2. **Build the LCD.** Take every distinct factor that appears in any denominator, and raise each one to the highest power it appears anywhere. That product is your LCD.
3. **Rescale each fraction.** Multiply the top and bottom of each fraction by whatever factors its denominator is missing, so its bottom becomes the LCD.
4. **Combine** the numerators over the single LCD.
5. **Simplify.** Expand, collect like terms, factor the new numerator, and cancel anything that the LCD still shares with it.

The logic is identical to what you'd do with plain numbers. Combining $\tfrac{1}{4} + \tfrac{2}{3}$ needs an LCD of $12$, giving $\tfrac{3}{12} + \tfrac{8}{12} = \tfrac{11}{12}$. Swap the integers for polynomials and the moves are the same, only now the LCD is a factored expression.

### Watch the minus sign in subtraction

Subtraction is the single biggest trap in this topic. When you write $\dfrac{A}{L} - \dfrac{B}{L}$ as one fraction, the minus sign belongs to **every** term inside $B$, not just the first. Many students lose a term or drop a sign because they forget to distribute that minus. Put $B$ in parentheses before you subtract, and you'll stop losing points: $\dfrac{A - (B)}{L}$.

### Track the restrictions

Every value that makes any original denominator zero must stay excluded from the domain of the final answer, even if the simplified expression looks like it would have allowed those values. Carry the restrictions along explicitly.

---

## Example 1: same denominator — just combine the tops

> Rewrite $\dfrac{3x}{x - 2} + \dfrac{6}{x - 2}$ as a single fraction in lowest terms.

The denominators are already identical, so the bottom stays put. Add the numerators:

$$
\dfrac{3x}{x - 2} + \dfrac{6}{x - 2} = \dfrac{3x + 6}{x - 2}
$$

Factor the numerator to check for simplification:

$$
= \dfrac{3(x + 2)}{x - 2}, \quad x \neq 2
$$

Nothing in the numerator matches $x - 2$, so this is the final form. The restriction $x \neq 2$ comes straight from the original denominator.

---

## Example 2: different denominators, no shared factors

> Combine $\dfrac{3}{x - 1} + \dfrac{2}{x + 4}$ into a single rational expression.

The two denominators $x - 1$ and $x + 4$ have no factor in common, so the LCD is simply their product: $(x - 1)(x + 4)$. Rescale each fraction so its bottom becomes the LCD. The first fraction needs $(x + 4)$ multiplied on top and bottom; the second needs $(x - 1)$:

$$
\dfrac{3}{x - 1} + \dfrac{2}{x + 4} = \dfrac{3(x + 4)}{(x - 1)(x + 4)} + \dfrac{2(x - 1)}{(x - 1)(x + 4)}
$$

Combine the numerators over the shared LCD:

$$
= \dfrac{3(x + 4) + 2(x - 1)}{(x - 1)(x + 4)} = \dfrac{3x + 12 + 2x - 2}{(x - 1)(x + 4)} = \dfrac{5x + 10}{(x - 1)(x + 4)}
$$

The top has a common factor of $5$:

$$
= \dfrac{5(x + 2)}{(x - 1)(x + 4)}, \quad x \neq 1,\; x \neq -4
$$

Nothing cancels with the denominator, so you're done.

---

## Example 3: denominators share a factor — find the true LCD

> Rewrite $\dfrac{x}{x^2 - x - 2} - \dfrac{2}{x^2 - 4}$ as a single fraction.

Start by factoring every denominator. That is nearly always step one in this topic, and if you skip it you'll end up with a "common denominator" that is too big.

$$
x^2 - x - 2 = (x - 2)(x + 1), \qquad x^2 - 4 = (x - 2)(x + 2)
$$

Both denominators contain $(x - 2)$, so the LCD reuses that factor once — not twice. The distinct factors across the two denominators are $(x - 2)$, $(x + 1)$, and $(x + 2)$, each appearing to the first power. So:

$$
\text{LCD} = (x - 2)(x + 1)(x + 2)
$$

Rebuild both fractions over this LCD. The first denominator is missing $(x + 2)$; the second is missing $(x + 1)$:

$$
\dfrac{x}{(x - 2)(x + 1)} \cdot \dfrac{x + 2}{x + 2} - \dfrac{2}{(x - 2)(x + 2)} \cdot \dfrac{x + 1}{x + 1}
$$

$$
= \dfrac{x(x + 2)}{(x - 2)(x + 1)(x + 2)} - \dfrac{2(x + 1)}{(x - 2)(x + 1)(x + 2)}
$$

Now combine the numerators — **and put the second numerator in parentheses** before you subtract it, so the minus reaches both terms:

$$
= \dfrac{x(x + 2) - (2(x + 1))}{(x - 2)(x + 1)(x + 2)} = \dfrac{x^2 + 2x - 2x - 2}{(x - 2)(x + 1)(x + 2)} = \dfrac{x^2 - 2}{(x - 2)(x + 1)(x + 2)}
$$

The numerator $x^2 - 2$ doesn't factor over the integers, so nothing cancels. Final answer:

$$
\dfrac{x^2 - 2}{(x - 2)(x + 1)(x + 2)}, \quad x \neq 2,\; x \neq -1,\; x \neq -2
$$

Notice how much cleaner the work stays because every denominator was factored before the LCD was built. If you had used the unfactored product $(x^2 - x - 2)(x^2 - 4)$ as a "common" denominator, you'd end up multiplying out a quartic and then re-factoring at the end just to cancel $(x - 2)$.

---

## Common pitfalls

- **Missing the distributed minus sign.** In $\dfrac{A}{L} - \dfrac{B}{L}$, the subtraction has to hit every term of $B$. Write the top as $A - (B)$ with explicit parentheses, then expand.
- **Using a "common" denominator that isn't the least.** Multiplying the two denominators together always gives a common denominator, but rarely the smallest one when they share a factor. Factoring first prevents enormous numerators you'll just have to cancel at the end.
- **Forgetting to factor the result.** The combined numerator is almost always meant to be factored and tested against the denominator for cancellation. Skip that step and you'll leave easy simplifications on the table.
- **Losing the domain restrictions.** A value that breaks an original denominator is still excluded even if the simplified expression accepts it. Carry those "$x \neq$" notes to the final answer.
- **Rewriting only the numerator when rescaling.** When you multiply a fraction's top by $(x + 2)$ to rebuild it onto the LCD, you must multiply the bottom by $(x + 2)$ too — otherwise the fraction has changed value.

---

## Prerequisites

Before you start combining rational expressions, make sure you are fluent with these building blocks:

- [[Simplifying_Rational_Expressions]] — canceling factors after you've combined the pieces
- [[Factoring_Trinomials_Leading_Coefficient_1]] — you'll factor every denominator before building the LCD
- [[Adding_And_Subtracting_Fractions]] — the same recipe with numbers; if numeric fractions still trip you up, start there

---

## Problems Involving Adding and Subtracting Rational Expressions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="adding_and_subtracting_rational_expressions"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Simplifying_Rational_Expressions]]
- [[Multiplying_And_Dividing_Rational_Expressions]]
- [[Solving_Rational_Equations]]
- [[Rational_Equations_And_Applications]]
- [[Factoring_Trinomials_Leading_Coefficient_1]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
