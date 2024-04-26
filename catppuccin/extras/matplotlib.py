"""Soothing pastel theme for matplotlib"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import matplotlib as mpl
import matplotlib.colors
import matplotlib.style

from catppuccin.palette import PALETTE

CATPPUCCIN_STYLE_DIRECTORY = Path(__file__).parent / "matplotlib_styles"


def _register_styles() -> None:
    """Register the included stylesheets in the mpl style library."""
    catppuccin_stylesheets = mpl.style.core.read_style_directory(  # type: ignore [attr-defined]
        CATPPUCCIN_STYLE_DIRECTORY
    )
    mpl.style.core.update_nested_dict(mpl.style.library, catppuccin_stylesheets)  # type: ignore [attr-defined]


def _register_colormap_list() -> None:
    """Register the included color maps in the `matplotlib` colormap library."""
    for palette_name in ["latte", "frappe", "macchiato", "mocha"]:
        cmap = get_colormap_from_list(palette_name, ["base", "blue"])
        mpl.colormaps.register(cmap=cmap, name=palette_name)


def get_colormap_from_list(
    palette_name: str, color_names: list[str]
) -> matplotlib.colors.LinearSegmentedColormap:
    """Get a `matplotlib` colormap from a list of colors for a specific palette."""
    colors = [load_color(palette_name, color_name) for color_name in color_names]
    return matplotlib.colors.LinearSegmentedColormap.from_list(palette_name, colors)


def load_color(palette_name: str, color_name: str) -> str:
    """Load the color for a given palette and color name."""
    return cast(
        str,
        PALETTE.__getattribute__(palette_name).colors.__getattribute__(color_name).hex,
    )
