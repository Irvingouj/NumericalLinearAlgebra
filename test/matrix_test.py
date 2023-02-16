import unittest
from AlgebraObject.Matrix import Matrix

class MatrixTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

    def test_matrix_plus(self):
        A = Matrix(3,3)
        A.matrix = [
            [1,2,3]
            ,[4,5,6]
            ,[7,8,10]]
        B = Matrix(3,3)
        B.matrix = [
            [1,2,3]
            ,[4,5,6]
            ,[7,8,10]]
        C = A+B
        print(C.matrix)
        self.assertEqual(C.matrix,[[2,4,6],[8,10,12],[14,16,20]])

if __name__ == "__main__":
    unittest.main()