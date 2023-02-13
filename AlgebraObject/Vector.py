from AlgebraObject.Matrix import Matrix
import random
class Vector(Matrix):
    def __init__(self, arr:list) -> None:
        super().__init__(len(arr),1)
        self.matrix = [[i] for i in arr]

    def get(self,index:int):
        return self.matrix[index][0]
    
    def set(self,index:int,value):
        self.matrix[index][0] = value

    def copy(self):
        return Vector([self.get(i) for i in range(len(self.matrix))])

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)
    @classmethod
    def Zero_Vector(cls, size:int):
        return cls([0 for i in range(size)])
    @classmethod
    def Random_Vector_Int(cls, size:int):
        return cls([random.randint(-10,10) for i in range(size)])
    
