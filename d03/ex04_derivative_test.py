"""Whether an iteration converges is decided by the size of g' at the root, and it is
computable."""
root = 2.0945514815423265
h = 1e-7

g1 = lambda x: (2 * x + 5) ** (1 / 3)
g2 = lambda x: (x ** 3 - 5) / 2
g3 = lambda x: 5 / (x * x - 2)

for name, g in (("cube root form", g1), ("linear term", g2), ("constant term", g3)):
    slope = (g(root + h) - g(root - h)) / (2 * h)
    print(f"{name:<16} g'(root) = {slope:+.6f}   |g'| < 1 ? {abs(slope) < 1}")
