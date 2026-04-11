"""Simplifying algebraic expressions: combine like terms, distribute, monomials.

Canonical topic slug ``simplifying_expressions`` at
wiki/topics/pre_algebra/Simplifying_Expressions.md.

- combine_like_terms_two_vars: collect $ax$, $by$, and constant terms
- distribute_and_combine: expand $a(bx + c) + dx + e$ to $(ab + d)x + (ac + e)$
- multiply_constant_term_generic: multiply monomials like $3x^2 \\cdot 4x^3$

Every generator uses backward construction: pick the final simplified
answer first, then derive operands or scatter terms that reduce to it.
No retry loops.
"""
from __future__ import annotations

import random

from ..base import Difficulty, Generator, Problem, make_problem_id, register


TOPIC_SLUG = "simplifying_expressions"

_BASES = ("x", "y", "m", "a", "p")

_TAGS = [
    "#branch-pre-algebra",
    "#topic-numbers-and-operations",
    "#skill-algebraic-manipulation",
]


def _term_with_coef(coef: int, var: str) -> str:
    """Render a signed coefficient times a variable.

    - ``1 * x`` -> ``x``
    - ``-1 * x`` -> ``-x``
    - ``3 * x`` -> ``3x``
    - ``-3 * x`` -> ``-3x``
    - ``0 * x`` -> ``0`` (caller should check first)
    """
    if coef == 0:
        return "0"
    if coef == 1:
        return var
    if coef == -1:
        return f"-{var}"
    return f"{coef}{var}"


def _join_with_signs(terms: list[str]) -> str:
    """Join pre-rendered terms with space-padded signs.

    Each term in ``terms`` may start with ``-`` or have no sign (positive).
    The first term is emitted as-is; each subsequent term uses
    `` + `` or `` - `` based on its leading character.
    """
    if not terms:
        return "0"
    out = [terms[0]]
    for t in terms[1:]:
        if t.startswith("-"):
            out.append(f" - {t[1:]}")
        else:
            out.append(f" + {t}")
    return "".join(out)


def _render_final(a_x: int, a_y: int, const: int) -> str:
    """Render $ax + by + c$ in simplified form, dropping zero terms."""
    parts: list[str] = []
    if a_x != 0:
        parts.append(_term_with_coef(a_x, "x"))
    if a_y != 0:
        parts.append(_term_with_coef(a_y, "y"))
    if const != 0:
        parts.append(str(const))
    if not parts:
        return "0"
    # Recompose with signs: first part keeps its sign, rest get " + "/" - ".
    out = [parts[0]]
    for p in parts[1:]:
        if p.startswith("-"):
            out.append(f" - {p[1:]}")
        else:
            out.append(f" + {p}")
    return "".join(out)


def _render_final_single_var(a: int, const: int, var: str) -> str:
    """Render $ax + c$ in a single variable, dropping zero terms."""
    parts: list[str] = []
    if a != 0:
        parts.append(_term_with_coef(a, var))
    if const != 0:
        parts.append(str(const))
    if not parts:
        return "0"
    out = [parts[0]]
    for p in parts[1:]:
        if p.startswith("-"):
            out.append(f" - {p[1:]}")
        else:
            out.append(f" + {p}")
    return "".join(out)


# ---------------------------------------------------------------------------

@register
class CombineLikeTermsTwoVars(Generator):
    """Simplify an expression with $x$-terms, $y$-terms, and constants.

    Backward construction: pick the final ``(a_x, a_y, const)``, then
    scatter each coefficient across two positive/negative chunks that
    sum to the target. Always at least two non-zero coefficients so the
    answer is non-trivial.
    """
    generator_id = "combine_like_terms_two_vars"
    topic_slug = TOPIC_SLUG
    display_name = "Combine like terms in a two-variable expression"

    _RANGES = {
        "easy":   {"final": (1, 6),  "split": (1, 5)},
        "medium": {"final": (2, 9),  "split": (2, 7)},
        "hard":   {"final": (2, 12), "split": (3, 9)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        f_lo, f_hi = r["final"]
        s_lo, s_hi = r["split"]

        # Pick targets; sign each one. f_lo >= 1 ensures every target != 0.
        a_x = rng.choice([-1, 1]) * rng.randint(f_lo, f_hi)
        a_y = rng.choice([-1, 1]) * rng.randint(f_lo, f_hi)
        const = rng.choice([-1, 1]) * rng.randint(f_lo, f_hi)

        # Split each non-zero target into two non-zero pieces that sum to it.
        # piece1 = signed mag from [s_lo, s_hi]; piece2 = target - piece1.
        # If piece2 would be 0, flip piece1's sign (guaranteed non-zero since
        # s_lo >= 1, so piece1 is never 0, and -piece1 is also never 0,
        # so piece2 = target - piece1 is nonzero unless piece1 = target —
        # detected once, corrected deterministically).
        def split_target(target: int) -> tuple[int, int]:
            mag = rng.randint(s_lo, s_hi)
            sign = rng.choice([-1, 1])
            piece1 = sign * mag
            piece2 = target - piece1
            if piece2 == 0:
                # Flip sign to guarantee a non-zero second piece.
                piece1 = -piece1
                piece2 = target - piece1
            return piece1, piece2

        x1, x2 = split_target(a_x)
        y1, y2 = split_target(a_y)
        c1, c2 = split_target(const)

        # Interleave the six terms in a fixed but shuffled order
        # (parameter tuple determines the seed-driven permutation).
        order = [
            ("x", x1), ("y", y1), ("c", c1),
            ("x", x2), ("y", y2), ("c", c2),
        ]
        rng.shuffle(order)

        rendered: list[str] = []
        for kind, coef in order:
            if kind == "c":
                rendered.append(str(coef))
            else:
                rendered.append(_term_with_coef(coef, kind))

        statement_body = _join_with_signs(rendered)
        answer_latex = _render_final(a_x, a_y, const)

        # Param tuple — the target triple plus piece splits uniquely
        # identify the statement (the shuffle is seed-determined too).
        params = (a_x, a_y, const, x1, y1, c1)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, params),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement_body}$.",
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"Group terms that share the same variable — "
                    r"all the $x$-terms together, all the $y$-terms "
                    r"together, and all the constants together."
                ),
                (
                    r"Inside each group, add the coefficients. The answer "
                    r"is written as a single $x$-term, a single $y$-term, "
                    r"and a single constant."
                ),
                (
                    f"Here the $x$-coefficients sum to ${a_x}$, the "
                    f"$y$-coefficients sum to ${a_y}$, and the constants "
                    f"sum to ${const}$."
                ),
            ],
            solution_steps_latex=[
                (
                    r"Group the like terms: $x$-terms with $x$-terms, "
                    r"$y$-terms with $y$-terms, constants with constants."
                ),
                (
                    f"Sum the $x$-coefficients to get ${a_x}$, the "
                    f"$y$-coefficients to get ${a_y}$, and the constants "
                    f"to get ${const}$."
                ),
                f"Write the simplified expression: ${answer_latex}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class DistributeAndCombine(Generator):
    """Simplify $a(bx + c) + dx + e$ into a single $(px + q)$ form.

    Backward construction: pick targets $p$ (non-zero final $x$-coefficient)
    and $q$ (final constant) first, then pick inner factors $a, b, c$
    and derive $d = p - ab$ and $e = q - ac$. This guarantees a clean
    two-term answer with at least a non-zero $x$-term.
    """
    generator_id = "distribute_and_combine"
    topic_slug = TOPIC_SLUG
    display_name = "Distribute a constant and combine like terms"

    _RANGES = {
        "easy":   {"a": (2, 5), "b": (1, 5), "c": (1, 6),  "p": (2, 8),  "q": (1, 10)},
        "medium": {"a": (2, 7), "b": (1, 7), "c": (1, 9),  "p": (2, 12), "q": (1, 15)},
        "hard":   {"a": (2, 9), "b": (1, 9), "c": (2, 12), "p": (3, 18), "q": (2, 20)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        a = rng.randint(*r["a"])
        b = rng.randint(*r["b"])
        c = rng.randint(*r["c"])
        # Target coefficients for the simplified answer (sign at random).
        p = rng.choice([-1, 1]) * rng.randint(*r["p"])
        q = rng.choice([-1, 1]) * rng.randint(*r["q"])
        d = p - a * b
        e = q - a * c

        var = rng.choice(_BASES)

        bx_term = _term_with_coef(b, var)
        # Inner expression `(bx + c)` — c is always positive here.
        inner_latex = f"({bx_term} + {c})"
        a_latex = f"{a}" if a != 1 else ""
        first_chunk = f"{a_latex}{inner_latex}"

        # Build `first_chunk + dx + e` with proper signs.
        tail_parts: list[str] = []
        if d != 0:
            dx = _term_with_coef(d, var)
            if dx.startswith("-"):
                tail_parts.append(f" - {dx[1:]}")
            else:
                tail_parts.append(f" + {dx}")
        if e != 0:
            if e >= 0:
                tail_parts.append(f" + {e}")
            else:
                tail_parts.append(f" - {-e}")

        statement_body = first_chunk + "".join(tail_parts)
        answer_latex = _render_final_single_var(p, q, var)

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d, e, var)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${statement_body}$.",
            answer_latex=f"${answer_latex}$",
            hints=[
                (
                    r"Distribute the constant in front of the parentheses "
                    r"to every term inside."
                ),
                (
                    f"After distributing, combine like terms: add the "
                    f"coefficients of ${var}$ together and add the "
                    f"constants together."
                ),
                (
                    f"Here the ${var}$-coefficient is ${a} \\cdot {b} + ({d}) = {p}$ "
                    f"and the constant is ${a} \\cdot {c} + ({e}) = {q}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Distribute: ${a}({bx_term} + {c}) = "
                    f"{_term_with_coef(a * b, var)} + {a * c}$."
                ),
                f"Rewrite the full expression: ${_term_with_coef(a * b, var)} + {a * c}{''.join(tail_parts)}$.",
                (
                    f"Combine like terms: ${var}$-coefficients give "
                    f"${a * b} + ({d}) = {p}$, constants give "
                    f"${a * c} + ({e}) = {q}$."
                ),
                f"Final simplified expression: ${answer_latex}$.",
            ],
            tags=list(_TAGS),
        )


# ---------------------------------------------------------------------------

@register
class MultiplyConstantTermGeneric(Generator):
    """Simplify $(c_1 x^{n_1})(c_2 x^{n_2})$ to $(c_1 c_2) x^{n_1 + n_2}$.

    Distinct from the exponent-rule generators: these have explicit
    coefficients and blend multiplication-of-integers with the product
    rule for exponents.
    """
    generator_id = "multiply_constant_term_generic"
    topic_slug = TOPIC_SLUG
    display_name = "Simplify a product of two single-variable monomials"

    _RANGES = {
        "easy":   {"c": (2, 6),  "n": (1, 4)},   # 5 bases * 25 coef * 16 exp = 2000
        "medium": {"c": (2, 9),  "n": (1, 6)},
        "hard":   {"c": (2, 12), "n": (2, 8)},
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        r = self._RANGES[difficulty]
        var = rng.choice(_BASES)
        c1 = rng.randint(*r["c"])
        c2 = rng.randint(*r["c"])
        n1 = rng.randint(*r["n"])
        n2 = rng.randint(*r["n"])

        coef_product = c1 * c2
        exp_sum = n1 + n2

        def _monomial(coef: int, exponent: int) -> str:
            if exponent == 0:
                return str(coef)
            base_part = var if exponent == 1 else f"{var}^{{{exponent}}}"
            if coef == 1:
                return base_part
            return f"{coef}{base_part}"

        left = _monomial(c1, n1)
        right = _monomial(c2, n2)
        answer = _monomial(coef_product, exp_sum)

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (var, c1, n1, c2, n2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=f"Simplify ${left} \\cdot {right}$.",
            answer_latex=f"${answer}$",
            hints=[
                (
                    r"When multiplying two monomials, multiply the "
                    r"coefficients together and apply the product rule "
                    r"to the powers: $x^m \cdot x^n = x^{m+n}$."
                ),
                f"Here the coefficients are ${c1}$ and ${c2}$, so multiply them: "
                f"${c1} \\cdot {c2} = {coef_product}$.",
                f"The exponents are ${n1}$ and ${n2}$, so add them: "
                f"${n1} + {n2} = {exp_sum}$.",
            ],
            solution_steps_latex=[
                (
                    r"Multiply the coefficients and apply the product rule "
                    r"to the powers: "
                    r"$(c_1 x^{n_1})(c_2 x^{n_2}) = (c_1 c_2) x^{n_1 + n_2}$."
                ),
                f"Compute the coefficient product: ${c1} \\cdot {c2} = {coef_product}$.",
                f"Compute the exponent sum: ${n1} + {n2} = {exp_sum}$.",
                f"Therefore ${left} \\cdot {right} = {answer}$.",
            ],
            tags=list(_TAGS),
        )
