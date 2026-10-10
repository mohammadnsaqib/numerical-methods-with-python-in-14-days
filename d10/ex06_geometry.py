"""The fit is the shadow of the data on the space the model can reach."""
import numpy as np

from nmkit.lstsq import lstsq_qr, residual

A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
b = np.array([1.0, 3.0, 2.0])
x = lstsq_qr(A, b)
fit = A @ x
r = residual(A, x, b)

print("the data      :", b)
print("what the model reaches:", np.array2string(fit, precision=8))
print("what is left  :", np.array2string(r, precision=8))
print("they are at right angles:", f"{float(fit @ r):+.3e}")
print("and the lengths obey Pythagoras:",
      f"{float(b @ b):.8f}", "=", f"{float(fit @ fit + r @ r):.8f}")
