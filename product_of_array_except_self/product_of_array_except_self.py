"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)"""

def productExceptSelf(nums: list[int]) -> list[int]:
    answer:list[int] = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                answer[j] *= nums[i]
        
    return answer


def productExceptSelfAgain(nums:list[int]) -> list[int]:
    max_len:int = len(nums)
    long_list:list[int] = nums
    item_number:int = 0
    multiply:int = 1
    returning_array:list[int] = []

    for i in range(1,len(long_list)+1):
        if (i-1 != item_number):
            multiply *= long_list[i-1]
        if (i%max_len == 0):
            item_number += max_len+1
            returning_array.append(multiply)
            long_list.pop()
            multiply = 1  
        i=0  
    return returning_array



def productExceptSelfAgainAgain(nums:list[int]) -> list[int]:
    prefix:int = 1
    postfix:int = 1
    output_array:list[int] = [1]*(len(nums))
    output_array[0] = nums[0]

    for i in range(1,len(nums)):
        output_array[i] = prefix*nums[i-1]
        prefix *= nums[i-1]

    for j in range(len(nums)-1, -1, -1):
        output_array[j] = postfix*output_array[j]
        if j ==0:
            output_array[j] = postfix
        postfix *= nums[j]

    return output_array


print(productExceptSelfAgainAgain([4,3,2,1,2]))
# correct answer for [4,3,2,1,2] is [12,16,24,48,24]







# print(productExceptSelf([1,2,3,4]))
# output array: [24,12,8,6]