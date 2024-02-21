"""Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1"""

def palindrome(x:int):
    y:int = x
    numbers:list[int] = []

    if y <0:
        return False

    while y >0:
        numbers.append(y%10)
        y = y //10
    
    reversed:int = 0
    power:int = 0
    for i in numbers[::-1]:
        reversed += i*(10**power)
        power += 1
    
    if reversed == x:
        return True
    
    return False

print(palindrome(1331))