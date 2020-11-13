import math
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        # dimenson row, c1, c2, where row, c1 is robot 1, and row, c2 is robot 2
        self.soln = [[[-math.inf for _ in range(num_cols)] for _ in range(num_cols)] for _ in range(num_rows)]
        self.soln[0][0][num_cols - 1] = grid[0][0] + grid[0][num_cols - 1]
        for row in range(1, num_rows):
            for c1 in range(num_cols):
                for c2 in range(num_cols):
                    if c1 == c2:
                        to_add = grid[row][c1]
                    else:
                        to_add = grid[row][c1] + grid[row][c2]

                    self.soln[row][c1][c2] = max(    
                        self.soln_helper(row-1,c1 - 1,c2 - 1),
                        self.soln_helper(row-1,c1 - 1,c2),
                        self.soln_helper(row-1,c1 - 1,c2 + 1),
                        self.soln_helper(row-1,c1,c2 - 1),
                        self.soln_helper(row-1,c1,c2),
                        self.soln_helper(row-1,c1,c2 + 1),
                        self.soln_helper(row-1,c1 + 1,c2 - 1),
                        self.soln_helper(row-1,c1 + 1,c2),
                        self.soln_helper(row-1,c1 + 1,c2 + 1)
                    ) + to_add
        return max(i for row in self.soln[num_rows-1] for i in row)
    
    def soln_helper(self, r, c1, c2):
        if r < 0 or c1 < 0 or c2 < 0:
            return -math.inf
        try:
            to_return = self.soln[r][c1][c2]
        except IndexError:
            to_return = -math.inf
        return to_return


    def __call__(self, n):
        return self.cherryPickup(n)
