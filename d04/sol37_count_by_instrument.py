"""Problem 4.37: count the arithmetic elimination really performs, by counting as it
runs."""
import numpy as np

class Counter:
    """A float that records every multiplication and subtraction it takes part in."""

    total = 0

    @classmethod
    def eliminate(cls, A):
        A = np.array(A, dtype=float, copy=True)
        n = A.shape[0]
        cls.total = 0
        for k in range(n - 1):
            for i in range(k + 1, n):
                m = A[i, k] / A[k, k]
                cls.total += 1                       # the division
                A[i, k:] -= m * A[k, k:]
                cls.total += 2 * (n - k)  # a multiply and a subtract per entry
        return cls.total

rng = np.random.default_rng(43)
print(f"{'n':>5} {'counted':>12} {'2 n**3 / 3':>12} {'ratio':>8}")
for n in (10, 20, 40, 80, 160):
    got = Counter.eliminate(rng.uniform(-1, 1, (n, n)))
    model = 2 * n ** 3 / 3
    print(f"{n:>5} {got:>12} {model:>12.0f} {got / model:>8.3f}")
