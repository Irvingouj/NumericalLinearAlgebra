from AlgebraObject.Matrix import Matrix
from AlgebraObject.Vector import Vector
from Lab3.Problem1 import LUDecomposition
import matplotlib.pyplot as plt
import time

def LUDecompositionEvaluateTime(A):
    start = time.process_time()
    L,U = LUDecomposition(A)
    end = time.process_time()

    return L,U,end-start

def LUDecompositionEvaluateTimeDifferentSize():
    sizes = []
    times = []
    for i in range(10,300):
        A = Matrix.Random_Square_Matrix_Int(i)
        L,U,time = LUDecompositionEvaluateTime(A)
        sizes.append(i)
        times.append(time)
        print("Size: ",i," Time: ",time)
    plt.plot(sizes, times)
    plt.xlabel('Sizes')
    plt.ylabel('Times')
    plt.title('Graph of Sizes vs Times')
    plt.show()

    


    