"""The error has three factors, and only one of them depends on where the nodes were
put."""
import numpy as np

from nmkit.interp import error_product, lagrange_eval

xs = np.linspace(0.0, 1.0, 5)
f = np.exp
t = np.linspace(0.0, 1.0, 400)

actual = np.abs(f(t) - lagrange_eval(xs, f(xs), t))
# The fifth derivative of exp is exp, at most e on [0, 1]; the factorial is 5!.
bound = np.abs(error_product(xs, t)) * np.e / 120.0

print("largest actual error:", f"{np.max(actual):.6e}")
print("largest bound       :", f"{np.max(bound):.6e}")
print("the bound holds everywhere:", bool(np.all(actual <= bound + 1e-15)))
