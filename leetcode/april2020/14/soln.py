import math
from typing import List
from itertools import cycle

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        lens = len(s)
        for item in shift:
            direction, amount = item[0], item[1]
            s_cycle = cycle(s)
            if direction:
                self.exhaust(next(s_cycle) for _ in range(-amount % lens))
            else:
                self.exhaust(next(s_cycle) for _ in range(amount))
            s = "".join(next(s_cycle) for _ in range(lens))
            print(s)
        return s

    def exhaust(self, gen):
        for _ in gen:
            pass

        

                

    def __call__(self, inp1, inp2):
        return self.stringShift(inp1, inp2)




