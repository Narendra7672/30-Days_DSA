# Search a 2D Matrix II:
def Search2DMatrix(matrix,target):
    for row in matrix:
        for col in row:
            if target == col:
                return True
    return False 
matrix = [[1,2,3,4],[2,3,4,5],[5,6,7,8]]
target = 6 
res = Search2DMatrix(matrix,target)
print(res) 
      
def Search2DMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        current = matrix[row][col]

        if current == target:
            return True
        elif current > target:
            col -= 1
        else:
            row += 1
    return False
matrix = [[1, 2, 3, 4],[2, 3, 4, 5],[5, 6, 7, 8]]
print(Search2DMatrix(matrix, 6))  # True
print(Search2DMatrix(matrix, 9))  # False