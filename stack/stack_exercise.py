"""1. Write a function in python that can reverse a string using stack data structure. 

reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW" 

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


def reverse_string(text):
    temp_stack = Stack()
    for char in text:
        temp_stack.push(char)
    
    reversed_result = ""
    for i in range(temp_stack.size()):
        reversed_result+= temp_stack.pop()
    return reversed_result


if __name__=="__main__":
    print(reverse_string("We will conquere COVID-19"))