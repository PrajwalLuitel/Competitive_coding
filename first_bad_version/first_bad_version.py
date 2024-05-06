"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
"""

bad = 4
def isBadVersion(n:int, bad:int =bad):
    if n == bad:
        return True
    return False


def firstBadVersion(n: int) -> int:
    versions:range = range(1,n+1)
    left:int = 0
    right:int = n-1
    while left <= right:
        mid:int = (right+left)//2
        if not isBadVersion(versions[mid]):
            left = mid +1
        elif isBadVersion(versions[mid]):
            if mid==0 or not isBadVersion(versions[mid-1]):
                return versions[mid]
            right = mid -1
        

print(firstBadVersion(5))