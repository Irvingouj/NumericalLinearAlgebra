import time
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector
import NumericalLinearAlgebra.Lab3.Problem1 as p1
from NumericalLinearAlgebra.Lab3.Problem4 import CHOLfact,inverseCol
from typing import Callable, Tuple
import math

def f (x:float)->float:
    return math.pi**2*math.sin(math.pi*x)

alpha = 0
beta = 0

def poisson1D(n:int)-> Matrix :
    dimension = n-1
    A = Matrix(dimension,dimension)
    
    #fill up A diagnoal with 2
    [A.set_value(i,i,2) for i in range(dimension)]
    #fill up A off-diagonal with -1
    [A.set_value(i,i+1,-1) for i in range(dimension-1)]
    [A.set_value(i+1,i,-1) for i in range(dimension-1)]
    
    return A

def source(n:int,f:Callable,alpha:int,beta:int):
    dimension = n-1
    b = Vector.Zero_Vector(dimension)
    h = 1/n
    for i in range(dimension):
        b.set(i,h**2*f((i+1)*h))
    b.set(0,b.get(0) + alpha/h)
    b.set(dimension-1,b.get(dimension-1) + beta/h)
    return b




def solve_with_LU(n:int,f:Callable,alpha:int,beta:int) -> Tuple[Vector,float]:
    A = poisson1D(n)
    b = source(n,f,alpha,beta)
    
    lu_start_time = time.process_time()
    res = p1.solve_with_LU(A,b)
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

