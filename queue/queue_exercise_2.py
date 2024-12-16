"""
Write a program to print binary numbers from 1 to 10 using Queue. 

Binary sequence should look like,

    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010

Hint: Notice a pattern above. 
After 1 second and third number is 1+0 and 1+1. 
4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.
"""

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[0]

    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

def produce_binary_numbers(n):
    q = Queue()
    q.enqueue("1")
    print(q.front())
    for i in range(n-1):
        if i%2 ==0:
            front_element = q.dequeue()
            new_element = front_element+"0"
            print(new_element)
            q.enqueue(new_element)
        else:
            new_element = front_element+"1"
            print(new_element)
            q.enqueue(new_element)
    


if __name__=="__main__":
    produce_binary_numbers(10)