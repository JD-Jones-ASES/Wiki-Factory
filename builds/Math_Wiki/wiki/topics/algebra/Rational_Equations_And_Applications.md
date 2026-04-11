---
title: "Rational Equations and Applications"
type: topic
aliases: ["Rational Equation Word Problems", "Work and Rate Problems"]
tags: ["#branch-algebra-2", "#topic-rational-expressions"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "6", section: "6.6"}
related:
  - "topics/algebra/Solving_Rational_Equations"
  - "topics/algebra/Simplifying_Rational_Expressions"
  - "topics/algebra/Multi_Step_Equations"
  - "topics/algebra/Modeling_With_Linear_Functions"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Solving_Rational_Equations"
  - "topics/algebra/Multi_Step_Equations"
problem_type_ids: []
figures: []
summary: "Turning real-world rate, work, and travel scenarios into rational equations, then solving and interpreting the answer."
---

> [[_overview|Home]] > [[Algebra_2|Algebra 2]] > Rational Equations and Applications

# Rational Equations and Applications

Once you know how to [[Solving_Rational_Equations|solve a rational equation]] — clear the denominators, solve what is left, throw out any value that would zero out an original denominator — the next step is to stop being handed equations and start building them from a story. Most real-world problems that become rational equations involve a quantity that must be split across time or distance: how fast something gets done when two helpers work together, how long a trip takes when part of it fights a current or a headwind, how an average speed comes out when the return leg is slower than the trip out.

The shared feature of all these problems is that "rate" is doing the heavy lifting, and a rate is a fraction. As soon as fractions enter the picture, the equation you end up with usually has a variable in at least one denominator — and that is what makes it rational.

---

## The three scenarios that show up again and again

Almost every rational-equation word problem in algebra 2 falls into one of three families. Knowing which family you are in tells you exactly which formula to reach for.

### Work problems (combined rates)

If one person finishes a job in $t_A$ hours and a second person finishes the same job in $t_B$ hours, their **rates** of work are $\dfrac{1}{t_A}$ and $\dfrac{1}{t_B}$ jobs per hour. Working together their rates add, and the time $T$ they take together satisfies

$$
\dfrac{1}{t_A} + \dfrac{1}{t_B} = \dfrac{1}{T}.
$$

The key mental picture: in one hour Alice gets $\dfrac{1}{t_A}$ of the job done and Bob gets $\dfrac{1}{t_B}$ of the job done, so together they finish $\dfrac{1}{t_A} + \dfrac{1}{t_B}$ of the job in one hour. The combined time $T$ is the reciprocal of that combined rate.

### Distance-rate-time with an obstacle

When a boat, kayak, plane, or runner moves through a medium that speeds them up one way and slows them down the other, split the trip into two legs and use $\text{time} = \dfrac{\text{distance}}{\text{rate}}$ for each leg. Let $v$ be the object's speed in still water (or still air), and let $c$ be the current (or wind). Then

- downstream rate: $v + c$
- upstream rate: $v - c$

You then write an equation that relates the two times — usually they sum to a total time, or they are equal to each other.

### Average rate over a round trip or two-segment journey

The average speed for a trip is **total distance divided by total time**, not the mean of the two leg speeds. If the legs have rates $r_1$ and $r_2$ and each covers distance $d$, the total time is $\dfrac{d}{r_1} + \dfrac{d}{r_2}$, and the average speed works out to

$$
\text{average rate} = \dfrac{2d}{\dfrac{d}{r_1} + \dfrac{d}{r_2}}.
$$

That fraction-inside-a-fraction is the reason average speed problems land in this unit.

---

## A four-step recipe

Every rational-equation word problem is long, but the steps are short. Every time:

1. **Name a variable** for the single unknown you care about. Write in words what it stands for, including units. ("Let $T$ be the number of hours Maya and Jordan take together.")
2. **Write each rate as a fraction.** Rates of work are $\dfrac{1}{\text{time}}$; distance-rate-time gives $\text{time} = \dfrac{d}{r}$. Attach correct units to every fraction.
3. **Set up the equation.** Add rates for work problems, add or equate times for travel problems, or use the average-rate formula.
4. **Solve and then interpret.** Clear denominators, solve the resulting equation, check for extraneous solutions, and finally translate the number back into the language of the story. A negative time or a negative speed gets rejected — it is a real solution of the equation but not of the problem.

---

## Example 1: stocking a bakery case together

> Maya can stock the front bakery case alone in $3$ hours. Her coworker Jordan, who is still learning the routine, can do it alone in $5$ hours. If they stock the case together, how long does it take?

**Set up the rates.** In one hour, Maya finishes $\dfrac{1}{3}$ of the case and Jordan finishes $\dfrac{1}{5}$. Let $T$ be the number of hours they take working together. Their combined rate is $\dfrac{1}{T}$ of the case per hour, so

$$
\dfrac{1}{3} + \dfrac{1}{5} = \dfrac{1}{T}.
$$

**Solve the equation.** The LCD on the left is $15$. Rewrite both fractions:

$$
\dfrac{5}{15} + \dfrac{3}{15} = \dfrac{1}{T} \quad\Longrightarrow\quad \dfrac{8}{15} = \dfrac{1}{T}.
$$

Take reciprocals of both sides:

$$
T = \dfrac{15}{8} = 1.875 \text{ hours}.
$$

**Interpret the answer.** So Maya and Jordan together finish stocking the case in $\dfrac{15}{8}$ hours, which is $1$ hour and $52.5$ minutes — just under two hours. Notice that the combined time is less than either person's solo time, which is exactly what we would expect: adding a helper should never slow things down.

---

## Example 2: a kayak versus a river current

> A kayaker paddles $12$ miles downstream in the same amount of time it takes her to paddle $6$ miles back upstream. If the river's current is $2$ miles per hour, find the kayaker's paddling speed in still water.

**Set up the variables.** Let $v$ be the kayaker's speed in still water, measured in miles per hour. Then her downstream speed is $v + 2$ and her upstream speed is $v - 2$, because the $2$ mph current helps her on the way down and fights her on the way up.

**Write each leg's time.** Using $\text{time} = \dfrac{\text{distance}}{\text{rate}}$, the downstream leg takes $\dfrac{12}{v + 2}$ hours and the upstream leg takes $\dfrac{6}{v - 2}$ hours. The problem says the two times are equal:

$$
\dfrac{12}{v + 2} = \dfrac{6}{v - 2}.
$$

**Solve.** Cross-multiply (which is just multiplying both sides by the LCD $(v+2)(v-2)$):

$$
12(v - 2) = 6(v + 2)
$$

$$
12v - 24 = 6v + 12
$$

$$
6v = 36 \quad\Longrightarrow\quad v = 6.
$$

**Check the restriction.** The original equation requires $v \ne 2$ and $v \ne -2$. Our answer $v = 6$ is fine. It is also positive, which is a physical must — a negative "paddling speed" would not make sense.

**Interpret the answer.** The kayaker's paddling speed in still water is $6$ miles per hour. Against the current she moves at $6 - 2 = 4$ mph, and with the current she moves at $6 + 2 = 8$ mph — so downstream she is twice as fast as upstream, which is why the longer downstream trip ($12$ miles) takes the same time as the shorter upstream trip ($6$ miles).

---

## Example 3: average speed on a round trip

> A cyclist rides from her house to a lookout point at a steady $18$ miles per hour, then turns around and rides home along the same route at only $12$ miles per hour (it is uphill the whole way back). What is her average speed for the round trip?

**Set up the variable.** Let $d$ be the distance from the house to the lookout, measured in miles. You might expect to need the actual number, but watch what happens — the $d$ will cancel, and the answer depends only on the two rates.

**Write the times.** The trip out takes $\dfrac{d}{18}$ hours, and the trip back takes $\dfrac{d}{12}$ hours. The total distance is $2d$ and the total time is $\dfrac{d}{18} + \dfrac{d}{12}$.

**Set up the average rate.**

$$
\text{average rate} = \dfrac{2d}{\dfrac{d}{18} + \dfrac{d}{12}}.
$$

**Simplify the complex fraction.** The LCD of $18$ and $12$ is $36$, so combine the denominator:

$$
\dfrac{d}{18} + \dfrac{d}{12} = \dfrac{2d}{36} + \dfrac{3d}{36} = \dfrac{5d}{36}.
$$

Substitute back:

$$
\text{average rate} = \dfrac{2d}{\dfrac{5d}{36}} = 2d \cdot \dfrac{36}{5d} = \dfrac{72d}{5d} = \dfrac{72}{5} = 14.4.
$$

**Interpret the answer.** The cyclist's average speed for the round trip is $14.4$ miles per hour. Notice that this is **not** the simple average $\dfrac{18 + 12}{2} = 15$ — the slower leg takes longer, so it pulls the average down below the midpoint. Averaging rates almost always gives the wrong answer in these problems. You have to weight each rate by the time it was in effect, which is exactly what the rational equation is doing for you.

---

## Common pitfalls

- **Averaging the two rates.** The average speed of a round trip at $18$ and $12$ mph is not $15$. The slower leg takes more time, so it counts more. Always go back to total distance over total time.
- **Forgetting to check extraneous solutions.** Whenever you multiply both sides of an equation by something containing the variable, a bogus solution can sneak in. Any value that zeroes one of the original denominators is extraneous and must be thrown out.
- **Not rejecting negative answers.** A negative time or negative speed is algebraically a solution of the equation but not a solution of the problem. After you solve, ask "does this number make sense for the situation?" before you circle it.
- **Setting up rates backward.** In work problems the rate is $\dfrac{1}{\text{time}}$, not $\dfrac{\text{time}}{1}$. It is easy to slip and add the times together — that would say one worker slows the other down, which is not how combined work behaves.
- **Skipping the interpretation step.** A bare number is not an answer. Convert $\dfrac{15}{8}$ hours into "about 1 hour 53 minutes," convert $v = 6$ into "the kayaker paddles 6 mph in still water," and so on. The problem asked a question in English; finish by answering it in English.

---

## Prerequisites

Before you attempt these word problems, make sure you are comfortable with:

- [[Solving_Rational_Equations]] — the mechanical move of clearing denominators and catching extraneous solutions
- [[Simplifying_Rational_Expressions]] — reducing the fractions that come out of your setup
- [[Multi_Step_Equations]] — so that once the denominators are cleared, the leftover linear (or quadratic) equation is easy to finish

If any of those feel shaky, work a few examples in that topic and come back.

---

## Problems Involving Rational Equations and Applications

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="rational_equations_and_applications"></div>

_Practice generators for this topic are coming in the Cluster 4 generator wave of this session._

---

## See Also

- [[Solving_Rational_Equations]]
- [[Simplifying_Rational_Expressions]]
- [[Multi_Step_Equations]]
- [[Modeling_With_Linear_Functions]]
- [[Algebra_2|Algebra 2]]
- [[Topics_Overview]]
- [[_overview|Home]]
