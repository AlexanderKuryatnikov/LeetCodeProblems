from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_increase = 0

        increase_grid = []
        for _ in range(n):
            increase_grid.append([0] * m)

        for i in range(n):
            row_max = max(grid[i])
            for j in range(m):
                increase_grid[i][j] = row_max - grid[i][j]

        for j in range(m):
            col_max = max([grid[i][j] for i in range(n)])
            for i in range(n):
                max_increase += min(
                    increase_grid[i][j],
                    col_max - grid[i][j]
                )

        return max_increase
