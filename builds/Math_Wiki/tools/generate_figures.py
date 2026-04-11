#!/usr/bin/env python3
"""Generate matplotlib SVG figures for Math Wiki topic pages.

Run from builds/Math_Wiki/:

    py -3 tools/generate_figures.py

Figures land in wiki/assets/figures/<branch>/<name>.svg. Each figure is
deterministic (no random elements) so regenerating gives identical output
and diffs only when the generator code actually changes.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Make SVG clip-path / pattern IDs deterministic across runs so regenerated
# figures are byte-identical when the figure code hasn't changed.
plt.rcParams["svg.hashsalt"] = "math-wiki"


ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = ROOT / "wiki" / "assets" / "figures"

# Consistent color palette used across all figures (matches Hymn Wiki theme)
C_LINE = "#284b63"     # primary circle / curve color
C_CENTER = "#84a59d"   # center marker
C_RADIUS = "#c44569"   # radius highlight
C_DASH = "#555555"     # dashed auxiliary lines
C_TEXT = "#2b2b2b"     # label text
C_GRID = "#dddddd"     # grid lines


def _save(fig, rel_path: str):
    out = FIGURES_DIR / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    # Fixed metadata so regenerated SVGs are byte-identical across runs.
    fig.savefig(
        out,
        format="svg",
        bbox_inches="tight",
        metadata={"Date": None, "Creator": "Math Wiki figure generator"},
    )
    plt.close(fig)
    print(f"  wrote {out.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# Geometry: circles

def fig_circle_parts():
    """A labeled circle: center, radius, diameter, chord."""
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect("equal")
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.6, 2.6)
    ax.axhline(0, color=C_GRID, linewidth=0.5, zorder=0)
    ax.axvline(0, color=C_GRID, linewidth=0.5, zorder=0)

    # The circle itself (radius 2)
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(2 * np.cos(theta), 2 * np.sin(theta), color=C_LINE, linewidth=2.2)

    # Center dot
    ax.plot(0, 0, "o", color=C_CENTER, markersize=9, zorder=3)
    ax.annotate("center", xy=(0, 0), xytext=(0.12, 0.15),
                fontsize=11, color=C_TEXT)

    # Radius line (to upper-right point)
    angle_r = np.pi / 6  # 30 degrees
    rx, ry = 2 * np.cos(angle_r), 2 * np.sin(angle_r)
    ax.plot([0, rx], [0, ry], color=C_RADIUS, linewidth=2.5)
    ax.annotate("r", xy=(rx / 2 - 0.05, ry / 2 + 0.15),
                fontsize=15, color=C_RADIUS, fontweight="bold")

    # Diameter (dashed, horizontal)
    ax.plot([-2, 2], [0, 0], color=C_DASH, linewidth=1.3, linestyle="--")
    ax.annotate("d = 2r", xy=(-1.8, -0.25), fontsize=11, color=C_DASH)

    ax.set_title("Parts of a Circle", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "geometry/circle_parts.svg")


# ---------------------------------------------------------------------------
# Pre-algebra: number line

def fig_number_line():
    """An integer number line from -10 to +10 with labeled ticks."""
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlim(-11.5, 11.5)
    ax.set_ylim(-1.2, 1.4)

    # Main axis line (without built-in arrows) + arrow heads via annotate
    ax.annotate(
        "", xy=(11.3, 0), xytext=(-11.3, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=2),
    )

    # Ticks + labels at each integer from -10..10
    for x in range(-10, 11):
        if x == 0:
            # Thicker tick for zero
            ax.plot([x, x], [-0.28, 0.28], color=C_LINE, linewidth=3)
        else:
            ax.plot([x, x], [-0.18, 0.18], color=C_LINE, linewidth=1.3)
        ax.text(x, -0.55, str(x), ha="center", va="top",
                fontsize=10, color=C_TEXT)

    ax.set_title("Integers on the Number Line", fontsize=14, pad=10)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "pre_algebra/number_line.svg")


# ---------------------------------------------------------------------------
# Pre-algebra: fraction bar (equivalent fractions)

def fig_fraction_bar():
    """Two bars: 3/8 and equivalent 6/16, same shaded proportion."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.5, 2.3)
    ax.set_aspect("auto")

    fill_color = C_RADIUS  # warm highlight
    fill_alpha = 0.35

    # --- Top bar: 3/8 ---
    top_y, bar_h = 1.55, 0.45
    parts_top = 8
    shaded_top = 3
    for i in range(parts_top):
        x0 = i / parts_top
        x1 = (i + 1) / parts_top
        if i < shaded_top:
            ax.fill_between([x0, x1], top_y, top_y + bar_h,
                            color=fill_color, alpha=fill_alpha, linewidth=0)
        # cell outline
        ax.plot([x0, x1, x1, x0, x0],
                [top_y, top_y, top_y + bar_h, top_y + bar_h, top_y],
                color=C_LINE, linewidth=1.5)
    ax.text(0.5, top_y - 0.18, "3/8", ha="center", va="top",
            fontsize=14, color=C_TEXT, fontweight="bold")

    # --- Bottom bar: 6/16 ---
    bot_y = 0.35
    parts_bot = 16
    shaded_bot = 6
    for i in range(parts_bot):
        x0 = i / parts_bot
        x1 = (i + 1) / parts_bot
        if i < shaded_bot:
            ax.fill_between([x0, x1], bot_y, bot_y + bar_h,
                            color=fill_color, alpha=fill_alpha, linewidth=0)
        ax.plot([x0, x1, x1, x0, x0],
                [bot_y, bot_y, bot_y + bar_h, bot_y + bar_h, bot_y],
                color=C_LINE, linewidth=1.2)
    ax.text(0.5, bot_y - 0.18, "6/16 = 3/8", ha="center", va="top",
            fontsize=14, color=C_TEXT, fontweight="bold")

    ax.set_title("A Fraction of a Whole", fontsize=14, pad=10)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "pre_algebra/fraction_bar.svg")


# ---------------------------------------------------------------------------
# Pre-algebra: area model for the distributive property

def fig_area_model_distributive():
    """Area model for 3(4 + 2) = 3*4 + 3*2 = 12 + 6 = 18."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_aspect("equal")

    a = 3  # height
    b = 4  # left width
    c = 2  # right width
    total_w = b + c

    ax.set_xlim(-0.9, total_w + 0.6)
    ax.set_ylim(-1.3, a + 1.2)

    # Left sub-rectangle (a x b) filled
    ax.fill_between([0, b], 0, a, color=C_GRID, alpha=0.7, linewidth=0)
    # Right sub-rectangle (a x c) filled slightly differently via edge only
    ax.fill_between([b, total_w], 0, a, color=C_GRID, alpha=0.4, linewidth=0)

    # Outer rectangle outline
    ax.plot([0, total_w, total_w, 0, 0],
            [0, 0, a, a, 0], color=C_LINE, linewidth=2.2)
    # Dashed vertical split
    ax.plot([b, b], [0, a], color=C_DASH, linewidth=1.8, linestyle="--")

    # Height label on the left
    ax.annotate("", xy=(-0.25, a), xytext=(-0.25, 0),
                arrowprops=dict(arrowstyle="<->", color=C_TEXT, lw=1.2))
    ax.text(-0.45, a / 2, "3", ha="right", va="center",
            fontsize=13, color=C_TEXT, fontweight="bold")

    # Width labels on top of each sub-rectangle
    ax.annotate("", xy=(b, a + 0.25), xytext=(0, a + 0.25),
                arrowprops=dict(arrowstyle="<->", color=C_TEXT, lw=1.2))
    ax.text(b / 2, a + 0.45, "4", ha="center", va="bottom",
            fontsize=13, color=C_TEXT, fontweight="bold")
    ax.annotate("", xy=(total_w, a + 0.25), xytext=(b, a + 0.25),
                arrowprops=dict(arrowstyle="<->", color=C_TEXT, lw=1.2))
    ax.text(b + c / 2, a + 0.45, "2", ha="center", va="bottom",
            fontsize=13, color=C_TEXT, fontweight="bold")

    # Area labels inside each sub-rectangle
    ax.text(b / 2, a / 2, "12", ha="center", va="center",
            fontsize=18, color=C_LINE, fontweight="bold")
    ax.text(b + c / 2, a / 2, "6", ha="center", va="center",
            fontsize=18, color=C_LINE, fontweight="bold")

    # Caption at the bottom
    ax.text(total_w / 2, -0.85,
            r"$3(4 + 2) = 3 \cdot 4 + 3 \cdot 2 = 12 + 6 = 18$",
            ha="center", va="center", fontsize=12, color=C_TEXT)

    ax.set_title("Distributive Property: Area Model", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "pre_algebra/area_model_distributive.svg")


# ---------------------------------------------------------------------------
# Pre-algebra: place value chart

def fig_place_value_chart():
    """Place value chart for the number 34.0806 with 'hundredths' highlighted."""
    # Columns: (header, digit, is_decimal_point, is_highlight)
    columns = [
        ("tens",            "3", False, False),
        ("ones",            "4", False, False),
        ("",                ".", True,  False),
        ("tenths",          "0", False, False),
        ("hundredths",      "8", False, True),
        ("thousandths",     "0", False, False),
        ("ten-thousandths", "6", False, False),
    ]

    n = len(columns)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_aspect("equal")

    cell_w = 1.0
    cell_h = 1.0
    header_h = 0.55
    total_w = n * cell_w

    ax.set_xlim(-0.4, total_w + 0.4)
    ax.set_ylim(-0.8, cell_h + header_h + 0.9)

    highlight = "#f6d365"  # warm highlight

    for i, (header, digit, is_dp, is_hl) in enumerate(columns):
        x0 = i * cell_w
        x1 = x0 + cell_w

        # Digit cell (bottom row)
        if not is_dp:
            if is_hl:
                ax.fill_between([x0, x1], 0, cell_h,
                                color=highlight, alpha=0.85, linewidth=0)
            ax.plot([x0, x1, x1, x0, x0],
                    [0, 0, cell_h, cell_h, 0],
                    color=C_LINE, linewidth=1.8)

        # Header cell (top row)
        if header:
            ax.plot([x0, x1, x1, x0, x0],
                    [cell_h, cell_h, cell_h + header_h,
                     cell_h + header_h, cell_h],
                    color=C_LINE, linewidth=1.4)
            ax.text(x0 + cell_w / 2, cell_h + header_h / 2, header,
                    ha="center", va="center",
                    fontsize=10, color=C_TEXT)

        # Digit or decimal point
        if is_dp:
            ax.text(x0 + cell_w / 2, cell_h / 2 - 0.18, ".",
                    ha="center", va="center",
                    fontsize=38, color=C_LINE, fontweight="bold")
        else:
            ax.text(x0 + cell_w / 2, cell_h / 2, digit,
                    ha="center", va="center",
                    fontsize=24, color=C_TEXT, fontweight="bold")

    ax.set_title("Place Value in 34.0806", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "pre_algebra/place_value_chart.svg")


# ---------------------------------------------------------------------------
# Algebra: coordinate plane

def fig_coordinate_plane():
    """A standard coordinate plane from -5 to 5 with four labeled example points."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)

    # Light grid at every integer
    for i in range(-5, 6):
        ax.plot([i, i], [-5, 5], color=C_GRID, linewidth=0.6, zorder=0)
        ax.plot([-5, 5], [i, i], color=C_GRID, linewidth=0.6, zorder=0)

    # x-axis and y-axis with arrowheads on both ends
    ax.annotate(
        "", xy=(5.5, 0), xytext=(-5.5, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.6),
    )
    ax.annotate(
        "", xy=(0, 5.5), xytext=(0, -5.5),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.6),
    )

    # Axis labels
    ax.text(5.7, 0.25, r"$x$", fontsize=14, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.25, 5.7, r"$y$", fontsize=14, color=C_TEXT,
            ha="left", va="bottom")

    # Origin label (lower-left of (0,0))
    ax.text(-0.25, -0.25, "O", fontsize=12, color=C_TEXT,
            ha="right", va="top", fontweight="bold")

    # Quadrant labels in the corners
    quadrant_color = "#8a8a8a"
    ax.text(4.5, 4.5, "I", fontsize=16, color=quadrant_color,
            ha="center", va="center", fontstyle="italic")
    ax.text(-4.5, 4.5, "II", fontsize=16, color=quadrant_color,
            ha="center", va="center", fontstyle="italic")
    ax.text(-4.5, -4.5, "III", fontsize=16, color=quadrant_color,
            ha="center", va="center", fontstyle="italic")
    ax.text(4.5, -4.5, "IV", fontsize=16, color=quadrant_color,
            ha="center", va="center", fontstyle="italic")

    # Example points: (coord, label, color)
    points = [
        ((3, 2), "A", "#2e86de"),    # blue
        ((-2, 3), "B", "#10ac84"),   # green
        ((-4, -1), "C", "#c44569"),  # red
        ((1, -3), "D", "#ee7c2a"),   # orange
    ]
    for (px, py), label, color in points:
        ax.plot(px, py, "o", color=color, markersize=9, zorder=4)
        ax.text(px + 0.25, py + 0.25, label, fontsize=13, color=color,
                ha="left", va="bottom", fontweight="bold")

    ax.set_title("The Coordinate Plane", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/coordinate_plane.svg")


# ---------------------------------------------------------------------------
# Algebra: inequality number line (4 stacked examples)

def fig_inequality_number_line():
    """Four stacked inequality number lines from -5 to 5."""
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    ax.set_xlim(-7.5, 6)
    ax.set_ylim(-0.6, 4.6)

    shade_color = C_RADIUS
    shade_alpha = 0.35

    # Each row: (y, label, draw callback)
    rows = [
        (4.0, r"$x > 2$"),
        (2.8, r"$x \leq -1$"),
        (1.6, r"$-2 < x \leq 3$"),
        (0.4, r"$x < 0$ or $x \geq 4$"),
    ]

    def draw_baseline(y):
        # Main line with arrow caps from -5 to 5
        ax.annotate(
            "", xy=(5.3, y), xytext=(-5.3, y),
            arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.6),
        )
        # Integer ticks
        for i in range(-5, 6):
            ax.plot([i, i], [y - 0.09, y + 0.09],
                    color=C_LINE, linewidth=1.0)
            ax.text(i, y - 0.33, str(i), ha="center", va="top",
                    fontsize=8, color=C_TEXT)

    def open_circle(x, y):
        ax.plot(x, y, "o", markerfacecolor="white",
                markeredgecolor=shade_color,
                markeredgewidth=2.2, markersize=11, zorder=4)

    def closed_circle(x, y):
        ax.plot(x, y, "o", color=shade_color, markersize=11, zorder=4)

    def shaded_ray(x_from, x_to, y):
        ax.plot([x_from, x_to], [y, y],
                color=shade_color, linewidth=4.0, alpha=0.75,
                solid_capstyle="round", zorder=3)

    # Row 1: x > 2
    y1 = rows[0][0]
    draw_baseline(y1)
    open_circle(2, y1)
    shaded_ray(2, 5.1, y1)

    # Row 2: x <= -1
    y2 = rows[1][0]
    draw_baseline(y2)
    closed_circle(-1, y2)
    shaded_ray(-1, -5.1, y2)

    # Row 3: -2 < x <= 3
    y3 = rows[2][0]
    draw_baseline(y3)
    open_circle(-2, y3)
    closed_circle(3, y3)
    shaded_ray(-2, 3, y3)

    # Row 4: x < 0 or x >= 4
    y4 = rows[3][0]
    draw_baseline(y4)
    open_circle(0, y4)
    shaded_ray(0, -5.1, y4)
    closed_circle(4, y4)
    shaded_ray(4, 5.1, y4)

    # Left-side row labels
    for y, label in rows:
        ax.text(-7.3, y, label, ha="left", va="center",
                fontsize=12, color=C_TEXT)

    ax.set_title("Graphing Inequalities on a Number Line",
                 fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/inequality_number_line.svg")


# ---------------------------------------------------------------------------
# Algebra: parallel & perpendicular lines

def fig_parallel_perpendicular_lines():
    """Coordinate plane showing two parallel lines and one perpendicular line."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)

    # Light grid
    for i in range(-5, 6):
        ax.plot([i, i], [-5, 5], color=C_GRID, linewidth=0.6, zorder=0)
        ax.plot([-5, 5], [i, i], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(5.5, 0), xytext=(-5.5, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 5.5), xytext=(0, -5.5),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(5.7, 0.25, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.25, 5.7, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")

    # x values for plotting lines
    xs = np.linspace(-5, 5, 200)

    # Line A: y = (1/2)x + 1 (solid blue)
    color_blue = "#2e86de"
    color_red = "#c44569"
    ya = 0.5 * xs + 1
    ax.plot(xs, ya, color=color_blue, linewidth=2.2, label="A")

    # Line B: y = (1/2)x - 2 (dashed blue, parallel)
    yb = 0.5 * xs - 2
    ax.plot(xs, yb, color=color_blue, linewidth=2.2, linestyle="--",
            label="B")

    # Line C: y = -2x + 3 (solid red, perpendicular)
    yc = -2 * xs + 3
    # Clip to the visible window so the label sits inside
    mask_c = (yc >= -5) & (yc <= 5)
    ax.plot(xs[mask_c], yc[mask_c], color=color_red, linewidth=2.2,
            label="C")

    # In-figure labels near each line
    ax.text(4.5, 0.5 * 4.5 + 1 + 0.25, r"A: $y = \frac{1}{2}x + 1$",
            fontsize=11, color=color_blue, ha="right", va="bottom")
    ax.text(4.5, 0.5 * 4.5 - 2 + 0.25, r"B: $y = \frac{1}{2}x - 2$",
            fontsize=11, color=color_blue, ha="right", va="bottom")
    ax.text(-0.2, -2 * (-0.2) + 3 + 0.35, r"C: $y = -2x + 3$",
            fontsize=11, color=color_red, ha="right", va="bottom")

    # Annotation box explaining the relationships
    info_text = (
        "A "
        + chr(0x2225)  # ∥
        + " B  (same slope)\n"
        + "A "
        + chr(0x22A5)  # ⊥
        + " C  (slopes multiply to -1)"
    )
    ax.text(-5.5, -5.4, info_text, fontsize=10, color=C_TEXT,
            ha="left", va="bottom",
            bbox=dict(boxstyle="round,pad=0.35",
                      facecolor="white",
                      edgecolor=C_DASH, linewidth=0.8))

    ax.set_title("Parallel and Perpendicular Lines", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/parallel_perpendicular_lines.svg")


# ---------------------------------------------------------------------------
# Algebra: scatter plot with trend line

def fig_scatter_trend_line():
    """Scatter plot of 10 data points with a fitted trend line."""
    # Local RNG so we don't leak state to other figure builders
    rng = np.random.RandomState(42)

    # 10 study-hours values spread across the range
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
    # y ≈ 1.5x + 2 with small deterministic jitter
    jitter = rng.normal(0.0, 1.2, size=x.shape)
    y = 1.5 * x + 2.0 + jitter

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 22)

    # Axis ticks visible here (this is a real plot, not a concept diagram)
    ax.set_xticks(range(0, 12, 2))
    ax.set_yticks(range(0, 23, 4))
    ax.tick_params(axis="both", colors=C_TEXT, labelsize=10)

    # Grid
    ax.grid(True, color=C_GRID, linewidth=0.7, zorder=0)

    # Scatter points (blue)
    ax.scatter(x, y, s=55, color="#2e86de",
               edgecolors="#1c4e80", linewidth=0.8, zorder=3)

    # Trend line: use the known generating slope/intercept so the line is
    # a clean positive straight line regardless of jitter details.
    xt = np.array([0.0, 11.0])
    yt = 1.5 * xt + 2.0
    ax.plot(xt, yt, color=C_RADIUS, linewidth=2.2, zorder=2,
            label="Trend line")

    ax.set_xlabel("Study Hours", fontsize=12, color=C_TEXT)
    ax.set_ylabel("Test Score", fontsize=12, color=C_TEXT)
    ax.set_title("Scatter Plot with Trend Line", fontsize=14, pad=12)

    for spine_name, spine in ax.spines.items():
        if spine_name in ("top", "right"):
            spine.set_visible(False)
        else:
            spine.set_color(C_LINE)
            spine.set_linewidth(1.2)

    _save(fig, "algebra/scatter_trend_line.svg")


# ---------------------------------------------------------------------------
# Algebra: area model for (x + 3)(x + 5)

def fig_area_model_multiplication():
    """Area model showing (x + 3)(x + 5) = x^2 + 5x + 3x + 15."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")

    # Use visual widths: x is drawn ~5 units, the constants at their numeric size
    x_vis = 5.0   # visual length standing in for the algebraic "x"
    left_w = x_vis
    right_w = 5.0
    bot_h = 3.0
    top_h = x_vis
    total_w = left_w + right_w
    total_h = bot_h + top_h

    ax.set_xlim(-1.6, total_w + 0.6)
    ax.set_ylim(-1.1, total_h + 1.4)

    # Pastel colors for the four sub-rectangles
    c_xx = "#cde4f0"     # x^2 (top-left)
    c_5x = "#fce1b7"     # 5x  (top-right)
    c_3x = "#d7ecd0"     # 3x  (bottom-left)
    c_15 = "#f4d0d6"     # 15  (bottom-right)

    # Coordinates of the four cells (top row is "x" tall, bottom row is "3" tall)
    # Top-left cell: x^2
    ax.fill_between([0, left_w], bot_h, total_h,
                    color=c_xx, linewidth=0)
    # Top-right cell: 5x
    ax.fill_between([left_w, total_w], bot_h, total_h,
                    color=c_5x, linewidth=0)
    # Bottom-left cell: 3x
    ax.fill_between([0, left_w], 0, bot_h,
                    color=c_3x, linewidth=0)
    # Bottom-right cell: 15
    ax.fill_between([left_w, total_w], 0, bot_h,
                    color=c_15, linewidth=0)

    # Outer rectangle outline
    ax.plot([0, total_w, total_w, 0, 0],
            [0, 0, total_h, total_h, 0],
            color=C_LINE, linewidth=2.2)
    # Inner dividers
    ax.plot([left_w, left_w], [0, total_h],
            color=C_LINE, linewidth=1.8)
    ax.plot([0, total_w], [bot_h, bot_h],
            color=C_LINE, linewidth=1.8)

    # Cell labels
    ax.text(left_w / 2, bot_h + top_h / 2, r"$x^{2}$",
            ha="center", va="center",
            fontsize=22, color=C_TEXT, fontweight="bold")
    ax.text(left_w + right_w / 2, bot_h + top_h / 2, r"$5x$",
            ha="center", va="center",
            fontsize=20, color=C_TEXT, fontweight="bold")
    ax.text(left_w / 2, bot_h / 2, r"$3x$",
            ha="center", va="center",
            fontsize=20, color=C_TEXT, fontweight="bold")
    ax.text(left_w + right_w / 2, bot_h / 2, r"$15$",
            ha="center", va="center",
            fontsize=20, color=C_TEXT, fontweight="bold")

    # Top side labels: x over the left column, 5 over the right column
    ax.text(left_w / 2, total_h + 0.35, r"$x$",
            ha="center", va="bottom",
            fontsize=15, color=C_TEXT, fontweight="bold")
    ax.text(left_w + right_w / 2, total_h + 0.35, r"$5$",
            ha="center", va="bottom",
            fontsize=15, color=C_TEXT, fontweight="bold")

    # Left side labels: x beside the top row, 3 beside the bottom row
    ax.text(-0.35, bot_h + top_h / 2, r"$x$",
            ha="right", va="center",
            fontsize=15, color=C_TEXT, fontweight="bold")
    ax.text(-0.35, bot_h / 2, r"$3$",
            ha="right", va="center",
            fontsize=15, color=C_TEXT, fontweight="bold")

    ax.set_title(r"Area model: $(x + 3)(x + 5)$", fontsize=14, pad=14)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/area_model_multiplication.svg")


# ---------------------------------------------------------------------------
# Algebra: the discriminant's three cases

def fig_discriminant_three_cases():
    """Three side-by-side parabolas showing Delta > 0, Delta = 0, Delta < 0."""
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 3.6))

    xs = np.linspace(-3, 3, 300)

    # Each panel: (y-values, label, x-intercepts to mark)
    panels = [
        (xs ** 2 - 4,
         r"$\Delta > 0$ (two real roots)",
         [-2.0, 2.0]),
        (xs ** 2,
         r"$\Delta = 0$ (one repeated root)",
         [0.0]),
        (xs ** 2 + 1,
         r"$\Delta < 0$ (no real roots)",
         []),
    ]

    for ax, (ys, label, roots) in zip(axes, panels):
        ax.set_xlim(-3, 3)
        ax.set_ylim(-5, 6)
        ax.set_aspect("equal")

        # Light grid
        for i in range(-3, 4):
            ax.plot([i, i], [-5, 6], color=C_GRID, linewidth=0.5, zorder=0)
        for i in range(-5, 7):
            ax.plot([-3, 3], [i, i], color=C_GRID, linewidth=0.5, zorder=0)

        # Axes with arrowheads
        ax.annotate(
            "", xy=(2.9, 0), xytext=(-2.9, 0),
            arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.2),
        )
        ax.annotate(
            "", xy=(0, 5.7), xytext=(0, -4.7),
            arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.2),
        )
        ax.text(2.95, 0.2, r"$x$", fontsize=10, color=C_TEXT,
                ha="right", va="bottom")
        ax.text(0.2, 5.7, r"$y$", fontsize=10, color=C_TEXT,
                ha="left", va="top")

        # Parabola
        ax.plot(xs, ys, color=C_LINE, linewidth=2.2)

        # Mark roots with red dots
        for r in roots:
            ax.plot(r, 0, "o", color=C_RADIUS,
                    markersize=8, zorder=4)

        ax.set_title(label, fontsize=10, color=C_TEXT, pad=6)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    fig.suptitle("The discriminant and the graph of a quadratic",
                 fontsize=14, y=1.02)
    fig.tight_layout()

    _save(fig, "algebra/discriminant_three_cases.svg")


# ---------------------------------------------------------------------------
# Algebra: parabola with vertex, axis of symmetry, intercepts

def fig_parabola_vertex_axis_of_symmetry():
    """Parabola y = x^2 - 4x + 1 with vertex, axis of symmetry, intercepts."""
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.set_aspect("equal")
    ax.set_xlim(-2.4, 6.4)
    ax.set_ylim(-4.6, 6.4)

    # Light grid
    for i in range(-2, 7):
        ax.plot([i, i], [-4.5, 6.5], color=C_GRID,
                linewidth=0.5, zorder=0)
    for j in range(-4, 7):
        ax.plot([-2.5, 6.5], [j, j], color=C_GRID,
                linewidth=0.5, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(6.2, 0), xytext=(-2.2, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 6.2), xytext=(0, -4.4),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(6.3, 0.25, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.25, 6.3, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")

    # Integer tick labels on x-axis
    for xt in range(-2, 7):
        if xt == 0:
            continue
        ax.text(xt, -0.3, str(xt), ha="center", va="top",
                fontsize=8, color=C_TEXT)

    # Axis of symmetry x = 2 (dashed vertical line)
    ax.plot([2, 2], [-4.5, 6.3], color=C_DASH,
            linewidth=1.6, linestyle="--", zorder=1)
    ax.text(2.15, 5.6, r"Axis of symmetry $x = 2$",
            fontsize=10, color=C_DASH, ha="left", va="top")

    # Parabola y = x^2 - 4x + 1
    xs = np.linspace(-1.2, 5.2, 400)
    ys = xs ** 2 - 4 * xs + 1
    ax.plot(xs, ys, color=C_LINE, linewidth=2.4, zorder=2)

    # Vertex (2, -3): red dot + label
    ax.plot(2, -3, "o", color=C_RADIUS, markersize=10, zorder=4)
    ax.annotate("Vertex $(2, -3)$",
                xy=(2, -3), xytext=(2.5, -3.8),
                fontsize=11, color=C_RADIUS, fontweight="bold",
                arrowprops=dict(arrowstyle="->",
                                color=C_RADIUS, lw=1.0))

    # y-intercept (0, 1): blue dot + label
    color_blue = "#2e86de"
    ax.plot(0, 1, "o", color=color_blue, markersize=9, zorder=4)
    ax.annotate(r"$y$-intercept $(0, 1)$",
                xy=(0, 1), xytext=(-2.0, 2.6),
                fontsize=10, color=color_blue, fontweight="bold",
                arrowprops=dict(arrowstyle="->",
                                color=color_blue, lw=1.0))

    # Roots at 2 - sqrt(3) and 2 + sqrt(3)
    sqrt3 = np.sqrt(3.0)
    root_color = "#10ac84"
    r1 = 2.0 - sqrt3
    r2 = 2.0 + sqrt3
    ax.plot(r1, 0, "o", color=root_color, markersize=8, zorder=4)
    ax.plot(r2, 0, "o", color=root_color, markersize=8, zorder=4)
    ax.annotate("roots",
                xy=(r2, 0), xytext=(4.5, 1.4),
                fontsize=10, color=root_color, fontweight="bold",
                arrowprops=dict(arrowstyle="->",
                                color=root_color, lw=1.0))
    ax.annotate("",
                xy=(r1, 0), xytext=(4.35, 1.3),
                arrowprops=dict(arrowstyle="->",
                                color=root_color, lw=1.0))

    ax.set_title("Key features of a parabola", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/parabola_vertex_axis_of_symmetry.svg")


# ---------------------------------------------------------------------------
# Algebra: geometric completion of the square

def fig_perfect_square_completion():
    """Geometric completion of x^2 + 6x + 9 = (x + 3)^2."""
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.set_aspect("equal")

    x_vis = 5.0   # visual length standing in for "x"
    three = 3.0
    total = x_vis + three

    ax.set_xlim(-1.6, total + 1.2)
    ax.set_ylim(-1.1, total + 1.4)

    # Pastel colors
    c_xx = "#cde4f0"   # x^2
    c_rect_a = "#fce1b7"  # top rectangle x by 3
    c_rect_b = "#fce1b7"  # right rectangle 3 by x
    c_corner = "#f4d0d6"  # 3 by 3 "completing" square

    # Bottom-left: x^2 square
    ax.fill_between([0, x_vis], 0, x_vis,
                    color=c_xx, linewidth=0)
    # Bottom-right: x by 3 rectangle
    ax.fill_between([x_vis, total], 0, x_vis,
                    color=c_rect_a, linewidth=0)
    # Top-left: 3 by x rectangle
    ax.fill_between([0, x_vis], x_vis, total,
                    color=c_rect_b, linewidth=0)
    # Top-right: 3 by 3 "completing" square (dashed outline)
    ax.fill_between([x_vis, total], x_vis, total,
                    color=c_corner, linewidth=0, alpha=0.9)

    # Outer square outline of the completed big square (solid)
    ax.plot([0, total, total, 0, 0],
            [0, 0, total, total, 0],
            color=C_LINE, linewidth=2.2)
    # Inner dividers between the pieces
    ax.plot([x_vis, x_vis], [0, total], color=C_LINE, linewidth=1.6)
    ax.plot([0, total], [x_vis, x_vis], color=C_LINE, linewidth=1.6)

    # Emphasize the "added" 3x3 square with a dashed outline
    ax.plot([x_vis, total, total, x_vis, x_vis],
            [x_vis, x_vis, total, total, x_vis],
            color=C_RADIUS, linewidth=2.0, linestyle="--")

    # Labels inside each piece
    ax.text(x_vis / 2, x_vis / 2, r"$x^{2}$",
            ha="center", va="center",
            fontsize=22, color=C_TEXT, fontweight="bold")
    ax.text(x_vis + three / 2, x_vis / 2, r"$3x$",
            ha="center", va="center",
            fontsize=18, color=C_TEXT, fontweight="bold")
    ax.text(x_vis / 2, x_vis + three / 2, r"$3x$",
            ha="center", va="center",
            fontsize=18, color=C_TEXT, fontweight="bold")
    ax.text(x_vis + three / 2, x_vis + three / 2, r"$9$",
            ha="center", va="center",
            fontsize=18, color=C_RADIUS, fontweight="bold")

    # Bottom side labels
    ax.text(x_vis / 2, -0.4, r"$x$",
            ha="center", va="top",
            fontsize=14, color=C_TEXT, fontweight="bold")
    ax.text(x_vis + three / 2, -0.4, r"$3$",
            ha="center", va="top",
            fontsize=14, color=C_TEXT, fontweight="bold")

    # Left side labels
    ax.text(-0.35, x_vis / 2, r"$x$",
            ha="right", va="center",
            fontsize=14, color=C_TEXT, fontweight="bold")
    ax.text(-0.35, x_vis + three / 2, r"$3$",
            ha="right", va="center",
            fontsize=14, color=C_TEXT, fontweight="bold")

    # Bracket-style callout for the completed side length x + 3
    ax.annotate("", xy=(total, total + 0.55), xytext=(0, total + 0.55),
                arrowprops=dict(arrowstyle="<->", color=C_DASH, lw=1.2))
    ax.text(total / 2, total + 0.75, r"$x + 3$",
            ha="center", va="bottom",
            fontsize=13, color=C_DASH, fontweight="bold")

    ax.set_title(r"Completing the square: $x^{2} + 6x + 9 = (x+3)^{2}$",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/perfect_square_completion.svg")


# ---------------------------------------------------------------------------
# Algebra: distance formula derivation (Pythagoras on a grid)

def fig_distance_formula_derivation():
    """Distance formula shown as the Pythagorean theorem on a coordinate grid."""
    fig, ax = plt.subplots(figsize=(6, 5.5))
    ax.set_aspect("equal")
    ax.set_xlim(-1.5, 7.5)
    ax.set_ylim(-1.5, 7.5)

    # Light grid at every integer
    for i in range(-1, 8):
        ax.plot([i, i], [-1, 7], color=C_GRID, linewidth=0.6, zorder=0)
        ax.plot([-1, 7], [i, i], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(7.3, 0), xytext=(-1.3, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 7.3), xytext=(0, -1.3),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(7.4, 0.25, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.25, 7.4, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")

    # Integer tick labels along x and y axes
    for t in range(1, 8):
        ax.text(t, -0.3, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
        ax.text(-0.2, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    color_blue = "#2e86de"

    # Points A = (1, 2), B = (5, 5), C = (5, 2)
    Ax, Ay = 1, 2
    Bx, By = 5, 5
    Cx, Cy = 5, 2

    # Horizontal leg from A to C (dashed red)
    ax.plot([Ax, Cx], [Ay, Cy], color=C_RADIUS, linewidth=2.0,
            linestyle="--", zorder=2)
    # Vertical leg from C to B (dashed red)
    ax.plot([Cx, Bx], [Cy, By], color=C_RADIUS, linewidth=2.0,
            linestyle="--", zorder=2)
    # Hypotenuse from A to B (solid blue)
    ax.plot([Ax, Bx], [Ay, By], color=color_blue, linewidth=2.6, zorder=3)

    # Point dots
    ax.plot(Ax, Ay, "o", color=color_blue, markersize=10, zorder=4)
    ax.plot(Bx, By, "o", color=color_blue, markersize=10, zorder=4)

    # Point labels A and B
    ax.text(Ax - 0.2, Ay - 0.2, r"$A = (1, 2)$",
            fontsize=11, color=color_blue,
            ha="right", va="top", fontweight="bold")
    ax.text(Bx + 0.2, By + 0.2, r"$B = (5, 5)$",
            fontsize=11, color=color_blue,
            ha="left", va="bottom", fontweight="bold")

    # Horizontal leg label
    ax.text((Ax + Cx) / 2, Ay - 0.5, r"$|x_2 - x_1| = 4$",
            ha="center", va="top",
            fontsize=11, color=C_RADIUS)
    # Vertical leg label
    ax.text(Cx + 0.25, (Cy + By) / 2, r"$|y_2 - y_1| = 3$",
            ha="left", va="center",
            fontsize=11, color=C_RADIUS)
    # Hypotenuse label (bold)
    ax.text((Ax + Bx) / 2 - 0.35, (Ay + By) / 2 + 0.35,
            r"$\sqrt{4^{2} + 3^{2}} = 5$",
            ha="right", va="bottom",
            fontsize=12, color=color_blue, fontweight="bold")

    ax.set_title("The distance formula as Pythagoras on a grid",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/distance_formula_derivation.svg")


# ---------------------------------------------------------------------------
# Algebra: square root parent function f(x) = sqrt(x)

def fig_square_root_function():
    """Plot of y = sqrt(x) with key points (0,0), (1,1), (4,2), (9,3)."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-1.5, 10.5)
    ax.set_ylim(-1.2, 4.2)

    # Light grid at every integer
    for i in range(-1, 11):
        ax.plot([i, i], [-1.2, 4.2], color=C_GRID, linewidth=0.6, zorder=0)
    for j in range(-1, 5):
        ax.plot([-1.5, 10.5], [j, j], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(10.3, 0), xytext=(-1.3, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 4.0), xytext=(0, -1.1),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(10.4, 0.2, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.2, 4.1, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")

    # Integer tick labels on x-axis
    for t in range(1, 11):
        ax.text(t, -0.22, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
    # Integer tick labels on y-axis
    for t in range(1, 5):
        ax.text(-0.18, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Dashed vertical "wall" at x = 0 marking where the domain starts
    ax.plot([0, 0], [-1.1, 4.0], color=C_DASH,
            linewidth=1.4, linestyle="--", zorder=1)

    # Smooth curve y = sqrt(x) from 0 to 10
    xs = np.linspace(0, 10, 400)
    ys = np.sqrt(xs)
    ax.plot(xs, ys, color=C_LINE, linewidth=2.6, zorder=2)

    # Key points
    key_points = [(0, 0), (1, 1), (4, 2), (9, 3)]
    for px, py in key_points:
        ax.plot(px, py, "o", color=C_RADIUS, markersize=8, zorder=4)
        ax.text(px + 0.2, py - 0.15, f"$({px}, {py})$",
                fontsize=10, color=C_RADIUS,
                ha="left", va="top", fontweight="bold")

    # Caption inside the plot area
    ax.text(6.5, 0.6, r"Domain: $x \geq 0$,   Range: $y \geq 0$",
            ha="center", va="center",
            fontsize=11, color=C_TEXT,
            bbox=dict(boxstyle="round,pad=0.35",
                      facecolor="white",
                      edgecolor=C_DASH, linewidth=0.8))

    ax.set_title(r"$f(x) = \sqrt{x}$: the parent square root function",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/square_root_function.svg")


# ---------------------------------------------------------------------------
# Algebra: cube root parent function f(x) = cbrt(x)

def fig_cube_root_function():
    """Plot of y = cbrt(x) with key points (-8,-2), (0,0), (8,2)."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-11, 11)
    ax.set_ylim(-3.3, 3.3)

    # Light grid at every 2 units
    for i in range(-10, 11, 2):
        ax.plot([i, i], [-3.3, 3.3], color=C_GRID, linewidth=0.6, zorder=0)
    for j in range(-3, 4):
        ax.plot([-11, 11], [j, j], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(10.6, 0), xytext=(-10.6, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 3.1), xytext=(0, -3.1),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(10.8, 0.15, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.2, 3.2, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")

    # Integer tick labels on x-axis (every 2 except 0)
    for t in range(-10, 11, 2):
        if t == 0:
            continue
        ax.text(t, -0.18, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
    # Integer tick labels on y-axis
    for t in range(-3, 4):
        if t == 0:
            continue
        ax.text(-0.25, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Smooth curve y = cbrt(x) from -10 to 10
    # Use sign * |x|^(1/3) to get the real cube root for negatives
    xs = np.linspace(-10, 10, 600)
    ys = np.sign(xs) * np.abs(xs) ** (1.0 / 3.0)
    ax.plot(xs, ys, color=C_LINE, linewidth=2.6, zorder=2)

    # Key points (label only three: endpoints and origin)
    labeled_points = [(-8, -2), (0, 0), (8, 2)]
    for px, py in labeled_points:
        ax.plot(px, py, "o", color=C_RADIUS, markersize=8, zorder=4)

    # Hand-place labels so they don't overlap the curve
    ax.text(-8, -2.35, r"$(-8, -2)$",
            fontsize=10, color=C_RADIUS,
            ha="center", va="top", fontweight="bold")
    ax.text(0.4, -0.35, r"$(0, 0)$",
            fontsize=10, color=C_RADIUS,
            ha="left", va="top", fontweight="bold")
    ax.text(8, 2.35, r"$(8, 2)$",
            fontsize=10, color=C_RADIUS,
            ha="center", va="bottom", fontweight="bold")

    # Extra unlabeled key points the curve passes through
    ax.plot(-1, -1, "o", color=C_RADIUS, markersize=6, zorder=4)
    ax.plot(1, 1, "o", color=C_RADIUS, markersize=6, zorder=4)

    # Caption inside the plot area (top-left corner)
    ax.text(-10, 2.6, "Domain: all reals,  Range: all reals",
            ha="left", va="center",
            fontsize=10, color=C_TEXT,
            bbox=dict(boxstyle="round,pad=0.35",
                      facecolor="white",
                      edgecolor=C_DASH, linewidth=0.8))

    ax.set_title(r"$f(x) = \sqrt[3]{x}$: the parent cube root function",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/cube_root_function.svg")


# ---------------------------------------------------------------------------
# Algebra: gallery of parent functions (Cluster 5)

def fig_parent_function_gallery():
    """A 2x4 grid showing eight common parent functions."""
    fig, axes = plt.subplots(2, 4, figsize=(8, 5))

    def draw_linear(ax):
        xs = np.linspace(-5, 5, 400)
        ax.plot(xs, xs, color=C_LINE, linewidth=1.6)

    def draw_quadratic(ax):
        xs = np.linspace(-5, 5, 400)
        ax.plot(xs, xs ** 2, color=C_LINE, linewidth=1.6)

    def draw_cubic(ax):
        xs = np.linspace(-3, 3, 400)
        ax.plot(xs, xs ** 3, color=C_LINE, linewidth=1.6)

    def draw_abs(ax):
        xs = np.linspace(-5, 5, 400)
        ax.plot(xs, np.abs(xs), color=C_LINE, linewidth=1.6)

    def draw_sqrt(ax):
        xs = np.linspace(0, 5, 400)
        ax.plot(xs, np.sqrt(xs), color=C_LINE, linewidth=1.6)

    def draw_cbrt(ax):
        xs = np.linspace(-5, 5, 400)
        ys = np.sign(xs) * np.abs(xs) ** (1.0 / 3.0)
        ax.plot(xs, ys, color=C_LINE, linewidth=1.6)

    def draw_reciprocal(ax):
        # Two branches: avoid x = 0
        xl = np.linspace(-5, -0.2, 200)
        xr = np.linspace(0.2, 5, 200)
        ax.plot(xl, 1.0 / xl, color=C_LINE, linewidth=1.6)
        ax.plot(xr, 1.0 / xr, color=C_LINE, linewidth=1.6)

    def draw_exponential(ax):
        xs = np.linspace(-5, 4, 400)
        ax.plot(xs, 2.0 ** xs, color=C_LINE, linewidth=1.6)

    # 2 rows x 4 columns = 8 panels
    panels = [
        (r"$y = x$", draw_linear, (-5, 5), (-5, 5)),
        (r"$y = x^{2}$", draw_quadratic, (-5, 5), (-1, 10)),
        (r"$y = x^{3}$", draw_cubic, (-3, 3), (-10, 10)),
        (r"$y = |x|$", draw_abs, (-5, 5), (-1, 6)),
        (r"$y = \sqrt{x}$", draw_sqrt, (-1, 6), (-1, 4)),
        (r"$y = \sqrt[3]{x}$", draw_cbrt, (-5, 5), (-3, 3)),
        (r"$y = 1/x$", draw_reciprocal, (-5, 5), (-5, 5)),
        (r"$y = 2^{x}$", draw_exponential, (-5, 4), (-1, 10)),
    ]

    for ax, (title, draw, xlim, ylim) in zip(axes.flat, panels):
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        # Lightweight axes through origin (no grid lines inside subplots)
        ax.axhline(0, color=C_GRID, linewidth=0.7, zorder=0)
        ax.axvline(0, color=C_GRID, linewidth=0.7, zorder=0)

        draw(ax)

        ax.set_title(title, fontsize=11, color=C_TEXT, pad=4)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine_name, spine in ax.spines.items():
            if spine_name in ("top", "right"):
                spine.set_visible(False)
            else:
                spine.set_color(C_DASH)
                spine.set_linewidth(0.6)

    fig.suptitle("A gallery of parent functions", fontsize=14, y=1.00)
    fig.tight_layout()

    _save(fig, "algebra/parent_function_gallery.svg")


# ---------------------------------------------------------------------------
# Algebra: transformation shifts on y = x^2 (Cluster 5)

def fig_transformation_shifts():
    """y = x^2 parent plus three shifted variants on a single coordinate plane."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-2, 10)

    # Light grid
    for i in range(-6, 7):
        ax.plot([i, i], [-2, 10], color=C_GRID, linewidth=0.6, zorder=0)
    for j in range(-2, 11):
        ax.plot([-6, 6], [j, j], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(5.8, 0), xytext=(-5.8, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 9.8), xytext=(0, -1.8),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(5.9, 0.2, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.2, 9.85, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # Integer tick labels
    for t in range(-5, 6):
        if t == 0:
            continue
        ax.text(t, -0.35, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
    for t in range(-1, 11):
        if t == 0:
            continue
        ax.text(-0.15, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Colors for the three transformed parabolas
    color_blue = "#2e86de"
    color_green = "#10ac84"
    color_red = "#c44569"

    # Parent y = x^2 in light gray, thin dashed line
    x_parent = np.linspace(-3.2, 3.2, 400)
    ax.plot(x_parent, x_parent ** 2, color="#bbbbbb", linewidth=1.4,
            linestyle="--", label=r"$y = x^{2}$", zorder=2)

    # Shift right 3:  y = (x - 3)^2
    x_a = np.linspace(-0.2, 6.0, 400)
    ya = (x_a - 3) ** 2
    mask_a = ya <= 10
    ax.plot(x_a[mask_a], ya[mask_a], color=color_blue, linewidth=2.2,
            label=r"$y = (x - 3)^{2}$", zorder=3)

    # Shift up 2: y = x^2 + 2
    x_b = np.linspace(-2.85, 2.85, 400)
    yb = x_b ** 2 + 2
    mask_b = yb <= 10
    ax.plot(x_b[mask_b], yb[mask_b], color=color_green, linewidth=2.2,
            label=r"$y = x^{2} + 2$", zorder=3)

    # Shift left 2, down 1: y = (x + 2)^2 - 1
    x_c = np.linspace(-5.3, 1.3, 400)
    yc = (x_c + 2) ** 2 - 1
    mask_c = yc <= 10
    ax.plot(x_c[mask_c], yc[mask_c], color=color_red, linewidth=2.2,
            label=r"$y = (x + 2)^{2} - 1$", zorder=3)

    # Legend labeling each curve
    ax.legend(loc="upper left", fontsize=9, framealpha=0.95,
              edgecolor=C_DASH)

    ax.set_title(r"Shifts of $f(x) = x^{2}$", fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/transformation_shifts.svg")


# ---------------------------------------------------------------------------
# Algebra: rational function with asymptotes (Cluster 5)

def fig_rational_asymptotes():
    """Plot f(x) = (x^2 - 4)/(x^2 - 1) with its asymptotes labeled."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Light grid
    for i in range(-5, 6):
        ax.plot([i, i], [-5, 5], color=C_GRID, linewidth=0.6, zorder=0)
        ax.plot([-5, 5], [i, i], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(4.85, 0), xytext=(-4.85, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 4.85), xytext=(0, -4.85),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(4.9, 0.2, r"$x$", fontsize=12, color=C_TEXT,
            ha="right", va="bottom")
    ax.text(0.2, 4.9, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # Integer tick labels
    for t in range(-4, 5):
        if t == 0:
            continue
        ax.text(t, -0.25, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
        ax.text(-0.18, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Asymptotes (dashed)
    # Vertical at x = -1 and x = 1
    ax.plot([-1, -1], [-5, 5], color=C_DASH,
            linewidth=1.6, linestyle="--", zorder=1)
    ax.plot([1, 1], [-5, 5], color=C_DASH,
            linewidth=1.6, linestyle="--", zorder=1)
    # Horizontal at y = 1
    ax.plot([-5, 5], [1, 1], color=C_DASH,
            linewidth=1.6, linestyle="--", zorder=1)

    # Compute f(x) = (x^2 - 4) / (x^2 - 1) across the full range, then mask
    # out regions where |y| leaves the y-window so the curve is drawn as
    # three separate pieces around the vertical asymptotes at x = +/-1.
    xs = np.linspace(-5, 5, 1200)
    # Exclude points too close to the asymptotes to avoid divide-by-zero.
    eps = 1e-6
    safe = np.abs(np.abs(xs) - 1) > eps
    xs_safe = xs[safe]
    ys = (xs_safe ** 2 - 4) / (xs_safe ** 2 - 1)

    # Only keep points whose |y| is within the plot window. Breaks in the
    # underlying index sequence become breaks in the drawn line, so the curve
    # renders as three visually disconnected pieces.
    in_window = np.abs(ys) <= 5.0
    xs_plot = np.where(in_window, xs_safe, np.nan)
    ys_plot = np.where(in_window, ys, np.nan)
    ax.plot(xs_plot, ys_plot, color=C_LINE, linewidth=2.4, zorder=3)

    # Asymptote labels
    ax.text(-1.15, -4.3, r"$x = -1$", fontsize=10, color=C_DASH,
            ha="right", va="bottom", fontweight="bold")
    ax.text(1.15, -4.3, r"$x = 1$", fontsize=10, color=C_DASH,
            ha="left", va="bottom", fontweight="bold")
    ax.text(4.6, 1.25, r"$y = 1$", fontsize=10, color=C_DASH,
            ha="right", va="bottom", fontweight="bold")

    ax.set_title(r"A rational function and its asymptotes",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/rational_asymptotes.svg")


# ---------------------------------------------------------------------------
# Algebra: piecewise function with 3 pieces (Cluster 5)

def fig_piecewise_function():
    """A 3-piece piecewise function with labeled formulas and boundary dots."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-4, 6)
    ax.set_ylim(-2, 6)

    # Light grid
    for i in range(-4, 7):
        ax.plot([i, i], [-2, 6], color=C_GRID,
                linewidth=0.6, zorder=0)
    for j in range(-2, 7):
        ax.plot([-4, 6], [j, j], color=C_GRID,
                linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(5.85, 0), xytext=(-3.85, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 5.85), xytext=(0, -1.85),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(5.9, 0.15, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.15, 5.9, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # Integer tick labels on x-axis
    for t in range(-3, 6):
        if t == 0:
            continue
        ax.text(t, -0.25, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
    # Integer tick labels on y-axis
    for t in range(-1, 6):
        if t == 0:
            continue
        ax.text(-0.12, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Colors for the three pieces
    color_blue = "#2e86de"
    color_green = "#10ac84"
    color_red = "#c44569"

    # Piece 1: y = x + 3 for x < 0 (open dot at x = 0, y = 3)
    x1 = np.linspace(-4, 0, 200)
    y1 = x1 + 3
    ax.plot(x1, y1, color=color_blue, linewidth=2.4, zorder=3)
    # Open circle at (0, 3)
    ax.plot(0, 3, "o", markerfacecolor="white",
            markeredgecolor=color_blue, markeredgewidth=2.2,
            markersize=10, zorder=4)

    # Piece 2: y = x^2 for 0 <= x <= 2 (closed both ends)
    x2 = np.linspace(0, 2, 200)
    y2 = x2 ** 2
    ax.plot(x2, y2, color=color_green, linewidth=2.4, zorder=3)

    # Piece 3: y = 4 for x > 2 (open dot at x = 2)
    x3 = np.linspace(2, 6, 200)
    y3 = np.full_like(x3, 4.0)
    ax.plot(x3, y3, color=color_red, linewidth=2.4, zorder=3)
    # Open circle at (2, 4) for piece 3
    ax.plot(2, 4, "o", markerfacecolor="white",
            markeredgecolor=color_red, markeredgewidth=2.2,
            markersize=10, zorder=5)

    # Closed circles at (0, 0) and (2, 4) from piece 2 drawn last so they
    # sit on top of the open circle at (2, 4) from piece 3.
    ax.plot(0, 0, "o", color=color_green, markersize=10, zorder=6)
    ax.plot(2, 4, "o", color=color_green, markersize=10, zorder=6)

    # In-figure formula labels for each piece
    ax.text(-3.2, 0.4, r"$y = x + 3$",
            fontsize=11, color=color_blue, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_blue, linewidth=0.8))
    ax.text(1.1, 5.1, r"$y = x^{2}$",
            fontsize=11, color=color_green, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_green, linewidth=0.8))
    ax.text(4.3, 4.7, r"$y = 4$",
            fontsize=11, color=color_red, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_red, linewidth=0.8))

    ax.set_title("A three-piece piecewise function",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/piecewise_function.svg")


# ---------------------------------------------------------------------------
# Algebra: exponential growth vs decay (Cluster 6)

def fig_exponential_growth_decay():
    """y = 2^x and y = (1/2)^x on a single plane with a shared asymptote."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-3, 5)
    ax.set_ylim(-1, 20)

    # Light grid at each integer
    for i in range(-3, 6):
        ax.plot([i, i], [-1, 20], color=C_GRID, linewidth=0.6, zorder=0)
    for j in range(-1, 21):
        ax.plot([-3, 5], [j, j], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(4.85, 0), xytext=(-2.85, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 19.6), xytext=(0, -0.85),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(4.9, 0.4, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.15, 19.7, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # Integer x tick labels
    for t in range(-2, 5):
        if t == 0:
            continue
        ax.text(t, -0.55, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
    # y tick labels at a few values (every 4)
    for t in [4, 8, 12, 16]:
        ax.text(-0.1, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Dashed horizontal asymptote at y = 0
    ax.plot([-3, 5], [0, 0], color=C_DASH,
            linewidth=1.4, linestyle="--", zorder=1)
    ax.text(4.75, 0.55, r"$y = 0$", fontsize=9, color=C_DASH,
            ha="right", va="bottom", fontweight="bold")

    # Colors
    color_growth = "#2e86de"   # blue
    color_decay = "#c44569"    # red

    # Growth: y = 2^x (clipped to the y window)
    xg = np.linspace(-3, 5, 400)
    yg = 2.0 ** xg
    mask_g = yg <= 20
    ax.plot(xg[mask_g], yg[mask_g], color=color_growth,
            linewidth=2.4, zorder=3)

    # Decay: y = (1/2)^x (clipped to the y window)
    xd = np.linspace(-3, 5, 400)
    yd = 0.5 ** xd
    mask_d = yd <= 20
    ax.plot(xd[mask_d], yd[mask_d], color=color_decay,
            linewidth=2.4, zorder=3)

    # Curve labels near the top of each plotted curve
    ax.text(4.3, 17.5, r"$y = 2^{x}$",
            fontsize=11, color=color_growth, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_growth, linewidth=0.8))
    ax.text(-2.3, 17.5, r"$y = (1/2)^{x}$",
            fontsize=11, color=color_decay, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_decay, linewidth=0.8))

    ax.set_title("Exponential growth vs decay", fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/exponential_growth_decay.svg")


# ---------------------------------------------------------------------------
# Algebra: logarithm as inverse of exponential (Cluster 6)

def fig_log_exp_inverses():
    """y = 2^x and y = log_2(x) reflected across y = x."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.set_xlim(-4, 8)
    ax.set_ylim(-4, 8)

    # Light grid
    for i in range(-4, 9):
        ax.plot([i, i], [-4, 8], color=C_GRID, linewidth=0.6, zorder=0)
        ax.plot([-4, 8], [i, i], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(7.85, 0), xytext=(-3.85, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 7.85), xytext=(0, -3.85),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    ax.text(7.9, 0.2, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.2, 7.9, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # Integer tick labels
    for t in range(-3, 8):
        if t == 0:
            continue
        ax.text(t, -0.25, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
        ax.text(-0.15, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    # Colors
    color_exp = "#2e86de"    # blue
    color_log = "#c44569"    # red

    # Mirror line y = x (dashed gray)
    ax.plot([-4, 8], [-4, 8], color=C_DASH,
            linewidth=1.4, linestyle="--", zorder=1)
    ax.text(6.4, 6.9, r"$y = x$", fontsize=10, color=C_DASH,
            ha="left", va="bottom", fontweight="bold")

    # Exponential: y = 2^x (clipped to window)
    xe = np.linspace(-4, 4, 400)
    ye = 2.0 ** xe
    mask_e = ye <= 8
    ax.plot(xe[mask_e], ye[mask_e], color=color_exp,
            linewidth=2.4, zorder=3)

    # Logarithm: y = log_2(x), only for x > 0, clipped to window
    xl = np.linspace(0.01, 8, 400)
    yl = np.log2(xl)
    mask_l = (yl >= -4) & (yl <= 8)
    ax.plot(xl[mask_l], yl[mask_l], color=color_log,
            linewidth=2.4, zorder=3)

    # Matching reflection points
    # (0, 1) on exponential <-> (1, 0) on logarithm
    # (1, 2) on exponential <-> (2, 1) on logarithm
    pair_pts = [
        ((0, 1), (1, 0)),
        ((1, 2), (2, 1)),
    ]
    for (ex, ey), (lx, ly) in pair_pts:
        ax.plot(ex, ey, "o", color=color_exp, markersize=7, zorder=5)
        ax.plot(lx, ly, "o", color=color_log, markersize=7, zorder=5)
        # Thin connector across the mirror line
        ax.plot([ex, lx], [ey, ly], color=C_DASH,
                linewidth=0.9, linestyle=":", zorder=2)

    # Point labels
    ax.text(0.15, 1.2, r"$(0,\,1)$", fontsize=8, color=color_exp,
            ha="left", va="bottom")
    ax.text(1.2, -0.1, r"$(1,\,0)$", fontsize=8, color=color_log,
            ha="left", va="top")
    ax.text(1.2, 2.1, r"$(1,\,2)$", fontsize=8, color=color_exp,
            ha="left", va="bottom")
    ax.text(2.2, 1.1, r"$(2,\,1)$", fontsize=8, color=color_log,
            ha="left", va="bottom")

    # Curve labels
    ax.text(3.1, 7.3, r"$y = 2^{x}$",
            fontsize=11, color=color_exp, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_exp, linewidth=0.8))
    ax.text(6.7, 2.3, r"$y = \log_{2}(x)$",
            fontsize=11, color=color_log, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_log, linewidth=0.8))

    ax.set_title("The logarithm is the mirror of the exponential",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/log_exp_inverses.svg")


# ---------------------------------------------------------------------------
# Algebra: compound growth comparison (Cluster 6)

def fig_compound_growth_comparison():
    """Simple, annual, monthly, and continuous compounding on $1000 at 5%."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 5000)

    # Light grid: vertical every 5 years, horizontal every 500 dollars
    for i in range(0, 31, 5):
        ax.plot([i, i], [0, 5000], color=C_GRID,
                linewidth=0.6, zorder=0)
    for j in range(0, 5001, 500):
        ax.plot([0, 30], [j, j], color=C_GRID,
                linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(29.7, 0), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=C_LINE, lw=1.4),
    )
    ax.annotate(
        "", xy=(0, 4950), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=C_LINE, lw=1.4),
    )

    # Tick labels
    for t in range(0, 31, 5):
        ax.text(t, -90, str(t), ha="center", va="top",
                fontsize=9, color=C_TEXT)
    for t in range(0, 5001, 1000):
        ax.text(-0.25, t, f"${t}", ha="right", va="center",
                fontsize=9, color=C_TEXT)

    # Axis labels
    ax.text(15, -330, "time (years)", fontsize=11,
            color=C_TEXT, ha="center", va="top")
    ax.text(-2.8, 2500, "balance (dollars)", fontsize=11,
            color=C_TEXT, ha="center", va="center", rotation=90)

    # Time array for smooth curves
    t = np.linspace(0, 30, 400)
    P = 1000.0
    r = 0.05

    # Colors per spec
    color_simple = "#888888"      # gray
    color_annual = "#10ac84"      # green
    color_monthly = "#2e86de"     # blue
    color_cont = "#c44569"        # red

    # Simple interest: straight line A = P(1 + r*t)
    A_simple = P * (1.0 + r * t)
    ax.plot(t, A_simple, color=color_simple, linewidth=2.2,
            label=r"simple: $A = 1000(1 + 0.05t)$", zorder=3)

    # Annual: A = P(1.05)^t
    A_annual = P * (1.0 + r) ** t
    ax.plot(t, A_annual, color=color_annual, linewidth=2.2,
            label=r"annual: $A = 1000(1.05)^{t}$", zorder=3)

    # Monthly: A = P(1 + r/12)^(12 t)
    A_monthly = P * (1.0 + r / 12.0) ** (12.0 * t)
    ax.plot(t, A_monthly, color=color_monthly, linewidth=2.2,
            label=r"monthly: $A = 1000(1 + 0.05/12)^{12t}$",
            zorder=3)

    # Continuous: A = P * e^(r t)
    A_cont = P * np.exp(r * t)
    ax.plot(t, A_cont, color=color_cont, linewidth=2.2,
            label=r"continuous: $A = 1000\,e^{0.05t}$", zorder=3)

    # Legend
    ax.legend(loc="upper left", fontsize=9, framealpha=0.95,
              edgecolor=C_DASH)

    ax.set_title(
        "Simple, annual, monthly, and continuous compounding on $1000 at 5%",
        fontsize=12, pad=12,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "algebra/compound_growth_comparison.svg")


# ---------------------------------------------------------------------------
# Precalculus: the unit circle with 16 special angles (Cluster 7)

def fig_unit_circle():
    """Unit circle with the 16 special angles labeled with exact (x, y)."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.9, 1.9)

    # Axes through the origin
    ax.annotate(
        "", xy=(1.8, 0), xytext=(-1.8, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.3),
    )
    ax.annotate(
        "", xy=(0, 1.8), xytext=(0, -1.8),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.3),
    )
    ax.text(1.85, 0.05, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.05, 1.85, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # The unit circle itself
    theta_c = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta_c), np.sin(theta_c),
            color=C_LINE, linewidth=2.2, zorder=2)

    # The 16 special angles as (angle, pretty pi label, (x, y) label)
    # Exact coordinates using radical expressions.
    specials = [
        (0,               r"$0$",            r"$(1,\, 0)$"),
        (np.pi / 6,       r"$\pi/6$",        r"$(\frac{\sqrt{3}}{2},\, \frac{1}{2})$"),
        (np.pi / 4,       r"$\pi/4$",        r"$(\frac{\sqrt{2}}{2},\, \frac{\sqrt{2}}{2})$"),
        (np.pi / 3,       r"$\pi/3$",        r"$(\frac{1}{2},\, \frac{\sqrt{3}}{2})$"),
        (np.pi / 2,       r"$\pi/2$",        r"$(0,\, 1)$"),
        (2 * np.pi / 3,   r"$2\pi/3$",       r"$(-\frac{1}{2},\, \frac{\sqrt{3}}{2})$"),
        (3 * np.pi / 4,   r"$3\pi/4$",       r"$(-\frac{\sqrt{2}}{2},\, \frac{\sqrt{2}}{2})$"),
        (5 * np.pi / 6,   r"$5\pi/6$",       r"$(-\frac{\sqrt{3}}{2},\, \frac{1}{2})$"),
        (np.pi,           r"$\pi$",          r"$(-1,\, 0)$"),
        (7 * np.pi / 6,   r"$7\pi/6$",       r"$(-\frac{\sqrt{3}}{2},\, -\frac{1}{2})$"),
        (5 * np.pi / 4,   r"$5\pi/4$",       r"$(-\frac{\sqrt{2}}{2},\, -\frac{\sqrt{2}}{2})$"),
        (4 * np.pi / 3,   r"$4\pi/3$",       r"$(-\frac{1}{2},\, -\frac{\sqrt{3}}{2})$"),
        (3 * np.pi / 2,   r"$3\pi/2$",       r"$(0,\, -1)$"),
        (5 * np.pi / 3,   r"$5\pi/3$",       r"$(\frac{1}{2},\, -\frac{\sqrt{3}}{2})$"),
        (7 * np.pi / 4,   r"$7\pi/4$",       r"$(\frac{\sqrt{2}}{2},\, -\frac{\sqrt{2}}{2})$"),
        (11 * np.pi / 6,  r"$11\pi/6$",      r"$(\frac{\sqrt{3}}{2},\, -\frac{1}{2})$"),
    ]

    dot_color = "#c44569"   # red dots
    radius_color = "#bfbfbf"

    # Draw radius lines from the origin to each special point first so the
    # dots and labels sit on top of them.
    for ang, _pi_label, _xy_label in specials:
        xr = np.cos(ang)
        yr = np.sin(ang)
        ax.plot([0, xr], [0, yr],
                color=radius_color, linewidth=1.0, zorder=1)

    # Now draw dots and (x, y) coordinate labels outside the circle.
    for ang, _pi_label, xy_label in specials:
        xd = np.cos(ang)
        yd = np.sin(ang)
        ax.plot(xd, yd, "o", color=dot_color, markersize=6, zorder=4)

        # Place the (x, y) label just outside the circle in the direction of
        # the radius so it never overlaps the circle interior.
        label_r = 1.28
        lx = label_r * np.cos(ang)
        ly = label_r * np.sin(ang)

        # Pick alignment based on the quadrant / axis to avoid clipping.
        if abs(np.cos(ang)) < 1e-9:
            ha = "center"
        elif np.cos(ang) > 0:
            ha = "left"
        else:
            ha = "right"
        if abs(np.sin(ang)) < 1e-9:
            va = "center"
        elif np.sin(ang) > 0:
            va = "bottom"
        else:
            va = "top"

        ax.text(lx, ly, xy_label, fontsize=8, color=C_TEXT,
                ha=ha, va=va)

    ax.set_title("The unit circle with the 16 special angles",
                 fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "precalculus/unit_circle.svg")


# ---------------------------------------------------------------------------
# Precalculus: sine and cosine graphs (Cluster 7)

def fig_sine_cosine_graphs():
    """Two stacked subplots showing y = sin x and y = cos x over [-2 pi, 2 pi]."""
    fig, (ax_sin, ax_cos) = plt.subplots(2, 1, figsize=(7, 6))

    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    pi_ticks = [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi]
    pi_labels = [r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"]

    color_sin = "#2e86de"   # blue
    color_cos = "#c44569"   # red

    for ax, y, color, title in (
        (ax_sin, y_sin, color_sin, r"$y = \sin x$"),
        (ax_cos, y_cos, color_cos, r"$y = \cos x$"),
    ):
        ax.set_xlim(-2 * np.pi - 0.3, 2 * np.pi + 0.3)
        ax.set_ylim(-1.5, 1.5)

        # Dashed reference lines at y = -1, 0, 1
        for y_ref in (-1.0, 0.0, 1.0):
            ax.plot(
                [-2 * np.pi - 0.3, 2 * np.pi + 0.3],
                [y_ref, y_ref],
                color=C_DASH, linewidth=1.0, linestyle="--", zorder=1,
            )

        # Vertical axis through x = 0
        ax.plot([0, 0], [-1.5, 1.5], color=C_GRID, linewidth=0.8, zorder=0)

        # The curve
        ax.plot(x, y, color=color, linewidth=2.4, zorder=3)

        # x ticks labeled in terms of pi
        ax.set_xticks(pi_ticks)
        ax.set_xticklabels(pi_labels, fontsize=10, color=C_TEXT)
        ax.set_yticks([-1, 0, 1])
        ax.set_yticklabels(["-1", "0", "1"], fontsize=10, color=C_TEXT)
        ax.tick_params(axis="both", colors=C_TEXT, length=3)

        ax.set_title(title, fontsize=13, pad=10)
        for spine_name in ("top", "right"):
            ax.spines[spine_name].set_visible(False)
        ax.spines["left"].set_color(C_LINE)
        ax.spines["bottom"].set_color(C_LINE)

    fig.tight_layout()
    _save(fig, "precalculus/sine_cosine_graphs.svg")


# ---------------------------------------------------------------------------
# Precalculus: 3-4-5 right triangle with SOH-CAH-TOA (Cluster 7)

def fig_right_triangle_soh_cah_toa():
    """A 3-4-5 right triangle with labeled sides and the three trig ratios."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_aspect("equal")
    ax.set_xlim(-1.2, 6.0)
    ax.set_ylim(-2.5, 4.0)

    # Vertices:
    #   A at origin (the angle theta)
    #   B at (4, 0) (the right angle)
    #   C at (4, 3) (top of the opposite side)
    A = (0.0, 0.0)
    B = (4.0, 0.0)
    C = (4.0, 3.0)

    tri_color = "#284b63"
    fill_color = "#d9e2ec"

    # Fill the triangle
    ax.fill(
        [A[0], B[0], C[0]],
        [A[1], B[1], C[1]],
        color=fill_color, zorder=1,
    )

    # Outline
    ax.plot([A[0], B[0]], [A[1], B[1]],
            color=tri_color, linewidth=2.4, zorder=3)
    ax.plot([B[0], C[0]], [B[1], C[1]],
            color=tri_color, linewidth=2.4, zorder=3)
    ax.plot([C[0], A[0]], [C[1], A[1]],
            color=tri_color, linewidth=2.4, zorder=3)

    # Right angle marker at B
    box = 0.25
    ax.plot(
        [B[0] - box, B[0] - box, B[0]],
        [B[1],       B[1] + box, B[1] + box],
        color=tri_color, linewidth=1.5, zorder=4,
    )

    # theta arc at vertex A
    arc_r = 0.55
    # The angle at A opens from the adjacent side (along +x) up to AC.
    # AC has angle atan2(3, 4).
    theta_top = np.arctan2(C[1] - A[1], C[0] - A[0])
    arc_t = np.linspace(0.0, theta_top, 60)
    ax.plot(arc_r * np.cos(arc_t), arc_r * np.sin(arc_t),
            color=C_RADIUS, linewidth=1.8, zorder=4)
    ax.text(0.75, 0.28, r"$\theta$",
            fontsize=14, color=C_RADIUS, fontweight="bold",
            ha="left", va="bottom")

    # Side labels
    # Adjacent side (bottom), length 4
    ax.text(2.0, -0.35, "adjacent = 4",
            fontsize=11, color=C_TEXT, ha="center", va="top")
    # Opposite side (right vertical), length 3
    ax.text(4.15, 1.5, "opposite = 3",
            fontsize=11, color=C_TEXT, ha="left", va="center")
    # Hypotenuse (from A to C), length 5
    # Midpoint is (2, 1.5). Place label slightly above-left.
    ax.text(1.75, 1.85, "hypotenuse = 5",
            fontsize=11, color=C_TEXT,
            ha="center", va="bottom",
            rotation=np.degrees(theta_top))

    # Three trig-ratio equations below the triangle
    ax.text(
        2.4, -1.35,
        r"$\sin\theta = \dfrac{\text{opp}}{\text{hyp}} = \dfrac{3}{5}$",
        fontsize=12, color=C_TEXT, ha="center", va="center",
    )
    ax.text(
        2.4, -1.95,
        r"$\cos\theta = \dfrac{\text{adj}}{\text{hyp}} = \dfrac{4}{5}, \qquad "
        r"\tan\theta = \dfrac{\text{opp}}{\text{adj}} = \dfrac{3}{4}$",
        fontsize=12, color=C_TEXT, ha="center", va="center",
    )

    ax.set_title("SOH-CAH-TOA on a 3-4-5 right triangle",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "precalculus/right_triangle_soh_cah_toa.svg")


# ---------------------------------------------------------------------------
# Precalculus: vector addition by the head-to-tail rule (Cluster 7)

def fig_vector_addition():
    """Three arrows from the origin plus a head-to-tail construction."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 8)

    # Light integer grid
    for i in range(-1, 9):
        ax.plot([i, i], [-1, 8], color=C_GRID, linewidth=0.6, zorder=0)
        ax.plot([-1, 8], [i, i], color=C_GRID, linewidth=0.6, zorder=0)

    # Axes with arrowheads
    ax.annotate(
        "", xy=(7.85, 0), xytext=(-0.85, 0),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.3),
    )
    ax.annotate(
        "", xy=(0, 7.85), xytext=(0, -0.85),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.3),
    )
    ax.text(7.9, 0.15, r"$x$", fontsize=12, color=C_TEXT,
            ha="left", va="bottom")
    ax.text(0.15, 7.9, r"$y$", fontsize=12, color=C_TEXT,
            ha="left", va="top")

    # Integer tick labels on the axes
    for t in range(1, 8):
        ax.text(t, -0.2, str(t), ha="center", va="top",
                fontsize=8, color=C_TEXT)
        ax.text(-0.15, t, str(t), ha="right", va="center",
                fontsize=8, color=C_TEXT)

    color_u = "#2e86de"   # blue
    color_v = "#3c9a5f"   # green
    color_sum = "#c44569"  # red

    # u = (5, 1) from the origin (blue)
    ax.annotate(
        "", xy=(5, 1), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=color_u,
                        lw=2.4, mutation_scale=18),
        zorder=4,
    )
    ax.text(2.5, 0.35, r"$\vec{u} = \langle 5,\, 1 \rangle$",
            fontsize=11, color=color_u, fontweight="bold",
            ha="center", va="top")

    # v = (2, 4) from the origin (green, solid)
    ax.annotate(
        "", xy=(2, 4), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=color_v,
                        lw=2.4, mutation_scale=18),
        zorder=4,
    )
    ax.text(0.7, 2.1, r"$\vec{v} = \langle 2,\, 4 \rangle$",
            fontsize=11, color=color_v, fontweight="bold",
            ha="right", va="center")

    # Head-to-tail copy of v starting at the head of u, dashed green
    ax.annotate(
        "", xy=(7, 5), xytext=(5, 1),
        arrowprops=dict(arrowstyle="-|>", color=color_v,
                        lw=2.2, mutation_scale=18,
                        linestyle="dashed"),
        zorder=3,
    )
    ax.text(6.25, 2.7, r"$\vec{v}$ (shifted)",
            fontsize=10, color=color_v,
            ha="left", va="center")

    # Sum u + v = (7, 5) from the origin (red)
    ax.annotate(
        "", xy=(7, 5), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=color_sum,
                        lw=2.6, mutation_scale=20),
        zorder=5,
    )
    ax.text(3.6, 3.2, r"$\vec{u} + \vec{v} = \langle 7,\, 5 \rangle$",
            fontsize=11, color=color_sum, fontweight="bold",
            ha="center", va="bottom",
            bbox=dict(boxstyle="round,pad=0.25",
                      facecolor="white",
                      edgecolor=color_sum, linewidth=0.8))

    ax.set_title(r"Vector addition: $\vec{u} + \vec{v}$ by the head-to-tail rule",
                 fontsize=13, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "precalculus/vector_addition.svg")


# ---------------------------------------------------------------------------
# Precalculus: Pascal's triangle (rows 0-6)

def fig_pascals_triangle():
    """Pascal's triangle rows 0-6 with parent-sum lines drawn in."""
    n_rows = 7  # rows 0..6 inclusive
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_aspect("equal")

    # Horizontal spacing between adjacent entries within a row.
    dx = 1.0
    # Vertical spacing between successive rows (rows grow downward).
    dy = 1.1

    # Compute Pascal's triangle values
    triangle = [[1]]
    for n in range(1, n_rows):
        prev = triangle[-1]
        row = [1]
        for k in range(1, n):
            row.append(prev[k - 1] + prev[k])
        row.append(1)
        triangle.append(row)

    # Positions: each row centered horizontally at x = 0.
    # Entry k of row n sits at x = (k - n/2) * dx, y = -n * dy.
    def pos(n, k):
        return ((k - n / 2.0) * dx, -n * dy)

    # Draw parent-sum lines (interior entries only) BEHIND the numbers.
    for n in range(1, n_rows):
        for k in range(1, n):
            x_child, y_child = pos(n, k)
            xl, yl = pos(n - 1, k - 1)
            xr, yr = pos(n - 1, k)
            ax.plot([xl, x_child], [yl, y_child],
                    color=C_DASH, linewidth=0.9, zorder=1)
            ax.plot([xr, x_child], [yr, y_child],
                    color=C_DASH, linewidth=0.9, zorder=1)

    # Draw each entry as a number inside a small white circle for readability.
    for n in range(n_rows):
        for k, value in enumerate(triangle[n]):
            x, y = pos(n, k)
            ax.plot(x, y, "o", markerfacecolor="white",
                    markeredgecolor=C_LINE, markeredgewidth=1.4,
                    markersize=22, zorder=2)
            ax.text(x, y, str(value),
                    ha="center", va="center",
                    fontsize=11, color=C_TEXT, fontweight="bold",
                    zorder=3)

    # Row labels on the left, aligned with each row's y-position.
    left_label_x = -(n_rows / 2.0) * dx - 1.0
    for n in range(n_rows):
        _, y = pos(n, 0)
        ax.text(left_label_x, y, f"row {n}",
                ha="right", va="center",
                fontsize=10, color=C_TEXT)

    # Set limits with a bit of padding on all sides.
    half_width = (n_rows / 2.0) * dx + 1.8
    ax.set_xlim(-half_width - 1.0, half_width)
    ax.set_ylim(-(n_rows - 1) * dy - 0.9, 0.9)

    ax.set_title("Pascal's Triangle (rows 0-6)", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "precalculus/pascals_triangle.svg")


# ---------------------------------------------------------------------------
# Pre-algebra: horizontal box plot with five-number summary

def fig_box_plot():
    """Horizontal box plot with annotated five-number summary."""
    # Data: 12, 18, 22, 25, 28, 30, 33, 38, 42, 48, 55 (sorted, 11 values)
    # Five-number summary:
    data_min = 12
    q1 = 22
    median = 30
    q3 = 42
    data_max = 55

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(8, 62)
    ax.set_ylim(-2.2, 3.2)

    # y-position of the box plot and its vertical half-height
    y_mid = 1.4
    box_half = 0.55
    box_top = y_mid + box_half
    box_bot = y_mid - box_half

    # Whisker vertical cap length
    whisker_cap = 0.35

    box_color = "#cde4f0"
    edge_color = C_LINE
    median_color = C_RADIUS

    # Box from Q1 to Q3, filled
    ax.fill_between([q1, q3], box_bot, box_top,
                    color=box_color, linewidth=0)
    # Box outline
    ax.plot([q1, q3, q3, q1, q1],
            [box_bot, box_bot, box_top, box_top, box_bot],
            color=edge_color, linewidth=2.0)
    # Median line inside the box
    ax.plot([median, median], [box_bot, box_top],
            color=median_color, linewidth=2.6)

    # Whisker: min to Q1 (horizontal line along y_mid)
    ax.plot([data_min, q1], [y_mid, y_mid],
            color=edge_color, linewidth=1.8)
    # Whisker: Q3 to max
    ax.plot([q3, data_max], [y_mid, y_mid],
            color=edge_color, linewidth=1.8)
    # Vertical caps on each whisker end
    for x in (data_min, data_max):
        ax.plot([x, x],
                [y_mid - whisker_cap, y_mid + whisker_cap],
                color=edge_color, linewidth=1.8)

    # Number line below the plot
    line_y = -0.8
    ax.annotate(
        "", xy=(60.5, line_y), xytext=(9.5, line_y),
        arrowprops=dict(arrowstyle="<|-|>", color=C_LINE, lw=1.4),
    )
    # Ticks at every 5 from 10 to 60
    for t in range(10, 61, 5):
        ax.plot([t, t], [line_y - 0.12, line_y + 0.12],
                color=C_LINE, linewidth=1.0)
        ax.text(t, line_y - 0.28, str(t),
                ha="center", va="top",
                fontsize=9, color=C_TEXT)

    # Annotate each of the five key points with its name and value.
    label_pairs = [
        (data_min, f"min = {data_min}"),
        (q1,       f"Q1 = {q1}"),
        (median,   f"median = {median}"),
        (q3,       f"Q3 = {q3}"),
        (data_max, f"max = {data_max}"),
    ]
    for x, text in label_pairs:
        ax.text(x, box_top + 0.35, text,
                ha="center", va="bottom",
                fontsize=10, color=C_TEXT, fontweight="bold")

    ax.set_title("A box plot with five-number summary",
                 fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "pre_algebra/box_plot.svg")


# ---------------------------------------------------------------------------
# Pre-algebra: histogram of test scores

def fig_histogram_example():
    """Simple histogram with touching bars: 5 bins of width 10."""
    bin_edges = [0, 10, 20, 30, 40, 50]
    frequencies = [3, 7, 12, 8, 4]

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-3, 53)
    ax.set_ylim(0, 14)

    bar_face = "#cde4f0"
    bar_edge = C_LINE

    # Draw each bar as a filled rectangle; because bars share edges,
    # they naturally touch (characteristic of a histogram).
    for i, freq in enumerate(frequencies):
        x0 = bin_edges[i]
        x1 = bin_edges[i + 1]
        ax.fill_between([x0, x1], 0, freq,
                        color=bar_face, linewidth=0)
        ax.plot([x0, x1, x1, x0, x0],
                [0, 0, freq, freq, 0],
                color=bar_edge, linewidth=1.6)
        # Frequency label above each bar
        ax.text((x0 + x1) / 2, freq + 0.3, str(freq),
                ha="center", va="bottom",
                fontsize=10, color=C_TEXT, fontweight="bold")

    # x-axis line
    ax.plot([0, 50], [0, 0], color=C_LINE, linewidth=1.4)
    # x-axis tick marks + labels at every bin boundary
    for x in bin_edges:
        ax.plot([x, x], [-0.18, 0.18], color=C_LINE, linewidth=1.2)
        ax.text(x, -0.45, str(x),
                ha="center", va="top",
                fontsize=10, color=C_TEXT)

    # y-axis line
    ax.plot([0, 0], [0, 13], color=C_LINE, linewidth=1.4)
    # y-axis tick marks + labels at each integer from 0..13
    for y in range(0, 14, 2):
        ax.plot([-0.6, 0.6], [y, y], color=C_LINE, linewidth=1.2)
        ax.text(-1.2, y, str(y),
                ha="right", va="center",
                fontsize=9, color=C_TEXT)

    # Axis labels
    ax.text(25, -1.5, "Score",
            ha="center", va="top",
            fontsize=12, color=C_TEXT)
    ax.text(-6.0, 7, "Frequency",
            ha="center", va="center",
            fontsize=12, color=C_TEXT, rotation=90)

    ax.set_title("A histogram of test scores", fontsize=14, pad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    _save(fig, "pre_algebra/histogram_example.svg")


# ---------------------------------------------------------------------------
# Figure registry

FIGURES = [
    ("circle_parts", fig_circle_parts),
    ("number_line", fig_number_line),
    ("fraction_bar", fig_fraction_bar),
    ("area_model_distributive", fig_area_model_distributive),
    ("place_value_chart", fig_place_value_chart),
    ("coordinate_plane", fig_coordinate_plane),
    ("inequality_number_line", fig_inequality_number_line),
    ("parallel_perpendicular_lines", fig_parallel_perpendicular_lines),
    ("scatter_trend_line", fig_scatter_trend_line),
    ("area_model_multiplication", fig_area_model_multiplication),
    ("discriminant_three_cases", fig_discriminant_three_cases),
    ("parabola_vertex_axis_of_symmetry", fig_parabola_vertex_axis_of_symmetry),
    ("perfect_square_completion", fig_perfect_square_completion),
    ("distance_formula_derivation", fig_distance_formula_derivation),
    ("square_root_function", fig_square_root_function),
    ("cube_root_function", fig_cube_root_function),
    ("parent_function_gallery", fig_parent_function_gallery),
    ("transformation_shifts", fig_transformation_shifts),
    ("rational_asymptotes", fig_rational_asymptotes),
    ("piecewise_function", fig_piecewise_function),
    ("exponential_growth_decay", fig_exponential_growth_decay),
    ("log_exp_inverses", fig_log_exp_inverses),
    ("compound_growth_comparison", fig_compound_growth_comparison),
    ("unit_circle", fig_unit_circle),
    ("sine_cosine_graphs", fig_sine_cosine_graphs),
    ("right_triangle_soh_cah_toa", fig_right_triangle_soh_cah_toa),
    ("vector_addition", fig_vector_addition),
    ("pascals_triangle", fig_pascals_triangle),
    ("box_plot", fig_box_plot),
    ("histogram_example", fig_histogram_example),
]


def main():
    print(f"Generating {len(FIGURES)} figure(s)...")
    for name, fn in FIGURES:
        fn()
    print("Done.")


if __name__ == "__main__":
    main()
