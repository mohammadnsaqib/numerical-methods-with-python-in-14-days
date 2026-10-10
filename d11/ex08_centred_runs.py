"""The centred difference, and the quartering that gives it its order."""
import numpy as np

from nmkit.diff import central_diff

x = 1.0
true = np.cos(x)
prev = None
print(f"{'h':>10} {'estimate':>20} {'error':>12} {'error ratio':>13}")
for k in range(1, 9):
    h = 2.0 ** (-k)
    e = abs(central_diff(np.sin, x, h) - true)
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{h:>10.6f} {central_diff(np.sin, x, h):>20.12f} {e:>12.3e} {ratio:>13}")
    prev = e
