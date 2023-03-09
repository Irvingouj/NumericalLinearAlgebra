import time
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector
import NumericalLinearAlgebra.Lab3.Problem1 as p1
from NumericalLinearAlgebra.Lab3.Problem4 import CHOLfact,inverseCol
from typing import Callable, Tuple
import math


f = lambda x: math.pi**2*math.sin(math.pi*x)
alpha = 0
beta = 0

def solve_triangle_down_band(A:Matrix,b:Vector,width:int)->Vector:
    n = A.num_of_row
    x = Vector.Zero_Vector(n)
    for i in range(n):
        x.set(i,b.get(i))
        for j in range(max(0,i-width),i):
            x.set(i,x.get(i) - A.get(i,j)*x.get(j))
        x.set(i,x.get(i)/A.get(i,i))
    return x

def solve_triangle_up_band(A:Matrix,b:Vector,width:int)->Vector:
    n = A.num_of_row
    x = Vector.Zero_Vector(n)
    for i in range(n-1,-1,-1):
        x.set(i,b.get(i))
        for j in range(i+1,min(n,i+width+1)):
            x.set(i,x.get(i) - A.get(i,j)*x.get(j))
        x.set(i,x.get(i)/A.get(i,i))
    return x

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
    L,U = p1.LUDecomposition(A)
    y = solve_triangle_down_band(L,b,1)
    x = solve_triangle_up_band(U,y,1)
    lu_end_time = time.process_time()
     
    return x,lu_end_time - lu_start_time;


def solve_with_Cholesky(n:int,f:Callable,alpha:int,beta:int):
    A = poisson1D(n)
    b = source(n,f,alpha,beta)
    
    chol_start_time = time.process_time()
    L, factorization_time = CHOLfact(A)
    y = solve_triangle_down_band(L,b,1)
    x = solve_triangle_up_band(L.transpose(),y,1)
    chol_end_time = time.process_time()
    
    return x,chol_end_time - chol_start_time + factorization_time;

def compare_time(n:int,f:Callable,alpha:int,beta:int):
    lu_res,lu_time = solve_with_LU(n,f,alpha,beta)
    chol_res,chol_time = solve_with_Cholesky(n,f,alpha,beta)
    print("LU time: ",lu_time)
    print("Cholesky time: ",chol_time)
    
    return lu_time,chol_time

