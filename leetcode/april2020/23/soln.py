from typing import List
from math import log

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            lowpow2 = 0
        else:
            lowpow2 = int(log(m, 2))
        if n == 0:
            highpow2 = 0
        else:
            highpow2 = int(log(n, 2))
        
        # if highpow2 > lowpow2, only care about n and up, because the 2^highpow2 <= n will put 0's on everything lower than it
        if lowpow2 == highpow2:
            res = m
            for num in range(m + 1, n + 1):
                res &= num
            return res
        else:
            res = 2 ** highpow2
            for num in range(res + 1, n + 1):
                res &= num
            return res

    def __call__(self, m, n):
        return self.rangeBitwiseAnd(m, n)
