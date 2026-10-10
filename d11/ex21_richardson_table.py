"""The whole table, and the level at which another column stops buying anything."""
import numpy as np

from nmkit.diff import central_diff, richardson

x = 1.0
true = np.cos(x)
T = richardson(lambda xx, hh: central_diff(np.sin, xx, hh), x, 0.4, order=2, gap=2,
               levels=6)

print("the estimates")
for i in range(6):
    print("  " + " ".join(f"{T[i, j]:>18.14f}" for j in range(i + 1)))
print()
print("their errors")
for i in range(6):
    print("  " + " ".join(f"{abs(T[i, j] - true):>10.2e}" for j in range(i + 1)))
print()
errs = [abs(T[i, j] - true) for i in range(6) for j in range(i + 1)]
print("column 0 is second order, column 1 is fourth, and column 2 is sixth")
print(f"the first entry is wrong by {errs[0]:.2e} and the best entry by "
      f"{min(errs):.2e}")
