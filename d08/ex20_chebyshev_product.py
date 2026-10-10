"""The same product, over Chebyshev nodes, is a fraction of what equal spacing gives."""
import numpy as np

from nmkit.interp import chebyshev_nodes, error_product

t = np.linspace(-1.0, 1.0, 2001)
print(f"{'points':>8} {'equally spaced':>18} {'Chebyshev':>14} {'ratio':>12}")
for n in (5, 9, 13, 17, 21):
    e = np.max(np.abs(error_product(np.linspace(-1, 1, n), t)))
    c = np.max(np.abs(error_product(chebyshev_nodes(-1, 1, n), t)))
    print(f"{n:>8} {e:>18.4e} {c:>14.4e} {e / c:>12.1f}")
