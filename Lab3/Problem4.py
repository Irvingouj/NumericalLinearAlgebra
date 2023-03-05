import time
from typing import Tuple

import numpy as np
from AlgebraObject.Vector import Vector
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from Lab2 import TriangDown, TriangUp

def CHOLfact(A:Matrix)-> Tuple[Matrix,int]:
    # A is a symmetric positive definite matrix
    if not A.is_square():
        raise ValueError("Matrix is not square")
    if not A.is_symmetric():
        raise ValueError("Matrix is not symmetric")
    if not A.is_positive_definite():
        raise ValueError("Matrix is not positive definite")
    
    n = A.num_of_row
    L = Matrix(n,n)
    start_time = time.process_time()
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = np.sqrt(A[i][i] - s)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - s))
    end_time = time.process_time()
    return L, end_time - start_time

def inverseCol(L:Matrix,b:Vector)->Vector:
    # L is a lower triangular matrix
    if not L.is_lower_triangular():
        raise ValueError("Matrix is not lower triangular")
    
    y = TriangDown(L,b)
    
    return TriangUp(L.transpose(),y)
