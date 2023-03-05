from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix
from NumericalLinearAlgebra.AlgebraObject.Vector import Vector

# solve Ax=b
def TriangUp(A:Matrix,b:Vector):
    if not A.is_upper_triangular():
        raise Exception("A is not upper triangular")
    n = A.num_of_row

    x = Vector([0 for i in range(n)])
    b_copy = b.copy()
    for i in range(n-1,-1,-1):
        b_copy.set(i, b_copy.get(i) - sum([A.get_value(i,j) * x.get(j) for j in range(i+1,n)]))
        x.set(i, b_copy.get(i) / A.get_value(i,i))
    
    return x


def TriangDown(A:Matrix,b:Vector):
    if not A.is_lower_triangular():
        raise Exception("A is not lower triangular")
    n = A.num_of_row

    x = Vector.Zero_Vector(n)
    b_copy = b.copy()
    for i in range(n):
        b_copy.set(i, b_copy.get(i) - sum([A.get_value(i,j) * x.get(j) for j in range(i)]))
        x.set(i, b_copy.get(i) / A.get_value(i,i))
    return x

if __name__ == "__main__":
    A:Matrix = Matrix(3,3)
    A.matrix = [
        [1,0,0]
       ,[1,1,0]
       ,[1,1,1]]
    b:Vector = Vector([1,2,3])
    print("A:")
    A.print()
    print("b:")
    b.print()
    print("TriangDown:")
    TriangDown(A,b).print()
