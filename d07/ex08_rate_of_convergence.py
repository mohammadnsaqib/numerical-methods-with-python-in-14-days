"""The DIRECTION improves by the ratio of the second eigenvalue to the first, and the
VALUE by its square."""
import numpy as np

from nmkit.eigen import power_method

print(f"{'second/first':>13} {'its square':>11} {'ratio seen':>12} {'iterations':>12}")
for second in (0.2, 0.5, 0.8, 0.95):
    A = np.diag([1.0, second, second / 2])
    Q, _ = np.linalg.qr(np.random.default_rng(101).normal(size=(3, 3)))
    M = Q @ A @ Q.T  # same eigenvalues, no longer diagonal
    lam, _, k, hist = power_method(M, tol=1e-12, max_iter=4000)
    errs = [abs(h - 1.0) for h in hist if abs(h - 1.0) > 1e-14]
    seen = errs[-1] / errs[-2] if len(errs) > 2 else float("nan")
    print(f"{second:>13.2f} {second ** 2:>11.4f} {seen:>12.6f} {k:>12}")
print()
print("the ratio seen matches the SQUARE, because the eigenvalue is read off with the")
print("Rayleigh quotient, whose error is the square of the error in the direction.")
