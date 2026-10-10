"""The secant line through the last two points replaces the tangent, so no derivative is
needed."""
def f(x):
    return x ** 3 - 2 * x - 5

a, b = 3.0, 2.5
print(f"{'step':>5} {'a':>18} {'b':>18} {'next':>18}")
for k in range(1, 5):
    fa, fb = f(a), f(b)
    nxt = b - fb * (b - a) / (fb - fa)
    print(f"{k:>5} {a:>18.12f} {b:>18.12f} {nxt:>18.12f}")
    a, b = b, nxt
