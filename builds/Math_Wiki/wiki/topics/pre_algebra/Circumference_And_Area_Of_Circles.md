---
title: "Circumference and Area of Circles"
type: topic
aliases: ["Area of a Circle", "Circumference Formula", "Pi and Circles"]
tags: ["#branch-pre-algebra", "#topic-analytic-geometry"]
created: 2026-04-11
updated: 2026-04-11
source_refs:
  - {book: "math_1", chapter: "9", section: "9.4"}
related:
  - "topics/geometry/Circles"
  - "topics/pre_algebra/Order_Of_Operations"
status: draft
confidence: high
branch: pre-algebra
prerequisites:
  - "topics/pre_algebra/Order_Of_Operations"
  - "topics/pre_algebra/Variables_And_Algebraic_Expressions"
problem_type_ids: []
figures: []
summary: "How far around a circle is, how much space it covers, and why one mysterious number — pi — controls both."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Circumference and Area of Circles

# Circumference and Area of Circles

A circle is the roundest shape there is. Every point on the edge sits the same distance from the middle, so unlike a square or a triangle there are no corners, no long sides, and no short sides — the shape looks the same no matter which way you turn it. That simple symmetry is what makes a wheel roll smoothly, a pizza cut into equal slices, and a garden hose spray in an even ring. It is also what lets us describe a circle with just **one** number: the **radius** $r$, the distance from the center out to the edge.

From that one number you can answer the two questions people usually ask about circles: **how far is it around the circle?** and **how much space does the circle cover?** The first is called the **circumference**, and it is the circle's version of perimeter. The second is the circle's **area**. Both answers turn out to be controlled by the same mysterious number, which we call **pi**.

---

## Meeting pi

Measure a few real circles and you will start to notice a pattern. Take the distance around a dinner plate and divide it by the distance across the plate through the center — in other words, divide the circumference by the diameter. You do not get a clean whole number. You get a decimal, and it starts $3.14$ and keeps going. Try it with a bicycle wheel and you get the same starting decimal. Try it with a tiny coin, or a huge pizza, or the ring of a stadium, and the answer is always the same: about $3.14$.

That ratio is a fixed constant of nature, and its name is **pi**, written with the Greek letter $\pi$. The defining equation is just

$$
\pi = \dfrac{\text{circumference}}{\text{diameter}}.
$$

For middle-school work, the two handy approximations are $\pi \approx 3.14$ and $\pi \approx \dfrac{22}{7}$. Either one is close enough for most problems. The real value of $\pi$ is irrational — its decimal never ends and never repeats — so every answer you write using $3.14$ or $\dfrac{22}{7}$ is rounded. That is fine; just do not expect everything to match up to the last digit.

The diameter $d$ of a circle is the straight-line distance across through the center, and it is always twice the radius:

$$
d = 2r \qquad \text{or equivalently} \qquad r = \dfrac{d}{2}.
$$

If a problem hands you the diameter instead of the radius, cut it in half first.

---

## The two formulas

Rearranging the definition $\pi = C/d$ gives the **circumference formula**:

$$
C = \pi d = 2\pi r.
$$

Both versions say the same thing. Use $\pi d$ if you know the diameter, or $2\pi r$ if you know the radius — whichever one saves you a step.

The **area formula** looks similar but squares the radius:

$$
A = \pi r^2.
$$

This is the amount of flat space the circle covers, measured in square units. The key move is that you **square the radius first**, and then multiply by $\pi$. That is the order the exponent demands. Doing it backwards (multiplying $\pi$ by $r$, then squaring the result) gives a completely wrong answer.

---

## Key ideas

- $\pi$ is not a fresh number for each circle — it is the same ratio every time. One circle, one million circles, the constant is the same.
- Diameter and radius are linked by $d = 2r$. Always identify which one you are given before plugging into a formula.
- Circumference is a **length** (inches, centimeters, miles) and area is a **square length** (square inches, square meters). Pay attention to the units on your final answer.
- Many problems will let you leave $\pi$ in the answer. Writing $25\pi$ square inches is exact; writing $78.5$ square inches is an approximation.

---

## Example 1: circumference from the radius

> A bicycle tire has a radius of $13$ inches. How far does the bike travel in one full roll of the tire? Use $\pi \approx 3.14$.

One full roll of a wheel traces out exactly the circumference of the tire. Use $C = 2\pi r$ with $r = 13$:

$$
C \approx 2 \times 3.14 \times 13 = 6.28 \times 13 = 81.64 \text{ inches}.
$$

So the bike moves forward about $81.64$ inches — just under seven feet — every time the wheel turns over once. If you wanted a tidier exact answer you could leave the result as $C = 26\pi$ inches.

---

## Example 2: area of a pizza

> A round pizza has a diameter of $16$ inches. How many square inches of pizza do you get? Use $\pi \approx 3.14$.

The area formula needs the radius, not the diameter. First convert:

$$
r = \dfrac{d}{2} = \dfrac{16}{2} = 8 \text{ inches}.
$$

Now square the radius, then multiply by $\pi$:

$$
A = \pi r^2 \approx 3.14 \times 8^2 = 3.14 \times 64 = 200.96 \text{ square inches}.
$$

The whole pizza covers about $200.96$ square inches. Notice the units — **square** inches for area, never plain inches.

If the pizza is cut into $8$ equal slices, each slice covers $\dfrac{200.96}{8} = 25.12$ square inches. A bigger pizza really does give you substantially more food per slice than a smaller one, because the area grows with the square of the radius: double the diameter and the area quadruples.

---

## Example 3: working backward from circumference

> A circular running track has a circumference of $400$ meters. What is the radius of the track, to the nearest meter? Use $\pi \approx 3.14$.

This time you know $C$ and you want $r$. Start from $C = 2\pi r$ and solve for $r$ by dividing both sides by $2\pi$:

$$
r = \dfrac{C}{2\pi} \approx \dfrac{400}{2 \times 3.14} = \dfrac{400}{6.28}.
$$

Compute the division:

$$
r \approx 63.69 \text{ meters}.
$$

Round to the nearest meter: the track has a radius of about $64$ meters. You can sanity-check by pushing the number back through the circumference formula: $2 \times 3.14 \times 64 \approx 401.9$, which is close to the given $400$ after rounding.

---

## Common pitfalls

- **Squaring the wrong thing in the area formula.** Remember the order: first $r^2$, then multiply by $\pi$. Writing $(\pi r)^2$ is a different expression and will give the wrong answer.
- **Forgetting to halve the diameter.** When a problem says "a circle with diameter $14$," you cannot plug $14$ into $A = \pi r^2$ as if it were the radius. Cut the diameter in half first to get $r = 7$.
- **Using circumference units for area.** Circumference answers are in inches, centimeters, or meters. Area answers are in **square** inches, **square** centimeters, or **square** meters. Label the units carefully — writing "$50$ square cm" when you mean circumference is a giveaway that the formulas got mixed up.
- **Treating $\pi$ as exactly $3.14$.** $3.14$ is only an approximation. If a problem asks for an "exact" answer, leave $\pi$ in the answer (for example, $49\pi$ square inches) rather than multiplying it out.

---

## Prerequisites

Before tackling practice problems, be comfortable with:

- [[Order_Of_Operations]] — so that $\pi r^2$ is evaluated in the correct order every time
- [[Variables_And_Algebraic_Expressions]] — for substituting numbers into a formula cleanly

---

## Problems Involving Circumference and Area of Circles

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="circumference_and_area_of_circles"></div>

---

## See Also

- [[Circles]] — the geometry-side treatment, with the circle equation $(x - h)^2 + (y - k)^2 = r^2$
- [[Order_Of_Operations]] — for evaluating $\pi r^2$ correctly
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
