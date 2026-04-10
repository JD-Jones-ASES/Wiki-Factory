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
# Figure registry

FIGURES = [
    ("circle_parts", fig_circle_parts),
    ("number_line", fig_number_line),
    ("fraction_bar", fig_fraction_bar),
    ("area_model_distributive", fig_area_model_distributive),
    ("place_value_chart", fig_place_value_chart),
]


def main():
    print(f"Generating {len(FIGURES)} figure(s)...")
    for name, fn in FIGURES:
        fn()
    print("Done.")


if __name__ == "__main__":
    main()
