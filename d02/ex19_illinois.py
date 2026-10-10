"""Halving the retained end's value breaks the stall, and it costs one line."""
from nmkit.roots import false_position

def f(x):
    return x ** 10 - 1.0

plain = false_position(f, 0.0, 1.3, tol=1e-12, max_iter=500)
fixed = false_position(f, 0.0, 1.3, tol=1e-12, max_iter=500, illinois=True)

print("plain false position:", plain.iterations, "steps, root", f"{plain.root:.12f}")
print("with the halving    :", fixed.iterations, "steps, root", f"{fixed.root:.12f}")
print("both agree with 1.0 to:",
      f"{max(abs(plain.root - 1.0), abs(fixed.root - 1.0)):.2e}")
