"""The second derivative from three values, and the order it achieves."""
import numpy as np

from nmkit.diff import second_diff

x = 1.0
true = -np.sin(x)
prev = None
print(f"{'h':>10} {'estimate':>20} {'error':>12} {'error ratio':>13}")
for k in range(1, 9):
    h = 2.0 ** (-k)
    e = abs(second_diff(np.sin, x, h) - true)
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{h:>10.6f} {second_diff(np.sin, x, h):>20.12f} {e:>12.3e} {ratio:>13}")
    prev = e
print()
print(f"the exact second derivative is {true:.12f}")
