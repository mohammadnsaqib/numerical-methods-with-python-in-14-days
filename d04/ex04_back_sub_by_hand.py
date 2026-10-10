"""An upper triangular system is solved from the bottom up, one unknown at a time."""
import numpy as np

U = np.array([[2.0, 1.0, -1.0], [0.0, 0.5, 0.5], [0.0, 0.0, -1.0]])
b = np.array([8.0, 1.0, 1.0])

x = np.zeros(3)
x[2] = b[2] / U[2, 2]
print(f"row 3: {U[2,2]} * x3 = {b[2]}          -> x3 = {x[2]}")
x[1] = (b[1] - U[1, 2] * x[2]) / U[1, 1]
print(f"row 2: {U[1,1]} * x2 + {U[1,2]} * x3 = {b[1]}  -> x2 = {x[1]}")
x[0] = (b[0] - U[0, 1] * x[1] - U[0, 2] * x[2]) / U[0, 0]
print(f"row 1: {U[0,0]} * x1 + {U[0,1]} * x2 - {abs(U[0,2])} * x3 = {b[0]} -> x1 = "
      f"{x[0]}")
print("\nx =", x)
