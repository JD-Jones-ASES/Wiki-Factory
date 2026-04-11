"""Number-theory generators for factors, primes, and divisibility.

Two canonical topic slugs covered here:

- ``divisibility_factors_and_prime_factorization`` at
  wiki/topics/pre_algebra/Divisibility_Factors_And_Prime_Factorization.md

  Generators:
    * list_all_factors        --- list every positive factor of n
    * prime_factorization     --- n as a product of prime powers
    * divisibility_rule_apply --- is n divisible by d? (clean rule)

- ``greatest_common_factor_and_least_common_multiple`` at
  wiki/topics/pre_algebra/Greatest_Common_Factor_And_Least_Common_Multiple.md

  Generators:
    * gcf_of_two_integers  --- GCF(a, b)
    * lcm_of_two_integers  --- LCM(a, b)
    * gcf_lcm_both         --- return both GCF and LCM of a pair
"""
from __future__ import annotations

import random
from math import gcd

from ..base import Difficulty, Generator, Problem, make_problem_id, register


_TAGS_BASE = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-procedural-calculation",
]


def _tags(difficulty: Difficulty) -> list[str]:
    return [*_TAGS_BASE, f"#difficulty-{difficulty}"]


def _lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


def _all_factors(n: int) -> list[int]:
    """Return the sorted list of positive factors of n (n > 0)."""
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
        i += 1
    return sorted(out)


def _prime_factorization(n: int) -> list[tuple[int, int]]:
    """Return the prime factorization of n as a list of (prime, exponent)."""
    out = []
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            out.append((d, e))
        d += 1
    if x > 1:
        out.append((x, 1))
    return out


def _format_prime_factorization(pe: list[tuple[int, int]]) -> str:
    """Render a prime factorization as LaTeX: '2^{2} \\cdot 3 \\cdot 5'."""
    parts = []
    for p, e in pe:
        if e == 1:
            parts.append(str(p))
        else:
            parts.append(f"{p}^{{{e}}}")
    return r" \cdot ".join(parts)


# ---------------------------------------------------------------------------
# Topic 1: divisibility_factors_and_prime_factorization
# ---------------------------------------------------------------------------


@register
class ListAllFactors(Generator):
    """List every positive factor of n.

    Parameter space is small (n up to 150), so cap the per-difficulty bank.
    """

    generator_id = "list_all_factors"
    topic_slug = "divisibility_factors_and_prime_factorization"
    display_name = "List all positive factors of a number"

    bank_count_per_difficulty = 15

    _RANGES = {
        "easy":   (6, 30),
        "medium": (20, 80),
        "hard":   (40, 150),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        # Prefer composites with >= 4 factors so the problem is non-trivial.
        n = rng.randint(lo, hi)
        factors = _all_factors(n)
        attempts = 0
        while len(factors) < 4 and attempts < 25:
            n = rng.randint(lo, hi)
            factors = _all_factors(n)
            attempts += 1

        factor_str = ", ".join(str(f) for f in factors)

        statement = f"Determine all positive factors of ${n}$."
        answer = f"${factor_str}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (n,),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                r"Test every whole number from $1$ up to $\sqrt{n}$. Whenever $d$ divides $n$, both $d$ and $n / d$ are factors.",
                f"Stop testing once you pass $\\sqrt{{{n}}}$; any divisor above it is already paired with a smaller one.",
                f"You should find ${len(factors)}$ factors in total.",
            ],
            solution_steps_latex=[
                f"Start by checking each integer from $1$ to $\\sqrt{{{n}}}$.",
                f"For each divisor $d$ you find, record both $d$ and ${n} / d$.",
                f"Sort the pairs: the factors of ${n}$ are ${factor_str}$.",
            ],
            tags=_tags(difficulty),
        )


@register
class PrimeFactorization(Generator):
    """Compute the prime factorization of n, written using exponents.

    Backward: choose the prime factorization (pool of small primes with
    small exponents), compute n.
    """

    generator_id = "prime_factorization"
    topic_slug = "divisibility_factors_and_prime_factorization"
    display_name = "Compute the prime factorization of n"

    bank_count_per_difficulty = 20

    # Each difficulty has a pool of base prime-factorization templates.
    # A template is a list of (prime, exponent) tuples.
    _TEMPLATES = {
        "easy": (
            [(2, 2), (3, 1)],        # 12
            [(2, 1), (3, 2)],        # 18
            [(2, 3), (3, 1)],        # 24
            [(2, 1), (3, 1), (5, 1)],# 30
            [(2, 2), (5, 1)],        # 20
            [(2, 2), (3, 2)],        # 36
            [(2, 1), (5, 1), (7, 1)],# 70
            [(3, 1), (5, 1), (7, 1)],# 105
            [(2, 3), (5, 1)],        # 40
            [(2, 2), (3, 1), (5, 1)],# 60
        ),
        "medium": (
            [(2, 4), (3, 1)],        # 48
            [(2, 1), (3, 3)],        # 54
            [(2, 3), (3, 2)],        # 72
            [(2, 1), (3, 2), (5, 1)],# 90
            [(2, 2), (3, 2), (5, 1)],# 180
            [(2, 3), (3, 1), (5, 1)],# 120
            [(2, 4), (5, 1)],        # 80
            [(2, 2), (3, 1), (7, 1)],# 84
            [(2, 1), (3, 1), (11, 1)],#66
            [(3, 2), (5, 1), (7, 1)],# 315
            [(2, 2), (11, 1)],       # 44
            [(2, 2), (3, 3)],        # 108
        ),
        "hard": (
            [(2, 5), (3, 1)],         # 96
            [(2, 1), (3, 4)],         # 162
            [(2, 3), (3, 3)],         # 216
            [(2, 2), (3, 1), (5, 1), (7, 1)],  # 420
            [(2, 4), (3, 2)],         # 144
            [(2, 1), (3, 2), (7, 1)], # 126
            [(2, 3), (5, 1), (7, 1)], # 280
            [(2, 2), (3, 2), (5, 1), (7, 1)],  # 1260
            [(2, 5), (3, 2)],         # 288
            [(2, 1), (5, 2), (7, 1)], # 350
            [(3, 1), (5, 1), (11, 1)],# 165
            [(2, 4), (3, 1), (5, 1)], # 240
        ),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        tpl = list(rng.choice(self._TEMPLATES[difficulty]))
        n = 1
        for p, e in tpl:
            n *= p ** e

        answer_latex = _format_prime_factorization(tpl)

        statement = f"Give the prime factorization of ${n}$."
        answer = f"${answer_latex}$"

        # Build a simple worked decomposition (factor tree narration).
        steps_lines = [f"Start with ${n}$."]
        running = n
        for p, e in tpl:
            for _ in range(e):
                nxt = running // p
                if nxt == 1:
                    steps_lines.append(f"Divide by ${p}$: ${running} \\div {p} = {nxt}$ (all primes found).")
                else:
                    steps_lines.append(f"Divide by ${p}$: ${running} \\div {p} = {nxt}$.")
                running = nxt
        steps_lines.append(f"Collect the prime factors: ${answer_latex}$.")

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty,
                tuple((p, e) for p, e in tpl),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                r"Start with the smallest prime that divides the number, then repeat on the quotient.",
                r"The primes to try in order are $2, 3, 5, 7, 11, \dots$",
                f"Collect the primes (with exponents for repeats) to get ${answer_latex}$.",
            ],
            solution_steps_latex=steps_lines,
            tags=_tags(difficulty),
        )


@register
class DivisibilityRuleApply(Generator):
    """Apply a clean divisibility rule: is n divisible by d?

    Backward: choose a yes/no outcome first, then build n accordingly.
    Divisors supported: 2, 3, 5, 6, 9, 10.
    """

    generator_id = "divisibility_rule_apply"
    topic_slug = "divisibility_factors_and_prime_factorization"
    display_name = "Apply a divisibility rule"

    bank_count_per_difficulty = 25

    _RANGES = {
        "easy":   (20, 200),
        "medium": (100, 900),
        "hard":   (500, 5000),
    }
    _DIVISORS = (2, 3, 5, 6, 9, 10)

    _RULE_TEXT = {
        2:  r"A number is divisible by $2$ if its last digit is even ($0, 2, 4, 6, 8$).",
        3:  r"A number is divisible by $3$ if the sum of its digits is divisible by $3$.",
        5:  r"A number is divisible by $5$ if its last digit is $0$ or $5$.",
        6:  r"A number is divisible by $6$ if it is divisible by both $2$ and $3$.",
        9:  r"A number is divisible by $9$ if the sum of its digits is divisible by $9$.",
        10: r"A number is divisible by $10$ if its last digit is $0$.",
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._RANGES[difficulty]
        d = rng.choice(self._DIVISORS)
        is_yes = rng.random() < 0.5

        if is_yes:
            # Pick a multiple of d in range.
            start_q = (lo + d - 1) // d
            end_q = hi // d
            q = rng.randint(start_q, end_q)
            n = d * q
        else:
            # Pick n not divisible by d.
            n = rng.randint(lo, hi)
            while n % d == 0:
                n = rng.randint(lo, hi)

        verdict = "yes" if n % d == 0 else "no"
        quotient = n // d if verdict == "yes" else None

        rule = self._RULE_TEXT[d]

        statement = f"Is ${n}$ divisible by ${d}$?"
        answer = f"$\\text{{{verdict}}}$"

        # Craft concrete reasoning per-divisor
        reasoning_lines: list[str] = []
        if d in (2, 5, 10):
            last_digit = n % 10
            reasoning_lines.append(f"The last digit of ${n}$ is ${last_digit}$.")
            if d == 2:
                reasoning_lines.append(
                    f"${last_digit}$ is {'even' if last_digit % 2 == 0 else 'odd'}, "
                    f"so ${n}$ is {'divisible' if last_digit % 2 == 0 else 'not divisible'} by $2$."
                )
            elif d == 5:
                ok = last_digit in (0, 5)
                reasoning_lines.append(
                    f"${last_digit}$ is {'either $0$ or $5$' if ok else 'neither $0$ nor $5$'}, "
                    f"so ${n}$ is {'divisible' if ok else 'not divisible'} by $5$."
                )
            else:  # d == 10
                ok = last_digit == 0
                reasoning_lines.append(
                    f"${last_digit}$ is {'$0$' if ok else 'not $0$'}, "
                    f"so ${n}$ is {'divisible' if ok else 'not divisible'} by $10$."
                )
        elif d in (3, 9):
            digit_sum = sum(int(ch) for ch in str(n))
            reasoning_lines.append(f"The digits of ${n}$ sum to ${digit_sum}$.")
            divisible = digit_sum % d == 0
            reasoning_lines.append(
                f"${digit_sum}$ is {'divisible' if divisible else 'not divisible'} by ${d}$, "
                f"so ${n}$ is {'divisible' if divisible else 'not divisible'} by ${d}$."
            )
        else:  # d == 6
            last_digit = n % 10
            even = last_digit % 2 == 0
            digit_sum = sum(int(ch) for ch in str(n))
            by_3 = digit_sum % 3 == 0
            reasoning_lines.append(
                f"Check divisibility by $2$: the last digit is ${last_digit}$, "
                f"which is {'even' if even else 'odd'}."
            )
            reasoning_lines.append(
                f"Check divisibility by $3$: the digit sum is ${digit_sum}$, "
                f"which is {'divisible' if by_3 else 'not divisible'} by $3$."
            )
            if even and by_3:
                reasoning_lines.append(f"Both tests pass, so ${n}$ is divisible by $6$.")
            else:
                reasoning_lines.append(f"At least one test fails, so ${n}$ is not divisible by $6$.")

        if verdict == "yes":
            final_step = f"Confirming: ${n} \\div {d} = {quotient}$ exactly. Answer: yes."
        else:
            final_step = f"The rule fails, so ${n}$ is not divisible by ${d}$. Answer: no."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (n, d),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                rule,
                "Apply the rule step by step using the digits of the number.",
                f"Answer: {verdict}.",
            ],
            solution_steps_latex=[
                f"Recall the rule: {rule}",
                *reasoning_lines,
                final_step,
            ],
            tags=_tags(difficulty),
        )


# ---------------------------------------------------------------------------
# Topic 2: greatest_common_factor_and_least_common_multiple
# ---------------------------------------------------------------------------


def _coprime(p: int, q: int) -> bool:
    return gcd(p, q) == 1


@register
class GcfOfTwoIntegers(Generator):
    """Find GCF(a, b). Backward: pick g and coprime multipliers p, q."""

    generator_id = "gcf_of_two_integers"
    topic_slug = "greatest_common_factor_and_least_common_multiple"
    display_name = "Find the GCF of two integers"

    _RANGES = {
        "easy":   {"g": (2, 6),  "pq": (2, 8)},
        "medium": {"g": (2, 12), "pq": (2, 12)},
        "hard":   {"g": (3, 18), "pq": (2, 15)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        g = rng.randint(*r["g"])
        p = rng.randint(*r["pq"])
        q = rng.randint(*r["pq"])
        # Ensure distinct coprime multipliers.
        attempts = 0
        while (p == q or not _coprime(p, q)) and attempts < 30:
            p = rng.randint(*r["pq"])
            q = rng.randint(*r["pq"])
            attempts += 1
        # Guarantee by swapping small neighbors if needed.
        if p == q or not _coprime(p, q):
            p, q = 2, 3
        a = g * p
        b = g * q

        opener = rng.choice([
            "Find the greatest common factor of",
            "Determine the GCF of",
            "Compute the greatest common factor of",
        ])
        statement = f"{opener} ${a}$ and ${b}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (g, p, q),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${g}$",
            hints=[
                r"The greatest common factor (GCF) is the largest integer that divides both numbers.",
                f"Write each number as a product: ${a} = {g} \\cdot {p}$ and ${b} = {g} \\cdot {q}$.",
                f"Since ${p}$ and ${q}$ share no common factor other than $1$, the GCF is ${g}$.",
            ],
            solution_steps_latex=[
                f"List the factor structure: ${a} = {g} \\cdot {p}$ and ${b} = {g} \\cdot {q}$.",
                f"The common factor is ${g}$; the leftover parts ${p}$ and ${q}$ are coprime.",
                f"Therefore $\\gcd({a}, {b}) = {g}$.",
            ],
            tags=_tags(difficulty),
        )


@register
class LcmOfTwoIntegers(Generator):
    """Find LCM(a, b).

    Backward: pick the target LCM L, choose two divisors a, b of L whose
    LCM is exactly L. We use a = L/p and b = L/q where p, q are coprime
    and each divides L.
    """

    generator_id = "lcm_of_two_integers"
    topic_slug = "greatest_common_factor_and_least_common_multiple"
    display_name = "Find the LCM of two integers"

    # L is constructed to have lots of small prime-power divisors.
    _L_POOL = {
        "easy":   (12, 18, 20, 24, 30, 36, 40, 48),
        "medium": (36, 48, 60, 72, 84, 90, 120, 144, 180),
        "hard":   (120, 144, 180, 210, 240, 300, 360, 420, 480, 540, 600),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        L = rng.choice(self._L_POOL[difficulty])
        divisors = [d for d in _all_factors(L) if 1 < d < L]
        # Try to pick (a, b) such that LCM(a, b) == L.
        found = None
        attempts = 0
        while attempts < 50 and found is None:
            a = rng.choice(divisors)
            b = rng.choice([d for d in divisors if d != a])
            if _lcm(a, b) == L:
                found = (a, b)
            attempts += 1
        if found is None:
            # Fallback: a = L, b = a small divisor. LCM is L trivially.
            a = L
            b = rng.choice(divisors) if divisors else 1
        else:
            a, b = found
        # Randomize order.
        if rng.random() < 0.5:
            a, b = b, a

        g = gcd(a, b)

        opener = rng.choice([
            "Find the least common multiple of",
            "Determine the LCM of",
            "Compute the least common multiple of",
        ])
        statement = f"{opener} ${a}$ and ${b}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (L, a, b),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"${L}$",
            hints=[
                r"The least common multiple (LCM) is the smallest positive integer that both numbers divide into evenly.",
                f"One shortcut: $\\text{{lcm}}(a, b) = \\dfrac{{a \\cdot b}}{{\\gcd(a, b)}}$. "
                f"Here $\\gcd({a}, {b}) = {g}$.",
                f"So $\\dfrac{{{a} \\cdot {b}}}{{{g}}} = \\dfrac{{{a * b}}}{{{g}}} = {L}$.",
            ],
            solution_steps_latex=[
                f"Compute $\\gcd({a}, {b}) = {g}$.",
                f"Apply the formula $\\text{{lcm}}(a, b) = \\dfrac{{a \\cdot b}}{{\\gcd(a, b)}}$: $\\dfrac{{{a} \\cdot {b}}}{{{g}}}$.",
                f"Simplify: $\\dfrac{{{a * b}}}{{{g}}} = {L}$.",
            ],
            tags=_tags(difficulty),
        )


@register
class GcfLcmBoth(Generator):
    """Return both GCF and LCM of a pair.

    Backward: pick the GCF g and two coprime multipliers p, q; derive
    a = g*p, b = g*q. Then GCF = g and LCM = g*p*q.
    """

    generator_id = "gcf_lcm_both"
    topic_slug = "greatest_common_factor_and_least_common_multiple"
    display_name = "Find both the GCF and LCM"

    _RANGES = {
        "easy":   {"g": (2, 6),  "pq": (2, 7)},
        "medium": {"g": (2, 10), "pq": (2, 9)},
        "hard":   {"g": (3, 15), "pq": (2, 12)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        g = rng.randint(*r["g"])
        p = rng.randint(*r["pq"])
        q = rng.randint(*r["pq"])
        attempts = 0
        while (p == q or not _coprime(p, q)) and attempts < 30:
            p = rng.randint(*r["pq"])
            q = rng.randint(*r["pq"])
            attempts += 1
        if p == q or not _coprime(p, q):
            p, q = 2, 3
        a = g * p
        b = g * q
        L = g * p * q

        opener = rng.choice([
            "Find the GCF and LCM of",
            "Compute the GCF and LCM of",
            "Determine both the GCF and the LCM of",
        ])
        statement = f"{opener} ${a}$ and ${b}$."

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (g, p, q),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=f"$\\text{{GCF}} = {g}$, $\\text{{LCM}} = {L}$",
            hints=[
                r"First find the GCF by pulling out the largest common factor; the LCM equals the product divided by the GCF.",
                f"Since ${a} = {g} \\cdot {p}$ and ${b} = {g} \\cdot {q}$, the GCF is ${g}$.",
                f"The LCM is $\\dfrac{{{a} \\cdot {b}}}{{{g}}} = {L}$.",
            ],
            solution_steps_latex=[
                f"Factor each number around the common piece: ${a} = {g} \\cdot {p}$, ${b} = {g} \\cdot {q}$.",
                f"Because $\\gcd({p}, {q}) = 1$, the greatest common factor is $\\gcd({a}, {b}) = {g}$.",
                f"Apply $\\text{{lcm}}(a, b) = \\dfrac{{a \\cdot b}}{{\\gcd(a, b)}} = \\dfrac{{{a * b}}}{{{g}}} = {L}$.",
                f"So $\\text{{GCF}} = {g}$ and $\\text{{LCM}} = {L}$.",
            ],
            tags=_tags(difficulty),
        )
