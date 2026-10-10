"""What the stability cost: a root-finding problem inside every step."""
import numpy as np

from nmkit.ode import euler, euler_implicit


def base(t, y):
    """A nonlinear stiff equation, so the implicit step cannot be rearranged by hand.

    Its solution is cos(t): the cubic terms cancel there, and so does the stiff part.
    """
    return np.array([-1000.0 * (y[0] - np.cos(t)) - np.sin(t)
                     - y[0] ** 3 + np.cos(t) ** 3])


print(f"the exact solution is cos(t), so y(3) = {np.cos(3.0):.9f}")
print(f"explicit Euler is stable only while h <= 2/1000 = {2 / 1000:.4f}")
print()
print(f"{'method':>16} {'h':>7} {'steps':>7} {'calls':>7} {'per step':>9} "
      f"{'y(3)':>13} {'error':>11}")
for name, method, h in (("explicit Euler", euler, 0.002),
                        ("explicit Euler", euler, 0.0005),
                        ("implicit Euler", euler_implicit, 0.05),
                        ("implicit Euler", euler_implicit, 0.01)):
    calls = [0]

    def counted(t, y):
        calls[0] += 1
        return base(t, y)

    n = int(round(3.0 / h))
    _, ys = method(counted, 0.0, [1.0], h, n)
    v = float(ys[-1])
    print(f"{name:>16} {h:>7.4f} {n:>7} {calls[0]:>7} {calls[0] / n:>9.2f} "
          f"{v:>13.8f} {abs(v - np.cos(3.0)):>11.2e}")
print()
print("the implicit method evaluates the equation about ten times per step, and the")
print("finite-difference Jacobian costs most of those. At the coarse end it still")
print("wins: 600 calls beat 1500 with a smaller error, because stability does not")
print("hold its step down. For a tight error, explicit Euler at h = 0.0005 wins.")
