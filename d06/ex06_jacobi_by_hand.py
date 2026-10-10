"""Each equation is solved for its own unknown, using the previous guess for the others.
"""
import numpy as np

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
b = np.array([2.0, 4.0, 10.0])
x = np.zeros(3)

print(f"{'sweep':>6} {'x1':>12} {'x2':>12} {'x3':>12}")
for k in range(1, 6):
    nxt = np.array([(b[0] + x[1]) / 4.0,
                    (b[1] + x[0] + x[2]) / 4.0,
                    (b[2] + x[1]) / 4.0])
    print(f"{k:>6} {nxt[0]:>12.8f} {nxt[1]:>12.8f} {nxt[2]:>12.8f}")
    x = nxt
print("\nthe true answer:", np.linalg.solve(A, b))
