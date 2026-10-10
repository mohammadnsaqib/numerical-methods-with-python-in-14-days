"""Two parts of one solution, one of which is over almost before it starts."""
import numpy as np

# y = exp(-1000 t) + exp(-t) solves y' = -1000 y + 999 exp(-t), y(0) = 2.
print(f"{'t':>8} {'exp(-1000t)':>14} {'exp(-t)':>12} {'their sum':>12}")
for t in (0.0, 0.001, 0.005, 0.01, 0.1, 1.0, 3.0):
    print(f"{t:>8.3f} {np.exp(-1000 * t):>14.3e} {np.exp(-t):>12.6f} "
          f"{np.exp(-1000 * t) + np.exp(-t):>12.6f}")
print()
print("after t = 0.01 the fast part contributes 4.5e-05 and never matters again.")
print("the interesting behaviour lasts to t = 3, three hundred times longer.")
