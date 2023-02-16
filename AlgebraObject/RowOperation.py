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

    class RowAddMatrix(Matrix):
        def inverse(self):
            return Matrix.Identity_Matrix(self.num_of_row)*2 - self
        
        def __init__(self, n ,op : 'RowAdd') -> None:
            super().__init__(n,n)
            self.matrix = Matrix.Identity_Matrix(n).matrix
            self.matrix[op.row2][op.row1] = op.scalar
        
        @classmethod
        def Identity_Matrix(cls, size: int):
            res = cls(size,RowAdd(0,0,0))
            for i in range(size):
                res.matrix[i][i] = 1
            return res
    # add row one*scalar to row two
    def __init__(self, row1:int, row2:int, scalar:float) -> None:
        self.row1 = row1
        self.row2 = row2
        self.scalar = scalar

    def apply(self, matrix:Matrix) -> Matrix:
        matrix.matrix[self.row2] = [matrix.matrix[self.row2][i] + self.scalar * matrix.matrix[self.row1][i] for i in range(matrix.num_of_col)]
        return matrix
    
    def to_matrix(self,size:int) -> Matrix:
        return RowAdd.RowAddMatrix(size,self)
    
    def inverse(self):
        return RowAdd(self.row1,self.row2,-self.scalar)
    

class RowSwap(RowOperation):
    
    class RowSwapMatrix(Matrix):
        def inverse(self):
            return self.transpose()
        def __init__(self, n, operation:'RowSwap') -> None:
            super().__init__(n,n)
            self.matrix = Matrix.Identity_Matrix(n).matrix
            self.matrix[operation.row1], self.matrix[operation.row2] = self.matrix[operation.row2], self.matrix[operation.row1] 
        
    def __init__(self, row1:int, row2:int) -> None:
        self.row1 = row1
        self.row2 = row2

    def apply(self, matrix) -> Matrix:
        matrix.matrix[self.row1], matrix.matrix[self.row2] = matrix.matrix[self.row2], matrix.matrix[self.row1]
        return matrix

    def to_matrix(self,size) -> RowSwapMatrix:
        return RowSwap.RowSwapMatrix(size,self)
    
    def inverse(self):
        return RowSwap(self.row2,self.row1)
    





    
