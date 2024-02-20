"""Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""

def palindrome(s:str) -> bool:
    if s == s[::-1]: 
        return True
    return False

def longestPalindrome(s: str) -> str:
    max_length:int = 0
    result:str = ""
    check_str:str = ""
    
    if len(s) == 1:
        return s

    for i in range(len(s)):
        for j in range(i,len(s)):
            check_str = s[i:j+1]
            if palindrome(check_str) and len(check_str) > max_length:
                max_length = len(check_str)
                result = check_str
    return result

print(longestPalindrome("axemadamzyrp"))


