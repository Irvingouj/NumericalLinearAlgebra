from AlgebraObject.Matrix import Matrix
from Lab3.Problem1 import LUDecomposition
from AlgebraObject.RowOperation import RowAdd, RowSwap

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
    [A.get_value(i,j) for i in range(j, A.num_of_row)]
    max = float('-inf')
    max_index = -1
    for i in range(j, A.num_of_row):
        if abs(A.get_value(i,j)) > max:
            max = abs(A.get_value(i,j))
            max_index = i
    return max_index, max


def LUPDecomposition(A:Matrix):
    A = A.copy()
    n = A.num_of_row
    matrices = []
    for i in range(n):
        pivot_index, _ = find_pivot(A, i)
        r = RowSwap(i, pivot_index)
        r.apply(A)
        matrices.append(r.to_matrix(n))
        a_i_i = A.matrix[i][i];
        I = RowAdd.RowAddMatrix.Identity_Matrix(n)
        for j in range(i+1,n):
            a_j_i = A.matrix[j][i]
            RowAdd(i,j,-a_j_i/a_i_i).apply(A)
            I.set_value(j,i,-a_j_i/a_i_i)
        matrices.append(I)

    I = Matrix.Identity_Matrix(n)
    P = Matrix.Identity_Matrix(n)
    for m in matrices:
        if isinstance(m, RowSwap.RowSwapMatrix):
            P = m*P
        I = m.inverse()*I
    return I,A,P

def Question4():
    L,U,P = LUPDecomposition(A.copy())
    print(L)
    print(U)
    print(P)
    print(P*A)
    print(L*U)
    print(P*A == L*U)
    
