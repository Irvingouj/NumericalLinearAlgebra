from AlgebraObject.Matrix import Matrix
from Lab3.Problem1 import LUDecomposition
from AlgebraObject.RowOperation import RowSwap

A = Matrix.from_list([[2, 4, -3, 1],
                       [3, 6, 1, -2], 
                       [-1, 1, 2, 3],
                       [1, 1, 4, 1]])
P = Matrix.from_list([[0, 1, 0, 0], 
                      [0, 0, 1, 0], 
                      [1, 0, 0, 0], 
                      [0, 0, 0, 1]])


def Question1():
    LUDecomposition(A.copy())


def Question2():
    A_copy = A.copy()
    L, U = LUDecomposition(P.copy() * A_copy)
    return L, U
