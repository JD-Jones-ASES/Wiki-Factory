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
    fig.savefig(out, format="svg", bbox_inches="tight")
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
# Figure registry

FIGURES = [
    ("circle_parts", fig_circle_parts),
]


def main():
    print(f"Generating {len(FIGURES)} figure(s)...")
    for name, fn in FIGURES:
        fn()
    print("Done.")


if __name__ == "__main__":
    main()
