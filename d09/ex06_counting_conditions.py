"""Four unknowns per piece, and the conditions run two short of pinning them down."""
def counts(n):
    pieces = n - 1
    unknowns = 4 * pieces
    through = 2 * pieces          # each piece meets the data at both its ends
    first = n - 2                 # slopes match at the interior knots
    second = n - 2                # curvatures match there too
    return pieces, unknowns, through + first + second

print(f"{'knots':>7} {'pieces':>8} {'unknowns':>10} {'conditions':>12} "
      f"{'short by':>10}")
for n in (3, 4, 5, 10, 100):
    p, u, c = counts(n)
    print(f"{n:>7} {p:>8} {u:>10} {c:>12} {u - c:>10}")
print("\ntwo short at every size, which is why two end conditions are needed.")
