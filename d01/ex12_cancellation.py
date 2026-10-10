"""Subtracting two close numbers destroys the digits they had in common."""
print(f"{'x':>10} {'(1+x)-1':>24} {'relative error':>16}")
x = 1.0
for _ in range(8):
    x /= 100.0
    computed = (1.0 + x) - 1.0
    print(f"{x:>10.0e} {computed:>24.17g} {abs(computed - x) / x:>16.3e}")
