"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    my_stack:list[str] = []
    opening_closing:dict[str:str] = {"{":"}","(":")","[":"]"}
    for bracket in s:
        if bracket in opening_closing:
            my_stack.append(bracket)
        else:
            if (len(my_stack)==0 or opening_closing[my_stack[-1]] != bracket):
                return False
            my_stack.pop(-1)
    
    if len(my_stack) == 0:
        return True
    return False

print(isValid("}"))
            