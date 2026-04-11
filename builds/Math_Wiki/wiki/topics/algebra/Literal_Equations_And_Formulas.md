---
title: "Literal Equations and Formulas"
type: topic
aliases: []
tags: ["#branch-algebra-1", "#topic-linear", "#skill-algebraic-manipulation", "#test-sat", "#test-psat", "#test-act"]
created: 2026-04-10
updated: 2026-04-11
source_refs:
  - {book: "algebra_1", chapter: "2", section: "2.5"}
related:
  - "topics/algebra/One_Step_Equations"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Equations_With_Variables_On_Both_Sides"
  - "topics/algebra/Solving_Equations_In_One_Variable"
  - "topics/algebra/Writing_Linear_Equations"
status: draft
confidence: high
branch: algebra-1
prerequisites:
  - "topics/algebra/One_Step_Equations"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/pre_algebra/The_Distributive_Property"
problem_type_ids: []
figures: []
summary: "Solve a formula for a different letter by treating every other letter as a constant and running the usual equation-solving moves."
---
> [[_overview|Home]] > [[Algebra_1|Algebra 1]] > Literal Equations and Formulas

# Literal Equations and Formulas

Up to now every equation you have solved had one letter in it — you were finding that single unknown. A **literal equation** is the next step: an equation whose job is to express a relationship among several letters at once, like $A = lw$ or $d = rt$, so that you can rearrange it to isolate whichever letter you care about. A **formula** is really the same thing wearing a different hat: $A = lw$, $d = rt$, $F = \tfrac{9}{5}C + 32$, $A = \tfrac{1}{2}bh$, $y = mx + b$. Each of these has a conventional "output" letter on the left, but nothing stops you from rearranging the letters to solve for any one of them. You just treat every other letter as if it were a constant, and run the same solving moves you already know.

That is the key move. Solving a literal equation is not a new technique — it is your ordinary equation-solving toolkit applied to a problem where the "numbers" happen to be spelled with letters. If you can solve $3x + 12 = 30$ for $x$, you can solve $ax + b = c$ for $x$, because you do exactly the same steps.

The reason this matters so much beyond Algebra 1 is that almost every formula in science, finance, and engineering comes pre-assembled in one arrangement, and you will constantly need to rearrange it to isolate whatever you care about. If you have a rectangle's area $A$ and its length $l$, the formula $A = lw$ is technically "about" $A$, but what you actually want is the width, so you need to rearrange it into $w = \dfrac{A}{l}$. That rearrangement is what this page teaches.

---

## Key ideas

### Treat every other letter as a constant

This is the whole idea of the topic in one line: when you are solving a literal equation for a specific letter, pretend every other letter in the equation is a plain number. The equation $ax + b = c$ might look intimidating at first — "four letters!" — but if you decide you are solving for $x$, then $a$, $b$, and $c$ are just numbers you don't happen to know yet. The equation behaves exactly like $3x + 5 = 20$, and the steps are identical.

So the instructions for solving any literal equation collapse into three words: **isolate the target**. Use the same moves you already know — add the same thing to both sides, subtract, multiply, divide, distribute, combine — and keep going until the target letter is alone on one side of the equals sign.

### The moves are the same as ordinary equation solving

You do not need any new rules. The familiar ones from [[One_Step_Equations]] and [[Multi_Step_Equations]] are all you need:

- **Add or subtract the same thing from both sides.** Use this to peel constants off the side of the target letter.
- **Multiply or divide both sides by the same nonzero thing.** Use this to strip a coefficient off the target letter.
- **Distribute** when a coefficient multiplies a sum or difference, so you can access the target letter inside.
- **Combine** like terms that share the target letter before you try to isolate it, if there are several of them.

The target letter goes on the left of the equals sign at the end; everything else lives on the right. That final form is the **solved** formula.

### Undo operations in the reverse of PEMDAS order

The order in which you undo operations is the reverse of PEMDAS. Look at what is being done to the target letter, from outermost operation inward, and undo it in the opposite sequence. For example, in $A = \tfrac{1}{2}bh$ solving for $h$:

1. The target $h$ is multiplied by $\tfrac{1}{2}$ and by $b$.
2. To undo the multiplication by $\tfrac{1}{2}b$, multiply both sides by $\dfrac{2}{b}$ (or equivalently, multiply by $2$ first and then divide by $b$).
3. You end up with $h = \dfrac{2A}{b}$.

In the trickier case $P = 2l + 2w$ solving for $l$, you have to undo an addition before you undo a multiplication, because the addition is applied to the target letter last:

1. The target $l$ is first multiplied by $2$, then added to $2w$.
2. Undo the addition first: subtract $2w$ from both sides, giving $P - 2w = 2l$.
3. Undo the multiplication: divide both sides by $2$, giving $\dfrac{P - 2w}{2} = l$, which is usually written with $l$ on the left: $l = \dfrac{P - 2w}{2}$.

That "undo addition before you undo multiplication" rule is the reverse of the usual PEMDAS order, which is exactly what you want when you are running the moves in reverse.

### Collect the target letter if it appears multiple times

If the target letter shows up in more than one place, your first job is to get all of its appearances onto the same side of the equation and then **factor** it out so it appears only once. For example, starting from $ax + b = cx + d$ and solving for $x$:

1. Subtract $cx$ from both sides: $ax - cx + b = d$.
2. Subtract $b$ from both sides: $ax - cx = d - b$.
3. Factor out the common $x$ on the left: $x(a - c) = d - b$.
4. Divide by $(a - c)$: $x = \dfrac{d - b}{a - c}$.

That factor-and-divide move at the end is the hallmark of a literal equation where the target appears twice, and it is the only thing that makes this flavor of problem different from a numerical equation.

---

## Example 1: Solve $P = 2l + 2w$ for $l$

> The perimeter formula for a rectangle is $P = 2l + 2w$, where $l$ is the length and $w$ is the width. Write the formula solved for $l$.

The target letter is $l$. Everything else in the equation — $P$, $w$, and the constants $2$ — gets treated as a number. The plan is to peel away whatever is being done to $l$, working from the outside in.

Step 1. The target $l$ appears in the term $2l$, which sits next to $+2w$. The $2w$ is being added to the target term, so undo that addition first by subtracting $2w$ from both sides:

$$
P - 2w = 2l
$$

Step 2. Now $l$ is only being multiplied by $2$. Undo that by dividing both sides by $2$:

$$
\frac{P - 2w}{2} = l
$$

Step 3. Rewrite with $l$ on the left, which is just a cosmetic flip:

$$
l = \frac{P - 2w}{2}
$$

That is the formula solved for $l$. To sanity-check, plug in numbers: a rectangle with $P = 20$ and $w = 4$ should give $l = (20 - 8)/2 = 6$. Check against the original: $P = 2(6) + 2(4) = 12 + 8 = 20$. Matches, so the rearrangement is correct.

---

## Example 2: Solve $d = rt$ for $r$

> The distance formula from physics is $d = rt$, where $d$ is distance, $r$ is rate, and $t$ is time. Emilia wants a version of the formula that gives $r$ directly. Write $d = rt$ solved for $r$.

The target letter is $r$. The only operation being applied to $r$ in the equation $d = rt$ is multiplication by $t$, so there is only one move to make. Undo the multiplication by dividing both sides by $t$:

$$
\frac{d}{t} = \frac{rt}{t}
$$

On the right side, the $t$'s cancel, leaving just $r$:

$$
\frac{d}{t} = r
$$

Flipping the equation so that the target is on the left gives the final answer:

$$
r = \frac{d}{t}
$$

This is the rate formula in the form you would actually use if you were given a distance and a time and wanted to compute the rate. For a quick check, pick numbers: a car that goes $d = 120$ miles in $t = 3$ hours has a rate of $r = 120/3 = 40$ mph. Against the original: $d = rt = 40 \cdot 3 = 120$. Consistent.

A subtle point: you are implicitly assuming $t \neq 0$ when you divide by $t$. In a real-world distance/rate/time context, $t = 0$ means zero time has passed, which makes "rate" meaningless anyway, so the assumption is fine. But in general, whenever you divide by a letter, you should keep a mental note that the rearranged formula is only valid when that letter is not zero.

---

## Example 3: Solve $C = 2\pi r$ for $r$

> The circumference formula for a circle is $C = 2\pi r$. Write the formula solved for $r$, so that knowing the circumference $C$ gives the radius $r$ immediately.

Target letter: $r$. Every other symbol — $C$, $\pi$, and the $2$ — is a constant for the purposes of this problem. In particular, $\pi$ is a specific number ($\approx 3.14159$), so treating it as a constant is literally true here.

The only operation being applied to $r$ is multiplication by $2\pi$. Undo it by dividing both sides by $2\pi$:

$$
\frac{C}{2\pi} = \frac{2\pi r}{2\pi}
$$

The $2\pi$'s cancel on the right, leaving just $r$:

$$
\frac{C}{2\pi} = r
$$

Putting the target on the left:

$$
r = \frac{C}{2\pi}
$$

That is the radius-from-circumference formula. A quick check: a circle with $C = 2\pi$ has $r = \dfrac{2\pi}{2\pi} = 1$, which says the unit circle has radius $1$. That matches the definition of the unit circle, so the rearrangement is correct.

A useful habit: when the coefficient of the target is a product of a number and an irrational constant like $\pi$, undo the whole thing in one move (divide by $2\pi$) rather than in two moves (divide by $2$, then by $\pi$). It keeps the expression tidy and avoids leaving messy intermediate steps.

---

## Common pitfalls

- **Treating a constant as a variable.** When you are solving for $l$ in $P = 2l + 2w$, the letters $P$ and $w$ are held fixed — they are the "numbers" of the problem. Trying to "solve for" all the letters at once makes no sense; pick one target at a time and treat everything else as constant.
- **Undoing multiplication before undoing addition.** If the equation is $P = 2l + 2w$ and you want to solve for $l$, you have to subtract $2w$ **first** and then divide by $2$, not the other way around. Running the moves in the wrong order mangles the formula, because division distributes over subtraction only if you remember to divide every term.
- **Forgetting to divide every term when you do divide.** When you divide both sides of $P - 2w = 2l$ by $2$, you are dividing the **entire** left side, giving $\dfrac{P - 2w}{2}$ — not just one of the terms. A common mistake is to write $P - w = l$, which has divided only the $2w$ and forgotten the $P$.
- **Dividing by a letter without noting the restriction.** When you divide by $t$ in $d = rt$, you are assuming $t \neq 0$. In most physical contexts that is harmless, but in a pure-algebra problem you should at least be aware of it.
- **Forgetting to factor when the target appears twice.** If the target letter appears in two places on the same side, the only way to isolate it cleanly is to factor it out. An equation like $ax - cx = d - b$ becomes $x(a - c) = d - b$, and then $x = \dfrac{d - b}{a - c}$. Missing that factoring step leaves you stuck with two $x$'s and no clean way to divide.

---

## Prerequisites

Literal equations are equation-solving with letters as numbers, so make sure these feel routine first:

- [[One_Step_Equations]] — the basic solving moves (add, subtract, multiply, divide)
- [[Multi_Step_Equations]] — how to combine those moves in sequence
- [[The_Distributive_Property]] — for rearranging expressions where the target letter is inside a set of parentheses

---

## Problems Involving Literal Equations and Formulas

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="literal_equations_and_formulas"></div>

---

## See Also

- [[One_Step_Equations]]
- [[Multi_Step_Equations]]
- [[Equations_With_Variables_On_Both_Sides]]
- [[Solving_Equations_In_One_Variable]]
- [[Writing_Linear_Equations]]
- [[Algebra_1|Algebra 1]]
- [[Topics_Overview]]
- [[_overview|Home]]
