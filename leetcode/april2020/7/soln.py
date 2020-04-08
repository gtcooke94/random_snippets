import math
from typing import List
from collections import Counter


class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = Counter(arr)
        total = 0
        for val in counts:
            if val + 1 in counts:
                total += counts[val]
        return total

    def __call__(self, n):
        return self.countElements(n)
"""
I thought it was right, thinking we had to pair duplicates s.t.
[1, 1, 2, 2] -> 2
[1, 1, 2] -> 1

But that is not the case, we just case if the i+1 element exists, it's even easier
[1, 1, 2] -> 2


class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = Counter(arr)
        total = 0
        for val in counts:
            total += min(counts[val], counts[val + 1])
        return total

    def __call__(self, n):
        return self.countElements(n)
"""
