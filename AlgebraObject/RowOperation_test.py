from Matrix import Matrix
from RowOperation import RowAdd, RowSwap

if __name__ == "__main__":
    A:Matrix = Matrix(3,3)
    A.matrix = [
        [1,1,1]
       ,[1,1,1]
       ,[1,1,1]]
    
    # (RowAdd(0,1,2).to_matrix(3)*A).print()

    B:Matrix = Matrix(5,5)
    # fill B with 1
    for i in range(B.num_of_row):
        for j in range(B.num_of_col):
            B.set_value(i,j,1)

    #create a deep copy of B
    C:Matrix = B.copy()
    RowAdd(0,1,2).apply(B).print()
    print("inverse :")
    RowAdd(0,1,2).inverse().apply(B).print()
    # print("C:")
    # (RowAdd(0,1,2).to_matrix(5)*C).print()

    # print("row swap test:")
    # RowSwap(0,1).apply(B).print()
    # print("C:")
    # C = RowAdd(0,1,2).to_matrix(5)*C
    # (RowSwap(0,1).to_matrix(5)*C).print()
    
