"""Richardson's table again, filled with areas instead of slopes."""
import numpy as np

from nmkit.quad import romberg

exact = 2.0
T = romberg(np.sin, 0.0, np.pi, levels=6)
print("the estimates")
for i in range(6):
    print("  " + " ".join(f"{T[i, j]:>18.14f}" for j in range(i + 1)))
print()
print("their errors")
for i in range(6):
    print("  " + " ".join(f"{abs(T[i, j] - exact):>10.2e}" for j in range(i + 1)))
print()
errs = [abs(T[i, j] - exact) for i in range(6) for j in range(i + 1)]
print(f"the first entry is wrong by {errs[0]:.2e} and the best by {min(errs):.2e},")
print(f"and the whole table used {2 ** 5 + 1} evaluations")
