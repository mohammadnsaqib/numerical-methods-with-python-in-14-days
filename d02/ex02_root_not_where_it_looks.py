"""A plot at coarse resolution can put a root in the wrong place, or hide one entirely.
"""
import numpy as np

def f(x):
    return np.sin(10 * x) * np.exp(-x)

coarse = np.linspace(0, 3, 7)
fine = np.linspace(0, 3, 601)

def sign_changes(xs):
    v = f(xs)
    return int(np.sum(v[:-1] * v[1:] < 0))

print("samples at 7 points :", sign_changes(coarse), "sign changes seen")
print("samples at 601 points:", sign_changes(fine), "sign changes seen")
print("true count of roots in (0, 3):", int(10 * 3 / np.pi))
