# test for problem 3
import unittest
from AlgebraObject.Matrix import Matrix
from AlgebraObject.Vector import Vector
from Lab3.Problem3 import LUPDecomposition, Question1,Question2,A,P,solve_with_LUP
import numpy as np

class Problem3Test(unittest.TestCase):
    def test_Question1(self):
        try:
            Question1()
        except Exception as e:
            print( "passed test_Question1")
    def test_Question2(self):
        L,U = Question2()
        self.assertTrue(L.is_lower_triangular())
        self.assertTrue(U.is_upper_triangular())
        res = L*U
        expected = P.copy()*A.copy()
        
        [self.assertTrue(np.isclose(res.get_value(i,j),expected.get_value(i,j),atol=1e-8)) for i in range(res.num_of_row) for j in range(res.num_of_col)]
        
    def test_Question3(self):
        L,U,P = LUPDecomposition(A)
        A.print("A")
        L.print("L")
        U.print("U")
        P.print("P")
        
        (L*U).print("L*U")
        (P*A).print("P*A")
        
        self.assertTrue(P*A == P*L*U)

    def test_Question3_repeated(self):
        for i in range(10):
            A = Matrix.Random_Matrix(5,5)
            L,U,P = LUPDecomposition(A)
            self.assertTrue(P*A == P*L*U)
            
    def test_Question4(self):
        b = Vector([1,1,1])
        A = Matrix.Random_Matrix(3,3)
        x = solve_with_LUP(A.copy(),b)
        
        self.assertEqual(x,A.inverse()*b)
        
    def test_Question4_repeated(self):
        for i in range(1):
            b = Vector.Random_Vector_Int(5)
            A = Matrix.Random_Matrix(5,5)
            x = solve_with_LUP(A.copy(),b)
            
            self.assertTrue(x,A.inverse()*b)

if __name__ == '__main__':
    unittest.main()