from AlgebraObject.Matrix import Matrix
from AlgebraObject.RowOperation import RowAdd, RowSwap
from Lab3.Problem3 import A,P,find_pivot,LUPDecomposition
from Lab3.Problem1 import LUDecomposition

A_copy = A.copy()
P_copy = P.copy()


L,U = LUDecomposition(P_copy*A_copy)

L.print("L")
U.print("U")
(L*U).print("L*U")
(P*A).print("P*A")

print("------------------")

L,U,P_test = LUPDecomposition(A.copy())

L.print("L")
(P_test*L).print("P*L")
U.print("U")

