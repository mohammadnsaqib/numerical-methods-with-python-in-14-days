"""Problem 11.40: a gradient by differences, checked against the gradient in symbols."""
import numpy as np
import sympy as sp

from nmkit.diff import best_step, gradient

u, v, w = sp.symbols("u v w")
expr = sp.exp(u * v) + sp.sin(w) * u ** 2 - sp.log(1 + v ** 2 + w ** 2)
f = sp.lambdify((u, v, w), expr, "numpy")

point = np.array([0.4, 1.1, 0.7])
exact = np.array([float(sp.diff(expr, s).subs({u: point[0], v: point[1], w: point[2]}))
                  for s in (u, v, w)])
est = gradient(lambda p: f(p[0], p[1], p[2]), point)

print(f"{'variable':>10} {'by differences':>18} {'in symbols':>18} {'error':>12}")
for name, a, b in zip(("u", "v", "w"), est, exact):
    print(f"{name:>10} {a:>18.12f} {b:>18.12f} {abs(a - b):>12.3e}")
print()
print(f"the step used was {best_step(2):.3e}, and 6 function calls were needed for 3 "
      f"partials")
