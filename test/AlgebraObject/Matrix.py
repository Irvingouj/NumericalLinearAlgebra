import unittest
from AlgebraObject.Matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_is_upper_triangular(self):
        # Test a 3x3 upper triangular matrix
        matrix = Matrix(3, 3)
        matrix.matrix = [[1, 2, 3], 
                         [0, 4, 5], 
                         [0, 0, 6]]
        self.assertTrue(matrix.is_upper_triangular())

        # Test a 3x3 non-upper triangular matrix
        matrix = Matrix(3, 3)
        matrix.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(matrix.is_upper_triangular())

if __name__ == '__main__':
    unittest.main()
