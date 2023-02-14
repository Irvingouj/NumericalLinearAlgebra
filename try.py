from AlgebraObject.Matrix import Matrix
from AlgebraObject.RowOperation import RowAdd, RowSwap
from Lab3.Problem3 import A,P,find_pivot
from Lab3.Problem1 import LUDecomposition

ori = A.copy()
operationMatrices = []
for i in range(4):
    pivot_index, pivot = find_pivot(A, i)
    r = RowSwap(i, pivot_index)
    r.apply(A)

    A.print("A before swap")
    r.to_matrix(4).print("p"+str(i))
    operationMatrices.append(r.to_matrix(4))

    A.print("A after swap")
    a_i_i = A.matrix[i][i];
    I = Matrix.Identity_Matrix(4)
    for j in range(i+1,4):
        a_j_i = A.matrix[j][i]
        RowAdd(i,j,-a_j_i/a_i_i).apply(A)
        I.set_value(j,i,-a_j_i/a_i_i)
    I.print("E"+str(i))
    
    
    operationMatrices.append(I)
    

    
for i in range(len(operationMatrices)):
    print(operationMatrices[i])
    print("------------------")

A.print("A")
# ori.print("ori")

I = Matrix.Identity_Matrix(4)
for m in operationMatrices:
    I = I* m.inverse()

I.print("I")
((P.inverse()*I)*A).print("P_-1*I*A")
(I*A).print("I*A")
# swapped =A.copy().operate(RowSwap(0,1)); 
# swapped.print("swapped")
# L,U = LUDecomposition(swapped)

# L.print("L")
# U.print("U")
# (L*U).print("L*U")
# ori.print("ori")