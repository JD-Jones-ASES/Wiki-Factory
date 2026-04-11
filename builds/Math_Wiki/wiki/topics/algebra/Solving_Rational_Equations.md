---
title: "Solving Rational Equations"
type: topic
aliases: ["Rational Equations", "Fractional Equations"]
tags: ["#branch-algebra-1", "#topic-rational-expressions", "#key-topic", "#test-sat", "#test-act"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_1", chapter: "9", section: "9.3"}
related:
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Adding_And_Subtracting_Rational_Expressions"
  - "topics/algebra/Multiplying_And_Dividing_Rational_Expressions"
  - "topics/algebra/Rational_Equations_And_Applications"
  - "topics/algebra/Multi_Step_Equations"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Factoring_Trinomials_Leading_Coefficient_1"
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
problem_type_ids: []
figures: []
summary: "Clear the fractions by multiplying both sides by the LCD, solve the resulting polynomial equation, and always verify each answer against the original — some solutions are mirages that must be thrown out."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Solving Rational Equations

# Solving Rational Equations

A **rational equation** is an equation that contains at least one rational expression — a fraction with the variable somewhere in the denominator. Your goal is the same as with any equation: isolate the variable. The wrinkle is that fractions get in the way, and you have to remove them before you can use the routine tools from [[Multi_Step_Equations]].

The trick is to rescale both sides of the equation by the least common denominator (LCD) of every fraction that appears. Once every denominator vanishes, what's left is a polynomial equation — linear or quadratic in disguise — and you solve that like normal. But there's a catch that has no analogue in linear algebra: some "answers" you'll get at the end are fakes that have to be thrown out. Skipping the final check is the single most common way students lose marks on this topic.

$$
\text{Rational equation} \quad\xrightarrow{\text{multiply by LCD}}\quad \text{polynomial equation} \quad\xrightarrow{\text{solve}}\quad \text{candidates} \quad\xrightarrow{\text{test in original}}\quad \text{real solutions}
$$

---

## Key ideas

### The four-step routine

1. **Factor every denominator** and work out the LCD needed to match them all.
2. **Rescale each side by that LCD.** Each denominator gets cancelled, leaving a denominator-free polynomial equation.
3. **Solve the polynomial equation** using whatever method fits: isolation for a linear result, factoring or the quadratic formula for a quadratic.
4. **Substitute each candidate back into the original equation.** Any value that makes one of the starting denominators equal to zero is not a real solution — it's an **extraneous solution** and must be rejected.

### What "extraneous" means and where these ghosts come from

When you scale both sides of an equation by an expression that contains the variable, you are not performing a perfectly reversible move. The scaling multiplies both sides by a quantity that is normally nonzero, but at specific values of the variable that quantity is zero — and multiplying by zero can transform a false statement into a true one. Those specific values can sneak into your candidate list as phantom solutions that never satisfied the equation in the first place. That's why step 4 isn't optional: plugging each candidate back into the original is how you catch the ghosts.

A candidate is extraneous precisely when it makes at least one of the original denominators equal to zero. If that happens, drop the value and move on. If every denominator stays nonzero and both sides of the original equation agree, the candidate is a genuine solution.

### Proportions: a special case you can cross-multiply

If the equation has exactly one fraction on each side — that is, it looks like $\dfrac{a}{b} = \dfrac{c}{d}$ — you can skip the LCD step and **cross-multiply** straight to $ad = bc$. That's just the LCD move in disguise, with $bd$ as the LCD, but it saves a little writing.

---

## Example 1: basic case with the variable in a denominator

> Find all real solutions to $\dfrac{3}{x} + \dfrac{1}{4} = \dfrac{5}{x}$.

The denominators are $x$ and $4$, so the LCD is $4x$. Scale every single term on both sides by $4x$:

$$
4x \cdot \dfrac{3}{x} + 4x \cdot \dfrac{1}{4} = 4x \cdot \dfrac{5}{x}
$$

Each fraction's denominator cancels with part of the LCD:

$$
12 + x = 20
$$

That's just a one-step linear equation. Subtract $12$ from both sides:

$$
x = 8
$$

**Check against the original.** With $x = 8$: $\dfrac{3}{8} + \dfrac{1}{4} = \dfrac{3}{8} + \dfrac{2}{8} = \dfrac{5}{8}$, and the right side is $\dfrac{5}{8}$. Both sides match, and neither denominator is zero, so $x = 8$ is a real solution.

**Solution:** $x = 8$.

---

## Example 2: a factored LCD and a proportion shortcut

> Find the value of $x$ that satisfies $\dfrac{x + 1}{3} = \dfrac{2x - 5}{7}$.

This is a proportion — one fraction on each side. You could multiply through by the LCD of $21$, but cross-multiplication is cleaner:

$$
7(x + 1) = 3(2x - 5)
$$

Distribute on each side:

$$
7x + 7 = 6x - 15
$$

Move the $x$ pieces to one side and the numbers to the other:

$$
x = -22
$$

**Check.** Plug into the original: $\dfrac{-22 + 1}{3} = \dfrac{-21}{3} = -7$, and $\dfrac{2(-22) - 5}{7} = \dfrac{-49}{7} = -7$. Both sides land at $-7$, so the candidate survives.

**Solution:** $x = -22$.

Notice that for a proportion there's no way for either denominator to become zero — they are the constants $3$ and $7$ — so the extraneous-solution check is automatic. As soon as a variable appears downstairs, the check becomes mandatory.

---

## Example 3: an extraneous solution — the case that makes this topic tricky

> Find all real solutions to $\dfrac{x}{x - 2} - \dfrac{3}{x + 1} = \dfrac{6}{(x - 2)(x + 1)}$.

Before touching anything, note the restrictions: the denominators are already factored, and they tell you that $x \neq 2$ and $x \neq -1$ — any candidate hitting either of those values will be a ghost.

The three denominators are $(x - 2)$, $(x + 1)$, and their product $(x - 2)(x + 1)$, which is itself the LCD. Scale each piece of the equation by that LCD:

$$
(x - 2)(x + 1) \cdot \dfrac{x}{x - 2} - (x - 2)(x + 1) \cdot \dfrac{3}{x + 1} = (x - 2)(x + 1) \cdot \dfrac{6}{(x - 2)(x + 1)}
$$

Each fraction loses the factor that cancels with its denominator:

$$
x(x + 1) - 3(x - 2) = 6
$$

Expand and collect:

$$
x^2 + x - 3x + 6 = 6
$$

$$
x^2 - 2x + 6 = 6
$$

$$
x^2 - 2x = 0
$$

Factor out the common $x$:

$$
x(x - 2) = 0
$$

So the candidates are $x = 0$ and $x = 2$.

**Now the check.** You *must* test both in the **original** equation, not the polynomial version.

*Candidate $x = 0$.* The original becomes $\dfrac{0}{0 - 2} - \dfrac{3}{0 + 1} = \dfrac{0}{-2} - 3 = 0 - 3 = -3$, and the right side is $\dfrac{6}{(-2)(1)} = -3$. Both sides equal $-3$, and no denominator hit zero, so $x = 0$ is a real solution.

*Candidate $x = 2$.* The very first term is $\dfrac{2}{2 - 2} = \dfrac{2}{0}$, which is undefined. The original equation has no meaning at $x = 2$, so this value is extraneous. Throw it out — it was introduced by the LCD multiplication, not by the original equation.

**Solution:** $x = 0$ only. The $x = 2$ was a ghost.

This is the whole lesson of the topic in one problem. When you scale both sides by $(x - 2)(x + 1)$ to clear the fractions, you quietly multiplied both sides by zero when $x = 2$, and that's how a non-solution sneaks onto the candidate list. The check is the only way to catch it.

---

## Common pitfalls

- **Skipping the check.** This is by far the number-one way students lose points on rational equations. If the variable appears in any denominator, running the check is not optional — it is part of the solving process. Not every equation has extraneous solutions, but you can't tell which ones do without testing.
- **Forgetting to distribute the minus sign.** When you multiply through by the LCD, terms that were being subtracted keep their sign only if you treat the entire numerator like a parenthesized group. Lose track of the minus and you'll silently turn a subtraction into an addition.
- **Multiplying only one side by the LCD.** This is not "clearing fractions" — it's breaking the equation. Every term on both sides must be scaled by the LCD.
- **Missing a term when distributing the LCD.** If the equation is $\dfrac{3}{x} + \dfrac{1}{4} = \dfrac{5}{x}$, the LCD $4x$ has to hit *all three* terms, including the $\dfrac{1}{4}$. Dropping the middle term is a classic slip.
- **Using the "solved" equation for the check instead of the original.** The extraneous candidate will satisfy the polynomial equation — that's where it came from. You have to substitute back into the original rational form to expose it.
- **Forgetting to factor denominators first.** If you try to guess the LCD before factoring, you'll usually produce one that's too large and mangle the next few steps.

---

## Prerequisites

Before you tackle rational equations, make sure each of these is solid:

- [[Multi_Step_Equations]] — the "solve after clearing fractions" step reduces to this
- [[Simplifying_Rational_Expressions]] — you need to see when a candidate breaks a denominator
- [[Factoring_Trinomials_Leading_Coefficient_1]] — many denominators need factoring to build the LCD
- [[Adding_And_Subtracting_Fractions]] — the LCD idea should already feel familiar from numeric fractions

---

## Problems Involving Solving Rational Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="solving_rational_equations"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Simplifying_Rational_Expressions]]
- [[Adding_And_Subtracting_Rational_Expressions]]
- [[Multiplying_And_Dividing_Rational_Expressions]]
- [[Rational_Equations_And_Applications]]
- [[Multi_Step_Equations]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
