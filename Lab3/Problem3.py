from AlgebraObject.Matrix import Matrix
from AlgebraObject.Vector import Vector
from Lab3.Problem1 import LUDecomposition
from Lab2 import TriangDown, TriangUp
from AlgebraObject.RowOperation import RowAdd, RowSwap
import numpy as np

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



def find_pivot(A:Matrix, j:int):
    # find the row index of the pivot
    max = float('-inf')
    max_index = -1
    for i in range(j, A.num_of_row):
        if A.get_value(i,j) > max:
            max = abs(A.get_value(i,j))
            max_index = i
    return max_index, max


# Question 3
def LUPDecomposition(A:Matrix):
    A = A.copy()
    n = A.num_of_row
    matrices = []
    for i in range(n-1):
        pivot_index, _ = find_pivot(A, i)
        r = RowSwap(i, pivot_index)
        r.apply(A)
        matrices.append(r.to_matrix(n).add_name("P_{}".format(i+1)))
        a_i_i = A.matrix[i][i];
        I = RowAdd.RowAddMatrix.Identity_Matrix(n)
        for j in range(i+1,n):
            a_j_i = A.matrix[j][i]
            RowAdd(i,j,-a_j_i/a_i_i).apply(A)
            I.set_value(j,i,-a_j_i/a_i_i)
        matrices.append(I.add_name("E_{}".format(i+1)))

    L = Matrix.Identity_Matrix(n)
    P = Matrix.Identity_Matrix(n)
    
    #from the end to the beginning 
    for i in range(len(matrices)-1,-1,-1):
        L = matrices[i].inverse()*L
        
    for m in matrices:
        if isinstance(m,RowSwap.RowSwapMatrix):
            P = m*P
    return L,A,P

# Question 4
def solve_with_LUP(A:Matrix,b:Vector) -> Vector:
    L,U,P = LUPDecomposition(A.copy())
    PA = P*A
    Pb = P*b
    PL = P*L # lower triangular matrix
    
    # PAx = Pb
    # Ax = P^-1 Pb
    # Ax = b
    # PLUx = b 
    # y = Ux
    # PLy = b
    y = TriangDown(PL,b)
    x = TriangUp(U,y)
    
    return x
    
    
    
    
    
    
