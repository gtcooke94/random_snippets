import math
from typing import List

class Solution:
    def checkValidString(self, s: str) -> bool:
        opened, closed, either_stars, closed_stars, open_stars = 0, 0, 0, 0, 0

        for c in s:
            if c == "(":
                opened += 1
            elif c == ")":
                closed += 1
                # Try to close. If  you can't, it's wrong
                if opened > 0:
                    opened -= 1
                    closed -= 1
                elif open_stars > 0:
                    open_stars -= 1
                    closed -= 1
                elif either_stars > 0:
                    either_stars -= 1
                    closed -= 1
                else:
                    return False
            elif c == "*":
                if opened > 0:
                    either_stars += 1
                else:
                    open_stars += 1
            if either_stars > opened:
                # if at any point we have more "either" stars than open parens,  the excess must become open only (because at that point, you could use at max a number of stars as close equal to opened
                open_stars += either_stars - opened
                either_stars = opened
            # This is a special case of the  above if statement
            #  if opened == 0:
            #      # If we have no more  opens, these stars can no longer be used as closes
            #      open_stars += either_stars
            #      either_stars = 0
        if opened > either_stars:
            return False
        return True

        #  import pdb; pdb.set_trace()
        #  for c in s:
        #      if c == "(":
        #          opened += 1
        #      elif c == ")":
        #          closed += 1
        #      elif c == "*":
        #          if opened > 0:
        #              either_stars += 1
        #          else:
        #              closed_stars += 1
        #      if closed > opened + either_stars + closed_stars:
        #          return False
        #      elif closed > opened:
        #          if closed - opened > closed_stars:
        #              closed_stars = 0
        #              either_stars -= closed - opened - closed_stars
        #          else:
        #              closed_stars -= closed - opened
        #          opened = closed
        #  if closed > opened + closed_stars + either_stars:
        #      return False
        #  if opened > closed + either_stars:
        #      return False
        #  return True

    def __call__(self, n):
        return self.checkValidString(n)
