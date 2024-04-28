"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


def search(nums: list[int], target: int) -> int:
    left:int = 0
    right:int = len(nums)-1
    mid:int = (right-left)//2

    while left <= mid <= right:

        if nums[mid] == target:
            return mid
        
        elif left+1 == right and nums[left] < target < nums[right]:
            return -1

        elif target > nums[mid]:
            left = mid
            mid = left + max(1,(right-left)//2)
        else:
            right = mid
            mid = right - max(1,(right-left)//2)

    return -1

print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(search(nums=[-1,0,3,5,9,12], target=2))
print(search(nums=[5], target=5))

# TODO : Optimization required