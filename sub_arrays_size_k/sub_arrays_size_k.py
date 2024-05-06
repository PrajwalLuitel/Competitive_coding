"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
"""



def numOfSubarrays(arr:list[int], k:int, threshold:int) -> int:
    left:int = 0
    right:int = left+k
    count:int = 0

    while right <= len(arr):
        if sum(set(arr[left:right]))/k >= threshold:
            count += 1
        left += 1
        right += 1 
    return count



def optimizednumOfSubarrays( arr: list[int], k: int, threshold: int) -> int:
    window:list[int] = arr[:k]
    total:int = sum(window)
    count:int = 0
    
    if total >= threshold*k:
        count += 1
    
    for num in arr[k:]:
        total -= (window.pop(0) - num)
        window.append(num)
        if total >= threshold*k:
            count += 1

    return count

# print(optimizednumOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
# print(optimizednumOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
print(optimizednumOfSubarrays([7,7,7,7,7,7,7], 7,7))

def furtheroptimizednumOfSubarrays( arr: list[int], k: int, threshold: int) -> int:
    res = 0
    runSum = sum(arr[:k-1])
    
    l = 0

    for r in range(k-1, len(arr)):
        runSum += arr[r]
        if runSum//k >= threshold:
            res += 1
        runSum -= arr[l]
        l+=1
    
    return res

# print(optimizednumOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
# print(optimizednumOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
print(optimizednumOfSubarrays([7,7,7,7,7,7,7], 7,7))