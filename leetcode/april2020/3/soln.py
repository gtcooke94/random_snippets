import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, maxj, maxsum = 0, 0, -math.inf
        cur_sum = -math.inf
        for n in nums:
            cur_sum = max(n, cur_sum + n)
            maxsum = max(maxsum, cur_sum)
        return maxsum


    def __call__(self, n):
        return self.maxSubArray(n)
