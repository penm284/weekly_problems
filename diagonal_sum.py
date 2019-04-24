#Create an algorithm below which finds the diagonal sum of a matrix. Make sure to run the program with each matrix to fulfill the proper test cases.
matrix1 = [[0 + x for x in range(5)] for y in range(5)]
matrix2 =[[0 + x for x in range(10)] for y in range(10)]
matrix3 =[[0 + x for x in range(8)] for y in range(8)]
matrix4 =[[0 + x for x in range(9)] for y in range(9)]
matrix5 =[[0 + x for x in range(3)] for y in range(3)]
matrix6 =[[0 + x for x in range(50)] for y in range(50)]
matrix7 =[[0 + x for x in range(100)] for y in range(100)]
matrix8 =[[0 + x for x in range(800)] for y in range(800)]

def diagonal_matrix(matrix1):












Solution:
matrix1 = [[0 + x for x in range(5)] for y in range(5)]
matrix2 =[[0 + x for x in range(10)] for y in range(10)]
matrix3 =[[0 + x for x in range(8)] for y in range(8)]
matrix4 =[[0 + x for x in range(9)] for y in range(9)]
matrix5 =[[0 + x for x in range(3)] for y in range(3)]
matrix6 =[[0 + x for x in range(50)] for y in range(50)]
matrix7 =[[0 + x for x in range(100)] for y in range(100)]
matrix8 =[[0 + x for x in range(800)] for y in range(800)]

def diagonal_sum(matrix8):
    total = 0
    for row in range(len(matrix8)):
        total += matrix8[row][row]
    return total
print(matrix8)
print(diagonal_sum(matrix8))
