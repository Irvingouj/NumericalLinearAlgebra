import unittest
import math
from NumericalLinearAlgebra.Lab4.Problem1 import solve_with_LU, solve_with_Cholesky
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector

class TestPoissonSolver(unittest.TestCase):

    def test_solve_with_LU(self):
        # Define test parameters
        n = 5
        alpha = 0
        beta = 0
        f = lambda x: math.pi**2 * math.sin(math.pi * x)

        # Solve using LU factorization
        x_lu, time_lu = solve_with_LU(n, f, alpha, beta)

        # Compute exact solution for comparison
        h = 1 / n
        x_exact = [math.sin(math.pi * i * h) for i in range(1, n)]
        x_exact_vec = Vector(x_exact)

        # Compare solution to exact solution
        self.assertAlmostEqual(x_lu, x_exact_vec, places=5)

    def test_solve_with_Cholesky(self):
        # Define test parameters
        n = 5
        alpha = 0
        beta = 0
        f = lambda x: math.pi**2 * math.sin(math.pi * x)

        # Solve using Cholesky factorization
        x_chol, time_chol = solve_with_Cholesky(n, f, alpha, beta)

        # Compute exact solution for comparison
        h = 1 / n
        x_exact = [math.sin(math.pi * i * h) for i in range(1, n)]
        x_exact_vec = Vector(x_exact)

        # Compare solution to exact solution
        self.assertAlmostEqual(x_chol, x_exact_vec, places=5)
