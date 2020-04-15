import math
from typing import List
"""
O(1) space and O(n) time solution.

Would be much easier to do with queues/stacks, but this successfully gets through without writing extra strings, keeping a queue, etc
Only extra thing to store is two counters, which is O(1)
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # keep counter of how many #
        # If 0, compare elements
        S_del_counter = 0
        T_del_counter = 0
        indS = len(S) - 1
        indT = len(T) - 1
        exhaustedS = False
        exhaustedT = False
        while True:
            while (S_del_counter != 0 and indS >= 0) or S[indS] == "#":
                if S[indS] == "#":
                    S_del_counter += 1
                else:
                    S_del_counter -= 1
                indS -= 1
            
            if indS < 0:
                exhaustedS = True

            while (T_del_counter != 0 and indT >= 0) or T[indT] == "#":
                if T[indT] == "#":
                    T_del_counter += 1
                else:
                    T_del_counter -= 1
                indT -= 1

            if indT < 0:
                exhaustedT = True

            if exhaustedS and exhaustedT:
                return True

            if exhaustedS ^ exhaustedT:
                return False

            if S[indS] != T[indT]:
                return False

            indS -= 1
            indT -= 1


    def __call__(self, str1, str2):
        return self.backspaceCompare(str1, str2)
