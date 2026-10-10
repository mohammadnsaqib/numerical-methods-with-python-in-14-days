"""Where the error comes from: the terms the formula throws away."""
import numpy as np
import sympy as sp

t = sp.Symbol("t")
x = 1.0
# The forward difference discards everything past the first derivative. The largest of
# the discarded terms is (h / 2) times the second derivative, so THAT is what the error
# should be.
second = float(sp.diff(sp.sin(t), t, 2).subs(t, x))
third = float(sp.diff(sp.sin(t), t, 3).subs(t, x))
true = float(sp.cos(x))

print(f"f''(x)  = {second:+.12f}     f'''(x) = {third:+.12f}")
print()
print(f"{'h':>8} {'forward error':>16} {'-(h/2) f\"':>16} {'centred error':>16} "
      f"{'-(h^2/6) f\"\"':>16}")
for h in (0.1, 0.05, 0.025, 0.0125):
    ef = (np.sin(x + h) - np.sin(x)) / h - true
    ec = (np.sin(x + h) - np.sin(x - h)) / (2 * h) - true
    print(f"{h:>8.4f} {ef:>16.3e} {h / 2 * second:>16.3e} {ec:>16.3e} "
          f"{h * h / 6 * third:>16.3e}")
