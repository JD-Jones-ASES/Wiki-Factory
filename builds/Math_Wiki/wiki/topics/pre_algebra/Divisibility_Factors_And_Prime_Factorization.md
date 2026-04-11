---
title: "Divisibility, Factors, and Prime Factorization"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-numbers-and-operations", "#skill-procedural-calculation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Greatest_Common_Factor_And_Least_Common_Multiple"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
  - "topics/pre_algebra/Order_Of_Operations"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Place_Value_Rounding_And_Estimation"
  - "topics/pre_algebra/Multiplying_And_Dividing_Integers"
  - "topics/pre_algebra/Equivalent_Fractions_And_Simplifying"
problem_type_ids: []
figures: []
summary: "Know when one whole number divides another, list factors of a number, and break a number down into its unique product of primes."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > Divisibility, Factors, and Prime Factorization

# Divisibility, Factors, and Prime Factorization

Every whole number has hidden structure. Behind the familiar decimal digits sits a list of building blocks — the primes it is made from — that explain almost everything else about how the number behaves. Whenever you reduce a fraction, find a common denominator, compute a GCF or LCM, or check whether one quantity divides another, you are really relying on facts about factors and primes. This lesson is where those facts get introduced.

The three skills that live together in this topic are: checking quickly whether one number divides another (**divisibility**), listing everything that divides a given number (**factors**), and writing a number as a product of primes in a unique way (**prime factorization**). Each builds on the one before.

## Divisibility and factors

A whole number $a$ is **divisible** by a nonzero whole number $b$ if $a \div b$ comes out with a remainder of $0$. Equivalently, $b$ goes into $a$ a whole number of times. When that happens we say that **$b$ divides $a$**, or that **$b$ is a factor** of $a$. For example, $4$ is a factor of $12$ because $12 \div 4 = 3$ with no remainder; but $4$ is not a factor of $10$ because $10 \div 4 = 2$ with remainder $2$.

The full list of factors of a number is the set of whole numbers that divide it evenly. For $12$ that list is $1, 2, 3, 4, 6, 12$. Every whole number has at least two factors — itself and $1$ — and factors always pair up around the square root. In the factorization $12 = 1 \cdot 12 = 2 \cdot 6 = 3 \cdot 4$, each factor on the left pairs with exactly one on the right. That pairing is what makes "listing all the factors" a finite, manageable job: once you pass the square root, every pair you find is one you have already listed in the opposite order.

A set of divisibility rules saves you from long division on small divisors. These are the most useful:

- **Divisible by $2$** if the last digit is $0$, $2$, $4$, $6$, or $8$ (even).
- **Divisible by $3$** if the sum of the digits is divisible by $3$.
- **Divisible by $4$** if the last two digits together form a number divisible by $4$.
- **Divisible by $5$** if the last digit is $0$ or $5$.
- **Divisible by $6$** if it is divisible by both $2$ and $3$.
- **Divisible by $9$** if the sum of the digits is divisible by $9$.
- **Divisible by $10$** if the last digit is $0$.

These rules are tested quickly in your head. For example, $1,\!764$ is divisible by $3$ because $1 + 7 + 6 + 4 = 18$ and $18$ is divisible by $3$. The divisibility rules are the fastest way to begin hunting for factors of any reasonably small number.

## Primes, composites, and prime factorization

Some numbers have a very short list of factors. A **prime** is an integer above $1$ with exactly two factors — the number itself and $1$, nothing else. The first few primes are $2, 3, 5, 7, 11, 13, 17, 19, 23, \ldots$. There is no largest prime — the list goes on forever.

Any whole number greater than $1$ that is not prime is **composite**. A composite has factors other than just $1$ and itself; it can be "broken down." The number $1$ is a special case — it is neither prime nor composite and is usually excluded from both lists.

The remarkable fact about primes is the **Fundamental Theorem of Arithmetic**: any integer above $1$ has one — and only one — expression as a product of prime numbers, setting the order of the factors aside. That one-way-only product is the **prime factorization** of the number. For instance,

$$
60 = 2 \cdot 2 \cdot 3 \cdot 5 = 2^2 \cdot 3 \cdot 5.
$$

No other list of primes will multiply to give $60$. The prime factorization is the number's unique fingerprint.

To find a prime factorization, you can use a **factor tree**. Start with the number at the top, split it into any two factors whose product is the original, and draw a branch to each of them. Any factor that is prime gets a circle and stops; any factor that is composite gets split further. When every branch ends in a circled prime, the product of all the circled primes (with repetition) is the prime factorization. Different trees starting from the same number can look different along the way, but they all end up producing the same list of primes at the leaves. That is exactly what the Fundamental Theorem guarantees.

## How to do it

1. **Divisibility check.** Use the short rules above. For divisors the rules do not cover (like $7$ or $11$), actually divide.
2. **Factor listing.** Start with $1 \cdot n$ and try $2, 3, 4, \ldots$ in turn, writing each successful pair. Stop when the smaller factor in the pair exceeds $\sqrt{n}$.
3. **Prime factorization.** Draw a factor tree or repeatedly divide by the smallest prime that works. Continue until every branch is a prime. Write the final answer as a product, using exponents for repeated primes.

## Worked examples

### Example 1: listing the factors of $36$

Give every factor of $36$.

Work through whole numbers starting at $1$ and write each pair:

- $1 \cdot 36 = 36$, so $1$ and $36$ are factors.
- $2 \cdot 18 = 36$, so $2$ and $18$ are factors.
- $3 \cdot 12 = 36$, so $3$ and $12$ are factors.
- $4 \cdot 9 = 36$, so $4$ and $9$ are factors.
- $5$? $36 \div 5$ leaves a remainder, so $5$ is not a factor.
- $6 \cdot 6 = 36$, so $6$ is a factor (and it pairs with itself).

Now $6 = \sqrt{36}$, so you can stop — anything beyond this point would just repeat the pairs in reverse. Collect all the numbers that appeared and sort them:

$$
1,\ 2,\ 3,\ 4,\ 6,\ 9,\ 12,\ 18,\ 36.
$$

There are nine factors in all. Notice how the pairs bracket the square root — $1$ with $36$, $2$ with $18$, $3$ with $12$, $4$ with $9$, and $6$ with itself.

### Example 2: prime factorization of $84$

Write $84$ as a product of primes.

Start with the smallest prime and work upward. Check $2$: $84$ is even, so $84 = 2 \cdot 42$. Is $42$ still even? Yes, so $42 = 2 \cdot 21$. That gives $84 = 2 \cdot 2 \cdot 21$. Next check $21$. It is odd, so $2$ is done. Try $3$: $2 + 1 = 3$, which is divisible by $3$, so $21 = 3 \cdot 7$. Now $7$ is prime, so the tree ends.

Collecting the circled primes:

$$
84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7.
$$

Multiply the primes back together as a check: $2 \cdot 2 = 4$, $4 \cdot 3 = 12$, $12 \cdot 7 = 84$. The factorization is verified.

A common mistake here is to stop too early. If you write $84 = 4 \cdot 21$ and call it a day, you have a factorization, but not a *prime* factorization — both $4$ and $21$ are composite. You must keep splitting until every branch is a prime.

### Example 3: prime factorization of $120$

Write $120$ as a product of primes.

$120$ is even, so take out $2$: $120 = 2 \cdot 60$. $60$ is still even: $60 = 2 \cdot 30$. Again: $30 = 2 \cdot 15$. Now $15$ is odd, so $2$ is done. Try $3$: $1 + 5 = 6$, divisible by $3$, so $15 = 3 \cdot 5$. $5$ is prime, and the tree ends.

Assemble the primes:

$$
120 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 5 = 2^3 \cdot 3 \cdot 5.
$$

Check: $2^3 = 8$, $8 \cdot 3 = 24$, $24 \cdot 5 = 120$. The prime factorization is correct.

You will see the same $2^3 \cdot 3 \cdot 5$ reappear in many places — reducing $\tfrac{120}{36}$ to lowest terms, finding the GCF of $120$ and something else, or computing an LCM — because the prime factorization is the piece of information those tasks all really depend on.

## Common pitfalls

- **Stopping the factor tree too early.** You must split every composite branch all the way down to primes. Leaving a $21$, a $9$, or a $4$ unfinished is the number-one error.
- **Confusing "factor" and "multiple."** A factor of $12$ is a number that divides it ($1, 2, 3, 4, 6, 12$). A multiple of $12$ is a number that $12$ divides ($12, 24, 36, 48, \ldots$). Factors sit below, multiples sit above.
- **Forgetting that $1$ is not prime.** Primes are whole numbers greater than $1$ whose only factors are $1$ and themselves. $1$ does not make the cut because it only has a single factor.
- **Missing a divisibility shortcut.** If you find yourself long-dividing $387$ by $3$, stop — the digit sum is $18$, which is divisible by $3$, and the rule is much faster than the division.
- **Not using exponents for repeated primes.** $2 \cdot 2 \cdot 2 \cdot 3 \cdot 5$ and $2^3 \cdot 3 \cdot 5$ are the same number, but the second is easier to read and to use later in GCF/LCM work. Get in the habit of compressing repeated primes.

## Problems Involving Divisibility, Factors, and Prime Factorization

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="divisibility_factors_and_prime_factorization"></div>

## See Also

- [[Greatest_Common_Factor_And_Least_Common_Multiple]]
- [[Equivalent_Fractions_And_Simplifying]]
- [[Adding_And_Subtracting_Fractions]]
- [[Order_Of_Operations]]
- [[Square_Roots_And_Cube_Roots]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
