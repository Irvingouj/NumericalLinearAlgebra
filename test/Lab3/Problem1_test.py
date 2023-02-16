import unittest
from AlgebraObject.Matrix import Matrix
from AlgebraObject.Vector import Vector
from Lab2 import TriangUp, TriangDown
from Lab3.Problem1 import LUDecomposition, solve_with_LU
import numpy as np


# Unit test for TriangUp and TriangDown
class Problem1Test(unittest.TestCase):

    def test_solve_with_LU(self):
        A = Matrix.Random_Square_Matrix_Int(3)
        b = Vector.Random_Vector_Int(3)

        numpy_A = np.array(A.matrix)

        numpy_b = np.array(b.transpose().matrix[0])
        
        numpy_x = np.linalg.solve(numpy_A,numpy_b)

        solve_with_LU_x = solve_with_LU(A,b)

        print(solve_with_LU_x.transpose().matrix[0])
        print(numpy_x)

        [self.assertAlmostEqual(solve_with_LU_x.get(i),numpy_x[i]) for i in range(len(numpy_x))]

    def test_solve_with_LU_repeat(self):
        for i in range(10):
            self.test_solve_with_LU()

    def test_LUDecomposition(self):
        A = Matrix.Random_Square_Matrix_Int(5)
        ori = A.copy()
        L,U = LUDecomposition(A)
        self.assertTrue(L.is_lower_triangular())
        self.assertTrue(U.is_upper_triangular())

        L.print("L")
        U.print("U")
        ori.print("Original A")

        (L*U).print("L*U")

        self.assertTrue((L*U) == ori)
        

    def test_LUDecomposition_repeat(self):
        for i in range(10):
            self.test_LUDecomposition()

   


if __name__ == "__main__":
    unittest.main()