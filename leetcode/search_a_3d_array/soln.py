import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row_idx = bisect.bisect_right([row[0] for row in matrix], target) - 1
        if row_idx < 0:
            return False
        if target > matrix[row_idx][-1]:
            return False
        col_idx = bisect.bisect_left(matrix[row_idx], target)
        if col_idx != len(matrix[row_idx]) and matrix[row_idx][col_idx] == target:
            return True
        return False
