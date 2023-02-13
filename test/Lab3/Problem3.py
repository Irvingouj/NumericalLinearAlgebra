# test for problem 3
import unittest
from AlgebraObject.Matrix import Matrix
from Lab3.Problem3 import Question1,Question2,A,P
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
        

if __name__ == '__main__':
    unittest.main()