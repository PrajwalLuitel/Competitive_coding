"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. 
This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)


Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']


This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread 
is consuming the food orders.
"""

from threading import Thread
from collections import deque
import time


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



q = Queue()



def place_order(orders_buffer):
    global q
    for food in orders_buffer:
        q.enqueue(food)
        print(f"Order placed for {food}")
        time.sleep(0.5)

def serve_order():
    global q
    while q.size() != 0:
        served_food = q.dequeue()
        print(f"Order served for {served_food}")
        time.sleep(2)

if __name__ == "__main__":
    t1 = Thread(target=place_order, args=[['pizza','samosa','pasta','biryani','burger']])
    t2 = Thread(target=serve_order)

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()
    print("All foods ordered and served !!!!")