---
title: "Repeating Decimals as Fractions"
type: topic
aliases: ["Recurring Decimals"]
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#key-technique", "#skill-algebraic-manipulation", "#test-act", "#test-clt"]
created: 2026-04-11
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Solving_Two_Step_Equations"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Fractions_Decimals_And_Percents"
  - "topics/pre_algebra/Solving_Two_Step_Equations"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "A clever trick that turns any repeating decimal, no matter how long the pattern, into an exact fraction in lowest terms."
---
> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Repeating Decimals as Fractions

# Repeating Decimals as Fractions

If you divide $1$ by $3$ on a calculator, the screen shows $0.3333333...$ with the $3$s marching off the right edge forever. That is a **repeating decimal**, and the little bar in $0.\overline{3}$ is the mathematician's way of saying, "the $3$ keeps going, and here is where the pattern begins." It turns out that every repeating decimal is secretly a fraction in disguise, and there is a short trick — really just a clever bit of subtraction — that will convert any repeating decimal you meet into its exact fractional form. That trick is the whole subject of this page.

Why care? Because fractions are exact and repeating decimals are not, at least not without that special bar. If you ever need to add $0.\overline{3}$ to $0.\overline{6}$ and get a precise answer, converting each to $\tfrac{1}{3}$ and $\tfrac{2}{3}$ first is the only honest way to do it. The conversion trick is also a showcase of how much leverage you get by naming the mystery thing $x$ and then solving for it — the same move you use in [[Solving_Two_Step_Equations]].

## What it means / The idea

A **terminating decimal** stops: $0.25$, $0.8$, $0.17$. A **repeating decimal** does not stop, but it eventually settles into a block of digits that loops forever. The bar over the top of those digits marks the loop. For example:

$$
0.\overline{3} = 0.333333... \qquad 0.\overline{27} = 0.272727... \qquad 0.1\overline{6} = 0.16666...
$$

Every repeating decimal is equal to a fraction with whole-number top and bottom. The reason this works is that the infinitely long pattern can be trapped by a single equation. Suppose the decimal is called $x$. Multiplying $x$ by a well-chosen power of $10$ shifts its decimal point to the right — and if you pick the shift so that both copies of $x$ line up at the repeating block, subtracting one from the other erases the infinite tail completely, leaving you with a clean, finite equation you can solve for $x$. The leftover equation is always something like $9x = 3$ or $99x = 27$, which is easy to turn into a fraction.

A separate, easier piece: if a decimal terminates, you do not need the trick at all. Just read the digits and put them over the matching power of $10$. For example, $0.25 = \tfrac{25}{100} = \tfrac{1}{4}$ and $0.8 = \tfrac{8}{10} = \tfrac{4}{5}$.

## How it works / The procedure

1. **Name the decimal $x$.** Write $x = 0.\overline{abc}$ where $\overline{abc}$ is the repeating block.
2. **Shift the decimal past one full loop.** Multiply both sides by $10^k$, where $k$ is the length of the repeating block. For a one-digit loop, multiply by $10$; for a two-digit loop, multiply by $100$; for a three-digit loop, multiply by $1000$.
3. **Subtract the original equation** from the shifted one. The matching repeating tails cancel, and you are left with a plain whole number on the right and a whole-number coefficient times $x$ on the left.
4. **Solve for $x$** by dividing, then simplify the fraction using [[Equivalent_Fractions_And_Simplifying]].

If there are some non-repeating digits in front of the loop (like $0.1\overline{6}$), the steps are the same, except you first shift the decimal point past those front digits before you multiply again to chase the loop. Example 3 walks through exactly that case.

## Why it works

Think of the decimal tail as a ghost. If you try to grab it directly, it slides away — there is always one more digit. But if you shift a copy of the same decimal until both copies have identical ghosts, subtracting one from the other causes the two ghosts to cancel each other out atom-for-atom, leaving nothing but a real, finite number. That is the whole trick. The multiplication by $10^k$ is chosen specifically so that the copies line up. If the loop has length $1$, a single factor of $10$ slides everything exactly one digit over. If the loop has length $2$, you need a factor of $100$. And so on. Without the right alignment, the subtraction would leave behind a messy piece and the cancellation would fail.

One more insight: the denominators you end up with — $9$, $99$, $999$ — are exactly the powers of $10$ minus $1$, which is a fingerprint of this method. Any fraction whose denominator, after simplification, contains only $2$s and $5$s will give a terminating decimal; any other denominator gives a repeating one. That is why $\tfrac{1}{4}$ terminates and $\tfrac{1}{3}$ does not.

## Worked examples

### Example 1

Rohan is double-checking a result from his community garden ratio sheet and wants to rewrite $0.\overline{3}$ as a fraction. The repeating block is a single digit, so multiply by $10$ to slide past one full loop:

$$
x = 0.\overline{3}
$$
$$
10x = 3.\overline{3}
$$

Subtract the first equation from the second. On the right, $3.\overline{3} - 0.\overline{3} = 3$, because the tails cancel exactly. On the left, $10x - x = 9x$:

$$
9x = 3
$$

Divide both sides by $9$:

$$
x = \frac{3}{9} = \frac{1}{3}
$$

So $0.\overline{3} = \tfrac{1}{3}$, exactly. The decimal pattern was stored as a fraction all along.

### Example 2

Emilia is running numbers for a farmer's market stand and needs to convert $0.\overline{27}$ into a fraction. The repeating block has two digits, so the shift multiplier is $100$:

$$
x = 0.\overline{27}
$$
$$
100 x = 27.\overline{27}
$$

Subtract the first from the second. The repeating tails cancel, leaving whole numbers on the right:

$$
99 x = 27
$$

Divide both sides by $99$ and simplify using the greatest common factor (here, $9$):

$$
x = \frac{27}{99} = \frac{3}{11}
$$

As a check, dividing $3$ by $11$ on paper gives $0.272727...$, matching the original decimal. The conversion is exact, not an approximation.

### Example 3

Mateo is writing up a result for his school newspaper's data column and wants to express $0.1\overline{6}$ (which is $0.1666...$) as a fraction. The tricky part here is that only the $6$ repeats, while the $1$ after the decimal point does not. The fix is to shift twice: once to push the non-repeating digit out of the decimal part, and a second time to chase the loop.

Start by naming the decimal and shifting past the single non-repeating digit:

$$
x = 0.1\overline{6}
$$
$$
10 x = 1.\overline{6}
$$

Now shift again to move past one full repeating block. The loop is one digit long, so multiply the *original* $x$ by $100$:

$$
100 x = 16.\overline{6}
$$

Subtract the $10x$ equation from the $100x$ equation. The repeating tails $0.\overline{6}$ line up on both sides and cancel:

$$
100 x - 10 x = 16.\overline{6} - 1.\overline{6}
$$
$$
90 x = 15
$$

Divide and simplify:

$$
x = \frac{15}{90} = \frac{1}{6}
$$

So $0.1\overline{6} = \tfrac{1}{6}$, exactly. A quick check: $1 \div 6 = 0.16666...$, matching.

## Common pitfalls

- **Using the wrong shift multiplier.** The multiplier is $10$ raised to the length of the repeating block, not the total length of the decimal. For $0.\overline{27}$ the loop is two digits, so multiply by $100$; for $0.\overline{3}$ the loop is one digit, so multiply by $10$. Miscounting the loop length sends everything sideways.
- **Forgetting that the tails must align for cancellation.** If the decimal has non-repeating digits before the loop (like $0.1\overline{6}$), you must shift once to clear those non-repeaters and again to chase the loop, then subtract. Skipping the first shift leaves a leftover piece and the tails fail to cancel.
- **Not simplifying the final fraction.** $\tfrac{27}{99}$ is a correct first answer, but $\tfrac{3}{11}$ is the final, lowest-terms form. On a test the simplified version is what is expected.
- **Confusing $0.\overline{9}$ with something less than $1$.** A famous special case: $0.\overline{9} = 1$, exactly, not almost. The method gives $9 x = 9$, so $x = 1$. It feels strange but it is a real equality, not a rounding.

## Prerequisites

- [[Fractions_Decimals_And_Percents]] — you need to be comfortable moving between these three representations
- [[Solving_Two_Step_Equations]] — the trick is really an equation you set up and solve for $x$
- [[Equivalent_Fractions_And_Simplifying]] — the final step is always putting the fraction in lowest terms

## Problems Involving Repeating Decimals as Fractions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="repeating_decimals_as_fractions"></div>

## See Also

- [[Fractions_Decimals_And_Percents]] — the broader topic of converting between decimal and fraction forms
- [[Equivalent_Fractions_And_Simplifying]] — reducing to lowest terms after the conversion
- [[Irrational_Numbers_And_Real_Numbers]] — repeating decimals are rational; truly non-repeating ones are not
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
