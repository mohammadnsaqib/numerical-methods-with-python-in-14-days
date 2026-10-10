"""QR costs about twice the normal equations, and keeps twice the digits."""
def flops_normal(m, n):
    return m * n * n + n ** 3 // 3        # form A.T A, then factor it

def flops_qr(m, n):
    return 2 * m * n * n - 2 * n ** 3 // 3

print(f"{'rows':>7} {'cols':>6} {'normal':>12} {'QR':>12} {'ratio':>8}")
for m, n in ((100, 5), (1000, 10), (10000, 20), (100000, 50)):
    a, b = flops_normal(m, n), flops_qr(m, n)
    print(f"{m:>7} {n:>6} {a:>12} {b:>12} {b / a:>8.2f}")
