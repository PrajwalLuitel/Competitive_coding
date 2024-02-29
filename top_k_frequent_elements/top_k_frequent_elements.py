"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    my_counts:dict[int:int] = {}
    for number in nums:
        if number in my_counts:
            my_counts[number] = my_counts[number] + 1
        else:
            my_counts[number] = 1
    
    sorted_counts = dict(sorted(my_counts.items(), key=lambda x: x[1], reverse=True))
    
    most_frequent:list[int] = []
    for element in sorted_counts.keys():
        if k>0:
            most_frequent.append(element)
            k-=1
        else:
            break
    
    return most_frequent

print(topKFrequent([4,1,-1,2,-1,2,3],2))
# print(topKFrequent([1],1))


    