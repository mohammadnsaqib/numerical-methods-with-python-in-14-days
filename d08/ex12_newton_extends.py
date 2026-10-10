"""Adding a point appends one coefficient and changes none of the others."""
import numpy as np

from nmkit.interp import divided_differences

xs = np.array([0.0, 1.0, 2.0, 4.0])
ys = np.array([1.0, 3.0, 2.0, 5.0])

for n in (2, 3, 4):
    c = divided_differences(xs[:n], ys[:n])[0]
    print(f"{n} points: coefficients {np.array2string(c, precision=8)}")
c4 = divided_differences(xs, ys)[0]
print(f"4 points: coefficients {np.array2string(c4, precision=8)}")
print("\neach row is the row above it with one number appended.")
