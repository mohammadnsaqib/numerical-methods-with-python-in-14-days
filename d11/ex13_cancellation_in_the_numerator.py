"""Why a tiny step ruins the numerator: the two values agree to nearly every digit."""
import numpy as np

x = 1.0
print(f"{'h':>8} {'f(x + h)':>22} {'f(x)':>22} {'shared digits':>15}")
for h in (1e-2, 1e-6, 1e-10, 1e-13, 1e-15):
    a, b = np.sin(x + h), np.sin(x)
    shared = 0 if a == b else int(-np.log10(abs(a - b) / abs(b)))
    print(f"{h:>8.0e} {a:>22.16f} {b:>22.16f} {shared:>15}")
print()
print("double precision carries about 16 digits. A numerator that shares 15 of them")
print("keeps 1, and dividing by h does not put the other 15 back.")
