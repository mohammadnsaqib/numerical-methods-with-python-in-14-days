"""Four steps of bisection, printed in full, so the invariant can be checked by eye."""
def f(x):
    return x ** 3 - 2 * x - 5

a, b = 2.0, 3.0
print(f"{'step':>4} {'a':>12} {'b':>12} {'mid':>12} {'f(mid)':>14} {'width':>10}")
for k in range(1, 5):
    m = a + (b - a) / 2
    fm = f(m)
    print(f"{k:>4} {a:>12.6f} {b:>12.6f} {m:>12.6f} {fm:>+14.6f} {b - a:>10.6f}")
    if f(a) * fm < 0:
        b = m
    else:
        a = m
print("\nafter every step one end is negative and the other positive.")
