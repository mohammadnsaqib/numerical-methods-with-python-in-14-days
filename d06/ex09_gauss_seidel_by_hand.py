"""One change: each new value is used at once by the equations below it."""
import numpy as np

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
b = np.array([2.0, 4.0, 10.0])
x = np.zeros(3)

print(f"{'sweep':>6} {'x1':>12} {'x2':>12} {'x3':>12}")
for k in range(1, 6):
    x[0] = (b[0] + x[1]) / 4.0            # uses the OLD x2
    x[1] = (b[1] + x[0] + x[2]) / 4.0     # uses the NEW x1
    x[2] = (b[2] + x[1]) / 4.0            # uses the NEW x2
    print(f"{k:>6} {x[0]:>12.8f} {x[1]:>12.8f} {x[2]:>12.8f}")
print("\nthe true answer:", np.linalg.solve(A, b))
