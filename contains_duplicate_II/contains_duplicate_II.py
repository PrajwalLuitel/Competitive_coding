"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    i:int = 0
    if k > len(nums): 
        k = len(nums)
    elif k ==0:
        return False
    while i <= len(nums)-k:
        j = i+k
        if sorted(list(set(nums[i:j+1]))) != sorted(nums[i:j+1]):
            return True
        i += 1
    return False

# print(containsNearbyDuplicate([1,0,1,1],1))
# print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
# print(containsNearbyDuplicate([99,99],2))
# print(containsNearbyDuplicate([2,2],3))
# print(containsNearbyDuplicate([4,1,2,3,1,5],3))


def optimizedContainsNearbyDuplicate(nums:list[int], k:int) -> bool:
    window:list[int] = []
    a:int = k if k < len(nums) else len(nums)-1
    
    for i in range(a+1):
        if nums[i] in window:
            return True
        window.append(nums[i])

    for num in nums[k+1:]:
        window.pop(0)
        if num in window:
            return True
        window.append(num)
    
    return False

# print(containsNearbyDuplicate([4,1,2,3,1,5],3))
# print(optimizedContainsNearbyDuplicate([1,2,3,1,2,3],2))
print(optimizedContainsNearbyDuplicate([1],1))


def furtherOptimized(nums:list[int], k:int) -> bool:
    dic = {}
    for i, n in enumerate(nums):
        if n in dic and i - dic[n]<= k:  
            return True
        dic[n] = i
    return False


print(furtherOptimized([1],1))
