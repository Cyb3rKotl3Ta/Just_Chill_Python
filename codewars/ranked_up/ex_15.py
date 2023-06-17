import numpy as np

def determinant(matrix):
    return round(np.linalg.det(matrix))

def determinant2(matrix):
    #your code here
    result = 0
    l = len(matrix)

    #base case when length of matrix is 1
    if l == 1:
        return matrix[0][0]

    #base case when length of matrix is 2
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #for length of matrix > 2
    for j in range(0, l):
        # create a sub matrix to find the determinant
        if l!=2:
            sub_matrix = []               
            sub_matrix = [(row[0:j]+row[j+1:]) for row in matrix[1:]]
        result = result + (-1)**j * matrix[0][j] * determinant(sub_matrix)
    return result

def determinant3(m):
    ans,sizeM = 0, len(m)
    if sizeM == 1: return m[0][0]
    for n in range(sizeM):
        ans+= (-1)**n * m[0][n] * determinant([ m[i][:n]+m[i][n+1:] for i in range(1,sizeM) ])
    return ans



matrix_a = [[1, 2], [3, 4]]

print(determinant2(matrix_a))

