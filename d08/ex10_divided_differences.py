"""The table is built column by column, each entry from two in the column before it."""
import numpy as np

from nmkit.interp import divided_differences

xs = np.array([0.0, 1.0, 2.0, 4.0])
ys = np.array([1.0, 3.0, 2.0, 5.0])
T = divided_differences(xs, ys)

print("the table (upper triangle is what matters):")
print(np.array2string(np.triu(T), precision=8))
print("\nthe top row is the Newton form's coefficients:")
print(np.array2string(T[0], precision=10))
