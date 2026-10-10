"""Anything smaller than half an epsilon is invisible when added to 1, and that is by
design."""
EPS = 2.0 ** -52

for name, delta in (("eps", EPS), ("eps/2", EPS / 2), ("eps/4", EPS / 4)):
    total = 1.0 + delta
    print(f"1 + {name:<6} == 1 ?  {str(total == 1.0):<6} value = {total:.20f}")

print()
print("but the same deltas are perfectly representable on their own:")
for name, delta in (("eps", EPS), ("eps/2", EPS / 2), ("eps/4", EPS / 4)):
    print(f"  {name:<6} = {delta:.6e}  is zero ? {delta == 0.0}")
