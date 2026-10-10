"""The ratio of one error to the next settles on g' itself, which is why the test is
that number."""
from nmkit.roots import fixed_point

root = 2.0945514815423265
g = lambda x: (2 * x + 5) ** (1 / 3)
r = fixed_point(g, 2.0, tol=1e-15, max_iter=80)

errs = [abs(x - root) for x, _ in r.history if abs(x - root) > 0]
print(f"{'step':>5} {'error':>12} {'ratio':>10}")
for k in range(1, 9):
    print(f"{k:>5} {errs[k]:>12.4e} {errs[k] / errs[k - 1]:>10.6f}")

# Measured here rather than quoted, so the two numbers cannot drift apart. An earlier
# draft printed a slope typed in by hand and it disagreed with the ratio above in the
# third digit.
h = 1e-7
slope = (g(root + h) - g(root - h)) / (2 * h)
print(f"\ng'(root) by a central difference: {slope:.6f}")
