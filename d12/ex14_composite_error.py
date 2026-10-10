"""Where the third power goes: one panel keeps it and n panels do not."""
import numpy as np

from nmkit.quad import trapezoid, trapezoid_n

exact_on = lambda a, b: np.exp(b) - np.exp(a)

print("ONE panel, on an interval that shrinks")
print(f"{'width':>10} {'error':>13} {'error ratio':>13}")
prev = None
for k in range(1, 6):
    w = 2.0 ** (-k)
    e = abs(trapezoid(np.exp, 0.0, w) - exact_on(0.0, w))
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{w:>10.6f} {e:>13.3e} {ratio:>13}")
    prev = e
print()
print("n panels, on an interval that does not")
print(f"{'width':>10} {'error':>13} {'error ratio':>13}")
prev = None
for k in range(1, 6):
    n = 2 ** k
    e = abs(trapezoid_n(np.exp, 0.0, 1.0, n) - exact_on(0.0, 1.0))
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{1.0 / n:>10.6f} {e:>13.3e} {ratio:>13}")
    prev = e
print()
print("the ratios are 8 and 4. Halving the width divides one panel's error by eight,")
print("and there are twice as many panels to add up.")
