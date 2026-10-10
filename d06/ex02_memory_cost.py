"""The cost of storing a factorisation grows as the square, and the sparse matrix does
not."""
def sparse_entries(n, per_row=5):
    return n * per_row

def full_entries(n):
    return n * n

print(f"{'n':>10} {'sparse, 5 per row':>19} {'a full factorisation':>22} {'ratio':>12}")
for n in (100, 1000, 10_000, 100_000, 1_000_000):
    s, f = sparse_entries(n), full_entries(n)
    print(f"{n:>10} {s:>19,} {f:>22,} {f / s:>12,.0f}")
print("\nat a million rows a full factorisation needs eight terabytes of doubles.")
