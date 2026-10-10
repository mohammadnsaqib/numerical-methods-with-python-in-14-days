"""Where Simpson's rule comes from: two rules whose errors have opposite signs."""
import numpy as np

from nmkit.quad import midpoint, simpson, trapezoid

exact = np.e - 1.0
a, b = 0.0, 1.0
T, M = trapezoid(np.exp, a, b), midpoint(np.exp, a, b)
print(f"trapezoidal : {T:.15f}   error {T - exact:+.9f}")
print(f"midpoint    : {M:.15f}   error {M - exact:+.9f}")
print(f"the errors have opposite signs, and the first is "
      f"{abs(T - exact) / abs(M - exact):.4f} times the second")
print()
print(f"one part trapezoidal to two parts midpoint: {(T + 2 * M) / 3:.15f}")
print(f"Simpson's rule on the same panel          : {simpson(np.exp, a, b):.15f}")
print(f"they differ by {abs((T + 2 * M) / 3 - simpson(np.exp, a, b)):.1e}")
