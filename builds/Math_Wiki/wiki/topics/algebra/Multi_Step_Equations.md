---
title: "Multi-Step Equations"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-linear", "#key-technique", "#skill-multi-step", "#test-sat", "#test-psat", "#test-act", "#test-clt"]
created: 2026-04-10
updated: 2026-04-11
source_refs: []
related:
  - "topics/algebra/One_Step_Equations"
  - "topics/algebra/Equations_With_Variables_On_Both_Sides"
  - "topics/algebra/Solving_Equations_In_One_Variable"
  - "topics/algebra/Literal_Equations_And_Formulas"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/One_Step_Equations"
  - "topics/pre_algebra/The_Distributive_Property_With_Variables"
  - "topics/pre_algebra/Order_Of_Operations"
problem_type_ids: []
figures: []
summary: "Undo operations in the reverse order they were done so $x$ peels out in several clean moves."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Multi-Step Equations

# Multi-Step Equations

Think of a multi-step equation as a gift box that has been wrapped several times: an outer ribbon, an inner tape job, a shell of paper, and finally the box itself. To reach what is inside, you do not rip off the innermost layer first — you work from the outside in, undoing each wrapping in the reverse order it went on. Multi-step equations behave the same way. Some operations were piled on top of $x$ one after another, and your job is to peel them off, back to front, one clean move at a time until $x$ stands alone.

The big idea is that [[One_Step_Equations|one-step solving]] already gives you the tools; you just use several of them in sequence. Every move still obeys the same rule as before — whatever you do to one side of the equation, you do to the other — and every move still uses an inverse operation to cancel something that is stuck to $x$. The only new skill is deciding **which** layer to peel first when more than one is in your way. The answer is almost always to peel them in the reverse order of the order of operations: addition and subtraction before multiplication and division, and never distribute a parenthesized group until you absolutely have to.

## What it means / The idea

A multi-step equation is any linear equation in one variable that needs at least two inverse operations to isolate $x$. A typical specimen looks like

$$
ax + b = c
$$

where $a$ is a coefficient, $b$ is a constant, and $c$ is the right-hand value. Sometimes the left side is wrapped in parentheses: $a(x + b) = c$. Sometimes there are like terms on the same side: $2x + 5x - 4 = 17$. And sometimes fractions show up to make it interesting. All of these count as multi-step, and the same game plan handles them.

## How it works / The procedure

1. **Clean up each side first.** If there are parentheses, distribute them. If there are like terms on the same side, combine them. You want each side of the equation to be as simple as possible before you start moving anything across.
2. **Peel addition and subtraction.** Add or subtract the same number from both sides so that the variable term ends up alone on one side. If the constant on the variable's side is a $+b$, subtract $b$; if it is a $-b$, add $b$.
3. **Peel multiplication and division.** Once the variable term is by itself (say $ax$), undo the coefficient by dividing both sides by $a$ — or equivalently, multiplying by its reciprocal if $a$ is a fraction.
4. **Write down $x$.** After the two peeling moves, $x$ should be standing alone on one side with a number on the other.
5. **Check the answer.** Substitute back into the original equation and verify that the two sides match.

Step 2 before step 3 is not a rule anyone invented for fun — it is just the reverse of the order of operations. When you evaluate $3x + 5$ you multiply first and then add, so when you **undo** that process to solve for $x$, you undo addition first and multiplication last.

## Why it works

Each move you make produces an equivalent equation — one with exactly the same solution as the original, just in a simpler form. Adding the same quantity to both sides of a true equality keeps it true. Dividing both sides by the same nonzero number keeps it true. Distribution and combining like terms only rewrite expressions without changing their values. So every single step preserves the original solution set, and after the last move, you are looking at the same equation you started with — only now it reads $x = \text{(number)}$, which is easy to interpret.

## Worked examples

**Example 1.** At a local bakery, Rohan is planning a birthday order. He will pay a flat $\$5$ decorating fee plus $\$2$ per cookie. If his total bill is $\$17$, how many cookies does he order? The equation is $2x + 5 = 17$.

Start by peeling the $+5$ from the left side. Subtract $5$ from both sides:

$$
2x + 5 - 5 = 17 - 5
$$

$$
2x = 12.
$$

Now peel the $2$ by dividing both sides by $2$:

$$
\frac{2x}{2} = \frac{12}{2}
$$

$$
x = 6.
$$

Rohan orders $6$ cookies. Check: $2 \cdot 6 + 5 = 12 + 5 = 17$. 

**Example 2.** Zoe is setting up a row of identical photo frames for a school display. Each frame takes up $(x - 4)$ inches of width, the display fits three frames in a row, and the total width comes out to $15$ inches. Determine $x$. The equation is $3(x - 4) = 15$.

Here the left side is wrapped in parentheses, so the first move is to distribute the $3$:

$$
3x - 12 = 15.
$$

Now the equation has the familiar $ax + b = c$ shape. Add $12$ to both sides:

$$
3x - 12 + 12 = 15 + 12
$$

$$
3x = 27.
$$

Divide both sides by $3$:

$$
x = 9.
$$

So $x = 9$ inches. Check by substituting back into the **original** equation: $3(9 - 4) = 3(5) = 15$. 

An alternative worth knowing: instead of distributing first, you can divide both sides by $3$ right away, giving $x - 4 = 5$ and then $x = 9$. When the coefficient in front of the parenthesis divides the right side cleanly, that shortcut is faster. When it does not, fall back to distributing.

**Example 3.** In a tutoring center, Emilia tracks how many practice problems two students finish. The equation $4x + 2 = x + 14$ describes the moment their totals are equal. What is $x$? Here the variable appears on **both** sides, which is the one twist this topic throws at you.

The fix is to move every $x$ to one side and every plain number to the other. Start by getting all the $x$s together. Subtract $x$ from both sides so only the left keeps a variable term:

$$
4x - x + 2 = x - x + 14
$$

$$
3x + 2 = 14.
$$

Now the equation is back in the familiar $ax + b = c$ shape. Subtract $2$ from both sides:

$$
3x = 12.
$$

Divide both sides by $3$:

$$
x = 4.
$$

Check: $4(4) + 2 = 18$ on the left, and $4 + 14 = 18$ on the right. The two sides agree, so $x = 4$ is the solution. When the variable is on both sides, this problem really lives in the territory of [[Equations_With_Variables_On_Both_Sides]], but the rest of the moves are pure multi-step technique.

## Common pitfalls

- **Forgetting to distribute.** If the equation is $4(x + 2) = 20$, the $4$ hits **both** the $x$ and the $2$, giving $4x + 8 = 20$. A very common error is to write $4x + 2 = 20$ and then solve that instead. Whenever a number sits in front of parentheses, apply it to every term inside.
- **Peeling in the wrong order.** If the equation is $5x - 3 = 12$ and you try to divide by $5$ first, you get $x - 3/5 = 12/5$, which is messier than it needs to be. Undo $-3$ first, then undo $\cdot 5$. Addition comes off before multiplication.
- **Missing a sign when you move a term.** Subtracting $3$ from both sides is not the same as moving a $3$ across the equals sign while leaving its sign the same. If your work says $5x = 17$ when it should say $5x = 7$, a sign probably drifted the wrong direction when you peeled a constant off.
- **Combining unlike terms.** In $3x + 4 = 2x + 9$, the $3x$ and $4$ are not like terms. They stay apart. Only combine $3x$ with $2x$, and only combine $4$ with $9$. Different species, different piles.
- **Skipping the check.** Especially for equations with variables on both sides, substitute your final answer back into the **original** equation. If both sides do not agree, walk back through the moves — you will usually spot the error inside one sign or one distribution.

## Problems Involving Multi-Step Equations

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="multi_step_equations"></div>

## See Also

- [[One_Step_Equations]] — the smallest version of the same idea
- [[Equations_With_Variables_On_Both_Sides]] — when $x$ appears twice, once per side
- [[Solving_Equations_In_One_Variable]] — the umbrella topic for these skills
- [[Literal_Equations_And_Formulas]] — multi-step solving when the "constants" are letters
- [[The_Distributive_Property_With_Variables|The Distributive Property]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
