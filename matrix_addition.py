#defining function with 2 inputs
def matrix_addition(matrixX, matrixY):
#iterating through row and col
    for x in range(len(matrixX)):
       for y in range(len(matrixX[0])):
#adding up the 2 matrices
           matrixX[x][y]= matrixX[x][y] + matrixY[x][y]
  #returning output
    return(matrixX)
