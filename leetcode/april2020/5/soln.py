import math
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n) solution with minimal ops
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1



    def __call__(self, n):
        return self.moveZeroes(n)

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  Sorting is O(nlogn), we can do this in O(n) above. But below looks nicer
        #  Python sort is stable. Provide a key that makes 0 a higher value and everything else the same
        #  Clean
        nums.sort(key=lambda x: not x)
        #  Clear
        #  nums.sort(key=lambda x: math.inf if x == 0 else 1)



    def __call__(self, n):
        return self.moveZeroes(n)
