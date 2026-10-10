"""How long a step each method survives on the same decaying equation."""
import numpy as np

from nmkit.ode import euler, heun, midpoint_ode, rk4, stability_region

LAM = -15.0
methods = [("euler", euler), ("heun", heun), ("midpoint", midpoint_ode), ("rk4", rk4)]

print(f"{'method':>10} {'largest stable z':>18} {'largest stable h':>18} "
      f"{'y(2) just past it':>19}")
limits = {}
for name, run in methods:
    zs = np.linspace(-4.0, -1e-6, 400000)
    ok = zs[stability_region(name if name != "midpoint" else "heun", zs) <= 1.0]
    z_max = float(np.min(ok))
    h_max = z_max / LAM
    h_over = h_max * 1.05
    n = max(1, int(round(2.0 / h_over)))
    _, ys = run(lambda t, y: LAM * y, 0.0, 1.0, h_over, n)
    limits[name] = h_max
    print(f"{name:>10} {z_max:>18.6f} {h_max:>18.6f} {float(ys[-1]):>19.3e}")
print()
print("Heun and the midpoint rule have the same "
      "stability polynomial, so the same limit.")
print(f"RK4 survives a step {limits['rk4'] / limits['euler']:.4f} times longer than "
      f"Euler's, for four times the work.")
print("A higher order buys accuracy. It does not buy much stability, and Day 14 shows")
print("what to reach for when the step this allows is still far too short.")
