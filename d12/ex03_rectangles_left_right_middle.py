"""Three ways to pick the height of a rectangle, and what each costs."""
import numpy as np

exact = np.e - 1.0
print(f"{'panels':>8} {'left':>13} {'right':>13} {'middle':>13}")
for n in (4, 8, 16, 32, 64):
    x = np.linspace(0.0, 1.0, n + 1)
    h = 1.0 / n
    left = float(np.sum(np.exp(x[:-1])) * h)
    right = float(np.sum(np.exp(x[1:])) * h)
    mid = float(np.sum(np.exp((x[:-1] + x[1:]) / 2)) * h)
    print(f"{n:>8} {abs(left - exact):>13.3e} {abs(right - exact):>13.3e} "
          f"{abs(mid - exact):>13.3e}")
print()
print("left and right are first order. The middle "
      "is second, for the same count of calls.")
