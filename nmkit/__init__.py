"""nmkit — the numerical methods library built across the fourteen days of this book.

Every routine here is written in a chapter, run in that chapter, and checked against an
independent implementation before the chapter ends. Nothing is imported from SciPy at
run time: SciPy appears in the book only as an oracle, in programs that compare the two
answers.

Module      Day   What it holds
------      ---   -------------
fp          1     what a floating-point number is made of
err         1     absolute and relative error, significant digits, error tables
roots       2,3   bisection, false position, fixed point, Newton, secant
linsolve    4     substitution, Gaussian elimination, LU with partial pivoting
norms       5     vector and matrix norms, condition number
factor      5     Cholesky, Gram-Schmidt, Householder QR
iterative   6     Jacobi, Gauss-Seidel, successive over-relaxation
nlsys       6     Newton and Broyden for systems
eigen       7     power method, inverse iteration, QR algorithm, singular values
interp      8     Vandermonde, Lagrange, divided differences, Chebyshev nodes
spline      9     the Thomas algorithm and cubic splines
lstsq       10    normal equations, least squares by QR, polynomial fitting
diff        11    finite differences and Richardson extrapolation
quad        12    trapezoidal, Simpson, Romberg, Gauss-Legendre, adaptive
ode         13,14 Euler, Heun, Runge-Kutta, step control, implicit methods
bvp         14    the shooting method and finite differences for boundary problems
"""
__version__ = "1.0"
