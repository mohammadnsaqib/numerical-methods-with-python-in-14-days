"""Problem 2.39: how the stall grows with the power, and what the halving costs."""
from nmkit.roots import false_position

print(f"{'n':>4} {'plain':>8} {'illinois':>10}")
for n in (2, 4, 6, 8, 10, 16, 24):
    f = (lambda p: (lambda x: x ** p - 1.0))(n)
    plain = false_position(f, 0.0, 1.3, tol=1e-12, max_iter=2000)
    fixed = false_position(f, 0.0, 1.3, tol=1e-12, max_iter=2000, illinois=True)
    print(f"{n:>4} {plain.iterations:>8} {fixed.iterations:>10}")
