"""Pushed far enough, the quotient stops improving and then returns nothing at all."""
import numpy as np

x = 1.0
true = np.cos(x)
print(f"{'h':>10} {'estimate':>22} {'error':>12}")
for k in (8, 10, 12, 14, 15, 16, 17):
    h = 10.0 ** (-k)
    est = (np.sin(x + h) - np.sin(x)) / h
    print(f"{h:>10.0e} {est:>22.15f} {abs(est - true):>12.3e}")
print()
print("at h = 1e-17 the two values are the same "
      "number, so the numerator is exactly zero:")
h = 1e-17
print(f"  sin(x + h) == sin(x): {np.sin(x + h) == np.sin(x)}")
print(f"  the quotient        : {(np.sin(x + h) - np.sin(x)) / h}")
