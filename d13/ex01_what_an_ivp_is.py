"""An equation for the SLOPE, a value at one instant, and the curve those two pin down.
"""
import numpy as np
import sympy as sp

t, y = sp.symbols("t y")
sol = sp.dsolve(sp.Eq(sp.Function("f")(t).diff(t), sp.Function("f")(t) - t ** 2 + 1),
                sp.Function("f")(t), ics={sp.Function("f")(0): 0.5})
print(f"the equation : y' = y - t^2 + 1,  y(0) = 0.5")
print(f"its solution : {sol.rhs}")
print()
f = sp.lambdify(t, sol.rhs, "numpy")
print(f"{'t':>5} {'y(t)':>12} {'slope there':>14}")
for v in (0.0, 0.5, 1.0, 1.5, 2.0):
    print(f"{v:>5.1f} {float(f(v)):>12.6f} {float(f(v)) - v ** 2 + 1:>14.6f}")
print()
print("the slope at every point is known before "
      "the curve is. That is the whole problem.")
