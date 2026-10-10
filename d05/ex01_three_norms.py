"""One vector has three sizes, and a statement about error has to say which one it used.
"""
import numpy as np

from nmkit.norms import vnorm

for name, x in (("spread out ", np.array([1.0, 1.0, 1.0, 1.0])),
                ("one big    ", np.array([2.0, 0.0, 0.0, 0.0])),
                ("mixed      ", np.array([1.0, -2.0, 0.5, 0.25]))):
    print(f"{name} 1-norm {vnorm(x, 1):>7.4f}   2-norm {vnorm(x, 2):>7.4f}   "
          f"inf-norm {vnorm(x, np.inf):>7.4f}")
