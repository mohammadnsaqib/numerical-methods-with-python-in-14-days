"""Each basis function is one at its own node and zero at every other."""
import numpy as np

xs = np.array([0.0, 1.0, 2.0])

def basis(i, t):
    out = np.ones_like(np.atleast_1d(np.asarray(t, float)))
    for j in range(xs.size):
        if i != j:
            out = out * (t - xs[j]) / (xs[i] - xs[j])
    return out

print(f"{'':>10} {'at x=0':>10} {'at x=1':>10} {'at x=2':>10}")
for i in range(3):
    vals = basis(i, xs)
    print(f"basis {i}   {vals[0]:>10.4f} {vals[1]:>10.4f} {vals[2]:>10.4f}")
