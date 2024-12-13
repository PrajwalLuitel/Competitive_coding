"""
Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". 

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""


from collections import deque

class Stack:

    def __init__(self):
        self.collection = deque()

    def push(self, value):
        self.collection.append(value)

    def pop(self):
        return self.collection.pop()
    
    def peek(self):
        return self.collection[-1]
    
    def is_empty(self):
        return len(self.collection) ==0
    
    def size(self):
        return len(self.collection)
    


def is_balanced(sequence):
    s = Stack()
    parantheses = {")":"(","}":"{","]":"["}

    for char in sequence:
        if char in parantheses.values():
            s.push(char)
        elif char in parantheses.keys():
            if not s.is_empty() and s.peek() == parantheses[char]:
                s.pop()
            else:
                return False

    return s.is_empty()


if __name__=="__main__":
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("(a{b+c)}"))
    print(is_balanced("(a{b+c}"))