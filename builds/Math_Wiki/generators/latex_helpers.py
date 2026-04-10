"""LaTeX formatting helpers for numbers, expressions, and signed terms.

These helpers assume the output will be rendered by KaTeX inside
inline math contexts (e.g., `$...$`).
"""
from __future__ import annotations


def shift_expr(var: str, shift: int) -> str:
    """Format a shifted variable `(var op n)` with correct sign handling.

    >>> shift_expr('x', 3)
    '(x - 3)'
    >>> shift_expr('y', -2)
    '(y + 2)'
    >>> shift_expr('x', 0)
    'x'
    """
    if shift == 0:
        return var
    op = "-" if shift > 0 else "+"
    return f"({var} {op} {abs(shift)})"


def signed_int(n: int) -> str:
    """Format an integer with an explicit leading sign.

    >>> signed_int(3)
    '+3'
    >>> signed_int(-5)
    '-5'
    >>> signed_int(0)
    '+0'
    """
    return f"+{n}" if n >= 0 else f"{n}"


def format_point(x, y) -> str:
    """Format a 2D point as `(x, y)`.

    >>> format_point(3, -2)
    '(3, -2)'
    """
    return f"({x}, {y})"


def format_fraction(numerator: int, denominator: int) -> str:
    """Render a fraction, simplifying to an integer when denominator is 1.

    >>> format_fraction(3, 4)
    '\\\\frac{3}{4}'
    >>> format_fraction(6, 1)
    '6'
    """
    if denominator == 0:
        raise ValueError("denominator cannot be zero")
    if denominator == 1:
        return str(numerator)
    if denominator == -1:
        return str(-numerator)
    return rf"\frac{{{numerator}}}{{{denominator}}}"
