"""An eigenvector is a direction the matrix does not turn, and the eigenvalue is the
stretch."""
import numpy as np

A = np.array([[3.0, 1.0], [1.0, 3.0]])
for name, v in (("an eigenvector    ", np.array([1.0, 1.0])),
                ("another           ", np.array([1.0, -1.0])),
                ("not an eigenvector", np.array([1.0, 0.0]))):
    Av = A @ v
    print(f"{name}: v = {v}   A v = {Av}")
    ratios = Av / v
    print(f"{'':20}  entry by entry ratio {np.array2string(ratios, precision=6)}")
