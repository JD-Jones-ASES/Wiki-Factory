---
title: "Polynomial Functions and Graphs"
type: topic
aliases: ["Polynomial Graphs", "Graphing Polynomials", "Polynomial Functions"]
tags: ["#branch-algebra-2", "#topic-polynomials", "#topic-functions", "#key-topic"]
created: 2026-04-10
updated: 2026-04-10
source_refs:
  - {book: "algebra_2", chapter: "5", section: "5.6"}
related:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Power_Functions"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Transformations_I_Shifts_And_Reflections"
  - "topics/algebra/Function_Basics"
status: draft
confidence: high
branch: algebra-2
prerequisites:
  - "topics/algebra/Quadratic_Functions"
  - "topics/algebra/Factoring_Completely"
  - "topics/algebra/Function_Basics"
  - "topics/algebra/Plotting_Points_And_The_Coordinate_Plane"
problem_type_ids: []
figures: []
summary: "Degree plus multiplicity: two rules that let you sketch any polynomial without plotting hundreds of points."
---

> [[_overview|Home]] > [[Algebra_Overview|Algebra]] > Polynomial Functions and Graphs

# Polynomial Functions and Graphs

A **polynomial function** is any rule you can build out of a variable raised to whole-number powers, each multiplied by a number and added together. In symbols:

$$
p(x) = a_{n} x^{n} + a_{n-1} x^{n-1} + \cdots + a_{1} x + a_{0},
$$

where the $a_{i}$ are real constants and $a_{n} \neq 0$. The biggest exponent that shows up is the **degree** of the polynomial, and the number out front of that biggest term, $a_{n}$, is the **leading coefficient**. The constant $a_{0}$ at the very end is just a number with no $x$ attached.

You already know how to handle the low-degree members of this family. A degree-$1$ polynomial is a line. A degree-$2$ polynomial is a parabola (see [[Quadratic_Functions]]). Once the degree climbs to $3$, $4$, $5$, and beyond, the graphs get more elaborate — they can dip and rise several times, and their arms can head in all sorts of directions. The goal of this topic is to give you two rules so powerful that you can sketch any polynomial by hand without ever building a giant table of values. Those two rules are **end behavior** and **multiplicity**.

---

## End behavior: where the arms of the graph go

Every polynomial's graph, no matter how wiggly it is in the middle, eventually calms down and heads toward $+\infty$ or $-\infty$ on both the left and the right. Two choices about the leading term dictate exactly which way each end points.

**Look at the degree first.** If the degree is **even** (like $x^{2}$, $x^{4}$, $x^{6}$), the two arms of the graph both point in the same direction — either both up or both down. Think of the parabola $y = x^{2}$ or the quartic $y = x^{4}$: both ends rise. If the degree is **odd** (like $x^{3}$, $x^{5}$), the arms point in opposite directions — one rising, one falling. Think of $y = x^{3}$, where the left arm plunges into the third quadrant and the right arm climbs into the first.

**Then look at the sign of the leading coefficient.** A positive leading coefficient means the right arm points up (as $x \to +\infty$, $y \to +\infty$). A negative leading coefficient flips that: the right arm points down. Combining the two rules:

| Degree | Leading coeff. | Left arm ($x \to -\infty$) | Right arm ($x \to +\infty$) |
|---|---|---|---|
| Even | Positive | $y \to +\infty$ | $y \to +\infty$ |
| Even | Negative | $y \to -\infty$ | $y \to -\infty$ |
| Odd | Positive | $y \to -\infty$ | $y \to +\infty$ |
| Odd | Negative | $y \to +\infty$ | $y \to -\infty$ |

Why does this work? For very large $|x|$, the leading term $a_{n} x^{n}$ swamps every other term in the polynomial. A polynomial like $-2x^{4} + 5x^{2} - 1$ evaluated at $x = 100$ is dominated by $-2 \cdot 100^{4}$ — the $5x^{2}$ and $-1$ become relatively invisible. So end behavior is really a question about one term, not the whole polynomial.

---

## Zeros and multiplicity: where and how the graph meets the x-axis

A **zero** of $p(x)$ — sometimes called a **root** — is a number $c$ where $p(c) = 0$. Geometrically, zeros are the $x$-intercepts of the graph: the points where it crosses or touches the horizontal axis. A powerful fact you inherit from the Factor Theorem is that $c$ is a zero of $p$ exactly when $(x - c)$ is a factor of the polynomial. So once you have $p$ in factored form, its zeros stare right back at you.

Here is where **multiplicity** enters. If you write $p$ in factored form and the factor $(x - c)$ appears raised to a power $k$, then $c$ is said to be a zero of multiplicity $k$. For instance, in

$$
p(x) = (x - 2)^{3}(x + 5)^{2}(x - 1),
$$

the zero $x = 2$ has multiplicity $3$, the zero $x = -5$ has multiplicity $2$, and the zero $x = 1$ has multiplicity $1$.

Multiplicity matters because it controls how the graph meets the $x$-axis at each zero:

- When the multiplicity is an **odd** number (like $1$, $3$, or $5$), the graph passes straight through the $x$-axis at that zero — it enters from one side and leaves on the other.
- When the multiplicity is an **even** number (like $2$, $4$, or $6$), the graph only kisses the $x$-axis at that zero and bounces right back where it came from — it does not change sign.
- When the multiplicity is $3$ or higher, the graph flattens out near the zero before crossing (or before bouncing, for high even multiplicities). The flatter the zero, the higher its multiplicity.

A polynomial of degree $n$ can have at most $n$ real zeros in total, counting multiplicity. It can also have fewer real zeros than $n$ — some zeros might be complex — but the total (counted with multiplicity) will never exceed the degree.

---

## Y-intercept and turning points

Besides end behavior and zeros, two other features round out the shape of a polynomial graph.

The **$y$-intercept** is the easiest feature to find: plug in $x = 0$ and read off $p(0)$. Because every term except the constant $a_{0}$ has an $x$ in it, they all vanish, leaving you with $p(0) = a_{0}$. The constant term of the polynomial is always the $y$-intercept.

A **turning point** is a place on the graph where the direction changes — the curve stops climbing and starts falling, or stops falling and starts climbing. These are the local high and low points of the graph. A polynomial of degree $n$ has at most $n - 1$ turning points. A cubic can have $0$ or $2$ turning points; a quartic can have $1$ or $3$. You cannot always tell the exact count from the formula alone, but the degree gives you a ceiling.

Combining all four features — end behavior, zeros with multiplicities, the $y$-intercept, and a rough guess at turning points — is usually enough to draw a clean sketch of any polynomial you encounter.

---

## Example 1: reading features off a polynomial in standard form

> Let $p(x) = -2x^{3} + 5x^{2} + x - 4$. Identify the degree, leading coefficient, end behavior, and $y$-intercept.

The highest power of $x$ that appears is $x^{3}$, so the **degree** is $3$. The coefficient in front of that highest power is $-2$, so the **leading coefficient** is $-2$.

Because the degree $3$ is odd, the two arms of the graph head in opposite directions. Because the leading coefficient $-2$ is negative, the right arm points down. So as $x \to +\infty$, $y \to -\infty$, and as $x \to -\infty$, $y \to +\infty$. In plain terms: the graph rises on the left and falls on the right.

For the **$y$-intercept**, plug in $x = 0$ and watch every term with an $x$ disappear:

$$
p(0) = -2(0)^{3} + 5(0)^{2} + 0 - 4 = -4.
$$

So the curve crosses the $y$-axis at $(0, -4)$, which you could have spotted directly as the constant term. Without computing a single zero, you already know the curve comes down from the upper-left, passes through $(0, -4)$, and continues falling off into the lower-right.

---

## Example 2: zeros and multiplicities from factored form

> For $p(x) = (x - 2)^{2}(x + 3)(x - 1)$, list every zero, give its multiplicity, and describe whether the graph crosses or touches the $x$-axis at each.

The factored form makes this easy. Each factor $(x - c)^{k}$ contributes the zero $c$ with multiplicity $k$.

- The factor $(x - 2)^{2}$ gives a zero at $x = 2$ with multiplicity $2$. Because $2$ is even, the graph **touches** the $x$-axis at $x = 2$ and bounces back — it does not cross.
- The factor $(x + 3)$ gives a zero at $x = -3$ with multiplicity $1$. Because $1$ is odd, the graph **crosses** the $x$-axis at $x = -3$, straight through.
- The factor $(x - 1)$ gives a zero at $x = 1$ with multiplicity $1$. Same story: the graph **crosses** the $x$-axis at $x = 1$.

The total of the multiplicities is $2 + 1 + 1 = 4$, which equals the degree of the polynomial. (If you expanded everything out, the leading term would be $x^{4}$.) Since $4$ is even and the leading coefficient is positive, both arms of the graph point upward. Putting it all together: the graph comes down from the upper-left, crosses at $x = -3$, crosses again at $x = 1$, dips down between $x = 1$ and $x = 2$, touches the $x$-axis at $x = 2$ without crossing, and then climbs back up into the upper-right.

---

## Example 3: sketching from factored form

> Describe what the graph of $q(x) = (x + 2)(x - 1)^{3}$ looks like. Include end behavior, zeros with multiplicities, the $y$-intercept, and the overall shape.

Start with the **degree and leading term**. If you imagined expanding, the highest power of $x$ comes from multiplying $x$ out of each factor, and the exponent $3$ on $(x - 1)$ contributes three copies. So the leading term is $x \cdot x^{3} = x^{4}$. Degree $4$, leading coefficient $+1$. Both arms point up.

Next, the **zeros**:

- $x = -2$ with multiplicity $1$ (odd). The graph crosses cleanly at $x = -2$.
- $x = 1$ with multiplicity $3$ (odd, but with a flattening). The graph crosses at $x = 1$, but the high multiplicity makes the crossing look stretched — the curve flattens out horizontally right at the zero before continuing.

The **$y$-intercept** is $q(0) = (2)(-1)^{3} = 2 \cdot (-1) = -2$, so the curve passes through $(0, -2)$.

Now sketch. The graph comes down from the upper-left (both arms up), crosses the $x$-axis at $x = -2$, dives into negative territory, passes through $(0, -2)$, and continues to $x = 1$ where it crosses the axis with a flattened inflection, then turns upward and heads off to $+\infty$. A polynomial of degree $4$ has at most $4 - 1 = 3$ turning points, and this one has exactly $1$ turning point (the dip between the two zeros). The combination of end behavior plus multiplicities is usually enough to produce a sketch this precise without a single test value.

---

## Common pitfalls

- **Missing the sign flip from the leading coefficient.** Degree alone does not decide end behavior — you also need the sign of the leading coefficient. A negative leading coefficient reverses both arms compared to the baseline pattern.
- **Reading the multiplicity wrong from standard form.** Multiplicity is only visible once you have factored the polynomial. Looking at coefficients in standard form cannot tell you which zeros bounce and which cross.
- **Forgetting that a high-multiplicity zero still only counts as one $x$-intercept.** The graph touches (or flattens at) that one location, even if the factor is raised to the fifth power. The zero does not produce multiple separate intercepts.
- **Assuming every zero of a polynomial is real.** A polynomial of degree $n$ has at most $n$ real zeros, but some may be complex numbers that do not show up on the $x$-axis at all. A degree-$4$ graph with only two $x$-intercepts is perfectly normal.

---

## Prerequisites

Before tackling practice problems on this topic, be comfortable with:

- [[Quadratic_Functions]] — the degree-$2$ baseline, where end behavior and turning points already make an appearance
- [[Factoring_Completely]] — because multiplicity only reveals itself in factored form
- [[Function_Basics]] — for the input-output language and notation used throughout
- [[Plotting_Points_And_The_Coordinate_Plane]] — so you can turn a sketch plan into an actual drawing

---

## Problems Involving Polynomial Functions and Graphs

Pick a problem type, pick a difficulty, pick how many you want, and click **Add to Vault**. Your choices are remembered in this browser, and you can build up a full practice set before opening your [[Vault]] to review hints, answers, or print a worksheet.

<div class="problem-vault-widget" data-topic-slug="polynomial_functions_and_graphs"></div>

---

## See Also

- [[Quadratic_Functions]] — the degree-$2$ case, written out in full
- [[Power_Functions]] — the single-term building blocks $y = k x^{n}$
- [[Factoring_Completely]] — how to get from standard form into factored form
- [[Transformations_I_Shifts_And_Reflections]] — shifting and flipping polynomial graphs
- [[Algebra_Overview|Algebra]]
- [[Topics_Overview]]
- [[_overview|Home]]
