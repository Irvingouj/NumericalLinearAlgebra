import unittest

import numpy as np
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector
from Lab3.Problem4 import CHOLfact,inverseCol


class Problem3Test(unittest.TestCase):
    def test_CHOL(self):
        l = [[10, 3, 1, 2],
              [3, 9, -2, 4],
              [1, -2, 7, 0],
              [2, 4, 0, 5]]
        
        arr = np.array(l)
        A = Matrix.from_list(
            [[10, 3, 1, 2],
              [3, 9, -2, 4],
              [1, -2, 7, 0],
              [2, 4, 0, 5]]
            )
        L, time = CHOLfact(A)
        
        self.assertAlmostEqual(L.matrix, np.linalg.cholesky(arr).tolist())   
        
        b = Vector([1, 2, 3, 4])
        x = inverseCol(L, b);
        
        self.assertTrue(A*x == b);
        
        