import math
from collections import deque

class MinStack():

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deque = deque()
        
    def push(self, x: int) -> None:
        if self.deque:
            self.deque.append((x, x if x < self.deque[-1][1] else self.deque[-1][1]))
        else:
            self.deque.append((x, x))

    def pop(self) -> None:
        self.deque.pop()
        
    def top(self) -> int:
        return self.deque[-1][0]
        
    def getMin(self) -> int:
        return self.deque[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
