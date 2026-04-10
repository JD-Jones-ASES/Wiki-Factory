---
title: "Applications of Quadratic Functions"
type: topic
aliases: ["Quadratic Word Problems", "Quadratic Modeling", "Optimization with Quadratics"]
tags: ["#branch-algebra-2", "#topic-quadratics", "#word-problem-support", "#skill-translation"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "3", section: "3.7"}
related:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Graphing_Quadratic_Functions"
  - "topics/algebra/Completing_The_Square"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Modeling_With_Linear_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Graphing_Quadratic_Functions"
  - "topics/algebra/The_Quadratic_Formula"
  - "topics/algebra/Modeling_With_Linear_Functions"
problem_type_ids: []
figures: []
summary: "Word problems where a quadratic is the model and the vertex is the answer: projectile flights, area optimization, and revenue."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Applications of Quadratic Functions

# Applications of Quadratic Functions

Once you know the shape of a parabola — the smooth rise, the turn at the vertex, the symmetric fall — you can use it as a model for a surprising number of real situations. Any time a quantity grows for a while, peaks, and then falls back, or any time you are trying to find the single best choice out of a trade-off, there is a decent chance a quadratic is hiding under the story. Three patterns cover almost all the problems you will see in an algebra-2 course: **projectile motion**, **area under a fixed perimeter**, and **revenue with a price–quantity trade-off**. Each of them is solved with the same tool — the vertex.

The big move in every problem is this: write the real-world quantity (height, area, dollars) as a function $f(x)$ of a single input variable, recognize that $f$ is a quadratic that opens downward, and locate its vertex. Because the parabola opens down, the vertex's $y$-coordinate is the **largest possible value** of the quantity, and its $x$-coordinate tells you **where** that maximum occurs. Translating the coordinates of one point back into English — "this is the biggest area, and this is the width that produces it" — is how the problem gets answered.

---

## The four-step recipe

Every quadratic application follows the same rhythm. When the problem feels overwhelming, fall back on this:

1. **Name the variables.** Pick a letter for the quantity you are choosing (the width of a pen, the number of items sold, the time elapsed) and a letter for the quantity you are trying to optimize (area, revenue, height).
2. **Write the function.** Translate the words into a formula that expresses the target quantity as a quadratic in the chosen variable. Expect to multiply two linear pieces together and get an $x^2$ term.
3. **Locate the vertex.** Use either the shortcut $x = -\dfrac{b}{2a}$ on standard form, or [[Completing_The_Square]] to rewrite the function in vertex form. Whichever is faster.
4. **Interpret in context.** State the $x$-value as what it means in the story — the best width, the ideal quantity, the moment of highest flight — and the $y$-value as what it produces — the maximum area, the peak revenue, the greatest height. Always attach units.

The final step is the one people skip, and it is the one that earns the credit. A pair of coordinates is not a solution until it has a sentence in English wrapped around it.

---

## The projectile model

For an object moving straight up or down under gravity, the height above the ground as a function of time is a quadratic. In American units (feet and seconds),

$$
h(t) = -16t^2 + v_0 t + h_0,
$$

where $v_0$ is the starting upward speed in feet per second and $h_0$ is the starting height in feet. In metric units (meters and seconds), the leading coefficient becomes $-4.9$ instead of $-16$, because the acceleration of gravity is about $9.8$ meters per second squared and the coefficient out front is half of that. Pick one unit system and stay in it — mixing them produces nonsense.

The vertex of this parabola is where the object reaches its **peak height**. Its $t$-coordinate tells you **when** the peak happens; its $h$-coordinate tells you **how high** the object got. The $t$-intercepts — values where $h(t) = 0$ — are where the object is at ground level, so the positive one is the time the object lands.

---

## Example 1: a firework over a cliff

> A toy rocket is launched straight up from the edge of a $48$-foot cliff with an initial upward speed of $32$ feet per second. Find the maximum height the rocket reaches (and how long after launch that happens), and find when the rocket returns to ground level at the bottom of the cliff.

**Name the variables.** Let $t$ be the number of seconds since launch and $h(t)$ the height in feet above ground level at the base of the cliff.

**Write the function.** Plug $v_0 = 32$ and $h_0 = 48$ into the projectile model:

$$
h(t) = -16t^2 + 32t + 48.
$$

**Find the vertex (maximum height and its time).** The shortcut gives

$$
t = -\dfrac{32}{2(-16)} = -\dfrac{32}{-32} = 1 \text{ second}.
$$

Then

$$
h(1) = -16(1)^2 + 32(1) + 48 = -16 + 32 + 48 = 64 \text{ feet}.
$$

**Interpret.** The vertex is $(1, 64)$. In this story, the vertex represents the **highest point of the rocket's flight**: the rocket reaches its maximum height of $64$ feet exactly $1$ second after launch. That is the entire point of finding the vertex here.

**When does it hit the ground?** Set $h(t) = 0$ and solve:

$$
-16t^2 + 32t + 48 = 0.
$$

Divide everything by $-16$ to simplify:

$$
t^2 - 2t - 3 = 0 \quad\Longrightarrow\quad (t - 3)(t + 1) = 0.
$$

So $t = 3$ or $t = -1$. The negative answer is before the rocket was even launched, so reject it. The rocket hits the ground at $t = 3$ seconds.

---

## Example 2: a garden against a barn

> A farmer has $120$ feet of fencing to build a rectangular pen against the straight wall of a barn. The barn forms one full side of the rectangle, so only three sides need fencing. What dimensions should the pen have to enclose the largest possible area?

**Name the variables.** Let $w$ be the width of the pen in feet — the dimension running perpendicular to the barn, so there are two of these sides. Let $\ell$ be the length running parallel to the barn, the one long side opposite the wall. Let $A$ be the enclosed area in square feet.

**Write the constraint and the area function.** The fencing covers the two widths and the single length, so

$$
2w + \ell = 120 \quad\Longrightarrow\quad \ell = 120 - 2w.
$$

Area is width times length:

$$
A(w) = w \cdot \ell = w(120 - 2w) = -2w^2 + 120w.
$$

This is a quadratic in $w$ with $a = -2$, $b = 120$, $c = 0$. Since $a < 0$, the parabola opens downward — there is a maximum.

**Locate the vertex.**

$$
w = -\dfrac{120}{2(-2)} = -\dfrac{120}{-4} = 30 \text{ feet}.
$$

Then $\ell = 120 - 2(30) = 60$ feet, and the enclosed area is $A(30) = 30 \cdot 60 = 1800$ square feet.

**Interpret.** The vertex is $(30, 1800)$. In this story, the vertex represents the **largest area the farmer can possibly enclose with the $120$ feet of fence**. The best choice is a pen that is $30$ feet wide and $60$ feet long, giving an area of $1800$ square feet. Notice that the long side parallel to the barn ends up being exactly twice each short side — a useful rule of thumb for three-sided fencing problems.

---

## Example 3: pricing a handmade product

> A craft shop finds that when it charges $x$ dollars for one of its handmade candles, the weekly number of candles sold drops off as the price rises, so that weekly revenue in dollars is modeled by $R(x) = x(100 - x)$. What price maximizes weekly revenue, and what is that maximum revenue?

**Read the model.** Start by expanding the revenue function so it is in a friendlier form:

$$
R(x) = x(100 - x) = -x^2 + 100x.
$$

So $R$ is a quadratic in the price $x$, with $a = -1$, $b = 100$, $c = 0$. Since $a < 0$, the graph opens downward and the vertex is a maximum.

**Locate the vertex.**

$$
x = -\dfrac{100}{2(-1)} = \dfrac{100}{2} = 50 \text{ dollars}.
$$

Then

$$
R(50) = 50(100 - 50) = 50 \cdot 50 = 2500 \text{ dollars}.
$$

**Interpret.** The vertex is $(50, 2500)$. In this story, the vertex represents the **ideal price that earns the shop the most weekly revenue**. Charging $\$50$ per candle brings in a peak weekly revenue of $\$2500$; any other price — whether higher or lower — produces less. A higher price scares off customers, a lower price leaves money on the table, and the vertex is the sweet spot in between.

This is a common pattern in revenue problems: the "price $\times$ quantity" product, where quantity is itself a linear function of price, always expands into a downward-opening quadratic with the vertex at the optimal price.

---

## Common pitfalls

- **Rejecting the wrong root.** Projectile problems give you two time answers, and one is often negative or past the physical end of the motion. Stop and ask which one makes sense in the story; keep the positive, in-range one.
- **Mixing feet and meters.** The projectile coefficient is $-16$ for feet/seconds and $-4.9$ for meters/seconds. Pick the unit system in the first sentence of the problem and do not swap mid-calculation.
- **Maximizing the wrong thing.** When a problem asks for the best price, the unknown is the price, not the quantity. Always ask: "what am I choosing?" The answer is the independent variable $x$. "What am I trying to make as big as possible?" is the function $f(x)$.
- **Forgetting what the vertex means.** The vertex is always a point $(x_v, y_v)$. The $x$-coordinate is the optimal choice (the width, the time, the price); the $y$-coordinate is the resulting optimum (the maximum area, the peak height, the peak revenue). Mixing these two up is a common source of lost points.
- **Skipping the English sentence.** The coordinates are not the final answer. Write a sentence naming what the vertex represents in the world of the problem.

---

## Prerequisites

Before you practice these applications, be comfortable with:

- [[Quadratic_Functions]] — especially vertex form and the vertex shortcut $x = -\dfrac{b}{2a}$
- [[The_Quadratic_Formula]] — for finding where a projectile returns to ground level
- [[Modeling_With_Linear_Functions]] — the general habit of translating a story into a formula with variables and units

---

## Problems Involving Applications of Quadratic Functions

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="applications_of_quadratic_functions"></div>

_Practice generators for this topic are coming in the Cluster 3 generator wave of this session._

---

## See Also

- [[Quadratic_Functions]]
- [[Graphing_Quadratic_Functions]]
- [[Completing_The_Square]]
- [[The_Quadratic_Formula]]
- [[Modeling_With_Linear_Functions]]
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
