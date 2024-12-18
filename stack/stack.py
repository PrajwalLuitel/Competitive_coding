from collections import deque
# Using deque instead of a list as list is dynamic array but deque is an implementation of double linked list, so more efficient



class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
    

s = Stack()
s.push(5)
print(s.peek())