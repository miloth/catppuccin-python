"""Soothing pastel theme for `matplotlib`.

The following code was ported from [catppuccin/matplotlib](https://github.com/catppuccin/matplotlib).
Thanks to [Bram de Wilde](https://github.com/brambozz) for the original source code and
for allowing this port.

The library tries to register styles and colormaps if `matplotlib` is installed.
See the examples below for some use cases:

1. Load a style, using `mpl.style.use`

   ```python
   import catppuccin
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   mpl.style.use(catppuccin.PALETTE.mocha.identifier)
   plt.plot([0,1,2,3], [1,2,3,4])
   plt.show()
   ```

1. Mix it with different stylesheets!

   ```python
   import catppuccin
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   mpl.style.use(["ggplot", catppuccin.PALETTE.mocha.identifier])
   plt.plot([0,1,2,3], [1,2,3,4])
   plt.show()
   ```

1. Load individual colors

   ```python
   import matplotlib.pyplot as plt
   import catppuccin
   from catppuccin.extras.matplotlib import load_color

   color = load_color(catppuccin.PALETTE.latte.identifier, "peach")
   plt.plot([0,1,2,3], [1,2,3,4], color=color)
   plt.show()
   ```

1. Define custom colormaps

   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   import catppuccin
   from catppuccin.extras.matplotlib import get_colormap_from_list

   cmap = get_colormap_from_list(
       catppuccin.PALETTE.frappe.identifier,
       ["red", "peach", "yellow", "green"],
   )
   rng = np.random.default_rng()
   data = rng.integers(2, size=(30, 30))

   plt.imshow(data, cmap=cmap)
   plt.show()
   ```
"""

import matplotlib as mpl
import matplotlib.colors

from catppuccin.palette import PALETTE

DEFAULT_COLORMAP_COLORS = ("blue", "teal", "yellow", "peach", "red")


# Register the included color maps in the `matplotlib` colormap library.
for _palette in PALETTE:
    _cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        _palette.identifier,
        [
            getattr(_palette.colors, color_name).hex
            for color_name in ("blue", "teal", "yellow", "peach", "red")
        ],
    )
    mpl.colormaps.register(cmap=_cmap, name=_palette.identifier, force=True)
