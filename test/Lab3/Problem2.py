# write unit tests for the function in Problem2.py

import unittest
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.Lab3.Problem1 import LUDecomposition
from NumericalLinearAlgebra.Lab3.Problem2 import LUDecompositionEvaluateTime, LUDecompositionEvaluateTimeDifferentSize

class Problem2Test(unittest.TestCase):
    def test_LUDecompositionEvaluateTime(self):
        A = Matrix.Random_Square_Matrix_Int(30)
        L,U,time = LUDecompositionEvaluateTime(A)
        print("Time: ",time)

    def test_LUDecompositionEvaluateTime_repeat(self):
        LUDecompositionEvaluateTimeDifferentSize()