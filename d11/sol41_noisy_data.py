"""Problem 11.41: differentiating measurements that carry noise, where a small step is
fatal."""
import numpy as np

from nmkit.diff import central_diff

rng = np.random.default_rng(31013)
noise = 1e-6
x = 1.0
true = np.cos(x)


def measured(t):
    """sin(t), as an instrument with a fixed noise level would report it."""
    return np.sin(t) + rng.normal(scale=noise, size=np.shape(t))


print(f"{'h':>9} {'clean data':>13} {'noisy data':>13} {'noise / h':>12}")
for h in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    clean = abs(central_diff(np.sin, x, h) - true)
    errs = [abs(central_diff(measured, x, h) - true) for _ in range(400)]
    print(f"{h:>9.0e} {clean:>13.3e} {np.mean(errs):>13.3e} {noise / h:>12.3e}")
print()
print("the noise level replaces the machine epsilon, so the best step moves up by")
print(f"the cube root of their ratio: about "
      f"{(noise / np.finfo(float).eps) ** (1 / 3):.0f} times")
