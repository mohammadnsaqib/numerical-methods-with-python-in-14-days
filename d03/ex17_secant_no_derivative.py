"""Where no derivative is available in closed form, the secant method still applies."""
import math

from nmkit.roots import secant

def f(x):
    """A function defined by a loop: there is no formula to differentiate."""
    total = 0.0
    for n in range(1, 40):
        total += math.sin(n * x) / n ** 2
    return total - 0.5

r = secant(f, 0.5, 1.0, tol=1e-13)
print("converged:", r.converged, " steps:", r.iterations)
print("root     :", f"{r.root:.14f}")
print("f(root)  :", f"{f(r.root):+.3e}")
