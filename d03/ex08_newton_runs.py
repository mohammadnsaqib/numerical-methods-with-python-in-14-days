"""The routine reaches the limit of the format in four steps from a start that is a
whole unit away."""
from mpmath import mp, findroot, mpf

from nmkit.roots import newton

mp.dps = 40
true = float(findroot(lambda x: x ** 3 - 2 * x - 5, mpf(2)))

r = newton(lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 3.0, tol=1e-15)
print("converged :", r.converged, " steps:", r.iterations)
print("root      :", f"{r.root:.16f}")
print("oracle    :", f"{true:.16f}")
print("abs error :", f"{abs(r.root - true):.3e}")
