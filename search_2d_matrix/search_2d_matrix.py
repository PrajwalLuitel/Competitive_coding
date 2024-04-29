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


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


# TODO : optimization required
def optimizedSearchMatrix(matrix: list[list[int]], target: int) -> bool:
    pass