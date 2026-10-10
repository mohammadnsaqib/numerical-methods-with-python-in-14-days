"""The smallest step available is not the best one, and it is not close."""
import numpy as np

from nmkit.diff import best_step, central_diff

x = 1.0
true = np.cos(x)
good = best_step(2)
print(f"{'h':>12} {'error':>12} {'compared with the best':>24}")
for h in (1.0, 1e-2, good, 1e-9, 1e-12, 1e-15):
    e = abs(central_diff(np.sin, x, h) - true)
    tag = "this is the best step" if h == good else ""
    print(f"{h:>12.3e} {e:>12.3e} {tag:>24}")
print()
best_err = abs(central_diff(np.sin, x, good) - true)
worst_err = abs(central_diff(np.sin, x, 1e-15) - true)
print(f"the best step is {good:.3e} and gives an error of {best_err:.3e}")
print(f"a step a billion times smaller gives {worst_err:.3e}, worse by "
      f"{worst_err / best_err:.3e} times")
