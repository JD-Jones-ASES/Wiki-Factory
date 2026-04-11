---
title: "Set Notation and the Real Numbers"
type: topic
aliases: ["Interval Notation", "Real Number System"]
tags: ["#branch-algebra-2", "#topic-numbers-and-operations", "#representation-symbolic", "#key-topic", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Compound_Inequalities"
  - "topics/algebra/Absolute_Value_Inequalities"
  - "topics/algebra/The_Coordinate_Plane"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/pre_algebra/Integers_And_The_Number_Line"
  - "topics/pre_algebra/Irrational_Numbers_And_Real_Numbers"
  - "topics/algebra/Inequalities_And_Their_Graphs"
problem_type_ids: []
figures: []
summary: "Learn to describe collections of real numbers three ways — with set-builder phrases, with interval notation, and with a number-line sketch — and to recognize the nested number systems inside the reals."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Set Notation and the Real Numbers

# Set Notation and the Real Numbers

Algebra 2 is the first math course where you are often asked to describe **a whole collection of numbers** at once, rather than a single answer. You might need to say "every number between $-2$ and $5$, including $5$ but not $-2$," or "every real number that is at least $3$ units from the origin," or "the common solutions of two separate inequalities." There are three standard ways to write a collection like that — in plain English with a set-builder phrase, in compact interval-notation shorthand, or as a picture on a number line — and a fluent Algebra 2 student can switch between all three without losing information. This page teaches the translations, along with the vocabulary of the number systems these collections live in.

The topic has two layers. The first is **notation**: the symbols and conventions for naming a set. The second is **classification**: the nested hierarchy of number systems inside $\mathbb{R}$, the set of all real numbers. The first layer shows up on every test. The second layer gives you the background vocabulary to talk about what kind of number you are dealing with — integer, rational, irrational — which matters a lot when the problem asks you to reason about whether certain operations produce numbers of a given type.

## What it means

A **set** is a collection of objects, called its **elements**. In algebra the elements are almost always numbers, but in principle a set could contain anything. Sets are usually named with capital letters. Two sets are considered the same if and only if they contain exactly the same elements, and the order in which you list elements does not matter: $\{1, 2, 3\}$ and $\{3, 1, 2\}$ name the same set.

There are three common ways to describe a set of numbers.

**Roster notation** lists the elements inside curly braces: $\{1, 2, 3, 4, 5\}$. This is great for small finite sets, but it breaks down for infinite ones.

**Set-builder notation** describes a set by a property. The shape is $\{x : P(x)\}$ or $\{x \mid P(x)\}$, read aloud as "the set of all $x$ such that $P(x)$ is true." The colon or the vertical bar both mean "such that." For example, $\{x : x \text{ is a real number and } -2 < x < 5\}$ is the collection of every real number strictly between $-2$ and $5$. Some books abbreviate the "$x$ is a real number" part as $x \in \mathbb{R}$.

**Interval notation** is a compact shorthand for a set of real numbers described by an inequality. It uses square brackets to include an endpoint and parentheses to exclude one. Here is the full lineup for a pair of real numbers $a < b$:

- $[a, b]$ — every real $x$ with $a \le x \le b$ (both endpoints included).
- $(a, b)$ — every real $x$ with $a < x < b$ (both endpoints excluded).
- $[a, b)$ — every real $x$ with $a \le x < b$ (left included, right excluded).
- $(a, b]$ — every real $x$ with $a < x \le b$ (left excluded, right included).
- $[a, \infty)$ — every real $x$ with $x \ge a$ (left included, goes on forever to the right).
- $(-\infty, b]$ — every real $x$ with $x \le b$ (right included, goes on forever to the left).
- $(-\infty, \infty)$ — every real number (the whole real line).

The infinity symbol $\infty$ is **always** paired with a parenthesis, never a bracket. Infinity is not a real number — it is a placeholder saying "keep going in that direction without stopping" — so you cannot "include" it. Writing $[3, \infty]$ is incorrect; the right form is $[3, \infty)$.

**Union and intersection** are the two operations that combine sets. The **union** $A \cup B$ contains every element that is in $A$, in $B$, or in both. The **intersection** $A \cap B$ contains only the elements that belong to both $A$ and $B$ at once. A quick visual: the union is "everything that shows up in either circle of a Venn diagram," and the intersection is "only the overlap in the middle." In interval notation, $(-\infty, -2] \cup [3, \infty)$ is the set of every real number that is either at most $-2$ or at least $3$, which is exactly the kind of solution set a [[Polynomial_Inequalities|polynomial inequality]] often produces.

### The nested number systems

Inside $\mathbb{R}$, there is a hierarchy of smaller and smaller sets, each contained in the next. The standard names and symbols:

- $\mathbb{N}$ — the **natural numbers**, or counting numbers. In most American textbooks, $\mathbb{N} = \{1, 2, 3, 4, \ldots\}$. A few books also include $0$; this wiki uses the $1$-and-up convention unless otherwise noted.
- $\mathbb{Z}$ — the **integers**, $\{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$. The letter $\mathbb{Z}$ comes from the German *Zahlen*, meaning "numbers."
- $\mathbb{Q}$ — the **rational numbers**: every number that can be expressed as a ratio $\tfrac{p}{q}$ where $p$ and $q$ are integers and $q \ne 0$. In decimal form, rationals are exactly the numbers whose decimal expansions either terminate (like $0.5$) or eventually repeat (like $0.333\ldots$).
- $\mathbb{I}$ — the **irrationals**, the real numbers that cannot be expressed as such a ratio. Their decimal expansions never terminate and never repeat. Familiar examples include $\sqrt{2}$, $\pi$, and $e$.
- $\mathbb{R}$ — the **real numbers**, the union of $\mathbb{Q}$ and $\mathbb{I}$: written compactly, $\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$. Geometrically, you can think of $\mathbb{R}$ as a perfect match with the number line — each tick or point on that line picks out one real number, and going the other direction, each real value lands at one spot on the line.

Stacking those up gives the containment chain

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}
$$

Each layer of that chain sits inside the next: the counting numbers are a subset of the signed whole numbers, those are a subset of fractions (any whole $n$ is just $n/1$), and fractions are a subset of the reals. The irrationals $\mathbb{I}$ sit alongside $\mathbb{Q}$ inside $\mathbb{R}$ without overlap — any real value is either rational or irrational but never both. The symbol $\subset$ means "is a subset of," and it is what formalizes the idea of one set fitting inside another.

## How it works

When a problem gives you a description of a set of real numbers in one form and asks for another, the translation is mechanical once you get the hang of it.

1. **Identify the endpoints and whether each one is included.** Words like "at least," "at most," "no greater than," "including," or the symbols $\le$ and $\ge$ mean the endpoint is included. Words like "greater than," "less than," "strictly," "excluding," or the symbols $<$ and $>$ mean the endpoint is excluded. "All real numbers greater than $-2$ and no larger than $5$" has $-2$ excluded and $5$ included.
2. **Write the set-builder version.** Start with $\{x : \ldots\}$ and put the inequality (or compound inequality) that describes the property inside. The example becomes $\{x : -2 < x \le 5\}$.
3. **Convert to interval notation.** Use a square bracket on any endpoint that is included and a parenthesis on any endpoint that is excluded. The example becomes $(-2, 5]$.
4. **Sketch the number line.** Draw a line, mark each endpoint, shade the included region between them, and use a closed dot (solid circle) on an included endpoint and an open dot on an excluded endpoint. For the example, you would draw an open dot at $-2$, a closed dot at $5$, and a shaded segment joining them.
5. **Check the translation.** Pick a number and test it in all three representations. If your test point is in the shaded region on the number line, it should satisfy the set-builder inequality and should fall inside the interval. If any of the three disagrees, you have a translation bug.

## Why it works

All three notations — set-builder, interval, number-line picture — are just different costumes for the same underlying object: a set of real numbers. Set-builder is the most flexible and the most verbose; you can describe extremely intricate properties with it (for example, $\{x \in \mathbb{R} : x^2 + 1 \le 5\}$). Interval notation is a compact shorthand that only works when the set is a union of intervals, but when it does apply it is by far the fastest to read and write. The number-line sketch is a visual aid that makes unions and intersections obvious — you can literally see whether two intervals overlap or not. Each notation has a job. The reason you learn all three is that textbooks, tests, and real-world math use different notations interchangeably, and fluency means being able to switch without losing information. The nested chain $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ is the bookkeeping that lets you talk about **which** kind of real number you are dealing with, which matters any time a problem restricts to integer solutions, rational solutions, or counting-number solutions.

## Worked examples

### Example 1

Express the phrase "every real number strictly between $-2$ and $5$" in set-builder notation and in interval notation, and describe the number-line picture.

"Strictly between" means both endpoints are excluded. In set-builder notation:

$$
\{x : -2 < x < 5\}
$$

In interval notation, both endpoints get parentheses:

$$
(-2, 5)
$$

The number-line picture has an open dot at $-2$, an open dot at $5$, and a shaded segment joining the two. Quick check: $0$ is strictly between $-2$ and $5$, so $0$ should be in the set. Substituting, $-2 < 0 < 5$ is true, $0$ is inside the shaded segment, and $0 \in (-2, 5)$. All three representations agree.

### Example 2

Rohan is describing the set of all real numbers that are at most $-2$ or at least $3$. Express this set in interval notation.

"At most $-2$" means $x \le -2$, which includes the endpoint $-2$ — so the interval is $(-\infty, -2]$. "At least $3$" means $x \ge 3$, which includes the endpoint $3$ — so the interval is $[3, \infty)$. The word "or" means union. Combine:

$$
(-\infty, -2] \cup [3, \infty)
$$

Both finite endpoints get square brackets because both are included; both infinities get parentheses, as always. Testing a value from each piece: $-5$ is in $(-\infty, -2]$ because $-5 \le -2$, and $10$ is in $[3, \infty)$ because $10 \ge 3$. Testing a value from the gap: $0$ is not in either piece, because $0$ is greater than $-2$ (so not in the left piece) and less than $3$ (so not in the right piece).

### Example 3

Zoe has two intervals: $A = [-1, 4)$ and $B = (2, 6]$. Determine $A \cup B$ and $A \cap B$, and classify the endpoint behavior of each.

For the **union** $A \cup B$, ask what it means for a number $x$ to belong to at least one of the two sets. If $x$ lives in $A$, it satisfies $-1 \le x < 4$. If $x$ lives in $B$, it satisfies $2 < x \le 6$. Taking the "or," the combined condition is $-1 \le x \le 6$, because every number in that sweep is covered by at least one of the two intervals. (The overlap around $x = 3$ is covered by both, which is fine for a union.) In interval notation:

$$
A \cup B = [-1, 6]
$$

Note the brackets on both ends — $-1$ is included because it is in $A$, and $6$ is included because it is in $B$.

For the **intersection** $A \cap B$, ask what it means for $x$ to belong to **both** sets at once. The first condition gives $-1 \le x < 4$ and the second gives $2 < x \le 6$. The overlap is the tighter requirement on each side: $2 < x < 4$. In interval notation:

$$
A \cap B = (2, 4)
$$

Both endpoints are open here. The left endpoint $2$ is open because $B$ excludes it (from $(2, 6]$), and the right endpoint $4$ is open because $A$ excludes it (from $[-1, 4)$). Quick check: $3$ is in both sets (it satisfies $-1 \le 3 < 4$ and $2 < 3 \le 6$), so $3$ should be in the intersection, and indeed $3 \in (2, 4)$. And $5$ is in $B$ but not in $A$, so it should be in the union but not in the intersection. Testing: $5 \in [-1, 6]$? Yes. $5 \in (2, 4)$? No. Both answers are consistent.

## Common pitfalls

- **Pairing infinity with a bracket.** Infinity is not a real number — it never "lives" at a specific point on the number line — so it can never be an included endpoint. Always write $[3, \infty)$ or $(-\infty, 3]$, never $[3, \infty]$ or $[-\infty, 3]$.
- **Confusing parentheses for open intervals with parentheses for ordered pairs.** The notation $(2, 5)$ can mean either the open interval from $2$ to $5$ **or** the point $(2, 5)$ in the coordinate plane, depending on context. Usually the rest of the sentence tells you which — if the problem talks about "the set of $x$ such that," you are in interval-land. If it talks about "the point" or uses $(x, y)$, you are in coordinate-land.
- **Using the wrong dot on a number line.** A closed (filled-in) dot means the endpoint is included, matching a square bracket. An open (hollow) dot means the endpoint is excluded, matching a parenthesis. Mixing these up is the most common number-line mistake.
- **Forgetting that $\le$ and $\ge$ include the boundary.** When translating "at most $5$" or "no larger than $5$," the number $5$ itself is part of the set, and the interval needs a closed bracket on the right. "Strictly less than $5$" is a different condition and needs a parenthesis.
- **Mistaking union for intersection.** The union $A \cup B$ is larger (or at least no smaller) than either $A$ or $B$, because it combines everything. The intersection $A \cap B$ is smaller (or at least no larger) than either, because it only keeps the overlap. When you see "or" in a description, reach for union; when you see "and," reach for intersection.
- **Mixing up the number-system symbols.** $\mathbb{N}$ is the naturals, $\mathbb{Z}$ is the integers, $\mathbb{Q}$ is the rationals, and $\mathbb{R}$ is the reals. The common swap is $\mathbb{Z}$ and $\mathbb{Q}$ — some students remember "$\mathbb{Z}$ for integers" by thinking of the German *Zahlen*, and "$\mathbb{Q}$ for quotient," which is a handy mnemonic.

## Problems Involving Set Notation and the Real Numbers

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="set_notation_and_the_real_numbers"></div>

## See Also

- [[Integers_And_The_Number_Line]]
- [[Irrational_Numbers_And_Real_Numbers]]
- [[Inequalities_And_Their_Graphs]]
- [[Compound_Inequalities]]
- [[Absolute_Value_Inequalities]]
- [[The_Coordinate_Plane]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
