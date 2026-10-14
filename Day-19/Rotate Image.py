# Rotate Image:
def RotateImage(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for row in matrix:
        row.reverse()
    return matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res =RotateImage(matrix)
print(res)