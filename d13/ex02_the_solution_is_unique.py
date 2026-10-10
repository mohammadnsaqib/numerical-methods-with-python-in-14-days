"""One slope rule, four starting values, four curves that never meet."""
import numpy as np

from nmkit.ode import rk4


def f(t, y):
    """y' = y - t^2 + 1, the equation of Example 13.1."""
    return y - t ** 2 + 1.0


print(f"{'t':>5} " + " ".join(f"{'y0 = ' + str(v):>12}" for v in (0.0, 0.5, 1.0, 1.5)))
tracks = [rk4(f, 0.0, v, 0.01, 200)[1] for v in (0.0, 0.5, 1.0, 1.5)]
for k in (0, 50, 100, 150, 200):
    print(f"{k * 0.01:>5.2f} " + " ".join(f"{tr[k]:>12.6f}" for tr in tracks))
print()
gaps = [abs(tracks[i + 1][-1] - tracks[i][-1]) for i in range(3)]
print(f"every pair started 0.5 apart and ends {gaps[0]:.6f} apart")
print(f"that is a factor of {gaps[0] / 0.5:.6f}, and exp(2) is {float(np.exp(2)):.6f}")
print("the curves spread apart and never cross. Two solutions of one equation cannot.")
