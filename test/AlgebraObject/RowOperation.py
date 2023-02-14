import unittest
from AlgebraObject.Matrix import Matrix
from AlgebraObject.RowOperation import RowAdd, RowSwap

class RowOpTest(unittest.TestCase):
    def test_RowAdd(self):
        A = Matrix.Random_Square_Matrix_Int(3)
        ori = A.copy()
        RowAdd(0,1,1).apply(A)
        
        self.assertEqual(A.matrix[1][0], ori.matrix[1][0] + ori.matrix[0][0])

    def test_RowAdd_matrx(self):
        A = Matrix.Random_Square_Matrix_Int(3)
        ori = A.copy()
        op = RowAdd(0,1,1);
        op.apply(A)
        self.assertEqual(op.to_matrix(3)*ori, A)

    def test_RowSwap(self):
        A = Matrix.Random_Square_Matrix_Int(3)
        ori = A.copy()
        RowSwap(0,1).apply(A)
        self.assertEqual(A.matrix[0][0], ori.matrix[1][0])
        self.assertEqual(A.matrix[1][0], ori.matrix[0][0])

    def test_RowSwap_matrix(self):
        A = Matrix.Random_Square_Matrix_Int(3)
        ori = A.copy()
        op = RowSwap(0,1)
        op.apply(A)
        self.assertEqual(op.to_matrix(3)*ori, A)

    def test_RowAdd_matrix_inverse(self):
        op = RowAdd(0,1,1)
        matrix = op.to_matrix(3)
        self.assertTrue(isinstance(matrix,RowAdd.RowAddMatrix))
        self.assertEqual(matrix.inverse()*matrix, Matrix.Identity_Matrix(3))

if __name__ == "__main__":
    unittest.main()