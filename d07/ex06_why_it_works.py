"""Every vector is a mixture, and each part is multiplied by its own eigenvalue every
step."""
import numpy as np

A = np.array([[3.0, 1.0], [1.0, 3.0]])
e1 = np.array([1.0, 1.0]) / np.sqrt(2)               # eigenvalue 4
e2 = np.array([1.0, -1.0]) / np.sqrt(2)              # eigenvalue 2
x = 0.3 * e1 + 0.7 * e2

print(f"{'step':>5} {'share of e1':>14} {'share of e2':>14} {'ratio':>10}")
for k in range(6):
    a, b = x @ e1, x @ e2
    print(f"{k:>5} {a:>14.8f} {b:>14.8f} {abs(b / a):>10.6f}")
    x = A @ x
print("\nthe ratio falls by 2/4 = 0.5 every step, which is why e1 takes over.")
