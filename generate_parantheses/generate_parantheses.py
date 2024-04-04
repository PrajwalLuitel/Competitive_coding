"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

def generateParantheses(n:int) -> list[str]:
    my_stack:list[str] = []
    opening_closing:list[str] = []
    open:int = 0
    close:int = 0

    def backtracking(open, close):
        if open == close == n:
            opening_closing.append("".join(my_stack))

        if open < n:
            my_stack.append("(")
            backtracking(open+1, close)
            my_stack.pop()

        if open > close:
            my_stack.append(")")
            backtracking(open, close+1)
            my_stack.pop()
        
        
    
    backtracking(open,close)

    return opening_closing

print(generateParantheses(3))