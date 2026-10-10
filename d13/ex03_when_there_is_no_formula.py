"""Two equations of similar length, one of which symbols can solve and one of which they
cannot."""
import numpy as np
import sympy as sp

from nmkit.ode import rk4

t = sp.Symbol("t")
f = sp.Function("f")
for rhs, label in ((f(t) - t ** 2 + 1, "y' = y - t^2 + 1"),
                   (sp.sin(t * f(t)), "y' = sin(t y)")):
    try:
        sol = sp.dsolve(sp.Eq(f(t).diff(t), rhs), f(t))
        print(f"{label:>18} : solved -> {sol.rhs}")
    except NotImplementedError as exc:
        print(f"{label:>18} : {type(exc).__name__}")
        print(f"{'':>21}{str(exc)[:74]}")
print()
_, ys = rk4(lambda tv, yv: np.sin(tv * yv), 0.0, 1.0, 0.001, 3000)
print(f"the second equation at t = 3, by fourth-order Runge-Kutta: "
      f"{float(ys[-1]):.12f}")
print("a method that only asks for the slope "
      "does not know one is harder than the other.")
