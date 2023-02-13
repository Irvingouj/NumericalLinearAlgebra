from Matrix import Matrix


A = Matrix(3,3)
A.matrix = [
    [1,2,3]
    ,[4,5,6]
    ,[7,8,10]]

B = Matrix(3,4)
B.matrix = [
    [1,2,3,4]
    ,[4,5,6,0]
    ,[7,8,10,1]]

print((A*B).print())
