"""Problem 11.39: Richardson with the wrong spacing, which fills the table and cancels
nothing."""
import numpy as np

from nmkit.diff import central_diff, forward_diff, richardson

x = 1.0
true = np.cos(x)


def show(label, estimate, order, gap):
    T = richardson(estimate, x, 0.4, order=order, gap=gap, levels=5)
    errs = [abs(T[4, j] - true) for j in range(5)]
    print(f"{label:>34}  " + " ".join(f"{e:>9.2e}" for e in errs))


print(f"{'last row of the table, column by column':>34}  " +
      " ".join(f"{'col ' + str(j):>9}" for j in range(5)))
show("centred, gap 2 (correct)", lambda xx, hh: central_diff(np.sin, xx, hh), 2, 2)
show("centred, gap 1 (wrong)", lambda xx, hh: central_diff(np.sin, xx, hh), 2, 1)
show("forward, gap 1 (correct)", lambda xx, hh: forward_diff(np.sin, xx, hh), 1, 1)
show("forward, gap 2 (wrong)", lambda xx, hh: forward_diff(np.sin, xx, hh), 1, 2)
print()
print("a wrong gap still produces a full table. Only the errors say it did nothing.")
