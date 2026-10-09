# Search a 2D Matrix:
def searchMatrix(matrix,target):
        if not matrix or not matrix[0]:
            return False
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = (ROWS * COLS) - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // COLS
            col = mid % COLS
            
            current_val = matrix[row][col]
            if current_val == target:
                return True
            elif current_val < target:
                left = mid + 1  
            else:
                right = mid - 1               
        return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
res = searchMatrix(matrix,target)
print(res)
# Output: True
