import unittest
from AlgebraObject.Matrix import Matrix
from AlgebraObject.Vector import Vector
from Lab2 import TriangUp, TriangDown

# Unit test for TriangUp and TriangDown
class TestTriangUpAndDown(unittest.TestCase):
    def test_TriangUp(self):
        A:Matrix = Matrix(3,3)
        A.matrix = [
            [1,0,0]
            ,[1,1,0]
            ,[1,1,1]]
        b:Vector = Vector([1,2,3])
        self.assertEqual(TriangDown(A,b), Vector([1,1,1]))
    
    def test_TriangDown(self):
        A:Matrix = Matrix(3,3)
        A.matrix = [
            [1,0,0]
            ,[1,1,0]
            ,[1,1,1]]
        b:Vector = Vector([3,2,1])
        self.assertEqual(TriangUp(A.transpose(),b), Vector([1,1,1]))

if __name__ == "__main__":
    unittest.main()