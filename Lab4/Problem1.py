import time
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector
from NumericalLinearAlgebra.Lab3.Problem1 import solve_with_LU
from NumericalLinearAlgebra.Lab3.Problem4 import CHOLfact,inverseCol
from typing import Callable
import math

def f (x:float)->float:
    return math.pi**2*math.sin(math.pi*x)

alpha = 0
beta = 0

def poisson1D(n:int)-> Matrix :
    dimension = n-1
    A = Matrix(dimension,dimension)
    
    #fill up A diagnoal with 2
    [A[i][i].set_value(2) for i in range(dimension)]
    #fill up A off-diagonal with -1
    [A[i][i+1].set_value(-1) for i in range(dimension-1)]
    [A[i+1][i].set_value(-1) for i in range(dimension-1)]
    
    return A

def source(n:int,f:Callable,alpha:int,beta:int):
    dimension = n-1
    b = Vector(dimension)
    h = 1/n
    for i in range(dimension):
        b[i].set_value(h**2*f((i+1)*h))
    b[0].set_value(b[0].get_value() + alpha/h)
    b[dimension-1].set_value(b[dimension-1].get_value() + beta/h)
    return b




def solve_with_LU(n:int,f:Callable,alpha:int,beta:int):
    A = poisson1D(n)
    b = source(n,f,alpha,beta)
    
    lu_start_time = time.process_time()
    res = solve_with_LU(A,b)
    lu_end_time = time.process_time()
     
    return res,lu_end_time - lu_start_time;


def solve_with_Cholesky(n:int,f:Callable,alpha:int,beta:int):
    A = poisson1D(n)
    b = source(n,f,alpha,beta)
    
    chol_start_time = time.process_time()
    L, factorization_time = CHOLfact(A)
    res = inverseCol(L,b)
    chol_end_time = time.process_time()
    
    return res,chol_end_time - chol_start_time + factorization_time;

