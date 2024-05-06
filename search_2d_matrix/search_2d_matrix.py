"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

#  trying a solution by creating a flat list
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    flat_matrix:list[int] = []

    for row in matrix:
        for el in row:
            flat_matrix.append(el)
    
    left:int = 0
    right:int = len(flat_matrix)-1

    while left <= right:
        mid:int = (right+left)//2
        if flat_matrix[mid] > target:
            right = mid -1
        elif flat_matrix[mid] < target:
            left = mid +1
        else:
            return True
    return False


# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


def optimizedSearchMatrix(matrix: list[list[int]], target: int) -> bool:
    
    left_row:int = 0
    right_row:int = len(matrix)
    mid_row:int = (left_row+right_row)//2

    left:int = 0
    right:int = len(matrix[0])

    while left_row <= right_row and left <= right:
        mid:int = (left+right)//2
        if matrix[mid_row][mid] > target:
            if target < matrix[mid_row][0]:
                if mid_row == 0 or (target > matrix[mid_row-1][-1]): return False
                mid_row -= 1
            else:
                right = mid -1
        elif matrix[mid_row][mid] < target:
            if target > matrix[mid_row][-1]:
                if mid_row == len(matrix)-1 or (target < matrix[mid_row+1][0]): return False
                mid_row += 1
            else:
                left = mid + 1
        else:
            return True
    
    return False

# print(optimizedSearchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
# print(optimizedSearchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(optimizedSearchMatrix(matrix=[[1],[3]], target=2))


def furtherOptimizedSearchMatrix(matrix:list[list[int]], target:int) -> bool:
    rows:int = len(matrix)
    cols:int = len(matrix[0])
    left:int = 0
    right:int = rows*cols -1

    while left <= right:
        mid:int = left + (right - left) // 2
        row, col = divmod(mid, cols)
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(optimizedSearchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(optimizedSearchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(optimizedSearchMatrix(matrix=[[1],[3]], target=2))