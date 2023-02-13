from AlgebraObject.Matrix import Matrix
from AlgebraObject.RowOperation import RowAdd, RowSwap
from AlgebraObject.Vector import Vector
from NumericalLinearAlgebra.Lab2 import TriangDown, TriangUp

def LUDecomposition(A:Matrix):
    # assume A is a square matrix and diagonal elements are not zero
    n = A.num_of_row
    I = Matrix.Identity_Matrix(n)
    for i in range(n):
        a_i_i = A.matrix[i][i];
        for j in range(i+1,n):
            a_j_i = A.matrix[j][i]
            RowAdd(i,j,-a_j_i/a_i_i).apply(A)
            I.set_value(j,i,a_j_i/a_i_i)
    return I,A

def solve_with_LU(A:Matrix,b:Vector) -> Vector:
    L,U = LUDecomposition(A)
    y = TriangDown(L,b)
    x = TriangUp(U,y)
    return x