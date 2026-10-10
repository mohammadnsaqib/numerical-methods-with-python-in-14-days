"""The oracle for this whole day: the derivative done in symbols, not in floating point.
"""
import numpy as np
import sympy as sp

t = sp.Symbol("t")
for expr, at in ((sp.sin(t), 1.0), (sp.exp(t) * sp.cos(t), 0.3), (sp.log(t) / t, 2.0)):
    d = sp.diff(expr, t)
    exact = float(d.subs(t, at))
    f = sp.lambdify(t, expr, "numpy")
    est = (f(at + 1e-6) - f(at - 1e-6)) / 2e-6
    print(f"f(t) = {str(expr):>16}   f'(t) = {str(sp.simplify(d)):>28}")
    print(f"{'':>19}at t = {at}: exact {exact:.12f}, estimated {est:.12f}")
