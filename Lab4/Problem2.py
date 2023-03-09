

from typing import Tuple
from NumericalLinearAlgebra.AlgebraObject.Matrix import Matrix

class BandedMatrix():
    def __init__(self, p: int,q:int, n: int):
        # p = upper bandwidth
        # q = lower bandwidth
        self.p = p
        self.q = q
        self.n = n
        self.storage = [[0]*n for i in range(p + q + 1)]
        
    def _index_to_storage_index(self, i:int, j:int) -> Tuple[int, int]:
        return [j - i + self.p, i]
        
    def get_value(self, i:int, j:int) -> float:
        if j - i > self.p or i - j > self.q:
            return 0
        else:
            _i,_j  = self._index_to_storage_index(i,j);
            return self.storage[_i][_j]
        
    def set_value(self, i:int, j:int, value:float):
        if j - i > self.p or i - j > self.q:
            raise Exception("Index out of range")
        else:
            _i,_j  = self._index_to_storage_index(i,j);
            self.storage[_i][_j] = value
            
    def to_list(self) -> list:
        return self.storage.copy()
        
    
       
    @classmethod 
    def from_matrix(cls,A:Matrix):
        # Compute the upper and lower bandwidths of A
        p = max([j - i for i in range(A.num_of_row) for j in range(i, A.num_of_col) if A.get_value(i, j) != 0])
        q = max([i - j for i in range(A.num_of_row) for j in range(i, A.num_of_col) if A.get_value(i, j) != 0])
        n = A.num_of_col
        return cls(p, q, n)

def StoreBand(A: Matrix) -> Tuple[Matrix, int, int]:
    p_candidates = [];
    for i in range(A.num_of_row):
        for j in range(i, A.num_of_col):
            if A.get_value(i, j) != 0:
                p_candidates.append(j - i)
    p = max(p_candidates)
    
    q_candidates = [];
    for i in range(A.num_of_row):
        for j in range(0, i + 1):
            if A.get_value(i, j) != 0:
                q_candidates.append(i - j)
    q = max(q_candidates)
                
    
    n = A.num_of_col
    
    Aband = BandedMatrix(p, q, n)
    
    for i in range(n):
        for j in range(max(0, i - p), min(n, i + q + 1)):
            Aband.set_value(i,j,A.get_value(i, j));
    
    return Aband, p, q

def invBand(ABand: BandedMatrix, p: int, q: int) -> Matrix:
    A = Matrix(ABand.n, ABand.n)
    for i in range(ABand.n):
        for j in range(max(0, i - p), min(ABand.n, i + q + 1)):
            A.set_value(i, j, ABand.get_value(i, j))
    return A
            
def LUBand(A: Matrix, b: Matrix) -> Matrix:
    Aband, p, q = StoreBand(A)
    L = Matrix(A.num_of_row, A.num_of_col)
    U = Matrix(A.num_of_row, A.num_of_col)
    for i in range(A.num_of_row):
        for j in range(i, min(A.num_of_col, i + q + 1)):
            U.set_value(i, j, Aband.get_value(i, j))
        for j in range(max(0, i - p), i):
            L.set_value(i, j, Aband.get_value(i, j))
    
    return L, U
    