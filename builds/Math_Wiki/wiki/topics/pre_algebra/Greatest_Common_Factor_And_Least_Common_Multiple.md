---
title: "Greatest Common Factor and Least Common Multiple"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Divisibility_Factors_And_Prime_Factorization"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Adding_And_Subtracting_Fractions"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Divisibility_Factors_And_Prime_Factorization"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "The GCF is the largest number that divides both; the LCM is the smallest number they both divide into. Use prime factorizations to find either quickly."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Greatest Common Factor and Least Common Multiple

# Greatest Common Factor and Least Common Multiple

Two of the most useful numbers you can compute from a pair of whole numbers are the **greatest common factor** (GCF) and the **least common multiple** (LCM). They answer complementary questions. The GCF is the largest number that divides both of the original numbers, so it is the fattest shared piece they have in common. The LCM is the smallest positive number that both of the originals divide into, so it is the thinnest shared whole they can both fit inside. One sits below them; the other sits above them.

These two numbers turn up constantly in pre-algebra. Whenever you reduce a fraction to lowest terms, you are dividing numerator and denominator by their GCF. Whenever you add or subtract fractions with different denominators, you are looking for their LCM. Arithmetic on rational numbers runs on the same engine that this lesson is teaching you to operate.

## The GCF

The **greatest common factor** — GCF for short — is the biggest positive integer that divides every number in a given list evenly. Another common name for it is the **greatest common divisor** or GCD. The notation varies — $\gcd(18, 24)$ and $(18, 24)$ both appear — but the idea does not.

There are two common ways to compute it.

**By listing factors.** Write out every factor of each number. Circle the factors that show up in *every* list. The largest circled number is the GCF. This is a reasonable strategy for small numbers, where the factor lists are short.

**By prime factorization.** Write each number as a product of primes. For each prime that appears in *all* the factorizations, take the **smallest** exponent that prime has across the factorizations. Multiply those minimum-powered primes together. The product is the GCF.

The prime-factorization method is faster for larger numbers because you do not have to list every factor. It is also more systematic, which makes it easier to check your work.

## The LCM

The **least common multiple** — LCM for short — is the smallest positive integer that every number on your list divides into without a remainder. It is what you need when you want a single pot big enough to catch whole multiples of each of the original numbers at once.

Again, two methods:

**By listing multiples.** Write the first several multiples of each number. Look for the smallest number that appears in every list. That is the LCM. This is quick for small numbers whose multiples show up often.

**By prime factorization.** Write each number as a product of primes. For each prime that appears in *any* of the factorizations, take the **largest** exponent that prime has across the factorizations. Multiply those maximum-powered primes together. The product is the LCM.

The minimum-vs-maximum contrast is the whole punch line. GCF takes minimum exponents because it wants the most a divisor can share with every number; LCM takes maximum exponents because it wants the least a multiple needs to contain to cover every number.

## Why the prime-factorization method works

Every integer above $1$ decomposes into primes in exactly one way. Any divisor of that integer has to be built from those very same prime building blocks, used no more times than they appear in the original. If a prime appears in one number's factorization but not the other, it cannot be in any common divisor — both numbers must contribute a positive amount of that prime for it to survive. That is why the GCF only includes primes that appear in *every* factorization, and only up to the **smallest** exponent any of them has.

For the LCM the story is the reverse. Any number that both of the originals divide into must contain at least as many copies of every prime as either of them has. If one number needs $2^3$ and the other needs $2^5$, then their shared multiple must contain $2^5$ (the maximum) so that both $2^3$ and $2^5$ fit inside it. A prime that appears in even a single factorization has to appear in the LCM because one of the numbers needs it. So the LCM takes every prime that shows up anywhere, raised to its **largest** exponent.

The GCF and LCM are tied together by a beautiful identity: for any two positive whole numbers $a$ and $b$,

$$
\gcd(a, b) \cdot \operatorname{lcm}(a, b) = a \cdot b.
$$

Once you know the GCF of two numbers, you can find the LCM as $\tfrac{ab}{\gcd(a, b)}$, and vice versa. This is the fastest shortcut for LCMs of two numbers once a GCF is in hand.

## Worked examples

### Example 1: GCF of $18$ and $24$

Give the greatest common factor of $18$ and $24$.

**Method A (list of factors).** Factors of $18$: $1, 2, 3, 6, 9, 18$. Factors of $24$: $1, 2, 3, 4, 6, 8, 12, 24$. The factors appearing in both lists are $1, 2, 3, 6$. The greatest is $6$, so $\gcd(18, 24) = 6$.

**Method B (prime factorization).** $18 = 2 \cdot 3^2$. $24 = 2^3 \cdot 3$. The primes that appear in both factorizations are $2$ and $3$. For $2$ the exponents are $1$ and $3$; the minimum is $1$, so keep $2^1$. For $3$ the exponents are $2$ and $1$; the minimum is $1$, so keep $3^1$. Multiply:

$$
\gcd(18, 24) = 2^1 \cdot 3^1 = 2 \cdot 3 = 6.
$$

Both methods agree: the greatest common factor is $6$.

### Example 2: LCM of $6$ and $8$

Give the least common multiple of $6$ and $8$.

**Method A (list of multiples).** Multiples of $6$: $6, 12, 18, 24, 30, 36, \ldots$. Multiples of $8$: $8, 16, 24, 32, \ldots$. The smallest number that shows up in both lists is $24$, so $\operatorname{lcm}(6, 8) = 24$.

**Method B (prime factorization).** $6 = 2 \cdot 3$. $8 = 2^3$. The primes that appear in at least one factorization are $2$ and $3$. The largest exponent of $2$ is $3$ (from $8$), so keep $2^3$. The largest exponent of $3$ is $1$ (from $6$; $8$ contributes nothing), so keep $3^1$. Multiply:

$$
\operatorname{lcm}(6, 8) = 2^3 \cdot 3 = 8 \cdot 3 = 24.
$$

Both methods give $24$. You could also use the identity: $\gcd(6, 8) = 2$, so $\operatorname{lcm}(6, 8) = \tfrac{6 \cdot 8}{2} = \tfrac{48}{2} = 24$. All three routes end in the same place.

### Example 3: GCF and LCM of $12$ and $30$

Determine both the greatest common factor and the least common multiple of $12$ and $30$.

Start by getting prime factorizations, which give you both answers in one pass:

$$
12 = 2^2 \cdot 3, \qquad 30 = 2 \cdot 3 \cdot 5.
$$

For the GCF, take primes appearing in *both* factorizations and use the minimum exponent for each. Both factorizations contain $2$ and $3$, but only $30$ contains $5$, so $5$ is excluded from the GCF. Minimum exponent of $2$ is $1$ (from $30$); minimum exponent of $3$ is $1$ (from both). So:

$$
\gcd(12, 30) = 2^1 \cdot 3^1 = 6.
$$

For the LCM, take primes appearing in *either* factorization and use the maximum exponent for each. Maximum exponent of $2$ is $2$ (from $12$); maximum exponent of $3$ is $1$; maximum exponent of $5$ is $1$ (from $30$). So:

$$
\operatorname{lcm}(12, 30) = 2^2 \cdot 3 \cdot 5 = 4 \cdot 15 = 60.
$$

Sanity-check with the identity: $\gcd \cdot \operatorname{lcm} = 6 \cdot 60 = 360$, and $12 \cdot 30 = 360$ as well. Both products agree, so both answers are consistent.

Notice how close the two answers sit to the originals. The GCF ($6$) is below both $12$ and $30$, and the LCM ($60$) is above both. That is always the case: the GCF can never be larger than the smallest of the numbers, and the LCM can never be smaller than the largest. If your work produces a GCF bigger than one of the originals or an LCM smaller than one of them, stop — something has gone wrong.

## Common pitfalls

- **Swapping GCF and LCM.** The GCF is small (below the numbers); the LCM is large (at or above the numbers). If your "GCF" ends up larger than the numbers themselves, you have computed the LCM by mistake.
- **Using maximum exponents for the GCF.** GCF uses the *minimum* exponent of each shared prime; LCM uses the *maximum*. Mixing these up is the most common technical slip.
- **Including primes that appear in only one factorization in the GCF.** A prime has to show up in *every* number's factorization to be part of the GCF. If one number has no factor of $5$, the GCF has no factor of $5$ either.
- **Listing an incomplete set of multiples.** When using the multiples method for the LCM, you have to extend the lists far enough to spot an overlap. Three or four multiples is not always enough for larger numbers.
- **Forgetting to multiply the primes at the end.** Writing the prime list is only part of the work — the GCF or LCM is the *product* of those primes, not the list itself.

## Problems Involving Greatest Common Factor and Least Common Multiple

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="greatest_common_factor_and_least_common_multiple"></div>

## See Also

- [[Divisibility_Factors_And_Prime_Factorization]]
- [[Equivalent_Fractions_And_Simplifying]]
- [[Adding_And_Subtracting_Fractions]]
- [[Multiplying_Fractions]]
- [[Dividing_Fractions]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
