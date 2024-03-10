"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""



def longestConsecutive( nums: list[int]) -> int:
    sorted_elements:list[int] = sorted(list(set(nums)))
    longest:int = 1
    length:int = 1

    for i in range(len(sorted_elements)-1):
        if sorted_elements[i] +1 == sorted_elements[i+1]:
            length += 1
        
        if i == len(sorted_elements)-2 or sorted_elements[i]+1 != sorted_elements[i+1]:
            if length > longest:
                longest = length
            length = 1

    return longest
    


def longestConsecutiveWithoutSorting(nums:list[int]) -> int:  # Function to find longest consecutive
   set_nums:set[int] = set(nums)  # Convert list to set for O(1) lookups
   longest:int = 0

   for num in set_nums:  # Iterate through set elements
       length:int = 0
       if num-1 not in set_nums:  # If not a starting number
           while num+length in set_nums:  # While next number is in set
               length += 1  # Increment length
           longest = max(longest, length)  # Update longest

   return longest  # Return longest consecutive sequence




print(longestConsecutive([0,3,7,2,5,8,4,6,0,100,101,102,32,48,60,61,62,1,103,104,105,106,107,108,109,110,111,112,114]))
print(longestConsecutiveWithoutSorting([0,3,7,2,5,8,4,6,0,100,101,102,32,48,60,61,62,1,103,104,105,106,107,108,109,110,111,112,114]))