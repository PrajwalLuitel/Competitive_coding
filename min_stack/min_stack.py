"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack:

    def __init__(self):
        self.minstack:list[int] = []

    def push(self, val: int) -> None:
        self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop(-1)
        
    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        min:int = 10**99
        for el in self.minstack:
            if el < min:
                min = el
        return min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.minstack)
obj.push(32)
print(obj.minstack)
obj.push(48)
print(obj.minstack)
obj.push(72)
print(obj.minstack)
obj.pop()
print(obj.minstack)
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)

