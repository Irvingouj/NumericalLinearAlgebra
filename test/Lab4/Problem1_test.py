from concurrent.futures import ThreadPoolExecutor
import unittest
import math
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector
from NumericalLinearAlgebra.Lab4.Problem1 import solve_with_LU, solve_with_Cholesky,compare_time,solve_triangle_down_band,solve_triangle_up_band
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.Lab2 import TriangUp, TriangDown
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

    def test_compare_time(self):
        
        times = []
        
        for i in range(10,500,50):
            lu,ch = compare_time(i,lambda x: math.pi**2 * math.sin(math.pi * x),0,0)
            times.append((lu,ch,i))
            self.assertLessEqual(lu,ch)
        
        lu,ch = compare_time(50,lambda x: math.pi**2 * math.sin(math.pi * x),0,0)
        
        with open('time.txt','w') as f:
            for data in times:
                f.write("at n = " + str(data[2]) + " LU time = " + str(data[0]) + " Cholesky time = " + str(data[1])+"\n")
                
    def test_solve_triangle_down_band(self):
        A = Matrix.from_list([
            [2,0,0,0,0],
            [1,2,0,0,0],
            [0,1,2,0,0],
            [0,0,1,2,0],
            [0,0,0,1,2]
        ])
        
        b = Vector([1,2,3,4,5])
        
        x = solve_triangle_down_band(A,b,1)
        
        x_correct = TriangDown(A,b)
        
        [self.assertAlmostEqual(x.get(i),x_correct.get(i)) for i in range(5)]
        
    def test_solve_triangle_up_band(self):
         A = Matrix.from_list([
            [2,1,0,0,0],
            [0,2,1,0,0],
            [0,0,2,1,0],
            [0,0,0,2,1],
            [0,0,0,0,2]
         ])
         
         b = Vector([1,2,3,4,5])
         
         x = solve_triangle_up_band(A,b,1)
         
         x_correct = TriangUp(A,b)
         
         [self.assertAlmostEqual(x.get(i),x_correct.get(i)) for i in range(5)]
         
    def test_convergence_error(self):
        differences = []
        n = 5
        f = lambda x: math.pi**2 * math.sin(math.pi * x)
        power = 8
        n_s = [ n*2**i for i in range(8)]
        
        with ThreadPoolExecutor(max_workers=power) as executor:
            res = executor.map(self._get_error_different_for_n, [f]*power, n_s)
        
        differences = list(res)
        differences.sort(key=lambda x: x[0])

        with open('convergence.txt','w') as f:
            for data in differences:
                f.write("at n = " + str(data[0]) + " error = " + str(data[1]) + "\n")
                
                
    def _get_error_different_for_n(self,f,n):
        h = 1 / n
        x_exact = [math.sin(math.pi * i * h) for i in range(1, n)]
        res,time = solve_with_LU(n,lambda x: math.pi**2 * math.sin(math.pi * x),0,0)
        return (n,math.sqrt(sum([(x_exact[i]-res.get(i))**2 for i in range(n-1)])))
    
    
    def test_convergence_plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        import re
        pattern = r"at n = (\d+) error = ([\d\.]+(?:[eE][-+]?\d+)?)"
        
        ns = []
        errors = []
        with open('convergence.txt','r') as f:
            for line in f:
                match = re.search(pattern, line)
                n = int(match.group(1))
                err = float(match.group(2))
                ns.append(n)
                errors.append(err)
                
        hs = [1/n for n in ns]
        hs.reverse()
        errors.reverse()

        plt.plot(hs,errors,marker='o',linestyle='--',color='r',label='error')
        plt.show()
        plt.plot([math.log(h) for h in hs ],[math.log(e) for e in errors],marker='x',linestyle='--',color='b',label='log')
        plt.show()