"""The same idea downwards: a lower triangular system is solved from the top."""
import numpy as np

from nmkit.linsolve import fwd_sub

L = np.array([[1.0, 0.0, 0.0], [-1.5, 1.0, 0.0], [-1.0, 4.0, 1.0]])
y_true = np.array([8.0, 1.0, 1.0])
b = L @ y_true

y = fwd_sub(L, b)
print("L has ones on the diagonal, so no division is needed at all.")
print("b        :", b)
print("recovered:", y)
print("true     :", y_true)
