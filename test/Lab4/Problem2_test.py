import unittest
from NumericalLinearAlgebra.Lab4.Problem2 import *
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix

class Problem2_test(unittest.TestCase):
    def test_store_band(self):
        # Test input matrix
        A = Matrix.from_list(
                   [[1, 2, 0, 0, 0],
                    [3, 4, 5, 0, 0],
                    [0, 6, 7, 8, 0],
                    [0, 0, 9, 10, 11],
                    [0, 0, 0, 12, 13]])
        
        # Expected output banded matrix and values of p and q
        
        p_expected = 1
        q_expected = 1
        
        # Compute actual output using StoreBand function
        Aband_actual, p_actual, q_actual = StoreBand(A)
        
        # Check that actual and expected outputs are equal
        [self.assertEqual(Aband_actual.get_value(i, j), A.get_value(i, j)) for i in range(A.num_of_row) for j in range(A.num_of_col)]
        self.assertEqual(p_actual, p_expected)
        self.assertEqual(q_actual, q_expected)
        
    def test_inv_band(self):
                # Test input matrix
        A = Matrix.from_list(
                [[1, 2, 0, 0, 0],
                    [3, 4, 5, 0, 0],
                    [0, 6, 7, 8, 0],
                    [0, 0, 9, 10, 11],
                    [0, 0, 0, 12, 13]])
        
        Aband_actual, p_actual, q_actual = StoreBand(A)
        
        A_copy = invBand(Aband_actual, p_actual, q_actual)
        
        [self.assertEqual(A_copy.get_value(i, j), A.get_value(i, j)) for i in range(A.num_of_row) for j in range(A.num_of_col)]