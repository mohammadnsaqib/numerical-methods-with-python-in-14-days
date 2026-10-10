"""The derivative is a limit, and this is that limit computed at ten values of h."""
import numpy as np

x = 1.0
true = np.cos(x)
print(f"{'h':>10} {'(f(x+h) - f(x)) / h':>24} {'error':>14}")
for k in range(1, 11):
    h = 10.0 ** (-k)
    est = (np.sin(x + h) - np.sin(x)) / h
    print(f"{h:>10.0e} {est:>24.15f} {abs(est - true):>14.3e}")
print(f"{'exact':>10} {true:>24.15f}")
