import math
from typing import List
from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack = deque()
        removed_counter = 0
        for digit in num:
            #  import pdb; pdb.set_trace()
            digit = int(digit)
            while stack and stack[-1] > digit and k:
                stack.pop()
                k -=1
            stack.append(digit)
        while k:
            stack.pop()
            k -= 1
        while stack and stack[0] == 0:
            stack.popleft()
        if not stack:
            return "0"
        return "".join(str(i) for i in stack)
                    

    def __call__(self, num, k):
        return self.removeKdigits(num, k)

# DP solution, there is a greedy linear solution
#  class Solution:
#      def removeKdigits(self, num: str, k: int) -> str:
#          dpgrid = {}
#          dpgrid[(0, 0)] = num[0]
#          for n, digit in enumerate(num):
#              for kk in range(k + 1):
#                  if kk > n:
#                      dpgrid[(n, kk)] = "0"
#                      continue
#                  if kk == 0:
#                      dpgrid[(n, kk)] = num[:n + 1]
#                      continue
#                  append_new_digit = int(dpgrid[(n - 1, kk)] + digit)
#                  remove_new_digit = int(dpgrid[(n - 1, kk - 1)])
#                  dpgrid[(n, kk)] = str(min(remove_new_digit, append_new_digit))
#          return dpgrid[(len(num) - 1), k]
#
#
#      def __call__(self, num, k):
#          return self.removeKdigits(num, k)
