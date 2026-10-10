"""Steps are the wrong currency: what a method costs is evaluations of F."""
import numpy as np
from scipy.optimize import fsolve

from nmkit.nlsys import broyden, count_calls, newton_system

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0, np.exp(x) + y - 1.0])

Fn = count_calls(F)
xn, kn, _ = newton_system(Fn, [1.0, 1.0], tol=1e-12)
Fb = count_calls(F)
xb, kb, _ = broyden(Fb, [1.0, 1.0], tol=1e-12)
sp = fsolve(F, [1.0, 1.0], xtol=1e-13)

print(f"Newton : {kn:>2} steps, {Fn.count():>3} evaluations -> "
      f"{np.array2string(xn, precision=10)}")
print(f"Broyden: {kb:>2} steps, {Fb.count():>3} evaluations -> "
      f"{np.array2string(xb, precision=10)}")
print(f"scipy fsolve                      -> {np.array2string(sp, precision=10)}")
print("largest gap between the three:",
      f"{max(np.max(np.abs(xn - sp)), np.max(np.abs(xb - sp))):.3e}")
