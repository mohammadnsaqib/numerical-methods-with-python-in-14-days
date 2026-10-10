"""A bound is a promise about the worst case, and this checks the promise."""
import numpy as np
import sympy as sp

from nmkit.quad import trapezoid_n

t = sp.Symbol("t")
expr = sp.sin(t) * sp.exp(-t / 3)
a, b = 0.0, 4.0
f = sp.lambdify(t, expr, "numpy")
exact = float(sp.integrate(expr, (t, a, b)))

# The bound needs the largest size of the second derivative anywhere on the interval,
# which is found here by asking sympy for it rather than by guessing.
d2 = sp.lambdify(t, sp.diff(expr, t, 2), "numpy")
grid = np.linspace(a, b, 20001)
M = float(np.max(np.abs(d2(grid))))
print(f"the largest second derivative on [{a}, {b}] is {M:.6f}")
print()
print(f"{'panels':>8} {'actual error':>15} {'the bound':>13} {'inside?':>9}")
for n in (4, 8, 16, 32, 64, 128):
    h = (b - a) / n
    err = abs(trapezoid_n(f, a, b, n) - exact)
    bound = (b - a) * h * h * M / 12.0
    print(f"{n:>8} {err:>15.3e} {bound:>13.3e} {str(err <= bound):>9}")
