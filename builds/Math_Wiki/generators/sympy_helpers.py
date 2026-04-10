"""SymPy utilities shared across generators.

Phase 1 relies on simple structural verification; Phase 3 adds deep
round-trip checks (parse answer LaTeX, re-solve, compare symbolically).
"""
from __future__ import annotations

import sympy as sp


def safe_parse_expr(expr_str: str) -> sp.Expr | None:
    """Attempt to parse a plain (non-LaTeX) expression string.

    Returns None on failure rather than raising.
    """
    try:
        return sp.sympify(expr_str)
    except (sp.SympifyError, SyntaxError, TypeError):
        return None


def symbols_xy() -> tuple[sp.Symbol, sp.Symbol]:
    """Convenience: return the symbols x and y."""
    return sp.Symbol("x"), sp.Symbol("y")


def circle_standard_form(h: int, k: int, r: int) -> sp.Expr:
    """Build the SymPy expression `(x - h)^2 + (y - k)^2 - r^2`.

    Equals zero on the circle. Useful for verification.
    """
    x, y = symbols_xy()
    return (x - h) ** 2 + (y - k) ** 2 - r * r
