
import random
from typing import List
from termcolor import colored
import numpy as np

class Matrix:
    def __init__(self, num_of_row:int,num_of_col:int) -> None:
        self.num_of_row = num_of_row
        self.num_of_col = num_of_col
        self.matrix:List[List[float]] = [[0 for i in range(num_of_col)] for j in range(num_of_row)]

    def __str__(self) -> str:
        res = ""
        for i in range(self.num_of_row):
            res += str(self.matrix[i]) + "\n"
        return res

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Matrix):
            if self.num_of_row == __o.num_of_row and self.num_of_col == __o.num_of_col:
                for i in range(self.num_of_row):
                    for j in range(self.num_of_col):
                        if self.matrix[i][j] != __o.matrix[i][j]:
                            return False
                return True
            else:
                return False
        else:
            return False

    def print(self,name:str = ""):
        print(name+":")
        for i in range(self.num_of_row):
            print([round(ele,3) for ele in self.matrix[i]])
    
    def set_value(self, row:int, col:int, value:float):
        self.matrix[row][col] = value

    def get_value(self, row:int, col:int) -> float:
        return self.matrix[row][col]

    def __mul__(self, other):
        if self.num_of_col == other.num_of_row:
            res = Matrix(self.num_of_row, other.num_of_col)
            for i in range(self.num_of_row):
                for j in range(other.num_of_col):
                    res.matrix[i][j] = sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.num_of_col)])
            return res
        else:
            raise Exception("Dimension Error")
        
    def copy(self):
        res = Matrix(self.num_of_row, self.num_of_col)
        for i in range(self.num_of_row):
            for j in range(self.num_of_col):
                res.matrix[i][j] = self.matrix[i][j]
        return res
    
    def operate(self, operation):
        return operation.apply(self)
    
    def transpose(self):
        res = Matrix(self.num_of_col, self.num_of_row)
        for i in range(self.num_of_row):
            for j in range(self.num_of_col):
                res.matrix[j][i] = self.matrix[i][j]
        return res
    
    def is_square(self):
        return self.num_of_row == self.num_of_col
    
    def is_upper_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.num_of_row):
            for j in range(self.num_of_col):
                if i > j and not np.isclose(self.matrix[i][j],0,atol=1e-8) :
                    return False
        return True
    
    def is_lower_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.num_of_row):
            for j in range(i+1, self.num_of_col):
                if not np.isclose(self.matrix[i][j],0,atol=1e-8):
                    return False
        return True

    
    def __add__(self,other):
        if self.num_of_row == other.num_of_row and self.num_of_col == other.num_of_col:
            res = Matrix(self.num_of_row, self.num_of_col)
            for i in range(self.num_of_row):
                for j in range(self.num_of_col):
                    res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return res
        else:
            raise Exception("Dimension Error")
    @classmethod
    def Identity_Matrix(cls, size:int):
        res = cls(size,size)
        for i in range(size):
            res.matrix[i][i] = 1
        return res

    @classmethod
    def Random_Matrix(cls, num_of_row:int, num_of_col:int):
        res = cls(num_of_row,num_of_col)
        for i in range(num_of_row):
            for j in range(num_of_col):
                res.matrix[i][j] = random.uniform(-10, 10)
        return res
    
    @classmethod
    def Random_Square_Matrix_Int(cls, size:int) -> "Matrix":
        res = cls(size,size)
        for i in range(size):
            for j in range(size):
                res.matrix[i][j] = random.randint(-10, 10)
                if i == j:
                    res.matrix[i][j] += 120 # diagonal dominant
        return res
        
    @classmethod
    def Zero_Matrix(cls, num_of_row:int, num_of_col:int) -> "Matrix":
        res = cls(num_of_row,num_of_col)
        return res

    @classmethod
    def from_list(cls, lst:List[List[float]]) -> "Matrix":
        res = cls(len(lst),len(lst[0]))
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                res.matrix[i][j] = lst[i][j]
        return res
    