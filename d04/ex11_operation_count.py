"""Elimination costs about n cubed over three operations, and the count can be measured.
"""

def count_ops(n):
    """Count the multiply-subtract pairs elimination performs on an n by n matrix."""
    total = 0
    for k in range(n - 1):
        for _ in range(k + 1, n):
            total += 1 + (n - k)          # one division, then n-k multiply-subtracts
    return total

print(f"{'n':>5} {'measured':>12} {'n**3 / 3':>12} {'ratio':>8}")
for n in (5, 10, 20, 50, 100, 200):
    m = count_ops(n)
    print(f"{n:>5} {m:>12} {n ** 3 / 3:>12.0f} {m / (n ** 3 / 3):>8.3f}")
