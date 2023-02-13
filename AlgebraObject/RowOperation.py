from abc import ABC, abstractmethod
from AlgebraObject.Matrix import Matrix

class RowOperation(ABC):

    @abstractmethod
    def apply(self, matrix) -> Matrix:
        pass

    @abstractmethod
    def to_matrix(self,size) -> Matrix:
        pass


class RowAdd(RowOperation):
    # add row one*scalar to row two
    def __init__(self, row1:int, row2:int, scalar:float) -> None:
        self.row1 = row1
        self.row2 = row2
        self.scalar = scalar

    def apply(self, matrix:Matrix) -> Matrix:
        matrix.matrix[self.row2] = [matrix.matrix[self.row2][i] + self.scalar * matrix.matrix[self.row1][i] for i in range(matrix.num_of_col)]
        return matrix
    
    def to_matrix(self,size:int) -> Matrix:
        matrix = Matrix.Identity_Matrix(size)
        matrix.set_value(self.row2,self.row1,self.scalar)
        return matrix
    
    def inverse(self):
        return RowAdd(self.row1,self.row2,-self.scalar)
    

class RowSwap(RowOperation):
    def __init__(self, row1:int, row2:int) -> None:
        self.row1 = row1
        self.row2 = row2

    def apply(self, matrix) -> Matrix:
        matrix.matrix[self.row1], matrix.matrix[self.row2] = matrix.matrix[self.row2], matrix.matrix[self.row1]
        return matrix

    def to_matrix(self,size) -> Matrix:
        res = Matrix.Identity_Matrix(size)
        res.matrix[self.row1], res.matrix[self.row2] = res.matrix[self.row2], res.matrix[self.row1]
        return res
    
    def inverse(self):
        return RowSwap(self.row2,self.row1)
    




    