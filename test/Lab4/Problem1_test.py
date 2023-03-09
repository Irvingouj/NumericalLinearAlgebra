import unittest
import math
from NumericalLinearAlgebra.Lab4.Problem1 import solve_with_LU, solve_with_Cholesky
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector

class TestPoissonSolver(unittest.TestCase):

    def test_solve_with_LU(self):
        # Define test parameters
        n = 50
        alpha = 0
        beta = 0
        f = lambda x: math.pi**2 * math.sin(math.pi * x)

        # Solve using LU factorization
        x_lu, time_lu = solve_with_LU(n=n, f=f, alpha=alpha, beta=beta)

        # Compute exact solution for comparison
        h = 1 / n
        x_exact = [math.sin(math.pi * i * h) for i in range(1, n)]
        
        self.assertEqual(len(x_lu), len(x_exact))
        # Compare solution to exact solution
        [self.assertAlmostEqual(x_lu.get(i), x_exact[i], places=2) for i in range(n-1)]

    def test_solve_with_Cholesky(self):
        # Define test parameters
        n = 50
        alpha = 0
        beta = 0
        f = lambda x: math.pi**2 * math.sin(math.pi * x)

        # Solve using Cholesky factorization
        x_chol, time_chol = solve_with_Cholesky(n, f, alpha, beta)

        # Compute exact solution for comparison
        h = 1 / n
        x_exact = [math.sin(math.pi * i * h) for i in range(1, n)]
        

        self.assertEqual(len(x_chol), len(x_exact))
        [self.assertAlmostEqual(x_chol.get(i), x_exact[i], places=2) for i in range(n-1)]