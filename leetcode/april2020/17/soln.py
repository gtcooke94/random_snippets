from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0
        self.visited = set()
        self.grid = grid
        if len(self.grid) == 0:
            return 0
        if len(self.grid[0]) == 0:
            return 0

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.visited:
                    continue
                if self.grid[i][j] == "1":
                    self.BFS_island(begin=(i, j))
                    self.islands += 1
                self.visited.add((i, j))
        return self.islands

    def BFS_island(self, begin=None):
        queue = deque()
        queue.append(begin)
        while queue:
            i, j = queue.popleft()
            if (i, j) in self.visited:
                continue
            self.visited.add((i, j))
            if self.grid[i][j] == "0":
                continue
            potentials = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for i, j in potentials:
                if i < 0 or i >= self.height or j < 0 or j >= self.width:
                    continue
                queue.append((i, j))

    def __call__(self, n):
        return self.numIslands(n)
