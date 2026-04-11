---
title: "Equations with Variables on Both Sides"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/Solving_Equations_In_One_Variable"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
  - "topics/algebra/Literal_Equations_And_Formulas"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/Multi_Step_Equations"
  - "topics/pre_algebra/Solving_Two_Step_Equations"
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
problem_type_ids: []
figures: []
summary: "When a variable lives on both sides of an equation, collect all the variable terms onto one side first, then finish it off with the standard multi-step procedure."
---

> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Equations with Variables on Both Sides

# Equations with Variables on Both Sides

Up to this point, nearly every equation you have solved has had the variable on one side and a pile of numbers on the other. Something like $3x + 5 = 20$ is friendly because the $x$ has a clear home — the left side — and you only have to peel constants away from it to get to an answer. But real equations rarely sort themselves that neatly. In expressions that come out of geometry problems, cost comparisons, and mixture setups, the variable often shows up on **both** sides at once. The equation looks more like $2x + 5 = x + 11$, and a natural question forms: which side do you "work from"?

The answer is that you get to choose, and once you have chosen, you work the problem exactly like any multi-step equation you already know. The one new move is collecting variable terms onto a single side before you start peeling numbers away.

## What changes when variables live on both sides

In a one-sided equation like $3x + 5 = 20$, every tool from [[Multi_Step_Equations]] works without modification: subtract the constant, divide by the coefficient, done. But in an equation like

$$
2x + 5 = x + 11,
$$

there is a value of $x$ hiding on the right side that has to be handled before the left side can be simplified. If you try to go straight at the $2x + 5$ and subtract $5$, you end up with $2x = x + 6$, which is a little better but not yet solvable in one step — there is still an $x$ on each side. The honest fix is to first move every variable term to a single side, then do the rest of the problem the way you always have.

## The procedure

Here is the whole method for any linear equation with variables on both sides.

1. **Expand anything inside parentheses.** If either side contains an expression like $3(x - 4)$, run the distributive property to open it up. This comes from [[The_Distributive_Property_With_Variables]].
2. **Simplify each side on its own.** Combine numerical pieces and variable pieces that are already on the same side.
3. **Collect variable terms on one side.** Pick the side that already has the larger coefficient on the variable, and use subtraction to remove the variable from the other side. Choosing the larger coefficient keeps the result positive, which cuts down on sign mistakes later.
4. **Collect constants on the other side.** Use addition or subtraction to push every number away from the variable.
5. **Divide by the coefficient.** Whatever number is multiplying the variable gets undone by division.
6. **Check the answer.** Plug the result back into the *original* equation and confirm that both sides are equal.

Step 3 is the new move. Steps 1, 2, 4, 5, and 6 are the same machinery you used in [[Multi_Step_Equations]].

## Why it works

The equal sign in an equation says "these two expressions always stand for the same number." As long as you change both sides in exactly the same way, the equation continues to stand for a true relationship — that is, you keep the equation balanced. So when you remove a variable term from the right side, you have to remove that same variable term from the left side too. The variable disappears from one side only because the two copies cancel, not because you made a copy vanish. After that cancellation, the equation is a one-sided multi-step equation again, and you can finish it with the usual tools.

A second reason the method works: the variable $x$ is a number. It might be $3$ or $-7$ or $\tfrac{1}{2}$, but whatever it is, it is a single number that obeys all the usual rules of arithmetic. If you treat $x$ like a number, you are allowed to add $x$ to both sides, subtract it from both sides, and so on. The "variable move" in step 3 is really just one more application of the same balance principle you have been using all along.

## Worked examples

### Example 1

Determine the value of $x$ that makes the equation $3x + 4 = x + 10$ true.

The variable sits on both sides: a $3x$ on the left and a smaller $x$ on the right. Since the larger coefficient is on the left, collect the $x$'s there by removing the $x$ from the right. Do this by subtracting $x$ from each side:

$$
3x + 4 - x = x + 10 - x
$$

$$
2x + 4 = 10.
$$

Now the equation is a familiar two-step equation. Remove the $4$ from the left by subtracting it from both sides:

$$
2x = 6.
$$

Finally divide by $2$:

$$
x = 3.
$$

Verification in the original: $3(3) + 4 = 9 + 4 = 13$ on the left, and $3 + 10 = 13$ on the right. Both sides read $13$, so $x = 3$ is correct.

### Example 2

Find all $x$ for which $5x - 7 = 2x + 8$.

Both sides carry a positive variable term, but the left has the larger coefficient ($5$ versus $2$), so collect the variable on the left. Subtract $2x$ from both sides:

$$
5x - 7 - 2x = 2x + 8 - 2x
$$

$$
3x - 7 = 8.
$$

Now push the constant away from the $x$ by adding $7$ to each side:

$$
3x = 15.
$$

Divide by $3$:

$$
x = 5.
$$

Verification: the left side becomes $5(5) - 7 = 25 - 7 = 18$, and the right side becomes $2(5) + 8 = 10 + 8 = 18$. The two sides match, so $x = 5$ is the solution.

### Example 3

Maya is working on the equation

$$
4(x - 2) = 2x + 6.
$$

What is the value of $x$?

The left side hides parentheses, so step 1 is to distribute the $4$ through $(x - 2)$:

$$
4 \cdot x - 4 \cdot 2 = 2x + 6
$$

$$
4x - 8 = 2x + 6.
$$

Now both sides are in simplest form and the equation looks like the earlier examples. The larger coefficient on the variable is on the left ($4$ versus $2$), so collect the variable there by subtracting $2x$ from each side:

$$
4x - 8 - 2x = 2x + 6 - 2x
$$

$$
2x - 8 = 6.
$$

Push the $-8$ away from the variable by adding $8$ to each side:

$$
2x = 14.
$$

Divide by $2$:

$$
x = 7.
$$

Verification in the original equation: the left side is $4(7 - 2) = 4(5) = 20$, and the right side is $2(7) + 6 = 14 + 6 = 20$. Both sides read $20$, so $x = 7$ is the correct solution.

## Common pitfalls

- **Collecting variables on the side with the smaller coefficient.** If you pull the larger variable term over to the smaller side instead of the other way around, you will end up with a negative coefficient on the variable — like $-2x = 6$ instead of $2x = 6$. The answer is still the same after division, but the extra negative sign gives many students trouble. Pick the side with the larger variable coefficient and subtract from the other side.
- **Forgetting to distribute before collecting.** If the equation contains parentheses, run the distributive property first. Trying to shuffle terms around while they are still locked inside parentheses leads to losing or duplicating pieces.
- **Subtracting a variable term from only one side.** Every move has to be balanced. If you remove an $x$ from the right, you must remove the same $x$ from the left. Otherwise you have secretly changed the equation and the answer will be wrong.
- **Assuming the equation has a unique solution.** Sometimes collecting variable terms makes them cancel completely. If the result is a true statement like $5 = 5$, every real number is a solution (an identity). If the result is a false statement like $3 = 7$, no real number is a solution (a contradiction). See [[Solving_Equations_In_One_Variable]] for the full story on these special cases.
- **Only checking the final value in the simplified equation.** Plug the answer back into the *original* equation, not a line of your own work. If you had a sign error three steps ago, verifying in your own half-solved form will not catch it.

## Problems Involving Equations with Variables on Both Sides

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="equations_with_variables_on_both_sides"></div>

## See Also

- [[Multi_Step_Equations]]
- [[Solving_Equations_In_One_Variable]]
- [[Literal_Equations_And_Formulas]]
- [[The_Distributive_Property_With_Variables]]
- [[Solving_Inequalities_In_One_Variable]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
