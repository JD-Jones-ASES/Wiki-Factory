"""Matrix generators (pre-calculus cluster).

Four topic slugs covered:

- matrix_arithmetic           (Matrix_Arithmetic.md)
- augmented_matrices          (Augmented_Matrices.md)
- determinants                (Determinants.md)
- matrix_methods              (Matrix_Methods.md)

Twelve generators total (3 per topic). Backward construction is used
throughout: for arithmetic and determinant problems we pick clean integer
entries directly; for systems and inverses we pick the solution (or the
inverse) first and derive the statement so every answer is a clean integer
vector or a matrix with integer entries.

sympy's ``Matrix`` class is used for every computation so the numerical
results are exact. LaTeX is rendered with ``\\begin{pmatrix}...\\end{pmatrix}``
for matrices and ``\\left[\\begin{array}{cc|c}...\\end{array}\\right]`` for
augmented matrices, both of which render cleanly in KaTeX.
"""
from __future__ import annotations

import random

import sympy as sp

from ..base import Difficulty, Generator, Problem, make_problem_id, register


MATRIX_TAGS = ["#branch-pre-calculus", "#topic-matrices"]


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _pmatrix(rows: list[list]) -> str:
    """Render a 2D list of numeric entries as a LaTeX pmatrix.

    >>> _pmatrix([[1, 2], [3, 4]])
    '\\\\begin{pmatrix} 1 & 2 \\\\\\\\ 3 & 4 \\\\end{pmatrix}'
    """
    body = " \\\\ ".join(" & ".join(str(entry) for entry in row) for row in rows)
    return r"\begin{pmatrix} " + body + r" \end{pmatrix}"


def _pmatrix_sym(M: sp.Matrix) -> str:
    """Render a sympy matrix as a LaTeX pmatrix via ``sp.latex`` entries."""
    rows, cols = M.shape
    row_strs: list[str] = []
    for i in range(rows):
        row_strs.append(" & ".join(sp.latex(M[i, j]) for j in range(cols)))
    body = " \\\\ ".join(row_strs)
    return r"\begin{pmatrix} " + body + r" \end{pmatrix}"


def _aug_matrix(coeff_rows: list[list], rhs: list) -> str:
    """Render a 2x2 augmented matrix as ``\\left[\\begin{array}{cc|c}...\\end{array}\\right]``.

    ``coeff_rows`` is a list of 2 rows, each a list of 2 coefficients.
    ``rhs`` is a list of 2 right-hand-side values.
    """
    lines: list[str] = []
    for row, b in zip(coeff_rows, rhs):
        lines.append(" & ".join(str(v) for v in row) + " & " + str(b))
    body = " \\\\ ".join(lines)
    return r"\left[\begin{array}{cc|c} " + body + r" \end{array}\right]"


def _col_vector(entries: list) -> str:
    """Render a column vector as a LaTeX pmatrix."""
    body = " \\\\ ".join(str(e) for e in entries)
    return r"\begin{pmatrix} " + body + r" \end{pmatrix}"


def _signed_int(n: int) -> str:
    """Return n with an explicit sign, e.g. 3 -> '+3', -5 -> '-5'."""
    return f"+{n}" if n >= 0 else str(n)


def _term(coeff: int, var: str, is_first: bool) -> str:
    """Render a signed term in a linear combination.

    Used to build statements like ``3x - 2y = 5`` from coefficient lists.
    Handles coefficient magnitudes of 1 (hidden), signs, and leading terms.
    """
    if coeff == 0:
        return ""
    if is_first:
        if coeff == 1:
            return var
        if coeff == -1:
            return f"-{var}"
        return f"{coeff}{var}"
    # non-first: explicit ' + ' or ' - '
    if coeff > 0:
        sign = " + "
    else:
        sign = " - "
    mag = abs(coeff)
    if mag == 1:
        return f"{sign}{var}"
    return f"{sign}{mag}{var}"


def _linear_equation(a: int, b: int, c: int) -> str:
    """Render ``ax + by = c`` cleanly, hiding zero and unit coefficients."""
    if a == 0 and b == 0:
        return f"0 = {c}"
    parts: list[str] = []
    if a != 0:
        parts.append(_term(a, "x", True))
        if b != 0:
            parts.append(_term(b, "y", False))
    else:
        parts.append(_term(b, "y", True))
    return "".join(parts) + f" = {c}"


# ===========================================================================
# Topic 1: matrix_arithmetic
# ===========================================================================


@register
class MatrixAddSubtract(Generator):
    """Add or subtract two matrices of the same shape (2x2 or 2x3).

    Backward: pick clean integer entries in a shape-appropriate range, then
    compute the sum or difference directly with ``sp.Matrix``.
    """
    generator_id = "matrix_add_subtract"
    topic_slug = "matrix_arithmetic"
    display_name = "Add or subtract two matrices"

    _ENTRY_RANGES = {"easy": (-5, 5), "medium": (-9, 9), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]
        shape = rng.choice([(2, 2), (2, 3)])
        op = rng.choice(["+", "-"])

        rows, cols = shape
        entries_A = [[rng.randint(lo, hi) for _ in range(cols)] for _ in range(rows)]
        entries_B = [[rng.randint(lo, hi) for _ in range(cols)] for _ in range(rows)]
        A = sp.Matrix(entries_A)
        B = sp.Matrix(entries_B)
        result = A + B if op == "+" else A - B

        op_word = "sum" if op == "+" else "difference"
        statement = (
            f"Let $A = {_pmatrix(entries_A)}$ and $B = {_pmatrix(entries_B)}$. "
            f"Compute the {op_word} $A {op} B$."
        )
        answer = f"$A {op} B = {_pmatrix_sym(result)}$"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (shape, op, tuple(map(tuple, entries_A)), tuple(map(tuple, entries_B))),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "Matrices of the same shape are added or subtracted "
                    "entry-by-entry."
                ),
                (
                    f"Compute each entry as $a_{{ij}} {op} b_{{ij}}$ and place it "
                    "in the corresponding position of the result."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Both matrices are ${rows}\\times {cols}$, so the operation is "
                    "defined."
                ),
                (
                    "Add (or subtract) corresponding entries: "
                    "$(A " + op + " B)_{ij} = a_{ij} " + op + " b_{ij}$."
                ),
                (
                    f"The result is ${_pmatrix_sym(result)}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class MatrixScalarMultiply(Generator):
    """Multiply a matrix by a scalar ``cA``. Backward: pick clean entries."""
    generator_id = "matrix_scalar_multiply"
    topic_slug = "matrix_arithmetic"
    display_name = "Multiply a matrix by a scalar"

    _ENTRY_RANGES = {"easy": (-6, 6), "medium": (-9, 9), "hard": (-12, 12)}
    _SCALAR_CHOICES = {
        "easy": (2, 3, -2, -3),
        "medium": (2, 3, 4, 5, -2, -3, -4),
        "hard": (2, 3, 4, 5, 6, 7, -2, -3, -4, -5, -6),
    }

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]
        shape = rng.choice([(2, 2), (2, 3)])
        rows, cols = shape
        entries = [[rng.randint(lo, hi) for _ in range(cols)] for _ in range(rows)]
        c = rng.choice(self._SCALAR_CHOICES[difficulty])
        A = sp.Matrix(entries)
        result = c * A

        statement = (
            f"Let $A = {_pmatrix(entries)}$ and $c = {c}$. Compute $cA$."
        )
        answer = f"$cA = {_pmatrix_sym(result)}$"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (shape, c, tuple(map(tuple, entries))),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Scalar multiplication distributes over every entry: "
                    r"$(cA)_{ij} = c\, a_{ij}$."
                ),
                (
                    f"Multiply every entry of $A$ by ${c}$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Write $cA = {c} \\cdot {_pmatrix(entries)}$."
                ),
                (
                    f"Multiply each entry by ${c}$, which gives "
                    f"${_pmatrix_sym(result)}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class MatrixMultiply2x2(Generator):
    """Multiply two 2x2 matrices. Backward with small integer entries."""
    generator_id = "matrix_multiply_2x2"
    topic_slug = "matrix_arithmetic"
    display_name = "Multiply two 2x2 matrices"

    bank_count_per_difficulty = 25

    _ENTRY_RANGES = {"easy": (-3, 4), "medium": (-5, 5), "hard": (-7, 7)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        d = rng.randint(lo, hi)
        e = rng.randint(lo, hi)
        f = rng.randint(lo, hi)
        g = rng.randint(lo, hi)
        h = rng.randint(lo, hi)

        entries_A = [[a, b], [c, d]]
        entries_B = [[e, f], [g, h]]
        A = sp.Matrix(entries_A)
        B = sp.Matrix(entries_B)
        product = A * B

        statement = (
            f"Let $A = {_pmatrix(entries_A)}$ and $B = {_pmatrix(entries_B)}$. "
            f"Compute the product $AB$."
        )
        answer = f"$AB = {_pmatrix_sym(product)}$"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, c, d, e, f, g, h),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"The $(i,j)$ entry of $AB$ is the dot product of row $i$ of "
                    r"$A$ with column $j$ of $B$."
                ),
                (
                    r"For $2\times 2$ matrices: "
                    r"$(AB)_{11} = a_{11}b_{11} + a_{12}b_{21}$, and similarly "
                    r"for the other three entries."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Compute entry $(1,1)$: $({a})({e}) + ({b})({g}) = "
                    rf"{a*e + b*g}$."
                ),
                (
                    rf"Compute entry $(1,2)$: $({a})({f}) + ({b})({h}) = "
                    rf"{a*f + b*h}$."
                ),
                (
                    rf"Compute entry $(2,1)$: $({c})({e}) + ({d})({g}) = "
                    rf"{c*e + d*g}$."
                ),
                (
                    rf"Compute entry $(2,2)$: $({c})({f}) + ({d})({h}) = "
                    rf"{c*f + d*h}$."
                ),
                (
                    f"Assemble the product: $AB = {_pmatrix_sym(product)}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


# ===========================================================================
# Topic 2: augmented_matrices
# ===========================================================================


@register
class AugmentedMatrixFromSystem(Generator):
    """Given a 2x2 linear system, write its augmented matrix form.

    Backward: pick integer coefficients and a known integer solution, then
    derive the right-hand side so the system is consistent.
    """
    generator_id = "augmented_matrix_from_system"
    topic_slug = "augmented_matrices"
    display_name = "Write the augmented matrix of a 2x2 system"

    _COEFF_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}
    _SOL_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEFF_RANGES[difficulty]
        s_lo, s_hi = self._SOL_RANGES[difficulty]

        # Draw nonzero coefficients so the equations actually involve both vars
        def _nonzero() -> int:
            while True:
                v = rng.randint(c_lo, c_hi)
                if v != 0:
                    return v

        a1 = _nonzero()
        b1 = _nonzero()
        a2 = _nonzero()
        b2 = _nonzero()

        # Pick a clean integer solution
        x0 = rng.randint(s_lo, s_hi)
        y0 = rng.randint(s_lo, s_hi)
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 + b2 * y0

        eq1 = _linear_equation(a1, b1, c1)
        eq2 = _linear_equation(a2, b2, c2)

        aug_latex = _aug_matrix([[a1, b1], [a2, b2]], [c1, c2])

        statement = (
            "Write the augmented matrix for the following linear system:\n\n"
            f"$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$"
        )
        answer = f"${aug_latex}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a1, b1, c1, a2, b2, c2)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "Each row of the augmented matrix holds the coefficients of one "
                    "equation, followed by its right-hand side."
                ),
                (
                    "Order the columns as [coefficient of $x$, coefficient of $y$, "
                    "constant]. Use a vertical bar to separate coefficients from "
                    "the constant."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Read coefficients from equation 1: $a_1 = {a1}$, "
                    f"$b_1 = {b1}$, constant $= {c1}$."
                ),
                (
                    f"Read coefficients from equation 2: $a_2 = {a2}$, "
                    f"$b_2 = {b2}$, constant $= {c2}$."
                ),
                (
                    f"Stack them into the augmented matrix: ${aug_latex}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class RowOperationApply(Generator):
    """Apply a specified elementary row operation to a 2x2 augmented matrix.

    Three operation types: swap rows, scale a row by a constant, or replace
    $R_j$ with $R_j + k R_i$. Backward: pick clean integer entries and a
    clean operation.
    """
    generator_id = "row_operation_apply"
    topic_slug = "augmented_matrices"
    display_name = "Apply a row operation to a 2x2 augmented matrix"

    bank_count_per_difficulty = 20

    _ENTRY_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-9, 9)}
    _SCALE_CHOICES = {"easy": (2, 3, -2), "medium": (2, 3, 4, -2, -3), "hard": (2, 3, 4, 5, -2, -3, -4)}
    _K_CHOICES = {"easy": (-2, -1, 1, 2), "medium": (-3, -2, -1, 1, 2, 3), "hard": (-4, -3, -2, -1, 1, 2, 3, 4)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]

        def _nonzero() -> int:
            while True:
                v = rng.randint(lo, hi)
                if v != 0:
                    return v

        a, b, e = _nonzero(), rng.randint(lo, hi), rng.randint(lo, hi)
        c, d, f = _nonzero(), rng.randint(lo, hi), rng.randint(lo, hi)

        op_type = rng.choice(["swap", "scale", "replace"])

        rows_in = [[a, b], [c, d]]
        rhs_in = [e, f]
        start_latex = _aug_matrix(rows_in, rhs_in)

        if op_type == "swap":
            rows_out = [rows_in[1], rows_in[0]]
            rhs_out = [rhs_in[1], rhs_in[0]]
            op_latex = r"R_1 \leftrightarrow R_2"
            op_word = (
                "Swap rows 1 and 2 ($R_1 \\leftrightarrow R_2$)."
            )
            step_line = "Exchange the two rows; all entries move together."
            params = ("swap",)
        elif op_type == "scale":
            k = rng.choice(self._SCALE_CHOICES[difficulty])
            target_row = rng.choice([1, 2])
            if target_row == 1:
                rows_out = [[k * a, k * b], rows_in[1]]
                rhs_out = [k * e, rhs_in[1]]
            else:
                rows_out = [rows_in[0], [k * c, k * d]]
                rhs_out = [rhs_in[0], k * f]
            op_latex = rf"R_{target_row} \to {k} R_{target_row}"
            op_word = (
                f"Scale row {target_row} by ${k}$ ($R_{target_row} "
                f"\\to {k} R_{target_row}$)."
            )
            step_line = f"Multiply every entry of row {target_row} by ${k}$."
            params = ("scale", k, target_row)
        else:  # replace
            k = rng.choice(self._K_CHOICES[difficulty])
            # Replace R2 with R2 + k*R1 (or vice versa).
            direction = rng.choice([1, 2])
            if direction == 2:
                new_row = [c + k * a, d + k * b]
                new_rhs = f + k * e
                rows_out = [rows_in[0], new_row]
                rhs_out = [rhs_in[0], new_rhs]
                op_latex = rf"R_2 \to R_2 + ({k}) R_1"
                op_word = (
                    f"Replace row 2 with $R_2 + ({k}) R_1$."
                )
                step_line = (
                    f"Add ${k}$ times row 1 to row 2, entry by entry."
                )
            else:
                new_row = [a + k * c, b + k * d]
                new_rhs = e + k * f
                rows_out = [new_row, rows_in[1]]
                rhs_out = [new_rhs, rhs_in[1]]
                op_latex = rf"R_1 \to R_1 + ({k}) R_2"
                op_word = (
                    f"Replace row 1 with $R_1 + ({k}) R_2$."
                )
                step_line = (
                    f"Add ${k}$ times row 2 to row 1, entry by entry."
                )
            params = ("replace", k, direction)

        result_latex = _aug_matrix(rows_out, rhs_out)

        statement = (
            f"Apply the row operation ${op_latex}$ to the augmented matrix "
            f"${start_latex}$. Give the resulting matrix."
        )
        answer = f"${result_latex}$"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, c, d, e, f) + params,
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "Elementary row operations act on the entire augmented row, "
                    "including the rightmost constant column."
                ),
                (
                    op_word
                ),
            ],
            solution_steps_latex=[
                (
                    f"Identify the operation: ${op_latex}$."
                ),
                (
                    step_line
                ),
                (
                    f"The resulting augmented matrix is ${result_latex}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class GaussianElimination2x2(Generator):
    """Gaussian elimination on a 2x2 augmented matrix.

    Backward: pick the solution $(x_0, y_0)$ first, then draw two linear
    combinations with integer coefficients so the system is guaranteed
    consistent and the row-echelon form clears cleanly.
    """
    generator_id = "gaussian_elimination_2x2"
    topic_slug = "augmented_matrices"
    display_name = "Solve a 2x2 system by Gaussian elimination"

    _COEFF_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}
    _SOL_RANGES = {"easy": (-5, 5), "medium": (-7, 7), "hard": (-9, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEFF_RANGES[difficulty]
        s_lo, s_hi = self._SOL_RANGES[difficulty]

        # Backward: pick solution and invertible coefficient matrix.
        for _ in range(50):
            a1 = rng.randint(c_lo, c_hi)
            if a1 == 0:
                continue
            b1 = rng.randint(c_lo, c_hi)
            a2 = rng.randint(c_lo, c_hi)
            b2 = rng.randint(c_lo, c_hi)
            det = a1 * b2 - b1 * a2
            if det != 0:
                break
        else:
            # Fallback to a known-good system
            a1, b1, a2, b2 = 1, 1, 1, -1

        x0 = rng.randint(s_lo, s_hi)
        y0 = rng.randint(s_lo, s_hi)
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 + b2 * y0

        aug_start = _aug_matrix([[a1, b1], [a2, b2]], [c1, c2])

        # Build a clean worked-solution path using exact sympy arithmetic.
        A_aug = sp.Matrix([[a1, b1, c1], [a2, b2, c2]])
        # After reaching row-echelon form via sympy's rref, we render the final
        # echelon form and back-substitute.
        rref, _pivots = A_aug.rref()
        final_rref_rows = [
            [rref[0, 0], rref[0, 1]],
            [rref[1, 0], rref[1, 1]],
        ]
        final_rref_rhs = [rref[0, 2], rref[1, 2]]
        rref_latex = _aug_matrix(final_rref_rows, final_rref_rhs)

        eq1 = _linear_equation(a1, b1, c1)
        eq2 = _linear_equation(a2, b2, c2)

        statement = (
            "Solve the linear system by Gaussian elimination:\n\n"
            f"$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$"
        )
        answer = f"$x = {x0},\\ y = {y0}$"

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a1, b1, a2, b2, x0, y0)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "Write the augmented matrix and use row operations to reach "
                    "row-echelon form."
                ),
                (
                    "Eliminate the $x$-coefficient in row 2 first; then solve for "
                    "$y$ and back-substitute into row 1 to find $x$."
                ),
            ],
            solution_steps_latex=[
                (
                    f"Write the augmented matrix: ${aug_start}$."
                ),
                (
                    "Use elementary row operations (scaling and row replacement) "
                    "to eliminate the entry below the first pivot."
                ),
                (
                    f"Continue until the matrix is in reduced row-echelon form: "
                    f"${rref_latex}$."
                ),
                (
                    f"Read off the solution: $x = {x0}$ and $y = {y0}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


# ===========================================================================
# Topic 3: determinants
# ===========================================================================


@register
class Determinant2x2(Generator):
    """Compute det = ad - bc for a 2x2 matrix with integer entries."""
    generator_id = "determinant_2x2"
    topic_slug = "determinants"
    display_name = "Compute the determinant of a 2x2 matrix"

    _ENTRY_RANGES = {"easy": (-6, 6), "medium": (-9, 9), "hard": (-12, 12)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]
        a = rng.randint(lo, hi)
        b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        d = rng.randint(lo, hi)
        det = a * d - b * c

        mat_latex = _pmatrix([[a, b], [c, d]])
        statement = f"Compute the determinant of $A = {mat_latex}$."
        answer = rf"$\det A = {det}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"For a $2\times 2$ matrix $\begin{pmatrix} a & b \\ c & d "
                    r"\end{pmatrix}$, the determinant is $ad - bc$."
                ),
                (
                    "Multiply the main-diagonal entries, then subtract the "
                    "product of the anti-diagonal entries."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Identify $a = {a}$, $b = {b}$, $c = {c}$, $d = {d}$."
                ),
                (
                    rf"Compute $ad - bc = ({a})({d}) - ({b})({c}) "
                    rf"= {a*d} - {b*c} = {det}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class Determinant3x3Cofactor(Generator):
    """Compute a 3x3 determinant by cofactor expansion along row 1.

    Backward: pick small integer entries in a tight range so the expansion
    lands on a clean integer.
    """
    generator_id = "determinant_3x3_cofactor"
    topic_slug = "determinants"
    display_name = "Compute a 3x3 determinant by cofactor expansion"

    bank_count_per_difficulty = 18

    _ENTRY_RANGES = {"easy": (-3, 3), "medium": (-4, 4), "hard": (-5, 5)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]
        entries = [[rng.randint(lo, hi) for _ in range(3)] for _ in range(3)]
        M = sp.Matrix(entries)
        det = int(M.det())

        a11, a12, a13 = entries[0]
        # First-row minors
        M11 = sp.Matrix(
            [[entries[1][1], entries[1][2]], [entries[2][1], entries[2][2]]]
        )
        M12 = sp.Matrix(
            [[entries[1][0], entries[1][2]], [entries[2][0], entries[2][2]]]
        )
        M13 = sp.Matrix(
            [[entries[1][0], entries[1][1]], [entries[2][0], entries[2][1]]]
        )
        d11, d12, d13 = int(M11.det()), int(M12.det()), int(M13.det())

        mat_latex = _pmatrix(entries)
        statement = (
            "Compute the determinant of the following matrix by cofactor "
            f"expansion along the first row:\n\n$$A = {mat_latex}$$"
        )
        answer = rf"$\det A = {det}$"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                tuple(v for row in entries for v in row),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    "Expanding along the first row: "
                    r"$\det A = a_{11} M_{11} - a_{12} M_{12} + a_{13} M_{13}$, "
                    r"where $M_{1j}$ is the $2\times 2$ minor obtained by "
                    "deleting row 1 and column $j$."
                ),
                (
                    "Watch the alternating sign pattern $+, -, +$ on the three "
                    "terms."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Compute the first minor $M_{{11}} = "
                    rf"\det{_pmatrix_sym(M11)} = {d11}$."
                ),
                (
                    rf"Compute the second minor $M_{{12}} = "
                    rf"\det{_pmatrix_sym(M12)} = {d12}$."
                ),
                (
                    rf"Compute the third minor $M_{{13}} = "
                    rf"\det{_pmatrix_sym(M13)} = {d13}$."
                ),
                (
                    rf"Assemble: $\det A = ({a11})({d11}) - ({a12})({d12}) + "
                    rf"({a13})({d13}) = {det}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class DeterminantSingularCheck(Generator):
    """Decide whether a 2x2 matrix is singular (det = 0) or invertible.

    Mixes both cases: half the time we pick entries that force det = 0 by
    making the rows proportional; the other half we draw generic entries and
    accept whatever determinant arises (rejected if accidentally zero).
    """
    generator_id = "determinant_singular_check"
    topic_slug = "determinants"
    display_name = "Decide whether a 2x2 matrix is singular or invertible"

    bank_count_per_difficulty = 20

    _ENTRY_RANGES = {"easy": (-5, 5), "medium": (-7, 7), "hard": (-9, 9)}
    _SCALE_CHOICES = (-3, -2, 2, 3)

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        lo, hi = self._ENTRY_RANGES[difficulty]
        make_singular = rng.choice([True, False])

        if make_singular:
            # Row 2 is a (nonzero) scalar multiple of row 1.
            for _ in range(40):
                a = rng.randint(lo, hi)
                b = rng.randint(lo, hi)
                if (a, b) == (0, 0):
                    continue
                k = rng.choice(self._SCALE_CHOICES)
                c, d = k * a, k * b
                if abs(c) <= hi + 2 and abs(d) <= hi + 2:
                    break
            else:
                a, b, c, d = 1, 2, 2, 4
        else:
            for _ in range(40):
                a = rng.randint(lo, hi)
                b = rng.randint(lo, hi)
                c = rng.randint(lo, hi)
                d = rng.randint(lo, hi)
                if a * d - b * c != 0:
                    break
            else:
                a, b, c, d = 1, 0, 0, 1

        det = a * d - b * c
        is_singular = det == 0
        mat_latex = _pmatrix([[a, b], [c, d]])

        if is_singular:
            answer_word = "singular"
            conclusion = (
                rf"Since $\det A = 0$, the matrix is singular (not invertible)."
            )
        else:
            answer_word = "invertible"
            conclusion = (
                rf"Since $\det A = {det} \neq 0$, the matrix is invertible."
            )

        statement = (
            f"Is the matrix $A = {mat_latex}$ singular or invertible? "
            "Support your answer by computing $\\det A$."
        )
        answer = rf"$\det A = {det}$; the matrix is {answer_word}."

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"A square matrix is invertible exactly when its determinant "
                    r"is nonzero; if $\det A = 0$, the matrix is singular."
                ),
                (
                    r"For a $2\times 2$ matrix, compute $\det A = ad - bc$ and "
                    "compare with zero."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Compute the determinant: $\det A = ({a})({d}) - ({b})({c}) "
                    rf"= {det}$."
                ),
                (
                    conclusion
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


# ===========================================================================
# Topic 4: matrix_methods
# ===========================================================================


def _draw_unimodular(rng: random.Random, difficulty: Difficulty) -> tuple[int, int, int, int]:
    """Return (a, b, c, d) with ad - bc = +-1.

    A simpler, more robust generator than ``_draw_unit_det_matrix``: seed
    with a list of base unimodular matrices and apply a small random row
    replacement to introduce variety.
    """
    base_matrices = [
        (1, 0, 0, 1),
        (1, 0, 0, -1),
        (-1, 0, 0, 1),
        (0, 1, 1, 0),
        (0, 1, -1, 0),
        (0, -1, 1, 0),
    ]
    noise_ranges = {"easy": (-2, 2), "medium": (-3, 3), "hard": (-4, 4)}
    k_lo, k_hi = noise_ranges[difficulty]

    a, b, c, d = rng.choice(base_matrices)
    # Apply a few elementary row operations (R1 -> R1 + k*R2 and vice versa)
    # which preserve the determinant.
    op_count = {"easy": 2, "medium": 3, "hard": 4}[difficulty]
    for _ in range(op_count):
        if rng.random() < 0.5:
            k = rng.randint(k_lo, k_hi)
            a += k * c
            b += k * d
        else:
            k = rng.randint(k_lo, k_hi)
            c += k * a
            d += k * b
    return a, b, c, d


@register
class MatrixInverse2x2(Generator):
    """Compute the inverse of a 2x2 matrix with $\\det = \\pm 1$."""
    generator_id = "matrix_inverse_2x2"
    topic_slug = "matrix_methods"
    display_name = "Compute the inverse of a 2x2 matrix"

    bank_count_per_difficulty = 20

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c, d = _draw_unimodular(rng, difficulty)
        det = a * d - b * c  # +-1 by construction
        # Inverse = (1/det) * [[d, -b], [-c, a]]
        inv_entries = [[det * d, -det * b], [-det * c, det * a]]

        mat_latex = _pmatrix([[a, b], [c, d]])
        inv_latex = _pmatrix(inv_entries)

        statement = (
            f"Compute the inverse of $A = {mat_latex}$. (You may assume "
            "$\\det A \\neq 0$.)"
        )
        answer = f"$A^{{-1}} = {inv_latex}$"

        return Problem(
            id=make_problem_id(self.generator_id, difficulty, (a, b, c, d)),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"For a $2\times 2$ matrix, the inverse formula is "
                    r"$A^{-1} = \dfrac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a "
                    r"\end{pmatrix}$."
                ),
                (
                    "Swap the main-diagonal entries, negate the anti-diagonal "
                    "entries, and divide by the determinant."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Compute the determinant: $\det A = ({a})({d}) - ({b})({c}) "
                    rf"= {det}$."
                ),
                (
                    rf"Form the adjugate: $\begin{{pmatrix}} d & -b \\ -c & a "
                    rf"\end{{pmatrix}} = \begin{{pmatrix}} {d} & {-b} \\ {-c} & "
                    rf"{a} \end{{pmatrix}}$."
                ),
                (
                    rf"Divide by $\det A = {det}$ to obtain "
                    rf"$A^{{-1}} = {inv_latex}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class SolveSystemViaInverse(Generator):
    """Solve $A\\vec{x} = \\vec{b}$ via $\\vec{x} = A^{-1}\\vec{b}$.

    Backward: pick a unimodular $A$ and an integer solution $\\vec{x}$, then
    compute $\\vec{b} = A\\vec{x}$.
    """
    generator_id = "solve_system_via_inverse"
    topic_slug = "matrix_methods"
    display_name = "Solve a 2x2 system via the matrix inverse"

    bank_count_per_difficulty = 18

    _SOL_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        a, b, c, d = _draw_unimodular(rng, difficulty)
        det = a * d - b * c
        s_lo, s_hi = self._SOL_RANGES[difficulty]
        x0 = rng.randint(s_lo, s_hi)
        y0 = rng.randint(s_lo, s_hi)
        b1 = a * x0 + b * y0
        b2 = c * x0 + d * y0

        inv_entries = [[det * d, -det * b], [-det * c, det * a]]

        A_latex = _pmatrix([[a, b], [c, d]])
        b_latex = _col_vector([b1, b2])
        inv_latex = _pmatrix(inv_entries)

        statement = (
            f"Use the inverse of $A = {A_latex}$ to solve $A\\vec{{x}} = "
            f"\\vec{{b}}$, where $\\vec{{b}} = {b_latex}$."
        )
        answer = (
            rf"$\vec{{x}} = \begin{{pmatrix}} {x0} \\ {y0} \end{{pmatrix}}$"
        )

        return Problem(
            id=make_problem_id(
                self.generator_id, difficulty, (a, b, c, d, x0, y0)
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Multiplying $A\vec{x} = \vec{b}$ on the left by $A^{-1}$ "
                    r"yields $\vec{x} = A^{-1}\vec{b}$."
                ),
                (
                    r"Compute $A^{-1}$ using the $2\times 2$ inverse formula, "
                    r"then multiply it by $\vec{b}$."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Compute $\det A = ({a})({d}) - ({b})({c}) = {det}$, so "
                    r"$A$ is invertible."
                ),
                (
                    rf"Apply the inverse formula: $A^{{-1}} = {inv_latex}$."
                ),
                (
                    rf"Multiply: $\vec{{x}} = A^{{-1}}\vec{{b}} = {inv_latex} "
                    rf"{b_latex} = \begin{{pmatrix}} {x0} \\ {y0} "
                    rf"\end{{pmatrix}}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )


@register
class CramersRule2x2(Generator):
    """Solve a 2x2 linear system using Cramer's rule.

    Backward: pick an integer solution $(x_0, y_0)$ and an invertible
    coefficient matrix so every determinant is clean.
    """
    generator_id = "cramers_rule_2x2"
    topic_slug = "matrix_methods"
    display_name = "Solve a 2x2 system using Cramer's rule"

    bank_count_per_difficulty = 20

    _COEFF_RANGES = {"easy": (-4, 4), "medium": (-6, 6), "hard": (-8, 8)}
    _SOL_RANGES = {"easy": (-5, 5), "medium": (-7, 7), "hard": (-9, 9)}

    def _generate_one(self, difficulty: Difficulty, rng: random.Random) -> Problem:
        c_lo, c_hi = self._COEFF_RANGES[difficulty]
        s_lo, s_hi = self._SOL_RANGES[difficulty]

        for _ in range(80):
            a = rng.randint(c_lo, c_hi)
            b = rng.randint(c_lo, c_hi)
            c = rng.randint(c_lo, c_hi)
            d = rng.randint(c_lo, c_hi)
            det = a * d - b * c
            if det == 0:
                continue
            x0 = rng.randint(s_lo, s_hi)
            y0 = rng.randint(s_lo, s_hi)
            e = a * x0 + b * y0
            f = c * x0 + d * y0
            # Prefer clean integer solutions: ensure det divides both numerators.
            # By construction x0 and y0 are integers, so det*x0 and det*y0 are
            # divisible by det. Just verify for safety.
            if (d * e - b * f) == det * x0 and (a * f - c * e) == det * y0:
                break
        else:
            a, b, c, d, x0, y0 = 1, 0, 0, 1, 1, 1
            e, f = a * x0 + b * y0, c * x0 + d * y0
            det = a * d - b * c

        det_x = d * e - b * f
        det_y = a * f - c * e

        eq1 = _linear_equation(a, b, e)
        eq2 = _linear_equation(c, d, f)

        A_latex = _pmatrix([[a, b], [c, d]])
        Ax_latex = _pmatrix([[e, b], [f, d]])
        Ay_latex = _pmatrix([[a, e], [c, f]])

        statement = (
            "Use Cramer's rule to solve the linear system:\n\n"
            f"$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$"
        )
        answer = f"$x = {x0},\\ y = {y0}$"

        return Problem(
            id=make_problem_id(
                self.generator_id,
                difficulty,
                (a, b, c, d, e, f),
            ),
            generator_id=self.generator_id,
            topic_slug=self.topic_slug,
            difficulty=difficulty,
            statement_latex=statement,
            answer_latex=answer,
            hints=[
                (
                    r"Cramer's rule: $x = \dfrac{\det A_x}{\det A}$ and "
                    r"$y = \dfrac{\det A_y}{\det A}$, where $A_x$ (resp. $A_y$) "
                    r"is $A$ with its first (resp. second) column replaced by "
                    r"the right-hand side."
                ),
                (
                    r"Compute $\det A$ first; if it is zero, Cramer's rule does "
                    "not apply."
                ),
            ],
            solution_steps_latex=[
                (
                    rf"Form the coefficient matrix $A = {A_latex}$ and compute "
                    rf"$\det A = ({a})({d}) - ({b})({c}) = {det}$."
                ),
                (
                    rf"Replace column 1 of $A$ with the constants: "
                    rf"$A_x = {Ax_latex}$, so $\det A_x = {det_x}$."
                ),
                (
                    rf"Replace column 2 of $A$ with the constants: "
                    rf"$A_y = {Ay_latex}$, so $\det A_y = {det_y}$."
                ),
                (
                    rf"Apply Cramer's rule: $x = \dfrac{{{det_x}}}{{{det}}} = "
                    rf"{x0}$ and $y = \dfrac{{{det_y}}}{{{det}}} = {y0}$."
                ),
            ],
            tags=list(MATRIX_TAGS),
        )
