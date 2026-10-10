"""The day's routines against an independent implementation, on four functions."""
import numpy as np
import scipy.differentiate as sd
import sympy as sp

from nmkit.diff import best_step, central_diff, five_point, richardson

t = sp.Symbol("t")
cases = [(sp.sin(t), 1.0), (sp.exp(t), 0.5), (sp.log(t), 2.0),
         (t ** 5 - 3 * t ** 2, 1.3)]

print(f"{'f':>16} {'centred':>11} {'five point':>12} {'Richardson':>12} {'scipy':>11}")
for expr, at in cases:
    f = sp.lambdify(t, expr, "numpy")
    exact = float(sp.diff(expr, t).subs(t, at))
    h = best_step(2)
    e_c = abs(central_diff(f, at, h) - exact)
    e_5 = abs(five_point(f, at, 1e-3) - exact)
    T = richardson(lambda xx, hh: central_diff(f, xx, hh), at, 0.2, order=2, gap=2,
                   levels=5)
    e_r = abs(T[4, 4] - exact)
    e_s = abs(float(sd.derivative(f, at).df) - exact)
    print(f"{str(expr):>16} {e_c:>11.2e} {e_5:>12.2e} {e_r:>12.2e} {e_s:>11.2e}")
print()
print("every column is an error against the derivative done in symbols")
