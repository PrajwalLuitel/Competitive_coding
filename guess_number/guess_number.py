"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""

pick = 6

def guess(n:int, pick:int =pick):
    if n>pick:
        return -1
    elif n < pick:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    nums:range = range(1,n+1)
    left:int = 0
    right:int = len(nums)-1

    while left <= right:
        mid:int = (right+left)//2
        if guess(nums[mid]) == -1:
            right = mid -1
        elif guess(nums[mid]) == 1:
            left = mid +1
        else:
            return nums[mid]


print(guessNumber(10))