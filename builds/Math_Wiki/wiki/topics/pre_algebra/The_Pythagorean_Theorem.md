---
title: "The Pythagorean Theorem"
type: topic
aliases: []
tags: ["#branch-pre-algebra", "#topic-right-triangles", "#key-formula", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/pre_algebra/Applications_Of_The_Pythagorean_Theorem"
  - "topics/pre_algebra/The_Distance_Formula"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Classifying_Triangles_And_Quadrilaterals"
  - "topics/pre_algebra/Square_Roots_And_Cube_Roots"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "In a right triangle, the square on the long side equals the sum of the squares on the two short sides."
---

> [[_overview|Home]] > [[Middle_School_Math|Middle School Math]] > The Pythagorean Theorem

# The Pythagorean Theorem

Lean a ladder against the wall. Stretch a tape measure diagonally across a TV screen. Draw a straight line from home plate to second base. In each of those situations there is a right angle hiding somewhere, and alongside it there is always a question of the form "how long is the slanted side?" The Pythagorean theorem is the one rule that answers all of them. It is the most famous result in elementary geometry, and its range of uses is astonishing: anything that involves a right angle, a distance, or a diagonal is probably a Pythagorean problem wearing a disguise.

## What it means

The theorem lives entirely inside **right triangles** — three-sided figures that contain a $90^{\circ}$ corner. In any right triangle, the two sides that meet at the right angle are called the **legs**, and the side across from the right angle — stretching between the two far ends of the legs — is called the **hypotenuse**. The hypotenuse is the one that leans. It is also, without exception, the longest of the three sides, since it faces the biggest angle.

Label the legs $a$ and $b$ and the hypotenuse $c$. The theorem says that the sum of the squares built on the two legs exactly matches the square built on the hypotenuse:

$$
a^2 + b^2 = c^2
$$

That single equation is the whole theorem. It tells you how the three side lengths of a right triangle are locked together. Know any two of them and you can solve for the third. The order of the legs on the left side of the equation does not matter — addition is commutative, so $a^2 + b^2$ is the same as $b^2 + a^2$ — but the hypotenuse always lives on the right side of the equals sign, because squaring the hypotenuse is the quantity that the two leg-squares add up to.

The relationship only works for right triangles. If the corner where the legs meet is not exactly $90^{\circ}$, the equation fails, and you need a more general tool. Pre-algebra worries only about the right-triangle case.

## How it works

Solving a triangle with the theorem usually fits into one of two patterns:

- **Finding the hypotenuse.** Square each leg, add the results, and take the square root. In symbols, $c = \sqrt{a^2 + b^2}$.
- **Finding a missing leg.** Rearrange the formula to isolate the unknown leg. If you know $b$ and $c$, then $a = \sqrt{c^2 - b^2}$. If you know $a$ and $c$, then $b = \sqrt{c^2 - a^2}$. The key move is the subtraction — you are peeling one leg-square out of the hypotenuse-square, not adding.

Notice that the final step in both patterns is the square root. Squaring gives you the area of the auxiliary square; taking the square root hands you back the side length you actually want. Forgetting the square root is the single most common error with this theorem — the most-often-seen wrong answer is "$c^2 = 169$" with no follow-up step, when the real answer is $c = 13$.

## Why it works

There are hundreds of proofs of the Pythagorean theorem, and most of them involve rearranging tiles. Imagine building a large square whose side length equals $a + b$. Slot four copies of your right triangle into the square so the hypotenuses form a tilted square in the middle. The tilted square's side length is $c$, so its area is $c^2$. The four triangles together have a fixed total area — and when you lay them out differently inside the same big square, you can instead expose two smaller squares of area $a^2$ and $b^2$. Both arrangements have to cover the same big square, so the tilted middle square must equal the two smaller squares combined. That equality is exactly $a^2 + b^2 = c^2$.

The deeper reason the theorem holds is that the right angle fits the two legs onto perpendicular axes. The hypotenuse crosses both axes at once, and its length ends up being a clean combination of how far it reaches in each direction. This same idea is what powers the [[The_Distance_Formula]] in coordinate geometry — that formula is just the Pythagorean theorem with coordinate labels.

## Worked examples

**Example 1.** A right triangle has legs measuring $9$ and $12$ units. How long is the hypotenuse?

Plug the leg values into the theorem:

$$
c^2 = 9^2 + 12^2 = 81 + 144 = 225
$$

Take the square root of both sides:

$$
c = \sqrt{225} = 15
$$

The hypotenuse is $15$ units long. This triangle is one of the **Pythagorean triples** — triangles whose three sides are all whole numbers. The $9$-$12$-$15$ triangle is really the $3$-$4$-$5$ triple scaled up by a factor of $3$, and once you spot the $3$-$4$-$5$ inside any right triangle the answer is almost automatic.

**Example 2.** A right triangle has hypotenuse $17$ and one leg $8$. What is the length of the other leg?

Now the unknown is a leg, not the hypotenuse, so you rearrange before you solve. Let the missing leg be $a$:

$$
a^2 + 8^2 = 17^2
$$

$$
a^2 + 64 = 289
$$

Subtract $64$ from both sides to isolate the square of the missing leg:

$$
a^2 = 289 - 64 = 225
$$

Then take the square root:

$$
a = \sqrt{225} = 15
$$

The missing leg measures $15$ units. This is another Pythagorean triple — the $8$-$15$-$17$ — and it is worth adding to your mental list alongside $3$-$4$-$5$ and $5$-$12$-$13$, because these triples show up constantly in problem sets.

**Example 3.** A carpenter is installing a $10$-foot ladder against the side of a garage to reach a second-story window. The base of the ladder is placed $4$ feet away from the garage wall. How high up the wall does the top of the ladder touch? Round your answer to one decimal place.

The ladder, the wall, and the ground form a right triangle. The right angle sits where the wall meets the ground. The ladder itself is the slanted side, so the ladder is the hypotenuse. The distance along the ground is one leg; the height on the wall is the other leg, and it is what you want to find. Call the height $h$:

$$
h^2 + 4^2 = 10^2
$$

$$
h^2 + 16 = 100
$$

$$
h^2 = 84
$$

The square root of $84$ is not a whole number. You can estimate by noting that $9^2 = 81$ and $10^2 = 100$, so $\sqrt{84}$ is a little bigger than $9$. A calculator (or a careful by-hand estimate) gives $\sqrt{84} \approx 9.165$, which rounds to $9.2$ feet. The top of the ladder touches the wall roughly $9.2$ feet above the ground. A sanity check: $9.2^2 + 4^2 \approx 84.6 + 16 = 100.6$, which is very close to the $10^2 = 100$ you started with. The small discrepancy is the rounding.

## Common pitfalls

- **Forgetting the square root.** The theorem gives you $c^2$, not $c$. Finishing at $c^2 = 225$ is an incomplete answer; the real answer is $c = 15$. Always perform the square root as the last step.
- **Putting the hypotenuse on the wrong side.** The hypotenuse is always the side that sits opposite the right angle, and always the longest side. It always occupies $c$ in the formula $a^2 + b^2 = c^2$. If you mistakenly square the hypotenuse into one of the leg slots, the arithmetic will not balance.
- **Using the theorem on a non-right triangle.** A triangle that does not have a $90^{\circ}$ corner cannot be solved with this formula. For those triangles, you need other tools (coming later in geometry).
- **Mixing up finding a leg versus finding the hypotenuse.** Finding the hypotenuse means adding the squared legs. Finding a missing leg means subtracting from the squared hypotenuse. Read the problem carefully — the wrong sign here produces a number that is way off.

## Problems Involving The Pythagorean Theorem

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="the_pythagorean_theorem"></div>

## See Also

- [[Applications_Of_The_Pythagorean_Theorem]]
- [[The_Distance_Formula]]
- [[Square_Roots_And_Cube_Roots]]
- [[Classifying_Triangles_And_Quadrilaterals]]
- [[Middle_School_Math|Middle School Math]]
- [[Topics_Overview]]
- [[_overview|Home]]
