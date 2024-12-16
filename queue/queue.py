from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

if __name__ == "__main__":
    q = Queue()
    q.enqueue(32)
    q.enqueue(44)
    q.enqueue(58)
    print(q.buffer)
    q.dequeue()
    print(q.buffer)
